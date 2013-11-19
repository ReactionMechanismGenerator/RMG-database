#!/usr/bin/env python
# encoding: utf-8

name = "thermo_DFT_CCSDTF12_BAC"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 3,
    label = "CH2(S)",
    molecule = """
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.09,8.32,8.62,8.99,9.79,10.50,11.83],'cal/(mol*K)'),
        H298 = (102.30,'kcal/mol'),
        S298 = (45.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 4,
    label = "CH2(T)",
    molecule = """
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.34,8.61,8.91,9.24,9.89,10.50,11.68],'cal/(mol*K)'),
        H298 = (93.88,'kcal/mol'),
        S298 = (46.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 5,
    label = "CH3",
    molecule = """
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.33,10.06,10.82,11.55,12.89,14.04,16.19],'cal/(mol*K)'),
        H298 = (35.15,'kcal/mol'),
        S298 = (46.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 6,
    label = "CH4",
    molecule = """
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.62,9.65,10.94,12.34,14.89,16.97,20.54],'cal/(mol*K)'),
        H298 = (-17.76,'kcal/mol'),
        S298 = (44.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 7,
    label = "OH",
    molecule = """
1 O 1 {2,S}
2 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,6.95,6.95,6.97,7.08,7.25,7.72],'cal/(mol*K)'),
        H298 = (8.76,'kcal/mol'),
        S298 = (42.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 8,
    label = "H2O",
    molecule = """
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.04,8.18,8.38,8.62,9.20,9.77,11.02],'cal/(mol*K)'),
        H298 = (-58.08,'kcal/mol'),
        S298 = (45.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 9,
    label = "CO",
    molecule = """
1 C 2T {2,D}
2 O 0  {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.02,7.12,7.26,7.58,7.86,8.35],'cal/(mol*K)'),
        H298 = (-26.31,'kcal/mol'),
        S298 = (47.20,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 10,
    label = "HCO",
    molecule = """
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.28,8.68,9.18,9.70,10.62,11.34,12.48],'cal/(mol*K)'),
        H298 = (10.02,'kcal/mol'),
        S298 = (52.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 11,
    label = "CH2O",
    molecule = """
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.52,9.35,10.36,11.42,13.24,14.67,16.93],'cal/(mol*K)'),
        H298 = (-26.30,'kcal/mol'),
        S298 = (52.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 12,
    label = "HCOH(S)",
    molecule = """
1 C 2S {2,S} {3,S}
2 O 0  {1,S} {4,S}
3 H 0  {1,S}
4 H 0  {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.80,9.89,11.16,12.37,14.34,15.80,17.89],'cal/(mol*K)'),
        H298 = (25.99,'kcal/mol'),
        S298 = (53.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 14,
    label = "CH3O",
    molecule = """
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.92,11.56,13.22,14.75,17.21,19.05,21.90],'cal/(mol*K)'),
        H298 = (4.86,'kcal/mol'),
        S298 = (54.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 15,
    label = "CH2OH",
    molecule = """
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.47,12.95,14.27,15.41,17.28,18.70,20.94],'cal/(mol*K)'),
        H298 = (-3.84,'kcal/mol'),
        S298 = (58.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 16,
    label = "CH3OH",
    molecule = """
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,12.61,14.34,15.99,18.85,21.11,24.85],'cal/(mol*K)'),
        H298 = (-48.23,'kcal/mol'),
        S298 = (57.40,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 18,
    label = "HO2",
    molecule = """
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.38,8.86,9.37,9.86,10.69,11.30,12.28],'cal/(mol*K)'),
        H298 = (2.85,'kcal/mol'),
        S298 = (54.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 19,
    label = "HOOH",
    molecule = """
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.91,10.83,11.68,12.44,13.71,14.69,16.28],'cal/(mol*K)'),
        H298 = (-32.58,'kcal/mol'),
        S298 = (55.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 20,
    label = "CO2",
    molecule = """
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.86,9.86,10.64,11.27,12.25,12.93,13.82],'cal/(mol*K)'),
        H298 = (-93.92,'kcal/mol'),
        S298 = (52.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 21,
    label = "HOCO",
    molecule = """
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 O 0 {1,S} {4,S}
4 H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.19,12.82,14.01,14.88,16.16,17.00,17.94],'cal/(mol*K)'),
        H298 = (-43.80,'kcal/mol'),
        S298 = (60.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 22,
    label = "formyloxy",
    molecule = """
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.41,12.76,13.87,14.80,16.22,17.21,18.49],'cal/(mol*K)'),
        H298 = (-30.36,'kcal/mol'),
        S298 = (61.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 23,
    label = "formic_acid",
    molecule = """
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S} {5,S}
4 H 0 {1,S}
5 H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.04,13.15,15.17,16.90,19.43,21.14,23.31],'cal/(mol*K)'),
        H298 = (-90.45,'kcal/mol'),
        S298 = (59.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 24,
    label = "CH3OO",
    molecule = """
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.33,14.37,16.28,17.99,20.80,22.96,26.30],'cal/(mol*K)'),
        H298 = (3.33,'kcal/mol'),
        S298 = (64.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 26,
    label = "CH3OOH",
    molecule = """
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.42,15.67,17.71,19.52,22.55,24.90,28.71],'cal/(mol*K)'),
        H298 = (-30.69,'kcal/mol'),
        S298 = (62.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 35,
    label = "HC2",
    molecule = """
1 C 1 {2,T}
2 C 0 {1,T} {3,S}
3 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.23,10.59,10.89,11.17,11.72,12.21,13.19],'cal/(mol*K)'),
        H298 = (135.60,'kcal/mol'),
        S298 = (51.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 36,
    label = "C2H2",
    molecule = """
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.21,11.55,12.69,13.60,15.02,16.08,17.75],'cal/(mol*K)'),
        H298 = (54.53,'kcal/mol'),
        S298 = (47.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 38,
    label = "H2CC(S)",
    molecule = """
1 C 2S {2,D}
2 C 0  {1,D} {3,S} {4,S}
3 H 0  {2,S}
4 H 0  {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.50,11.47,12.33,13.11,14.41,15.44,17.17],'cal/(mol*K)'),
        H298 = (98.44,'kcal/mol'),
        S298 = (53.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 40,
    label = "C2H3",
    molecule = """
1 C 1 {2,D} {3,S}
2 C 0 {1,D} {4,S} {5,S}
3 H 0 {1,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.46,12.23,13.84,15.21,17.44,19.13,21.78],'cal/(mol*K)'),
        H298 = (71.03,'kcal/mol'),
        S298 = (55.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 41,
    label = "CCH3",
    molecule = """
1 C 3 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.46,12.19,13.80,15.22,17.55,19.32,22.02],'cal/(mol*K)'),
        H298 = (120.41,'kcal/mol'),
        S298 = (55.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 42,
    label = "C2H4",
    molecule = """
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.35,12.47,14.63,16.63,19.85,22.28,26.11],'cal/(mol*K)'),
        H298 = (12.27,'kcal/mol'),
        S298 = (52.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 44,
    label = "CHCH3(S)",
    molecule = """
1 C 2S {2,S} {3,S}
2 C 0  {1,S} {4,S} {5,S} {6,S}
3 H 0  {1,S}
4 H 0  {2,S}
5 H 0  {2,S}
6 H 0  {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.74,15.06,16.56,18.00,20.43,22.37,25.58],'cal/(mol*K)'),
        H298 = (88.33,'kcal/mol'),
        S298 = (89.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 46,
    label = "C2H5",
    molecule = """
1 C 1 {2,S} {3,S} {4,S}
2 C 0 {1,S} {5,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.32,14.72,17.07,19.22,22.82,25.63,30.14],'cal/(mol*K)'),
        H298 = (28.86,'kcal/mol'),
        S298 = (59.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 47,
    label = "C2H6",
    molecule = """
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.72,15.55,18.38,21.01,25.47,28.95,34.56],'cal/(mol*K)'),
        H298 = (-20.15,'kcal/mol'),
        S298 = (54.85,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 49,
    label = "C2O(T)",
    molecule = """
1 C 2T {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.30,11.13,11.72,12.22,12.98,13.50,14.16],'cal/(mol*K)'),
        H298 = (90.98,'kcal/mol'),
        S298 = (55.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 50,
    label = "HCCO",
    molecule = """
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.79,13.03,13.93,14.65,15.78,16.62,17.89],'cal/(mol*K)'),
        H298 = (42.88,'kcal/mol'),
        S298 = (58.85,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 220,
    label = "HCN",
    molecule =         """
        1 H 0 0 {2,S}
        2 C 0 0 {1,S} {3,T}
        3 N 0 1 {2,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.41,9.16,9.78,10.31,11.20,11.89,13.01],'cal/(mol*K)'),
        H298 = (30.72,'kcal/mol'),
        S298 = (48.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 221,
    label = "HNC",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 0 0 {1,S} {3,T}
        3 C 0 1 {2,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.38,10.05,10.51,10.89,11.53,12.05,13.01],'cal/(mol*K)'),
        H298 = (46.88,'kcal/mol'),
        S298 = (48.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 222,
    label = "HNCO",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 0 1 {1,S} {3,D}
        3 C 0 0 {2,D} {4,D}
        4 O 0 2 {3,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.85,12.06,13.10,13.94,15.25,16.19,17.56],'cal/(mol*K)'),
        H298 = (-27.92,'kcal/mol'),
        S298 = (57.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 223,
    label = "HOCN",
    molecule =         """
        1 H 0 0 {2,S}
        2 O 0 2 {1,S} {3,S}
        3 C 0 0 {2,S} {4,T}
        4 N 0 1 {3,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.98,12.15,13.12,13.91,15.16,16.09,17.50],'cal/(mol*K)'),
        H298 = (-3.79,'kcal/mol'),
        S298 = (57.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 224,
    label = "HCNO",
    molecule =         """
        1 H 0 0 {2,S}
        2 C 0 0 {1,S} {3,T}
        3 N 0 0 {2,T} {4,S}
        4 O 0 3 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.86,14.01,14.79,15.47,16.57,17.40,18.71],'cal/(mol*K)'),
        H298 = (41.57,'kcal/mol'),
        S298 = (56.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 225,
    label = "HONC",
    molecule =         """
        1 H 0 0 {2,S}
        2 O 0 2 {1,S} {3,S}
        3 N 0 0 {2,S} {4,T}
        4 C 0 1 {3,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.95,12.81,13.56,14.23,15.35,16.22,17.63],'cal/(mol*K)'),
        H298 = (55.84,'kcal/mol'),
        S298 = (59.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 229,
    label = "CH2NJ",
    molecule =         """
        1 H 0 0 {3,S}
        2 H 0 0 {3,S}
        3 C 0 0 {1,S} {2,S} {4,D}
        4 N 1 1 {3,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.04,10.04,11.11,12.14,13.88,15.12,17.09],'cal/(mol*K)'),
        H298 = (57.47,'kcal/mol'),
        S298 = (53.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 231,
    label = "HCNHJ_cis",
    molecule =         """
        1 H 0 0 {2,S}
        2 C 1 0 {1,S} {3,D}
        3 N 0 1 {2,D} {4,S}
        4 H 0 0 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.50,10.64,11.71,12.62,14.12,15.27,17.08],'cal/(mol*K)'),
        H298 = (69.86,'kcal/mol'),
        S298 = (54.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 254,
    label = "CH3NHJ",
    molecule =         """
        1 C 0 0 {2,S} {3,S} {4,S} {5,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 H 0 0 {1,S}
        5 N 1 1 {1,S} {6,S}
        6 H 0 0 {5,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.21,12.99,14.79,16.49,19.41,21.71,25.44],'cal/(mol*K)'),
        H298 = (42.57,'kcal/mol'),
        S298 = (58.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 255,
    label = "CH2NH2J",
    molecule =         """
        1 C 1 0 {2,S} {3,S} {4,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 N 0 1 {1,S} {5,S} {6,S}
        5 H 0 0 {4,S}
        6 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.36,14.98,16.48,17.87,20.33,22.33,25.62],'cal/(mol*K)'),
        H298 = (35.75,'kcal/mol'),
        S298 = (58.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 259,
    label = "CH3NH2",
    molecule =         """
        1 C 0 0 {2,S} {3,S} {4,S} {5,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 H 0 0 {1,S}
        5 N 0 1 {1,S} {6,S} {7,S}
        6 H 0 0 {5,S}
        7 H 0 0 {5,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.00,14.22,16.43,18.51,22.07,24.91,29.60],'cal/(mol*K)'),
        H298 = (-4.98,'kcal/mol'),
        S298 = (57.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 264,
    label = "CNJ",
    molecule =         """
        1 C 1 0 {2,T}
        2 N 0 1 {1,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.03,7.14,7.29,7.62,7.90,8.38],'cal/(mol*K)'),
        H298 = (106.48,'kcal/mol'),
        S298 = (48.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 265,
    label = "NCOJ",
    molecule =         """
        1 N 0 1 {2,T}
        2 C 0 0 {1,T} {3,S}
        3 O 1 0 {2,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.38,10.34,11.13,11.76,12.70,13.33,14.08],'cal/(mol*K)'),
        H298 = (30.34,'kcal/mol'),
        S298 = (54.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 266,
    label = "CNNJJ",
    molecule =         """
        1 C 1 0 {2,T}
        2 N 0 0 {1,T} {3,S}
        3 N 1 2 {2,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.16,11.12,11.80,12.36,13.19,13.72,14.32],'cal/(mol*K)'),
        H298 = (137.34,'kcal/mol'),
        S298 = (55.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 267,
    label = "NCNJJ",
    molecule =         """
        1 N 1 1 {2,D}
        2 C 0 0 {1,D} {3,D}
        3 N 1 1 {2,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.91,10.92,11.68,12.26,13.12,13.68,14.30],'cal/(mol*K)'),
        H298 = (108.49,'kcal/mol'),
        S298 = (53.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 291,
    label = "CH3NHCH3",
    molecule =         """
        1 C 0 0 {2,S} {3,S} {4,S} {5,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 H 0 0 {1,S}
        5 N 0 1 {1,S} {6,S} {7,S}
        6 H 0 0 {5,S}
        7 C 0 0 {5,S} {8,S} {9,S} {10,S}
        8 H 0 0 {7,S}
        9 H 0 0 {7,S}
        10 H 0 0 {7,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.98,20.89,24.52,27.76,33.17,37.37,44.05],'cal/(mol*K)'),
        H298 = (-3.89,'kcal/mol'),
        S298 = (65.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 297,
    label = "NCCN",
    molecule =         """
        1 N 0 1 {2,T} 
        2 C 0 0 {1,T} {3,S} 
        3 C 0 0 {2,S} {4,T}
        4 N 0 1 {3,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.21,14.49,15.36,16.10,17.27,18.11,19.30],'cal/(mol*K)'),
        H298 = (73.74,'kcal/mol'),
        S298 = (57.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 318,
    label = "HONO",
    molecule =         """
        1 O 0 2 {2,D}
        2 N 0 1 {1,D} {3,S}
        3 O 0 2 {2,S} {4,S}
        4 H 0 0 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.28,12.62,13.73,14.62,15.99,16.93,18.12],'cal/(mol*K)'),
        H298 = (-18.17,'kcal/mol'),
        S298 = (59.89,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 319,
    label = "NO2OH",
    molecule =         """
        1 O 0 3 {3,S}
        2 O 0 2 {3,D}
        3 N 0 0 {1,S} {2,D} {4,S}
        4 O 0 2 {3,S} {5,S}
        5 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.80,15.22,17.09,18.44,20.42,21.72,23.22],'cal/(mol*K)'),
        H298 = (-31.75,'kcal/mol'),
        S298 = (63.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 320,
    label = "NHJJ",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 2 1 {1,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,6.95,6.96,7.01,7.17,7.39,7.89],'cal/(mol*K)'),
        H298 = (85.74,'kcal/mol'),
        S298 = (43.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 321,
    label = "NH2J",
    molecule =         """
        1 H 0 0 {3,S}
        2 H 0 0 {3,S}
        3 N 1 1 {1,S} {2,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.06,8.23,8.47,8.76,9.44,10.08,11.40],'cal/(mol*K)'),
        H298 = (44.39,'kcal/mol'),
        S298 = (46.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 322,
    label = "NH2OJ",
    molecule =         """
        1 H 0 0 {3,S}
        2 H 0 0 {3,S}
        3 N 0 1 {1,S} {2,S} {4,S}
        4 O 1 2 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.22,10.79,11.63,12.41,13.77,14.90,16.83],'cal/(mol*K)'),
        H298 = (16.44,'kcal/mol'),
        S298 = (62.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 323,
    label = "NH3",
    molecule =         """
        1 H 0 0 {3,S}
        2 H 0 0 {3,S}
        3 N 0 1 {1,S} {2,S} {4,S}
        4 H 0 0 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.49,9.05,9.74,10.48,11.92,13.16,15.50],'cal/(mol*K)'),
        H298 = (-10.69,'kcal/mol'),
        S298 = (45.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 324,
    label = "NH2OH",
    molecule =         """
        1 H 0 0 {3,S}
        2 H 0 0 {3,S}
        3 N 0 1 {1,S} {2,S} {4,S}
        4 O 0 2 {3,S} {5,S}
        5 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.56,12.28,13.96,15.47,17.76,19.35,21.59],'cal/(mol*K)'),
        H298 = (-9.68,'kcal/mol'),
        S298 = (56.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 325,
    label = "NOJ",
    molecule =         """
        1 N 1 0 {2,D}
        2 O 0 2 {1,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.20,7.37,7.72,8.00,8.46],'cal/(mol*K)'),
        H298 = (21.85,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 326,
    label = "NO2J",
    molecule =         """
        1 N 1 0 {2,D} {3,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.86,9.57,10.29,10.92,11.84,12.44,13.19],'cal/(mol*K)'),
        H298 = (8.33,'kcal/mol'),
        S298 = (57.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 327,
    label = "NO3J",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 O 1 2 {1,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.01,14.61,15.74,16.59,17.81,18.55,19.25],'cal/(mol*K)'),
        H298 = (19.35,'kcal/mol'),
        S298 = (62.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 328,
    label = "N2",
    molecule =         """
        1 N 0 1 {2,T}
        2 N 0 1 {1,T}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.94,6.98,7.07,7.18,7.46,7.73,8.25],'cal/(mol*K)'),
        H298 = (0.00,'kcal/mol'),
        S298 = (45.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 329,
    label = "NNHJ",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 0 1 {1,S} {3,D}
        3 N 1 1 {2,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.28,8.68,9.17,9.69,10.59,11.30,12.45],'cal/(mol*K)'),
        H298 = (59.61,'kcal/mol'),
        S298 = (53.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 332,
    label = "NH2NHJ",
    molecule =         """
        1 N 0 1 {2,S} {3,S} {4,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 N 1 1 {1,S} {5,S}
        5 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.78,11.00,12.20,13.29,15.18,16.70,19.32],'cal/(mol*K)'),
        H298 = (53.53,'kcal/mol'),
        S298 = (56.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 335,
    label = "NO2NO",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 N 0 1 {1,S} {5,D}
        5 O 0 2 {4,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.99,18.58,19.80,20.79,22.23,23.10,23.95],'cal/(mol*K)'),
        H298 = (19.90,'kcal/mol'),
        S298 = (71.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 336,
    label = "NO2NO2",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 N 0 0 {1,S} {5,D} {6,S}
        5 O 0 2 {4,D}
        6 O 0 3 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.78,21.47,23.46,24.94,27.10,28.46,29.85],'cal/(mol*K)'),
        H298 = (2.35,'kcal/mol'),
        S298 = (73.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 337,
    label = "NO2ONO2",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 O 0 2 {1,S} {5,S}
        5 N 0 0 {4,S} {6,D} {7,S}
        6 O 0 2 {5,D}
        7 O 0 3 {5,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.31,23.22,25.61,27.57,30.39,32.14,33.98],'cal/(mol*K)'),
        H298 = (3.90,'kcal/mol'),
        S298 = (84.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 338,
    label = "NNNJ",
    molecule =         """
        1 N 1 1 {2,D}
        2 N 0 0 {1,D} {3,D}
        3 N 0 2 {2,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.46,10.45,11.26,11.90,12.85,13.47,14.18],'cal/(mol*K)'),
        H298 = (107.66,'kcal/mol'),
        S298 = (52.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 339,
    label = "HNNN",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 0 1 {1,S} {3,D}
        3 N 0 0 {2,D} {4,D}
        4 N 0 2 {3,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.61,11.83,12.83,13.69,15.07,16.08,17.59],'cal/(mol*K)'),
        H298 = (69.78,'kcal/mol'),
        S298 = (57.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 343,
    label = "NNH2",
    molecule =         """
        1 N 0 0 {2,S} {3,S} {4,D}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 N 0 2 {1,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.61,9.45,10.46,11.48,13.24,14.63,16.86],'cal/(mol*K)'),
        H298 = (71.66,'kcal/mol'),
        S298 = (52.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 345,
    label = "HNOHJ",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 1 1 {1,S} {3,S}
        3 O 0 2 {2,S} {4,S}
        4 H 0 0 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.30,10.39,11.56,12.68,14.59,15.98,17.94],'cal/(mol*K)'),
        H298 = (23.24,'kcal/mol'),
        S298 = (55.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 346,
    label = "NOHJJ",
    molecule =         """
        1 N 2 1 {2,S}
        2 O 0 2 {1,S} {3,S}
        3 H 0 0 {2,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.51,9.06,9.62,10.11,10.88,11.44,12.34],'cal/(mol*K)'),
        H298 = (52.27,'kcal/mol'),
        S298 = (55.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 347,
    label = "HNO",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 0 0 {1,S} {3,D}
        3 O 0 2 {2,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.09,8.42,8.87,9.37,10.34,11.11,12.35],'cal/(mol*K)'),
        H298 = (25.34,'kcal/mol'),
        S298 = (52.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 348,
    label = "N_CH3_3",
    molecule =         """
        1 N 0 1 {2,S} {6,S} {10,S}
        2 C 0 0 {1,S} {3,S} {4,S} {5,S}
        3 H 0 0 {2,S}
        4 H 0 0 {2,S}
        5 H 0 0 {2,S}
        6 C 0 0 {1,S} {7,S} {8,S} {9,S}
        7 H 0 0 {6,S}
        8 H 0 0 {6,S}
        9 H 0 0 {6,S}
        10 C 0 0 {1,S} {11,S} {12,S} {13,S}
        11 H 0 0 {10,S}
        12 H 0 0 {10,S}
        13 H 0 0 {10,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.32,28.98,33.84,38.08,44.97,50.15,58.10],'cal/(mol*K)'),
        H298 = (-5.79,'kcal/mol'),
        S298 = (70.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 352,
    label = "CNOJ",
    molecule =         """
        1 C 1 1 {2,D}
        2 N 0 0 {1,D} {3,D}
        3 O 0 2 {2,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.32,11.09,11.69,12.20,12.98,13.51,14.19],'cal/(mol*K)'),
        H298 = (93.81,'kcal/mol'),
        S298 = (55.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 353,
    label = "CH2NH",
    molecule =         """
        1 C 0 0 {2,S} {3,S} {4,D}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 N 0 1 {1,D} {5,S}
        5 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.24,10.64,12.18,13.70,16.32,18.27,21.35],'cal/(mol*K)'),
        H298 = (21.23,'kcal/mol'),
        S298 = (54.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 354,
    label = "ONNO_cis",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 N 0 1 {2,S} {4,D}
4 O 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.35,15.28,16.71,17.60,18.54,18.94,18.86],'cal/(mol*K)'),
        H298 = (42.50,'kcal/mol'),
        S298 = (63.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 355,
    label = "ONNOJJ_cis",
    molecule = """
 1 O 1 2 {2,S}
2 N 0 1 {1,S} {3,D}
3 N 0 1 {2,D} {4,S}
4 O 1 2 {3,S}
 """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.42,15.25,15.94,16.53,17.45,18.09,18.94],'cal/(mol*K)'),
        H298 = (218.89,'kcal/mol'),
        S298 = (69.60,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 356,
    label = "HCNN",
    molecule = """
1 H 0 0 {2,S}
2 C 1 0 {1,S} {3,D}
3 N 0 0 {2,D} {4,D}
4 N 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.16,12.45,13.52,14.39,15.74,16.69,18.01],'cal/(mol*K)'),
        H298 = (111.77,'kcal/mol'),
        S298 = (58.80,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 358,
    label = "HNO2",
    molecule = """
1 H 0 0 {2,S}
2 N 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 3 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.27,10.47,11.71,12.86,14.66,15.91,17.69],'cal/(mol*K)'),
        H298 = (-10.40,'kcal/mol'),
        S298 = (58.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 360,
    label = "ONOOH",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {5,S}
5 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.64,17.29,18.52,19.53,21.04,22.05,23.23],'cal/(mol*K)'),
        H298 = (-2.60,'kcal/mol'),
        S298 = (69.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: 
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 361,
    label = "ONONO",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 O 0 2 {2,S} {4,S}
4 N 0 1 {3,S} {5,D}
5 O 0 2 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.59,21.61,23.42,24.36,25.35,25.62,24.92],'cal/(mol*K)'),
        H298 = (21.77,'kcal/mol'),
        S298 = (69.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 363,
    label = "NO2OOH",
    molecule = """
1 N 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 0 3 {1,S}
4 O 0 2 {1,S} {5,S}
5 O 0 2 {4,S} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.02,20.77,22.60,23.99,26.02,27.29,28.58],'cal/(mol*K)'),
        H298 = (-12.10,'kcal/mol'),
        S298 = (72.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

