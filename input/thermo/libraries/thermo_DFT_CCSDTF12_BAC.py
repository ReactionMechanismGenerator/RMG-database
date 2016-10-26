#!/usr/bin/env python
# encoding: utf-8

name = "thermo_DFT_CCSDTF12_BAC"
shortDesc = u""
longDesc = u"""
work done by B. Buesser using DFT and CCSDTF12 using or deriving bond additvity corrections
"""
entry(
    index = 3,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.09,8.32,8.62,8.99,9.79,10.5,11.83],'cal/(mol*K)'),
        H298 = (102.3,'kcal/mol'),
        S298 = (45.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 4,
    label = "CH2(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.34,8.61,8.91,9.24,9.89,10.5,11.68],'cal/(mol*K)'),
        H298 = (93.88,'kcal/mol'),
        S298 = (46.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 5,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
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
)

entry(
    index = 6,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
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
)

entry(
    index = 7,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,6.95,6.95,6.97,7.08,7.25,7.72],'cal/(mol*K)'),
        H298 = (8.76,'kcal/mol'),
        S298 = (43.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC ===
! NOTE THAT multiplicity = 4 because we do not account for the spin orbit coupling; hence 2 for spin degeneracy and 2 for spatial degeneracy.
""",
)

entry(
    index = 8,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.04,8.18,8.38,8.62,9.2,9.77,11.02],'cal/(mol*K)'),
        H298 = (-58.08,'kcal/mol'),
        S298 = (45.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 9,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.02,7.12,7.26,7.58,7.86,8.35],'cal/(mol*K)'),
        H298 = (-26.31,'kcal/mol'),
        S298 = (47.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 10,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.28,8.68,9.18,9.7,10.62,11.34,12.48],'cal/(mol*K)'),
        H298 = (10.02,'kcal/mol'),
        S298 = (52.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 11,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.52,9.35,10.36,11.42,13.24,14.67,16.93],'cal/(mol*K)'),
        H298 = (-26.3,'kcal/mol'),
        S298 = (52.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 12,
    label = "HCOH(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.8,9.89,11.16,12.37,14.34,15.8,17.89],'cal/(mol*K)'),
        H298 = (25.99,'kcal/mol'),
        S298 = (53.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 14,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.92,11.56,13.22,14.75,17.21,19.05,21.9],'cal/(mol*K)'),
        H298 = (4.86,'kcal/mol'),
        S298 = (54.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 15,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.47,12.95,14.27,15.41,17.28,18.7,20.94],'cal/(mol*K)'),
        H298 = (-3.84,'kcal/mol'),
        S298 = (58.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 16,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,12.61,14.34,15.99,18.85,21.11,24.85],'cal/(mol*K)'),
        H298 = (-48.23,'kcal/mol'),
        S298 = (57.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 18,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.38,8.86,9.37,9.86,10.69,11.3,12.28],'cal/(mol*K)'),
        H298 = (2.85,'kcal/mol'),
        S298 = (54.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 19,
    label = "HOOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
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
)

entry(
    index = 20,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.86,9.86,10.64,11.27,12.25,12.93,13.82],'cal/(mol*K)'),
        H298 = (-93.92,'kcal/mol'),
        S298 = (51.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 21,
    label = "HOCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.19,12.82,14.01,14.88,16.16,17,17.94],'cal/(mol*K)'),
        H298 = (-43.8,'kcal/mol'),
        S298 = (60.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 22,
    label = "formyloxy",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.41,12.76,13.87,14.8,16.22,17.21,18.49],'cal/(mol*K)'),
        H298 = (-30.36,'kcal/mol'),
        S298 = (61.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 23,
    label = "formic_acid",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.04,13.15,15.17,16.9,19.43,21.14,23.31],'cal/(mol*K)'),
        H298 = (-90.45,'kcal/mol'),
        S298 = (59.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 24,
    label = "CH3OO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.33,14.37,16.28,17.99,20.8,22.96,26.3],'cal/(mol*K)'),
        H298 = (3.33,'kcal/mol'),
        S298 = (64.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 26,
    label = "CH3OOH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.42,15.67,17.71,19.52,22.55,24.9,28.71],'cal/(mol*K)'),
        H298 = (-30.69,'kcal/mol'),
        S298 = (62.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 35,
    label = "HC2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.23,10.59,10.89,11.17,11.72,12.21,13.19],'cal/(mol*K)'),
        H298 = (135.6,'kcal/mol'),
        S298 = (51.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 36,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.21,11.55,12.69,13.6,15.02,16.08,17.75],'cal/(mol*K)'),
        H298 = (54.53,'kcal/mol'),
        S298 = (47.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 38,
    label = "H2CC(S)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.5,11.47,12.33,13.11,14.41,15.44,17.17],'cal/(mol*K)'),
        H298 = (98.44,'kcal/mol'),
        S298 = (53.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 40,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
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
)

entry(
    index = 41,
    label = "CCH3",
    molecule = 
"""
multiplicity 4
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u3 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.46,12.19,13.8,15.22,17.55,19.32,22.02],'cal/(mol*K)'),
        H298 = (120.41,'kcal/mol'),
        S298 = (55.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 42,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
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
)

entry(
    index = 44,
    label = "CHCH3(S)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p1 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.74,15.06,16.56,18,20.43,22.37,25.58],'cal/(mol*K)'),
        H298 = (88.33,'kcal/mol'),
        S298 = (89.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 46,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
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
)

entry(
    index = 47,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
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
)

entry(
    index = 49,
    label = "C2O(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.13,11.72,12.22,12.98,13.5,14.16],'cal/(mol*K)'),
        H298 = (90.98,'kcal/mol'),
        S298 = (55.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 50,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
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
)

entry(
    index = 220,
    label = "HCN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 H u0 p0 c0 {1,S}
3 N u0 p1 c0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.41,9.16,9.78,10.31,11.2,11.89,13.01],'cal/(mol*K)'),
        H298 = (30.72,'kcal/mol'),
        S298 = (48.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 221,
    label = "HNC",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,T}
2 H u0 p0 c0 {1,S}
3 C u0 p1 c-1 {1,T}
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
)

entry(
    index = 222,
    label = "HNCO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,D}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.85,12.06,13.1,13.94,15.25,16.19,17.56],'cal/(mol*K)'),
        H298 = (-27.92,'kcal/mol'),
        S298 = (57.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 223,
    label = "HOCN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 N u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.98,12.15,13.12,13.91,15.16,16.09,17.5],'cal/(mol*K)'),
        H298 = (-3.79,'kcal/mol'),
        S298 = (57.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 224,
    label = "HCNO",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.86,14.01,14.79,15.47,16.57,17.4,18.71],'cal/(mol*K)'),
        H298 = (41.57,'kcal/mol'),
        S298 = (56.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 225,
    label = "HONC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p0 c+1 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 C u0 p1 c-1 {2,T}
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
)

entry(
    index = 226,
    label = "HNCNJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,D}
3 H u0 p0 c0 {1,S}
4 N u1 p1 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.09,12.35,13.39,14.23,15.56,16.5,17.84],'cal/(mol*K)'),
        H298 = (105.06,'kcal/mol'),
        S298 = (58.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 228,
    label = "CH_NO2_3",
    molecule = 
"""
1  H u0 p0 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  N u0 p0 c+1 {2,S} {4,S} {5,D}
4  O u0 p3 c-1 {3,S}
5  O u0 p2 c0 {3,D}
6  N u0 p0 c+1 {2,S} {7,S} {8,D}
7  O u0 p3 c-1 {6,S}
8  O u0 p2 c0 {6,D}
9  N u0 p0 c+1 {2,S} {10,S} {11,D}
10 O u0 p3 c-1 {9,S}
11 O u0 p2 c0 {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.46,37.56,41.52,44.6,48.95,51.78,55.12],'cal/(mol*K)'),
        H298 = (1.75,'kcal/mol'),
        S298 = (97.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 229,
    label = "CH2NJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u1 p1 c0 {1,D}
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
)

entry(
    index = 231,
    label = "HCNHJ_cis",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.5,10.64,11.71,12.62,14.12,15.27,17.08],'cal/(mol*K)'),
        H298 = (69.86,'kcal/mol'),
        S298 = (54.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 233,
    label = "CH2NOJ",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 O u0 p2 c0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.38,13.32,14.98,16.36,18.57,20.19,22.54],'cal/(mol*K)'),
        H298 = (38.4,'kcal/mol'),
        S298 = (60.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, no rotors
""",
)

entry(
    index = 235,
    label = "CH2NO2J",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 N u0 p0 c+1 {3,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.3,16.84,18.92,20.52,22.84,24.42,26.48],'cal/(mol*K)'),
        H298 = (31.24,'kcal/mol'),
        S298 = (64.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, cosine rotor fit
""",
)

entry(
    index = 238,
    label = "CH2NN",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 N u0 p0 c+1 {3,D} {5,D}
5 N u0 p2 c-1 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.33,14.03,15.45,16.67,18.64,20.12,22.39],'cal/(mol*K)'),
        H298 = (64.99,'kcal/mol'),
        S298 = (57.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 243,
    label = "CH2_NO2_2",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {7,S}
4 N u0 p0 c+1 {3,S} {5,D} {6,S}
5 O u0 p2 c0 {4,D}
6 O u0 p3 c-1 {4,S}
7 N u0 p0 c+1 {3,S} {8,D} {9,S}
8 O u0 p2 c0 {7,D}
9 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.44,24.72,28.52,31.7,36.19,39.06,43.05],'cal/(mol*K)'),
        H298 = (-11.18,'kcal/mol'),
        S298 = (82.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 244,
    label = "CH3NJJ",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u2 p1 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.64,11.25,12.92,14.51,17.07,18.95,21.85],'cal/(mol*K)'),
        H298 = (75.63,'kcal/mol'),
        S298 = (54.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 245,
    label = "CH3NO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.18,15.06,16.8,18.35,20.93,22.93,26.1],'cal/(mol*K)'),
        H298 = (16.93,'kcal/mol'),
        S298 = (62.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 248,
    label = "HOCHNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.88,15.84,18.44,20.51,23.5,25.56,28.15],'cal/(mol*K)'),
        H298 = (-34.05,'kcal/mol'),
        S298 = (60.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 249,
    label = "CH3NO2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.81,16.77,19.44,21.71,25.27,27.86,31.57],'cal/(mol*K)'),
        H298 = (-18.17,'kcal/mol'),
        S298 = (65.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 250,
    label = "CH3ONO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.71,18.2,20.59,22.7,26.06,28.52,32.04],'cal/(mol*K)'),
        H298 = (-15.16,'kcal/mol'),
        S298 = (69.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 251,
    label = "CH3ONO2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {1,S} {6,S}
6 N u0 p0 c+1 {5,S} {7,D} {8,S}
7 O u0 p2 c0 {6,D}
8 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.13,21.54,24.61,27.24,31.13,33.67,37.31],'cal/(mol*K)'),
        H298 = (-28.56,'kcal/mol'),
        S298 = (72.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 252,
    label = "CH3NNJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 N u1 p1 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.31,14.32,16.17,17.83,20.58,22.7,26.04],'cal/(mol*K)'),
        H298 = (55.81,'kcal/mol'),
        S298 = (63.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 253,
    label = "CH2NNHJ",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.96,17,18.82,20.43,22.98,24.75,27.2],'cal/(mol*K)'),
        H298 = (79.81,'kcal/mol'),
        S298 = (96.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 254,
    label = "CH3NHJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
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
)

entry(
    index = 255,
    label = "CH2NH2J",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
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
)

entry(
    index = 259,
    label = "CH3NH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p1 c0 {1,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12,14.22,16.43,18.51,22.07,24.91,29.6],'cal/(mol*K)'),
        H298 = (-4.98,'kcal/mol'),
        S298 = (57.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 263,
    label = "CH3NHNH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p1 c0 {1,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 N u0 p1 c0 {5,S} {8,S} {9,S}
8 H u0 p0 c0 {7,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.77,21.27,24.2,26.76,30.98,34.2,39.32],'cal/(mol*K)'),
        H298 = (22.76,'kcal/mol'),
        S298 = (66.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 264,
    label = "CNJ",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.03,7.14,7.29,7.62,7.9,8.38],'cal/(mol*K)'),
        H298 = (106.48,'kcal/mol'),
        S298 = (48.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 265,
    label = "NCOJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p1 c0 {1,T}
3 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.38,10.34,11.13,11.76,12.7,13.33,14.08],'cal/(mol*K)'),
        H298 = (30.34,'kcal/mol'),
        S298 = (54.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 266,
    label = "CNNJJ",
    molecule = 
"""
multiplicity 3
1 N u0 p0 c+1 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 N u1 p2 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.16,11.12,11.8,12.36,13.19,13.72,14.32],'cal/(mol*K)'),
        H298 = (137.34,'kcal/mol'),
        S298 = (55.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 267,
    label = "NCNJJ",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,D}
2 N u1 p1 c0 {1,D}
3 N u1 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.91,10.92,11.68,12.26,13.12,13.68,14.3],'cal/(mol*K)'),
        H298 = (108.49,'kcal/mol'),
        S298 = (53.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 268,
    label = "C_NO2_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {11,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S}
5  N u0 p0 c+1 {1,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p3 c-1 {5,S}
8  N u0 p0 c+1 {1,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p3 c-1 {8,S}
11 N u0 p0 c+1 {1,S} {12,D} {13,S}
12 O u0 p2 c0 {11,D}
13 O u0 p3 c-1 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.46,44.67,49.76,53.88,59.73,63.18,66.22],'cal/(mol*K)'),
        H298 = (19.11,'kcal/mol'),
        S298 = (102,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 269,
    label = "HCCNJJ",
    molecule = 
"""
multiplicity 3
1 H u0 p0 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 N u1 p1 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.6,13.67,14.42,15.07,16.12,16.89,18.06],'cal/(mol*K)'),
        H298 = (115.69,'kcal/mol'),
        S298 = (59.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 272,
    label = "CH2CNJ",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u1 p1 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.47,14.22,15.67,16.88,18.84,20.29,22.49],'cal/(mol*K)'),
        H298 = (62.56,'kcal/mol'),
        S298 = (59.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 273,
    label = "CH2NCJ",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p0 c+1 {1,S} {5,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p1 c-1 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.93,14.5,15.82,16.97,18.86,20.3,22.53],'cal/(mol*K)'),
        H298 = (86.13,'kcal/mol'),
        S298 = (59.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 276,
    label = "CH3CN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 N u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.41,14.53,16.49,18.24,21.14,23.37,26.87],'cal/(mol*K)'),
        H298 = (17.51,'kcal/mol'),
        S298 = (57.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 277,
    label = "CH3NC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 C u0 p1 c-1 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.72,14.58,16.4,18.11,21.05,23.31,26.87],'cal/(mol*K)'),
        H298 = (41.85,'kcal/mol'),
        S298 = (58.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 284,
    label = "C2H5NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  N u0 p0 c+1 {5,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p3 c-1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.43,23.92,27.73,30.99,36.2,40.01,45.54],'cal/(mol*K)'),
        H298 = (-25.3,'kcal/mol'),
        S298 = (75.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 286,
    label = "C2H5NNN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u1 p1 c0 {1,S} {6,S}
6 C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.44,24.59,28.38,31.71,36.9,40.53,46.03],'cal/(mol*K)'),
        H298 = (64.07,'kcal/mol'),
        S298 = (75.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 290,
    label = "CH3_2_NNO2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  N u0 p1 c0 {1,S} {2,S} {4,S}
4  N u0 p0 c+1 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.4,29.32,33.98,38.03,44.53,49.28,56.06],'cal/(mol*K)'),
        H298 = (-1.99,'kcal/mol'),
        S298 = (114.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, one rigid rotor
""",
)

entry(
    index = 291,
    label = "CH3NHCH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  N u0 p1 c0 {1,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
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
)

entry(
    index = 295,
    label = "N_CH3_2_NH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  N u0 p1 c0 {1,S} {5,S} {10,S}
10 N u0 p1 c0 {9,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.82,28.29,32.73,36.44,42.42,46.86,53.62],'cal/(mol*K)'),
        H298 = (20.04,'kcal/mol'),
        S298 = (73.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 297,
    label = "NCCN",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.21,14.49,15.36,16.1,17.27,18.11,19.3],'cal/(mol*K)'),
        H298 = (73.74,'kcal/mol'),
        S298 = (57.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 298,
    label = "NO2CCNO2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {6,S}
3 N u0 p0 c+1 {1,S} {4,S} {5,D}
4 O u0 p3 c-1 {3,S}
5 O u0 p2 c0 {3,D}
6 N u0 p0 c+1 {2,S} {7,S} {8,D}
7 O u0 p3 c-1 {6,S}
8 O u0 p2 c0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.97,28,30.51,32.57,35.59,37.48,39.45],'cal/(mol*K)'),
        H298 = (87.12,'kcal/mol'),
        S298 = (87.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 301,
    label = "HCCCN",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.85,16.9,18.25,19.32,21.02,22.25,24.04],'cal/(mol*K)'),
        H298 = (89.51,'kcal/mol'),
        S298 = (59.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 314,
    label = "C3H7CN",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,T}
12 N u0 p1 c0 {11,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.05,28.97,33.29,37.08,43.26,47.91,55],'cal/(mol*K)'),
        H298 = (7.97,'kcal/mol'),
        S298 = (78.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 316,
    label = "C4H9NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 H u0 p0 c0 {11,S}
13 H u0 p0 c0 {11,S}
14 N u0 p0 c+1 {11,S} {15,D} {16,S}
15 O u0 p2 c0 {14,D}
16 O u0 p3 c-1 {14,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.72,37.59,43.95,49.47,58.36,64.89,74.42],'cal/(mol*K)'),
        H298 = (-34.86,'kcal/mol'),
        S298 = (95.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 318,
    label = "HONO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {2,S}
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
)

entry(
    index = 319,
    label = "NO2OH",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.8,15.22,17.09,18.44,20.42,21.72,23.22],'cal/(mol*K)'),
        H298 = (-31.75,'kcal/mol'),
        S298 = (63.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 320,
    label = "NHJJ",
    molecule = 
"""
multiplicity 3
1 H u0 p0 c0 {2,S}
2 N u2 p1 c0 {1,S}
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
)

entry(
    index = 321,
    label = "NH2J",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 N u1 p1 c0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.06,8.23,8.47,8.76,9.44,10.08,11.4],'cal/(mol*K)'),
        H298 = (44.39,'kcal/mol'),
        S298 = (46.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 322,
    label = "NH2OJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.22,10.79,11.63,12.41,13.77,14.9,16.83],'cal/(mol*K)'),
        H298 = (16.44,'kcal/mol'),
        S298 = (62.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 323,
    label = "NH3",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.49,9.05,9.74,10.48,11.92,13.16,15.5],'cal/(mol*K)'),
        H298 = (-10.69,'kcal/mol'),
        S298 = (45.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 324,
    label = "NH2OH",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 H u0 p0 c0 {4,S}
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
)

entry(
    index = 325,
    label = "NOJ",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.2,7.37,7.72,8,8.46],'cal/(mol*K)'),
        H298 = (21.85,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 326,
    label = "NO2J",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
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
)

entry(
    index = 327,
    label = "NO3J",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
4 O u1 p2 c0 {1,S}
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
)

entry(
    index = 328,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.94,6.98,7.07,7.18,7.46,7.73,8.25],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (45.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 329,
    label = "NNHJ",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u1 p1 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.28,8.68,9.17,9.69,10.59,11.3,12.45],'cal/(mol*K)'),
        H298 = (59.61,'kcal/mol'),
        S298 = (53.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 330,
    label = "HNNH",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.42,9.19,10.14,11.15,12.92,14.32,16.61],'cal/(mol*K)'),
        H298 = (47.63,'kcal/mol'),
        S298 = (52.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 331,
    label = "NH2NO2",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p0 c+1 {1,S} {5,D} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13,15.71,17.8,19.38,21.82,23.55,25.95],'cal/(mol*K)'),
        H298 = (0.45,'kcal/mol'),
        S298 = (63.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, cosine rotor fit
""",
)

entry(
    index = 332,
    label = "NH2NHJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u1 p1 c0 {1,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.78,11,12.2,13.29,15.18,16.7,19.32],'cal/(mol*K)'),
        H298 = (53.53,'kcal/mol'),
        S298 = (56.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, rigid scan
""",
)

entry(
    index = 333,
    label = "NH2NH2",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p1 c0 {1,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.55,13.62,15.48,17.08,19.74,21.81,25.17],'cal/(mol*K)'),
        H298 = (23.35,'kcal/mol'),
        S298 = (56.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 334,
    label = "N2O",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,D}
2 N u0 p2 c-1 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2,10.11,10.88,11.5,12.44,13.08,13.9],'cal/(mol*K)'),
        H298 = (19.74,'kcal/mol'),
        S298 = (52.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 335,
    label = "NO2NO",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 O u0 p2 c0 {1,D}
4 O u0 p3 c-1 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.99,18.58,19.8,20.79,22.23,23.1,23.95],'cal/(mol*K)'),
        H298 = (19.9,'kcal/mol'),
        S298 = (71.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 336,
    label = "NO2NO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p0 c+1 {1,S} {5,D} {6,S}
3 O u0 p2 c0 {1,D}
4 O u0 p3 c-1 {1,S}
5 O u0 p2 c0 {2,D}
6 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.78,21.47,23.46,24.94,27.1,28.46,29.85],'cal/(mol*K)'),
        H298 = (2.35,'kcal/mol'),
        S298 = (73.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 337,
    label = "NO2ONO2",
    molecule = 
"""
1 N u0 p0 c+1 {3,S} {4,D} {5,S}
2 N u0 p0 c+1 {3,S} {6,D} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,D}
5 O u0 p3 c-1 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.31,23.22,25.61,27.57,30.39,32.14,33.98],'cal/(mol*K)'),
        H298 = (3.9,'kcal/mol'),
        S298 = (84.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 338,
    label = "NNNJ",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 N u0 p2 c-1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.46,10.45,11.26,11.9,12.85,13.47,14.18],'cal/(mol*K)'),
        H298 = (107.66,'kcal/mol'),
        S298 = (52.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 339,
    label = "HNNN",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p0 c+1 {2,D} {4,D}
4 N u0 p2 c-1 {3,D}
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
)

entry(
    index = 340,
    label = "NO2ONO",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {4,D} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {6,D}
4 O u0 p2 c0 {1,D}
5 O u0 p3 c-1 {1,S}
6 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.7,21.28,23.11,24.55,26.68,28.02,29.42],'cal/(mol*K)'),
        H298 = (10.61,'kcal/mol'),
        S298 = (76.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 343,
    label = "NNH2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p2 c-1 {1,D}
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
)

entry(
    index = 345,
    label = "HNOHJ",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.3,10.39,11.56,12.68,14.59,15.98,17.94],'cal/(mol*K)'),
        H298 = (23.24,'kcal/mol'),
        S298 = (55.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 346,
    label = "NOHJJ",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
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
)

entry(
    index = 347,
    label = "HNO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
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
)

entry(
    index = 348,
    label = "N_CH3_3",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  H u0 p0 c0 {2,S}
4  H u0 p0 c0 {2,S}
5  H u0 p0 c0 {2,S}
6  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.32,28.98,33.84,38.08,44.97,50.15,58.1],'cal/(mol*K)'),
        H298 = (-5.79,'kcal/mol'),
        S298 = (70.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 352,
    label = "CNOJ",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {3,D}
2 C u1 p1 c-1 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.32,11.09,11.69,12.2,12.98,13.51,14.19],'cal/(mol*K)'),
        H298 = (93.81,'kcal/mol'),
        S298 = (55.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 353,
    label = "CH2NH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.24,10.64,12.18,13.7,16.32,18.27,21.35],'cal/(mol*K)'),
        H298 = (21.23,'kcal/mol'),
        S298 = (54.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 354,
    label = "ONNO_cis",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.35,15.28,16.71,17.6,18.54,18.94,18.86],'cal/(mol*K)'),
        H298 = (42.5,'kcal/mol'),
        S298 = (63.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 355,
    label = "ONNOJJ_cis",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 O u1 p2 c0 {1,S}
4 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.42,15.25,15.94,16.53,17.45,18.09,18.94],'cal/(mol*K)'),
        H298 = (218.89,'kcal/mol'),
        S298 = (69.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, no rotors
""",
)

entry(
    index = 356,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 N u0 p0 c+1 {1,D} {4,D}
3 H u0 p0 c0 {1,S}
4 N u0 p2 c-1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.16,12.45,13.52,14.39,15.74,16.69,18.01],'cal/(mol*K)'),
        H298 = (111.77,'kcal/mol'),
        S298 = (58.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 357,
    label = "ONOONO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {5,D}
4 N u0 p1 c0 {2,S} {6,D}
5 O u0 p2 c0 {3,D}
6 O u0 p2 c0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.09,25.22,26.7,27.89,29.59,30.58,31.32],'cal/(mol*K)'),
        H298 = (31.51,'kcal/mol'),
        S298 = (76.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, no O-O rotor
""",
)

entry(
    index = 358,
    label = "HNO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 O u0 p3 c-1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.27,10.47,11.71,12.86,14.66,15.91,17.69],'cal/(mol*K)'),
        H298 = (-10.4,'kcal/mol'),
        S298 = (58.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 359,
    label = "HNO2JJ",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 O u1 p2 c0 {1,S}
4 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.62,12.1,13.34,14.3,15.72,16.71,18.04],'cal/(mol*K)'),
        H298 = (57.44,'kcal/mol'),
        S298 = (61.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, MOLPRO NoSym
""",
)

entry(
    index = 360,
    label = "ONOOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.64,17.29,18.52,19.53,21.04,22.05,23.23],'cal/(mol*K)'),
        H298 = (-2.6,'kcal/mol'),
        S298 = (69.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 361,
    label = "ONONO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {1,S} {5,D}
4 O u0 p2 c0 {2,D}
5 O u0 p2 c0 {3,D}
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
)

entry(
    index = 363,
    label = "NO2OOH",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {4,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.02,20.77,22.6,23.99,26.02,27.29,28.58],'cal/(mol*K)'),
        H298 = (-12.1,'kcal/mol'),
        S298 = (72.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 364,
    label = "ONOOJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.66,15.51,16.23,16.83,17.75,18.36,19.1],'cal/(mol*K)'),
        H298 = (33.48,'kcal/mol'),
        S298 = (70.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//PBEPBE/6-311++g(d,p) + BAC, bad geometry, no rotors
""",
)

entry(
    index = 365,
    label = "NO2OOJ",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u1 p2 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.15,18.62,20.27,21.39,22.94,23.81,24.41],'cal/(mol*K)'),
        H298 = (51.01,'kcal/mol'),
        S298 = (72.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//PBEPBE/6-311++g(d,p) + BAC, bad geometry
""",
)

entry(
    index = 368,
    label = "HNOO",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.19,13.18,13.92,14.55,15.53,16.21,17.17],'cal/(mol*K)'),
        H298 = (85.08,'kcal/mol'),
        S298 = (66.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 369,
    label = "NH2OOH",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.35,16.67,18.52,20.04,22.44,24.16,26.56],'cal/(mol*K)'),
        H298 = (3.07,'kcal/mol'),
        S298 = (64.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, NH2 rotor rigid scan
""",
)

entry(
    index = 370,
    label = "CH3N(S)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.19,10.49,11.9,13.28,15.67,17.42,20.15],'cal/(mol*K)'),
        H298 = (110.86,'kcal/mol'),
        S298 = (54.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 371,
    label = "NH2OOJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u1 p2 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.68,14.06,15.3,16.4,18.18,19.49,21.5],'cal/(mol*K)'),
        H298 = (37.98,'kcal/mol'),
        S298 = (66.06,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 372,
    label = "NCNO",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.21,14.27,15.13,15.85,16.97,17.74,18.73],'cal/(mol*K)'),
        H298 = (76.78,'kcal/mol'),
        S298 = (64.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, no rotors
""",
)

entry(
    index = 373,
    label = "HONNOH",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p2 c0 {2,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.43,20.17,21.99,23.31,25.26,26.49,27.84],'cal/(mol*K)'),
        H298 = (5.23,'kcal/mol'),
        S298 = (65.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 374,
    label = "HNOHOH",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.47,18.11,20.08,21.46,23.46,24.81,26.59],'cal/(mol*K)'),
        H298 = (-21.9,'kcal/mol'),
        S298 = (63.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 376,
    label = "HNC(T)",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u2 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.31,8.76,9.29,9.81,10.68,11.36,12.43],'cal/(mol*K)'),
        H298 = (152.52,'kcal/mol'),
        S298 = (54.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 377,
    label = "HNCJJ(S",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p1 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.38,10.05,10.51,10.89,11.53,12.05,13.01],'cal/(mol*K)'),
        H298 = (45.46,'kcal/mol'),
        S298 = (48.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 378,
    label = "HCNOJJ",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.74,12.94,13.92,14.73,16.02,16.93,18.18],'cal/(mol*K)'),
        H298 = (103.44,'kcal/mol'),
        S298 = (62.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 383,
    label = "NCCOJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.29,14.25,15.03,15.71,16.78,17.54,18.61],'cal/(mol*K)'),
        H298 = (51.43,'kcal/mol'),
        S298 = (65.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 386,
    label = "HNNOH",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.18,14.11,15.77,17.11,19.17,20.62,22.55],'cal/(mol*K)'),
        H298 = (19.35,'kcal/mol'),
        S298 = (61.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 389,
    label = "ONOONO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {5,D} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u0 p1 c0 {3,S} {7,D}
5 O u0 p2 c0 {1,D}
6 O u0 p3 c-1 {1,S}
7 O u0 p2 c0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.47,27.37,29.74,31.63,34.26,35.71,36.57],'cal/(mol*K)'),
        H298 = (19.99,'kcal/mol'),
        S298 = (84.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 392,
    label = "NO2OONO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 O u0 p2 c0 {4,S} {6,S}
6 N u0 p0 c+1 {5,S} {7,D} {8,S}
7 O u0 p2 c0 {6,D}
8 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.13,29.07,32.28,34.86,38.46,40.51,41.95],'cal/(mol*K)'),
        H298 = (9.17,'kcal/mol'),
        S298 = (85.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 395,
    label = "CH3NNN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p0 c+1 {2,D} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 N u0 p2 c-1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.07,17.67,20.07,22.16,25.53,28.02,31.67],'cal/(mol*K)'),
        H298 = (71.26,'kcal/mol'),
        S298 = (67.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 398,
    label = "HNNNH2",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.92,14.14,16,17.52,20.01,21.88,24.8],'cal/(mol*K)'),
        H298 = (54,'kcal/mol'),
        S298 = (59.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, cosine rotor fit
""",
)

entry(
    index = 400,
    label = "NH2NHOJ",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.75,16.17,18.23,19.9,22.45,24.23,26.66],'cal/(mol*K)'),
        H298 = (35.58,'kcal/mol'),
        S298 = (64.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 401,
    label = "CH3C_NO2_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p0 c+1 {1,S} {9,D} {10,S}
4  N u0 p0 c+1 {1,S} {11,D} {12,S}
5  N u0 p0 c+1 {1,S} {13,D} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 O u0 p3 c-1 {3,S}
11 O u0 p2 c0 {4,D}
12 O u0 p3 c-1 {4,S}
13 O u0 p2 c0 {5,D}
14 O u0 p3 c-1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.81,46.45,51.32,55.08,60.81,64.66,69.39],'cal/(mol*K)'),
        H298 = (-12.48,'kcal/mol'),
        S298 = (98.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 402,
    label = "CH3NONOCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  N u0 p0 c+1 {1,S} {4,D} {11,S}
4  N u0 p0 c+1 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p3 c-1 {3,S}
12 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.06,30.02,34.47,38.4,44.75,49.3,55.94],'cal/(mol*K)'),
        H298 = (16.57,'kcal/mol'),
        S298 = (79.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, not N=N rotor
""",
)

entry(
    index = 403,
    label = "CH_NO2_2J",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p0 c+1 {1,S} {5,D} {6,S}
3 N u0 p0 c+1 {1,S} {7,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 O u0 p3 c-1 {2,S}
7 O u0 p2 c0 {3,D}
8 O u0 p3 c-1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.99,27.36,30,32.09,35.08,37.02,39.23],'cal/(mol*K)'),
        H298 = (41.56,'kcal/mol'),
        S298 = (85.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 431,
    label = "NH2NO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.88,13.8,15.49,16.89,19.03,20.56,22.69],'cal/(mol*K)'),
        H298 = (18.82,'kcal/mol'),
        S298 = (59.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

entry(
    index = 432,
    label = "NNOJJ",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.44,10.35,11.1,11.65,12.39,12.88,13.41],'cal/(mol*K)'),
        H298 = (94.33,'kcal/mol'),
        S298 = (59.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
)

#entry(
#    index = 434,
#    label = "NNH2(S)",
#    molecule = 
#"""
#1 N u0 p0 c+2 {2,S} {3,S} {4,S}
#2 H u0 p0 c0 {1,S}
#3 H u0 p0 c0 {1,S}
#4 N u0 p3 c-2 {1,S}
#""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([8.61,9.45,10.46,11.48,13.24,14.63,16.86],'cal/(mol*K)'),
#        H298 = (71.66,'kcal/mol'),
#        S298 = (52.09,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
#level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#)

