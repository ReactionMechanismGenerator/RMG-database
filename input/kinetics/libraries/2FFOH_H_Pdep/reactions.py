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
    label = "2FFOH + H <=> W1",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.96905e+13,'cm^3/(mol*s)'), n=-1.21382, Ea=(15.0105,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 1388.65, dn = +|- 1.00513, dEa = +|- 3.91062 kJ/mol"""), Arrhenius(A=(6.9751e+14,'cm^3/(mol*s)'), n=-1.76508, Ea=(9.88956,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 1519.08, dn = +|- 1.0176, dEa = +|- 3.95913 kJ/mol"""), Arrhenius(A=(4.10561e+33,'cm^3/(mol*s)'), n=-7.46646, Ea=(34.5286,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 33.5565, dn = +|- 0.488006, dEa = +|- 1.89866 kJ/mol"""), Arrhenius(A=(3.56529e+21,'cm^3/(mol*s)'), n=-3.23425, Ea=(25.1491,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 420.314, dn = +|- 0.839126, dEa = +|- 3.26475 kJ/mol""")]),
)

entry(
    index = 1,
    label = "2FFOH + H <=> W2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(6.36325e+55,'cm^3/(mol*s)'), n=-14.6866, Ea=(63.7035,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 962.5, dn = +|- 0.954213, dEa = +|- 3.71252 kJ/mol"""), Arrhenius(A=(2.73014e+48,'cm^3/(mol*s)'), n=-12.0082, Ea=(59.3237,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 6655.27, dn = +|- 1.2228, dEa = +|- 4.75751 kJ/mol"""), Arrhenius(A=(1.43505e+37,'cm^3/(mol*s)'), n=-8.11636, Ea=(49.8831,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 26823.8, dn = +|- 1.41642, dEa = +|- 5.51081 kJ/mol"""), Arrhenius(A=(9.50725e+23,'cm^3/(mol*s)'), n=-3.68571, Ea=(37.2041,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 6819.61, dn = +|- 1.22619, dEa = +|- 4.7707 kJ/mol""")]),
)

entry(
    index = 2,
    label = "2FFOH + H <=> W3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(9.39478e+41,'cm^3/(mol*s)'), n=-9.74166, Ea=(53.9921,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 7 data points; dA = *|/ 9707.95, dn = +|- 1.26394, dEa = +|- 5.19343 kJ/mol"""), Arrhenius(A=(1.23998e+29,'cm^3/(mol*s)'), n=-5.39726, Ea=(41.8142,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 7 data points; dA = *|/ 9707.21, dn = +|- 1.26393, dEa = +|- 5.19339 kJ/mol"""), Arrhenius(A=(1.00612e+17,'cm^3/(mol*s)'), n=-1.3943, Ea=(29.2504,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 7 data points; dA = *|/ 561.984, dn = +|- 0.871674, dEa = +|- 3.58165 kJ/mol"""), Arrhenius(A=(2.97699e+09,'cm^3/(mol*s)'), n=1.07543, Ea=(21.0678,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(900,'K'), comment="""Fitted to 7 data points; dA = *|/ 16.8125, dn = +|- 0.38853, dEa = +|- 1.59645 kJ/mol""")]),
)

entry(
    index = 3,
    label = "2FFOH + H <=> W4",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(4.21994,'cm^3/(mol*s)'), n=2.85109, Ea=(-3.91519,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 3.9145, dn = +|- 0.189562, dEa = +|- 0.737521 kJ/mol"""), Arrhenius(A=(5.09698e+29,'cm^3/(mol*s)'), n=-6.40842, Ea=(25.0426,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 928.887, dn = +|- 0.949276, dEa = +|- 3.69331 kJ/mol"""), Arrhenius(A=(1.59977e+34,'cm^3/(mol*s)'), n=-7.36633, Ea=(35.7498,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 665.011, dn = +|- 0.902856, dEa = +|- 3.5127 kJ/mol"""), Arrhenius(A=(1.9408e+18,'cm^3/(mol*s)'), n=-1.93364, Ea=(21.381,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(800,'K'), comment="""Fitted to 6 data points; dA = *|/ 231.789, dn = +|- 0.756453, dEa = +|- 2.9431 kJ/mol""")]),
)

entry(
    index = 4,
    label = "2FFOH + H <=> W5",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(8.51644e+28,'cm^3/(mol*s)'), n=-5.60386, Ea=(34.1372,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 151.369, dn = +|- 0.678581, dEa = +|- 3.12367 kJ/mol"""), Arrhenius(A=(2.40061e+23,'cm^3/(mol*s)'), n=-3.64758, Ea=(31.0551,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 248.7, dn = +|- 0.745703, dEa = +|- 3.43265 kJ/mol"""), Arrhenius(A=(2.52275e+18,'cm^3/(mol*s)'), n=-1.87184, Ea=(31.297,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 35.8722, dn = +|- 0.48395, dEa = +|- 2.22774 kJ/mol"""), Arrhenius(A=(2.33716e+10,'cm^3/(mol*s)'), n=0.792558, Ea=(28.5278,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 285.222, dn = +|- 0.764226, dEa = +|- 3.51791 kJ/mol""")]),
)

entry(
    index = 5,
    label = "2FFOH + H <=> W8",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.13554e+50,'cm^3/(mol*s)'), n=-12.4662, Ea=(95.9311,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 49609.9, dn = +|- 1.46159, dEa = +|- 6.72805 kJ/mol"""), Arrhenius(A=(8.02549e+33,'cm^3/(mol*s)'), n=-7.11847, Ea=(90.6045,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 1.11639e+06, dn = +|- 1.88251, dEa = +|- 8.66563 kJ/mol"""), Arrhenius(A=(1.01221e+15,'cm^3/(mol*s)'), n=-1.13019, Ea=(79.0717,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 1.38343e+09, dn = +|- 2.84531, dEa = +|- 13.0976 kJ/mol"""), Arrhenius(A=(839774,'cm^3/(mol*s)'), n=1.78739, Ea=(88.3145,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 1.5253e+10, dn = +|- 3.16978, dEa = +|- 14.5912 kJ/mol""")]),
)

entry(
    index = 6,
    label = "2FFOH + H <=> W12",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(3.76401e+35,'cm^3/(mol*s)'), n=-7.47275, Ea=(42.4422,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 14799.4, dn = +|- 1.29807, dEa = +|- 5.97534 kJ/mol"""), Arrhenius(A=(1.28633e+26,'cm^3/(mol*s)'), n=-4.28629, Ea=(34.6791,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 1013.39, dn = +|- 0.935609, dEa = +|- 4.30683 kJ/mol"""), Arrhenius(A=(4.49774e+20,'cm^3/(mol*s)'), n=-2.38209, Ea=(34.5716,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 204.758, dn = +|- 0.719421, dEa = +|- 3.31167 kJ/mol"""), Arrhenius(A=(1.10727e+11,'cm^3/(mol*s)'), n=0.731638, Ea=(29.3277,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 2325.63, dn = +|- 1.0479, dEa = +|- 4.82376 kJ/mol""")]),
)

entry(
    index = 7,
    label = "2FFOH + H <=> W18",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(2.02243e+31,'cm^3/(mol*s)'), n=-7.1548, Ea=(65.2748,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 2.62774e+10, dn = +|- 3.24331, dEa = +|- 14.9297 kJ/mol"""), Arrhenius(A=(1.42882e+39,'cm^3/(mol*s)'), n=-9.16939, Ea=(88.3683,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 60808.4, dn = +|- 1.48911, dEa = +|- 6.85471 kJ/mol"""), Arrhenius(A=(8.90952e+33,'cm^3/(mol*s)'), n=-7.22236, Ea=(90.6252,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 3151.45, dn = +|- 1.08898, dEa = +|- 5.01285 kJ/mol"""), Arrhenius(A=(2.18888e+21,'cm^3/(mol*s)'), n=-3.00219, Ea=(87.2436,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 167.894, dn = +|- 0.692588, dEa = +|- 3.18815 kJ/mol""")]),
)

entry(
    index = 8,
    label = "2FFOH + H <=> W19",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(6.66568e+33,'cm^3/(mol*s)'), n=-6.92996, Ea=(54.8209,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 315217, dn = +|- 1.72908, dEa = +|- 7.46317 kJ/mol"""), Arrhenius(A=(1.82154e+18,'cm^3/(mol*s)'), n=-1.91428, Ea=(43.8059,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 130295, dn = +|- 1.60843, dEa = +|- 6.94241 kJ/mol"""), Arrhenius(A=(23415.1,'cm^3/(mol*s)'), n=2.50638, Ea=(36.3847,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 63419.4, dn = +|- 1.5101, dEa = +|- 6.51798 kJ/mol"""), Arrhenius(A=(4.4636e-11,'cm^3/(mol*s)'), n=7.07436, Ea=(27.9255,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 49615.2, dn = +|- 1.47657, dEa = +|- 6.37328 kJ/mol""")]),
)

entry(
    index = 9,
    label = "2FFOH + H <=> W20",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(4.0087e+29,'cm^3/(mol*s)'), n=-5.66322, Ea=(47.0306,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 10487.1, dn = +|- 1.26433, dEa = +|- 5.45717 kJ/mol"""), Arrhenius(A=(2.45576e+11,'cm^3/(mol*s)'), n=0.327944, Ea=(34.1723,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 13405.6, dn = +|- 1.29786, dEa = +|- 5.6019 kJ/mol"""), Arrhenius(A=(0.000377878,'cm^3/(mol*s)'), n=5.07682, Ea=(25.4399,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 361.531, dn = +|- 0.804429, dEa = +|- 3.47213 kJ/mol"""), Arrhenius(A=(1.00782e-15,'cm^3/(mol*s)'), n=8.64088, Ea=(20.5302,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1000,'K'), comment="""Fitted to 8 data points; dA = *|/ 379.869, dn = +|- 0.811186, dEa = +|- 3.50129 kJ/mol""")]),
)

entry(
    index = 10,
    label = "2FFOH + H <=> W15",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.20249e+32,'cm^3/(mol*s)'), n=-6.13771, Ea=(76.3383,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 176068, dn = +|- 1.63283, dEa = +|- 7.51629 kJ/mol"""), Arrhenius(A=(7.5586e+10,'cm^3/(mol*s)'), n=0.750561, Ea=(64.1616,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 2.56741e+06, dn = +|- 1.99509, dEa = +|- 9.18386 kJ/mol"""), Arrhenius(A=(3.35156e-10,'cm^3/(mol*s)'), n=7.09967, Ea=(49.9116,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 954048, dn = +|- 1.86126, dEa = +|- 8.56784 kJ/mol"""), Arrhenius(A=(6.94589e-12,'cm^3/(mol*s)'), n=7.44842, Ea=(61.4157,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(1200,'K'), comment="""Fitted to 9 data points; dA = *|/ 9.92646e+17, dn = +|- 5.60187, dEa = +|- 25.7867 kJ/mol""")]),
)

entry(
    index = 11,
    label = "2FFOH + H <=> P3 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.06773e+15,'cm^3/(mol*s)'), n=-0.574468, Ea=(40.6992,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 3.27755, dn = +|- 0.143464, dEa = +|- 1.40872 kJ/mol"""), Arrhenius(A=(2.82076e+14,'cm^3/(mol*s)'), n=-0.416634, Ea=(42.5339,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 8.87852, dn = +|- 0.263899, dEa = +|- 2.59131 kJ/mol"""), Arrhenius(A=(1.03762e+14,'cm^3/(mol*s)'), n=-0.301546, Ea=(45.1518,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 12.5534, dn = +|- 0.305758, dEa = +|- 3.00233 kJ/mol"""), Arrhenius(A=(1.05874e+14,'cm^3/(mol*s)'), n=-0.298866, Ea=(50.4503,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 12.2753, dn = +|- 0.30305, dEa = +|- 2.97574 kJ/mol""")]),
)

entry(
    index = 12,
    label = "2FFOH + H <=> P4 + CHO",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(6.18503e+18,'cm^3/(mol*s)'), n=-1.72431, Ea=(72.1927,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 6.21736, dn = +|- 0.220841, dEa = +|- 2.1685 kJ/mol"""), Arrhenius(A=(7.16704e+19,'cm^3/(mol*s)'), n=-1.93162, Ea=(89.004,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 8.2044, dn = +|- 0.254356, dEa = +|- 2.4976 kJ/mol"""), Arrhenius(A=(6.69431e+19,'cm^3/(mol*s)'), n=-1.86551, Ea=(105.526,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 31.8763, dn = +|- 0.418377, dEa = +|- 4.10817 kJ/mol"""), Arrhenius(A=(2.55322e+18,'cm^3/(mol*s)'), n=-1.46907, Ea=(121.149,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 281.207, dn = +|- 0.681502, dEa = +|- 6.69188 kJ/mol""")]),
)

entry(
    index = 13,
    label = "2FFOH + H <=> P6 + CH2CHOH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(2.61693e+21,'cm^3/(mol*s)'), n=-2.3976, Ea=(110.664,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.6817, dn = +|- 0.119216, dEa = +|- 1.17062 kJ/mol"""), Arrhenius(A=(6.34041e+23,'cm^3/(mol*s)'), n=-2.93964, Ea=(129.889,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 5.4619, dn = +|- 0.205184, dEa = +|- 2.01476 kJ/mol"""), Arrhenius(A=(1.23339e+25,'cm^3/(mol*s)'), n=-3.18565, Ea=(153.212,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 14.6461, dn = +|- 0.324391, dEa = +|- 3.18529 kJ/mol"""), Arrhenius(A=(4.03533e+23,'cm^3/(mol*s)'), n=-2.75378, Ea=(173.952,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 207.813, dn = +|- 0.64495, dEa = +|- 6.33296 kJ/mol""")]),
)

entry(
    index = 14,
    label = "2FFOH + H <=> P7 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.78536e+19,'cm^3/(mol*s)'), n=-1.88979, Ea=(76.2417,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 5.71417, dn = +|- 0.210641, dEa = +|- 2.06835 kJ/mol"""), Arrhenius(A=(3.78884e+21,'cm^3/(mol*s)'), n=-2.40505, Ea=(98.3815,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 6.29141, dn = +|- 0.222271, dEa = +|- 2.18255 kJ/mol"""), Arrhenius(A=(4.70897e+22,'cm^3/(mol*s)'), n=-2.60302, Ea=(122.049,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 7.89062, dn = +|- 0.249643, dEa = +|- 2.45132 kJ/mol"""), Arrhenius(A=(4.94376e+21,'cm^3/(mol*s)'), n=-2.30023, Ea=(144.271,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 62.9856, dn = +|- 0.500683, dEa = +|- 4.91636 kJ/mol""")]),
)

entry(
    index = 15,
    label = "2FFOH + H <=> P10 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.18442e+16,'cm^3/(mol*s)'), n=-0.780694, Ea=(59.3053,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.30038, dn = +|- 0.10068, dEa = +|- 0.988605 kJ/mol"""), Arrhenius(A=(2.56331e+16,'cm^3/(mol*s)'), n=-0.86116, Ea=(61.1006,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1.96771, dn = +|- 0.0818018, dEa = +|- 0.803237 kJ/mol"""), Arrhenius(A=(1.81665e+17,'cm^3/(mol*s)'), n=-1.06305, Ea=(66.0295,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1.62444, dn = +|- 0.0586339, dEa = +|- 0.575744 kJ/mol"""), Arrhenius(A=(2.56734e+18,'cm^3/(mol*s)'), n=-1.33019, Ea=(73.796,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1.64408, dn = +|- 0.0600862, dEa = +|- 0.590004 kJ/mol""")]),
)

entry(
    index = 16,
    label = "2FFOH + H <=> P11 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(2.78094e+15,'cm^3/(mol*s)'), n=-0.540053, Ea=(38.4239,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1.75383, dn = +|- 0.0678954, dEa = +|- 0.666686 kJ/mol"""), Arrhenius(A=(2.21692e+16,'cm^3/(mol*s)'), n=-0.754026, Ea=(43.6505,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.04239, dn = +|- 0.0863036, dEa = +|- 0.847442 kJ/mol"""), Arrhenius(A=(3.09594e+17,'cm^3/(mol*s)'), n=-1.02215, Ea=(50.9604,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.68492, dn = +|- 0.119361, dEa = +|- 1.17204 kJ/mol"""), Arrhenius(A=(4.17569e+18,'cm^3/(mol*s)'), n=-1.27915, Ea=(59.6931,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.96844, dn = +|- 0.131493, dEa = +|- 1.29117 kJ/mol""")]),
)

entry(
    index = 17,
    label = "2FFOH + H <=> P13 + CH2OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(5.12175e+17,'cm^3/(mol*s)'), n=-1.24958, Ea=(63.6703,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.0026, dn = +|- 0.0839263, dEa = +|- 0.824098 kJ/mol"""), Arrhenius(A=(3.0203e+18,'cm^3/(mol*s)'), n=-1.4091, Ea=(73.274,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 4.13565, dn = +|- 0.171568, dEa = +|- 1.68468 kJ/mol"""), Arrhenius(A=(6.24994e+18,'cm^3/(mol*s)'), n=-1.45013, Ea=(84.1136,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 9.94049, dn = +|- 0.277553, dEa = +|- 2.72538 kJ/mol"""), Arrhenius(A=(2.47992e+18,'cm^3/(mol*s)'), n=-1.31441, Ea=(95.9144,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 36.2354, dn = +|- 0.433867, dEa = +|- 4.26028 kJ/mol""")]),
)

entry(
    index = 18,
    label = "2FFOH + H <=> P14 + P21",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.89095e+14,'cm^3/(mol*s)'), n=-1.23998, Ea=(86.5646,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.40541, dn = +|- 0.106075, dEa = +|- 1.04158 kJ/mol"""), Arrhenius(A=(3.28529e+15,'cm^3/(mol*s)'), n=-1.52209, Ea=(96.141,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.04077, dn = +|- 0.0862078, dEa = +|- 0.8465 kJ/mol"""), Arrhenius(A=(9.5185e+16,'cm^3/(mol*s)'), n=-1.84821, Ea=(109.063,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.52762, dn = +|- 0.112065, dEa = +|- 1.1004 kJ/mol"""), Arrhenius(A=(3.98993e+18,'cm^3/(mol*s)'), n=-2.19414, Ea=(127.801,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 5.32949, dn = +|- 0.202218, dEa = +|- 1.98564 kJ/mol""")]),
)

entry(
    index = 19,
    label = "2FFOH + H <=> P15 + CH2CHO",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(5.33084e+16,'cm^3/(mol*s)'), n=-0.963941, Ea=(72.3159,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.74923, dn = +|- 0.122221, dEa = +|- 1.20013 kJ/mol"""), Arrhenius(A=(7.56876e+17,'cm^3/(mol*s)'), n=-1.23426, Ea=(79.5628,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1.76512, dn = +|- 0.0686707, dEa = +|- 0.674299 kJ/mol"""), Arrhenius(A=(1.04609e+19,'cm^3/(mol*s)'), n=-1.49144, Ea=(88.8561,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.0405, dn = +|- 0.0861919, dEa = +|- 0.846345 kJ/mol"""), Arrhenius(A=(4.80864e+19,'cm^3/(mol*s)'), n=-1.62218, Ea=(98.7286,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 4.84814, dn = +|- 0.190778, dEa = +|- 1.87331 kJ/mol""")]),
)

entry(
    index = 20,
    label = "2FFOH + H <=> P19 + OH",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.17539e+17,'cm^3/(mol*s)'), n=-0.908493, Ea=(50.7112,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.23362, dn = +|- 0.0971205, dEa = +|- 0.953655 kJ/mol"""), Arrhenius(A=(5.93576e+16,'cm^3/(mol*s)'), n=-0.824758, Ea=(52.1918,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 3.08548, dn = +|- 0.136166, dEa = +|- 1.33706 kJ/mol"""), Arrhenius(A=(9.22841e+16,'cm^3/(mol*s)'), n=-0.863234, Ea=(55.8106,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.70059, dn = +|- 0.120064, dEa = +|- 1.17894 kJ/mol"""), Arrhenius(A=(4.54091e+17,'cm^3/(mol*s)'), n=-1.01679, Ea=(63.0792,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 3.28745, dn = +|- 0.143829, dEa = +|- 1.4123 kJ/mol""")]),
)

entry(
    index = 21,
    label = "2FFOH + H <=> P22 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.51612e+20,'cm^3/(mol*s)'), n=-2.11289, Ea=(56.3534,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 42.1327, dn = +|- 0.45209, dEa = +|- 4.43921 kJ/mol"""), Arrhenius(A=(3.68075e+21,'cm^3/(mol*s)'), n=-2.40313, Ea=(73.4562,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 26.5486, dn = +|- 0.396275, dEa = +|- 3.89114 kJ/mol"""), Arrhenius(A=(1.53013e+22,'cm^3/(mol*s)'), n=-2.4968, Ea=(91.6386,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 12.8212, dn = +|- 0.308309, dEa = +|- 3.02738 kJ/mol"""), Arrhenius(A=(4.43727e+21,'cm^3/(mol*s)'), n=-2.30759, Ea=(110.144,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 19.5111, dn = +|- 0.359053, dEa = +|- 3.52565 kJ/mol""")]),
)

entry(
    index = 22,
    label = "2FFOH + H <=> P16 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(5.40645e+20,'cm^3/(mol*s)'), n=-2.22563, Ea=(108.113,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.19485, dn = +|- 0.0950044, dEa = +|- 0.932877 kJ/mol"""), Arrhenius(A=(1.72656e+23,'cm^3/(mol*s)'), n=-2.79559, Ea=(128.127,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 4.75163, dn = +|- 0.188348, dEa = +|- 1.84945 kJ/mol"""), Arrhenius(A=(3.85068e+24,'cm^3/(mol*s)'), n=-3.05537, Ea=(151.789,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 16.9984, dn = +|- 0.342392, dEa = +|- 3.36205 kJ/mol"""), Arrhenius(A=(1.55942e+23,'cm^3/(mol*s)'), n=-2.64459, Ea=(172.916,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 277.575, dn = +|- 0.679931, dEa = +|- 6.67645 kJ/mol""")]),
)

entry(
    index = 23,
    label = "2FFOH + H <=> P24 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(1.64419e+23,'cm^3/(mol*s)'), n=-2.60565, Ea=(129.529,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.60369, dn = +|- 0.115648, dEa = +|- 1.13558 kJ/mol"""), Arrhenius(A=(2.37926e+25,'cm^3/(mol*s)'), n=-3.08538, Ea=(149.448,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 6.80178, dn = +|- 0.231698, dEa = +|- 2.27511 kJ/mol"""), Arrhenius(A=(1.02758e+26,'cm^3/(mol*s)'), n=-3.16904, Ea=(171.665,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 52.9169, dn = +|- 0.479633, dEa = +|- 4.70966 kJ/mol"""), Arrhenius(A=(4.77505e+23,'cm^3/(mol*s)'), n=-2.534, Ea=(190.158,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1564.36, dn = +|- 0.888903, dEa = +|- 8.72841 kJ/mol""")]),
)

entry(
    index = 24,
    label = "2FFOH + H <=> P25 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(7.56949e+15,'cm^3/(mol*s)'), n=-1.78257, Ea=(76.046,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 5.28419, dn = +|- 0.201187, dEa = +|- 1.97551 kJ/mol"""), Arrhenius(A=(1.09271e+17,'cm^3/(mol*s)'), n=-2.01438, Ea=(92.8548,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 7.71805, dn = +|- 0.246971, dEa = +|- 2.42508 kJ/mol"""), Arrhenius(A=(1.18337e+17,'cm^3/(mol*s)'), n=-1.96395, Ea=(109.349,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 30.9285, dn = +|- 0.414729, dEa = +|- 4.07235 kJ/mol"""), Arrhenius(A=(4.90889e+15,'cm^3/(mol*s)'), n=-1.57638, Ea=(124.897,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 269.066, dn = +|- 0.676168, dEa = +|- 6.6395 kJ/mol""")]),
)

entry(
    index = 25,
    label = "2FFOH + H <=> P18 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.00101325,0.101325,1.01325,10.1325],'bar'), arrhenius=[Arrhenius(A=(9.57928e+16,'cm^3/(mol*s)'), n=-1.39264, Ea=(86.9464,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.09494, dn = +|- 0.0893742, dEa = +|- 0.877593 kJ/mol"""), Arrhenius(A=(1.58967e+18,'cm^3/(mol*s)'), n=-1.67001, Ea=(96.4135,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 1.97711, dn = +|- 0.082378, dEa = +|- 0.808894 kJ/mol"""), Arrhenius(A=(4.14796e+19,'cm^3/(mol*s)'), n=-1.98507, Ea=(109.148,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 2.53381, dn = +|- 0.11236, dEa = +|- 1.1033 kJ/mol"""), Arrhenius(A=(1.55826e+21,'cm^3/(mol*s)'), n=-2.31931, Ea=(127.72,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(25000,'K'), comment="""Fitted to 15 data points; dA = *|/ 4.92401, dn = +|- 0.192655, dEa = +|- 1.89174 kJ/mol""")]),
)
