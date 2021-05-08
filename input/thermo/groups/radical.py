#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Radical",
    group = "OR{RJ, RJ2_triplet, RJ3}",
    thermo = 'RJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "RJ",
    group = 
"""
1 * R u1
""",
    thermo = 'CJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CJ",
    group = 
"""
1 * C u1
""",
    thermo = 'CsJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "CsJ",
    group = 
"""
1 * Cs u1
""",
    thermo = 'Cs_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "CsBr1sBr1sCO",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.4815,-1.76183,-2.0107,-2.26705,-2.73704,-3.12225,-3.7534],'cal/(mol*K)','+|-',[0.503132,0.514858,0.482243,0.450189,0.396999,0.347485,0.259848]),
        H298 = (87.2667,'kcal/mol','+|-',0.783558),
        S298 = (-1.07088,'cal/(mol*K)','+|-',1.17914),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 5,
    label = "CsBr1sCOCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53049,-1.95284,-2.17323,-2.33206,-2.64706,-2.99283,-3.66811],'cal/(mol*K)','+|-',[0.450015,0.460503,0.431331,0.402661,0.355086,0.3108,0.232415]),
        H298 = (86.1036,'kcal/mol','+|-',0.700836),
        S298 = (-1.30245,'cal/(mol*K)','+|-',1.05465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOClBr_G4 |         5
""",
)

entry(
    index = 6,
    label = "CsCOCl1sCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54265,-1.90747,-2.176,-2.39507,-2.80178,-3.1353,-3.76431],'cal/(mol*K)','+|-',[0.318208,0.325625,0.304997,0.284724,0.251084,0.219769,0.164343]),
        H298 = (85.6592,'kcal/mol','+|-',0.495566),
        S298 = (0.0476657,'cal/(mol*K)','+|-',0.745751),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         8
CHOClBr_G4 |         2
""",
)

entry(
    index = 7,
    label = "CsBr1sCOF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.977717,-1.45636,-1.86809,-2.24133,-2.83579,-3.26685,-3.90411],'cal/(mol*K)','+|-',[0.380332,0.389196,0.364541,0.340311,0.300103,0.262674,0.196427]),
        H298 = (88.8935,'kcal/mol','+|-',0.592315),
        S298 = (-1.10963,'cal/(mol*K)','+|-',0.891343),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         7
""",
)

entry(
    index = 8,
    label = "CsCOCl1sF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.22697,-1.55808,-1.89386,-2.20446,-2.70713,-3.10769,-3.80702],'cal/(mol*K)','+|-',[0.380332,0.389196,0.364541,0.340311,0.300103,0.262674,0.196427]),
        H298 = (88.6672,'kcal/mol','+|-',0.592315),
        S298 = (-1.26647,'cal/(mol*K)','+|-',0.891343),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         4
CHOFClBr_G4 |         3
""",
)

entry(
    index = 9,
    label = "CsCOF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.114833,-0.447746,-0.938002,-1.43026,-2.29597,-2.93054,-3.80896],'cal/(mol*K)','+|-',[0.279087,0.285592,0.2675,0.24972,0.220215,0.19275,0.144138]),
        H298 = (92.3731,'kcal/mol','+|-',0.43464),
        S298 = (-2.25107,'cal/(mol*K)','+|-',0.654067),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         7
CHOFCl_G4 |         1
CHOFBr_G4 |         5
""",
)

entry(
    index = 10,
    label = "CsBr1sCOH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.434914,-0.781665,-1.14199,-1.46951,-2.09165,-2.6703,-3.76698],'cal/(mol*K)','+|-',[0.410805,0.42038,0.39375,0.367578,0.324148,0.283721,0.212165]),
        H298 = (90.335,'kcal/mol','+|-',0.639773),
        S298 = (-1.98245,'cal/(mol*K)','+|-',0.96276),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 11,
    label = "CsCOCl1sH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.80433,-0.962668,-1.24881,-1.53549,-2.09622,-2.61788,-3.57454],'cal/(mol*K)','+|-',[0.279087,0.285592,0.2675,0.24972,0.220215,0.19275,0.144138]),
        H298 = (88.3027,'kcal/mol','+|-',0.43464),
        S298 = (-2.06491,'cal/(mol*K)','+|-',0.654067),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         8
CHOClBr_G4 |         5
""",
)

entry(
    index = 12,
    label = "CsCOF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18361,-1.43197,-1.78593,-2.16254,-2.82112,-3.2789,-4.02742],'cal/(mol*K)','+|-',[0.225007,0.230252,0.215666,0.201331,0.177543,0.1554,0.116208]),
        H298 = (89.9362,'kcal/mol','+|-',0.350418),
        S298 = (-1.71373,'cal/(mol*K)','+|-',0.527325),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         8
CHOFCl_G4   |         3
CHOFClBr_G4 |         1
CHOFBr_G4   |         8
""",
)

entry(
    index = 13,
    label = "CsBr1sCOO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06989,-2.96139,-3.42753,-3.62903,-3.80578,-3.865,-3.99777],'cal/(mol*K)','+|-',[0.503132,0.514858,0.482243,0.450189,0.396999,0.347485,0.259848]),
        H298 = (83.0654,'kcal/mol','+|-',0.783558),
        S298 = (-0.516226,'cal/(mol*K)','+|-',1.17914),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         2
CHOFBr_G4  |         1
CHOClBr_G4 |         1
""",
)

entry(
    index = 14,
    label = "CsCOCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.30789,-3.14343,-3.54971,-3.65949,-3.72569,-3.71624,-3.64574],'cal/(mol*K)','+|-',[0.580966,0.594507,0.556846,0.519833,0.458415,0.401241,0.300047]),
        H298 = (81.7661,'kcal/mol','+|-',0.904775),
        S298 = (0.125636,'cal/(mol*K)','+|-',1.36155),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOCl_G4  |         2
CHOFCl_G4 |         1
""",
)

entry(
    index = 15,
    label = "CsCOF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00005,-2.77291,-3.25129,-3.46512,-3.63633,-3.66557,-3.58204],'cal/(mol*K)','+|-',[0.711535,0.728119,0.681994,0.636663,0.561441,0.491418,0.367481]),
        H298 = (85.1381,'kcal/mol','+|-',1.10812),
        S298 = (0.447461,'cal/(mol*K)','+|-',1.66755),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 16,
    label = "CsBr1sCOCO",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "CsCOCOCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "CsCOCOF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "CsBr1sCOCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "CsCOCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "CsCOCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "CsBr1sCOCd",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "CsCOCdCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "CsCOCdF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "CsBr1sCOCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   CO   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9623,-2.33493,-2.59894,-2.81599,-3.18812,-3.51323,-4.09122],'cal/(mol*K)','+|-',[0.244055,0.249743,0.233922,0.218374,0.192573,0.168555,0.126045]),
        H298 = (88.1116,'kcal/mol','+|-',0.380082),
        S298 = (1.43586,'cal/(mol*K)','+|-',0.571965),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         3
CHOFClBr_G4 |         1
CHOFBr_G4   |         9
CHOClBr_G4  |         4
""",
)

entry(
    index = 26,
    label = "CsCOCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   CO   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36723,-1.86501,-2.30191,-2.65374,-3.18409,-3.56287,-4.14002],'cal/(mol*K)','+|-',[0.3034,0.310471,0.290803,0.271474,0.239399,0.209542,0.156694]),
        H298 = (86.9272,'kcal/mol','+|-',0.472504),
        S298 = (1.27989,'cal/(mol*K)','+|-',0.711045),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         8
CHOFCl_G4   |         1
CHOFClBr_G4 |         1
CHOClBr_G4  |         1
""",
)

entry(
    index = 27,
    label = "CsCOCsF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   CO  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31272,-1.63216,-2.02142,-2.40946,-3.0498,-3.49232,-4.01408],'cal/(mol*K)','+|-',[0.290483,0.297253,0.278423,0.259917,0.229207,0.200621,0.150024]),
        H298 = (89.2932,'kcal/mol','+|-',0.452388),
        S298 = (0.0367457,'cal/(mol*K)','+|-',0.680774),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         8
CHOFCl_G4 |         1
CHOFBr_G4 |         3
""",
)

entry(
    index = 28,
    label = "CsBr1sBr1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01928,-2.11344,-2.91245,-3.51863,-4.30204,-4.69417,-4.91746],'cal/(mol*K)','+|-',[0.219585,0.224702,0.210468,0.196479,0.173264,0.151655,0.113407]),
        H298 = (94.7322,'kcal/mol','+|-',0.341973),
        S298 = (3.04996,'cal/(mol*K)','+|-',0.514617),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         19
CHOFBr_G4  |         1
CHOClBr_G4 |         1
""",
)

entry(
    index = 29,
    label = "CsBr1sCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24794,-1.27652,-2.11139,-2.77556,-3.71217,-4.32038,-5.07912],'cal/(mol*K)','+|-',[0.259816,0.265872,0.249029,0.232477,0.205009,0.179441,0.134185]),
        H298 = (95.0803,'kcal/mol','+|-',0.404628),
        S298 = (5.58262,'cal/(mol*K)','+|-',0.608903),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFClBr_G4 |         1
CHOClBr_G4  |         14
""",
)

entry(
    index = 30,
    label = "CsCl1sCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.205255,-1.2948,-2.25684,-3.01284,-4.03108,-4.61632,-5.20431],'cal/(mol*K)','+|-',[0.163237,0.167042,0.15646,0.146061,0.128803,0.112739,0.084306]),
        H298 = (94.8893,'kcal/mol','+|-',0.25422),
        S298 = (4.23056,'cal/(mol*K)','+|-',0.382562),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         31
CHOFCl_G4  |         1
CHOClBr_G4 |         6
""",
)

entry(
    index = 31,
    label = "CsBr1sF1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.120238,-0.647923,-1.5211,-2.24019,-3.3314,-4.06049,-4.9272],'cal/(mol*K)','+|-',[0.230853,0.236233,0.221268,0.206561,0.182156,0.159437,0.119227]),
        H298 = (97.9,'kcal/mol','+|-',0.359521),
        S298 = (2.88377,'cal/(mol*K)','+|-',0.541024),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         19
""",
)

entry(
    index = 32,
    label = "CsCl1sF1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.169994,-0.664701,-1.55436,-2.28286,-3.36294,-4.09029,-4.93399],'cal/(mol*K)','+|-',[0.214536,0.219536,0.205629,0.191961,0.169281,0.148168,0.1108]),
        H298 = (98.5996,'kcal/mol','+|-',0.33411),
        S298 = (3.30973,'cal/(mol*K)','+|-',0.502785),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         15
CHOFClBr_G4 |         7
""",
)

entry(
    index = 33,
    label = "CsF1sF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.778734,-1.53103,-2.08219,-2.53994,-3.29184,-3.8508,-4.68196],'cal/(mol*K)','+|-',[0.129908,0.132936,0.124515,0.116238,0.102505,0.0897204,0.0670926]),
        H298 = (103.113,'kcal/mol','+|-',0.202314),
        S298 = (2.20659,'cal/(mol*K)','+|-',0.304451),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         33
CHOFCl_G4   |         9
CHOFClBr_G4 |         1
CHOFBr_G4   |         17
""",
)

entry(
    index = 34,
    label = "CsBr1sHO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.613115,-0.114558,-1.00931,-1.73619,-2.8384,-3.60839,-4.73531],'cal/(mol*K)','+|-',[0.201253,0.205943,0.192897,0.180076,0.1588,0.138994,0.103939]),
        H298 = (96.8021,'kcal/mol','+|-',0.313423),
        S298 = (0.858236,'cal/(mol*K)','+|-',0.471654),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         23
CHOFBr_G4  |         1
CHOClBr_G4 |         1
""",
)

entry(
    index = 35,
    label = "CsCl1sHO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.524793,-0.359081,-1.26984,-1.97666,-3.02373,-3.72869,-4.68384],'cal/(mol*K)','+|-',[0.150005,0.153501,0.143777,0.13422,0.118362,0.1036,0.0774718]),
        H298 = (96.294,'kcal/mol','+|-',0.233612),
        S298 = (1.10346,'cal/(mol*K)','+|-',0.35155),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         31
CHOFCl_G4  |         1
CHOClBr_G4 |         13
""",
)

entry(
    index = 36,
    label = "CsF1sHO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.033938,-0.721524,-1.4199,-2.01089,-2.94865,-3.62703,-4.6039],'cal/(mol*K)','+|-',[0.122027,0.124871,0.116961,0.109187,0.0962864,0.0842776,0.0630225]),
        H298 = (99.7763,'kcal/mol','+|-',0.190041),
        S298 = (1.69417,'cal/(mol*K)','+|-',0.285982),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         33
CHOFCl_G4   |         13
CHOFClBr_G4 |         6
CHOFBr_G4   |         16
""",
)

entry(
    index = 37,
    label = "CsBr1sO2sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.681089,-1.65099,-2.3705,-2.85413,-3.61187,-4.15796,-4.8243],'cal/(mol*K)','+|-',[0.268935,0.275203,0.25777,0.240636,0.212205,0.185739,0.138895]),
        H298 = (94.7306,'kcal/mol','+|-',0.41883),
        S298 = (3.26482,'cal/(mol*K)','+|-',0.630274),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         4
CHOFClBr_G4 |         1
CHOFBr_G4   |         6
CHOClBr_G4  |         3
""",
)

entry(
    index = 38,
    label = "CsCl1sO2sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.492434,-2.3146,-3.29062,-3.80665,-4.50572,-4.90385,-5.24337],'cal/(mol*K)','+|-',[0.410805,0.42038,0.39375,0.367578,0.324148,0.283721,0.212165]),
        H298 = (96.2474,'kcal/mol','+|-',0.639773),
        S298 = (4.22306,'cal/(mol*K)','+|-',0.96276),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOCl_G4  |         5
CHOFCl_G4 |         1
""",
)

entry(
    index = 39,
    label = "CsF1sO2sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9976,-2.68003,-2.85561,-3.05791,-3.47427,-3.77563,-4.20926],'cal/(mol*K)','+|-',[0.355768,0.36406,0.340997,0.318332,0.280721,0.245709,0.183741]),
        H298 = (101.087,'kcal/mol','+|-',0.55406),
        S298 = (3.00532,'cal/(mol*K)','+|-',0.833775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         5
CHOFCl_G4 |         2
CHOFBr_G4 |         1
""",
)

entry(
    index = 40,
    label = "CsBr1sBr1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.129472,-0.934237,-1.56595,-2.09216,-2.93783,-3.57706,-4.54461],'cal/(mol*K)','+|-',[0.380332,0.389196,0.364541,0.340311,0.300103,0.262674,0.196427]),
        H298 = (84.6657,'kcal/mol','+|-',0.592315),
        S298 = (0.356232,'cal/(mol*K)','+|-',0.891343),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         5
CHOFBr_G4  |         1
CHOClBr_G4 |         1
""",
)

entry(
    index = 41,
    label = "CsBr1sCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.219038,-0.936655,-1.58634,-2.17912,-3.11889,-3.77716,-4.70025],'cal/(mol*K)','+|-',[0.450015,0.460503,0.431331,0.402661,0.355086,0.3108,0.232415]),
        H298 = (84.3736,'kcal/mol','+|-',0.700836),
        S298 = (2.35583,'cal/(mol*K)','+|-',1.05465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFClBr_G4 |         1
CHOClBr_G4  |         4
""",
)

entry(
    index = 42,
    label = "CsCl1sCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.131238,-0.664074,-1.33007,-1.88375,-2.76731,-3.42317,-4.40269],'cal/(mol*K)','+|-',[0.335421,0.343239,0.321495,0.300126,0.264666,0.231657,0.173232]),
        H298 = (83.5889,'kcal/mol','+|-',0.522372),
        S298 = (1.11107,'cal/(mol*K)','+|-',0.78609),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         7
CHOFCl_G4  |         1
CHOClBr_G4 |         1
""",
)

entry(
    index = 43,
    label = "CsBr1sCtF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.619447,-0.448637,-1.16481,-1.75279,-2.70333,-3.40779,-4.45179],'cal/(mol*K)','+|-',[1.00626,1.02972,0.964485,0.900377,0.793997,0.69497,0.519696]),
        H298 = (88.5703,'kcal/mol','+|-',1.56712),
        S298 = (2.98074,'cal/(mol*K)','+|-',2.35827),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         1
""",
)

entry(
    index = 44,
    label = "CsCl1sCtF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.252954,-0.590735,-1.32627,-1.94695,-2.93378,-3.64431,-4.67477],'cal/(mol*K)','+|-',[0.450015,0.460503,0.431331,0.402661,0.355086,0.3108,0.232415]),
        H298 = (88.463,'kcal/mol','+|-',0.700836),
        S298 = (1.85725,'cal/(mol*K)','+|-',1.05465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         4
CHOFClBr_G4 |         1
""",
)

entry(
    index = 45,
    label = "CsCtF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.892215,0.0755021,-0.696053,-1.36041,-2.41909,-3.1969,-4.3354],'cal/(mol*K)','+|-',[0.355768,0.36406,0.340997,0.318332,0.280721,0.245709,0.183741]),
        H298 = (93.9773,'kcal/mol','+|-',0.55406),
        S298 = (0.5544,'cal/(mol*K)','+|-',0.833775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         6
CHOFCl_G4 |         1
CHOFBr_G4 |         1
""",
)

entry(
    index = 46,
    label = "CsBr1sCtH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.219477,-0.35918,-1.00576,-1.60069,-2.58125,-3.31551,-4.41953],'cal/(mol*K)','+|-',[0.355768,0.36406,0.340997,0.318332,0.280721,0.245709,0.183741]),
        H298 = (87.3539,'kcal/mol','+|-',0.55406),
        S298 = (1.22389,'cal/(mol*K)','+|-',0.833775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         6
CHOFBr_G4  |         1
CHOClBr_G4 |         1
""",
)

entry(
    index = 47,
    label = "CsCl1sCtH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.334384,-0.267977,-0.888879,-1.45517,-2.4214,-3.17414,-4.33315],'cal/(mol*K)','+|-',[0.318208,0.325625,0.304997,0.284724,0.251084,0.219769,0.164343]),
        H298 = (86.2853,'kcal/mol','+|-',0.495566),
        S298 = (1.36537,'cal/(mol*K)','+|-',0.745751),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         6
CHOFCl_G4  |         1
CHOClBr_G4 |         3
""",
)

entry(
    index = 48,
    label = "CsCtF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.457276,-0.1203,-0.789616,-1.4125,-2.45076,-3.23275,-4.42834],'cal/(mol*K)','+|-',[0.244055,0.249743,0.233922,0.218374,0.192573,0.168555,0.126045]),
        H298 = (88.3784,'kcal/mol','+|-',0.380082),
        S298 = (1.22145,'cal/(mol*K)','+|-',0.571965),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         7
CHOFCl_G4   |         3
CHOFClBr_G4 |         1
CHOFBr_G4   |         6
""",
)

entry(
    index = 49,
    label = "CsBr1sCtO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "CsCl1sCtO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "CsCtF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "CsBr1sCtCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Ct   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "CsCl1sCtCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Ct   u0 {1,S}
3   Ct   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "CsCtCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   Ct  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "CsBr1sBr1sCd",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01591,-1.58193,-2.07384,-2.47821,-3.07666,-3.49012,-4.07695],'cal/(mol*K)','+|-',[0.177884,0.18203,0.170499,0.159166,0.14036,0.122855,0.0918703]),
        H298 = (85.6972,'kcal/mol','+|-',0.27703),
        S298 = (-0.0170482,'cal/(mol*K)','+|-',0.416887),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         17
CHOFClBr_G4 |         1
CHOFBr_G4   |         9
CHOClBr_G4  |         5
""",
)

entry(
    index = 56,
    label = "CsBr1sCdCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.786963,-1.4274,-1.95924,-2.37947,-3.02804,-3.50058,-4.23908],'cal/(mol*K)','+|-',[0.205403,0.21019,0.196875,0.183789,0.162074,0.14186,0.106083]),
        H298 = (84.4668,'kcal/mol','+|-',0.319886),
        S298 = (0.254596,'cal/(mol*K)','+|-',0.48138),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFClBr_G4 |         8
CHOClBr_G4  |         16
""",
)

entry(
    index = 57,
    label = "CsCdCl1sCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.873071,-1.35561,-1.80755,-2.20663,-2.85245,-3.32108,-4.01443],'cal/(mol*K)','+|-',[0.127796,0.130774,0.12249,0.114348,0.100838,0.0882614,0.0660016]),
        H298 = (84.3383,'kcal/mol','+|-',0.199024),
        S298 = (-0.855791,'cal/(mol*K)','+|-',0.299501),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         44
CHOFCl_G4  |         8
CHOClBr_G4 |         10
""",
)

entry(
    index = 58,
    label = "CsBr1sCdF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04874,-1.57052,-1.9928,-2.36333,-2.94317,-3.3614,-3.96494],'cal/(mol*K)','+|-',[0.201253,0.205943,0.192897,0.180076,0.1588,0.138994,0.103939]),
        H298 = (87.6069,'kcal/mol','+|-',0.313423),
        S298 = (0.560886,'cal/(mol*K)','+|-',0.471654),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         25
""",
)

entry(
    index = 59,
    label = "CsCdCl1sF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.739951,-1.17699,-1.66127,-2.07935,-2.72121,-3.17191,-3.86938],'cal/(mol*K)','+|-',[0.193655,0.198169,0.185615,0.173278,0.152805,0.133747,0.100016]),
        H298 = (86.9457,'kcal/mol','+|-',0.301592),
        S298 = (1.10392,'cal/(mol*K)','+|-',0.453849),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         18
CHOFClBr_G4 |         9
""",
)

entry(
    index = 60,
    label = "CsCdF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.40857,-0.831437,-1.27778,-1.69171,-2.40654,-2.95432,-3.78401],'cal/(mol*K)','+|-',[0.123862,0.126749,0.11872,0.110829,0.0977344,0.085545,0.0639703]),
        H298 = (92.8812,'kcal/mol','+|-',0.192899),
        S298 = (-0.199788,'cal/(mol*K)','+|-',0.290283),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         40
CHOFCl_G4   |         7
CHOFClBr_G4 |         1
CHOFBr_G4   |         18
""",
)

entry(
    index = 61,
    label = "CsBr1sCdH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.17728,-0.587649,-1.0765,-1.51368,-2.21006,-2.76289,-3.70594],'cal/(mol*K)','+|-',[0.167711,0.171619,0.160748,0.150063,0.132333,0.115828,0.0866161]),
        H298 = (85.8424,'kcal/mol','+|-',0.261186),
        S298 = (-1.29433,'cal/(mol*K)','+|-',0.393045),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         23
CHOFClBr_G4 |         4
CHOFBr_G4   |         8
CHOClBr_G4  |         1
""",
)

entry(
    index = 62,
    label = "CsCdCl1sH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.275131,-0.581132,-0.980326,-1.36445,-2.03632,-2.59642,-3.59125],'cal/(mol*K)','+|-',[0.116193,0.118901,0.111369,0.103967,0.091683,0.0802483,0.0600094]),
        H298 = (84.3217,'kcal/mol','+|-',0.180955),
        S298 = (-1.31917,'cal/(mol*K)','+|-',0.27231),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         40
CHOFCl_G4   |         10
CHOFClBr_G4 |         1
CHOClBr_G4  |         24
""",
)

entry(
    index = 63,
    label = "CsCdF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.386883,-0.536176,-0.889276,-1.27496,-1.98269,-2.55733,-3.5178],'cal/(mol*K)','+|-',[0.0996349,0.101957,0.0954984,0.0891507,0.0786175,0.0688124,0.0514577]),
        H298 = (85.6325,'kcal/mol','+|-',0.155168),
        S298 = (-1.03551,'cal/(mol*K)','+|-',0.233504),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         43
CHOFCl_G4   |         17
CHOFClBr_G4 |         5
CHOFBr_G4   |         37
""",
)

entry(
    index = 64,
    label = "CsBr1sCdO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "CsCdCl1sO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "CsCdF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "CsBr1sCdCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Ct   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "CsCdCl1sCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Ct   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "CsCdCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   Ct  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "CsBr1sCdCd",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cd   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "CsCdCdCl1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S}
3   Cd   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "CsCdCdF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "CsBr1sBr1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17733,-2.12595,-2.85583,-3.42914,-4.20173,-4.62964,-4.99879],'cal/(mol*K)','+|-',[0.125783,0.128715,0.120561,0.112547,0.0992497,0.0868714,0.0649621]),
        H298 = (93.7666,'kcal/mol','+|-',0.19589),
        S298 = (3.44361,'cal/(mol*K)','+|-',0.294784),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         53
CHOFClBr_G4 |         1
CHOFBr_G4   |         6
CHOClBr_G4  |         4
""",
)

entry(
    index = 74,
    label = "CsBr1sCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cl1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.712648,-1.58607,-2.28999,-2.8685,-3.71586,-4.27587,-4.99393],'cal/(mol*K)','+|-',[0.146779,0.1502,0.140685,0.131334,0.115816,0.101372,0.0758056]),
        H298 = (93.444,'kcal/mol','+|-',0.228588),
        S298 = (4.17242,'cal/(mol*K)','+|-',0.343989),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFClBr_G4 |         4
CHOClBr_G4  |         43
""",
)

entry(
    index = 75,
    label = "CsCl1sCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.446355,-1.47501,-2.3157,-2.99059,-3.91813,-4.4785,-5.14413],'cal/(mol*K)','+|-',[0.0708004,0.0724506,0.067861,0.0633504,0.0558655,0.048898,0.0365657]),
        H298 = (92.1113,'kcal/mol','+|-',0.110262),
        S298 = (3.66045,'cal/(mol*K)','+|-',0.165927),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         161
CHOFCl_G4  |         2
CHOClBr_G4 |         39
""",
)

entry(
    index = 76,
    label = "CsBr1sCsF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   F1s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432944,-1.42886,-2.23195,-2.87954,-3.76549,-4.2896,-4.92068],'cal/(mol*K)','+|-',[0.122027,0.124871,0.116961,0.109187,0.0962864,0.0842776,0.0630225]),
        H298 = (96.582,'kcal/mol','+|-',0.190041),
        S298 = (3.86519,'cal/(mol*K)','+|-',0.285982),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         68
""",
)

entry(
    index = 77,
    label = "CsCl1sCsF1s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   F1s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.233802,-1.18939,-1.96615,-2.5783,-3.4616,-4.05151,-4.81647],'cal/(mol*K)','+|-',[0.111807,0.114413,0.107165,0.100042,0.088222,0.077219,0.0577441]),
        H298 = (96.6239,'kcal/mol','+|-',0.174124),
        S298 = (3.50686,'cal/(mol*K)','+|-',0.26203),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         45
CHOFClBr_G4 |         36
""",
)

entry(
    index = 78,
    label = "CsCsF1sF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31705,-1.15724,-1.85433,-2.4141,-3.26386,-3.876,-4.79239],'cal/(mol*K)','+|-',[0.0575242,0.058865,0.055136,0.0514712,0.0453898,0.0397288,0.0297091]),
        H298 = (100.512,'kcal/mol','+|-',0.0895861),
        S298 = (2.80065,'cal/(mol*K)','+|-',0.134813),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         163
CHOFCl_G4   |         38
CHOFClBr_G4 |         9
CHOFBr_G4   |         96
""",
)

entry(
    index = 79,
    label = "CsBr1sCsH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   H    u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0860589,-1.12834,-1.96863,-2.64147,-3.60194,-4.21276,-4.99222],'cal/(mol*K)','+|-',[0.113937,0.116592,0.109207,0.101948,0.0899025,0.07869,0.0588441]),
        H298 = (97.5213,'kcal/mol','+|-',0.177441),
        S298 = (3.87558,'cal/(mol*K)','+|-',0.267022),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         64
CHOFClBr_G4 |         2
CHOFBr_G4   |         8
CHOClBr_G4  |         4
""",
)

entry(
    index = 80,
    label = "CsCl1sCsH",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   H    u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.196281,-0.860331,-1.75784,-2.46694,-3.47216,-4.11959,-4.95488],'cal/(mol*K)','+|-',[0.062769,0.0642319,0.060163,0.056164,0.0495282,0.0433511,0.0324178]),
        H298 = (95.9727,'kcal/mol','+|-',0.0977541),
        S298 = (3.64388,'cal/(mol*K)','+|-',0.147105),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         153
CHOFCl_G4  |         6
CHOClBr_G4 |         98
""",
)

entry(
    index = 81,
    label = "CsCsF1sH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.200318,-0.679221,-1.44023,-2.0621,-3.01867,-3.69711,-4.68644],'cal/(mol*K)','+|-',[0.0460736,0.0471475,0.0441608,0.0412255,0.0363547,0.0318205,0.0237953]),
        H298 = (98.9072,'kcal/mol','+|-',0.0717534),
        S298 = (3.27227,'cal/(mol*K)','+|-',0.107978),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         163
CHOFCl_G4   |         103
CHOFClBr_G4 |         45
CHOFBr_G4   |         166
""",
)

entry(
    index = 82,
    label = "CsBr1sCsO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   O2s  u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.74509,-1.82789,-2.57587,-3.16217,-3.98004,-4.45021,-4.89864],'cal/(mol*K)','+|-',[0.120271,0.123075,0.115278,0.107616,0.0949009,0.0830649,0.0621157]),
        H298 = (93.9799,'kcal/mol','+|-',0.187306),
        S298 = (3.71068,'cal/(mol*K)','+|-',0.281867),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         16
CHOFClBr_G4 |         8
CHOFBr_G4   |         31
CHOClBr_G4  |         15
""",
)

entry(
    index = 83,
    label = "CsCl1sCsO2s",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   O2s  u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.137892,-1.16515,-2.04237,-2.73491,-3.7006,-4.29115,-4.98641],'cal/(mol*K)','+|-',[0.134468,0.137602,0.128885,0.120318,0.106102,0.0928694,0.0694474]),
        H298 = (94.3874,'kcal/mol','+|-',0.209415),
        S298 = (3.4988,'cal/(mol*K)','+|-',0.315137),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         38
CHOFCl_G4   |         11
CHOFClBr_G4 |         1
CHOClBr_G4  |         6
""",
)

entry(
    index = 84,
    label = "CsCsF1sO2s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0735327,-1.27866,-2.21889,-2.90854,-3.84402,-4.426,-5.13878],'cal/(mol*K)','+|-',[0.138221,0.141442,0.132482,0.123676,0.109064,0.0954616,0.0713859]),
        H298 = (98.7383,'kcal/mol','+|-',0.21526),
        S298 = (3.48663,'cal/(mol*K)','+|-',0.323933),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         36
CHOFCl_G4   |         5
CHOFClBr_G4 |         1
CHOFBr_G4   |         11
""",
)

entry(
    index = 85,
    label = "CsBr1sCsCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Ct   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.82572,-1.62914,-2.25211,-2.76149,-3.54279,-4.07997,-4.80955],'cal/(mol*K)','+|-',[0.355768,0.36406,0.340997,0.318332,0.280721,0.245709,0.183741]),
        H298 = (85.5595,'kcal/mol','+|-',0.55406),
        S298 = (3.73091,'cal/(mol*K)','+|-',0.833775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         4
CHOFBr_G4  |         3
CHOClBr_G4 |         1
""",
)

entry(
    index = 86,
    label = "CsCl1sCsCt",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Ct   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.341286,-1.14288,-1.85552,-2.44808,-3.3592,-3.98766,-4.79635],'cal/(mol*K)','+|-',[0.279087,0.285592,0.2675,0.24972,0.220215,0.19275,0.144138]),
        H298 = (84.9763,'kcal/mol','+|-',0.43464),
        S298 = (4.00135,'cal/(mol*K)','+|-',0.654067),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         8
CHOFCl_G4   |         2
CHOFClBr_G4 |         1
CHOClBr_G4  |         2
""",
)

entry(
    index = 87,
    label = "CsCsCtF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0249493,-0.845945,-1.61613,-2.2443,-3.17493,-3.82744,-4.79528],'cal/(mol*K)','+|-',[0.237179,0.242706,0.227332,0.212221,0.187147,0.163806,0.122494]),
        H298 = (88.1297,'kcal/mol','+|-',0.369373),
        S298 = (4.37416,'cal/(mol*K)','+|-',0.55585),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         7
CHOFCl_G4   |         2
CHOFClBr_G4 |         1
CHOFBr_G4   |         8
""",
)

entry(
    index = 88,
    label = "CsBr1sCdCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cd   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.491933,-1.27165,-1.8412,-2.31263,-3.01427,-3.47314,-4.05317],'cal/(mol*K)','+|-',[1.00626,1.02972,0.964485,0.900377,0.793997,0.69497,0.519696]),
        H298 = (84.5219,'kcal/mol','+|-',1.56712),
        S298 = (-0.852262,'cal/(mol*K)','+|-',2.35827),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         1
""",
)

entry(
    index = 89,
    label = "CsCdCl1sCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cd   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06079,-1.4982,-1.89189,-2.24122,-2.85895,-3.30708,-3.98505],'cal/(mol*K)','+|-',[0.580966,0.594507,0.556846,0.519833,0.458415,0.401241,0.300047]),
        H298 = (86.2725,'kcal/mol','+|-',0.904775),
        S298 = (-0.0146229,'cal/(mol*K)','+|-',1.36155),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOCl_G4  |         1
CHOFCl_G4 |         2
""",
)

entry(
    index = 90,
    label = "CsCdCsF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.709084,-0.820436,-1.12575,-1.48307,-2.16704,-2.69205,-3.55538],'cal/(mol*K)','+|-',[0.279087,0.285592,0.2675,0.24972,0.220215,0.19275,0.144138]),
        H298 = (84.9698,'kcal/mol','+|-',0.43464),
        S298 = (0.628117,'cal/(mol*K)','+|-',0.654067),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         4
CHOFCl_G4   |         2
CHOFClBr_G4 |         1
CHOFBr_G4   |         6
""",
)

entry(
    index = 91,
    label = "CsBr1sCsCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cs   u0 {1,S}
4   Br1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19507,-2.29895,-3.09853,-3.68635,-4.45283,-4.89673,-5.39291],'cal/(mol*K)','+|-',[0.107883,0.110397,0.103404,0.0965306,0.0851255,0.0745087,0.0557174]),
        H298 = (94.5923,'kcal/mol','+|-',0.168013),
        S298 = (5.86938,'cal/(mol*K)','+|-',0.252833),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         24
CHOFClBr_G4 |         7
CHOFBr_G4   |         39
CHOClBr_G4  |         17
""",
)

entry(
    index = 92,
    label = "CsCl1sCsCs",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cs   u0 {1,S}
4   Cl1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.650662,-1.75094,-2.60765,-3.26755,-4.16351,-4.69758,-5.34915],'cal/(mol*K)','+|-',[0.0882551,0.0903121,0.084591,0.0789683,0.0696382,0.060953,0.0455804]),
        H298 = (93.4505,'kcal/mol','+|-',0.137445),
        S298 = (5.47132,'cal/(mol*K)','+|-',0.206834),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         76
CHOFCl_G4   |         18
CHOFClBr_G4 |         9
CHOClBr_G4  |         27
""",
)

entry(
    index = 93,
    label = "CsCsCsF1s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   F1s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.759753,-1.95172,-2.7021,-3.21475,-3.91006,-4.37474,-5.02968],'cal/(mol*K)','+|-',[0.0803086,0.0821803,0.0769744,0.071858,0.0633679,0.0554647,0.0414763]),
        H298 = (97.6321,'kcal/mol','+|-',0.12507),
        S298 = (4.77013,'cal/(mol*K)','+|-',0.188211),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         80
CHOFCl_G4   |         27
CHOFClBr_G4 |         7
CHOFBr_G4   |         43
""",
)

entry(
    index = 94,
    label = "CH3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol','+|-',0.1),
        S298 = (0.52,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cs_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 97,
    label = "C=C(O)CJ",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-2.3,-4.6,-7.1,-11,-13.5,-16.6],'J/(mol*K)'),
        H298 = (376.8,'kJ/mol'),
        S298 = (-3.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 98,
    label = "CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (3.54,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "CJC(C)OC",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   O2s u0 {1,S} {7,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,1.8,-2,-5.5,-11,-14.7,-19.8],'J/(mol*K)'),
        H298 = (429.9,'kJ/mol'),
        S298 = (7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 100,
    label = "CJC(C)2O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,1.1,-2.1,-5.1,-9.7,-13.1,-18.5],'J/(mol*K)'),
        H298 = (431.1,'kJ/mol'),
        S298 = (5.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 101,
    label = "C=CC(C)(O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.5,-2.7,-5.5,-7.9,-11.8,-14.6,-19],'J/(mol*K)'),
        H298 = (431.9,'kJ/mol'),
        S298 = (9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 102,
    label = "C=CC(O)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,0.9,-2.4,-5.2,-9.7,-13,-18.1],'J/(mol*K)'),
        H298 = (432.3,'kJ/mol'),
        S298 = (6.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 103,
    label = "CJC(C)(C=O)O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.6,5.1,2.3,-0.9,-6.8,-11.3,-17.8],'J/(mol*K)'),
        H298 = (430.9,'kJ/mol'),
        S298 = (3.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 104,
    label = "CJC(O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.4,-1.5,-5,-7.4,-10.8,-13.6,-18.2],'J/(mol*K)'),
        H298 = (435.3,'kJ/mol'),
        S298 = (8.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 105,
    label = "C=CC(O)2CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {8,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-0.2,-2,-4,-8.1,-11.6,-17.2],'J/(mol*K)'),
        H298 = (431.8,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 106,
    label = "CJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.8,-1.5,-4.1,-6.7,-11.1,-14.3,-19.2],'J/(mol*K)'),
        H298 = (430,'kJ/mol'),
        S298 = (6.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 107,
    label = "CJC(C)2C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.9,2.5,-1.1,-4.4,-9.7,-13.6,-19],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (7.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 108,
    label = "CJC(C=O)2C",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.5,0.6,-1.9,-6.9,-10.9,-17.1],'J/(mol*K)'),
        H298 = (427,'kJ/mol'),
        S298 = (8.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 109,
    label = "C=CC(C=O)2CJ",
    group = 
"""
1    Cs  u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs  u1 {1,S} {6,S} {7,S}
3    CO  u0 {1,S} {9,D}
4    CO  u0 {1,S} {10,D}
5    Cd  u0 {1,S} {8,D}
6    H   u0 {2,S}
7    H   u0 {2,S}
8    C   u0 {5,D}
9    O2d u0 {3,D}
10   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,2.4,-0.6,-3.5,-8.4,-12.1,-17.6],'J/(mol*K)'),
        H298 = (429.8,'kJ/mol'),
        S298 = (5.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 110,
    label = "C=CC(C)(C=O)CJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   C   u0 {4,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,0.6,-2.7,-5.8,-10.8,-14.4,-19.3],'J/(mol*K)'),
        H298 = (430.6,'kJ/mol'),
        S298 = (9.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 111,
    label = "CJC(C)C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6,0.2,-3,-5.8,-10.5,-14.1,-19.3],'J/(mol*K)'),
        H298 = (429.5,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 112,
    label = "C=C(C=O)CJ",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * Cs  u1 {1,S} {5,S} {6,S}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,D}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8,-1.2,-2.4,-4.4,-8.2,-11.3,-15.9],'J/(mol*K)'),
        H298 = (374,'kJ/mol'),
        S298 = (-16.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 113,
    label = "CJCC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {5,S} {6,S}
2   C   u0 {1,S} {3,S}
3   Cd  u0 {2,S} {4,D}
4   Cdd u0 {3,D} {7,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3,-5.8,-8.1,-10.1,-13.4,-15.9,-19.9],'J/(mol*K)'),
        H298 = (420.3,'kJ/mol'),
        S298 = (16.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 114,
    label = "CJC(C)C=C=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {5,S}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,S}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.2,-0.5,-4.1,-7.2,-11.8,-15,-19.5],'J/(mol*K)'),
        H298 = (430.1,'kJ/mol'),
        S298 = (9.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 115,
    label = "C=C(CJ)C=C=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {5,D}
2 * Cs  u1 {1,S} {6,S} {7,S}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {8,D}
5   C   u0 {1,D}
6   H   u0 {2,S}
7   H   u0 {2,S}
8   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-5.6,-5.7,-6.4,-8.2,-10,-12.8],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (-8.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 116,
    label = "CsCsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cs_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "CCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.21,-1.75,-2.24,-3.02,-3.63,-3.63],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "RCCJ",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "Neopentyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.32,-2.05,-2.65,-3.5,-4.06,-4.87],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (3.03,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "Isobutyl",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {6,S} {7,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {2,S}
7   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54,-1.26,-1.92,-2.46,-3.27,-3.84,-3.84],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.91,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "Benzyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.492,0.642,0.109,-0.656,-1.606,-2.293,-4.101],'cal/(mol*K)'),
        H298 = (90.788,'kcal/mol','+|-',2.4),
        S298 = (-5.163,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted From  Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
[CH2]C1C=CC=CC=1
""",
)

entry(
    index = 122,
    label = "Allyl_P",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (-2.56,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "C=CC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],'cal/(mol*K)'),
        H298 = (80,'kcal/mol'),
        S298 = (-1.55,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "CTCC=CCJ",
    group = 
"""
1 * Cs u1 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Ct u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],'cal/(mol*K)'),
        H298 = (81,'kcal/mol'),
        S298 = (-3.55,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "CJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-2.6,-4.5,-8.1,-11,-15.6],'J/(mol*K)'),
        H298 = (373.5,'kJ/mol'),
        S298 = (-1.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 126,
    label = "Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],'cal/(mol*K)'),
        H298 = (89.4,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "CJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.5,1.1,-0.4,-2.3,-6.1,-9.2,-14.4],'J/(mol*K)'),
        H298 = (402.4,'kJ/mol'),
        S298 = (-7.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 128,
    label = "C2JC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],'cal/(mol*K)'),
        H298 = (94.4,'kcal/mol'),
        S298 = (-1.16,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "Cs_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.33,-3.1,-3.39,-3.75,-4.45,-5.2],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.44,'cal/(mol*K)'),
    ),
    shortDesc = """Generic secondary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 131,
    label = "C=CCJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2s u0 {2,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.2,2.4,1,-1.8,-4.5,-9.8],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-19.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 132,
    label = "C=CCJC(O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cs  u0 {1,S} {4,S} {6,S}
3   Cd  u0 {1,S} {8,D}
4   Cd  u0 {2,S} {7,D}
5   H   u0 {1,S}
6   O2s u0 {2,S}
7   C   u0 {4,D}
8   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3,-4.5,-3,-2.8,-3.9,-5.6,-10.2],'J/(mol*K)'),
        H298 = (286.3,'kJ/mol'),
        S298 = (-9.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 133,
    label = "CCJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.4,-2,-2.5,-3.27,-3.84,-4.73],'cal/(mol*K)'),
        H298 = (99.98,'kcal/mol'),
        S298 = (4.79,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "CCJCC=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   C   u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-8.3,-10,-11.6,-14.5,-16.8,-20.3],'J/(mol*K)'),
        H298 = (416.9,'kJ/mol'),
        S298 = (13.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 135,
    label = "CCJC(C)=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   C   u0 {1,S} {6,S}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,S}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-4,-6.2,-7.9,-10.8,-12.9,-16.9],'J/(mol*K)'),
        H298 = (365.4,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 136,
    label = "(Cs)2CsJ",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'Cs_S',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "cyclopentene-4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "bicyclo[2.1.1]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (104.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.2,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "bicyclo[2.1.0]pent-2-ene-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "bicyclo[1.1.1]pentane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "tricyclo[1.1.1.0(1,3)]pentane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (111.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "bicyclo[2.1.1]hexane-C5",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C5",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "cyclopropane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """D.F. McMillen, D.M. Golden, HYDROCARBON BOND-DISSOCIATION ENERGIES, Annual Review of Physical Chemistry, 33 (1982) 493-532.. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "spiro[2.2]pentane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2 * Cs u1 {1,S} {3,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (107.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {7,S}
2   Cs u0 {1,S} {3,S} {4,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {5,S}
5   C  u0 {1,S} {4,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "bicyclo[2.1.0]pentane-secondary-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {6,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "bicyclo[1.1.0]butane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {5,S}
4   Cs u0 {1,S} {2,S}
5   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "bicyclo[3.1.0]hexane-C3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {7,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "bicyclo[4.1.0]heptane-C3-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {2,S} {6,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {4,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "tricyclo[2.1.1.0(1,4)]hexane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "bicyclo[3.1.1]heptane-C6",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "bicyclo[2.2.2]octane-C2",
    group = 
"""
1   Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "tricyclo[2.2.2.0(1,4)]octane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S} {8,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {7,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {5,S}
8   C  u0 {2,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "cyclobutane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "bicyclo[2.1.0]pentane-secondary-C4",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {5,S} {6,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "bicyclo[2.2.0]hexane-secondary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {7,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "bicyclo[3.2.0]heptane-C5-6",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S} {7,S}
3 * Cs u1 {1,S} {5,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "bicyclo[4.2.0]octane-C4-7",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {1,S} {4,S} {9,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {1,S} {8,S}
6   C  u0 {2,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {5,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "bicyclo[3.1.1]heptane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "bicyclo[3.1.0]hexane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {3,S} {5,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (93.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "bicyclo[3.1.0]hexane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {6,S} {8,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {1,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "bicyclo[2.1.1]hexane-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {1,S} {6,S} {7,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "7-norbornyl",
    group = 
"""
1   Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3 * Cs u1 {1,S} {2,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "2-norbornyl",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S} {8,S}
2 * Cs u1 {1,S} {5,S} {9,S}
3   Cs u0 {4,S} {5,S} {7,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {1,S}
9   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.02,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "bicyclo[4.1.0]heptane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {4,S} {6,S}
3 * Cs u1 {5,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   Cs u0 {1,S} {3,S}
6   C  u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "cycloheptane",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {8,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {3,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (92.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "bicyclo[3.2.0]heptane-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "bicyclo[3.2.0]heptane-C5-3",
    group = 
"""
1   Cs u0 {2,S} {5,S} {6,S}
2   Cs u0 {1,S} {4,S} {7,S}
3 * Cs u1 {4,S} {5,S} {8,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "bicyclo[4.1.0]heptane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u1 {1,S} {6,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   C  u0 {5,S} {6,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "bicyclo[3.1.1]heptane-C3",
    group = 
"""
1   Cs u0 {4,S} {5,S} {7,S}
2   Cs u0 {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "tricyclo[3.1.1.0(1,5)]heptane-C3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S} {7,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3 * Cs u1 {6,S} {7,S} {8,S}
4   C  u0 {1,S} {2,S}
5   C  u0 {1,S} {2,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {3,S}
8   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "octahydro-pentalene-C5-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {8,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {5,S}
8   C  u0 {4,S} {6,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "octahydro-pentalene-C5-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {5,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {3,S}
6   C  u0 {1,S} {8,S}
7   C  u0 {2,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "bicyclo[4.2.0]octane-C6-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u1 {1,S} {7,S} {9,S}
4   C  u0 {1,S} {5,S}
5   C  u0 {2,S} {4,S}
6   C  u0 {2,S} {8,S}
7   Cs u0 {3,S} {8,S}
8   C  u0 {6,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "bicyclo[4.2.0]octane-C6-3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {5,S} {7,S}
3 * Cs u1 {4,S} {8,S} {9,S}
4   Cs u0 {1,S} {3,S}
5   C  u0 {2,S} {6,S}
6   C  u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
9   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "CCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "RCCJC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (5.13,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "RCCJCC",
    group = 
"""
1    Cs u0 {3,S} {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    C  u0 {2,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "cyclopentane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {6,S} {7,S}
2    Cs u0 {3,S} {5,S} {8,S} {9,S}
3  * Cs u1 {1,S} {2,S} {10,S}
4    C  u0 {1,S} {5,S}
5    C  u0 {2,S} {4,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
10   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (96.4,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "cyclohexane",
    group = 
"""
1    Cs u0 {3,S} {4,S} {7,S} {8,S}
2    Cs u0 {3,S} {5,S} {9,S} {10,S}
3  * Cs u1 {1,S} {2,S} {11,S}
4    C  u0 {1,S} {6,S}
5    C  u0 {2,S} {6,S}
6    C  u0 {4,S} {5,S}
7    H  u0 {1,S}
8    H  u0 {1,S}
9    H  u0 {2,S}
10   H  u0 {2,S}
11   H  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "Benzyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0448,-1.3002,-2.199,-2.5546,-2.5872,-2.8074,-5.6336],'cal/(mol*K)'),
        H298 = (88.064,'kcal/mol','+|-',2.4),
        S298 = (-4.8554,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted From Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 7/2017, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[CH]C1C=CC=CC=1
CC[CH]C1C=CC=CC=1
CCC[CH]C1C=CC=CC=1
CCCC[CH]C1C=CC=CC=1
CCCCC[CH]C1C=CC=CC=1
""",
)

entry(
    index = 192,
    label = "Indenyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cb u0 {1,S} {4,B}
3   Cd u0 {1,S} {5,D}
4   Cb u0 {2,B} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.36,-0.72,-1.23,-1.77,-2.7,-3.43,-4.54],'cal/(mol*K)'),
        H298 = (81.62,'kcal/mol'),
        S298 = (0.69,'cal/(mol*K)'),
    ),
    shortDesc = """A.G. Vandeputte CBS-QB3""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "Benzyl_S_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {6,[S,D,T]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {3,[S,D,T]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.054016,-0.57486,-1.16181,-1.58687,-2.40332,-3.15038,-4.41676],'cal/(mol*K)','+|-',[0.20119,0.20119,0.20119,0.20119,0.20119,0.20119,0.20119]),
        H298 = (88.5038,'kcal/mol','+|-',0.737851),
        S298 = (3.11253,'cal/(mol*K)','+|-',0.434935),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CC[CH]C2=C1
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 194,
    label = "Benzyl_S_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881557,-1.19162,-1.64981,-2.00346,-2.50574,-3.09492,-4.34126],'cal/(mol*K)','+|-',[0.318445,0.318445,0.318445,0.318445,0.318445,0.318445,0.318445]),
        H298 = (86.3797,'kcal/mol','+|-',1.14843),
        S298 = (1.33063,'cal/(mol*K)','+|-',0.744626),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2CCC[CH]C2=C1
CC1CC[CH]C2=CC=CC=C21
CCC1CC[CH]C2=CC=CC=C21
""",
)

entry(
    index = 195,
    label = "Benzyl_S_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {3,[S,D,B]} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.762975,-1.09193,-1.45447,-1.90836,-2.74844,-3.44654,-4.57653],'cal/(mol*K)','+|-',[0.226952,0.226952,0.226952,0.226952,0.226952,0.226952,0.226952]),
        H298 = (83.6682,'kcal/mol','+|-',0.869131),
        S298 = (1.4331,'cal/(mol*K)','+|-',0.350884),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2C=CC[CH]C2=C1
CC1=CC[CH]C2=CC=CC=C12
CCC1=CC[CH]C2=CC=CC=C12

Modified 10/2019 by Max Liu. Added enthalpy of H atom so that GAV predicted
enthalpy for C1=CC=C2C=CC[CH]C2=C1 matches calculated value.
""",
)

entry(
    index = 196,
    label = "Benzyl_S_Fused7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {8,[S,D,T,B]}
4   H  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   C  u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-1.64,-1.86,-2.18,-2.74,-3.34,-4.5],'cal/(mol*K)','+|-',[1.4792,1.4792,1.4792,1.4792,1.4792,1.4792,1.4792]),
        H298 = (92.1,'kcal/mol','+|-',5.4578),
        S298 = (4.72,'cal/(mol*K)','+|-',4.205),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCC[CH]C2=C1
""",
)

entry(
    index = 197,
    label = "Allyl_S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "Aromatic_pi_S_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.013276,-1.28931,-2.31258,-2.92159,-3.39846,-3.6762,-4.8642],'cal/(mol*K)','+|-',[0.023461,0.023461,0.023461,0.023461,0.023461,0.023461,0.023461]),
        H298 = (75.4692,'kcal/mol','+|-',0.139824),
        S298 = (1.48461,'cal/(mol*K)','+|-',0.036353),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1
CC1[CH]CC=CC=1
CC1C=CC[CH]C=1
CC1[CH]C=CC=C1
""",
)

entry(
    index = 199,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S} {8,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {5,S}
9   C  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.104911,-1.14065,-2.32405,-3.03895,-3.75201,-4.05481,-5.14193],'cal/(mol*K)','+|-',[0.061305,0.061305,0.061305,0.061305,0.061305,0.061305,0.061305]),
        H298 = (75.5447,'kcal/mol','+|-',0.399656),
        S298 = (2.79083,'cal/(mol*K)','+|-',0.079011),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1=CC=C[CH]C1C
CC1[CH]C(C)C=CC=1
CC1C=CC(C)[CH]C=1
CC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 200,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.453462,-1.20244,-2.43607,-2.95615,-3.47107,-3.9488,-5.03407],'cal/(mol*K)','+|-',[0.068504,0.068504,0.068504,0.068504,0.068504,0.068504,0.068504]),
        H298 = (74.982,'kcal/mol','+|-',0.417781),
        S298 = (1.24362,'cal/(mol*K)','+|-',0.106961),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1[CH]C=CC=C1C
CCC1[CH]C(C)=CC=C1
CCC1[CH]C=C(C)C=C1
CCC1(C)[CH]C=CC=C1
""",
)

entry(
    index = 201,
    label = "Aromatic_pi_S_(fused5)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S} {10,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 202,
    label = "Aromatic_pi_S_(fused6)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S} {11,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 203,
    label = "Aromatic_pi_S_(fused7)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S} {12,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {10,S} {12,S}
12   C  u0 {8,S} {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.084287,-0.439484,-1.00984,-1.6168,-2.48415,-3.29208,-4.57923],'cal/(mol*K)','+|-',[1.08001,1.08001,1.08001,1.08001,1.08001,1.08001,1.08001]),
        H298 = (76.4252,'kcal/mol','+|-',4.19016),
        S298 = (0.527688,'cal/(mol*K)','+|-',2.02975),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CCCCCC2[CH]1
C1=CC=C2CCCCC(C)C2[CH]1
""",
)

entry(
    index = 204,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.831072,-0.828879,-1.89888,-2.14323,-2.47359,-2.80572,-3.59479],'cal/(mol*K)','+|-',[0.208059,0.208059,0.208059,0.208059,0.208059,0.208059,0.208059]),
        H298 = (74.1331,'kcal/mol','+|-',0.742606),
        S298 = (-0.854817,'cal/(mol*K)','+|-',0.322012),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 205,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S} {8,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {5,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.67718,-0.360591,-1.61836,-2.06586,-2.45313,-2.74791,-3.50658],'cal/(mol*K)','+|-',[0.245046,0.245046,0.245046,0.245046,0.245046,0.245046,0.245046]),
        H298 = (74.3294,'kcal/mol','+|-',0.850906),
        S298 = (-3.58784,'cal/(mol*K)','+|-',0.338262),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 08/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
""",
)

entry(
    index = 206,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 207,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 208,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 209,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 210,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {4,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 211,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 212,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 213,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 214,
    label = "Aromatic_pi_S_(CH3_CH3_Para)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {3,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 215,
    label = "Aromatic_pi_S_(CH3_C2H5_Para)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 216,
    label = "Aromatic_pi_S_(CH3_Benzyl_Para)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 217,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 218,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {8,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {6,S}
9   C  u0 {6,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 219,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {8,S} {9,S}
7   H  u0 {1,S}
8   C  u0 {6,S} {9,S}
9   C  u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.48192,0.127981,-0.882314,-1.47156,-2.2164,-3.23195,-4.40182],'cal/(mol*K)','+|-',[0.7049,0.7049,0.7049,0.7049,0.7049,0.7049,0.7049]),
        H298 = (70.66,'kcal/mol','+|-',4.28202),
        S298 = (-1.77936,'cal/(mol*K)','+|-',1.91485),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCCC1CC12C=C[CH]C=C2
""",
)

entry(
    index = 220,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 221,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S} {10,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85011,2.02306,1.41734,0.955199,-0.252841,-1.61161,-3.21428],'cal/(mol*K)','+|-',[0.733897,0.733897,0.733897,0.733897,0.733897,0.733897,0.733897]),
        H298 = (72.4956,'kcal/mol','+|-',4.45566),
        S298 = (2.72,'cal/(mol*K)','+|-',2.01098),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCCC1CCC12C=C[CH]C=C2
""",
)

entry(
    index = 222,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S} {11,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.344733,-0.12429,-0.432103,-0.924571,-2.30122,-3.16695,-4.31502],'cal/(mol*K)','+|-',[0.781339,0.781339,0.781339,0.781339,0.781339,0.781339,0.781339]),
        H298 = (73.496,'kcal/mol','+|-',4.73954),
        S298 = (-3.2868,'cal/(mol*K)','+|-',2.17587),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CCC1CCCC12C=C[CH]C=C2
""",
)

entry(
    index = 223,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S} {12,S}
9    C  u0 {6,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {10,S} {12,S}
12   C  u0 {8,S} {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.226242,-0.404788,-1.08177,-1.65237,-2.56959,-3.27321,-4.6477],'cal/(mol*K)','+|-',[0.872202,0.872202,0.872202,0.872202,0.872202,0.872202,0.872202]),
        H298 = (74.0097,'kcal/mol','+|-',5.28577),
        S298 = (-1.20585,'cal/(mol*K)','+|-',2.5221),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
CC1CCCCC12C=C[CH]C=C2
""",
)

entry(
    index = 224,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S}
9    C  u0 {6,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 225,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S} {9,S}
7    H  u0 {1,S}
8    C  u0 {6,S}
9    Cs u0 {6,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 226,
    label = "CJ-Cd-Benzene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {7,S}
4   H  u0 {1,S}
5   Cd u0 {2,D} {6,S}
6   Cb u0 {5,S} {7,B}
7   Cb u0 {3,S} {6,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.038694,-0.486795,-1.26614,-1.94355,-2.84643,-3.50953,-4.60995],'cal/(mol*K)','+|-',[0.244001,0.244001,0.244001,0.244001,0.244001,0.244001,0.244001]),
        H298 = (80.0557,'kcal/mol','+|-',0.913362),
        S298 = (1.93251,'cal/(mol*K)','+|-',0.367823),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C1=CC=C2C=C[CH]CC2=C1
CC1[CH]C=CC2=CC=CC=C12
CC1=C[CH]CC2=CC=CC=C12
CCC1[CH]C=CC2=CC=CC=C12
CCC1=C[CH]CC2=CC=CC=C12
""",
)

entry(
    index = 227,
    label = "CJ-Cd-Benzene7",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cs u0 {1,S} {8,S}
4   H  u0 {1,S}
5   Cd u0 {2,D} {6,S}
6   Cb u0 {5,S} {7,B}
7   Cb u0 {6,B} {8,S}
8   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.5,-1,-1.5,-2.5,-3.3,-4.5],'cal/(mol*K)','+|-',[2.4642,2.4642,2.4642,2.4642,2.4642,2.4642,2.4642]),
        H298 = (80.7,'kcal/mol','+|-',7.3256),
        S298 = (1,'cal/(mol*K)','+|-',3.8642),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 04/2019, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds include:
C1=CC=C2CC[CH]C=CC2=C1
""",
)

entry(
    index = 228,
    label = "cyclobutene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (91.2,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "cyclopentene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.3,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Furuyama, S.; Golden, D. M.; Benson, S. W., "Kinetic Study of the Gas-Phase Reaction c-C5H8+I2 c-C5H6+2HI. Heat of Formation and the Stabilization Energy of the Cyclopentenyl Radical,"Int. J. Chem. Kinet. 1970, 2, 93-99. S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "cyclohexene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {7,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,D}
4   C  u0 {2,S} {6,S}
5   Cd u0 {3,D} {6,S}
6   C  u0 {4,S} {5,S}
7   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """Alfassi, Z. B.; Feldman, L., "The Kinetics of Radiation-Induced Hydrogen Abstraction by Trichloromethyl Radicals in the Liquid Phase: Cyclohexene," Int. J. Chem. Kinet. 1981, 13, 771-783. S, Cp copied from Allyl_S""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "C=CCJC=C",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (76,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "Aromatic_pi_S_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 233,
    label = "Aromatic_pi_S_(CH3_CH3_Ortho)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {8,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {3,S}
9   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 234,
    label = "Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 235,
    label = "Aromatic_pi_S_(fused5)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S} {10,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.748775,0.045256,-0.710099,-1.36165,-2.51235,-3.30599,-4.5709],'cal/(mol*K)','+|-',[0.098378,0.098378,0.098378,0.098378,0.098378,0.098378,0.098378]),
        H298 = (74.4829,'kcal/mol','+|-',1.11628),
        S298 = (0.780097,'cal/(mol*K)','+|-',0.163349),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
""",
)

entry(
    index = 236,
    label = "Aromatic_pi_S_(fused6)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S} {11,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.01284,-0.508381,-1.05994,-1.55009,-2.56531,-3.36004,-4.58598],'cal/(mol*K)','+|-',[0.129371,0.129371,0.129371,0.129371,0.129371,0.129371,0.129371]),
        H298 = (73.7347,'kcal/mol','+|-',1.66562),
        S298 = (0.399676,'cal/(mol*K)','+|-',0.285184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 237,
    label = "Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {4,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 238,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {3,S}
9    Cs u0 {4,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 239,
    label = "Aromatic_pi_S_(CH3_CH3_Meta)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D} {8,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {2,S}
9   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 240,
    label = "Aromatic_pi_S_(CH3_C2H5_Meta)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 241,
    label = "Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    C  u0 {4,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 242,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D} {8,S}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {2,S}
9    Cs u0 {4,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 243,
    label = "Aromatic_pi_S_(CH3_CH3_Sub)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {4,S}
9   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 244,
    label = "Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S} {8,S} {9,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   H  u0 {1,S}
8   C  u0 {4,S} {9,S}
9   C  u0 {4,S} {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
""",
)

entry(
    index = 245,
    label = "Aromatic_pi_S_(CH3_C2H5_Sub)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 246,
    label = "Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S} {10,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {8,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
""",
)

entry(
    index = 247,
    label = "Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S} {11,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {8,S} {10,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
""",
)

entry(
    index = 248,
    label = "Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S} {12,S}
9    C  u0 {4,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {10,S} {12,S}
12   C  u0 {8,S} {11,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
""",
)

entry(
    index = 249,
    label = "Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    C  u0 {4,S} {10,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 250,
    label = "Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cs u0 {3,S} {5,S} {8,S} {9,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {1,S} {5,D}
7    H  u0 {1,S}
8    C  u0 {4,S}
9    Cs u0 {4,S} {10,S} {16,S}
10   Cb u0 {9,S} {11,B} {15,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {13,B} {15,B}
15   Cb u0 {10,B} {14,B}
16   C  u0 {9,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 251,
    label = "cyclopropenyl-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (90.6,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = """DeFrees, D. J.; McIver, R. T., Jr.; Hehre, W. J., "Heats of Formation of Gaseous Free Radicals via Ion Cyclotron Double Resonance Spectroscopy," J. Am. Chem. Soc. 1980, 102, 3334-3338, DOI: 10.1021/ja00530a005 S, Cp copied from C=CCJC=C""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "1,3-cyclopentadiene-allyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
6   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.157,0.892,-0.937,-2.776,-4.931,-3.793,-4.855],'cal/(mol*K)'),
        H298 = (84.912,'kcal/mol'),
        S298 = (-2.047,'cal/(mol*K)'),
    ),
    shortDesc = """Combined experimental and theoretical results of Tranter for 1,2-CPD'yl""",
    longDesc = 
"""
Absolute Enthalpy of formation at 298 K from experiment (1998 Kern and Tranter).
All other  values from theory (2001 Kiefer and Tranter).
""",
)

entry(
    index = 253,
    label = "C=CCJC=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-3.8,-3.7,-4.3,-6.1,-8.1,-11.5],'J/(mol*K)'),
        H298 = (318,'kJ/mol'),
        S298 = (-22,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 254,
    label = "Sec_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (-0.45,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "CCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-3.4,-3.4,-4.2,-6.7,-9.2,-13.9],'J/(mol*K)'),
        H298 = (379.1,'kJ/mol'),
        S298 = (-5.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 256,
    label = "CCJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],'cal/(mol*K)'),
        H298 = (91.9,'kcal/mol'),
        S298 = (-2.37,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "C=OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,1.5,0.9,0,-2.5,-5.1,-10.2],'J/(mol*K)'),
        H298 = (382.7,'kJ/mol'),
        S298 = (-13,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 258,
    label = "Cs_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = 'Tertalkyl',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "CCJ(C)CO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.8,-9.3,-10.3,-11,-12.4,-13.7,-16.1],'J/(mol*K)'),
        H298 = (369.4,'kJ/mol'),
        S298 = (-0.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 260,
    label = "C2CJCOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],'cal/(mol*K)'),
        H298 = (97.2,'kcal/mol'),
        S298 = (7.31,'cal/(mol*K)'),
    ),
    shortDesc = """WIJAYA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "Tertalkyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (96.5,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "bicyclo[1.1.0]butane-tertiary",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2 * Cs u1 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (113.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "bicyclo[2.1.0]pentane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "bicyclo[1.1.1]pentane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (106.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "bicyclo[3.1.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "bicyclo[2.2.0]hexane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "bicyclo[2.1.1]hexane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "bridgehead_norbornyl",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (107.42,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "bicyclo[3.2.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "bicyclo[4.1.0]heptane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "bicyclo[3.1.1]heptane-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {7,S}
7   C  u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (103.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "octahydro-pentalene-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   C  u0 {2,S} {7,S}
6   C  u0 {2,S} {8,S}
7   C  u0 {4,S} {5,S}
8   C  u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (95.7,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "bicyclo[4.2.0]octane-tertiary",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   C  u0 {5,S} {8,S}
8   C  u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "bicyclo[2.2.2]octane-C1",
    group = 
"""
1 * Cs u1 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   C  u0 {2,S} {3,S}
5   C  u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   C  u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (101.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "Benzyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],'cal/(mol*K)'),
        H298 = (83.8,'kcal/mol'),
        S298 = (-5.34,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "Benzyl_T_Fused5",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {6,[S,B,T]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {3,[S,B,T]} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.457289,-1.56269,-2.22771,-2.42903,-2.80968,-3.48772,-4.25286],'cal/(mol*K)','+|-',[0.282803,0.282803,0.282803,0.282803,0.282803,0.282803,0.282803]),
        H298 = (85.4498,'kcal/mol','+|-',1.02262),
        S298 = (4.37066,'cal/(mol*K)','+|-',0.608769),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
CC1C[CH]C2=CC=CC=C21
CCC1C[CH]C2=CC=CC=C21
CCCC1C[CH]C2=CC=CC=C21
""",
)

entry(
    index = 277,
    label = "Benzyl_T_Fused6",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   C  u0 {5,S} {7,[S,D,T,B]}
7   C  u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148032,-0.974235,-1.84864,-2.42284,-3.01207,-3.46526,-4.43708],'cal/(mol*K)','+|-',[0.514226,0.514226,0.514226,0.514226,0.514226,0.514226,0.514226]),
        H298 = (84.72,'kcal/mol','+|-',1.82377),
        S298 = (1.70208,'cal/(mol*K)','+|-',1.17522),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Compounds Include
C[C]1CCCC2=CC=CC=C21
CC[C]1CCCC2=CC=CC=C21
""",
)

entry(
    index = 278,
    label = "Benzyl_T_dihydronaphthalene",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cb u0 {1,S} {5,B}
3   C  u0 {1,S} {7,[S,D,T,B]}
4   C  u0 {1,S}
5   Cb u0 {2,B} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {3,[S,D,T,B]} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.264274,-0.237466,-0.864612,-1.639,-2.84087,-3.59047,-4.6789],'cal/(mol*K)','+|-',[0.546927,0.546927,0.546927,0.546927,0.546927,0.546927,0.546927]),
        H298 = (83.3368,'kcal/mol','+|-',2.01563),
        S298 = (2.12045,'cal/(mol*K)','+|-',0.802466),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 07/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C[C]1CC=CC2=CC=CC=C12
CC[C]1CC=CC2=CC=CC=C12
""",
)

entry(
    index = 279,
    label = "CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.1,-10,-11.8,-12.9,-14.1,-15.1,-16.9],'J/(mol*K)'),
        H298 = (361.8,'kJ/mol'),
        S298 = (3.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 280,
    label = "C=CCJ(C)C=C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.8,-8.2,-8.9,-9.3,-10.1,-11,-12.9],'J/(mol*K)'),
        H298 = (313.4,'kJ/mol'),
        S298 = (0.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 281,
    label = "C=CCJ(C=C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
8   O2d u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.7,-9.3,-8.1,-7.2,-6.8,-7.2,-8.8],'J/(mol*K)'),
        H298 = (287.1,'kJ/mol'),
        S298 = (-27.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 282,
    label = "Allyl_T",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],'cal/(mol*K)'),
        H298 = (83.4,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "Aromatic_pi_T_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cs u0 {1,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {2,D} {6,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 284,
    label = "Aromatic_pi_T_(CH3_CH3_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 285,
    label = "Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cs u0 {1,S} {5,S} {8,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S} {9,S}
9   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 286,
    label = "Aromatic_pi_T_(fused5)_1_3",
    group = 
"""
1 * Cs u1 {2,S} {6,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {1,S} {5,S} {8,S}
7   C  u0 {1,S} {9,S}
8   C  u0 {6,S} {9,S}
9   C  u0 {7,S} {8,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 287,
    label = "Aromatic_pi_T_(fused6)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {6,S} {7,S}
2    Cd u0 {1,S} {3,D}
3    Cd u0 {2,D} {4,S}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {1,S} {5,S} {8,S}
7    C  u0 {1,S} {10,S}
8    C  u0 {6,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {7,S} {9,S}
""",
    thermo = 'Aromatic_pi_S_(fused5)_1_4',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations and group values for radical groups already present in the database, 03/2018, Lawrence Lai

Uncertainty of CBS-QB3 is 2.4kcal/mol, by Somers, K, and Simmie, J, "Benchmarking Compound Methods (CBS-QB3, CBS-APNO, G3, G4, W1BD") against the Active Thermochemical  Tables: Formation Enthalpies of Radicals. 2015.
http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448

Model Species used include:
C1=CC=C2CCCC2[CH]1
CC1CCC2=CC=C[CH]C21
CCC1CCC2=CC=C[CH]C21
CCCC1CCC2=CC=C[CH]C21
C1=CC=C2CCCCC2[CH]1
CC1CCCC2=CC=C[CH]C21
CCC1CCCC2=CC=C[CH]C21
""",
)

entry(
    index = 288,
    label = "Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cs u0 {1,S} {5,S} {8,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {5,D} {7,S}
7    Cd u0 {2,D} {6,S}
8    C  u0 {4,S} {9,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 289,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cs u0 {1,S} {5,S} {8,S}
5    Cd u0 {4,S} {6,D}
6    Cd u0 {5,D} {7,S}
7    Cd u0 {2,D} {6,S}
8    Cs u0 {4,S} {9,S} {15,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
15   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 290,
    label = "Aromatic_pi_T_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {2,D} {6,S}
""",
    thermo = 'Aromatic_pi_S_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_1_3
""",
)

entry(
    index = 291,
    label = "Aromatic_pi_T_(CH3_CH3_Para)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_CH3_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
""",
)

entry(
    index = 292,
    label = "Aromatic_pi_T_(CH3_C2H5_Para)_1_4",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {7,D}
3   C  u0 {1,S}
4   Cd u0 {1,S} {5,D} {8,S}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {2,D} {6,S}
8   C  u0 {4,S} {9,S}
9   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
See Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
""",
)

entry(
    index = 293,
    label = "Aromatic_pi_T_(CH3_Benzyl_Para)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cd u0 {1,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cd u0 {2,D} {6,S}
8    C  u0 {4,S} {9,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
""",
    thermo = 'Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 294,
    label = "Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4",
    group = 
"""
1  * Cs u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {7,D}
3    C  u0 {1,S}
4    Cd u0 {1,S} {5,D} {8,S}
5    Cd u0 {4,D} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cd u0 {2,D} {6,S}
8    Cs u0 {4,S} {9,S} {15,S}
9    Cb u0 {8,S} {10,B} {14,B}
10   Cb u0 {9,B} {11,B}
11   Cb u0 {10,B} {12,B}
12   Cb u0 {11,B} {13,B}
13   Cb u0 {12,B} {14,B}
14   Cb u0 {9,B} {13,B}
15   C  u0 {8,S}
""",
    thermo = 'Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3',
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
""",
)

entry(
    index = 295,
    label = "bicyclo[2.1.0]pent-2-ene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (112.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "bicyclo[2.1.1]hex-2-ene-C1",
    group = 
"""
1 * Cs u1 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C1",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "C=CCJ(C)C=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.2,-10.5,-9.4,-9,-9.1,-9.7,-11.5],'J/(mol*K)'),
        H298 = (335.4,'kJ/mol'),
        S298 = (-17.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 299,
    label = "C=CCJ(C=O)C=C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10,-7.5,-6.1,-5.5,-5.6,-6.4,-8.5],'J/(mol*K)'),
        H298 = (307.4,'kJ/mol'),
        S298 = (-27.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 300,
    label = "Tert_Propargyl",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],'cal/(mol*K)'),
        H298 = (84.5,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "C2CJCO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   R   u0 {2,S}
""",
    thermo = 'C2CJCHO',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "C2CJCHO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D} {6,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],'cal/(mol*K)'),
        H298 = (89.8,'kcal/mol'),
        S298 = (-1.71,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9,3.7,1.6,-0.9,-5.9,-10.3,-17.5],'J/(mol*K)'),
        H298 = (413.3,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 304,
    label = "CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],'cal/(mol*K)'),
        H298 = (96.51,'kcal/mol'),
        S298 = (0.09,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'CsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = 'CsJOCH3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "CsJOCH3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN #""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "CsJOCC",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],'cal/(mol*K)'),
        H298 = (96.83,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "CsJOCC2",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],'cal/(mol*K)'),
        H298 = (96.16,'kcal/mol'),
        S298 = (-0.59,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "CsJOCC3",
    group = 
"""
1   Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 * Cs  u1 {3,S} {7,S} {8,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   H   u0 {2,S}
8   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],'cal/(mol*K)'),
        H298 = (95.75,'kcal/mol'),
        S298 = (0.27,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = 'CsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],'cal/(mol*K)'),
        H298 = (100.88,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],'cal/(mol*K)'),
        H298 = (100.48,'kcal/mol'),
        S298 = (-0.17,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "C=COCJ",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   Cd  u0 {2,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-7.2,-8.9,-10.6,-13.6,-15.9,-19.7],'J/(mol*K)'),
        H298 = (409.4,'kJ/mol'),
        S298 = (13.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 316,
    label = "CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol'),
        S298 = (-1.57,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],'cal/(mol*K)'),
        H298 = (98.91,'kcal/mol'),
        S298 = (-1.52,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],'cal/(mol*K)'),
        H298 = (98.34,'kcal/mol'),
        S298 = (-1.62,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "CCsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.4,-1.5,-3.9,-8.6,-12.5,-18.7],'J/(mol*K)'),
        H298 = (402,'kJ/mol'),
        S298 = (3.9,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 320,
    label = "CCsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'CCsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "C=CCJ(O)C",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S} {6,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.7,-8.4,-10,-11,-12.1,-13.1,-15.5],'J/(mol*K)'),
        H298 = (328.3,'kJ/mol'),
        S298 = (4.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 322,
    label = "CCsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],'cal/(mol*K)'),
        H298 = (95.41,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "CCsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   H       u0 {1,S}
5   [CO,Cd] u0 {2,S}
""",
    thermo = 'CCsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "CCsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],'cal/(mol*K)'),
        H298 = (98.7,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "CCsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],'cal/(mol*K)'),
        H298 = (98.87,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "CCsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "C=CCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-3.9,-3,-3.2,-5.7,-8.6,-13.8],'J/(mol*K)'),
        H298 = (333.9,'kJ/mol'),
        S298 = (-7.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 328,
    label = "OCJC=O",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.3,-5.6,-7.4,-9.8,-11.2,-14],'J/(mol*K)'),
        H298 = (356.6,'kJ/mol'),
        S298 = (0.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 329,
    label = "CCsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],'cal/(mol*K)'),
        H298 = (95.39,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "CCsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "CCsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],'cal/(mol*K)'),
        H298 = (97.19,'kcal/mol'),
        S298 = (0.77,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "CCsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "C2CsJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2,-7.1,-10.7,-13.4,-16.6,-18.5,-21.2],'J/(mol*K)'),
        H298 = (398.4,'kJ/mol'),
        S298 = (14.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 334,
    label = "C2CsJOH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],'cal/(mol*K)'),
        H298 = (94.5,'kcal/mol'),
        S298 = (2.17,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "C2CsJOC",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {2,S}
""",
    thermo = 'C2CsJOCs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "C2CsJOCs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (3.71,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "C2CsJOCds",
    group = 
"""
1 * Cs      u1 {2,S} {3,S} {4,S}
2   O2s     u0 {1,S} {5,S}
3   C       u0 {1,S}
4   C       u0 {1,S}
5   [Cd,CO] u0 {2,S}
""",
    thermo = 'C2CsJOC(O)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "C2CsJOC(O)",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   CO  u0 {2,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (4.77,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "C2CsJOC(O)H",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],'cal/(mol*K)'),
        H298 = (99.97,'kcal/mol'),
        S298 = (4.88,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "C2CsJOC(O)C",
    group = 
"""
1 * Cs  u1 {3,S} {4,S} {5,S}
2   CO  u0 {3,S} {6,D} {7,S}
3   O2s u0 {1,S} {2,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],'cal/(mol*K)'),
        H298 = (100.25,'kcal/mol'),
        S298 = (4.66,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "C2CsJOO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (2.22,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "C2CsJOOH",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],'cal/(mol*K)'),
        H298 = (96.74,'kcal/mol'),
        S298 = (2.37,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "C2CsJOOC",
    group = 
"""
1 * Cs  u1 {2,S} {4,S} {5,S}
2   O2s u0 {1,S} {3,S}
3   O2s u0 {2,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],'cal/(mol*K)'),
        H298 = (96.58,'kcal/mol'),
        S298 = (2.08,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "CsJ-S",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   R  ux {1,S}
4   R  ux {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "CsJ-SsHH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.07,-0.32,-0.73,-1.22,-2.18,-2.99,-4.27],'cal/(mol*K)'),
        H298 = (95.34,'kcal/mol'),
        S298 = (1.18,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "CsJ-CSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "CsJ-CsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.79,-1.36,-1.9,-2.82,-3.53,-4.64],'cal/(mol*K)'),
        H298 = (92.87,'kcal/mol'),
        S298 = (1.91,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "CsJ-CtSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26,-0.02,-0.47,-0.97,-1.95,-2.77,-4.12],'cal/(mol*K)'),
        H298 = (83.48,'kcal/mol'),
        S298 = (-0.16,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "CsJ-CbSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.38,-0.65,-1.01,-1.75,-2.4,-3.57],'cal/(mol*K)'),
        H298 = (84.88,'kcal/mol'),
        S298 = (-0.98,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "CsJ-CdSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21,-2.77,-2.39,-2.24,-2.39,-2.74,-3.56],'cal/(mol*K)'),
        H298 = (81.92,'kcal/mol'),
        S298 = (0.66,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "CsJ-C=SSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75,-2.93,-2.07,-1.54,-1.2,-1.31,-2.01],'cal/(mol*K)'),
        H298 = (71.51,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "CsJ-CCS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "CsJ-CsCsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72,-2.04,-2.88,-3.4,-3.99,-4.36,-4.96],'cal/(mol*K)'),
        H298 = (92.32,'kcal/mol'),
        S298 = (3.87,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "CsJ-CsCtSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.99,-1.64,-2.18,-2.62,-3.3,-3.82,-4.65],'cal/(mol*K)'),
        H298 = (81.17,'kcal/mol'),
        S298 = (3.05,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "CsJ-CsCbSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.26,-2.53,-2.75,-3.12,-3.49,-4.43],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "CsJ-CsCdSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-4.74,-4.81,-4.59,-4.17,-3.99,-4.12],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (2.53,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "CsJ-CsC=SSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86,-3.83,-3.41,-2.93,-2.28,-2.07,-2.36],'cal/(mol*K)'),
        H298 = (69.17,'kcal/mol'),
        S298 = (-1.97,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "CsJ-SS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   R   u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "CsJ-SsSsH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-4,-3.64,-3.53,-3.68,-4,-4.72],'cal/(mol*K)'),
        H298 = (90.16,'kcal/mol'),
        S298 = (1.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "CsJ-CSS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "CsJ-CsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36,-4,-4.17,-4.24,-4.37,-4.55,-5],'cal/(mol*K)'),
        H298 = (89.98,'kcal/mol'),
        S298 = (5.5,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "CsJ-CtSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "CsJ-CbSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "CsJ-CdSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "CsJ-C=SSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "CsJ-SsSsSs",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "CCsJOS",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = 'CCsJOHSH',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "CCsJOHSH",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S} {5,S}
3   S2s u0 {1,S} {6,S}
4   C   u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.21,-2.38,-2.47,-2.55,-2.89,-3.33,-4.54],'cal/(mol*K)'),
        H298 = (92.6,'kcal/mol'),
        S298 = (1.67,'cal/(mol*K)'),
    ),
    shortDesc = """CAC CBS-QB3 1d-hr""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "CsJ-SsOsH",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   S  ux {1,S}
3   O  ux {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95,-2.6,-2.88,-2.9,-2.72,-2.63,-3.06],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (-0.74,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 370,
    label = "OCJO",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1,-8.2,-14.4,-17.5,-19.4,-20.1,-21.5],'J/(mol*K)'),
        H298 = (408.4,'kJ/mol'),
        S298 = (15.1,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 371,
    label = "CsJ-HNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.8532,11.0458,6.19232,1.63176,-4.64424,-8.53536,-15.9829],'J/(mol*K)'),
        H298 = (438.663,'kJ/mol'),
        S298 = (7.12357,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "CsJ-HNN3ds",
    group = 
"""
1 * Cs        u1 {2,S} {3,S} {4,S}
2   N         u0 {1,S}
3   [N3d,N3s] u0 {1,S}
4   H         u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.58597,-5.80395,-8.7662,-11.0768,-14.324,-16.3676,-18.708],'J/(mol*K)'),
        H298 = (393.258,'kJ/mol'),
        S298 = (0.575878,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "CsJ-HN(N3dCd)",
    group = 
"""
1 * Cs       u1 {2,S} {3,S} {4,S}
2   N3d      u0 {1,S} {5,D}
3   N        u0 {1,S}
4   H        u0 {1,S}
5   [Cd,Cdd] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.17364,0.526339,-1.56312,-4.04119,-8.28715,-11.0029,-15.4736],'J/(mol*K)'),
        H298 = (342.422,'kJ/mol'),
        S298 = (-4.66094,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "CsJ-HN(N3dOd)",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   N   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.31137,-4.08151,-5.05929,-6.59864,-9.61356,-12.7552,-18.2312],'J/(mol*K)'),
        H298 = (303.519,'kJ/mol'),
        S298 = (-8.01983,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "CsJ-HN(N3dN5dc)",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N3d  u0 {1,S} {5,D}
3   N    u0 {1,S}
4   H    u0 {1,S}
5   N5dc u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.95318,3.13485,0.33421,-2.701,-7.67123,-10.5415,-15.8149],'J/(mol*K)'),
        H298 = (275.434,'kJ/mol'),
        S298 = (4.69758,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "CsJ-HN5scN5sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5sc u0 {1,S}
3   N5sc u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0538838,-1.876,-4.04855,-6.08546,-9.70524,-12.7382,-17.9892],'J/(mol*K)'),
        H298 = (436.377,'kJ/mol'),
        S298 = (7.19164,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "CsJ-NNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.26669,-1.87614,-5.88538,-8.95583,-13.0988,-15.6997,-18.3991],'J/(mol*K)'),
        H298 = (388.334,'kJ/mol'),
        S298 = (-4.02418,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "CsJ-HNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.29692,-8.29409,-11.2699,-13.4031,-16.5816,-18.4631,-19.9014],'J/(mol*K)'),
        H298 = (371.563,'kJ/mol'),
        S298 = (2.01997,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "CsJ-HON1sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N1sc u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.80826,-12.344,-15.0884,-16.9587,-18.722,-18.5848,-14.5979],'J/(mol*K)'),
        H298 = (273.333,'kJ/mol'),
        S298 = (-3.14275,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "CsJ-NNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.60436,-6.81991,-9.0924,-11.5084,-13.7941,-14.5737,-13.827],'J/(mol*K)'),
        H298 = (311.145,'kJ/mol'),
        S298 = (4.53151,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "CsJ-NOO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   O  u0 {1,S}
3   O  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42994,-4.90751,-5.57809,-6.41818,-8.08512,-9.63419,-13.0091],'J/(mol*K)'),
        H298 = (324.92,'kJ/mol'),
        S298 = (-3.22872,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "CsJ-CNN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.80085,-5.80744,-7.57663,-9.14825,-11.7549,-13.7367,-16.6315],'J/(mol*K)'),
        H298 = (383.839,'kJ/mol'),
        S298 = (-5.21955,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "CsJ-CNO",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   C  u0 {1,S}
3   O  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.889156,-3.17426,-6.57797,-9.40356,-13.6201,-16.3703,-19.6483],'J/(mol*K)'),
        H298 = (390.332,'kJ/mol'),
        S298 = (4.50509,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = 'CCsJN',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "CsJN3s",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.34639,0.0642418,-2.22164,-4.63062,-8.66372,-11.6685,-16.1145],'J/(mol*K)'),
        H298 = (388.92,'kJ/mol'),
        S298 = (-10.2036,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "CsJN5sdtc",
    group = 
"""
1 * Cs                     u1 {2,S} {3,S} {4,S}
2   [N5sc,N5dc,N5ddc,N5tc] u0 {1,S}
3   H                      u0 {1,S}
4   H                      u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.81722,3.24544,2.72474,1.22104,-2.23308,-5.66919,-12.8356],'J/(mol*K)'),
        H298 = (404.243,'kJ/mol'),
        S298 = (-14.4918,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "CsJN5sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5sc u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.491933,-0.720255,-2.86803,-5.09749,-8.94641,-12.0652,-17.2889],'J/(mol*K)'),
        H298 = (432.825,'kJ/mol'),
        S298 = (-2.63962,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "CsJN5dcOdO0sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S} {5,D} {6,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   O2d  u0 {2,D}
6   O0sc u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.05016,0.29288,-2.17568,-4.97896,-10.1671,-14.393,-21.2966],'J/(mol*K)'),
        H298 = (424.73,'kJ/mol'),
        S298 = (-14.8665,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "CsJN5dcN3dO0sc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S} {5,D} {6,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   N3d  u0 {2,D}
6   O0sc u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27482,3.34223,2.42357,0.716726,-3.09483,-6.83265,-14.3794],'J/(mol*K)'),
        H298 = (421.503,'kJ/mol'),
        S298 = (-9.69349,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "CsJN3dCd",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.334539,-0.181647,-0.845982,-1.98298,-4.81941,-7.87964,-14.2395],'J/(mol*K)'),
        H298 = (374.018,'kJ/mol'),
        S298 = (-11.1917,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "CsJN3dCdd",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.55707,4.38485,1.99807,-0.696803,-5.27072,-8.57746,-14.1022],'J/(mol*K)'),
        H298 = (389.255,'kJ/mol'),
        S298 = (-9.12797,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "CsJN3dN5dc",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   N3d  u0 {1,S} {5,D}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   N5dc u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.315332,0.568578,-0.652395,-2.70945,-6.57117,-9.32981,-14.8325],'J/(mol*K)'),
        H298 = (331.765,'kJ/mol'),
        S298 = (-9.5881,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "CCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-1.4,-1.9,-2.8,-3.4,-4.5],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (2.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "CdCsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.49236,-8.5813,-8.63032,-9.10002,-10.0385,-11.4238,-14.1214],'J/(mol*K)'),
        H298 = (329.078,'kJ/mol'),
        S298 = (-10.2951,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "C2CsJN",
    group = 
"""
1 * Cs u1 {2,S} {3,S} {4,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4665,-7.70578,-11.17,-13.75,-16.6445,-18.2536,-20.0442],'J/(mol*K)'),
        H298 = (392.461,'kJ/mol'),
        S298 = (-9.03706,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "CdsJ",
    group = 
"""
1 * [Cd,CO] u1
""",
    thermo = 'Cds_P',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "CdBr1sCdd",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   Cdd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.758104,-1.6682,-2.31233,-2.8316,-3.65583,-4.26359,-5.16596],'cal/(mol*K)','+|-',[0.380332,0.389196,0.364541,0.340311,0.300103,0.262674,0.196427]),
        H298 = (95.2979,'kcal/mol','+|-',0.592315),
        S298 = (-0.120787,'cal/(mol*K)','+|-',0.891343),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         7
""",
)

entry(
    index = 398,
    label = "CdCddCl1s",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   Cdd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.154618,-0.976143,-1.62147,-2.18484,-3.09001,-3.72652,-4.59724],'cal/(mol*K)','+|-',[0.318208,0.325625,0.304997,0.284724,0.251084,0.219769,0.164343]),
        H298 = (95.178,'kcal/mol','+|-',0.495566),
        S298 = (2.18226,'cal/(mol*K)','+|-',0.745751),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         7
CHOClBr_G4 |         3
""",
)

entry(
    index = 399,
    label = "CdCddF1s",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   Cdd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.423163,-1.07399,-1.67409,-2.19205,-2.99365,-3.54873,-4.3315],'cal/(mol*K)','+|-',[0.237179,0.242706,0.227332,0.212221,0.187147,0.163806,0.122494]),
        H298 = (103.207,'kcal/mol','+|-',0.369373),
        S298 = (1.33428,'cal/(mol*K)','+|-',0.55585),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         9
CHOFCl_G4   |         6
CHOFClBr_G4 |         1
CHOFBr_G4   |         2
""",
)

entry(
    index = 400,
    label = "CdBr1sCd",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   Cd   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.275344,-0.999163,-1.66376,-2.24084,-3.12829,-3.74905,-4.66764],'cal/(mol*K)','+|-',[0.131004,0.134058,0.125565,0.117219,0.10337,0.0904775,0.0676588]),
        H298 = (108.469,'kcal/mol','+|-',0.204021),
        S298 = (1.5399,'cal/(mol*K)','+|-',0.307021),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         59
""",
)

entry(
    index = 401,
    label = "CdCdCl1s",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   Cd   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.349585,-1.10196,-1.74578,-2.29373,-3.1376,-3.73318,-4.61343],'cal/(mol*K)','+|-',[0.0733893,0.0750998,0.0703424,0.0656668,0.0579082,0.050686,0.0379028]),
        H298 = (108.733,'kcal/mol','+|-',0.114294),
        S298 = (1.71675,'cal/(mol*K)','+|-',0.171995),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         102
CHOClBr_G4 |         86
""",
)

entry(
    index = 402,
    label = "CdCdF1s",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   Cd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.395973,-1.13754,-1.77838,-2.31506,-3.14346,-3.73729,-4.63544],'cal/(mol*K)','+|-',[0.053787,0.0550406,0.051554,0.0481272,0.042441,0.0371478,0.027779]),
        H298 = (113.448,'kcal/mol','+|-',0.0837659),
        S298 = (1.69347,'cal/(mol*K)','+|-',0.126055),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         97
CHOFCl_G4   |         79
CHOFClBr_G4 |         36
CHOFBr_G4   |         138
""",
)

entry(
    index = 403,
    label = "CdsJO",
    group = 
"""
1 * CO  u1 {2,D}
2   O2d u0 {1,D}
""",
    thermo = 'CCJ=O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "COBr1sO2d",
    group = 
"""
1 * CO   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   O2d  u0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "COCl1sO2d",
    group = 
"""
1 * CO   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   O2d  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.174031,-0.863816,-1.52171,-2.09023,-2.99954,-3.66182,-4.61006],'cal/(mol*K)','+|-',[1.00626,1.02972,0.964485,0.900377,0.793997,0.69497,0.519696]),
        H298 = (90.8783,'kcal/mol','+|-',1.56712),
        S298 = (1.16039,'cal/(mol*K)','+|-',2.35827),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         1
""",
)

entry(
    index = 406,
    label = "COF1sO2d",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.402717,-0.899898,-1.45939,-2.01242,-2.89452,-3.54367,-4.54736],'cal/(mol*K)','+|-',[1.00626,1.02972,0.964485,0.900377,0.793997,0.69497,0.519696]),
        H298 = (100.836,'kcal/mol','+|-',1.56712),
        S298 = (0.552887,'cal/(mol*K)','+|-',2.35827),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         1
""",
)

entry(
    index = 407,
    label = "COJ-NOd",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   N   u0 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499049,-2.566,-5.4926,-8.03919,-12.3239,-15.6108,-20.2366],'J/(mol*K)'),
        H298 = (352.267,'kJ/mol'),
        S298 = (5.58481,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "HCdsJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],'cal/(mol*K)'),
        H298 = (88.45,'kcal/mol'),
        S298 = (-0.01,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "CCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
""",
    thermo = 'CsCJ=O',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "CC(C)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1,-5.8,-7.9,-9.9,-13.5,-16.2,-20.3],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 411,
    label = "CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7,-5,-7.4,-9.6,-13.1,-15.6,-19.9],'J/(mol*K)'),
        H298 = (373.3,'kJ/mol'),
        S298 = (7.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 412,
    label = "CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7,-4,-5.4,-7.2,-10.9,-13.9,-18.6],'J/(mol*K)'),
        H298 = (375.2,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 413,
    label = "C=CC(C)(C=O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {1,S}
6   C   u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.5,2.6,-2.4,-6.5,-12,-15.3,-19.7],'J/(mol*K)'),
        H298 = (373.6,'kJ/mol'),
        S298 = (1.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 414,
    label = "C=CC(C)2CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-4.2,-7,-9.3,-12.8,-15.4,-19.4],'J/(mol*K)'),
        H298 = (371.9,'kJ/mol'),
        S298 = (10.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 415,
    label = "CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {6,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.9,-2.6,-5.6,-8.1,-12,-14.9,-19.6],'J/(mol*K)'),
        H298 = (374.9,'kJ/mol'),
        S298 = (6.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 416,
    label = "C=CC(C)(O)CJ=O",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u1 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1,-4.5,-7.4,-9.7,-12.7,-15.1,-19.5],'J/(mol*K)'),
        H298 = (375.3,'kJ/mol'),
        S298 = (8.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 417,
    label = "CCCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {4,D}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7,-3.9,-7,-9.9,-14.5,-17.5,-21.4],'J/(mol*K)'),
        H298 = (378,'kJ/mol'),
        S298 = (8.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 418,
    label = "C=OCCJ=O",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * CO  u1 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,1.4,-2.8,-6.4,-12,-15.8,-20.4],'J/(mol*K)'),
        H298 = (379.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 419,
    label = "C=OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.2,-4.6,-4.4,-4.5,-4.9,-5.7,-7.8],'J/(mol*K)'),
        H298 = (330.2,'kJ/mol'),
        S298 = (-19.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 420,
    label = "C=C(C)CJ=O",
    group = 
"""
1   Cd  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-3.8,-6.4,-8.8,-12.5,-15.3,-19.5],'J/(mol*K)'),
        H298 = (381.7,'kJ/mol'),
        S298 = (6.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 421,
    label = "CsCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.12,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "C=CCJ=O",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   Cd  u0 {1,S} {4,D}
3   O2d u0 {1,D}
4   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,2.5,-1.1,-4.5,-9.9,-13.7,-18.9],'J/(mol*K)'),
        H298 = (379.9,'kJ/mol'),
        S298 = (7.2,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 423,
    label = "OC=OCJ=O",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * CO  u1 {1,S} {5,D}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3,-4.7,-7,-9.5,-14,-17.2,-21.1],'J/(mol*K)'),
        H298 = (376.2,'kJ/mol'),
        S298 = (4.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 424,
    label = "(O)CJO",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = '(O)CJOC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "(O)CJOH",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],'cal/(mol*K)'),
        H298 = (100.75,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN #""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "(O)CJOC",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   O2s u0 {1,S} {4,S}
3   O2d u0 {1,D}
4   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,-0.2,-3.5,-6.5,-10.9,-13.6,-17],'J/(mol*K)'),
        H298 = (415.2,'kJ/mol'),
        S298 = (-4.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 427,
    label = "(O)CJOCH3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "(O)CJOCC",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],'cal/(mol*K)'),
        H298 = (99.49,'kcal/mol'),
        S298 = (0.55,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "(O)CJOCC2",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.82,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "(O)CJOCC3",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   O2s u0 {1,S} {3,S}
3 * CO  u1 {2,S} {7,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {1,S}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],'cal/(mol*K)'),
        H298 = (97.98,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "SCJ=O",
    group = 
"""
1 * CO  u1 {2,D} {3,S}
2   O2d u0 {1,D}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.3,-0.86,-1.5,-2.06,-2.99,-3.68,-4.7],'cal/(mol*K)'),
        H298 = (86.68,'kcal/mol'),
        S298 = (-1.02,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 432,
    label = "Cds_P",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],'cal/(mol*K)'),
        H298 = (111.2,'kcal/mol'),
        S298 = (1.39,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "C=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.29,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "N=C=CJ",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   Cdd u0 {1,D} {4,D}
3   H   u0 {1,S}
4   N   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92302,-3.87776,-5.86459,-7.91273,-11.031,-13.2669,-16.8954],'J/(mol*K)'),
        H298 = (369.234,'kJ/mol'),
        S298 = (-5.93117,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "Cds_S",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "C=CJC=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   CO  u0 {1,S} {4,D}
3   C   u0 {1,D}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.4,-2.2,-4.8,-7.2,-11.6,-15.5,-22],'J/(mol*K)'),
        H298 = (462.3,'kJ/mol'),
        S298 = (9.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 437,
    label = "C=CJC=C",
    group = 
"""
1 * Cd      u1 {2,D} {3,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],'cal/(mol*K)'),
        H298 = (99.8,'kcal/mol'),
        S298 = (0.71,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "cyclobutadiene-C1",
    group = 
"""
1 * Cd u1 {2,D} {4,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (104.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "bicyclo[2.2.0]hexa-1(4),2,5-triene-C2",
    group = 
"""
1   Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (102.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "1,3-cyclopentadiene-vinyl-2",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4 * Cd u1 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.2,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "cyclopropenyl-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Fattahi, A.; McCarthy, R. E.; Ahmad, M. R.; Kass, S. R., "Why Does Cyclopropene Have the Acidity of an Acetylene but the Bond Energy of Methane?," J. Am. Chem. Soc. 2003, 125, 11746-11750, DOI: 10.1021/ja035725s. S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "cyclobutene-vinyl",
    group = 
"""
1   C  u0 {2,S} {4,S}
2   C  u0 {1,S} {3,S}
3 * Cd u1 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (112.5,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "bicyclo[2.1.0]pent-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   C  u0 {1,S} {2,S}
4 * Cd u1 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109.8,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "bicyclo[2.2.0]hexa-2,5-diene-C2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cd u1 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (111.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "cyclopentene-vinyl",
    group = 
"""
1   C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   C  u0 {1,S} {4,S}
4 * Cd u1 {3,S} {5,D}
5   Cd u0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (113.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "bicyclo[2.1.1]hex-2-ene-C2",
    group = 
"""
1   Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   C  u0 {1,S} {2,S}
4   C  u0 {1,S} {2,S}
5 * Cd u1 {2,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (115.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "1,3-cyclopentadiene-vinyl-1",
    group = 
"""
1   C  u0 {2,S} {3,S}
2 * Cd u1 {1,S} {4,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {2,D} {5,S}
5   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = """Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "CCCJ=C=O",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   C   u0 {1,S} {4,S}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,S}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6,-3,-4.9,-6.5,-9.4,-11.6,-15.1],'J/(mol*K)'),
        H298 = (420.2,'kJ/mol'),
        S298 = (-2.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 450,
    label = "CC(C)CJ=C=O",
    group = 
"""
1   Cs  u0 {2,S} {4,S} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.8,-3.6,-6,-7.8,-10.6,-12.6,-15.8],'J/(mol*K)'),
        H298 = (424,'kJ/mol'),
        S298 = (1.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 451,
    label = "C=C(C)CJ=C=O",
    group = 
"""
1   Cd  u0 {2,S} {4,D} {5,S}
2 * Cd  u1 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   C   u0 {1,D}
5   C   u0 {1,S}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.5,-13.7,-14.6,-15,-15.7,-16.3,-17.8],'J/(mol*K)'),
        H298 = (404,'kJ/mol'),
        S298 = (5.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 452,
    label = "OC=CJCb",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D} {4,S}
3   Cb  u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.047,0.607,0.374,-0.3,-1.28,-1.972,-3.196],'cal/(mol*K)'),
        H298 = (123.797,'kcal/mol'),
        S298 = (2.661,'cal/(mol*K)'),
    ),
    shortDesc = """Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations""",
    longDesc = 
"""
Fit to CCSD(T)-F12/cc-pVDZ-F12//M06/vtz calculations for OC=[C]c1ccccc1
""",
)

entry(
    index = 453,
    label = "N=C=CJC",
    group = 
"""
1 * Cd u1 {2,D} {3,S}
2   C  u0 {1,D} {4,D}
3   C  u0 {1,S}
4   N  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07662,-4.81991,-7.34354,-9.45507,-12.8991,-15.5773,-19.5204],'J/(mol*K)'),
        H298 = (345.84,'kJ/mol'),
        S298 = (0.774208,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "S2s-CJ=C",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   S2s u0 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.16,-0.48,-1.16,-1.76,-2.68,-3.35,-4.45],'cal/(mol*K)'),
        H298 = (104.73,'kcal/mol'),
        S298 = (0.37,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "C=CJO",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-11.8,-15.2,-17.2,-19.2,-20.3,-22],'J/(mol*K)'),
        H298 = (457.4,'kJ/mol'),
        S298 = (26.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 456,
    label = "CdJ-NN",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   N  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.97657,-2.2041,-5.32888,-7.99133,-12.3333,-15.391,-19.6103],'J/(mol*K)'),
        H298 = (404.968,'kJ/mol'),
        S298 = (8.19458,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "CdJ-CdN",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   N  u0 {1,S}
3   C  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18369,-4.23173,-7.03311,-9.35183,-12.8111,-15.2187,-18.7271],'J/(mol*K)'),
        H298 = (445.085,'kJ/mol'),
        S298 = (5.80115,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "CdJ-CddN",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   N   u0 {1,S}
3   Cdd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3921,-2.08105,-5.04651,-7.48487,-11.2668,-13.9403,-17.7653],'J/(mol*K)'),
        H298 = (371.87,'kJ/mol'),
        S298 = (2.60652,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "CdJ-NdO",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   O  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.33945,-1.92324,-6.02047,-9.57875,-15.2601,-19.0789,-23.7518],'J/(mol*K)'),
        H298 = (437.007,'kJ/mol'),
        S298 = (7.57533,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "CdJ-NdC",
    group = 
"""
1 * Cd u1 {2,S} {3,D}
2   C  u0 {1,S}
3   N  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00763889,-2.36896,-5.21801,-7.8464,-11.991,-15.0452,-19.5882],'J/(mol*K)'),
        H298 = (431.362,'kJ/mol'),
        S298 = (4.60475,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "CdJ-HN3d",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.535181,-3.60589,-6.39413,-8.86095,-12.7727,-15.5717,-19.8329],'J/(mol*K)'),
        H298 = (415.298,'kJ/mol'),
        S298 = (5.57767,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "CdJ-H(N3dOs)",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   N3d u0 {1,D} {4,S}
3   H   u0 {1,S}
4   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.72438,-0.600728,-4.42251,-7.70232,-13.0613,-16.7127,-21.0715],'J/(mol*K)'),
        H298 = (440.68,'kJ/mol'),
        S298 = (7.40719,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "CdJ-H(N3dCO)",
    group = 
"""
1   N3d u0 {2,D} {3,S}
2 * Cd  u1 {1,D} {4,S}
3   CO  u0 {1,S} {5,D}
4   H   u0 {2,S}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19479,-3.60166,-4.82249,-6.06327,-8.74387,-11.0941,-15.1265],'J/(mol*K)'),
        H298 = (411.286,'kJ/mol'),
        S298 = (-2.27887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "CdJ-H(N3dN3d)",
    group = 
"""
1 * Cd  u1 {2,D} {3,S}
2   N3d u0 {1,D} {4,S}
3   H   u0 {1,S}
4   N3d u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.175838,-2.38908,-4.71217,-6.73125,-10.4295,-13.5563,-18.2391],'J/(mol*K)'),
        H298 = (426.882,'kJ/mol'),
        S298 = (5.53135,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "CdJ-H(N3dCd)",
    group = 
"""
1 * Cd       u1 {2,D} {3,S}
2   N3d      u0 {1,D} {4,S}
3   H        u0 {1,S}
4   [Cd,Cdd] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.23929,-2.28161,-6.55411,-9.87574,-14.8878,-18.2186,-21.9295],'J/(mol*K)'),
        H298 = (422.544,'kJ/mol'),
        S298 = (13.1379,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "CdJ-HN5dc",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   H    u0 {1,S}
3   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.58018,-0.431227,-3.62097,-6.67779,-11.585,-15.0896,-19.8118],'J/(mol*K)'),
        H298 = (490.037,'kJ/mol'),
        S298 = (7.65582,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "CtJ",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T}
""",
    thermo = 'Acetyl',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "Acetyl",
    group = 
"""
1   Ct u0 {2,T} {3,S}
2 * Ct u1 {1,T}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],'cal/(mol*K)'),
        H298 = (132.7,'kcal/mol'),
        S298 = (2.11,'cal/(mol*K)'),
    ),
    shortDesc = """LAY et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "CbJ",
    group = 
"""
1 * Cb u1 {2,B} {3,B}
2   C  u0 {1,B}
3   C  u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],'cal/(mol*K)'),
        H298 = (113,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from TSANG, S and Cp from THERM""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "C=SJ",
    group = 
"""
1 * CS  u1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = 'C=SJ-H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "C=SJ-S2s",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   S2s u0 p2 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "C=SJ-H",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   H   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.88,-1.47,-1.99,-2.85,-3.49,-4.52],'cal/(mol*K)'),
        H298 = (92.39,'kcal/mol'),
        S298 = (-0.14,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "C=SJ-C",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   C   u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "C=SJ-Cd",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cd  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21,-1.76,-2.24,-2.65,-3.3,-3.81,-4.67],'cal/(mol*K)'),
        H298 = (77.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "C=SJ-Cs",
    group = 
"""
1 * CS  u1 {2,S} {3,D}
2   Cs  u0 {1,S}
3   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.8,-2.25,-2.63,-3.24,-3.74,-4.64],'cal/(mol*K)'),
        H298 = (91.94,'kcal/mol'),
        S298 = (0.65,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "OJ",
    group = 
"""
1 * O u1
""",
    thermo = 'COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "HOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],'cal/(mol*K)'),
        H298 = (119.22,'kcal/mol'),
        S298 = (-2.6,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from NIST values for H2O, OH and H""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   C   ux {1,S}
""",
    thermo = 'CsOJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "CCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.1,-12.2,-14.4,-15.1,-14.7,-14.5,-15.6],'J/(mol*K)'),
        H298 = (442.9,'kJ/mol'),
        S298 = (3.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 480,
    label = "C=OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-9.3,-11.5,-13.2,-15,-16,-17.5],'J/(mol*K)'),
        H298 = (461,'kJ/mol'),
        S298 = (2.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 481,
    label = "C=CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4 * O2s u1 {1,S}
5   C   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-11.3,-14.6,-16.2,-17.2,-17.4,-18.4],'J/(mol*K)'),
        H298 = (462.1,'kJ/mol'),
        S298 = (10.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 482,
    label = "CC(C)(C=O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.6,-13.9,-16.3,-17.5,-18.4,-18.8,-19.1],'J/(mol*K)'),
        H298 = (459.1,'kJ/mol'),
        S298 = (16.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 483,
    label = "C=OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3 * O2s u1 {1,S}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1,-6.8,-10.1,-13,-17.5,-20.9,-25.9],'J/(mol*K)'),
        H298 = (479.5,'kJ/mol'),
        S298 = (16,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 484,
    label = "CC(C)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.3,-6.3,-7.3,-8.3,-9.8,-11.2,-14.2],'J/(mol*K)'),
        H298 = (447.6,'kJ/mol'),
        S298 = (-6.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 485,
    label = "CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.2,-7.9,-9,-9.9,-10.7,-11.7,-14.6],'J/(mol*K)'),
        H298 = (446.1,'kJ/mol'),
        S298 = (-4.6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 486,
    label = "C=CC(C)2OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-12.1,-12.9,-12.9,-12.6,-12.9,-14.8],'J/(mol*K)'),
        H298 = (445.9,'kJ/mol'),
        S298 = (2.7,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 487,
    label = "CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.8,-18.8,-22.1,-22.3,-19.5,-17.2,-16],'J/(mol*K)'),
        H298 = (449,'kJ/mol'),
        S298 = (8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 488,
    label = "C=CC(C)(O)OJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3 * O2s u1 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.2,-12.5,-16.7,-19.1,-20.1,-19.4,-18.2],'J/(mol*K)'),
        H298 = (450.7,'kJ/mol'),
        S298 = (8.5,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 489,
    label = "C=C(C)OJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D} {4,S}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.2,-13.1,-15.6,-17,-17.7,-17.6,-17.6],'J/(mol*K)'),
        H298 = (354.8,'kJ/mol'),
        S298 = (7.4,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 490,
    label = "CdsOJ",
    group = 
"""
1 * O2s     u1 {2,S}
2   [Cd,CO] u0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "RC=COJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],'cal/(mol*K)'),
        H298 = (88,'kcal/mol'),
        S298 = (-1.11,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "C=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.1,-13.5,-14.6,-14.6,-14.3,-14.5,-16],'J/(mol*K)'),
        H298 = (358.1,'kJ/mol'),
        S298 = (3.3,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 493,
    label = "N=COJ",
    group = 
"""
1   Cd  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata=([300,400,500,600,800,1000,1500],'K'), 
        Cpdata=([5.28217,1.42099,-3.86345,-8.97042,-15.9178,-20.3522,-25.06],'J/(mol*K)'), 
        H298=(428.303,'kJ/mol'),
        S298=(12.3017,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Derived from OCDN/[NH]CDO in CHON_G4 thermolibrary
""",
)

entry(
    index = 4930000,
    label = "O0scN5dc=COJ",
    group = 
"""
1   Cd   u0 {2,S} {3,D}
2 * O2s  u1 {1,S}
3   N5dc u0 {1,D} {4,S}
4   O0sc u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.58496,-8.79662,-8.0527,-8.55566,-10.0922,-11.8503,-16.2634],'J/(mol*K)'),
        H298 = (158.992,'kJ/mol'),
        S298 = (-7.51805,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)


entry(
    index = 494,
    label = "OJC=O",
    group = 
"""
1   CO  u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "OC=OOJ",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
4   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.5,-13.1,-16.3,-18.3,-20.4,-21.2,-21.4],'J/(mol*K)'),
        H298 = (460.9,'kJ/mol'),
        S298 = (6,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 496,
    label = "OCOJ",
    group = 
"""
1   C   u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.9,-17.5,-19.8,-19.3,-16.2,-14.3,-14.3],'J/(mol*K)'),
        H298 = (444.4,'kJ/mol'),
        S298 = (0.8,'J/(mol*K)'),
    ),
    shortDesc = """\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 497,
    label = "SCOJ",
    group = 
"""
1   C   ux {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.09,-4.17,-4.38,-4.16,-3.24,-2.43,-1.96],'cal/(mol*K)'),
        H298 = (104.33,'kcal/mol'),
        S298 = (1.24,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 498,
    label = "CsOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],'cal/(mol*K)'),
        H298 = (104.06,'kcal/mol'),
        S298 = (-1.46,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI(ROJ)""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "H3COJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],'cal/(mol*K)'),
        H298 = (104.27,'kcal/mol'),
        S298 = (0.51,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "CbOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "OOJ",
    group = 
"""
1 * O2s u1 {2,S}
2   O2s u0 {1,S}
""",
    thermo = 'ROOJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "ROOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   R!H u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "C(=O)OOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (98.33,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "C3COOJ",
    group = 
"""
1   Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S} {6,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6 * O2s u1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (85.3,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = """CHEN & BOZZELLI""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "SOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   S   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39,-2.62,-2.95,-3.22,-3.66,-3.98,-4.52],'cal/(mol*K)'),
        H298 = (91.79,'kcal/mol'),
        S298 = (1.36,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 506,
    label = "HOOJ",
    group = 
"""
1   O2s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],'cal/(mol*K)'),
        H298 = (85.13,'kcal/mol'),
        S298 = (-0.92,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "SOJ",
    group = 
"""
1 * O u1 p2 c0 {2,S}
2   S ux c0 {1,S}
""",
    thermo = 'O2sJ-S2s',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 508,
    label = "O2sJ-S2s",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.53,-0.81,-0.99,-1.17,-1.56,-1.88,-2.49],'cal/(mol*K)'),
        H298 = (79.78,'kcal/mol'),
        S298 = (1.28,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 509,
    label = "O2sJ-S4d",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S}
""",
    thermo = 'O2sJ-(S4d-OdO)',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value of 52.103 kcal/mol, 4/2017, Ryan Gillis
""",
)

entry(
    index = 510,
    label = "O2sJ-(S4d-OdO)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   O2d u0 p2 c0 {2,D}
4   O   u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.07,-0.61,-0.93,-1.55,-2,-2.49],'cal/(mol*K)'),
        H298 = (28.13,'kcal/mol'),
        S298 = (2.64,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 511,
    label = "O2sJ-(S4d-OdC)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   O   u0 p2 c0 {2,D}
4   C   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.33,-2.94,-3.19,-3.38,-3.72,-4.01,-4.59],'cal/(mol*K)'),
        H298 = (78.16,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 512,
    label = "O2sJ-(S4d-OdH)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   O   u0 p2 c0 {2,D}
4   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69,-3.3,-3.74,-4.07,-4.4,-4.54,-4.927],'cal/(mol*K)'),
        H298 = (79.582,'kcal/mol'),
        S298 = (-1.49,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 513,
    label = "O2sJ-(S4d-CdC)",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S4d u0 p1 c0 {1,S} {3,D} {4,S}
3   C   u0 p0 c0 {2,D}
4   C   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-1.86,-2.28,-2.63,-3.2,-3.64,-4.39],'cal/(mol*K)'),
        H298 = (74.659,'kcal/mol'),
        S298 = (0.698,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 514,
    label = "O2sJ-S6d",
    group = 
"""
1 * O2s u1 p2 c0 {2,S}
2   S6d u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-2.09,-2.45,-2.77,-3.3,-3.71,-4.41],'cal/(mol*K)'),
        H298 = (106.21,'kcal/mol'),
        S298 = (-1.07,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 515,
    label = "O2sJ-N",
    group = 
"""
1 * O2s u1 {2,S}
2   N   u0 {1,S}
""",
    thermo = 'O2sJ-N3s',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "O2sJ-N3s",
    group = 
"""
1 * O2s u1 {2,S}
2   N3s u0 {1,S}
""",
    thermo = 'O2sJ-N3sC',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "O2sJ-N3sC",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95666,-8.30392,-10.4418,-11.9018,-14.2655,-16.1736,-18.5966],'J/(mol*K)'),
        H298 = (327.882,'kJ/mol'),
        S298 = (3.22862,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "O2sJ-N3sCO",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3 * O2s u1 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.80695,-9.17585,-11.1673,-12.1719,-13.6433,-14.6347,-16.2533],'J/(mol*K)'),
        H298 = (317.059,'kJ/mol'),
        S298 = (3.29589,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "O2sJ-N3sO2s",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * O2s u1 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.49247,-14.5591,-18.7597,-21.1308,-24.037,-25.4752,-25.7812],'J/(mol*K)'),
        H298 = (337.881,'kJ/mol'),
        S298 = (3.72329,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "O2sJ-N3s(N5sdcO0sc)",
    group = 
"""
1   N3s         u0 {2,S} {3,S}
2   [N5sc,N5dc] u0 {1,S} {4,S}
3 * O2s         u1 {1,S}
4   O0sc        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.50052,-2.35159,-6.76321,-10.6251,-17.0766,-21.9786,-28.6277],'J/(mol*K)'),
        H298 = (340.144,'kJ/mol'),
        S298 = (17.5768,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "O2sJ-N5sdtc",
    group = 
"""
1 * O2s                    u1 {2,S}
2   [N5sc,N5dc,N5ddc,N5tc] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.452,-13.7444,-13.9339,-14.0699,-14.6564,-15.3839,-17.2753],'J/(mol*K)'),
        H298 = (431.96,'kJ/mol'),
        S298 = (-8.08566,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "O2sJ-N5dcOd",
    group = 
"""
1   [N5dc,N5ddc] u0 {2,S} {3,D}
2 * O2s          u1 {1,S}
3   O2d          u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39039,-6.26822,-9.33998,-11.4358,-14.5602,-16.8834,-20.3064],'J/(mol*K)'),
        H298 = (400.951,'kJ/mol'),
        S298 = (16.5987,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "O2sJ-N5dcOdO0sc",
    group = 
"""
1   N5dc u0 {2,S} {3,D} {4,S}
2 * O2s  u1 {1,S}
3   O2d  u0 {1,D}
4   O0sc u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.87864,-2.55224,-5.6484,-7.7404,-10.9202,-13.2633,-16.6105],'J/(mol*K)'),
        H298 = (431.801,'kJ/mol'),
        S298 = (-4.97896,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "O2sJ-N1sc",
    group = 
"""
1 * O2s  u1 {2,S}
2   N1sc u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.37293,-7.06222,-9.51612,-11.2729,-13.4699,-14.9722,-17.077],'J/(mol*K)'),
        H298 = (347.821,'kJ/mol'),
        S298 = (2.24576,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "O2sJ-N3dN3d",
    group = 
"""
1   N3d u0 {2,S} {3,D}
2 * O2s u1 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.29692,-10.2926,-12.6566,-14.1838,-16.3385,-17.5728,-18.6188],'J/(mol*K)'),
        H298 = (664.976,'kJ/mol'),
        S298 = (5.17262,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "O2sJ-N3dCd",
    group = 
"""
1   N3d      u0 {2,S} {3,D}
2 * O2s      u1 {1,S}
3   [Cd,Cdd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.28771,-10.3803,-11.9598,-13.1984,-15.0803,-16.3293,-16.2292],'J/(mol*K)'),
        H298 = (355.56,'kJ/mol'),
        S298 = (-8.0332,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "SiJ",
    group = 
"""
1 * Si u1
""",
    thermo = 'CJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "SJ",
    group = 
"""
1 * S u1
""",
    thermo = 'S2J',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "S2J",
    group = 
"""
1 * S2s u1 p2
""",
    thermo = 'S2J-C',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 530,
    label = "S2J-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.52,-1.84,-2.17,-2.73,-3.2,-3.95],'cal/(mol*K)'),
        H298 = (91.82,'kcal/mol'),
        S298 = (-4.62,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "S2J-C",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   C   u0 {1,S}
""",
    thermo = 'S2J-Cs',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "S2J-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S}
""",
    thermo = 'S2sJ-(CsHHH)',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 533,
    label = "S2sJ-(CsHHH)",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   H   u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35,-1.58,-1.87,-2.16,-2.66,-3.11,-3.95],'cal/(mol*K)'),
        H298 = (87.08,'kcal/mol'),
        S298 = (-3.45,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 534,
    label = "S2J-(Cs-Cb)",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0 {1,S} {3,S}
3   Cb  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.29,-3.84,-4.16,-4.58,-5.31,-5.9,-6.84],'cal/(mol*K)'),
        H298 = (86.83,'kcal/mol'),
        S298 = (-4.81,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 3/2018, Ryan Gillis
""",
)

entry(
    index = 535,
    label = "S2J-Ct",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18,-2.05,-2.66,-3.12,-3.76,-4.24,-4.99],'cal/(mol*K)'),
        H298 = (77.56,'kcal/mol'),
        S298 = (-4.6,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "S2J-Cb",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cb  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92,-2.1,-2.3,-2.51,-2.93,-3.32,-3.96],'cal/(mol*K)'),
        H298 = (81.36,'kcal/mol'),
        S298 = (-3.66,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "S2J-Cd",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cd  u0 {1,S} {3,D}
3   C   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29,-2.56,-2.72,-2.87,-3.19,-3.52,-4.13],'cal/(mol*K)'),
        H298 = (79.29,'kcal/mol'),
        S298 = (-1.79,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "S2J-C=S",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CS  u0 {1,S} {3,D}
3   S2d u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93,-3.56,-3.88,-4.08,-4.41,-4.74,-5.25],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (-0.7,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "S2J-CO",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CO  u0 {1,S} {3,D}
3   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-2.82,-3.17,-3.44,-3.89,-4.29,-4.95],'cal/(mol*K)'),
        H298 = (89.6,'kcal/mol'),
        S298 = (-0.42,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 CAC""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "S2J-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S}
""",
    thermo = 'S2J-S2s-H',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "S2J-S2s-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93,-2.7,-3.26,-3.67,-4.24,-4.59,-5],'cal/(mol*K)'),
        H298 = (73.97,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "S2J-S2s-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   C   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95,-3.43,-3.78,-4.06,-4.47,-4.74,-5.03],'cal/(mol*K)'),
        H298 = (71.05,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "S2J-S2s-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S} {3,S}
3   S2s u0 p2 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63,-4.32,-4.84,-5.26,-5.82,-6.07,-5.99],'cal/(mol*K)'),
        H298 = (72.74,'kcal/mol'),
        S298 = (0.6,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "S2sJ-O",
    group = 
"""
1 * S2s u1 p2 c0 {2,S}
2   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.15904,-4.00975,-4.36187,-4.91092,-5.32059,-5.53025,-5.75797],'cal/(mol*K)'),
        H298 = (108.577,'kcal/mol'),
        S298 = (-7.47722,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 545,
    label = "S4sJ",
    group = 
"""
1 * S4s u1 p1
""",
    thermo = 'S4sJ-CCC',
    shortDesc = """Sulfur Oxygen Extension""",
    longDesc = 
"""
"
""",
)

entry(
    index = 546,
    label = "S4sJ-CCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.055,-3.801,-4.696,-5.408,-6.524,-7.325,-8.52],'cal/(mol*K)'),
        H298 = (63.249,'kcal/mol'),
        S298 = (12.849,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Calculated at CBS-QB3
""",
)

entry(
    index = 547,
    label = "S4sJ-OCC",
    group = 
"""
1 * S4s u1 p1 c0 {2,S} {3,S} {4,S}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.475,-0.55,-2.75,-4.66,-7.27,-9.325,-8.64],'cal/(mol*K)'),
        H298 = (21.67,'kcal/mol'),
        S298 = (15.449,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 548,
    label = "S4dJ",
    group = 
"""
1 * S4d u1 p1
""",
    thermo = 'S4dJ-OdO',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 549,
    label = "S4dJ-OdH",
    group = 
"""
1   O2d u0 p2 c0 {2,D}
2 * S4d u1 p1 c0 {1,D} {3,S}
3   H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.2,-1.93,-2.59,-3.6,-4.27,-5.1],'cal/(mol*K)'),
        H298 = (58,'kcal/mol'),
        S298 = (0.54,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 550,
    label = "S4dJ-OdO",
    group = 
"""
1   O2d u0 p2 c0 {2,D}
2 * S4d u1 p1 c0 {1,D} {3,S}
3   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-2.41,-3.09,-3.65,-4.42,-4.89,-5.45],'cal/(mol*K)'),
        H298 = (58.9,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 551,
    label = "S6sJ",
    group = 
"""
1 * S6s u1 p0
""",
    thermo = 'S6sJ-CCCCC',
    shortDesc = """Calculated at CBS-QB3""",
    longDesc = 
"""
"
""",
)

entry(
    index = 552,
    label = "S6sJ-CCCCC",
    group = 
"""
1 * S6s u1 p0 c0 {2,S} {3,S} {4,S} {5,S} {6,S}
2   C   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   C   ux {1,S}
6   C   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.815,3.48,2.34,1.364,-0.161,-1.233,-2.644],'cal/(mol*K)'),
        H298 = (60.164,'kcal/mol'),
        S298 = (9.723,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 553,
    label = "S6dJ",
    group = 
"""
1 * S6d u1 p0
""",
    thermo = 'S6dJ-OdOCC',
    shortDesc = """Calculated at CBS-QB3""",
    longDesc = 
"""
"
""",
)

entry(
    index = 554,
    label = "S6dJ-OdOCC",
    group = 
"""
1 * S6d u1 p0 c0 {2,S} {3,S} {4,S} {5,D}
2   O   ux {1,S}
3   C   ux {1,S}
4   C   ux {1,S}
5   O   ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.35,1.6,-0.19,-0.45,-0.95,-1.42,-3.65],'cal/(mol*K)'),
        H298 = (56.531,'kcal/mol'),
        S298 = (3.34,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
Based on radical calculations at CBS-QB3
""",
)

entry(
    index = 555,
    label = "S6ddJ",
    group = 
"""
1 * S6dd u1 p0
""",
    thermo = 'S6ddJ-OdOdO',
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
""",
)

entry(
    index = 556,
    label = "S6ddJ-OdOdH",
    group = 
"""
1   O2d  u0 p2 c0 {2,D}
2 * S6dd u1 p0 c0 {1,D} {3,D} {4,S}
3   O2d  u0 p2 c0 {2,D}
4   H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.977,0.64,-0.027,-0.741,-1.913,-2.873,-4.269],'cal/(mol*K)'),
        H298 = (75.948,'kcal/mol'),
        S298 = (3.331,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 557,
    label = "S6ddJ-OdOdO",
    group = 
"""
1   O2d  u0 p2 c0 {2,D}
2 * S6dd u1 p0 c0 {1,D} {3,D} {4,S}
3   O2d  u0 p2 c0 {2,D}
4   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.539,-1.537,-2.332,-2.933,-4.01,-4.785,-5.701],'cal/(mol*K)'),
        H298 = (86.194,'kcal/mol'),
        S298 = (4.146,'cal/(mol*K)'),
    ),
    shortDesc = """Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc = 
"""
"
From comparison with the saturated closed-shell species, mostly calculated at cbsqb3 with the hydrogen value take from BurcatH2O2 library, 4/2017, Ryan Gillis
""",
)

entry(
    index = 558,
    label = "NJ",
    group = 
"""
1 * N u1
""",
    thermo = 'N3sJ',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "N5scJ-HNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.23096,2.78632,-0.890733,-4.71711,-11.537,-16.9037,-24.8648],'J/(mol*K)'),
        H298 = (244.093,'kJ/mol'),
        S298 = (9.44819,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 560,
    label = "N5scJ-NNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   N    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.26078,-4.51709,-6.33547,-8.68178,-12.6875,-15.8402,-20.7728],'J/(mol*K)'),
        H298 = (243.145,'kJ/mol'),
        S298 = (6.887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "N5scJ-HOO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   O    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.33189,-3.30638,-6.33549,-9.29979,-13.9065,-17.5137,-22.8214],'J/(mol*K)'),
        H298 = (249.25,'kJ/mol'),
        S298 = (-4.29011,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "N5scJ-NOO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   O    u0 {1,S}
3   O    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.490477,-4.77156,-9.06461,-12.6536,-18.0458,-21.5371,-25.0925],'J/(mol*K)'),
        H298 = (268.345,'kJ/mol'),
        S298 = (16.9494,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "N5scJ-CHO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.68916,-0.596662,-3.96519,-7.11111,-12.1745,-15.8829,-21.1153],'J/(mol*K)'),
        H298 = (221.895,'kJ/mol'),
        S298 = (9.67402,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "N5scJ-CNO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   N    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.18288,-10.1337,-12.6351,-14.4515,-17.1056,-18.8129,-21.0934],'J/(mol*K)'),
        H298 = (242.269,'kJ/mol'),
        S298 = (21.4951,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "N5scJ-COO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   O    u0 {1,S}
4   O    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5935,-4.28154,-7.14307,-9.65718,-13.7651,-16.838,-21.2973],'J/(mol*K)'),
        H298 = (252.716,'kJ/mol'),
        S298 = (2.97211,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "N5scJ-CCO",
    group = 
"""
1 * N5sc u1 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   O    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.68915,-13.5775,-15.5782,-17.0545,-19.0312,-20.0961,-21.1052],'J/(mol*K)'),
        H298 = (231.664,'kJ/mol'),
        S298 = (-4.55651,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "N5dcJ-NOd",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   N    u0 {1,S}
3   O    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39198,-3.81228,-7.35331,-10.7644,-15.958,-19.1788,-22.8709],'J/(mol*K)'),
        H298 = (334.654,'kJ/mol'),
        S298 = (10.2785,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "N5dcJ-NdO",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   O    u0 {1,S}
3   N    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499652,-2.21608,-5.07031,-7.71348,-12.0168,-14.9458,-19.6336],'J/(mol*K)'),
        H298 = (330.642,'kJ/mol'),
        S298 = (6.64296,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "N5dcJ-CdO",
    group = 
"""
1 * N5dc u1 {2,S} {3,D}
2   O    u0 {1,S}
3   C    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.630065,-3.07143,-5.60254,-7.95144,-11.7011,-14.4828,-19.0124],'J/(mol*K)'),
        H298 = (292.28,'kJ/mol'),
        S298 = (1.06787,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 570,
    label = "N3sJ-NN",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.34071,-5.69699,-7.91406,-9.88987,-12.9386,-14.9969,-17.7496],'J/(mol*K)'),
        H298 = (312.632,'kJ/mol'),
        S298 = (-0.792667,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "N3sJ-NO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.34109,-6.50259,-10.1593,-12.9651,-16.8921,-19.2488,-21.4789],'J/(mol*K)'),
        H298 = (324.57,'kJ/mol'),
        S298 = (5.85483,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "N3sJ-OO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O   u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.13984,-7.76932,-11.2129,-13.2285,-15.9222,-17.5188,-19.276],'J/(mol*K)'),
        H298 = (311.479,'kJ/mol'),
        S298 = (2.11221,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 573,
    label = "N3sJ-CN",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.80393,-7.37641,-9.47396,-11.2655,-13.9993,-15.8916,-18.271],'J/(mol*K)'),
        H298 = (351.185,'kJ/mol'),
        S298 = (-2.7415,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "N3sJ-CO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   C   u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.19861,-11.8128,-13.9282,-15.0709,-16.1492,-16.3336,-16.3143],'J/(mol*K)'),
        H298 = (332.252,'kJ/mol'),
        S298 = (-0.98057,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "N3sJ-CtO",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   Ct  u0 {1,S}
3   O   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-26.6987,-32.4179,-35.63,-37.6419,-41.0509,-44.038,-47.8704],'J/(mol*K)'),
        H298 = (301.079,'kJ/mol'),
        S298 = (-75.7278,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "N3sJ",
    group = 
"""
1 * N3s u1 p1
""",
    thermo = 'NHJ_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 577,
    label = "NH2J",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   H   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.43,-0.82,-1.27,-1.72,-2.48,-3.08,-4.1],'cal/(mol*K)'),
        H298 = (107.183,'kcal/mol'),
        S298 = (0.53,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to ammonia from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "NHJ_C",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-1.23,-1.64,-2.02,-2.66,-3.2,-4.16],'cal/(mol*K)'),
        H298 = (99.653,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated in relation to CH3NH2 from thermo_DFT_CCSDTF12_BAC values""",
    longDesc = 
"""

""",
)

entry(
    index = 579,
    label = "NHJ_Cd",
    group = 
"""
1 * N3s      u1 p1 {2,S} {3,S}
2   [Cd,Cdd] u0 p0 {1,S}
3   H        u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.36968,-7.21186,-7.55213,-8.1556,-9.51515,-10.9959,-14.5568],'J/(mol*K)'),
        H298 = (353.261,'kJ/mol'),
        S298 = (-3.90709,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 580,
    label = "NHJ_O",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   O   u0 p2 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26,-1.89,-2.4,-2.79,-3.17,-3.37,-3.65],'cal/(mol*K)'),
        H298 = (85.023,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2OH and [NH]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "NHJ_N",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N   u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77,-2.62,-3.28,-3.79,-4.57,-5.11,-5.85],'cal/(mol*K)'),
        H298 = (82.283,'kcal/mol'),
        S298 = (-0.33,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2NH2 and [NH]NH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "NHJ_N3d",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   N3d u0 {1,S}
3   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.70038,-4.63454,-6.10735,-7.60395,-10.2929,-12.3802,-15.6322],'J/(mol*K)'),
        H298 = (339.161,'kJ/mol'),
        S298 = (1.25886,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "NHJ_N5dc",
    group = 
"""
1 * N3s  u1 p1 {2,S} {3,S}
2   N5dc u0 {1,S}
3   H    u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.78518,1.52507,-3.04956,-6.60718,-12.0808,-15.9009,-20.6874],'J/(mol*K)'),
        H298 = (434.288,'kJ/mol'),
        S298 = (2.72516,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 584,
    label = "NJ_CC",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   C   u0 p0 {1,S}
3   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.88844,-7.02096,-9.05679,-10.9554,-13.6124,-15.7099,-19.2836],'J/(mol*K)'),
        H298 = (389.974,'kJ/mol'),
        S298 = (-10.0809,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "NJ_CCd",
    group = 
"""
1 * N3s      u1 p1 {2,S} {3,S}
2   C        u0 p0 {1,S}
3   [Cd,Cdd] u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94584,-1.87787,-2.86025,-4.58312,-8.42517,-11.1267,-15.6176],'J/(mol*K)'),
        H298 = (350.499,'kJ/mol'),
        S298 = (-11.7385,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "NJ_CCO",
    group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   CO  u0 p0 {1,S} {4,D}
3   C   u0 p0 {1,S}
4   O2d u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.961761,-0.807363,-3.28705,-5.60897,-9.76264,-13.2901,-19.6482],'J/(mol*K)'),
        H298 = (450.927,'kJ/mol'),
        S298 = (3.87449,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 587,
    label = "N3dJ",
    group = 
"""
1 * N3d u1 p1
""",
    thermo = 'N3dJ_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 588,
    label = "N3dJ_C",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   C   u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2,-0.6,-1.07,-1.56,-2.44,-3.15,-4.26],'cal/(mol*K)'),
        H298 = (88.343,'kcal/mol'),
        S298 = (-0.71,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH=CH2 and [N]=CH2, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 589,
    label = "N3dJ_Cdd",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   Cdd u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.67103,-7.14899,-8.76464,-10.2906,-12.8917,-14.9076,-18.0576],'J/(mol*K)'),
        H298 = (257.412,'kJ/mol'),
        S298 = (-1.20388,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 590,
    label = "N3dJ_O",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   O   u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12,-1.36,-1.67,-2,-2.62,-3.11,-3.89],'cal/(mol*K)'),
        H298 = (48.613,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t HN=O and [N]=O, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 591,
    label = "N3dJ_N",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14,-0.51,-0.97,-1.46,-2.33,-3.02,-4.16],'cal/(mol*K)'),
        H298 = (64.083,'kcal/mol'),
        S298 = (1.49,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t HN=NH and [N]=NH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 592,
    label = "N3dJ_N5dc",
    group = 
"""
1 * N3d  u1 p1 {2,D}
2   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0356123,-2.98703,-5.6088,-7.86526,-11.8936,-15.0898,-19.6396],'J/(mol*K)'),
        H298 = (413.171,'kJ/mol'),
        S298 = (2.89249,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "N3dJ_N3d",
    group = 
"""
1 * N3d u1 p1 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.05081,-2.13979,-6.00346,-9.14917,-13.5357,-16.2931,-19.6448],'J/(mol*K)'),
        H298 = (306.397,'kJ/mol'),
        S298 = (18.8295,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 594,
    label = "RJ2_triplet",
    group = 
"""
1 * R!H u2
""",
    thermo = 'CJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 595,
    label = "CJ2_triplet",
    group = 
"""
1 * C u2
""",
    thermo = 'CsJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "OsCsJ2H_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   O  u0 p2 {1,S} {4,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.444,-1.111,-1.988,-2.889,-4.529,-5.915,-8.422],'cal/(mol*K)'),
        H298 = (205.773,'kcal/mol'),
        S298 = (-2.011,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 597,
    label = "CsJ2_triplet",
    group = 
"""
1 * Cs u2
""",
    thermo = 'CH2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "CH2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (214.44,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 599,
    label = "CsJ2_P_triplet",
    group = 
"""
1 * Cs       u2 {2,S} {3,S}
2   C        u0 {1,S}
3   [H,Val7] u0 {1,S}
""",
    thermo = 'CsCsJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "CsCVal7_triplet",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   C    u0 {1,S}
3   Val7 u0 {1,S}
""",
    thermo = 'CsCCl_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "CsCF_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   F  u0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 602,
    label = "CsCCl_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   Cl u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46058,-2.59924,-3.68621,-4.60621,-6.0777,-7.22296,-9.13333],'cal/(mol*K)','+|-',[0.580966,0.594507,0.556846,0.519833,0.458415,0.401241,0.300047]),
        H298 = (192.67,'kcal/mol','+|-',0.904775),
        S298 = (-1.68686,'cal/(mol*K)','+|-',1.36155),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 603,
    label = "CsCBr_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   Br u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19766,-2.41025,-3.49516,-4.42152,-5.96821,-7.20171,-9.18029],'cal/(mol*K)','+|-',[0.450015,0.460503,0.431331,0.402661,0.355086,0.3108,0.232415]),
        H298 = (196.298,'kcal/mol','+|-',0.700836),
        S298 = (-0.701079,'cal/(mol*K)','+|-',1.05465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 604,
    label = "CsCsJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = 'CCJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "CCJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
5   H  u0 {2,S}
6   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],'cal/(mol*K)'),
        H298 = (211.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 606,
    label = "PhCH_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (195,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from PUTSMA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "AllylJ2_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (192.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """BDE from PUTSMA et al.""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "CsJ2_S_triplet",
    group = 
"""
1 * Cs u2 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = 'CsJ2_P_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "CdJ2_triplet",
    group = 
"""
1 * [Cd,CO] u2
""",
    thermo = 'CCdJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 610,
    label = "CCdJ2_triplet",
    group = 
"""
1 * Cd u2 {2,D}
2   C  u0 {1,D}
""",
    thermo = 'CdCdJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "CdCdJ2_triplet",
    group = 
"""
1 * Cd u2 {2,D}
2   Cd u0 {1,D} {3,S} {4,S}
3   H  u0 {2,S}
4   H  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904,-2.152,-3.433,-4.583,-6.214,-7.197,-9.27],'cal/(mol*K)'),
        H298 = (237.632,'kcal/mol'),
        S298 = (1.79,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 612,
    label = "(CO)CdJ2_triplet",
    group = 
"""
1 * Cd  u2 {2,D}
2   Cdd u0 {1,D} {3,D}
3   O   u0 p2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.763,-2.732,-3.654,-4.473,-5.712,-6.563,-8.315],'cal/(mol*K)'),
        H298 = (206.595,'kcal/mol'),
        S298 = (-1.634,'cal/(mol*K)'),
    ),
    shortDesc = """Fittted to DFT_QCI_thermo library""",
    longDesc = 
"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 613,
    label = "NCdJ2_triplet",
    group = 
"""
1 * Cd  u2 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.67688,-8.56951,-13.0936,-17.1322,-23.6155,-28.3134,-35.4124],'J/(mol*K)'),
        H298 = (587.145,'kJ/mol'),
        S298 = (22.0742,'J/(mol*K)'),
    ),
    shortDesc = """Derived from nitrogen species in RMG thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "CdJ2-Sd_triplet",
    group = 
"""
1 * CS  u2 {2,D}
2   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-2.3,-3.22,-4.04,-5.42,-6.5,-8.29],'cal/(mol*K)'),
        H298 = (238.75,'kcal/mol'),
        S298 = (-3.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 615,
    label = "Oa_triplet",
    group = 
"""
1 * O u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (221.55,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 616,
    label = "SiJ2_triplet",
    group = 
"""
1 * Si u2
""",
    thermo = 'CJ2_triplet',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 617,
    label = "SJ2_triplet",
    group = 
"""
1 * S u2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19,-3.52,-3.89,-4.3,-5.12,-5.86,-7.14],'cal/(mol*K)'),
        H298 = (176.42,'kcal/mol'),
        S298 = (-12.02,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "NJ2_triplet",
    group = 
"""
1 * N u2
""",
    thermo = 'NJ2_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "N3sJ2",
    group = 
"""
1 * N3s u2 p1
""",
    thermo = 'NJ2_C',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "NHJ2",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.1,-2.78,-3.47,-4.75,-5.77,-7.61],'cal/(mol*K)'),
        H298 = (200.636,'kcal/mol'),
        S298 = (-2.72,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH3 and [N], both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 621,
    label = "NJ2_C",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.36,-2.97,-3.51,-4,-5,-5.96,-7.75],'cal/(mol*K)'),
        H298 = (184.816,'kcal/mol'),
        S298 = (-3.04,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2CH3 and [N]CH3, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "NJ2_O",
    group = 
"""
1 * N3s u2 p1 {2,S}
2   O   u0 p2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-3.22,-4.34,-5.36,-6.88,-7.91,-9.25],'cal/(mol*K)'),
        H298 = (166.156,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated w.r.t NH2OH and [N]OH, both from thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "RJ3",
    group = 
"""
1 * R!H u3
""",
    thermo = 'CJ3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 624,
    label = "CJ3",
    group = 
"""
1 * Cs u3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],'cal/(mol*K)'),
        H298 = (316.19,'kcal/mol'),
        S298 = (-5.7,'cal/(mol*K)'),
    ),
    shortDesc = """Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "SiJ3",
    group = 
"""
1 * Sis u3
""",
    thermo = 'CJ3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CsBr1sBr1sCO
                L5: CsBr1sCOCl1s
                L5: CsCOCl1sCl1s
                L5: CsBr1sCOF1s
                L5: CsCOCl1sF1s
                L5: CsCOF1sF1s
                L5: CsBr1sCOH
                L5: CsCOCl1sH
                L5: CsCOF1sH
                L5: CsBr1sCOO2s
                L5: CsCOCl1sO2s
                L5: CsCOF1sO2s
                L5: CsBr1sCOCO
                L5: CsCOCOCl1s
                L5: CsCOCOF1s
                L5: CsBr1sCOCt
                L5: CsCOCl1sCt
                L5: CsCOCtF1s
                L5: CsBr1sCOCd
                L5: CsCOCdCl1s
                L5: CsCOCdF1s
                L5: CsBr1sCOCs
                L5: CsCOCl1sCs
                L5: CsCOCsF1s
                L5: CsBr1sBr1sO2s
                L5: CsBr1sCl1sO2s
                L5: CsCl1sCl1sO2s
                L5: CsBr1sF1sO2s
                L5: CsCl1sF1sO2s
                L5: CsF1sF1sO2s
                L5: CsBr1sHO2s
                L5: CsCl1sHO2s
                L5: CsF1sHO2s
                L5: CsBr1sO2sO2s
                L5: CsCl1sO2sO2s
                L5: CsF1sO2sO2s
                L5: CsBr1sBr1sCt
                L5: CsBr1sCl1sCt
                L5: CsCl1sCl1sCt
                L5: CsBr1sCtF1s
                L5: CsCl1sCtF1s
                L5: CsCtF1sF1s
                L5: CsBr1sCtH
                L5: CsCl1sCtH
                L5: CsCtF1sH
                L5: CsBr1sCtO2s
                L5: CsCl1sCtO2s
                L5: CsCtF1sO2s
                L5: CsBr1sCtCt
                L5: CsCl1sCtCt
                L5: CsCtCtF1s
                L5: CsBr1sBr1sCd
                L5: CsBr1sCdCl1s
                L5: CsCdCl1sCl1s
                L5: CsBr1sCdF1s
                L5: CsCdCl1sF1s
                L5: CsCdF1sF1s
                L5: CsBr1sCdH
                L5: CsCdCl1sH
                L5: CsCdF1sH
                L5: CsBr1sCdO2s
                L5: CsCdCl1sO2s
                L5: CsCdF1sO2s
                L5: CsBr1sCdCt
                L5: CsCdCl1sCt
                L5: CsCdCtF1s
                L5: CsBr1sCdCd
                L5: CsCdCdCl1s
                L5: CsCdCdF1s
                L5: CsBr1sBr1sCs
                L5: CsBr1sCl1sCs
                L5: CsCl1sCl1sCs
                L5: CsBr1sCsF1s
                L5: CsCl1sCsF1s
                L5: CsCsF1sF1s
                L5: CsBr1sCsH
                L5: CsCl1sCsH
                L5: CsCsF1sH
                L5: CsBr1sCsO2s
                L5: CsCl1sCsO2s
                L5: CsCsF1sO2s
                L5: CsBr1sCsCt
                L5: CsCl1sCsCt
                L5: CsCsCtF1s
                L5: CsBr1sCdCs
                L5: CsCdCl1sCs
                L5: CsCdCsF1s
                L5: CsBr1sCsCs
                L5: CsCl1sCsCs
                L5: CsCsCsF1s
                L5: CH3
                L5: Cs_P
                    L6: CJCO
                        L7: C=C(O)CJ
                        L7: CJCOOH
                        L7: CJC(C)OC
                        L7: CJC(C)2O
                            L8: C=CC(C)(O)CJ
                                L9: C=CC(O)(C=O)CJ
                            L8: CJC(C)(C=O)O
                        L7: CJC(O)2C
                            L8: C=CC(O)2CJ
                    L6: CJCC=O
                        L7: CJC(C)2C=O
                            L8: CJC(C=O)2C
                                L9: C=CC(C=O)2CJ
                            L8: C=CC(C)(C=O)CJ
                        L7: CJC(C)C=O
                        L7: C=C(C=O)CJ
                    L6: CJCC=C=O
                        L7: CJC(C)C=C=O
                        L7: C=C(CJ)C=C=O
                    L6: CsCsJ
                        L7: CCJ
                        L7: RCCJ
                        L7: Neopentyl
                        L7: Isobutyl
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                        L7: CJC=C=O
                    L6: Propargyl
                    L6: CJC=O
                        L7: C2JC=O
                L5: Cs_S
                    L6: CCJCO
                        L7: C=CCJCO
                            L8: C=CCJC(O)C=C
                        L7: CCJCOOH
                    L6: CCJCC=O
                    L6: CCJC(C)=C=O
                    L6: (Cs)2CsJ
                        L7: cyclopentene-4
                            L8: bicyclo[2.1.1]hex-2-ene-C5
                                L9: tricyclo[2.1.1.0(1,4)]hex-2-ene-C5
                            L8: bicyclo[2.1.0]pent-2-ene-C5
                        L7: bicyclo[1.1.1]pentane-C2
                            L8: tricyclo[1.1.1.0(1,3)]pentane-C2
                        L7: bicyclo[2.1.1]hexane-C5
                            L8: tricyclo[2.1.1.0(1,4)]hexane-C5
                        L7: cyclopropane
                            L8: spiro[2.2]pentane-secondary
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C7
                            L8: bicyclo[2.1.0]pentane-secondary-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C6
                            L8: bicyclo[1.1.0]butane-secondary
                            L8: bicyclo[3.1.0]hexane-C3
                            L8: bicyclo[4.1.0]heptane-C3-7
                            L8: bicyclo[4.1.0]heptane-C3-7
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C2
                        L7: bicyclo[3.1.1]heptane-C6
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C2
                        L7: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[2.2.2]octane-C2
                            L8: tricyclo[2.2.2.0(1,4)]octane-C2
                        L7: cyclobutane
                            L8: bicyclo[2.1.0]pentane-secondary-C4
                            L8: bicyclo[2.2.0]hexane-secondary
                            L8: bicyclo[3.2.0]heptane-C5-6
                            L8: tricyclo[2.2.1.0(1,4)]heptane-C2
                            L8: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[3.1.1]heptane-C2
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C2
                        L7: bicyclo[3.1.0]hexane-C5-2
                        L7: bicyclo[3.1.0]hexane-C5-3
                        L7: bicyclo[2.1.1]hexane-C2
                        L7: 7-norbornyl
                        L7: 2-norbornyl
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: cycloheptane
                            L8: bicyclo[3.2.0]heptane-C5-2
                            L8: bicyclo[3.2.0]heptane-C5-3
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[3.1.1]heptane-C3
                            L8: tricyclo[3.1.1.0(1,5)]heptane-C3
                        L7: octahydro-pentalene-C5-2
                        L7: octahydro-pentalene-C5-3
                        L7: bicyclo[4.2.0]octane-C6-2
                        L7: bicyclo[4.2.0]octane-C6-3
                        L7: CCJC
                        L7: RCCJC
                        L7: RCCJCC
                            L8: cyclopentane
                            L8: cyclohexane
                    L6: Benzyl_S
                        L7: Indenyl
                        L7: Benzyl_S_Fused5
                        L7: Benzyl_S_Fused6
                            L8: Benzyl_S_dihydronaphthalene
                        L7: Benzyl_S_Fused7
                    L6: Allyl_S
                        L7: Aromatic_pi_S_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_S_(fused5)_1_3
                                    L10: Aromatic_pi_S_(fused6)_1_3
                                    L10: Aromatic_pi_S_(fused7)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_1
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_1
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_1
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_1
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_3_2
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_3_2
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_3_2
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_3_2
                            L8: Aromatic_pi_S_(CH3_CH3_Para)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Para)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Para)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Para)_1_3
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_3
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_3
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_3
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_3
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_3
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_3
                        L7: CJ-Cd-Benzene
                        L7: CJ-Cd-Benzene7
                        L7: cyclobutene-allyl
                        L7: cyclopentene-allyl
                        L7: cyclohexene-allyl
                    L6: C=CCJC=C
                        L7: Aromatic_pi_S_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Ortho)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Ortho)_1_4
                                    L10: Aromatic_pi_S_(fused5)_1_4
                                    L10: Aromatic_pi_S_(fused6)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Ortho)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Ortho)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Meta)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Meta)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Meta)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Meta)_1_4
                            L8: Aromatic_pi_S_(CH3_CH3_Sub)_1_4
                                L9: Aromatic_pi_S_(s1_3_6_diene_1_4)_1_4
                                L9: Aromatic_pi_S_(CH3_C2H5_Sub)_1_4
                                    L10: Aromatic_pi_S_(s1_4_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_5_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(s1_6_6_diene_1_4)_1_4
                                    L10: Aromatic_pi_S_(CH3_Benzyl_Sub)_1_4
                                        L11: Aromatic_pi_S_(CH3_EBenzyl_Sub)_1_4
                        L7: cyclopropenyl-allyl
                        L7: 1,3-cyclopentadiene-allyl
                        L7: C=CCJC=C=O
                    L6: Sec_Propargyl
                    L6: CCJC=O
                        L7: CCJCHO
                        L7: C=OCJC=O
                L5: Cs_T
                    L6: CCJ(C)CO
                        L7: C2CJCOOH
                    L6: Tertalkyl
                        L7: bicyclo[1.1.0]butane-tertiary
                        L7: bicyclo[2.1.0]pentane-tertiary
                        L7: bicyclo[1.1.1]pentane-C1
                        L7: bicyclo[3.1.0]hexane-tertiary
                        L7: bicyclo[2.2.0]hexane-tertiary
                        L7: bicyclo[2.1.1]hexane-C1
                        L7: bridgehead_norbornyl
                        L7: bicyclo[3.2.0]heptane-tertiary
                        L7: bicyclo[4.1.0]heptane-tertiary
                        L7: bicyclo[3.1.1]heptane-C1
                        L7: octahydro-pentalene-tertiary
                        L7: bicyclo[4.2.0]octane-tertiary
                        L7: bicyclo[2.2.2]octane-C1
                    L6: Benzyl_T
                        L7: Benzyl_T_Fused5
                        L7: Benzyl_T_Fused6
                            L8: Benzyl_T_dihydronaphthalene
                    L6: CCJ(C)C=C=O
                        L7: C=CCJ(C)C=C=O
                            L8: C=CCJ(C=C=O)C=C
                    L6: Allyl_T
                        L7: Aromatic_pi_T_1_3
                            L8: Aromatic_pi_T_(CH3_CH3_Ortho)_1_3
                                L9: Aromatic_pi_T_(CH3_C2H5_Ortho)_1_3
                                    L10: Aromatic_pi_T_(fused5)_1_3
                                    L10: Aromatic_pi_T_(fused6)_1_3
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Ortho)_1_3
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Ortho)_1_3
                        L7: Aromatic_pi_T_1_4
                            L8: Aromatic_pi_T_(CH3_CH3_Para)_1_4
                                L9: Aromatic_pi_T_(CH3_C2H5_Para)_1_4
                                    L10: Aromatic_pi_T_(CH3_Benzyl_Para)_1_4
                                        L11: Aromatic_pi_T_(CH3_EBenzyl_Para)_1_4
                        L7: bicyclo[2.1.0]pent-2-ene-C1
                        L7: bicyclo[2.1.1]hex-2-ene-C1
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C1
                        L7: C=CCJ(C)C=O
                            L8: C=CCJ(C=O)C=C
                    L6: Tert_Propargyl
                    L6: C2CJCO
                        L7: C2CJCHO
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                            L8: C=COCJ
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                L5: CCsJO
                    L6: CCsJOC
                        L7: C=CCJ(O)C
                        L7: CCsJOCs
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: C=CCJO
                    L6: OCJC=O
                    L6: CCsJOH
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                L5: C2CsJO
                    L6: C2CsJOH
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
                L5: CsJ-S
                    L6: CsJ-SsHH
                    L6: CsJ-CSH
                        L7: CsJ-CsSsH
                        L7: CsJ-CtSsH
                        L7: CsJ-CbSsH
                        L7: CsJ-CdSsH
                        L7: CsJ-C=SSsH
                    L6: CsJ-CCS
                        L7: CsJ-CsCsSs
                        L7: CsJ-CsCtSs
                        L7: CsJ-CsCbSs
                        L7: CsJ-CsCdSs
                        L7: CsJ-CsC=SSs
                    L6: CsJ-SS
                        L7: CsJ-SsSsH
                        L7: CsJ-CSS
                            L8: CsJ-CsSsSs
                            L8: CsJ-CtSsSs
                            L8: CsJ-CbSsSs
                            L8: CsJ-CdSsSs
                            L8: CsJ-C=SSsSs
                        L7: CsJ-SsSsSs
                    L6: CCsJOS
                        L7: CCsJOHSH
                    L6: CsJ-SsOsH
                L5: OCJO
                L5: CsJ-HNN
                    L6: CsJ-HNN3ds
                        L7: CsJ-HN(N3dCd)
                        L7: CsJ-HN(N3dOd)
                        L7: CsJ-HN(N3dN5dc)
                    L6: CsJ-HN5scN5sc
                L5: CsJ-NNN
                L5: CsJ-HNO
                    L6: CsJ-HON1sc
                L5: CsJ-NNO
                L5: CsJ-NOO
                L5: CsJ-CNN
                L5: CsJ-CNO
                L5: CsJN
                    L6: CsJN3s
                    L6: CsJN5sdtc
                        L7: CsJN5sc
                        L7: CsJN5dcOdO0sc
                        L7: CsJN5dcN3dO0sc
                    L6: CsJN3dCd
                    L6: CsJN3dCdd
                    L6: CsJN3dN5dc
                L5: CCsJN
                    L6: CdCsJN
                L5: C2CsJN
            L4: CdsJ
                L5: CdBr1sCdd
                L5: CdCddCl1s
                L5: CdCddF1s
                L5: CdBr1sCd
                L5: CdCdCl1s
                L5: CdCdF1s
                L5: CdsJO
                    L6: COBr1sO2d
                    L6: COCl1sO2d
                    L6: COF1sO2d
                    L6: COJ-NOd
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CC(C)CJ=O
                            L8: CC(C)2CJ=O
                                L9: CC(C)(C=O)CJ=O
                                    L10: C=CC(C)(C=O)CJ=O
                                L9: C=CC(C)2CJ=O
                            L8: CC(C)(O)CJ=O
                                L9: C=CC(C)(O)CJ=O
                        L7: CCCJ=O
                            L8: C=OCCJ=O
                                L9: C=OC=OCJ=O
                            L8: C=C(C)CJ=O
                        L7: CsCJ=O
                        L7: C=CCJ=O
                        L7: OC=OCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                    L6: SCJ=O
                L5: Cds_P
                    L6: C=C=CJ
                    L6: N=C=CJ
                L5: Cds_S
                    L6: C=CJC=O
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                            L8: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                        L7: 1,3-cyclopentadiene-vinyl-2
                    L6: cyclopropenyl-vinyl
                    L6: cyclobutene-vinyl
                        L7: bicyclo[2.1.0]pent-2-ene-C2
                            L8: tricyclo[2.1.1.0(1,4)]hex-2-ene-C2
                        L7: bicyclo[2.2.0]hexa-2,5-diene-C2
                    L6: cyclopentene-vinyl
                        L7: bicyclo[2.1.1]hex-2-ene-C2
                    L6: 1,3-cyclopentadiene-vinyl-1
                    L6: CCCJ=C=O
                        L7: CC(C)CJ=C=O
                        L7: C=C(C)CJ=C=O
                    L6: OC=CJCb
                    L6: N=C=CJC
                L5: S2s-CJ=C
                L5: C=CJO
                L5: CdJ-NN
                L5: CdJ-CdN
                    L6: CdJ-CddN
                L5: CdJ-NdO
                L5: CdJ-NdC
                L5: CdJ-HN3d
                    L6: CdJ-H(N3dOs)
                    L6: CdJ-H(N3dCO)
                    L6: CdJ-H(N3dN3d)
                    L6: CdJ-H(N3dCd)
                L5: CdJ-HN5dc
            L4: CtJ
                L5: Acetyl
            L4: CbJ
            L4: C=SJ
                L5: C=SJ-S2s
                L5: C=SJ-H
                L5: C=SJ-C
                    L6: C=SJ-Cd
                    L6: C=SJ-Cs
        L3: OJ
            L4: HOJ
            L4: COJ
                L5: CCOJ
                    L6: C=OCOJ
                        L7: C=CC(C)(C=O)OJ
                        L7: CC(C)(C=O)OJ
                        L7: C=OC=OOJ
                    L6: CC(C)OJ
                        L7: CC(C)2OJ
                            L8: C=CC(C)2OJ
                        L7: CC(C)(O)OJ
                            L8: C=CC(C)(O)OJ
                    L6: C=C(C)OJ
                L5: CdsOJ
                    L6: RC=COJ
                        L7: C=COJ
                        L7: N=COJ
                            L8: O0scN5dc=COJ
                    L6: OJC=O
                        L7: OC=OOJ
                L5: OCOJ
                L5: SCOJ
                L5: CsOJ
                    L6: H3COJ
                L5: CbOJ
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                    L6: SOOJ
                L5: HOOJ
            L4: SOJ
                L5: O2sJ-S2s
                L5: O2sJ-S4d
                    L6: O2sJ-(S4d-OdO)
                    L6: O2sJ-(S4d-OdC)
                    L6: O2sJ-(S4d-OdH)
                    L6: O2sJ-(S4d-CdC)
                L5: O2sJ-S6d
            L4: O2sJ-N
                L5: O2sJ-N3s
                    L6: O2sJ-N3sC
                        L7: O2sJ-N3sCO
                    L6: O2sJ-N3sO2s
                    L6: O2sJ-N3s(N5sdcO0sc)
                L5: O2sJ-N5sdtc
                    L6: O2sJ-N5dcOd
                        L7: O2sJ-N5dcOdO0sc
                L5: O2sJ-N1sc
                L5: O2sJ-N3dN3d
                L5: O2sJ-N3dCd
        L3: SiJ
        L3: SJ
            L4: S2J
                L5: S2J-H
                L5: S2J-C
                    L6: S2J-Cs
                        L7: S2sJ-(CsHHH)
                        L7: S2J-(Cs-Cb)
                    L6: S2J-Ct
                    L6: S2J-Cb
                    L6: S2J-Cd
                    L6: S2J-C=S
                    L6: S2J-CO
                L5: S2J-S2s
                    L6: S2J-S2s-H
                    L6: S2J-S2s-Cs
                    L6: S2J-S2s-S2s
                L5: S2sJ-O
            L4: S4sJ
                L5: S4sJ-CCC
                L5: S4sJ-OCC
            L4: S4dJ
                L5: S4dJ-OdH
                L5: S4dJ-OdO
            L4: S6sJ
                L5: S6sJ-CCCCC
            L4: S6dJ
                L5: S6dJ-OdOCC
            L4: S6ddJ
                L5: S6ddJ-OdOdH
                L5: S6ddJ-OdOdO
        L3: NJ
            L4: N5scJ-HNO
            L4: N5scJ-NNO
            L4: N5scJ-HOO
            L4: N5scJ-NOO
            L4: N5scJ-CHO
            L4: N5scJ-CNO
            L4: N5scJ-COO
            L4: N5scJ-CCO
            L4: N5dcJ-NOd
            L4: N5dcJ-NdO
            L4: N5dcJ-CdO
            L4: N3sJ-NN
            L4: N3sJ-NO
            L4: N3sJ-OO
            L4: N3sJ-CN
            L4: N3sJ-CO
                L5: N3sJ-CtO
            L4: N3sJ
                L5: NH2J
                L5: NHJ_C
                    L6: NHJ_Cd
                L5: NHJ_O
                L5: NHJ_N
                    L6: NHJ_N3d
                    L6: NHJ_N5dc
                L5: NJ_CC
                    L6: NJ_CCd
                    L6: NJ_CCO
            L4: N3dJ
                L5: N3dJ_C
                    L6: N3dJ_Cdd
                L5: N3dJ_O
                L5: N3dJ_N
                    L6: N3dJ_N5dc
                    L6: N3dJ_N3d
    L2: RJ2_triplet
        L3: CJ2_triplet
            L4: OsCsJ2H_triplet
            L4: CsJ2_triplet
                L5: CH2_triplet
                L5: CsJ2_P_triplet
                    L6: CsCVal7_triplet
                        L7: CsCF_triplet
                        L7: CsCCl_triplet
                        L7: CsCBr_triplet
                    L6: CsCsJ2_triplet
                        L7: CCJ2_triplet
                    L6: PhCH_triplet
                    L6: AllylJ2_triplet
                L5: CsJ2_S_triplet
            L4: CdJ2_triplet
                L5: CCdJ2_triplet
                    L6: CdCdJ2_triplet
                    L6: (CO)CdJ2_triplet
                L5: NCdJ2_triplet
            L4: CdJ2-Sd_triplet
        L3: Oa_triplet
        L3: SiJ2_triplet
        L3: SJ2_triplet
        L3: NJ2_triplet
            L4: N3sJ2
                L5: NHJ2
                L5: NJ2_C
                L5: NJ2_O
    L2: RJ3
        L3: CJ3
        L3: SiJ3
"""
)

