#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H",
    kinetics = ArrheniusBM(A=(0.00210365,'m^3/(mol*s)'), n=3.0721, w0=(249000,'J/mol'), E0=(47627.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00843623183255,var=2.99846187306,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H
""",
)

entry(
    index = 2,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000262713,'m^3/(mol*s)'), n=2.73478, w0=(317500,'J/mol'), E0=(37189.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00831517972036,var=0.510500461583,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
""",
)

entry(
    index = 3,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(72.6931,'m^3/(mol*s)'), n=1.62321, w0=(317500,'J/mol'), E0=(28916.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000663407518378,var=0.864666140084,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 4,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.65059e-05,'m^3/(mol*s)'), n=3.17159, w0=(272000,'J/mol'), E0=(46745,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013510044396,var=1.36465881133,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
""",
)

entry(
    index = 5,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H",
    kinetics = ArrheniusBM(A=(123479,'m^3/(mol*s)'), n=0.382011, w0=(312854,'J/mol'), E0=(62557.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.121713639537,var=3.73022853458,Tref=1000.0,N=99,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H
""",
)

entry(
    index = 6,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O",
    kinetics = ArrheniusBM(A=(7.86001e-14,'m^3/(mol*s)'), n=6.83939, w0=(272000,'J/mol'), E0=(22703.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0102816094324,var=0.0,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
""",
)

entry(
    index = 7,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H",
    kinetics = ArrheniusBM(A=(1.13489,'m^3/(mol*s)'), n=1.90056, w0=(317500,'J/mol'), E0=(58127.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00354671906531,var=4.43546885428,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H
""",
)

entry(
    index = 8,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(0.0616046,'m^3/(mol*s)'), n=2.51389, w0=(317500,'J/mol'), E0=(23636.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0555968198146,var=1.91524436646,Tref=1000.0,N=38,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C
""",
)

entry(
    index = 9,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C",
    kinetics = ArrheniusBM(A=(1.13892e+06,'m^3/(mol*s)'), n=0.508541, w0=(294500,'J/mol'), E0=(64596.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.120392336655,var=2.70981260646,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C
""",
)

entry(
    index = 10,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.591254,'m^3/(mol*s)'), n=2.05592, w0=(272000,'J/mol'), E0=(67331.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0115141946781,var=2.15880334916,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 11,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.000241175,'m^3/(mol*s)'), n=2.77038, w0=(272000,'J/mol'), E0=(48708.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00856663028221,var=0.579723152952,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 12,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(5.65083e+06,'m^3/(mol*s)'), n=-0.209756, w0=(317500,'J/mol'), E0=(77852.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.115797309179,var=6.6347320719,Tref=1000.0,N=8,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R
""",
)

entry(
    index = 13,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.623254,'m^3/(mol*s)'), n=2.12775, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0225520045585,var=37.2222545335,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 14,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.000161894,'m^3/(mol*s)'), n=2.80487, w0=(317500,'J/mol'), E0=(40940.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004602113457,var=0.603292409767,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C
""",
)

entry(
    index = 15,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(133.922,'m^3/(mol*s)'), n=1.83268, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00451233202255,var=4.08806707174,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C
""",
)

entry(
    index = 16,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.23866,'m^3/(mol*s)'), n=1.86415, w0=(317500,'J/mol'), E0=(32888.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00416017910563,var=0.0713437445308,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R
""",
)

entry(
    index = 17,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H",
    kinetics = ArrheniusBM(A=(0.0196163,'m^3/(mol*s)'), n=2.78709, w0=(294500,'J/mol'), E0=(49427,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0147312846697,var=12.6785332449,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H
""",
)

entry(
    index = 18,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS",
    kinetics = ArrheniusBM(A=(0.00151658,'m^3/(mol*s)'), n=2.73203, w0=(272000,'J/mol'), E0=(52391.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000126336448417,var=3.67040599037,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS
""",
)

entry(
    index = 19,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.55213,'m^3/(mol*s)'), n=1.89257, w0=(317500,'J/mol'), E0=(35919.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00671632701415,var=0.142979417472,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C
""",
)

entry(
    index = 20,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(3.65325,'m^3/(mol*s)'), n=2.35991, w0=(317500,'J/mol'), E0=(39377.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R
""",
)

entry(
    index = 21,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.25856e-05,'m^3/(mol*s)'), n=2.87622, w0=(272000,'J/mol'), E0=(50486.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00397751698654,var=35.4303862873,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 22,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.0545724,'m^3/(mol*s)'), n=2.56074, w0=(317500,'J/mol'), E0=(23398.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0875538896256,var=1.96069674179,Tref=1000.0,N=18,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O
""",
)

entry(
    index = 23,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S",
    kinetics = ArrheniusBM(A=(2.7671e-09,'m^3/(mol*s)'), n=4.95327, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.130583308253,var=8.54337116031,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S
""",
)

entry(
    index = 24,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(33027.1,'m^3/(mol*s)'), n=0.637878, w0=(262591,'J/mol'), E0=(59992.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.129465142133,var=9.73224514211,Tref=1000.0,N=22,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S
""",
)

entry(
    index = 25,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C",
    kinetics = ArrheniusBM(A=(0.00706363,'m^3/(mol*s)'), n=2.86548, w0=(249000,'J/mol'), E0=(39095.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00189195458264,var=0.00411136771473,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C
""",
)

entry(
    index = 26,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C",
    kinetics = ArrheniusBM(A=(4.06214e+06,'m^3/(mol*s)'), n=0.31104, w0=(294500,'J/mol'), E0=(64204.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.125122207198,var=1.04408577291,Tref=1000.0,N=8,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C
""",
)

entry(
    index = 27,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(0.221491,'m^3/(mol*s)'), n=1.94805, w0=(317500,'J/mol'), E0=(49055.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0346263163828,var=4.27172445914,Tref=1000.0,N=9,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R
""",
)

entry(
    index = 28,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.92348,'m^3/(mol*s)'), n=1.7861, w0=(317500,'J/mol'), E0=(38696.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00454610292748,var=0.0784878802369,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H
""",
)

entry(
    index = 29,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H",
    kinetics = ArrheniusBM(A=(1.47526e-08,'m^3/(mol*s)'), n=4.38609, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.118766371834,var=3.38214673482,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H
""",
)

entry(
    index = 30,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000323852,'m^3/(mol*s)'), n=2.90024, w0=(272000,'J/mol'), E0=(57770.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00804154035797,var=7.07361434067,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 31,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000329563,'m^3/(mol*s)'), n=2.74977, w0=(317500,'J/mol'), E0=(34897.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00846629425747,var=0.0122754283254,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 32,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(7.47355,'m^3/(mol*s)'), n=1.86203, w0=(317500,'J/mol'), E0=(32763.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00413482416969,var=0.456006049275,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 33,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C",
    kinetics = ArrheniusBM(A=(4.5479,'m^3/(mol*s)'), n=1.8917, w0=(317500,'J/mol'), E0=(35669.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00312809117276,var=1.10218533272,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C
""",
)

entry(
    index = 34,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.00033045,'m^3/(mol*s)'), n=2.70027, w0=(317500,'J/mol'), E0=(42476.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0080428540947,var=0.509215682854,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R
""",
)

entry(
    index = 35,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS",
    kinetics = ArrheniusBM(A=(5.28116e+06,'m^3/(mol*s)'), n=0.105471, w0=(253182,'J/mol'), E0=(59210.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.156740133087,var=4.64322947177,Tref=1000.0,N=11,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS
""",
)

entry(
    index = 36,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.66928,'m^3/(mol*s)'), n=1.89782, w0=(317500,'J/mol'), E0=(33774.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00816718161748,var=2.67670088107,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 37,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H",
    kinetics = ArrheniusBM(A=(1.72291e-12,'m^3/(mol*s)'), n=5.80277, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18232810625,var=19.0911628403,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H
""",
)

entry(
    index = 38,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(46.0113,'m^3/(mol*s)'), n=1.48934, w0=(317500,'J/mol'), E0=(30898.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00317550537416,var=7.57494116763,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 39,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S",
    kinetics = ArrheniusBM(A=(11.1904,'m^3/(mol*s)'), n=1.86011, w0=(317500,'J/mol'), E0=(33507.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0042045271908,var=0.181730157675,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S
""",
)

entry(
    index = 40,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.05439e-09,'m^3/(mol*s)'), n=4.46643, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0877311875179,var=7.94803308613,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 41,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C",
    kinetics = ArrheniusBM(A=(0.000438786,'m^3/(mol*s)'), n=2.80472, w0=(317500,'J/mol'), E0=(41136.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00459534634838,var=1.04936521474,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C
""",
)

entry(
    index = 42,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(7.09316,'m^3/(mol*s)'), n=1.81488, w0=(317500,'J/mol'), E0=(40695.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0046518971504,var=0.509245800448,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R
""",
)

entry(
    index = 43,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000948253,'m^3/(mol*s)'), n=2.8265, w0=(272000,'J/mol'), E0=(58850.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0184562066824,var=0.1067264526,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 44,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R",
    kinetics = ArrheniusBM(A=(105.332,'m^3/(mol*s)'), n=1.86618, w0=(294500,'J/mol'), E0=(26384.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0687472798732,var=1.30118973584,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R
""",
)

entry(
    index = 45,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.474196,'m^3/(mol*s)'), n=2.19716, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0331011313917,var=6.4873899742,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
""",
)

entry(
    index = 46,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C",
    kinetics = ArrheniusBM(A=(0.522281,'m^3/(mol*s)'), n=2.19521, w0=(249000,'J/mol'), E0=(36541.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15419602006,var=2.91807131447,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C
""",
)

entry(
    index = 47,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S",
    kinetics = ArrheniusBM(A=(0.0985348,'m^3/(mol*s)'), n=2.56968, w0=(249000,'J/mol'), E0=(55099.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0229235715418,var=6.37655098362,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S
""",
)

entry(
    index = 48,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS",
    kinetics = ArrheniusBM(A=(3.86358,'m^3/(mol*s)'), n=1.86587, w0=(317500,'J/mol'), E0=(41247.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00335826781227,var=2.62178651927,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS
""",
)

entry(
    index = 49,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.60293,'m^3/(mol*s)'), n=1.85069, w0=(317500,'J/mol'), E0=(35343.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00433516582109,var=0.510488043436,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
""",
)

entry(
    index = 50,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.000337832,'m^3/(mol*s)'), n=2.80975, w0=(317500,'J/mol'), E0=(39743.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00463483895218,var=2.02744468266,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R
""",
)

entry(
    index = 51,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H",
    kinetics = ArrheniusBM(A=(0.000245202,'m^3/(mol*s)'), n=3.12975, w0=(317500,'J/mol'), E0=(42127.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.17810689831,var=25.9593419504,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H
""",
)

entry(
    index = 52,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O",
    kinetics = ArrheniusBM(A=(3.28488e-07,'m^3/(mol*s)'), n=4.27975, w0=(272000,'J/mol'), E0=(39446.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.116131220677,var=128.127413988,Tref=1000.0,N=3,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O
""",
)

entry(
    index = 53,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.000165826,'m^3/(mol*s)'), n=2.78045, w0=(317500,'J/mol'), E0=(39442.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00819919097163,var=0.609670443378,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R
""",
)

entry(
    index = 54,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H",
    kinetics = ArrheniusBM(A=(0.000103852,'m^3/(mol*s)'), n=2.81251, w0=(317500,'J/mol'), E0=(36087.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00867709233886,var=4.46284959293,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H
""",
)

entry(
    index = 55,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.6991e-17,'m^3/(mol*s)'), n=6.69355, w0=(272000,'J/mol'), E0=(12052,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.175734228892,var=5.35176518722,Tref=1000.0,N=25,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R
""",
)

entry(
    index = 56,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(2.41587,'m^3/(mol*s)'), n=2.26861, w0=(294500,'J/mol'), E0=(29400.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00174303959013,var=0.404173893369,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R
""",
)

entry(
    index = 57,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS",
    kinetics = ArrheniusBM(A=(1.34652e+08,'m^3/(mol*s)'), n=-0.673195, w0=(317500,'J/mol'), E0=(57765.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.154941161525,var=3.13247558938,Tref=1000.0,N=9,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS
""",
)

entry(
    index = 58,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.00802442,'m^3/(mol*s)'), n=2.59296, w0=(249000,'J/mol'), E0=(37197,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000932211150159,var=2.99796061866,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C
""",
)

entry(
    index = 59,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C",
    kinetics = ArrheniusBM(A=(0.00448706,'m^3/(mol*s)'), n=2.86702, w0=(249000,'J/mol'), E0=(37152.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00196941466557,var=0.382888548845,Tref=1000.0,N=9,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C
""",
)

entry(
    index = 60,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(0.0769577,'m^3/(mol*s)'), n=2.19862, w0=(272000,'J/mol'), E0=(63584.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00926025561461,var=3.87267750073,Tref=1000.0,N=8,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R
""",
)

entry(
    index = 61,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.000645968,'m^3/(mol*s)'), n=2.57735, w0=(317500,'J/mol'), E0=(41069.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00140632983989,var=0.475236421435,Tref=1000.0,N=14,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R
""",
)

entry(
    index = 62,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H",
    kinetics = ArrheniusBM(A=(7282.5,'m^3/(mol*s)'), n=0.786819, w0=(317500,'J/mol'), E0=(49954.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.251413021005,var=2.84016765866,Tref=1000.0,N=5,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H
""",
)

entry(
    index = 63,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C",
    kinetics = ArrheniusBM(A=(0.00764072,'m^3/(mol*s)'), n=2.78832, w0=(317500,'J/mol'), E0=(40405.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C
""",
)

entry(
    index = 64,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H",
    kinetics = ArrheniusBM(A=(9.25824,'m^3/(mol*s)'), n=1.54136, w0=(317500,'J/mol'), E0=(62975.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0341250270607,var=1.96450216014,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H
""",
)

entry(
    index = 65,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(2.04923e-11,'m^3/(mol*s)'), n=6.22286, w0=(272000,'J/mol'), E0=(35943.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0056026372566,var=0.0,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R
""",
)

entry(
    index = 66,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(3.54749,'m^3/(mol*s)'), n=1.89574, w0=(317500,'J/mol'), E0=(37627.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00447016276218,var=0.609728255244,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R
""",
)

entry(
    index = 67,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R",
    kinetics = ArrheniusBM(A=(0.0487754,'m^3/(mol*s)'), n=2.74944, w0=(294500,'J/mol'), E0=(6681.52,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00929119556987,var=2.0163159585,Tref=1000.0,N=8,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R
""",
)

entry(
    index = 68,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH",
    kinetics = ArrheniusBM(A=(0.000353138,'m^3/(mol*s)'), n=2.6679, w0=(317500,'J/mol'), E0=(38903.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00533573803697,var=1.10226802228,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH
""",
)

entry(
    index = 69,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000492003,'m^3/(mol*s)'), n=2.74322, w0=(249000,'J/mol'), E0=(44746.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00059135818677,var=38.8462115916,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C
""",
)

entry(
    index = 70,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000352,'m^3/(mol*s)'), n=2.74522, w0=(317500,'J/mol'), E0=(34654.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00847990432217,var=0.455935686443,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 71,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(14840.8,'m^3/(mol*s)'), n=0.66298, w0=(317500,'J/mol'), E0=(70565.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0935904657892,var=2.95242873909,Tref=1000.0,N=24,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R
""",
)

entry(
    index = 72,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H",
    kinetics = ArrheniusBM(A=(1.56413e-11,'m^3/(mol*s)'), n=5.07655, w0=(249000,'J/mol'), E0=(7669.94,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0988069573204,var=5.19066501021,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H
""",
)

entry(
    index = 73,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C",
    kinetics = ArrheniusBM(A=(822.791,'m^3/(mol*s)'), n=1.47488, w0=(294500,'J/mol'), E0=(36925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0444629247443,var=0.713115864662,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C
""",
)

entry(
    index = 74,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S",
    kinetics = ArrheniusBM(A=(2.60201,'m^3/(mol*s)'), n=2.04012, w0=(317500,'J/mol'), E0=(42392.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00332838151464,var=0.590996777245,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S
""",
)

entry(
    index = 75,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S",
    kinetics = ArrheniusBM(A=(0.014587,'m^3/(mol*s)'), n=2.68322, w0=(249000,'J/mol'), E0=(35560.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00313134377187,var=1.28748824936,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S
""",
)

entry(
    index = 76,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C",
    kinetics = ArrheniusBM(A=(934.537,'m^3/(mol*s)'), n=1.46036, w0=(294500,'J/mol'), E0=(43931.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0316109509951,var=2.50665481813,Tref=1000.0,N=20,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C
""",
)

entry(
    index = 77,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.54573e-05,'m^3/(mol*s)'), n=2.92362, w0=(272000,'J/mol'), E0=(50619.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00352526582938,var=6.14957919047,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
""",
)

entry(
    index = 78,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.12648,'m^3/(mol*s)'), n=1.72497, w0=(317500,'J/mol'), E0=(37783.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00331594960669,var=44.3780847136,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 79,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O",
    kinetics = ArrheniusBM(A=(0.747411,'m^3/(mol*s)'), n=2.17882, w0=(317500,'J/mol'), E0=(45243.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O
""",
)

entry(
    index = 80,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.116559,'m^3/(mol*s)'), n=2.29091, w0=(272000,'J/mol'), E0=(66037.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000142362141798,var=4.79017189654,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 81,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C",
    kinetics = ArrheniusBM(A=(7.29133,'m^3/(mol*s)'), n=1.67767, w0=(317500,'J/mol'), E0=(52006.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.122650470114,var=5.59452367395,Tref=1000.0,N=5,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C
""",
)

entry(
    index = 82,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R",
    kinetics = ArrheniusBM(A=(7.84289e-05,'m^3/(mol*s)'), n=3.09168, w0=(249000,'J/mol'), E0=(26217.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00328495863281,var=4.25321989219,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R
""",
)

entry(
    index = 83,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(2.86214e-05,'m^3/(mol*s)'), n=3.21767, w0=(317500,'J/mol'), E0=(39450.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0175138914903,var=0.855197908687,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R
""",
)

entry(
    index = 84,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H",
    kinetics = ArrheniusBM(A=(0.114733,'m^3/(mol*s)'), n=2.16824, w0=(249000,'J/mol'), E0=(34338.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0723816988575,var=1.98952729714,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H
""",
)

entry(
    index = 85,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.00131328,'m^3/(mol*s)'), n=2.50295, w0=(317500,'J/mol'), E0=(39951.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00367341204157,var=0.550892885656,Tref=1000.0,N=22,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R
""",
)

entry(
    index = 86,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000669757,'m^3/(mol*s)'), n=3.2344, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0883720960567,var=19.091162867,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C
""",
)

entry(
    index = 87,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H",
    kinetics = ArrheniusBM(A=(0.000263164,'m^3/(mol*s)'), n=2.74358, w0=(317500,'J/mol'), E0=(35384.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00842426420426,var=0.181751298575,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H
""",
)

entry(
    index = 88,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.206297,'m^3/(mol*s)'), n=1.90863, w0=(249000,'J/mol'), E0=(34889.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R
""",
)

entry(
    index = 89,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.000222314,'m^3/(mol*s)'), n=2.70417, w0=(317500,'J/mol'), E0=(43170.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00800748980276,var=4.1508848373,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R
""",
)

entry(
    index = 90,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H",
    kinetics = ArrheniusBM(A=(1.63358e-06,'m^3/(mol*s)'), n=3.83075, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.132040787943,var=37.2222546283,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H
""",
)

entry(
    index = 91,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(0.00308134,'m^3/(mol*s)'), n=2.49286, w0=(249000,'J/mol'), E0=(28255.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11527044848,var=0.216458659628,Tref=1000.0,N=3,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R
""",
)

entry(
    index = 92,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C",
    kinetics = ArrheniusBM(A=(6326.18,'m^3/(mol*s)'), n=0.936759, w0=(317500,'J/mol'), E0=(33727,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0577137497597,var=0.337910152279,Tref=1000.0,N=8,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
""",
)

entry(
    index = 93,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(7.01108,'m^3/(mol*s)'), n=1.86628, w0=(317500,'J/mol'), E0=(33012.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00415100648175,var=0.0122631108174,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 94,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.34536,'m^3/(mol*s)'), n=2.01914, w0=(317500,'J/mol'), E0=(37193.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00316280703475,var=0.228215829406,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C
""",
)

entry(
    index = 95,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H",
    kinetics = ArrheniusBM(A=(761.375,'m^3/(mol*s)'), n=1.10609, w0=(317500,'J/mol'), E0=(29037.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0289865588632,var=0.23787098691,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H
""",
)

entry(
    index = 96,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(0.000304701,'m^3/(mol*s)'), n=2.53736, w0=(317500,'J/mol'), E0=(32458.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00659674286707,var=0.651831792607,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R
""",
)

entry(
    index = 97,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(12.9088,'m^3/(mol*s)'), n=2.02008, w0=(294500,'J/mol'), E0=(44921.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0027733191886,var=21.6831064657,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R
""",
)

entry(
    index = 98,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H",
    kinetics = ArrheniusBM(A=(0.000583799,'m^3/(mol*s)'), n=3.32782, w0=(294500,'J/mol'), E0=(25836,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00975494245184,var=2.9405877534,Tref=1000.0,N=14,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H
""",
)

entry(
    index = 99,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H",
    kinetics = ArrheniusBM(A=(1823.51,'m^3/(mol*s)'), n=1.44855, w0=(294500,'J/mol'), E0=(39873.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0464858097249,var=1.04148676112,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H
""",
)

entry(
    index = 100,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H",
    kinetics = ArrheniusBM(A=(2.93216,'m^3/(mol*s)'), n=1.91512, w0=(317500,'J/mol'), E0=(32033,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0047377561762,var=1.81067713789,Tref=1000.0,N=18,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H
""",
)

entry(
    index = 101,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(5.51278e-05,'m^3/(mol*s)'), n=3.08704, w0=(249000,'J/mol'), E0=(29014.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00324405059895,var=1.50458864235,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R
""",
)

entry(
    index = 102,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(365.826,'m^3/(mol*s)'), n=1.19352, w0=(317500,'J/mol'), E0=(63746.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.104584829802,var=0.844045062728,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 103,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.432629,'m^3/(mol*s)'), n=2.09836, w0=(317500,'J/mol'), E0=(26953.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0208548693447,var=8.93013502435,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R
""",
)

entry(
    index = 104,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.37489e-05,'m^3/(mol*s)'), n=3.22915, w0=(272000,'J/mol'), E0=(46577.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000848412783548,var=5.72779101495,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R
""",
)

entry(
    index = 105,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C",
    kinetics = ArrheniusBM(A=(0.0348212,'m^3/(mol*s)'), n=2.74164, w0=(249000,'J/mol'), E0=(35313.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00442183537928,var=1.35791851641,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C
""",
)

entry(
    index = 106,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H",
    kinetics = ArrheniusBM(A=(0.054922,'m^3/(mol*s)'), n=2.83633, w0=(294500,'J/mol'), E0=(41263.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0150043998966,var=1.34227837343,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H
""",
)

entry(
    index = 107,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(0.000769204,'m^3/(mol*s)'), n=2.47029, w0=(272000,'J/mol'), E0=(44285.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00719632349523,var=7.14926540915,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R
""",
)

entry(
    index = 108,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H",
    kinetics = ArrheniusBM(A=(0.00249635,'m^3/(mol*s)'), n=2.26195, w0=(317500,'J/mol'), E0=(34559.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00151737661254,var=0.121198694291,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H
""",
)

entry(
    index = 109,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(2.1537e+11,'m^3/(mol*s)'), n=-1.45145, w0=(311565,'J/mol'), E0=(72090.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.226774375055,var=4.31388859825,Tref=1000.0,N=31,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S
""",
)

entry(
    index = 110,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.79732,'m^3/(mol*s)'), n=1.74702, w0=(317500,'J/mol'), E0=(23206.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0030111029281,var=0.652176874295,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R
""",
)

entry(
    index = 111,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H",
    kinetics = ArrheniusBM(A=(0.000413434,'m^3/(mol*s)'), n=2.58428, w0=(317500,'J/mol'), E0=(51970,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0353007931754,var=2.69767689692,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H
""",
)

entry(
    index = 112,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H",
    kinetics = ArrheniusBM(A=(1.67892e-06,'m^3/(mol*s)'), n=3.79472, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0257200440012,var=0.0683491082891,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H
""",
)

entry(
    index = 113,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.139927,'m^3/(mol*s)'), n=2.44782, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0375921496911,var=0.739085977174,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
""",
)

entry(
    index = 114,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.0256985,'m^3/(mol*s)'), n=2.36996, w0=(272000,'J/mol'), E0=(62760,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00653334675381,var=2.39376613159,Tref=1000.0,N=12,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R
""",
)

entry(
    index = 115,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S",
    kinetics = ArrheniusBM(A=(1.34753,'m^3/(mol*s)'), n=2.29012, w0=(294500,'J/mol'), E0=(30022.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000953520881109,var=0.594195557868,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S
""",
)

entry(
    index = 116,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H",
    kinetics = ArrheniusBM(A=(1.88659e-06,'m^3/(mol*s)'), n=3.86072, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.104250554129,var=2.84008173723,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H
""",
)

entry(
    index = 117,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C",
    kinetics = ArrheniusBM(A=(3.84153,'m^3/(mol*s)'), n=1.84895, w0=(317500,'J/mol'), E0=(31466.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00328061267399,var=0.246583970103,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C
""",
)

entry(
    index = 118,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C",
    kinetics = ArrheniusBM(A=(6.1547e-14,'m^3/(mol*s)'), n=5.83921, w0=(317500,'J/mol'), E0=(11798.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0903900454791,var=0.370658803722,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C
""",
)

entry(
    index = 119,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H",
    kinetics = ArrheniusBM(A=(3.1483e-10,'m^3/(mol*s)'), n=4.43122, w0=(317500,'J/mol'), E0=(30350.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0993378347151,var=2.7801191794,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H
""",
)

entry(
    index = 120,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.334601,'m^3/(mol*s)'), n=2.23101, w0=(317500,'J/mol'), E0=(25929.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0290101103123,var=2.30648104931,Tref=1000.0,N=12,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R
""",
)

entry(
    index = 121,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C",
    kinetics = ArrheniusBM(A=(0.0333183,'m^3/(mol*s)'), n=2.75213, w0=(294500,'J/mol'), E0=(52756.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00893669863197,var=7.36636757577,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C
""",
)

entry(
    index = 122,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S",
    kinetics = ArrheniusBM(A=(10.2646,'m^3/(mol*s)'), n=2.12941, w0=(294500,'J/mol'), E0=(24832.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.60804862614e-05,var=0.221821804459,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S
""",
)

entry(
    index = 123,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R",
    kinetics = ArrheniusBM(A=(0.0587163,'m^3/(mol*s)'), n=2.295, w0=(249000,'J/mol'), E0=(36927.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0112947810461,var=1.24646692873,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R
""",
)

entry(
    index = 124,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.1149,'m^3/(mol*s)'), n=1.83598, w0=(272000,'J/mol'), E0=(34662.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00321419700186,var=7.14911131457,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 125,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H",
    kinetics = ArrheniusBM(A=(4.44414e-06,'m^3/(mol*s)'), n=4.10377, w0=(294500,'J/mol'), E0=(29450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0788385084028,var=4.08806708178,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H
""",
)

entry(
    index = 126,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(2.94482,'m^3/(mol*s)'), n=1.80356, w0=(312822,'J/mol'), E0=(53751.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0383629850836,var=4.31591327657,Tref=1000.0,N=59,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R
""",
)

entry(
    index = 127,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH",
    kinetics = ArrheniusBM(A=(0.000130394,'m^3/(mol*s)'), n=2.78875, w0=(317500,'J/mol'), E0=(31771.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00664946482321,var=0.246609582379,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH
""",
)

entry(
    index = 128,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C",
    kinetics = ArrheniusBM(A=(0.872622,'m^3/(mol*s)'), n=2.13548, w0=(317500,'J/mol'), E0=(32709.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014557534602,var=1.30546386542,Tref=1000.0,N=79,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C
""",
)

entry(
    index = 129,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS",
    kinetics = ArrheniusBM(A=(4.11651,'m^3/(mol*s)'), n=1.80326, w0=(317500,'J/mol'), E0=(36430.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00441008287296,var=0.0435344478491,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS
""",
)

entry(
    index = 130,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(6.4839e-14,'m^3/(mol*s)'), n=5.61727, w0=(272000,'J/mol'), E0=(24410.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.172730467721,var=1.64723226166,Tref=1000.0,N=18,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
""",
)

entry(
    index = 131,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.000236897,'m^3/(mol*s)'), n=2.79171, w0=(272000,'J/mol'), E0=(53638.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00469004092788,var=3.22011741565,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
""",
)

entry(
    index = 132,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(6.04317e+07,'m^3/(mol*s)'), n=-0.215867, w0=(317500,'J/mol'), E0=(42704.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0888317062121,var=0.487243617705,Tref=1000.0,N=9,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C
""",
)

entry(
    index = 133,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(827472,'m^3/(mol*s)'), n=0.265567, w0=(317500,'J/mol'), E0=(72975.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0933251855789,var=2.49232674004,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 134,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S",
    kinetics = ArrheniusBM(A=(2.50118e-11,'m^3/(mol*s)'), n=5.07998, w0=(264947,'J/mol'), E0=(29474.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.139639494085,var=8.21147995891,Tref=1000.0,N=75,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S
""",
)

entry(
    index = 135,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.23254,'m^3/(mol*s)'), n=1.81823, w0=(317500,'J/mol'), E0=(37030.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00444763072905,var=0.305898578432,Tref=1000.0,N=8,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R
""",
)

entry(
    index = 136,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C",
    kinetics = ArrheniusBM(A=(3.18215e-17,'m^3/(mol*s)'), n=6.67705, w0=(272000,'J/mol'), E0=(14907.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.220383462356,var=4.59515396088,Tref=1000.0,N=27,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C
""",
)

entry(
    index = 137,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S",
    kinetics = ArrheniusBM(A=(2.27572,'m^3/(mol*s)'), n=2.05032, w0=(317500,'J/mol'), E0=(39415,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0032436675722,var=0.603302871581,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S
""",
)

entry(
    index = 138,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH",
    kinetics = ArrheniusBM(A=(0.000192726,'m^3/(mol*s)'), n=2.68766, w0=(317500,'J/mol'), E0=(38260.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00825213551912,var=0.0435365808194,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH
""",
)

entry(
    index = 139,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.417097,'m^3/(mol*s)'), n=2.01617, w0=(317500,'J/mol'), E0=(60138.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0100138630264,var=5.59596058388,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H
""",
)

entry(
    index = 140,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.11735,'m^3/(mol*s)'), n=2.47419, w0=(317500,'J/mol'), E0=(29032.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00452901618121,var=0.981376301179,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R
""",
)

entry(
    index = 141,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H",
    kinetics = ArrheniusBM(A=(0.0185311,'m^3/(mol*s)'), n=2.86681, w0=(294500,'J/mol'), E0=(38024.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0246352362079,var=0.0576931650242,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H
""",
)

entry(
    index = 142,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(1.03517,'m^3/(mol*s)'), n=1.79236, w0=(272000,'J/mol'), E0=(65365.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014470501526,var=9.36087565735,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R
""",
)

entry(
    index = 143,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H",
    kinetics = ArrheniusBM(A=(4.84138,'m^3/(mol*s)'), n=1.70367, w0=(287160,'J/mol'), E0=(51671.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0530173699069,var=5.1468855033,Tref=1000.0,N=197,correlation='Root_N-4CCCCHHHHOOOOSSSS->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H
""",
)

entry(
    index = 144,
    label = "Root_4CCCCHHHHOOOOSSSS->H",
    kinetics = ArrheniusBM(A=(94.2569,'m^3/(mol*s)'), n=1.57154, w0=(312854,'J/mol'), E0=(38899.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0199767483263,var=1.85022117483,Tref=1000.0,N=99,correlation='Root_4CCCCHHHHOOOOSSSS->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H
""",
)

entry(
    index = 145,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000559419,'m^3/(mol*s)'), n=2.57974, w0=(272000,'J/mol'), E0=(58417.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0206049913537,var=0.579515123153,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 146,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(610.119,'m^3/(mol*s)'), n=1.4984, w0=(317500,'J/mol'), E0=(37873.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
""",
)

entry(
    index = 147,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.00944671,'m^3/(mol*s)'), n=2.80866, w0=(294500,'J/mol'), E0=(44494,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00197122094233,var=0.402697129047,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R
""",
)

entry(
    index = 148,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R",
    kinetics = ArrheniusBM(A=(1.89513e-11,'m^3/(mol*s)'), n=5.05732, w0=(249000,'J/mol'), E0=(4282.95,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.125564589668,var=8.92243218165,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R
""",
)

entry(
    index = 149,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.24734e-05,'m^3/(mol*s)'), n=3.19683, w0=(249000,'J/mol'), E0=(29462.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00234767420058,var=0.00411069335082,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C
""",
)

entry(
    index = 150,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H",
    kinetics = ArrheniusBM(A=(0.00168766,'m^3/(mol*s)'), n=2.7938, w0=(317500,'J/mol'), E0=(38032,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00775563066768,var=0.0165732963629,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H
""",
)

entry(
    index = 151,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(7.98975e-06,'m^3/(mol*s)'), n=3.41372, w0=(317500,'J/mol'), E0=(34005.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0080349980059,var=0.980743825254,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R
""",
)

entry(
    index = 152,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0316458,'m^3/(mol*s)'), n=2.30166, w0=(272000,'J/mol'), E0=(52278.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0340390530594,var=2.3401116137,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
""",
)

entry(
    index = 153,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.0100277,'m^3/(mol*s)'), n=2.60995, w0=(249000,'J/mol'), E0=(29680.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R
""",
)

entry(
    index = 154,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O",
    kinetics = ArrheniusBM(A=(678.134,'m^3/(mol*s)'), n=0.859092, w0=(317500,'J/mol'), E0=(57559.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.104551942701,var=2.80590851651,Tref=1000.0,N=8,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O
""",
)

entry(
    index = 155,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C",
    kinetics = ArrheniusBM(A=(0.00744543,'m^3/(mol*s)'), n=2.78559, w0=(249000,'J/mol'), E0=(37193.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00128927950809,var=0.51766543709,Tref=1000.0,N=7,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C
""",
)

entry(
    index = 156,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S",
    kinetics = ArrheniusBM(A=(5.13072,'m^3/(mol*s)'), n=1.84368, w0=(317500,'J/mol'), E0=(33849.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00481478270791,var=0.199111827001,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S
""",
)

entry(
    index = 157,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.000340598,'m^3/(mol*s)'), n=2.7475, w0=(317500,'J/mol'), E0=(34776.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00846125192261,var=0.0713383952927,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R
""",
)

entry(
    index = 158,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S",
    kinetics = ArrheniusBM(A=(4.3037e-07,'m^3/(mol*s)'), n=3.7483, w0=(249000,'J/mol'), E0=(22191.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0673521914509,var=1.77269700655,Tref=1000.0,N=23,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S
""",
)

entry(
    index = 159,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H",
    kinetics = ArrheniusBM(A=(0.00155066,'m^3/(mol*s)'), n=3.10102, w0=(249000,'J/mol'), E0=(53888,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00430731538454,var=38.8491840631,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H
""",
)

entry(
    index = 160,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H",
    kinetics = ArrheniusBM(A=(0.000227863,'m^3/(mol*s)'), n=2.95433, w0=(317500,'J/mol'), E0=(44943.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0134422143339,var=0.320305742768,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H
""",
)

entry(
    index = 161,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C",
    kinetics = ArrheniusBM(A=(0.00293703,'m^3/(mol*s)'), n=2.954, w0=(249000,'J/mol'), E0=(31415.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.045641688526,var=1.79097512774,Tref=1000.0,N=10,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C
""",
)

entry(
    index = 162,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.226599,'m^3/(mol*s)'), n=2.33188, w0=(317500,'J/mol'), E0=(26742.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0323525094179,var=1.60893147074,Tref=1000.0,N=47,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R
""",
)

entry(
    index = 163,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(1.37676,'m^3/(mol*s)'), n=2.03141, w0=(317500,'J/mol'), E0=(35454.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00519902184918,var=0.450108606438,Tref=1000.0,N=26,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R
""",
)

entry(
    index = 164,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.95374e+07,'m^3/(mol*s)'), n=-0.258108, w0=(317500,'J/mol'), E0=(78614.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0874737432838,var=15.7440378617,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 165,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R",
    kinetics = ArrheniusBM(A=(0.00861378,'m^3/(mol*s)'), n=2.81442, w0=(249000,'J/mol'), E0=(36762.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00313054099783,var=4.25330038314,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R
""",
)

entry(
    index = 166,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(6.12693e-05,'m^3/(mol*s)'), n=3.01426, w0=(272000,'J/mol'), E0=(49315.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.020910551183,var=0.67781109938,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
""",
)

entry(
    index = 167,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS",
    kinetics = ArrheniusBM(A=(1.45312e+11,'m^3/(mol*s)'), n=-1.33788, w0=(309136,'J/mol'), E0=(74795.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.221376570941,var=5.21796847883,Tref=1000.0,N=22,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS
""",
)

entry(
    index = 168,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H",
    kinetics = ArrheniusBM(A=(3.48912,'m^3/(mol*s)'), n=1.92374, w0=(317500,'J/mol'), E0=(36559.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00148429383421,var=0.474241814963,Tref=1000.0,N=30,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H
""",
)

entry(
    index = 169,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(4.77517,'m^3/(mol*s)'), n=1.81866, w0=(317500,'J/mol'), E0=(41395.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00469277533703,var=4.15083922302,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R
""",
)

entry(
    index = 170,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH",
    kinetics = ArrheniusBM(A=(0.000299602,'m^3/(mol*s)'), n=2.64301, w0=(317500,'J/mol'), E0=(44393.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00514516828328,var=2.62176318505,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH
""",
)

entry(
    index = 171,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.122965,'m^3/(mol*s)'), n=2.24668, w0=(272000,'J/mol'), E0=(63097.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011188641985,var=35.430086705,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 172,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H",
    kinetics = ArrheniusBM(A=(0.009146,'m^3/(mol*s)'), n=2.80328, w0=(294500,'J/mol'), E0=(41203.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0077334141477,var=0.22101308533,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H
""",
)

entry(
    index = 173,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H",
    kinetics = ArrheniusBM(A=(0.00018884,'m^3/(mol*s)'), n=2.94976, w0=(317500,'J/mol'), E0=(40613.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0160417044016,var=1.21284937012,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H
""",
)

entry(
    index = 174,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.0502412,'m^3/(mol*s)'), n=1.94893, w0=(272000,'J/mol'), E0=(39788.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0162479344153,var=3.06296938594,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R
""",
)

entry(
    index = 175,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C",
    kinetics = ArrheniusBM(A=(6721.19,'m^3/(mol*s)'), n=0.689328, w0=(317500,'J/mol'), E0=(52822.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0957393746591,var=2.05965510867,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C
""",
)

entry(
    index = 176,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.000131503,'m^3/(mol*s)'), n=3.04118, w0=(249000,'J/mol'), E0=(28817.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00100830069601,var=1.46510536854,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C
""",
)

entry(
    index = 177,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O",
    kinetics = ArrheniusBM(A=(4.73892e+06,'m^3/(mol*s)'), n=-0.0422028, w0=(261105,'J/mol'), E0=(64262.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.159380014333,var=7.78268360354,Tref=1000.0,N=19,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O
""",
)

entry(
    index = 178,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H",
    kinetics = ArrheniusBM(A=(7.13418e-08,'m^3/(mol*s)'), n=3.9682, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.127450056861,var=0.941118093626,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H
""",
)

entry(
    index = 179,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R",
    kinetics = ArrheniusBM(A=(9.07103,'m^3/(mol*s)'), n=1.75298, w0=(317500,'J/mol'), E0=(38726,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00819513119163,var=0.407192133334,Tref=1000.0,N=14,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R
""",
)

entry(
    index = 180,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S",
    kinetics = ArrheniusBM(A=(1.28283e+13,'m^3/(mol*s)'), n=-2.12606, w0=(314433,'J/mol'), E0=(75114.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.251183918967,var=2.68117455418,Tref=1000.0,N=30,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S
""",
)

entry(
    index = 181,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C",
    kinetics = ArrheniusBM(A=(82.8457,'m^3/(mol*s)'), n=1.89968, w0=(294500,'J/mol'), E0=(26787.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0204520671484,var=1.4242421347,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C
""",
)

entry(
    index = 182,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(13.7072,'m^3/(mol*s)'), n=1.65926, w0=(317500,'J/mol'), E0=(30028.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0160231010611,var=2.12180796062,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R
""",
)

entry(
    index = 183,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(8.61402e-05,'m^3/(mol*s)'), n=2.97376, w0=(317500,'J/mol'), E0=(48952.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000287141849508,var=3.50750080291,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 184,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000323223,'m^3/(mol*s)'), n=2.67107, w0=(317500,'J/mol'), E0=(40498.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00813529819835,var=0.0784841550306,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H
""",
)

entry(
    index = 185,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H",
    kinetics = ArrheniusBM(A=(0.0309712,'m^3/(mol*s)'), n=2.62165, w0=(317500,'J/mol'), E0=(25389.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0619757403062,var=0.261584146981,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H
""",
)

entry(
    index = 186,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(6.95615e-06,'m^3/(mol*s)'), n=3.07034, w0=(317500,'J/mol'), E0=(43341.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0179757143557,var=7.57540943206,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R
""",
)

entry(
    index = 187,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.938773,'m^3/(mol*s)'), n=2.20208, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0260499835125,var=0.941118094854,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 188,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(0.208566,'m^3/(mol*s)'), n=2.33237, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0339502379118,var=3.41838728973,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
""",
)

entry(
    index = 189,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.170582,'m^3/(mol*s)'), n=2.26245, w0=(317500,'J/mol'), E0=(28943.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0185843988556,var=4.94378549995,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H
""",
)

entry(
    index = 190,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.14803,'m^3/(mol*s)'), n=1.76089, w0=(272000,'J/mol'), E0=(39938.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
""",
)

entry(
    index = 191,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S",
    kinetics = ArrheniusBM(A=(8.44438e-08,'m^3/(mol*s)'), n=3.97888, w0=(249000,'J/mol'), E0=(20536.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0959068301106,var=3.0790303131,Tref=1000.0,N=12,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S
""",
)

entry(
    index = 192,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(0.228349,'m^3/(mol*s)'), n=1.97933, w0=(272000,'J/mol'), E0=(51250.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0377443501423,var=1.72840528665,Tref=1000.0,N=5,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C
""",
)

entry(
    index = 193,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.36797e-08,'m^3/(mol*s)'), n=4.30575, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.149801558659,var=5.46084366797,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H
""",
)

entry(
    index = 194,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O",
    kinetics = ArrheniusBM(A=(77.3871,'m^3/(mol*s)'), n=1.76602, w0=(317500,'J/mol'), E0=(32668,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O
""",
)

entry(
    index = 195,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S",
    kinetics = ArrheniusBM(A=(0.000224133,'m^3/(mol*s)'), n=2.924, w0=(249000,'J/mol'), E0=(28111.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00183042651546,var=0.449089650506,Tref=1000.0,N=8,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S
""",
)

entry(
    index = 196,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(3855.38,'m^3/(mol*s)'), n=0.62041, w0=(317500,'J/mol'), E0=(70568.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0697403126373,var=2.06791038467,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 197,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S",
    kinetics = ArrheniusBM(A=(0.107829,'m^3/(mol*s)'), n=2.38806, w0=(249000,'J/mol'), E0=(33439.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.883369845655,var=14.5663655542,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S
""",
)

entry(
    index = 198,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000704515,'m^3/(mol*s)'), n=2.81476, w0=(317500,'J/mol'), E0=(38540.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00468016341325,var=0.228232859335,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C
""",
)

entry(
    index = 199,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(2.47894e-05,'m^3/(mol*s)'), n=3.00698, w0=(272000,'J/mol'), E0=(47664.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0119720903356,var=1.43757070794,Tref=1000.0,N=6,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R
""",
)

entry(
    index = 200,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S",
    kinetics = ArrheniusBM(A=(16.6405,'m^3/(mol*s)'), n=1.95224, w0=(294500,'J/mol'), E0=(42462.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00368276434229,var=12.6725658524,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S
""",
)

entry(
    index = 201,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.87248,'m^3/(mol*s)'), n=1.89793, w0=(317500,'J/mol'), E0=(35155.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000899494422696,var=0.55583258536,Tref=1000.0,N=6,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H
""",
)

entry(
    index = 202,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.047814,'m^3/(mol*s)'), n=2.75172, w0=(294500,'J/mol'), E0=(52339.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00905494328086,var=21.6868619307,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R
""",
)

entry(
    index = 203,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R",
    kinetics = ArrheniusBM(A=(9.65682e-05,'m^3/(mol*s)'), n=2.93167, w0=(249000,'J/mol'), E0=(24234.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R
""",
)

entry(
    index = 204,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.82524e-07,'m^3/(mol*s)'), n=4.0621, w0=(249000,'J/mol'), E0=(12600.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R
""",
)

entry(
    index = 205,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.43283e-05,'m^3/(mol*s)'), n=3.44301, w0=(317500,'J/mol'), E0=(43467.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R
""",
)

entry(
    index = 206,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S",
    kinetics = ArrheniusBM(A=(0.0111231,'m^3/(mol*s)'), n=2.82449, w0=(294500,'J/mol'), E0=(44986.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00195365912763,var=0.216261076795,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S
""",
)

entry(
    index = 207,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S",
    kinetics = ArrheniusBM(A=(7.73691,'m^3/(mol*s)'), n=2.04103, w0=(294500,'J/mol'), E0=(45254,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00300501546717,var=7.36212621291,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S
""",
)

entry(
    index = 208,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.170833,'m^3/(mol*s)'), n=2.39009, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03577119111,var=1.61943291312,Tref=1000.0,N=12,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R
""",
)

entry(
    index = 209,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(149725,'m^3/(mol*s)'), n=0.320652, w0=(317500,'J/mol'), E0=(74198.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.103743138728,var=3.68476403693,Tref=1000.0,N=16,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R
""",
)

entry(
    index = 210,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S",
    kinetics = ArrheniusBM(A=(0.00683213,'m^3/(mol*s)'), n=2.79556, w0=(249000,'J/mol'), E0=(39522,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00316458392635,var=1.50461525496,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S
""",
)

entry(
    index = 211,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R",
    kinetics = ArrheniusBM(A=(0.0363465,'m^3/(mol*s)'), n=2.4086, w0=(264132,'J/mol'), E0=(53096.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0139790167011,var=7.8818872562,Tref=1000.0,N=38,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R
""",
)

entry(
    index = 212,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS",
    kinetics = ArrheniusBM(A=(1.03367e-05,'m^3/(mol*s)'), n=3.24078, w0=(272000,'J/mol'), E0=(53348.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000807169539019,var=5.72795655162,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS
""",
)

entry(
    index = 213,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.734907,'m^3/(mol*s)'), n=2.16898, w0=(317500,'J/mol'), E0=(31395.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00301816480279,var=1.0130233228,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R
""",
)

entry(
    index = 214,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(486245,'m^3/(mol*s)'), n=0.232163, w0=(249000,'J/mol'), E0=(47005,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.211252540387,var=19.1384353485,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R
""",
)

entry(
    index = 215,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H",
    kinetics = ArrheniusBM(A=(5.22328e-10,'m^3/(mol*s)'), n=4.66989, w0=(261204,'J/mol'), E0=(28694.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.109940149705,var=6.66171652801,Tref=1000.0,N=98,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H
""",
)

entry(
    index = 216,
    label = "Root",
    kinetics = ArrheniusBM(A=(619912,'m^3/(mol*s)'), n=0.269721, w0=(295753,'J/mol'), E0=(58580.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.120762461869,var=6.24178333645,Tref=1000.0,N=296,correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root
""",
)

entry(
    index = 217,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(110066,'m^3/(mol*s)'), n=0.596004, w0=(317500,'J/mol'), E0=(40510,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0605643757,var=1.98687176509,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R
""",
)

entry(
    index = 218,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.0628369,'m^3/(mol*s)'), n=2.68842, w0=(249000,'J/mol'), E0=(32597.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0032382795604,var=0.000926874500329,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R
""",
)

entry(
    index = 219,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS",
    kinetics = ArrheniusBM(A=(0.000280478,'m^3/(mol*s)'), n=2.63571, w0=(272000,'J/mol'), E0=(46689.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00335275336522,var=2.07823469346,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS
""",
)

entry(
    index = 220,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S",
    kinetics = ArrheniusBM(A=(4.68566e+11,'m^3/(mol*s)'), n=-1.4484, w0=(308300,'J/mol'), E0=(76916.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.217801261128,var=4.22753429489,Tref=1000.0,N=10,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S
""",
)

entry(
    index = 221,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S",
    kinetics = ArrheniusBM(A=(1.19566e+08,'m^3/(mol*s)'), n=-0.0859361, w0=(294500,'J/mol'), E0=(66431,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.144659913569,var=2.10543780571,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S
""",
)

entry(
    index = 222,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C",
    kinetics = ArrheniusBM(A=(0.000650397,'m^3/(mol*s)'), n=2.69845, w0=(272000,'J/mol'), E0=(50920.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00113154464901,var=6.79167958848,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C
""",
)

entry(
    index = 223,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.09573e-05,'m^3/(mol*s)'), n=3.12812, w0=(272000,'J/mol'), E0=(49748.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0216777739443,var=1.61103605495,Tref=1000.0,N=12,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
""",
)

entry(
    index = 224,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.11636,'m^3/(mol*s)'), n=2.46646, w0=(317500,'J/mol'), E0=(31750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0419533659097,var=1.489071392,Tref=1000.0,N=4,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
""",
)

entry(
    index = 225,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R",
    kinetics = ArrheniusBM(A=(0.000397862,'m^3/(mol*s)'), n=2.86573, w0=(249000,'J/mol'), E0=(27081,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00122826283021,var=0.647844721872,Tref=1000.0,N=4,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R
""",
)

entry(
    index = 226,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H",
    kinetics = ArrheniusBM(A=(0.0608488,'m^3/(mol*s)'), n=2.11329, w0=(317500,'J/mol'), E0=(57171.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0238025797512,var=44.2858898961,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H
""",
)

entry(
    index = 227,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.000291555,'m^3/(mol*s)'), n=2.70279, w0=(317500,'J/mol'), E0=(38852.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00822010231514,var=0.305901746479,Tref=1000.0,N=8,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R
""",
)

entry(
    index = 228,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S",
    kinetics = ArrheniusBM(A=(0.00504329,'m^3/(mol*s)'), n=2.85668, w0=(249000,'J/mol'), E0=(38797.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00142978695296,var=1.46515671227,Tref=1000.0,N=2,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S
""",
)

entry(
    index = 229,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H",
    kinetics = ArrheniusBM(A=(0.0312775,'m^3/(mol*s)'), n=2.64618, w0=(317500,'J/mol'), E0=(20190.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0821479586045,var=1.78039145329,Tref=1000.0,N=19,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H
""",
)

entry(
    index = 230,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(5.51127e-19,'m^3/(mol*s)'), n=7.22361, w0=(272000,'J/mol'), E0=(-10565.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.359978501607,var=6.37411318422,Tref=1000.0,N=20,correlation='Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C
""",
)

entry(
    index = 231,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H",
    kinetics = ArrheniusBM(A=(17.2563,'m^3/(mol*s)'), n=1.86647, w0=(317500,'J/mol'), E0=(40149.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00359290834952,var=0.0165677517485,Tref=1000.0,N=2,correlation='Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H
""",
)

