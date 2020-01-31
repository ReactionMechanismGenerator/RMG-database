#!/usr/bin/env python
# encoding: utf-8

name = "thermo_DFT_CCSDTF12_BAC"
shortDesc = u""
longDesc = u"""
Done by B. Buesser using DFT and CCSDTF12 using or deriving bond additvity corrections, unless otherwise noted
"""
entry(
    index = 0,
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
    index = 1,
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
    index = 2,
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
    index = 3,
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
    index = 4,
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
    index = 5,
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
    index = 6,
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
    index = 7,
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
    index = 8,
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
    index = 9,
    label = "HCOH(S)",
    molecule = 
"""
1 O u0 p1 c+1 {2,D} {4,S}
2 C u0 p1 c-1 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
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
    index = 10,
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
    index = 11,
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
    index = 12,
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
    index = 13,
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
    index = 14,
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
    index = 15,
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
    index = 16,
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
    index = 17,
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
    index = 18,
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
    index = 19,
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
    index = 20,
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
    index = 21,
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
    index = 22,
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
    index = 23,
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
    index = 24,
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
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 28,
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
    index = 29,
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
    index = 30,
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
    index = 31,
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
    index = 32,
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
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
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
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 59,
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
    index = 60,
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
    index = 61,
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
    index = 62,
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
    index = 63,
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
    index = 64,
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
    index = 65,
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
    index = 66,
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
    index = 67,
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
    index = 68,
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
    index = 69,
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
    index = 70,
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
    index = 71,
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
    index = 72,
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
    index = 73,
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
    index = 74,
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
    index = 75,
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
    index = 76,
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
    index = 77,
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
    index = 78,
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
    index = 79,
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
    index = 80,
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
    index = 81,
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
    index = 82,
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
    index = 83,
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
    index = 84,
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
    index = 85,
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
    index = 86,
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
    index = 87,
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
    index = 88,
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
    index = 89,
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
    index = 90,
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
    index = 91,
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
    index = 92,
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
    index = 93,
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
    index = 94,
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
    index = 95,
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
    index = 96,
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
    index = 97,
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
    index = 98,
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
    index = 99,
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
    index = 100,
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
    index = 101,
    label = "NNH2(S)",
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
    index = 102,
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
    index = 103,
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
    index = 104,
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
    index = 105,
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
    index = 106,
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
    index = 107,
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
    index = 108,
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
    index = 109,
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
    index = 110,
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
    index = 111,
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
    index = 112,
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
    index = 113,
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
    index = 114,
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
    index = 115,
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
    index = 116,
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
    index = 117,
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
    index = 118,
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
    index = 119,
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
    index = 120,
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
    index = 121,
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
    index = 122,
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
    index = 123,
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
    index = 124,
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
    index = 125,
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
    index = 126,
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
    index = 127,
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
    index = 128,
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
    index = 129,
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
    index = 130,
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
    index = 131,
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
    index = 132,
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
    index = 133,
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
    index = 134,
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
    index = 135,
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
    index = 136,
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
    index = 137,
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
    index = 138,
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
    index = 139,
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
    index = 140,
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

entry(
    index = 141,
    label = "cyanoisopropyl",
    molecule =
"""
multiplicity 2
1  N u0 p1 c0 {5,T}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {3,S} {5,S}
5  C u0 p0 c0 {1,T} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59561,0.0433769,-0.000150104,3.758e-07,-3.18699e-10,21337.9,10.6486], Tmin=(10,'K'), Tmax=(420.268,'K')),
            NASAPolynomial(coeffs=[1.30227,0.0361352,-2.05055e-05,5.63964e-09,-6.03973e-13,21787.4,22.7788], Tmin=(420.268,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (177.402,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Calculated by A. Grinberg Dana using ARC 1.0.0

Conformers:       b97-d3/6-311+g(d,p)
Optimization:     wb97xd/6-311++g(d,p) (using a fine grid)
Frequencies:      wb97xd/6-311++g(d,p)
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      b3lyp/6-311+g(d,p)

Bond corrections: {'C#N': 1, 'C-C': 3, 'C-H': 6}

1D rotors:
pivots: [2, 4], dihedral: [6, 2, 4, 3], rotor symmetry: 3, max scan energy: 2.27 kJ/mol
pivots: [3, 4], dihedral: [9, 3, 4, 2], rotor symmetry: 3, max scan energy: 2.27 kJ/mol

External symmetry: 2, optical isomers: 2

Geometry:
N       2.24465000    0.00288700   -0.00395200
C      -1.06286400    1.28810400    0.08614100
C      -1.06016300   -1.28990600   -0.08427100
C      -0.30986700   -0.00004000   -0.00017600
C       1.08027800    0.00155300   -0.00223100
H      -0.40232600    2.15369500    0.04243700
H      -1.79151100    1.35912100   -0.72933900
H      -1.63021700    1.33369300    1.02401500
H      -0.39751600   -2.15398100   -0.04252600
H      -1.78622800   -1.36259100    0.73336200
H      -1.63018200   -1.33679700   -1.02046300
""",
)

entry(
    index = 142,
    label = "cyanoisopropylOOH",
    molecule =
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {14,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,T} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69904,0.0241458,0.000242618,-8.48082e-07,8.45693e-10,-7791.09,11.5584],Tmin=(10,'K'),Tmax=(357.267,'K'),),
            NASAPolynomial(coeffs=[6.03838,0.0431102,-2.65938e-05,8.0486e-09,-9.47215e-13,-8246.43,-1.35299],Tmin=(357.267,'K'),Tmax=(3000,'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-64.7396, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (320.107, 'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Calculated by A. Grinberg Dana using ARC 1.0.0

Conformers:       b97-d3/6-311+g(d,p)
Optimization:     wb97xd/6-311++g(d,p) (using a fine grid)
Frequencies:      wb97xd/6-311++g(d,p)
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      b3lyp/6-311+g(d,p)

Bond corrections: {'C-O': 1, 'H-O': 1, 'C#N': 1, 'C-H': 6, 'C-C': 3, 'O-O': 1}

1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 24.14 kJ/mol
pivots: [1, 2], dihedral: [4, 1, 2, 14], rotor symmetry: 1, max scan energy: 36.41 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 8], rotor symmetry: 3, max scan energy: 11.66 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 11], rotor symmetry: 3, max scan energy: 12.77 kJ/mol

External symmetry: 1, optical isomers: 2

Geometry:
O       1.02648700   -0.19743200    0.74293100
O       1.85498100    0.74962100    0.08453600
N      -1.49916600    1.87241100   -0.07890000
C      -0.16600800   -0.39808900   -0.01625100
C      -0.94394300   -1.43237200    0.79401300
C       0.13694700   -0.87673800   -1.43338100
C      -0.92155500    0.87834800   -0.05737800
H      -1.90042000   -1.63533200    0.31006300
H      -1.12711500   -1.07115500    1.80649300
H      -0.36394700   -2.35551300    0.84037500
H      -0.79518600   -1.04953600   -1.97516700
H       0.69604000   -1.81257900   -1.37455900
H       0.72914100   -0.13907900   -1.97306800
H       1.71371600    1.54061300    0.61900900
""",
)

entry(
    index = 143,
    label = "cyanoisopropane",
    molecule =
"""
1  N u0 p1 c0 {5,T}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,T} {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91153,0.00781557,0.000180226,-5.88386e-07,6.55296e-10,2094.77,9.32227], Tmin=(10,'K'), Tmax=(226.564,'K')),
            NASAPolynomial(coeffs=[2.18326,0.0383288,-2.17942e-05,6.07013e-09,-6.61958e-13,2173.08,15.0941], Tmin=(226.564,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (17.4281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Calculated by A. Grinberg Dana using ARC 1.0.0

Conformers:       b97-d3/6-311+g(d,p)
Optimization:     wb97xd/6-311++g(d,p) (using a fine grid)
Frequencies:      wb97xd/6-311++g(d,p)
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      b3lyp/6-311+g(d,p)

Bond corrections: {'C#N': 1, 'C-C': 3, 'C-H': 7}

1D rotors:
pivots: [2, 4], dihedral: [3, 2, 4, 10], rotor symmetry: 3, max scan energy: 13.19 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 7], rotor symmetry: 3, max scan energy: 13.18 kJ/mol

External symmetry: 1, optical isomers: 1

Geometry:
N      -2.20312500    0.15910800    0.00000000
C       0.35469500   -0.39904900    0.00000000
C       1.01752500    0.14256700   -1.27321800
C       1.01752500    0.14256700    1.27321800
C      -1.08030100   -0.09186200    0.00000000
H       0.43242300   -1.49152700    0.00000000
H       0.54500800   -0.26089100   -2.17033700
H       2.07327100   -0.13786000   -1.28141800
H       0.95018100    1.23248900   -1.30888200
H       0.54500800   -0.26089100    2.17033700
H       2.07327100   -0.13786000    1.28141800
H       0.95018100    1.23248900    1.30888200
""",
)

entry(
    index = 144,
    label = "cyanoisopropylOO",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  N u0 p1 c0 {7,T}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,T} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73277,0.0228798,0.000218553,-8.18582e-07,8.85419e-10,10803.4,12.6662], Tmin=(10,'K'), Tmax=(324.224,'K')),
            NASAPolynomial(coeffs=[4.94043,0.0419159,-2.65147e-05,8.14503e-09,-9.65226e-13,10546.7,5.44954], Tmin=(324.224,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (89.8672,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Calculated by A. Grinberg Dana using ARC 1.0.0

Conformers:       b97-d3/6-311+g(d,p)
Optimization:     wb97xd/6-311++g(d,p) (using a fine grid)
Frequencies:      wb97xd/6-311++g(d,p)
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      b3lyp/6-311+g(d,p)

Bond corrections: {'C-O': 1, 'C-C': 3, 'C#N': 1, 'O-O': 1, 'C-H': 6}

1D rotors:
pivots: [1, 4], dihedral: [2, 1, 4, 5], rotor symmetry: 1, max scan energy: 8.51 kJ/mol
pivots: [4, 6], dihedral: [1, 4, 6, 11], rotor symmetry: 3, max scan energy: 13.22 kJ/mol
pivots: [4, 5], dihedral: [1, 4, 5, 8], rotor symmetry: 3, max scan energy: 13.22 kJ/mol

External symmetry: 1, optical isomers: 1

Geometry:
O      -0.76231100   -1.01654800   -0.00031900
O      -2.03043700   -0.75204100   -0.00031000
N       2.52595900   -0.66596100   -0.00011200
C       0.06045200    0.21651900    0.00005100
C      -0.22025700    1.00359100   -1.27386500
C      -0.22032600    1.00287000    1.27439800
C       1.43559100   -0.30406900   -0.00005400
H      -0.02569500    0.39341200   -2.15673700
H      -1.26432800    1.31841100   -1.27191100
H       0.41994800    1.88678200   -1.30579400
H      -0.02581700    0.39218200    2.15693000
H       0.41988100    1.88603900    1.30686400
H      -1.26439600    1.31769600    1.27256600
""",
)

entry(
    index = 145,
    label = "cyanoisopropanol",
    molecule =
"""
1  O u0 p2 c0 {3,S} {13,S}
2  N u0 p1 c0 {6,T}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {2,T} {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79905,0.0147559,0.000193632,-5.5562e-07,4.71803e-10,-17325,11.435],
                           Tmin=(10,'K'), Tmax=(406.456,'K')),
            NASAPolynomial(coeffs=[4.70095,0.0398378,-2.42495e-05,7.29483e-09,-8.56322e-13,-17678.8,4.44523],
                           Tmin=(406.456,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-144.044,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Calculated by A. Grinberg Dana using ARC 1.1.0

Conformers:       apfd/def2svp
Optimization:     wb97xd/def2tzvp (using a fine grid)
Frequencies:      wb97xd/def2tzvp
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      wb97xd/def2tzvp

Bond corrections: {'H-O': 1, 'C-H': 6, 'C-O': 1, 'C#N': 1, 'C-C': 3}
1D rotors:
pivots: [3, 4], dihedral: [2, 3, 4, 7], rotor symmetry: 1, max scan energy: 9.40 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 8], rotor symmetry: 3, max scan energy: 14.17 kJ/mol
pivots: [3, 6], dihedral: [2, 3, 6, 11], rotor symmetry: 3, max scan energy: 15.56 kJ/mol

External symmetry: 1, optical isomers: 2

Geometry:
N       2.68045600   -0.50225400   -0.32595600
C       1.57982700   -0.28284100   -0.08843700
C       0.16234000    0.03467500    0.22573700
O      -0.00746200    0.07786300    1.62802000
C      -0.73064500   -1.09059200   -0.28132800
C      -0.19527800    1.37449300   -0.41778200
H       0.53821600    0.77896900    1.99217000
H      -0.46331600   -2.02927600    0.20126400
H      -0.63198700   -1.20316300   -1.36043400
H      -1.76548300   -0.85004700   -0.03787000
H      -0.07529900    1.33167600   -1.50044600
H       0.44526200    2.17116500   -0.03559000
H      -1.23294300    1.60944800   -0.18059000
""",
)

entry(
    index = 146,
    label = "methanediol",
    molecule =
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92739,0.00397483,6.56102e-05,-1.2376e-07,6.75141e-11,-48280.5,6.35739],
                           Tmin=(10,'K'), Tmax=(639.758,'K')),
            NASAPolynomial(coeffs=[4.46055,0.0193316,-1.42176e-05,5.09053e-09,-6.8174e-13,-48731.2,1.03399],
                           Tmin=(639.758,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-401.461,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Calculated by A. Grinberg Dana using ARC 1.1.0

Conformers:       apfd/def2svp
Optimization:     wb97xd/def2tzvp (using a fine grid)
Frequencies:      wb97xd/def2tzvp
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      wb97xd/def2tzvp

Bond corrections: {'H-O': 2, 'C-H': 2, 'C-O': 2}
1D rotors:
pivots: [1, 2], dihedral: [4, 1, 2, 3], rotor symmetry: 1, max scan energy: 16.39 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 7], rotor symmetry: 1, max scan energy: 16.39 kJ/mol

External symmetry: 2, optical isomers: 2

Geometry:
O      -0.94490700   -0.51883200    0.46328300
C       0.02452000    0.39447900    0.03976700
O      -0.51773300    1.62734000   -0.33347400
H      -1.54032300   -0.68571800   -0.27093200
H       0.71714800    0.49105600    0.88040200
H       0.56398300    0.03745500   -0.84184600
H      -0.94684400    2.01079700    0.43481500
""",
)

entry(
    index = 147,
    label = "iC3H6CNOO",
    molecule =
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  N u0 p1 c0 {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,D}
5  C u0 p0 c0 {4,D} {6,S} {7,S}
6  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27201,0.0640735,-0.000120937,1.65836e-07,-9.26395e-11,67520.2,12.7741], Tmin=(10,'K'), Tmax=(537.94,'K')),
            NASAPolynomial(coeffs=[4.9458,0.0404352,-2.38144e-05,6.79624e-09,-7.53272e-13,67502.1,7.24198], Tmin=(537.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (561.349,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc =
"""
Calculated by A. Grinberg Dana using ARC 1.1.0

Conformers:       apfd/def2svp
Optimization:     wb97xd/def2tzvp (using a fine grid)
Frequencies:      wb97xd/def2tzvp
Single point:     ccsd(t)-f12/cc-pvtz-f12
Rotor scans:      wb97xd/def2tzvp

! This species is predicted to be relatively stable by RMG's GAV (see RMG-Py/issues/1877),
! where in fact it is very high in energy.
! This species has a relatively shallow well, where a torsion mode about pivots 2-3 cause it to fall apart
! into iC3H6C[N] and O2. THis mode was hence treated here a vibration instead of internal rotation.
! Although calculated at a relatively high level, this entry primarily functions to alert RMG that the thermo is high
! and that these species shouldn't normally be included in the core
! (so a lower calculation level would have also been suffice).

Bond corrections: {'C-H': 6, 'C=C': 1, 'O-O': 1, 'N-O': 1, 'C-C': 2, 'C=N': 1}

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: inconsistent scan
pivots: [5, 6], dihedral: [4, 5, 6, 8], rotor symmetry: 3, max scan energy: 7.17 kJ/mol
pivots: [5, 7], dihedral: [4, 5, 7, 11], rotor symmetry: 3, max scan energy: 7.18 kJ/mol

External symmetry: 1, optical isomers: 1

Geometry:
O       3.83074800   -0.34645300    0.64712600
O       2.69031900   -0.49706800    0.13398900
N       1.96702500   -1.67203000    0.77618000
C       0.86544400   -1.77688000    0.24401100
C      -0.32156500   -1.96182400   -0.26491600
C      -1.52609800   -1.28157800    0.32022600
C      -0.52134800   -2.86621400   -1.44736700
H      -2.00435100   -0.65623400   -0.43740300
H      -1.26981100   -0.65918200    1.17502100
H      -2.25641100   -2.02992900    0.63733600
H      -1.21885400   -3.66629500   -1.18794100
H      -0.95961200   -2.30397000   -2.27536800
H       0.41224500   -3.31201200   -1.78411800
""",
)
