#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(114.345,'m^3/(mol*s)'), n=1.49417, w0=(570.117,'kJ/mol'), E0=(15.3163,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014071902696354032, var=2.2535225941554673, Tref=1000.0, N=261, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 261 training reactions at node Root
    Total Standard Deviation in ln(k): 3.044812190935231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.044812190935231""",
    longDesc = 
"""
BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.044812190935231
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(17.2361,'m^3/(mol*s)'), n=1.74177, w0=(569.306,'kJ/mol'), E0=(0.581852,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06887744459353408, var=3.8037698572079446, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 116 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 4.082945003031199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.082945003031199""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.082945003031199
""",
)

entry(
    index = 3,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(16.6503,'m^3/(mol*s)'), n=1.55608, w0=(549.943,'kJ/mol'), E0=(72.4225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06691716445657264, var=0.9690666179029853, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 35 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.141618471493909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.141618471493909""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.141618471493909
""",
)

entry(
    index = 4,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(788.677,'m^3/(mol*s)'), n=1.29375, w0=(577.391,'kJ/mol'), E0=(51.1839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05087153676234823, var=1.158518339434855, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 110 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 2.285604303943809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.285604303943809""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.285604303943809
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(21.776,'m^3/(mol*s)'), n=1.77675, w0=(568.731,'kJ/mol'), E0=(19.617,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028372937891844962, var=2.439874353731134, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 3.13854454831016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.13854454831016""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.13854454831016
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(777786,'m^3/(mol*s)'), n=-0.289496, w0=(570.583,'kJ/mol'), E0=(31.2567,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1881459702694794, var=5.276600412398765, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 7.590338657192336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.590338657192336""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.590338657192336
""",
)

entry(
    index = 7,
    label = "Root_4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(502138,'m^3/(mol*s)'), n=-0.0462845, w0=(537.647,'kJ/mol'), E0=(43.703,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05436843351861486, var=0.8667211938737663, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.002969603341029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.002969603341029""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.002969603341029
""",
)

entry(
    index = 8,
    label = "Root_4R->C_2R!H->C",
    kinetics = ArrheniusBM(A=(42.5674,'m^3/(mol*s)'), n=1.42312, w0=(560.045,'kJ/mol'), E0=(58.3505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5203513562340824, var=1.9619659651661965, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_2R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
    Total Standard Deviation in ln(k): 4.115451808961039"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 4.115451808961039""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 4.115451808961039
""",
)

entry(
    index = 9,
    label = "Root_4R->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(11.7894,'m^3/(mol*s)'), n=1.60471, w0=(563.929,'kJ/mol'), E0=(72.9639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.039360793943976846, var=1.334161008456657, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.4144835136097638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.4144835136097638""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.4144835136097638
""",
)

entry(
    index = 10,
    label = "Root_N-4R->C_4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(136.757,'m^3/(mol*s)'), n=1.34862, w0=(569.125,'kJ/mol'), E0=(45.3985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08880133839694762, var=0.34438168151540827, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.3995785205749087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.3995785205749087""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.3995785205749087
""",
)

entry(
    index = 11,
    label = "Root_N-4R->C_N-4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(1078.45,'m^3/(mol*s)'), n=1.29893, w0=(578.039,'kJ/mol'), E0=(42.7124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03691087024811249, var=0.6694907296644995, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N',), comment="""BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.7330634979708728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.7330634979708728""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.7330634979708728
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(927.382,'m^3/(mol*s)'), n=0.855533, w0=(542.539,'kJ/mol'), E0=(14.0861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2285102502962846, var=26.783078519437773, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R',), comment="""BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
    Total Standard Deviation in ln(k): 13.461688418739328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.461688418739328""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.461688418739328
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.10299e+14,'m^3/(mol*s)'), n=-2.59221, w0=(547.45,'kJ/mol'), E0=(97.6584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15685767132340672, var=2.824420520723321, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.7632750047347643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.7632750047347643""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.7632750047347643
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O",
    kinetics = ArrheniusBM(A=(12.4764,'m^3/(mol*s)'), n=1.90962, w0=(626.45,'kJ/mol'), E0=(5.88182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03726558617263095, var=0.707033449878994, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
    Total Standard Deviation in ln(k): 1.779319251333028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 1.779319251333028""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 1.779319251333028
""",
)

entry(
    index = 15,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O",
    kinetics = ArrheniusBM(A=(59.6637,'m^3/(mol*s)'), n=1.5802, w0=(597.409,'kJ/mol'), E0=(25.2477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4958466675864032, var=5.442975175454614, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
    Total Standard Deviation in ln(k): 5.922929858937989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 5.922929858937989""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 5.922929858937989
""",
)

entry(
    index = 16,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(872573,'m^3/(mol*s)'), n=-0.447227, w0=(569.967,'kJ/mol'), E0=(8.81926,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04586515146754451, var=7.306108763159307, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 5.534000816759298"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.534000816759298""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.534000816759298
""",
)

entry(
    index = 17,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(601990,'m^3/(mol*s)'), n=-0.252162, w0=(573.667,'kJ/mol'), E0=(56.6888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.07181190555409, var=7.753052480238043, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 10.787602783093513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 10.787602783093513""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 10.787602783093513
""",
)

entry(
    index = 18,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1",
    kinetics = ArrheniusBM(A=(463467,'m^3/(mol*s)'), n=-0.0491773, w0=(537.562,'kJ/mol'), E0=(32.2414,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031702797179893036, var=0.6271750550269313, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1',), comment="""BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
    Total Standard Deviation in ln(k): 1.6672928764579167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.6672928764579167""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.6672928764579167
""",
)

entry(
    index = 19,
    label = "Root_4R->C_Ext-1R!H-R_N-4C-u1",
    kinetics = Arrhenius(A=(1.81e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_4R->C_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.09946e+07,'m^3/(mol*s)'), n=-0.4, w0=(536.7,'kJ/mol'), E0=(51.3801,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4049817529935226e-09, var=3.9478985185588176, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.983272154668733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.983272154668733""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.983272154668733
""",
)

entry(
    index = 21,
    label = "Root_4R->C_2R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544,'kJ/mol'), E0=(60.2066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6327414716789567, var=1.1029778038569251, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
    Total Standard Deviation in ln(k): 3.695230603159588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 3.695230603159588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 3.695230603159588
""",
)

entry(
    index = 22,
    label = "Root_4R->C_2R!H->C_N-1R!H->N",
    kinetics = ArrheniusBM(A=(6.85584e+07,'m^3/(mol*s)'), n=-0.0487474, w0=(597.25,'kJ/mol'), E0=(78.8444,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.08604148246761, var=17.73650737761785, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 13.6841985144745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.6841985144745""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.6841985144745
""",
)

entry(
    index = 23,
    label = "Root_4R->C_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(112.108,'m^3/(mol*s)'), n=1.32982, w0=(553.333,'kJ/mol'), E0=(43.0961,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27629899179559614, var=1.5748785276237214, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 3.210044104385652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 3.210044104385652""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 3.210044104385652
""",
)

entry(
    index = 24,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.405661,'m^3/(mol*s)'), n=2.01996, w0=(571.875,'kJ/mol'), E0=(73.629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2513322757466883, var=1.0006094465131603, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.6368340037645503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.6368340037645503""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.6368340037645503
""",
)

entry(
    index = 25,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1",
    kinetics = ArrheniusBM(A=(124.61,'m^3/(mol*s)'), n=1.35269, w0=(577.357,'kJ/mol'), E0=(43.9953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06656793763388545, var=0.37225289199368317, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
    Total Standard Deviation in ln(k): 1.3903957321350946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.3903957321350946""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.3903957321350946
""",
)

entry(
    index = 26,
    label = "Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1",
    kinetics = Arrhenius(A=(1.8,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O",
    kinetics = ArrheniusBM(A=(369.642,'m^3/(mol*s)'), n=1.46442, w0=(674.25,'kJ/mol'), E0=(33.0357,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27034670298400953, var=1.788932884151972, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
    Total Standard Deviation in ln(k): 3.360616199294864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 3.360616199294864""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 3.360616199294864
""",
)

entry(
    index = 28,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1230.74,'m^3/(mol*s)'), n=1.27876, w0=(569.851,'kJ/mol'), E0=(43.8528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04061985987792457, var=0.7202835677848364, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O',), comment="""BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8034690167575957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8034690167575957""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8034690167575957
""",
)

entry(
    index = 29,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S",
    kinetics = Arrhenius(A=(4.65863e-05,'m^3/(mol*s)'), n=2.77, Ea=(3.4518,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=10.03440738040793, var=258.6597048583084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
    Total Standard Deviation in ln(k): 57.45403464381054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
Total Standard Deviation in ln(k): 57.45403464381054""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
Total Standard Deviation in ln(k): 57.45403464381054
""",
)

entry(
    index = 30,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(10877.4,'m^3/(mol*s)'), n=0.589799, w0=(543.403,'kJ/mol'), E0=(17.3348,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.7609350736937794, var=20.833044320444312, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
    Total Standard Deviation in ln(k): 16.087281192797743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 16.087281192797743""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 16.087281192797743
""",
)

entry(
    index = 31,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.43691e+07,'m^3/(mol*s)'), n=0.00213472, w0=(533.25,'kJ/mol'), E0=(70.5653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 32,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(6.59858e+09,'m^3/(mol*s)'), n=-1.27052, w0=(551,'kJ/mol'), E0=(75.2908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.047046405308611226, var=1.8255605882838954, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.8268709196220567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.8268709196220567""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.8268709196220567
""",
)

entry(
    index = 33,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(15.3304,'m^3/(mol*s)'), n=1.9099, w0=(626.125,'kJ/mol'), E0=(6.48613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28095356066626137, var=0.6266060910912323, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.2928307720928642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.2928307720928642""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.2928307720928642
""",
)

entry(
    index = 34,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7.45181,'m^3/(mol*s)'), n=1.90892, w0=(627.75,'kJ/mol'), E0=(60.6074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3054013179894528, var=0.5005020717835997, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 4.698176115914675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.698176115914675""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.698176115914675
""",
)

entry(
    index = 35,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N",
    kinetics = Arrhenius(A=(0.92,'m^3/(mol*s)'), n=1.94, Ea=(8.91192,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(26.9307,'m^3/(mol*s)'), n=1.7319, w0=(597.357,'kJ/mol'), E0=(3.38148,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8913527925375262, var=3.0867715687884476, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
    Total Standard Deviation in ln(k): 5.7617411338184805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 5.7617411338184805""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 5.7617411338184805
""",
)

entry(
    index = 37,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C",
    kinetics = Arrhenius(A=(1.9874e+07,'m^3/(mol*s)'), n=-0.859655, Ea=(5.40155,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.4941980004384667e-16, var=6.579479562083139, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 5.1422449519957105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 5.1422449519957105""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 5.1422449519957105
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = Arrhenius(A=(5.7209e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(875780,'m^3/(mol*s)'), n=0.0848555, w0=(551.5,'kJ/mol'), E0=(85.9373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04912622395878689, var=11.657066990368756, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.9680888713159455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.9680888713159455""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.9680888713159455
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N",
    kinetics = Arrhenius(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, Ea=(0.6276,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = Arrhenius(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, Ea=(13.849,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(9.08823e+06,'m^3/(mol*s)'), n=-0.455602, w0=(539,'kJ/mol'), E0=(75.3679,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02186076674118266, var=0.3402149380709907, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.2242473595066103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.2242473595066103""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.2242473595066103
""",
)

entry(
    index = 43,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.17609e+08,'m^3/(mol*s)'), n=-0.666002, w0=(527.5,'kJ/mol'), E0=(82.6584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06453965778288306, var=1.0045671039736606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.1714677232878796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.1714677232878796""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.1714677232878796
""",
)

entry(
    index = 44,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(65.219,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0194766152141867, var=0.8394590096019454, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
    Total Standard Deviation in ln(k): 1.8857145055341362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.8857145055341362""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.8857145055341362
""",
)

entry(
    index = 45,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N",
    kinetics = Arrhenius(A=(1.6,'m^3/(mol*s)'), n=1.87, Ea=(-2.63592,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N",
    kinetics = Arrhenius(A=(0.82,'m^3/(mol*s)'), n=1.87, Ea=(-4.64424,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C",
    kinetics = ArrheniusBM(A=(8.18048e+07,'m^3/(mol*s)'), n=-0.338981, w0=(539,'kJ/mol'), E0=(77.6785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=14.717775896447812, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
    Total Standard Deviation in ln(k): 7.690916252578897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916252578897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916252578897
""",
)

entry(
    index = 49,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(6.61168e+07,'m^3/(mol*s)'), n=1.10162e-07, w0=(655.5,'kJ/mol'), E0=(9.55855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.7507532944488107, var=36.13951493076956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
    Total Standard Deviation in ln(k): 21.475698718431726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718431726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718431726
""",
)

entry(
    index = 50,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C",
    kinetics = Arrhenius(A=(2.4,'m^3/(mol*s)'), n=1.87, Ea=(-4.64424,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(87.4311,'m^3/(mol*s)'), n=1.32982, w0=(547,'kJ/mol'), E0=(40.4604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0342155798062556, var=2.674370149116384, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
    Total Standard Deviation in ln(k): 5.876975439152881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 5.876975439152881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 5.876975439152881
""",
)

entry(
    index = 52,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(0.000279549,'m^3/(mol*s)'), n=2.9189, w0=(587.833,'kJ/mol'), E0=(52.6126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16136337268930884, var=0.634161987511495, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.001892121215636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.001892121215636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.001892121215636
""",
)

entry(
    index = 53,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1",
    kinetics = Arrhenius(A=(1.6,'m^3/(mol*s)'), n=1.87, Ea=(0.54392,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R",
    kinetics = Arrhenius(A=(1.8,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(141.823,'m^3/(mol*s)'), n=1.33331, w0=(581.125,'kJ/mol'), E0=(43.87,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11852140276515255, var=0.9725163470330533, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.274786893520754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.274786893520754""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.274786893520754
""",
)

entry(
    index = 56,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(591.25,'kJ/mol'), E0=(84.8231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9156671068834038, var=0.22709122189323483, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 3.2560093651328748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 3.2560093651328748""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 3.2560093651328748
""",
)

entry(
    index = 57,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl",
    kinetics = Arrhenius(A=(4e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(367.482,'m^3/(mol*s)'), n=1.46504, w0=(675.714,'kJ/mol'), E0=(27.1747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2493341844318142, var=1.6884268619991576, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.2314101471594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.2314101471594""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.2314101471594
""",
)

entry(
    index = 59,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(4.91196e+08,'m^3/(mol*s)'), n=-0.395719, w0=(551.367,'kJ/mol'), E0=(84.6239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10464632949023335, var=1.637663430329422, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 2.828414502884135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 2.828414502884135""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 2.828414502884135
""",
)

entry(
    index = 60,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(1222.19,'m^3/(mol*s)'), n=1.27971, w0=(573.361,'kJ/mol'), E0=(43.8496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040623678900907255, var=0.7195710084702719, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 1.802636822392288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.802636822392288""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.802636822392288
""",
)

entry(
    index = 61,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R",
    kinetics = Arrhenius(A=(644,'m^3/(mol*s)'), n=1.19, Ea=(2.13384,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O",
    kinetics = ArrheniusBM(A=(144382,'m^3/(mol*s)'), n=0.00520863, w0=(563,'kJ/mol'), E0=(52.2254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012859927794979813, var=0.2609081494203839, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
    Total Standard Deviation in ln(k): 1.0563133922917451"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.0563133922917451""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.0563133922917451
""",
)

entry(
    index = 63,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O",
    kinetics = ArrheniusBM(A=(9661,'m^3/(mol*s)'), n=0.617407, w0=(534.78,'kJ/mol'), E0=(22.3114,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.1486553644641257, var=20.01191625945876, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O',), comment="""BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
    Total Standard Deviation in ln(k): 16.87931267028296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 16.87931267028296""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 16.87931267028296
""",
)

entry(
    index = 64,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R",
    kinetics = ArrheniusBM(A=(1.10126e+11,'m^3/(mol*s)'), n=-1.57797, w0=(539,'kJ/mol'), E0=(72.6766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1550508870513327, var=7.888900482083563, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
    Total Standard Deviation in ln(k): 8.532874717066496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 8.532874717066496""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 8.532874717066496
""",
)

entry(
    index = 67,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C",
    kinetics = Arrhenius(A=(333333,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C",
    kinetics = ArrheniusBM(A=(173205,'m^3/(mol*s)'), n=-2.15017e-09, w0=(563,'kJ/mol'), E0=(48.9135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012693247883409827, var=0.888325353181433, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
    Total Standard Deviation in ln(k): 1.9213757095706525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9213757095706525""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9213757095706525
""",
)

entry(
    index = 69,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br",
    kinetics = Arrhenius(A=(3.33333e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(15.2824,'m^3/(mol*s)'), n=1.91038, w0=(621.929,'kJ/mol'), E0=(6.63571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31643116482463285, var=0.7582228429227088, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
    Total Standard Deviation in ln(k): 2.5406961389104965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 2.5406961389104965""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 2.5406961389104965
""",
)

entry(
    index = 71,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = Arrhenius(A=(0.014,'m^3/(mol*s)'), n=2.69, Ea=(-6.73624,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = Arrhenius(A=(0.014,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O",
    kinetics = Arrhenius(A=(292368,'m^3/(mol*s)'), n=0.463, Ea=(-1.34306,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.5085777080715174, var=0.3489022912286526, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 2.4619893836184943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.4619893836184943""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.4619893836184943
""",
)

entry(
    index = 74,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(146.419,'m^3/(mol*s)'), n=1.39942, w0=(554.864,'kJ/mol'), E0=(48.0295,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19947934681182802, var=0.4815992650452661, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8924374741437513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8924374741437513""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8924374741437513
""",
)

entry(
    index = 75,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R",
    kinetics = Arrhenius(A=(1.48985e+07,'m^3/(mol*s)'), n=-0.881364, Ea=(0.968976,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.0646230426113968e-15, var=4.651226332011816, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.32355239122137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.32355239122137""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.32355239122137
""",
)

entry(
    index = 76,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.63837e+15,'m^3/(mol*s)'), n=-3.19276, w0=(563,'kJ/mol'), E0=(48.8533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.421508258037305, var=20.346816805721687, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 10.101913890708353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.101913890708353""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.101913890708353
""",
)

entry(
    index = 77,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(240647,'m^3/(mol*s)'), n=0.318315, w0=(551.5,'kJ/mol'), E0=(95.3248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07555230606214904, var=13.917768878138517, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 7.668800058634606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.668800058634606""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.668800058634606
""",
)

entry(
    index = 78,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C",
    kinetics = Arrhenius(A=(300000,'m^3/(mol*s)'), n=0, Ea=(77.404,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(1.83989e+07,'m^3/(mol*s)'), n=-0.354252, w0=(539,'kJ/mol'), E0=(89.2538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6775105459389898, var=1.6347776925581186, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 4.26551050568189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.26551050568189""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.26551050568189
""",
)

entry(
    index = 80,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.04475e+06,'m^3/(mol*s)'), n=-0.517587, w0=(539,'kJ/mol'), E0=(63.0042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012010946129419754, var=0.13827911084152764, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 0.7756570241670969"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7756570241670969""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7756570241670969
""",
)

entry(
    index = 81,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = Arrhenius(A=(3e+06,'m^3/(mol*s)'), n=0, Ea=(12.552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = Arrhenius(A=(5e+06,'m^3/(mol*s)'), n=0, Ea=(8.368,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(64.3571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 84,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1",
    kinetics = Arrhenius(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1",
    kinetics = Arrhenius(A=(3.01e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1",
    kinetics = Arrhenius(A=(8.49e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1",
    kinetics = Arrhenius(A=(1.21e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R",
    kinetics = Arrhenius(A=(1.6,'m^3/(mol*s)'), n=1.87, Ea=(-4.64424,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N",
    kinetics = ArrheniusBM(A=(9.98847e-05,'m^3/(mol*s)'), n=3.03309, w0=(562.75,'kJ/mol'), E0=(43.0213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9786870550842044, var=0.04968705417484676, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N
    Total Standard Deviation in ln(k): 2.9058800405005876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N
Total Standard Deviation in ln(k): 2.9058800405005876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N
Total Standard Deviation in ln(k): 2.9058800405005876
""",
)

entry(
    index = 90,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N",
    kinetics = Arrhenius(A=(1.6,'m^3/(mol*s)'), n=1.87, Ea=(8.7864,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(550.25,'kJ/mol'), E0=(0.117054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7132564079598208, var=4.493222864552059, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 6.041583288013453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 6.041583288013453""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 6.041583288013453
""",
)

entry(
    index = 92,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(1271.49,'m^3/(mol*s)'), n=1.08195, w0=(612,'kJ/mol'), E0=(52.0386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8475141618169849, var=0.3237805768286674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 3.270161313026353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.270161313026353""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.270161313026353
""",
)

entry(
    index = 93,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = Arrhenius(A=(0.92,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = Arrhenius(A=(0.92,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N",
    kinetics = ArrheniusBM(A=(332.977,'m^3/(mol*s)'), n=1.47687, w0=(657.5,'kJ/mol'), E0=(41.4376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017984131532875182, var=0.8031311711859094, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N
    Total Standard Deviation in ln(k): 1.841781441225873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N
Total Standard Deviation in ln(k): 1.841781441225873""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N
Total Standard Deviation in ln(k): 1.841781441225873
""",
)

entry(
    index = 96,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N",
    kinetics = ArrheniusBM(A=(7.34947e+07,'m^3/(mol*s)'), n=5.14994e-08, w0=(689.375,'kJ/mol'), E0=(56.2996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.080045040011711, var=3.36332195945171, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N
    Total Standard Deviation in ln(k): 6.390237220567182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N
Total Standard Deviation in ln(k): 6.390237220567182""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N
Total Standard Deviation in ln(k): 6.390237220567182
""",
)

entry(
    index = 97,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.40573e+07,'m^3/(mol*s)'), n=-0.057296, w0=(545.2,'kJ/mol'), E0=(62.8134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.049026102696637326, var=1.168136114539103, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.2899057663109184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.2899057663109184""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.2899057663109184
""",
)

entry(
    index = 98,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2.15445e+07,'m^3/(mol*s)'), n=-1.05297e-06, w0=(543.667,'kJ/mol'), E0=(26.6365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03213824649816105, var=4.201524170253009, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 4.189979102523637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 4.189979102523637""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 4.189979102523637
""",
)

entry(
    index = 99,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C",
    kinetics = Arrhenius(A=(6e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C",
    kinetics = Arrhenius(A=(1.33333e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(740.831,'m^3/(mol*s)'), n=1.33202, w0=(572.735,'kJ/mol'), E0=(39.2558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.039020418962707595, var=0.9139756611084066, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1',), comment="""BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
    Total Standard Deviation in ln(k): 2.0146095719487938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 2.0146095719487938""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 2.0146095719487938
""",
)

entry(
    index = 102,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(5237.05,'m^3/(mol*s)'), n=1.12116, w0=(576.538,'kJ/mol'), E0=(53.8055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.058569379337753844, var=0.354704161507858, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 1.3411202177424575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.3411202177424575""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.3411202177424575
""",
)

entry(
    index = 103,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-3.66776e-08, w0=(563,'kJ/mol'), E0=(39.4544,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04830224167320565, var=0.011665533185035404, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.3378880339230098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.3378880339230098""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.3378880339230098
""",
)

entry(
    index = 104,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.43889e+08,'m^3/(mol*s)'), n=-0.818569, w0=(563,'kJ/mol'), E0=(68.2438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02223373898509248, var=0.49128437348381154, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.4610161796226309"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4610161796226309""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4610161796226309
""",
)

entry(
    index = 105,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(20257.8,'m^3/(mol*s)'), n=0.566193, w0=(539,'kJ/mol'), E0=(82.0813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34931669112273933, var=8.019579645315076, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 6.554861797999056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.554861797999056""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.554861797999056
""",
)

entry(
    index = 106,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(14342.3,'m^3/(mol*s)'), n=0.567352, w0=(533.725,'kJ/mol'), E0=(21.8745,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.3666768138340797, var=21.797729251063497, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 17.818701787219553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 17.818701787219553""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 17.818701787219553
""",
)

entry(
    index = 107,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R",
    kinetics = Arrhenius(A=(50000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(173205,'m^3/(mol*s)'), n=3.86886e-08, w0=(563,'kJ/mol'), E0=(48.0313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 110,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C",
    kinetics = Arrhenius(A=(1.21e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C",
    kinetics = ArrheniusBM(A=(15.2296,'m^3/(mol*s)'), n=1.91087, w0=(612.333,'kJ/mol'), E0=(6.37774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31517745860094626, var=0.7532270030947089, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
    Total Standard Deviation in ln(k): 2.5317857023348997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 2.5317857023348997""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 2.5317857023348997
""",
)

entry(
    index = 112,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(16.4899,'m^3/(mol*s)'), n=1.89829, w0=(646,'kJ/mol'), E0=(13.7415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6779368755822698, var=1.3357464456460317, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 4.020321474399072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 4.020321474399072""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 4.020321474399072
""",
)

entry(
    index = 113,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(8.061,'m^3/(mol*s)'), n=1.89922, w0=(641.25,'kJ/mol'), E0=(15.1022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4335652126640468, var=7.684834775066688, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 9.159355914956995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 9.159355914956995""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 9.159355914956995
""",
)

entry(
    index = 114,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O",
    kinetics = Arrhenius(A=(2.41e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O",
    kinetics = ArrheniusBM(A=(144.21,'m^3/(mol*s)'), n=1.4012, w0=(547.2,'kJ/mol'), E0=(47.9562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.127153862953604, var=0.18128597243860048, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
    Total Standard Deviation in ln(k): 1.1730519633957504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.1730519633957504""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.1730519633957504
""",
)

entry(
    index = 116,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.59376,'m^3/(mol*s)'), n=1.13083, w0=(563,'kJ/mol'), E0=(7.22219,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2345187937662739, var=1.6749215895033598, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 3.1837465141141634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 3.1837465141141634""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 3.1837465141141634
""",
)

entry(
    index = 117,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = Arrhenius(A=(1.05224e+09,'m^3/(mol*s)'), n=-1.49154, Ea=(-7.50062,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-6.954975193530339e-17, var=4.463830581201113, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 4.2355600268756985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.2355600268756985""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.2355600268756985
""",
)

entry(
    index = 118,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C",
    kinetics = Arrhenius(A=(7.23e+06,'m^3/(mol*s)'), n=0, Ea=(92.048,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.76105e+09,'m^3/(mol*s)'), n=-1.65753, w0=(563,'kJ/mol'), E0=(6.86482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02269164371212678, var=16.245364745716824, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 8.137206966060432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.137206966060432""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.137206966060432
""",
)

entry(
    index = 120,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R",
    kinetics = Arrhenius(A=(300000,'m^3/(mol*s)'), n=0, Ea=(71.128,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(8.32046e+06,'m^3/(mol*s)'), n=-0.32, w0=(539,'kJ/mol'), E0=(51.4404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.8378904353806438, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
    Total Standard Deviation in ln(k): 1.8350614246030303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.8350614246030303""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.8350614246030303
""",
)

entry(
    index = 122,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H",
    kinetics = Arrhenius(A=(3.01e+06,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(55.6026,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0345300728262653, var=0.005961629646936012, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.2415477600203948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.2415477600203948""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.2415477600203948
""",
)

entry(
    index = 124,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(62.7695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008691273185662204, var=0.3822595522753264, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2613077784899787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2613077784899787""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2613077784899787
""",
)

entry(
    index = 125,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N",
    kinetics = Arrhenius(A=(0.82,'m^3/(mol*s)'), n=1.87, Ea=(7.61488,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N",
    kinetics = Arrhenius(A=(1.6,'m^3/(mol*s)'), n=1.87, Ea=(12.3846,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N",
    kinetics = Arrhenius(A=(0.46,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N",
    kinetics = Arrhenius(A=(1.8,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N",
    kinetics = Arrhenius(A=(1.8,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N",
    kinetics = Arrhenius(A=(0.92,'m^3/(mol*s)'), n=1.94, Ea=(-4.8116,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->H",
    kinetics = Arrhenius(A=(480,'m^3/(mol*s)'), n=1.5, Ea=(1.58992,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_4BrFHO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H",
    kinetics = ArrheniusBM(A=(583.069,'m^3/(mol*s)'), n=1.37285, w0=(662,'kJ/mol'), E0=(21.4729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5478125776741563, var=4.025579899746094, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H
    Total Standard Deviation in ln(k): 5.398683466119156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H
Total Standard Deviation in ln(k): 5.398683466119156""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H
Total Standard Deviation in ln(k): 5.398683466119156
""",
)

entry(
    index = 133,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(5.06939e+07,'m^3/(mol*s)'), n=-0.0911781, w0=(692.667,'kJ/mol'), E0=(85.1031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.095365765509729, var=0.07908624829546873, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1
    Total Standard Deviation in ln(k): 0.8033896346115963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1
Total Standard Deviation in ln(k): 0.8033896346115963""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1
Total Standard Deviation in ln(k): 0.8033896346115963
""",
)

entry(
    index = 134,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1",
    kinetics = Arrhenius(A=(9.04e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O",
    kinetics = Arrhenius(A=(3.66667e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(7.32757e+08,'m^3/(mol*s)'), n=-0.568754, w0=(544.944,'kJ/mol'), E0=(77.4793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11555420608562446, var=0.9541728389170934, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.2485979290335103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.2485979290335103""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.2485979290335103
""",
)

entry(
    index = 137,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.59918e-09, w0=(547.5,'kJ/mol'), E0=(67.3436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 138,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN",
    kinetics = Arrhenius(A=(1e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(1.52545e+07,'m^3/(mol*s)'), n=0.00167319, w0=(619.889,'kJ/mol'), E0=(101.585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06985593625953757, var=0.3108745548490395, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 1.2932800366675852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.2932800366675852""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.2932800366675852
""",
)

entry(
    index = 140,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(736.578,'m^3/(mol*s)'), n=1.3328, w0=(565.289,'kJ/mol'), E0=(38.2534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03902956129507376, var=0.91413145926253, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 2.0147958867434452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 2.0147958867434452""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 2.0147958867434452
""",
)

entry(
    index = 141,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(18289.5,'m^3/(mol*s)'), n=0.994152, w0=(572.25,'kJ/mol'), E0=(64.3797,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0781776540940957, var=0.43866354313984113, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.5241959872362454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.5241959872362454""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.5241959872362454
""",
)

entry(
    index = 142,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5519.78,'m^3/(mol*s)'), n=1.06696, w0=(583.4,'kJ/mol'), E0=(66.1438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040833600365106505, var=0.00046406628051178775, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.1457833851579023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.1457833851579023""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.1457833851579023
""",
)

entry(
    index = 143,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=7.27917e-10, w0=(563,'kJ/mol'), E0=(38.5348,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05755734047414289, var=0.009938542396485315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.3444729606093259"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.3444729606093259""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.3444729606093259
""",
)

entry(
    index = 144,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(141421,'m^3/(mol*s)'), n=-7.99721e-09, w0=(563,'kJ/mol'), E0=(45.2129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 145,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R",
    kinetics = Arrhenius(A=(84300,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(279022,'m^3/(mol*s)'), n=0.46279, w0=(539,'kJ/mol'), E0=(82.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.079560686398513, var=8.050357758251643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
    Total Standard Deviation in ln(k): 5.887966604807892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 5.887966604807892""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 5.887966604807892
""",
)

entry(
    index = 147,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = Arrhenius(A=(964000,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = Arrhenius(A=(2.41e+06,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C",
    kinetics = ArrheniusBM(A=(27604.4,'m^3/(mol*s)'), n=0.515881, w0=(537.029,'kJ/mol'), E0=(26.601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42036323818648824, var=0.6132459835559247, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
    Total Standard Deviation in ln(k): 2.626097557928205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.626097557928205""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.626097557928205
""",
)

entry(
    index = 150,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C",
    kinetics = ArrheniusBM(A=(6.41947,'m^3/(mol*s)'), n=1.17357, w0=(515,'kJ/mol'), E0=(46.4605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.526667037500865, var=35.54334886128459, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
    Total Standard Deviation in ln(k): 20.812850734858937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 20.812850734858937""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 20.812850734858937
""",
)

entry(
    index = 151,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C",
    kinetics = Arrhenius(A=(8.03333e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(15.1785,'m^3/(mol*s)'), n=1.91136, w0=(603.7,'kJ/mol'), E0=(5.98267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3031286772711573, var=0.7071363768385572, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.4474396608211317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.4474396608211317""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.4474396608211317
""",
)

entry(
    index = 153,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R",
    kinetics = Arrhenius(A=(1.81e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(15.3833,'m^3/(mol*s)'), n=1.90892, w0=(627,'kJ/mol'), E0=(12.6991,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.148638264042989, var=11.557858500679005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
    Total Standard Deviation in ln(k): 19.751744935290038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 19.751744935290038""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 19.751744935290038
""",
)

entry(
    index = 155,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(8.60156e+07,'m^3/(mol*s)'), n=-0.489747, w0=(655.5,'kJ/mol'), E0=(78.3738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0178154319487774, var=0.0357176626280382, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 0.4236396211863206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 0.4236396211863206""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 0.4236396211863206
""",
)

entry(
    index = 156,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O",
    kinetics = Arrhenius(A=(1.81e+08,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(7.88926,'m^3/(mol*s)'), n=1.90164, w0=(636.5,'kJ/mol'), E0=(9.38302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3913619153736603, var=1.1022533966913421, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 8.11318342531521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 8.11318342531521""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O
Total Standard Deviation in ln(k): 8.11318342531521
""",
)

entry(
    index = 158,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS",
    kinetics = Arrhenius(A=(3.61e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS",
    kinetics = ArrheniusBM(A=(142.376,'m^3/(mol*s)'), n=1.40297, w0=(548.111,'kJ/mol'), E0=(47.9515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25226111593981626, var=0.23799232895955677, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 1.6118210303487266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.6118210303487266""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.6118210303487266
""",
)

entry(
    index = 160,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C",
    kinetics = ArrheniusBM(A=(214739,'m^3/(mol*s)'), n=-0.283413, w0=(563,'kJ/mol'), E0=(39.3473,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07064047807972207, var=0.3065378621305859, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
    Total Standard Deviation in ln(k): 1.28742748508532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.28742748508532""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.28742748508532
""",
)

entry(
    index = 161,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C",
    kinetics = Arrhenius(A=(602200,'m^3/(mol*s)'), n=0, Ea=(56.6932,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R",
    kinetics = Arrhenius(A=(3.58117e+09,'m^3/(mol*s)'), n=-1.73125, Ea=(-7.06835,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.5069112919315733e-15, var=2.628361496766517, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.250121058957103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.250121058957103""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.250121058957103
""",
)

entry(
    index = 163,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(6.16313e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(3.63381,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13425847588306006, var=16.351560954538137, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 8.44389279407243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 8.44389279407243""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 8.44389279407243
""",
)

entry(
    index = 164,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C",
    kinetics = Arrhenius(A=(300000,'m^3/(mol*s)'), n=0, Ea=(7.7655,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFILiNOPSSi->Cl",
    kinetics = Arrhenius(A=(250000,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFILiNOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFILiNOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl",
    kinetics = ArrheniusBM(A=(4.23154e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(5.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1342584977368451, var=21.205889827508237, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl
    Total Standard Deviation in ln(k): 9.569108517325883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 9.569108517325883""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl
Total Standard Deviation in ln(k): 9.569108517325883
""",
)

entry(
    index = 167,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R",
    kinetics = Arrhenius(A=(6.02e+06,'m^3/(mol*s)'), n=-0.32, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(56.9108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.041149340162468656, var=0.005079804587419779, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.24627327961161904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.24627327961161904""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.24627327961161904
""",
)

entry(
    index = 169,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(61.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 170,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_4FO-u1",
    kinetics = Arrhenius(A=(2.4,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_4FO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_4FO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_4FO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_4FO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_N-4FO-u1",
    kinetics = Arrhenius(A=(330,'m^3/(mol*s)'), n=1.5, Ea=(-1.50624,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_N-4FO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_N-4FO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_N-4FO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->N_N-4BrFHO->H_N-4FO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F",
    kinetics = Arrhenius(A=(3e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(4.36325e+07,'m^3/(mol*s)'), n=-0.0854631, w0=(672.75,'kJ/mol'), E0=(81.548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07943523273796656, var=0.022916978970634327, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 0.5030699231409677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.5030699231409677""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.5030699231409677
""",
)

entry(
    index = 174,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.10064e+07,'m^3/(mol*s)'), n=4.06143e-08, w0=(547.5,'kJ/mol'), E0=(50.54,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.55881087024917e-08, var=0.694426533139768, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.6705911093210883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705911093210883""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705911093210883
""",
)

entry(
    index = 175,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(7.53121e+06,'m^3/(mol*s)'), n=0.00112828, w0=(547.5,'kJ/mol'), E0=(67.1967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0018952128342636279, var=1.4349655925688098, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 2.406234980041198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.406234980041198""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.406234980041198
""",
)

entry(
    index = 176,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(3.91761e+12,'m^3/(mol*s)'), n=-1.70261, w0=(536,'kJ/mol'), E0=(90.6112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360836e-16, var=5.180580787960471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.56295530433249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.56295530433249""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.56295530433249
""",
)

entry(
    index = 177,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(4.1033e+09,'m^3/(mol*s)'), n=-0.719949, w0=(608.333,'kJ/mol'), E0=(111.037,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26661855681451446, var=0.5124757374881537, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.105033805275586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.105033805275586""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.105033805275586
""",
)

entry(
    index = 179,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.16525e+07,'m^3/(mol*s)'), n=0.00067734, w0=(612.167,'kJ/mol'), E0=(101.585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14205424537658834, var=1.046653045284202, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.4078857385532944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4078857385532944""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4078857385532944
""",
)

entry(
    index = 180,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=-7.04437e-09, w0=(604.5,'kJ/mol'), E0=(97.911,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 181,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2007.91,'m^3/(mol*s)'), n=1.24075, w0=(556.26,'kJ/mol'), E0=(5.97461,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021361461246596245, var=5.703792089777163, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.841503237393601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.841503237393601""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.841503237393601
""",
)

entry(
    index = 183,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(4.06592e+14,'m^3/(mol*s)'), n=-2.17794, w0=(558.273,'kJ/mol'), E0=(133.489,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27054413914204295, var=0.5819245550779502, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.209050841988004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.209050841988004""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.209050841988004
""",
)

entry(
    index = 184,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H",
    kinetics = ArrheniusBM(A=(8924.88,'m^3/(mol*s)'), n=1.09658, w0=(578.65,'kJ/mol'), E0=(68.2331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0024860410138958992, var=0.3457223651196158, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
    Total Standard Deviation in ln(k): 1.184993678011032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.184993678011032""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.184993678011032
""",
)

entry(
    index = 185,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(188.44,'m^3/(mol*s)'), n=1.42021, w0=(580.682,'kJ/mol'), E0=(50.8228,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07554383262331116, var=0.4958479860453128, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.6014723863213642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.6014723863213642""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.6014723863213642
""",
)

entry(
    index = 186,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(7858.44,'m^3/(mol*s)'), n=1.08489, w0=(574.75,'kJ/mol'), E0=(59.546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21734593500663904, var=0.4864433163807869, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.9443075866164823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.9443075866164823""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.9443075866164823
""",
)

entry(
    index = 187,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(16838.4,'m^3/(mol*s)'), n=1.06173, w0=(569.75,'kJ/mol'), E0=(74.7658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1056913849963954, var=0.21306240465439347, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 1.1909155596425742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 1.1909155596425742""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 1.1909155596425742
""",
)

entry(
    index = 188,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.53564e+07,'m^3/(mol*s)'), n=-3.65929e-06, w0=(551.5,'kJ/mol'), E0=(91.1448,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.202693327970796, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.987000417702588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.987000417702588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.987000417702588
""",
)

entry(
    index = 189,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(621.5,'kJ/mol'), E0=(89.998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5802692593018619, var=0.03506183960602674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.8333457365700663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.8333457365700663""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.8333457365700663
""",
)

entry(
    index = 190,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N",
    kinetics = Arrhenius(A=(170,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(100000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R",
    kinetics = Arrhenius(A=(2.89e+07,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-1.37111e-09, w0=(539,'kJ/mol'), E0=(96.0238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 194,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C",
    kinetics = Arrhenius(A=(445757,'m^3/(mol*s)'), n=0.106667, Ea=(-0.516863,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.2394789325394425, var=0.22466768689009325, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 1.5519327074451308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.5519327074451308""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.5519327074451308
""",
)

entry(
    index = 195,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515,'kJ/mol'), E0=(49.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31790119796116745, var=0.0033834799613936027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.9153575336382757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.9153575336382757""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.9153575336382757
""",
)

entry(
    index = 196,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573.833,'kJ/mol'), E0=(26.301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1493927707451135, var=0.14941967970344067, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N
    Total Standard Deviation in ln(k): 1.1502858937765923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N
Total Standard Deviation in ln(k): 1.1502858937765923""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N
Total Standard Deviation in ln(k): 1.1502858937765923
""",
)

entry(
    index = 197,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N",
    kinetics = ArrheniusBM(A=(15.241,'m^3/(mol*s)'), n=1.91136, w0=(648.5,'kJ/mol'), E0=(6.51971,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.107478462379262, var=3.3211308061353755, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N
    Total Standard Deviation in ln(k): 8.948595196155114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 8.948595196155114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 8.948595196155114
""",
)

entry(
    index = 198,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C",
    kinetics = Arrhenius(A=(4.82e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C",
    kinetics = Arrhenius(A=(0.029,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.88102e+07,'m^3/(mol*s)'), n=-0.373812, w0=(655.5,'kJ/mol'), E0=(71.6801,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.534556459657866e-17, var=0.06912283083491368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693322083507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083507""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083507
""",
)

entry(
    index = 201,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C",
    kinetics = ArrheniusBM(A=(1.90316e+07,'m^3/(mol*s)'), n=1.01874e-07, w0=(655.5,'kJ/mol'), E0=(63.9336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14792259994922297, var=2.26745835923828, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C
    Total Standard Deviation in ln(k): 3.3904113583707383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 3.3904113583707383""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C
Total Standard Deviation in ln(k): 3.3904113583707383
""",
)

entry(
    index = 202,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C",
    kinetics = Arrhenius(A=(0.014,'m^3/(mol*s)'), n=2.69, Ea=(-6.73624,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S",
    kinetics = Arrhenius(A=(979000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S",
    kinetics = ArrheniusBM(A=(139.694,'m^3/(mol*s)'), n=1.40572, w0=(549.438,'kJ/mol'), E0=(40.3988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17482245265236634, var=0.1090098185438215, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
    Total Standard Deviation in ln(k): 1.1011484564289769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.1011484564289769""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.1011484564289769
""",
)

entry(
    index = 205,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=2.51744e-08, w0=(563,'kJ/mol'), E0=(20.958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004726808059886787, var=2.9790285836160006e-05, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
    Total Standard Deviation in ln(k): 0.02281834204828608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 0.02281834204828608""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 0.02281834204828608
""",
)

entry(
    index = 206,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=-4.0411e-09, w0=(563,'kJ/mol'), E0=(19.4136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.5272805777722495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495
""",
)

entry(
    index = 207,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R",
    kinetics = Arrhenius(A=(2.62907e+08,'m^3/(mol*s)'), n=-1.385, Ea=(-12.1817,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360836e-16, var=3.6099107664394032, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.8089495705345158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.8089495705345158""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.8089495705345158
""",
)

entry(
    index = 208,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.63887e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(5.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.00421011414115, var=9.457635837855566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.688356797663342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.688356797663342""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.688356797663342
""",
)

entry(
    index = 209,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.32925e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(1.68921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1076607117836883, var=26.82573783154405, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 13.166305558028174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 13.166305558028174""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 13.166305558028174
""",
)

entry(
    index = 210,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.23154e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(5.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3603544400804772, var=40.84205681236206, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 16.22979490511209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.22979490511209""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFILiNOPSSi->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.22979490511209
""",
)

entry(
    index = 211,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->H",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->H",
    kinetics = Arrhenius(A=(2.41e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->N_4BrFHO-u1_N-4BrFHO->F_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.88785e-07, w0=(547.5,'kJ/mol'), E0=(45.6403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 215,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.32866e-07, w0=(547.5,'kJ/mol'), E0=(49.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 216,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = Arrhenius(A=(2e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(4.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(4.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1.46191e+07,'m^3/(mol*s)'), n=0.00442141, w0=(616,'kJ/mol'), E0=(101.585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 221,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = Arrhenius(A=(5e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(50272.6,'m^3/(mol*s)'), n=0.749628, w0=(561.071,'kJ/mol'), E0=(87.8601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06615542379335865, var=0.3641763719922233, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.3760176848734766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.3760176848734766""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.3760176848734766
""",
)

entry(
    index = 223,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(2007.44,'m^3/(mol*s)'), n=1.24159, w0=(550.136,'kJ/mol'), E0=(41.5362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01412063779095612, var=5.932756175028661, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.918462294412191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.918462294412191""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.918462294412191
""",
)

entry(
    index = 224,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN",
    kinetics = ArrheniusBM(A=(5.22263e+12,'m^3/(mol*s)'), n=-1.62956, w0=(557.8,'kJ/mol'), E0=(124.965,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20052054760253252, var=0.4977846371801274, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 1.9182383391305022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 1.9182383391305022""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 1.9182383391305022
""",
)

entry(
    index = 225,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN",
    kinetics = Arrhenius(A=(6.03e+06,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(52087.9,'m^3/(mol*s)'), n=0.904964, w0=(573.286,'kJ/mol'), E0=(75.1809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004922182644202237, var=0.39030380380174096, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.2648114798822403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.2648114798822403""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.2648114798822403
""",
)

entry(
    index = 227,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(591.167,'kJ/mol'), E0=(81.9113,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.089696339125849, var=0.051276531436941074, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.6793263504391293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.6793263504391293""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.6793263504391293
""",
)

entry(
    index = 228,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(219.201,'m^3/(mol*s)'), n=1.43236, w0=(571.688,'kJ/mol'), E0=(60.417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20552615990759934, var=0.6561650465910014, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 2.1403132919539636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.1403132919539636""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.1403132919539636
""",
)

entry(
    index = 229,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(604.667,'kJ/mol'), E0=(94.6186,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.061855717510470004, var=0.0408779444982319, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.5607396237407745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.5607396237407745""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.5607396237407745
""",
)

entry(
    index = 230,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C",
    kinetics = Arrhenius(A=(330,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2306.38,'m^3/(mol*s)'), n=1.23055, w0=(573.833,'kJ/mol'), E0=(52.6412,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3563496110844976, var=0.9591439277072575, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 2.858705996213457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 2.858705996213457""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 2.858705996213457
""",
)

entry(
    index = 232,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73205e+07,'m^3/(mol*s)'), n=-3.49549e-08, w0=(563,'kJ/mol'), E0=(42.9189,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-17, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 233,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R",
    kinetics = Arrhenius(A=(3e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = Arrhenius(A=(170,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = Arrhenius(A=(170,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R",
    kinetics = Arrhenius(A=(6.03e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(340826,'m^3/(mol*s)'), n=-4.17997e-08, w0=(539,'kJ/mol'), E0=(49.3909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 238,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(25585.2,'m^3/(mol*s)'), n=0.525802, w0=(536.423,'kJ/mol'), E0=(7.10202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3912222686341234, var=0.2691759508063824, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
    Total Standard Deviation in ln(k): 2.0230705743202844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.0230705743202844""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.0230705743202844
""",
)

entry(
    index = 239,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R",
    kinetics = Arrhenius(A=(763000,'m^3/(mol*s)'), n=0, Ea=(-2.3012,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548,'kJ/mol'), E0=(42.2214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6517157604447155, var=1.4333460049661602, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N
    Total Standard Deviation in ln(k): 6.550157132462611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N
Total Standard Deviation in ln(k): 6.550157132462611""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N
Total Standard Deviation in ln(k): 6.550157132462611
""",
)

entry(
    index = 241,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N",
    kinetics = Arrhenius(A=(0.029,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N",
    kinetics = Arrhenius(A=(0.0294,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N",
    kinetics = Arrhenius(A=(0.029,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = Arrhenius(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5CS=4CCNSS",
    kinetics = Arrhenius(A=(3.01e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5CS=4CCNSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5CS=4CCNSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5CS=4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_Sp-5CS=4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5CS=4CCNSS",
    kinetics = Arrhenius(A=(1.20333e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5CS=4CCNSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5CS=4CCNSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5CS=4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->O_2R!H->C_N-Sp-5CS=4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(127.638,'m^3/(mol*s)'), n=1.41908, w0=(593.5,'kJ/mol'), E0=(58.4203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2786278929612728, var=0.6716860743959365, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
    Total Standard Deviation in ln(k): 2.3430799122511248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
Total Standard Deviation in ln(k): 2.3430799122511248""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
Total Standard Deviation in ln(k): 2.3430799122511248
""",
)

entry(
    index = 248,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(1.38436e+07,'m^3/(mol*s)'), n=-0.304179, w0=(534.75,'kJ/mol'), E0=(29.1578,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1561219854084911, var=0.24938097352307353, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 1.393392080446586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.393392080446586""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.393392080446586
""",
)

entry(
    index = 249,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-5.54694e-10, w0=(563,'kJ/mol'), E0=(21.1323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 250,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(2.62907e+08,'m^3/(mol*s)'), n=-1.385, Ea=(-12.1817,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=6.8887373345443345e-16, var=12.18344883673298, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.9974871778520145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.9974871778520145""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.9974871778520145
""",
)

entry(
    index = 251,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H",
    kinetics = ArrheniusBM(A=(4.47385e+06,'m^3/(mol*s)'), n=5.19133e-05, w0=(549.5,'kJ/mol'), E0=(68.1314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360836e-16, var=5.180580787960471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H
    Total Standard Deviation in ln(k): 4.56295530433249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H
Total Standard Deviation in ln(k): 4.56295530433249""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H
Total Standard Deviation in ln(k): 4.56295530433249
""",
)

entry(
    index = 255,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(1.73231e+06,'m^3/(mol*s)'), n=0.341032, w0=(563,'kJ/mol'), E0=(103.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012210846136371887, var=0.23744948224324192, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.0075636324945996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H
Total Standard Deviation in ln(k): 1.0075636324945996""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H
Total Standard Deviation in ln(k): 1.0075636324945996
""",
)

entry(
    index = 256,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.53553e+06,'m^3/(mol*s)'), n=1.10189e-07, w0=(551.5,'kJ/mol'), E0=(49.3379,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 257,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1988.48,'m^3/(mol*s)'), n=1.24316, w0=(549.833,'kJ/mol'), E0=(40.9929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04047112068514121, var=5.781941309870041, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.922205565325282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.922205565325282""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.922205565325282
""",
)

entry(
    index = 258,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H",
    kinetics = ArrheniusBM(A=(1.48466e+06,'m^3/(mol*s)'), n=2.93844e-08, w0=(549.5,'kJ/mol'), E0=(53.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.5879582258502154e-08, var=0.4209386825786314, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H
    Total Standard Deviation in ln(k): 1.3006679482609889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H
Total Standard Deviation in ln(k): 1.3006679482609889""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H
Total Standard Deviation in ln(k): 1.3006679482609889
""",
)

entry(
    index = 259,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(3.98669e+08,'m^3/(mol*s)'), n=-0.344453, w0=(561.357,'kJ/mol'), E0=(112.909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07765333983742352, var=0.23666232030374607, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.1703714459044403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H
Total Standard Deviation in ln(k): 1.1703714459044403""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H
Total Standard Deviation in ln(k): 1.1703714459044403
""",
)

entry(
    index = 260,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1",
    kinetics = ArrheniusBM(A=(98381.1,'m^3/(mol*s)'), n=0.822879, w0=(579.75,'kJ/mol'), E0=(76.2551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16279028617007202, var=0.774798350754046, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
    Total Standard Deviation in ln(k): 2.1736413723216335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 2.1736413723216335""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 2.1736413723216335
""",
)

entry(
    index = 261,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1",
    kinetics = Arrhenius(A=(480,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(608,'kJ/mol'), E0=(91.1223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5760190308689298, var=0.03284697304998707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.8106168479970777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.8106168479970777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.8106168479970777
""",
)

entry(
    index = 263,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N",
    kinetics = Arrhenius(A=(240,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(211.933,'m^3/(mol*s)'), n=1.42089, w0=(574.75,'kJ/mol'), E0=(54.2907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21182995306512284, var=0.6623850206003079, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 2.1638305932017157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 2.1638305932017157""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 2.1638305932017157
""",
)

entry(
    index = 265,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N",
    kinetics = ArrheniusBM(A=(397.042,'m^3/(mol*s)'), n=1.41411, w0=(568.625,'kJ/mol'), E0=(73.0592,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5035087457950456, var=2.2032551466583294, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 6.753361817072652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 6.753361817072652""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 6.753361817072652
""",
)

entry(
    index = 266,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(621.5,'kJ/mol'), E0=(103.585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 267,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N",
    kinetics = Arrhenius(A=(1.2,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586.75,'kJ/mol'), E0=(37.8299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19851425044504023, var=0.571842701104847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.0147658374783632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.0147658374783632""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.0147658374783632
""",
)

entry(
    index = 269,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1",
    kinetics = Arrhenius(A=(330,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(3e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->N_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R",
    kinetics = Arrhenius(A=(241000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(19988.7,'m^3/(mol*s)'), n=0.559387, w0=(505.5,'kJ/mol'), E0=(6.17265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.64758096922484, var=0.12856071166579067, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
    Total Standard Deviation in ln(k): 4.858455732628403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.858455732628403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.858455732628403
""",
)

entry(
    index = 273,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.00744e+06,'m^3/(mol*s)'), n=-0.141162, w0=(545.7,'kJ/mol'), E0=(25.4151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2334177583490611, var=0.46599858967224705, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.9549909245191572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.9549909245191572""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.9549909245191572
""",
)

entry(
    index = 274,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(974410,'m^3/(mol*s)'), n=-0.0210882, w0=(539,'kJ/mol'), E0=(58.1819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.126200438346133, var=0.04686742152957978, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.7510893169823581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7510893169823581""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7510893169823581
""",
)

entry(
    index = 275,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(1.49065e+06,'m^3/(mol*s)'), n=-1.47799e-09, w0=(539,'kJ/mol'), E0=(55.4502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11491157996520027, var=0.026409342420197233, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
    Total Standard Deviation in ln(k): 0.6145110875777948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
Total Standard Deviation in ln(k): 0.6145110875777948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
Total Standard Deviation in ln(k): 0.6145110875777948
""",
)

entry(
    index = 276,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C",
    kinetics = Arrhenius(A=(1.21e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1",
    kinetics = Arrhenius(A=(0.029,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1",
    kinetics = Arrhenius(A=(0.029,'m^3/(mol*s)'), n=2.69, Ea=(-6.6944,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N",
    kinetics = Arrhenius(A=(1.2,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N",
    kinetics = Arrhenius(A=(2.89e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(8.57298e+06,'m^3/(mol*s)'), n=-0.225015, w0=(533.9,'kJ/mol'), E0=(30.6713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14333601097932763, var=0.14721231219756026, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 1.1293226316954987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.1293226316954987""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.1293226316954987
""",
)

entry(
    index = 282,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS",
    kinetics = Arrhenius(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(10000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H_Ext-2R!H-R",
    kinetics = Arrhenius(A=(2e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(297614,'m^3/(mol*s)'), n=0.560071, w0=(563,'kJ/mol'), E0=(99.6094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.048845920386939516, var=0.19290627441212677, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.003230077110535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R
Total Standard Deviation in ln(k): 1.003230077110535""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R
Total Standard Deviation in ln(k): 1.003230077110535
""",
)

entry(
    index = 286,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_5R!H->Cl",
    kinetics = Arrhenius(A=(6.66667e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.07359e+06,'m^3/(mol*s)'), n=0.250891, w0=(563,'kJ/mol'), E0=(110.06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04633756987201762, var=0.9143736065897192, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.033411565246553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.033411565246553""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.033411565246553
""",
)

entry(
    index = 288,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R",
    kinetics = Arrhenius(A=(5e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H",
    kinetics = ArrheniusBM(A=(15553.5,'m^3/(mol*s)'), n=1.06652, w0=(542.875,'kJ/mol'), E0=(43.0725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3751043806901457, var=3.633396278694178, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H
    Total Standard Deviation in ln(k): 7.276355829734608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H
Total Standard Deviation in ln(k): 7.276355829734608""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H
Total Standard Deviation in ln(k): 7.276355829734608
""",
)

entry(
    index = 290,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(254.888,'m^3/(mol*s)'), n=1.41958, w0=(555.4,'kJ/mol'), E0=(54.9731,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4879301375267737, var=1.0646421367640162, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H
    Total Standard Deviation in ln(k): 3.294470787474354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H
Total Standard Deviation in ln(k): 3.294470787474354""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H
Total Standard Deviation in ln(k): 3.294470787474354
""",
)

entry(
    index = 291,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C",
    kinetics = ArrheniusBM(A=(1.27915e+06,'m^3/(mol*s)'), n=1.10445e-07, w0=(549.5,'kJ/mol'), E0=(55.0218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9639738002758667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C
    Total Standard Deviation in ln(k): 1.9682923503688117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C
Total Standard Deviation in ln(k): 1.9682923503688117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C
Total Standard Deviation in ln(k): 1.9682923503688117
""",
)

entry(
    index = 292,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_N-5R!H->C",
    kinetics = Arrhenius(A=(2e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(2.37079e+07,'m^3/(mol*s)'), n=0.0401314, w0=(563,'kJ/mol'), E0=(109.41,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03318565382030598, var=0.24251853655855699, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.0706363055711745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.0706363055711745""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.0706363055711745
""",
)

entry(
    index = 294,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = Arrhenius(A=(5e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N",
    kinetics = ArrheniusBM(A=(681.442,'m^3/(mol*s)'), n=1.42008, w0=(570.167,'kJ/mol'), E0=(59.4604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27093583783198855, var=0.8366788881093619, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N
    Total Standard Deviation in ln(k): 2.514477552713894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N
Total Standard Deviation in ln(k): 2.514477552713894""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N
Total Standard Deviation in ln(k): 2.514477552713894
""",
)

entry(
    index = 296,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N",
    kinetics = ArrheniusBM(A=(71249.2,'m^3/(mol*s)'), n=0.923296, w0=(589.333,'kJ/mol'), E0=(76.8214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3314060582003253, var=4.561123735609295, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N
    Total Standard Deviation in ln(k): 7.626711462255872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N
Total Standard Deviation in ln(k): 7.626711462255872""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N
Total Standard Deviation in ln(k): 7.626711462255872
""",
)

entry(
    index = 297,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = Arrhenius(A=(240,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = Arrhenius(A=(240,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = ArrheniusBM(A=(2120.6,'m^3/(mol*s)'), n=1.11273, w0=(548,'kJ/mol'), E0=(90.1415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0577719610994099, var=0.10970470284393032, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 3.3217208386648753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 3.3217208386648753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 3.3217208386648753
""",
)

entry(
    index = 300,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(601.5,'kJ/mol'), E0=(60.1635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8517473409002706, var=0.12793378685806792, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 2.85711898780005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 2.85711898780005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 2.85711898780005
""",
)

entry(
    index = 301,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C",
    kinetics = ArrheniusBM(A=(8.89076e+11,'m^3/(mol*s)'), n=-1.45278, w0=(538.75,'kJ/mol'), E0=(95.1297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4940832532737766, var=6.662992128043824, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 6.416192212778926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 6.416192212778926""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 6.416192212778926
""",
)

entry(
    index = 302,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(382.985,'m^3/(mol*s)'), n=1.41908, w0=(598.5,'kJ/mol'), E0=(62.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4204039765851029, var=1.7995148930277942, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 3.745563286554192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 3.745563286554192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 3.745563286554192
""",
)

entry(
    index = 303,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N",
    kinetics = Arrhenius(A=(1.2,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N",
    kinetics = Arrhenius(A=(1.2,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N",
    kinetics = Arrhenius(A=(170,'m^3/(mol*s)'), n=1.5, Ea=(-2.7196,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N",
    kinetics = Arrhenius(A=(330,'m^3/(mol*s)'), n=1.5, Ea=(2.05016,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->N_N-2R!H->C_2NO-u1_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing",
    kinetics = Arrhenius(A=(0.000675,'m^3/(mol*s)'), n=2.7, Ea=(-18.4222,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing",
    kinetics = Arrhenius(A=(2e+06,'m^3/(mol*s)'), n=0, Ea=(8.368,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R",
    kinetics = Arrhenius(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(3e+06,'m^3/(mol*s)'), n=0, Ea=(4.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C",
    kinetics = Arrhenius(A=(2.16e+08,'m^3/(mol*s)'), n=-0.75, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462319, w0=(561.5,'kJ/mol'), E0=(20.6926,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1875486056776, var=1.424548425305546, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
    Total Standard Deviation in ln(k): 2.863968137578843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.863968137578843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.863968137578843
""",
)

entry(
    index = 313,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R",
    kinetics = Arrhenius(A=(783000,'m^3/(mol*s)'), n=0, Ea=(-0.54392,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C",
    kinetics = Arrhenius(A=(843000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C",
    kinetics = Arrhenius(A=(843000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R",
    kinetics = Arrhenius(A=(1.45e+06,'m^3/(mol*s)'), n=0, Ea=(-0.54392,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(7.88543e+08,'m^3/(mol*s)'), n=-0.898041, w0=(539,'kJ/mol'), E0=(64.7317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.04891149884417056, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.4433660913390885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390885""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390885
""",
)

entry(
    index = 318,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C",
    kinetics = ArrheniusBM(A=(2.95928e+07,'m^3/(mol*s)'), n=-0.381632, w0=(539,'kJ/mol'), E0=(52.4404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12581781838528797, var=0.02950531244438124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
    Total Standard Deviation in ln(k): 0.6604807308986197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 0.6604807308986197""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 0.6604807308986197
""",
)

entry(
    index = 319,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C",
    kinetics = Arrhenius(A=(644,'m^3/(mol*s)'), n=1.19, Ea=(2.13384,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(8306.14,'m^3/(mol*s)'), n=0.980744, w0=(563,'kJ/mol'), E0=(87.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13720069350505879, var=0.08615133866550422, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.9331461447686789"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.9331461447686789""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.9331461447686789
""",
)

entry(
    index = 321,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.11045e+07,'m^3/(mol*s)'), n=3.31172e-05, w0=(563,'kJ/mol'), E0=(109.438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.758265666606295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295
""",
)

entry(
    index = 322,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.8105e+07,'m^3/(mol*s)'), n=2.83014e-07, w0=(563,'kJ/mol'), E0=(112.488,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5096568970344721, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.907809337393689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_N-5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689
""",
)

entry(
    index = 323,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(370355,'m^3/(mol*s)'), n=0.49636, w0=(538,'kJ/mol'), E0=(68.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014583719869054195, var=0.22544094474037574, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.988503192610954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R
Total Standard Deviation in ln(k): 0.988503192610954""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R
Total Standard Deviation in ln(k): 0.988503192610954
""",
)

entry(
    index = 324,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_2R!H->N",
    kinetics = Arrhenius(A=(480,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_N-2R!H->N",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-4.24385e-09, w0=(551.5,'kJ/mol'), E0=(59.1005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 327,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_2R!H->N",
    kinetics = Arrhenius(A=(2.4,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_N-2R!H->N",
    kinetics = ArrheniusBM(A=(3.53601e+07,'m^3/(mol*s)'), n=-1.67864e-05, w0=(551.5,'kJ/mol'), E0=(125.936,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.4053866559415926, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_N-2R!H->N
    Total Standard Deviation in ln(k): 8.008842950292529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_N-2R!H->N
Total Standard Deviation in ln(k): 8.008842950292529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_N-2R!H->N
Total Standard Deviation in ln(k): 8.008842950292529
""",
)

entry(
    index = 329,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C_Ext-1CN-R",
    kinetics = Arrhenius(A=(904000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->H_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C",
    kinetics = ArrheniusBM(A=(1.70766e+07,'m^3/(mol*s)'), n=-1.1356e-07, w0=(563,'kJ/mol'), E0=(62.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C
    Total Standard Deviation in ln(k): 1.9534182263699047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C
Total Standard Deviation in ln(k): 1.9534182263699047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C
Total Standard Deviation in ln(k): 1.9534182263699047
""",
)

entry(
    index = 331,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.10971e+07,'m^3/(mol*s)'), n=0.175069, w0=(563,'kJ/mol'), E0=(115.213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030727805018147705, var=0.19083552716044783, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C
    Total Standard Deviation in ln(k): 0.8834835763770185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 0.8834835763770185""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 0.8834835763770185
""",
)

entry(
    index = 332,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C",
    kinetics = Arrhenius(A=(400,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(26.4236,'m^3/(mol*s)'), n=1.81767, w0=(573.25,'kJ/mol'), E0=(49.4325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18907253258610912, var=0.32124585143762036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 1.6113114733907676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 1.6113114733907676""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 1.6113114733907676
""",
)

entry(
    index = 334,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C",
    kinetics = Arrhenius(A=(3.61e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609.25,'kJ/mol'), E0=(56.36,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632987, var=0.4111323726295285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C
    Total Standard Deviation in ln(k): 2.9843512490456052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 2.9843512490456052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C
Total Standard Deviation in ln(k): 2.9843512490456052
""",
)

entry(
    index = 336,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1",
    kinetics = Arrhenius(A=(1.2,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1",
    kinetics = Arrhenius(A=(2.4,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C",
    kinetics = Arrhenius(A=(2.4,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C",
    kinetics = Arrhenius(A=(2.4,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->O",
    kinetics = Arrhenius(A=(2.41e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->O",
    kinetics = Arrhenius(A=(2.37e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_2R!H->C_N-4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N",
    kinetics = Arrhenius(A=(3.6,'m^3/(mol*s)'), n=2, Ea=(-4.97896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R",
    kinetics = Arrhenius(A=(1.94e+06,'m^3/(mol*s)'), n=0, Ea=(1.50624,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = Arrhenius(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R",
    kinetics = Arrhenius(A=(2.29e+07,'m^3/(mol*s)'), n=-0.35, Ea=(-0.54392,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R",
    kinetics = Arrhenius(A=(2.2e+07,'m^3/(mol*s)'), n=0, Ea=(12.552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->H_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_5CFO->C",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(12.552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_N-5CFO->C",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(12.552,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->H_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_5CFO->C",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_N-5CFO->C",
    kinetics = Arrhenius(A=(2e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->H_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R",
    kinetics = Arrhenius(A=(1.21e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(4.4e+07,'m^3/(mol*s)'), n=8.90972e-08, w0=(563,'kJ/mol'), E0=(116.386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 3.793107781493648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 3.793107781493648""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->H_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 3.793107781493648
""",
)

entry(
    index = 354,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N",
    kinetics = Arrhenius(A=(240,'m^3/(mol*s)'), n=1.5, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N",
    kinetics = Arrhenius(A=(480,'m^3/(mol*s)'), n=1.5, Ea=(6.52704,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N",
    kinetics = Arrhenius(A=(720,'m^3/(mol*s)'), n=1.5, Ea=(-3.72376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N",
    kinetics = Arrhenius(A=(1.81e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->N_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

