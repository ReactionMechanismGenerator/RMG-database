#!/usr/bin/env python
# encoding: utf-8

name = "Pdep Kientic Library Furfuryl and H 2023"
shortDesc = "The reactions of 2-furfuryl alcohol with hydrogen atom: A theoretical calculation and kinetic modeling analysis"
longDesc = """
DOI: 10.1016/j.combustflame.2023.112627
"""
autoGenerated=False
entry(
    index = 0,
    label = "2FFOH + OH <=> P1 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(0.051328,'cm^3/(mol*s)'), n=3.8714, Ea=(16.6556,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.94573, dn = +|- 0.0849193, dEa = +|- 0.529783 kJ/mol"""), Arrhenius(A=(0.051328,'cm^3/(mol*s)'), n=3.8714, Ea=(16.6556,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.94573, dn = +|- 0.0849193, dEa = +|- 0.529783 kJ/mol"""), Arrhenius(A=(0.051328,'cm^3/(mol*s)'), n=3.8714, Ea=(16.6556,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.94573, dn = +|- 0.0849193, dEa = +|- 0.529783 kJ/mol"""), Arrhenius(A=(0.051328,'cm^3/(mol*s)'), n=3.8714, Ea=(16.6556,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.94573, dn = +|- 0.0849193, dEa = +|- 0.529783 kJ/mol""")]),
)

entry(
    index = 1,
    label = "2FFOH + OH <=> P2 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(3.81552,'cm^3/(mol*s)'), n=3.619, Ea=(21.3387,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.9503, dn = +|- 0.0852184, dEa = +|- 0.531649 kJ/mol"""), Arrhenius(A=(3.81552,'cm^3/(mol*s)'), n=3.619, Ea=(21.3387,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.9503, dn = +|- 0.0852184, dEa = +|- 0.531649 kJ/mol"""), Arrhenius(A=(3.78475,'cm^3/(mol*s)'), n=3.62002, Ea=(21.3331,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.95194, dn = +|- 0.0853261, dEa = +|- 0.532321 kJ/mol"""), Arrhenius(A=(3.77343,'cm^3/(mol*s)'), n=3.6204, Ea=(21.3309,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.95207, dn = +|- 0.0853344, dEa = +|- 0.532372 kJ/mol""")]),
)

entry(
    index = 2,
    label = "2FFOH + OH <=> P3 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.75808,'cm^3/(mol*s)'), n=3.72877, Ea=(24.3929,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.06905, dn = +|- 0.092759, dEa = +|- 0.578692 kJ/mol"""), Arrhenius(A=(1.75808,'cm^3/(mol*s)'), n=3.72877, Ea=(24.3929,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.06905, dn = +|- 0.092759, dEa = +|- 0.578692 kJ/mol"""), Arrhenius(A=(1.74552,'cm^3/(mol*s)'), n=3.72969, Ea=(24.3885,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.07331, dn = +|- 0.0930216, dEa = +|- 0.58033 kJ/mol"""), Arrhenius(A=(1.7447,'cm^3/(mol*s)'), n=3.72975, Ea=(24.3889,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.07528, dn = +|- 0.093143, dEa = +|- 0.581087 kJ/mol""")]),
)

entry(
    index = 3,
    label = "2FFOH + OH <=> P4 + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(221.193,'cm^3/(mol*s)'), n=2.9808, Ea=(-9.36388,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.08585, dn = +|- 0.0105075, dEa = +|- 0.065553 kJ/mol"""), Arrhenius(A=(220.576,'cm^3/(mol*s)'), n=2.98115, Ea=(-9.36597,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.08647, dn = +|- 0.0105806, dEa = +|- 0.0660086 kJ/mol"""), Arrhenius(A=(220.576,'cm^3/(mol*s)'), n=2.98115, Ea=(-9.36597,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.08647, dn = +|- 0.0105806, dEa = +|- 0.0660086 kJ/mol"""), Arrhenius(A=(220.12,'cm^3/(mol*s)'), n=2.98141, Ea=(-9.36757,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 1.08693, dn = +|- 0.0106341, dEa = +|- 0.0663422 kJ/mol""")]),
)

entry(
    index = 4,
    label = "2FFOH + OH <=> P5 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(9.85449e+21,'cm^3/(mol*s)'), n=-2.90393, Ea=(65.7474,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.89087, dn = +|- 0.135429, dEa = +|- 0.844897 kJ/mol"""), Arrhenius(A=(1.05184e+22,'cm^3/(mol*s)'), n=-2.91193, Ea=(65.8208,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.89016, dn = +|- 0.135398, dEa = +|- 0.844701 kJ/mol"""), Arrhenius(A=(1.21669e+23,'cm^3/(mol*s)'), n=-3.21072, Ea=(68.8066,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 3.29543, dn = +|- 0.152139, dEa = +|- 0.949144 kJ/mol"""), Arrhenius(A=(4.15045e+25,'cm^3/(mol*s)'), n=-3.90476, Ea=(77.8239,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 4.44689, dn = +|- 0.190369, dEa = +|- 1.18765 kJ/mol""")]),
)

entry(
    index = 5,
    label = "2FFOH + OH <=> P29 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(9.45229e+16,'cm^3/(mol*s)'), n=-1.16496, Ea=(33.1007,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.97872, dn = +|- 0.139249, dEa = +|- 0.868724 kJ/mol"""), Arrhenius(A=(3.3433e+18,'cm^3/(mol*s)'), n=-1.57571, Ea=(40.1557,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.98125, dn = +|- 0.139356, dEa = +|- 0.869398 kJ/mol"""), Arrhenius(A=(4.69904e+19,'cm^3/(mol*s)'), n=-1.85493, Ea=(48.3137,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 4.30319, dn = +|- 0.186179, dEa = +|- 1.16151 kJ/mol"""), Arrhenius(A=(2.84796e+18,'cm^3/(mol*s)'), n=-1.43974, Ea=(53.4581,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 16.6439, dn = +|- 0.358749, dEa = +|- 2.23812 kJ/mol""")]),
)

entry(
    index = 6,
    label = "2FFOH + OH <=> P35 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(0.00799065,'cm^3/(mol*s)'), n=3.85272, Ea=(-0.550977,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.70076, dn = +|- 0.126751, dEa = +|- 0.790757 kJ/mol"""), Arrhenius(A=(0.0481871,'cm^3/(mol*s)'), n=3.66162, Ea=(4.66612,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.86392, dn = +|- 0.134234, dEa = +|- 0.837442 kJ/mol"""), Arrhenius(A=(0.0152514,'cm^3/(mol*s)'), n=3.83065, Ea=(6.45235,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 6.50234, dn = +|- 0.238843, dEa = +|- 1.49006 kJ/mol"""), Arrhenius(A=(0.176221,'cm^3/(mol*s)'), n=3.56096, Ea=(12.8321,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 8.74681, dn = +|- 0.276673, dEa = +|- 1.72607 kJ/mol""")]),
)

entry(
    index = 7,
    label = "2FFOH + OH <=> P47 + CH2CHCHO",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(2.35934e+29,'cm^3/(mol*s)'), n=-5.17986, Ea=(47.9226,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 30.9576, dn = +|- 0.43792, dEa = +|- 2.73203 kJ/mol"""), Arrhenius(A=(8.89608e+33,'cm^3/(mol*s)'), n=-6.37171, Ea=(71.4202,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 17.0992, dn = +|- 0.362192, dEa = +|- 2.25959 kJ/mol"""), Arrhenius(A=(1.11244e+34,'cm^3/(mol*s)'), n=-6.235, Ea=(91.0155,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 29.5087, dn = +|- 0.431805, dEa = +|- 2.69388 kJ/mol"""), Arrhenius(A=(2.64451e+25,'cm^3/(mol*s)'), n=-3.56672, Ea=(97.7228,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 739.714, dn = +|- 0.8428, dEa = +|- 5.25795 kJ/mol""")]),
)

entry(
    index = 8,
    label = "2FFOH + OH <=> P49 + CH2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(6.32167e-06,'cm^3/(mol*s)'), n=4.3685, Ea=(2.98053,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.74453, dn = +|- 0.128802, dEa = +|- 0.803552 kJ/mol"""), Arrhenius(A=(9.8385e-05,'cm^3/(mol*s)'), n=4.05723, Ea=(8.8661,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.78843, dn = +|- 0.130826, dEa = +|- 0.81618 kJ/mol"""), Arrhenius(A=(4.53745e-05,'cm^3/(mol*s)'), n=4.17807, Ea=(10.8437,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 6.19453, dn = +|- 0.232656, dEa = +|- 1.45146 kJ/mol"""), Arrhenius(A=(0.000536262,'cm^3/(mol*s)'), n=3.90395, Ea=(17.0389,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 8.24066, dn = +|- 0.269068, dEa = +|- 1.67862 kJ/mol""")]),
)

entry(
    index = 9,
    label = "2FFOH + OH <=> P52 + CHO",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(2.77808e+15,'cm^3/(mol*s)'), n=-1.10225, Ea=(16.3685,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.14243, dn = +|- 0.0972056, dEa = +|- 0.606433 kJ/mol"""), Arrhenius(A=(6.20054e+17,'cm^3/(mol*s)'), n=-1.72373, Ea=(27.1762,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 2.94719, dn = +|- 0.137891, dEa = +|- 0.860253 kJ/mol"""), Arrhenius(A=(3.03557e+18,'cm^3/(mol*s)'), n=-1.84875, Ea=(36.8616,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 12.2048, dn = +|- 0.319173, dEa = +|- 1.99121 kJ/mol"""), Arrhenius(A=(7.51238e+16,'cm^3/(mol*s)'), n=-1.2846, Ea=(45.7637,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 24 data points; dA = *|/ 82.4172, dn = +|- 0.562839, dEa = +|- 3.51136 kJ/mol""")]),
)

entry(
    index = 10,
    label = "2FFOH + OH <=> INT1",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(2.85248e+41,'cm^3/(mol*s)'), n=-11.3129, Ea=(12.4351,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 2.86032, dn = +|- 0.151177, dEa = +|- 0.472531 kJ/mol"""), Arrhenius(A=(1.52993e+28,'cm^3/(mol*s)'), n=-6.56003, Ea=(3.34394,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 2.33115, dn = +|- 0.12175, dEa = +|- 0.380551 kJ/mol"""), Arrhenius(A=(3.33339e+11,'cm^3/(mol*s)'), n=-0.836775, Ea=(-11.0158,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 1.68153, dn = +|- 0.0747597, dEa = +|- 0.233675 kJ/mol"""), Arrhenius(A=(1576.84,'cm^3/(mol*s)'), n=1.98622, Ea=(-18.6777,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 1.17505, dn = +|- 0.0232048, dEa = +|- 0.0725307 kJ/mol""")]),
)

entry(
    index = 11,
    label = "2FFOH + OH <=> INT2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(3.02044e+47,'cm^3/(mol*s)'), n=-12.5951, Ea=(38.6057,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(600,'K'), comment="""Fitted to 5 data points; dA = *|/ 48.9829, dn = +|- 0.553038, dEa = +|- 1.85842 kJ/mol"""), Arrhenius(A=(3.58898e+35,'cm^3/(mol*s)'), n=-8.33776, Ea=(30.3486,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(600,'K'), comment="""Fitted to 5 data points; dA = *|/ 511.102, dn = +|- 0.886313, dEa = +|- 2.97834 kJ/mol"""), Arrhenius(A=(5.86312e+19,'cm^3/(mol*s)'), n=-2.93698, Ea=(16.4554,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(600,'K'), comment="""Fitted to 5 data points; dA = *|/ 350.442, dn = +|- 0.832683, dEa = +|- 2.79812 kJ/mol"""), Arrhenius(A=(3.71301e+08,'cm^3/(mol*s)'), n=0.833008, Ea=(5.76548,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(600,'K'), comment="""Fitted to 5 data points; dA = *|/ 9.49669, dn = +|- 0.319894, dEa = +|- 1.07496 kJ/mol""")]),
)

entry(
    index = 12,
    label = "2FFOH + OH <=> INT3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.36866e+33,'cm^3/(mol*s)'), n=-7.60022, Ea=(11.5835,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 7 data points; dA = *|/ 28.1017, dn = +|- 0.464668, dEa = +|- 1.75631 kJ/mol"""), Arrhenius(A=(1.64119e+29,'cm^3/(mol*s)'), n=-6.02793, Ea=(10.9472,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 7 data points; dA = *|/ 231.947, dn = +|- 0.758678, dEa = +|- 2.86758 kJ/mol"""), Arrhenius(A=(3.38157e+17,'cm^3/(mol*s)'), n=-2.05264, Ea=(0.320221,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 7 data points; dA = *|/ 280.7, dn = +|- 0.785252, dEa = +|- 2.96802 kJ/mol"""), Arrhenius(A=(1.34457e+08,'cm^3/(mol*s)'), n=1.06884, Ea=(-9.29505,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 7 data points; dA = *|/ 13.7422, dn = +|- 0.365022, dEa = +|- 1.37967 kJ/mol""")]),
)

entry(
    index = 13,
    label = "2FFOH + OH <=> INT4",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(4.87424e+37,'cm^3/(mol*s)'), n=-9.74866, Ea=(15.7816,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 29251.9, dn = +|- 1.47932, dEa = +|- 4.62386 kJ/mol"""), Arrhenius(A=(1.99534e+12,'cm^3/(mol*s)'), n=-1.20747, Ea=(-8.1576,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 1.80477e+07, dn = +|- 2.40353, dEa = +|- 7.51266 kJ/mol"""), Arrhenius(A=(5.13352e+21,'cm^3/(mol*s)'), n=-4.45365, Ea=(-5.93415,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 205.947, dn = +|- 0.766381, dEa = +|- 2.39546 kJ/mol"""), Arrhenius(A=(4.95456e+13,'cm^3/(mol*s)'), n=-1.30861, Ea=(-9.34728,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(500,'K'), comment="""Fitted to 4 data points; dA = *|/ 1.09716, dn = +|- 0.0133383, dEa = +|- 0.0416912 kJ/mol""")]),
)

entry(
    index = 14,
    label = "2FFOH + OH <=> INT13",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.09203e+45,'cm^3/(mol*s)'), n=-10.931, Ea=(36.0646,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 9 data points; dA = *|/ 737.488, dn = +|- 0.904986, dEa = +|- 3.75788 kJ/mol"""), Arrhenius(A=(1.44502e+34,'cm^3/(mol*s)'), n=-7.13987, Ea=(32.382,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 9 data points; dA = *|/ 4391.18, dn = +|- 1.1495, dEa = +|- 4.77321 kJ/mol"""), Arrhenius(A=(1.16794e+17,'cm^3/(mol*s)'), n=-1.54508, Ea=(19.4732,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 9 data points; dA = *|/ 94264.9, dn = +|- 1.56977, dEa = +|- 6.51835 kJ/mol"""), Arrhenius(A=(0.000292053,'cm^3/(mol*s)'), n=4.98246, Ea=(-0.314229,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 9 data points; dA = *|/ 13592.7, dn = +|- 1.30436, dEa = +|- 5.41625 kJ/mol""")]),
)

entry(
    index = 15,
    label = "2FFOH + OH <=> INT19",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(5.96327e+39,'cm^3/(mol*s)'), n=-9.81172, Ea=(19.4115,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 8 data points; dA = *|/ 6148.68, dn = +|- 1.20493, dEa = +|- 4.78464 kJ/mol"""), Arrhenius(A=(1.00532e+25,'cm^3/(mol*s)'), n=-4.8441, Ea=(5.20676,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 8 data points; dA = *|/ 4568.87, dn = +|- 1.16391, dEa = +|- 4.62177 kJ/mol"""), Arrhenius(A=(2.43251e+14,'cm^3/(mol*s)'), n=-1.25842, Ea=(-3.72315,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 8 data points; dA = *|/ 133.624, dn = +|- 0.676086, dEa = +|- 2.68466 kJ/mol"""), Arrhenius(A=(1.38905e+06,'cm^3/(mol*s)'), n=1.5557, Ea=(-6.89358,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 8 data points; dA = *|/ 85.6624, dn = +|- 0.614677, dEa = +|- 2.44081 kJ/mol""")]),
)
