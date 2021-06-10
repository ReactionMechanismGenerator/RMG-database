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
        Cpdata = ([-0.0259703,0.145361,0.228419,0.264736,0.272031,0.260902,0.386662],'cal/(mol*K)','+|-',[0.194532,0.223575,0.228548,0.225195,0.195275,0.168423,0.137261]),
        H298 = (4.00851,'kcal/mol','+|-',0.69349),
        S298 = (0.213049,'cal/(mol*K)','+|-',0.472655),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         5
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
        Cpdata = ([0.58395,0.422438,0.329857,0.265712,0.142862,0.039853,-0.000261073],'cal/(mol*K)','+|-',[0.426787,0.490505,0.501416,0.49406,0.428416,0.369505,0.301139]),
        H298 = (4.083,'kcal/mol','+|-',1.52146),
        S298 = (-0.560747,'cal/(mol*K)','+|-',1.03697),
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
        Cpdata = ([0.120285,0.291299,0.303352,0.332491,0.374215,0.363645,0.297872],'cal/(mol*K)','+|-',[0.424053,0.487362,0.498204,0.490894,0.425672,0.367138,0.299209]),
        H298 = (5.51679,'kcal/mol','+|-',1.51171),
        S298 = (-0.927557,'cal/(mol*K)','+|-',1.03032),
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
        Cpdata = ([-0.641264,-0.611657,-0.463313,-0.410666,-0.367564,-0.278016,0.26121],'cal/(mol*K)','+|-',[0.12583,0.144616,0.147833,0.145664,0.126311,0.108942,0.0887851]),
        H298 = (4.63192,'kcal/mol','+|-',0.448574),
        S298 = (1.83946,'cal/(mol*K)','+|-',0.30573),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         8
CHOFClBr_G4 |         15
CHOFBr_G4   |         20
CHOClBr_G4  |         11
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
        Cpdata = ([-0.0562964,-0.279006,-0.263713,-0.232479,-0.195939,-0.109275,0.408085],'cal/(mol*K)','+|-',[0.171967,0.197641,0.202038,0.199074,0.172624,0.148886,0.121339]),
        H298 = (9.19951,'kcal/mol','+|-',0.613048),
        S298 = (0.302736,'cal/(mol*K)','+|-',0.417829),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         40
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
        Cpdata = ([-0.227608,-0.224725,-0.105533,-0.0413895,-0.021153,0.0368277,0.363019],'cal/(mol*K)','+|-',[0.162445,0.186697,0.19085,0.18805,0.163065,0.140642,0.11462]),
        H298 = (10.1314,'kcal/mol','+|-',0.579102),
        S298 = (1.73408,'cal/(mol*K)','+|-',0.394693),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         41
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
        Cpdata = ([-0.174914,-0.468033,-0.577286,-0.695076,-0.868638,-0.895252,-0.406172],'cal/(mol*K)','+|-',[0.840468,0.965947,0.987434,0.972947,0.843677,0.727664,0.59303]),
        H298 = (5.01486,'kcal/mol','+|-',2.9962),
        S298 = (2.35415,'cal/(mol*K)','+|-',2.04209),
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
        Cpdata = ([-0.272434,-0.28022,-0.208647,-0.165339,-0.112686,-0.0594042,0.277132],'cal/(mol*K)','+|-',[0.0940798,0.108126,0.110531,0.108909,0.094439,0.0814528,0.0663822]),
        H298 = (2.92929,'kcal/mol','+|-',0.335387),
        S298 = (1.94606,'cal/(mol*K)','+|-',0.228586),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         15
CHOFClBr_G4 |         21
CHOFBr_G4   |         63
CHOClBr_G4  |         21
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
        Cpdata = ([-0.218209,-0.313114,-0.280043,-0.250572,-0.215988,-0.129575,0.282924],'cal/(mol*K)','+|-',[0.138023,0.158629,0.162158,0.159779,0.13855,0.119498,0.0973881]),
        H298 = (5.43337,'kcal/mol','+|-',0.492039),
        S298 = (1.24034,'cal/(mol*K)','+|-',0.335354),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         60
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
        Cpdata = ([0.0765787,0.195496,0.229714,0.210363,0.151387,0.122269,0.252817],'cal/(mol*K)','+|-',[0.129794,0.149171,0.15249,0.150253,0.130289,0.112373,0.0915817]),
        H298 = (6.64698,'kcal/mol','+|-',0.462703),
        S298 = (1.38455,'cal/(mol*K)','+|-',0.31536),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         62
CHOFBr_G4 |         2
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
        Cpdata = ([-0.468657,-0.616864,-0.632656,-0.67907,-0.720854,-0.606538,0.0468072],'cal/(mol*K)','+|-',[0.322295,0.370412,0.378652,0.373097,0.323525,0.279038,0.227409]),
        H298 = (3.36394,'kcal/mol','+|-',1.14895),
        S298 = (1.47743,'cal/(mol*K)','+|-',0.783081),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOBr_G4  |         7
CHOFBr_G4 |         1
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
        Cpdata = ([0.0473653,0.373771,0.469393,0.502914,0.486225,0.452641,0.477837],'cal/(mol*K)','+|-',[0.162931,0.187256,0.191421,0.188613,0.163553,0.141063,0.114963]),
        H298 = (4.68074,'kcal/mol','+|-',0.580835),
        S298 = (1.5466,'cal/(mol*K)','+|-',0.395874),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         3
CHOFClBr_G4 |         6
CHOFBr_G4   |         21
CHOClBr_G4  |         6
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
        Cpdata = ([-0.333743,-0.0133789,0.172704,0.254693,0.327201,0.376529,0.492609],'cal/(mol*K)','+|-',[0.241749,0.277841,0.284022,0.279855,0.242672,0.209302,0.170577]),
        H298 = (3.7534,'kcal/mol','+|-',0.861815),
        S298 = (0.760007,'cal/(mol*K)','+|-',0.587379),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         19
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
        Cpdata = ([-0.143786,-0.0464458,-0.0301482,-0.0290795,0.0102118,0.0731887,0.186089],'cal/(mol*K)','+|-',[0.238665,0.274297,0.280399,0.276285,0.239576,0.206633,0.168401]),
        H298 = (6.2676,'kcal/mol','+|-',0.850821),
        S298 = (1.75859,'cal/(mol*K)','+|-',0.579886),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         19
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
        Cpdata = ([0.0440436,0.466065,0.580598,0.605073,0.553519,0.469747,0.238252],'cal/(mol*K)','+|-',[0.614621,0.706382,0.722095,0.711501,0.616967,0.532129,0.433673]),
        H298 = (3.94376,'kcal/mol','+|-',2.19107),
        S298 = (1.81077,'cal/(mol*K)','+|-',1.49335),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOBr_G4  |         1
CHOFBr_G4 |         1
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
        Cpdata = ([-0.287996,-0.400491,-0.353923,-0.331456,-0.281032,-0.201107,0.0592729],'cal/(mol*K)','+|-',[0.0499708,0.0574313,0.0587089,0.0578475,0.0501616,0.043264,0.0352592]),
        H298 = (1.88891,'kcal/mol','+|-',0.178142),
        S298 = (1.11734,'cal/(mol*K)','+|-',0.121414),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         12
CHOFClBr_G4 |         18
CHOFBr_G4   |         54
CHOClBr_G4  |         18
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
        Cpdata = ([-0.504428,-0.552738,-0.463401,-0.415572,-0.331486,-0.179609,0.259167],'cal/(mol*K)','+|-',[0.0679688,0.0781163,0.079854,0.0786824,0.0682283,0.0588463,0.0479584]),
        H298 = (3.08883,'kcal/mol','+|-',0.242303),
        S298 = (0.151144,'cal/(mol*K)','+|-',0.165144),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         55
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
        Cpdata = ([-0.293681,-0.334611,-0.249395,-0.210793,-0.189,-0.125573,0.129855],'cal/(mol*K)','+|-',[0.0631259,0.0725503,0.0741642,0.0730762,0.0633669,0.0546534,0.0445413]),
        H298 = (3.74925,'kcal/mol','+|-',0.225038),
        S298 = (1.0306,'cal/(mol*K)','+|-',0.153377),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         56
CHOFBr_G4 |         2
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
        Cpdata = ([-0.528564,-0.604058,-0.532782,-0.484116,-0.397119,-0.309744,-0.101087],'cal/(mol*K)','+|-',[0.165289,0.189966,0.194192,0.191343,0.16592,0.143104,0.116627]),
        H298 = (1.48754,'kcal/mol','+|-',0.58924),
        S298 = (0.529359,'cal/(mol*K)','+|-',0.401603),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOBr_G4  |         6
CHOFBr_G4 |         1
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
        Cpdata = ([-0.405196,-0.351636,-0.24263,-0.206045,-0.159053,-0.0808746,0.215826],'cal/(mol*K)','+|-',[0.055396,0.0636665,0.0650827,0.0641279,0.0556075,0.047961,0.0390872]),
        H298 = (2.3345,'kcal/mol','+|-',0.197482),
        S298 = (1.69175,'cal/(mol*K)','+|-',0.134596),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         77
CHOFClBr_G4 |         57
CHOFBr_G4   |         172
CHOClBr_G4  |         88
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
        Cpdata = ([-0.715291,-0.645127,-0.434825,-0.333433,-0.221158,-0.035405,0.469835],'cal/(mol*K)','+|-',[0.0835745,0.0960519,0.0981886,0.0967481,0.0838936,0.0723575,0.0589698]),
        H298 = (3.56967,'kcal/mol','+|-',0.297936),
        S298 = (0.8342,'cal/(mol*K)','+|-',0.203061),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         123
CHOFCl_G4  |         2
CHOClBr_G4 |         4
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
        Cpdata = ([-0.295076,-0.152037,0.0132143,0.0659162,0.0716455,0.123005,0.327998],'cal/(mol*K)','+|-',[0.0771622,0.0886823,0.090655,0.089325,0.0774568,0.0668058,0.0544453]),
        H298 = (4.6743,'kcal/mol','+|-',0.275077),
        S298 = (1.61147,'cal/(mol*K)','+|-',0.187481),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         126
CHOFCl_G4 |         4
CHOFBr_G4 |         31
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
        Cpdata = ([-0.533259,-0.489383,-0.315142,-0.21834,-0.131172,-0.0481284,0.187158],'cal/(mol*K)','+|-',[0.109197,0.125499,0.128291,0.126409,0.109614,0.0945408,0.0770486]),
        H298 = (2.39313,'kcal/mol','+|-',0.389277),
        S298 = (0.774199,'cal/(mol*K)','+|-',0.265316),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         50
CHOFBr_G4  |         24
CHOClBr_G4 |         6
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
        Cpdata = ([-0.511483,-0.332273,-0.19635,-0.126282,-0.0451817,0.0556001,0.404346],'cal/(mol*K)','+|-',[0.105921,0.121735,0.124443,0.122617,0.106326,0.0917051,0.0747376]),
        H298 = (3.57833,'kcal/mol','+|-',0.377601),
        S298 = (1.83172,'cal/(mol*K)','+|-',0.257358),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         18
CHOFClBr_G4 |         21
CHOFBr_G4   |         41
CHOClBr_G4  |         25
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
        Cpdata = ([-0.357494,-0.0502204,0.173519,0.285409,0.374694,0.435673,0.733549],'cal/(mol*K)','+|-',[0.164429,0.188978,0.193181,0.190347,0.165057,0.14236,0.11602]),
        H298 = (2.93915,'kcal/mol','+|-',0.586175),
        S298 = (0.37319,'cal/(mol*K)','+|-',0.399514),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         37
CHOFCl_G4  |         1
CHOClBr_G4 |         3
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
        Cpdata = ([-0.00832893,0.0830613,0.0886107,0.0715734,0.0730917,0.104164,0.38665],'cal/(mol*K)','+|-',[0.158563,0.182236,0.18629,0.183557,0.159169,0.137282,0.111882]),
        H298 = (3.9659,'kcal/mol','+|-',0.565266),
        S298 = (1.36426,'cal/(mol*K)','+|-',0.385263),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         37
CHOFBr_G4 |         6
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
        Cpdata = ([-0.374639,-0.200608,-0.0350328,0.0673066,0.188527,0.21298,0.282395],'cal/(mol*K)','+|-',[0.212412,0.244124,0.249555,0.245894,0.213223,0.183903,0.149877]),
        H298 = (1.7071,'kcal/mol','+|-',0.757231),
        S298 = (1.73968,'cal/(mol*K)','+|-',0.516098),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         10
CHOFBr_G4  |         8
CHOClBr_G4 |         2
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
        Cpdata = ([-0.145298,-0.119167,-0.0859063,-0.0789092,-0.0736843,-0.0466396,0.0579328],'cal/(mol*K)','+|-',[0.0367635,0.0422522,0.0431921,0.0425584,0.0369039,0.0318293,0.0259401]),
        H298 = (1.211,'kcal/mol','+|-',0.131059),
        S298 = (1.08994,'cal/(mol*K)','+|-',0.0893245),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         51
CHOFClBr_G4 |         28
CHOFBr_G4   |         82
CHOClBr_G4  |         53
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
        Cpdata = ([-0.212013,-0.139086,-0.0392286,0.0215442,0.0690026,0.110935,0.206044],'cal/(mol*K)','+|-',[0.0486499,0.0559131,0.0571569,0.0563184,0.0488356,0.0421203,0.0343271]),
        H298 = (1.15744,'kcal/mol','+|-',0.173433),
        S298 = (0.660503,'cal/(mol*K)','+|-',0.118205),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         74
CHOFCl_G4  |         13
CHOClBr_G4 |         19
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
        Cpdata = ([-0.148682,-0.0760222,0.0144627,0.0592617,0.0805109,0.10537,0.176623],'cal/(mol*K)','+|-',[0.043691,0.0502139,0.0513309,0.0505778,0.0438578,0.037827,0.0308281]),
        H298 = (1.71275,'kcal/mol','+|-',0.155755),
        S298 = (0.707187,'cal/(mol*K)','+|-',0.106156),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         77
CHOFCl_G4   |         18
CHOFClBr_G4 |         1
CHOFBr_G4   |         46
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
        Cpdata = ([-0.241659,-0.152083,-0.0407121,0.0220502,0.0720941,0.108305,0.194193],'cal/(mol*K)','+|-',[0.0497753,0.0572066,0.0584791,0.0576212,0.0499653,0.0430947,0.0351212]),
        H298 = (0.907176,'kcal/mol','+|-',0.177445),
        S298 = (0.311152,'cal/(mol*K)','+|-',0.120939),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         49
CHOFClBr_G4 |         1
CHOFBr_G4   |         37
CHOClBr_G4  |         13
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
        Cpdata = ([-0.487245,-0.366436,-0.26625,-0.211496,-0.0949754,-0.000924551,0.319447],'cal/(mol*K)','+|-',[0.112622,0.129436,0.132315,0.130374,0.113052,0.0975059,0.0794652]),
        H298 = (2.0618,'kcal/mol','+|-',0.401486),
        S298 = (2.25071,'cal/(mol*K)','+|-',0.273637),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         21
CHOFClBr_G4 |         16
CHOFBr_G4   |         31
CHOClBr_G4  |         22
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
        Cpdata = ([-0.370477,-0.128165,0.0193874,0.0781517,0.147875,0.195604,0.451944],'cal/(mol*K)','+|-',[0.148659,0.170854,0.174654,0.172092,0.149227,0.128707,0.104893]),
        H298 = (1.80547,'kcal/mol','+|-',0.529958),
        S298 = (1.18089,'cal/(mol*K)','+|-',0.361199),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         37
CHOFCl_G4  |         8
CHOClBr_G4 |         8
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
        Cpdata = ([-0.251678,-0.133366,-0.0656162,-0.0246591,0.0483949,0.101528,0.422424],'cal/(mol*K)','+|-',[0.140481,0.161454,0.165046,0.162624,0.141017,0.121626,0.0991226]),
        H298 = (2.40802,'kcal/mol','+|-',0.500803),
        S298 = (1.49949,'cal/(mol*K)','+|-',0.341327),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         37
CHOFCl_G4   |         6
CHOFClBr_G4 |         1
CHOFBr_G4   |         16
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
        Cpdata = ([-0.452812,-0.282992,-0.116251,-0.0195095,0.116198,0.185973,0.374584],'cal/(mol*K)','+|-',[0.143709,0.165164,0.168838,0.166361,0.144257,0.124421,0.1014]),
        H298 = (1.40742,'kcal/mol','+|-',0.51231),
        S298 = (1.55969,'cal/(mol*K)','+|-',0.34917),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         24
CHOFClBr_G4 |         1
CHOFBr_G4   |         20
CHOClBr_G4  |         8
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
        Cpdata = ([-0.112012,0.0156248,0.139183,0.111374,0.0182027,-0.022415,0.149256],'cal/(mol*K)','+|-',[0.129797,0.149176,0.152494,0.150257,0.130293,0.112376,0.0915843]),
        H298 = (0.238344,'kcal/mol','+|-',0.462717),
        S298 = (-0.323271,'cal/(mol*K)','+|-',0.315369),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         3
CHOFClBr_G4 |         6
CHOFBr_G4   |         6
CHOClBr_G4  |         5
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
        Cpdata = ([-0.143088,-0.103202,0.0161273,-0.00344062,-0.0986116,-0.130257,0.110146],'cal/(mol*K)','+|-',[0.199567,0.229361,0.234463,0.231023,0.200328,0.172782,0.140813]),
        H298 = (0.0446388,'kcal/mol','+|-',0.711438),
        S298 = (-0.247106,'cal/(mol*K)','+|-',0.484888),
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
        Cpdata = ([-0.0595707,-0.0266998,0.078211,0.0517162,-0.0393958,-0.0704584,0.121822],'cal/(mol*K)','+|-',[0.181395,0.208477,0.213114,0.209988,0.182088,0.157049,0.127991]),
        H298 = (0.675509,'kcal/mol','+|-',0.646659),
        S298 = (-0.234891,'cal/(mol*K)','+|-',0.440737),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         6
CHOFCl_G4   |         1
CHOFClBr_G4 |         1
CHOFBr_G4   |         4
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
        Cpdata = ([-0.158306,-0.131038,0.00641817,0.0123105,-0.0231756,-0.0296819,0.16498],'cal/(mol*K)','+|-',[0.194245,0.223245,0.228211,0.224863,0.194987,0.168174,0.137058]),
        H298 = (-0.0544731,'kcal/mol','+|-',0.692468),
        S298 = (-0.698698,'cal/(mol*K)','+|-',0.471958),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         2
CHOFClBr_G4 |         1
CHOFBr_G4   |         4
CHOClBr_G4  |         3
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
        Cpdata = ([0.192955,0.160487,0.102905,0.0777284,0.0301348,0.000628364,-0.0942518],'cal/(mol*K)','+|-',[0.0503904,0.0579135,0.0592018,0.0583333,0.0505828,0.0436272,0.0355552]),
        H298 = (1.72557,'kcal/mol','+|-',0.179638),
        S298 = (0.0587532,'cal/(mol*K)','+|-',0.122434),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         35
CHOFClBr_G4 |         23
CHOFBr_G4   |         50
CHOClBr_G4  |         36
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
        Cpdata = ([0.275328,0.248766,0.186314,0.14346,0.0567248,0.00969829,-0.0904599],'cal/(mol*K)','+|-',[0.0687218,0.0789817,0.0807387,0.0795542,0.0689842,0.0594983,0.0484898]),
        H298 = (1.36086,'kcal/mol','+|-',0.244988),
        S298 = (-0.0401011,'cal/(mol*K)','+|-',0.166974),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         61
CHOFCl_G4  |         5
CHOClBr_G4 |         16
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
        Cpdata = ([0.143061,0.084595,0.0485554,0.0373149,0.0157509,0.00236969,-0.0605414],'cal/(mol*K)','+|-',[0.0584833,0.0672147,0.0687098,0.0677018,0.0587066,0.0506339,0.0412655]),
        H298 = (3.00962,'kcal/mol','+|-',0.208488),
        S298 = (0.220095,'cal/(mol*K)','+|-',0.142097),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         61
CHOFCl_G4   |         14
CHOFClBr_G4 |         1
CHOFBr_G4   |         38
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
        Cpdata = ([0.191068,0.135447,0.086284,0.0841781,0.0456014,0.0200424,-0.0716922],'cal/(mol*K)','+|-',[0.0792966,0.0911353,0.0931626,0.0917958,0.0795993,0.0686537,0.0559512]),
        H298 = (1.36026,'kcal/mol','+|-',0.282686),
        S298 = (-0.219487,'cal/(mol*K)','+|-',0.192667),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         36
CHOFClBr_G4 |         1
CHOFBr_G4   |         16
CHOClBr_G4  |         7
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
        Cpdata = ([0.673678,0.59465,0.424297,0.347296,0.147457,0.0428923,-0.140663],'cal/(mol*K)','+|-',[0.0986813,0.113414,0.115937,0.114236,0.099058,0.0854367,0.069629]),
        H298 = (4.13515,'kcal/mol','+|-',0.35179),
        S298 = (0.0907781,'cal/(mol*K)','+|-',0.239766),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         26
CHOFClBr_G4 |         24
CHOFBr_G4   |         54
CHOClBr_G4  |         32
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
        Cpdata = ([0.808793,0.68909,0.477174,0.340111,0.058019,-0.0518429,-0.180425],'cal/(mol*K)','+|-',[0.169115,0.194364,0.198687,0.195772,0.169761,0.146418,0.119327]),
        H298 = (4.48625,'kcal/mol','+|-',0.602883),
        S298 = (-0.0854678,'cal/(mol*K)','+|-',0.410901),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         41
CHOClBr_G4 |         3
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
        Cpdata = ([0.625181,0.428351,0.277535,0.202859,0.0484449,-0.0283805,-0.182571],'cal/(mol*K)','+|-',[0.147287,0.169276,0.173042,0.170503,0.147849,0.127519,0.103925]),
        H298 = (9.53999,'kcal/mol','+|-',0.525066),
        S298 = (0.805085,'cal/(mol*K)','+|-',0.357864),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         41
CHOFCl_G4 |         2
CHOFBr_G4 |         12
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
        Cpdata = ([0.931498,0.846831,0.626012,0.543721,0.243418,0.0913837,-0.0829819],'cal/(mol*K)','+|-',[0.226402,0.260203,0.265991,0.262089,0.227266,0.196015,0.159748]),
        H298 = (3.28324,'kcal/mol','+|-',0.807104),
        S298 = (-0.702183,'cal/(mol*K)','+|-',0.55009),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         18
CHOFBr_G4  |         3
CHOClBr_G4 |         1
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
        Cpdata = ([0.366857,0.381128,0.254896,0.214348,0.047758,-0.0649548,-0.228799],'cal/(mol*K)','+|-',[0.129014,0.148275,0.151574,0.14935,0.129506,0.111698,0.0910315]),
        H298 = (2.69645,'kcal/mol','+|-',0.459924),
        S298 = (0.209895,'cal/(mol*K)','+|-',0.313466),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         3
CHOFClBr_G4 |         3
CHOFBr_G4   |         3
CHOClBr_G4  |         3
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
        Cpdata = ([0.481327,0.388344,0.196757,0.1248,-0.0466783,-0.169316,-0.413763],'cal/(mol*K)','+|-',[0.42547,0.488991,0.499868,0.492535,0.427094,0.368365,0.300209]),
        H298 = (2.30214,'kcal/mol','+|-',1.51676),
        S298 = (-0.714443,'cal/(mol*K)','+|-',1.03377),
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
        Cpdata = ([0.139807,0.220789,0.119538,0.0837254,0.0120292,-0.0449158,-0.192433],'cal/(mol*K)','+|-',[0.421803,0.484776,0.49556,0.48829,0.423413,0.36519,0.297622]),
        H298 = (6.56934,'kcal/mol','+|-',1.50369),
        S298 = (-0.699783,'cal/(mol*K)','+|-',1.02486),
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
        Cpdata = ([0.479747,0.529404,0.381618,0.348283,0.122474,-0.0464348,-0.235161],'cal/(mol*K)','+|-',[0.431033,0.495385,0.506405,0.498975,0.432679,0.373182,0.304135]),
        H298 = (2.03071,'kcal/mol','+|-',1.5366),
        S298 = (-0.870439,'cal/(mol*K)','+|-',1.04728),
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
        Cpdata = ([-1.06386,-1.20862,-0.943059,-0.789355,-0.620847,-0.373784,0.753352],'cal/(mol*K)','+|-',[0.297638,0.342074,0.349684,0.344554,0.298774,0.25769,0.210012]),
        H298 = (1.12112,'kcal/mol','+|-',1.06106),
        S298 = (-0.692179,'cal/(mol*K)','+|-',0.723173),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         6
CHOFCl_G4 |         2
CHOFBr_G4 |         3
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
        Cpdata = ([-0.422772,-0.744553,-0.613767,-0.56569,-0.556662,-0.380805,0.784709],'cal/(mol*K)','+|-',[0.283472,0.325794,0.333041,0.328155,0.284554,0.245426,0.200017]),
        H298 = (1.50026,'kcal/mol','+|-',1.01055),
        S298 = (-0.468017,'cal/(mol*K)','+|-',0.688754),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         6
CHOFCl_G4   |         4
CHOFClBr_G4 |         1
CHOClBr_G4  |         2
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
        Cpdata = ([-0.20967,-0.406407,-0.293647,-0.27708,-0.33155,-0.20493,0.914061],'cal/(mol*K)','+|-',[0.259182,0.297877,0.304504,0.300036,0.260172,0.224396,0.182878]),
        H298 = (1.5797,'kcal/mol','+|-',0.923964),
        S298 = (-1.67374,'cal/(mol*K)','+|-',0.629737),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         5
CHOFClBr_G4 |         1
CHOFBr_G4   |         6
CHOClBr_G4  |         4
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
        Cpdata = ([0.953551,0.775975,0.542237,0.323105,-0.028744,-0.256398,-0.244508],'cal/(mol*K)','+|-',[0.149905,0.172285,0.176117,0.173534,0.150477,0.129785,0.105772]),
        H298 = (7.42177,'kcal/mol','+|-',0.534398),
        S298 = (1.27642,'cal/(mol*K)','+|-',0.364224),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         8
CHOFClBr_G4 |         6
CHOFBr_G4   |         14
CHOClBr_G4  |         8
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
        Cpdata = ([1.00173,0.803673,0.610895,0.405257,0.098006,-0.0583939,-0.0230311],'cal/(mol*K)','+|-',[0.12325,0.141651,0.144802,0.142677,0.123721,0.106708,0.0869646]),
        H298 = (5.35662,'kcal/mol','+|-',0.439376),
        S298 = (0.478493,'cal/(mol*K)','+|-',0.299461),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         13
CHOFClBr_G4 |         8
CHOFBr_G4   |         18
CHOClBr_G4  |         12
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
        Cpdata = ([0.553053,0.359619,0.23948,0.102061,-0.0455756,-0.126411,0.0661729],'cal/(mol*K)','+|-',[0.155178,0.178345,0.182313,0.179638,0.15577,0.134351,0.109493]),
        H298 = (5.69302,'kcal/mol','+|-',0.553196),
        S298 = (0.255621,'cal/(mol*K)','+|-',0.377037),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         19
CHOFCl_G4 |         5
CHOFBr_G4 |         9
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
        Cpdata = ([1.03875,0.946333,0.783166,0.574621,0.293886,0.112986,0.159695],'cal/(mol*K)','+|-',[0.166226,0.191043,0.195292,0.192427,0.16686,0.143916,0.117288]),
        H298 = (3.32449,'kcal/mol','+|-',0.592581),
        S298 = (-1.03523,'cal/(mol*K)','+|-',0.403879),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         20
CHOFCl_G4  |         3
CHOClBr_G4 |         5
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
        Cpdata = ([0.72324,0.70693,0.609928,0.457264,0.256316,0.115386,0.119257],'cal/(mol*K)','+|-',[0.183887,0.211341,0.216042,0.212873,0.184589,0.159207,0.12975]),
        H298 = (3.28059,'kcal/mol','+|-',0.655543),
        S298 = (-0.42528,'cal/(mol*K)','+|-',0.446792),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOBr_G4   |         12
CHOFBr_G4  |         9
CHOClBr_G4 |         3
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
        Cpdata = ([0.766257,0.642872,0.526694,0.407388,0.264391,0.129391,0.199383],'cal/(mol*K)','+|-',[0.136628,0.157026,0.160519,0.158164,0.13715,0.118291,0.0964042]),
        H298 = (2.88294,'kcal/mol','+|-',0.487068),
        S298 = (-0.429316,'cal/(mol*K)','+|-',0.331966),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         20
CHOFCl_G4   |         9
CHOFClBr_G4 |         1
CHOFBr_G4   |         13
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
        Cpdata = ([0.907799,0.657924,0.459162,0.259969,0.0188469,-0.137679,-0.0584824],'cal/(mol*K)','+|-',[0.141429,0.162544,0.16616,0.163722,0.141969,0.122447,0.0997915]),
        H298 = (2.82528,'kcal/mol','+|-',0.504182),
        S298 = (0.119868,'cal/(mol*K)','+|-',0.343631),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         20
CHOFCl_G4   |         9
CHOFClBr_G4 |         2
CHOClBr_G4  |         9
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
        Cpdata = ([0.623537,0.409917,0.257852,0.105523,-0.0121102,-0.0816768,0.0108625],'cal/(mol*K)','+|-',[0.136631,0.15703,0.160523,0.158168,0.137153,0.118293,0.0964061]),
        H298 = (2.4411,'kcal/mol','+|-',0.487078),
        S298 = (-0.19929,'cal/(mol*K)','+|-',0.331973),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         16
CHOFClBr_G4 |         2
CHOFBr_G4   |         17
CHOClBr_G4  |         9
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
        Cpdata = ([0.0670598,0.0484804,0.0276092,0.140954,0.356983,0.353706,0.503953],'cal/(mol*K)','+|-',[0.124716,0.143335,0.146524,0.144374,0.125192,0.107977,0.0879988]),
        H298 = (0.345464,'kcal/mol','+|-',0.444602),
        S298 = (-1.2655,'cal/(mol*K)','+|-',0.303023),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         10
CHOFClBr_G4 |         8
CHOFBr_G4   |         24
CHOClBr_G4  |         12
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
        Cpdata = ([0.298108,0.432618,0.341545,0.365618,0.427909,0.349086,0.201933],'cal/(mol*K)','+|-',[0.170385,0.195823,0.200179,0.197242,0.171035,0.147517,0.120223]),
        H298 = (2.90335,'kcal/mol','+|-',0.607408),
        S298 = (-0.832571,'cal/(mol*K)','+|-',0.413985),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         19
CHOFCl_G4 |         1
CHOFBr_G4 |         6
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
        Cpdata = ([-0.216391,-0.0684263,0.0158986,0.110809,0.248751,0.277267,0.388703],'cal/(mol*K)','+|-',[0.188979,0.217193,0.222024,0.218767,0.1897,0.163615,0.133343]),
        H298 = (1.09963,'kcal/mol','+|-',0.673694),
        S298 = (-0.532953,'cal/(mol*K)','+|-',0.459163),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         19
CHOClBr_G4 |         1
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
        Cpdata = ([-0.112183,-0.111612,-0.130547,-0.107409,0.00609917,0.0755697,0.431962],'cal/(mol*K)','+|-',[0.280107,0.321926,0.329087,0.324259,0.281176,0.242512,0.197642]),
        H298 = (1.4366,'kcal/mol','+|-',0.998558),
        S298 = (-1.22448,'cal/(mol*K)','+|-',0.680577),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOBr_G4  |         10
CHOFBr_G4 |         1
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
        Cpdata = ([0.42524,0.0449695,-0.0076727,0.164389,0.288088,0.420841,0.797181],'cal/(mol*K)','+|-',[0.214423,0.246435,0.251917,0.248221,0.215241,0.185644,0.151296]),
        H298 = (7.07575,'kcal/mol','+|-',0.764399),
        S298 = (0.378738,'cal/(mol*K)','+|-',0.520984),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         2
CHOFClBr_G4 |         4
CHOFBr_G4   |         6
CHOClBr_G4  |         4
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
        Cpdata = ([0.434852,0.304563,0.258223,0.298993,0.188632,0.134846,0.239834],'cal/(mol*K)','+|-',[0.339946,0.390699,0.39939,0.39353,0.341244,0.29432,0.239864]),
        H298 = (5.41042,'kcal/mol','+|-',1.21188),
        S298 = (0.422543,'cal/(mol*K)','+|-',0.825968),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         6
CHOFBr_G4 |         1
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
        Cpdata = ([0.281472,0.226703,0.308853,0.405078,0.369993,0.35266,0.465835],'cal/(mol*K)','+|-',[0.342844,0.39403,0.402795,0.396886,0.344153,0.296829,0.241909]),
        H298 = (2.92725,'kcal/mol','+|-',1.22221),
        S298 = (-1.01438,'cal/(mol*K)','+|-',0.833011),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         6
CHOClBr_G4 |         1
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
        Cpdata = ([0.269679,-0.339568,-0.437638,-0.371549,-0.316557,-0.150457,0.25956],'cal/(mol*K)','+|-',[0.609982,0.70105,0.716645,0.706131,0.612311,0.528113,0.4304]),
        H298 = (6.86856,'kcal/mol','+|-',2.17453),
        S298 = (0.944778,'cal/(mol*K)','+|-',1.48208),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOBr_G4  |         1
CHOFBr_G4 |         1
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
        Cpdata = ([-0.241633,-0.997631,-1.22081,-1.04804,-0.705697,-0.387207,-0.230067],'cal/(mol*K)','+|-',[0.141218,0.162301,0.165912,0.163478,0.141757,0.122264,0.0996426]),
        H298 = (5.4645,'kcal/mol','+|-',0.50343),
        S298 = (1.47032,'cal/(mol*K)','+|-',0.343118),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         11
CHOFClBr_G4 |         6
CHOFBr_G4   |         15
CHOClBr_G4  |         11
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
        Cpdata = ([-0.243726,-0.892465,-1.00432,-0.809524,-0.465755,-0.153704,-0.0076276],'cal/(mol*K)','+|-',[0.157399,0.180898,0.184922,0.182209,0.158,0.136274,0.11106]),
        H298 = (8.49439,'kcal/mol','+|-',0.561115),
        S298 = (1.84388,'cal/(mol*K)','+|-',0.382434),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         18
CHOFCl_G4 |         6
CHOFBr_G4 |         14
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
        Cpdata = ([-0.105823,-0.766456,-0.977777,-0.85146,-0.597257,-0.327485,-0.276673],'cal/(mol*K)','+|-',[0.193567,0.222465,0.227414,0.224078,0.194306,0.167587,0.13658]),
        H298 = (5.42706,'kcal/mol','+|-',0.690049),
        S298 = (1.79238,'cal/(mol*K)','+|-',0.47031),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library    | Number of Species
CHOCl_G4   |         19
CHOClBr_G4 |         6
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
        Cpdata = ([-0.239894,-0.712398,-0.893193,-0.690186,-0.406385,-0.16506,-0.163833],'cal/(mol*K)','+|-',[0.252131,0.289774,0.29622,0.291874,0.253094,0.218291,0.177903]),
        H298 = (4.18013,'kcal/mol','+|-',0.898828),
        S298 = (0.317992,'cal/(mol*K)','+|-',0.612605),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         14
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
        Cpdata = ([-0.380226,-0.90248,-0.976221,-0.797113,-0.449641,-0.181964,-0.152742],'cal/(mol*K)','+|-',[0.106372,0.122253,0.124973,0.123139,0.106778,0.0920953,0.0750556]),
        H298 = (6.39782,'kcal/mol','+|-',0.379208),
        S298 = (1.32798,'cal/(mol*K)','+|-',0.258453),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOF_G4     |         30
CHOFCl_G4   |         19
CHOFClBr_G4 |         4
CHOFBr_G4   |         29
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
        Cpdata = ([-0.514656,-1.01793,-1.0856,-0.88761,-0.466709,-0.160292,-0.152415],'cal/(mol*K)','+|-',[0.123009,0.141374,0.144519,0.142398,0.123478,0.106499,0.0867944]),
        H298 = (4.85599,'kcal/mol','+|-',0.438516),
        S298 = (1.34987,'cal/(mol*K)','+|-',0.298875),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOCl_G4    |         30
CHOFCl_G4   |         7
CHOFClBr_G4 |         3
CHOClBr_G4  |         19
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
        Cpdata = ([-0.734756,-1.3408,-1.43206,-1.19224,-0.627405,-0.225675,-0.182377],'cal/(mol*K)','+|-',[0.138319,0.15897,0.162506,0.160122,0.138847,0.119755,0.0975974]),
        H298 = (5.01034,'kcal/mol','+|-',0.493097),
        S298 = (1.41174,'cal/(mol*K)','+|-',0.336075),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOBr_G4    |         26
CHOFClBr_G4 |         1
CHOFBr_G4   |         12
CHOClBr_G4  |         7
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
        Cpdata = ([-0.0613148,0.014087,0.137551,0.213407,0.248535,0.276004,0.330381],'cal/(mol*K)','+|-',[0.0890383,0.102331,0.104608,0.103073,0.0893782,0.0770879,0.0628249]),
        H298 = (1.96277,'kcal/mol','+|-',0.317414),
        S298 = (-0.694615,'cal/(mol*K)','+|-',0.216337),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         14
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
        Cpdata = ([0.429706,0.325512,0.262386,0.223978,0.159683,0.128005,0.103564],'cal/(mol*K)','+|-',[0.0912424,0.104865,0.107197,0.105625,0.0915907,0.0789962,0.0643802]),
        H298 = (5.36116,'kcal/mol','+|-',0.325272),
        S298 = (-0.831813,'cal/(mol*K)','+|-',0.221692),
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
        Cpdata = ([-0.124569,-0.0414804,0.137115,0.18829,0.127109,0.148913,0.223763],'cal/(mol*K)','+|-',[0.146487,0.168357,0.172102,0.169577,0.147046,0.126826,0.103361]),
        H298 = (2.86687,'kcal/mol','+|-',0.522214),
        S298 = (-0.0461551,'cal/(mol*K)','+|-',0.355921),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         26
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
        Cpdata = ([0.211057,-0.0849622,-0.261928,-0.331928,-0.359998,-0.293467,-0.0908236],'cal/(mol*K)','+|-',[0.148192,0.170317,0.174106,0.171551,0.148758,0.128303,0.104564]),
        H298 = (6.29532,'kcal/mol','+|-',0.528293),
        S298 = (-0.542737,'cal/(mol*K)','+|-',0.360064),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         26
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
        Cpdata = ([-0.432377,-0.382519,-0.280526,-0.140557,0.0752877,0.282769,0.68794],'cal/(mol*K)','+|-',[0.158593,0.182271,0.186325,0.183592,0.159199,0.137307,0.111903]),
        H298 = (2.57853,'kcal/mol','+|-',0.565371),
        S298 = (0.805811,'cal/(mol*K)','+|-',0.385335),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFClBr_G4 |         9
CHOFBr_G4   |         15
CHOClBr_G4  |         9
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
        Cpdata = ([-0.602376,-0.448942,-0.211492,-0.0750071,-0.00521891,0.0217937,0.151667],'cal/(mol*K)','+|-',[0.188239,0.216342,0.221155,0.21791,0.188957,0.162974,0.13282]),
        H298 = (1.33119,'kcal/mol','+|-',0.671056),
        S298 = (0.806138,'cal/(mol*K)','+|-',0.457365),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         24
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
        Cpdata = ([0.0789661,-0.00826368,-0.031511,-0.047384,-0.02161,0.0392074,0.200236],'cal/(mol*K)','+|-',[0.190162,0.218553,0.223415,0.220137,0.190888,0.16464,0.134178]),
        H298 = (2.70883,'kcal/mol','+|-',0.677913),
        S298 = (0.0802435,'cal/(mol*K)','+|-',0.462038),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         24
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
        Cpdata = ([-0.11987,0.154996,0.179495,0.136543,-0.0362734,-0.102538,-0.023355],'cal/(mol*K)','+|-',[0.429404,0.493513,0.504491,0.49709,0.431044,0.371771,0.302985]),
        H298 = (2.51094,'kcal/mol','+|-',1.53079),
        S298 = (1.71964,'cal/(mol*K)','+|-',1.04333),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOFBr_G4 |         4
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
        Cpdata = ([-0.774085,-0.642314,-0.412453,-0.260714,-0.21398,-0.217231,-0.0639702],'cal/(mol*K)','+|-',[0.280037,0.321846,0.329005,0.324178,0.281106,0.242452,0.197593]),
        H298 = (1.96179,'kcal/mol','+|-',0.998309),
        S298 = (-0.52294,'cal/(mol*K)','+|-',0.680408),
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
        Cpdata = ([0.245379,0.333856,0.340188,0.362121,0.345499,0.354879,0.459335],'cal/(mol*K)','+|-',[0.283918,0.326306,0.333565,0.328671,0.285002,0.245812,0.200331]),
        H298 = (7.38508,'kcal/mol','+|-',1.01215),
        S298 = (-1.56652,'cal/(mol*K)','+|-',0.689838),
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
        Cpdata = ([1.28858,1.60873,1.59757,1.44213,0.990463,0.627,0.204681],'cal/(mol*K)','+|-',[0.192574,0.221324,0.226247,0.222928,0.193309,0.166727,0.135879]),
        H298 = (2.34139,'kcal/mol','+|-',0.686509),
        S298 = (-0.572184,'cal/(mol*K)','+|-',0.467897),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library     | Number of Species
CHOFCl_G4   |         4
CHOFClBr_G4 |         2
CHOFBr_G4   |         10
CHOClBr_G4  |         4
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
        Cpdata = ([0.692902,0.748947,0.732154,0.654874,0.448645,0.294028,0.0858244],'cal/(mol*K)','+|-',[0.263555,0.302903,0.309641,0.305098,0.264561,0.228182,0.185963]),
        H298 = (1.68467,'kcal/mol','+|-',0.939551),
        S298 = (-0.143794,'cal/(mol*K)','+|-',0.640361),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library   | Number of Species
CHOF_G4   |         8
CHOFBr_G4 |         3
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
        Cpdata = ([0.815477,0.963953,0.996605,0.942743,0.729321,0.528441,0.248787],'cal/(mol*K)','+|-',[0.308984,0.355115,0.363014,0.357688,0.310164,0.267514,0.218018]),
        H298 = (1.52396,'kcal/mol','+|-',1.1015),
        S298 = (-0.764091,'cal/(mol*K)','+|-',0.750741),
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
        Cpdata = ([1.5681,1.85074,1.80473,1.61193,1.06923,0.615793,-0.054756],'cal/(mol*K)','+|-',[0.594067,0.682759,0.697947,0.687708,0.596335,0.514334,0.419171]),
        H298 = (3.76862,'kcal/mol','+|-',2.1178),
        S298 = (-1.1101,'cal/(mol*K)','+|-',1.44341),
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

