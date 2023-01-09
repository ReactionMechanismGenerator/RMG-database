#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction"
shortDesc = "Library of computed reactions by ARC"
longDesc = """

35 REACTIONS/90 REACTIONS
"""

entry(
    index = 1,
    label = "H2NNT + NH2OH <=> HNOH + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.72268e-05,'cm^3/(mol*s)'), n=4.5273, Ea=(4.41074,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc = """""",
)

entry(
    index = 2,
    label = "N + HNO2 <=> NO2 + NH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(286.297,'cm^3/(mol*s)'), n=3.30301, Ea=(5.06061,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 3,
    label = "O2 + H2NNS <=> HO2 + NNH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.21885,'cm^3/(mol*s)'), n=3.54012, Ea=(0.757679,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

#entry(
#    index = 4,
#    label = "H2NNT + NH2OH <=> HNOH + N2H3",
#    degeneracy = 1.0,
#    kinetics = Arrhenius(A=(9.7219e-05,'cm^3/(mol*s)'), n=4.52731, Ea=(4.41087,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
#                         Tmax=(3000,'K')),
#    longDesc ="""""",
#)
#
entry(
    index = 5,
    label = "NO2 + HNO <=> NO + HNO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12.5304,'cm^3/(mol*s)'), n=3.5418, Ea=(2.5719,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 6,
    label = "HO2 + NH <=> N + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00149367,'cm^3/(mol*s)'), n=4.48727, Ea=(12.2886,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 7,
    label = "NH + H2O2 <=> HO2 + NH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.86962,'cm^3/(mol*s)'), n=3.66208, Ea=(-0.823893,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 8,
    label = "N + NH2OH <=> NH + H2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.180599,'cm^3/(mol*s)'), n=4.10733, Ea=(9.37053,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 9,
    label = "NH + HNOH <=> N + NH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00196607,'cm^3/(mol*s)'), n=4.40434, Ea=(13.449,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 10,
    label = "N + N2H2 <=> NH + NNH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12526.7,'cm^3/(mol*s)'), n=2.91279, Ea=(1.27082,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 11,
    label = "NH + N2H3 <=> N + N2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0235874,'cm^3/(mol*s)'), n=3.95889, Ea=(16.6774,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 12,
    label = "HO2 + N2H4 <=> H2O2 + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.114187,'cm^3/(mol*s)'), n=3.76949, Ea=(4.51861,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 13,
    label = "NH2OH + N2H3 <=> H2NO + N2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0048183,'cm^3/(mol*s)'), n=3.85449, Ea=(0.0489392,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 14,
    label = "HNOH + N2H4 <=> NH2OH + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.91142e-06,'cm^3/(mol*s)'), n=4.98406, Ea=(14.1054,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 15,
    label = "HNOH + N2H2 <=> NNH + NH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00918288,'cm^3/(mol*s)'), n=4.40655, Ea=(-0.730177,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 16,
    label = "NNH + N2H4 <=> N2H2 + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.23287,'cm^3/(mol*s)'), n=3.64307, Ea=(70.9214,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 17,
    label = "NH + N2H3 <=> NH2 + H2NNT",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(477.726,'cm^3/(mol*s)'), n=2.91037, Ea=(-3.43781,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 18,
    label = "HO2 + N2H3 <=> H2O2 + H2NNT",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000180696,'cm^3/(mol*s)'), n=4.67583, Ea=(15.0967,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 19,
    label = "H2NNT + NH2OH <=> H2NO + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.525649,'cm^3/(mol*s)'), n=3.40859, Ea=(-8.28269,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 20,
    label = "H + N2H3 <=> H2 + H2NNT",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.28842e+07,'cm^3/(mol*s)'), n=1.78355, Ea=(5.13185,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 21,
    label = "H2NNT + N2H2 <=> NNH + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19786,'cm^3/(mol*s)'), n=3.88285, Ea=(-4.38175,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 22,
    label = "N + HONO <=> NO2 + NH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00123046,'cm^3/(mol*s)'), n=4.72332, Ea=(20.4433,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 23,
    label = "HO2 + HONO <=> NO2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.20021e-07,'cm^3/(mol*s)'), n=5.27468, Ea=(8.89369,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 24,
    label = "NO2 + NH2OH <=> HONO + H2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(23929.1,'cm^3/(mol*s)'), n=3.0051, Ea=(9.92365,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 25,
    label = "HONO + HNOH <=> NO2 + NH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.82899,'cm^3/(mol*s)'), n=3.26304, Ea=(7.19158,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 26,
    label = "HONO + H2NNT <=> NO2 + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0225963,'cm^3/(mol*s)'), n=3.96959, Ea=(0.351983,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 27,
    label = "HO2 + H2NO <=> O2 + H3NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.727e-05,'cm^3/(mol*s)'), n=4.55865, Ea=(19.2649,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 28,
    label = "H2NO + H2NNS <=> NNH + H3NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.171771,'cm^3/(mol*s)'), n=3.30243, Ea=(9.2476,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 29,
    label = "NNH + H3NO <=> H2NO + N2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00850441,'cm^3/(mol*s)'), n=4.21355, Ea=(0.260233,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 30,
    label = "HNNO + NH2OH <=> H2NO + NH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39069,'cm^3/(mol*s)'), n=3.28683, Ea=(1.9912,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 31,
    label = "HNOH + NH2NO <=> HNNO + NH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000551441,'cm^3/(mol*s)'), n=4.36147, Ea=(24.1494,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 32,
    label = "HNO2 + HNNO <=> NO2 + NH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.95388,'cm^3/(mol*s)'), n=3.68865, Ea=(-4.22167,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 33,
    label = "HONO + HNNO <=> NO2 + NH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.36855e-05,'cm^3/(mol*s)'), n=4.54667, Ea=(13.8383,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'),
                         Tmax=(3000,'K')),
    longDesc ="""""",
)

entry(
    index = 34,
    label = "HNNO + N2H2 <=> NNH + NH2NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.619995, 'cm^3/(mol*s)'), n=3.93877, Ea=(-4.44506, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'),
                         Tmax=(3000, 'K')),
    longDesc ="""""",
)

entry(
    index = 35,
    label = "H2NNT + NH2NO <=> HNNO + N2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.44631e-05, 'cm^3/(mol*s)'), n=4.84163, Ea=(10.8646, 'kJ/mol'), T0=(1, 'K'),
                         Tmin=(300, 'K'),
                         Tmax=(3000, 'K')),
    longDesc ="""""",
)
