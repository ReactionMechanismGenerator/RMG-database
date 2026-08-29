#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(48738.1,'m^3/(mol*s)'), n=0.590978, w0=(295753,'J/mol'), E0=(56497.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1038751644594564, var=6.664463309693581, Tref=1000.0, N=296, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 296 training reactions at node Root
    Total Standard Deviation in ln(k): 5.436341140201111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 296 training reactions at node Root
Total Standard Deviation in ln(k): 5.436341140201111""",
    longDesc = 
"""
BM rule fitted to 296 training reactions at node Root
Total Standard Deviation in ln(k): 5.436341140201111
""",
)

entry(
    index = 2,
    label = "Root_4R->H",
    kinetics = ArrheniusBM(A=(26.9633,'m^3/(mol*s)'), n=1.72951, w0=(312854,'J/mol'), E0=(37766.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002411810976433415, var=1.9890434076482735, Tref=1000.0, N=99, data_mean=0.0, correlation='Root_4R->H',), comment="""BM rule fitted to 99 training reactions at node Root_4R->H
    Total Standard Deviation in ln(k): 2.833406873675473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 99 training reactions at node Root_4R->H
Total Standard Deviation in ln(k): 2.833406873675473""",
    longDesc = 
"""
BM rule fitted to 99 training reactions at node Root_4R->H
Total Standard Deviation in ln(k): 2.833406873675473
""",
)

entry(
    index = 3,
    label = "Root_N-4R->H",
    kinetics = ArrheniusBM(A=(0.0116191,'m^3/(mol*s)'), n=2.47195, w0=(287160,'J/mol'), E0=(46261.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01656090400500132, var=5.436327955620116, Tref=1000.0, N=197, data_mean=0.0, correlation='Root_N-4R->H',), comment="""BM rule fitted to 197 training reactions at node Root_N-4R->H
    Total Standard Deviation in ln(k): 4.715837461014406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 197 training reactions at node Root_N-4R->H
Total Standard Deviation in ln(k): 4.715837461014406""",
    longDesc = 
"""
BM rule fitted to 197 training reactions at node Root_N-4R->H
Total Standard Deviation in ln(k): 4.715837461014406
""",
)

entry(
    index = 4,
    label = "Root_4R->H_2R->C",
    kinetics = ArrheniusBM(A=(0.108436,'m^3/(mol*s)'), n=2.40439, w0=(317500,'J/mol'), E0=(30418,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.043595946099428816, var=1.4268792077532064, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_4R->H_2R->C',), comment="""BM rule fitted to 79 training reactions at node Root_4R->H_2R->C
    Total Standard Deviation in ln(k): 2.5042346856245015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_4R->H_2R->C
Total Standard Deviation in ln(k): 2.5042346856245015""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_4R->H_2R->C
Total Standard Deviation in ln(k): 2.5042346856245015
""",
)

entry(
    index = 5,
    label = "Root_4R->H_N-2R->C",
    kinetics = ArrheniusBM(A=(194.194,'m^3/(mol*s)'), n=1.6509, w0=(294500,'J/mol'), E0=(42385.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024089876175387378, var=3.007504314290568, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_4R->H_N-2R->C',), comment="""BM rule fitted to 20 training reactions at node Root_4R->H_N-2R->C
    Total Standard Deviation in ln(k): 3.5371704998851348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_4R->H_N-2R->C
Total Standard Deviation in ln(k): 3.5371704998851348""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_4R->H_N-2R->C
Total Standard Deviation in ln(k): 3.5371704998851348
""",
)

entry(
    index = 6,
    label = "Root_N-4R->H_2R->H",
    kinetics = ArrheniusBM(A=(14.9181,'m^3/(mol*s)'), n=1.5316, w0=(312854,'J/mol'), E0=(54112.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06927127821209753, var=4.363639386564023, Tref=1000.0, N=99, data_mean=0.0, correlation='Root_N-4R->H_2R->H',), comment="""BM rule fitted to 99 training reactions at node Root_N-4R->H_2R->H
    Total Standard Deviation in ln(k): 4.361804885280358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 99 training reactions at node Root_N-4R->H_2R->H
Total Standard Deviation in ln(k): 4.361804885280358""",
    longDesc = 
"""
BM rule fitted to 99 training reactions at node Root_N-4R->H_2R->H
Total Standard Deviation in ln(k): 4.361804885280358
""",
)

entry(
    index = 7,
    label = "Root_N-4R->H_N-2R->H",
    kinetics = ArrheniusBM(A=(4.128e-08,'m^3/(mol*s)'), n=4.1008, w0=(261204,'J/mol'), E0=(33898.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07890765960825927, var=6.7207769687928245, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H',), comment="""BM rule fitted to 98 training reactions at node Root_N-4R->H_N-2R->H
    Total Standard Deviation in ln(k): 5.395428156653948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-4R->H_N-2R->H
Total Standard Deviation in ln(k): 5.395428156653948""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-4R->H_N-2R->H
Total Standard Deviation in ln(k): 5.395428156653948
""",
)

entry(
    index = 8,
    label = "Root_4R->H_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.0299609,'m^3/(mol*s)'), n=2.59467, w0=(317500,'J/mol'), E0=(26142.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05829467309663924, var=1.996889335167154, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R',), comment="""BM rule fitted to 47 training reactions at node Root_4R->H_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.9793869255685683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_4R->H_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.9793869255685683""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_4R->H_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.9793869255685683
""",
)

entry(
    index = 9,
    label = "Root_4R->H_2R->C_3R->H",
    kinetics = ArrheniusBM(A=(242.676,'m^3/(mol*s)'), n=1.52291, w0=(317500,'J/mol'), E0=(42475.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.123611835132447e-14, var=0.041466420084076354, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_3R->H
    Total Standard Deviation in ln(k): 0.40823032333065695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_3R->H
Total Standard Deviation in ln(k): 0.40823032333065695""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_3R->H
Total Standard Deviation in ln(k): 0.40823032333065695
""",
)

entry(
    index = 10,
    label = "Root_4R->H_2R->C_N-3R->H",
    kinetics = ArrheniusBM(A=(9.08807e-07,'m^3/(mol*s)'), n=3.8986, w0=(317500,'J/mol'), E0=(15960.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10728838849803903, var=0.40901000086542755, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H',), comment="""BM rule fitted to 30 training reactions at node Root_4R->H_2R->C_N-3R->H
    Total Standard Deviation in ln(k): 1.551674875635759"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_4R->H_2R->C_N-3R->H
Total Standard Deviation in ln(k): 1.551674875635759""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_4R->H_2R->C_N-3R->H
Total Standard Deviation in ln(k): 1.551674875635759
""",
)

entry(
    index = 11,
    label = "Root_4R->H_N-2R->C_3R->H",
    kinetics = ArrheniusBM(A=(40.1393,'m^3/(mol*s)'), n=1.95377, w0=(294500,'J/mol'), E0=(31207,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10102651464978389, var=1.5125135274524155, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_N-2R->C_3R->H',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_N-2R->C_3R->H
    Total Standard Deviation in ln(k): 2.7193446398063337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_N-2R->C_3R->H
Total Standard Deviation in ln(k): 2.7193446398063337""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_N-2R->C_3R->H
Total Standard Deviation in ln(k): 2.7193446398063337
""",
)

entry(
    index = 12,
    label = "Root_4R->H_N-2R->C_N-3R->H",
    kinetics = ArrheniusBM(A=(0.00881436,'m^3/(mol*s)'), n=2.91909, w0=(294500,'J/mol'), E0=(29258.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0003649909962652854, var=3.4396276954837828, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H',), comment="""BM rule fitted to 14 training reactions at node Root_4R->H_N-2R->C_N-3R->H
    Total Standard Deviation in ln(k): 3.7189455074327626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->H_N-2R->C_N-3R->H
Total Standard Deviation in ln(k): 3.7189455074327626""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->H_N-2R->C_N-3R->H
Total Standard Deviation in ln(k): 3.7189455074327626
""",
)

entry(
    index = 13,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00134817,'m^3/(mol*s)'), n=2.77539, w0=(312822,'J/mol'), E0=(46261,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009639399187656212, var=5.470376824934864, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 59 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.713061732488851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 59 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.713061732488851""",
    longDesc = 
"""
BM rule fitted to 59 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.713061732488851
""",
)

entry(
    index = 14,
    label = "Root_N-4R->H_2R->H_3R->S",
    kinetics = ArrheniusBM(A=(6.16662e+09,'m^3/(mol*s)'), n=-0.882728, w0=(308300,'J/mol'), E0=(73468.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20184127208593916, var=4.506218237689724, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->H_2R->H_3R->S
    Total Standard Deviation in ln(k): 4.76276140871011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->H_2R->H_3R->S
Total Standard Deviation in ln(k): 4.76276140871011""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->H_2R->H_3R->S
Total Standard Deviation in ln(k): 4.76276140871011
""",
)

entry(
    index = 15,
    label = "Root_N-4R->H_2R->H_N-3R->S",
    kinetics = ArrheniusBM(A=(9.28287e+09,'m^3/(mol*s)'), n=-1.19691, w0=(314433,'J/mol'), E0=(68926.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21541406916306371, var=2.2833542506663096, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S',), comment="""BM rule fitted to 30 training reactions at node Root_N-4R->H_2R->H_N-3R->S
    Total Standard Deviation in ln(k): 3.5705508116797966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-4R->H_2R->H_N-3R->S
Total Standard Deviation in ln(k): 3.5705508116797966""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-4R->H_2R->H_N-3R->S
Total Standard Deviation in ln(k): 3.5705508116797966
""",
)

entry(
    index = 16,
    label = "Root_N-4R->H_N-2R->H_2CS->S",
    kinetics = ArrheniusBM(A=(5.65815e-08,'m^3/(mol*s)'), n=4.04541, w0=(249000,'J/mol'), E0=(21003.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07204676785946203, var=1.8370961444214888, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S',), comment="""BM rule fitted to 23 training reactions at node Root_N-4R->H_N-2R->H_2CS->S
    Total Standard Deviation in ln(k): 2.8982303281874677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-4R->H_N-2R->H_2CS->S
Total Standard Deviation in ln(k): 2.8982303281874677""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-4R->H_N-2R->H_2CS->S
Total Standard Deviation in ln(k): 2.8982303281874677
""",
)

entry(
    index = 17,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S",
    kinetics = ArrheniusBM(A=(5.51119e-08,'m^3/(mol*s)'), n=4.07006, w0=(264947,'J/mol'), E0=(37781.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08495598871304003, var=7.954237995004958, Tref=1000.0, N=75, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S',), comment="""BM rule fitted to 75 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S
    Total Standard Deviation in ln(k): 5.867463452951612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 75 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S
Total Standard Deviation in ln(k): 5.867463452951612""",
    longDesc = 
"""
BM rule fitted to 75 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S
Total Standard Deviation in ln(k): 5.867463452951612
""",
)

entry(
    index = 18,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(8.18793e+08,'m^3/(mol*s)'), n=-0.580824, w0=(317500,'J/mol'), E0=(44566.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10002960113761468, var=0.8521223116493635, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 9 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C
    Total Standard Deviation in ln(k): 2.101911054911934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 2.101911054911934""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 2.101911054911934
""",
)

entry(
    index = 19,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(0.00383635,'m^3/(mol*s)'), n=2.88256, w0=(317500,'J/mol'), E0=(21327.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09451059779875554, var=2.3581635390672804, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 38 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C
    Total Standard Deviation in ln(k): 3.315997778947692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 3.315997778947692""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 3.315997778947692
""",
)

entry(
    index = 20,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(5.49487e-07,'m^3/(mol*s)'), n=3.96567, w0=(317500,'J/mol'), E0=(15081.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12101317515783797, var=0.4294957355443869, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R',), comment="""BM rule fitted to 26 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R
    Total Standard Deviation in ln(k): 1.6178748638347114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R
Total Standard Deviation in ln(k): 1.6178748638347114""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R
Total Standard Deviation in ln(k): 1.6178748638347114
""",
)

entry(
    index = 21,
    label = "Root_4R->H_2R->C_N-3R->H_3CS->S",
    kinetics = ArrheniusBM(A=(35.3139,'m^3/(mol*s)'), n=1.70617, w0=(317500,'J/mol'), E0=(43507.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.3609503636116697e-15, var=0.0014227530166913047, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_3CS->S
    Total Standard Deviation in ln(k): 0.07561740109815406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 0.07561740109815406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 0.07561740109815406
""",
)

entry(
    index = 22,
    label = "Root_4R->H_2R->C_N-3R->H_N-3CS->S",
    kinetics = ArrheniusBM(A=(35.6098,'m^3/(mol*s)'), n=1.63727, w0=(317500,'J/mol'), E0=(34127.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360837e-15, var=0.44664157146758726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_N-3CS->S
    Total Standard Deviation in ln(k): 1.3397894721319432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 1.3397894721319432""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 1.3397894721319432
""",
)

entry(
    index = 23,
    label = "Root_4R->H_N-2R->C_3R->H_Ext-2HS-R",
    kinetics = ArrheniusBM(A=(36.8492,'m^3/(mol*s)'), n=1.98454, w0=(294500,'J/mol'), E0=(23930,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10979768079775974, var=2.445947229286707, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_N-2R->C_3R->H_Ext-2HS-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R
    Total Standard Deviation in ln(k): 3.411183882293935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R
Total Standard Deviation in ln(k): 3.411183882293935""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R
Total Standard Deviation in ln(k): 3.411183882293935
""",
)

entry(
    index = 24,
    label = "Root_4R->H_N-2R->C_N-3R->H_3CS->S",
    kinetics = ArrheniusBM(A=(0.0151627,'m^3/(mol*s)'), n=2.81626, w0=(294500,'J/mol'), E0=(32745.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06936215507971392, var=3.9840007477348753, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_3CS->S',), comment="""BM rule fitted to 8 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S
    Total Standard Deviation in ln(k): 4.175720326521691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 4.175720326521691""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 4.175720326521691
""",
)

entry(
    index = 25,
    label = "Root_4R->H_N-2R->C_N-3R->H_N-3CS->S",
    kinetics = ArrheniusBM(A=(0.0219541,'m^3/(mol*s)'), n=2.84703, w0=(294500,'J/mol'), E0=(2866.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7837775163681058, var=8.200273007022998, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_N-3CS->S',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S
    Total Standard Deviation in ln(k): 7.710073428720813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 7.710073428720813""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 7.710073428720813
""",
)

entry(
    index = 26,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(536.391,'m^3/(mol*s)'), n=1.02484, w0=(317500,'J/mol'), E0=(69297.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08618323198392233, var=3.4669765672291084, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.949321196832809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.949321196832809""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.949321196832809
""",
)

entry(
    index = 27,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S",
    kinetics = ArrheniusBM(A=(2.76638e-09,'m^3/(mol*s)'), n=4.97355, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11085167605216564, var=10.089975035602704, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S
    Total Standard Deviation in ln(k): 6.646506850938779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S
Total Standard Deviation in ln(k): 6.646506850938779""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S
Total Standard Deviation in ln(k): 6.646506850938779
""",
)

entry(
    index = 28,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(2.37412e+09,'m^3/(mol*s)'), n=-0.868325, w0=(311565,'J/mol'), E0=(67624.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2048595364781261, var=4.764401524250889, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S
    Total Standard Deviation in ln(k): 4.890559762968766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S
Total Standard Deviation in ln(k): 4.890559762968766""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S
Total Standard Deviation in ln(k): 4.890559762968766
""",
)

entry(
    index = 29,
    label = "Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.000300006,'m^3/(mol*s)'), n=3.36681, w0=(294500,'J/mol'), E0=(48582.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08584591969357706, var=9.590731934837482, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 6.4241386591090395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 6.4241386591090395""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 6.4241386591090395
""",
)

entry(
    index = 30,
    label = "Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(4.08727e-06,'m^3/(mol*s)'), n=3.41675, w0=(317500,'J/mol'), E0=(37050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02487531931331927, var=0.568282844378074, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 1.573761061799268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 1.573761061799268""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 1.573761061799268
""",
)

entry(
    index = 31,
    label = "Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(5630.42,'m^3/(mol*s)'), n=1.11829, w0=(294500,'J/mol'), E0=(59498.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09368993351446467, var=1.3472725558014564, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 2.562339356050877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 2.562339356050877""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 2.562339356050877
""",
)

entry(
    index = 32,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.00130987,'m^3/(mol*s)'), n=2.54116, w0=(317500,'J/mol'), E0=(39987.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014934171564478032, var=1.0659140424520515, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 26 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 2.107273949571474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 2.107273949571474""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 2.107273949571474
""",
)

entry(
    index = 33,
    label = "Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0815562,'m^3/(mol*s)'), n=2.27149, w0=(249000,'J/mol'), E0=(32688.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1705282198556788, var=4.6101971024765565, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 7.245466447196838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 7.245466447196838""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 7.245466447196838
""",
)

entry(
    index = 34,
    label = "Root_N-4R->H_N-2R->H_2CS->S_3R->S",
    kinetics = ArrheniusBM(A=(1.73711e-05,'m^3/(mol*s)'), n=3.24553, w0=(249000,'J/mol'), E0=(27398.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01749335764171125, var=0.7521194320955391, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_3R->S',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S
    Total Standard Deviation in ln(k): 1.7825560376486598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S
Total Standard Deviation in ln(k): 1.7825560376486598""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S
Total Standard Deviation in ln(k): 1.7825560376486598
""",
)

entry(
    index = 35,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S",
    kinetics = ArrheniusBM(A=(4.10871e-09,'m^3/(mol*s)'), n=4.41877, w0=(249000,'J/mol'), E0=(16074.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10128137996841306, var=2.5903944607723504, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S
    Total Standard Deviation in ln(k): 3.4810372797793363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S
Total Standard Deviation in ln(k): 3.4810372797793363""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S
Total Standard Deviation in ln(k): 3.4810372797793363
""",
)

entry(
    index = 36,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.218872,'m^3/(mol*s)'), n=2.1494, w0=(264132,'J/mol'), E0=(54456.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.026538020750966514, var=8.108917069208998, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 38 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.775394191632173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.775394191632173""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.775394191632173
""",
)

entry(
    index = 37,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H",
    kinetics = ArrheniusBM(A=(4.25207e-17,'m^3/(mol*s)'), n=6.67291, w0=(269032,'J/mol'), E0=(15471.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21478276008852448, var=6.3410155465969, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H
    Total Standard Deviation in ln(k): 5.587853384919751"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H
Total Standard Deviation in ln(k): 5.587853384919751""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H
Total Standard Deviation in ln(k): 5.587853384919751
""",
)

entry(
    index = 38,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H",
    kinetics = ArrheniusBM(A=(0.000510051,'m^3/(mol*s)'), n=3.17499, w0=(249000,'J/mol'), E0=(31024.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023706456142312506, var=1.0398599575247929, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H
    Total Standard Deviation in ln(k): 2.103862963303436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H
Total Standard Deviation in ln(k): 2.103862963303436""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H
Total Standard Deviation in ln(k): 2.103862963303436
""",
)

entry(
    index = 39,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C",
    kinetics = ArrheniusBM(A=(27027.1,'m^3/(mol*s)'), n=0.716328, w0=(317500,'J/mol'), E0=(34697.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.056154515112976686, var=0.618264774874968, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
    Total Standard Deviation in ln(k): 1.7174112216928048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
Total Standard Deviation in ln(k): 1.7174112216928048""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
Total Standard Deviation in ln(k): 1.7174112216928048
""",
)

entry(
    index = 40,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1260,'m^3/(mol*s)'), n=1.46, w0=(317500,'J/mol'), E0=(40936.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(12.7,'m^3/(mol*s)'), n=2.26, w0=(317500,'J/mol'), E0=(43793.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O",
    kinetics = ArrheniusBM(A=(3910,'m^3/(mol*s)'), n=1.32, w0=(317500,'J/mol'), E0=(43191.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.0417064,'m^3/(mol*s)'), n=2.53895, w0=(317500,'J/mol'), E0=(29507.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.061737766922007185, var=2.2091021443570296, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O',), comment="""BM rule fitted to 36 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.1347675109916264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1347675109916264""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1347675109916264
""",
)

entry(
    index = 44,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(0.115706,'m^3/(mol*s)'), n=2.31759, w0=(317500,'J/mol'), E0=(32311,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.042127389448435304, var=0.39057371053304885, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R',), comment="""BM rule fitted to 14 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R
    Total Standard Deviation in ln(k): 1.3587248754182346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R
Total Standard Deviation in ln(k): 1.3587248754182346""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R
Total Standard Deviation in ln(k): 1.3587248754182346
""",
)

entry(
    index = 45,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(77.1598,'m^3/(mol*s)'), n=1.52405, w0=(317500,'J/mol'), E0=(34372.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004680369447601296, var=0.13394309389745518, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.745457413644234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.745457413644234""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.745457413644234
""",
)

entry(
    index = 46,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->S",
    kinetics = ArrheniusBM(A=(48.9339,'m^3/(mol*s)'), n=1.70373, w0=(317500,'J/mol'), E0=(38807,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.272150233908559e-15, var=1.887543441990775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->S
    Total Standard Deviation in ln(k): 2.7542633762270654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->S
Total Standard Deviation in ln(k): 2.7542633762270654""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->S
Total Standard Deviation in ln(k): 2.7542633762270654
""",
)

entry(
    index = 47,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(458.224,'m^3/(mol*s)'), n=1.28791, w0=(317500,'J/mol'), E0=(39639.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020592637178593547, var=0.5000297646200432, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S
    Total Standard Deviation in ln(k): 1.4693442546859972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S
Total Standard Deviation in ln(k): 1.4693442546859972""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S
Total Standard Deviation in ln(k): 1.4693442546859972
""",
)

entry(
    index = 48,
    label = "Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C",
    kinetics = ArrheniusBM(A=(25.3782,'m^3/(mol*s)'), n=2.06603, w0=(294500,'J/mol'), E0=(29072.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2117664745776033, var=0.5366865189802603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C
    Total Standard Deviation in ln(k): 2.000723265321178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C
Total Standard Deviation in ln(k): 2.000723265321178""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C
Total Standard Deviation in ln(k): 2.000723265321178
""",
)

entry(
    index = 49,
    label = "Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(98.6075,'m^3/(mol*s)'), n=1.81709, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2955000438353378, var=9.638257054424626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.96627121447344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.96627121447344""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.96627121447344
""",
)

entry(
    index = 50,
    label = "Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R",
    kinetics = ArrheniusBM(A=(1.01408,'m^3/(mol*s)'), n=2.25445, w0=(294500,'J/mol'), E0=(32601.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012001138556957634, var=2.3948720119052163, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R
    Total Standard Deviation in ln(k): 3.1325561286861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R
Total Standard Deviation in ln(k): 3.1325561286861""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R
Total Standard Deviation in ln(k): 3.1325561286861
""",
)

entry(
    index = 51,
    label = "Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(119.362,'m^3/(mol*s)'), n=1.72429, w0=(294500,'J/mol'), E0=(47971.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.6866075604722907e-14, var=27.73239685281507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R
    Total Standard Deviation in ln(k): 10.557247244422026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R
Total Standard Deviation in ln(k): 10.557247244422026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R
Total Standard Deviation in ln(k): 10.557247244422026
""",
)

entry(
    index = 52,
    label = "Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R",
    kinetics = ArrheniusBM(A=(0.148213,'m^3/(mol*s)'), n=2.57622, w0=(294500,'J/mol'), E0=(-10045.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.050481104888601254, var=4.8290219161416355, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R
    Total Standard Deviation in ln(k): 4.532249425477151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R
Total Standard Deviation in ln(k): 4.532249425477151""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R
Total Standard Deviation in ln(k): 4.532249425477151
""",
)

entry(
    index = 53,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1421.37,'m^3/(mol*s)'), n=0.846074, w0=(317500,'J/mol'), E0=(71419.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09229402024172977, var=4.029796288488547, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.256270387262151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.256270387262151""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.256270387262151
""",
)

entry(
    index = 54,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(457.97,'m^3/(mol*s)'), n=1.24222, w0=(317500,'J/mol'), E0=(65889.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05897354011004171, var=2.5414392734512394, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 3.344101775927699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.344101775927699""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.344101775927699
""",
)

entry(
    index = 55,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.247929,'m^3/(mol*s)'), n=2.02965, w0=(317500,'J/mol'), E0=(59692.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04502790366011018, var=0.5843231435586389, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.6455756265354256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.6455756265354256""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.6455756265354256
""",
)

entry(
    index = 56,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C",
    kinetics = ArrheniusBM(A=(3.57433e-12,'m^3/(mol*s)'), n=5.70933, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.501075173835103, var=10.216414683279746, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C
    Total Standard Deviation in ln(k): 10.179305790418463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C
Total Standard Deviation in ln(k): 10.179305790418463""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C
Total Standard Deviation in ln(k): 10.179305790418463
""",
)

entry(
    index = 57,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C",
    kinetics = ArrheniusBM(A=(2.14106e-06,'m^3/(mol*s)'), n=4.23777, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.311273691999663, var=9.638257054424729, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C
    Total Standard Deviation in ln(k): 12.031029124434088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C
Total Standard Deviation in ln(k): 12.031029124434088""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C
Total Standard Deviation in ln(k): 12.031029124434088
""",
)

entry(
    index = 58,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(8880.78,'m^3/(mol*s)'), n=0.582687, w0=(317500,'J/mol'), E0=(49410.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09639540025605056, var=2.411587868771733, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 3.355410343223453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 3.355410343223453""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 3.355410343223453
""",
)

entry(
    index = 59,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(4.93861e+09,'m^3/(mol*s)'), n=-0.904825, w0=(309136,'J/mol'), E0=(71139.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2073520920479286, var=6.057784270319831, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi
    Total Standard Deviation in ln(k): 5.455152685689254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 5.455152685689254""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi
Total Standard Deviation in ln(k): 5.455152685689254
""",
)

entry(
    index = 60,
    label = "Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.00133884,'m^3/(mol*s)'), n=3.20083, w0=(294500,'J/mol'), E0=(49507.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5015801590849759, var=20.76455684709073, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S_Ext-3S-R
    Total Standard Deviation in ln(k): 10.395457186494813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S_Ext-3S-R
Total Standard Deviation in ln(k): 10.395457186494813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_4BrCClFINOPSSi->S_Ext-3S-R
Total Standard Deviation in ln(k): 10.395457186494813
""",
)

entry(
    index = 61,
    label = "Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(2.68282e-07,'m^3/(mol*s)'), n=3.74352, w0=(317500,'J/mol'), E0=(32941.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04847581116853986, var=1.1580754049590416, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R
    Total Standard Deviation in ln(k): 2.279172361952245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R
Total Standard Deviation in ln(k): 2.279172361952245""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R
Total Standard Deviation in ln(k): 2.279172361952245
""",
)

entry(
    index = 62,
    label = "Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_3CH->C",
    kinetics = ArrheniusBM(A=(0.00122128,'m^3/(mol*s)'), n=3.07079, w0=(294500,'J/mol'), E0=(46194.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6523332123069664, var=1.3652848766208332, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_3CH->C
    Total Standard Deviation in ln(k): 3.981469000270202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_3CH->C
Total Standard Deviation in ln(k): 3.981469000270202""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_3CH->C
Total Standard Deviation in ln(k): 3.981469000270202
""",
)

entry(
    index = 63,
    label = "Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(0.00114109,'m^3/(mol*s)'), n=3.14721, w0=(294500,'J/mol'), E0=(35330.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8513968857368823, var=0.31374304267251746, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_N-3CH->C
    Total Standard Deviation in ln(k): 3.2620958073605477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_N-3CH->C
Total Standard Deviation in ln(k): 3.2620958073605477""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_4BrCClFINOPSSi->S_N-3CH->C
Total Standard Deviation in ln(k): 3.2620958073605477
""",
)

entry(
    index = 64,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(3.62446e-07,'m^3/(mol*s)'), n=3.56947, w0=(317500,'J/mol'), E0=(31942.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04026554689668887, var=0.6851733663372017, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R
    Total Standard Deviation in ln(k): 1.76059317692533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R
Total Standard Deviation in ln(k): 1.76059317692533""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R
Total Standard Deviation in ln(k): 1.76059317692533
""",
)

entry(
    index = 65,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_3CH->C",
    kinetics = ArrheniusBM(A=(0.000303339,'m^3/(mol*s)'), n=2.79083, w0=(317500,'J/mol'), E0=(34632.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.04146775158944e-16, var=0.4466415714676377, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_3CH->C
    Total Standard Deviation in ln(k): 1.3397894721320165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_3CH->C
Total Standard Deviation in ln(k): 1.3397894721320165""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_3CH->C
Total Standard Deviation in ln(k): 1.3397894721320165
""",
)

entry(
    index = 66,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(0.000276162,'m^3/(mol*s)'), n=3.02811, w0=(317500,'J/mol'), E0=(37940.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04146642008410201, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_N-3CH->C
    Total Standard Deviation in ln(k): 0.4082303233307048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_N-3CH->C
Total Standard Deviation in ln(k): 0.4082303233307048""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_N-3CH->C
Total Standard Deviation in ln(k): 0.4082303233307048
""",
)

entry(
    index = 67,
    label = "Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.00093,'m^3/(mol*s)'), n=2.61, w0=(249000,'J/mol'), E0=(30343.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-2S-R",
    kinetics = ArrheniusBM(A=(0.000985232,'m^3/(mol*s)'), n=2.86458, w0=(249000,'J/mol'), E0=(28498,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-2S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-2S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_Ext-4BrCClFINOPSSi-R_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.000321817,'m^3/(mol*s)'), n=2.90711, w0=(249000,'J/mol'), E0=(28539.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0020972647730856508, var=0.2667906122222293, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R
    Total Standard Deviation in ln(k): 1.0407508117630733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R
Total Standard Deviation in ln(k): 1.0407508117630733""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R
Total Standard Deviation in ln(k): 1.0407508117630733
""",
)

entry(
    index = 70,
    label = "Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(3.13216e-05,'m^3/(mol*s)'), n=3.13465, w0=(249000,'J/mol'), E0=(30851,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.0138225838631463e-16, var=0.7561257818316697, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-2S-R
    Total Standard Deviation in ln(k): 1.7432272762831922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-2S-R
Total Standard Deviation in ln(k): 1.7432272762831922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-2S-R
Total Standard Deviation in ln(k): 1.7432272762831922
""",
)

entry(
    index = 71,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C",
    kinetics = ArrheniusBM(A=(1.07972e-11,'m^3/(mol*s)'), n=5.19767, w0=(249000,'J/mol'), E0=(4171.24,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6195246395897674, var=9.521958450185915, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C
    Total Standard Deviation in ln(k): 7.742740070687853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C
Total Standard Deviation in ln(k): 7.742740070687853""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C
Total Standard Deviation in ln(k): 7.742740070687853
""",
)

entry(
    index = 72,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(2.59669e-05,'m^3/(mol*s)'), n=3.28114, w0=(249000,'J/mol'), E0=(25464.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.153254969678016, var=3.642686153416635, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C
    Total Standard Deviation in ln(k): 4.211264495452325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C
Total Standard Deviation in ln(k): 4.211264495452325""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C
Total Standard Deviation in ln(k): 4.211264495452325
""",
)

entry(
    index = 73,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.325655,'m^3/(mol*s)'), n=1.9742, w0=(272000,'J/mol'), E0=(65375.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03228217622293969, var=3.0127884002946286, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.5608070017646867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.5608070017646867""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.5608070017646867
""",
)

entry(
    index = 74,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S",
    kinetics = ArrheniusBM(A=(10.7573,'m^3/(mol*s)'), n=1.95659, w0=(249000,'J/mol'), E0=(59651.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06241823742413118, var=6.723437890527555, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S
    Total Standard Deviation in ln(k): 5.355026189415012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S
Total Standard Deviation in ln(k): 5.355026189415012""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S
Total Standard Deviation in ln(k): 5.355026189415012
""",
)

entry(
    index = 75,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(202.91,'m^3/(mol*s)'), n=1.28345, w0=(262591,'J/mol'), E0=(54689.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.095304420058149, var=8.51176074522108, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S
    Total Standard Deviation in ln(k): 6.088257296022055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S
Total Standard Deviation in ln(k): 6.088257296022055""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S
Total Standard Deviation in ln(k): 6.088257296022055
""",
)

entry(
    index = 76,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.08686e-18,'m^3/(mol*s)'), n=6.98186, w0=(270296,'J/mol'), E0=(12945,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2259351125985472, var=5.353393738772006, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R',), comment="""BM rule fitted to 27 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R
    Total Standard Deviation in ln(k): 5.206112312348269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R
Total Standard Deviation in ln(k): 5.206112312348269""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R
Total Standard Deviation in ln(k): 5.206112312348269
""",
)

entry(
    index = 77,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.0407493,'m^3/(mol*s)'), n=2.45388, w0=(249000,'J/mol'), E0=(31893.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.044952847726052, var=20.761768270638864, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 11.760101771282905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 11.760101771282905""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 11.760101771282905
""",
)

entry(
    index = 78,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.00513,'m^3/(mol*s)'), n=2.54, w0=(272000,'J/mol'), E0=(56062.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7208456881689997e-15, var=2.1453318836518373e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 1.3609210193539073e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 1.3609210193539073e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 1.3609210193539073e-14
""",
)

entry(
    index = 79,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(0.0212544,'m^3/(mol*s)'), n=2.75929, w0=(249000,'J/mol'), E0=(32540.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.375424572644175e-15, var=0.00415747184548603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_Ext-3CS-R
    Total Standard Deviation in ln(k): 0.1292622311437395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_Ext-3CS-R
Total Standard Deviation in ln(k): 0.1292622311437395""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_Ext-3CS-R
Total Standard Deviation in ln(k): 0.1292622311437395
""",
)

entry(
    index = 80,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_3CS->S",
    kinetics = ArrheniusBM(A=(0.00614548,'m^3/(mol*s)'), n=2.81945, w0=(249000,'J/mol'), E0=(34411,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.894402766999692e-15, var=6.96476892639379, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_3CS->S
    Total Standard Deviation in ln(k): 5.290666001739405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 5.290666001739405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 5.290666001739405
""",
)

entry(
    index = 81,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_N-3CS->S",
    kinetics = ArrheniusBM(A=(0.00244964,'m^3/(mol*s)'), n=2.94489, w0=(249000,'J/mol'), E0=(33558.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-16, var=1.9611583150125462, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_N-3CS->S
    Total Standard Deviation in ln(k): 2.8074583125512653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 2.8074583125512653""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 2.8074583125512653
""",
)

entry(
    index = 82,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C",
    kinetics = ArrheniusBM(A=(55790.2,'m^3/(mol*s)'), n=0.50055, w0=(317500,'J/mol'), E0=(32447.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04377427522747485, var=0.3275462580166088, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C
    Total Standard Deviation in ln(k): 1.2573287224148515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C
Total Standard Deviation in ln(k): 1.2573287224148515""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C
Total Standard Deviation in ln(k): 1.2573287224148515
""",
)

entry(
    index = 83,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C",
    kinetics = ArrheniusBM(A=(20.0752,'m^3/(mol*s)'), n=1.76822, w0=(317500,'J/mol'), E0=(31116.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.015956506795648157, var=0.4796828538377225, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C
    Total Standard Deviation in ln(k): 1.4285540088824804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C
Total Standard Deviation in ln(k): 1.4285540088824804""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C
Total Standard Deviation in ln(k): 1.4285540088824804
""",
)

entry(
    index = 84,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.00592685,'m^3/(mol*s)'), n=2.82213, w0=(317500,'J/mol'), E0=(29055,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07001943073463741, var=1.8929703388781485, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 24 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 2.934148158750102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 2.934148158750102""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 2.934148158750102
""",
)

entry(
    index = 85,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C",
    kinetics = ArrheniusBM(A=(443.223,'m^3/(mol*s)'), n=1.19946, w0=(317500,'J/mol'), E0=(34136.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008918723417135966, var=1.8598445532241372, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C
    Total Standard Deviation in ln(k): 2.756388725445905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C
Total Standard Deviation in ln(k): 2.756388725445905""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C
Total Standard Deviation in ln(k): 2.756388725445905
""",
)

entry(
    index = 86,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C",
    kinetics = ArrheniusBM(A=(0.0290934,'m^3/(mol*s)'), n=2.61516, w0=(317500,'J/mol'), E0=(27617.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15806653742000057, var=6.551905071355407, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C
    Total Standard Deviation in ln(k): 5.528610210279264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C
Total Standard Deviation in ln(k): 5.528610210279264""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C
Total Standard Deviation in ln(k): 5.528610210279264
""",
)

entry(
    index = 87,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS",
    kinetics = ArrheniusBM(A=(15.4598,'m^3/(mol*s)'), n=1.59706, w0=(317500,'J/mol'), E0=(40100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-16, var=2.327449793419232, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS
    Total Standard Deviation in ln(k): 3.058420176650364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS
Total Standard Deviation in ln(k): 3.058420176650364""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS
Total Standard Deviation in ln(k): 3.058420176650364
""",
)

entry(
    index = 88,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS",
    kinetics = ArrheniusBM(A=(63.6958,'m^3/(mol*s)'), n=1.51517, w0=(317500,'J/mol'), E0=(38428.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001878874801628208, var=0.21761991682257942, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS',), comment="""BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS
    Total Standard Deviation in ln(k): 0.9399246912565254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS
Total Standard Deviation in ln(k): 0.9399246912565254""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS
Total Standard Deviation in ln(k): 0.9399246912565254
""",
)

entry(
    index = 89,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(75.3042,'m^3/(mol*s)'), n=1.52456, w0=(317500,'J/mol'), E0=(33920.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.411058067090517e-15, var=0.8114235428826955, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8058463327547583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8058463327547583""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8058463327547583
""",
)

entry(
    index = 90,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(60.6,'m^3/(mol*s)'), n=1.55801, w0=(317500,'J/mol'), E0=(34547.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1409471210339054e-15, var=0.06120644243360033, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.49597017149143735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.49597017149143735""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.49597017149143735
""",
)

entry(
    index = 91,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_3CS->S",
    kinetics = ArrheniusBM(A=(19.6803,'m^3/(mol*s)'), n=1.71128, w0=(317500,'J/mol'), E0=(40709.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2916382502270627e-15, var=2.0135705987417425, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_3CS->S
    Total Standard Deviation in ln(k): 2.844725855270249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_3CS->S
Total Standard Deviation in ln(k): 2.844725855270249""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_3CS->S
Total Standard Deviation in ln(k): 2.844725855270249
""",
)

entry(
    index = 92,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S",
    kinetics = ArrheniusBM(A=(177.699,'m^3/(mol*s)'), n=1.40192, w0=(317500,'J/mol'), E0=(36569,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009926309440726474, var=0.5521710810402327, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S
    Total Standard Deviation in ln(k): 1.5146233266514977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S
Total Standard Deviation in ln(k): 1.5146233266514977""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S
Total Standard Deviation in ln(k): 1.5146233266514977
""",
)

entry(
    index = 93,
    label = "Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R_Ext-3S-R",
    kinetics = ArrheniusBM(A=(4.59463,'m^3/(mol*s)'), n=2.0774, w0=(294500,'J/mol'), E0=(33823.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.032177513690579e-14, var=12.445504203658531, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R_Ext-3S-R
    Total Standard Deviation in ln(k): 7.072341730799946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R_Ext-3S-R
Total Standard Deviation in ln(k): 7.072341730799946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_3CS->S_Ext-2HS-R_Ext-3S-R
Total Standard Deviation in ln(k): 7.072341730799946
""",
)

entry(
    index = 94,
    label = "Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_5R!H->C",
    kinetics = ArrheniusBM(A=(14.6534,'m^3/(mol*s)'), n=2.04407, w0=(294500,'J/mol'), E0=(24375.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09579597121871126, var=0.10514310734442568, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_5R!H->C
    Total Standard Deviation in ln(k): 0.8907443390176879"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_5R!H->C
Total Standard Deviation in ln(k): 0.8907443390176879""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_5R!H->C
Total Standard Deviation in ln(k): 0.8907443390176879
""",
)

entry(
    index = 95,
    label = "Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.00192903,'m^3/(mol*s)'), n=3.0727, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3881902698267545, var=10.216414683279227, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_N-5R!H->C
    Total Standard Deviation in ln(k): 9.895675378337025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_N-5R!H->C
Total Standard Deviation in ln(k): 9.895675378337025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-2R->C_N-3R->H_N-3CS->S_Ext-2HS-R_N-5R!H->C
Total Standard Deviation in ln(k): 9.895675378337025
""",
)

entry(
    index = 96,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(380.898,'m^3/(mol*s)'), n=0.934938, w0=(317500,'J/mol'), E0=(70647.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08234403607518832, var=7.245831232226086, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.603256826051979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.603256826051979""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.603256826051979
""",
)

entry(
    index = 97,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C",
    kinetics = ArrheniusBM(A=(4.73341,'m^3/(mol*s)'), n=1.5916, w0=(317500,'J/mol'), E0=(63328,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03868672607114094, var=1.7946619641676695, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C
    Total Standard Deviation in ln(k): 2.7828460572863802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C
Total Standard Deviation in ln(k): 2.7828460572863802""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C
Total Standard Deviation in ln(k): 2.7828460572863802
""",
)

entry(
    index = 98,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C",
    kinetics = ArrheniusBM(A=(29.8975,'m^3/(mol*s)'), n=1.49988, w0=(317500,'J/mol'), E0=(67924.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04706126915169529, var=2.6989100505355466, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C
    Total Standard Deviation in ln(k): 3.411695306309034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C
Total Standard Deviation in ln(k): 3.411695306309034""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C
Total Standard Deviation in ln(k): 3.411695306309034
""",
)

entry(
    index = 99,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->C",
    kinetics = ArrheniusBM(A=(0.154216,'m^3/(mol*s)'), n=2.18909, w0=(317500,'J/mol'), E0=(56362.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2658081826039391, var=8.107237683030892, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->C
    Total Standard Deviation in ln(k): 8.888547138397302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 8.888547138397302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 8.888547138397302
""",
)

entry(
    index = 100,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->C",
    kinetics = ArrheniusBM(A=(1.33397e-07,'m^3/(mol*s)'), n=4.18658, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6942296889161879, var=5.19091504951638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->C
    Total Standard Deviation in ln(k): 6.311799846537147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 6.311799846537147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 6.311799846537147
""",
)

entry(
    index = 101,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->C",
    kinetics = ArrheniusBM(A=(5.18473e-05,'m^3/(mol*s)'), n=3.04327, w0=(317500,'J/mol'), E0=(48037.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5496790161333472, var=0.5963962519461896, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->C
    Total Standard Deviation in ln(k): 2.9292937122174445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 2.9292937122174445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 2.9292937122174445
""",
)

entry(
    index = 102,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->C",
    kinetics = ArrheniusBM(A=(0.000104098,'m^3/(mol*s)'), n=3.11698, w0=(317500,'J/mol'), E0=(52141.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21067986745716097, var=0.6348756686514542, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->C
    Total Standard Deviation in ln(k): 2.1267009795776057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 2.1267009795776057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 2.1267009795776057
""",
)

entry(
    index = 103,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C",
    kinetics = ArrheniusBM(A=(0.00142365,'m^3/(mol*s)'), n=2.39072, w0=(317500,'J/mol'), E0=(33779.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003922005537813955, var=0.1101071823935851, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C
    Total Standard Deviation in ln(k): 0.6750735441652626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C
Total Standard Deviation in ln(k): 0.6750735441652626""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C
Total Standard Deviation in ln(k): 0.6750735441652626
""",
)

entry(
    index = 104,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C",
    kinetics = ArrheniusBM(A=(4.05312,'m^3/(mol*s)'), n=1.73858, w0=(317500,'J/mol'), E0=(43822.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28401942585150025, var=2.89836193298741, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C
    Total Standard Deviation in ln(k): 4.126593147681154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C
Total Standard Deviation in ln(k): 4.126593147681154""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C
Total Standard Deviation in ln(k): 4.126593147681154
""",
)

entry(
    index = 105,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.84617,'m^3/(mol*s)'), n=1.49611, w0=(317500,'J/mol'), E0=(51849.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06573501842308456, var=4.47986070353437, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.408321762636396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.408321762636396""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.408321762636396
""",
)

entry(
    index = 106,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(1494.28,'m^3/(mol*s)'), n=1.33088, w0=(294500,'J/mol'), E0=(55894,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0941889225617271, var=1.1774245321223955, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 2.4119774714536635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 2.4119774714536635""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 2.4119774714536635
""",
)

entry(
    index = 107,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(42.4829,'m^3/(mol*s)'), n=1.46962, w0=(317500,'J/mol'), E0=(52924.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2056758129768, var=10.475782606845037, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 7.005361833766911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 7.005361833766911""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 7.005361833766911
""",
)

entry(
    index = 108,
    label = "Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.29942e-05,'m^3/(mol*s)'), n=3.18988, w0=(317500,'J/mol'), E0=(38065.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0333106001816501e-15, var=2.013570598741806, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_5R!H->C
    Total Standard Deviation in ln(k): 2.8447258552702928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_5R!H->C
Total Standard Deviation in ln(k): 2.8447258552702928""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_5R!H->C
Total Standard Deviation in ln(k): 2.8447258552702928
""",
)

entry(
    index = 109,
    label = "Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.52792e-05,'m^3/(mol*s)'), n=3.1083, w0=(317500,'J/mol'), E0=(37030.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3777474669088669e-15, var=1.8875434419906463, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.7542633762269664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.7542633762269664""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_3R->S_N-4BrCClFINOPSSi->S_Ext-3S-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.7542633762269664
""",
)

entry(
    index = 110,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(6.81025e-06,'m^3/(mol*s)'), n=3.1715, w0=(317500,'J/mol'), E0=(36674.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018616247097733737, var=0.5771529562157245, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R
    Total Standard Deviation in ln(k): 1.569783426757663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 1.569783426757663""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 1.569783426757663
""",
)

entry(
    index = 111,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.000123856,'m^3/(mol*s)'), n=2.91347, w0=(317500,'J/mol'), E0=(34418.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0056866487702667, var=0.15207352310321687, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.7960666892489359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.7960666892489359""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.7960666892489359
""",
)

entry(
    index = 112,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Sp-5R!H-3CH",
    kinetics = ArrheniusBM(A=(2.02602e-05,'m^3/(mol*s)'), n=2.99418, w0=(317500,'J/mol'), E0=(31401.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.8932696805086206e-14, var=1.773215617680309, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Sp-5R!H-3CH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Sp-5R!H-3CH
    Total Standard Deviation in ln(k): 2.6695481791230513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Sp-5R!H-3CH
Total Standard Deviation in ln(k): 2.6695481791230513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Sp-5R!H-3CH
Total Standard Deviation in ln(k): 2.6695481791230513
""",
)

entry(
    index = 113,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_N-Sp-5R!H-3CH",
    kinetics = ArrheniusBM(A=(1.51815e-05,'m^3/(mol*s)'), n=3.06732, w0=(317500,'J/mol'), E0=(36222,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.616587100635776e-15, var=1.8371583048114932, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_N-Sp-5R!H-3CH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_N-Sp-5R!H-3CH
    Total Standard Deviation in ln(k): 2.7172542680303793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_N-Sp-5R!H-3CH
Total Standard Deviation in ln(k): 2.7172542680303793""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_N-Sp-5R!H-3CH
Total Standard Deviation in ln(k): 2.7172542680303793
""",
)

entry(
    index = 114,
    label = "Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R",
    kinetics = ArrheniusBM(A=(2.90595e-05,'m^3/(mol*s)'), n=3.18979, w0=(249000,'J/mol'), E0=(27477.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0548379043521012e-15, var=0.03553994326654111, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R
    Total Standard Deviation in ln(k): 0.3779334695863017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R
Total Standard Deviation in ln(k): 0.3779334695863017""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R
Total Standard Deviation in ln(k): 0.3779334695863017
""",
)

entry(
    index = 115,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R",
    kinetics = ArrheniusBM(A=(1.01782e-11,'m^3/(mol*s)'), n=5.1829, w0=(249000,'J/mol'), E0=(5186.61,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7348495423344288, var=14.833856239914466, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R
    Total Standard Deviation in ln(k): 9.567541772050072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R
Total Standard Deviation in ln(k): 9.567541772050072""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R
Total Standard Deviation in ln(k): 9.567541772050072
""",
)

entry(
    index = 116,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R",
    kinetics = ArrheniusBM(A=(4.83368e-05,'m^3/(mol*s)'), n=3.20995, w0=(249000,'J/mol'), E0=(29321.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03229632635727639, var=2.7690877446905993, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R
    Total Standard Deviation in ln(k): 3.4171412194191744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R
Total Standard Deviation in ln(k): 3.4171412194191744""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R
Total Standard Deviation in ln(k): 3.4171412194191744
""",
)

entry(
    index = 117,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.58052,'m^3/(mol*s)'), n=1.86431, w0=(272000,'J/mol'), E0=(65669.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036674540385570734, var=4.6415632286791455, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 4.411205968546126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.411205968546126""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 4.411205968546126
""",
)

entry(
    index = 118,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.318433,'m^3/(mol*s)'), n=2.12407, w0=(272000,'J/mol'), E0=(66475.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-16, var=3.3242586145640645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 3.655143154322567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.655143154322567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.655143154322567
""",
)

entry(
    index = 119,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.00122069,'m^3/(mol*s)'), n=2.68685, w0=(272000,'J/mol'), E0=(60040.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-16, var=0.29949067578057637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.0971061316503168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.0971061316503168""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.0971061316503168
""",
)

entry(
    index = 120,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C",
    kinetics = ArrheniusBM(A=(8.16927e-05,'m^3/(mol*s)'), n=3.42308, w0=(249000,'J/mol'), E0=(51484.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.40286438830249, var=22.327128356111366, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C
    Total Standard Deviation in ln(k): 10.4849142403674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C
Total Standard Deviation in ln(k): 10.4849142403674""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_3R->C
Total Standard Deviation in ln(k): 10.4849142403674
""",
)

entry(
    index = 121,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C",
    kinetics = ArrheniusBM(A=(0.00158501,'m^3/(mol*s)'), n=3.15106, w0=(249000,'J/mol'), E0=(45774.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7817322278639215, var=6.896063717904553, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C
    Total Standard Deviation in ln(k): 7.228657292633147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C
Total Standard Deviation in ln(k): 7.228657292633147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_5R!H->S_N-3R->C
Total Standard Deviation in ln(k): 7.228657292633147
""",
)

entry(
    index = 122,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O",
    kinetics = ArrheniusBM(A=(6.04742e-05,'m^3/(mol*s)'), n=3.53682, w0=(272000,'J/mol'), E0=(44735.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13600577328471436, var=117.11307444908414, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O
    Total Standard Deviation in ln(k): 22.036724349887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O
Total Standard Deviation in ln(k): 22.036724349887""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O
Total Standard Deviation in ln(k): 22.036724349887
""",
)

entry(
    index = 123,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O",
    kinetics = ArrheniusBM(A=(8897.71,'m^3/(mol*s)'), n=0.762863, w0=(261105,'J/mol'), E0=(57735.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11486465242533507, var=7.012339137822798, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O
    Total Standard Deviation in ln(k): 5.597307852742134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O
Total Standard Deviation in ln(k): 5.597307852742134""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O
Total Standard Deviation in ln(k): 5.597307852742134
""",
)

entry(
    index = 124,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(0.00063138,'m^3/(mol*s)'), n=2.72973, w0=(272000,'J/mol'), E0=(45623.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001505039884908918, var=0.7554593378624788, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C
    Total Standard Deviation in ln(k): 1.746240380020996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 1.746240380020996""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 1.746240380020996
""",
)

entry(
    index = 125,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(1.23982e-18,'m^3/(mol*s)'), n=7.11048, w0=(269909,'J/mol'), E0=(11921.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22427056071867568, var=7.192115220925325, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C
    Total Standard Deviation in ln(k): 5.93981631559424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 5.93981631559424""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 5.93981631559424
""",
)

entry(
    index = 126,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(26.0573,'m^3/(mol*s)'), n=1.51612, w0=(317500,'J/mol'), E0=(24050.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-17, var=0.4322015750855826, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 1.3179537254195421"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.3179537254195421""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.3179537254195421
""",
)

entry(
    index = 127,
    label = "Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.936426,'m^3/(mol*s)'), n=2.24723, w0=(317500,'J/mol'), E0=(31132.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.4443686672721672e-16, var=1.0177168789086954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.022415933127977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.022415933127977""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.022415933127977
""",
)

entry(
    index = 128,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(5277.35,'m^3/(mol*s)'), n=0.962043, w0=(317500,'J/mol'), E0=(52796.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0405316847159589, var=3.454023927111954, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 3.8276394496831356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 3.8276394496831356""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 3.8276394496831356
""",
)

entry(
    index = 129,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.348827,'m^3/(mol*s)'), n=2.32595, w0=(317500,'J/mol'), E0=(39769.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03945263744700713, var=0.5800336573371802, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 1.6259322766841693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 1.6259322766841693""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 1.6259322766841693
""",
)

entry(
    index = 130,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.181589,'m^3/(mol*s)'), n=2.24426, w0=(317500,'J/mol'), E0=(24153.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.024164290124884302, var=2.0221625910255896, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.91150297511187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.91150297511187""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.91150297511187
""",
)

entry(
    index = 131,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(12782.7,'m^3/(mol*s)'), n=0.833, w0=(317500,'J/mol'), E0=(39748.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013993924033727474, var=4.115981758489139, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 4.102343580134411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.102343580134411""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.102343580134411
""",
)

entry(
    index = 132,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(150.566,'m^3/(mol*s)'), n=1.44115, w0=(317500,'J/mol'), E0=(41378.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008896832520293687, var=0.12675407312254353, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R
    Total Standard Deviation in ln(k): 0.7360904236832122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R
Total Standard Deviation in ln(k): 0.7360904236832122""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R
Total Standard Deviation in ln(k): 0.7360904236832122
""",
)

entry(
    index = 133,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(14.1474,'m^3/(mol*s)'), n=1.67094, w0=(317500,'J/mol'), E0=(34184.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007818845280629075, var=0.5190858533336257, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.4640091093495922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.4640091093495922""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.4640091093495922
""",
)

entry(
    index = 134,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_Sp-5C-3C",
    kinetics = ArrheniusBM(A=(60.7269,'m^3/(mol*s)'), n=1.52344, w0=(317500,'J/mol'), E0=(33439.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-16, var=1.7732156176804723, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_Sp-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_Sp-5C-3C
    Total Standard Deviation in ln(k): 2.669548179123103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_Sp-5C-3C
Total Standard Deviation in ln(k): 2.669548179123103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_Sp-5C-3C
Total Standard Deviation in ln(k): 2.669548179123103
""",
)

entry(
    index = 135,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_N-Sp-5C-3C",
    kinetics = ArrheniusBM(A=(62.8616,'m^3/(mol*s)'), n=1.55368, w0=(317500,'J/mol'), E0=(37464.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.411058067090517e-15, var=1.837158304811619, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_N-Sp-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_N-Sp-5C-3C
    Total Standard Deviation in ln(k): 2.71725426803047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_N-Sp-5C-3C
Total Standard Deviation in ln(k): 2.71725426803047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->S_N-3CS->S_N-Sp-5C-3C
Total Standard Deviation in ln(k): 2.71725426803047
""",
)

entry(
    index = 136,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(349.269,'m^3/(mol*s)'), n=1.0579, w0=(317500,'J/mol'), E0=(69973.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04946624747382939, var=17.261026676291305, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 8.453237942438196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 8.453237942438196""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 8.453237942438196
""",
)

entry(
    index = 137,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.228988,'m^3/(mol*s)'), n=1.78128, w0=(317500,'J/mol'), E0=(63180.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036397997279162486, var=2.4682504370614042, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 3.241024688337303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.241024688337303""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.241024688337303
""",
)

entry(
    index = 138,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.0665415,'m^3/(mol*s)'), n=2.22257, w0=(317500,'J/mol'), E0=(59702.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.128867229747107, var=3.937611656191781, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 9.326991884321862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 9.326991884321862""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 9.326991884321862
""",
)

entry(
    index = 139,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.35403e-05,'m^3/(mol*s)'), n=2.91782, w0=(317500,'J/mol'), E0=(49877.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4385527697102232, var=3.9204543891872103, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.583857182717773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.583857182717773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.583857182717773
""",
)

entry(
    index = 140,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.13314e-09,'m^3/(mol*s)'), n=4.54204, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2343458155994984, var=4.610088382862965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.405761410277548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.405761410277548""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.405761410277548
""",
)

entry(
    index = 141,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000236897,'m^3/(mol*s)'), n=2.94337, w0=(317500,'J/mol'), E0=(54908.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5214030811476161, var=6.547848804953537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 6.439927417319847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 6.439927417319847""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 6.439927417319847
""",
)

entry(
    index = 142,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000399452,'m^3/(mol*s)'), n=2.54537, w0=(317500,'J/mol'), E0=(31702,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3437025027686733, var=1.3075674026009199, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 3.155966907759866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 3.155966907759866""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_3R->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 3.155966907759866
""",
)

entry(
    index = 143,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C",
    kinetics = ArrheniusBM(A=(5.18866e-16,'m^3/(mol*s)'), n=6.4776, w0=(317500,'J/mol'), E0=(7877.05,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11718273055059752, var=1.6666914659043952, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C
    Total Standard Deviation in ln(k): 2.8825500821487626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C
Total Standard Deviation in ln(k): 2.8825500821487626""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C
Total Standard Deviation in ln(k): 2.8825500821487626
""",
)

entry(
    index = 144,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_N-5CO->C",
    kinetics = ArrheniusBM(A=(2.65871e-05,'m^3/(mol*s)'), n=3.25466, w0=(317500,'J/mol'), E0=(17394.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_5CO->O",
    kinetics = ArrheniusBM(A=(1.05137e-06,'m^3/(mol*s)'), n=3.65502, w0=(317500,'J/mol'), E0=(19286.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O",
    kinetics = ArrheniusBM(A=(81.7556,'m^3/(mol*s)'), n=1.11093, w0=(317500,'J/mol'), E0=(54657.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08119831268982, var=3.8817021078574037, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O
    Total Standard Deviation in ln(k): 4.153752067729581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O
Total Standard Deviation in ln(k): 4.153752067729581""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O
Total Standard Deviation in ln(k): 4.153752067729581
""",
)

entry(
    index = 147,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S",
    kinetics = ArrheniusBM(A=(0.000254077,'m^3/(mol*s)'), n=3.34456, w0=(294500,'J/mol'), E0=(41581.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0071769324355312435, var=2.3093211498828183, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S
    Total Standard Deviation in ln(k): 3.064518277901262"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S
Total Standard Deviation in ln(k): 3.064518277901262""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S
Total Standard Deviation in ln(k): 3.064518277901262
""",
)

entry(
    index = 148,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S",
    kinetics = ArrheniusBM(A=(4198.94,'m^3/(mol*s)'), n=1.20272, w0=(294500,'J/mol'), E0=(54758.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09741757981091793, var=1.0437770750767241, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S
    Total Standard Deviation in ln(k): 2.292913575204471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S
Total Standard Deviation in ln(k): 2.292913575204471""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S
Total Standard Deviation in ln(k): 2.292913575204471
""",
)

entry(
    index = 149,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_Ext-3R-R",
    kinetics = ArrheniusBM(A=(6.38794e-08,'m^3/(mol*s)'), n=3.978, w0=(317500,'J/mol'), E0=(23104,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_Ext-3R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_3R->C",
    kinetics = ArrheniusBM(A=(9.49305e-05,'m^3/(mol*s)'), n=2.84136, w0=(317500,'J/mol'), E0=(34837.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4880317614378089, var=11.740517523808274, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_3R->C
    Total Standard Deviation in ln(k): 8.095322652174971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_3R->C
Total Standard Deviation in ln(k): 8.095322652174971""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_3R->C
Total Standard Deviation in ln(k): 8.095322652174971
""",
)

entry(
    index = 151,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_N-3R->C",
    kinetics = ArrheniusBM(A=(0.000164712,'m^3/(mol*s)'), n=3.26193, w0=(317500,'J/mol'), E0=(40468.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7932259541480697, var=51.958821769895444, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_N-3R->C
    Total Standard Deviation in ln(k): 18.956218033868687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_N-3R->C
Total Standard Deviation in ln(k): 18.956218033868687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-4BrCClFINOPSSi->S_N-3R->C
Total Standard Deviation in ln(k): 18.956218033868687
""",
)

entry(
    index = 152,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.22276e-07,'m^3/(mol*s)'), n=3.59374, w0=(317500,'J/mol'), E0=(32628.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04893764120994924, var=0.40393660937716264, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.3970884743551029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.3970884743551029""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.3970884743551029
""",
)

entry(
    index = 153,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(7.99565e-07,'m^3/(mol*s)'), n=3.36447, w0=(317500,'J/mol'), E0=(37963.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.153863503536176e-14, var=0.007655398737838622, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R
    Total Standard Deviation in ln(k): 0.17540456725742395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 0.17540456725742395""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 0.17540456725742395
""",
)

entry(
    index = 154,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH",
    kinetics = ArrheniusBM(A=(0.000276632,'m^3/(mol*s)'), n=2.75658, w0=(317500,'J/mol'), E0=(42173.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022235845222001054, var=2.4243872931305988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH
    Total Standard Deviation in ln(k): 3.17733050261347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH
Total Standard Deviation in ln(k): 3.17733050261347""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH
Total Standard Deviation in ln(k): 3.17733050261347
""",
)

entry(
    index = 155,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH",
    kinetics = ArrheniusBM(A=(1.01283e-06,'m^3/(mol*s)'), n=3.3304, w0=(317500,'J/mol'), E0=(33000.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.563788484135622e-15, var=2.543419805558462, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH
    Total Standard Deviation in ln(k): 3.1971720952496043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH
Total Standard Deviation in ln(k): 3.1971720952496043""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH
Total Standard Deviation in ln(k): 3.1971720952496043
""",
)

entry(
    index = 156,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.18435e-05,'m^3/(mol*s)'), n=2.96355, w0=(317500,'J/mol'), E0=(33999.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.2388396337269086e-15, var=0.8114235428827421, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8058463327548095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8058463327548095""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8058463327548095
""",
)

entry(
    index = 157,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.38863e-05,'m^3/(mol*s)'), n=2.98781, w0=(317500,'J/mol'), E0=(33846.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.1171536438813114e-14, var=0.06120644243364482, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.495970171491693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.495970171491693""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.495970171491693
""",
)

entry(
    index = 158,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.000122281,'m^3/(mol*s)'), n=3.13926, w0=(249000,'J/mol'), E0=(31149.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.958984679511045e-15, var=0.24973797734205969, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_5R!H->C
    Total Standard Deviation in ln(k): 1.0018421149746142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_5R!H->C
Total Standard Deviation in ln(k): 1.0018421149746142""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_5R!H->C
Total Standard Deviation in ln(k): 1.0018421149746142
""",
)

entry(
    index = 159,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0010924,'m^3/(mol*s)'), n=2.69456, w0=(249000,'J/mol'), E0=(45689.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3777474669088669e-15, var=28.035916919514833, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.614862468062919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.614862468062919""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_3CH->C_Ext-2S-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.614862468062919
""",
)

entry(
    index = 160,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.79502e-05,'m^3/(mol*s)'), n=3.14646, w0=(249000,'J/mol'), E0=(29617.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.166553000908251e-16, var=1.4248494433636956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_5R!H->C
    Total Standard Deviation in ln(k): 2.3929932740192723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_5R!H->C
Total Standard Deviation in ln(k): 2.3929932740192723""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_5R!H->C
Total Standard Deviation in ln(k): 2.3929932740192723
""",
)

entry(
    index = 161,
    label = "Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0042243,'m^3/(mol*s)'), n=2.6257, w0=(249000,'J/mol'), E0=(36684.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.967147752817193, var=6.89606371790433, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.694525445781986"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.694525445781986""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_2CS->S_N-3R->S_N-3CH->C_Ext-2S-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.694525445781986
""",
)

entry(
    index = 162,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.208329,'m^3/(mol*s)'), n=1.92192, w0=(272000,'J/mol'), E0=(64668.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02779143253114869, var=11.89387245274249, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 6.983656623603287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 6.983656623603287""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 6.983656623603287
""",
)

entry(
    index = 163,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.124705,'m^3/(mol*s)'), n=2.20292, w0=(272000,'J/mol'), E0=(65417.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360837e-15, var=3.9427479530338196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 3.9806729430002163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.9806729430002163""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.9806729430002163
""",
)

entry(
    index = 164,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000903657,'m^3/(mol*s)'), n=2.70222, w0=(272000,'J/mol'), E0=(58538.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.894402766999692e-15, var=5.9615646681069725, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 4.894824431661776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 4.894824431661776""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 4.894824431661776
""",
)

entry(
    index = 165,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.882e-11,'m^3/(mol*s)'), n=6.08176, w0=(272000,'J/mol'), E0=(39450.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.881784197001246e-16, var=3.5126004205114634e-61, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 2.2316040695983044e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.2316040695983044e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_5CO->O_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.2316040695983044e-15
""",
)

entry(
    index = 166,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.96921e-05,'m^3/(mol*s)'), n=2.97296, w0=(272000,'J/mol'), E0=(46376.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.027099445432831742, var=1.6392319257344832, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 2.6348013560046626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.6348013560046626""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.6348013560046626
""",
)

entry(
    index = 167,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(12999.2,'m^3/(mol*s)'), n=0.86794, w0=(253182,'J/mol'), E0=(53059.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12209463686639228, var=3.6865599743767437, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi
    Total Standard Deviation in ln(k): 4.155945309329785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi
Total Standard Deviation in ln(k): 4.155945309329785""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi
Total Standard Deviation in ln(k): 4.155945309329785
""",
)

entry(
    index = 168,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_N-Sp-5C-4BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(0.00339221,'m^3/(mol*s)'), n=2.69997, w0=(272000,'J/mol'), E0=(53185.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.027645167726293e-16, var=0.6807477725787159, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_N-Sp-5C-4BrCClFINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_N-Sp-5C-4BrCClFINOPSSi
    Total Standard Deviation in ln(k): 1.654055599696762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_N-Sp-5C-4BrCClFINOPSSi
Total Standard Deviation in ln(k): 1.654055599696762""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_N-Sp-5C-4BrCClFINOPSSi
Total Standard Deviation in ln(k): 1.654055599696762
""",
)

entry(
    index = 169,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.000115636,'m^3/(mol*s)'), n=3.01361, w0=(272000,'J/mol'), E0=(47245.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00019374198799441432, var=1.0322324752660537, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C
    Total Standard Deviation in ln(k): 2.0372744183304503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C
Total Standard Deviation in ln(k): 2.0372744183304503""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C
Total Standard Deviation in ln(k): 2.0372744183304503
""",
)

entry(
    index = 170,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.88,'m^3/(mol*s)'), n=1.4, w0=(272000,'J/mol'), E0=(44431,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O",
    kinetics = ArrheniusBM(A=(3.16045e-26,'m^3/(mol*s)'), n=10.4017, w0=(264333,'J/mol'), E0=(-4566.59,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8137202181114271, var=10.615334355788283, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
    Total Standard Deviation in ln(k): 11.088749863328255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
Total Standard Deviation in ln(k): 11.088749863328255""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
Total Standard Deviation in ln(k): 11.088749863328255
""",
)

entry(
    index = 172,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(6.51682e-09,'m^3/(mol*s)'), n=4.14862, w0=(270789,'J/mol'), E0=(38860,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07532332692547754, var=2.013720702208465, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.034086474908031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
Total Standard Deviation in ln(k): 3.034086474908031""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
Total Standard Deviation in ln(k): 3.034086474908031
""",
)

entry(
    index = 173,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(30758.9,'m^3/(mol*s)'), n=0.713891, w0=(317500,'J/mol'), E0=(54947.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.032746966070939174, var=5.447921481281428, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R',), comment="""BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
    Total Standard Deviation in ln(k): 4.761487438056783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
Total Standard Deviation in ln(k): 4.761487438056783""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
Total Standard Deviation in ln(k): 4.761487438056783
""",
)

entry(
    index = 174,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_3R->C",
    kinetics = ArrheniusBM(A=(34.803,'m^3/(mol*s)'), n=1.59855, w0=(317500,'J/mol'), E0=(43294.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9928860211485868, var=8.107237683030348, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_3R->C
    Total Standard Deviation in ln(k): 8.202813064388687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_3R->C
Total Standard Deviation in ln(k): 8.202813064388687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_3R->C
Total Standard Deviation in ln(k): 8.202813064388687
""",
)

entry(
    index = 175,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-3R->C",
    kinetics = ArrheniusBM(A=(0.00946561,'m^3/(mol*s)'), n=2.78699, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9218362828165603, var=5.1909150495160805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-3R->C
    Total Standard Deviation in ln(k): 6.883675710608302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-3R->C
Total Standard Deviation in ln(k): 6.883675710608302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-3R->C
Total Standard Deviation in ln(k): 6.883675710608302
""",
)

entry(
    index = 176,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.00803084,'m^3/(mol*s)'), n=2.82316, w0=(317500,'J/mol'), E0=(26228.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04371997329334815, var=0.9219553772975455, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R',), comment="""BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.034765878774659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
Total Standard Deviation in ln(k): 2.034765878774659""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
Total Standard Deviation in ln(k): 2.034765878774659
""",
)

entry(
    index = 177,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_3R->C",
    kinetics = ArrheniusBM(A=(35.8438,'m^3/(mol*s)'), n=1.71112, w0=(317500,'J/mol'), E0=(45108.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.567867059839517e-14, var=0.44611839864362796, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_3R->C
    Total Standard Deviation in ln(k): 1.339004562186042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_3R->C
Total Standard Deviation in ln(k): 1.339004562186042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_3R->C
Total Standard Deviation in ln(k): 1.339004562186042
""",
)

entry(
    index = 178,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_N-3R->C",
    kinetics = ArrheniusBM(A=(56.8649,'m^3/(mol*s)'), n=1.72749, w0=(317500,'J/mol'), E0=(53582,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4500675694456033, var=0.6348756686513871, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_N-3R->C
    Total Standard Deviation in ln(k): 5.2407404318097885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_N-3R->C
Total Standard Deviation in ln(k): 5.2407404318097885""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_N-3R->C
Total Standard Deviation in ln(k): 5.2407404318097885
""",
)

entry(
    index = 179,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(110.007,'m^3/(mol*s)'), n=1.36375, w0=(317500,'J/mol'), E0=(31445.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.411058067090517e-15, var=8.097837060469875, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 5.704814225193424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 5.704814225193424""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_3R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 5.704814225193424
""",
)

entry(
    index = 180,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(72.0205,'m^3/(mol*s)'), n=1.5324, w0=(317500,'J/mol'), E0=(31168.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.8887373345443345e-16, var=10.35076642840592, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 6.4497553835964005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 6.4497553835964005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_N-3R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 6.4497553835964005
""",
)

entry(
    index = 181,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(84.2383,'m^3/(mol*s)'), n=1.51775, w0=(317500,'J/mol'), E0=(39991.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007518479787444011, var=0.20215427729965116, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.9202510170069755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.9202510170069755""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.9202510170069755
""",
)

entry(
    index = 182,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(139.299,'m^3/(mol*s)'), n=1.33084, w0=(317500,'J/mol'), E0=(38021.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.837241968382899e-15, var=0.007606726199997144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 0.1748460725872101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 0.1748460725872101""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 0.1748460725872101
""",
)

entry(
    index = 183,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(69.5507,'m^3/(mol*s)'), n=1.50841, w0=(317500,'J/mol'), E0=(34264.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.749829501362376e-16, var=0.26612572665234635, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 1.034190203517799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.034190203517799""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.034190203517799
""",
)

entry(
    index = 184,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_3R->C",
    kinetics = ArrheniusBM(A=(0.00161828,'m^3/(mol*s)'), n=2.47164, w0=(317500,'J/mol'), E0=(55641.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.472947902811076, var=35.30942718077387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_3R->C
    Total Standard Deviation in ln(k): 15.613357994435821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 15.613357994435821""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 15.613357994435821
""",
)

entry(
    index = 185,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_N-3R->C",
    kinetics = ArrheniusBM(A=(0.0181847,'m^3/(mol*s)'), n=2.50777, w0=(317500,'J/mol'), E0=(59291.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.684161091946942, var=45.64933145830045, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_N-3R->C
    Total Standard Deviation in ln(k): 15.263847728877783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 15.263847728877783""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 15.263847728877783
""",
)

entry(
    index = 186,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_3R->C",
    kinetics = ArrheniusBM(A=(1.06572e-05,'m^3/(mol*s)'), n=2.94577, w0=(317500,'J/mol'), E0=(50445,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.560985788174477, var=1.6419856422771029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_3R->C
    Total Standard Deviation in ln(k): 6.490942124295471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 6.490942124295471""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 6.490942124295471
""",
)

entry(
    index = 187,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_N-3R->C",
    kinetics = ArrheniusBM(A=(0.00012375,'m^3/(mol*s)'), n=2.88368, w0=(317500,'J/mol'), E0=(55655.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6212330765782702, var=3.4216002655130398, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_N-3R->C
    Total Standard Deviation in ln(k): 5.269159493815183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 5.269159493815183""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 5.269159493815183
""",
)

entry(
    index = 188,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.17983e-06,'m^3/(mol*s)'), n=3.59343, w0=(317500,'J/mol'), E0=(33355.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.6734642928398245e-15, var=1.0177168789087654, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 2.0224159331280624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.0224159331280624""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_N-3R->C_5CO->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.0224159331280624
""",
)

entry(
    index = 189,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C",
    kinetics = ArrheniusBM(A=(1.26113e-11,'m^3/(mol*s)'), n=4.8106, w0=(317500,'J/mol'), E0=(23677.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08208945360923768, var=2.225430870213649, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C
    Total Standard Deviation in ln(k): 3.1968942594020513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C
Total Standard Deviation in ln(k): 3.1968942594020513""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C
Total Standard Deviation in ln(k): 3.1968942594020513
""",
)

entry(
    index = 190,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C",
    kinetics = ArrheniusBM(A=(0.193475,'m^3/(mol*s)'), n=2.04696, w0=(317500,'J/mol'), E0=(47870,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006494642291235608, var=3.994418155305171, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C
    Total Standard Deviation in ln(k): 4.0229898448931785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C
Total Standard Deviation in ln(k): 4.0229898448931785""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C
Total Standard Deviation in ln(k): 4.0229898448931785
""",
)

entry(
    index = 191,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.000378441,'m^3/(mol*s)'), n=3.29067, w0=(294500,'J/mol'), E0=(42046.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.30683552942995, var=9.954720634132677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S_Ext-3S-R
    Total Standard Deviation in ln(k): 9.60866652893314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S_Ext-3S-R
Total Standard Deviation in ln(k): 9.60866652893314""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_3R->S_Ext-3S-R
Total Standard Deviation in ln(k): 9.60866652893314
""",
)

entry(
    index = 192,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_3CH->C",
    kinetics = ArrheniusBM(A=(0.000168127,'m^3/(mol*s)'), n=3.31719, w0=(294500,'J/mol'), E0=(32767.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8763909524969404, var=0.41538588024913176, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_3CH->C
    Total Standard Deviation in ln(k): 6.006610645775539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_3CH->C
Total Standard Deviation in ln(k): 6.006610645775539""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_3CH->C
Total Standard Deviation in ln(k): 6.006610645775539
""",
)

entry(
    index = 193,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(0.00130518,'m^3/(mol*s)'), n=3.25056, w0=(294500,'J/mol'), E0=(36544.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5846175072348962, var=0.5366865189802562, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_N-3CH->C
    Total Standard Deviation in ln(k): 5.450097719233969"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_N-3CH->C
Total Standard Deviation in ln(k): 5.450097719233969""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_4BrCClFINOPSSi->S_N-3R->S_N-3CH->C
Total Standard Deviation in ln(k): 5.450097719233969
""",
)

entry(
    index = 194,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(1.69062e-05,'m^3/(mol*s)'), n=3.05785, w0=(317500,'J/mol'), E0=(38626.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01641759802277024, var=0.2021570600865039, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R
    Total Standard Deviation in ln(k): 0.9426168144514403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R
Total Standard Deviation in ln(k): 0.9426168144514403""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R
Total Standard Deviation in ln(k): 0.9426168144514403
""",
)

entry(
    index = 195,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.36475e-05,'m^3/(mol*s)'), n=2.9519, w0=(317500,'J/mol'), E0=(38454.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.47201383499846e-16, var=0.007606726200006975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 0.17484607258731583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 0.17484607258731583""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 0.17484607258731583
""",
)

entry(
    index = 196,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000117597,'m^3/(mol*s)'), n=2.88236, w0=(317500,'J/mol'), E0=(34154.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3562201627384158e-15, var=0.2661257266523192, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 1.0341902035177475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.0341902035177475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.0341902035177475
""",
)

entry(
    index = 197,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.0481574,'m^3/(mol*s)'), n=2.29034, w0=(272000,'J/mol'), E0=(63127.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.8887373345443345e-16, var=49.79105836987804, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 14.145967902635931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 14.145967902635931""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 14.145967902635931
""",
)

entry(
    index = 198,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000232678,'m^3/(mol*s)'), n=2.6151, w0=(272000,'J/mol'), E0=(58490.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.478203818225993, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 3.7388195349137856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.7388195349137856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_Ext-5R!H-R_Ext-4BrCClFINOPSSi-R_Ext-4BrCClFINOPSSi-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.7388195349137856
""",
)

entry(
    index = 199,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.31512e-05,'m^3/(mol*s)'), n=3.15407, w0=(272000,'J/mol'), E0=(52696.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3777474669088669e-15, var=6.00116130851357, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.911053210752405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.911053210752405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.911053210752405
""",
)

entry(
    index = 200,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.0331181,'m^3/(mol*s)'), n=2.03449, w0=(272000,'J/mol'), E0=(49218.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006635234598803894, var=2.252552323130456, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 3.025479153629953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 3.025479153629953""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 3.025479153629953
""",
)

entry(
    index = 201,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.000101356,'m^3/(mol*s)'), n=3.32729, w0=(249000,'J/mol'), E0=(33214.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013667616071770203, var=0.21646287498870315, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 0.9670551841880897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 0.9670551841880897""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 0.9670551841880897
""",
)

entry(
    index = 202,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.00400332,'m^3/(mol*s)'), n=2.52625, w0=(272000,'J/mol'), E0=(50833.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3777474669088669e-15, var=19.76986215110708, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 8.913716350271828"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 8.913716350271828""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 8.913716350271828
""",
)

entry(
    index = 203,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.1422e-05,'m^3/(mol*s)'), n=3.31201, w0=(272000,'J/mol'), E0=(46431.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2055290335452585e-15, var=6.001161308513851, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 4.911053210752519"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.911053210752519""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.911053210752519
""",
)

entry(
    index = 204,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.00118,'m^3/(mol*s)'), n=3, w0=(249000,'J/mol'), E0=(35155.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(9.07819e-13,'m^3/(mol*s)'), n=6.54523, w0=(272000,'J/mol'), E0=(28835.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.6645352591003718e-15, var=1.4050401682045853e-60, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 6.694812208794905e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 6.694812208794905e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 6.694812208794905e-15
""",
)

entry(
    index = 206,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.75636e-06,'m^3/(mol*s)'), n=3.39984, w0=(270231,'J/mol'), E0=(49804,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030481786267696046, var=2.1572469046243734, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 3.0210559303198896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 3.0210559303198896""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 3.0210559303198896
""",
)

entry(
    index = 207,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.000847638,'m^3/(mol*s)'), n=2.45089, w0=(272000,'J/mol'), E0=(37705.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007311331572653886, var=2.0829810984271337, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 2.911711397694038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 2.911711397694038""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 2.911711397694038
""",
)

entry(
    index = 208,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(541.183,'m^3/(mol*s)'), n=1.18659, w0=(317500,'J/mol'), E0=(52006,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0168422787979835, var=14.59106135872072, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 7.700054011691474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 7.700054011691474""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 7.700054011691474
""",
)

entry(
    index = 209,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_3R->C",
    kinetics = ArrheniusBM(A=(428.89,'m^3/(mol*s)'), n=1.28555, w0=(317500,'J/mol'), E0=(43219.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1076385270609916, var=3.937611656191449, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_3R->C
    Total Standard Deviation in ln(k): 6.761090621291252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_3R->C
Total Standard Deviation in ln(k): 6.761090621291252""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_3R->C
Total Standard Deviation in ln(k): 6.761090621291252
""",
)

entry(
    index = 210,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_N-3R->C",
    kinetics = ArrheniusBM(A=(0.0316441,'m^3/(mol*s)'), n=2.62141, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0735389150915517, var=4.610088382862507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_N-3R->C
    Total Standard Deviation in ln(k): 7.0017239718151565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_N-3R->C
Total Standard Deviation in ln(k): 7.0017239718151565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_N-3R->C
Total Standard Deviation in ln(k): 7.0017239718151565
""",
)

entry(
    index = 211,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C",
    kinetics = ArrheniusBM(A=(48.4804,'m^3/(mol*s)'), n=1.64064, w0=(317500,'J/mol'), E0=(41518.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.021721567018700396, var=0.7861118892583977, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C
    Total Standard Deviation in ln(k): 1.8320340823237513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C
Total Standard Deviation in ln(k): 1.8320340823237513""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C
Total Standard Deviation in ln(k): 1.8320340823237513
""",
)

entry(
    index = 212,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C",
    kinetics = ArrheniusBM(A=(77.6048,'m^3/(mol*s)'), n=1.63775, w0=(317500,'J/mol'), E0=(50769.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0026656730735853183, var=1.819305617137978, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C
    Total Standard Deviation in ln(k): 2.710717173692484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C
Total Standard Deviation in ln(k): 2.710717173692484""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C
Total Standard Deviation in ln(k): 2.710717173692484
""",
)

entry(
    index = 213,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(118.666,'m^3/(mol*s)'), n=1.47784, w0=(317500,'J/mol'), E0=(41535.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8599590803269704e-14, var=0.6725897953292215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_Sp-8R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 1.6441147527974131"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 1.6441147527974131""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 1.6441147527974131
""",
)

entry(
    index = 214,
    label = "Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_N-Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(59.7566,'m^3/(mol*s)'), n=1.55785, w0=(317500,'J/mol'), E0=(38430.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2916382502270627e-14, var=0.5669634519679208, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_N-Sp-8R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 1.5095048800962314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 1.5095048800962314""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS_Ext-3CS-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 1.5095048800962314
""",
)

entry(
    index = 215,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.25487e-05,'m^3/(mol*s)'), n=2.96431, w0=(317500,'J/mol'), E0=(41451.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8591943270160467, var=8.675092268907342, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 10.575990911990473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 10.575990911990473""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_3R->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 10.575990911990473
""",
)

entry(
    index = 216,
    label = "Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0015774,'m^3/(mol*s)'), n=2.72499, w0=(317500,'J/mol'), E0=(42725.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9510124977991288, var=12.044761294481486, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.859587480400982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.859587480400982""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-Sp-5BrCCCClFINOOOPSSi=4BrBrCCCCClClFFIINNOOOOPPSSSiSi_Ext-4BrCClFINOPSSi-R_N-5CO->O_N-3R->C_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.859587480400982
""",
)

entry(
    index = 217,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.37786e-05,'m^3/(mol*s)'), n=3.01805, w0=(317500,'J/mol'), E0=(40183.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-16, var=0.6725897953291446, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 1.6441147527972744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.6441147527972744""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.6441147527972744
""",
)

entry(
    index = 218,
    label = "Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.20148e-05,'m^3/(mol*s)'), n=3.09782, w0=(317500,'J/mol'), E0=(37052.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.391570050772014e-15, var=0.5669634519678879, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 1.5095048800961666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.5095048800961666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_2R->H_N-3R->S_N-4BrCClFINOPSSi->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Ext-3CH-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.5095048800961666
""",
)

entry(
    index = 219,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi_Ext-4BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0983678,'m^3/(mol*s)'), n=1.89166, w0=(272000,'J/mol'), E0=(46357.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.534556459657866e-16, var=0.2076282395513497, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi_Ext-4BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi_Ext-4BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 0.9134824336369911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 0.9134824336369911""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Ext-4BrCClFINOPSSi-R_N-Sp-5C=4BrBrCCClClFFIINNOOPPSSSiSi_Ext-4BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 0.9134824336369911
""",
)

entry(
    index = 220,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.00389628,'m^3/(mol*s)'), n=2.92766, w0=(249000,'J/mol'), E0=(36515.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.102990732322871e-15, var=0.03553994326656973, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_Ext-3R-R
    Total Standard Deviation in ln(k): 0.3779334695864665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_Ext-3R-R
Total Standard Deviation in ln(k): 0.3779334695864665""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_Ext-3R-R
Total Standard Deviation in ln(k): 0.3779334695864665
""",
)

entry(
    index = 221,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H",
    kinetics = ArrheniusBM(A=(0.000867266,'m^3/(mol*s)'), n=2.98635, w0=(249000,'J/mol'), E0=(33662.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009029643095896475, var=0.4417425041429647, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H
    Total Standard Deviation in ln(k): 1.355108897984193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H
Total Standard Deviation in ln(k): 1.355108897984193""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H
Total Standard Deviation in ln(k): 1.355108897984193
""",
)

entry(
    index = 222,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H",
    kinetics = ArrheniusBM(A=(0.000616863,'m^3/(mol*s)'), n=3.10857, w0=(249000,'J/mol'), E0=(36138.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0046351408964815715, var=0.1520600357345039, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H
    Total Standard Deviation in ln(k): 0.7933900410070241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H
Total Standard Deviation in ln(k): 0.7933900410070241""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H
Total Standard Deviation in ln(k): 0.7933900410070241
""",
)

entry(
    index = 223,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.81233e-05,'m^3/(mol*s)'), n=3.13131, w0=(272000,'J/mol'), E0=(50349.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014604051809093252, var=3.291537364665263, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 3.6738031634639032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R
Total Standard Deviation in ln(k): 3.6738031634639032""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R
Total Standard Deviation in ln(k): 3.6738031634639032
""",
)

entry(
    index = 224,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2.66495e-08,'m^3/(mol*s)'), n=3.99364, w0=(264333,'J/mol'), E0=(48197.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3112914277261781, var=3.159280718550299, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 4.345428681780079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 4.345428681780079""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 4.345428681780079
""",
)

entry(
    index = 225,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.000849598,'m^3/(mol*s)'), n=2.78644, w0=(272000,'J/mol'), E0=(57199.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1527304170451045e-17, var=0.29949067578057087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 1.0971061316503046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 1.0971061316503046""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 1.0971061316503046
""",
)

entry(
    index = 226,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.00222758,'m^3/(mol*s)'), n=2.28445, w0=(272000,'J/mol'), E0=(33071.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.870722732412196e-14, var=0.20762823955138776, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 0.9134824336371198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 0.9134824336371198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 0.9134824336371198
""",
)

entry(
    index = 227,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_3R->C",
    kinetics = ArrheniusBM(A=(10.1009,'m^3/(mol*s)'), n=1.62919, w0=(317500,'J/mol'), E0=(43306.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0048633346027744, var=35.309427180773326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_3R->C
    Total Standard Deviation in ln(k): 14.437266114515372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_3R->C
Total Standard Deviation in ln(k): 14.437266114515372""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_3R->C
Total Standard Deviation in ln(k): 14.437266114515372
""",
)

entry(
    index = 228,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_N-3R->C",
    kinetics = ArrheniusBM(A=(11.1645,'m^3/(mol*s)'), n=1.76823, w0=(317500,'J/mol'), E0=(50143.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2602343414810055, var=45.649331458300324, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_N-3R->C
    Total Standard Deviation in ln(k): 16.711267953837723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_N-3R->C
Total Standard Deviation in ln(k): 16.711267953837723""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R_N-3R->C
Total Standard Deviation in ln(k): 16.711267953837723
""",
)

entry(
    index = 229,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(35.7817,'m^3/(mol*s)'), n=1.68478, w0=(317500,'J/mol'), E0=(41458,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.47201383499846e-16, var=1.4671526163333815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.4282569231961437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.4282569231961437""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.4282569231961437
""",
)

entry(
    index = 230,
    label = "Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(46.1861,'m^3/(mol*s)'), n=1.70955, w0=(317500,'J/mol'), E0=(50217.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3128566721595518, var=3.42160026551288, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.006907221406256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.006907221406256""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.006907221406256
""",
)

entry(
    index = 231,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.25e-05,'m^3/(mol*s)'), n=3.21, w0=(249000,'J/mol'), E0=(25061.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_3R->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_3CS->S",
    kinetics = ArrheniusBM(A=(0.00106023,'m^3/(mol*s)'), n=3.03645, w0=(249000,'J/mol'), E0=(36913.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.7561257818317645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_3CS->S
    Total Standard Deviation in ln(k): 1.7432272762833005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 1.7432272762833005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_3CS->S
Total Standard Deviation in ln(k): 1.7432272762833005
""",
)

entry(
    index = 233,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_N-3CS->S",
    kinetics = ArrheniusBM(A=(0.000240974,'m^3/(mol*s)'), n=3.2319, w0=(249000,'J/mol'), E0=(34976.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7867662461474368e-15, var=0.24973797734199882, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_N-3CS->S
    Total Standard Deviation in ln(k): 1.0018421149744918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 1.0018421149744918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_Ext-4BrCClFINOPSSi-R_N-5R!H->S_N-5CO->O_Sp-5C-4BrCClFINOPSSi_4BrCClFINOPSSi->S_N-3R->H_N-3CS->S
Total Standard Deviation in ln(k): 1.0018421149744918
""",
)

entry(
    index = 234,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.36412e-05,'m^3/(mol*s)'), n=3.17809, w0=(272000,'J/mol'), E0=(49943.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018775013366061726, var=8.299059303874646, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 5.822431839722577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 5.822431839722577""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 5.822431839722577
""",
)

entry(
    index = 235,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(8.31698e-05,'m^3/(mol*s)'), n=3.00467, w0=(272000,'J/mol'), E0=(52246.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-16, var=3.9427479530334866, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 3.980672943000045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 3.980672943000045""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 3.980672943000045
""",
)

entry(
    index = 236,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.000715253,'m^3/(mol*s)'), n=2.79472, w0=(272000,'J/mol'), E0=(52049.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.8887373345443345e-16, var=5.961564668106701, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 4.894824431661662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 4.894824431661662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 4.894824431661662
""",
)

entry(
    index = 237,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(0.0046576,'m^3/(mol*s)'), n=2.32839, w0=(249000,'J/mol'), E0=(32672.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_4BrCClFINOPSSi->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-4BrCClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(4.22798e-05,'m^3/(mol*s)'), n=3.05049, w0=(272000,'J/mol'), E0=(56309.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-16, var=3.324258614563852, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-4BrCClFINOPSSi->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-4BrCClFINOPSSi->S
    Total Standard Deviation in ln(k): 3.6551431543224493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 3.6551431543224493""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_N-4BrCClFINOPSSi->S
Total Standard Deviation in ln(k): 3.6551431543224493
""",
)

entry(
    index = 239,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(3.43735e-05,'m^3/(mol*s)'), n=3.04343, w0=(272000,'J/mol'), E0=(52292.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0666212003633003e-15, var=49.791058369876545, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 14.145967902635721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 14.145967902635721""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 14.145967902635721
""",
)

entry(
    index = 240,
    label = "Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.000116203,'m^3/(mol*s)'), n=2.91849, w0=(272000,'J/mol'), E0=(50554,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360836e-16, var=3.4782038182257122, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 3.7388195349136355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 3.7388195349136355""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-2R->H_N-2CS->S_3R->H_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Ext-2C-R_Ext-2C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 3.7388195349136355
""",
)

