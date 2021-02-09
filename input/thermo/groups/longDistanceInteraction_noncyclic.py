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
from species in RMG thermo libraries (primarily from CHOF_G4, CHOCl_G4, CHOBr_G4 libraries).

August-7-2020
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
1 *1 [Cs,Cd,CO] u0 {2,[S,D]} {3,S}
2 *2 [Cs,Cd,CO] u0 {1,[S,D]}
3    Val7       u0 {1,S}
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
        Cpdata = ([-0.529742,-0.12119,0.168368,0.247349,0.339672,0.421187,0.864623],'J/(mol*K)'),
        H298 = (13.9272,'kJ/mol'),
        S298 = (3.43161,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by 2 to avoid overcounting
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
        Cpdata = ([0.947742,0.575457,0.326244,-0.152372,-0.873789,-0.954336,0.221784],'J/(mol*K)'),
        H298 = (19.5104,'kJ/mol'),
        S298 = (1.68293,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by 2 to avoid overcounting
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
        Cpdata = ([-0.438445,0.251019,1.11857,1.41726,1.13095,0.616262,0.242229],'J/(mol*K)'),
        H298 = (17.3505,'kJ/mol'),
        S298 = (0.65968,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-3.40168,-3.36022,-2.68659,-2.47415,-2.13689,-1.51586,1.08433],'J/(mol*K)'),
        H298 = (17.769,'kJ/mol'),
        S298 = (7.24989,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.265221,-1.32012,-1.4324,-1.45038,-1.16875,-0.665883,0.955672],'J/(mol*K)'),
        H298 = (27.8398,'kJ/mol'),
        S298 = (2.02036,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.824174,-1.73197,-1.35322,-1.04179,-0.783977,-0.314955,0.967663],'J/(mol*K)'),
        H298 = (42.536,'kJ/mol'),
        S298 = (6.1525,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-1.26137,-3.21586,-3.96479,-4.65219,-5.46937,-5.31927,-3.10366],'J/(mol*K)'),
        H298 = (24.7386,'kJ/mol'),
        S298 = (14.5448,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.384807,-0.8262,-0.65871,-0.58872,-0.483384,-0.202857,1.24703],'J/(mol*K)'),
        H298 = (8.60765,'kJ/mol'),
        S298 = (2.49831,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.13893,-0.281614,-0.504605,-0.482039,-0.349953,0.181301,1.23424],'J/(mol*K)'),
        H298 = (17.1014,'kJ/mol'),
        S298 = (-4.17377,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.266786,0.807114,1.35442,1.49779,1.34949,1.32902,1.66602],'J/(mol*K)'),
        H298 = (27.4753,'kJ/mol'),
        S298 = (-0.674738,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.0616075,-0.591998,-0.782394,-1.22607,-1.884,-1.75009,-0.0281582],'J/(mol*K)'),
        H298 = (10.5477,'kJ/mol'),
        S298 = (5.07066,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.398592,1.56377,1.76325,2.17722,1.98501,1.77419,1.85435],'J/(mol*K)'),
        H298 = (14.7231,'kJ/mol'),
        S298 = (2.72798,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-3.07202,-1.64294,-0.770345,0.117648,0.939375,1.44901,1.85659],'J/(mol*K)'),
        H298 = (9.59621,'kJ/mol'),
        S298 = (-0.79276,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.0390615,-0.232897,-0.462973,-0.159579,-0.0043318,0.210228,0.647601],'J/(mol*K)'),
        H298 = (26.1533,'kJ/mol'),
        S298 = (3.75973,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-4.25549,-2.01543,-0.574666,1.03972,2.03748,2.17648,1.81831],'J/(mol*K)'),
        H298 = (10.7201,'kJ/mol'),
        S298 = (-0.166157,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.800333,-1.4553,-1.35226,-1.2805,-1.00637,-0.638272,0.519775],'J/(mol*K)'),
        H298 = (8.38918,'kJ/mol'),
        S298 = (3.26507,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by 2 to avoid overcounting
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
        Cpdata = ([-1.42558,-1.69189,-1.23361,-0.905715,-0.401635,0.226004,2.10269],'J/(mol*K)'),
        H298 = (9.90194,'kJ/mol'),
        S298 = (0.930705,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by 2 to avoid overcounting
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
        Cpdata = ([-1.22739,-1.5133,-1.11989,-0.815503,-0.538434,-0.20086,0.716195],'J/(mol*K)'),
        H298 = (17.7733,'kJ/mol'),
        S298 = (2.78099,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-1.79588,-2.57965,-2.59911,-2.58817,-2.33286,-1.90765,-0.778093],'J/(mol*K)'),
        H298 = (8.05588,'kJ/mol'),
        S298 = (5.52935,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.368941,-0.419035,-0.0729775,0.0957825,0.281575,0.598207,1.64502],'J/(mol*K)'),
        H298 = (9.58639,'kJ/mol'),
        S298 = (-0.223748,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.74105,-0.880659,-0.143275,0.312666,0.745187,1.38352,3.24172],'J/(mol*K)'),
        H298 = (11.2199,'kJ/mol'),
        S298 = (-3.10015,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-1.00177,-0.380523,0.45733,0.938707,1.13406,1.34574,1.99217],'J/(mol*K)'),
        H298 = (20.5556,'kJ/mol'),
        S298 = (0.715696,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.326439,-1.06733,-0.872835,-0.801797,-0.72407,-0.343688,1.12368],'J/(mol*K)'),
        H298 = (9.83905,'kJ/mol'),
        S298 = (-0.0597878,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-1.25113,-1.02792,-0.784512,-0.105912,0.231758,0.510921,1.85507],'J/(mol*K)'),
        H298 = (11.2978,'kJ/mol'),
        S298 = (2.61523,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-1.86898,-0.898645,0.0650487,1.13225,1.71848,1.96505,3.03735],'J/(mol*K)'),
        H298 = (5.46139,'kJ/mol'),
        S298 = (-3.05484,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.05642,1.00829,0.686562,0.882763,0.70789,0.672368,1.90496],'J/(mol*K)'),
        H298 = (17.1634,'kJ/mol'),
        S298 = (0.100189,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-3.11346,-2.95658,-2.06993,-0.573182,0.891629,1.54872,3.02214],'J/(mol*K)'),
        H298 = (1.13493,'kJ/mol'),
        S298 = (0.341285,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.125903,0.0889524,0.180822,0.226978,0.187136,0.27747,0.604756],'J/(mol*K)'),
        H298 = (4.06556,'kJ/mol'),
        S298 = (-0.856968,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([-0.0749744,-0.124025,0.123459,0.347939,0.537627,0.740233,0.919625],'J/(mol*K)'),
        H298 = (3.39857,'kJ/mol'),
        S298 = (-1.95746,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([-0.609838,-0.120636,0.385688,0.717245,0.892761,0.981489,1.20305],'J/(mol*K)'),
        H298 = (5.7115,'kJ/mol'),
        S298 = (-0.736743,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.298748,-0.232254,0.152791,0.385098,0.568146,0.754993,1.15422],'J/(mol*K)'),
        H298 = (2.62224,'kJ/mol'),
        S298 = (-1.19321,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-1.5211,-1.53099,-1.32798,-0.603647,-0.090436,0.314471,2.0413],'J/(mol*K)'),
        H298 = (5.74849,'kJ/mol'),
        S298 = (1.68318,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([-1.90043,-1.78628,-1.34908,-0.467974,0.253572,0.691766,2.22236],'J/(mol*K)'),
        H298 = (4.80444,'kJ/mol'),
        S298 = (-0.715677,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([-0.0692617,0.128163,0.0531473,0.469141,0.51094,0.574046,1.91523],'J/(mol*K)'),
        H298 = (10.1012,'kJ/mol'),
        S298 = (1.90144,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-2.95746,-2.90816,-2.21198,-1.00569,0.116269,0.800843,2.65696],'J/(mol*K)'),
        H298 = (2.14458,'kJ/mol'),
        S298 = (-0.735541,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.418707,2.39466,2.76676,3.3436,2.93721,2.43499,1.44959],'J/(mol*K)'),
        H298 = (1.40513,'kJ/mol'),
        S298 = (-3.80728,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([-0.532407,0.781297,1.19972,1.86957,1.6742,1.43464,1.00501],'J/(mol*K)'),
        H298 = (2.30632,'kJ/mol'),
        S298 = (-1.86683,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([0.133629,2.61882,3.34217,4.05961,3.86938,3.48073,2.32761],'J/(mol*K)'),
        H298 = (4.36178,'kJ/mol'),
        S298 = (-4.02036,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([0.848553,1.90457,1.83845,2.31766,1.76422,1.28937,0.885185],'J/(mol*K)'),
        H298 = (-0.177434,'kJ/mol'),
        S298 = (-3.68324,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.73662,2.05957,1.847,1.58065,0.862155,0.344604,-0.119108],'J/(mol*K)'),
        H298 = (2.02451,'kJ/mol'),
        S298 = (-1.66965,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid doublecounting
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
        Cpdata = ([1.84875,2.07254,1.78329,1.43733,0.651333,0.15848,-0.228229],'J/(mol*K)'),
        H298 = (0.883403,'kJ/mol'),
        S298 = (-1.09169,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid doublecounting
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
        Cpdata = ([1.3234,1.43009,1.16112,0.914916,0.332648,-0.0448858,-0.165288],'J/(mol*K)'),
        H298 = (9.15208,'kJ/mol'),
        S298 = (0.679686,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.56198,1.80563,1.72693,1.50582,0.80628,0.275192,-0.17243],'J/(mol*K)'),
        H298 = (-0.491826,'kJ/mol'),
        S298 = (-1.57959,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([3.28363,3.95243,3.56905,2.92526,1.51044,0.51336,-0.420545],'J/(mol*K)'),
        H298 = (6.5837,'kJ/mol'),
        S298 = (-6.27847,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([4.71016,5.1356,4.51864,3.57861,1.76361,0.683852,-0.0607263],'J/(mol*K)'),
        H298 = (5.64366,'kJ/mol'),
        S298 = (-4.86812,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([3.58591,3.81799,3.31886,2.62084,1.20098,0.255113,-0.368934],'J/(mol*K)'),
        H298 = (28.5269,'kJ/mol'),
        S298 = (0.314289,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([4.96417,5.29651,4.81575,4.12214,2.32288,1.05542,0.192316],'J/(mol*K)'),
        H298 = (1.69564,'kJ/mol'),
        S298 = (-7.40438,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.40459,2.07281,1.73727,1.38429,0.436811,-0.315872,-1.04913],'J/(mol*K)'),
        H298 = (4.32781,'kJ/mol'),
        S298 = (-2.21325,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([1.86891,2.60461,2.26753,1.74784,0.49946,-0.47273,-1.22624],'J/(mol*K)'),
        H298 = (5.47483,'kJ/mol'),
        S298 = (-0.82657,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""
Divided by two to avoid overcounting
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
        Cpdata = ([1.62966,2.82064,2.94908,2.69411,1.68979,0.750626,-0.336932],'J/(mol*K)'),
        H298 = (23.4831,'kJ/mol'),
        S298 = (0.536918,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.24901,2.75128,2.39637,2.0226,0.904266,-0.0892755,-0.862529],'J/(mol*K)'),
        H298 = (1.9332,'kJ/mol'),
        S298 = (-0.295765,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-3.45422,-2.05872,-0.748656,0.670592,1.09487,1.7769,5.38621],'J/(mol*K)'),
        H298 = (14.567,'kJ/mol'),
        S298 = (-6.57779,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-2.2942,-1.82275,-1.21894,-0.16045,-0.00764052,0.560942,3.66258],'J/(mol*K)'),
        H298 = (13.4626,'kJ/mol'),
        S298 = (-3.7952,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([-0.0558217,0.122408,0.161036,0.879168,0.513532,0.712393,3.78075],'J/(mol*K)'),
        H298 = (11.0867,'kJ/mol'),
        S298 = (-4.66996,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.4949,1.94487,1.2943,0.479628,-0.770068,-1.40769,-0.751726],'J/(mol*K)'),
        H298 = (26.6435,'kJ/mol'),
        S298 = (6.04694,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.96129,1.45881,1.15198,0.665466,-0.296221,-0.824115,-0.554834],'J/(mol*K)'),
        H298 = (44.8116,'kJ/mol'),
        S298 = (5.039,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.83487,1.27993,-0.0880021,-1.30071,-2.91192,-3.56698,-3.47775],'J/(mol*K)'),
        H298 = (34.4827,'kJ/mol'),
        S298 = (5.72238,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([4.36115,3.80596,2.37853,0.58909,-2.05155,-3.01838,-2.43301],'J/(mol*K)'),
        H298 = (21.0463,'kJ/mol'),
        S298 = (12.4088,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([3.41703,2.53591,1.88665,1.15944,0.22432,-0.161451,0.360997],'J/(mol*K)'),
        H298 = (21.7658,'kJ/mol'),
        S298 = (0.550887,'J/(mol*K)'),
    ),
    shortDesc = """Derived from chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.79873,1.52268,0.889428,0.197554,-0.370686,-0.638744,0.376926],'J/(mol*K)'),
        H298 = (25.5004,'kJ/mol'),
        S298 = (-2.9804,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([3.90501,3.54115,2.92691,2.14794,1.21308,0.57418,0.86693],'J/(mol*K)'),
        H298 = (11.039,'kJ/mol'),
        S298 = (-5.77323,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([1.8799,1.58349,1.18728,0.671541,0.141805,-0.173482,1.00635],'J/(mol*K)'),
        H298 = (7.89011,'kJ/mol'),
        S298 = (-3.44795,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.02754,1.83455,1.79212,1.52065,1.3104,0.985188,1.55713],'J/(mol*K)'),
        H298 = (14.3551,'kJ/mol'),
        S298 = (-1.1458,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Fluorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.82865,1.44161,0.833956,0.302595,-0.0498998,-0.359348,0.397952],'J/(mol*K)'),
        H298 = (9.67318,'kJ/mol'),
        S298 = (0.809872,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Chlorine species in thermo libraries""",
    longDesc = 
"""

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
        Cpdata = ([2.23266,1.36458,0.943371,0.376736,-0.139231,-0.439512,0.637492],'J/(mol*K)'),
        H298 = (8.57038,'kJ/mol'),
        S298 = (0.231177,'J/(mol*K)'),
    ),
    shortDesc = """Derived from Bromine species in thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "intRVal7",
    group = 
"""
1 *1 [Cs,Cd,CO] u0 {2,[S,D]} {4,S}
2    R!H        ux {1,[S,D]} {3,[S,D]}
3 *2 [Cs,Cd,CO] u0 {2,[S,D]}
4    [Cl,Br]    u0 {1,S}
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
    index = 74,
    label = "Cs(Cl/Br)3-R-Cs(Cl/Br)3",
    group = 
"""
1 *1 Cs      u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs      u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H     ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br] u0 {1,S}
5    [Cl,Br] u0 {2,S}
6    [Cl,Br] u0 {1,S}
7    [Cl,Br] u0 {2,S}
8    [Cl,Br] u0 {1,S}
9    [Cl,Br] u0 {2,S}
""",
    thermo = 'Cs(Cl)3-R-Cs(Cl)3',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "Cs(Cl)3-R-Cs(Cl)3",
    group = 
"""
1 *1 Cs  u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs  u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H ux {1,[S,D]} {2,[S,D]}
4    Cl  u0 {1,S}
5    Cl  u0 {2,S}
6    Cl  u0 {1,S}
7    Cl  u0 {2,S}
8    Cl  u0 {1,S}
9    Cl  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00364917,-0.168952,-0.293536,-0.402694,-0.457559,-0.234409,0.415146],'J/(mol*K)'),
        H298 = (34.7298,'kJ/mol'),
        S298 = (-3.68704,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "Cs(Br)3-R-Cs(Br)3",
    group = 
"""
1 *1 Cs  u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs  u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H ux {1,[S,D]} {2,[S,D]}
4    Br  u0 {1,S}
5    Br  u0 {2,S}
6    Br  u0 {1,S}
7    Br  u0 {2,S}
8    Br  u0 {1,S}
9    Br  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.940191,-1.05731,-0.520803,0.0464141,0.720499,1.16673,1.8637],'J/(mol*K)'),
        H298 = (63.0877,'kJ/mol'),
        S298 = (-8.5464,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "Cs(Cl/Br)3-R-Cs(Cl/Br)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {2,S}
6    [Cl,Br]     u0 {1,S}
7    [Cl,Br]     u0 {2,S}
8    [Cl,Br]     u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = 'Cs(Cl)3-R-Cs(Cl)2',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "Cs(Cl)3-R-Cs(Cl)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {2,S}
6    Cl          u0 {1,S}
7    Cl          u0 {2,S}
8    Cl          u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.52802,-1.94969,-2.55231,-3.07312,-3.44373,-2.82436,-0.42704],'J/(mol*K)'),
        H298 = (46.4307,'kJ/mol'),
        S298 = (-6.62843,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "Cs(Br)3-R-Cs(Br)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {2,S}
6    Br          u0 {1,S}
7    Br          u0 {2,S}
8    Br          u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.70274,-4.38554,-3.93957,-3.22716,-2.05777,-0.803218,2.0757],'J/(mol*K)'),
        H298 = (75.8475,'kJ/mol'),
        S298 = (-15.4149,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "Cs(Cl/Br)3-R-C(Cl/Br)",
    group = 
"""
1 *1 Cs      u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H     ux {1,[S,D]} {3,[S,D]}
3 *2 [Cs,Cd] u0 {2,[S,D]} {7,S}
4    [Cl,Br] u0 {1,S}
5    [Cl,Br] u0 {1,S}
6    [Cl,Br] u0 {1,S}
7    [Cl,Br] u0 {3,S}
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
    index = 81,
    label = "Cs(Cl/Br)3-R-Cs(Cl/Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {2,S}
6    [Cl,Br]     u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [Cl,Br]     u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = 'Cs(Cl)3-R-Cs(Cl)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "Cs(Cl)3-R-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {2,S}
6    Cl          u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    Cl          u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.94642,-1.76913,-1.74212,-1.94442,-2.16328,-1.63217,-0.15035],'J/(mol*K)'),
        H298 = (10.0055,'kJ/mol'),
        S298 = (-1.93784,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "Cs(Br)3-R-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {2,S}
6    Br          u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    Br          u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.16758,-3.48563,-3.35742,-3.05002,-2.55089,-1.87675,-0.459252],'J/(mol*K)'),
        H298 = (23.6619,'kJ/mol'),
        S298 = (-5.52749,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "Cs(Cl/Br)3-R-Cds(Cl/Br)",
    group = 
"""
1 *1 Cs        u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]   u0 {1,S}
5    [Cl,Br]   u0 {1,S}
6    [Cl,Br]   u0 {1,S}
7    [Cl,Br]   u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = 'Cs(Cl)3-R-Cds(Cl)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "Cs(Cl)3-R-Cds(Cl)",
    group = 
"""
1 *1 Cs        u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,[S,D]} {2,[S,D]}
4    Cl        u0 {1,S}
5    Cl        u0 {1,S}
6    Cl        u0 {1,S}
7    Cl        u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1331,-1.53844,-1.64343,-1.50602,-1.13384,-0.567102,0.925525],'J/(mol*K)'),
        H298 = (25.7277,'kJ/mol'),
        S298 = (-2.90598,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "Cs(Br)3-R-Cds(Br)",
    group = 
"""
1 *1 Cs        u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd        u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H       ux {1,[S,D]} {2,[S,D]}
4    Br        u0 {1,S}
5    Br        u0 {1,S}
6    Br        u0 {1,S}
7    Br        u0 {2,S}
8    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.159,-2.65667,-1.92243,-1.11682,0.182753,1.26542,3.46491],'J/(mol*K)'),
        H298 = (75.9408,'kJ/mol'),
        S298 = (-11.9482,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "Cs(Cl/Br)3-R-Cds(Cl/Br)2",
    group = 
"""
1 *1 Cs      u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd      u0 {3,[S,D]} {7,S} {8,S}
3    R!H     ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br] u0 {1,S}
5    [Cl,Br] u0 {1,S}
6    [Cl,Br] u0 {1,S}
7    [Cl,Br] u0 {2,S}
8    [Cl,Br] u0 {2,S}
""",
    thermo = 'Cs(Cl)3-R-Cds(Cl)2',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "Cs(Cl)3-R-Cds(Cl)2",
    group = 
"""
1 *1 Cs  u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,[S,D]} {7,S} {8,S}
3    R!H ux {1,[S,D]} {2,[S,D]}
4    Cl  u0 {1,S}
5    Cl  u0 {1,S}
6    Cl  u0 {1,S}
7    Cl  u0 {2,S}
8    Cl  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.01739,-1.8821,-1.3655,-0.992874,-0.576793,-0.574997,-0.661126],'J/(mol*K)'),
        H298 = (22.1573,'kJ/mol'),
        S298 = (-14.5884,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "Cs(Br)3-R-Cds(Br)2",
    group = 
"""
1 *1 Cs  u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd  u0 {3,[S,D]} {7,S} {8,S}
3    R!H ux {1,[S,D]} {2,[S,D]}
4    Br  u0 {1,S}
5    Br  u0 {1,S}
6    Br  u0 {1,S}
7    Br  u0 {2,S}
8    Br  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.0612,0.920505,1.87346,2.47989,2.69498,2.4206,1.84936],'J/(mol*K)'),
        H298 = (23.3623,'kJ/mol'),
        S298 = (-0.501741,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "Cs(Cl/Br)2-R-Cs(Cl/Br)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {2,S}
6    [Cl,Br]     u0 {1,S}
7    [Cl,Br]     u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = 'Cs(Cl)2-R-Cs(Cl)2',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "Cs(Cl)2-R-Cs(Cl)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {2,S}
6    Cl          u0 {1,S}
7    Cl          u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.05017,-0.986642,-0.922873,-0.9632,-0.975503,-0.725737,0.425722],'J/(mol*K)'),
        H298 = (7.39031,'kJ/mol'),
        S298 = (-1.63346,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "Cs(Br)2-R-Cs(Br)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {2,S}
6    Br          u0 {1,S}
7    Br          u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.7483,-1.68064,-1.45394,-1.27761,-0.991376,-0.613613,0.00356614],'J/(mol*K)'),
        H298 = (9.50199,'kJ/mol'),
        S298 = (-2.04667,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "Cs(Cl/Br)2-R-C(Cl/Br)",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 [Cs,Cd]     u0 {2,[S,D]} {7,S}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    [Cl,Br]     u0 {3,S}
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
    index = 94,
    label = "Cs(Cl/Br)2-R-Cs(Cl/Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {2,S}
6    [Cl,Br]     u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = 'Cs(Cl)2-R-Cs(Cl)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cs(Cl)2-R-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {2,S}
6    Cl          u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.237482,-0.00934623,0.225826,0.470475,0.620047,0.662133,0.901825],'J/(mol*K)'),
        H298 = (0.706954,'kJ/mol'),
        S298 = (-4.24712,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "Cs(Br)2-R-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {2,S}
6    Br          u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18726,-0.504446,0.239543,0.680764,0.91001,0.964654,0.785582],'J/(mol*K)'),
        H298 = (-1.00498,'kJ/mol'),
        S298 = (-1.72593,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "Cs(Cl/Br)2-R-Cds(Cl/Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    [Cl,Br]     u0 {2,S}
8    [C,N,O,S]   u0 {2,[S,D]}
""",
    thermo = 'Cs(Cl)2-R-Cds(Cl)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "Cs(Cl)2-R-Cds(Cl)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    Cl          u0 {2,S}
8    [C,N,O,S]   u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.938505,1.10006,0.967191,0.978471,0.709443,0.590291,1.27675],'J/(mol*K)'),
        H298 = (1.21226,'kJ/mol'),
        S298 = (-3.72275,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "Cs(Br)2-R-Cds(Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    Br          u0 {2,S}
8    [C,N,O,S]   u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.313165,0.394994,0.905183,1.35439,1.38462,1.18258,1.08655],'J/(mol*K)'),
        H298 = (-0.151419,'kJ/mol'),
        S298 = (-1.6193,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "Cs(Cl/Br)2-R-Cds(Cl/Br)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,D} {7,S} {8,S}
3    R!H         ux {1,[S,D]} {2,D}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    [Cl,Br]     u0 {2,S}
8    [Cl,Br]     u0 {2,S}
""",
    thermo = 'Cs(Cl)2-R-Cds(Cl)2',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "Cs(Cl)2-R-Cds(Cl)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,D} {7,S} {8,S}
3    R!H         ux {1,[S,D]} {2,D}
4    Cl          u0 {1,S}
5    Cl          u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    Cl          u0 {2,S}
8    Cl          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.103366,0.984804,1.3602,1.47907,1.30657,1.21332,2.01686],'J/(mol*K)'),
        H298 = (10.2875,'kJ/mol'),
        S298 = (-6.40949,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "Cs(Br)2-R-Cds(Br)2",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,D} {7,S} {8,S}
3    R!H         ux {1,[S,D]} {2,D}
4    Br          u0 {1,S}
5    Br          u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    Br          u0 {2,S}
8    Br          u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.7316,-0.535243,0.944514,1.95224,2.8834,3.03984,3.88002],'J/(mol*K)'),
        H298 = (39.7619,'kJ/mol'),
        S298 = (-22.772,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "C(Cl/Br)-R-C(Cl/Br)",
    group = 
"""
1    R!H     ux {2,[S,D]} {3,[S,D]}
2 *1 [Cs,Cd] u0 {1,[S,D]} {4,S}
3 *2 [Cs,Cd] u0 {1,[S,D]} {5,S}
4    [Cl,Br] u0 {2,S}
5    [Cl,Br] u0 {3,S}
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
    index = 104,
    label = "Cs(Cl/Br)-R-Cs(Cl/Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {2,S}
6    [C,H,N,O,S] u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = 'Cs(Cl)-R-Cs(Cl)',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "Cs(Cl)-R-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {2,S}
6    [C,H,N,O,S] u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0475936,0.425717,0.740709,0.899892,0.939305,0.862424,0.526511],'J/(mol*K)'),
        H298 = (-1.30736,'kJ/mol'),
        S298 = (-0.24506,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "Cs(Br)-R-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {6,S} {8,S}
2 *2 Cs          u0 {3,[S,D]} {5,S} {7,S} {9,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {2,S}
6    [C,H,N,O,S] u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
8    [C,H,N,O,S] u0 {1,S}
9    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.247306,0.297522,0.735416,1.01823,1.21134,1.21393,0.987939],'J/(mol*K)'),
        H298 = (-1.6983,'kJ/mol'),
        S298 = (-2.08457,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "Cs(Cl/Br)-R-Cds(Cl/Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    [Cl,Br]     u0 {2,S}
8    [C,N,O,S]   u0 {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "Cs(Cl)-R-Cds(Cl)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    Cl          u0 {2,S}
8    [C,N,O,S]   u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.535348,-0.242394,-0.0450451,0.211158,0.409668,0.519366,0.630577],'J/(mol*K)'),
        H298 = (-2.86965,'kJ/mol'),
        S298 = (-1.00838,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "Cs(Br)-R-Cds(Br)",
    group = 
"""
1 *1 Cs          u0 {3,[S,D]} {4,S} {5,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {7,S} {8,[S,D]}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    [C,H,N,O,S] u0 {1,S}
7    Br          u0 {2,S}
8    [C,N,O,S]   u0 {2,[S,D]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.133816,0.28651,0.451904,0.745501,0.93322,1.05004,1.26993],'J/(mol*K)'),
        H298 = (-2.14693,'kJ/mol'),
        S298 = (-2.2269,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "Cds(Cl/Br)-R-Cds(Cl/Br)",
    group = 
"""
1 *1 Cd        u0 {3,[S,D]} {4,S} {6,[S,D]}
2 *2 Cd        u0 {3,[S,D]} {5,S} {7,[S,D]}
3    R!H       ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]   u0 {1,S}
5    [Cl,Br]   u0 {2,S}
6    [C,N,O,S] u0 {1,[S,D]}
7    [C,N,O,S] u0 {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "Cds(Cl)-R-Cds(Cl)",
    group = 
"""
1 *1 Cd        u0 {3,S} {5,[S,D]} {7,[S,D]}
2 *2 Cd        u0 {4,S} {6,[S,D]} {7,[S,D]}
3    Cl        u0 {1,S}
4    Cl        u0 {2,S}
5    [C,N,O,S] u0 {1,[S,D]}
6    [C,N,O,S] u0 {2,[S,D]}
7    R!H       ux {1,[S,D]} {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "Cds(Br)-R-Cds(Br)",
    group = 
"""
1 *1 Cd        u0 {3,S} {5,[S,D]} {7,[S,D]}
2 *2 Cd        u0 {4,S} {6,[S,D]} {7,[S,D]}
3    Br        u0 {1,S}
4    Br        u0 {2,S}
5    [C,N,O,S] u0 {1,[S,D]}
6    [C,N,O,S] u0 {2,[S,D]}
7    R!H       ux {1,[S,D]} {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "Cds(Cl/Br)2-R-Cds(Cl/Br)",
    group = 
"""
1 *1 Cd          u0 {3,[S,D]} {4,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {5,S} {7,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {2,S}
6    [Cl,Br]     u0 {1,S}
7    [C,H,O,N,S] u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "Cds(Cl)2-R-Cds(Cl)",
    group = 
"""
1 *1 Cd          u0 {3,[S,D]} {4,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {5,S} {7,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Cl          u0 {1,S}
5    Cl          u0 {2,S}
6    Cl          u0 {1,S}
7    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.675981,0.438533,0.443288,0.381115,0.113486,-0.142367,-0.67713],'J/(mol*K)'),
        H298 = (2.28434,'kJ/mol'),
        S298 = (-3.87462,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "Cds(Br)2-R-Cds(Br)",
    group = 
"""
1 *1 Cd          u0 {3,[S,D]} {4,S} {6,S}
2 *2 Cd          u0 {3,[S,D]} {5,S} {7,S}
3    R!H         ux {1,[S,D]} {2,[S,D]}
4    Br          u0 {1,S}
5    Br          u0 {2,S}
6    Br          u0 {1,S}
7    [C,H,O,N,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.25545,-1.46816,-1.40463,-1.24488,-1.36192,-1.50779,-1.72509],'J/(mol*K)'),
        H298 = (4.56288,'kJ/mol'),
        S298 = (-9.25935,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "Cds(Cl/Br)2-R-Cds(Cl/Br)2",
    group = 
"""
1 *1 Cd      u0 {3,[S,D]} {4,S} {6,S}
2 *2 Cd      u0 {3,[S,D]} {5,S} {7,S}
3    R!H     ux {1,[S,D]} {2,[S,D]}
4    [Cl,Br] u0 {1,S}
5    [Cl,Br] u0 {2,S}
6    [Cl,Br] u0 {1,S}
7    [Cl,Br] u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "Cds(Cl)2-R-Cds(Cl)2",
    group = 
"""
1 *1 Cd  u0 {3,[S,D]} {4,S} {6,S}
2 *2 Cd  u0 {3,[S,D]} {5,S} {7,S}
3    R!H ux {1,[S,D]} {2,[S,D]}
4    Cl  u0 {1,S}
5    Cl  u0 {2,S}
6    Cl  u0 {1,S}
7    Cl  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.609395,-0.411032,-0.478077,-0.492356,-0.852755,-1.09669,-1.35592],'J/(mol*K)'),
        H298 = (5.68501,'kJ/mol'),
        S298 = (-6.30921,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "Cds(Br)2-R-Cds(Br)2",
    group = 
"""
1 *1 Cd  u0 {3,[S,D]} {4,S} {6,S}
2 *2 Cd  u0 {3,[S,D]} {5,S} {7,S}
3    R!H ux {1,[S,D]} {2,[S,D]}
4    Br  u0 {1,S}
5    Br  u0 {2,S}
6    Br  u0 {1,S}
7    Br  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.827656,-0.247468,-0.311888,-0.56415,-1.32131,-1.72763,-1.84597],'J/(mol*K)'),
        H298 = (2.6784,'kJ/mol'),
        S298 = (-9.77371,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "Cd(Cl/Br)-R-CO",
    group = 
"""
1    R!H     ux {2,[S,D]} {3,[S,D]}
2 *1 Cd      u0 {1,[S,D]} {4,S}
3 *2 CO      u0 {1,[S,D]} {5,D}
4    [Cl,Br] u0 {2,S}
5    O2d     u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "Cd(Cl)-R-CO",
    group = 
"""
1    R!H ux {2,[S,D]} {3,[S,D]}
2 *1 Cd  u0 {1,[S,D]} {4,S}
3 *2 CO  u0 {1,[S,D]} {5,D}
4    Cl  u0 {2,S}
5    O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.318271,1.5099,2.01203,2.0497,1.58892,1.21065,1.47255],'J/(mol*K)'),
        H298 = (-1.14196,'kJ/mol'),
        S298 = (-5.43884,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "Cd(Br)-R-CO",
    group = 
"""
1    R!H ux {2,[S,D]} {3,[S,D]}
2 *1 Cd  u0 {1,[S,D]} {4,S}
3 *2 CO  u0 {1,[S,D]} {5,D}
4    Br  u0 {2,S}
5    O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.713548,1.25158,1.9655,2.05902,1.54611,1.23418,1.67856],'J/(mol*K)'),
        H298 = (-1.49348,'kJ/mol'),
        S298 = (-7.284,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "Cs(Cl/Br)3-R-CO",
    group = 
"""
1 *1 Cs      u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H     ux {1,[S,D]} {3,[S,D]}
3 *2 CO      u0 {2,[S,D]} {7,D}
4    [Cl,Br] u0 {1,S}
5    [Cl,Br] u0 {1,S}
6    [Cl,Br] u0 {1,S}
7    O2d     u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
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
        Cpdata = ([4.53374,4.91369,4.86114,4.4266,3.13892,2.06862,0.586956],'J/(mol*K)'),
        H298 = (6.70163,'kJ/mol'),
        S298 = (-4.17022,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
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
        Cpdata = ([5.97022,7.34575,7.37311,6.65715,4.47471,2.7193,-0.106225],'J/(mol*K)'),
        H298 = (15.6237,'kJ/mol'),
        S298 = (-4.31791,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "Cs(Cl/Br)2-R-CO",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 CO          u0 {2,[S,D]} {7,D}
4    [Cl,Br]     u0 {1,S}
5    [Cl,Br]     u0 {1,S}
6    [C,H,O,N,S] u0 {1,S}
7    O2d         u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "Cs(Cl)2-R-CO",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 CO          u0 {2,[S,D]} {7,D}
4    Cl          u0 {1,S}
5    Cl          u0 {1,S}
6    [C,H,O,N,S] u0 {1,S}
7    O2d         u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.00641,0.545385,0.175423,-0.00124011,0.0690117,0.161532,0.978524],'J/(mol*K)'),
        H298 = (2.6357,'kJ/mol'),
        S298 = (1.50352,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "Cs(Br)2-R-CO",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 CO          u0 {2,[S,D]} {7,D}
4    Br          u0 {1,S}
5    Br          u0 {1,S}
6    [C,H,O,N,S] u0 {1,S}
7    O2d         u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.134143,0.572003,0.738729,0.568397,0.307578,0.348373,0.514591],'J/(mol*K)'),
        H298 = (5.05111,'kJ/mol'),
        S298 = (-2.86059,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "Cs(Cl/Br)-R-CO",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 CO          u0 {2,[S,D]} {7,D}
4    [Cl,Br]     u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {1,S}
7    O2d         u0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "Cs(Cl)-R-CO",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 CO          u0 {2,[S,D]} {7,D}
4    Cl          u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {1,S}
7    O2d         u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.20122,0.679442,0.249191,-0.196846,-0.861141,-1.05166,-0.510242],'J/(mol*K)'),
        H298 = (-0.982592,'kJ/mol'),
        S298 = (3.13447,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "Cs(Br)-R-CO",
    group = 
"""
1 *1 Cs          u0 {2,[S,D]} {4,S} {5,S} {6,S}
2    R!H         ux {1,[S,D]} {3,[S,D]}
3 *2 CO          u0 {2,[S,D]} {7,D}
4    Br          u0 {1,S}
5    [C,H,O,N,S] u0 {1,S}
6    [C,H,O,N,S] u0 {1,S}
7    O2d         u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.3774,1.09863,0.829816,0.411183,-0.234696,-0.44195,0.0331537],'J/(mol*K)'),
        H298 = (-0.341897,'kJ/mol'),
        S298 = (2.46806,'J/(mol*K)'),
    ),
    shortDesc = """Derived from halogen species in CHOClBr_wb97xd3 thermo libraries""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
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
    index = 132,
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
    index = 133,
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
    index = 134,
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
    index = 135,
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
    index = 136,
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
    index = 137,
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
    index = 138,
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
    index = 139,
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
    index = 140,
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
    index = 141,
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
    index = 142,
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
    index = 143,
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
    index = 144,
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
    index = 145,
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
    index = 146,
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
    index = 147,
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
    index = 148,
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
    index = 149,
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
    index = 150,
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
    index = 151,
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
    index = 152,
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
    index = 153,
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
    index = 154,
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
    index = 155,
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
    index = 156,
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
    index = 157,
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
    index = 158,
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
    index = 159,
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
    index = 160,
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
    index = 161,
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
    index = 162,
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
    index = 163,
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
    index = 164,
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
    index = 165,
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
    index = 166,
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
    index = 167,
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
    index = 168,
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
    index = 169,
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
    index = 170,
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
    L2: intRVal7
        L3: Cs(Cl/Br)3-R-Cs(Cl/Br)3
            L4: Cs(Cl)3-R-Cs(Cl)3
            L4: Cs(Br)3-R-Cs(Br)3
        L3: Cs(Cl/Br)3-R-Cs(Cl/Br)2
            L4: Cs(Cl)3-R-Cs(Cl)2
            L4: Cs(Br)3-R-Cs(Br)2
        L3: Cs(Cl/Br)3-R-C(Cl/Br)
            L4: Cs(Cl/Br)3-R-Cs(Cl/Br)
                L5: Cs(Cl)3-R-Cs(Cl)
                L5: Cs(Br)3-R-Cs(Br)
            L4: Cs(Cl/Br)3-R-Cds(Cl/Br)
                L5: Cs(Cl)3-R-Cds(Cl)
                L5: Cs(Br)3-R-Cds(Br)
            L4: Cs(Cl/Br)3-R-Cds(Cl/Br)2
                L5: Cs(Cl)3-R-Cds(Cl)2
                L5: Cs(Br)3-R-Cds(Br)2
        L3: Cs(Cl/Br)2-R-Cs(Cl/Br)2
            L4: Cs(Cl)2-R-Cs(Cl)2
            L4: Cs(Br)2-R-Cs(Br)2
        L3: Cs(Cl/Br)2-R-C(Cl/Br)
            L4: Cs(Cl/Br)2-R-Cs(Cl/Br)
                L5: Cs(Cl)2-R-Cs(Cl)
                L5: Cs(Br)2-R-Cs(Br)
            L4: Cs(Cl/Br)2-R-Cds(Cl/Br)
                L5: Cs(Cl)2-R-Cds(Cl)
                L5: Cs(Br)2-R-Cds(Br)
            L4: Cs(Cl/Br)2-R-Cds(Cl/Br)2
                L5: Cs(Cl)2-R-Cds(Cl)2
                L5: Cs(Br)2-R-Cds(Br)2
        L3: C(Cl/Br)-R-C(Cl/Br)
            L4: Cs(Cl/Br)-R-Cs(Cl/Br)
                L5: Cs(Cl)-R-Cs(Cl)
                L5: Cs(Br)-R-Cs(Br)
            L4: Cs(Cl/Br)-R-Cds(Cl/Br)
                L5: Cs(Cl)-R-Cds(Cl)
                L5: Cs(Br)-R-Cds(Br)
            L4: Cds(Cl/Br)-R-Cds(Cl/Br)
                L5: Cds(Cl)-R-Cds(Cl)
                L5: Cds(Br)-R-Cds(Br)
            L4: Cds(Cl/Br)2-R-Cds(Cl/Br)
                L5: Cds(Cl)2-R-Cds(Cl)
                L5: Cds(Br)2-R-Cds(Br)
            L4: Cds(Cl/Br)2-R-Cds(Cl/Br)2
                L5: Cds(Cl)2-R-Cds(Cl)2
                L5: Cds(Br)2-R-Cds(Br)2
        L3: Cd(Cl/Br)-R-CO
            L4: Cd(Cl)-R-CO
            L4: Cd(Br)-R-CO
        L3: Cs(Cl/Br)3-R-CO
            L4: Cs(Cl)3-R-CO
            L4: Cs(Br)3-R-CO
        L3: Cs(Cl/Br)2-R-CO
            L4: Cs(Cl)2-R-CO
            L4: Cs(Br)2-R-CO
        L3: Cs(Cl/Br)-R-CO
            L4: Cs(Cl)-R-CO
            L4: Cs(Br)-R-CO
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

