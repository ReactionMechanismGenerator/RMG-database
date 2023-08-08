#!/usr/bin/env python
# encoding: utf-8

name = "Ring Corrections"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Dummy Root""",
    longDesc = 
"""

""",
    rank = 10,
)

entry(
    index = 1,
    label = "Aromatic",
    group = 
"""
1 * Cb u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatic""",
    longDesc = 
"""
Ring correction is zero because RMG uses Cb group corrections instead in the case of a ring containing Cb bonds
""",
    rank = 1,
)

entry(
    index = 2,
    label = "Benzene",
    group = 
"""
1 * Cb u0 {2,B} {6,B}
2   Cb u0 {1,B} {3,B}
3   Cb u0 {2,B} {4,B}
4   Cb u0 {3,B} {5,B}
5   Cb u0 {4,B} {6,B}
6   Cb u0 {1,B} {5,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatic""",
    longDesc = 
"""
Ring correction is zero because RMG uses Cb group corrections instead in the case of a ring containing Cb bonds
""",
    rank = 1,
)

entry(
    index = 3,
    label = "ThreeMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {3,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {1,[S,D]} {2,[S,D]}
""",
    thermo = 'Cyclopropane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "Cyclopropane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (27.53,'kcal/mol'),
        S298 = (32.0088,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopropane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "Cs-Cs-Cs(C-BrBrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {2,S} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.61227,-2.73932,-2.78112,-2.79916,-2.79183,-2.53906,-1.59282],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (31.5693,'kcal/mol','+|-',1.536),
        S298 = (35.2151,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 6,
    label = "Cs-Cs-Cs(Br)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.71567,-3.40839,-3.21508,-3.03894,-2.70467,-2.34933,-1.50193],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (31.7661,'kcal/mol','+|-',2.66044),
        S298 = (34.6898,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 7,
    label = "Cs-Cs(C)-Cs(Br)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.57244,-3.66119,-3.56584,-3.40747,-3.12547,-2.71276,-1.66086],'cal/(mol*K)','+|-',[0.16009,0.177701,0.172514,0.165858,0.149773,0.127188,0.0902133]),
        H298 = (35.0709,'kcal/mol','+|-',0.935205),
        S298 = (35.8927,'cal/(mol*K)','+|-',0.494128),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         12
""",
)

entry(
    index = 8,
    label = "Cs(C)-Cs-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.66744,-4.29064,-4.46919,-4.38542,-3.99643,-3.38843,-2.25226],'cal/(mol*K)','+|-',[0.219968,0.244165,0.237038,0.227892,0.205791,0.174759,0.123955]),
        H298 = (33.5444,'kcal/mol','+|-',1.28499),
        S298 = (37.1682,'cal/(mol*K)','+|-',0.678943),
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
    index = 9,
    label = "Cs-Cs-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.81631,-4.03607,-4.04411,-3.9402,-3.55871,-2.99627,-1.79289],'cal/(mol*K)','+|-',[0.150738,0.167319,0.162435,0.156168,0.141023,0.119757,0.0849429]),
        H298 = (33.7637,'kcal/mol','+|-',0.880568),
        S298 = (37.4909,'cal/(mol*K)','+|-',0.46526),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         10
""",
)

entry(
    index = 10,
    label = "Cs-Cs-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.43686,-3.64179,-3.75375,-3.70824,-3.4042,-2.94,-1.8973],'cal/(mol*K)','+|-',[0.198793,0.220661,0.21422,0.205954,0.185981,0.157936,0.112023]),
        H298 = (36.1253,'kcal/mol','+|-',1.16129),
        S298 = (35.8466,'cal/(mol*K)','+|-',0.613585),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         9
""",
)

entry(
    index = 11,
    label = "Cs-Cs(Br)(O2)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.23767,-4.33706,-4.15493,-3.99465,-3.61073,-3.07074,-1.70253],'cal/(mol*K)','+|-',[0.276267,0.306657,0.297706,0.286219,0.258461,0.219487,0.15568]),
        H298 = (36.5994,'kcal/mol','+|-',1.61388),
        S298 = (36.3519,'cal/(mol*K)','+|-',0.852712),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 12,
    label = "Cs-Cs-Cs(C-BrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cs   u0 p0 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.26593,-3.70522,-3.77337,-3.62941,-3.3305,-2.93443,-1.75093],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (25.4054,'kcal/mol','+|-',2.66044),
        S298 = (33.1286,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 13,
    label = "Cs-Cs(C-Br)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.59333,-3.85363,-3.90738,-3.75407,-3.22627,-2.65686,-1.87717],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (28.7951,'kcal/mol','+|-',2.66044),
        S298 = (32.8166,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 14,
    label = "Cs-Cs-Cs(C-Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.15795,-4.25937,-4.1245,-3.92886,-3.40626,-2.75058,-1.59025],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (30.7395,'kcal/mol','+|-',1.88121),
        S298 = (34.0376,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 15,
    label = "Cs-Cs(C-ClClCl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * Cs   u0 p0 c0 {2,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.78244,-2.93905,-3.04407,-2.99606,-2.80598,-2.43476,-1.57625],'cal/(mol*K)','+|-',[0.228167,0.253267,0.245874,0.236387,0.213462,0.181273,0.128576]),
        H298 = (33.0014,'kcal/mol','+|-',1.33289),
        S298 = (34.8743,'cal/(mol*K)','+|-',0.70425),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 16,
    label = "Cs(C-ClCl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cs   u0 p0 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.13981,-4.27391,-4.16181,-4.10136,-3.86265,-3.22478,-1.68903],'cal/(mol*K)','+|-',[0.175998,0.195359,0.189656,0.182338,0.164655,0.139826,0.0991775]),
        H298 = (33.6527,'kcal/mol','+|-',1.02813),
        S298 = (34.9011,'cal/(mol*K)','+|-',0.543227),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         7
""",
)

entry(
    index = 17,
    label = "Cs(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.74707,-3.55144,-3.41961,-3.36579,-3.07611,-2.66397,-1.99505],'cal/(mol*K)','+|-',[0.273982,0.304121,0.295244,0.283852,0.256324,0.217671,0.154393]),
        H298 = (33.1093,'kcal/mol','+|-',1.60053),
        S298 = (36.4095,'cal/(mol*K)','+|-',0.84566),
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
    index = 18,
    label = "Cs-Cs-Cs(Cl)(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.15137,-4.26778,-4.08907,-3.86478,-3.30077,-2.68836,-1.49447],'cal/(mol*K)','+|-',[0.220173,0.244393,0.237259,0.228105,0.205983,0.174922,0.124071]),
        H298 = (36.0634,'kcal/mol','+|-',1.28619),
        S298 = (35.2583,'cal/(mol*K)','+|-',0.679577),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 19,
    label = "Cs-Cs(C)-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.38159,-3.78789,-3.76345,-3.6029,-3.13341,-2.5706,-1.63545],'cal/(mol*K)','+|-',[0.301812,0.335013,0.325234,0.312685,0.282361,0.239782,0.170076]),
        H298 = (31.7878,'kcal/mol','+|-',1.76311),
        S298 = (35.8976,'cal/(mol*K)','+|-',0.93156),
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
    index = 20,
    label = "Cs(Cl)-Cs-Cs(O2)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {5,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.52555,-3.47518,-3.37837,-3.18349,-2.54847,-1.88377,-0.929619],'cal/(mol*K)','+|-',[0.323322,0.35889,0.348413,0.33497,0.302484,0.256871,0.182197]),
        H298 = (36.8381,'kcal/mol','+|-',1.88876),
        S298 = (35.5382,'cal/(mol*K)','+|-',0.997953),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 21,
    label = "Cs(O2)-Cs-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.77014,-3.93057,-3.86798,-3.62304,-2.94074,-2.23523,-1.04506],'cal/(mol*K)','+|-',[0.273175,0.303225,0.294374,0.283016,0.255569,0.21703,0.153938]),
        H298 = (37.7914,'kcal/mol','+|-',1.59581),
        S298 = (35.1628,'cal/(mol*K)','+|-',0.843169),
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
    index = 22,
    label = "Cs-Cs-Cs(Cl)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.6581,-3.6979,-3.55926,-3.37346,-2.91773,-2.3718,-1.39686],'cal/(mol*K)','+|-',[0.220173,0.244393,0.237259,0.228105,0.205983,0.174922,0.124071]),
        H298 = (31.7631,'kcal/mol','+|-',1.28619),
        S298 = (35.1123,'cal/(mol*K)','+|-',0.679577),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 23,
    label = "Cs-Cs(Cl)-Cs(C)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.99355,-4.19733,-4.10001,-3.97226,-3.66135,-3.0477,-1.63799],'cal/(mol*K)','+|-',[0.134366,0.149146,0.144793,0.139206,0.125706,0.10675,0.075717]),
        H298 = (34.0379,'kcal/mol','+|-',0.784927),
        S298 = (37.0119,'cal/(mol*K)','+|-',0.414727),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         14
""",
)

entry(
    index = 24,
    label = "Cs-Cs(Cl)(Cl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.85567,-3.69582,-3.63227,-3.53447,-3.21305,-2.81183,-2.0478],'cal/(mol*K)','+|-',[0.240212,0.266636,0.258853,0.248866,0.22473,0.190842,0.135363]),
        H298 = (32.9281,'kcal/mol','+|-',1.40325),
        S298 = (36.0286,'cal/(mol*K)','+|-',0.741428),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 25,
    label = "Cs-Cs(F)(F)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.30244,-3.76169,-3.26154,-3.02032,-2.59928,-2.13012,-1.34575],'cal/(mol*K)','+|-',[0.239136,0.265442,0.257694,0.247751,0.223724,0.189987,0.134757]),
        H298 = (39.9322,'kcal/mol','+|-',1.39697),
        S298 = (34.743,'cal/(mol*K)','+|-',0.738107),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 26,
    label = "Cs-Cs(F)(F)-Cs(O2)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.04514,-3.90983,-3.56763,-3.23889,-2.54025,-1.80537,-0.5756],'cal/(mol*K)','+|-',[0.219437,0.243576,0.236466,0.227342,0.205294,0.174337,0.123656]),
        H298 = (46.4846,'kcal/mol','+|-',1.28189),
        S298 = (34.854,'cal/(mol*K)','+|-',0.677304),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 27,
    label = "Cs(F)(F)-Cs(C)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.56589,-4.35996,-3.75374,-3.30448,-2.69835,-1.99098,-0.616936],'cal/(mol*K)','+|-',[0.147272,0.163472,0.1587,0.152577,0.13778,0.117004,0.0829898]),
        H298 = (42.0714,'kcal/mol','+|-',0.860322),
        S298 = (35.0479,'cal/(mol*K)','+|-',0.454562),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         15
""",
)

entry(
    index = 28,
    label = "Cs(C)-Cs-Cs(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.23964,-4.093,-3.69758,-3.28763,-2.60253,-1.92992,-0.855233],'cal/(mol*K)','+|-',[0.181855,0.20186,0.195968,0.188407,0.170135,0.144479,0.102478]),
        H298 = (37.0097,'kcal/mol','+|-',1.06235),
        S298 = (34.6716,'cal/(mol*K)','+|-',0.561307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         8
""",
)

entry(
    index = 29,
    label = "Cs-Cs(F)(C)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.33767,-3.87574,-3.35859,-2.9573,-2.29908,-1.63893,-0.460287],'cal/(mol*K)','+|-',[0.18705,0.207627,0.201566,0.193789,0.174995,0.148606,0.105406]),
        H298 = (38.3018,'kcal/mol','+|-',1.0927),
        S298 = (33.4237,'cal/(mol*K)','+|-',0.577341),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 30,
    label = "Cs(F)-Cs-Cs(O2)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {5,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.83503,-3.79758,-3.55506,-3.2624,-2.57112,-1.92649,-0.992282],'cal/(mol*K)','+|-',[0.275417,0.305715,0.29679,0.285339,0.257667,0.218812,0.155202]),
        H298 = (39.3374,'kcal/mol','+|-',1.60891),
        S298 = (34.2231,'cal/(mol*K)','+|-',0.850091),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 31,
    label = "Cs-Cs(C-FFF)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs  u0 p0 c0 {2,S} {4,S}
4 * Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.2275,-2.98663,-2.70268,-2.45094,-1.99535,-1.44947,-0.721708],'cal/(mol*K)','+|-',[0.263734,0.292746,0.2842,0.273235,0.246736,0.20953,0.148618]),
        H298 = (32.5364,'kcal/mol','+|-',1.54066),
        S298 = (34.6529,'cal/(mol*K)','+|-',0.814029),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 32,
    label = "Cs-Cs(F)(O2)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.07853,-4.20829,-3.81304,-3.43611,-2.78529,-2.22948,-1.22419],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (36.5408,'kcal/mol','+|-',2.66044),
        S298 = (34.2158,'cal/(mol*K)','+|-',1.40568),
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
    index = 33,
    label = "Cs(F)-Cs-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.91269,-3.87879,-3.57222,-3.22496,-2.64993,-2.084,-1.23377],'cal/(mol*K)','+|-',[0.185919,0.206371,0.200347,0.192617,0.173937,0.147708,0.104768]),
        H298 = (37.8907,'kcal/mol','+|-',1.08609),
        S298 = (35.879,'cal/(mol*K)','+|-',0.57385),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 34,
    label = "Cs-Cs(C-FF)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4 * Cs  u0 p0 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.02246,-4.07259,-3.85968,-3.51009,-2.76453,-2.10161,-1.39947],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (25.8826,'kcal/mol','+|-',2.66044),
        S298 = (32.7091,'cal/(mol*K)','+|-',1.40568),
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
    index = 35,
    label = "Cs(C-F)-Cs-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.71326,-3.89336,-3.81237,-3.55337,-2.88207,-2.20336,-1.40088],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.7792,'kcal/mol','+|-',2.66044),
        S298 = (33.7955,'cal/(mol*K)','+|-',1.40568),
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
    index = 36,
    label = "oxirene",
    group = 
"""
1   [C,N,S] u0 {2,S} {3,D}
2 * O2s     u0 {1,S} {3,S}
3   [C,N,S] u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283,-1.56,-2.46,-2.83,-3.22,-3.08,-3.04],'cal/(mol*K)'),
        H298 = (80.64,'kcal/mol'),
        S298 = (38.08,'cal/(mol*K)'),
    ),
    shortDesc = """Derived from goldsmith's DFT-QCI library""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "Cyclopropene",
    group = 
"""
1 * [Cs,N]  u0 {2,S} {3,S}
2   [C,N,S] u0 {1,S} {3,D}
3   [C,N,S] u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (55.4702,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopropene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "Cd(O2)-Cs-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74747,-3.10505,-3.36569,-3.06425,-2.60364,-2.18428,-1.2839],'cal/(mol*K)','+|-',[0.557148,0.618437,0.600384,0.577219,0.52124,0.44264,0.313961]),
        H298 = (65.8952,'kcal/mol','+|-',3.25471),
        S298 = (34.9682,'cal/(mol*K)','+|-',1.71967),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 39,
    label = "Cd(C)-Cs-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60932,-2.34278,-2.5936,-2.53323,-2.35844,-2.16522,-1.50474],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (56.2703,'kcal/mol','+|-',1.88121),
        S298 = (36.0338,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 40,
    label = "Cd-Cs-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.996296,-1.61197,-2.00128,-2.16154,-2.3145,-2.35669,-2.23556],'cal/(mol*K)','+|-',[0.329718,0.365989,0.355305,0.341596,0.308468,0.261953,0.185801]),
        H298 = (59.5609,'kcal/mol','+|-',1.92613),
        S298 = (35.3443,'cal/(mol*K)','+|-',1.01769),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 41,
    label = "Cs-Cd-Cd(C-Cl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71264,-2.2885,-2.38199,-2.25652,-2.12958,-2.00687,-1.15857],'cal/(mol*K)','+|-',[0.22771,0.252759,0.245381,0.235913,0.213034,0.180909,0.128318]),
        H298 = (55.5547,'kcal/mol','+|-',1.33022),
        S298 = (35.5797,'cal/(mol*K)','+|-',0.702839),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 42,
    label = "Cs-Cd-Cd(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3 * Cs   u0 p0 c0 {2,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.61,-1.97119,-2.11754,-2.16691,-2.21268,-2.10011,-1.49924],'cal/(mol*K)','+|-',[0.265281,0.294464,0.285868,0.274838,0.248184,0.210759,0.14949]),
        H298 = (54.3009,'kcal/mol','+|-',1.5497),
        S298 = (37.674,'cal/(mol*K)','+|-',0.818806),
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
    index = 43,
    label = "Cs-Cd(Cl)-Cd(O2)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.58943,-2.32604,-2.46095,-2.34619,-2.19063,-1.98781,-1.22261],'cal/(mol*K)','+|-',[0.518896,0.575977,0.559163,0.537589,0.485453,0.412249,0.292405]),
        H298 = (60.3185,'kcal/mol','+|-',3.03125),
        S298 = (34.9765,'cal/(mol*K)','+|-',1.6016),
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
    index = 44,
    label = "Cs(O2)-Cd-Cd(Cl)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   O2s  u0 p2 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54152,-1.04553,-1.51157,-1.41115,-1.45619,-1.3114,-0.659268],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (58.3961,'kcal/mol','+|-',2.66044),
        S298 = (33.8136,'cal/(mol*K)','+|-',1.40568),
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
    index = 45,
    label = "Cs-Cd(Cl)-Cd(C)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.4263,-2.07575,-2.28914,-2.26003,-2.2028,-2.03218,-1.48748],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (56.4373,'kcal/mol','+|-',2.66044),
        S298 = (36.2063,'cal/(mol*K)','+|-',1.40568),
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
    index = 46,
    label = "Cs-Cd(F)-Cd",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cd  u0 p0 c0 {1,D} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7769,-2.09062,-2.18408,-2.2462,-2.19586,-2.10593,-1.92256],'cal/(mol*K)','+|-',[0.32986,0.366146,0.355458,0.341743,0.3086,0.262065,0.185881]),
        H298 = (64.7854,'kcal/mol','+|-',1.92695),
        S298 = (34.7864,'cal/(mol*K)','+|-',1.01813),
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
    index = 47,
    label = "Cd-Cd(F)-Cs(O2)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71539,-1.9978,-2.12822,-1.99029,-1.83344,-1.52027,-0.824703],'cal/(mol*K)','+|-',[0.243774,0.270591,0.262692,0.252556,0.228063,0.193672,0.137371]),
        H298 = (63.1957,'kcal/mol','+|-',1.42406),
        S298 = (35.251,'cal/(mol*K)','+|-',0.752423),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 48,
    label = "Cs-Cd(C)-Cd(F)",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {3,S} {4,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.31271,-2.61483,-2.47365,-2.19093,-1.91286,-1.74028,-0.877724],'cal/(mol*K)','+|-',[0.179894,0.199683,0.193854,0.186374,0.168299,0.142921,0.101373]),
        H298 = (60.7089,'kcal/mol','+|-',1.05089),
        S298 = (36.9438,'cal/(mol*K)','+|-',0.555251),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 49,
    label = "Cd-Cs-Cd(C-FF)",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cs  u0 p0 c0 {1,S} {4,S}
4   Cd  u0 p0 c0 {1,D} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40437,-1.89169,-1.86276,-1.67761,-1.59056,-1.54425,-0.952119],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (54.4794,'kcal/mol','+|-',1.88121),
        S298 = (35.081,'cal/(mol*K)','+|-',0.993964),
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
    index = 50,
    label = "Cd-Cs-Cd(C-F)",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cd  u0 p0 c0 {1,D} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.75938,-2.4421,-2.52045,-2.25238,-1.84703,-1.7791,-1.02996],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (53.8651,'kcal/mol','+|-',2.66044),
        S298 = (35.0668,'cal/(mol*K)','+|-',1.40568),
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
    index = 51,
    label = "Cyclopropene2",
    group = 
"""
1   [Cs,N,O2s,S] u0 {2,S} {3,S}
2 * [C,N,O,S]    u0 {1,S} {3,D}
3   [C,N,O,S]    u0 {1,S} {2,D}
""",
    thermo = 'Cyclopropene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "Cd(C)-Cd-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.64202,-2.83284,-2.77308,-2.68495,-2.54689,-2.29357,-1.32633],'cal/(mol*K)','+|-',[0.198127,0.219922,0.213502,0.205264,0.185358,0.157407,0.111647]),
        H298 = (48.6932,'kcal/mol','+|-',1.1574),
        S298 = (38.98,'cal/(mol*K)','+|-',0.611529),
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
    index = 53,
    label = "Cd-Cs(C-BrBr)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.44747,-2.52024,-2.59483,-2.68521,-2.78152,-2.59857,-1.79992],'cal/(mol*K)','+|-',[0.234662,0.260476,0.252872,0.243115,0.219538,0.186432,0.132235]),
        H298 = (54.2466,'kcal/mol','+|-',1.37083),
        S298 = (38.121,'cal/(mol*K)','+|-',0.724296),
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
    index = 54,
    label = "Cs(C-BrBrBr)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * Cd   u0 p0 c0 {2,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.28196,-1.27592,-1.44957,-1.59138,-1.82723,-1.85289,-1.45842],'cal/(mol*K)','+|-',[0.267477,0.296901,0.288234,0.277113,0.250238,0.212503,0.150727]),
        H298 = (54.3722,'kcal/mol','+|-',1.56253),
        S298 = (38.8836,'cal/(mol*K)','+|-',0.825583),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 55,
    label = "Cd-Cs(C-Br)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7884,-2.80912,-2.85798,-2.845,-2.75403,-2.50684,-1.85876],'cal/(mol*K)','+|-',[0.205787,0.228425,0.221757,0.213201,0.192524,0.163493,0.115964]),
        H298 = (56.821,'kcal/mol','+|-',1.20215),
        S298 = (39.1919,'cal/(mol*K)','+|-',0.635174),
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
    index = 56,
    label = "Cs(C)-Cd(Br)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90325,-1.94378,-2.12885,-2.16209,-2.04409,-1.90146,-1.70456],'cal/(mol*K)','+|-',[0.280658,0.311532,0.302438,0.290769,0.26257,0.222975,0.158155]),
        H298 = (56.9662,'kcal/mol','+|-',1.63953),
        S298 = (38.0658,'cal/(mol*K)','+|-',0.866266),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 57,
    label = "Cd-Cd-Cs(Br)(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.55848,-2.69297,-2.72241,-2.79349,-2.82568,-2.58473,-1.77707],'cal/(mol*K)','+|-',[0.285098,0.31646,0.307222,0.295368,0.266723,0.226503,0.160657]),
        H298 = (56.7628,'kcal/mol','+|-',1.66546),
        S298 = (38.8112,'cal/(mol*K)','+|-',0.87997),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 58,
    label = "Cd-Cd-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77166,-1.8064,-2.00163,-2.18474,-2.42432,-2.44426,-2.00554],'cal/(mol*K)','+|-',[0.346035,0.3841,0.372888,0.3585,0.323733,0.274915,0.194996]),
        H298 = (51.7167,'kcal/mol','+|-',2.02144),
        S298 = (37.3281,'cal/(mol*K)','+|-',1.06805),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 59,
    label = "Cd(O2)-Cs(Br)(Br)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.94727,-4.01056,-4.07164,-3.73265,-3.1816,-2.60726,-1.30119],'cal/(mol*K)','+|-',[0.367649,0.408092,0.396179,0.380893,0.343954,0.292087,0.207175]),
        H298 = (59.2908,'kcal/mol','+|-',2.1477),
        S298 = (37.5656,'cal/(mol*K)','+|-',1.13477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 60,
    label = "Cd-Cd-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.22009,-2.14876,-2.19925,-2.30762,-2.34895,-2.25858,-1.84319],'cal/(mol*K)','+|-',[0.285098,0.31646,0.307222,0.295368,0.266723,0.226503,0.160657]),
        H298 = (54.5942,'kcal/mol','+|-',1.66546),
        S298 = (37.2718,'cal/(mol*K)','+|-',0.87997),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 61,
    label = "Cs(Br)-Cd(C)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.75181,-2.8614,-2.75972,-2.61642,-2.32286,-1.99663,-1.10225],'cal/(mol*K)','+|-',[0.195149,0.216616,0.210293,0.202179,0.182572,0.155041,0.109969]),
        H298 = (51.5921,'kcal/mol','+|-',1.14001),
        S298 = (39.0648,'cal/(mol*K)','+|-',0.602338),
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
    index = 62,
    label = "Cd-Cd(O2)-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   O2s  u0 p2 c0 {2,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3132,-4.10494,-4.06794,-3.71088,-3.04606,-2.38928,-1.07541],'cal/(mol*K)','+|-',[0.35851,0.397948,0.386331,0.371425,0.335404,0.284827,0.202026]),
        H298 = (61.9182,'kcal/mol','+|-',2.09432),
        S298 = (38.7249,'cal/(mol*K)','+|-',1.10656),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 63,
    label = "Cd-Cd-Cs(Br)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79978,-1.64661,-1.61845,-1.65288,-1.84146,-1.82704,-1.50146],'cal/(mol*K)','+|-',[0.327443,0.363463,0.352853,0.339239,0.306339,0.260145,0.184519]),
        H298 = (55.5584,'kcal/mol','+|-',1.91283),
        S298 = (38.3382,'cal/(mol*K)','+|-',1.01067),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 64,
    label = "Cs-Cd-Cd(C-Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cd   u0 p0 c0 {1,D} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.62435,-2.34693,-2.4491,-2.28344,-2.07304,-1.97435,-1.22401],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (53.623,'kcal/mol','+|-',2.66044),
        S298 = (35.0668,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 65,
    label = "Cd-Cs-Cd(C-BrBrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   Cs   u0 p0 c0 {2,S} {4,S}
4 * Cd   u0 p0 c0 {2,D} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.960574,-1.61039,-1.89552,-1.89235,-1.82655,-1.70524,-1.2625],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (53.6735,'kcal/mol','+|-',1.88121),
        S298 = (36.3703,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 66,
    label = "Cd(C-BrBr)-Cd-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cd   u0 p0 c0 {1,D} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79053,-2.36266,-2.5516,-2.49434,-2.30948,-2.1014,-1.30597],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (54.4726,'kcal/mol','+|-',1.88121),
        S298 = (35.8028,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 67,
    label = "Cs(O2)-Cd-Cd(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.510886,-1.31932,-1.83753,-1.69318,-1.66744,-1.47256,-0.787953],'cal/(mol*K)','+|-',[0.329718,0.365989,0.355305,0.341596,0.308468,0.261953,0.185801]),
        H298 = (58.7354,'kcal/mol','+|-',1.92613),
        S298 = (35.6897,'cal/(mol*K)','+|-',1.01769),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 68,
    label = "Cd-Cd-Cs(C-ClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.25148,-2.45846,-2.63389,-2.71109,-2.70154,-2.41438,-1.75697],'cal/(mol*K)','+|-',[0.273395,0.303469,0.294611,0.283243,0.255774,0.217205,0.154062]),
        H298 = (55.5247,'kcal/mol','+|-',1.5971),
        S298 = (36.6774,'cal/(mol*K)','+|-',0.843847),
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
    index = 69,
    label = "Cd-Cd-Cs(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * Cd   u0 p0 c0 {2,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27687,-1.26079,-1.44086,-1.56612,-1.79722,-1.81042,-1.57751],'cal/(mol*K)','+|-',[0.231121,0.256545,0.249056,0.239447,0.216225,0.183619,0.13024]),
        H298 = (55.7681,'kcal/mol','+|-',1.35014),
        S298 = (37.8981,'cal/(mol*K)','+|-',0.713367),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 70,
    label = "Cd-Cs-Cd(Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.77835,-2.06987,-2.28024,-2.29976,-2.20967,-2.05875,-1.82957],'cal/(mol*K)','+|-',[0.192388,0.213552,0.207318,0.199319,0.179989,0.152847,0.108414]),
        H298 = (58.2794,'kcal/mol','+|-',1.12388),
        S298 = (36.3564,'cal/(mol*K)','+|-',0.593817),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         11
""",
)

entry(
    index = 71,
    label = "Cd-Cd(Cl)-Cs(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.28627,-2.332,-2.38648,-2.39666,-2.32164,-2.07584,-1.57132],'cal/(mol*K)','+|-',[0.233749,0.259462,0.251888,0.242169,0.218684,0.185707,0.131721]),
        H298 = (58.0894,'kcal/mol','+|-',1.3655),
        S298 = (38.5596,'cal/(mol*K)','+|-',0.721478),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 72,
    label = "Cd-Cs(Cl)(C)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.40246,-2.23423,-2.16801,-2.19699,-2.34109,-2.12476,-1.35418],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (55.2027,'kcal/mol','+|-',1.88121),
        S298 = (37.6204,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 73,
    label = "Cd-Cd-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.30413,-2.45164,-2.37829,-2.26632,-2.10394,-1.92948,-1.20409],'cal/(mol*K)','+|-',[0.222954,0.24748,0.240255,0.230985,0.208584,0.177131,0.125638]),
        H298 = (53.7757,'kcal/mol','+|-',1.30243),
        S298 = (37.195,'cal/(mol*K)','+|-',0.688159),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 74,
    label = "Cs(Cl)-Cd-Cd(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.26249,-4.00636,-3.9009,-3.60326,-3.01664,-2.40382,-1.07183],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (61.9519,'kcal/mol','+|-',2.66044),
        S298 = (39.0307,'cal/(mol*K)','+|-',1.40568),
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
    index = 75,
    label = "Cd(O2)-Cs(Cl)(Cl)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.42448,-4.21448,-4.23991,-3.93207,-3.31404,-2.63046,-1.0423],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (60.3659,'kcal/mol','+|-',2.66044),
        S298 = (37.0364,'cal/(mol*K)','+|-',1.40568),
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
    index = 76,
    label = "Cs(Cl)(Cl)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.52229,-2.57153,-2.41958,-2.35766,-2.34969,-2.15325,-1.09379],'cal/(mol*K)','+|-',[0.174482,0.193676,0.188022,0.180768,0.163237,0.138621,0.0983233]),
        H298 = (50.8008,'kcal/mol','+|-',1.01928),
        S298 = (37.5881,'cal/(mol*K)','+|-',0.538549),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 77,
    label = "Cd-Cs(Cl)(O2)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.51773,-2.4757,-2.35134,-2.34827,-2.38339,-2.18878,-1.50007],'cal/(mol*K)','+|-',[0.326328,0.362226,0.351652,0.338084,0.305297,0.259259,0.183891]),
        H298 = (57.3784,'kcal/mol','+|-',1.90632),
        S298 = (37.4787,'cal/(mol*K)','+|-',1.00723),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 78,
    label = "Cd-Cd(C)-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {2,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59292,-2.54535,-2.31876,-2.15615,-2.09803,-1.94808,-0.850275],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (50.9835,'kcal/mol','+|-',1.536),
        S298 = (38.8849,'cal/(mol*K)','+|-',0.811568),
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
    index = 79,
    label = "Cs(C-Cl)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.58787,-2.4677,-2.53853,-2.5626,-2.33242,-2.07104,-1.6824],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (54.1982,'kcal/mol','+|-',2.66044),
        S298 = (37.8491,'cal/(mol*K)','+|-',1.40568),
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
    index = 80,
    label = "Cd-Cs(F)(C)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {3,D}
3 * Cd  u0 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91613,-2.50274,-2.08291,-1.83867,-1.64032,-1.28266,-0.536269],'cal/(mol*K)','+|-',[0.169612,0.18827,0.182774,0.175722,0.158681,0.134752,0.0955788]),
        H298 = (60.6185,'kcal/mol','+|-',0.990827),
        S298 = (35.29,'cal/(mol*K)','+|-',0.523517),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         11
""",
)

entry(
    index = 81,
    label = "Cd(C)-Cd-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {5,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.59075,-2.34929,-1.95026,-1.67795,-1.57645,-1.46502,-0.47255],'cal/(mol*K)','+|-',[0.22771,0.252759,0.245381,0.235913,0.213034,0.180909,0.128318]),
        H298 = (50.2011,'kcal/mol','+|-',1.33022),
        S298 = (38.4611,'cal/(mol*K)','+|-',0.702839),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 82,
    label = "Cd-Cd(C)-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91637,-2.7106,-2.18118,-1.86225,-1.69534,-1.48258,-0.346737],'cal/(mol*K)','+|-',[0.198008,0.219789,0.213374,0.205141,0.185246,0.157312,0.11158]),
        H298 = (54.8856,'kcal/mol','+|-',1.15671),
        S298 = (37.274,'cal/(mol*K)','+|-',0.611161),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 83,
    label = "Cd-Cs(C-FFF)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cd  u0 p0 c0 {2,S} {4,D}
4 * Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.63962,-2.04245,-1.72674,-1.59771,-1.32418,-1.07978,-0.819224],'cal/(mol*K)','+|-',[0.267215,0.29661,0.287952,0.276842,0.249994,0.212296,0.15058]),
        H298 = (59.8186,'kcal/mol','+|-',1.561),
        S298 = (37.5484,'cal/(mol*K)','+|-',0.824775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 84,
    label = "Cd-Cd-Cs(C-FF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4 * Cd  u0 p0 c0 {1,S} {3,D}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.33109,-2.9934,-2.72248,-2.52631,-2.15976,-1.79548,-1.23935],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (57.081,'kcal/mol','+|-',1.88121),
        S298 = (36.8635,'cal/(mol*K)','+|-',0.993964),
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
    index = 85,
    label = "Cs(F)(O2)-Cd-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.56801,-2.49656,-2.13687,-2.01257,-1.98119,-1.7623,-1.12555],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (57.3163,'kcal/mol','+|-',2.66044),
        S298 = (36.8857,'cal/(mol*K)','+|-',1.40568),
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
    index = 86,
    label = "Cd-Cs(F)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97533,-1.73476,-1.59444,-1.63414,-1.72565,-1.70361,-1.39181],'cal/(mol*K)','+|-',[0.28467,0.315986,0.306762,0.294926,0.266324,0.226163,0.160416]),
        H298 = (53.9424,'kcal/mol','+|-',1.66297),
        S298 = (35.6783,'cal/(mol*K)','+|-',0.878651),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 87,
    label = "Cs(F)(F)-Cd-Cd(O2)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.39807,-3.7719,-3.3501,-2.92453,-2.35559,-1.79279,-0.509579],'cal/(mol*K)','+|-',[0.358902,0.398383,0.386754,0.371831,0.335771,0.285138,0.202247]),
        H298 = (61.3357,'kcal/mol','+|-',2.09661),
        S298 = (35.3317,'cal/(mol*K)','+|-',1.10777),
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
    index = 88,
    label = "Cs(F)-Cd-Cd(O2)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   O2s u0 p2 c0 {2,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9677,-3.46255,-3.24279,-2.88155,-2.34694,-1.83885,-0.676982],'cal/(mol*K)','+|-',[0.347882,0.386151,0.374879,0.360415,0.325461,0.276383,0.196037]),
        H298 = (59.801,'kcal/mol','+|-',2.03223),
        S298 = (37.5842,'cal/(mol*K)','+|-',1.07376),
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
    index = 89,
    label = "Cd-Cd-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39315,-2.09321,-1.67769,-1.60863,-1.67201,-1.6118,-1.21539],'cal/(mol*K)','+|-',[0.34531,0.383295,0.372107,0.357749,0.323055,0.274339,0.194587]),
        H298 = (53.4701,'kcal/mol','+|-',2.01721),
        S298 = (35.0844,'cal/(mol*K)','+|-',1.06582),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 90,
    label = "Cd(C-FF)-Cd-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4 * Cd  u0 p0 c0 {1,D} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.04919,-3.43317,-3.72416,-3.71575,-3.91918,-3.67213,-3.09083],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (84.2623,'kcal/mol','+|-',1.88121),
        S298 = (35.0832,'cal/(mol*K)','+|-',0.993964),
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
    index = 91,
    label = "Cd-Cd-Cs(C-F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.49024,-3.29469,-3.03779,-2.75162,-2.27289,-1.92047,-1.34778],'cal/(mol*K)','+|-',[0.267215,0.29661,0.287952,0.276842,0.249994,0.212296,0.15058]),
        H298 = (61.9432,'kcal/mol','+|-',1.561),
        S298 = (38.4058,'cal/(mol*K)','+|-',0.824775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 92,
    label = "Cd-Cd(F)-Cs(C)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.6101,-2.47456,-2.48036,-2.38523,-1.9461,-1.63288,-1.41861],'cal/(mol*K)','+|-',[0.32986,0.366146,0.355458,0.341743,0.3086,0.262065,0.185881]),
        H298 = (63.9604,'kcal/mol','+|-',1.92695),
        S298 = (38.252,'cal/(mol*K)','+|-',1.01813),
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
    index = 93,
    label = "Cd(F)-Cd(O2)-Cs",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {3,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.0046,-3.05815,-3.13524,-2.85595,-2.37644,-1.96207,-1.06874],'cal/(mol*K)','+|-',[0.528399,0.586526,0.569404,0.547435,0.494344,0.419799,0.297761]),
        H298 = (68.553,'kcal/mol','+|-',3.08677),
        S298 = (35.4087,'cal/(mol*K)','+|-',1.63093),
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
    index = 94,
    label = "Cyclopropadiene",
    group = 
"""
1 * [C,N,O,S]   u0 {2,S} {3,D}
2   [C,N,O,S]   u0 {1,S} {3,D}
3   [Cdd,N,O,S] u0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (73.04,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cyclopropadiene2",
    group = 
"""
1   [C,N,O,S]   u0 {2,S} {3,D}
2   [C,N,O,S]   u0 {1,S} {3,D}
3 * [Cdd,N,O,S] u0 {1,D} {2,D}
""",
    thermo = 'Cyclopropadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "Cyclopropyne",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22,1.515,0.554,-0.319,-1.215,-1.31,-2.439],'cal/(mol*K)'),
        H298 = (111.641,'kcal/mol'),
        S298 = (37.345,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to M06 calculations
""",
)

entry(
    index = 97,
    label = "Cyclopropatriene",
    group = 
"""
1 * [Cdd,N,O,S] u0 {2,D} {3,D}
2   [Cdd,N,O,S] u0 {1,D} {3,D}
3   [Cdd,N,O,S] u0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (78,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "Ethylene_oxide",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.891,-2.459,-2.221,-1.969,-1.965,-1.759,2.564],'cal/(mol*K)'),
        H298 = (26.82,'kcal/mol'),
        S298 = (31.1767,'cal/(mol*K)'),
    ),
    shortDesc = """CY/C2O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "O2s-Cs(Br)-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {5,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.75932,-4.9058,-5.02996,-4.86447,-4.24457,-3.68335,-1.84812],'cal/(mol*K)','+|-',[0.323596,0.359193,0.348708,0.335253,0.30274,0.257088,0.182351]),
        H298 = (29.6973,'kcal/mol','+|-',1.89036),
        S298 = (36.4934,'cal/(mol*K)','+|-',0.998796),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 100,
    label = "O2s-Cs(Br)(Br)-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.21731,-4.49047,-4.68044,-4.48237,-3.88917,-3.42412,-1.74163],'cal/(mol*K)','+|-',[0.328062,0.36415,0.35352,0.33988,0.306918,0.260636,0.184868]),
        H298 = (28.8544,'kcal/mol','+|-',1.91645),
        S298 = (35.8969,'cal/(mol*K)','+|-',1.01258),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 101,
    label = "O2s-Cs(C)-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42251,-5.06851,-5.20007,-5.19397,-4.84042,-4.24119,-2.45705],'cal/(mol*K)','+|-',[0.196186,0.217767,0.211411,0.203253,0.183542,0.155865,0.110554]),
        H298 = (28.8101,'kcal/mol','+|-',1.14607),
        S298 = (39.064,'cal/(mol*K)','+|-',0.605539),
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
    index = 102,
    label = "O2s-Cs(C-BrBrBr)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {2,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.77591,-4.17169,-4.28913,-4.35616,-4.20336,-3.7346,-2.12066],'cal/(mol*K)','+|-',[0.228264,0.253374,0.245978,0.236487,0.213552,0.18135,0.12863]),
        H298 = (31.0288,'kcal/mol','+|-',1.33346),
        S298 = (38.4967,'cal/(mol*K)','+|-',0.704549),
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
    index = 103,
    label = "O2s-Cs(Br)(C)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.25822,-5.8972,-5.89679,-5.87231,-5.55177,-4.86388,-2.78238],'cal/(mol*K)','+|-',[0.188623,0.209372,0.203261,0.195418,0.176466,0.149856,0.106292]),
        H298 = (30.1474,'kcal/mol','+|-',1.10188),
        S298 = (39.7306,'cal/(mol*K)','+|-',0.582195),
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
    index = 104,
    label = "O2s-Cs-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.68614,-4.83989,-4.81289,-4.86313,-4.65191,-4.18353,-2.82766],'cal/(mol*K)','+|-',[0.323596,0.359193,0.348708,0.335253,0.30274,0.257088,0.182351]),
        H298 = (28.047,'kcal/mol','+|-',1.89036),
        S298 = (38.984,'cal/(mol*K)','+|-',0.998796),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 105,
    label = "O2s-Cs-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.33292,-4.30445,-4.35833,-4.39436,-4.23399,-3.87595,-2.6577],'cal/(mol*K)','+|-',[0.28202,0.313044,0.303906,0.29218,0.263844,0.224058,0.158923]),
        H298 = (26.9946,'kcal/mol','+|-',1.64749),
        S298 = (37.6395,'cal/(mol*K)','+|-',0.870472),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 106,
    label = "Cs(C)-Cs(Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9554,-5.44328,-5.4933,-5.41944,-4.91085,-4.1748,-2.33253],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (27.1485,'kcal/mol','+|-',1.536),
        S298 = (38.4268,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 107,
    label = "Cs-Cs(Br)(O2)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51158,-5.32825,-5.02722,-4.86354,-4.36695,-3.71168,-2.171],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (29.7242,'kcal/mol','+|-',2.66044),
        S298 = (36.2967,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 108,
    label = "Cs(C-BrBr)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.33303,-4.55663,-4.53851,-4.38457,-3.8603,-3.35546,-1.88248],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (25.7897,'kcal/mol','+|-',2.66044),
        S298 = (34.6862,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 109,
    label = "Cs(C-Br)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.48702,-4.62326,-4.62132,-4.47528,-3.85742,-3.17032,-1.93272],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (26.6106,'kcal/mol','+|-',2.66044),
        S298 = (35.0215,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 110,
    label = "Cs(C-Cl)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31371,-5.65785,-5.55705,-5.46734,-5.01293,-4.24764,-2.29702],'cal/(mol*K)','+|-',[0.204924,0.227467,0.220827,0.212307,0.191717,0.162807,0.115478]),
        H298 = (29.3324,'kcal/mol','+|-',1.19711),
        S298 = (37.9918,'cal/(mol*K)','+|-',0.63251),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 111,
    label = "O2s-Cs-Cs(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {2,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.69981,-3.97267,-4.14623,-4.20363,-3.99008,-3.53336,-2.16186],'cal/(mol*K)','+|-',[0.203997,0.226438,0.219828,0.211346,0.19085,0.16207,0.114955]),
        H298 = (31.7667,'kcal/mol','+|-',1.1917),
        S298 = (37.8258,'cal/(mol*K)','+|-',0.629648),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 112,
    label = "O2s-Cs(C-ClCl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.86191,-5.24477,-5.21321,-5.262,-5.05802,-4.3779,-2.35098],'cal/(mol*K)','+|-',[0.204924,0.227467,0.220827,0.212307,0.191717,0.162807,0.115478]),
        H298 = (29.2242,'kcal/mol','+|-',1.19711),
        S298 = (37.5825,'cal/(mol*K)','+|-',0.63251),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 113,
    label = "Cs-O2s-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.59297,-4.77901,-4.75123,-4.7785,-4.52372,-4.06277,-2.7839],'cal/(mol*K)','+|-',[0.323322,0.35889,0.348413,0.33497,0.302484,0.256871,0.182197]),
        H298 = (27.5942,'kcal/mol','+|-',1.88876),
        S298 = (38.5369,'cal/(mol*K)','+|-',0.997953),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 114,
    label = "Cs(O2)-O2s-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.01363,-4.13116,-4.39999,-4.27008,-3.70314,-3.23899,-1.59732],'cal/(mol*K)','+|-',[0.325293,0.361077,0.350536,0.337011,0.304328,0.258437,0.183307]),
        H298 = (28.7517,'kcal/mol','+|-',1.90027),
        S298 = (35.3923,'cal/(mol*K)','+|-',1.00403),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 115,
    label = "Cs-O2s-Cs(Cl)(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.91293,-5.20607,-5.12128,-4.97698,-4.39692,-3.69978,-2.10863],'cal/(mol*K)','+|-',[0.323322,0.35889,0.348413,0.33497,0.302484,0.256871,0.182197]),
        H298 = (29.5382,'kcal/mol','+|-',1.88876),
        S298 = (36.7267,'cal/(mol*K)','+|-',0.997953),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 116,
    label = "Cs(Cl)-O2s-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42317,-4.20626,-4.32826,-4.04672,-3.29719,-2.93182,-1.17206],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (29.7051,'kcal/mol','+|-',2.66044),
        S298 = (34.0754,'cal/(mol*K)','+|-',1.40568),
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
    index = 117,
    label = "Cs(Cl)-O2s-Cs(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {5,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.3685,-4.96838,-5.09636,-5.0952,-4.63398,-3.96602,-2.30177],'cal/(mol*K)','+|-',[0.323322,0.35889,0.348413,0.33497,0.302484,0.256871,0.182197]),
        H298 = (25.8668,'kcal/mol','+|-',1.88876),
        S298 = (39.2073,'cal/(mol*K)','+|-',0.997953),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 118,
    label = "Cs(Cl)(Cl)-O2s-Cs(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.90752,-4.50572,-4.62055,-4.61444,-4.22709,-3.66541,-2.18848],'cal/(mol*K)','+|-',[0.325293,0.361077,0.350536,0.337011,0.304328,0.258437,0.183307]),
        H298 = (25.1902,'kcal/mol','+|-',1.90027),
        S298 = (38.5653,'cal/(mol*K)','+|-',1.00403),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 119,
    label = "Cs-O2s-Cs(Cl)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.8166,-4.9513,-4.79164,-4.67675,-4.28911,-3.72247,-2.16906],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.8163,'kcal/mol','+|-',2.66044),
        S298 = (38.0391,'cal/(mol*K)','+|-',1.40568),
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
    index = 120,
    label = "Cs(Cl)(Cl)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08003,-4.12461,-4.18808,-4.24773,-4.06972,-3.72882,-2.6976],'cal/(mol*K)','+|-',[0.273175,0.303225,0.294374,0.283016,0.255569,0.21703,0.153938]),
        H298 = (26.6167,'kcal/mol','+|-',1.59581),
        S298 = (37.3215,'cal/(mol*K)','+|-',0.843169),
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
    index = 121,
    label = "O2s-Cs-Cs(C-FFF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs  u0 p0 c0 {2,S} {4,S}
4 * O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.06632,-4.02465,-3.78968,-3.64913,-3.24136,-2.62909,-1.18425],'cal/(mol*K)','+|-',[0.204041,0.226486,0.219875,0.211391,0.19089,0.162105,0.11498]),
        H298 = (35.4568,'kcal/mol','+|-',1.19195),
        S298 = (36.4216,'cal/(mol*K)','+|-',0.629783),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 122,
    label = "Cs(F)(O2)-O2s-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5784,-4.51427,-4.1561,-3.93076,-3.35918,-2.74277,-1.39355],'cal/(mol*K)','+|-',[0.26555,0.294762,0.286157,0.275116,0.248435,0.210972,0.149641]),
        H298 = (30.663,'kcal/mol','+|-',1.55127),
        S298 = (35.0006,'cal/(mol*K)','+|-',0.819635),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 123,
    label = "Cs(O2)-O2s-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {5,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.97559,-3.86517,-4.02595,-3.69305,-2.89021,-2.55106,-1.01184],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (31.6244,'kcal/mol','+|-',2.66044),
        S298 = (33.3543,'cal/(mol*K)','+|-',1.40568),
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
    index = 124,
    label = "Cs(O2)-Cs(F)(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.93677,-3.57788,-3.59467,-3.28808,-2.54779,-2.22587,-0.591049],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (34.4708,'kcal/mol','+|-',2.66044),
        S298 = (32.263,'cal/(mol*K)','+|-',1.40568),
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
    index = 125,
    label = "O2s-Cs-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.00506,-3.95103,-3.78643,-3.80843,-3.601,-3.22192,-2.1629],'cal/(mol*K)','+|-',[0.269728,0.299399,0.29066,0.279445,0.252344,0.214292,0.151996]),
        H298 = (30.3109,'kcal/mol','+|-',1.57568),
        S298 = (35.5399,'cal/(mol*K)','+|-',0.832531),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 126,
    label = "Cs(C)-Cs(F)(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.74574,-5.04704,-4.77639,-4.55446,-4.13156,-3.41787,-1.52863],'cal/(mol*K)','+|-',[0.192474,0.213648,0.207411,0.199408,0.180069,0.152916,0.108462]),
        H298 = (33.9421,'kcal/mol','+|-',1.12438),
        S298 = (36.8472,'cal/(mol*K)','+|-',0.594083),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 127,
    label = "Cs(F)(C)-Cs-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.00521,-5.40251,-5.21853,-5.00898,-4.5895,-3.89195,-2.00485],'cal/(mol*K)','+|-',[0.188448,0.209178,0.203072,0.195237,0.176303,0.149717,0.106193]),
        H298 = (32.4383,'kcal/mol','+|-',1.10086),
        S298 = (37.8012,'cal/(mol*K)','+|-',0.581656),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 128,
    label = "O2s-Cs(F)-Cs(C)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.49474,-4.82375,-4.81327,-4.64357,-4.05844,-3.35609,-1.74729],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (29.7742,'kcal/mol','+|-',1.536),
        S298 = (37.2525,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 129,
    label = "Cs-Cs(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.90886,-4.10716,-4.11243,-4.17118,-4.02744,-3.65819,-2.59825],'cal/(mol*K)','+|-',[0.323494,0.35908,0.348598,0.335148,0.302645,0.257007,0.182294]),
        H298 = (28.5172,'kcal/mol','+|-',1.88976),
        S298 = (37.571,'cal/(mol*K)','+|-',0.998482),
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
    index = 130,
    label = "Cs(C-F)-Cs-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.77503,-4.71481,-4.49418,-4.19552,-3.41452,-2.65501,-1.49702],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.6674,'kcal/mol','+|-',2.66044),
        S298 = (33.8319,'cal/(mol*K)','+|-',1.40568),
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
    index = 131,
    label = "Cs(C-FF)-Cs-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.79857,-4.66732,-4.45215,-4.15705,-3.36962,-2.59604,-1.39573],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.095,'kcal/mol','+|-',2.66044),
        S298 = (33.743,'cal/(mol*K)','+|-',1.40568),
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
    index = 132,
    label = "dioxirane",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   O2s    u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.099,-3.194,-3.095,-3.038,-3.281,-3.818,-1.346],'cal/(mol*K)'),
        H298 = (25.1977,'kcal/mol'),
        S298 = (32.3877,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "O2s-O2s-Cs(Br)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.22429,-6.39554,-6.76488,-6.93864,-6.99263,-6.85729,-4.33579],'cal/(mol*K)','+|-',[0.22771,0.252759,0.245381,0.235913,0.213034,0.180909,0.128318]),
        H298 = (27.9689,'kcal/mol','+|-',1.33022),
        S298 = (39.117,'cal/(mol*K)','+|-',0.702839),
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
    index = 134,
    label = "Cs(C-BrBr)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.1118,-4.94922,-5.61548,-5.50755,-5.21746,-5.49693,-3.09215],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (29.6345,'kcal/mol','+|-',2.66044),
        S298 = (34.6488,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 135,
    label = "Cs(C-BrBrBr)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {2,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.85739,-3.45795,-4.23466,-4.29671,-4.26718,-4.70892,-2.71739],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (29.0544,'kcal/mol','+|-',2.66044),
        S298 = (34.2845,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 136,
    label = "O2s-Cs(C-Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.36708,-5.1987,-5.72423,-5.46858,-5.11719,-5.36095,-3.07805],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.4751,'kcal/mol','+|-',2.66044),
        S298 = (35.2035,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 137,
    label = "O2s-Cs(Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.24478,-6.43615,-6.58675,-6.49976,-6.25939,-6.2389,-4.47887],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (26.9905,'kcal/mol','+|-',2.66044),
        S298 = (38.2125,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 138,
    label = "O2s-O2s-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.84871,-4.46413,-4.85546,-4.95675,-5.06965,-5.38406,-4.16152],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (25.7264,'kcal/mol','+|-',2.66044),
        S298 = (35.7353,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 139,
    label = "O2s-Cs(C-ClClCl)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {2,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.35047,-4.39576,-5.10277,-5.1644,-5.12065,-5.36835,-3.53375],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (31.4858,'kcal/mol','+|-',1.88121),
        S298 = (36.1131,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 140,
    label = "O2s-O2s-Cs(C-ClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.66439,-5.71544,-6.23671,-6.26204,-6.12279,-6.10514,-3.67642],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (30.0576,'kcal/mol','+|-',1.88121),
        S298 = (36.1477,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 141,
    label = "O2s-Cs(Cl)(C)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.06485,-6.33464,-6.71856,-6.7774,-6.58569,-6.38398,-4.08131],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (25.4344,'kcal/mol','+|-',1.88121),
        S298 = (38.9037,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 142,
    label = "Cs(Cl)(Cl)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.37836,-5.00231,-5.22174,-5.38419,-5.51067,-5.72649,-4.29323],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (24.5128,'kcal/mol','+|-',2.66044),
        S298 = (36.0216,'cal/(mol*K)','+|-',1.40568),
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
    index = 143,
    label = "O2s-O2s-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.14641,-6.44421,-6.53697,-6.33153,-5.97608,-5.90471,-4.22769],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (26.0955,'kcal/mol','+|-',2.66044),
        S298 = (37.6614,'cal/(mol*K)','+|-',1.40568),
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
    index = 144,
    label = "Cs(C-Cl)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.37313,-5.17795,-5.66064,-5.37769,-5.01112,-5.21031,-2.94206],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.8115,'kcal/mol','+|-',2.66044),
        S298 = (34.9159,'cal/(mol*K)','+|-',1.40568),
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
    index = 145,
    label = "O2s-O2s-Cs(C-F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.98912,-5.75366,-5.92525,-5.68354,-5.28596,-5.21828,-2.98357],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (28.9265,'kcal/mol','+|-',1.88121),
        S298 = (36.1193,'cal/(mol*K)','+|-',0.993964),
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
    index = 146,
    label = "O2s-O2s-Cs(C-FF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.30912,-6.00308,-5.95972,-5.59745,-5.23081,-5.21599,-2.85667],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (32.1047,'kcal/mol','+|-',1.88121),
        S298 = (35.0637,'cal/(mol*K)','+|-',0.993964),
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
    index = 147,
    label = "Cs(C-FFF)-O2s-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s u0 p2 c0 {2,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.06556,-4.52852,-4.65121,-4.52565,-4.29507,-4.39523,-2.44385],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (34.8284,'kcal/mol','+|-',1.88121),
        S298 = (34.8377,'cal/(mol*K)','+|-',0.993964),
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
    index = 148,
    label = "O2s-O2s-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {3,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.49653,-5.32523,-5.37649,-5.30891,-5.18726,-5.2635,-3.81192],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (25.5765,'kcal/mol','+|-',2.66044),
        S298 = (36.3776,'cal/(mol*K)','+|-',1.40568),
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
    index = 149,
    label = "O2s-O2s-Cs(F)(C)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.66115,-5.52713,-5.5801,-5.51012,-5.28611,-5.22869,-3.3767],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (21.3599,'kcal/mol','+|-',2.66044),
        S298 = (36.6592,'cal/(mol*K)','+|-',1.40568),
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
    index = 150,
    label = "O2s-Cs(F)(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.94086,-4.85142,-4.93556,-4.8981,-4.91401,-5.13281,-3.90475],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (27.6567,'kcal/mol','+|-',2.66044),
        S298 = (35.3984,'cal/(mol*K)','+|-',1.40568),
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
    index = 151,
    label = "2(co)oxirane",
    group = 
"""
1   [CO,CS]  u0 {2,S} {3,S}
2 * [O2s,S]  u0 {1,S} {3,S}
3   [Cs,N,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147,-1.715,-2.067,-2.254,-2.546,-2.592,-1.488],'cal/(mol*K)'),
        H298 = (40.7699,'kcal/mol'),
        S298 = (34.529,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "O2s-CO(O2d)-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   CO   u0 p0 c0 {1,S} {3,S} {5,D}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09495,-2.03731,-2.48122,-3.0806,-3.94116,-4.27668,-4.21667],'cal/(mol*K)','+|-',[0.648007,0.719291,0.698294,0.671351,0.606243,0.514825,0.365162]),
        H298 = (46.4946,'kcal/mol','+|-',3.78548),
        S298 = (37.1453,'cal/(mol*K)','+|-',2.00011),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 153,
    label = "CO(O2d)-O2s-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   CO   u0 p0 c0 {1,S} {3,S} {6,D}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.74335,-1.78721,-2.31958,-2.92224,-3.83749,-4.24058,-4.11949],'cal/(mol*K)','+|-',[0.788605,0.875356,0.849803,0.817015,0.73778,0.626526,0.444391]),
        H298 = (48.8238,'kcal/mol','+|-',4.60682),
        S298 = (36.3403,'cal/(mol*K)','+|-',2.43407),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 154,
    label = "cyclopropanedione",
    group = 
"""
1   [CO,CS]      u0 {2,S} {3,S}
2 * [CO,CS]      u0 {1,S} {3,S}
3   [Cs,N,O2s,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85,1.69,0.674,-0.137,-1.157,-2.068,0.878],'cal/(mol*K)'),
        H298 = (67.2975,'kcal/mol'),
        S298 = (38.9107,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "cyclopropenone",
    group = 
"""
1   [C,N,O,S] u0 {2,S} {3,D}
2 * [CO,CS]   u0 {1,S} {3,S}
3   [C,N,O,S] u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.734,-1.275,-1.673,-1.861,-2.134,-2.557,-1.78],'cal/(mol*K)'),
        H298 = (56.774,'kcal/mol'),
        S298 = (35.6157,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "Cd(Br)-CO(O2d)-Cd",
    group = 
"""
1 * CO   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   O2d  u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.551594,-0.0443182,-0.386512,-0.72685,-1.1855,-1.55523,-1.39612],'cal/(mol*K)','+|-',[1.02814,1.14124,1.10792,1.06517,0.961873,0.816827,0.57937]),
        H298 = (52.8407,'kcal/mol','+|-',6.00609),
        S298 = (32.6995,'cal/(mol*K)','+|-',3.1734),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 157,
    label = "Cd-Cd(Cl)-CO(O2d)",
    group = 
"""
1 * CO   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {2,S}
5   O2d  u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.773681,-0.104589,-0.0994121,-0.441021,-1.15178,-1.64797,-1.26962],'cal/(mol*K)','+|-',[1.02904,1.14223,1.10889,1.06611,0.962715,0.817542,0.579877]),
        H298 = (53.7694,'kcal/mol','+|-',6.01135),
        S298 = (32.7334,'cal/(mol*K)','+|-',3.17618),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 158,
    label = "CO(O2d)-Cd-Cd(F)",
    group = 
"""
1 * CO  u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   O2d u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.9418,-0.499242,-0.396104,-0.614257,-1.21425,-1.69433,-1.36067],'cal/(mol*K)','+|-',[1.02832,1.14144,1.10812,1.06536,0.962043,0.816971,0.579472]),
        H298 = (58.7252,'kcal/mol','+|-',6.00715),
        S298 = (32.2454,'cal/(mol*K)','+|-',3.17396),
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
    index = 159,
    label = "thiirane",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.02,-2.54,-2.13,-1.81,-1.49,-1.26,-0.96],'cal/(mol*K)'),
        H298 = (17.82,'kcal/mol'),
        S298 = (28.57,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "dithiirane",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.26,-6.35,-5.37,-4.63,-3.67,-3.08,-2.21],'cal/(mol*K)'),
        H298 = (21.37,'kcal/mol'),
        S298 = (31.73,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "trithiirane",
    group = 
"""
1 * S u0 {2,S} {3,S}
2   S u0 {1,S} {3,S}
3   S u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.97,-6.66,-6.4,-6.29,-6.1,-5.72,-4.28],'cal/(mol*K)'),
        H298 = (24.72,'kcal/mol'),
        S298 = (34.89,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "thiirene",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   [C,N] u0 {1,S} {3,D}
3   [C,N] u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-3.8,-6.26,-8.36,-11.65,-14.12,-18.01],'cal/(mol*K)'),
        H298 = (52.44,'kcal/mol'),
        S298 = (34.28,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "Ethyleneimine",
    group = 
"""
1 * N        u0 {2,S} {3,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (27.7,'kcal/mol'),
        S298 = (31.6,'cal/(mol*K)'),
    ),
    shortDesc = """Ethyleneimine ring BENSON (Aziridine)""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "Methylene_cyclopropane",
    group = 
"""
1 * [Cd,N] u0 {2,S} {3,S} {4,D}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
4   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1,-2.121,-2.081,-2.005,-1.98,-1.903,-1.541],'cal/(mol*K)'),
        H298 = (40.92,'kcal/mol'),
        S298 = (31.4507,'cal/(mol*K)'),
    ),
    shortDesc = """Methylene cyclopropane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "Cs-Cd(Cd)-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.96396,-3.12197,-3.14312,-3.02044,-2.7614,-2.45799,-1.5377],'cal/(mol*K)','+|-',[0.212663,0.236056,0.229166,0.220324,0.198957,0.168955,0.119839]),
        H298 = (41.1108,'kcal/mol','+|-',1.24232),
        S298 = (36.1562,'cal/(mol*K)','+|-',0.656395),
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
    index = 166,
    label = "Cs-Cd(Cd-BrBr)-Cs",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.35358,-2.36837,-2.42145,-2.30328,-2.15183,-1.95945,-1.44851],'cal/(mol*K)','+|-',[0.323596,0.359193,0.348708,0.335253,0.30274,0.257088,0.182351]),
        H298 = (39.6167,'kcal/mol','+|-',1.89036),
        S298 = (36.0486,'cal/(mol*K)','+|-',0.998796),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 167,
    label = "Cd(Cd-Br)-Cs-Cs",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.85259,-2.93631,-2.94791,-2.84408,-2.55852,-2.20872,-1.47324],'cal/(mol*K)','+|-',[0.263789,0.292808,0.28426,0.273292,0.246788,0.209574,0.148649]),
        H298 = (42.1965,'kcal/mol','+|-',1.54099),
        S298 = (36.2627,'cal/(mol*K)','+|-',0.814201),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 168,
    label = "Cs-Cd(Cd)-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {2,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.53104,-3.41322,-3.26698,-3.16739,-2.7833,-2.34882,-1.29809],'cal/(mol*K)','+|-',[0.323596,0.359193,0.348708,0.335253,0.30274,0.257088,0.182351]),
        H298 = (42.4164,'kcal/mol','+|-',1.89036),
        S298 = (37.4299,'cal/(mol*K)','+|-',0.998796),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 169,
    label = "Cs-Cd(Cd)-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cd   u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.80328,-2.78872,-2.73223,-2.67995,-2.52387,-2.26454,-1.3027],'cal/(mol*K)','+|-',[0.188154,0.208851,0.202755,0.194932,0.176027,0.149483,0.106027]),
        H298 = (42.6115,'kcal/mol','+|-',1.09914),
        S298 = (37.9144,'cal/(mol*K)','+|-',0.580747),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 170,
    label = "Cs-Cs(Cl)(Cl)-Cd(Cd)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.04198,-3.01201,-2.94996,-2.87494,-2.66386,-2.35785,-1.21034],'cal/(mol*K)','+|-',[0.183472,0.203655,0.19771,0.190082,0.171648,0.145764,0.103389]),
        H298 = (42.3615,'kcal/mol','+|-',1.0718),
        S298 = (36.2256,'cal/(mol*K)','+|-',0.566298),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         7
""",
)

entry(
    index = 171,
    label = "Cs-Cd(Cd-ClCl)-Cs",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31295,-1.73567,-2.16028,-2.20617,-2.16871,-2.03083,-1.92744],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (37.9634,'kcal/mol','+|-',2.66044),
        S298 = (33.6381,'cal/(mol*K)','+|-',1.40568),
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
    index = 172,
    label = "Cs-Cs-Cd(Cd-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9767,-2.25254,-2.44197,-2.4282,-2.24715,-2.02974,-1.83559],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (39.5029,'kcal/mol','+|-',2.66044),
        S298 = (33.496,'cal/(mol*K)','+|-',1.40568),
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
    index = 173,
    label = "Cs-Cs(F)(F)-Cd(Cd)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cd  u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.06148,-2.82861,-2.46417,-2.29955,-2.12668,-1.85204,-0.743525],'cal/(mol*K)','+|-',[0.170024,0.188727,0.183218,0.176149,0.159066,0.135079,0.0958109]),
        H298 = (50.2845,'kcal/mol','+|-',0.993233),
        S298 = (36.1016,'cal/(mol*K)','+|-',0.524788),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         8
""",
)

entry(
    index = 174,
    label = "Cd(Cd-F)-Cs-Cs",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.73579,-2.79082,-2.71305,-2.54631,-2.27025,-1.98678,-1.28684],'cal/(mol*K)','+|-',[0.263734,0.292746,0.2842,0.273235,0.246736,0.20953,0.148618]),
        H298 = (43.5228,'kcal/mol','+|-',1.54066),
        S298 = (35.8901,'cal/(mol*K)','+|-',0.814029),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 175,
    label = "Cs-Cd(Cd-FF)-Cs",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53453,-2.51598,-2.39091,-2.22435,-2.11264,-1.9502,-1.20737],'cal/(mol*K)','+|-',[0.263734,0.292746,0.2842,0.273235,0.246736,0.20953,0.148618]),
        H298 = (42.8342,'kcal/mol','+|-',1.54066),
        S298 = (36.3872,'cal/(mol*K)','+|-',0.814029),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 176,
    label = "Cd(Cd)-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   Cd  u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.6191,-2.54093,-2.47957,-2.37819,-2.07801,-1.80504,-0.970386],'cal/(mol*K)','+|-',[0.323494,0.35908,0.348598,0.335148,0.302645,0.257007,0.182294]),
        H298 = (44.2284,'kcal/mol','+|-',1.88976),
        S298 = (37.3101,'cal/(mol*K)','+|-',0.998482),
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
    index = 177,
    label = "cyclopropanone",
    group = 
"""
1 * [C,N,S]   u0 {2,S} {3,S} {4,D}
2   [C,N,O,S] u0 {1,S} {3,S}
3   [C,N,O,S] u0 {1,S} {2,S}
4   [O,S]     u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.274,-1.932,-1.307,-0.838,-1.06,-1.032,-0.271],'cal/(mol*K)'),
        H298 = (45.6,'kcal/mol'),
        S298 = (30.7247,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "Cs-CO(O2d)-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.37652,-2.33935,-2.11893,-2.15519,-2.15148,-2.00756,-1.64288],'cal/(mol*K)','+|-',[0.937801,1.04096,1.01058,0.971584,0.87736,0.745058,0.528465]),
        H298 = (50.0834,'kcal/mol','+|-',5.47838),
        S298 = (33.313,'cal/(mol*K)','+|-',2.89457),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 179,
    label = "Cs-Cs(Br)-CO(O2d)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.56994,-2.35336,-1.97737,-1.97062,-1.96745,-1.85719,-1.54785],'cal/(mol*K)','+|-',[0.761293,0.845038,0.820371,0.788718,0.712228,0.604827,0.429]),
        H298 = (49.7725,'kcal/mol','+|-',4.44727),
        S298 = (33.6701,'cal/(mol*K)','+|-',2.34977),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 180,
    label = "Cs-CO(O2d)-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.37252,-2.3073,-1.87135,-1.69747,-1.59392,-1.53196,-1.30125],'cal/(mol*K)','+|-',[0.758628,0.842081,0.8175,0.785957,0.709735,0.60271,0.427498]),
        H298 = (49.8874,'kcal/mol','+|-',4.4317),
        S298 = (33.0428,'cal/(mol*K)','+|-',2.34155),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 181,
    label = "Cs-CO(O2d)-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.5583,-2.5964,-2.11458,-1.9393,-1.84522,-1.72852,-1.21111],'cal/(mol*K)','+|-',[0.932254,1.03481,1.0046,0.965838,0.872171,0.740652,0.525339]),
        H298 = (49.8061,'kcal/mol','+|-',5.44598),
        S298 = (32.7274,'cal/(mol*K)','+|-',2.87745),
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
    index = 182,
    label = "O2s-Cs(Cl)-CO(O2d)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {5,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.23121,-2.3417,-2.6364,-3.00353,-3.67988,-4.02213,-4.00054],'cal/(mol*K)','+|-',[0.64654,0.717662,0.696713,0.669831,0.604871,0.513659,0.364335]),
        H298 = (46.5416,'kcal/mol','+|-',3.77691),
        S298 = (36.3633,'cal/(mol*K)','+|-',1.99558),
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
    index = 183,
    label = "O2s-CO(O2d)-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.82449,-1.89477,-2.27253,-2.71755,-3.52519,-3.91978,-3.83073],'cal/(mol*K)','+|-',[0.779934,0.86573,0.840459,0.80803,0.729667,0.619637,0.439504]),
        H298 = (47.8102,'kcal/mol','+|-',4.55616),
        S298 = (35.3448,'cal/(mol*K)','+|-',2.40731),
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
    index = 184,
    label = "CO(O2d)-O2s-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.91488,-1.69116,-1.9902,-2.45399,-2.93547,-3.16748,-3.38433],'cal/(mol*K)','+|-',[0.766272,0.850565,0.825736,0.793876,0.716886,0.608783,0.431805]),
        H298 = (48.7576,'kcal/mol','+|-',4.47635),
        S298 = (32.7854,'cal/(mol*K)','+|-',2.36514),
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
    index = 185,
    label = "CO(O2d)-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.05204,-1.86991,-1.45264,-1.31724,-1.11262,-1.06976,-1.03135],'cal/(mol*K)','+|-',[0.758907,0.84239,0.8178,0.786246,0.709995,0.602931,0.427655]),
        H298 = (50.5092,'kcal/mol','+|-',4.43333),
        S298 = (32.5974,'cal/(mol*K)','+|-',2.34241),
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
    index = 186,
    label = "Cs(F)(F)-Cs-CO(O2d)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21621,-1.87623,-1.44696,-1.37712,-1.13759,-0.946761,-0.81083],'cal/(mol*K)','+|-',[0.920863,1.02216,0.992325,0.954037,0.861514,0.731602,0.51892]),
        H298 = (54.3852,'kcal/mol','+|-',5.37943),
        S298 = (31.6269,'cal/(mol*K)','+|-',2.8423),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 187,
    label = "O2s-CO(O2d)-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {5,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.80046,-1.95038,-2.29803,-2.68584,-3.28349,-3.64285,-3.85968],'cal/(mol*K)','+|-',[0.646466,0.71758,0.696633,0.669755,0.604801,0.5136,0.364293]),
        H298 = (46.7422,'kcal/mol','+|-',3.77648),
        S298 = (35.6152,'cal/(mol*K)','+|-',1.99535),
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
    index = 188,
    label = "methylenecyclopropene",
    group = 
"""
1 * [C,N,S]   u0 {2,S} {3,S} {4,D}
2   [C,N,S]   u0 {1,S} {3,D}
3   [C,N,O,S] u0 {1,S} {2,D}
4   [C,N,O,S] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.457,-0.093,-0.645,-1.124,-1.936,-2.246,-2.962],'cal/(mol*K)'),
        H298 = (69.316,'kcal/mol'),
        S298 = (39.8857,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "Cd(Cd)-Cd-Cd(Br)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   Cd   u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.315188,-0.162092,-0.613752,-1.15569,-2.14453,-2.49017,-2.97387],'cal/(mol*K)','+|-',[0.198944,0.220829,0.214382,0.206111,0.186122,0.158056,0.112108]),
        H298 = (61.4749,'kcal/mol','+|-',1.16218),
        S298 = (40.7053,'cal/(mol*K)','+|-',0.614051),
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
    index = 190,
    label = "Cd-Cd-Cd(Cd-Br)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.358346,-0.268423,-1.01428,-1.56474,-2.29819,-2.50544,-3.31892],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (62.3899,'kcal/mol','+|-',2.66044),
        S298 = (42.043,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 191,
    label = "Cd-Cd-Cd(Cd-BrBr)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.0214,0.0862788,-0.845376,-1.34263,-2.14003,-2.42389,-3.3087],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (60.9194,'kcal/mol','+|-',2.66044),
        S298 = (42.1322,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 192,
    label = "Cd(Cd)-Cd(Cl)-Cd",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {2,S}
5   Cd   u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.369876,-0.348727,-0.908859,-1.51261,-2.51845,-2.84609,-3.26577],'cal/(mol*K)','+|-',[0.200103,0.222115,0.215632,0.207312,0.187206,0.158977,0.112761]),
        H298 = (63.0384,'kcal/mol','+|-',1.16895),
        S298 = (41.8241,'cal/(mol*K)','+|-',0.617629),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 193,
    label = "Cd-Cd-Cd(Cd-ClCl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03062,0.119731,-0.892959,-1.47646,-2.28072,-2.54653,-3.4885],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (62.3294,'kcal/mol','+|-',2.66044),
        S298 = (42.2004,'cal/(mol*K)','+|-',1.40568),
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
    index = 194,
    label = "Cd-Cd(Cd-Cl)-Cd",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.229221,-0.458741,-1.11539,-1.63949,-2.30789,-2.49152,-3.33904],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (63.0168,'kcal/mol','+|-',2.66044),
        S298 = (41.9405,'cal/(mol*K)','+|-',1.40568),
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
    index = 195,
    label = "Cd(F)-Cd-Cd(Cd)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   Cd  u0 p0 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.350481,-0.473913,-1.06316,-1.70176,-2.68602,-2.97488,-3.32074],'cal/(mol*K)','+|-',[0.199178,0.221088,0.214635,0.206353,0.186341,0.158242,0.11224]),
        H298 = (71.317,'kcal/mol','+|-',1.16354),
        S298 = (42.2217,'cal/(mol*K)','+|-',0.614773),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 196,
    label = "Cd-Cd-Cd(Cd-F)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0833895,-0.646677,-1.22087,-1.67696,-2.26439,-2.41989,-3.29756],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (65.5197,'kcal/mol','+|-',2.66044),
        S298 = (41.7553,'cal/(mol*K)','+|-',1.40568),
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
    index = 197,
    label = "Cd-Cd(Cd-FF)-Cd",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {1,S} {3,D}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.732651,0.0721818,-0.721514,-1.30552,-2.0752,-2.32612,-3.23509],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (68.2136,'kcal/mol','+|-',2.66044),
        S298 = (41.9612,'cal/(mol*K)','+|-',1.40568),
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
    index = 198,
    label = "methylenecyclopropanone",
    group = 
"""
1 * [C,N,S]    u0 {2,S} {3,S} {4,D}
2   [CO,CS]    u0 {1,S} {3,S}
3   [Cs,N,O,S] u0 {1,S} {2,S}
4   [C,N,O,S]  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.13,-1.101,-1.774,-2.139,-2.509,-2.858,-0.084],'cal/(mol*K)'),
        H298 = (57.7946,'kcal/mol'),
        S298 = (37.18,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "methyleneoxirane",
    group = 
"""
1 * [C,N,S]   u0 {2,S} {3,S} {4,D}
2   [O2s,S2s] u0 {1,S} {3,S}
3   [Cs,N]    u0 {1,S} {2,S}
4   [C,N,O,S] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.101,-2.381,-2.338,-2.236,-2.424,-2.639,-2.068],'cal/(mol*K)'),
        H298 = (36.0543,'kcal/mol'),
        S298 = (29.893,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "Cs-O2s-Cd(Cd-BrBr)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.81936,-4.18202,-4.67837,-4.54517,-4.16808,-3.55408,-2.25879],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (48.7249,'kcal/mol','+|-',1.88121),
        S298 = (39.8921,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 201,
    label = "Cs(Br)-O2s-Cd(Cd)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {5,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Cd   u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.45214,-5.75087,-6.03131,-5.92601,-5.35729,-4.44887,-2.52461],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (48.0834,'kcal/mol','+|-',1.88121),
        S298 = (42.6424,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 202,
    label = "Cs(Br)(Br)-O2s-Cd(Cd)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.00183,-5.37064,-5.8016,-5.67778,-5.11861,-4.29442,-2.51752],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (49.3418,'kcal/mol','+|-',1.88121),
        S298 = (41.2878,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 203,
    label = "Cd(Cd-Br)-Cs-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.69301,-3.81399,-4.23807,-4.10117,-3.598,-2.95566,-1.99276],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (45.452,'kcal/mol','+|-',2.66044),
        S298 = (35.8673,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 204,
    label = "Cd(Cd)-O2s-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.62819,-4.97992,-5.46983,-5.41956,-4.94921,-4.16227,-2.42878],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (50.4797,'kcal/mol','+|-',1.88121),
        S298 = (41.2973,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 205,
    label = "Cs-Cd(Cd-ClCl)-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09118,-3.45981,-4.01988,-3.93923,-3.54929,-2.99484,-2.17536],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (47.2665,'kcal/mol','+|-',2.66044),
        S298 = (37.3377,'cal/(mol*K)','+|-',1.40568),
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
    index = 206,
    label = "Cs-O2s-Cd(Cd-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.55567,-4.82958,-5.18115,-5.05498,-4.45845,-3.65895,-2.2367],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (48.4857,'kcal/mol','+|-',1.88121),
        S298 = (38.9382,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 207,
    label = "Cs(Cl)-Cd(Cd)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {2,D}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.45135,-5.77201,-5.97047,-5.8161,-5.16359,-4.27405,-2.45572],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (45.9521,'kcal/mol','+|-',2.66044),
        S298 = (42.569,'cal/(mol*K)','+|-',1.40568),
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
    index = 208,
    label = "O2s-Cs(F)(F)-Cd(Cd)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cd  u0 p0 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.93695,-5.16592,-5.3553,-5.15465,-4.47205,-3.58377,-1.85713],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (59.1074,'kcal/mol','+|-',1.536),
        S298 = (39.1654,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 209,
    label = "Cd(Cd-F)-Cs-O2s",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.46503,-4.75904,-5.11598,-4.9502,-4.28927,-3.48469,-2.1592],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (51.9028,'kcal/mol','+|-',1.88121),
        S298 = (38.4522,'cal/(mol*K)','+|-',0.993964),
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
    index = 210,
    label = "O2s-Cs-Cd(Cd-FF)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.96115,-4.24854,-4.6949,-4.61925,-4.12471,-3.40205,-2.08951],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (56.2025,'kcal/mol','+|-',1.88121),
        S298 = (39.9742,'cal/(mol*K)','+|-',0.993964),
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
    index = 211,
    label = "Cs(F)-Cd(Cd)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {2,D}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.92242,-5.37143,-5.64926,-5.47222,-4.78479,-3.9197,-2.28952],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (47.677,'kcal/mol','+|-',2.66044),
        S298 = (41.9074,'cal/(mol*K)','+|-',1.40568),
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
    index = 212,
    label = "12Methylenecyclopropane",
    group = 
"""
1   [C,N,S]    u0 {2,S} {3,S} {4,D}
2 * [C,N,S]    u0 {1,S} {3,S} {5,D}
3   [Cs,N,O,S] u0 {1,S} {2,S}
4   [C,N,O,S]  u0 {1,D}
5   [C,N,O,S]  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.326,-3.139,-3.361,-3.148,-2.736,-2.412,-1.706],'cal/(mol*K)'),
        H298 = (51.4711,'kcal/mol'),
        S298 = (35.3587,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "O2s-O2s-Cd(Cd-Br)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.76822,-1.43502,-1.0737,-0.999194,-1.6455,-1.5856,-1.2504],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (12.2961,'kcal/mol','+|-',2.66044),
        S298 = (31.1479,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 214,
    label = "O2s-O2s-Cd(Cd-BrBr)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17264,-1.09742,-0.814365,-0.721313,-1.48658,-1.5352,-1.27193],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (14.1127,'kcal/mol','+|-',2.66044),
        S298 = (31.2968,'cal/(mol*K)','+|-',1.40568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 215,
    label = "O2s-O2s-Cd(Cd-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.90805,-1.56709,-1.1337,-1.06934,-1.67779,-1.59798,-1.26773],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (13.3174,'kcal/mol','+|-',2.66044),
        S298 = (31.0524,'cal/(mol*K)','+|-',1.40568),
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
    index = 216,
    label = "O2s-Cd(Cd-ClCl)-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12638,-1.11762,-0.918257,-0.894512,-1.64136,-1.65629,-1.44016],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (16.2136,'kcal/mol','+|-',2.66044),
        S298 = (31.3462,'cal/(mol*K)','+|-',1.40568),
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
    index = 217,
    label = "O2s-Cd(Cd-FF)-O2s",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34614,-1.1458,-0.865689,-0.828669,-1.51035,-1.48249,-1.19525],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (25.372,'kcal/mol','+|-',2.66044),
        S298 = (31.1199,'cal/(mol*K)','+|-',1.40568),
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
    index = 218,
    label = "O2s-O2s-Cd(Cd-F)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09981,-1.74622,-1.20869,-1.1102,-1.66695,-1.56499,-1.2382],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (17.8221,'kcal/mol','+|-',2.66044),
        S298 = (30.8322,'cal/(mol*K)','+|-',1.40568),
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
    index = 219,
    label = "FourMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
    thermo = 'Cyclobutane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "Cyclobutane",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclobutane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "Cs-Cs(Br)(Br)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.29139,-5.30361,-5.04172,-4.75385,-4.2209,-3.58414,-2.04327],'cal/(mol*K)','+|-',[0.185358,0.205749,0.199743,0.192036,0.173412,0.147262,0.104452]),
        H298 = (26.8602,'kcal/mol','+|-',1.08281),
        S298 = (33.706,'cal/(mol*K)','+|-',0.572119),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         9
""",
)

entry(
    index = 222,
    label = "Cs(Br)-Cs-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.36472,-5.21895,-4.88017,-4.47428,-3.75853,-3.0223,-1.59202],'cal/(mol*K)','+|-',[0.212738,0.23614,0.229247,0.220402,0.199027,0.169015,0.119881]),
        H298 = (25.3791,'kcal/mol','+|-',1.24276),
        S298 = (33.8457,'cal/(mol*K)','+|-',0.656628),
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
    index = 223,
    label = "Cs-Cs(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.356,-5.0227,-4.59698,-4.19976,-3.46742,-2.71417,-1.40203],'cal/(mol*K)','+|-',[0.219134,0.24324,0.236139,0.227028,0.205011,0.174096,0.123485]),
        H298 = (24.6934,'kcal/mol','+|-',1.28012),
        S298 = (33.1563,'cal/(mol*K)','+|-',0.676369),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 224,
    label = "Cs-Cs(Cl)(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.56014,-5.36817,-4.97146,-4.60184,-3.88771,-3.09699,-1.46244],'cal/(mol*K)','+|-',[0.187611,0.208249,0.20217,0.194369,0.175519,0.149052,0.105721]),
        H298 = (24.8924,'kcal/mol','+|-',1.09597),
        S298 = (33.0586,'cal/(mol*K)','+|-',0.579071),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         10
""",
)

entry(
    index = 225,
    label = "Cs(F)-Cs-Cs-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5449,-5.08454,-4.43604,-3.84839,-2.88569,-2.06425,-0.947457],'cal/(mol*K)','+|-',[0.221109,0.245432,0.238268,0.229074,0.206859,0.175665,0.124598]),
        H298 = (24.3801,'kcal/mol','+|-',1.29166),
        S298 = (31.8292,'cal/(mol*K)','+|-',0.682465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 226,
    label = "Cs-Cs-Cs(F)(F)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.89389,-5.28957,-4.46556,-3.83405,-2.82002,-1.97566,-0.660989],'cal/(mol*K)','+|-',[0.186883,0.207441,0.201386,0.193615,0.174838,0.148474,0.105311]),
        H298 = (26.992,'kcal/mol','+|-',1.09172),
        S298 = (31.808,'cal/(mol*K)','+|-',0.576824),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         10
""",
)

entry(
    index = 227,
    label = "34methylenecyclobutene",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {5,D}
2   Cd u0 {1,S} {4,S} {6,D}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {1,D}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.441,0.307,-0.336,-1.197,-1.921,-1.513,-3.264],'cal/(mol*K)'),
        H298 = (33.076,'kcal/mol'),
        S298 = (38.6947,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "dioxerene",
    group = 
"""
1   [Cd,N] u0 {2,D} {4,S}
2 * [Cd,N] u0 {1,D} {3,S}
3   O2s    u0 {2,S} {4,S}
4   O2s    u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.375,-4.281,-4.206,-4.037,-3.926,-3.327,-2.473],'cal/(mol*K)'),
        H298 = (24.4413,'kcal/mol'),
        S298 = (29.7827,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "Oxetene",
    group = 
"""
1 * O2s     u0 {2,S} {4,S}
2   [C,N,S] u0 {1,S} {3,D}
3   [C,N,S] u0 {2,D} {4,S}
4   [C,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.88,-4.22,-4.18,-3.97,-3.65,-3.56,-2.93],'cal/(mol*K)'),
        H298 = (32.51,'kcal/mol'),
        S298 = (29.26,'cal/(mol*K)'),
    ),
    shortDesc = """Derived from goldsmith's DFT-QCI library""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "four-inringonedouble",
    group = 
"""
1   R!H u0 {2,D} {4,S}
2   R!H u0 {1,D} {3,S}
3 * R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
""",
    thermo = 'Cyclobutene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclobutene correction for any four membered ring with one double bond
""",
)

entry(
    index = 231,
    label = "Cyclobutene",
    group = 
"""
1 * [Cs,N,O,S] u0 {2,S} {4,S}
2   [C,N,O,S]  u0 {1,S} {3,D}
3   [C,N,O,S]  u0 {2,D} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],'cal/(mol*K)'),
        H298 = (29.84,'kcal/mol'),
        S298 = (29.8677,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclobutene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "Cd-Cd-O2s-Cs(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.77279,-5.69045,-5.89872,-5.81575,-5.0907,-4.22503,-2.73176],'cal/(mol*K)','+|-',[0.242692,0.269389,0.261525,0.251435,0.22705,0.192812,0.13676]),
        H298 = (40.4005,'kcal/mol','+|-',1.41774),
        S298 = (38.2845,'cal/(mol*K)','+|-',0.749081),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 233,
    label = "O2s-Cd-Cd-Cs(F)(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {4,D}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cd  u0 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.99788,-5.74682,-5.66948,-5.4679,-4.68498,-3.83344,-2.32573],'cal/(mol*K)','+|-',[0.264904,0.294045,0.285462,0.274447,0.247831,0.210459,0.149278]),
        H298 = (42.1341,'kcal/mol','+|-',1.5475),
        S298 = (35.9334,'cal/(mol*K)','+|-',0.817642),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 234,
    label = "Cs(Br)-Cd-Cd-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.2477,-6.19156,-6.47028,-6.40839,-5.67052,-4.72428,-2.95865],'cal/(mol*K)','+|-',[0.246234,0.273321,0.265343,0.255105,0.230365,0.195627,0.138757]),
        H298 = (37.8035,'kcal/mol','+|-',1.43843),
        S298 = (39.389,'cal/(mol*K)','+|-',0.760016),
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
    index = 235,
    label = "Cd-Cd-Cs(Br)(Br)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd   u0 p0 c0 {1,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.76472,-5.65977,-6.03818,-5.99563,-5.3599,-4.51982,-2.85194],'cal/(mol*K)','+|-',[0.276237,0.306624,0.297674,0.286188,0.258434,0.219463,0.155664]),
        H298 = (38.1048,'kcal/mol','+|-',1.6137),
        S298 = (38.1494,'cal/(mol*K)','+|-',0.852621),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 236,
    label = "Cs-Cd-Cd-Cs(Br)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.81769,-3.6227,-3.33802,-3.13984,-2.74856,-2.33747,-1.23801],'cal/(mol*K)','+|-',[0.153606,0.170504,0.165526,0.15914,0.143706,0.122036,0.0865594]),
        H298 = (28.9156,'kcal/mol','+|-',0.897326),
        S298 = (32.6982,'cal/(mol*K)','+|-',0.474114),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         13
""",
)

entry(
    index = 237,
    label = "Cd(Br)-Cd-Cs-O2s",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61314,-3.90132,-4.04036,-3.98519,-3.53931,-3.02136,-2.22364],'cal/(mol*K)','+|-',[0.329718,0.365989,0.355305,0.341596,0.308468,0.261953,0.185801]),
        H298 = (33.1494,'kcal/mol','+|-',1.92613),
        S298 = (32.6242,'cal/(mol*K)','+|-',1.01769),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 238,
    label = "Cd(Br)-Cd-O2s-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.13061,-4.94915,-5.24503,-5.09234,-4.32921,-3.54455,-2.55895],'cal/(mol*K)','+|-',[0.557148,0.618437,0.600384,0.577219,0.52124,0.44264,0.313961]),
        H298 = (38.8214,'kcal/mol','+|-',3.25471),
        S298 = (34.3546,'cal/(mol*K)','+|-',1.71967),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         1
""",
)

entry(
    index = 239,
    label = "Cd(Br)-Cd-Cs-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.92054,-2.98899,-2.98132,-2.85941,-2.54527,-2.16847,-1.55851],'cal/(mol*K)','+|-',[0.277207,0.307702,0.29872,0.287194,0.259342,0.220234,0.156211]),
        H298 = (29.3407,'kcal/mol','+|-',1.61937),
        S298 = (30.8914,'cal/(mol*K)','+|-',0.855616),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 240,
    label = "O2s-O2s-Cd-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13555,-1.70054,-1.35536,-1.41639,-2.09871,-2.11435,-1.72817],'cal/(mol*K)','+|-',[0.373976,0.415115,0.402998,0.387449,0.349874,0.297114,0.210741]),
        H298 = (17.7711,'kcal/mol','+|-',2.18467),
        S298 = (25.6443,'cal/(mol*K)','+|-',1.1543),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 241,
    label = "Cs-Cd(Cl)-Cd-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.08083,-2.96088,-2.84769,-2.73306,-2.38688,-2.05385,-1.39319],'cal/(mol*K)','+|-',[0.208429,0.231357,0.224604,0.215938,0.194996,0.165592,0.117453]),
        H298 = (28.1639,'kcal/mol','+|-',1.21759),
        S298 = (31.1535,'cal/(mol*K)','+|-',0.643328),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         8
""",
)

entry(
    index = 242,
    label = "Cd-Cd-O2s-Cs(Cl)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9897,-5.8937,-6.16047,-6.10376,-5.37247,-4.50308,-2.95305],'cal/(mol*K)','+|-',[0.242467,0.269139,0.261283,0.251201,0.22684,0.192633,0.136633]),
        H298 = (36.7438,'kcal/mol','+|-',1.41642),
        S298 = (38.7492,'cal/(mol*K)','+|-',0.748386),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 243,
    label = "Cd-Cs(Cl)(Cl)-O2s-Cd",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd   u0 p0 c0 {1,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.54991,-5.37108,-5.71268,-5.70255,-5.07943,-4.29063,-2.8643],'cal/(mol*K)','+|-',[0.263134,0.29208,0.283554,0.272614,0.246175,0.209053,0.14828]),
        H298 = (37.8512,'kcal/mol','+|-',1.53716),
        S298 = (37.2812,'cal/(mol*K)','+|-',0.812179),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 244,
    label = "Cd(Cl)-O2s-Cs-Cd",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.64708,-4.05648,-4.13942,-4.0046,-3.45435,-2.91571,-2.21033],'cal/(mol*K)','+|-',[0.330419,0.366767,0.356061,0.342322,0.309124,0.262509,0.186196]),
        H298 = (32.2404,'kcal/mol','+|-',1.93022),
        S298 = (32.5938,'cal/(mol*K)','+|-',1.01986),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 245,
    label = "Cs-Cs(Cl)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.55938,-3.21098,-2.93771,-2.80714,-2.45889,-2.08379,-1.09296],'cal/(mol*K)','+|-',[0.263641,0.292642,0.2841,0.273138,0.246649,0.209455,0.148565]),
        H298 = (29.5724,'kcal/mol','+|-',1.54012),
        S298 = (33.2894,'cal/(mol*K)','+|-',0.813741),
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
    index = 246,
    label = "Cd-Cs-Cs(Cl)(Cl)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.52929,-3.28548,-3.04317,-2.90467,-2.55568,-2.16383,-0.980261],'cal/(mol*K)','+|-',[0.225577,0.250392,0.243083,0.233704,0.211039,0.179215,0.127116]),
        H298 = (27.3061,'kcal/mol','+|-',1.31776),
        S298 = (31.5733,'cal/(mol*K)','+|-',0.696257),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 247,
    label = "Cs-O2s-Cd-Cd(Cl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.01927,-4.33843,-4.42661,-4.39384,-3.87586,-3.30137,-2.51184],'cal/(mol*K)','+|-',[0.518896,0.575977,0.559163,0.537589,0.485453,0.412249,0.292405]),
        H298 = (32.7476,'kcal/mol','+|-',3.03125),
        S298 = (34.3177,'cal/(mol*K)','+|-',1.6016),
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
    index = 248,
    label = "Cd-O2s-O2s-Cd(Cl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.09644,-1.46401,-0.976103,-1.0795,-1.86359,-1.99042,-1.74659],'cal/(mol*K)','+|-',[0.358643,0.398096,0.386475,0.371563,0.335529,0.284933,0.202101]),
        H298 = (13.911,'kcal/mol','+|-',2.0951),
        S298 = (25.5553,'cal/(mol*K)','+|-',1.10697),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 249,
    label = "Cs(F)-Cs-Cd-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.52525,-3.13692,-2.75361,-2.50545,-2.02304,-1.61963,-0.760133],'cal/(mol*K)','+|-',[0.19486,0.216295,0.209981,0.201879,0.182301,0.154811,0.109806]),
        H298 = (27.7915,'kcal/mol','+|-',1.13832),
        S298 = (32.0117,'cal/(mol*K)','+|-',0.601445),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 250,
    label = "Cd-Cs-Cs(F)(F)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.62673,-3.1852,-2.69071,-2.40815,-1.9028,-1.50367,-0.571361],'cal/(mol*K)','+|-',[0.203262,0.225622,0.219035,0.210584,0.190162,0.161486,0.114541]),
        H298 = (27.7129,'kcal/mol','+|-',1.1874),
        S298 = (30.5917,'cal/(mol*K)','+|-',0.627379),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 251,
    label = "Cd(F)-Cd-Cs-Cs",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,D} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.67931,-3.5078,-3.17363,-2.89641,-2.335,-1.844,-1.37537],'cal/(mol*K)','+|-',[0.32986,0.366146,0.355458,0.341743,0.3086,0.262065,0.185881]),
        H298 = (28.922,'kcal/mol','+|-',1.92695),
        S298 = (29.2777,'cal/(mol*K)','+|-',1.01813),
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
    index = 252,
    label = "Cd-Cd(F)-Cs-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,D} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.44493,-4.69197,-4.60576,-4.47491,-3.80438,-3.12644,-2.26575],'cal/(mol*K)','+|-',[0.365487,0.405693,0.39385,0.378654,0.341932,0.29037,0.205958]),
        H298 = (37.4364,'kcal/mol','+|-',2.13508),
        S298 = (33.6496,'cal/(mol*K)','+|-',1.1281),
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
    index = 253,
    label = "Cs-Cd-Cd(F)-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {4,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4 * Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.00261,-4.19025,-4.06905,-3.96997,-3.53122,-3.03228,-2.21411],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (32.0388,'kcal/mol','+|-',2.66044),
        S298 = (32.2553,'cal/(mol*K)','+|-',1.40568),
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
    index = 254,
    label = "Cd-Cd(F)-O2s-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {4,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.27908,-1.70722,-1.11278,-1.19997,-1.95677,-2.06982,-1.82597],'cal/(mol*K)','+|-',[0.365487,0.405693,0.39385,0.378654,0.341932,0.29037,0.205958]),
        H298 = (21.0605,'kcal/mol','+|-',2.13508),
        S298 = (26.3373,'cal/(mol*K)','+|-',1.1281),
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
    index = 255,
    label = "Oxetane",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [Cs,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08,-4.28,-3.636,-3.016,-2.451,-1.896,2.84],'cal/(mol*K)'),
        H298 = (25.08,'kcal/mol'),
        S298 = (28.5487,'cal/(mol*K)'),
    ),
    shortDesc = """CY/C3O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "Cs-Cs(Br)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.94434,-5.91055,-5.58501,-5.24032,-4.51678,-3.78904,-2.13964],'cal/(mol*K)','+|-',[0.205153,0.22772,0.221073,0.212543,0.191931,0.162988,0.115607]),
        H298 = (23.2983,'kcal/mol','+|-',1.19845),
        S298 = (33.6204,'cal/(mol*K)','+|-',0.633215),
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
    index = 257,
    label = "O2s-Cs-Cs(Br)(Br)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.92037,-5.94836,-5.6498,-5.35218,-4.75605,-4.08779,-2.37526],'cal/(mol*K)','+|-',[0.243268,0.270029,0.262147,0.252032,0.22759,0.19327,0.137085]),
        H298 = (27.0767,'kcal/mol','+|-',1.42111),
        S298 = (35.5523,'cal/(mol*K)','+|-',0.750861),
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
    index = 258,
    label = "Cs-Cs-Cs(Br)(Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.88446,-5.88672,-5.58778,-5.34927,-4.85515,-4.26446,-2.33667],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (20.4368,'kcal/mol','+|-',1.536),
        S298 = (36.0805,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 259,
    label = "O2s-Cs(Br)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.389,-6.43151,-6.0799,-5.75702,-5.09501,-4.28004,-2.33642],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (22.6061,'kcal/mol','+|-',1.88121),
        S298 = (36.4045,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 260,
    label = "O2s-Cs(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.18438,-6.21913,-5.86573,-5.56909,-4.90001,-4.09974,-2.19442],'cal/(mol*K)','+|-',[0.196461,0.218073,0.211707,0.203539,0.183799,0.156083,0.110709]),
        H298 = (23.0791,'kcal/mol','+|-',1.14767),
        S298 = (35.9949,'cal/(mol*K)','+|-',0.606389),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 261,
    label = "O2s-Cs-Cs-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.57151,-5.49252,-5.24398,-5.07091,-4.5273,-3.80926,-2.06684],'cal/(mol*K)','+|-',[0.188262,0.208972,0.202872,0.195044,0.176129,0.149569,0.106089]),
        H298 = (21.0687,'kcal/mol','+|-',1.09978),
        S298 = (35.1619,'cal/(mol*K)','+|-',0.581082),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         8
""",
)

entry(
    index = 262,
    label = "O2s-Cs-Cs(Cl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.97299,-5.58443,-5.05169,-4.56142,-3.68219,-2.86726,-1.56093],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (28.2133,'kcal/mol','+|-',2.66044),
        S298 = (33.3402,'cal/(mol*K)','+|-',1.40568),
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
    index = 263,
    label = "Cs-Cs(Cl)(Cl)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.38819,-6.00666,-5.20561,-4.60919,-3.96838,-3.2671,-1.57903],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (28.0877,'kcal/mol','+|-',2.66044),
        S298 = (36.1776,'cal/(mol*K)','+|-',1.40568),
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
    index = 264,
    label = "O2s-Cs-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.54702,-5.54538,-5.26563,-4.95183,-4.19821,-3.42054,-1.88743],'cal/(mol*K)','+|-',[0.196663,0.218297,0.211925,0.203748,0.183988,0.156244,0.110823]),
        H298 = (22.827,'kcal/mol','+|-',1.14885),
        S298 = (34.6896,'cal/(mol*K)','+|-',0.607012),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 265,
    label = "Cs-Cs(F)(F)-O2s-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.42211,-5.27727,-4.8824,-4.55355,-3.76673,-3.00954,-1.50278],'cal/(mol*K)','+|-',[0.19525,0.216729,0.210402,0.202284,0.182666,0.155121,0.110026]),
        H298 = (19.7135,'kcal/mol','+|-',1.1406),
        S298 = (32.7133,'cal/(mol*K)','+|-',0.602651),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 266,
    label = "Cs-O2s-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4 * O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.03629,-5.55365,-4.8388,-4.23652,-3.27863,-2.4565,-1.22544],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (29.0119,'kcal/mol','+|-',2.66044),
        S298 = (33.0363,'cal/(mol*K)','+|-',1.40568),
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
    index = 267,
    label = "Cs-O2s-Cs-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4 * O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.39241,-5.71788,-4.82985,-4.17729,-3.18403,-2.36315,-1.04156],'cal/(mol*K)','+|-',[0.455419,0.505518,0.490761,0.471826,0.426068,0.361819,0.256636]),
        H298 = (29.455,'kcal/mol','+|-',2.66044),
        S298 = (30.6376,'cal/(mol*K)','+|-',1.40568),
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
    index = 268,
    label = "Beta-Propiolactone",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [CO,CS]  u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.434,-4.019,-3.31,-2.703,-2.253,-2.012,1.3],'cal/(mol*K)'),
        H298 = (22.98,'kcal/mol'),
        S298 = (30.392,'cal/(mol*K)'),
    ),
    shortDesc = """Beta-Propiolactone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "Cyclobutanone",
    group = 
"""
1 * [CO,CS]  u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [Cs,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.62,-4.96,-3.744,-2.671,-1.962,-1.415,-0.3],'cal/(mol*K)'),
        H298 = (22.53,'kcal/mol'),
        S298 = (29.8337,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclobutanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "12dioxetane",
    group = 
"""
1   [Cs,N] u0 {2,S} {4,S}
2 * [Cs,N] u0 {1,S} {3,S}
3   O2s    u0 {2,S} {4,S}
4   O2s    u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.512,-4.727,-5.01,-4.504,-4.218,-4.242,-2.465],'cal/(mol*K)','+|-',[0.7921,0.7921,0.7921,0.7921,0.7921,0.7921,0.7921]),
        H298 = (26.826,'kcal/mol','+|-',3.3865),
        S298 = (27.858,'cal/(mol*K)','+|-',1.0404),
    ),
    shortDesc = """Calculations from Duminda Ranasinghe""",
    longDesc = 
"""
Based on CBS-QB3 calculation with rotors and BAC for singlet C=CC1COO1 from Duminda Ranasinghe in 05/2019, fitted by Hao-Wei Pang
""",
)

entry(
    index = 271,
    label = "Cs-Cs(Br)-O2s-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.00457,-6.74082,-6.74049,-6.55807,-6.22465,-6.05585,-3.86926],'cal/(mol*K)','+|-',[0.323596,0.359193,0.348708,0.335253,0.30274,0.257088,0.182351]),
        H298 = (28.1892,'kcal/mol','+|-',1.89036),
        S298 = (36.3206,'cal/(mol*K)','+|-',0.998796),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 272,
    label = "O2s-Cs(Br)(Br)-Cs-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.65161,-6.23303,-6.21656,-6.09697,-5.89674,-5.83538,-3.73291],'cal/(mol*K)','+|-',[0.276176,0.306556,0.297608,0.286125,0.258376,0.219414,0.155629]),
        H298 = (29.3524,'kcal/mol','+|-',1.61334),
        S298 = (36.992,'cal/(mol*K)','+|-',0.852431),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 273,
    label = "Cs(Cl)-O2s-O2s-Cs",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.93715,-6.68835,-6.6508,-6.50053,-6.14277,-5.91068,-3.80451],'cal/(mol*K)','+|-',[0.323322,0.35889,0.348413,0.33497,0.302484,0.256871,0.182197]),
        H298 = (27.9564,'kcal/mol','+|-',1.88876),
        S298 = (35.9893,'cal/(mol*K)','+|-',0.997953),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 274,
    label = "O2s-Cs-Cs(Cl)(Cl)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.30308,-5.93368,-6.00005,-5.95584,-5.73649,-5.62101,-3.64817],'cal/(mol*K)','+|-',[0.276865,0.307321,0.29835,0.286839,0.259021,0.219962,0.156017]),
        H298 = (27.6954,'kcal/mol','+|-',1.61737),
        S298 = (36.1847,'cal/(mol*K)','+|-',0.854559),
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
    index = 275,
    label = "Cs-Cs(F)-O2s-O2s",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.19903,-5.96408,-6.07413,-5.9919,-5.65199,-5.48276,-3.64315],'cal/(mol*K)','+|-',[0.323494,0.35908,0.348598,0.335148,0.302645,0.257007,0.182294]),
        H298 = (27.2312,'kcal/mol','+|-',1.88976),
        S298 = (35.1172,'cal/(mol*K)','+|-',0.998482),
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
    index = 276,
    label = "O2s-Cs(F)(F)-Cs-O2s",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.14616,-5.78989,-5.78487,-5.59848,-5.15664,-4.99494,-3.23681],'cal/(mol*K)','+|-',[0.276769,0.307215,0.298247,0.28674,0.258932,0.219886,0.155964]),
        H298 = (27.1883,'kcal/mol','+|-',1.61681),
        S298 = (32.8765,'cal/(mol*K)','+|-',0.854263),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 277,
    label = "four-inringtwodouble",
    group = 
"""
1   R!H u0 {2,D} {4,[S,D]}
2 * R!H u0 {1,D} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,D}
4   R!H u0 {1,[S,D]} {3,D}
""",
    thermo = 'cyclobutadiene_13',
    shortDesc = """""",
    longDesc = 
"""
Use cyclobutadiene_13 correction for any four membered ring with at least two double bonds in the 1,3-positions
""",
)

entry(
    index = 278,
    label = "cyclobutadiene_13",
    group = 
"""
1   [Cd,N] u0 {2,D} {4,S}
2 * [Cd,N] u0 {1,D} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.336,-3.24,-3.526,-3.419,-3.071,-2.761,-2.346],'cal/(mol*K)'),
        H298 = (77.2135,'kcal/mol'),
        S298 = (36.4303,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "Cd-Cd-Cd-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4 * Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.14985,-2.99686,-3.21511,-3.25887,-3.10886,-2.84408,-2.23297],'cal/(mol*K)','+|-',[0.251045,0.278662,0.270527,0.260089,0.234866,0.199449,0.141468]),
        H298 = (71.1036,'kcal/mol','+|-',1.46654),
        S298 = (37.7115,'cal/(mol*K)','+|-',0.774866),
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
    index = 280,
    label = "Cd-Cd-Cd(Cl)-Cd",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4 * Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.10991,-3.09568,-3.39744,-3.48757,-3.40552,-3.15298,-2.43729],'cal/(mol*K)','+|-',[0.251193,0.278825,0.270686,0.260242,0.235004,0.199566,0.141551]),
        H298 = (71.0927,'kcal/mol','+|-',1.4674),
        S298 = (38.9433,'cal/(mol*K)','+|-',0.77532),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 281,
    label = "Cd-Cd-Cd-Cd(F)",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cd  u0 p0 c0 {1,S} {4,D}
3   Cd  u0 p0 c0 {1,D} {4,S}
4   Cd  u0 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.02466,-3.18773,-3.49048,-3.65799,-3.63585,-3.37977,-2.58608],'cal/(mol*K)','+|-',[0.267215,0.29661,0.287952,0.276842,0.249994,0.212296,0.15058]),
        H298 = (74.0354,'kcal/mol','+|-',1.561),
        S298 = (39.8368,'cal/(mol*K)','+|-',0.824775),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 282,
    label = "cyclobutadiene_12",
    group = 
"""
1   R!H u0 {2,D} {4,S}
2 * R!H u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {1,S} {3,S}
""",
    thermo = 'cyclobutadiene_13',
    shortDesc = """""",
    longDesc = 
"""
Use cyclobutadiene_13 correction for 1,2_CBD
""",
)

entry(
    index = 283,
    label = "thietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42,-3.66,-2.92,-2.3,-1.53,-1.01,-0.3],'cal/(mol*K)'),
        H298 = (19.82,'kcal/mol'),
        S298 = (25.35,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "1,2-dithietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.24,-3.62,-3.13,-2.69,-2.11,-1.62,-0.79],'cal/(mol*K)'),
        H298 = (23.45,'kcal/mol'),
        S298 = (24.44,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "1,3-dithietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   [C,N] u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.59,-9.53,-7.27,-5.52,-3.34,-2.19,-0.96],'cal/(mol*K)'),
        H298 = (16.87,'kcal/mol'),
        S298 = (29.55,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "trithietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   S     u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.81,-7.66,-6.51,-5.66,-4.53,-3.75,-2.33],'cal/(mol*K)'),
        H298 = (30.77,'kcal/mol'),
        S298 = (29.05,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "tetrathietane",
    group = 
"""
1 * S u0 {2,S} {4,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   S u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.92,-7.46,-7.14,-6.99,-6.77,-6.27,-4.36],'cal/(mol*K)'),
        H298 = (22.72,'kcal/mol'),
        S298 = (32.19,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "Azetidine",
    group = 
"""
1 * N          u0 {2,S} {4,S}
2   [Cs,N,O,S] u0 {1,S} {3,S}
3   [Cs,N,O,S] u0 {2,S} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (29.3,'cal/(mol*K)'),
    ),
    shortDesc = """Azetidine ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "4-Methylene-2-oxetanone",
    group = 
"""
1   [Cd,N]  u0 {2,S} {3,S} {5,D}
2 * O       u0 {1,S} {4,S}
3   [Cs,N]  u0 {1,S} {4,S}
4   [CO,CS] u0 {2,S} {3,S}
5   [Cd,N]  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.912,-1.903,-1.567,-1.378,-1.566,-1.528,1.547],'cal/(mol*K)'),
        H298 = (16.94,'kcal/mol'),
        S298 = (35.477,'cal/(mol*K)'),
    ),
    shortDesc = """4-Methylene-2-oxetanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "methylenecyclobutane",
    group = 
"""
1 * [Cd,N] u0 {2,S} {3,S} {5,D}
2   [Cs,N] u0 {1,S} {4,S}
3   [Cs,N] u0 {1,S} {4,S}
4   [Cs,N] u0 {2,S} {3,S}
5   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.862,-3.896,-3.629,-3.244,-2.48,-1.836,-1.085],'cal/(mol*K)'),
        H298 = (29.371,'kcal/mol'),
        S298 = (30.511,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted from CBS-QB3 calculation""",
    longDesc = 
"""
"
Fitted from CBS-QB3 calculation for C=C1CCC1. Mengjie Liu 9/9/19.
""",
)

entry(
    index = 291,
    label = "2methyleneoxetane",
    group = 
"""
1 * [Cd,N]    u0 {2,S} {3,S} {5,D}
2   [O2s,S2s] u0 {1,S} {4,S}
3   [Cs,N]    u0 {1,S} {4,S}
4   [Cs,N]    u0 {2,S} {3,S}
5   [Cd,N]    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.33,-3.553,-3.213,-2.78,-2.445,-2.331,0.556],'cal/(mol*K)'),
        H298 = (23.79,'kcal/mol'),
        S298 = (25.597,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "12methylenecyclobutane",
    group = 
"""
1 * [Cd,N,S]   u0 {2,S} {4,S} {5,D}
2   [Cd,N,S]   u0 {1,S} {3,S} {6,D}
3   [Cs,N,O,S] u0 {2,S} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
5   [Cd,N,O,S] u0 {1,D}
6   [Cd,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.313,-4.605,-4.416,-3.887,-3.024,-2.355,-1.276],'cal/(mol*K)'),
        H298 = (28.04,'kcal/mol'),
        S298 = (31.4877,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "O2s-Cs-O2s-Cs(Br)(Br)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.96536,-6.43179,-6.4249,-6.21115,-5.44585,-4.63348,-2.57998],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (22.2786,'kcal/mol','+|-',1.536),
        S298 = (34.6353,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 294,
    label = "Cs-O2s-Cs(Br)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.81191,-9.15621,-9.17295,-8.67523,-7.24905,-5.84517,-3.04075],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (25.9742,'kcal/mol','+|-',1.88121),
        S298 = (39.1617,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 295,
    label = "O2s-Cs-O2s-Cs(Cl)(Cl)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17811,-6.85074,-7.03116,-6.84816,-5.90135,-4.87813,-2.70192],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (20.5021,'kcal/mol','+|-',1.536),
        S298 = (34.7563,'cal/(mol*K)','+|-',0.811568),
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
    index = 296,
    label = "Cs-O2s-Cs(Cl)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.60623,-8.97832,-9.02501,-8.45091,-6.80465,-5.30995,-2.69616],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (25.0483,'kcal/mol','+|-',1.88121),
        S298 = (38.2453,'cal/(mol*K)','+|-',0.993964),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 297,
    label = "O2s-Cs-O2s-Cs(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.82641,-7.61214,-7.46945,-6.99142,-5.59653,-4.29718,-2.07205],'cal/(mol*K)','+|-',[0.32203,0.357455,0.347021,0.333631,0.301276,0.255845,0.181469]),
        H298 = (22.3536,'kcal/mol','+|-',1.88121),
        S298 = (36.097,'cal/(mol*K)','+|-',0.993964),
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
    index = 298,
    label = "Cs-O2s-Cs(F)(F)-O2s",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.77388,-6.16376,-6.00411,-5.75828,-4.83308,-3.91753,-2.10777],'cal/(mol*K)','+|-',[0.262937,0.291861,0.283341,0.272409,0.24599,0.208896,0.148169]),
        H298 = (19.1301,'kcal/mol','+|-',1.536),
        S298 = (32.7719,'cal/(mol*K)','+|-',0.811568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 299,
    label = "FiveMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
    thermo = 'Cyclopentane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "Cyclopentane",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (6.3,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "Cyclopentene",
    group = 
"""
1   [Cs,N] u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5 * [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (5.97,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "Cyclopentadiene",
    group = 
"""
1 * [Cs,N]     u0 {2,S} {5,S}
2   [Cd,N,O,S] u0 {1,S} {3,D}
3   [Cd,N,O,S] u0 {2,D} {4,S}
4   [Cd,N,O,S] u0 {3,S} {5,D}
5   [Cd,N,O,S] u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7845,-3.72708,-3.2688,-2.74383,-2.05359,-1.65464,-0.98756],'cal/(mol*K)'),
        H298 = (6.05,'kcal/mol'),
        S298 = (27.9821,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "five-inringtwodouble-12",
    group = 
"""
1 * R!H u0 {2,[S,D]} {5,S}
2   R!H u0 {1,[S,D]} {3,D}
3   Cdd u0 {2,D} {4,D}
4   R!H u0 {3,D} {5,[S,D]}
5   R!H u0 {1,S} {4,[S,D]}
""",
    thermo = '1,2-Cyclopentadiene',
    shortDesc = """""",
    longDesc = 
"""
For now, any 5-membered ring that has at least 2 double-bonds in the 1,2 positions will use this general correction.
""",
)

entry(
    index = 304,
    label = "1,2-Cyclopentadiene",
    group = 
"""
1 * C   u0 {2,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61023,-3.22037,-2.91832,-2.86073,-2.50323,-1.66978,-1.31002],'cal/(mol*K)'),
        H298 = (65.8534,'kcal/mol'),
        S298 = (26.7523,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to M06 calculation""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "five-inringthreedouble-124",
    group = 
"""
1 * R!H       u0 {2,D} {5,[S,D]}
2   [Cdd,N,S] u0 {1,D} {3,D}
3   R!H       u0 {2,D} {4,[S,D]}
4   R!H       u0 {3,[S,D]} {5,D}
5   R!H       u0 {1,[S,D]} {4,D}
""",
    thermo = 'Cyclopentatriene',
    shortDesc = """""",
    longDesc = 
"""
For now, any 5-membered ring that has at least 3 double-bonds in the 1,2,4 positions will use this general correction.
""",
)

entry(
    index = 306,
    label = "Cyclopentatriene",
    group = 
"""
1 * Cd  u0 {2,D} {5,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08,-4.69,-4.58,-4.25,-3.54,-3.08,-2.47],'cal/(mol*K)'),
        H298 = (70.16,'kcal/mol'),
        S298 = (36.76,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 isodesmic reaction approach allene + 2-butene = cyclopentatriene + 2 CH4, DHr = 220.8 kJ mol-1, exp data from NIST""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "five-inringonetriple",
    group = 
"""
1 * R!H u0 {2,T} {5,S}
2   R!H u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,S} {4,[S,D,T]}
""",
    thermo = 'Cyclopentyne',
    shortDesc = """""",
    longDesc = 
"""
Use cyclopentyne ring correction for any five-membered ring containing a triple bond.
""",
)

entry(
    index = 308,
    label = "Cyclopentyne",
    group = 
"""
1 * Ct u0 {2,T} {5,S}
2   Ct u0 {1,T} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.441,-1.573,-1.731,-1.812,-1.511,-1.194,-3.151],'cal/(mol*K)'),
        H298 = (72.047,'kcal/mol'),
        S298 = (28.96,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to CBS-QB3 calculation""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "Tetrahydrofuran",
    group = 
"""
1 * O      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.93,-5.71,-4.67,-3.721,-2.689,-1.856,3.213],'cal/(mol*K)'),
        H298 = (5.96,'kcal/mol'),
        S298 = (21.1624,'cal/(mol*K)'),
    ),
    shortDesc = """CY/C4O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "2,3-Dihydrofuran",
    group = 
"""
1 * O      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.56,-5.96,-5.695,-5.144,-4.218,-3.708,-0.284],'cal/(mol*K)'),
        H298 = (4.57,'kcal/mol'),
        S298 = (23.83,'cal/(mol*K)'),
    ),
    shortDesc = """2,3-Dihydrofuran ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "1,3-Dioxolane",
    group = 
"""
1 * [Cs,N] u0 {2,S} {5,S}
2   O      u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O      u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.655,-6.405,-6.306,-6.405,-7.631,-8.27,-3.21],'cal/(mol*K)'),
        H298 = (5.13,'kcal/mol'),
        S298 = (20.4021,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Dioxolane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "Furan",
    group = 
"""
1   [Cd,N] u0 {2,D} {5,S}
2   [Cd,N] u0 {1,D} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {3,D} {5,S}
5 * O      u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.09,-7.18,-6.79,-5.86,-4.83,-3.71,-2.9],'cal/(mol*K)'),
        H298 = (-6.3,'kcal/mol'),
        S298 = (31.71,'cal/(mol*K)'),
    ),
    shortDesc = """Furan ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "Dihydro-2,5-furandione",
    group = 
"""
1 * O       u0 {2,S} {5,S}
2   [CO,CS] u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [CO,CS] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.235,-4.726,-3.615,-1.82,-1.835,-1.084,1.104],'cal/(mol*K)'),
        H298 = (1.4,'kcal/mol'),
        S298 = (37.7647,'cal/(mol*K)'),
    ),
    shortDesc = """Dihydro-2,5-furandione ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "2,5-Furandione",
    group = 
"""
1 * O       u0 {2,S} {5,S}
2   [CO,CS] u0 {1,S} {3,S}
3   [Cd,N]  u0 {2,S} {4,D}
4   [Cd,N]  u0 {3,D} {5,S}
5   [CO,CS] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """2,5-Furandione ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "Cyclopentanone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   [Cs,N]  u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.06,-4.927,-3.392,-2.097,-1.093,-0.322,1.29],'cal/(mol*K)'),
        H298 = (4.47,'kcal/mol'),
        S298 = (24.6287,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "butyrolactone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   O2s     u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.836,-5.134,-4.114,-3.222,-2.341,-1.822,1.888],'cal/(mol*K)'),
        H298 = (7.92,'kcal/mol'),
        S298 = (27.4547,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "25dihydrofuran",
    group = 
"""
1 * [Cs,N] u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.946,-3.361,-2.438,-1.799,-1.458,-1.056,-0.254],'cal/(mol*K)'),
        H298 = (4.23674,'kcal/mol'),
        S298 = (25.1504,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "12dioxolane",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95,-4.859,-4.265,-3.679,-3.089,-3.091,1.915],'cal/(mol*K)'),
        H298 = (6.05383,'kcal/mol'),
        S298 = (25.0554,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "12dioxolene",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.159,-4.213,-3.754,-3.376,-3.14,-2.919,-1.982],'cal/(mol*K)'),
        H298 = (4.56853,'kcal/mol'),
        S298 = (29.97,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "123trioxolane",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   O2s    u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.566,-3.543,-3.344,-2.829,-2.487,-2.78,2.13],'cal/(mol*K)'),
        H298 = (10.1971,'kcal/mol'),
        S298 = (23.316,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "124trioxolane",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   O2s    u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.648,-4.764,-3.63,-2.89,-2.711,-2.859,2.25],'cal/(mol*K)'),
        H298 = (9.45319,'kcal/mol'),
        S298 = (25.1104,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "thiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.61,-4.54,-3.51,-2.63,-1.49,-0.73,0.32],'cal/(mol*K)'),
        H298 = (2.02,'kcal/mol'),
        S298 = (20.68,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "2,3-dihydrothiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [C,N]  u0 {3,S} {5,S}
5   [C,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.58,-4.63,-3.67,-2.89,-1.9,-1.26,-0.41],'cal/(mol*K)'),
        H298 = (3.37,'kcal/mol'),
        S298 = (24.24,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "2,5-dihydrothiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [C,N]  u0 {1,S} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {3,D} {5,S}
5   [C,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.84,-9.28,-7.17,-5.42,-3.18,-1.97,-0.74],'cal/(mol*K)'),
        H298 = (2.19,'kcal/mol'),
        S298 = (28.23,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "thiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cd,N] u0 {3,S} {5,D}
5   [Cd,N] u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15,-3.75,-2.7,-2.03,-1.45,-1.14,-0.76],'cal/(mol*K)'),
        H298 = (-17.22,'kcal/mol'),
        S298 = (23.78,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "1,2-dithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15,-6.27,-7.52,-8.83,-11.39,-13.48,-16.94],'cal/(mol*K)'),
        H298 = (23.29,'kcal/mol'),
        S298 = (23.78,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "1,3-dithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   [C,N] u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.45,-6.68,-4.91,-3.49,-1.72,-0.7,0.45],'cal/(mol*K)'),
        H298 = (0.48,'kcal/mol'),
        S298 = (22.84,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "1,2,3-trithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51,-4.63,-3.98,-3.49,-2.82,-2.2,-0.88],'cal/(mol*K)'),
        H298 = (9.12,'kcal/mol'),
        S298 = (22.01,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "1,2,4-trithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   S     u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.78,-9.58,-7.37,-5.67,-3.5,-2.26,-0.71],'cal/(mol*K)'),
        H298 = (4.4,'kcal/mol'),
        S298 = (24.39,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "tetrathiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   S     u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.82,-8.46,-7.22,-6.33,-5.17,-4.28,-2.4],'cal/(mol*K)'),
        H298 = (10.72,'kcal/mol'),
        S298 = (26.56,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "pentathiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   S u0 {3,S} {5,S}
5   S u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.87,-8.3,-7.89,-7.72,-7.45,-6.84,-4.46],'cal/(mol*K)'),
        H298 = (10.99,'kcal/mol'),
        S298 = (30.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "Pyrrolidine",
    group = 
"""
1 * N      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17,-5.58,-4.8,-4,-2.87,-2.17,0],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (26.7,'cal/(mol*K)'),
    ),
    shortDesc = """Pyrrolidine ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "methylenecyclopentane",
    group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
6   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.861,-4.909,-3.91,-3.01,-1.769,-0.969,0],'cal/(mol*K)'),
        H298 = (5.21,'kcal/mol'),
        S298 = (24.6287,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "Fulvene",
    group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cd,N] u0 {3,S} {5,D}
5   [Cd,N] u0 {1,S} {4,D}
6   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.376,-3.662,-3.634,-3.412,-3.209,-2.823,-2.737],'cal/(mol*K)'),
        H298 = (9.06,'kcal/mol'),
        S298 = (33.947,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fit to CBS-QB3 calculations of fulvene thermo in vinylCPD_H and Fulvene_H libraries
""",
)

entry(
    index = 335,
    label = "3-Methylenecyclopentene",
    group = 
"""
1 * [Cs,N] u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {4,S}
3   Cd     u0 {1,S} {5,S} {6,D}
4   [Cd,N] u0 {2,S} {5,D}
5   [Cd,N] u0 {3,S} {4,D}
6   [Cd,N] u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.8,-4.4,-3.7,-2.7,-2,-0.9],'cal/(mol*K)'),
        H298 = (6.2,'kcal/mol'),
        S298 = (28.9,'cal/(mol*K)'),
    ),
    shortDesc = """Copied from 4-methylenecyclopentene""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "4-Methylenecyclopentene",
    group = 
"""
1 * [Cs,N] u0 {3,S} {4,S}
2   [Cs,N] u0 {3,S} {5,S}
3   Cd     u0 {1,S} {2,S} {6,D}
4   [Cd,N] u0 {1,S} {5,D}
5   [Cd,N] u0 {2,S} {4,D}
6   [Cd,N] u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.8,-4.4,-3.7,-2.7,-2,-0.9],'cal/(mol*K)'),
        H298 = (6.2,'kcal/mol'),
        S298 = (28.9,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "12methylenecyclopentane",
    group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   Cd     u0 {1,S} {3,S} {7,D}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
6   [Cd,N] u0 {1,D}
7   [Cd,N] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.844,-5.197,-4.882,-4.175,-2.988,-2.088,-0.655],'cal/(mol*K)'),
        H298 = (6.67,'kcal/mol'),
        S298 = (31.384,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "SixMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {6,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D,T]}
4   R!H u0 {3,[S,D,T]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D,T]}
6   R!H u0 {1,[S,D]} {5,[S,D,T]}
""",
    thermo = 'Cyclohexane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "sixnosidedouble",
    group = 
"""
1 * [Cs,O2s,N,S2s] u0 {2,S} {6,S}
2   [Cs,O2s,N,S2s] u0 {1,S} {3,S}
3   [Cs,O2s,N,S2s] u0 {2,S} {4,S}
4   [Cs,O2s,N,S2s] u0 {3,S} {5,S}
5   [Cs,O2s,N,S2s] u0 {4,S} {6,S}
6   [Cs,O2s,N,S2s] u0 {1,S} {5,S}
""",
    thermo = 'Cyclohexane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "Cyclohexane",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.8,-4.1,-2.9,-1.3,1.08,2.16,3],'cal/(mol*K)'),
        H298 = (0.08,'kcal/mol'),
        S298 = (18.1277,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclohexane ring BENSON https:""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "12dioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.66,-5.11,-4.17,-3.36,-2.52,-2.4,2.76],'cal/(mol*K)'),
        H298 = (3.9,'kcal/mol'),
        S298 = (19.6424,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "1,3-Dioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2 * Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.28,-5.951,-4.458,-3.15,-1.967,-0.83,6.799],'cal/(mol*K)'),
        H298 = (1.88,'kcal/mol'),
        S298 = (16.1924,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Dioxane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "1,4-Dioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3 * O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.6,-5,-3.8,-2.6,-1.5,-0.4,8.9],'cal/(mol*K)'),
        H298 = (3.4,'kcal/mol'),
        S298 = (17.8049,'cal/(mol*K)'),
    ),
    shortDesc = """1,4-Dioxane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "1,3,5-Trioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.01,-5.719,-3.632,-2.189,-1.525,-0.624,7.031],'cal/(mol*K)'),
        H298 = (4.09,'kcal/mol'),
        S298 = (16.1953,'cal/(mol*K)'),
    ),
    shortDesc = """1,3,5-Trioxane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "124trioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.68,-4.07,-2.95,-2.09,-1.73,-1.8,5.2],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (19.9,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "123trioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.08,-2.81,-2.55,-1.93,-1.55,-1.9,3.09],'cal/(mol*K)'),
        H298 = (4.87,'kcal/mol'),
        S298 = (17.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "Oxane",
    group = 
"""
1 * Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-5.5,-4.2,-3,-1.6,-0.5,4.9],'cal/(mol*K)'),
        H298 = (0.7,'kcal/mol'),
        S298 = (18.8,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "hexasulfur",
    group = 
"""
1 * S2s u0 {2,S} {6,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-0.16,-5.5,-6.91,-8.91,-9.24,-7.14],'cal/(mol*K)'),
        H298 = (6.1,'kcal/mol'),
        S298 = (4.36,'cal/(mol*K)'),
    ),
    shortDesc = """All from NIST-JANAF table""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "Piperidine",
    group = 
"""
1 * N  u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17,-5.58,-4.8,-4,-2.87,-2.17,0],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (26.7,'cal/(mol*K)'),
    ),
    shortDesc = """Piperidine ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "six-sidedoubles",
    group = 
"""
1   [C,O]   u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [C,O]   u0 {2,S} {4,S}
4   [C,O]   u0 {3,S} {5,S}
5   [C,O]   u0 {4,S} {6,S}
6   [C,O]   u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10,10,10,10,10,10,0],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (10,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "six-onesidedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'Cyclohexanone',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "Cyclohexanone",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.4,-3.9,-2.3,-1,0.1,0.9,0],'cal/(mol*K)'),
        H298 = (1.29,'kcal/mol'),
        S298 = (19.1,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclohexanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "sixmembd-allsingles-twosidedoubles-para",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cd,CO]  u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = '14methylenecyclohexane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "14methylenecyclohexane",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,S} {7,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,S} {8,D}
6   Cs u0 {1,S} {5,S}
7   Cd u0 {2,D}
8   Cd u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-5.349,-4.468,-3.521,-2.203,-1.238,0.384],'cal/(mol*K)'),
        H298 = (1.23,'kcal/mol'),
        S298 = (15.7314,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "sixmembd-allsingles-twosidedoubles-ortho",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cd,CO]  u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'six-sidedoubles',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "sixmembd-allsingles-twosidedoubles-meta",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cd,CO]  u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'six-sidedoubles',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "six-inringonedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'Cyclohexene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "34dihydro12dioxin",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5 * Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.7,-4.9,-4.3,-3.7,-3.11,-2.62,0.62],'cal/(mol*K)'),
        H298 = (1.07,'kcal/mol'),
        S298 = (20.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "36dihydro2hpyran",
    group = 
"""
1 * Cd  u0 {2,S} {6,D}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cd  u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.4,-4,-3,-2.2,-1.5,-0.8,2.3],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (19.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "Cyclohexene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.1,-4.3,-3.3,-2.5,-1.4,-0.7,0.4],'cal/(mol*K)'),
        H298 = (1.17,'kcal/mol'),
        S298 = (21.2114,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclohexene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "3,4-Dihydro-2H-pyran",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5 * Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.26,-6.496,-5.96,-5.142,-3.74,-2.915,0.529],'cal/(mol*K)'),
        H298 = (3.94,'kcal/mol'),
        S298 = (22.01,'cal/(mol*K)'),
    ),
    shortDesc = """3,4-Dihydro-2H-pyran ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "36dihydro12dioxin",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2 * Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cs  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.45,-4.66,-3.81,-3.16,-2.65,-2.68,-1.53],'cal/(mol*K)'),
        H298 = (3.32,'kcal/mol'),
        S298 = (18.72,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "24dihydro13dioxin",
    group = 
"""
1   Cd  u0 {2,D} {6,S}
2 * Cd  u0 {1,D} {3,S}
3   Cs  u0 {2,S} {4,S}
4   O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-5.1,-4.2,-3.4,-2.8,-2.3,0.9],'cal/(mol*K)'),
        H298 = (3.1,'kcal/mol'),
        S298 = (20.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "23dihydro14dioxin",
    group = 
"""
1   Cd  u0 {2,D} {6,S}
2 * Cd  u0 {1,D} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.3,-7.5,-7.5,-6.9,-5.5,-4.9,0.7],'cal/(mol*K)'),
        H298 = (7.9,'kcal/mol'),
        S298 = (19.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "124trioxene",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51,-5.86,-5.48,-4.98,-4.44,-4.15,-0.75],'cal/(mol*K)'),
        H298 = (6.98,'kcal/mol'),
        S298 = (24.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "123trioxene",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73,-2.67,-2.62,-2.27,-2.14,-2.08,-0.97],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (21.57,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "six-inringtwodouble-13",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   Cd       u0 {3,S} {5,D}
5   Cd       u0 {4,D} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = '1,3-Cyclohexadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "1,3-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.8,-4.7,-4.2,-3.5,-2.5,-1.8,-0.7],'cal/(mol*K)'),
        H298 = (3.78,'kcal/mol'),
        S298 = (23.9824,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Cyclohexadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "six-inringtwodouble-14",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = '1,4-Cyclohexadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "1,4-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4,-3.2,-2.6,-1.9,-1.2,-0.8,0.2],'cal/(mol*K)'),
        H298 = (0.52,'kcal/mol'),
        S298 = (25.3849,'cal/(mol*K)'),
    ),
    shortDesc = """1,4-Cyclohexadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "14dioxin",
    group = 
"""
1   Cd  u0 {2,D} {6,S}
2   Cd  u0 {1,D} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.9,-7.5,-7.5,-7.5,-6.8,-5.6,-4.2],'cal/(mol*K)'),
        H298 = (11.71,'kcal/mol','+|-',-2.9),
        S298 = (27.6,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "six-inringthreedouble_124",
    group = 
"""
1   R!H u0 {2,D} {6,S}
2 * Cdd u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,D}
6   R!H u0 {1,S} {5,D}
""",
    thermo = '124cyclohexatriene',
    shortDesc = """""",
    longDesc = 
"""
Use 124cyclohexatriene correction for any 6-membered ring that contains at least 3 double bonds in the 1,2 and 4 p
positions.
""",
)

entry(
    index = 373,
    label = "124cyclohexatriene",
    group = 
"""
1   Cd       u0 {2,D} {6,S}
2 * Cdd      u0 {1,D} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.21,-4.32,-3.9,-3.46,-2.71,-2.25,-1.38],'cal/(mol*K)'),
        H298 = (36.04,'kcal/mol'),
        S298 = (26.47,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 isodesmic reaction approach C1=CC=CCC=1 + 3 ethane + ethene = allene + 2 2-butene + propane""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "six-inringthreedouble_123",
    group = 
"""
1   Cdd u0 {2,D} {6,D}
2 * Cdd u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {1,D} {5,[S,D]}
""",
    thermo = '123cyclohexatriene',
    shortDesc = """""",
    longDesc = 
"""
Use 123cyclohexatriene correction for any 6-membered ring that contains at least 3 double bonds in the 1,2 and 3
positions.
""",
)

entry(
    index = 375,
    label = "123cyclohexatriene",
    group = 
"""
1   Cdd u0 {2,D} {6,D}
2 * Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cd  u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.033,-4.022,-3.919,-3.755,-3.149,-2.312,-1.645],'cal/(mol*K)'),
        H298 = (50.291,'kcal/mol'),
        S298 = (27.334,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to M06 calculations
""",
)

entry(
    index = 376,
    label = "six-inringtwodouble-12",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   C        u0 {2,D} {4,D}
4   Cd       u0 {3,D} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10,10,10,10,10,10,10],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (10,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "six-oneside-twoindoubles-25",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2   Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4 * [Cd,CO]  u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = '14cyclohexadiene3methylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "25cyclohexadienone",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4,-3.4,-3.1,-2.6,-2,-1.9,-0.3],'cal/(mol*K)'),
        H298 = (2.9,'kcal/mol'),
        S298 = (25.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "14cyclohexadiene3methylene",
    group = 
"""
1   Cd u0 {2,D} {6,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * Cd u0 {1,S} {5,S} {7,D}
7   Cd u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.71,-2.829,-2.749,-2.625,-2.174,-1.591,-1.484],'cal/(mol*K)','+|-',[0.3481,0.3481,0.3481,0.3481,0.3481,0.3481,0.3481]),
        H298 = (-3.253,'kcal/mol','+|-',2.9353),
        S298 = (26.101,'cal/(mol*K)','+|-',0.5184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations, 02/2019, Lawrence Lai
Model species is 1,4-cyclohexadiene-3-methylene
""",
)

entry(
    index = 380,
    label = "six-oneside-twoindoubles-24",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2   Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   Cd       u0 {3,S} {5,D}
5   Cd       u0 {4,D} {6,S}
6 * [Cd,CO]  u0 {1,S} {5,S}
""",
    thermo = '13cyclohexadiene5methylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "24cyclohexadienone",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * CO u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.6,-4.3,-4.4,-4.1,-3.5,-3.3,0.3],'cal/(mol*K)'),
        H298 = (3.3,'kcal/mol'),
        S298 = (29.7,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "13cyclohexadiene5methylene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * Cd u0 {1,S} {5,S} {7,D}
7   Cd u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.182,-6.383,-6.343,-5.497,-3.657,-2.381,-1.242],'cal/(mol*K)','+|-',[0.3969,0.3969,0.3969,0.3969,0.3969,0.3969,0.3969]),
        H298 = (5.22,'kcal/mol','+|-',3.016),
        S298 = (27.698,'cal/(mol*K)','+|-',0.5184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations, 02/2019, Lawrence Lai
Model species is 1,3-cyclohexadiene-5-methylene
""",
)

entry(
    index = 383,
    label = "six-twoin13-twoout",
    group = 
"""
1   [CO,Cd] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6 * [Cd,CO] u0 {1,S} {5,S}
""",
    thermo = 'oxylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "fg6",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,S} {7,D}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.597,-6.43,-6.331,-5.573,-4.198,-3.361,-1.155],'cal/(mol*K)'),
        H298 = (-4.62,'kcal/mol'),
        S298 = (28.901,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "oxylene",
    group = 
"""
1 * Cd u0 {5,S} {6,S} {8,D}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   Cd u0 {1,S} {2,S} {7,D}
7   Cd u0 {6,D}
8   Cd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.078,-2.192,-2.249,-2.275,-2.541,-2.331,-2.797],'cal/(mol*K)'),
        H298 = (4.16,'kcal/mol'),
        S298 = (32.519,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "obenzoquinone",
    group = 
"""
1 * CO u0 {5,S} {6,S}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   CO u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.887,-3.225,-3.233,-2.897,-2.4,-2.365,-0.077],'cal/(mol*K)'),
        H298 = (11,'kcal/mol'),
        S298 = (25.331,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "six-twoin14-twoout",
    group = 
"""
1   [Cd,CO] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4 * [Cd,CO] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    thermo = 'pxylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "pbenzoquinone",
    group = 
"""
1 * CO u0 {4,S} {5,S}
2   Cd u0 {5,D} {6,S}
3   Cd u0 {4,D} {6,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,S} {2,D}
6   CO u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.957,-3.282,-3.278,-2.934,-2.427,-2.627,-0.312],'cal/(mol*K)'),
        H298 = (15.52,'kcal/mol'),
        S298 = (24.9239,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "pxylene",
    group = 
"""
1 * Cd u0 {4,S} {5,S} {6,D}
2   Cd u0 {5,D} {7,S}
3   Cd u0 {4,D} {7,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,S} {2,D}
6   Cd u0 {1,D}
7   Cd u0 {2,S} {3,S} {8,D}
8   Cd u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.139,-2.309,-2.384,-2.407,-2.643,-2.403,-2.826],'cal/(mol*K)'),
        H298 = (1.16,'kcal/mol'),
        S298 = (31.3499,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "3,4-dimethylenecyclohexene",
    group = 
"""
1 * C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   Cd u0 {1,S} {4,S} {7,D}
4   Cd u0 {3,S} {6,S} {8,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1,-2.2,-2.2,-2.3,-2.5,-2.3,-0.3],'cal/(mol*K)'),
        H298 = (4.2,'kcal/mol'),
        S298 = (32.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "six-inringonetriple",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = 'cyclohexyne',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohexyne correction for any 6-membered ring containing 1 triple bond
""",
)

entry(
    index = 392,
    label = "cyclohexyne",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   [C,O2s] u0 {2,S} {4,S}
4   [C,O2s] u0 {3,S} {5,S}
5   [C,O2s] u0 {4,S} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.306,-2.849,-2.452,-2.229,-1.543,-0.932,-2.535],'cal/(mol*K)'),
        H298 = (39.857,'kcal/mol'),
        S298 = (21.862,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for cyclohexyne
""",
)

entry(
    index = 393,
    label = "six-inringonetripleonedouble-13",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,S}
5   R!H u0 {4,S} {6,[S,D]}
6   R!H u0 {1,S} {5,[S,D]}
""",
    thermo = 'cyclohex_1_yne_3_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and one double bond in the 1,3-positions.
""",
)

entry(
    index = 394,
    label = "cyclohex_1_yne_3_ene",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   Cd      u0 {2,S} {4,D}
4   Cd      u0 {3,D} {5,S}
5   [C,O2s] u0 {4,S} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.292,-2.038,-2.856,-3.187,-2.814,-1.639,-2.564],'cal/(mol*K)'),
        H298 = (48.034,'kcal/mol'),
        S298 = (25.6327,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for cyclohex_1_yne_3_ene
""",
)

entry(
    index = 395,
    label = "o_benzyne",
    group = 
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.003,-4.523,-5.242,-5.892,-5.423,-3.742,-3.198],'cal/(mol*K)'),
        H298 = (26.527,'kcal/mol'),
        S298 = (29.264,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for o_benzyne
""",
)

entry(
    index = 396,
    label = "six-inringonetripleonedouble-14",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,D}
5   R!H u0 {4,D} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = 'cyclohex_1_yne_4_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_4_ene correction for any 6-membered ring containing at least one triple bond
and one double bond in the 1,4-positions.
""",
)

entry(
    index = 397,
    label = "cyclohex_1_yne_4_ene",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   [C,O2s] u0 {2,S} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.431,-0.775,-1.308,-1.515,-1.294,-0.369,-1.036],'cal/(mol*K)'),
        H298 = (38.484,'kcal/mol'),
        S298 = (25.2137,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for cyclohex_1_yne_4_ene
""",
)

entry(
    index = 398,
    label = "six-inringonetripletwodouble-134",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,D}
5   R!H u0 {4,D} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = 'cyclohex_1_yne_3_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and two double bonds in the 1,3,4-positions.
""",
)

entry(
    index = 399,
    label = "six-inringonetriplethreedouble-1345",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,D}
5   R!H u0 {4,D} {6,D}
6   R!H u0 {1,S} {5,D}
""",
    thermo = 'cyclohex_1_yne_3_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and three double bonds in the 1,3,4,5-positions.
""",
)

entry(
    index = 400,
    label = "six-inringtwotriple-13",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   Ct  u0 {2,S} {4,T}
4   Ct  u0 {3,T} {5,S}
5   R!H u0 {4,S} {6,[S,D,T]}
6   R!H u0 {1,S} {5,[S,D,T]}
""",
    thermo = '1_3_cyclohexadiyne',
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Use 1_3_cyclohexadiyne correction for any six-membered  ring with at least two triple bonds
""",
)

entry(
    index = 401,
    label = "1_3_cyclohexadiyne",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   Ct      u0 {2,S} {4,T}
4   Ct      u0 {3,T} {5,S}
5   [C,O2s] u0 {4,S} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.086,-1.458,-1.692,-1.747,-1.465,-1.403,-3.712],'cal/(mol*K)'),
        H298 = (103.484,'kcal/mol'),
        S298 = (31.221,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for 1_3_cyclohexadiyne
""",
)

entry(
    index = 402,
    label = "SevenMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {7,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    thermo = 'Cycloheptane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "Cycloheptane",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.1,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.4,'kcal/mol'),
        S298 = (15.9,'cal/(mol*K)'),
    ),
    shortDesc = """Cycloheptane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "Cycloheptene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.1,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (5.4,'kcal/mol'),
        S298 = (15.6,'cal/(mol*K)'),
    ),
    shortDesc = """Cycloheptene ring BENSON Cp 300K copied from cycloheptane""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "1,3-Cycloheptadiene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Cycloheptadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "1,3,5-Cycloheptatriene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.7,'kcal/mol'),
        S298 = (23.7,'cal/(mol*K)'),
    ),
    shortDesc = """1,3,5-Cycloheptatriene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "Cycloheptanone",
    group = 
"""
1 * CO u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cycloheptanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "1,4-Cycloheptadiene",
    group = 
"""
1 * C  u0 {2,D} {7,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.1,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.3,'kcal/mol'),
        S298 = (15.9,'cal/(mol*K)'),
    ),
    shortDesc = """Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cycloheptane""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "seven-inringtwodouble-12",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,S} {6,[S,D]}
""",
    thermo = '1_2_cycloheptadiene',
    shortDesc = """""",
    longDesc = 
"""
Use 1_2_cycloheptadiene correction for any seven membered ring with at least two double bonds in the 1,2-positions
""",
)

entry(
    index = 410,
    label = "1_2_cycloheptadiene",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   C   u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.058,-4.616,-4.065,-3.549,-2.425,-1.185,-0.012],'cal/(mol*K)'),
        H298 = (19.726,'kcal/mol'),
        S298 = (17.979,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 411,
    label = "1,2,4,6-Cycloheptatetraene",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   Cd  u0 {5,S} {7,D}
7   Cd  u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-7.5,-7.3,-6.5,-4.9,-3.7,-2.2],'cal/(mol*K)'),
        H298 = (23.9,'kcal/mol'),
        S298 = (25.5,'cal/(mol*K)'),
    ),
    shortDesc = """AG Vandeputte""",
    longDesc = 
"""
CBS-QB3 isodesmic reaction approach C7H6 + 4 ethene = allene + 3 butadiene
""",
)

entry(
    index = 412,
    label = "seven-inringthreedouble-123",
    group = 
"""
1 * R!H u0 {2,D} {7,[S,D]}
2   Cdd u0 {1,D} {3,D}
3   Cdd u0 {2,D} {4,D}
4   R!H u0 {3,D} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    thermo = '1_2_3_cycloheptatriene',
    shortDesc = """""",
    longDesc = 
"""
Use 1_2_3_cycloheptatriene correction for any seven membered ring with at least three double bonds in the 1,2 and 3-positions
""",
)

entry(
    index = 413,
    label = "1_2_3_cycloheptatriene",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cdd u0 {2,D} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   C   u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.854,-4.544,-4.148,-3.726,-2.801,-1.852,-0.8],'cal/(mol*K)'),
        H298 = (25.76,'kcal/mol'),
        S298 = (22.122,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 414,
    label = "seven-inringonetriple",
    group = 
"""
1 * Ct  u0 {2,T} {7,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,S} {6,[S,D]}
""",
    thermo = 'cycloheptyne',
    shortDesc = """""",
    longDesc = 
"""
Use cycloheptyne correction for any seven membered ring with at least one triple bond
""",
)

entry(
    index = 415,
    label = "cycloheptyne",
    group = 
"""
1 * Ct u0 {2,T} {7,S}
2   Ct u0 {1,T} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-3.568,-3.106,-2.646,-1.582,-0.695,-1.916],'cal/(mol*K)'),
        H298 = (24.448,'kcal/mol'),
        S298 = (17.688,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 416,
    label = "heptasulfur",
    group = 
"""
1 * S2s u0 {2,S} {7,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {5,S} {7,S}
7   S2s u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-9.91,-9.2,-8.99,-8.5,-7.55,-3.9],'cal/(mol*K)'),
        H298 = (-0.44,'kcal/mol'),
        S298 = (8.52,'cal/(mol*K)'),
    ),
    shortDesc = """All from NIST-JANAF table""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "oxepane",
    group = 
"""
1 * C   u0 {2,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   O2s u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-5.33,-3.85,-2.52,-0.92,0.26,5.83],'cal/(mol*K)'),
        H298 = (6.54,'kcal/mol'),
        S298 = (17.14,'cal/(mol*K)'),
    ),
    shortDesc = """Calculation: Mixture of two twist chair formations""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "EightMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {8,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {1,[S,D]} {7,[S,D]}
""",
    thermo = 'Cyclooctane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "Cyclooctane",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.8,-7.5,-5.9,-4.5,-2.3,-0.8,1.4],'cal/(mol*K)'),
        H298 = (10.5,'kcal/mol'),
        S298 = (16.63,'cal/(mol*K)'),
    ),
    shortDesc = """Updated AG Vandeputte (good agreement with BENSON correction but explicit for cyclooctane from CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp, results in perfect agreement with calculations of Dorofeeva et al.)""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "cis-Cyclooctene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-5.8,-4.6,-3.4,-1.8,-0.7,1.2],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (13.01,'cal/(mol*K)'),
    ),
    shortDesc = """Updated AG Vandeputte (CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp)""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "1,3,5-Cyclooctatriene",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.3,-3.3,-2.5,-1.3,-0.5,1],'cal/(mol*K)'),
        H298 = (8.9,'kcal/mol'),
        S298 = (13.89,'cal/(mol*K)'),
    ),
    shortDesc = """1,3,5-Cyclooctatriene ring BENSON, S and cp from 1,4-cyclooctadiene""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "Cyclooctatetraene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.3,-3.3,-2.5,-1.3,-0.5,1],'cal/(mol*K)'),
        H298 = (17.1,'kcal/mol'),
        S298 = (13.89,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclooctatetraene ring BENSON, S and cp from 1,4-cyclooctadiene""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "Cyclooctanone",
    group = 
"""
1 * CO u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclooctanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "1,3-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = '1,4-cyclooctadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "1,4-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.3,-3.3,-2.5,-1.3,-0.5,1],'cal/(mol*K)'),
        H298 = (8.2,'kcal/mol'),
        S298 = (13.89,'cal/(mol*K)'),
    ),
    shortDesc = """Updated AG Vandeputte (CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp)""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "1,5-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = '1,4-cyclooctadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "octasulfur",
    group = 
"""
1 * S2s u0 {2,S} {8,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {5,S} {7,S}
7   S2s u0 {6,S} {8,S}
8   S2s u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56,-10.72,-9.9,-9.63,-9.1,-8.08,-4.19],'cal/(mol*K)'),
        H298 = (-10.14,'kcal/mol'),
        S298 = (2.42,'cal/(mol*K)'),
    ),
    shortDesc = """All from NIST-JANAF table""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "NineMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {9,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {7,[S,D]} {9,[S,D]}
9   R!H u0 {1,[S,D]} {8,[S,D]}
""",
    thermo = 'Cyclononane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "Cyclononane",
    group = 
"""
1 * Cs u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (12.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclononane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "Cyclononanone",
    group = 
"""
1 * CO u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclononanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "TenMember",
    group = 
"""
1  * R!H u0 {2,[S,D]} {10,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {1,[S,D]} {9,[S,D]}
""",
    thermo = 'Cyclodecane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "Cyclodecane",
    group = 
"""
1  * Cs u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (12.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclodecane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "Cyclodecanone",
    group = 
"""
1  * CO u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclodecanone ring BENSON""",
    longDesc = 
"""

""",
)

tree(
"""
L1: Ring
    L2: Aromatic
        L3: Benzene
    L2: ThreeMember
        L3: Cyclopropane
            L4: Cs-Cs-Cs(C-BrBrBr)
            L4: Cs-Cs-Cs(Br)(C)
            L4: Cs-Cs(C)-Cs(Br)
            L4: Cs(C)-Cs-Cs(Br)(Br)
            L4: Cs-Cs-Cs(Br)
                L5: Cs-Cs-Cs(Br)(Br)
                L5: Cs-Cs(Br)(O2)-Cs
            L4: Cs-Cs-Cs(C-BrBr)
            L4: Cs-Cs(C-Br)-Cs
            L4: Cs-Cs-Cs(C-Cl)
                L5: Cs-Cs(C-ClClCl)-Cs
                L5: Cs(C-ClCl)-Cs-Cs
            L4: Cs(Cl)-Cs-Cs
                L5: Cs-Cs-Cs(Cl)(O2)
                L5: Cs-Cs(C)-Cs(Cl)(Cl)
                L5: Cs(Cl)-Cs-Cs(O2)
                L5: Cs(O2)-Cs-Cs(Cl)(Cl)
                L5: Cs-Cs-Cs(Cl)(C)
                L5: Cs-Cs(Cl)-Cs(C)
                L5: Cs-Cs(Cl)(Cl)-Cs
            L4: Cs-Cs(F)(F)-Cs
                L5: Cs-Cs(F)(F)-Cs(O2)
                L5: Cs(F)(F)-Cs(C)-Cs
            L4: Cs(C)-Cs-Cs(F)
            L4: Cs-Cs(F)(C)-Cs
            L4: Cs(F)-Cs-Cs(O2)
            L4: Cs-Cs(C-FFF)-Cs
            L4: Cs-Cs(F)(O2)-Cs
            L4: Cs(F)-Cs-Cs
            L4: Cs-Cs(C-FF)-Cs
            L4: Cs(C-F)-Cs-Cs
        L3: oxirene
        L3: Cyclopropene
            L4: Cd(O2)-Cs-Cd(Br)
            L4: Cd(C)-Cs-Cd(Br)
            L4: Cd-Cs-Cd(Br)
            L4: Cs-Cd-Cd(C-Cl)
                L5: Cs-Cd-Cd(C-ClClCl)
            L4: Cs-Cd(Cl)-Cd(O2)
            L4: Cs(O2)-Cd-Cd(Cl)
            L4: Cs-Cd(Cl)-Cd(C)
            L4: Cs-Cd(F)-Cd
                L5: Cd-Cd(F)-Cs(O2)
                L5: Cs-Cd(C)-Cd(F)
            L4: Cd-Cs-Cd(C-FF)
            L4: Cd-Cs-Cd(C-F)
        L3: Cyclopropene2
            L4: Cd(C)-Cd-Cs(Br)(Br)
            L4: Cd-Cs(C-BrBr)-Cd
                L5: Cs(C-BrBrBr)-Cd-Cd
            L4: Cd-Cs(C-Br)-Cd
            L4: Cs(C)-Cd(Br)-Cd
            L4: Cd-Cd-Cs(Br)(O2)
            L4: Cd-Cd-Cs(Br)(Br)
                L5: Cd(O2)-Cs(Br)(Br)-Cd
            L4: Cd-Cd-Cs(Br)
                L5: Cs(Br)-Cd(C)-Cd
                L5: Cd-Cd(O2)-Cs(Br)
                L5: Cd-Cd-Cs(Br)(C)
            L4: Cs-Cd-Cd(C-Br)
                L5: Cd-Cs-Cd(C-BrBrBr)
                L5: Cd(C-BrBr)-Cd-Cs
            L4: Cs(O2)-Cd-Cd(Br)
            L4: Cd-Cd-Cs(C-ClCl)
                L5: Cd-Cd-Cs(C-ClClCl)
            L4: Cd-Cs-Cd(Cl)
            L4: Cd-Cd(Cl)-Cs(C)
            L4: Cd-Cs(Cl)(C)-Cd
            L4: Cd-Cd-Cs(Cl)
                L5: Cs(Cl)-Cd-Cd(O2)
                    L6: Cd(O2)-Cs(Cl)(Cl)-Cd
                L5: Cs(Cl)(Cl)-Cd-Cd
                L5: Cd-Cs(Cl)(O2)-Cd
                L5: Cd-Cd(C)-Cs(Cl)
            L4: Cs(C-Cl)-Cd-Cd
            L4: Cd-Cs(F)(C)-Cd
            L4: Cd(C)-Cd-Cs(F)
                L5: Cd-Cd(C)-Cs(F)(F)
            L4: Cd-Cs(C-FFF)-Cd
            L4: Cd-Cd-Cs(C-FF)
            L4: Cs(F)(O2)-Cd-Cd
            L4: Cd-Cs(F)-Cd
                L5: Cs(F)(F)-Cd-Cd(O2)
                L5: Cs(F)-Cd-Cd(O2)
                L5: Cd-Cd-Cs(F)(F)
            L4: Cd(C-FF)-Cd-O2s
            L4: Cd-Cd-Cs(C-F)
            L4: Cd-Cd(F)-Cs(C)
            L4: Cd(F)-Cd(O2)-Cs
        L3: Cyclopropadiene
        L3: Cyclopropadiene2
        L3: Cyclopropyne
        L3: Cyclopropatriene
        L3: Ethylene_oxide
            L4: O2s-Cs(Br)-Cs(O2)
                L5: O2s-Cs(Br)(Br)-Cs(O2)
            L4: O2s-Cs(C)-Cs(Br)(Br)
            L4: O2s-Cs(C-BrBrBr)-Cs
            L4: O2s-Cs(Br)(C)-Cs
            L4: O2s-Cs-Cs(Br)
                L5: O2s-Cs-Cs(Br)(Br)
                L5: Cs(C)-Cs(Br)-O2s
                L5: Cs-Cs(Br)(O2)-O2s
            L4: Cs(C-BrBr)-Cs-O2s
            L4: Cs(C-Br)-Cs-O2s
            L4: Cs(C-Cl)-Cs-O2s
                L5: O2s-Cs-Cs(C-ClClCl)
                L5: O2s-Cs(C-ClCl)-Cs
            L4: Cs-O2s-Cs(Cl)
                L5: Cs(O2)-O2s-Cs(Cl)(Cl)
                L5: Cs-O2s-Cs(Cl)(O2)
                L5: Cs(Cl)-O2s-Cs(O2)
                L5: Cs(Cl)-O2s-Cs(C)
                    L6: Cs(Cl)(Cl)-O2s-Cs(C)
                L5: Cs-O2s-Cs(Cl)(C)
                L5: Cs(Cl)(Cl)-Cs-O2s
            L4: O2s-Cs-Cs(C-FFF)
            L4: Cs(F)(O2)-O2s-Cs
            L4: Cs(O2)-O2s-Cs(F)
                L5: Cs(O2)-Cs(F)(F)-O2s
            L4: O2s-Cs-Cs(F)(F)
                L5: Cs(C)-Cs(F)(F)-O2s
            L4: Cs(F)(C)-Cs-O2s
            L4: O2s-Cs(F)-Cs(C)
            L4: Cs-Cs(F)-O2s
            L4: Cs(C-F)-Cs-O2s
                L5: Cs(C-FF)-Cs-O2s
        L3: dioxirane
            L4: O2s-O2s-Cs(Br)(C)
            L4: Cs(C-BrBr)-O2s-O2s
                L5: Cs(C-BrBrBr)-O2s-O2s
            L4: O2s-Cs(C-Br)-O2s
            L4: O2s-Cs(Br)-O2s
                L5: O2s-O2s-Cs(Br)(Br)
            L4: O2s-Cs(C-ClClCl)-O2s
            L4: O2s-O2s-Cs(C-ClCl)
            L4: O2s-Cs(Cl)(C)-O2s
            L4: Cs(Cl)(Cl)-O2s-O2s
            L4: O2s-O2s-Cs(Cl)
            L4: Cs(C-Cl)-O2s-O2s
            L4: O2s-O2s-Cs(C-F)
                L5: O2s-O2s-Cs(C-FF)
                    L6: Cs(C-FFF)-O2s-O2s
            L4: O2s-O2s-Cs(F)
                L5: O2s-O2s-Cs(F)(C)
                L5: O2s-Cs(F)(F)-O2s
        L3: 2(co)oxirane
            L4: O2s-CO(O2d)-Cs(Br)
                L5: CO(O2d)-O2s-Cs(Br)(Br)
        L3: cyclopropanedione
        L3: cyclopropenone
            L4: Cd(Br)-CO(O2d)-Cd
            L4: Cd-Cd(Cl)-CO(O2d)
            L4: CO(O2d)-Cd-Cd(F)
        L3: thiirane
        L3: dithiirane
        L3: trithiirane
        L3: thiirene
        L3: Ethyleneimine
        L3: Methylene_cyclopropane
            L4: Cs-Cd(Cd)-Cs(Br)(Br)
            L4: Cs-Cd(Cd-BrBr)-Cs
            L4: Cd(Cd-Br)-Cs-Cs
            L4: Cs-Cd(Cd)-Cs(Br)
            L4: Cs-Cd(Cd)-Cs(Cl)
                L5: Cs-Cs(Cl)(Cl)-Cd(Cd)
            L4: Cs-Cd(Cd-ClCl)-Cs
            L4: Cs-Cs-Cd(Cd-Cl)
            L4: Cs-Cs(F)(F)-Cd(Cd)
            L4: Cd(Cd-F)-Cs-Cs
                L5: Cs-Cd(Cd-FF)-Cs
            L4: Cd(Cd)-Cs-Cs(F)
        L3: cyclopropanone
            L4: Cs-CO(O2d)-Cs(Br)(Br)
            L4: Cs-Cs(Br)-CO(O2d)
            L4: Cs-CO(O2d)-Cs(Cl)
                L5: Cs-CO(O2d)-Cs(Cl)(Cl)
            L4: O2s-Cs(Cl)-CO(O2d)
                L5: O2s-CO(O2d)-Cs(Cl)(Cl)
            L4: CO(O2d)-O2s-Cs(F)(F)
            L4: CO(O2d)-Cs-Cs(F)
                L5: Cs(F)(F)-Cs-CO(O2d)
            L4: O2s-CO(O2d)-Cs(F)
        L3: methylenecyclopropene
            L4: Cd(Cd)-Cd-Cd(Br)
            L4: Cd-Cd-Cd(Cd-Br)
                L5: Cd-Cd-Cd(Cd-BrBr)
            L4: Cd(Cd)-Cd(Cl)-Cd
            L4: Cd-Cd-Cd(Cd-ClCl)
            L4: Cd-Cd(Cd-Cl)-Cd
            L4: Cd(F)-Cd-Cd(Cd)
            L4: Cd-Cd-Cd(Cd-F)
                L5: Cd-Cd(Cd-FF)-Cd
        L3: methylenecyclopropanone
        L3: methyleneoxirane
            L4: Cs-O2s-Cd(Cd-BrBr)
            L4: Cs(Br)-O2s-Cd(Cd)
                L5: Cs(Br)(Br)-O2s-Cd(Cd)
            L4: Cd(Cd-Br)-Cs-O2s
            L4: Cd(Cd)-O2s-Cs(Cl)(Cl)
            L4: Cs-Cd(Cd-ClCl)-O2s
            L4: Cs-O2s-Cd(Cd-Cl)
            L4: Cs(Cl)-Cd(Cd)-O2s
            L4: O2s-Cs(F)(F)-Cd(Cd)
            L4: Cd(Cd-F)-Cs-O2s
                L5: O2s-Cs-Cd(Cd-FF)
            L4: Cs(F)-Cd(Cd)-O2s
        L3: 12Methylenecyclopropane
        L3: O2s-O2s-Cd(Cd-Br)
            L4: O2s-O2s-Cd(Cd-BrBr)
        L3: O2s-O2s-Cd(Cd-Cl)
            L4: O2s-Cd(Cd-ClCl)-O2s
        L3: O2s-Cd(Cd-FF)-O2s
        L3: O2s-O2s-Cd(Cd-F)
    L2: FourMember
        L3: Cyclobutane
            L4: Cs-Cs(Br)(Br)-Cs-Cs
            L4: Cs(Br)-Cs-Cs-Cs
            L4: Cs-Cs(Cl)-Cs-Cs
                L5: Cs-Cs(Cl)(Cl)-Cs-Cs
            L4: Cs(F)-Cs-Cs-Cs
                L5: Cs-Cs-Cs(F)(F)-Cs
        L3: 34methylenecyclobutene
        L3: dioxerene
        L3: Oxetene
        L3: four-inringonedouble
            L4: Cyclobutene
                L5: Cd-Cd-O2s-Cs(F)
                    L6: O2s-Cd-Cd-Cs(F)(F)
                L5: Cs(Br)-Cd-Cd-O2s
                    L6: Cd-Cd-Cs(Br)(Br)-O2s
                L5: Cs-Cd-Cd-Cs(Br)
                L5: Cd(Br)-Cd-Cs-O2s
                L5: Cd(Br)-Cd-O2s-Cs
                L5: Cd(Br)-Cd-Cs-Cs
                L5: O2s-O2s-Cd-Cd(Br)
                L5: Cs-Cd(Cl)-Cd-Cs
                L5: Cd-Cd-O2s-Cs(Cl)
                    L6: Cd-Cs(Cl)(Cl)-O2s-Cd
                L5: Cd(Cl)-O2s-Cs-Cd
                L5: Cs-Cs(Cl)-Cd-Cd
                    L6: Cd-Cs-Cs(Cl)(Cl)-Cd
                L5: Cs-O2s-Cd-Cd(Cl)
                L5: Cd-O2s-O2s-Cd(Cl)
                L5: Cs(F)-Cs-Cd-Cd
                    L6: Cd-Cs-Cs(F)(F)-Cd
                L5: Cd(F)-Cd-Cs-Cs
                L5: Cd-Cd(F)-Cs-O2s
                L5: Cs-Cd-Cd(F)-O2s
                L5: Cd-Cd(F)-O2s-O2s
        L3: Oxetane
            L4: Cs-Cs(Br)-Cs-O2s
                L5: O2s-Cs-Cs(Br)(Br)-Cs
            L4: Cs-Cs-Cs(Br)(Br)-O2s
            L4: O2s-Cs(Br)-Cs-Cs
            L4: O2s-Cs(Cl)-Cs-Cs
                L5: O2s-Cs-Cs-Cs(Cl)(Cl)
            L4: O2s-Cs-Cs(Cl)-Cs
                L5: Cs-Cs(Cl)(Cl)-Cs-O2s
            L4: O2s-Cs-Cs-Cs(F)
                L5: Cs-Cs(F)(F)-O2s-Cs
            L4: Cs-O2s-Cs-Cs(F)
                L5: Cs-O2s-Cs-Cs(F)(F)
        L3: Beta-Propiolactone
        L3: Cyclobutanone
        L3: 12dioxetane
            L4: Cs-Cs(Br)-O2s-O2s
                L5: O2s-Cs(Br)(Br)-Cs-O2s
            L4: Cs(Cl)-O2s-O2s-Cs
                L5: O2s-Cs-Cs(Cl)(Cl)-O2s
            L4: Cs-Cs(F)-O2s-O2s
                L5: O2s-Cs(F)(F)-Cs-O2s
        L3: four-inringtwodouble
            L4: cyclobutadiene_13
                L5: Cd-Cd-Cd-Cd(Br)
                L5: Cd-Cd-Cd(Cl)-Cd
                L5: Cd-Cd-Cd-Cd(F)
        L3: cyclobutadiene_12
        L3: thietane
        L3: 1,2-dithietane
        L3: 1,3-dithietane
        L3: trithietane
        L3: tetrathietane
        L3: Azetidine
        L3: 4-Methylene-2-oxetanone
        L3: methylenecyclobutane
        L3: 2methyleneoxetane
        L3: 12methylenecyclobutane
        L3: O2s-Cs-O2s-Cs(Br)(Br)
        L3: Cs-O2s-Cs(Br)-O2s
        L3: O2s-Cs-O2s-Cs(Cl)(Cl)
        L3: Cs-O2s-Cs(Cl)-O2s
        L3: O2s-Cs-O2s-Cs(F)
            L4: Cs-O2s-Cs(F)(F)-O2s
    L2: FiveMember
        L3: Cyclopentane
        L3: Cyclopentene
        L3: Cyclopentadiene
        L3: five-inringtwodouble-12
            L4: 1,2-Cyclopentadiene
        L3: five-inringthreedouble-124
            L4: Cyclopentatriene
        L3: five-inringonetriple
            L4: Cyclopentyne
        L3: Tetrahydrofuran
        L3: 2,3-Dihydrofuran
        L3: 1,3-Dioxolane
        L3: Furan
        L3: Dihydro-2,5-furandione
        L3: 2,5-Furandione
        L3: Cyclopentanone
        L3: butyrolactone
        L3: 25dihydrofuran
        L3: 12dioxolane
        L3: 12dioxolene
        L3: 123trioxolane
        L3: 124trioxolane
        L3: thiolane
        L3: 2,3-dihydrothiophene
        L3: 2,5-dihydrothiophene
        L3: thiophene
        L3: 1,2-dithiolane
        L3: 1,3-dithiolane
        L3: 1,2,3-trithiolane
        L3: 1,2,4-trithiolane
        L3: tetrathiolane
        L3: pentathiolane
        L3: Pyrrolidine
        L3: methylenecyclopentane
        L3: Fulvene
        L3: 3-Methylenecyclopentene
        L3: 4-Methylenecyclopentene
        L3: 12methylenecyclopentane
    L2: SixMember
        L3: sixnosidedouble
            L4: Cyclohexane
            L4: 12dioxane
            L4: 1,3-Dioxane
            L4: 1,4-Dioxane
            L4: 1,3,5-Trioxane
            L4: 124trioxane
            L4: 123trioxane
            L4: Oxane
            L4: hexasulfur
            L4: Piperidine
        L3: six-sidedoubles
            L4: six-onesidedouble
                L5: Cyclohexanone
            L4: sixmembd-allsingles-twosidedoubles-para
                L5: 14methylenecyclohexane
            L4: sixmembd-allsingles-twosidedoubles-ortho
            L4: sixmembd-allsingles-twosidedoubles-meta
        L3: six-inringonedouble
            L4: 34dihydro12dioxin
            L4: 36dihydro2hpyran
            L4: Cyclohexene
            L4: 3,4-Dihydro-2H-pyran
            L4: 36dihydro12dioxin
            L4: 24dihydro13dioxin
            L4: 23dihydro14dioxin
            L4: 124trioxene
            L4: 123trioxene
        L3: six-inringtwodouble-13
            L4: 1,3-Cyclohexadiene
        L3: six-inringtwodouble-14
            L4: 1,4-Cyclohexadiene
            L4: 14dioxin
        L3: six-inringthreedouble_124
            L4: 124cyclohexatriene
        L3: six-inringthreedouble_123
            L4: 123cyclohexatriene
        L3: six-inringtwodouble-12
        L3: six-oneside-twoindoubles-25
            L4: 25cyclohexadienone
            L4: 14cyclohexadiene3methylene
        L3: six-oneside-twoindoubles-24
            L4: 24cyclohexadienone
            L4: 13cyclohexadiene5methylene
        L3: six-twoin13-twoout
            L4: fg6
            L4: oxylene
            L4: obenzoquinone
        L3: six-twoin14-twoout
            L4: pbenzoquinone
            L4: pxylene
        L3: 3,4-dimethylenecyclohexene
        L3: six-inringonetriple
            L4: cyclohexyne
        L3: six-inringonetripleonedouble-13
            L4: cyclohex_1_yne_3_ene
            L4: o_benzyne
        L3: six-inringonetripleonedouble-14
            L4: cyclohex_1_yne_4_ene
        L3: six-inringonetripletwodouble-134
        L3: six-inringonetriplethreedouble-1345
        L3: six-inringtwotriple-13
            L4: 1_3_cyclohexadiyne
    L2: SevenMember
        L3: Cycloheptane
        L3: Cycloheptene
        L3: 1,3-Cycloheptadiene
        L3: 1,3,5-Cycloheptatriene
        L3: Cycloheptanone
        L3: 1,4-Cycloheptadiene
        L3: seven-inringtwodouble-12
            L4: 1_2_cycloheptadiene
            L4: 1,2,4,6-Cycloheptatetraene
        L3: seven-inringthreedouble-123
            L4: 1_2_3_cycloheptatriene
        L3: seven-inringonetriple
            L4: cycloheptyne
        L3: heptasulfur
        L3: oxepane
    L2: EightMember
        L3: Cyclooctane
        L3: cis-Cyclooctene
        L3: 1,3,5-Cyclooctatriene
        L3: Cyclooctatetraene
        L3: Cyclooctanone
        L3: 1,3-cyclooctadiene
        L3: 1,4-cyclooctadiene
        L3: 1,5-cyclooctadiene
        L3: octasulfur
    L2: NineMember
        L3: Cyclononane
        L3: Cyclononanone
    L2: TenMember
        L3: Cyclodecane
        L3: Cyclodecanone
"""
)

