#!/usr/bin/env python
# encoding: utf-8

name = "Long distance interaction correction for non-cyclic molecule"
shortDesc = ""
longDesc = """
Designed to account for the long distance interaction for non-cyclic molecule.
Currently include gauche(1,4) and 1,5 interaction corrections.
For gauche interaction, we apply the simple counting scheme as it is in the old RMG database
    P-P,S,T,orQ: 0
    S-S: 0
    S-T: 1
    S-Q: 2
    T-T: 2 (except T-T-T, which is 5 total)
    T-Q: 4
    Q-Q: 6
        A single gauche correction is worth 0.8 kcal/mol for alkanes and 0.5 kcal/mol for ethers 
        (cf. Benson, Thermochemical Kinetics: Methods for the Estimation of Thermochemical Data and Rate Parameters, 2nd Edition, 1976. and Cohen and Benson, Chem. Rev. 93 (1993) 2419)
        For alkenes, the value of 0.5 kcal/mol is used and the counting scheme discussed in Benson, Cruickshank, Golden, Haugen, O'Neal, Rodgers, Shaw, and Walsh, Chemical Reviews, 1969, 69, 279, was used
For 1,5 interaction, values used are 1976 values (1.5 kcal/mol per 1,5 interaction in alkanes and 3.5 per 1,5 interaction in ethers)

Watch out:  if the groups on the two labeled atoms are identical, it's value should be halved because it'll be counted twice.
            For example, the value of the entry CsCS-QQ is (6 * 0.8 / 2)= 2.4, 
            because Q-Q is counted as 6 gauche corrections, one gauche worth 0.8 kcal/mol, 
            then divided by 2 since it'll be counted in both {'*1': atom1, '*2'atom2} and {'*2': atom1, '*1'atom2}.
            It should be claimed in the 'longDesc' if a entry was halved.

Sep-30-2016 PZ

Non-Next Nearest Neighbor (NNI) interaction terms for chlorine added (intCl). Values come from:
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558

March-16-2018

Refit NNI interaction terms for chlorine (intCl) and dervied terms for fluroine (intF) and bromine (intBr)
from species in RMG thermo libraries (primarily halogen G4 thermo libraries).

April-6-2021
"""
entry(
    index = 0,
    label = "R",
    group = 
"""
1 *1 R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "intVal7",
    group = 
"""
1 *1 C    u0 {2,[S,D]} {3,S}
2 *2 C    u0 {1,[S,D]}
3    Val7 u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "Cs(Val7)3-Cs(Val7)3",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 {1,S} {4,S} {6,S} {8,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
5    Val7 u0 {1,S}
6    Val7 u0 {2,S}
7    Val7 u0 {1,S}
8    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0237077,0.1644,0.256666,0.293265,0.299715,0.280658,0.394394],'cal/(mol*K)','+|-',[0.185831,0.207701,0.209983,0.206526,0.179917,0.154629,0.131536]),
        H298 = (4.00388,'kcal/mol','+|-',0.631215),
        S298 = (0.542585,'cal/(mol*K)','+|-',0.545452),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOFBr_G4 |         5
""",
)

entry(
    index = 3,
    label = "Cs(Cl)3-Cs(Cl)3",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 {1,S} {4,S} {6,S} {8,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
5    Cl1s u0 {1,S}
6    Cl1s u0 {2,S}
7    Cl1s u0 {1,S}
8    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.579455,0.432446,0.349853,0.288426,0.164176,0.0561215,0.00914887],'cal/(mol*K)','+|-',[0.407642,0.455616,0.460623,0.453038,0.394669,0.339197,0.288541]),
        H298 = (4.02983,'kcal/mol','+|-',1.38464),
        S298 = (-1.03837,'cal/(mol*K)','+|-',1.19651),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         1
""",
)

entry(
    index = 4,
    label = "Cs(F)3-Cs(F)3",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs  u0 {1,S} {4,S} {6,S} {8,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
5    F1s u0 {1,S}
6    F1s u0 {2,S}
7    F1s u0 {1,S}
8    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.130504,0.31238,0.328377,0.356799,0.395379,0.376677,0.301946],'cal/(mol*K)','+|-',[0.405035,0.452703,0.457678,0.450141,0.392146,0.337028,0.286696]),
        H298 = (5.50479,'kcal/mol','+|-',1.37579),
        S298 = (-1.4598,'cal/(mol*K)','+|-',1.18886),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         1
""",
)

entry(
    index = 5,
    label = "Cs(Br)3-Cs(Br)3",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 {1,S} {4,S} {6,S} {8,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
5    Br1s u0 {1,S}
6    Br1s u0 {2,S}
7    Br1s u0 {1,S}
8    Br1s u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "Cs(Val7)3-Cs(Val7)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
6    Val7        u0 {2,S}
7    Val7        u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.649432,-0.613998,-0.459804,-0.402124,-0.349373,-0.260931,0.272767],'cal/(mol*K)','+|-',[0.120322,0.134483,0.135961,0.133722,0.116493,0.10012,0.0851677]),
        H298 = (4.62481,'kcal/mol','+|-',0.408701),
        S298 = (2.4581,'cal/(mol*K)','+|-',0.353171),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         8
library:CHOFClBr_G4 |         15
library:CHOFBr_G4   |         20
library:CHOClBr_G4  |         11
""",
)

entry(
    index = 7,
    label = "Cs(Cl)3-Cs(Cl)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
6    Cl1s        u0 {2,S}
7    Cl1s        u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00372668,-0.254112,-0.263806,-0.231626,-0.181975,-0.0751458,0.42894],'cal/(mol*K)','+|-',[0.166232,0.185796,0.187838,0.184744,0.160942,0.138321,0.117664]),
        H298 = (9.49979,'kcal/mol','+|-',0.564644),
        S298 = (2.21743,'cal/(mol*K)','+|-',0.487926),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         40
""",
)

entry(
    index = 8,
    label = "Cs(F)3-Cs(F)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
6    F1s         u0 {2,S}
7    F1s         u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.250048,-0.189885,-0.0500303,0.0311503,0.0713201,0.144045,0.436909],'cal/(mol*K)','+|-',[0.156494,0.174912,0.176834,0.173922,0.151514,0.130218,0.110771]),
        H298 = (10.414,'kcal/mol','+|-',0.531566),
        S298 = (3.40118,'cal/(mol*K)','+|-',0.459342),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         41
""",
)

entry(
    index = 9,
    label = "Cs(Br)3-Cs(Br)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
6    Br1s        u0 {2,S}
7    Br1s        u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.167718,-0.447111,-0.549533,-0.662454,-0.833597,-0.865357,-0.384133],'cal/(mol*K)','+|-',[0.802758,0.897233,0.907092,0.892155,0.777211,0.667971,0.568215]),
        H298 = (4.96565,'kcal/mol','+|-',2.72674),
        S298 = (2.6469,'cal/(mol*K)','+|-',2.35626),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         1
""",
)

entry(
    index = 10,
    label = "Cs(Val7)3-C(Val7)",
    group = 
"""
1 *1 Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd] u0 {1,S} {6,S}
3    Val7    u0 {1,S}
4    Val7    u0 {1,S}
5    Val7    u0 {1,S}
6    Val7    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "Cs(Val7)3-Cs(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    Val7        u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.310155,-0.32123,-0.239056,-0.184464,-0.121291,-0.0528434,0.297517],'cal/(mol*K)','+|-',[0.0903475,0.10098,0.10209,0.100409,0.0874724,0.0751778,0.0639506]),
        H298 = (2.9397,'kcal/mol','+|-',0.306885),
        S298 = (3.21398,'cal/(mol*K)','+|-',0.265188),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         15
library:CHOFClBr_G4 |         21
library:CHOFBr_G4   |         63
library:CHOClBr_G4  |         21
""",
)

entry(
    index = 12,
    label = "Cs(Cl)3-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    Cl1s        u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.192711,-0.290667,-0.268575,-0.238512,-0.199744,-0.10067,0.303139],'cal/(mol*K)','+|-',[0.132753,0.148376,0.150006,0.147536,0.128528,0.110463,0.0939661]),
        H298 = (5.57149,'kcal/mol','+|-',0.450923),
        S298 = (3.36258,'cal/(mol*K)','+|-',0.389656),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         60
""",
)

entry(
    index = 13,
    label = "Cs(F)3-Cs(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    F1s         u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.073355,0.208602,0.246827,0.234723,0.186484,0.170508,0.290019],'cal/(mol*K)','+|-',[0.125188,0.139921,0.141458,0.139129,0.121204,0.104168,0.0886114]),
        H298 = (6.65334,'kcal/mol','+|-',0.425227),
        S298 = (3.22236,'cal/(mol*K)','+|-',0.367451),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         62
library:CHOFBr_G4 |         2
""",
)

entry(
    index = 14,
    label = "Cs(Br)3-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    Br1s        u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.433704,-0.571648,-0.592816,-0.639095,-0.678003,-0.565108,0.0871202],'cal/(mol*K)','+|-',[0.308366,0.344657,0.348444,0.342706,0.298553,0.25659,0.21827]),
        H298 = (3.64152,'kcal/mol','+|-',1.04743),
        S298 = (2.50793,'cal/(mol*K)','+|-',0.905116),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOBr_G4  |         7
library:CHOFBr_G4 |         1
""",
)

entry(
    index = 15,
    label = "Cs(Val7)3-Cds(Val7)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {6,S} {7,D}
3    Val7      u0 {1,S}
4    Val7      u0 {1,S}
5    Val7      u0 {1,S}
6    Val7      u0 {2,S}
7    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0751243,0.473581,0.602548,0.648239,0.621319,0.560548,0.541552],'cal/(mol*K)','+|-',[0.155888,0.174234,0.176149,0.173248,0.150927,0.129714,0.110342]),
        H298 = (4.37607,'kcal/mol','+|-',0.529508),
        S298 = (2.89978,'cal/(mol*K)','+|-',0.457564),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         3
library:CHOFClBr_G4 |         6
library:CHOFBr_G4   |         21
library:CHOClBr_G4  |         6
""",
)

entry(
    index = 16,
    label = "Cs(Cl)3-Cds(Cl)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {6,S} {7,D}
3    Cl1s      u0 {1,S}
4    Cl1s      u0 {1,S}
5    Cl1s      u0 {1,S}
6    Cl1s      u0 {2,S}
7    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.325899,0.0189191,0.213026,0.300168,0.372871,0.414767,0.517436],'cal/(mol*K)','+|-',[0.230996,0.258181,0.261018,0.25672,0.223644,0.19221,0.163505]),
        H298 = (3.63586,'kcal/mol','+|-',0.784626),
        S298 = (2.10133,'cal/(mol*K)','+|-',0.678019),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         19
""",
)

entry(
    index = 17,
    label = "Cs(F)3-Cds(F)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {6,S} {7,D}
3    F1s       u0 {1,S}
4    F1s       u0 {1,S}
5    F1s       u0 {1,S}
6    F1s       u0 {2,S}
7    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.123102,0.00317034,0.0294552,0.0373139,0.0734727,0.123219,0.21547],'cal/(mol*K)','+|-',[0.228069,0.25491,0.257711,0.253468,0.220811,0.189775,0.161434]),
        H298 = (6.08999,'kcal/mol','+|-',0.774686),
        S298 = (3.06248,'cal/(mol*K)','+|-',0.66943),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         19
""",
)

entry(
    index = 18,
    label = "Cs(Br)3-Cds(Br)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {6,S} {7,D}
3    Br1s      u0 {1,S}
4    Br1s      u0 {1,S}
5    Br1s      u0 {1,S}
6    Br1s      u0 {2,S}
7    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0717925,0.513416,0.635187,0.670602,0.619926,0.524993,0.275934],'cal/(mol*K)','+|-',[0.58708,0.656172,0.663383,0.652459,0.568397,0.488507,0.415552]),
        H298 = (3.80425,'kcal/mol','+|-',1.99414),
        S298 = (3.8777,'cal/(mol*K)','+|-',1.7232),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOBr_G4  |         1
library:CHOFBr_G4 |         1
""",
)

entry(
    index = 19,
    label = "Cs(Val7)2-Cs(Val7)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
6    Val7        u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284649,-0.409923,-0.37118,-0.347857,-0.290373,-0.201661,0.0672598],'cal/(mol*K)','+|-',[0.0479988,0.0536477,0.0542372,0.053344,0.0464713,0.0399396,0.0339749]),
        H298 = (1.96415,'kcal/mol','+|-',0.163038),
        S298 = (1.62492,'cal/(mol*K)','+|-',0.140886),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         12
library:CHOFClBr_G4 |         18
library:CHOFBr_G4   |         54
library:CHOClBr_G4  |         18
""",
)

entry(
    index = 20,
    label = "Cs(Cl)2-Cs(Cl)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
6    Cl1s        u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.478099,-0.542091,-0.466901,-0.418184,-0.3247,-0.165141,0.269073],'cal/(mol*K)','+|-',[0.0654694,0.0731743,0.0739784,0.0727602,0.0633859,0.0544768,0.0463411]),
        H298 = (3.13266,'kcal/mol','+|-',0.222381),
        S298 = (0.975081,'cal/(mol*K)','+|-',0.192166),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         55
""",
)

entry(
    index = 21,
    label = "Cs(F)2-Cs(F)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
6    F1s         u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.287684,-0.32564,-0.246644,-0.205197,-0.174325,-0.104232,0.146018],'cal/(mol*K)','+|-',[0.0606915,0.0678342,0.0685796,0.0674503,0.0587601,0.0505011,0.0429592]),
        H298 = (3.72987,'kcal/mol','+|-',0.206152),
        S298 = (1.73568,'cal/(mol*K)','+|-',0.178142),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         56
library:CHOFBr_G4 |         2
""",
)

entry(
    index = 22,
    label = "Cs(Br)2-Cs(Br)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
6    Br1s        u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.461224,-0.570172,-0.528765,-0.494455,-0.415179,-0.329415,-0.104976],'cal/(mol*K)','+|-',[0.158625,0.177293,0.179241,0.17629,0.153577,0.131991,0.112279]),
        H298 = (1.77662,'kcal/mol','+|-',0.538804),
        S298 = (0.955255,'cal/(mol*K)','+|-',0.465597),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOBr_G4  |         6
library:CHOFBr_G4 |         1
""",
)

entry(
    index = 23,
    label = "Cs(Val7)2-C(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd]     u0 {1,S} {6,S}
3    Val7        u0 {1,S}
4    Val7        u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Val7        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "Cs(Val7)2-Cs(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41389,-0.396523,-0.302539,-0.260401,-0.200646,-0.100577,0.222751],'cal/(mol*K)','+|-',[0.0535507,0.0598529,0.0605106,0.0595142,0.0518465,0.0445593,0.0379047]),
        H298 = (2.43816,'kcal/mol','+|-',0.181896),
        S298 = (3.06667,'cal/(mol*K)','+|-',0.157182),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         77
library:CHOFClBr_G4 |         57
library:CHOFBr_G4   |         172
library:CHOClBr_G4  |         88
""",
)

entry(
    index = 25,
    label = "Cs(Cl)2-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.679258,-0.634445,-0.448961,-0.346821,-0.220663,-0.0212432,0.484401],'cal/(mol*K)','+|-',[0.0804473,0.0899149,0.090903,0.089406,0.0778871,0.0669398,0.0569429]),
        H298 = (3.57066,'kcal/mol','+|-',0.273256),
        S298 = (2.61355,'cal/(mol*K)','+|-',0.236129),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         123
library:CHOFCl_G4  |         2
library:CHOClBr_G4 |         4
""",
)

entry(
    index = 26,
    label = "Cs(F)2-Cs(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.296002,-0.171172,-0.0220443,0.0351913,0.0558415,0.12462,0.339124],'cal/(mol*K)','+|-',[0.074347,0.0830968,0.0840099,0.0826265,0.0719811,0.0618638,0.052625]),
        H298 = (4.58289,'kcal/mol','+|-',0.252536),
        S298 = (3.1689,'cal/(mol*K)','+|-',0.218224),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         126
library:CHOFCl_G4 |         4
library:CHOFBr_G4 |         31
""",
)

entry(
    index = 27,
    label = "Cs(Br)2-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.50974,-0.479363,-0.315746,-0.214276,-0.123541,-0.0276579,0.214132],'cal/(mol*K)','+|-',[0.104905,0.117251,0.11854,0.116588,0.101567,0.0872913,0.0742551]),
        H298 = (2.46493,'kcal/mol','+|-',0.356334),
        S298 = (2.14605,'cal/(mol*K)','+|-',0.307919),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOBr_G4   |         50
library:CHOFBr_G4  |         24
library:CHOClBr_G4 |         6
""",
)

entry(
    index = 28,
    label = "Cs(Val7)2-Cds(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    Val7        u0 {1,S}
4    Val7        u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Val7        u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.499807,-0.269605,-0.109785,-0.0288718,0.0553637,0.135258,0.451358],'cal/(mol*K)','+|-',[0.101668,0.113633,0.114882,0.11299,0.0984329,0.0845977,0.0719638]),
        H298 = (3.28024,'kcal/mol','+|-',0.345338),
        S298 = (2.96437,'cal/(mol*K)','+|-',0.298417),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         18
library:CHOFClBr_G4 |         21
library:CHOFBr_G4   |         41
library:CHOClBr_G4  |         25
""",
)

entry(
    index = 29,
    label = "Cs(Cl)2-Cds(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Cl1s        u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.344059,-0.00952927,0.223041,0.334201,0.424109,0.470633,0.749599],'cal/(mol*K)','+|-',[0.157455,0.175986,0.17792,0.17499,0.152445,0.131018,0.111451]),
        H298 = (2.79769,'kcal/mol','+|-',0.534831),
        S298 = (1.79498,'cal/(mol*K)','+|-',0.462164),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         37
library:CHOFCl_G4  |         1
library:CHOClBr_G4 |         3
""",
)

entry(
    index = 30,
    label = "Cs(F)2-Cds(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    F1s         u0 {1,S}
4    F1s         u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    F1s         u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0443613,0.162268,0.173293,0.147865,0.137284,0.145904,0.401044],'cal/(mol*K)','+|-',[0.151951,0.169834,0.1717,0.168873,0.147116,0.126438,0.107556]),
        H298 = (3.58466,'kcal/mol','+|-',0.516135),
        S298 = (2.62263,'cal/(mol*K)','+|-',0.446008),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         37
library:CHOFBr_G4 |         6
""",
)

entry(
    index = 31,
    label = "Cs(Br)2-Cds(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    Br1s        u0 {1,S}
4    Br1s        u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Br1s        u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436242,-0.25018,-0.0645881,0.0558657,0.202503,0.228086,0.299509],'cal/(mol*K)','+|-',[0.203149,0.227057,0.229552,0.225772,0.196684,0.16904,0.143795]),
        H298 = (1.6173,'kcal/mol','+|-',0.69004),
        S298 = (3.30743,'cal/(mol*K)','+|-',0.596284),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOBr_G4   |         10
library:CHOFBr_G4  |         8
library:CHOClBr_G4 |         2
""",
)

entry(
    index = 32,
    label = "C(Val7)-C(Val7)",
    group = 
"""
1 *1 [Cs,Cd] u0 {2,S} {3,S}
2 *2 [Cs,Cd] u0 {1,S} {4,S}
3    Val7    u0 {1,S}
4    Val7    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "Cs(Val7)-Cs(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.15098,-0.139548,-0.112754,-0.102134,-0.0908677,-0.0532462,0.0631659],'cal/(mol*K)','+|-',[0.0354217,0.0395904,0.0400254,0.0393663,0.0342944,0.0294742,0.0250725]),
        H298 = (1.2224,'kcal/mol','+|-',0.120317),
        S298 = (1.87987,'cal/(mol*K)','+|-',0.10397),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         51
library:CHOFClBr_G4 |         28
library:CHOFBr_G4   |         82
library:CHOClBr_G4  |         53
""",
)

entry(
    index = 34,
    label = "Cs(Cl)-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.212233,-0.151109,-0.0593742,0.00374713,0.0588283,0.108516,0.210587],'cal/(mol*K)','+|-',[0.0467129,0.0522104,0.0527841,0.0519149,0.0452263,0.0388695,0.0330647]),
        H298 = (1.14474,'kcal/mol','+|-',0.15867),
        S298 = (1.52173,'cal/(mol*K)','+|-',0.137112),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         74
library:CHOFCl_G4  |         13
library:CHOClBr_G4 |         19
""",
)

entry(
    index = 35,
    label = "Cs(F)-Cs(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.153589,-0.0933673,-0.0103177,0.0371537,0.066095,0.099934,0.179448],'cal/(mol*K)','+|-',[0.0420027,0.0469459,0.0474618,0.0466802,0.040666,0.0349503,0.0297307]),
        H298 = (1.66609,'kcal/mol','+|-',0.142671),
        S298 = (1.47616,'cal/(mol*K)','+|-',0.123286),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOF_G4     |         77
library:CHOFCl_G4   |         18
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         46
""",
)

entry(
    index = 36,
    label = "Cs(Br)-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          u0 {1,S} {4,S} {6,S} {8,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {2,S}
7    [C,H,N,O,S] u0 {1,S}
8    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234257,-0.154171,-0.0495199,0.0156258,0.0703032,0.111296,0.201131],'cal/(mol*K)','+|-',[0.0477146,0.05333,0.0539161,0.0530282,0.0461962,0.0397031,0.0337738]),
        H298 = (0.923421,'kcal/mol','+|-',0.162073),
        S298 = (0.967614,'cal/(mol*K)','+|-',0.140052),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         49
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         37
library:CHOClBr_G4  |         13
""",
)

entry(
    index = 37,
    label = "Cs(Val7)-Cds(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    Val7        u0 {1,S}
4    [C,H,N,O,S] u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Val7        u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.488249,-0.318101,-0.1909,-0.129265,-0.0182219,0.0550723,0.354748],'cal/(mol*K)','+|-',[0.107952,0.120657,0.121983,0.119974,0.104517,0.0898266,0.0764117]),
        H298 = (1.72447,'kcal/mol','+|-',0.366683),
        S298 = (3.38948,'cal/(mol*K)','+|-',0.316862),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         21
library:CHOFClBr_G4 |         16
library:CHOFBr_G4   |         31
library:CHOClBr_G4  |         22
""",
)

entry(
    index = 38,
    label = "Cs(Cl)-Cds(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    Cl1s        u0 {1,S}
4    [C,H,N,O,S] u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Cl1s        u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.364209,-0.101525,0.0554152,0.115861,0.184745,0.220096,0.466894],'cal/(mol*K)','+|-',[0.142291,0.159037,0.160785,0.158137,0.137763,0.1184,0.100718]),
        H298 = (1.59754,'kcal/mol','+|-',0.483324),
        S298 = (2.48235,'cal/(mol*K)','+|-',0.417654),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         37
library:CHOFCl_G4  |         8
library:CHOClBr_G4 |         8
""",
)

entry(
    index = 39,
    label = "Cs(F)-Cds(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    F1s         u0 {1,S}
4    [C,H,N,O,S] u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    F1s         u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.214431,-0.0580059,0.0221815,0.0622322,0.126312,0.158286,0.448108],'cal/(mol*K)','+|-',[0.134571,0.150408,0.152061,0.149557,0.130288,0.111976,0.0952529]),
        H298 = (2.04755,'kcal/mol','+|-',0.457098),
        S298 = (2.6289,'cal/(mol*K)','+|-',0.394992),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOF_G4     |         37
library:CHOFCl_G4   |         6
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         16
""",
)

entry(
    index = 40,
    label = "Cs(Br)-Cds(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          u0 {1,S} {6,S} {7,D}
3    Br1s        u0 {1,S}
4    [C,H,N,O,S] u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Br1s        u0 {2,S}
7    [C,N,O,S]   u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.471998,-0.304533,-0.133164,-0.0307646,0.111438,0.175859,0.376174],'cal/(mol*K)','+|-',[0.137533,0.153719,0.155408,0.152849,0.133156,0.11444,0.0973496]),
        H298 = (1.26769,'kcal/mol','+|-',0.46716),
        S298 = (3.13421,'cal/(mol*K)','+|-',0.403686),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         24
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         20
library:CHOClBr_G4  |         8
""",
)

entry(
    index = 41,
    label = "Cds(Val7)-Cds(Val7)",
    group = 
"""
1 *1 Cd        u0 {2,S} {3,S} {5,D}
2 *2 Cd        u0 {1,S} {4,S} {6,D}
3    Val7      u0 {1,S}
4    Val7      u0 {2,S}
5    [C,N,O,S] u0 {1,D}
6    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.142598,0.000177485,0.138481,0.117533,0.0286904,-0.0166047,0.154016],'cal/(mol*K)','+|-',[0.124047,0.138645,0.140169,0.137861,0.120099,0.103219,0.0878038]),
        H298 = (0.207797,'kcal/mol','+|-',0.421351),
        S298 = (-0.447847,'cal/(mol*K)','+|-',0.364102),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         3
library:CHOFClBr_G4 |         6
library:CHOFBr_G4   |         6
library:CHOClBr_G4  |         5
""",
)

entry(
    index = 42,
    label = "Cds(Cl)-Cds(Cl)",
    group = 
"""
1 *1 Cd        u0 {2,S} {3,S} {5,D}
2 *2 Cd        u0 {1,S} {4,S} {6,D}
3    Cl1s      u0 {1,S}
4    Cl1s      u0 {2,S}
5    [C,N,O,S] u0 {1,D}
6    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16018,-0.106826,0.0234607,0.00711724,-0.0873311,-0.124167,0.113025],'cal/(mol*K)','+|-',[0.190637,0.213073,0.215414,0.211867,0.184571,0.158628,0.134939]),
        H298 = (0.00140718,'kcal/mol','+|-',0.647541),
        S298 = (-0.613282,'cal/(mol*K)','+|-',0.559559),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         6
library:CHOFCl_G4  |         1
library:CHOClBr_G4 |         3
""",
)

entry(
    index = 43,
    label = "Cds(F)-Cds(F)",
    group = 
"""
1 *1 Cd        u0 {2,S} {3,S} {5,D}
2 *2 Cd        u0 {1,S} {4,S} {6,D}
3    F1s       u0 {1,S}
4    F1s       u0 {2,S}
5    [C,N,O,S] u0 {1,D}
6    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0793163,-0.0366229,0.0783675,0.055825,-0.0323221,-0.0675522,0.123364],'cal/(mol*K)','+|-',[0.173278,0.193671,0.195799,0.192575,0.167764,0.144184,0.122651]),
        H298 = (0.64848,'kcal/mol','+|-',0.588577),
        S298 = (-0.560258,'cal/(mol*K)','+|-',0.508607),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOF_G4     |         6
library:CHOFCl_G4   |         1
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         4
""",
)

entry(
    index = 44,
    label = "Cds(Br)-Cds(Br)",
    group = 
"""
1 *1 Cd        u0 {2,S} {3,S} {5,D}
2 *2 Cd        u0 {1,S} {4,S} {6,D}
3    Br1s      u0 {1,S}
4    Br1s      u0 {2,S}
5    [C,N,O,S] u0 {1,D}
6    [C,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.188062,-0.148187,0.00275799,0.0154253,-0.0148553,-0.0259878,0.167964],'cal/(mol*K)','+|-',[0.185576,0.207416,0.209695,0.206242,0.17967,0.154417,0.131356]),
        H298 = (-0.0683126,'kcal/mol','+|-',0.630348),
        S298 = (-0.879077,'cal/(mol*K)','+|-',0.544702),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         2
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         4
library:CHOClBr_G4  |         3
""",
)

entry(
    index = 45,
    label = "Cds(Val7)=Cds(Val7)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.184761,0.156906,0.101795,0.0779607,0.0262641,-0.0022401,-0.094175],'cal/(mol*K)','+|-',[0.0483455,0.0540352,0.0546289,0.0537294,0.046807,0.0402281,0.0342203]),
        H298 = (1.74451,'kcal/mol','+|-',0.164216),
        S298 = (0.222228,'cal/(mol*K)','+|-',0.141904),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         35
library:CHOFClBr_G4 |         23
library:CHOFBr_G4   |         50
library:CHOClBr_G4  |         36
""",
)

entry(
    index = 46,
    label = "Cds(Cl)=Cds(Cl)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.261934,0.228743,0.162619,0.121248,0.0370342,-0.00437144,-0.0966026],'cal/(mol*K)','+|-',[0.0657899,0.0735325,0.0743406,0.0731164,0.0636962,0.0547435,0.046568]),
        H298 = (1.4249,'kcal/mol','+|-',0.22347),
        S298 = (0.0940235,'cal/(mol*K)','+|-',0.193107),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         61
library:CHOFCl_G4  |         5
library:CHOClBr_G4 |         16
""",
)

entry(
    index = 47,
    label = "Cds(F)=Cds(F)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.135785,0.0663028,0.0248023,0.012661,-0.0107362,-0.018141,-0.0717221],'cal/(mol*K)','+|-',[0.0560374,0.0626323,0.0633206,0.0622778,0.0542541,0.0466285,0.0396649]),
        H298 = (3.08514,'kcal/mol','+|-',0.190343),
        S298 = (0.349813,'cal/(mol*K)','+|-',0.164481),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOF_G4     |         61
library:CHOFCl_G4   |         14
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         38
""",
)

entry(
    index = 48,
    label = "Cds(Br)=Cds(Br)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.203748,0.143777,0.0917331,0.0890436,0.0463408,0.0210995,-0.0697324],'cal/(mol*K)','+|-',[0.0759135,0.0848476,0.0857799,0.0843674,0.0734976,0.0631673,0.0537337]),
        H298 = (1.36489,'kcal/mol','+|-',0.257857),
        S298 = (-0.0352288,'cal/(mol*K)','+|-',0.222821),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         36
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         16
library:CHOClBr_G4  |         7
""",
)

entry(
    index = 49,
    label = "Cds(Val7)2=Cds(Val7)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62041,0.54885,0.390576,0.334775,0.156668,0.0584541,-0.12133],'cal/(mol*K)','+|-',[0.0949969,0.106177,0.107344,0.105576,0.0919738,0.0790465,0.0672415]),
        H298 = (4.22891,'kcal/mol','+|-',0.322677),
        S298 = (0.668683,'cal/(mol*K)','+|-',0.278835),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         26
library:CHOFClBr_G4 |         24
library:CHOFBr_G4   |         54
library:CHOClBr_G4  |         32
""",
)

entry(
    index = 50,
    label = "Cds(Cl)2=Cds(Cl)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.741676,0.632153,0.441937,0.331819,0.0750462,-0.0317226,-0.150782],'cal/(mol*K)','+|-',[0.162058,0.18113,0.183121,0.180105,0.156901,0.134848,0.114709]),
        H298 = (4.55559,'kcal/mol','+|-',0.550465),
        S298 = (0.557188,'cal/(mol*K)','+|-',0.475674),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         41
library:CHOClBr_G4 |         3
""",
)

entry(
    index = 51,
    label = "Cds(F)2=Cds(F)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.578717,0.408499,0.278386,0.223224,0.0823162,0.00749726,-0.146829],'cal/(mol*K)','+|-',[0.141091,0.157695,0.159428,0.156803,0.136601,0.117401,0.0998679]),
        H298 = (9.52668,'kcal/mol','+|-',0.479244),
        S298 = (1.28946,'cal/(mol*K)','+|-',0.414129),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         41
library:CHOFCl_G4 |         2
library:CHOFBr_G4 |         12
""",
)

entry(
    index = 52,
    label = "Cds(Br)2=Cds(Br)",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {5,S}
2 *2 Cd          u0 {1,D} {4,S} {6,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
6    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.810598,0.739294,0.546141,0.499323,0.237356,0.0903159,-0.071499],'cal/(mol*K)','+|-',[0.217247,0.242814,0.245482,0.24144,0.210333,0.18077,0.153773]),
        H298 = (3.50906,'kcal/mol','+|-',0.737925),
        S298 = (0.204005,'cal/(mol*K)','+|-',0.637663),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOBr_G4   |         18
library:CHOFBr_G4  |         3
library:CHOClBr_G4 |         1
""",
)

entry(
    index = 53,
    label = "Cds(Val7)2=Cds(Val7)2",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
5    Val7 u0 {1,S}
6    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.378665,0.39011,0.259112,0.220757,0.0572574,-0.0534602,-0.220215],'cal/(mol*K)','+|-',[0.123242,0.137746,0.13926,0.136966,0.11932,0.102549,0.0872342]),
        H298 = (2.7133,'kcal/mol','+|-',0.418618),
        S298 = (0.383951,'cal/(mol*K)','+|-',0.36174),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         3
library:CHOFClBr_G4 |         3
library:CHOFBr_G4   |         3
library:CHOClBr_G4  |         3
""",
)

entry(
    index = 54,
    label = "Cds(Cl)2=Cds(Cl)2",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
5    Cl1s u0 {1,S}
6    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.499042,0.40291,0.205764,0.135147,-0.0354983,-0.156485,-0.403602],'cal/(mol*K)','+|-',[0.40638,0.454206,0.459197,0.451635,0.393447,0.338147,0.287647]),
        H298 = (2.29873,'kcal/mol','+|-',1.38036),
        S298 = (-1.69197,'cal/(mol*K)','+|-',1.19281),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         1
""",
)

entry(
    index = 55,
    label = "Cds(F)2=Cds(F)2",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 {1,D} {4,S} {6,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
5    F1s u0 {1,S}
6    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.156954,0.238593,0.132126,0.0981617,0.0279164,-0.0260023,-0.177291],'cal/(mol*K)','+|-',[0.402879,0.450293,0.455242,0.447745,0.390058,0.335234,0.28517]),
        H298 = (6.59153,'kcal/mol','+|-',1.36847),
        S298 = (-1.75167,'cal/(mol*K)','+|-',1.18253),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         1
""",
)

entry(
    index = 56,
    label = "Cds(Br)2=Cds(Br)2",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 {1,D} {4,S} {6,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
5    Br1s u0 {1,S}
6    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.480811,0.527827,0.377849,0.348437,0.127589,-0.0391841,-0.228514],'cal/(mol*K)','+|-',[0.41169,0.460141,0.465198,0.457537,0.398589,0.342566,0.291406]),
        H298 = (2.04335,'kcal/mol','+|-',1.39839),
        S298 = (-1.80825,'cal/(mol*K)','+|-',1.20839),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         1
""",
)

entry(
    index = 57,
    label = "Cd(Val7)-CO",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 CO   u0 {1,S} {4,D}
3    Val7 u0 {1,S}
4    O2d  u0 {2,D}
""",
    thermo = None,
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "Cd(F)-CO",
    group = 
"""
1 *1 Cd  u0 {2,S} {3,S}
2 *2 CO  u0 {1,S} {4,D}
3    F1s u0 {1,S}
4    O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.08737,-1.21811,-0.939665,-0.780645,-0.609515,-0.368616,0.75594],'cal/(mol*K)','+|-',[0.284322,0.317783,0.321275,0.315984,0.275274,0.236583,0.201251]),
        H298 = (1.08495,'kcal/mol','+|-',0.96576),
        S298 = (-0.803826,'cal/(mol*K)','+|-',0.834542),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         6
library:CHOFCl_G4 |         2
library:CHOFBr_G4 |         3
""",
)

entry(
    index = 59,
    label = "Cd(Cl)-CO",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 CO   u0 {1,S} {4,D}
3    Cl1s u0 {1,S}
4    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.433398,-0.74474,-0.605495,-0.555971,-0.547387,-0.377001,0.785247],'cal/(mol*K)','+|-',[0.270761,0.302626,0.305952,0.300914,0.262144,0.225299,0.191652]),
        H298 = (1.45622,'kcal/mol','+|-',0.919698),
        S298 = (-0.658435,'cal/(mol*K)','+|-',0.794739),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOCl_G4    |         6
library:CHOFCl_G4   |         4
library:CHOFClBr_G4 |         1
library:CHOClBr_G4  |         2
""",
)

entry(
    index = 60,
    label = "Cd(Br)-CO",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 CO   u0 {1,S} {4,D}
3    Br1s u0 {1,S}
4    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.213007,-0.401698,-0.282564,-0.266493,-0.322718,-0.202174,0.913452],'cal/(mol*K)','+|-',[0.247562,0.276697,0.279738,0.275132,0.239684,0.205996,0.175232]),
        H298 = (1.52842,'kcal/mol','+|-',0.840899),
        S298 = (-1.89942,'cal/(mol*K)','+|-',0.726646),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         5
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         6
library:CHOClBr_G4  |         4
""",
)

entry(
    index = 61,
    label = "Cs(Val7)3-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO   u0 {1,S} {6,D}
3    Val7 u0 {1,S}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.013,0.869341,0.643358,0.420375,0.0611501,-0.179942,-0.189931],'cal/(mol*K)','+|-',[0.143836,0.160763,0.16253,0.159854,0.139258,0.119685,0.101811]),
        H298 = (7.18331,'kcal/mol','+|-',0.488569),
        S298 = (1.40285,'cal/(mol*K)','+|-',0.422187),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         8
library:CHOFClBr_G4 |         6
library:CHOFBr_G4   |         14
library:CHOClBr_G4  |         8
""",
)

entry(
    index = 62,
    label = "Cs(F)3-CO",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO  u0 {1,S} {6,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
6    O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """CsCOFFF""",
    longDesc = 
"""
CsCOFFF group accounts for this interaction
""",
)

entry(
    index = 63,
    label = "Cs(Cl)3-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO   u0 {1,S} {6,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
6    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """CsClClClCO""",
    longDesc = 
"""
CsClClClCO group accounts for this interaction
""",
)

entry(
    index = 64,
    label = "Cs(Br)3-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO   u0 {1,S} {6,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
6    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """CsBrBrBrCO""",
    longDesc = 
"""
CsBrBrBrCO group accounts for this interaction
""",
)

entry(
    index = 65,
    label = "Cs(Val7)2-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    Val7        u0 {1,S}
4    Val7        u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.04701,0.846094,0.641695,0.430531,0.130561,-0.0285996,0.00914967],'cal/(mol*K)','+|-',[0.118637,0.132599,0.134056,0.131848,0.114861,0.0987169,0.0839744]),
        H298 = (5.10999,'kcal/mol','+|-',0.402975),
        S298 = (0.715597,'cal/(mol*K)','+|-',0.348222),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         13
library:CHOFClBr_G4 |         8
library:CHOFBr_G4   |         18
library:CHOClBr_G4  |         12
""",
)

entry(
    index = 66,
    label = "Cs(F)2-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    F1s         u0 {1,S}
4    F1s         u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.632355,0.415303,0.276497,0.125574,-0.0201702,-0.10415,0.0944342],'cal/(mol*K)','+|-',[0.149235,0.166798,0.168631,0.165854,0.144486,0.124178,0.105633]),
        H298 = (5.33804,'kcal/mol','+|-',0.506909),
        S298 = (0.286084,'cal/(mol*K)','+|-',0.438035),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         19
library:CHOFCl_G4 |         5
library:CHOFBr_G4 |         9
""",
)

entry(
    index = 67,
    label = "Cs(Cl)2-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.08725,1.01885,0.858772,0.642795,0.360809,0.170742,0.209378],'cal/(mol*K)','+|-',[0.159691,0.178485,0.180446,0.177475,0.154609,0.132878,0.113034]),
        H298 = (3.06523,'kcal/mol','+|-',0.542425),
        S298 = (-0.958133,'cal/(mol*K)','+|-',0.468726),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         20
library:CHOFCl_G4  |         3
library:CHOClBr_G4 |         5
""",
)

entry(
    index = 68,
    label = "Cs(Br)2-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    Br1s        u0 {1,S}
4    Br1s        u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.697505,0.705171,0.624551,0.478532,0.293354,0.146137,0.140992],'cal/(mol*K)','+|-',[0.176391,0.19715,0.199317,0.196034,0.170778,0.146774,0.124855]),
        H298 = (3.02429,'kcal/mol','+|-',0.599151),
        S298 = (-0.326436,'cal/(mol*K)','+|-',0.517744),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOBr_G4   |         12
library:CHOFBr_G4  |         9
library:CHOClBr_G4 |         3
""",
)

entry(
    index = 69,
    label = "Cs(Val7)-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    Val7        u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = None,
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "Cs(F)-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    F1s         u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.80429,0.708677,0.600579,0.482871,0.34976,0.209865,0.2642],'cal/(mol*K)','+|-',[0.131486,0.14696,0.148575,0.146129,0.127302,0.109409,0.0930695]),
        H298 = (2.44511,'kcal/mol','+|-',0.44662),
        S298 = (-0.565233,'cal/(mol*K)','+|-',0.385938),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOF_G4     |         20
library:CHOFCl_G4   |         9
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         13
""",
)

entry(
    index = 71,
    label = "Cs(Cl)-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    Cl1s        u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.960482,0.726648,0.526973,0.323138,0.0842669,-0.0819546,-0.0154854],'cal/(mol*K)','+|-',[0.135828,0.151814,0.153482,0.150955,0.131506,0.113022,0.0961433]),
        H298 = (2.54653,'kcal/mol','+|-',0.461371),
        S298 = (0.074418,'cal/(mol*K)','+|-',0.398684),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOCl_G4    |         20
library:CHOFCl_G4   |         9
library:CHOFClBr_G4 |         2
library:CHOClBr_G4  |         9
""",
)

entry(
    index = 72,
    label = "Cs(Br)-CO",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 CO          u0 {1,S} {6,D}
3    Br1s        u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    O2d         u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.642396,0.434926,0.28201,0.122798,0.00211848,-0.0788144,0.0110401],'cal/(mol*K)','+|-',[0.130862,0.146263,0.14787,0.145435,0.126697,0.10889,0.0926278]),
        H298 = (2.31991,'kcal/mol','+|-',0.444501),
        S298 = (-0.111058,'cal/(mol*K)','+|-',0.384106),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         16
library:CHOFClBr_G4 |         2
library:CHOFBr_G4   |         17
library:CHOClBr_G4  |         9
""",
)

entry(
    index = 73,
    label = "Cs(Val7)3-COs",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 C    u0 {1,S} {6,S}
3    Val7 u0 {1,S}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    O2s  u0 {2,S}
""",
    thermo = None,
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "Cs(Val7)3-CsOs",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 {1,S} {6,S}
3    Val7 u0 {1,S}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0497515,0.0783582,0.0939335,0.19816,0.382482,0.35478,0.480906],'cal/(mol*K)','+|-',[0.119581,0.133655,0.135123,0.132898,0.115776,0.0995031,0.0846431]),
        H298 = (0.36966,'kcal/mol','+|-',0.406184),
        S298 = (-0.994976,'cal/(mol*K)','+|-',0.350995),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         10
library:CHOFClBr_G4 |         8
library:CHOFBr_G4   |         24
library:CHOClBr_G4  |         12
""",
)

entry(
    index = 75,
    label = "Cs(F)3-CsOs",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u0 {1,S} {6,S}
3    F   u0 {1,S}
4    F   u0 {1,S}
5    F   u0 {1,S}
6    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.253983,0.46243,0.433558,0.453034,0.475246,0.36147,0.190065],'cal/(mol*K)','+|-',[0.163983,0.183282,0.185296,0.182245,0.158765,0.13645,0.116072]),
        H298 = (3.26567,'kcal/mol','+|-',0.557004),
        S298 = (-0.552766,'cal/(mol*K)','+|-',0.481324),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         19
library:CHOFCl_G4 |         1
library:CHOFBr_G4 |         6
""",
)

entry(
    index = 76,
    label = "Cs(Cl)3-CsOs",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u0 {1,S} {6,S}
3    Cl  u0 {1,S}
4    Cl  u0 {1,S}
5    Cl  u0 {1,S}
6    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.244657,-0.0272253,0.105771,0.194017,0.284089,0.278936,0.361748],'cal/(mol*K)','+|-',[0.181729,0.203116,0.205348,0.201967,0.175946,0.151216,0.128633]),
        H298 = (1.31798,'kcal/mol','+|-',0.617282),
        S298 = (-0.182703,'cal/(mol*K)','+|-',0.533412),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         19
library:CHOClBr_G4 |         1
""",
)

entry(
    index = 77,
    label = "Cs(Br)3-CsOs",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u0 {1,S} {6,S}
3    Br  u0 {1,S}
4    Br  u0 {1,S}
5    Br  u0 {1,S}
6    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.132326,-0.100362,-0.088418,-0.0700958,0.0134247,0.0518882,0.397422],'cal/(mol*K)','+|-',[0.267728,0.299236,0.302524,0.297542,0.259208,0.222775,0.189505]),
        H298 = (1.37496,'kcal/mol','+|-',0.909394),
        S298 = (-1.12546,'cal/(mol*K)','+|-',0.785835),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOBr_G4  |         10
library:CHOFBr_G4 |         1
""",
)

entry(
    index = 78,
    label = "Cs(Val7)3-CdOs",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 {1,S} {6,S}
3    Val7 u0 {1,S}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20177,-0.21247,-0.244353,-0.0460469,0.157355,0.339933,0.781153],'cal/(mol*K)','+|-',[0.206466,0.230765,0.2333,0.229459,0.199896,0.1718,0.146143]),
        H298 = (7.44325,'kcal/mol','+|-',0.701307),
        S298 = (1.30018,'cal/(mol*K)','+|-',0.60602),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         2
library:CHOFClBr_G4 |         4
library:CHOFBr_G4   |         6
library:CHOClBr_G4  |         4
""",
)

entry(
    index = 79,
    label = "Cs(F)3-CdOs",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 {1,S} {6,S}
3    F   u0 {1,S}
4    F   u0 {1,S}
5    F   u0 {1,S}
6    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.346476,0.178464,0.127667,0.178184,0.112379,0.095405,0.263444],'cal/(mol*K)','+|-',[0.326238,0.364632,0.368639,0.362569,0.315856,0.271461,0.230921]),
        H298 = (6.2014,'kcal/mol','+|-',1.10814),
        S298 = (1.25035,'cal/(mol*K)','+|-',0.957575),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         6
library:CHOFBr_G4 |         1
""",
)

entry(
    index = 80,
    label = "Cs(Cl)3-CdOs",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 {1,S} {6,S}
3    Cl  u0 {1,S}
4    Cl  u0 {1,S}
5    Cl  u0 {1,S}
6    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0745819,0.0266297,0.151812,0.283541,0.313607,0.341311,0.51347],'cal/(mol*K)','+|-',[0.32828,0.366914,0.370946,0.364837,0.317833,0.27316,0.232366]),
        H298 = (3.01916,'kcal/mol','+|-',1.11507),
        S298 = (-0.399395,'cal/(mol*K)','+|-',0.963567),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         6
library:CHOClBr_G4 |         1
""",
)

entry(
    index = 81,
    label = "Cs(Br)3-CdOs",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 {1,S} {6,S}
3    Br  u0 {1,S}
4    Br  u0 {1,S}
5    Br  u0 {1,S}
6    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.455867,-0.0597096,-0.14324,-0.0927532,-0.107564,0.00679977,0.313697],'cal/(mol*K)','+|-',[0.582815,0.651405,0.658563,0.647718,0.564267,0.484957,0.412533]),
        H298 = (6.14095,'kcal/mol','+|-',1.97966),
        S298 = (1.12754,'cal/(mol*K)','+|-',1.71068),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOBr_G4  |         1
library:CHOFBr_G4 |         1
""",
)

entry(
    index = 82,
    label = "Cd(Val7)2=CdOs",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 {1,D} {5,S}
3    Val7 u0 {1,S}
4    Val7 u0 {1,S}
5    O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.453571,-1.28041,-1.50034,-1.30278,-0.887874,-0.531494,-0.284053],'cal/(mol*K)','+|-',[0.136266,0.152303,0.153976,0.151441,0.131929,0.113386,0.0964529]),
        H298 = (5.91884,'kcal/mol','+|-',0.462857),
        S298 = (1.4277,'cal/(mol*K)','+|-',0.399968),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         11
library:CHOFClBr_G4 |         6
library:CHOFBr_G4   |         15
library:CHOClBr_G4  |         11
""",
)

entry(
    index = 83,
    label = "Cd(F)2=CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S}
3    F   u0 {1,S}
4    F   u0 {1,S}
5    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.494795,-1.24385,-1.35935,-1.13515,-0.696934,-0.330716,-0.0505083],'cal/(mol*K)','+|-',[0.152651,0.170616,0.17249,0.16965,0.147793,0.12702,0.10805]),
        H298 = (9.52269,'kcal/mol','+|-',0.518511),
        S298 = (2.1749,'cal/(mol*K)','+|-',0.44806),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         18
library:CHOFCl_G4 |         6
library:CHOFBr_G4 |         14
""",
)

entry(
    index = 84,
    label = "Cd(Cl)2=CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S}
3    Cl  u0 {1,S}
4    Cl  u0 {1,S}
5    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.385662,-1.11567,-1.30982,-1.14563,-0.802146,-0.4834,-0.311198],'cal/(mol*K)','+|-',[0.186939,0.208939,0.211235,0.207757,0.18099,0.155551,0.132321]),
        H298 = (5.9382,'kcal/mol','+|-',0.634978),
        S298 = (1.96528,'cal/(mol*K)','+|-',0.548703),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library            | Number of Species
library:CHOCl_G4   |         19
library:CHOClBr_G4 |         6
""",
)

entry(
    index = 85,
    label = "Cd(Br)2=CdOs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S}
3    Br  u0 {1,S}
4    Br  u0 {1,S}
5    O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.509935,-1.07314,-1.25114,-1.01773,-0.642749,-0.349817,-0.236676],'cal/(mol*K)','+|-',[0.242505,0.271045,0.274023,0.269511,0.234787,0.201787,0.171652]),
        H298 = (4.7386,'kcal/mol','+|-',0.82372),
        S298 = (0.360208,'cal/(mol*K)','+|-',0.711801),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         14
""",
)

entry(
    index = 86,
    label = "Cd(Val7)=CdOs",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {4,S}
2 *2 Cd          u0 {1,D} {5,S}
3    Val7        u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    O2s         u0 {2,S}
""",
    thermo = None,
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library| Number of Species
""",
)

entry(
    index = 87,
    label = "Cd(F)=CdOs",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {4,S}
2 *2 Cd          u0 {1,D} {5,S}
3    F           u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    O2s         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678754,-1.36075,-1.46251,-1.25875,-0.799514,-0.442528,-0.237204],'cal/(mol*K)','+|-',[0.106117,0.118606,0.119909,0.117935,0.10274,0.0882997,0.0751128]),
        H298 = (7.73655,'kcal/mol','+|-',0.36045),
        S298 = (1.91714,'cal/(mol*K)','+|-',0.311476),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOF_G4     |         30
library:CHOFCl_G4   |         19
library:CHOFClBr_G4 |         4
library:CHOFBr_G4   |         29
""",
)

entry(
    index = 88,
    label = "Cd(Cl)=CdOs",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {4,S}
2 *2 Cd          u0 {1,D} {5,S}
3    Cl          u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    O2s         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83265,-1.52071,-1.62737,-1.40122,-0.856566,-0.450082,-0.259538],'cal/(mol*K)','+|-',[0.124031,0.138627,0.140151,0.137843,0.120084,0.103205,0.0877924]),
        H298 = (5.96841,'kcal/mol','+|-',0.421297),
        S298 = (1.9389,'cal/(mol*K)','+|-',0.364055),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOCl_G4    |         30
library:CHOFCl_G4   |         7
library:CHOFClBr_G4 |         3
library:CHOClBr_G4  |         19
""",
)

entry(
    index = 89,
    label = "Cd(Br)=CdOs",
    group = 
"""
1 *1 Cd          u0 {2,D} {3,S} {4,S}
2 *2 Cd          u0 {1,D} {5,S}
3    Br          u0 {1,S}
4    [C,H,O,N,S] u0 {1,S}
5    O2s         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.96471,-1.75494,-1.89773,-1.64427,-0.980527,-0.494077,-0.302675],'cal/(mol*K)','+|-',[0.139216,0.1556,0.15731,0.154719,0.134785,0.115841,0.0985409]),
        H298 = (5.90028,'kcal/mol','+|-',0.472876),
        S298 = (2.07085,'cal/(mol*K)','+|-',0.408626),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOBr_G4    |         26
library:CHOFClBr_G4 |         1
library:CHOFBr_G4   |         12
library:CHOClBr_G4  |         7
""",
)

entry(
    index = 90,
    label = "intRVal7",
    group = 
"""
1 *1 [Cs,Cd,CO] u0 {2,[S,D]} {4,S}
2    R!H        ux {1,[S,D]} {3,[S,D]}
3 *2 [Cs,Cd,CO] u0 {2,[S,D]}
4    Val7       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "Cs(Val7)3-R-Cs(Val7)3",
    group = 
"""
1  *1 Cs   u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs   u0 {3,S} {5,S} {7,S} {9,S}
3     R!H  ux {1,S} {2,S} {10,S}
4     Val7 u0 {1,S}
5     Val7 u0 {2,S}
6     Val7 u0 {1,S}
7     Val7 u0 {2,S}
8     Val7 u0 {1,S}
9     Val7 u0 {2,S}
10    R!H  u0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "Cs(F)3-R-Cs(F)3",
    group = 
"""
1  *1 Cs  u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs  u0 {3,S} {5,S} {7,S} {9,S}
3     R!H ux {1,S} {2,S} {10,S}
4     F   u0 {1,S}
5     F   u0 {2,S}
6     F   u0 {1,S}
7     F   u0 {2,S}
8     F   u0 {1,S}
9     F   u0 {2,S}
10    R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0536953,0.0191018,0.140117,0.214366,0.247385,0.270068,0.324087],'cal/(mol*K)','+|-',[0.0851459,0.0951665,0.0962123,0.0946279,0.0824363,0.0708495,0.0602687]),
        H298 = (1.9218,'kcal/mol','+|-',0.289216),
        S298 = (-1.02994,'cal/(mol*K)','+|-',0.249921),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         14
""",
)

entry(
    index = 93,
    label = "Cs(Cl)3-R-Cs(Cl)3",
    group = 
"""
1  *1 Cs  u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs  u0 {3,S} {5,S} {7,S} {9,S}
3     R!H ux {1,S} {2,S} {10,S}
4     Cl  u0 {1,S}
5     Cl  u0 {2,S}
6     Cl  u0 {1,S}
7     Cl  u0 {2,S}
8     Cl  u0 {1,S}
9     Cl  u0 {2,S}
10    R!H u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.423779,0.325903,0.268323,0.231788,0.168362,0.132954,0.106658],'cal/(mol*K)','+|-',[0.0872624,0.0975321,0.0986038,0.0969801,0.0844854,0.0726106,0.0617668]),
        H298 = (5.27416,'kcal/mol','+|-',0.296405),
        S298 = (-1.16713,'cal/(mol*K)','+|-',0.256133),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         14
""",
)

entry(
    index = 94,
    label = "Cs(Br)3-R-Cs(Br)3",
    group = 
"""
1  *1 Cs  u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs  u0 {3,S} {5,S} {7,S} {9,S}
3     R!H ux {1,S} {2,S} {10,S}
4     Br  u0 {1,S}
5     Br  u0 {2,S}
6     Br  u0 {1,S}
7     Br  u0 {2,S}
8     Br  u0 {1,S}
9     Br  u0 {2,S}
10    R!H u0 {3,S}
""",
    thermo = None,
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cs(Val7)3-R-Cs(Val7)2",
    group = 
"""
1  *1 Cs          u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs          u0 {3,S} {5,S} {7,S} {9,S}
3     R!H         ux {1,S} {2,S} {10,S}
4     Val7        u0 {1,S}
5     Val7        u0 {2,S}
6     Val7        u0 {1,S}
7     Val7        u0 {2,S}
8     Val7        u0 {1,S}
9     [C,H,N,O,S] u0 {2,S}
10    R!H         u0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "Cs(F)3-R-Cs(F)2",
    group = 
"""
1  *1 Cs          u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs          u0 {3,S} {5,S} {7,S} {9,S}
3     R!H         ux {1,S} {2,S} {10,S}
4     F           u0 {1,S}
5     F           u0 {2,S}
6     F           u0 {1,S}
7     F           u0 {2,S}
8     F           u0 {1,S}
9     [C,H,N,O,S] u0 {2,S}
10    R!H         u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.10085,-0.0376323,0.129194,0.173183,0.105408,0.117052,0.19886],'cal/(mol*K)','+|-',[0.140308,0.15682,0.158543,0.155933,0.135843,0.116749,0.0993138]),
        H298 = (2.72867,'kcal/mol','+|-',0.476585),
        S298 = (0.333882,'cal/(mol*K)','+|-',0.411832),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         26
""",
)

entry(
    index = 97,
    label = "Cs(Cl)3-R-Cs(Cl)2",
    group = 
"""
1  *1 Cs          u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs          u0 {3,S} {5,S} {7,S} {9,S}
3     R!H         ux {1,S} {2,S} {10,S}
4     Cl          u0 {1,S}
5     Cl          u0 {2,S}
6     Cl          u0 {1,S}
7     Cl          u0 {2,S}
8     Cl          u0 {1,S}
9     [C,H,N,O,S] u0 {2,S}
10    R!H         u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.189116,-0.0860562,-0.248296,-0.31494,-0.343759,-0.287109,-0.0861114],'cal/(mol*K)','+|-',[0.14199,0.1587,0.160444,0.157802,0.137471,0.118149,0.100504]),
        H298 = (6.11769,'kcal/mol','+|-',0.482298),
        S298 = (-0.18798,'cal/(mol*K)','+|-',0.416768),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         26
""",
)

entry(
    index = 98,
    label = "Cs(Br)3-R-Cs(Br)2",
    group = 
"""
1  *1 Cs          u0 {3,S} {4,S} {6,S} {8,S}
2  *2 Cs          u0 {3,S} {5,S} {7,S} {9,S}
3     R!H         ux {1,S} {2,S} {10,S}
4     Br          u0 {1,S}
5     Br          u0 {2,S}
6     Br          u0 {1,S}
7     Br          u0 {2,S}
8     Br          u0 {1,S}
9     [C,H,N,O,S] u0 {2,S}
10    R!H         u0 {3,S}
""",
    thermo = None,
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         2
""",
)

entry(
    index = 99,
    label = "Cs(Val7)3-R-C(Val7)",
    group = 
"""
1 *1 Cs      u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H     ux {1,[S,D]} {3,[S,D]}
3 *2 [Cs,Cd] u0 {2,[S,D]} {7,S}
4    Val7    u0 {1,S}
5    Val7    u0 {1,S}
6    Val7    u0 {1,S}
7    Val7    u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "Cs(Val7)3-R-Cds(Val7)",
    group = 
"""
1 *1 Cs        u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,S} {2,[S,D]}
4    Val7      u0 {1,S}
5    Val7      u0 {1,S}
6    Val7      u0 {1,S}
7    Val7      u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.360785,-0.0412382,0.208141,0.393838,0.560745,0.676692,0.927224],'cal/(mol*K)','+|-',[0.155578,0.173887,0.175798,0.172903,0.150627,0.129455,0.110122]),
        H298 = (1.37525,'kcal/mol','+|-',0.528453),
        S298 = (0.895676,'cal/(mol*K)','+|-',0.456652),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFClBr_G4 |         9
library:CHOFBr_G4   |         15
library:CHOClBr_G4  |         9
""",
)

entry(
    index = 101,
    label = "Cs(F)3-R-Cds(F)",
    group = 
"""
1 *1 Cs        u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,S} {2,[S,D]}
4    F         u0 {1,S}
5    F         u0 {1,S}
6    F         u0 {1,S}
7    F         u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.520463,-0.260359,0.0245977,0.166647,0.196998,0.177119,0.236754],'cal/(mol*K)','+|-',[0.180888,0.202176,0.204398,0.201032,0.175132,0.150516,0.128038]),
        H298 = (0.829319,'kcal/mol','+|-',0.614426),
        S298 = (0.716855,'cal/(mol*K)','+|-',0.530944),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         24
""",
)

entry(
    index = 102,
    label = "Cs(Cl)3-R-Cds(Cl)",
    group = 
"""
1 *1 Cs        u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,S} {2,[S,D]}
4    Cl        u0 {1,S}
5    Cl        u0 {1,S}
6    Cl        u0 {1,S}
7    Cl        u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.120592,0.114628,0.139861,0.141065,0.145024,0.168425,0.279768],'cal/(mol*K)','+|-',[0.182815,0.20433,0.206575,0.203173,0.176997,0.152119,0.129401]),
        H298 = (2.11523,'kcal/mol','+|-',0.620969),
        S298 = (0.0710461,'cal/(mol*K)','+|-',0.536598),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         24
""",
)

entry(
    index = 103,
    label = "Cs(Br)3-R-Cds(Br)",
    group = 
"""
1 *1 Cs        u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,S} {2,[S,D]}
4    Br        u0 {1,S}
5    Br        u0 {1,S}
6    Br        u0 {1,S}
7    Br        u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = None,
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "Cs(Val7)3-R-Cds(Val7)2",
    group = 
"""
1 *1 Cs   u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd   u0 {3,D} {7,S} {8,S}
3    R!H  ux {1,S} {2,D}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    Val7 u0 {1,S}
7    Val7 u0 {2,S}
8    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0878905,0.209475,0.239065,0.19681,0.0199138,-0.0548582,0.00246089],'cal/(mol*K)','+|-',[0.410152,0.458422,0.463459,0.455827,0.397099,0.341285,0.290317]),
        H298 = (2.4843,'kcal/mol','+|-',1.39317),
        S298 = (2.44707,'cal/(mol*K)','+|-',1.20388),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOFBr_G4 |         4
""",
)

entry(
    index = 105,
    label = "Cs(F)3-R-Cds(F)2",
    group = 
"""
1 *1 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,D} {7,S} {8,S}
3    R!H ux {1,S} {2,D}
4    F   u0 {1,S}
5    F   u0 {1,S}
6    F   u0 {1,S}
7    F   u0 {2,S}
8    F   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.711296,-0.546028,-0.309022,-0.156667,-0.124581,-0.143955,-0.0280199],'cal/(mol*K)','+|-',[0.26756,0.299048,0.302334,0.297356,0.259045,0.222635,0.189386]),
        H298 = (1.75222,'kcal/mol','+|-',0.908824),
        S298 = (-0.587698,'cal/(mol*K)','+|-',0.785342),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         8
""",
)

entry(
    index = 106,
    label = "Cs(Cl)3-R-Cds(Cl)2",
    group = 
"""
1 *1 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,D} {7,S} {8,S}
3    R!H ux {1,S} {2,D}
4    Cl  u0 {1,S}
5    Cl  u0 {1,S}
6    Cl  u0 {1,S}
7    Cl  u0 {2,S}
8    Cl  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.305208,0.41396,0.423655,0.444474,0.412851,0.407651,0.483941],'cal/(mol*K)','+|-',[0.271242,0.303164,0.306495,0.301448,0.26261,0.225699,0.191993]),
        H298 = (7.23178,'kcal/mol','+|-',0.921333),
        S298 = (-1.56525,'cal/(mol*K)','+|-',0.796151),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         8
""",
)

entry(
    index = 107,
    label = "Cs(Br)3-R-Cds(Br)2",
    group = 
"""
1 *1 Cs  u0 {3,S} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,D} {7,S} {8,S}
3    R!H ux {1,S} {2,D}
4    Br  u0 {1,S}
5    Br  u0 {1,S}
6    Br  u0 {1,S}
7    Br  u0 {2,S}
8    Br  u0 {2,S}
""",
    thermo = None,
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "Cs(Val7)3-R-CO",
    group = 
"""
1 *1 Cs   u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H  ux {1,[S,D]} {3,[S,D]}
3 *2 CO   u0 {2,[S,D]} {7,D}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    Val7 u0 {1,S}
7    O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.28792,1.68908,1.71197,1.57447,1.10652,0.695355,0.232733],'cal/(mol*K)','+|-',[0.185964,0.20785,0.210134,0.206673,0.180046,0.15474,0.131631]),
        H298 = (2.37584,'kcal/mol','+|-',0.631667),
        S298 = (-0.115162,'cal/(mol*K)','+|-',0.545842),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library             | Number of Species
library:CHOFCl_G4   |         4
library:CHOFClBr_G4 |         2
library:CHOFBr_G4   |         10
library:CHOClBr_G4  |         4
""",
)

entry(
    index = 109,
    label = "Cs(F)3-R-CO",
    group = 
"""
1 *1 Cs  u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H ux {1,[S,D]} {3,[S,D]}
3 *2 CO  u0 {2,[S,D]} {7,D}
4    F   u0 {1,S}
5    F   u0 {1,S}
6    F   u0 {1,S}
7    O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.676581,0.737019,0.716671,0.627472,0.397746,0.228975,0.034705],'cal/(mol*K)','+|-',[0.254142,0.284051,0.287173,0.282444,0.246054,0.21147,0.179889]),
        H298 = (1.9062,'kcal/mol','+|-',0.863247),
        S298 = (0.0645047,'cal/(mol*K)','+|-',0.745958),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library           | Number of Species
library:CHOF_G4   |         8
library:CHOFBr_G4 |         3
""",
)

entry(
    index = 110,
    label = "Cs(Cl)3-R-CO",
    group = 
"""
1 *1 Cs  u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H ux {1,[S,D]} {3,[S,D]}
3 *2 CO  u0 {2,[S,D]} {7,D}
4    Cl  u0 {1,S}
5    Cl  u0 {1,S}
6    Cl  u0 {1,S}
7    O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.758337,0.918714,0.955907,0.90391,0.687791,0.478327,0.216737],'cal/(mol*K)','+|-',[0.296711,0.331631,0.335275,0.329754,0.287269,0.246892,0.210021]),
        H298 = (1.34802,'kcal/mol','+|-',1.00784),
        S298 = (-0.785265,'cal/(mol*K)','+|-',0.870908),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         8
""",
)

entry(
    index = 111,
    label = "Cs(Br)3-R-CO",
    group = 
"""
1 *1 Cs  u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H ux {1,[S,D]} {3,[S,D]}
3 *2 CO  u0 {2,[S,D]} {7,D}
4    Br  u0 {1,S}
5    Br  u0 {1,S}
6    Br  u0 {1,S}
7    O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.59529,1.90393,1.87184,1.68818,1.1184,0.615772,-0.07249],'cal/(mol*K)','+|-',[0.568867,0.635816,0.642803,0.632218,0.550764,0.473352,0.402661]),
        H298 = (3.63807,'kcal/mol','+|-',1.93228),
        S298 = (-1.12272,'cal/(mol*K)','+|-',1.66974),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         2
""",
)

entry(
    index = 112,
    label = "int14_gauche",
    group = 
"""
1 *1 [Cs,O2s,Cd,S2s] u0 {2,S}
2 *2 Cs              u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "CsCs",
    group = 
"""
1 *1 Cs u0 {2,S}
2 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "CsCs-P",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Lumped PP/PS/PT/PQ, because they all counted as 0 as long as the first carbon is primary carbon""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "CsCs-S",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    Cs                          u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "CsCs-SS",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
8    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "CsCs-ST",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "CsCs-SQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    Cs                          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "CsCs-T",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "CsCs-TT",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Half Value!!!
""",
)

entry(
    index = 121,
    label = "CsCs-T(TTP)",
    group = 
"""
1  *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2  *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3     Cs                          u0 {1,S} {9,S} {10,S} {11,S}
4     Cs                          u0 {1,S} {12,S} {13,S} {14,S}
5     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6     Cs                          u0 {2,S}
7     Cs                          u0 {2,S}
8     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
9     Cs                          u0 {3,S}
10    Cs                          u0 {3,S}
11    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {3,S}
12    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
13    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
14    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 122,
    label = "CsCs-T(TTS)",
    group = 
"""
1  *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2  *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3     Cs                          u0 {1,S} {9,S} {10,S} {11,S}
4     Cs                          u0 {1,S} {12,S} {13,S} {14,S}
5     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6     Cs                          u0 {2,S}
7     Cs                          u0 {2,S}
8     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
9     Cs                          u0 {3,S}
10    Cs                          u0 {3,S}
11    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {3,S}
12    Cs                          u0 {4,S}
13    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
14    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 123,
    label = "CsCs-T(TTT)",
    group = 
"""
1  *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2  *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3     Cs                          u0 {1,S} {9,S} {10,S} {11,S}
4     Cs                          u0 {1,S} {12,S} {13,S} {14,S}
5     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6     Cs                          u0 {2,S}
7     Cs                          u0 {2,S}
8     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
9     Cs                          u0 {3,S}
10    Cs                          u0 {3,S}
11    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {3,S}
12    Cs                          u0 {4,S}
13    Cs                          u0 {4,S}
14    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.067,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
(2 GI) / 2 + (1 GI) / 3 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 124,
    label = "CsCs-T(TTQ)",
    group = 
"""
1  *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2  *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3     Cs                          u0 {1,S} {9,S} {10,S} {11,S}
4     Cs                          u0 {1,S} {12,S} {13,S} {14,S}
5     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6     Cs                          u0 {2,S}
7     Cs                          u0 {2,S}
8     [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
9     Cs                          u0 {3,S}
10    Cs                          u0 {3,S}
11    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {3,S}
12    Cs                          u0 {4,S}
13    Cs                          u0 {4,S}
14    Cs                          u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 125,
    label = "CsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                          u0 {1,S} {6,S} {7,S} {8,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
7    Cs                          u0 {2,S}
8    Cs                          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "CsCs-Q",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "CsCs-QQ",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs u0 {1,S} {6,S} {7,S} {8,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {2,S}
7    Cs u0 {2,S}
8    Cs u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Half Value!!!
""",
)

entry(
    index = 128,
    label = "OsCs",
    group = 
"""
1 *1 O2s u0 {2,S}
2 *2 Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "OsCs-P",
    group = 
"""
1 *1 O2s                         u0 {2,S} {3,S}
2 *2 Cs                          u0 {1,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "OsCs-S",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cs  u0 {1,S}
3    Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "OsCs-SP",
    group = 
"""
1 *2 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s                         u0 {1,S} {6,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "OsCs-SS",
    group = 
"""
1 *2 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *1 O2s                         u0 {1,S} {6,S}
3    Cs                          u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cs                          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "OsCs-ST",
    group = 
"""
1 *1 O2s                         u0 {2,S} {3,S}
2 *2 Cs                          u0 {1,S} {4,S} {5,S} {6,S}
3    Cs                          u0 {1,S}
4    Cs                          u0 {2,S}
5    Cs                          u0 {2,S}
6    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "OsCs-SQ",
    group = 
"""
1 *1 O2s u0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S} {5,S} {6,S}
3    Cs  u0 {1,S}
4    Cs  u0 {2,S}
5    Cs  u0 {2,S}
6    Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Cd u0 {1,D}
3 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "CdCs-P",
    group = 
"""
1 *1 Cd                          u0 {2,D} {3,S} {4,S}
2    Cd                          u0 {1,D}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4 *2 Cs                          u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "CdCs-S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D}
3    Cs u0 {1,S}
4 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "CdCs-SP",
    group = 
"""
1 *2 Cs                          u0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd                          u0 {1,S} {6,D} {7,S}
3    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
4    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
5    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
6    Cd                          u0 {2,D}
7    Cs                          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "CdCs-SS",
    group = 
"""
1 *1 Cd                          u0 {2,D} {3,S} {4,S}
2    Cd                          u0 {1,D}
3    Cs                          u0 {1,S}
4 *2 Cs                          u0 {1,S} {5,S} {6,S} {7,S}
5    Cs                          u0 {4,S}
6    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
7    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "CdCs-ST",
    group = 
"""
1 *1 Cd                          u0 {2,D} {3,S} {4,S}
2    Cd                          u0 {1,D}
3    Cs                          u0 {1,S}
4 *2 Cs                          u0 {1,S} {5,S} {6,S} {7,S}
5    Cs                          u0 {4,S}
6    Cs                          u0 {4,S}
7    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "CdCs-SQ",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2    Cd u0 {1,D}
3    Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5    Cs u0 {4,S}
6    Cs u0 {4,S}
7    Cs u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "int15",
    group = 
"""
1 *1 Cs           u0 {2,S} {4,S} {5,S}
2    [Cs,O2s,S2s] u0 {1,S} {3,S}
3 *2 Cs           u0 {2,S} {6,S} {7,S} {8,S}
4    Cs           u0 {1,S}
5    Cs           u0 {1,S}
6    Cs           u0 {3,S}
7    Cs           u0 {3,S}
8    Cs           u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "CsCsCs",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S}
2    Cs u0 {1,S} {3,S}
3 *2 Cs u0 {2,S} {6,S} {7,S} {8,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {3,S}
7    Cs u0 {3,S}
8    Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "CsCsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {4,S} {5,S} {9,S}
2    Cs                          u0 {1,S} {3,S}
3 *2 Cs                          u0 {2,S} {6,S} {7,S} {8,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
6    Cs                          u0 {3,S}
7    Cs                          u0 {3,S}
8    Cs                          u0 {3,S}
9    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "CsCsCs-QQ",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Cs u0 {1,S} {3,S}
3 *2 Cs u0 {2,S} {7,S} {8,S} {9,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {1,S}
7    Cs u0 {3,S}
8    Cs u0 {3,S}
9    Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Half Value!!!
""",
)

entry(
    index = 146,
    label = "CsOsCs",
    group = 
"""
1 *1 Cs  u0 {2,S} {4,S} {5,S}
2    O2s u0 {1,S} {3,S}
3 *2 Cs  u0 {2,S} {6,S} {7,S} {8,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "CsOsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {4,S} {5,S} {9,S}
2    O2s                         u0 {1,S} {3,S}
3 *2 Cs                          u0 {2,S} {6,S} {7,S} {8,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
6    Cs                          u0 {3,S}
7    Cs                          u0 {3,S}
8    Cs                          u0 {3,S}
9    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "CsOsCs-QQ",
    group = 
"""
1 *1 Cs  u0 {2,S} {4,S} {5,S} {6,S}
2    O2s u0 {1,S} {3,S}
3 *2 Cs  u0 {2,S} {7,S} {8,S} {9,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Half Value!!!
""",
)

entry(
    index = 149,
    label = "CsSsCs",
    group = 
"""
1 *1 Cs  u0 {2,S} {4,S} {5,S}
2    S2s u0 {1,S} {3,S}
3 *2 Cs  u0 {2,S} {6,S} {7,S} {8,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {3,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "CsSsCs-TQ",
    group = 
"""
1 *1 Cs                          u0 {2,S} {4,S} {5,S} {9,S}
2    S2s                         u0 {1,S} {3,S}
3 *2 Cs                          u0 {2,S} {6,S} {7,S} {8,S}
4    Cs                          u0 {1,S}
5    Cs                          u0 {1,S}
6    Cs                          u0 {3,S}
7    Cs                          u0 {3,S}
8    Cs                          u0 {3,S}
9    [Cd,Cdd,Ct,Cb,Cbf,O2s,CO,H] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.1,-0.2,-0.1,0,0.2,0.1,-0.2],'cal/(mol*K)'),
        H298 = (3.1,'kcal/mol'),
        S298 = (-1.9,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "CsSsCs-QQ",
    group = 
"""
1 *1 Cs  u0 {2,S} {4,S} {5,S} {6,S}
2    S2s u0 {1,S} {3,S}
3 *2 Cs  u0 {2,S} {7,S} {8,S} {9,S}
4    Cs  u0 {1,S}
5    Cs  u0 {1,S}
6    Cs  u0 {1,S}
7    Cs  u0 {3,S}
8    Cs  u0 {3,S}
9    Cs  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.5,-0.5,-0.4,-0.35,-0.3,-0.35,-0.5],'cal/(mol*K)'),
        H298 = (2.85,'kcal/mol'),
        S298 = (-0.85,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Half Value!!!
""",
)

tree(
"""
L1: R
    L2: intVal7
        L3: Cs(Val7)3-Cs(Val7)3
            L4: Cs(Cl)3-Cs(Cl)3
            L4: Cs(F)3-Cs(F)3
            L4: Cs(Br)3-Cs(Br)3
        L3: Cs(Val7)3-Cs(Val7)2
            L4: Cs(Cl)3-Cs(Cl)2
            L4: Cs(F)3-Cs(F)2
            L4: Cs(Br)3-Cs(Br)2
        L3: Cs(Val7)3-C(Val7)
            L4: Cs(Val7)3-Cs(Val7)
                L5: Cs(Cl)3-Cs(Cl)
                L5: Cs(F)3-Cs(F)
                L5: Cs(Br)3-Cs(Br)
            L4: Cs(Val7)3-Cds(Val7)
                L5: Cs(Cl)3-Cds(Cl)
                L5: Cs(F)3-Cds(F)
                L5: Cs(Br)3-Cds(Br)
        L3: Cs(Val7)2-Cs(Val7)2
            L4: Cs(Cl)2-Cs(Cl)2
            L4: Cs(F)2-Cs(F)2
            L4: Cs(Br)2-Cs(Br)2
        L3: Cs(Val7)2-C(Val7)
            L4: Cs(Val7)2-Cs(Val7)
                L5: Cs(Cl)2-Cs(Cl)
                L5: Cs(F)2-Cs(F)
                L5: Cs(Br)2-Cs(Br)
            L4: Cs(Val7)2-Cds(Val7)
                L5: Cs(Cl)2-Cds(Cl)
                L5: Cs(F)2-Cds(F)
                L5: Cs(Br)2-Cds(Br)
        L3: C(Val7)-C(Val7)
            L4: Cs(Val7)-Cs(Val7)
                L5: Cs(Cl)-Cs(Cl)
                L5: Cs(F)-Cs(F)
                L5: Cs(Br)-Cs(Br)
            L4: Cs(Val7)-Cds(Val7)
                L5: Cs(Cl)-Cds(Cl)
                L5: Cs(F)-Cds(F)
                L5: Cs(Br)-Cds(Br)
            L4: Cds(Val7)-Cds(Val7)
                L5: Cds(Cl)-Cds(Cl)
                L5: Cds(F)-Cds(F)
                L5: Cds(Br)-Cds(Br)
        L3: Cds(Val7)=Cds(Val7)
            L4: Cds(Cl)=Cds(Cl)
            L4: Cds(F)=Cds(F)
            L4: Cds(Br)=Cds(Br)
        L3: Cds(Val7)2=Cds(Val7)
            L4: Cds(Cl)2=Cds(Cl)
            L4: Cds(F)2=Cds(F)
            L4: Cds(Br)2=Cds(Br)
        L3: Cds(Val7)2=Cds(Val7)2
            L4: Cds(Cl)2=Cds(Cl)2
            L4: Cds(F)2=Cds(F)2
            L4: Cds(Br)2=Cds(Br)2
        L3: Cd(Val7)-CO
            L4: Cd(F)-CO
            L4: Cd(Cl)-CO
            L4: Cd(Br)-CO
        L3: Cs(Val7)3-CO
            L4: Cs(F)3-CO
            L4: Cs(Cl)3-CO
            L4: Cs(Br)3-CO
        L3: Cs(Val7)2-CO
            L4: Cs(F)2-CO
            L4: Cs(Cl)2-CO
            L4: Cs(Br)2-CO
        L3: Cs(Val7)-CO
            L4: Cs(F)-CO
            L4: Cs(Cl)-CO
            L4: Cs(Br)-CO
        L3: Cs(Val7)3-COs
            L4: Cs(Val7)3-CsOs
                L5: Cs(F)3-CsOs
                L5: Cs(Cl)3-CsOs
                L5: Cs(Br)3-CsOs
            L4: Cs(Val7)3-CdOs
                L5: Cs(F)3-CdOs
                L5: Cs(Cl)3-CdOs
                L5: Cs(Br)3-CdOs
        L3: Cd(Val7)2=CdOs
            L4: Cd(F)2=CdOs
            L4: Cd(Cl)2=CdOs
            L4: Cd(Br)2=CdOs
        L3: Cd(Val7)=CdOs
            L4: Cd(F)=CdOs
            L4: Cd(Cl)=CdOs
            L4: Cd(Br)=CdOs
    L2: intRVal7
        L3: Cs(Val7)3-R-Cs(Val7)3
            L4: Cs(F)3-R-Cs(F)3
            L4: Cs(Cl)3-R-Cs(Cl)3
            L4: Cs(Br)3-R-Cs(Br)3
        L3: Cs(Val7)3-R-Cs(Val7)2
            L4: Cs(F)3-R-Cs(F)2
            L4: Cs(Cl)3-R-Cs(Cl)2
            L4: Cs(Br)3-R-Cs(Br)2
        L3: Cs(Val7)3-R-C(Val7)
            L4: Cs(Val7)3-R-Cds(Val7)
                L5: Cs(F)3-R-Cds(F)
                L5: Cs(Cl)3-R-Cds(Cl)
                L5: Cs(Br)3-R-Cds(Br)
            L4: Cs(Val7)3-R-Cds(Val7)2
                L5: Cs(F)3-R-Cds(F)2
                L5: Cs(Cl)3-R-Cds(Cl)2
                L5: Cs(Br)3-R-Cds(Br)2
        L3: Cs(Val7)3-R-CO
            L4: Cs(F)3-R-CO
            L4: Cs(Cl)3-R-CO
            L4: Cs(Br)3-R-CO
    L2: int14_gauche
        L3: CsCs
            L4: CsCs-P
            L4: CsCs-S
                L5: CsCs-SS
                L5: CsCs-ST
                L5: CsCs-SQ
            L4: CsCs-T
                L5: CsCs-TT
                    L6: CsCs-T(TTP)
                    L6: CsCs-T(TTS)
                    L6: CsCs-T(TTT)
                    L6: CsCs-T(TTQ)
                L5: CsCs-TQ
            L4: CsCs-Q
                L5: CsCs-QQ
        L3: OsCs
            L4: OsCs-P
            L4: OsCs-S
                L5: OsCs-SP
                L5: OsCs-SS
                L5: OsCs-ST
                L5: OsCs-SQ
        L3: CdCs
            L4: CdCs-P
            L4: CdCs-S
                L5: CdCs-SP
                L5: CdCs-SS
                L5: CdCs-ST
                L5: CdCs-SQ
    L2: int15
        L3: CsCsCs
            L4: CsCsCs-TQ
            L4: CsCsCs-QQ
        L3: CsOsCs
            L4: CsOsCs-TQ
            L4: CsOsCs-QQ
        L3: CsSsCs
            L4: CsSsCs-TQ
            L4: CsSsCs-QQ
"""
)

