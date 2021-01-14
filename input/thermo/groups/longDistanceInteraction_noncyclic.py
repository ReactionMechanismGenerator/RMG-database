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
        Cpdata = ([-0.0615047,0.111995,0.204157,0.244912,0.259704,0.249044,0.372897],'cal/(mol*K)','+|-',[0.192883,0.222989,0.228507,0.225439,0.195993,0.169257,0.13479]),
        H298 = (4.03105,'kcal/mol','+|-',0.700433),
        S298 = (0.242371,'cal/(mol*K)','+|-',0.454868),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:FC(F)(F)C(F)(F)Br smiles:FC(F)(F)C(F)(F)Br H298:-257.40 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)(Br)Br smiles:FC(F)(Br)C(Br)(Br)Br H298:-81.00 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)(Br)Br smiles:FC(F)(F)C(Br)(Br)Br H298:-144.68 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)(Br)Br smiles:FC(Br)(Br)C(Br)(Br)Br H298:-21.80 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(F)(Br)Br smiles:FC(F)(F)C(F)(Br)Br H298:-198.37 kcal/mol
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
        Cpdata = ([0.600273,0.433984,0.340454,0.272228,0.149393,0.0450281,-0.00208503],'cal/(mol*K)','+|-',[0.422487,0.488431,0.500518,0.493796,0.4293,0.370736,0.295241]),
        H298 = (5.7246,'kcal/mol','+|-',1.53421),
        S298 = (-0.176373,'cal/(mol*K)','+|-',0.996333),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Hexachloroethane smiles:ClC(Cl)(Cl)C(Cl)(Cl)Cl H298:-35.71 kcal/mol
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
        Cpdata = ([0.109127,0.233358,0.228902,0.251746,0.296682,0.29407,0.257457],'cal/(mol*K)','+|-',[0.419509,0.484989,0.496991,0.490317,0.426274,0.368124,0.293161]),
        H298 = (5.78245,'kcal/mol','+|-',1.5234),
        S298 = (-0.293759,'cal/(mol*K)','+|-',0.989312),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Hexafluoroethane smiles:FC(F)(F)C(F)(F)F H298:-320.86 kcal/mol
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
        Cpdata = ([-0.786251,-0.687122,-0.482632,-0.399552,-0.314343,-0.203003,0.354846],'cal/(mol*K)','+|-',[0.132793,0.153521,0.15732,0.155207,0.134935,0.116528,0.0927984]),
        H298 = (4.73418,'kcal/mol','+|-',0.482225),
        S298 = (1.14028,'cal/(mol*K)','+|-',0.313161),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:FC(Cl)(Cl)C(Cl)Cl smiles:FC(Cl)(Cl)C(Cl)Cl H298:-82.62 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)(Cl)Cl smiles:FC(F)C(F)(Cl)Cl H298:-168.95 kcal/mol
library:CHOFCl_G4 label:FC(F)(Cl)C(Cl)Cl smiles:FC(F)(Cl)C(Cl)Cl H298:-129.86 kcal/mol
library:CHOFCl_G4 label:FC(F)(F)C(Cl)Cl smiles:FC(F)(F)C(Cl)Cl H298:-180.18 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)(F)Cl smiles:FC(F)C(F)(F)Cl H298:-215.90 kcal/mol
library:CHOFCl_G4 label:FC(Cl)C(Cl)(Cl)Cl smiles:FC(Cl)C(Cl)(Cl)Cl H298:-80.26 kcal/mol
library:CHOFCl_G4 label:FC(F)C(Cl)(Cl)Cl smiles:FC(F)C(Cl)(Cl)Cl H298:-125.60 kcal/mol
library:CHOFCl_G4 label:FC(Cl)C(F)(F)F smiles:FC(Cl)C(F)(F)F H298:-221.16 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)(Br)Br smiles:FC(Cl)C(Cl)(Br)Br H298:-56.55 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)(Br)Br smiles:FC(F)C(Cl)(Br)Br H298:-101.80 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Br)C(Br)Br smiles:FC(Cl)(Br)C(Br)Br H298:-46.77 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)(Cl)Br smiles:FC(F)C(Cl)(Cl)Br H298:-113.64 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)(Cl)Br smiles:FC(Cl)C(Cl)(Cl)Br H298:-68.28 kcal/mol
library:CHOFClBr_G4 label:FC(F)(F)C(Cl)Br smiles:FC(F)(F)C(Cl)Br H298:-168.46 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)C(Cl)Br smiles:FC(F)(Cl)C(Cl)Br H298:-118.11 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(F)(Cl)Br smiles:FC(F)C(F)(Cl)Br H298:-156.08 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)C(Cl)Br smiles:FC(Cl)(Cl)C(Cl)Br H298:-70.91 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)(Br)Br smiles:FC(Cl)C(Br)(Br)Br H298:-44.83 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)C(Br)Br smiles:FC(Cl)(Cl)C(Br)Br H298:-59.38 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)C(Br)Br smiles:FC(F)(Cl)C(Br)Br H298:-106.37 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)(F)F smiles:OC(Br)(Br)C(F)(F)F H298:-196.43 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)(Br)Br smiles:CC(F)(Br)C(Br)(Br)Br H298:-43.00 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(F)(F)F smiles:FC(Br)C(F)(F)F H298:-208.45 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)(F)Br smiles:OC(Br)(Br)C(F)(F)Br H298:-132.91 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)(Br)Br smiles:OC(Br)(Br)C(F)(Br)Br H298:-73.69 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)(Br)Br smiles:CC(Br)(Br)C(F)(Br)Br H298:-43.88 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)(Br)Br smiles:CC(F)(F)C(Br)(Br)Br H298:-102.19 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)(F)Br smiles:CC(F)(F)C(F)(F)Br H298:-216.00 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)(F)Br smiles:CC(Br)(Br)C(F)(F)Br H298:-103.44 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)Br smiles:FC(F)(Br)C(Br)Br H298:-93.01 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)Br smiles:FC(Br)C(Br)(Br)Br H298:-32.32 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)Br smiles:FC(F)C(F)(F)Br H298:-202.36 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)Br smiles:FC(Br)(Br)C(Br)Br H298:-34.21 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)Br smiles:FC(F)C(Br)(Br)Br H298:-90.07 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)(F)F smiles:OC(F)(Br)C(F)(F)F H298:-254.54 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)(Br)Br smiles:CC(F)(F)C(F)(Br)Br H298:-156.44 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)Br smiles:FC(F)C(F)(Br)Br H298:-143.49 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)Br smiles:FC(F)(F)C(Br)Br H298:-156.93 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)(F)F smiles:CC(Br)(Br)C(F)(F)F H298:-167.52 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)(F)F smiles:CC(F)(Br)C(F)(F)F H298:-220.90 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Cl)C(Br)Br smiles:ClC(Cl)(Cl)C(Br)Br H298:-15.68 kcal/mol
library:CHOClBr_G4 label:ClC(Br)(Br)C(Br)Br smiles:ClC(Br)(Br)C(Br)Br H298:7.95 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)(Br)Br smiles:ClC(Cl)C(Br)(Br)Br H298:-3.49 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Br)C(Br)Br smiles:ClC(Cl)(Br)C(Br)Br H298:-3.80 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)(Cl)Br smiles:ClC(Cl)C(Cl)(Cl)Br H298:-27.04 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)(Br)Br smiles:ClC(Cl)C(Cl)(Br)Br H298:-15.21 kcal/mol
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
        Cpdata = ([-0.0711893,-0.299328,-0.280761,-0.249996,-0.200401,-0.101526,0.423223],'cal/(mol*K)','+|-',[0.171286,0.198021,0.202921,0.200196,0.174048,0.150305,0.119698]),
        H298 = (9.33728,'kcal/mol','+|-',0.622006),
        S298 = (-1.28838,'cal/(mol*K)','+|-',0.403936),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Pentachloroethane smiles:ClC(Cl)C(Cl)(Cl)Cl H298:-37.57 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)Cl H298:-41.53 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.15 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-55.19 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:C=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-21.09 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-85.64 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-70.00 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-56.00 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-60.00 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-53.17 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.38 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-29.12 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC#CC(Cl)(Cl)C(Cl)(Cl)Cl H298:24.52 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-48.10 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-47.42 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-42.50 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-24.56 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)Cl H298:-50.01 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-52.65 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)Cl H298:-79.76 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:O=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-60.22 kcal/mol
library:CHOCl_G4 label:CCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:CCC(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.06 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOCC(Cl)(Cl)C(Cl)(Cl)Cl H298:-46.06 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-59.89 kcal/mol
library:CHOCl_G4 label:ClC(Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-59.06 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-27.25 kcal/mol
library:CHOCl_G4 label:OCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:OCC(Cl)(Cl)C(Cl)(Cl)Cl H298:-82.69 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCOC(Cl)(Cl)C(Cl)(Cl)Cl H298:-81.72 kcal/mol
library:CHOCl_G4 label:OOC(Cl)(Cl)C(Cl)(Cl)Cl smiles:OOC(Cl)(Cl)C(Cl)(Cl)Cl H298:-57.62 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-22.98 kcal/mol
library:CHOCl_G4 label:ClC(Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl H298:-85.85 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-84.83 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl H298:-82.36 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOOC(Cl)(Cl)C(Cl)(Cl)Cl H298:-23.92 kcal/mol
library:CHOCl_G4 label:COC(Cl)(Cl)C(Cl)(Cl)Cl smiles:COC(Cl)(Cl)C(Cl)(Cl)Cl H298:-77.04 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-28.39 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-48.77 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-46.43 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)(Cl)C(Cl)(Cl)Cl smiles:C#CC(Cl)(Cl)C(Cl)(Cl)Cl H298:25.60 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-48.77 kcal/mol
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
        Cpdata = ([-0.230599,-0.194392,-0.0584022,0.00591093,0.0292199,0.0845259,0.393645],'cal/(mol*K)','+|-',[0.160948,0.18607,0.190674,0.188114,0.163543,0.141233,0.112473]),
        H298 = (10.1478,'kcal/mol','+|-',0.584464),
        S298 = (0.410919,'cal/(mol*K)','+|-',0.379557),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)(F)F smiles:FC=C(F)C(F)(F)C(F)(F)F H298:-332.04 kcal/mol
library:CHOF_G4 label:FC(F)CC(F)(F)C(F)(F)F smiles:FC(F)CC(F)(F)C(F)(F)F H298:-378.83 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)C(F)(F)C(F)(F)F H298:-414.81 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)C(F)(F)F smiles:OC(F)(F)C(F)(F)C(F)(F)F H298:-416.21 kcal/mol
library:CHOF_G4 label:FC(F)(F)OC(F)(F)C(F)(F)F smiles:FC(F)(F)OC(F)(F)C(F)(F)F H298:-468.96 kcal/mol
library:CHOF_G4 label:FCCC(F)(F)C(F)(F)F smiles:FCCC(F)(F)C(F)(F)F H298:-326.56 kcal/mol
library:CHOF_G4 label:OOC(F)(F)C(F)(F)F smiles:OOC(F)(F)C(F)(F)F H298:-292.26 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)C(F)(F)F smiles:C=C(F)C(F)(F)C(F)(F)F H298:-293.10 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)C(F)(F)F smiles:FCC(F)(F)C(F)(F)C(F)(F)F H298:-415.15 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)(F)C(F)(F)C(F)(F)C(F)(F)F H298:-518.11 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)(F)C(F)(F)F smiles:FC(F)=CC(F)(F)C(F)(F)F H298:-341.93 kcal/mol
library:CHOF_G4 label:FC(C(F)(F)F)C(F)(F)C(F)(F)F smiles:FC(C(F)(F)F)C(F)(F)C(F)(F)F H298:-471.81 kcal/mol
library:CHOF_G4 label:FOCC(F)(F)C(F)(F)F smiles:FOCC(F)(F)C(F)(F)F H298:-279.59 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)F smiles:CC(F)(F)C(F)(F)F H298:-280.00 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)C(F)(F)F smiles:O=C(F)C(F)(F)C(F)(F)F H298:-344.15 kcal/mol
library:CHOF_G4 label:COC(F)(F)C(F)(F)F smiles:COC(F)(F)C(F)(F)F H298:-312.94 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)C(F)(F)F smiles:O=CC(F)(F)C(F)(F)F H298:-285.38 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)F smiles:FOC(F)(F)C(F)(F)F H298:-276.59 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)F smiles:FC(F)C(F)(F)F H298:-266.16 kcal/mol
library:CHOF_G4 label:CDCC(F)(F)C(F)(F)F smiles:C=CC(F)(F)C(F)(F)F H298:-250.77 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)C(F)(F)F smiles:OC(F)C(F)(F)C(F)(F)F H298:-360.97 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)C(F)(F)F smiles:CC(F)(F)C(F)(F)C(F)(F)F H298:-378.68 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)F smiles:FCC(F)(F)C(F)(F)F H298:-316.54 kcal/mol
library:CHOF_G4 label:FCDCC(F)(F)C(F)(F)F smiles:FC=CC(F)(F)C(F)(F)F H298:-295.00 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)(F)C(F)(F)F H298:-463.90 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)(F)F H298:-365.14 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)C(F)(F)F smiles:FOC(F)(F)C(F)(F)C(F)(F)F H298:-375.57 kcal/mol
library:CHOF_G4 label:CCC(F)(F)C(F)(F)F smiles:CCC(F)(F)C(F)(F)F H298:-284.69 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)C(F)(F)F smiles:FOC(F)C(F)(F)C(F)(F)F H298:-325.79 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)F smiles:OC(F)(F)C(F)(F)F H298:-317.29 kcal/mol
library:CHOF_G4 label:FOOC(F)(F)C(F)(F)F smiles:FOOC(F)(F)C(F)(F)F H298:-264.90 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)C(F)(F)F H298:-374.89 kcal/mol
library:CHOF_G4 label:FC#CC(F)(F)C(F)(F)F smiles:FC#CC(F)(F)C(F)(F)F H298:-231.32 kcal/mol
library:CHOF_G4 label:OCC(F)(F)C(F)(F)F smiles:OCC(F)(F)C(F)(F)F H298:-311.38 kcal/mol
library:CHOF_G4 label:FC(F)(F)CC(F)(F)C(F)(F)F smiles:FC(F)(F)CC(F)(F)C(F)(F)F H298:-435.66 kcal/mol
library:CHOF_G4 label:FCOC(F)(F)C(F)(F)F smiles:FCOC(F)(F)C(F)(F)F H298:-360.16 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)C(F)(F)F smiles:FCC(F)C(F)(F)C(F)(F)F H298:-366.48 kcal/mol
library:CHOF_G4 label:FC(F)OC(F)(F)C(F)(F)F smiles:FC(F)OC(F)(F)C(F)(F)F H298:-414.48 kcal/mol
library:CHOF_G4 label:C#CC(F)(F)C(F)(F)F smiles:C#CC(F)(F)C(F)(F)F H298:-202.29 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)(F)C(F)(F)C(F)(F)F H298:-420.07 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)C(F)(F)F smiles:CC(F)C(F)(F)C(F)(F)F H298:-327.15 kcal/mol
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
        Cpdata = ([-0.357799,-0.654841,-0.742496,-0.847892,-0.980091,-0.972729,-0.432186],'cal/(mol*K)','+|-',[0.832302,0.962214,0.986024,0.972783,0.845724,0.730353,0.581628]),
        H298 = (5.26618,'kcal/mol','+|-',3.02241),
        S298 = (2.41018,'cal/(mol*K)','+|-',1.96278),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC(Br)C(Br)(Br)Br smiles:BrC(Br)C(Br)(Br)Br H298:19.64 kcal/mol
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
        Cpdata = ([-0.259877,-0.255026,-0.185151,-0.152218,-0.112956,-0.0692446,0.282323],'cal/(mol*K)','+|-',[0.0968394,0.111955,0.114725,0.113185,0.098401,0.0849775,0.0676731]),
        H298 = (2.8743,'kcal/mol','+|-',0.351662),
        S298 = (0.711251,'cal/(mol*K)','+|-',0.228373),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CC(F)C(F)(F)Cl smiles:CC(F)C(F)(F)Cl H298:-176.83 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)(Cl)Cl smiles:FCC(Cl)(Cl)Cl H298:-75.52 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)(F)Cl smiles:CC(Cl)C(F)(F)Cl H298:-137.48 kcal/mol
library:CHOFCl_G4 label:FCC(F)(F)Cl smiles:FCC(F)(F)Cl H298:-166.36 kcal/mol
library:CHOFCl_G4 label:CC(F)C(F)(Cl)Cl smiles:CC(F)C(F)(Cl)Cl H298:-129.20 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)(F)F smiles:OC(Cl)C(F)(F)F H298:-218.08 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)(Cl)Cl smiles:OC(Cl)C(F)(Cl)Cl H298:-120.98 kcal/mol
library:CHOFCl_G4 label:FCC(F)(Cl)Cl smiles:FCC(F)(Cl)Cl H298:-119.17 kcal/mol
library:CHOFCl_G4 label:FC(F)(F)CCl smiles:FC(F)(F)CCl H298:-178.90 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)(F)F smiles:CC(Cl)C(F)(F)F H298:-188.21 kcal/mol
library:CHOFCl_G4 label:FC(Cl)(Cl)CCl smiles:FC(Cl)(Cl)CCl H298:-81.17 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)(Cl)Cl smiles:CC(Cl)C(F)(Cl)Cl H298:-89.77 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)(F)Cl smiles:OC(Cl)C(F)(F)Cl H298:-168.09 kcal/mol
library:CHOFCl_G4 label:FC(F)(Cl)CCl smiles:FC(F)(Cl)CCl H298:-128.54 kcal/mol
library:CHOFCl_G4 label:CC(F)C(Cl)(Cl)Cl smiles:CC(F)C(Cl)(Cl)Cl H298:-85.45 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)(Cl)Br smiles:CC(F)C(Cl)(Cl)Br H298:-73.47 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)CBr smiles:FC(F)(Cl)CBr H298:-117.46 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Br)CBr smiles:FC(Cl)(Br)CBr H298:-57.16 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)(Cl)Br smiles:OC(Br)C(F)(Cl)Br H298:-96.24 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)CBr smiles:FC(Cl)(Cl)CBr H298:-70.06 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)(Cl)Cl smiles:CC(Br)C(F)(Cl)Cl H298:-78.43 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)(Br)Br smiles:CC(F)C(Cl)(Br)Br H298:-61.58 kcal/mol
library:CHOFClBr_G4 label:FCC(F)(Cl)Br smiles:FCC(F)(Cl)Br H298:-106.35 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)(F)Cl smiles:OC(Br)C(F)(F)Cl H298:-155.84 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)(F)Cl smiles:CC(Br)C(F)(F)Cl H298:-125.95 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)(Cl)Br smiles:CC(Br)C(F)(Cl)Br H298:-65.74 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)(Cl)Cl smiles:OC(Br)C(F)(Cl)Cl H298:-108.77 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Br)Br smiles:FCC(Cl)(Br)Br H298:-51.74 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(F)(Cl)Br smiles:CC(F)C(F)(Cl)Br H298:-116.60 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Cl)Br smiles:FCC(Cl)(Cl)Br H298:-63.60 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(Br)(Br)Br smiles:C=CC(F)C(Br)(Br)Br H298:-22.76 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)Br smiles:FCC(Br)(Br)Br H298:-39.93 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)Br smiles:FCC(F)(Br)Br H298:-93.77 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)OBr smiles:FC(F)(F)C(Br)OBr H298:-165.06 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)CBr smiles:FC(Br)(Br)C(Br)CBr H298:-45.23 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(F)(F)Br smiles:CC(C)(F)C(F)(F)Br H298:-174.07 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)(Br)Br smiles:FCC(F)C(Br)(Br)Br H298:-89.52 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)(F)F smiles:OC(O)(Br)C(F)(F)F H298:-250.38 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)(F)Br smiles:CC(C)(Br)C(F)(F)Br H298:-121.60 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)(F)Br smiles:OC(O)(Br)C(F)(F)Br H298:-186.80 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)(Br)Br smiles:CCC(Br)C(F)(Br)Br H298:-58.73 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)CBr smiles:FC(F)(Br)C(Br)CBr H298:-103.98 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(F)(Br)Br smiles:C=CC(F)C(F)(Br)Br H298:-76.97 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)Br smiles:OC(Br)C(F)(Br)Br H298:-83.79 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(Br)Br smiles:FCC(F)C(F)(Br)Br H298:-143.53 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)(F)F smiles:COC(Br)C(F)(F)F H298:-201.89 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(Br)(Br)Br smiles:CC(C)(F)C(Br)(Br)Br H298:-59.15 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(Br)(Br)Br smiles:CCC(F)C(Br)(Br)Br H298:-54.82 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)(F)F smiles:OCC(Br)C(F)(F)F H298:-210.68 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)(F)Br smiles:OCC(Br)C(F)(F)Br H298:-146.37 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)(F)Br smiles:COC(Br)C(F)(F)Br H298:-138.22 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)(Br)Br smiles:CC(C)(Br)C(F)(Br)Br H298:-61.65 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(F)(Br)Br smiles:CC(O)(F)C(F)(Br)Br H298:-152.60 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(F)Br smiles:FCC(F)C(F)(F)Br H298:-202.76 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)(Br)Br smiles:OCC(Br)C(F)(Br)Br H298:-86.78 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)CBr smiles:FC(F)(F)CBr H298:-168.26 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(F)(F)Br smiles:CCC(F)C(F)(F)Br H298:-168.15 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)(F)F smiles:CC(O)(Br)C(F)(F)F H298:-217.65 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)Br smiles:CC(Br)C(F)(F)Br H298:-112.46 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(F)(Br)Br smiles:CCC(F)C(F)(Br)Br H298:-108.64 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)CBr smiles:FC(F)(Br)CBr H298:-104.19 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(Br)(Br)Br smiles:C#CC(F)C(Br)(Br)Br H298:22.52 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)F smiles:CC(Br)C(F)(F)F H298:-176.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)F smiles:OC(Br)C(F)(F)F H298:-205.75 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)Br smiles:OC(Br)C(F)(F)Br H298:-142.64 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(F)(Br)Br smiles:C#CC(F)C(F)(Br)Br H298:-31.18 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(F)(F)Br smiles:C=CC(F)C(F)(F)Br H298:-136.31 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)(Br)Br smiles:OC(O)(Br)C(F)(Br)Br H298:-127.91 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(F)(F)Br smiles:C#CC(F)C(F)(F)Br H298:-90.01 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)(F)F smiles:CC(C)(Br)C(F)(F)F H298:-186.11 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(F)(Br)Br smiles:CC(C)(F)C(F)(Br)Br H298:-114.09 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)(Br)Br smiles:OOC(Br)C(F)(Br)Br H298:-62.36 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)CBr smiles:FC(Br)(Br)CBr H298:-44.83 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(Br)Br smiles:CC(Br)C(F)(Br)Br H298:-53.22 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(Br)(Br)Br smiles:CC(O)(F)C(Br)(Br)Br H298:-98.20 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)(F)F smiles:OOC(Br)C(F)(F)F H298:-184.61 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)(Br)Br smiles:COC(Br)C(F)(Br)Br H298:-79.76 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)(Br)Br smiles:CC(O)(Br)C(F)(Br)Br H298:-94.61 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)Br smiles:FCC(F)(F)Br H298:-152.84 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)(F)Br smiles:OOC(Br)C(F)(F)Br H298:-120.88 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)(F)F smiles:CCC(Br)C(F)(F)F H298:-181.85 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)OBr smiles:FC(F)(Br)C(Br)OBr H298:-101.65 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)Br smiles:CC(F)C(Br)(Br)Br H298:-49.71 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)(F)Br smiles:CCC(Br)C(F)(F)Br H298:-117.92 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(Br)Br smiles:CC(F)C(F)(Br)Br H298:-103.89 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)Br smiles:O=CC(Br)C(F)(F)Br H298:-126.04 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(F)(F)Br smiles:CC(O)(F)C(F)(F)Br H298:-212.15 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(Br)Br smiles:O=CC(Br)C(F)(Br)Br H298:-66.98 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)Br smiles:CC(F)C(F)(F)Br H298:-163.31 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)F smiles:O=CC(Br)C(F)(F)F H298:-189.47 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)OBr smiles:FC(Br)(Br)C(Br)OBr H298:-43.33 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)CBr smiles:FC(F)(F)C(Br)CBr H298:-167.97 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)(F)Br smiles:CC(O)(Br)C(F)(F)Br H298:-154.18 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)Br smiles:ClCC(Cl)(Cl)Br H298:-25.52 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)(Cl)Cl smiles:OC(Br)C(Cl)(Cl)Cl H298:-65.33 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)(Br)Br smiles:CC(Cl)C(Cl)(Br)Br H298:-21.88 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)(Cl)Br smiles:CC(Cl)C(Cl)(Cl)Br H298:-33.72 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Br)Br smiles:ClCC(Cl)(Br)Br H298:-13.65 kcal/mol
library:CHOClBr_G4 label:ClC(Br)(Br)CBr smiles:ClC(Br)(Br)CBr H298:-2.54 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)(Cl)Cl smiles:CC(Br)C(Cl)(Cl)Cl H298:-34.27 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)(Cl)Br smiles:CC(Br)C(Cl)(Cl)Br H298:-22.25 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Cl)CBr smiles:ClC(Cl)(Cl)CBr H298:-26.27 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)(Br)Br smiles:OC(Br)C(Cl)(Br)Br H298:-41.74 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)(Br)Br smiles:CC(Cl)C(Br)(Br)Br H298:-9.99 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)Br smiles:ClCC(Br)(Br)Br H298:-1.89 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)(Br)Br smiles:CC(Br)C(Cl)(Br)Br H298:-10.49 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Br)CBr smiles:ClC(Cl)(Br)CBr H298:-14.37 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)(Cl)Br smiles:OC(Br)C(Cl)(Cl)Br H298:-53.47 kcal/mol
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
        Cpdata = ([-0.194362,-0.291461,-0.257475,-0.230751,-0.195084,-0.109262,0.289278],'cal/(mol*K)','+|-',[0.137269,0.158695,0.162622,0.160438,0.139483,0.120455,0.0959263]),
        H298 = (5.51901,'kcal/mol','+|-',0.498479),
        S298 = (-0.572995,'cal/(mol*K)','+|-',0.323717),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,1,1,2-Tetrachloroethane smiles:ClCC(Cl)(Cl)Cl H298:-36.59 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)C(Cl)(Cl)Cl smiles:CC(Cl)(CCl)C(Cl)(Cl)Cl H298:-56.96 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.15 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-23.64 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)C(Cl)(Cl)Cl smiles:ClOOC(Cl)C(Cl)(Cl)Cl H298:-22.52 kcal/mol
library:CHOCl_G4 label:ClC(OC(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(OC(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-84.70 kcal/mol
library:CHOCl_G4 label:ClC(CC(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(CC(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-62.70 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-44.60 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)C(Cl)(Cl)Cl smiles:OC(Cl)(CCl)C(Cl)(Cl)Cl H298:-90.00 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(CCl)C(Cl)(Cl)Cl H298:-58.50 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-54.39 kcal/mol
library:CHOCl_G4 label:CCC(Cl)C(Cl)(Cl)Cl smiles:CCC(Cl)C(Cl)(Cl)Cl H298:-50.94 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-57.91 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-58.28 kcal/mol
library:CHOCl_G4 label:CC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-56.43 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-32.82 kcal/mol
library:CHOCl_G4 label:COC(Cl)C(Cl)(Cl)Cl smiles:COC(Cl)C(Cl)(Cl)Cl H298:-72.72 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-55.56 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-34.54 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-52.54 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-48.96 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)C(Cl)(Cl)Cl smiles:ClOCC(Cl)C(Cl)(Cl)Cl H298:-45.43 kcal/mol
library:CHOCl_G4 label:OC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-83.45 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-72.30 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=CC(Cl)C(Cl)(Cl)Cl H298:-31.12 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)C(Cl)(Cl)Cl smiles:C=CC(Cl)C(Cl)(Cl)Cl H298:-19.29 kcal/mol
library:CHOCl_G4 label:ClC(Cl)OC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)OC(Cl)C(Cl)(Cl)Cl H298:-84.49 kcal/mol
library:CHOCl_G4 label:OC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-86.10 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)C(Cl)(Cl)Cl smiles:ClCCC(Cl)C(Cl)(Cl)Cl H298:-57.47 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)C(Cl)(Cl)Cl H298:-39.03 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-29.53 kcal/mol
library:CHOCl_G4 label:CC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-50.56 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-88.64 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-54.92 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)C(Cl)(Cl)Cl H298:-45.71 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)C(Cl)(Cl)Cl smiles:C#CC(Cl)C(Cl)(Cl)Cl H298:25.96 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-50.55 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-60.27 kcal/mol
library:CHOCl_G4 label:CC(O)(Cl)C(Cl)(Cl)Cl smiles:CC(O)(Cl)C(Cl)(Cl)Cl H298:-88.39 kcal/mol
library:CHOCl_G4 label:OOC(Cl)C(Cl)(Cl)Cl smiles:OOC(Cl)C(Cl)(Cl)Cl H298:-55.74 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-46.21 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)C(Cl)(Cl)Cl H298:-77.53 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-86.00 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)C(Cl)(Cl)Cl smiles:O=CC(Cl)C(Cl)(Cl)Cl H298:-59.13 kcal/mol
library:CHOCl_G4 label:CC(C)(Cl)C(Cl)(Cl)Cl smiles:CC(C)(Cl)C(Cl)(Cl)Cl H298:-54.24 kcal/mol
library:CHOCl_G4 label:OCC(Cl)C(Cl)(Cl)Cl smiles:OCC(Cl)C(Cl)(Cl)Cl H298:-78.86 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-43.74 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)C(Cl)(Cl)Cl H298:-48.51 kcal/mol
library:CHOCl_G4 label:OC(O)(Cl)C(Cl)(Cl)Cl smiles:OC(O)(Cl)C(Cl)(Cl)Cl H298:-122.12 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)C(Cl)(Cl)Cl smiles:ClC=CC(Cl)C(Cl)(Cl)Cl H298:-26.50 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-62.52 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-48.72 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(OCl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(OCl)C(Cl)(Cl)Cl H298:-41.32 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)C(Cl)(Cl)Cl smiles:ClC#CC(Cl)C(Cl)(Cl)Cl H298:25.22 kcal/mol
library:CHOCl_G4 label:CC(Cl)(OCl)C(Cl)(Cl)Cl smiles:CC(Cl)(OCl)C(Cl)(Cl)Cl H298:-48.84 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)C(Cl)(Cl)Cl smiles:ClCOC(Cl)C(Cl)(Cl)Cl H298:-80.85 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-49.19 kcal/mol
library:CHOCl_G4 label:ClC(Cl)CC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)CC(Cl)C(Cl)(Cl)Cl H298:-62.56 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-40.31 kcal/mol
library:CHOCl_G4 label:OC(Cl)(OCl)C(Cl)(Cl)Cl smiles:OC(Cl)(OCl)C(Cl)(Cl)Cl H298:-83.16 kcal/mol
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
        Cpdata = ([0.0937782,0.243616,0.289448,0.268161,0.2066,0.170818,0.276392],'cal/(mol*K)','+|-',[0.128541,0.148604,0.152281,0.150236,0.130613,0.112796,0.0898265]),
        H298 = (6.65915,'kcal/mol','+|-',0.466781),
        S298 = (-0.130527,'cal/(mol*K)','+|-',0.303132),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:OOC(F)C(F)(F)F smiles:OOC(F)C(F)(F)F H298:-240.39 kcal/mol
library:CHOF_G4 label:FOCC(F)C(F)(F)F smiles:FOCC(F)C(F)(F)F H298:-231.40 kcal/mol
library:CHOF_G4 label:FOC(F)(OF)C(F)(F)F smiles:FOC(F)(OF)C(F)(F)F H298:-231.91 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)C(F)(F)F smiles:O=C(F)C(F)C(F)(F)F H298:-298.02 kcal/mol
library:CHOF_G4 label:FC(CC(F)(F)F)C(F)(F)F smiles:FC(CC(F)(F)F)C(F)(F)F H298:-386.97 kcal/mol
library:CHOF_G4 label:CC(O)(F)C(F)(F)F smiles:CC(O)(F)C(F)(F)F H298:-275.70 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)(F)F)C(F)(F)F smiles:FCC(F)(C(F)(F)F)C(F)(F)F H298:-421.30 kcal/mol
library:CHOF_G4 label:CC(F)(C(F)F)C(F)(F)F smiles:CC(F)(C(F)F)C(F)(F)F H298:-329.47 kcal/mol
library:CHOF_G4 label:CDCC(F)C(F)(F)F smiles:C=CC(F)C(F)(F)F H298:-199.52 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)(F)F smiles:FC(F)=C(F)C(F)C(F)(F)F H298:-327.95 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)(F)F smiles:FCC(F)(C(F)F)C(F)(F)F H298:-365.50 kcal/mol
library:CHOF_G4 label:FC(F)OC(F)C(F)(F)F smiles:FC(F)OC(F)C(F)(F)F H298:-362.98 kcal/mol
library:CHOF_G4 label:OC(F)(CF)C(F)(F)F smiles:OC(F)(CF)C(F)(F)F H298:-313.99 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)F smiles:FCC(F)C(F)(F)F H298:-266.99 kcal/mol
library:CHOF_G4 label:OC(F)(C(F)(F)F)C(F)(F)F smiles:OC(F)(C(F)(F)F)C(F)(F)F H298:-417.77 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)C(F)(F)F smiles:FOC(F)C(F)C(F)(F)F H298:-277.45 kcal/mol
library:CHOF_G4 label:FC(C(F)C(F)(F)F)C(F)(F)F smiles:FC(C(F)C(F)(F)F)C(F)(F)F H298:-424.07 kcal/mol
library:CHOF_G4 label:CC(F)(CF)C(F)(F)F smiles:CC(F)(CF)C(F)(F)F H298:-277.92 kcal/mol
library:CHOF_G4 label:FCOC(F)C(F)(F)F smiles:FCOC(F)C(F)(F)F H298:-307.20 kcal/mol
library:CHOF_G4 label:FOC(F)(C(F)F)C(F)(F)F smiles:FOC(F)(C(F)F)C(F)(F)F H298:-323.85 kcal/mol
library:CHOF_G4 label:CCC(F)C(F)(F)F smiles:CCC(F)C(F)(F)F H298:-232.32 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)C(F)(F)F smiles:FCC(F)C(F)C(F)(F)F H298:-317.77 kcal/mol
library:CHOF_G4 label:FC(C(F)(F)F)C(F)(F)C(F)(F)F smiles:FC(C(F)(F)F)C(F)(F)C(F)(F)F H298:-471.81 kcal/mol
library:CHOF_G4 label:FCC(F)(F)F smiles:FCC(F)(F)F H298:-217.08 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)C(F)(F)F smiles:FC(F)C(F)C(F)C(F)(F)F H298:-367.06 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(C(F)(F)F)C(F)(F)F smiles:FC(F)(F)C(F)(C(F)(F)F)C(F)(F)F H298:-523.90 kcal/mol
library:CHOF_G4 label:OC(F)(C(F)F)C(F)(F)F smiles:OC(F)(C(F)F)C(F)(F)F H298:-362.54 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)F smiles:CC(F)C(F)(F)F H298:-227.62 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)C(F)(F)F H298:-415.54 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)C(F)(F)F smiles:FCC(F)(OF)C(F)(F)F H298:-275.95 kcal/mol
library:CHOF_G4 label:C#CC(F)C(F)(F)F smiles:C#CC(F)C(F)(F)F H298:-153.93 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)C(F)(F)F smiles:CC(F)(F)C(F)C(F)(F)F H298:-329.68 kcal/mol
library:CHOF_G4 label:FC(F)CC(F)C(F)(F)F smiles:FC(F)CC(F)C(F)(F)F H298:-328.00 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)(F)F)C(F)(F)F H298:-469.60 kcal/mol
library:CHOF_G4 label:FC#CC(F)C(F)(F)F smiles:FC#CC(F)C(F)(F)F H298:-182.63 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)F smiles:FOC(F)C(F)(F)F H298:-226.58 kcal/mol
library:CHOF_G4 label:FC(C(F)(F)F)C(F)(F)F smiles:FC(C(F)(F)F)C(F)(F)F H298:-372.46 kcal/mol
library:CHOF_G4 label:FOC(F)(C(F)(F)F)C(F)(F)F smiles:FOC(F)(C(F)(F)F)C(F)(F)F H298:-377.83 kcal/mol
library:CHOF_G4 label:OC(F)(OF)C(F)(F)F smiles:OC(F)(OF)C(F)(F)F H298:-273.46 kcal/mol
library:CHOF_G4 label:CC(C)(F)C(F)(F)F smiles:CC(C)(F)C(F)(F)F H298:-238.61 kcal/mol
library:CHOF_G4 label:OC(F)C(F)C(F)(F)F smiles:OC(F)C(F)C(F)(F)F H298:-311.08 kcal/mol
library:CHOF_G4 label:OCC(F)C(F)(F)F smiles:OCC(F)C(F)(F)F H298:-261.39 kcal/mol
library:CHOF_G4 label:CC(F)(C(F)(F)F)C(F)(F)F smiles:CC(F)(C(F)(F)F)C(F)(F)F H298:-384.64 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)C(F)(F)F smiles:FCC(F)(F)C(F)C(F)(F)F H298:-368.56 kcal/mol
library:CHOF_G4 label:FOOC(F)C(F)(F)F smiles:FOOC(F)C(F)(F)F H298:-215.00 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)F smiles:OC(F)C(F)(F)F H298:-262.59 kcal/mol
library:CHOF_G4 label:ODCC(F)C(F)(F)F smiles:O=CC(F)C(F)(F)F H298:-237.65 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)(F)F smiles:FC=C(F)C(F)C(F)(F)F H298:-283.24 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)C(F)(F)F smiles:FCC(F)(CF)C(F)(F)F H298:-317.42 kcal/mol
library:CHOF_G4 label:FCDCC(F)C(F)(F)F smiles:FC=CC(F)C(F)(F)F H298:-244.66 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)C(F)(F)F smiles:FOC(F)(F)C(F)C(F)(F)F H298:-328.06 kcal/mol
library:CHOF_G4 label:CC(F)C(F)C(F)(F)F smiles:CC(F)C(F)C(F)(F)F H298:-276.26 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)F)C(F)(F)F H298:-414.90 kcal/mol
library:CHOF_G4 label:CC(F)(OF)C(F)(F)F smiles:CC(F)(OF)C(F)(F)F H298:-239.41 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)C(F)(F)F smiles:FC(F)=CC(F)C(F)(F)F H298:-293.32 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)C(F)(F)F smiles:C=C(F)C(F)C(F)(F)F H298:-243.94 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)C(F)(F)F smiles:OC(F)(F)C(F)C(F)(F)F H298:-367.83 kcal/mol
library:CHOF_G4 label:FC(OC(F)(F)F)C(F)(F)F smiles:FC(OC(F)(F)F)C(F)(F)F H298:-418.60 kcal/mol
library:CHOF_G4 label:FCCC(F)C(F)(F)F smiles:FCCC(F)C(F)(F)F H298:-276.55 kcal/mol
library:CHOF_G4 label:OC(O)(F)C(F)(F)F smiles:OC(O)(F)C(F)(F)F H298:-312.62 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)F smiles:FC(F)C(F)C(F)(F)F H298:-317.05 kcal/mol
library:CHOF_G4 label:COC(F)C(F)(F)F smiles:COC(F)C(F)(F)F H298:-257.28 kcal/mol
library:CHOFBr_G4 label:FC(CBr)C(F)(F)F smiles:FC(CBr)C(F)(F)F H298:-218.24 kcal/mol
library:CHOFBr_G4 label:FC(OBr)C(F)(F)F smiles:FC(OBr)C(F)(F)F H298:-220.61 kcal/mol
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
        Cpdata = ([-0.572672,-0.704004,-0.690757,-0.723155,-0.747859,-0.638443,-0.0153372],'cal/(mol*K)','+|-',[0.320784,0.370854,0.380031,0.374927,0.325957,0.281491,0.224169]),
        H298 = (3.45219,'kcal/mol','+|-',1.16489),
        S298 = (1.30002,'cal/(mol*K)','+|-',0.756491),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCC(Br)(Br)Br smiles:BrCC(Br)(Br)Br H298:9.20 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)(Br)Br smiles:OC(Br)C(Br)(Br)Br H298:-30.03 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)(Br)Br smiles:CC(Br)C(Br)(Br)Br H298:1.38 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)(Br)Br smiles:BrCC(Br)C(Br)(Br)Br H298:8.92 kcal/mol
library:CHOBr_G4 label:COC(Br)C(Br)(Br)Br smiles:COC(Br)C(Br)(Br)Br H298:-25.86 kcal/mol
library:CHOBr_G4 label:CCC(Br)C(Br)(Br)Br smiles:CCC(Br)C(Br)(Br)Br H298:-4.16 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C(Br)(Br)Br smiles:BrOC(Br)C(Br)(Br)Br H298:10.24 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)(Br)Br smiles:FCC(Br)C(Br)(Br)Br H298:-38.74 kcal/mol
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
        Cpdata = ([0.0702458,0.343881,0.372951,0.457198,0.379975,0.30518,0.350535],'cal/(mol*K)','+|-',[0.170409,0.197007,0.201882,0.199171,0.173157,0.149535,0.119085]),
        H298 = (4.30651,'kcal/mol','+|-',0.61882),
        S298 = (0.444126,'cal/(mol*K)','+|-',0.401868),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(F)C(F)(F)Cl smiles:C=C(F)C(F)(F)Cl H298:-142.24 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)(Cl)Cl smiles:C=C(F)C(F)(Cl)Cl H298:-95.11 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)(Cl)Cl smiles:C=C(F)C(Cl)(Cl)Cl H298:-50.75 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Br)Br smiles:C=C(F)C(Cl)(Br)Br H298:-27.26 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Cl)Br smiles:C=C(F)C(Cl)(Cl)Br H298:-38.99 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)(Cl)Br smiles:C=C(F)C(F)(Cl)Br H298:-82.65 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(Br)(Br)Br smiles:CC=C(F)C(Br)(Br)Br H298:-23.85 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)(Br)Br smiles:FC=C(F)C(Br)(Br)Br H298:-54.68 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)Br smiles:C=C(F)C(F)(Br)Br H298:-70.32 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)(Br)Br smiles:CC=C(Br)C(F)(Br)Br H298:-28.59 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(F)(F)Br smiles:CC=C(F)C(F)(F)Br H298:-137.22 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)Br smiles:OC=C(Br)C(F)(F)Br H298:-122.10 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)F smiles:OC=C(Br)C(F)(F)F H298:-186.37 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)(F)Br smiles:CC=C(Br)C(F)(F)Br H298:-87.63 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(F)Br smiles:FC=C(F)C(F)(F)Br H298:-167.75 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(F)(F)Br smiles:C=C=C(F)C(F)(F)Br H298:-89.62 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)(F)F smiles:O=C=C(Br)C(F)(F)F H298:-156.65 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)Br smiles:C=C(F)C(F)(F)Br H298:-128.95 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)Br smiles:C=C(F)C(Br)(Br)Br H298:-15.45 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)(F)Br smiles:O=C=C(Br)C(F)(F)Br H298:-93.23 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(Br)(Br)Br smiles:C=C=C(F)C(Br)(Br)Br H298:22.84 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)(F)F smiles:CC=C(Br)C(F)(F)F H298:-151.60 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(F)(Br)Br smiles:C=C=C(F)C(F)(Br)Br H298:-30.88 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(Br)Br smiles:FC=C(F)C(F)(Br)Br H298:-108.96 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)(Br)Br smiles:O=C=C(Br)C(F)(Br)Br H298:-34.38 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(F)(Br)Br smiles:CC=C(F)C(F)(Br)Br H298:-78.56 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(Br)Br smiles:OC=C(Br)C(F)(Br)Br H298:-62.92 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Br)Br smiles:C=C(Cl)C(Cl)(Br)Br H298:11.90 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Cl)Br smiles:C=C(Cl)C(Cl)(Cl)Br H298:0.09 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)(Br)Br smiles:C=C(Cl)C(Br)(Br)Br H298:23.73 kcal/mol
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
        Cpdata = ([-0.365877,-0.0702808,0.0772233,0.228614,0.285937,0.327136,0.494707],'cal/(mol*K)','+|-',[0.239131,0.276457,0.283298,0.279493,0.242988,0.20984,0.167109]),
        H298 = (3.33936,'kcal/mol','+|-',0.868379),
        S298 = (-0.550337,'cal/(mol*K)','+|-',0.563934),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-14.16 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)C(Cl)(Cl)Cl smiles:OC=C(Cl)C(Cl)(Cl)Cl H298:-55.01 kcal/mol
library:CHOCl_G4 label:ODCDC(Cl)C(Cl)(Cl)Cl smiles:O=C=C(Cl)C(Cl)(Cl)Cl H298:-25.26 kcal/mol
library:CHOCl_G4 label:ClCCDC(Cl)C(Cl)(Cl)Cl smiles:ClCC=C(Cl)C(Cl)(Cl)Cl H298:-24.15 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)Cl H298:-16.64 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-20.67 kcal/mol
library:CHOCl_G4 label:CDCDC(Cl)C(Cl)(Cl)Cl smiles:C=C=C(Cl)C(Cl)(Cl)Cl H298:24.00 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-13.38 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCDC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C=C(Cl)C(Cl)(Cl)Cl H298:17.15 kcal/mol
library:CHOCl_G4 label:CCDC(Cl)C(Cl)(Cl)Cl smiles:CC=C(Cl)C(Cl)(Cl)Cl H298:-20.73 kcal/mol
library:CHOCl_G4 label:ClOCDC(Cl)C(Cl)(Cl)Cl smiles:ClOC=C(Cl)C(Cl)(Cl)Cl H298:-13.09 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)(Cl)Cl H298:-11.78 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-23.53 kcal/mol
library:CHOCl_G4 label:ClCDCDC(Cl)C(Cl)(Cl)Cl smiles:ClC=C=C(Cl)C(Cl)(Cl)Cl H298:20.55 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-53.77 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-19.61 kcal/mol
library:CHOCl_G4 label:ClC(DCC(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(=CC(Cl)Cl)C(Cl)(Cl)Cl H298:-28.45 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)Cl H298:-26.83 kcal/mol
library:CHOCl_G4 label:ClC(DCC(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(=CC(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-26.55 kcal/mol
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
        Cpdata = ([-0.0676423,-0.0628733,-0.141765,-0.0820844,-0.100134,-0.078506,0.0420808],'cal/(mol*K)','+|-',[0.234253,0.270817,0.277519,0.273792,0.238031,0.20556,0.1637]),
        H298 = (5.85383,'kcal/mol','+|-',0.850665),
        S298 = (0.535576,'cal/(mol*K)','+|-',0.55243),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC(DCC(F)F)C(F)(F)F smiles:FC(=CC(F)F)C(F)(F)F H298:-293.36 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)(F)F smiles:FCC(F)=C(F)C(F)(F)F H298:-280.88 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)(F)F smiles:FC(=C(F)C(F)(F)F)C(F)(F)F H298:-382.97 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)F H298:-274.47 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)C(F)(F)F smiles:CC(F)=C(F)C(F)(F)F H298:-241.68 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)F smiles:FC=C(F)C(F)(F)F H298:-231.74 kcal/mol
library:CHOF_G4 label:FOCDC(F)C(F)(F)F smiles:FOC=C(F)C(F)(F)F H298:-194.83 kcal/mol
library:CHOF_G4 label:CCDC(F)C(F)(F)F smiles:CC=C(F)C(F)(F)F H298:-201.10 kcal/mol
library:CHOF_G4 label:FC(DCC(F)(F)F)C(F)(F)F smiles:FC(=CC(F)(F)F)C(F)(F)F H298:-349.10 kcal/mol
library:CHOF_G4 label:FCDCDC(F)C(F)(F)F smiles:FC=C=C(F)C(F)(F)F H298:-193.81 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)F smiles:FC(=C(F)C(F)(F)F)C(F)F H298:-329.07 kcal/mol
library:CHOF_G4 label:ODCDC(F)C(F)(F)F smiles:O=C=C(F)C(F)(F)F H298:-196.38 kcal/mol
library:CHOF_G4 label:FC(F)DCDC(F)C(F)(F)F smiles:FC(F)=C=C(F)C(F)(F)F H298:-240.00 kcal/mol
library:CHOF_G4 label:CDCDC(F)C(F)(F)F smiles:C=C=C(F)C(F)(F)F H298:-153.45 kcal/mol
library:CHOF_G4 label:FCCDC(F)C(F)(F)F smiles:FCC=C(F)C(F)(F)F H298:-241.52 kcal/mol
library:CHOF_G4 label:OCDC(F)C(F)(F)F smiles:OC=C(F)C(F)(F)F H298:-232.28 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)C(F)(F)F smiles:OC(F)=C(F)C(F)(F)F H298:-274.97 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)F smiles:C=C(F)C(F)(F)F H298:-192.87 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)C(F)(F)F smiles:FOC(F)=C(F)C(F)(F)F H298:-238.81 kcal/mol
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
        Cpdata = ([-0.402634,-0.100625,0.0951122,0.315772,0.459968,0.449552,0.266504],'cal/(mol*K)','+|-',[0.844426,0.97623,1.00039,0.986953,0.858043,0.740992,0.5901]),
        H298 = (3.53203,'kcal/mol','+|-',3.06644),
        S298 = (0.358881,'cal/(mol*K)','+|-',1.99138),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:FCDC(Br)C(Br)(Br)Br smiles:FC=C(Br)C(Br)(Br)Br H298:-6.70 kcal/mol
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
        Cpdata = ([-0.2777,-0.386945,-0.339974,-0.325207,-0.280704,-0.204638,0.0625393],'cal/(mol*K)','+|-',[0.0520868,0.0602169,0.061707,0.0608783,0.0529268,0.0457067,0.0363992]),
        H298 = (1.74778,'kcal/mol','+|-',0.189148),
        S298 = (0.70333,'cal/(mol*K)','+|-',0.122834),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CC(F)(Cl)C(Cl)Cl smiles:CC(F)(Cl)C(Cl)Cl H298:-90.93 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)C(F)F smiles:OC(F)(Cl)C(F)F H298:-212.52 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)C(F)Cl smiles:OC(Cl)(Cl)C(F)Cl H298:-120.90 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)C(F)F smiles:OC(Cl)(Cl)C(F)F H298:-166.26 kcal/mol
library:CHOFCl_G4 label:CC(F)(F)C(Cl)Cl smiles:CC(F)(F)C(Cl)Cl H298:-137.32 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)C(F)F smiles:CC(Cl)(Cl)C(F)F H298:-135.45 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)C(F)F smiles:CC(F)(Cl)C(F)F H298:-177.87 kcal/mol
library:CHOFCl_G4 label:FC(F)C(Cl)Cl smiles:FC(F)C(Cl)Cl H298:-124.24 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)C(F)Cl smiles:CC(Cl)(Cl)C(F)Cl H298:-89.91 kcal/mol
library:CHOFCl_G4 label:CC(F)(F)C(F)Cl smiles:CC(F)(F)C(F)Cl H298:-178.68 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)Cl smiles:FC(F)C(F)Cl H298:-165.25 kcal/mol
library:CHOFCl_G4 label:FC(Cl)C(Cl)Cl smiles:FC(Cl)C(Cl)Cl H298:-78.94 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)C(F)Cl smiles:CC(Cl)(Br)C(F)Cl H298:-78.12 kcal/mol
library:CHOFClBr_G4 label:OC(Br)(Br)C(F)Cl smiles:OC(Br)(Br)C(F)Cl H298:-96.32 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)Br smiles:FC(Cl)C(Cl)Br H298:-67.25 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)C(F)F smiles:CC(Cl)(Br)C(F)F H298:-123.51 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)Br smiles:FC(F)C(Cl)Br H298:-113.13 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)Br smiles:FC(Cl)C(Br)Br H298:-55.64 kcal/mol
library:CHOFClBr_G4 label:CC(F)(F)C(Cl)Br smiles:CC(F)(F)C(Cl)Br H298:-125.51 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(Br)Br smiles:CC(F)(Cl)C(Br)Br H298:-67.60 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(Cl)Br smiles:CC(F)(Cl)C(Cl)Br H298:-79.13 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)C(F)Cl smiles:OC(Cl)(Br)C(F)Cl H298:-108.56 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(F)Cl smiles:CC(Br)(Br)C(F)Cl H298:-66.32 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)C(F)F smiles:OC(Cl)(Br)C(F)F H298:-153.77 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(Br)Br smiles:FCC(F)(F)C(Br)Br H298:-152.86 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(F)C(Br)Br smiles:C=CC(F)(F)C(Br)Br H298:-85.23 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)Br smiles:CC(Br)(Br)C(F)Br H298:-53.83 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)C(F)F smiles:OOC(Br)(Br)C(F)F H298:-119.47 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)Br smiles:FC(F)C(F)Br H298:-152.51 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)C(F)F smiles:CCC(Br)(Br)C(F)F H298:-117.05 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)OBr smiles:FC(Br)C(Br)(Br)OBr H298:-43.95 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)C(F)Br smiles:COC(Br)(Br)C(F)Br H298:-81.88 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)Br smiles:O=CC(Br)(Br)C(F)Br H298:-67.14 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)Br smiles:CC(F)(Br)C(Br)Br H298:-55.06 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)F smiles:O=CC(Br)(Br)C(F)F H298:-124.59 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)Br smiles:FC(F)C(Br)Br H298:-100.98 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(O)(Br)Br smiles:CC(F)(F)C(O)(Br)Br H298:-154.37 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)F smiles:CC(F)(Br)C(F)F H298:-165.03 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)OBr smiles:FC(F)C(Br)(Br)OBr H298:-101.35 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)Br smiles:CC(F)(F)C(F)Br H298:-165.90 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)F smiles:OC(Br)(Br)C(F)F H298:-141.54 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(C)(Br)Br smiles:CC(F)(Br)C(C)(Br)Br H298:-64.71 kcal/mol
library:CHOFBr_G4 label:CCC(F)(F)C(Br)Br smiles:CCC(F)(F)C(Br)Br H298:-118.22 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)C(F)Br smiles:C#CC(F)(F)C(F)Br H298:-89.14 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(F)C(F)Br smiles:C=CC(F)(F)C(F)Br H298:-136.82 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)OBr smiles:FC(F)C(F)(Br)OBr H298:-157.78 kcal/mol
library:CHOFBr_G4 label:COC(F)(Br)C(F)F smiles:COC(F)(Br)C(F)F H298:-195.70 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)C(F)Br smiles:OOC(Br)(Br)C(F)Br H298:-62.14 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)C(F)F smiles:OCC(F)(Br)C(F)F H298:-198.73 kcal/mol
library:CHOFBr_G4 label:OOC(F)(Br)C(F)F smiles:OOC(F)(Br)C(F)F H298:-175.84 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)C(F)Br smiles:OCC(Br)(Br)C(F)Br H298:-90.13 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(C)(F)Br smiles:CC(F)(F)C(C)(F)Br H298:-177.99 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(C)(Br)Br smiles:CC(F)(F)C(C)(Br)Br H298:-123.98 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(F)Br smiles:FCC(F)(F)C(F)Br H298:-204.62 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(Br)C(Br)Br smiles:C#CC(F)(Br)C(Br)Br H298:19.72 kcal/mol
library:CHOFBr_G4 label:CCC(F)(F)C(F)Br smiles:CCC(F)(F)C(F)Br H298:-170.56 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)C(F)F smiles:CCC(F)(Br)C(F)F H298:-169.95 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(O)(F)Br smiles:OC(F)(F)C(O)(F)Br H298:-249.87 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)CBr smiles:FC(F)C(F)(Br)CBr H298:-154.76 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)C(Br)Br smiles:C#CC(F)(F)C(Br)Br H298:-37.78 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)F smiles:CC(Br)(Br)C(F)F H298:-111.74 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(O)(Br)Br smiles:OC(F)(Br)C(O)(Br)Br H298:-128.97 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)C(F)F smiles:O=CC(F)(Br)C(F)F H298:-174.91 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)CBr smiles:FC(F)C(Br)(Br)CBr H298:-103.69 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)C(Br)Br smiles:CCC(F)(Br)C(Br)Br H298:-60.35 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)F smiles:OC(F)(Br)C(F)F H298:-199.37 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(O)(Br)Br smiles:OC(F)(F)C(O)(Br)Br H298:-191.88 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(O)(F)Br smiles:CC(F)(F)C(O)(F)Br H298:-212.80 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)C(Br)Br smiles:FCC(F)(Br)C(Br)Br H298:-94.23 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)CBr smiles:FC(Br)C(Br)(Br)CBr H298:-46.80 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)Br smiles:CC(F)(F)C(Br)Br H298:-113.86 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)C(F)F smiles:OCC(Br)(Br)C(F)F H298:-147.74 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)Br smiles:FC(Br)C(Br)Br H298:-43.27 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(O)(Br)Br smiles:CC(F)(Br)C(O)(Br)Br H298:-95.12 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(Br)C(Br)Br smiles:C=CC(F)(Br)C(Br)Br H298:-27.62 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)C(F)Br smiles:CCC(Br)(Br)C(F)Br H298:-59.31 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)Br smiles:OC(Br)(Br)C(F)Br H298:-83.90 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)C(F)F smiles:COC(Br)(Br)C(F)F H298:-139.08 kcal/mol
library:CHOClBr_G4 label:ClC(Br)C(Br)Br smiles:ClC(Br)C(Br)Br H298:-3.21 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)Cl smiles:CC(Br)(Br)C(Cl)Cl H298:-24.27 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)C(Cl)Cl smiles:OC(Br)(Br)C(Cl)Cl H298:-55.04 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(Br)Br smiles:CC(Cl)(Br)C(Br)Br H298:-13.25 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)C(Cl)Cl smiles:OC(Cl)(Br)C(Cl)Cl H298:-67.29 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(Cl)Br smiles:CC(Cl)(Cl)C(Cl)Br H298:-36.59 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)C(Cl)Br smiles:OC(Br)(Br)C(Cl)Br H298:-43.47 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)Br smiles:ClC(Cl)C(Br)Br H298:-14.64 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)Br smiles:CC(Br)(Br)C(Cl)Br H298:-13.08 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)Br smiles:ClC(Cl)C(Cl)Br H298:-26.14 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(Br)Br smiles:CC(Cl)(Cl)C(Br)Br H298:-25.01 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(Cl)Cl smiles:CC(Cl)(Br)C(Cl)Cl H298:-36.43 kcal/mol
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
        Cpdata = ([-0.527114,-0.576967,-0.485559,-0.43689,-0.344702,-0.184195,0.266396],'cal/(mol*K)','+|-',[0.0676269,0.0781826,0.0801172,0.0790414,0.0687175,0.0593433,0.0472589]),
        H298 = (3.12995,'kcal/mol','+|-',0.24558),
        S298 = (-0.547171,'cal/(mol*K)','+|-',0.159482),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,1,2,2-Tetrachloroethane smiles:ClC(Cl)C(Cl)Cl H298:-37.36 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)(Cl)C(Cl)Cl smiles:ClC=CC(Cl)(Cl)C(Cl)Cl H298:-26.46 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(O)(Cl)Cl smiles:CC(Cl)(Cl)C(O)(Cl)Cl H298:-89.90 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)CCl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)CCl H298:-59.14 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)CCl smiles:OC(Cl)(Cl)C(Cl)(Cl)CCl H298:-91.46 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)Cl H298:-51.97 kcal/mol
library:CHOCl_G4 label:OCC(Cl)(Cl)C(Cl)Cl smiles:OCC(Cl)(Cl)C(Cl)Cl H298:-84.61 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)C(Cl)Cl smiles:O=CC(Cl)(Cl)C(Cl)Cl H298:-60.87 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)Cl H298:-79.68 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-85.64 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)CCl smiles:CC(Cl)(Cl)C(Cl)(Cl)CCl H298:-60.01 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-91.10 kcal/mol
library:CHOCl_G4 label:ClC(Cl)CC(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)CC(Cl)(Cl)C(Cl)Cl H298:-61.84 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)(Cl)C(Cl)Cl smiles:ClCOC(Cl)(Cl)C(Cl)Cl H298:-81.30 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-52.61 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)(Cl)C(Cl)Cl smiles:ClC#CC(Cl)(Cl)C(Cl)Cl H298:25.23 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-53.17 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-58.28 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.38 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)(Cl)C(Cl)Cl smiles:ClCCC(Cl)(Cl)C(Cl)Cl H298:-57.58 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-48.10 kcal/mol
library:CHOCl_G4 label:ClC(Cl)OC(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)OC(Cl)(Cl)C(Cl)Cl H298:-85.70 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)(Cl)C(Cl)Cl smiles:C=CC(Cl)(Cl)C(Cl)Cl H298:-20.40 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCC(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)=CC(Cl)(Cl)C(Cl)Cl H298:-28.52 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-74.08 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-60.78 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-47.42 kcal/mol
library:CHOCl_G4 label:OOC(Cl)(Cl)C(Cl)Cl smiles:OOC(Cl)(Cl)C(Cl)Cl H298:-58.15 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(O)(Cl)Cl smiles:OC(Cl)(Cl)C(O)(Cl)Cl H298:-120.57 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:CC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-60.47 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClOC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-54.08 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)(Cl)C(Cl)Cl smiles:C#CC(Cl)(Cl)C(Cl)Cl H298:26.11 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)Cl H298:-48.28 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:OC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-91.30 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-31.97 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)Cl H298:-41.44 kcal/mol
library:CHOCl_G4 label:COC(Cl)(Cl)C(Cl)Cl smiles:COC(Cl)(Cl)C(Cl)Cl H298:-76.75 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-52.65 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-28.26 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)CC(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)CC(Cl)(Cl)Cl H298:-60.05 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)(Cl)C(Cl)Cl smiles:ClOCC(Cl)(Cl)C(Cl)Cl H298:-48.01 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(C)(Cl)Cl smiles:CC(Cl)(Cl)C(C)(Cl)Cl H298:-58.12 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-53.42 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)OC(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)OC(Cl)(Cl)Cl H298:-82.28 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-58.19 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:C=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-26.81 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)(Cl)C(Cl)Cl smiles:ClOOC(Cl)(Cl)C(Cl)Cl H298:-23.90 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-59.48 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)OCl smiles:CC(Cl)(Cl)C(Cl)(Cl)OCl H298:-51.88 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)OCl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)OCl H298:-44.07 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-59.49 kcal/mol
library:CHOCl_G4 label:CCC(Cl)(Cl)C(Cl)Cl smiles:CCC(Cl)(Cl)C(Cl)Cl H298:-53.46 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-46.43 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)OCl smiles:OC(Cl)(Cl)C(Cl)(Cl)OCl H298:-82.43 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)OCl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)OCl H298:-53.35 kcal/mol
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
        Cpdata = ([-0.291347,-0.32088,-0.229666,-0.189519,-0.170356,-0.110933,0.13427],'cal/(mol*K)','+|-',[0.0626262,0.0724013,0.0741929,0.0731966,0.0636361,0.0549551,0.0437643]),
        H298 = (3.72107,'kcal/mol','+|-',0.22742),
        S298 = (0.504173,'cal/(mol*K)','+|-',0.147689),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC(F)C(F)(F)C(F)F smiles:FC(F)C(F)(F)C(F)F H298:-310.56 kcal/mol
library:CHOF_G4 label:COC(F)(F)C(F)F smiles:COC(F)(F)C(F)F H298:-257.07 kcal/mol
library:CHOF_G4 label:FCCC(F)(F)C(F)F smiles:FCCC(F)(F)C(F)F H298:-270.86 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)C(F)F smiles:OC(F)(F)C(F)(F)C(F)F H298:-361.43 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)C(F)F smiles:C=C(F)C(F)(F)C(F)F H298:-237.67 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)(F)C(F)F smiles:FC(F)=CC(F)(F)C(F)F H298:-286.35 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(O)(F)F smiles:OC(F)(F)C(O)(F)F H298:-312.96 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)C(F)(F)F smiles:OC(F)(F)C(F)(F)C(F)(F)F H298:-416.21 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)C(F)F smiles:CC(F)C(F)(F)C(F)F H298:-272.41 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)C(F)F smiles:FOC(F)(F)C(F)(F)C(F)F H298:-320.53 kcal/mol
library:CHOF_G4 label:FCDCC(F)(F)C(F)F smiles:FC=CC(F)(F)C(F)F H298:-239.21 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)OF smiles:OC(F)(F)C(F)(F)OF H298:-272.97 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)F smiles:FC=C(F)C(F)(F)C(F)F H298:-276.56 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)C(F)F smiles:O=CC(F)(F)C(F)F H298:-230.22 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)C(F)(F)F smiles:FCC(F)(F)C(F)(F)C(F)(F)F H298:-415.15 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)CF smiles:OC(F)(F)C(F)(F)CF H298:-312.63 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)F smiles:OC(F)(F)C(F)F H298:-261.64 kcal/mol
library:CHOF_G4 label:FOOC(F)(F)C(F)F smiles:FOOC(F)(F)C(F)F H298:-209.86 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)(F)C(F)(F)C(F)(F)C(F)(F)F H298:-518.11 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)C(F)F smiles:FCC(F)(F)C(F)(F)C(F)F H298:-360.16 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)CF smiles:CC(F)(F)C(F)(F)CF H298:-275.08 kcal/mol
library:CHOF_G4 label:OCC(F)(F)C(F)F smiles:OCC(F)(F)C(F)F H298:-256.28 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)C(F)F smiles:OC(F)C(F)(F)C(F)F H298:-306.17 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)OF smiles:CC(F)(F)C(F)(F)OF H298:-236.01 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)F smiles:FOC(F)(F)C(F)F H298:-221.86 kcal/mol
library:CHOF_G4 label:FC#CC(F)(F)C(F)F smiles:FC#CC(F)(F)C(F)F H298:-175.86 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)C(F)(F)F H298:-415.54 kcal/mol
library:CHOF_G4 label:FC(F)CC(F)(F)C(F)F smiles:FC(F)CC(F)(F)C(F)F H298:-323.47 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)C(F)F smiles:CC(F)(F)C(F)(F)C(F)F H298:-323.72 kcal/mol
library:CHOF_G4 label:C#CC(F)(F)C(F)F smiles:C#CC(F)(F)C(F)F H298:-146.79 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(C)(F)F smiles:CC(F)(F)C(C)(F)F H298:-237.65 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)C(F)F smiles:FC(F)C(F)(F)C(F)(F)C(F)F H298:-409.06 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)F smiles:CC(F)(F)C(F)F H298:-224.09 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)C(F)(F)F smiles:CC(F)(F)C(F)(F)C(F)(F)F H298:-378.68 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)C(F)F smiles:FC(F)C(F)C(F)(F)C(F)F H298:-360.28 kcal/mol
library:CHOF_G4 label:FC(F)C(F)F smiles:FC(F)C(F)F H298:-210.35 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)(F)C(F)(F)F H298:-463.90 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)C(F)F smiles:FCC(F)C(F)(F)C(F)F H298:-310.46 kcal/mol
library:CHOF_G4 label:CCC(F)(F)C(F)F smiles:CCC(F)(F)C(F)F H298:-228.59 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)(F)F H298:-365.14 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)C(F)(F)F smiles:FOC(F)(F)C(F)(F)C(F)(F)F H298:-375.57 kcal/mol
library:CHOF_G4 label:FCOC(F)(F)C(F)F smiles:FCOC(F)(F)C(F)F H298:-304.58 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)OF smiles:FOC(F)(F)C(F)(F)OF H298:-232.32 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)C(F)F smiles:FOC(F)C(F)(F)C(F)F H298:-270.79 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)F smiles:FCC(F)(F)C(F)F H298:-261.57 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)OF smiles:FCC(F)(F)C(F)(F)OF H298:-272.22 kcal/mol
library:CHOF_G4 label:FC(F)OC(F)(F)C(F)F smiles:FC(F)OC(F)(F)C(F)F H298:-359.38 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)OC(F)(F)F smiles:FC(F)C(F)(F)OC(F)(F)F H298:-413.83 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)F smiles:FC(F)=C(F)C(F)(F)C(F)F H298:-319.55 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)CF smiles:FCC(F)(F)C(F)(F)CF H298:-312.03 kcal/mol
library:CHOF_G4 label:CDCC(F)(F)C(F)F smiles:C=CC(F)(F)C(F)F H298:-194.71 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)CC(F)(F)F smiles:FC(F)C(F)(F)CC(F)(F)F H298:-380.59 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)C(F)F smiles:O=C(F)C(F)(F)C(F)F H298:-289.49 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(O)(F)F smiles:CC(F)(F)C(O)(F)F H298:-275.21 kcal/mol
library:CHOF_G4 label:FOCC(F)(F)C(F)F smiles:FOCC(F)(F)C(F)F H298:-225.15 kcal/mol
library:CHOF_G4 label:OOC(F)(F)C(F)F smiles:OOC(F)(F)C(F)F H298:-236.81 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)CBr smiles:FC(F)C(F)(F)CBr H298:-213.12 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)OBr smiles:FC(F)C(F)(F)OBr H298:-219.13 kcal/mol
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
        Cpdata = ([-0.637284,-0.724389,-0.657829,-0.613011,-0.50289,-0.375698,-0.0698224],'cal/(mol*K)','+|-',[0.164456,0.190125,0.19483,0.192214,0.167108,0.144312,0.114925]),
        H298 = (1.61277,'kcal/mol','+|-',0.597204),
        S298 = (0.784825,'cal/(mol*K)','+|-',0.38783),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrOC(Br)(Br)C(Br)Br smiles:BrOC(Br)(Br)C(Br)Br H298:7.56 kcal/mol
library:CHOBr_G4 label:CCC(Br)(Br)C(Br)Br smiles:CCC(Br)(Br)C(Br)Br H298:-7.38 kcal/mol
library:CHOBr_G4 label:COC(Br)(Br)C(Br)Br smiles:COC(Br)(Br)C(Br)Br H298:-29.78 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(Br)Br smiles:CC(Br)(Br)C(Br)Br H298:-1.08 kcal/mol
library:CHOBr_G4 label:OC(Br)(Br)C(Br)Br smiles:OC(Br)(Br)C(Br)Br H298:-31.92 kcal/mol
library:CHOBr_G4 label:BrC(Br)C(Br)Br smiles:BrC(Br)C(Br)Br H298:8.19 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)C(Br)Br smiles:FCC(Br)(Br)C(Br)Br H298:-43.39 kcal/mol
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
        Cpdata = ([-0.335673,-0.254206,-0.139475,-0.108407,-0.0767123,-0.012783,0.228327],'cal/(mol*K)','+|-',[0.0560007,0.0647417,0.0663438,0.0654529,0.0569038,0.0491412,0.0391343]),
        H298 = (2.34495,'kcal/mol','+|-',0.203361),
        S298 = (0.351241,'cal/(mol*K)','+|-',0.132064),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CC(F)C(F)Cl smiles:CC(F)C(F)Cl H298:-124.13 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)(Cl)CF smiles:CCC(Cl)(Cl)CF H298:-89.51 kcal/mol
library:CHOFCl_G4 label:CC(C)(F)C(Cl)Cl smiles:CC(C)(F)C(Cl)Cl H298:-93.69 kcal/mol
library:CHOFCl_G4 label:OC(O)(Cl)C(F)F smiles:OC(O)(Cl)C(F)F H298:-207.81 kcal/mol
library:CHOFCl_G4 label:FC(F)C(Cl)OCl smiles:FC(F)C(Cl)OCl H298:-123.69 kcal/mol
library:CHOFCl_G4 label:CDCC(F)(F)CCl smiles:C=CC(F)(F)CCl H298:-105.69 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)(Cl)CCl smiles:FCC(Cl)(Cl)CCl H298:-87.81 kcal/mol
library:CHOFCl_G4 label:C#CC(F)C(Cl)Cl smiles:C#CC(F)C(Cl)Cl H298:-10.91 kcal/mol
library:CHOFCl_G4 label:CCC(F)C(F)Cl smiles:CCC(F)C(F)Cl H298:-128.90 kcal/mol
library:CHOFCl_G4 label:CCC(F)C(Cl)Cl smiles:CCC(F)C(Cl)Cl H298:-88.02 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)C(F)F smiles:OCC(Cl)C(F)F H298:-165.42 kcal/mol
library:CHOFCl_G4 label:CC(C)(Cl)C(F)Cl smiles:CC(C)(Cl)C(F)Cl H298:-94.67 kcal/mol
library:CHOFCl_G4 label:OC(F)C(O)(Cl)Cl smiles:OC(F)C(O)(Cl)Cl H298:-162.82 kcal/mol
library:CHOFCl_G4 label:CC(C)(F)C(F)Cl smiles:CC(C)(F)C(F)Cl H298:-134.90 kcal/mol
library:CHOFCl_G4 label:CCC(F)(Cl)CF smiles:CCC(F)(Cl)CF H298:-130.66 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)C(F)Cl smiles:CCC(Cl)C(F)Cl H298:-90.41 kcal/mol
library:CHOFCl_G4 label:CC(F)(F)C(O)Cl smiles:CC(F)(F)C(O)Cl H298:-174.42 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)CF smiles:CC(F)(Cl)CF H298:-126.63 kcal/mol
library:CHOFCl_G4 label:FCC(F)(F)CCl smiles:FCC(F)(F)CCl H298:-174.61 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)C(F)Cl smiles:O=CC(Cl)C(F)Cl H298:-98.16 kcal/mol
library:CHOFCl_G4 label:CC(C)(Cl)C(F)F smiles:CC(C)(Cl)C(F)F H298:-140.33 kcal/mol
library:CHOFCl_G4 label:CCC(F)(Cl)CCl smiles:CCC(F)(Cl)CCl H298:-93.40 kcal/mol
library:CHOFCl_G4 label:OC(F)C(O)(F)Cl smiles:OC(F)C(O)(F)Cl H298:-208.78 kcal/mol
library:CHOFCl_G4 label:C#CC(F)(Cl)CCl smiles:C#CC(F)(Cl)CCl H298:-13.43 kcal/mol
library:CHOFCl_G4 label:FCC(F)(Cl)OCl smiles:FCC(F)(Cl)OCl H298:-123.20 kcal/mol
library:CHOFCl_G4 label:CC(F)(F)CCl smiles:CC(F)(F)CCl H298:-134.69 kcal/mol
library:CHOFCl_G4 label:FC(Cl)C(Cl)OCl smiles:FC(Cl)C(Cl)OCl H298:-78.73 kcal/mol
library:CHOFCl_G4 label:CCC(F)(F)CCl smiles:CCC(F)(F)CCl H298:-139.59 kcal/mol
library:CHOFCl_G4 label:COC(Cl)(Cl)CF smiles:COC(Cl)(Cl)CF H298:-112.89 kcal/mol
library:CHOFCl_G4 label:CDCC(F)C(F)Cl smiles:C=CC(F)C(F)Cl H298:-97.08 kcal/mol
library:CHOFCl_G4 label:CC(O)(F)C(Cl)Cl smiles:CC(O)(F)C(Cl)Cl H298:-132.55 kcal/mol
library:CHOFCl_G4 label:COC(Cl)C(F)Cl smiles:COC(Cl)C(F)Cl H298:-112.38 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)F smiles:CC(Cl)C(F)F H298:-130.64 kcal/mol
library:CHOFCl_G4 label:CC(F)C(C)(Cl)Cl smiles:CC(F)C(C)(Cl)Cl H298:-93.79 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)C(F)F smiles:CCC(Cl)C(F)F H298:-135.58 kcal/mol
library:CHOFCl_G4 label:FCC(F)C(F)Cl smiles:FCC(F)C(F)Cl H298:-165.30 kcal/mol
library:CHOFCl_G4 label:CC(O)(Cl)C(F)Cl smiles:CC(O)(Cl)C(F)Cl H298:-128.65 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(C)(F)F smiles:CC(Cl)C(C)(F)F H298:-143.16 kcal/mol
library:CHOFCl_G4 label:OCC(F)(Cl)CF smiles:OCC(F)(Cl)CF H298:-161.64 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)(Cl)CF smiles:O=CC(Cl)(Cl)CF H298:-96.67 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(O)(F)Cl smiles:OC(Cl)C(O)(F)Cl H298:-164.56 kcal/mol
library:CHOFCl_G4 label:COC(F)(Cl)CF smiles:COC(F)(Cl)CF H298:-158.28 kcal/mol
library:CHOFCl_G4 label:FC(F)CCl smiles:FC(F)CCl H298:-121.98 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)C(F)Cl smiles:OCC(Cl)C(F)Cl H298:-120.20 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)CCl smiles:CC(F)(Cl)CCl H298:-88.49 kcal/mol
library:CHOFCl_G4 label:CC(O)(F)C(F)Cl smiles:CC(O)(F)C(F)Cl H298:-173.89 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)C(F)F smiles:O=CC(Cl)C(F)F H298:-143.65 kcal/mol
library:CHOFCl_G4 label:OC(F)(Cl)CF smiles:OC(F)(Cl)CF H298:-162.48 kcal/mol
library:CHOFCl_G4 label:CDCC(F)C(Cl)Cl smiles:C=CC(F)C(Cl)Cl H298:-55.86 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(Cl)CF smiles:OC(Cl)(Cl)CF H298:-116.05 kcal/mol
library:CHOFCl_G4 label:OC(O)(Cl)C(F)Cl smiles:OC(O)(Cl)C(F)Cl H298:-162.65 kcal/mol
library:CHOFCl_G4 label:C#CC(F)(F)CCl smiles:C#CC(F)(F)CCl H298:-58.95 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)Cl smiles:FCC(Cl)Cl H298:-73.24 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)Cl smiles:OC(Cl)C(F)Cl H298:-117.21 kcal/mol
library:CHOFCl_G4 label:FC(Cl)C(Cl)CCl smiles:FC(Cl)C(Cl)CCl H298:-88.88 kcal/mol
library:CHOFCl_G4 label:FCC(F)(Cl)CCl smiles:FCC(F)(Cl)CCl H298:-129.46 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)C(O)Cl smiles:CC(F)(Cl)C(O)Cl H298:-128.98 kcal/mol
library:CHOFCl_G4 label:CC(F)C(O)(F)Cl smiles:CC(F)C(O)(F)Cl H298:-172.88 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)(Cl)CF smiles:OCC(Cl)(Cl)CF H298:-120.28 kcal/mol
library:CHOFCl_G4 label:CC(F)C(O)(Cl)Cl smiles:CC(F)C(O)(Cl)Cl H298:-126.33 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(Cl)CF smiles:CC(Cl)(Cl)CF H298:-84.12 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)F smiles:OC(Cl)C(F)F H298:-161.64 kcal/mol
library:CHOFCl_G4 label:FCC(F)Cl smiles:FCC(F)Cl H298:-114.61 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(C)(F)Cl smiles:CC(Cl)C(C)(F)Cl H298:-96.89 kcal/mol
library:CHOFCl_G4 label:CDCC(F)(Cl)CCl smiles:C=CC(F)(Cl)CCl H298:-60.32 kcal/mol
library:CHOFCl_G4 label:C#CC(F)C(F)Cl smiles:C#CC(F)C(F)Cl H298:-51.95 kcal/mol
library:CHOFCl_G4 label:ODCC(F)(Cl)CF smiles:O=CC(F)(Cl)CF H298:-137.80 kcal/mol
library:CHOFCl_G4 label:CC(F)C(Cl)Cl smiles:CC(F)C(Cl)Cl H298:-83.20 kcal/mol
library:CHOFCl_G4 label:COC(Cl)C(F)F smiles:COC(Cl)C(F)F H298:-157.57 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)(Cl)OCl smiles:FCC(Cl)(Cl)OCl H298:-78.14 kcal/mol
library:CHOFCl_G4 label:FCC(F)C(Cl)Cl smiles:FCC(F)C(Cl)Cl H298:-124.19 kcal/mol
library:CHOFCl_G4 label:FC(F)C(Cl)CCl smiles:FC(F)C(Cl)CCl H298:-133.87 kcal/mol
library:CHOFCl_G4 label:CC(O)(Cl)C(F)F smiles:CC(O)(Cl)C(F)F H298:-173.37 kcal/mol
library:CHOFCl_G4 label:CC(F)C(C)(F)Cl smiles:CC(F)C(C)(F)Cl H298:-136.28 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(O)(F)F smiles:OC(Cl)C(O)(F)F H298:-213.67 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)Cl smiles:CC(Cl)C(F)Cl H298:-85.33 kcal/mol
library:CHOFCl_G4 label:FC(Cl)CCl smiles:FC(Cl)CCl H298:-76.78 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)CBr smiles:FC(Cl)CBr H298:-65.70 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)CBr smiles:FC(F)C(Cl)CBr H298:-122.76 kcal/mol
library:CHOFClBr_G4 label:FCC(F)C(Cl)Br smiles:FCC(F)C(Cl)Br H298:-112.51 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Cl)OBr smiles:FCC(Cl)(Cl)OBr H298:-76.00 kcal/mol
library:CHOFClBr_G4 label:ODCC(Cl)(Br)CF smiles:O=CC(Cl)(Br)CF H298:-85.48 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)Cl smiles:OC(Br)C(F)Cl H298:-105.09 kcal/mol
library:CHOFClBr_G4 label:OC(O)(Br)C(F)Cl smiles:OC(O)(Br)C(F)Cl H298:-149.98 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)Br smiles:CC(F)C(Cl)Br H298:-71.48 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)(Cl)CBr smiles:C=CC(F)(Cl)CBr H298:-49.32 kcal/mol
library:CHOFClBr_G4 label:OCC(Br)C(F)Cl smiles:OCC(Br)C(F)Cl H298:-108.96 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)CBr smiles:FC(Cl)C(Br)CBr H298:-66.74 kcal/mol
library:CHOFClBr_G4 label:COC(Cl)(Br)CF smiles:COC(Cl)(Br)CF H298:-103.51 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(O)(Cl)Br smiles:CC(F)C(O)(Cl)Br H298:-113.92 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(O)Br smiles:CC(F)(Cl)C(O)Br H298:-116.74 kcal/mol
library:CHOFClBr_G4 label:FCC(F)(Cl)CBr smiles:FCC(F)(Cl)CBr H298:-118.29 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)Cl smiles:CC(Br)C(F)Cl H298:-73.93 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)CBr smiles:FC(Cl)C(Cl)CBr H298:-77.50 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)Br smiles:FCC(Cl)Br H298:-61.59 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Br)OBr smiles:FCC(Cl)(Br)OBr H298:-63.64 kcal/mol
library:CHOFClBr_G4 label:CCC(Cl)(Br)CF smiles:CCC(Cl)(Br)CF H298:-77.31 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)C(Cl)Br smiles:C=CC(F)C(Cl)Br H298:-44.24 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)CBr smiles:CC(F)(Cl)CBr H298:-77.35 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(C)(F)Cl smiles:CC(Br)C(C)(F)Cl H298:-85.18 kcal/mol
library:CHOFClBr_G4 label:CCC(Br)C(F)Cl smiles:CCC(Br)C(F)Cl H298:-79.23 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(C)(Cl)Br smiles:CC(F)C(C)(Cl)Br H298:-81.86 kcal/mol
library:CHOFClBr_G4 label:CC(C)(Br)C(F)Cl smiles:CC(C)(Br)C(F)Cl H298:-83.18 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Br)CBr smiles:FCC(Cl)(Br)CBr H298:-65.13 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)CF smiles:CC(Cl)(Br)CF H298:-72.30 kcal/mol
library:CHOFClBr_G4 label:CC(O)(F)C(Cl)Br smiles:CC(O)(F)C(Cl)Br H298:-120.87 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)OBr smiles:FC(Cl)C(Cl)OBr H298:-76.25 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Cl)Br smiles:FCC(Cl)C(Cl)Br H298:-73.02 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)(Cl)CBr smiles:C#CC(F)(Cl)CBr H298:-2.40 kcal/mol
library:CHOFClBr_G4 label:FCC(F)(Cl)OBr smiles:FCC(F)(Cl)OBr H298:-121.18 kcal/mol
library:CHOFClBr_G4 label:CCC(F)(Cl)CBr smiles:CCC(F)(Cl)CBr H298:-83.10 kcal/mol
library:CHOFClBr_G4 label:CC(O)(Br)C(F)Cl smiles:CC(O)(Br)C(F)Cl H298:-116.39 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)OBr smiles:FC(Cl)C(Br)OBr H298:-64.02 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(O)(F)Cl smiles:OC(Br)C(O)(F)Cl H298:-152.61 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Br)Br smiles:FCC(Cl)C(Br)Br H298:-61.63 kcal/mol
library:CHOFClBr_G4 label:COC(Br)C(F)Cl smiles:COC(Br)C(F)Cl H298:-100.55 kcal/mol
library:CHOFClBr_G4 label:OC(F)C(O)(Cl)Br smiles:OC(F)C(O)(Cl)Br H298:-150.25 kcal/mol
library:CHOFClBr_G4 label:OCC(Cl)(Br)CF smiles:OCC(Cl)(Br)CF H298:-108.72 kcal/mol
library:CHOFClBr_G4 label:CCC(F)C(Cl)Br smiles:CCC(F)C(Cl)Br H298:-76.43 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)C(Cl)Br smiles:C#CC(F)C(Cl)Br H298:0.76 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Cl)CBr smiles:FCC(Cl)(Cl)CBr H298:-76.68 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)OBr smiles:FC(F)C(Cl)OBr H298:-121.34 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)CF smiles:OC(Cl)(Br)CF H298:-103.49 kcal/mol
library:CHOFClBr_G4 label:CC(C)(F)C(Cl)Br smiles:CC(C)(F)C(Cl)Br H298:-81.93 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)C(F)Cl smiles:O=CC(Br)C(F)Cl H298:-87.91 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CBr smiles:CC(F)(Br)CBr H298:-64.96 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)CF smiles:OC(Br)C(F)(Br)CF H298:-144.70 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)CBr smiles:FCC(Br)(Br)CBr H298:-53.62 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)Br smiles:O=CC(Br)C(F)Br H298:-75.47 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)CF smiles:OC(Br)C(Br)(Br)CF H298:-92.64 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)CBr smiles:FC(F)C(F)(F)CBr H298:-213.12 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(Br)Br smiles:C=CC(F)C(Br)Br H298:-32.65 kcal/mol
library:CHOFBr_G4 label:OC(Br)(OBr)C(F)F smiles:OC(Br)(OBr)C(F)F H298:-153.83 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)Br smiles:O=C(Br)C(Br)C(F)Br H298:-77.95 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)CBr smiles:CC(F)(Br)C(Br)CBr H298:-65.55 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(Br)OBr smiles:CC(F)C(F)(Br)OBr H298:-118.71 kcal/mol
library:CHOFBr_G4 label:CC(F)C(C)(F)Br smiles:CC(F)C(C)(F)Br H298:-123.48 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)OBr smiles:FC(Br)C(Br)OBr H298:-51.50 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)OF smiles:OC(Br)C(F)(Br)OF H298:-103.26 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)CF smiles:CC(Br)(Br)CF H298:-60.51 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)F smiles:OOC(Br)C(F)F H298:-128.46 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)CBr smiles:CC(F)C(F)(F)CBr H298:-174.01 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)F smiles:O=CC(Br)C(F)F H298:-132.48 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)CF smiles:OCC(F)(Br)CF H298:-149.23 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)OBr smiles:CC(F)C(Br)(Br)OBr H298:-61.52 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)CF smiles:CC(F)(Br)C(F)CF H298:-164.23 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(O)(F)F smiles:OC(Br)C(O)(F)F H298:-201.02 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)(F)CBr smiles:FC#CC(F)(F)CBr H298:-76.81 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(F)Br smiles:C#CC(F)C(F)Br H298:-39.18 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)F smiles:OC(Br)(CBr)C(F)F H298:-153.48 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)Br smiles:COC(Br)C(F)Br H298:-87.55 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)Br smiles:CC(F)(CBr)C(F)Br H298:-114.70 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(Br)Br smiles:CC(F)(CBr)C(Br)Br H298:-62.22 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)COBr smiles:FC(F)C(Br)COBr H298:-116.13 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)C(Br)Br smiles:FC#CC(F)C(Br)Br H298:-16.74 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(F)Br smiles:OC(F)(CF)C(F)Br H298:-202.42 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)OOBr smiles:FC(F)C(Br)OOBr H298:-91.97 kcal/mol
library:CHOFBr_G4 label:FCC(F)Br smiles:FCC(F)Br H298:-102.10 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)C(Br)Br smiles:FCC(Br)(Br)C(Br)Br H298:-43.39 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(O)(F)Br smiles:OC(Br)C(O)(F)Br H298:-139.52 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)OCBr smiles:FC(Br)C(Br)OCBr H298:-90.48 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)Br smiles:CC(O)(Br)C(F)Br H298:-103.87 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)CF smiles:OOC(Br)(Br)CF H298:-70.17 kcal/mol
library:CHOFBr_G4 label:FCC(Br)Br smiles:FCC(Br)Br H298:-49.98 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)CF smiles:CC(Br)(Br)C(F)CF H298:-110.91 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(Br)Br smiles:OC(F)(CF)C(Br)Br H298:-148.20 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)CBr smiles:FCC(F)(Br)CBr H298:-105.78 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)CCBr smiles:FC(Br)C(Br)CCBr H298:-62.78 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)OCBr smiles:FCC(F)(Br)OCBr H298:-137.93 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(Br)CBr smiles:C=CC(F)(Br)CBr H298:-37.48 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)CCBr smiles:FCC(F)(Br)CCBr H298:-112.88 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)F smiles:CC(Br)C(Br)C(F)F H298:-120.51 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(F)Br smiles:FC(F)C(F)C(F)Br H298:-203.52 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)OOBr smiles:FCC(Br)(Br)OOBr H298:-33.42 kcal/mol
library:CHOFBr_G4 label:CC(F)C(O)(F)Br smiles:CC(F)C(O)(F)Br H298:-159.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)CF smiles:OC(Br)(Br)CF H298:-91.35 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)OBr smiles:CC(F)(F)C(Br)OBr H298:-122.95 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)F smiles:COC(Br)C(F)F H298:-145.68 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)Br smiles:CC(F)C(Br)Br H298:-59.98 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)CF smiles:CC(Br)C(F)(F)CF H298:-170.21 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)CF smiles:CCC(F)(Br)CF H298:-117.86 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(F)Br smiles:CC(F)C(F)C(F)Br H298:-163.01 kcal/mol
library:CHOFBr_G4 label:CC(F)C(O)(Br)Br smiles:CC(F)C(O)(Br)Br H298:-101.58 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CF smiles:CC(F)(Br)CF H298:-114.06 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)F smiles:OC(Br)C(F)F H298:-149.47 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)CBr smiles:C#CC(F)(F)CBr H298:-47.89 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)CBr smiles:FC(F)C(Br)CBr H298:-111.49 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)C(F)Br smiles:FC#CC(F)C(F)Br H298:-67.70 kcal/mol
library:CHOFBr_G4 label:OC(F)C(Br)(Br)OBr smiles:OC(F)C(Br)(Br)OBr H298:-98.06 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)Br smiles:CC(C)(Br)C(F)Br H298:-70.75 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)CF smiles:OCC(Br)(Br)CF H298:-97.07 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)Br smiles:FCC(F)C(Br)Br H298:-100.93 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(F)Br smiles:CC(O)(F)C(F)Br H298:-161.34 kcal/mol
library:CHOFBr_G4 label:FC(Br)CBr smiles:FC(Br)CBr H298:-53.35 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)F smiles:O=C(Br)C(Br)C(F)F H298:-135.56 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)F smiles:CC(O)(Br)C(F)F H298:-161.11 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)Br smiles:CCC(Br)C(F)Br H298:-66.80 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)C(F)Br smiles:CC(F)(OBr)C(F)Br H298:-120.06 kcal/mol
library:CHOFBr_G4 label:FC(F)CBr smiles:FC(F)CBr H298:-110.84 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)(Br)CBr smiles:FC#CC(F)(Br)CBr H298:-19.11 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)(Br)CF smiles:CC(Br)C(Br)(Br)CF H298:-61.71 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)F smiles:OC(O)(Br)C(F)F H298:-195.00 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(C)(F)Br smiles:CC(Br)C(C)(F)Br H298:-72.57 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(Br)OBr smiles:OC(F)(Br)C(Br)OBr H298:-98.49 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(Br)Br smiles:CCC(F)C(Br)Br H298:-64.90 kcal/mol
library:CHOFBr_G4 label:FCCC(F)(Br)CBr smiles:FCCC(F)(Br)CBr H298:-113.35 kcal/mol
library:CHOFBr_G4 label:OC(Br)(OBr)C(F)Br smiles:OC(Br)(OBr)C(F)Br H298:-96.83 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)C(Br)Br smiles:FC(F)C(Br)C(Br)Br H298:-102.78 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)Br smiles:FCC(F)C(F)Br H298:-152.58 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)CF smiles:COC(Br)(Br)CF H298:-89.68 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(Br)Br smiles:C#CC(F)C(Br)Br H298:12.11 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(Br)Br smiles:CC(C)(F)C(Br)Br H298:-70.32 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(F)Br smiles:C=C(F)C(F)C(F)Br H298:-129.81 kcal/mol
library:CHOFBr_G4 label:FCCC(F)(F)CBr smiles:FCCC(F)(F)CBr H298:-171.44 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)OBr smiles:FC(F)C(Br)OBr H298:-108.89 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)C(Br)Br smiles:CC(F)(OBr)C(Br)Br H298:-68.40 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)Br smiles:OOC(Br)C(F)Br H298:-70.93 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(F)Br smiles:C=CC(F)C(F)Br H298:-84.49 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)(F)CBr smiles:FC=CC(F)(F)CBr H298:-139.23 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(Br)Br smiles:CC(F)C(F)C(Br)Br H298:-111.37 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)CBr smiles:FC(F)C(F)(Br)CBr H298:-154.76 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(Br)OBr smiles:OC(F)(F)C(Br)OBr H298:-160.19 kcal/mol
library:CHOFBr_G4 label:CCC(F)(F)CBr smiles:CCC(F)(F)CBr H298:-128.48 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)CBr smiles:C=C(F)C(F)(Br)CBr H298:-83.28 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)C(Br)Br smiles:FC(Br)C(Br)C(Br)Br H298:-45.66 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)(Br)CF smiles:O=C(Br)C(Br)(Br)CF H298:-74.61 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)CF smiles:OC(Br)C(F)(F)CF H298:-201.14 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(C)(F)F smiles:CC(Br)C(C)(F)F H298:-131.68 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)CF smiles:O=CC(Br)(Br)CF H298:-74.39 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)Br smiles:CC(Br)(CBr)C(F)Br H298:-63.12 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)Br smiles:OC(Br)C(Br)C(F)Br H298:-94.42 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)F smiles:OC(Br)C(Br)C(F)F H298:-152.46 kcal/mol
library:CHOFBr_G4 label:OOC(F)(Br)CF smiles:OOC(F)(Br)CF H298:-126.67 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)C(Br)Br smiles:FC=CC(F)C(Br)Br H298:-77.83 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)CBr smiles:CC(F)(F)CBr H298:-123.47 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)CF smiles:O=CC(F)(Br)CF H298:-125.89 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)Br smiles:CC(Br)C(F)Br H298:-61.30 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)CBr smiles:CC(F)(F)C(Br)CBr H298:-123.98 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)F smiles:OCC(Br)C(F)F H298:-154.18 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)COBr smiles:FCC(F)(Br)COBr H298:-109.69 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)OCBr smiles:FCC(Br)(Br)OCBr H298:-81.40 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)OF smiles:OC(Br)C(F)(F)OF H298:-162.29 kcal/mol
library:CHOFBr_G4 label:OC(F)C(O)(F)Br smiles:OC(F)C(O)(F)Br H298:-195.79 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)CCBr smiles:FCC(Br)(Br)CCBr H298:-60.09 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)OOBr smiles:FCC(F)(Br)OOBr H298:-89.52 kcal/mol
library:CHOFBr_G4 label:OC(F)C(O)(Br)Br smiles:OC(F)C(O)(Br)Br H298:-138.16 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)F smiles:CC(Br)(CBr)C(F)F H298:-120.77 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)CBr smiles:FCC(F)(F)CBr H298:-163.41 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(Br)CBr smiles:C#CC(F)(Br)CBr H298:9.52 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)OBr smiles:FCC(F)(Br)OBr H298:-108.25 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)COBr smiles:FC(Br)C(Br)COBr H298:-58.24 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(Br)Br smiles:CC(O)(F)C(Br)Br H298:-109.25 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)OOBr smiles:FC(Br)C(Br)OOBr H298:-34.33 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)CF smiles:OC(F)(Br)C(F)CF H298:-199.94 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)OF smiles:OC(Br)(Br)C(F)OF H298:-101.97 kcal/mol
library:CHOFBr_G4 label:FCCC(F)C(Br)Br smiles:FCCC(F)C(Br)Br H298:-109.62 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)OCBr smiles:FC(F)C(Br)OCBr H298:-141.39 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)CBr smiles:CCC(F)(Br)CBr H298:-69.72 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(O)Br smiles:CC(F)(F)C(O)Br H298:-162.16 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)CCBr smiles:FC(F)C(Br)CCBr H298:-119.92 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)Br smiles:OCC(Br)C(F)Br H298:-96.52 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)CF smiles:O=C(Br)C(F)(Br)CF H298:-127.23 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(F)Br smiles:CC(F)(CF)C(F)Br H298:-163.92 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(Br)Br smiles:CC(F)(CF)C(Br)Br H298:-112.16 kcal/mol
library:CHOFBr_G4 label:FCCC(F)C(F)Br smiles:FCCC(F)C(F)Br H298:-161.42 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)CBr smiles:C=C(F)C(F)(F)CBr H298:-139.82 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)CF smiles:OC(Br)(Br)C(F)CF H298:-141.72 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)OF smiles:OC(F)(Br)C(F)OF H298:-160.02 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(F)Br smiles:CC(C)(F)C(F)Br H298:-122.20 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)Br smiles:OC(Br)(CBr)C(F)Br H298:-95.34 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)Br smiles:CC(Br)C(Br)C(F)Br H298:-62.62 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)CF smiles:CCC(Br)(Br)CF H298:-66.11 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)Br smiles:OC(O)(Br)C(F)Br H298:-137.58 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)C(Br)Br smiles:FCC(F)(Br)C(Br)Br H298:-94.23 kcal/mol
library:CHOFBr_G4 label:COC(F)(Br)CF smiles:COC(F)(Br)CF H298:-145.97 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)CBr smiles:CC(F)C(Br)(Br)CBr H298:-63.58 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)Br smiles:OC(Br)C(F)Br H298:-92.64 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)F smiles:CCC(Br)C(F)F H298:-124.51 kcal/mol
library:CHOFBr_G4 label:CC(Br)(OBr)C(F)F smiles:CC(Br)(OBr)C(F)F H298:-121.10 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(Br)Br smiles:C=C(F)C(F)C(Br)Br H298:-78.69 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(F)Br smiles:CCC(F)C(F)Br H298:-117.35 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)CBr smiles:FC(Br)C(Br)CBr H298:-53.87 kcal/mol
library:CHOFBr_G4 label:CC(F)C(C)(Br)Br smiles:CC(F)C(C)(Br)Br H298:-70.08 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(Br)CBr smiles:CC(F)C(F)(Br)CBr H298:-116.10 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(Br)CF smiles:CC(Br)C(F)(Br)CF H298:-111.90 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(Br)Br smiles:FC(F)C(F)C(Br)Br H298:-151.26 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)C(F)Br smiles:FC=CC(F)C(F)Br H298:-129.04 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(F)CBr smiles:C=CC(F)(F)CBr H298:-94.62 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)F smiles:CC(Br)C(F)F H298:-119.26 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)OBr smiles:CC(F)(Br)C(Br)OBr H298:-63.85 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)CF smiles:OC(F)(Br)CF H298:-149.28 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)OBr smiles:FCC(Br)(Br)OBr H298:-51.67 kcal/mol
library:CHOFBr_G4 label:OC(F)C(F)(Br)OBr smiles:OC(F)C(F)(Br)OBr H298:-154.80 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)(Br)CBr smiles:FC=CC(F)(Br)CBr H298:-81.49 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)Br smiles:CC(F)C(F)Br H298:-111.37 kcal/mol
library:CHOFBr_G4 label:CC(Br)(OBr)C(F)Br smiles:CC(Br)(OBr)C(F)Br H298:-63.38 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(O)Br smiles:CC(F)(Br)C(O)Br H298:-104.23 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)CCl smiles:OC(Br)(Br)CCl H298:-53.45 kcal/mol
library:CHOClBr_G4 label:ClC(Br)CBr smiles:ClC(Br)CBr H298:-12.69 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)C(Cl)Br smiles:CC(O)(Br)C(Cl)Br H298:-63.29 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)(Br)CCl smiles:O=CC(Br)(Br)CCl H298:-36.74 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)OBr smiles:ClCC(Br)(Br)OBr H298:-13.89 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(O)Br smiles:CC(Cl)(Br)C(O)Br H298:-62.74 kcal/mol
library:CHOClBr_G4 label:COC(Br)C(Cl)Cl smiles:COC(Br)C(Cl)Cl H298:-59.81 kcal/mol
library:CHOClBr_G4 label:OC(O)(Br)C(Cl)Cl smiles:OC(O)(Br)C(Cl)Cl H298:-108.91 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Br)CCl smiles:CCC(Cl)(Br)CCl H298:-39.82 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)CBr smiles:ClCC(Cl)(Cl)CBr H298:-39.15 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(C)(Br)Br smiles:CC(Cl)C(C)(Br)Br H298:-30.54 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Br)Br smiles:ClCC(Cl)C(Br)Br H298:-24.43 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(O)(Cl)Br smiles:OC(Cl)C(O)(Cl)Br H298:-106.66 kcal/mol
library:CHOClBr_G4 label:CC(C)(Cl)C(Cl)Br smiles:CC(C)(Cl)C(Cl)Br H298:-41.14 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)Cl smiles:OC(Br)C(Cl)Cl H298:-64.15 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)Br smiles:ClCC(Cl)Br H298:-23.73 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Cl smiles:O=CC(Br)C(Cl)Cl H298:-46.58 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CCl smiles:CC(Cl)(Br)CCl H298:-34.24 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)OBr smiles:ClC(Cl)C(Br)OBr H298:-23.53 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(O)(Cl)Cl smiles:OC(Br)C(O)(Cl)Cl H298:-106.80 kcal/mol
library:CHOClBr_G4 label:COC(Br)(Br)CCl smiles:COC(Br)(Br)CCl H298:-51.16 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(O)(Br)Br smiles:OC(Cl)C(O)(Br)Br H298:-94.44 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Cl)Br smiles:ClCC(Cl)C(Cl)Br H298:-35.77 kcal/mol
library:CHOClBr_G4 label:CC(C)(Cl)C(Br)Br smiles:CC(C)(Cl)C(Br)Br H298:-29.69 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)Br smiles:ClCC(Br)Br H298:-12.17 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)C(Cl)Cl smiles:CC(C)(Br)C(Cl)Cl H298:-41.45 kcal/mol
library:CHOClBr_G4 label:CCC(Br)C(Cl)Br smiles:CCC(Br)C(Cl)Br H298:-26.59 kcal/mol
library:CHOClBr_G4 label:OCC(Br)C(Cl)Cl smiles:OCC(Br)C(Cl)Cl H298:-67.86 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)Br smiles:CC(Br)C(Cl)Br H298:-21.07 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(C)(Cl)Cl smiles:CC(Br)C(C)(Cl)Cl H298:-42.67 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Br)CBr smiles:ClCC(Cl)(Br)CBr H298:-27.60 kcal/mol
library:CHOClBr_G4 label:OCC(Br)(Br)CCl smiles:OCC(Br)(Br)CCl H298:-59.23 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)CBr smiles:ClC(Cl)CBr H298:-24.29 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(C)(Cl)Br smiles:CC(Cl)C(C)(Cl)Br H298:-42.23 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Br)CBr smiles:C=CC(Cl)(Br)CBr H298:4.39 kcal/mol
library:CHOClBr_G4 label:CCC(Br)(Br)CCl smiles:CCC(Br)(Br)CCl H298:-28.07 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Br)OBr smiles:ClCC(Cl)(Br)OBr H298:-25.97 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(C)(Cl)Br smiles:CC(Br)C(C)(Cl)Br H298:-30.88 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Br)Br smiles:C#CC(Cl)C(Br)Br H298:50.71 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)CCl smiles:OC(Cl)(Br)CCl H298:-65.70 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)Cl smiles:CC(Br)C(Cl)Cl H298:-32.74 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)CCl smiles:O=CC(Cl)(Br)CCl H298:-47.33 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)Br smiles:CC(Cl)C(Br)Br H298:-20.91 kcal/mol
library:CHOClBr_G4 label:CC(O)(Cl)C(Cl)Br smiles:CC(O)(Cl)C(Cl)Br H298:-75.33 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Cl)CBr smiles:CCC(Cl)(Cl)CBr H298:-40.69 kcal/mol
library:CHOClBr_G4 label:COC(Cl)(Br)CCl smiles:COC(Cl)(Br)CCl H298:-63.07 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)CBr smiles:CC(Cl)(Cl)CBr H298:-34.87 kcal/mol
library:CHOClBr_G4 label:OCC(Br)C(Cl)Br smiles:OCC(Br)C(Cl)Br H298:-56.28 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)C(Br)Br smiles:CCC(Cl)C(Br)Br H298:-26.39 kcal/mol
library:CHOClBr_G4 label:CCC(Br)C(Cl)Cl smiles:CCC(Br)C(Cl)Cl H298:-38.14 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(O)(Br)Br smiles:CC(Cl)C(O)(Br)Br H298:-62.03 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Cl)Br smiles:C=CC(Cl)C(Cl)Br H298:-5.74 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Cl)CBr smiles:C#CC(Cl)(Cl)CBr H298:39.21 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)C(Cl)Br smiles:CC(C)(Br)C(Cl)Br H298:-29.75 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)CCl smiles:CC(Br)(Br)CCl H298:-22.50 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(O)Br smiles:CC(Cl)(Cl)C(O)Br H298:-74.45 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)C(Cl)Br smiles:CCC(Cl)C(Cl)Br H298:-37.68 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Br)Br smiles:C=CC(Cl)C(Br)Br H298:5.72 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)CBr smiles:ClC(Cl)C(Br)CBr H298:-25.22 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(O)(Cl)Br smiles:OC(Br)C(O)(Cl)Br H298:-94.55 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(O)(Cl)Br smiles:CC(Cl)C(O)(Cl)Br H298:-74.18 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CBr smiles:CC(Cl)(Br)CBr H298:-22.83 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Br smiles:O=CC(Br)C(Cl)Br H298:-34.82 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)Br smiles:OC(Br)C(Cl)Br H298:-52.60 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Br)CBr smiles:C#CC(Cl)(Br)CBr H298:50.67 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Br)CCl smiles:OCC(Cl)(Br)CCl H298:-70.59 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Br)CBr smiles:CCC(Cl)(Br)CBr H298:-28.86 kcal/mol
library:CHOClBr_G4 label:OC(O)(Br)C(Cl)Br smiles:OC(O)(Br)C(Cl)Br H298:-97.16 kcal/mol
library:CHOClBr_G4 label:COC(Br)C(Cl)Br smiles:COC(Br)C(Cl)Br H298:-48.04 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Cl)CBr smiles:C=CC(Cl)(Cl)CBr H298:-6.93 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Cl)Br smiles:C#CC(Cl)C(Cl)Br H298:39.27 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)CBr smiles:ClCC(Br)(Br)CBr H298:-16.20 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)C(Cl)Cl smiles:CC(O)(Br)C(Cl)Cl H298:-74.99 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)Br smiles:CC(Cl)C(Cl)Br H298:-32.30 kcal/mol
library:CHOClBr_G4 label:CC(O)(Cl)C(Br)Br smiles:CC(O)(Cl)C(Br)Br H298:-63.97 kcal/mol
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
        Cpdata = ([-0.729467,-0.662152,-0.450405,-0.349957,-0.230988,-0.0385617,0.472339],'cal/(mol*K)','+|-',[0.0829965,0.0959511,0.0983255,0.0970051,0.0843349,0.0728302,0.0579994]),
        H298 = (3.62069,'kcal/mol','+|-',0.301393),
        S298 = (-0.694382,'cal/(mol*K)','+|-',0.195727),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,1,2-Trichloroethane smiles:ClCC(Cl)Cl H298:-35.44 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)CCl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)CCl H298:-59.14 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)CCl smiles:OC(Cl)(Cl)C(Cl)(Cl)CCl H298:-91.46 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)Cl smiles:CC(Cl)C(Cl)Cl H298:-43.99 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)C(Cl)Cl H298:-64.73 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.15 kcal/mol
library:CHOCl_G4 label:OC(Cl)(OCl)C(Cl)Cl smiles:OC(Cl)(OCl)C(Cl)Cl H298:-83.01 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)C(Cl)Cl smiles:C#CC(Cl)C(Cl)Cl H298:27.68 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)(Cl)CCl smiles:C=CC(Cl)(Cl)CCl H298:-18.08 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-55.19 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)Cl H298:-51.97 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)Cl smiles:ClOC(Cl)C(Cl)Cl H298:-37.97 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-44.60 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)C(Cl)Cl smiles:ClCOC(Cl)C(Cl)Cl H298:-79.26 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)OCl smiles:ClCC(Cl)(Cl)OCl H298:-40.27 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)CCl smiles:CC(Cl)(Cl)C(Cl)(Cl)CCl H298:-60.01 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-54.39 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)CCl smiles:C=C(Cl)C(Cl)(Cl)CCl H298:-24.81 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)Cl H298:-50.72 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)CCl smiles:CC(Cl)(Cl)C(Cl)CCl H298:-57.76 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCC(Cl)C(Cl)Cl smiles:ClC(Cl)=CC(Cl)C(Cl)Cl H298:-29.11 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-56.00 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)OCl smiles:ClOC(Cl)C(Cl)(Cl)OCl H298:-41.43 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-60.00 kcal/mol
library:CHOCl_G4 label:OOC(Cl)(Cl)CCl smiles:OOC(Cl)(Cl)CCl H298:-56.47 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)Cl H298:-30.04 kcal/mol
library:CHOCl_G4 label:ClC(Cl)CC(Cl)C(Cl)Cl smiles:ClC(Cl)CC(Cl)C(Cl)Cl H298:-60.86 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-26.72 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)CCl smiles:ClCC(Cl)C(Cl)(Cl)CCl H298:-61.87 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(O)(Cl)Cl smiles:CC(Cl)C(O)(Cl)Cl H298:-86.56 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-57.91 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)C(Cl)Cl smiles:O=C(Cl)C(Cl)C(Cl)Cl H298:-73.21 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)COCl smiles:ClCC(Cl)(Cl)COCl H298:-46.03 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)C(Cl)Cl smiles:OC(Cl)C(Cl)C(Cl)Cl H298:-88.48 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-58.28 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)OCl smiles:OC(Cl)(Cl)C(Cl)OCl H298:-79.79 kcal/mol
library:CHOCl_G4 label:CCC(Cl)C(Cl)Cl smiles:CCC(Cl)C(Cl)Cl H298:-49.26 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)OOCl smiles:ClCC(Cl)(Cl)OOCl H298:-22.69 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)C(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)C(Cl)Cl H298:-58.82 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.38 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)C(Cl)Cl smiles:CC(Cl)(CCl)C(Cl)Cl H298:-57.51 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)(Cl)CCl smiles:ClCOC(Cl)(Cl)CCl H298:-79.61 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(O)Cl smiles:CC(Cl)(Cl)C(O)Cl H298:-86.57 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)C(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)C(Cl)Cl H298:-51.23 kcal/mol
library:CHOCl_G4 label:CC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-56.43 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)(Cl)CCl smiles:C#CC(Cl)(Cl)CCl H298:28.14 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)C(Cl)Cl smiles:ClOCC(Cl)C(Cl)Cl H298:-44.08 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)C(Cl)Cl smiles:C=CC(Cl)C(Cl)Cl H298:-17.24 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)C(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)C(Cl)Cl H298:-90.87 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)CCl smiles:CC(Cl)(Cl)CCl H298:-46.01 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)C(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)C(Cl)Cl H298:-60.95 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(OCl)C(Cl)Cl smiles:ClCC(Cl)(OCl)C(Cl)Cl H298:-50.89 kcal/mol
library:CHOCl_G4 label:CCC(Cl)(Cl)CCl smiles:CCC(Cl)(Cl)CCl H298:-51.68 kcal/mol
library:CHOCl_G4 label:CC(O)(Cl)C(Cl)Cl smiles:CC(O)(Cl)C(Cl)Cl H298:-87.19 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-60.78 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)CCl smiles:OC(Cl)C(Cl)(Cl)CCl H298:-89.47 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-55.56 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)CCl smiles:O=C(Cl)C(Cl)(Cl)CCl H298:-72.19 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)OCl smiles:ClCC(Cl)(Cl)C(Cl)OCl H298:-52.31 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-52.54 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:CC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-60.47 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-48.96 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)CDC(Cl)Cl smiles:ClCC(Cl)(Cl)C=C(Cl)Cl H298:-26.23 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClOC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-54.08 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)C(Cl)Cl smiles:ClCC(Cl)C(Cl)C(Cl)Cl H298:-61.79 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:OC(Cl)C(Cl)(Cl)C(Cl)Cl H298:-91.30 kcal/mol
library:CHOCl_G4 label:OOC(Cl)C(Cl)Cl smiles:OOC(Cl)C(Cl)Cl H298:-55.24 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)CCl smiles:ClC=C(Cl)C(Cl)(Cl)CCl H298:-29.97 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)Cl H298:-30.71 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)OC(Cl)Cl smiles:ClCC(Cl)(Cl)OC(Cl)Cl H298:-84.03 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)OCl smiles:CC(Cl)C(Cl)(Cl)OCl H298:-48.76 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)C(Cl)Cl smiles:C=C(Cl)C(Cl)C(Cl)Cl H298:-24.03 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)Cl H298:-50.01 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)(Cl)CCl smiles:CC(Cl)C(Cl)(Cl)CCl H298:-56.74 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(C)(Cl)Cl smiles:CC(Cl)C(C)(Cl)Cl H298:-54.04 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)OC(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)OC(Cl)(Cl)Cl H298:-83.76 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)(Cl)CCl smiles:ClC=CC(Cl)(Cl)CCl H298:-23.91 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)C(Cl)Cl smiles:ClC#CC(Cl)C(Cl)Cl H298:27.00 kcal/mol
library:CHOCl_G4 label:COC(Cl)C(Cl)Cl smiles:COC(Cl)C(Cl)Cl H298:-71.05 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)C(Cl)Cl smiles:ClOC(Cl)C(Cl)C(Cl)Cl H298:-51.48 kcal/mol
library:CHOCl_G4 label:OC(O)(Cl)C(Cl)Cl smiles:OC(O)(Cl)C(Cl)Cl H298:-121.60 kcal/mol
library:CHOCl_G4 label:OC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-86.10 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)OCl smiles:OC(Cl)C(Cl)(Cl)OCl H298:-80.02 kcal/mol
library:CHOCl_G4 label:OCC(Cl)(Cl)CCl smiles:OCC(Cl)(Cl)CCl H298:-82.33 kcal/mol
library:CHOCl_G4 label:ClC(Cl)OC(Cl)C(Cl)Cl smiles:ClC(Cl)OC(Cl)C(Cl)Cl H298:-87.66 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)C(Cl)Cl smiles:OC(Cl)(CCl)C(Cl)Cl H298:-89.76 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)C(Cl)Cl smiles:ClCCC(Cl)C(Cl)Cl H298:-55.91 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)Cl smiles:OC(Cl)C(Cl)Cl H298:-76.19 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)C(Cl)Cl smiles:O=CC(Cl)C(Cl)Cl H298:-57.25 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-60.27 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(OCl)C(Cl)Cl smiles:ClOC(Cl)(OCl)C(Cl)Cl H298:-44.89 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)Cl smiles:ClCC(Cl)C(Cl)Cl H298:-48.33 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-46.21 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)CCl smiles:OC(Cl)(Cl)C(Cl)CCl H298:-89.99 kcal/mol
library:CHOCl_G4 label:OCC(Cl)C(Cl)Cl smiles:OCC(Cl)C(Cl)Cl H298:-79.02 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)Cl H298:-59.61 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-86.00 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)CC(Cl)Cl smiles:ClCC(Cl)(Cl)CC(Cl)Cl H298:-59.64 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(C(Cl)Cl)C(Cl)Cl smiles:ClOC(Cl)(C(Cl)Cl)C(Cl)Cl H298:-50.16 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)OCl smiles:ClCC(Cl)C(Cl)(Cl)OCl H298:-51.63 kcal/mol
library:CHOCl_G4 label:CC(Cl)(C(Cl)Cl)C(Cl)Cl smiles:CC(Cl)(C(Cl)Cl)C(Cl)Cl H298:-60.30 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)Cl)C(Cl)Cl smiles:ClCC(Cl)(C(Cl)Cl)C(Cl)Cl H298:-58.79 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)CC(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)CC(Cl)(Cl)Cl H298:-61.65 kcal/mol
library:CHOCl_G4 label:COC(Cl)(Cl)CCl smiles:COC(Cl)(Cl)CCl H298:-75.05 kcal/mol
library:CHOCl_G4 label:CC(C)(Cl)C(Cl)Cl smiles:CC(C)(Cl)C(Cl)Cl H298:-53.00 kcal/mol
library:CHOCl_G4 label:OC(Cl)(C(Cl)Cl)C(Cl)Cl smiles:OC(Cl)(C(Cl)Cl)C(Cl)Cl H298:-92.70 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-84.83 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(O)(Cl)Cl smiles:OC(Cl)C(O)(Cl)Cl H298:-118.84 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)C(Cl)Cl smiles:ClC=CC(Cl)C(Cl)Cl H298:-25.57 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)(Cl)CCl smiles:ClC#CC(Cl)(Cl)CCl H298:27.39 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)OCl smiles:CC(Cl)(Cl)C(Cl)OCl H298:-48.84 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)C(Cl)Cl smiles:CC(Cl)C(Cl)C(Cl)Cl H298:-56.47 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)C(Cl)Cl smiles:ClOOC(Cl)C(Cl)Cl H298:-21.40 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)CCl smiles:ClCC(Cl)(Cl)CCl H298:-50.17 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)CCl smiles:O=CC(Cl)(Cl)CCl H298:-58.99 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)CCl smiles:OC(Cl)(Cl)CCl H298:-78.06 kcal/mol
library:CHOCl_G4 label:CC(Cl)(OCl)C(Cl)Cl smiles:CC(Cl)(OCl)C(Cl)Cl H298:-50.10 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl H298:-59.49 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-49.19 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)(Cl)CCl smiles:ClCCC(Cl)(Cl)CCl H298:-55.94 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)C(Cl)Cl smiles:ClCC(Cl)(CCl)C(Cl)Cl H298:-60.43 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-48.77 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)OCl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)OCl H298:-53.35 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)(Cl)CCl smiles:FCC(Cl)(Cl)CCl H298:-87.81 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)C(Cl)Cl smiles:FCC(Cl)C(Cl)Cl H298:-84.61 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)CBr smiles:ClCC(Cl)(Cl)CBr H298:-39.15 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)OBr smiles:ClC(Cl)C(Cl)OBr H298:-35.43 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)CBr smiles:ClC(Cl)C(Cl)CBr H298:-36.55 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)OBr smiles:ClCC(Cl)(Cl)OBr H298:-38.15 kcal/mol
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
        Cpdata = ([-0.246605,-0.0948818,0.0683587,0.117146,0.111654,0.15154,0.329737],'cal/(mol*K)','+|-',[0.0765579,0.0885076,0.0906978,0.0894799,0.0777925,0.0671803,0.0535001]),
        H298 = (4.63314,'kcal/mol','+|-',0.278012),
        S298 = (0.336312,'cal/(mol*K)','+|-',0.180544),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCC(F)(F)OOF smiles:FCC(F)(F)OOF H298:-161.38 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)OF smiles:CC(F)(F)C(F)OF H298:-185.04 kcal/mol
library:CHOF_G4 label:OOC(F)C(F)F smiles:OOC(F)C(F)F H298:-184.22 kcal/mol
library:CHOF_G4 label:FC(F)C(F)CC(F)(F)F smiles:FC(F)C(F)CC(F)(F)F H298:-330.00 kcal/mol
library:CHOF_G4 label:FCC(F)F smiles:FCC(F)F H298:-159.49 kcal/mol
library:CHOF_G4 label:FC(F)OC(F)C(F)F smiles:FC(F)OC(F)C(F)F H298:-306.77 kcal/mol
library:CHOF_G4 label:FOC(F)(C(F)F)C(F)F smiles:FOC(F)(C(F)F)C(F)F H298:-269.40 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)CF smiles:CC(F)(F)C(F)CF H298:-223.33 kcal/mol
library:CHOF_G4 label:OC(F)C(F)F smiles:OC(F)C(F)F H298:-205.91 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(O)F smiles:CC(F)(F)C(O)F H298:-219.23 kcal/mol
library:CHOF_G4 label:CCC(F)(F)CF smiles:CCC(F)(F)CF H298:-177.06 kcal/mol
library:CHOF_G4 label:FCDCC(F)C(F)F smiles:FC=CC(F)C(F)F H298:-187.02 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)F smiles:FCC(F)C(F)F H298:-209.90 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)C(F)(F)C(F)(F)F H298:-414.81 kcal/mol
library:CHOF_G4 label:CC(F)(C(F)F)C(F)(F)F smiles:CC(F)(C(F)F)C(F)(F)F H298:-329.47 kcal/mol
library:CHOF_G4 label:CDCC(F)C(F)F smiles:C=CC(F)C(F)F H298:-142.22 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)C(F)F smiles:CC(F)C(F)(F)C(F)F H298:-272.41 kcal/mol
library:CHOF_G4 label:FOCC(F)C(F)F smiles:FOCC(F)C(F)F H298:-173.85 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)CF smiles:OC(F)C(F)(F)CF H298:-258.28 kcal/mol
library:CHOF_G4 label:OC(F)(CF)C(F)F smiles:OC(F)(CF)C(F)F H298:-259.20 kcal/mol
library:CHOF_G4 label:FC(F)C(F)OC(F)(F)F smiles:FC(F)C(F)OC(F)(F)F H298:-362.91 kcal/mol
library:CHOF_G4 label:FOC(F)(OF)C(F)F smiles:FOC(F)(OF)C(F)F H298:-177.93 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)(F)F smiles:FCC(F)(C(F)F)C(F)(F)F H298:-365.50 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)OF smiles:OC(F)C(F)(F)OF H298:-219.04 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)C(F)(F)F smiles:FCC(F)(F)C(F)(F)C(F)(F)F H298:-415.15 kcal/mol
library:CHOF_G4 label:CC(F)C(F)C(F)F smiles:CC(F)C(F)C(F)F H298:-220.98 kcal/mol
library:CHOF_G4 label:FCOC(F)(F)CF smiles:FCOC(F)(F)CF H298:-255.22 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)C(F)F smiles:FCC(F)(F)C(F)C(F)F H298:-312.28 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)(F)CF smiles:OC(F)(F)C(F)(F)CF H298:-312.63 kcal/mol
library:CHOF_G4 label:FCC(F)(F)OC(F)F smiles:FCC(F)(F)OC(F)F H298:-310.07 kcal/mol
library:CHOF_G4 label:CC(O)(F)C(F)F smiles:CC(O)(F)C(F)F H298:-218.61 kcal/mol
library:CHOF_G4 label:CC(F)C(F)F smiles:CC(F)C(F)F H298:-169.65 kcal/mol
library:CHOF_G4 label:FC(F)CC(F)C(F)F smiles:FC(F)CC(F)C(F)F H298:-272.33 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)CF smiles:FC=C(F)C(F)(F)CF H298:-227.47 kcal/mol
library:CHOF_G4 label:FOC(F)(C(F)F)C(F)(F)F smiles:FOC(F)(C(F)F)C(F)(F)F H298:-323.85 kcal/mol
library:CHOF_G4 label:FCC(F)(F)CC(F)F smiles:FCC(F)(F)CC(F)F H298:-273.24 kcal/mol
library:CHOF_G4 label:COC(F)(F)CF smiles:COC(F)(F)CF H298:-207.17 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)C(F)F smiles:FCC(F)(F)C(F)(F)C(F)F H298:-360.16 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)CF smiles:CC(F)(F)C(F)(F)CF H298:-275.08 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)F)C(F)F smiles:FC(F)C(F)(C(F)F)C(F)F H298:-360.38 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)F smiles:FC(F)C(F)C(F)F H298:-260.94 kcal/mol
library:CHOF_G4 label:C#CC(F)(F)CF smiles:C#CC(F)(F)CF H298:-96.51 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)C(F)F smiles:FOC(F)(F)C(F)C(F)F H298:-272.90 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)F smiles:FOC(F)C(F)F H298:-171.54 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)CF smiles:O=C(F)C(F)(F)CF H298:-240.95 kcal/mol
library:CHOF_G4 label:FC(C(F)(F)F)C(F)(F)C(F)(F)F smiles:FC(C(F)(F)F)C(F)(F)C(F)(F)F H298:-471.81 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)C(F)F smiles:OC(F)C(F)(F)C(F)F H298:-306.17 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)C(F)F smiles:C=C(F)C(F)C(F)F H298:-187.04 kcal/mol
library:CHOF_G4 label:OCC(F)C(F)F smiles:OCC(F)C(F)F H298:-202.56 kcal/mol
library:CHOF_G4 label:FCC(F)(F)CDC(F)F smiles:FCC(F)(F)C=C(F)F H298:-237.90 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)CF smiles:FCC(F)C(F)(F)CF H298:-262.80 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)C(F)(F)F smiles:FC(F)C(F)C(F)C(F)(F)F H298:-367.06 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)C(F)F smiles:FCC(F)(CF)C(F)F H298:-261.93 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)F smiles:FCC(F)(C(F)F)C(F)F H298:-312.20 kcal/mol
library:CHOF_G4 label:OC(F)C(O)(F)F smiles:OC(F)C(O)(F)F H298:-258.01 kcal/mol
library:CHOF_G4 label:CC(F)(OF)C(F)F smiles:CC(F)(OF)C(F)F H298:-185.19 kcal/mol
library:CHOF_G4 label:FCCC(F)(F)CF smiles:FCCC(F)(F)CF H298:-220.38 kcal/mol
library:CHOF_G4 label:CC(C)(F)C(F)F smiles:CC(C)(F)C(F)F H298:-180.72 kcal/mol
library:CHOF_G4 label:ODCC(F)C(F)F smiles:O=CC(F)C(F)F H298:-180.26 kcal/mol
library:CHOF_G4 label:FC#CC(F)(F)CF smiles:FC#CC(F)(F)CF H298:-125.44 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)OF smiles:FCC(F)C(F)(F)OF H298:-223.34 kcal/mol
library:CHOF_G4 label:OC(F)(C(F)F)C(F)(F)F smiles:OC(F)(C(F)F)C(F)(F)F H298:-362.54 kcal/mol
library:CHOF_G4 label:FOOC(F)C(F)F smiles:FOOC(F)C(F)F H298:-160.05 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)C(F)(F)F H298:-415.54 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)C(F)F smiles:FOC(F)C(F)C(F)F H298:-222.80 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)C(F)F smiles:FC(F)=CC(F)C(F)F H298:-235.89 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)C(F)F smiles:FCC(F)C(F)C(F)F H298:-261.79 kcal/mol
library:CHOF_G4 label:OC(F)(C(F)F)C(F)F smiles:OC(F)(C(F)F)C(F)F H298:-308.47 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)C(F)(F)F smiles:CC(F)(F)C(F)C(F)(F)F H298:-329.68 kcal/mol
library:CHOF_G4 label:OC(F)C(F)(F)C(F)(F)F smiles:OC(F)C(F)(F)C(F)(F)F H298:-360.97 kcal/mol
library:CHOF_G4 label:OC(O)(F)C(F)F smiles:OC(O)(F)C(F)F H298:-256.94 kcal/mol
library:CHOF_G4 label:FCCC(F)C(F)F smiles:FCCC(F)C(F)F H298:-218.81 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)(F)F)C(F)(F)F H298:-469.60 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)OF smiles:FOC(F)C(F)(F)OF H298:-182.32 kcal/mol
library:CHOF_G4 label:FC#CC(F)C(F)F smiles:FC#CC(F)C(F)F H298:-125.88 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)F smiles:FCC(F)(F)C(F)(F)F H298:-316.54 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)CF smiles:O=CC(F)(F)CF H298:-181.03 kcal/mol
library:CHOF_G4 label:OC(F)(OF)C(F)F smiles:OC(F)(OF)C(F)F H298:-218.32 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)F smiles:FC(F)=C(F)C(F)C(F)F H298:-272.23 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)C(F)F smiles:FC(F)C(F)C(F)(F)C(F)F H298:-360.28 kcal/mol
library:CHOF_G4 label:CC(F)(F)CF smiles:CC(F)(F)CF H298:-172.49 kcal/mol
library:CHOF_G4 label:CC(F)C(C)(F)F smiles:CC(F)C(C)(F)F H298:-182.66 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)F smiles:FC=C(F)C(F)C(F)F H298:-226.59 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)C(F)F smiles:CC(F)(F)C(F)C(F)F H298:-273.38 kcal/mol
library:CHOF_G4 label:COC(F)C(F)F smiles:COC(F)C(F)F H298:-201.04 kcal/mol
library:CHOF_G4 label:C#CC(F)C(F)F smiles:C#CC(F)C(F)F H298:-97.24 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)C(F)F smiles:FCC(F)C(F)(F)C(F)F H298:-310.46 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)C(F)F smiles:O=C(F)C(F)C(F)F H298:-241.91 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)C(F)(F)F smiles:FCC(F)(F)C(F)C(F)(F)F H298:-368.56 kcal/mol
library:CHOF_G4 label:OCC(F)(F)CF smiles:OCC(F)(F)CF H298:-206.47 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)C(F)(F)F smiles:FOC(F)C(F)(F)C(F)(F)F H298:-325.79 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)CF smiles:C=C(F)C(F)(F)CF H298:-188.16 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)OF smiles:FCC(F)(F)C(F)OF H298:-222.72 kcal/mol
library:CHOF_G4 label:CDCC(F)(F)CF smiles:C=CC(F)(F)CF H298:-143.21 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)(F)C(F)F smiles:FOC(F)C(F)(F)C(F)F H298:-270.79 kcal/mol
library:CHOF_G4 label:OC(F)C(F)C(F)F smiles:OC(F)C(F)C(F)F H298:-257.09 kcal/mol
library:CHOF_G4 label:FCC(F)(F)CC(F)(F)F smiles:FCC(F)(F)CC(F)(F)F H298:-330.74 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)F smiles:FCC(F)(F)C(F)F H298:-261.57 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)OF smiles:FCC(F)(F)C(F)(F)OF H298:-272.22 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)OF smiles:CC(F)C(F)(F)OF H298:-184.30 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)DC(F)F smiles:FCC(F)(F)C(F)=C(F)F H298:-270.34 kcal/mol
library:CHOF_G4 label:CC(F)C(O)(F)F smiles:CC(F)C(O)(F)F H298:-222.40 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)C(F)F smiles:FCC(F)(OF)C(F)F H298:-220.88 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)CF smiles:FCC(F)(F)C(F)(F)CF H298:-312.03 kcal/mol
library:CHOF_G4 label:FCOC(F)C(F)F smiles:FCOC(F)C(F)F H298:-250.93 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)CF smiles:CC(F)C(F)(F)CF H298:-221.49 kcal/mol
library:CHOF_G4 label:CC(F)(CF)C(F)F smiles:CC(F)(CF)C(F)F H298:-221.98 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)C(F)(F)F smiles:FCC(F)C(F)(F)C(F)(F)F H298:-366.48 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)C(F)(F)F smiles:FOC(F)(F)C(F)C(F)(F)F H298:-328.06 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)C(F)F smiles:OC(F)(F)C(F)C(F)F H298:-312.06 kcal/mol
library:CHOF_G4 label:FCC(F)(F)OC(F)(F)F smiles:FCC(F)(F)OC(F)(F)F H298:-364.87 kcal/mol
library:CHOF_G4 label:OOC(F)(F)CF smiles:OOC(F)(F)CF H298:-187.74 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)F)C(F)(F)F H298:-414.90 kcal/mol
library:CHOF_G4 label:CC(F)C(F)(F)C(F)(F)F smiles:CC(F)C(F)(F)C(F)(F)F H298:-327.15 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)C(F)(F)F smiles:OC(F)(F)C(F)C(F)(F)F H298:-367.83 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)CF smiles:OC(F)(F)C(F)CF H298:-262.54 kcal/mol
library:CHOF_G4 label:FCC(F)(F)OF smiles:FCC(F)(F)OF H298:-173.67 kcal/mol
library:CHOF_G4 label:OC(F)(F)CF smiles:OC(F)(F)CF H298:-212.02 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)C(F)F smiles:FC(F)C(F)C(F)C(F)F H298:-313.85 kcal/mol
library:CHOF_G4 label:CC(F)(C(F)F)C(F)F smiles:CC(F)(C(F)F)C(F)F H298:-272.88 kcal/mol
library:CHOF_G4 label:CCC(F)C(F)F smiles:CCC(F)C(F)F H298:-174.34 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)F smiles:FC(F)C(F)C(F)(F)F H298:-317.05 kcal/mol
library:CHOF_G4 label:FCC(F)(F)COF smiles:FCC(F)(F)COF H298:-175.71 kcal/mol
library:CHOF_G4 label:FCC(F)(F)CF smiles:FCC(F)(F)CF H298:-212.34 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)OF smiles:OC(F)(F)C(F)OF H298:-222.38 kcal/mol
library:CHOF_G4 label:FCDCC(F)(F)CF smiles:FC=CC(F)(F)CF H298:-187.81 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)CCl smiles:FC(F)C(F)CCl H298:-172.53 kcal/mol
library:CHOFCl_G4 label:FCC(F)(F)CCl smiles:FCC(F)(F)CCl H298:-174.61 kcal/mol
library:CHOFCl_G4 label:FCC(F)(F)OCl smiles:FCC(F)(F)OCl H298:-171.79 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)OCl smiles:FC(F)C(F)OCl H298:-167.37 kcal/mol
library:CHOFBr_G4 label:OC(F)C(F)(F)OBr smiles:OC(F)C(F)(F)OBr H298:-215.93 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(Br)Br smiles:FCC(F)(F)C(Br)Br H298:-152.86 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)OBr smiles:FC(F)C(F)OBr H298:-164.74 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)CBr smiles:CC(F)C(F)(F)CBr H298:-174.01 kcal/mol
library:CHOFBr_G4 label:OC(F)(OBr)C(F)F smiles:OC(F)(OBr)C(F)F H298:-214.43 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)COBr smiles:FC(F)C(F)COBr H298:-165.65 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)OOBr smiles:FC(F)C(F)OOBr H298:-147.37 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(F)OBr smiles:OC(F)(F)C(F)OBr H298:-216.00 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)CBr smiles:CC(F)(F)C(F)CBr H298:-174.71 kcal/mol
library:CHOFBr_G4 label:OC(F)(CBr)C(F)F smiles:OC(F)(CBr)C(F)F H298:-210.81 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)OBr smiles:FCC(F)(F)OBr H298:-169.84 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(F)Br smiles:FC(F)C(F)C(F)Br H298:-203.52 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)C(F)F smiles:OC(Br)C(F)C(F)F H298:-201.16 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)CF smiles:CC(Br)C(F)(F)CF H298:-170.21 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)CF smiles:O=C(Br)C(F)(F)CF H298:-182.34 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)COBr smiles:FCC(F)(F)COBr H298:-166.78 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)OOBr smiles:FCC(F)(F)OOBr H298:-150.30 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)OCBr smiles:FCC(F)(F)OCBr H298:-200.42 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(F)Br smiles:FCC(F)(F)C(F)Br H298:-204.62 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)CCBr smiles:FCC(F)(F)CCBr H298:-170.68 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)C(F)F smiles:O=C(Br)C(F)C(F)F H298:-182.79 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)CF smiles:OC(Br)C(F)(F)CF H298:-201.14 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)C(F)F smiles:CC(Br)C(F)C(F)F H298:-170.09 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)CBr smiles:FCC(F)(F)CBr H298:-163.41 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)OBr smiles:CC(F)(F)C(F)OBr H298:-178.84 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)CCBr smiles:FC(F)C(F)CCBr H298:-169.40 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)F smiles:CC(F)(CBr)C(F)F H298:-172.71 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)OBr smiles:CC(F)C(F)(F)OBr H298:-180.53 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(Br)Br smiles:FC(F)C(F)C(Br)Br H298:-151.26 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)CBr smiles:FC(F)C(F)CBr H298:-161.40 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)C(F)F smiles:CC(F)(OBr)C(F)F H298:-177.52 kcal/mol
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
        Cpdata = ([-0.575891,-0.534963,-0.365518,-0.279969,-0.185277,-0.0766211,0.225846],'cal/(mol*K)','+|-',[0.111286,0.128656,0.13184,0.130069,0.113081,0.0976545,0.0777686]),
        H298 = (2.55873,'kcal/mol','+|-',0.404123),
        S298 = (0.242565,'cal/(mol*K)','+|-',0.262441),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CC(Br)(Br)C(Br)CBr smiles:CC(Br)(Br)C(Br)CBr H298:-12.36 kcal/mol
library:CHOBr_G4 label:BrOOC(Br)C(Br)Br smiles:BrOOC(Br)C(Br)Br H298:16.31 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)(Br)CBr smiles:BrCCC(Br)(Br)CBr H298:-11.18 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)Br smiles:CC(Br)C(Br)Br H298:-9.76 kcal/mol
library:CHOBr_G4 label:C#CC(Br)C(Br)Br smiles:C#CC(Br)C(Br)Br H298:61.32 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)(Br)OBr smiles:CC(Br)C(Br)(Br)OBr H298:-11.19 kcal/mol
library:CHOBr_G4 label:CDCC(Br)(Br)CBr smiles:C=CC(Br)(Br)CBr H298:16.09 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)C(Br)Br smiles:BrC#CC(Br)C(Br)Br H298:71.52 kcal/mol
library:CHOBr_G4 label:OOC(Br)(Br)CBr smiles:OOC(Br)(Br)CBr H298:-21.52 kcal/mol
library:CHOBr_G4 label:CCC(Br)C(Br)Br smiles:CCC(Br)C(Br)Br H298:-15.37 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)C(Br)Br smiles:CC(Br)(CBr)C(Br)Br H298:-12.14 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)(Br)CBr smiles:BrC=CC(Br)(Br)CBr H298:21.57 kcal/mol
library:CHOBr_G4 label:C#CC(Br)(Br)CBr smiles:C#CC(Br)(Br)CBr H298:61.46 kcal/mol
library:CHOBr_G4 label:CC(Br)C(O)(Br)Br smiles:CC(Br)C(O)(Br)Br H298:-50.62 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)C(Br)Br smiles:BrCCC(Br)C(Br)Br H298:-11.10 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)CBr smiles:CC(Br)(Br)CBr H298:-11.45 kcal/mol
library:CHOBr_G4 label:CDCC(Br)C(Br)Br smiles:C=CC(Br)C(Br)Br H298:16.57 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)(Br)CBr smiles:BrC#CC(Br)(Br)CBr H298:71.53 kcal/mol
library:CHOBr_G4 label:CC(O)(Br)C(Br)Br smiles:CC(O)(Br)C(Br)Br H298:-51.82 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)C(Br)Br smiles:BrC=CC(Br)C(Br)Br H298:20.42 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C(Br)Br smiles:BrOC(Br)C(Br)Br H298:-0.77 kcal/mol
library:CHOBr_G4 label:CCC(Br)(Br)CBr smiles:CCC(Br)(Br)CBr H298:-17.47 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)OBr smiles:BrCC(Br)(Br)OBr H298:-3.03 kcal/mol
library:CHOBr_G4 label:OOC(Br)C(Br)Br smiles:OOC(Br)C(Br)Br H298:-20.43 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)CBr smiles:BrCC(Br)(Br)CBr H298:-5.30 kcal/mol
library:CHOBr_G4 label:OC(O)(Br)C(Br)Br smiles:OC(O)(Br)C(Br)Br H298:-85.72 kcal/mol
library:CHOBr_G4 label:COC(Br)C(Br)Br smiles:COC(Br)C(Br)Br H298:-36.87 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)OOBr smiles:BrCC(Br)(Br)OOBr H298:15.20 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)COBr smiles:BrCC(Br)(Br)COBr H298:-9.23 kcal/mol
library:CHOBr_G4 label:OCC(Br)(Br)CBr smiles:OCC(Br)(Br)CBr H298:-48.25 kcal/mol
library:CHOBr_G4 label:CC(Br)(OBr)C(Br)Br smiles:CC(Br)(OBr)C(Br)Br H298:-12.65 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)C(Br)Br smiles:CC(Br)C(Br)C(Br)Br H298:-11.03 kcal/mol
library:CHOBr_G4 label:OC(Br)C(O)(Br)Br smiles:OC(Br)C(O)(Br)Br H298:-82.47 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)(Br)CBr smiles:BrCOC(Br)(Br)CBr H298:-33.75 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)Br smiles:OC(Br)C(Br)Br H298:-41.26 kcal/mol
library:CHOBr_G4 label:BrOCC(Br)C(Br)Br smiles:BrOCC(Br)C(Br)Br H298:-6.98 kcal/mol
library:CHOBr_G4 label:ODCC(Br)C(Br)Br smiles:O=CC(Br)C(Br)Br H298:-23.73 kcal/mol
library:CHOBr_G4 label:OCC(Br)C(Br)Br smiles:OCC(Br)C(Br)Br H298:-45.03 kcal/mol
library:CHOBr_G4 label:COC(Br)(Br)CBr smiles:COC(Br)(Br)CBr H298:-40.31 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)Br smiles:BrCC(Br)C(Br)Br H298:-2.46 kcal/mol
library:CHOBr_G4 label:CC(C)(Br)C(Br)Br smiles:CC(C)(Br)C(Br)Br H298:-18.20 kcal/mol
library:CHOBr_G4 label:BrCC(Br)Br smiles:BrCC(Br)Br H298:-1.16 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(O)Br smiles:CC(Br)(Br)C(O)Br H298:-51.22 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)(Br)CBr smiles:CC(Br)C(Br)(Br)CBr H298:-11.39 kcal/mol
library:CHOBr_G4 label:CC(Br)C(C)(Br)Br smiles:CC(Br)C(C)(Br)Br H298:-19.26 kcal/mol
library:CHOBr_G4 label:BrC(Br)C(Br)C(Br)Br smiles:BrC(Br)C(Br)C(Br)Br H298:9.09 kcal/mol
library:CHOBr_G4 label:ODCC(Br)(Br)CBr smiles:O=CC(Br)(Br)CBr H298:-25.71 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(Br)OBr smiles:CC(Br)(Br)C(Br)OBr H298:-11.19 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)C(Br)Br smiles:BrCOC(Br)C(Br)Br H298:-33.27 kcal/mol
library:CHOBr_G4 label:OC(Br)(Br)CBr smiles:OC(Br)(Br)CBr H298:-42.50 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)CBr smiles:FCC(Br)(Br)CBr H298:-53.62 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)CF smiles:OC(Br)C(Br)(Br)CF H298:-92.64 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)OF smiles:OC(Br)C(Br)(Br)OF H298:-46.20 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)C(Br)Br smiles:OC(Br)(CF)C(Br)Br H298:-93.20 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)Br smiles:FCC(Br)C(Br)Br H298:-50.50 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)C(Br)Br smiles:CC(Br)(CF)C(Br)Br H298:-60.48 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)(Br)CF smiles:CC(Br)C(Br)(Br)CF H298:-61.71 kcal/mol
library:CHOFBr_G4 label:FCCC(Br)C(Br)Br smiles:FCCC(Br)C(Br)Br H298:-59.75 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)C(Br)Br smiles:FC(F)C(Br)C(Br)Br H298:-102.78 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)CF smiles:CC(Br)(Br)C(Br)CF H298:-60.33 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)C(Br)Br smiles:C=C(F)C(Br)C(Br)Br H298:-29.68 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)C(Br)Br smiles:FC=CC(Br)C(Br)Br H298:-28.81 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)C(Br)Br smiles:FC(Br)C(Br)C(Br)Br H298:-45.66 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)C(Br)Br smiles:CC(F)C(Br)C(Br)Br H298:-60.56 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)(Br)CBr smiles:FC#CC(Br)(Br)CBr H298:33.20 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)CBr smiles:FC(F)C(Br)(Br)CBr H298:-103.69 kcal/mol
library:CHOFBr_G4 label:FCCC(Br)(Br)CBr smiles:FCCC(Br)(Br)CBr H298:-59.66 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)CBr smiles:C=C(F)C(Br)(Br)CBr H298:-29.64 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)CBr smiles:CC(F)C(Br)(Br)CBr H298:-63.58 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)CBr smiles:FC(Br)C(Br)(Br)CBr H298:-46.80 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)(Br)CBr smiles:FC=CC(Br)(Br)CBr H298:-27.91 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)OF smiles:OC(Br)(Br)C(Br)OF H298:-46.32 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)CF smiles:OC(Br)(Br)C(Br)CF H298:-91.03 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)C(Br)Br smiles:FC#CC(Br)C(Br)Br H298:32.93 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)C(Br)Br smiles:ClCC(Br)C(Br)Br H298:-13.35 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)CBr smiles:ClCC(Br)(Br)CBr H298:-16.20 kcal/mol
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
        Cpdata = ([-0.35531,-0.246446,-0.194353,-0.084457,-0.0800933,-0.0518484,0.236869],'cal/(mol*K)','+|-',[0.10744,0.12421,0.127283,0.125574,0.109172,0.0942795,0.0750809]),
        H298 = (3.01542,'kcal/mol','+|-',0.390156),
        S298 = (0.69263,'cal/(mol*K)','+|-',0.253371),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODCDC(Cl)C(F)Cl smiles:O=C=C(Cl)C(F)Cl H298:-64.71 kcal/mol
library:CHOFCl_G4 label:ODCDC(Cl)C(F)F smiles:O=C=C(Cl)C(F)F H298:-109.43 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(O)(Cl)Cl smiles:C=C(F)C(O)(Cl)Cl H298:-92.40 kcal/mol
library:CHOFCl_G4 label:CCDC(F)C(F)Cl smiles:CC=C(F)C(F)Cl H298:-98.81 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)C(F)Cl smiles:OC=C(Cl)C(F)Cl H298:-95.22 kcal/mol
library:CHOFCl_G4 label:CCDC(Cl)C(F)F smiles:CC=C(Cl)C(F)F H298:-106.32 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(C)(F)Cl smiles:C=C(F)C(C)(F)Cl H298:-103.08 kcal/mol
library:CHOFCl_G4 label:CCDC(Cl)C(F)Cl smiles:CC=C(Cl)C(F)Cl H298:-61.04 kcal/mol
library:CHOFCl_G4 label:CDCDC(F)C(F)Cl smiles:C=C=C(F)C(F)Cl H298:-51.79 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)Cl smiles:C=C(F)C(Cl)Cl H298:-49.98 kcal/mol
library:CHOFCl_G4 label:CCDC(F)C(Cl)Cl smiles:CC=C(F)C(Cl)Cl H298:-58.00 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(C)(Cl)Cl smiles:C=C(F)C(C)(Cl)Cl H298:-59.84 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)C(F)F smiles:OC=C(Cl)C(F)F H298:-140.56 kcal/mol
library:CHOFCl_G4 label:CDCDC(F)C(Cl)Cl smiles:C=C=C(F)C(Cl)Cl H298:-10.93 kcal/mol
library:CHOFCl_G4 label:FCDC(F)C(Cl)Cl smiles:FC=C(F)C(Cl)Cl H298:-89.17 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(O)(F)Cl smiles:C=C(F)C(O)(F)Cl H298:-138.53 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)Cl smiles:C=C(F)C(F)Cl H298:-91.02 kcal/mol
library:CHOFCl_G4 label:FCDC(F)C(F)Cl smiles:FC=C(F)C(F)Cl H298:-129.92 kcal/mol
library:CHOFClBr_G4 label:FCDC(F)C(Cl)Br smiles:FC=C(F)C(Cl)Br H298:-77.80 kcal/mol
library:CHOFClBr_G4 label:CDCDC(F)C(Cl)Br smiles:C=C=C(F)C(Cl)Br H298:0.35 kcal/mol
library:CHOFClBr_G4 label:CCDC(Br)C(F)Cl smiles:CC=C(Br)C(F)Cl H298:-49.25 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(C)(Cl)Br smiles:C=C(F)C(C)(Cl)Br H298:-48.30 kcal/mol
library:CHOFClBr_G4 label:CCDC(F)C(Cl)Br smiles:CC=C(F)C(Cl)Br H298:-46.70 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)Br smiles:C=C(F)C(Cl)Br H298:-38.60 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Br)Br smiles:FC=C(Cl)C(Br)Br H298:-30.31 kcal/mol
library:CHOFClBr_G4 label:ODCDC(Br)C(F)Cl smiles:O=C=C(Br)C(F)Cl H298:-54.98 kcal/mol
library:CHOFClBr_G4 label:OCDC(Br)C(F)Cl smiles:OC=C(Br)C(F)Cl H298:-80.46 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Cl)Br smiles:FC=C(Cl)C(Cl)Br H298:-41.49 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(O)(Cl)Br smiles:C=C(F)C(O)(Cl)Br H298:-80.32 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)Br smiles:C=C(F)C(Br)Br H298:-27.29 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)Br smiles:FC=C(F)C(F)Br H298:-117.56 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)DCF smiles:CC(Br)(Br)C(F)=CF H298:-75.93 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)Br smiles:C=C(F)C(F)Br H298:-78.79 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(C)(Br)Br smiles:C=C(F)C(C)(Br)Br H298:-36.73 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(O)(F)Br smiles:C=C(F)C(O)(F)Br H298:-125.66 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)DCOBr smiles:FC(Br)C(Br)=COBr H298:-27.31 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)OBr smiles:C=C(F)C(Br)(Br)OBr H298:-27.70 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)F smiles:OC(Br)=C(Br)C(F)F H298:-118.56 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)Br smiles:OC=C(Br)C(F)Br H298:-71.62 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(Br)Br smiles:CC=C(F)C(Br)Br H298:-35.49 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)F smiles:CC(Br)=C(Br)C(F)F H298:-89.02 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)Br smiles:FC=C(F)C(Br)Br H298:-66.55 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)Br smiles:O=C=C(Br)C(F)Br H298:-42.74 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(Br)Br smiles:C=C=C(F)C(Br)Br H298:11.52 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)F smiles:OC=C(Br)C(F)F H298:-129.38 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)OBr smiles:C=C(F)C(F)(Br)OBr H298:-84.37 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)Br smiles:CC(Br)=C(Br)C(F)Br H298:-29.49 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(F)Br smiles:C=C=C(F)C(F)Br H298:-39.57 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)DCF smiles:OC(Br)(Br)C(F)=CF H298:-107.58 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)DCOBr smiles:FC(F)C(Br)=COBr H298:-84.74 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)DCF smiles:OC(F)(Br)C(F)=CF H298:-161.23 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(C)(F)Br smiles:C=C(F)C(C)(F)Br H298:-90.79 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(F)Br smiles:FC(F)=C(F)C(F)Br H298:-162.37 kcal/mol
library:CHOFBr_G4 label:FCCDC(F)C(Br)Br smiles:FCC=C(F)C(Br)Br H298:-76.71 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(Br)Br smiles:FC(F)=C(F)C(Br)Br H298:-111.56 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)DCCBr smiles:FC(F)C(Br)=CCBr H298:-86.98 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)F smiles:O=C=C(Br)C(F)F H298:-99.70 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(O)(Br)Br smiles:C=C(F)C(O)(Br)Br H298:-68.36 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)DCF smiles:CC(F)(Br)C(F)=CF H298:-129.76 kcal/mol
library:CHOFBr_G4 label:FCCDC(F)C(F)Br smiles:FCC=C(F)C(F)Br H298:-128.18 kcal/mol
library:CHOFBr_G4 label:FCDCDC(F)C(Br)Br smiles:FC=C=C(F)C(Br)Br H298:-29.65 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)CBr smiles:C=C(F)C(F)(Br)CBr H298:-83.28 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(Br)Br smiles:CC(F)=C(F)C(Br)Br H298:-77.72 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)Br smiles:OC(Br)=C(Br)C(F)Br H298:-61.66 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)Br smiles:CC=C(Br)C(F)Br H298:-37.08 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(F)Br smiles:CC(F)=C(F)C(F)Br H298:-130.06 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)CBr smiles:C=C(F)C(Br)(Br)CBr H298:-29.64 kcal/mol
library:CHOFBr_G4 label:FCDCDC(F)C(F)Br smiles:FC=C=C(F)C(F)Br H298:-80.44 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)F smiles:CC=C(Br)C(F)F H298:-94.65 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(F)Br smiles:CC=C(F)C(F)Br H298:-86.59 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Cl)Br smiles:C=C=C(Cl)C(Cl)Br H298:36.40 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)Br smiles:C=C(Cl)C(Br)Br H298:11.52 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(C)(Cl)Br smiles:C=C(Cl)C(C)(Cl)Br H298:-9.01 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)C(Cl)Br smiles:CC=C(Br)C(Cl)Br H298:3.01 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(C)(Br)Br smiles:C=C(Cl)C(C)(Br)Br H298:2.83 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Cl smiles:OC=C(Br)C(Cl)Cl H298:-42.93 kcal/mol
library:CHOClBr_G4 label:ODCDC(Br)C(Cl)Br smiles:O=C=C(Br)C(Cl)Br H298:-1.95 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)Br smiles:C=C(Cl)C(Cl)Br H298:0.17 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Br)Br smiles:C=C=C(Cl)C(Br)Br H298:47.64 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Br)Br smiles:ClC=C(Cl)C(Br)Br H298:6.40 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(O)(Cl)Br smiles:C=C(Cl)C(O)(Cl)Br H298:-41.22 kcal/mol
library:CHOClBr_G4 label:ODCDC(Br)C(Cl)Cl smiles:O=C=C(Br)C(Cl)Cl H298:-13.41 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Br smiles:OC=C(Br)C(Cl)Br H298:-31.52 kcal/mol
library:CHOClBr_G4 label:CCDC(Cl)C(Br)Br smiles:CC=C(Cl)C(Br)Br H298:2.56 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)C(Cl)Cl smiles:CC=C(Br)C(Cl)Cl H298:-8.36 kcal/mol
library:CHOClBr_G4 label:CCDC(Cl)C(Cl)Br smiles:CC=C(Cl)C(Cl)Br H298:-8.75 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(O)(Br)Br smiles:C=C(Cl)C(O)(Br)Br H298:-29.20 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Cl)Br smiles:ClC=C(Cl)C(Cl)Br H298:-4.69 kcal/mol
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
        Cpdata = ([-0.389369,-0.117035,0.0666284,0.252965,0.322479,0.364131,0.694661],'cal/(mol*K)','+|-',[0.164073,0.189682,0.194376,0.191766,0.166719,0.143975,0.114657]),
        H298 = (2.49189,'kcal/mol','+|-',0.595812),
        S298 = (-1.15857,'cal/(mol*K)','+|-',0.386926),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODCDC(Cl)C(Cl)Cl smiles:O=C=C(Cl)C(Cl)Cl H298:-23.18 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-56.21 kcal/mol
library:CHOCl_G4 label:ClC(DCC(Cl)Cl)C(Cl)Cl smiles:ClC(=CC(Cl)Cl)C(Cl)Cl H298:-28.03 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCDC(Cl)C(Cl)Cl smiles:ClC(Cl)=C=C(Cl)C(Cl)Cl H298:18.38 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)Cl H298:-16.23 kcal/mol
library:CHOCl_G4 label:ClC(DCC(Cl)(Cl)Cl)C(Cl)Cl smiles:ClC(=CC(Cl)(Cl)Cl)C(Cl)Cl H298:-26.46 kcal/mol
library:CHOCl_G4 label:CCDC(Cl)C(Cl)Cl smiles:CC=C(Cl)C(Cl)Cl H298:-20.12 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)CCl smiles:C=C(Cl)C(Cl)(Cl)CCl H298:-24.81 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-26.72 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)Cl)C(Cl)Cl smiles:ClC(=C(Cl)C(Cl)Cl)C(Cl)Cl H298:-32.21 kcal/mol
library:CHOCl_G4 label:ClOCDC(Cl)C(Cl)Cl smiles:ClOC=C(Cl)C(Cl)Cl H298:-12.48 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)CCl smiles:ClC=C(Cl)C(Cl)(Cl)CCl H298:-29.97 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-24.56 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-31.97 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(O)(Cl)Cl smiles:C=C(Cl)C(O)(Cl)Cl H298:-53.35 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-24.49 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)Cl smiles:C=C(Cl)C(Cl)Cl H298:-11.25 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)OCl smiles:ClC=C(Cl)C(Cl)(Cl)OCl H298:-19.65 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)C(Cl)Cl smiles:OC(Cl)=C(Cl)C(Cl)Cl H298:-59.29 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-28.26 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)Cl H298:-19.32 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)Cl H298:-27.36 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-17.72 kcal/mol
library:CHOCl_G4 label:ClCCDC(Cl)C(Cl)Cl smiles:ClCC=C(Cl)C(Cl)Cl H298:-23.73 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)DCCl smiles:OC(Cl)(Cl)C(Cl)=CCl H298:-58.64 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)C(Cl)Cl smiles:OC=C(Cl)C(Cl)Cl H298:-54.16 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)C(Cl)Cl smiles:CC(Cl)=C(Cl)C(Cl)Cl H298:-25.12 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(C)(Cl)Cl smiles:C=C(Cl)C(C)(Cl)Cl H298:-20.67 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:C=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-26.81 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-22.98 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)C(Cl)Cl smiles:ClOC(Cl)=C(Cl)C(Cl)Cl H298:-17.86 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)OCl smiles:C=C(Cl)C(Cl)(Cl)OCl H298:-14.66 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)Cl H298:-26.83 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-28.39 kcal/mol
library:CHOCl_G4 label:CDCDC(Cl)C(Cl)Cl smiles:C=C=C(Cl)C(Cl)Cl H298:25.04 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)DCCl smiles:CC(Cl)(Cl)C(Cl)=CCl H298:-25.82 kcal/mol
library:CHOCl_G4 label:ClCDCDC(Cl)C(Cl)Cl smiles:ClC=C=C(Cl)C(Cl)Cl H298:21.58 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)C(Cl)Cl smiles:FC=C(Cl)C(Cl)Cl H298:-53.06 kcal/mol
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
        Cpdata = ([0.0709673,0.0792507,-0.00327203,0.040078,-0.0211774,-0.0310914,0.284642],'cal/(mol*K)','+|-',[0.153267,0.17719,0.181575,0.179137,0.155739,0.134494,0.107106]),
        H298 = (3.51474,'kcal/mol','+|-',0.556574),
        S298 = (0.231255,'cal/(mol*K)','+|-',0.361444),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)(F)F smiles:FC=C(F)C(F)(F)C(F)(F)F H298:-332.04 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)DC(F)F smiles:OC(F)(F)C(F)=C(F)F H298:-269.96 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)C(F)F smiles:C=C(F)C(F)(F)C(F)F H298:-237.67 kcal/mol
library:CHOF_G4 label:FCCDC(F)C(F)F smiles:FCC=C(F)C(F)F H298:-184.76 kcal/mol
library:CHOF_G4 label:CCDC(F)C(F)F smiles:CC=C(F)C(F)F H298:-143.85 kcal/mol
library:CHOF_G4 label:FCDCDC(F)C(F)F smiles:FC=C=C(F)C(F)F H298:-138.30 kcal/mol
library:CHOF_G4 label:CDC(F)C(C)(F)F smiles:C=C(F)C(C)(F)F H298:-149.09 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)DC(F)F smiles:FOC(F)(F)C(F)=C(F)F H298:-232.08 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)C(F)(F)F smiles:C=C(F)C(F)(F)C(F)(F)F H298:-293.10 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)F smiles:FC=C(F)C(F)(F)C(F)F H298:-276.56 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)F smiles:C=C(F)C(F)F H298:-136.01 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)CF smiles:FC=C(F)C(F)(F)CF H298:-227.47 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)F smiles:FC=C(F)C(F)F H298:-175.17 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)F)C(F)F smiles:FC(=C(F)C(F)F)C(F)F H298:-274.12 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)DCF smiles:CC(F)(F)C(F)=CF H298:-188.50 kcal/mol
library:CHOF_G4 label:FOCDC(F)C(F)F smiles:FOC=C(F)C(F)F H298:-140.05 kcal/mol
library:CHOF_G4 label:FC(DCC(F)F)C(F)F smiles:FC(=CC(F)F)C(F)F H298:-237.17 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)OF smiles:FC=C(F)C(F)(F)OF H298:-188.95 kcal/mol
library:CHOF_G4 label:CDC(F)C(O)(F)F smiles:C=C(F)C(O)(F)F H298:-187.98 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)F smiles:FC(=C(F)C(F)(F)F)C(F)F H298:-329.07 kcal/mol
library:CHOF_G4 label:CDCDC(F)C(F)F smiles:C=C=C(F)C(F)F H298:-96.79 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)F smiles:FCC(F)=C(F)C(F)F H298:-223.99 kcal/mol
library:CHOF_G4 label:OCDC(F)C(F)F smiles:OC=C(F)C(F)F H298:-175.43 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)C(F)F smiles:OC(F)=C(F)C(F)F H298:-219.73 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)C(F)F smiles:FOC(F)=C(F)C(F)F H298:-183.03 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)F smiles:FC(F)=C(F)C(F)F H298:-219.25 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)C(F)F smiles:CC(F)=C(F)C(F)F H298:-186.76 kcal/mol
library:CHOF_G4 label:FC(DCC(F)(F)F)C(F)F smiles:FC(=CC(F)(F)F)C(F)F H298:-293.12 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)OF smiles:C=C(F)C(F)(F)OF H298:-149.98 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)DCF smiles:OC(F)(F)C(F)=CF H298:-227.38 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)CF smiles:C=C(F)C(F)(F)CF H298:-188.16 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)C(F)(F)F H298:-374.89 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)DC(F)F smiles:FCC(F)(F)C(F)=C(F)F H298:-270.34 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)F smiles:FC(F)=C(F)C(F)(F)C(F)F H298:-319.55 kcal/mol
library:CHOF_G4 label:ODCDC(F)C(F)F smiles:O=C=C(F)C(F)F H298:-139.76 kcal/mol
library:CHOF_G4 label:FC(F)DCDC(F)C(F)F smiles:FC(F)=C=C(F)C(F)F H298:-183.88 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)DC(F)F smiles:CC(F)(F)C(F)=C(F)F H298:-231.21 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)OBr smiles:C=C(F)C(F)(F)OBr H298:-145.71 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)C(F)F smiles:OC(Br)=C(F)C(F)F H298:-166.31 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)C(F)F smiles:CC(Br)=C(F)C(F)F H298:-136.64 kcal/mol
library:CHOFBr_G4 label:FC(DCCBr)C(F)F smiles:FC(=CCBr)C(F)F H298:-136.46 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)CBr smiles:C=C(F)C(F)(F)CBr H298:-139.82 kcal/mol
library:CHOFBr_G4 label:FC(DCOBr)C(F)F smiles:FC(=COBr)C(F)F H298:-131.05 kcal/mol
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
        Cpdata = ([-0.428533,-0.246962,-0.0818379,0.0834028,0.196705,0.213758,0.342099],'cal/(mol*K)','+|-',[0.213498,0.246822,0.25293,0.249534,0.216941,0.187347,0.149196]),
        H298 = (1.33585,'kcal/mol','+|-',0.775295),
        S298 = (0.329663,'cal/(mol*K)','+|-',0.503484),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCCDC(Br)C(Br)Br smiles:BrCC=C(Br)C(Br)Br H298:21.04 kcal/mol
library:CHOBr_G4 label:ODCDC(Br)C(Br)Br smiles:O=C=C(Br)C(Br)Br H298:9.22 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(O)(Br)Br smiles:C=C(Br)C(O)(Br)Br H298:-16.99 kcal/mol
library:CHOBr_G4 label:CCDC(Br)C(Br)Br smiles:CC=C(Br)C(Br)Br H298:14.31 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)Br smiles:C=C(Br)C(Br)Br H298:23.22 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(C)(Br)Br smiles:C=C(Br)C(C)(Br)Br H298:14.80 kcal/mol
library:CHOBr_G4 label:OCDC(Br)C(Br)Br smiles:OC=C(Br)C(Br)Br H298:-20.26 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)C(Br)Br smiles:BrOC=C(Br)C(Br)Br H298:23.64 kcal/mol
library:CHOBr_G4 label:CDCDC(Br)C(Br)Br smiles:C=C=C(Br)C(Br)Br H298:58.52 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)Br smiles:BrC=C(Br)C(Br)Br H298:29.46 kcal/mol
library:CHOFBr_G4 label:FCDCDC(Br)C(Br)Br smiles:FC=C=C(Br)C(Br)Br H298:18.92 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)Br smiles:FC=C(Br)C(Br)Br H298:-19.12 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)C(Br)Br smiles:FC(F)=C(Br)C(Br)Br H298:-65.37 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)C(Br)Br smiles:CC(F)=C(Br)C(Br)Br H298:-31.52 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)DCF smiles:CC(Br)(Br)C(Br)=CF H298:-27.79 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)DCF smiles:OC(Br)(Br)C(Br)=CF H298:-59.62 kcal/mol
library:CHOFBr_G4 label:FCCDC(Br)C(Br)Br smiles:FCC=C(Br)C(Br)Br H298:-26.87 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)C(Br)Br smiles:FC(Br)=C(Br)C(Br)Br H298:-11.97 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)C(Br)Br smiles:ClC=C(Br)C(Br)Br H298:17.96 kcal/mol
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
        Cpdata = ([-0.115975,-0.0852516,-0.0538502,-0.0511812,-0.0526672,-0.031879,0.0569412],'cal/(mol*K)','+|-',[0.0365618,0.0422686,0.0433146,0.0427329,0.0371514,0.0320833,0.02555]),
        H298 = (1.22221,'kcal/mol','+|-',0.13277),
        S298 = (0.212658,'cal/(mol*K)','+|-',0.0862222),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:FCC(F)CCl smiles:FCC(F)CCl H298:-120.85 kcal/mol
library:CHOFCl_G4 label:CC(C)(Cl)CF smiles:CC(C)(Cl)CF H298:-87.57 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)CCl smiles:FC(F)C(F)CCl H298:-172.53 kcal/mol
library:CHOFCl_G4 label:OC(O)(Cl)CF smiles:OC(O)(Cl)CF H298:-157.39 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(CF)CCl smiles:CC(Cl)(CF)CCl H298:-91.88 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)OCCl smiles:FCC(Cl)OCCl H298:-114.37 kcal/mol
library:CHOFCl_G4 label:CC(F)C(Cl)CCl smiles:CC(F)C(Cl)CCl H298:-92.01 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)CCCl smiles:FCC(Cl)CCCl H298:-89.29 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)CF smiles:CC(Cl)C(F)CF H298:-129.57 kcal/mol
library:CHOFCl_G4 label:FCDCC(F)CCl smiles:FC=CC(F)CCl H298:-96.48 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)CCl smiles:FCC(Cl)CCl H298:-81.91 kcal/mol
library:CHOFCl_G4 label:CCC(F)CCl smiles:CCC(F)CCl H298:-84.02 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)CCl smiles:C=C(F)C(F)CCl H298:-98.42 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)CF smiles:CCC(Cl)CF H298:-82.94 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)C(Cl)Cl smiles:FCC(Cl)C(Cl)Cl H298:-84.61 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)CF smiles:O=CC(Cl)CF H298:-91.94 kcal/mol
library:CHOFCl_G4 label:OC(F)C(Cl)OCl smiles:OC(F)C(Cl)OCl H298:-118.40 kcal/mol
library:CHOFCl_G4 label:CC(F)(CCl)CCl smiles:CC(F)(CCl)CCl H298:-93.92 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(CF)OCl smiles:OC(Cl)(CF)OCl H298:-119.02 kcal/mol
library:CHOFCl_G4 label:OC(F)C(O)Cl smiles:OC(F)C(O)Cl H298:-158.03 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)CF smiles:OCC(Cl)CF H298:-113.37 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)CF smiles:OC(Cl)C(Cl)CF H298:-121.54 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)OF smiles:OC(Cl)C(F)OF H298:-122.10 kcal/mol
library:CHOFCl_G4 label:CDCC(F)CCl smiles:C=CC(F)CCl H298:-51.46 kcal/mol
library:CHOFCl_G4 label:OC(Cl)CF smiles:OC(Cl)CF H298:-109.48 kcal/mol
library:CHOFCl_G4 label:CC(F)C(F)CCl smiles:CC(F)C(F)CCl H298:-130.63 kcal/mol
library:CHOFCl_G4 label:CC(C)(F)CCl smiles:CC(C)(F)CCl H298:-89.73 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)CF smiles:OC(Cl)C(F)CF H298:-160.50 kcal/mol
library:CHOFCl_G4 label:FC#CC(F)CCl smiles:FC#CC(F)CCl H298:-36.28 kcal/mol
library:CHOFCl_G4 label:OC(F)(CF)CCl smiles:OC(F)(CF)CCl H298:-169.98 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(Cl)CF smiles:O=C(Cl)C(Cl)CF H298:-107.52 kcal/mol
library:CHOFCl_G4 label:CC(F)(CCl)OCl smiles:CC(F)(CCl)OCl H298:-90.47 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(CF)CCl smiles:OC(Cl)(CF)CCl H298:-125.33 kcal/mol
library:CHOFCl_G4 label:CC(F)CCl smiles:CC(F)CCl H298:-79.10 kcal/mol
library:CHOFCl_G4 label:CC(O)(Cl)CF smiles:CC(O)(Cl)CF H298:-120.52 kcal/mol
library:CHOFCl_G4 label:CC(Cl)CF smiles:CC(Cl)CF H298:-78.01 kcal/mol
library:CHOFCl_G4 label:FCCC(F)CCl smiles:FCCC(F)CCl H298:-128.10 kcal/mol
library:CHOFCl_G4 label:CC(O)(F)CCl smiles:CC(O)(F)CCl H298:-129.19 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)OCl smiles:FCC(Cl)OCl H298:-73.82 kcal/mol
library:CHOFCl_G4 label:CC(F)(CF)CCl smiles:CC(F)(CF)CCl H298:-131.11 kcal/mol
library:CHOFCl_G4 label:OOC(Cl)CF smiles:OOC(Cl)CF H298:-90.38 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(Cl)CF smiles:CC(Cl)C(Cl)CF H298:-90.28 kcal/mol
library:CHOFCl_G4 label:C#CC(F)CCl smiles:C#CC(F)CCl H298:-7.78 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)COCl smiles:FCC(Cl)COCl H298:-77.96 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(CF)OCl smiles:CC(Cl)(CF)OCl H298:-85.11 kcal/mol
library:CHOFCl_G4 label:CC(F)C(Cl)OCl smiles:CC(F)C(Cl)OCl H298:-82.71 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)OOCl smiles:FCC(Cl)OOCl H298:-57.50 kcal/mol
library:CHOFCl_G4 label:CC(F)C(O)Cl smiles:CC(F)C(O)Cl H298:-120.09 kcal/mol
library:CHOFCl_G4 label:CC(F)C(C)Cl smiles:CC(F)C(C)Cl H298:-88.19 kcal/mol
library:CHOFCl_G4 label:COC(Cl)CF smiles:COC(Cl)CF H298:-106.37 kcal/mol
library:CHOFCl_G4 label:FCCCl smiles:FCCCl H298:-68.53 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)CBr smiles:FC(F)C(Cl)CBr H298:-122.76 kcal/mol
library:CHOFClBr_G4 label:FC#CC(Cl)CBr smiles:FC#CC(Cl)CBr H298:13.50 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)OBr smiles:CC(F)C(Cl)OBr H298:-80.68 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)OOBr smiles:FCC(Cl)OOBr H298:-54.15 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(CF)OBr smiles:CC(Cl)(CF)OBr H298:-82.23 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)COBr smiles:FCC(Cl)COBr H298:-74.61 kcal/mol
library:CHOFClBr_G4 label:FCDCC(Cl)CBr smiles:FC=CC(Cl)CBr H298:-47.45 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)OBr smiles:FCC(Cl)OBr H298:-71.00 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)CF smiles:O=C(Br)C(Cl)CF H298:-95.04 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)CF smiles:CC(Br)C(Cl)CF H298:-79.46 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)CBr smiles:FC(Cl)C(Cl)CBr H298:-77.50 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(CF)CBr smiles:OC(Cl)(CF)CBr H298:-114.32 kcal/mol
library:CHOFClBr_G4 label:CC(F)(CCl)OBr smiles:CC(F)(CCl)OBr H298:-87.82 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)CBr smiles:C=C(F)C(Cl)CBr H298:-48.12 kcal/mol
library:CHOFClBr_G4 label:FCCC(Cl)CBr smiles:FCCC(Cl)CBr H298:-78.36 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(CF)OBr smiles:OC(Cl)(CF)OBr H298:-116.47 kcal/mol
library:CHOFClBr_G4 label:CC(F)(CCl)CBr smiles:CC(F)(CCl)CBr H298:-82.84 kcal/mol
library:CHOFClBr_G4 label:OC(F)C(Cl)OBr smiles:OC(F)C(Cl)OBr H298:-117.37 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Cl)Br smiles:FCC(Cl)C(Cl)Br H298:-73.02 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)CBr smiles:FCC(Cl)CBr H298:-70.78 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Br)Br smiles:FCC(Cl)C(Br)Br H298:-61.63 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)CCBr smiles:FCC(Cl)CCBr H298:-78.23 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)OCBr smiles:FCC(Cl)OCBr H298:-102.56 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)CBr smiles:CC(F)C(Cl)CBr H298:-79.53 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(CF)CBr smiles:CC(Cl)(CF)CBr H298:-80.74 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)OF smiles:OC(Br)C(Cl)OF H298:-67.50 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)CF smiles:OC(Br)C(Cl)CF H298:-111.55 kcal/mol
library:CHOFBr_G4 label:FCCBr smiles:FCCBr H298:-58.02 kcal/mol
library:CHOFBr_G4 label:OCC(Br)CF smiles:OCC(Br)CF H298:-102.29 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CF)CBr smiles:FCC(F)(CF)CBr H298:-161.24 kcal/mol
library:CHOFBr_G4 label:CC(F)C(C)Br smiles:CC(F)C(C)Br H298:-76.92 kcal/mol
library:CHOFBr_G4 label:CC(F)C(O)Br smiles:CC(F)C(O)Br H298:-107.99 kcal/mol
library:CHOFBr_G4 label:OC(Br)CF smiles:OC(Br)CF H298:-97.34 kcal/mol
library:CHOFBr_G4 label:CCC(Br)CF smiles:CCC(Br)CF H298:-71.90 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)OBr smiles:FCC(F)C(Br)OBr H298:-109.69 kcal/mol
library:CHOFBr_G4 label:C#CC(F)CBr smiles:C#CC(F)CBr H298:3.36 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)C(Br)Br smiles:OC(Br)(CF)C(Br)Br H298:-93.20 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)OBr smiles:CC(F)(CBr)OBr H298:-77.46 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)CBr smiles:FCC(Br)C(Br)CBr H298:-60.06 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)CF smiles:O=CC(Br)CF H298:-81.14 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)CF smiles:CC(Br)C(Br)CF H298:-68.53 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)Br smiles:CC(F)(CBr)C(F)Br H298:-114.70 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(Br)Br smiles:CC(F)(CBr)C(Br)Br H298:-62.22 kcal/mol
library:CHOFBr_G4 label:FC(CBr)C(F)(F)F smiles:FC(CBr)C(F)(F)F H298:-218.24 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)CBr smiles:CC(F)(F)C(F)CBr H298:-174.71 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)OBr smiles:OC(Br)(CF)OBr H298:-103.85 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)CBr smiles:CC(F)(CF)CBr H298:-119.99 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)CBr smiles:CC(O)(F)CBr H298:-118.14 kcal/mol
library:CHOFBr_G4 label:FCCC(F)CBr smiles:FCCC(F)CBr H298:-117.03 kcal/mol
library:CHOFBr_G4 label:OC(F)(CBr)C(F)F smiles:OC(F)(CBr)C(F)F H298:-210.81 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OBr smiles:FCC(Br)OBr H298:-59.13 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)C(F)F smiles:OC(Br)C(F)C(F)F H298:-201.16 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)Br smiles:FCC(Br)C(Br)Br H298:-50.50 kcal/mol
library:CHOFBr_G4 label:CC(F)CBr smiles:CC(F)CBr H298:-68.05 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)C(Br)Br smiles:CC(Br)(CF)C(Br)Br H298:-60.48 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)CF smiles:O=C(Br)C(Br)CF H298:-84.62 kcal/mol
library:CHOFBr_G4 label:FCC(Br)COBr smiles:FCC(Br)COBr H298:-63.57 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OOBr smiles:FCC(Br)OOBr H298:-42.27 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)CBr smiles:OC(F)(CF)CBr H298:-158.98 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)OBr smiles:FCC(F)(CBr)OBr H298:-117.97 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CC(Br)Br smiles:FCC(Br)CC(Br)Br H298:-60.44 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)CF smiles:CC(C)(Br)CF H298:-76.19 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)CBr smiles:FCC(Br)(CBr)CBr H298:-62.47 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)OBr smiles:CC(F)C(Br)OBr H298:-67.91 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)CF smiles:OC(O)(Br)CF H298:-144.59 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)CBr smiles:CC(Br)(CF)CBr H298:-69.43 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)CBr smiles:FC#CC(F)CBr H298:-25.37 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)OBr smiles:CC(Br)(CF)OBr H298:-70.32 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)CBr smiles:CC(C)(F)CBr H298:-78.64 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)CBr smiles:CC(F)C(F)CBr H298:-120.06 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)CF smiles:CC(Br)(Br)C(Br)CF H298:-60.33 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)CBr smiles:FC=C(F)C(F)CBr H298:-127.57 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)OBr smiles:FCC(Br)(CBr)OBr H298:-62.11 kcal/mol
library:CHOFBr_G4 label:CDCC(F)CBr smiles:C=CC(F)CBr H298:-40.34 kcal/mol
library:CHOFBr_G4 label:COC(Br)CF smiles:COC(Br)CF H298:-94.76 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)CBr smiles:CC(F)C(Br)CBr H298:-69.70 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)CBr smiles:FCC(F)(CBr)CBr H298:-112.82 kcal/mol
library:CHOFBr_G4 label:FOC(F)C(Br)OBr smiles:FOC(F)C(Br)OBr H298:-70.71 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OCBr smiles:FCC(Br)OCBr H298:-90.86 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)CBr smiles:FC(F)=CC(F)CBr H298:-134.83 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)CF smiles:CC(Br)C(F)CF H298:-118.27 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CCBr smiles:FCC(Br)CCBr H298:-67.17 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)CF smiles:OC(Br)C(Br)CF H298:-100.52 kcal/mol
library:CHOFBr_G4 label:OC(F)C(O)Br smiles:OC(F)C(O)Br H298:-146.00 kcal/mol
library:CHOFBr_G4 label:CC(Br)CF smiles:CC(Br)CF H298:-66.70 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)C(Br)Br smiles:CC(F)C(Br)C(Br)Br H298:-60.56 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)C(F)F smiles:CC(Br)C(F)C(F)F H298:-170.09 kcal/mol
library:CHOFBr_G4 label:OOC(Br)CF smiles:OOC(Br)CF H298:-78.52 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)CBr smiles:FCC(F)C(F)CBr H298:-159.78 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CBr smiles:FCC(Br)CBr H298:-59.71 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)(Br)Br smiles:FCC(Br)C(Br)(Br)Br H298:-38.74 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)CBr smiles:C=C(F)C(F)CBr H298:-87.36 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(OBr)OBr smiles:FCC(Br)(OBr)OBr H298:-63.76 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)CBr smiles:OC(Br)(CF)CBr H298:-101.26 kcal/mol
library:CHOFBr_G4 label:CCC(F)CBr smiles:CCC(F)CBr H298:-73.06 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)CF smiles:OC(Br)C(F)CF H298:-148.71 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)CBr smiles:FC=CC(F)CBr H298:-85.38 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)CBr smiles:CC(F)(CBr)CBr H298:-71.86 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OC(Br)Br smiles:FCC(Br)OC(Br)Br H298:-81.88 kcal/mol
library:CHOFBr_G4 label:OC(F)C(Br)OBr smiles:OC(F)C(Br)OBr H298:-105.42 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)OBr smiles:FCC(Br)C(Br)OBr H298:-60.33 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)OF smiles:OC(Br)C(F)OF H298:-109.82 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)CF smiles:CC(O)(Br)CF H298:-108.85 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)F smiles:CC(F)(CBr)C(F)F H298:-172.71 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)CBr smiles:FCC(F)C(Br)CBr H298:-110.02 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)CBr smiles:FC(F)C(F)CBr H298:-161.40 kcal/mol
library:CHOFBr_G4 label:FC(F)CC(F)CBr smiles:FC(F)CC(F)CBr H298:-169.99 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)CF smiles:OC(Br)(Br)C(Br)CF H298:-91.03 kcal/mol
library:CHOFBr_G4 label:FCC(F)CBr smiles:FCC(F)CBr H298:-108.84 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CBr)CBr smiles:CC(Cl)(CBr)CBr H298:-32.36 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)CBr smiles:ClCC(Cl)CBr H298:-33.50 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)OOBr smiles:ClCC(Br)OOBr H298:-4.76 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)COBr smiles:ClCC(Br)COBr H298:-25.98 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)CCl smiles:CC(Br)C(Cl)CCl H298:-42.26 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)OCl smiles:OC(Br)C(Cl)OCl H298:-64.12 kcal/mol
library:CHOClBr_G4 label:ClCCC(Cl)CBr smiles:ClCCC(Cl)CBr H298:-40.63 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)CBr smiles:CCC(Cl)CBr H298:-34.43 kcal/mol
library:CHOClBr_G4 label:CC(Cl)CBr smiles:CC(Cl)CBr H298:-29.13 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)CBr smiles:CC(Cl)C(Cl)CBr H298:-41.86 kcal/mol
library:CHOClBr_G4 label:CC(C)(Cl)CBr smiles:CC(C)(Cl)CBr H298:-38.60 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)CBr smiles:CC(Cl)C(Br)CBr H298:-30.66 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(Br)OBr smiles:OC(Cl)C(Br)OBr H298:-59.79 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)CBr smiles:C=C(Cl)C(Cl)CBr H298:-11.03 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)CBr smiles:C=CC(Cl)CBr H298:-2.49 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)OBr smiles:CC(Br)(CCl)OBr H298:-33.00 kcal/mol
library:CHOClBr_G4 label:OC(Br)(CCl)CBr smiles:OC(Br)(CCl)CBr H298:-64.30 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)CCl smiles:CC(Br)C(Br)CCl H298:-31.33 kcal/mol
library:CHOClBr_G4 label:CC(O)(Cl)CBr smiles:CC(O)(Cl)CBr H298:-72.67 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)CBr smiles:C#CC(Cl)CBr H298:41.77 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CCl)CBr smiles:CC(Cl)(CCl)CBr H298:-43.28 kcal/mol
library:CHOClBr_G4 label:ClCCBr smiles:ClCCBr H298:-20.50 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)CCl smiles:O=CC(Br)CCl H298:-43.90 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)CBr smiles:ClCC(Br)CBr H298:-22.63 kcal/mol
library:CHOClBr_G4 label:COC(Br)CCl smiles:COC(Br)CCl H298:-57.26 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)OBr smiles:ClCC(Br)OBr H298:-21.57 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(CCl)CBr smiles:OC(Cl)(CCl)CBr H298:-76.21 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Cl)CBr smiles:ClC=CC(Cl)CBr H298:-9.51 kcal/mol
library:CHOClBr_G4 label:OC(Br)CCl smiles:OC(Br)CCl H298:-60.22 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)CCl smiles:OC(Br)C(Br)CCl H298:-60.44 kcal/mol
library:CHOClBr_G4 label:OC(Br)(CCl)OBr smiles:OC(Br)(CCl)OBr H298:-66.42 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)CBr smiles:CC(Br)(CCl)CBr H298:-32.04 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(O)Br smiles:OC(Cl)C(O)Br H298:-102.28 kcal/mol
library:CHOClBr_G4 label:ClC#CC(Cl)CBr smiles:ClC#CC(Cl)CBr H298:41.23 kcal/mol
library:CHOClBr_G4 label:CCC(Br)CCl smiles:CCC(Br)CCl H298:-34.35 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)OBr smiles:CC(Cl)C(Br)OBr H298:-29.04 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)C(Br)Br smiles:ClCC(Br)C(Br)Br H298:-13.35 kcal/mol
library:CHOClBr_G4 label:CC(Br)CCl smiles:CC(Br)CCl H298:-29.00 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)CBr smiles:ClC(Cl)C(Cl)CBr H298:-36.55 kcal/mol
library:CHOClBr_G4 label:OC(O)(Br)CCl smiles:OC(O)(Br)CCl H298:-107.09 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)CCl smiles:CC(C)(Br)CCl H298:-38.32 kcal/mol
library:CHOClBr_G4 label:OOC(Br)CCl smiles:OOC(Br)CCl H298:-40.89 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)CCl smiles:OC(Br)C(Cl)CCl H298:-72.07 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)CCl smiles:O=C(Br)C(Br)CCl H298:-47.67 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)CCl smiles:CC(O)(Br)CCl H298:-71.55 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)CCBr smiles:ClCC(Br)CCBr H298:-31.74 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(C)Br smiles:CC(Cl)C(C)Br H298:-37.00 kcal/mol
library:CHOClBr_G4 label:OCC(Br)CCl smiles:OCC(Br)CCl H298:-64.63 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(O)Br smiles:CC(Cl)C(O)Br H298:-67.91 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)OCBr smiles:ClCC(Br)OCBr H298:-53.47 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CBr)OBr smiles:CC(Cl)(CBr)OBr H298:-33.93 kcal/mol
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
        Cpdata = ([-0.195956,-0.124889,-0.0265957,0.0327574,0.0791913,0.118216,0.20349],'cal/(mol*K)','+|-',[0.0482979,0.0558366,0.0572183,0.0564499,0.0490768,0.0423819,0.0337515]),
        H298 = (1.17252,'kcal/mol','+|-',0.175389),
        S298 = (-0.116861,'cal/(mol*K)','+|-',0.113899),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,2-Dichloroethane smiles:ClCCCl H298:-31.20 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)C(Cl)(Cl)Cl smiles:CC(Cl)(CCl)C(Cl)(Cl)Cl H298:-56.96 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)CCl smiles:O=CC(Cl)CCl H298:-54.06 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)C(Cl)Cl H298:-64.73 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)OCl smiles:ClCC(Cl)OCl H298:-36.25 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)CC(Cl)Cl smiles:ClCC(Cl)CC(Cl)Cl H298:-56.92 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(O)Cl smiles:CC(Cl)C(O)Cl H298:-81.57 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(C)Cl smiles:CC(Cl)C(C)Cl H298:-48.20 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)C(Cl)(Cl)Cl smiles:OC(Cl)(CCl)C(Cl)(Cl)Cl H298:-90.00 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(CCl)C(Cl)(Cl)Cl H298:-58.50 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)CCl smiles:ClCC(Cl)(CCl)CCl H298:-57.97 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)CCl smiles:ClC=C(Cl)C(Cl)CCl H298:-27.32 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)CCl smiles:CC(Cl)(Cl)C(Cl)CCl H298:-57.76 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-56.00 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)CCl smiles:ClCC(Cl)C(Cl)(Cl)CCl H298:-61.87 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)C(Cl)Cl smiles:OC(Cl)C(Cl)C(Cl)Cl H298:-88.48 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)OCl smiles:CC(Cl)C(Cl)OCl H298:-44.39 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)CCl smiles:OC(Cl)C(Cl)CCl H298:-84.09 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)C(Cl)Cl smiles:CC(Cl)(CCl)C(Cl)Cl H298:-57.51 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)CCl smiles:O=C(Cl)C(Cl)CCl H298:-70.40 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)OCl smiles:ClOC(Cl)C(Cl)OCl H298:-38.19 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)CCl smiles:ClCC(Cl)C(Cl)CCl H298:-56.27 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)CDC(Cl)Cl smiles:ClCC(Cl)C=C(Cl)Cl H298:-25.10 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)CCl smiles:ClC#CC(Cl)CCl H298:30.28 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(O)Cl smiles:OC(Cl)C(O)Cl H298:-115.08 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(OCl)C(Cl)Cl smiles:ClCC(Cl)(OCl)C(Cl)Cl H298:-50.89 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-55.56 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)CCl smiles:ClC=CC(Cl)CCl H298:-19.91 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)C(Cl)Cl smiles:ClCC(Cl)C(Cl)C(Cl)Cl H298:-61.79 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)OCl smiles:CC(Cl)(CCl)OCl H298:-47.56 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)CCl smiles:OC(Cl)(CCl)CCl H298:-87.23 kcal/mol
library:CHOCl_G4 label:OCC(Cl)CCl smiles:OCC(Cl)CCl H298:-75.68 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)OOCl smiles:ClCC(Cl)OOCl H298:-19.87 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)C(Cl)Cl smiles:ClOC(Cl)C(Cl)C(Cl)Cl H298:-51.48 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)DC(Cl)Cl smiles:ClCC(Cl)C(Cl)=C(Cl)Cl H298:-30.56 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)OCl smiles:OC(Cl)(CCl)OCl H298:-81.44 kcal/mol
library:CHOCl_G4 label:CC(Cl)(CCl)CCl smiles:CC(Cl)(CCl)CCl H298:-54.32 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)COCl smiles:ClCC(Cl)COCl H298:-40.19 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)CCl smiles:C#CC(Cl)CCl H298:30.77 kcal/mol
library:CHOCl_G4 label:CC(O)(Cl)CCl smiles:CC(O)(Cl)CCl H298:-83.75 kcal/mol
library:CHOCl_G4 label:OOC(Cl)CCl smiles:OOC(Cl)CCl H298:-52.69 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)CCl smiles:C=CC(Cl)CCl H298:-13.46 kcal/mol
library:CHOCl_G4 label:OC(Cl)(CCl)C(Cl)Cl smiles:OC(Cl)(CCl)C(Cl)Cl H298:-89.76 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-88.64 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)CCl smiles:C=C(Cl)C(Cl)CCl H298:-20.12 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)OCl smiles:ClCC(Cl)C(Cl)OCl H298:-47.65 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-54.92 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)CC(Cl)(Cl)Cl smiles:ClCC(Cl)CC(Cl)(Cl)Cl H298:-56.82 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(OCl)OCl smiles:ClCC(Cl)(OCl)OCl H298:-43.23 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-50.55 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-60.27 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)Cl smiles:ClCC(Cl)C(Cl)Cl H298:-48.33 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)OC(Cl)Cl smiles:ClCC(Cl)OC(Cl)Cl H298:-80.56 kcal/mol
library:CHOCl_G4 label:CC(C)(Cl)CCl smiles:CC(C)(Cl)CCl H298:-49.63 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)CCl smiles:OC(Cl)(Cl)C(Cl)CCl H298:-89.99 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)CCl smiles:ClCOC(Cl)CCl H298:-76.81 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)OCl smiles:OC(Cl)C(Cl)OCl H298:-76.14 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)CCl smiles:CC(Cl)C(Cl)CCl H298:-51.86 kcal/mol
library:CHOCl_G4 label:CC(Cl)CCl smiles:CC(Cl)CCl H298:-40.15 kcal/mol
library:CHOCl_G4 label:OC(O)(Cl)CCl smiles:OC(O)(Cl)CCl H298:-119.86 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)OCl smiles:ClCC(Cl)C(Cl)(Cl)OCl H298:-51.63 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)Cl)C(Cl)Cl smiles:ClCC(Cl)(C(Cl)Cl)C(Cl)Cl H298:-58.79 kcal/mol
library:CHOCl_G4 label:CCC(Cl)CCl smiles:CCC(Cl)CCl H298:-45.41 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)C(Cl)(Cl)Cl H298:-48.51 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-62.52 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-48.72 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)C(Cl)Cl smiles:CC(Cl)C(Cl)C(Cl)Cl H298:-56.47 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)OCl smiles:ClCC(Cl)(CCl)OCl H298:-50.56 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)CCl smiles:ClCCC(Cl)CCl H298:-51.58 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)OC(Cl)(Cl)Cl smiles:ClCC(Cl)OC(Cl)(Cl)Cl H298:-81.11 kcal/mol
library:CHOCl_G4 label:OC(Cl)CCl smiles:OC(Cl)CCl H298:-72.39 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(CCl)C(Cl)Cl smiles:ClCC(Cl)(CCl)C(Cl)Cl H298:-60.43 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)CCl smiles:ClCC(Cl)CCl H298:-44.54 kcal/mol
library:CHOCl_G4 label:COC(Cl)CCl smiles:COC(Cl)CCl H298:-68.76 kcal/mol
library:CHOFCl_G4 label:CC(Cl)(CF)CCl smiles:CC(Cl)(CF)CCl H298:-91.88 kcal/mol
library:CHOFCl_G4 label:CC(F)C(Cl)CCl smiles:CC(F)C(Cl)CCl H298:-92.01 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)CCl smiles:FCC(Cl)CCl H298:-81.91 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)CF smiles:OC(Cl)C(Cl)CF H298:-121.54 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)OF smiles:OC(Cl)C(Cl)OF H298:-79.62 kcal/mol
library:CHOFCl_G4 label:FCCC(Cl)CCl smiles:FCCC(Cl)CCl H298:-89.35 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)CCl smiles:C=C(F)C(Cl)CCl H298:-59.19 kcal/mol
library:CHOFCl_G4 label:OC(Cl)(CF)CCl smiles:OC(Cl)(CF)CCl H298:-125.33 kcal/mol
library:CHOFCl_G4 label:FC(Cl)C(Cl)CCl smiles:FC(Cl)C(Cl)CCl H298:-88.88 kcal/mol
library:CHOFCl_G4 label:FCDCC(Cl)CCl smiles:FC=CC(Cl)CCl H298:-58.38 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(Cl)CF smiles:CC(Cl)C(Cl)CF H298:-90.28 kcal/mol
library:CHOFCl_G4 label:FC#CC(Cl)CCl smiles:FC#CC(Cl)CCl H298:2.53 kcal/mol
library:CHOFCl_G4 label:FC(F)C(Cl)CCl smiles:FC(F)C(Cl)CCl H298:-133.87 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)CBr smiles:ClCC(Cl)CBr H298:-33.50 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)CCl smiles:CC(Br)C(Cl)CCl H298:-42.26 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Br)Br smiles:ClCC(Cl)C(Br)Br H298:-24.43 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)CBr smiles:CC(Cl)C(Cl)CBr H298:-41.86 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(Cl)OBr smiles:OC(Cl)C(Cl)OBr H298:-71.59 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Cl)Br smiles:ClCC(Cl)C(Cl)Br H298:-35.77 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)COBr smiles:ClCC(Cl)COBr H298:-36.85 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CCl)CBr smiles:CC(Cl)(CCl)CBr H298:-43.28 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(CCl)OBr smiles:OC(Cl)(CCl)OBr H298:-78.89 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)OOBr smiles:ClCC(Cl)OOBr H298:-16.57 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)OCBr smiles:ClCC(Cl)OCBr H298:-65.04 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)CCBr smiles:ClCC(Cl)CCBr H298:-40.57 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(CCl)CBr smiles:OC(Cl)(CCl)CBr H298:-76.21 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CCl)OBr smiles:CC(Cl)(CCl)OBr H298:-44.82 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)CCl smiles:O=C(Br)C(Cl)CCl H298:-58.00 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)OBr smiles:CC(Cl)C(Cl)OBr H298:-41.09 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)CCl smiles:OC(Br)C(Cl)CCl H298:-72.07 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)OBr smiles:ClCC(Cl)OBr H298:-33.44 kcal/mol
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
        Cpdata = ([-0.126314,-0.0461699,0.0468318,0.0921387,0.110043,0.129437,0.182905],'cal/(mol*K)','+|-',[0.043313,0.0500736,0.0513127,0.0506237,0.0440115,0.0380076,0.0302679]),
        H298 = (1.69896,'kcal/mol','+|-',0.157287),
        S298 = (0.0397565,'cal/(mol*K)','+|-',0.102143),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,2-Difluoroethane smiles:FCCF H298:-107.03 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)OF smiles:FCC(F)(CF)OF H298:-172.72 kcal/mol
library:CHOF_G4 label:FCC(F)OF smiles:FCC(F)OF H298:-121.98 kcal/mol
library:CHOF_G4 label:CC(F)CF smiles:CC(F)CF H298:-116.60 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)CF smiles:C=C(F)C(F)CF H298:-136.33 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)CF smiles:FCC(F)(CF)CF H298:-209.77 kcal/mol
library:CHOF_G4 label:CC(O)(F)CF smiles:CC(O)(F)CF H298:-166.49 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)CF smiles:CC(F)(F)C(F)CF H298:-223.33 kcal/mol
library:CHOF_G4 label:FCC(F)CF smiles:FCC(F)CF H298:-158.06 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)(F)F)C(F)(F)F smiles:FCC(F)(C(F)(F)F)C(F)(F)F H298:-421.30 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)F smiles:FCC(F)C(F)F H298:-209.90 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)OF smiles:FOC(F)C(F)OF H298:-133.41 kcal/mol
library:CHOF_G4 label:OC(F)(CF)C(F)F smiles:OC(F)(CF)C(F)F H298:-259.20 kcal/mol
library:CHOF_G4 label:FCC(F)CDC(F)F smiles:FCC(F)C=C(F)F H298:-183.35 kcal/mol
library:CHOF_G4 label:CC(F)C(C)F smiles:CC(F)C(C)F H298:-126.78 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)(F)F smiles:FCC(F)(C(F)F)C(F)(F)F H298:-365.50 kcal/mol
library:CHOF_G4 label:CCC(F)CF smiles:CCC(F)CF H298:-121.23 kcal/mol
library:CHOF_G4 label:FCC(F)OC(F)F smiles:FCC(F)OC(F)F H298:-255.59 kcal/mol
library:CHOF_G4 label:OC(F)(CF)C(F)(F)F smiles:OC(F)(CF)C(F)(F)F H298:-313.99 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)CF smiles:FC=C(F)C(F)CF H298:-175.27 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)F smiles:FCC(F)C(F)(F)F H298:-266.99 kcal/mol
library:CHOF_G4 label:CC(F)C(F)C(F)F smiles:CC(F)C(F)C(F)F H298:-220.98 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)C(F)(F)F smiles:FOC(F)C(F)C(F)(F)F H298:-277.45 kcal/mol
library:CHOF_G4 label:FCC(F)OOF smiles:FCC(F)OOF H298:-109.37 kcal/mol
library:CHOF_G4 label:FC(C(F)C(F)(F)F)C(F)(F)F smiles:FC(C(F)C(F)(F)F)C(F)(F)F H298:-424.07 kcal/mol
library:CHOF_G4 label:CC(F)(CF)C(F)(F)F smiles:CC(F)(CF)C(F)(F)F H298:-277.92 kcal/mol
library:CHOF_G4 label:FCC(F)CC(F)F smiles:FCC(F)CC(F)F H298:-219.99 kcal/mol
library:CHOF_G4 label:OC(O)(F)CF smiles:OC(O)(F)CF H298:-206.61 kcal/mol
library:CHOF_G4 label:CC(C)(F)CF smiles:CC(C)(F)CF H298:-127.10 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)C(F)(F)F smiles:FCC(F)C(F)C(F)(F)F H298:-317.77 kcal/mol
library:CHOF_G4 label:FCDCC(F)CF smiles:FC=CC(F)CF H298:-134.50 kcal/mol
library:CHOF_G4 label:FCC(F)OC(F)(F)F smiles:FCC(F)OC(F)(F)F H298:-312.19 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)CF smiles:O=C(F)C(F)CF H298:-191.81 kcal/mol
library:CHOF_G4 label:FC#CC(F)CF smiles:FC#CC(F)CF H298:-74.35 kcal/mol
library:CHOF_G4 label:OC(F)CF smiles:OC(F)CF H298:-154.21 kcal/mol
library:CHOF_G4 label:CC(F)(CF)CF smiles:CC(F)(CF)CF H298:-169.36 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)CF smiles:FCC(F)C(F)(F)CF H298:-262.80 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)C(F)(F)F smiles:FC(F)C(F)C(F)C(F)(F)F H298:-367.06 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)C(F)F smiles:FCC(F)(CF)C(F)F H298:-261.93 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)F smiles:FCC(F)(C(F)F)C(F)F H298:-312.20 kcal/mol
library:CHOF_G4 label:OC(F)C(F)OF smiles:OC(F)C(F)OF H298:-167.37 kcal/mol
library:CHOF_G4 label:CC(F)(CF)OF smiles:CC(F)(CF)OF H298:-133.59 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)OF smiles:FCC(F)C(F)(F)OF H298:-223.34 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)DC(F)F smiles:FCC(F)C(F)=C(F)F H298:-219.99 kcal/mol
library:CHOF_G4 label:COC(F)CF smiles:COC(F)CF H298:-149.37 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)C(F)F smiles:FOC(F)C(F)C(F)F H298:-222.80 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)C(F)(F)F smiles:FCC(F)(OF)C(F)(F)F H298:-275.95 kcal/mol
library:CHOF_G4 label:FCC(F)CC(F)(F)F smiles:FCC(F)CC(F)(F)F H298:-277.64 kcal/mol
library:CHOF_G4 label:OC(F)C(F)CF smiles:OC(F)C(F)CF H298:-204.96 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)C(F)F smiles:FCC(F)C(F)C(F)F H298:-261.79 kcal/mol
library:CHOF_G4 label:OC(F)C(O)F smiles:OC(F)C(O)F H298:-201.91 kcal/mol
library:CHOF_G4 label:ODCC(F)CF smiles:O=CC(F)CF H298:-130.64 kcal/mol
library:CHOF_G4 label:OCC(F)CF smiles:OCC(F)CF H298:-151.68 kcal/mol
library:CHOF_G4 label:FCCC(F)CF smiles:FCCC(F)CF H298:-165.49 kcal/mol
library:CHOF_G4 label:C#CC(F)CF smiles:C#CC(F)CF H298:-45.83 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)CF smiles:FCC(F)C(F)CF H298:-209.28 kcal/mol
library:CHOF_G4 label:OC(F)C(F)C(F)(F)F smiles:OC(F)C(F)C(F)(F)F H298:-311.08 kcal/mol
library:CHOF_G4 label:CDCC(F)CF smiles:C=CC(F)CF H298:-91.25 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)C(F)F smiles:FCC(F)C(F)(F)C(F)F H298:-310.46 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)OF smiles:FCC(F)C(F)OF H298:-171.75 kcal/mol
library:CHOF_G4 label:FCC(F)COF smiles:FCC(F)COF H298:-123.22 kcal/mol
library:CHOF_G4 label:CC(F)C(F)OF smiles:CC(F)C(F)OF H298:-131.73 kcal/mol
library:CHOF_G4 label:OC(F)C(F)C(F)F smiles:OC(F)C(F)C(F)F H298:-257.09 kcal/mol
library:CHOF_G4 label:OOC(F)CF smiles:OOC(F)CF H298:-133.71 kcal/mol
library:CHOF_G4 label:FCOC(F)CF smiles:FCOC(F)CF H298:-199.88 kcal/mol
library:CHOF_G4 label:OC(F)(CF)CF smiles:OC(F)(CF)CF H298:-207.08 kcal/mol
library:CHOF_G4 label:CC(F)C(O)F smiles:CC(F)C(O)F H298:-164.67 kcal/mol
library:CHOF_G4 label:FCC(F)(CF)C(F)(F)F smiles:FCC(F)(CF)C(F)(F)F H298:-317.42 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)C(F)F smiles:FCC(F)(OF)C(F)F H298:-220.88 kcal/mol
library:CHOF_G4 label:CC(F)C(F)CF smiles:CC(F)C(F)CF H298:-168.87 kcal/mol
library:CHOF_G4 label:CC(F)(CF)C(F)F smiles:CC(F)(CF)C(F)F H298:-221.98 kcal/mol
library:CHOF_G4 label:OC(F)(CF)OF smiles:OC(F)(CF)OF H298:-169.47 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)C(F)(F)F smiles:FCC(F)C(F)(F)C(F)(F)F H298:-366.48 kcal/mol
library:CHOF_G4 label:CC(F)C(F)C(F)(F)F smiles:CC(F)C(F)C(F)(F)F H298:-276.26 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)OF smiles:FCC(F)(OF)OF H298:-130.33 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)CF smiles:OC(F)(F)C(F)CF H298:-262.54 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)C(F)F smiles:FC(F)C(F)C(F)C(F)F H298:-313.85 kcal/mol
library:CHOFCl_G4 label:FCC(F)CCl smiles:FCC(F)CCl H298:-120.85 kcal/mol
library:CHOFCl_G4 label:FCC(F)OOCl smiles:FCC(F)OOCl H298:-100.55 kcal/mol
library:CHOFCl_G4 label:FCC(F)COCl smiles:FCC(F)COCl H298:-117.10 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)CF smiles:CC(Cl)C(F)CF H298:-129.57 kcal/mol
library:CHOFCl_G4 label:CC(F)(CF)OCl smiles:CC(F)(CF)OCl H298:-128.70 kcal/mol
library:CHOFCl_G4 label:OC(F)(CF)OCl smiles:OC(F)(CF)OCl H298:-166.60 kcal/mol
library:CHOFCl_G4 label:FCC(F)C(F)Cl smiles:FCC(F)C(F)Cl H298:-165.30 kcal/mol
library:CHOFCl_G4 label:CC(F)C(F)CCl smiles:CC(F)C(F)CCl H298:-130.63 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)CF smiles:OC(Cl)C(F)CF H298:-160.50 kcal/mol
library:CHOFCl_G4 label:CC(F)C(F)OCl smiles:CC(F)C(F)OCl H298:-127.22 kcal/mol
library:CHOFCl_G4 label:OC(F)(CF)CCl smiles:OC(F)(CF)CCl H298:-169.98 kcal/mol
library:CHOFCl_G4 label:CC(F)(CF)CCl smiles:CC(F)(CF)CCl H298:-131.11 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)CF smiles:O=C(Cl)C(F)CF H298:-145.69 kcal/mol
library:CHOFCl_G4 label:OC(F)C(F)OCl smiles:OC(F)C(F)OCl H298:-161.59 kcal/mol
library:CHOFCl_G4 label:FCC(F)C(Cl)Cl smiles:FCC(F)C(Cl)Cl H298:-124.19 kcal/mol
library:CHOFCl_G4 label:FCC(F)CCCl smiles:FCC(F)CCCl H298:-127.93 kcal/mol
library:CHOFCl_G4 label:FCC(F)OCl smiles:FCC(F)OCl H298:-116.86 kcal/mol
library:CHOFCl_G4 label:FCC(F)OCCl smiles:FCC(F)OCCl H298:-157.08 kcal/mol
library:CHOFClBr_G4 label:FCC(F)C(Cl)Br smiles:FCC(F)C(Cl)Br H298:-112.51 kcal/mol
library:CHOFBr_G4 label:FCC(F)OCBr smiles:FCC(F)OCBr H298:-145.15 kcal/mol
library:CHOFBr_G4 label:FCC(F)OBr smiles:FCC(F)OBr H298:-113.63 kcal/mol
library:CHOFBr_G4 label:FCC(F)CCBr smiles:FCC(F)CCBr H298:-116.80 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CF)CBr smiles:FCC(F)(CF)CBr H298:-161.24 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)(Br)Br smiles:FCC(F)C(Br)(Br)Br H298:-89.52 kcal/mol
library:CHOFBr_G4 label:FOC(F)C(F)OBr smiles:FOC(F)C(F)OBr H298:-126.17 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)CF smiles:CC(F)(Br)C(F)CF H298:-164.23 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)OBr smiles:FCC(F)C(Br)OBr H298:-109.69 kcal/mol
library:CHOFBr_G4 label:FCC(F)OC(Br)Br smiles:FCC(F)OC(Br)Br H298:-135.82 kcal/mol
library:CHOFBr_G4 label:OC(F)C(F)OBr smiles:OC(F)C(F)OBr H298:-158.71 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(Br)Br smiles:FCC(F)C(F)(Br)Br H298:-143.53 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)CBr smiles:CC(F)(CF)CBr H298:-119.99 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(F)Br smiles:OC(F)(CF)C(F)Br H298:-202.42 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)CF smiles:CC(Br)(Br)C(F)CF H298:-110.91 kcal/mol
library:CHOFBr_G4 label:FCC(F)(OBr)OBr smiles:FCC(F)(OBr)OBr H298:-121.20 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(Br)Br smiles:OC(F)(CF)C(Br)Br H298:-148.20 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)OBr smiles:FCC(F)C(F)OBr H298:-165.60 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(F)Br smiles:FCC(F)C(F)(F)Br H298:-202.76 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(F)Br smiles:CC(F)C(F)C(F)Br H298:-163.01 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)CF smiles:O=C(Br)C(F)CF H298:-133.66 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)CBr smiles:OC(F)(CF)CBr H298:-158.98 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)OBr smiles:FCC(F)(CBr)OBr H298:-117.97 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)Br smiles:FCC(F)C(Br)Br H298:-100.93 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)OBr smiles:CC(F)C(F)OBr H298:-124.15 kcal/mol
library:CHOFBr_G4 label:FCC(F)(OF)OBr smiles:FCC(F)(OF)OBr H298:-126.89 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)CBr smiles:CC(F)C(F)CBr H298:-120.06 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)Br smiles:FCC(F)C(F)Br H298:-152.58 kcal/mol
library:CHOFBr_G4 label:FCC(F)CC(Br)Br smiles:FCC(F)CC(Br)Br H298:-112.62 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)CBr smiles:FCC(F)(CBr)CBr H298:-112.82 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)OBr smiles:OC(F)(CF)OBr H298:-163.94 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)CF smiles:CC(Br)C(F)CF H298:-118.27 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(Br)Br smiles:CC(F)C(F)C(Br)Br H298:-111.37 kcal/mol
library:CHOFBr_G4 label:FCC(F)OC(F)Br smiles:FCC(F)OC(F)Br H298:-192.79 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)CBr smiles:FCC(F)C(F)CBr H298:-159.78 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)CF smiles:OC(F)(Br)C(F)CF H298:-199.94 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)OBr smiles:CC(F)(CF)OBr H298:-125.85 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)CF smiles:OC(Br)C(F)CF H298:-148.71 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(F)Br smiles:CC(F)(CF)C(F)Br H298:-163.92 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(Br)Br smiles:CC(F)(CF)C(Br)Br H298:-112.16 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)CF smiles:OC(Br)(Br)C(F)CF H298:-141.72 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)CBr smiles:FCC(F)C(Br)CBr H298:-110.02 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CF)OBr smiles:FCC(F)(CF)OBr H298:-166.08 kcal/mol
library:CHOFBr_G4 label:FCC(F)COBr smiles:FCC(F)COBr H298:-113.27 kcal/mol
library:CHOFBr_G4 label:FCC(F)CC(F)Br smiles:FCC(F)CC(F)Br H298:-161.98 kcal/mol
library:CHOFBr_G4 label:FCC(F)OOBr smiles:FCC(F)OOBr H298:-97.10 kcal/mol
library:CHOFBr_G4 label:FCC(F)CBr smiles:FCC(F)CBr H298:-108.84 kcal/mol
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
        Cpdata = ([-0.236543,-0.141694,-0.0309254,0.0259143,0.0714773,0.106218,0.192785],'cal/(mol*K)','+|-',[0.0494753,0.0571977,0.0586131,0.057826,0.0502731,0.043415,0.0345742]),
        H298 = (0.925243,'kcal/mol','+|-',0.179664),
        S298 = (0.0514285,'cal/(mol*K)','+|-',0.116676),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,2-Dibromoethane smiles:BrCCBr H298:-9.23 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(Br)CBr smiles:CC(Br)(Br)C(Br)CBr H298:-12.36 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)CBr smiles:BrC=CC(Br)CBr H298:13.51 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(OBr)OBr smiles:BrCC(Br)(OBr)OBr H298:-16.19 kcal/mol
library:CHOBr_G4 label:OCC(Br)CBr smiles:OCC(Br)CBr H298:-53.75 kcal/mol
library:CHOBr_G4 label:CC(O)(Br)CBr smiles:CC(O)(Br)CBr H298:-60.49 kcal/mol
library:CHOBr_G4 label:OC(Br)C(O)Br smiles:OC(Br)C(O)Br H298:-91.10 kcal/mol
library:CHOBr_G4 label:C#CC(Br)CBr smiles:C#CC(Br)CBr H298:52.32 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)CBr smiles:O=C(Br)C(Br)CBr H298:-36.94 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)OBr smiles:BrCC(Br)C(Br)OBr H298:-11.15 kcal/mol
library:CHOBr_G4 label:BrCC(Br)OC(Br)Br smiles:BrCC(Br)OC(Br)Br H298:-33.91 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)OBr smiles:CC(Br)(CBr)OBr H298:-22.20 kcal/mol
library:CHOBr_G4 label:OC(Br)(CBr)CBr smiles:OC(Br)(CBr)CBr H298:-53.41 kcal/mol
library:CHOBr_G4 label:CDCC(Br)CBr smiles:C=CC(Br)CBr H298:8.14 kcal/mol
library:CHOBr_G4 label:OOC(Br)CBr smiles:OOC(Br)CBr H298:-29.92 kcal/mol
library:CHOBr_G4 label:CC(C)(Br)CBr smiles:CC(C)(Br)CBr H298:-27.34 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)CBr smiles:BrC#CC(Br)CBr H298:62.76 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)C(Br)Br smiles:CC(Br)(CBr)C(Br)Br H298:-12.14 kcal/mol
library:CHOBr_G4 label:OC(O)(Br)CBr smiles:OC(O)(Br)CBr H298:-95.83 kcal/mol
library:CHOBr_G4 label:CC(Br)CBr smiles:CC(Br)CBr H298:-18.05 kcal/mol
library:CHOBr_G4 label:CC(Br)C(O)Br smiles:CC(Br)C(O)Br H298:-56.54 kcal/mol
library:CHOBr_G4 label:CC(Br)C(C)Br smiles:CC(Br)C(C)Br H298:-25.86 kcal/mol
library:CHOBr_G4 label:BrCC(Br)OBr smiles:BrCC(Br)OBr H298:-10.74 kcal/mol
library:CHOBr_G4 label:CCC(Br)CBr smiles:CCC(Br)CBr H298:-23.45 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(CBr)OBr smiles:BrCC(Br)(CBr)OBr H298:-14.67 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)OBr smiles:CC(Br)C(Br)OBr H298:-18.40 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)CBr smiles:OC(Br)C(Br)CBr H298:-52.12 kcal/mol
library:CHOBr_G4 label:OC(Br)CBr smiles:OC(Br)CBr H298:-49.20 kcal/mol
library:CHOBr_G4 label:COC(Br)CBr smiles:COC(Br)CBr H298:-46.48 kcal/mol
library:CHOBr_G4 label:ODCC(Br)CBr smiles:O=CC(Br)CBr H298:-33.11 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)OBr smiles:OC(Br)C(Br)OBr H298:-49.51 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)CBr smiles:CC(Br)C(Br)CBr H298:-20.52 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)(Br)Br smiles:BrCC(Br)C(Br)(Br)Br H298:8.92 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(CBr)CBr smiles:BrCC(Br)(CBr)CBr H298:-14.18 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)C(Br)Br smiles:CC(Br)C(Br)C(Br)Br H298:-11.03 kcal/mol
library:CHOBr_G4 label:BrCC(Br)CC(Br)Br smiles:BrCC(Br)CC(Br)Br H298:-12.09 kcal/mol
library:CHOBr_G4 label:BrCC(Br)CBr smiles:BrCC(Br)CBr H298:-11.65 kcal/mol
library:CHOBr_G4 label:BrCC(Br)COBr smiles:BrCC(Br)COBr H298:-15.07 kcal/mol
library:CHOBr_G4 label:BrCC(Br)OOBr smiles:BrCC(Br)OOBr H298:6.09 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)Br smiles:BrCC(Br)C(Br)Br H298:-2.46 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)CBr smiles:BrC=C(Br)C(Br)CBr H298:17.10 kcal/mol
library:CHOBr_G4 label:OC(Br)(CBr)OBr smiles:OC(Br)(CBr)OBr H298:-55.56 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)CBr smiles:CC(Br)(CBr)CBr H298:-21.20 kcal/mol
library:CHOBr_G4 label:BrCC(Br)CDC(Br)Br smiles:BrCC(Br)C=C(Br)Br H298:19.58 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)CBr smiles:BrCCC(Br)CBr H298:-20.00 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C(Br)OBr smiles:BrOC(Br)C(Br)OBr H298:-9.69 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)CBr smiles:BrCC(Br)C(Br)CBr H298:-12.13 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)CBr smiles:C=C(Br)C(Br)CBr H298:11.40 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)CBr smiles:BrCOC(Br)CBr H298:-42.71 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)CBr smiles:FC(Cl)C(Br)CBr H298:-66.74 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)CBr smiles:FC=C(Br)C(Br)CBr H298:-31.39 kcal/mol
library:CHOFBr_G4 label:FCCC(Br)CBr smiles:FCCC(Br)CBr H298:-67.34 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)CBr smiles:FC(Br)(Br)C(Br)CBr H298:-45.23 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)CBr smiles:CC(F)(Br)C(Br)CBr H298:-65.55 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)CBr smiles:FCC(Br)C(Br)CBr H298:-60.06 kcal/mol
library:CHOFBr_G4 label:FOC(Br)C(Br)OBr smiles:FOC(Br)C(Br)OBr H298:-15.55 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)CF smiles:CC(Br)C(Br)CF H298:-68.53 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)CBr smiles:FC(F)(Br)C(Br)CBr H298:-103.98 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)F smiles:OC(Br)(CBr)C(F)F H298:-153.48 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)F smiles:CC(Br)C(Br)C(F)F H298:-120.51 kcal/mol
library:CHOFBr_G4 label:FC(F)CC(Br)CBr smiles:FC(F)CC(Br)CBr H298:-121.40 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)CBr smiles:FC=CC(Br)CBr H298:-36.42 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)CBr smiles:FC#CC(Br)CBr H298:24.09 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)CBr smiles:FC(F)C(Br)CBr H298:-111.49 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)CBr smiles:FCC(Br)(CBr)CBr H298:-62.47 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)CBr smiles:CC(Br)(CF)CBr H298:-69.43 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)OF smiles:OC(Br)C(Br)OF H298:-55.48 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)OBr smiles:FCC(Br)(CBr)OBr H298:-62.11 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)CBr smiles:CC(F)C(Br)CBr H298:-69.70 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(Br)CBr smiles:FC(F)=CC(Br)CBr H298:-85.43 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)CF smiles:OC(Br)C(Br)CF H298:-100.52 kcal/mol
library:CHOFBr_G4 label:FC(Br)CC(Br)CBr smiles:FC(Br)CC(Br)CBr H298:-61.94 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)CBr smiles:FC=C(F)C(Br)CBr H298:-78.41 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)Br smiles:CC(Br)(CBr)C(F)Br H298:-63.12 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)Br smiles:OC(Br)C(Br)C(F)Br H298:-94.42 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)F smiles:OC(Br)C(Br)C(F)F H298:-152.46 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)CBr smiles:CC(F)(F)C(Br)CBr H298:-123.98 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CBr smiles:FCC(Br)CBr H298:-59.71 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)F smiles:CC(Br)(CBr)C(F)F H298:-120.77 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)CBr smiles:OC(Br)(CF)CBr H298:-101.26 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCC(Br)CBr smiles:FC(Br)=CC(Br)CBr H298:-30.70 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)Br smiles:OC(Br)(CBr)C(F)Br H298:-95.34 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)Br smiles:CC(Br)C(Br)C(F)Br H298:-62.62 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)OBr smiles:FCC(Br)C(Br)OBr H298:-60.33 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)CBr smiles:FCC(F)C(Br)CBr H298:-110.02 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)CBr smiles:FC(Br)C(Br)CBr H298:-53.87 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)CBr smiles:FC(F)(F)C(Br)CBr H298:-167.97 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)CBr smiles:C=C(Cl)C(Br)CBr H298:-0.44 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)CBr smiles:CC(Cl)C(Br)CBr H298:-30.66 kcal/mol
library:CHOClBr_G4 label:OC(Br)(CCl)CBr smiles:OC(Br)(CCl)CBr H298:-64.30 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)CCl smiles:CC(Br)C(Br)CCl H298:-31.33 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)OCl smiles:OC(Br)C(Br)OCl H298:-52.06 kcal/mol
library:CHOClBr_G4 label:ClCCC(Br)CBr smiles:ClCCC(Br)CBr H298:-29.69 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)CBr smiles:ClCC(Br)CBr H298:-22.63 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)CCl smiles:OC(Br)C(Br)CCl H298:-60.44 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)CBr smiles:CC(Br)(CCl)CBr H298:-32.04 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)CBr smiles:ClC(Cl)C(Br)CBr H298:-25.22 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Br)CBr smiles:ClC=CC(Br)CBr H298:1.59 kcal/mol
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
        Cpdata = ([-0.471541,-0.403022,-0.361701,-0.238505,-0.159632,-0.0942955,0.258679],'cal/(mol*K)','+|-',[0.109257,0.12631,0.129436,0.127698,0.111019,0.0958739,0.0763506]),
        H298 = (1.60409,'kcal/mol','+|-',0.396754),
        S298 = (0.530855,'cal/(mol*K)','+|-',0.257656),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:OCDC(Cl)CF smiles:OC=C(Cl)CF H298:-85.17 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)CCl smiles:FC(F)=C(F)CCl H298:-132.03 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)DCF smiles:CC(Cl)C(F)=CF H298:-95.41 kcal/mol
library:CHOFCl_G4 label:CCDC(F)CCl smiles:CC=C(F)CCl H298:-55.02 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(O)Cl smiles:C=C(F)C(O)Cl H298:-86.95 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(C)Cl smiles:C=C(F)C(C)Cl H298:-55.81 kcal/mol
library:CHOFCl_G4 label:FCDCDC(F)CCl smiles:FC=C=C(F)CCl H298:-50.55 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)DCCCl smiles:FCC(Cl)=CCCl H298:-58.31 kcal/mol
library:CHOFCl_G4 label:CDC(F)CCl smiles:C=C(F)CCl H298:-47.43 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(Cl)CF smiles:CC(Cl)=C(Cl)CF H298:-59.88 kcal/mol
library:CHOFCl_G4 label:CCDC(Cl)CF smiles:CC=C(Cl)CF H298:-54.13 kcal/mol
library:CHOFCl_G4 label:CDCDC(F)CCl smiles:C=C=C(F)CCl H298:-8.21 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)OCl smiles:C=C(F)C(Cl)OCl H298:-49.88 kcal/mol
library:CHOFCl_G4 label:FCCDC(F)CCl smiles:FCC=C(F)CCl H298:-96.67 kcal/mol
library:CHOFCl_G4 label:ODCDC(Cl)CF smiles:O=C=C(Cl)CF H298:-58.58 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)DCF smiles:OC(Cl)C(F)=CF H298:-126.01 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)CCl smiles:C=C(F)C(Cl)CCl H298:-59.19 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(Cl)CF smiles:OC(Cl)=C(Cl)CF H298:-93.25 kcal/mol
library:CHOFCl_G4 label:FCDC(F)CCl smiles:FC=C(F)CCl H298:-87.06 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)DCOCl smiles:FCC(Cl)=COCl H298:-46.74 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(F)CCl smiles:CC(F)=C(F)CCl H298:-98.98 kcal/mol
library:CHOFClBr_G4 label:CC(F)DC(Cl)CBr smiles:CC(F)=C(Cl)CBr H298:-53.13 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)CBr smiles:FC(Cl)=C(Cl)CBr H298:-44.48 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)DCOBr smiles:FCC(Cl)=COBr H298:-44.02 kcal/mol
library:CHOFClBr_G4 label:FCDCDC(Cl)CBr smiles:FC=C=C(Cl)CBr H298:-1.12 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CBr smiles:FC=C(Cl)CBr H298:-39.29 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)CBr smiles:FC(F)=C(Cl)CBr H298:-85.61 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(Cl)CF smiles:OC(Br)=C(Cl)CF H298:-80.74 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)CBr smiles:C=C(F)C(Cl)CBr H298:-48.12 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)DCF smiles:OC(Br)C(Cl)=CF H298:-77.55 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)DCF smiles:CC(Br)C(Cl)=CF H298:-47.67 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)OBr smiles:C=C(F)C(Cl)OBr H298:-47.15 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)CF smiles:CC(Br)=C(Cl)CF H298:-47.90 kcal/mol
library:CHOFClBr_G4 label:FCCDC(Cl)CBr smiles:FCC=C(Cl)CBr H298:-47.05 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)DCCBr smiles:FCC(Cl)=CCBr H298:-47.74 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)CF smiles:OC(Br)=C(Br)CF H298:-66.57 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)CBr smiles:FCC(Br)=C(Br)CBr H298:-28.71 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DCF smiles:OC(Br)C(F)=CF H298:-114.11 kcal/mol
library:CHOFBr_G4 label:FC(F)DCDC(F)CBr smiles:FC(F)=C=C(F)CBr H298:-85.84 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)CBr smiles:CC(F)=C(F)CBr H298:-88.38 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CBr smiles:FC=C(F)CBr H298:-76.28 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)CF smiles:CC=C(Br)CF H298:-42.37 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCC(Br)Br smiles:FCC(Br)=CC(Br)Br H298:-28.85 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)CBr smiles:FCC(F)=C(F)CBr H298:-127.49 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)OBr smiles:FC=C(F)C(Br)OBr H298:-74.69 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCCBr smiles:FCC(Br)=CCBr H298:-36.00 kcal/mol
library:CHOFBr_G4 label:FC(DCC(F)F)CBr smiles:FC(=CC(F)F)CBr H298:-138.96 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)CF smiles:OC=C(Br)CF H298:-77.42 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DC(F)F smiles:OC(Br)C(F)=C(F)F H298:-158.88 kcal/mol
library:CHOFBr_G4 label:FCCDC(F)CBr smiles:FCC=C(F)CBr H298:-85.98 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DC(F)F smiles:CC(Br)C(F)=C(F)F H298:-129.35 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)C(Br)Br smiles:C=C(F)C(Br)C(Br)Br H298:-29.68 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)CBr smiles:C=C=C(F)CBr H298:2.46 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)CBr smiles:FC=C(F)C(Br)CBr H298:-78.41 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCOBr smiles:FCC(Br)=COBr H298:-32.74 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DCF smiles:CC(Br)C(F)=CF H298:-84.38 kcal/mol
library:CHOFBr_G4 label:CDC(F)CBr smiles:C=C(F)CBr H298:-36.62 kcal/mol
library:CHOFBr_G4 label:FCDCDC(F)CBr smiles:FC=C=C(F)CBr H298:-39.16 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(C)Br smiles:C=C(F)C(C)Br H298:-44.46 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(O)Br smiles:C=C(F)C(O)Br H298:-75.13 kcal/mol
library:CHOFBr_G4 label:CCDC(F)CBr smiles:CC=C(F)CBr H298:-44.35 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)OBr smiles:C=C(F)C(Br)OBr H298:-35.32 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)CF smiles:O=C=C(Br)CF H298:-48.63 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CBr smiles:FC(F)=C(F)CBr H298:-121.31 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)CF smiles:CC(Br)=C(Br)CF H298:-36.19 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)OBr smiles:FCC(Br)=C(Br)OBr H298:-26.22 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)CCl smiles:CC(Br)=C(Br)CCl H298:0.38 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)CBr smiles:ClC(Cl)=C(Cl)CBr H298:-5.94 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)CBr smiles:C=C=C(Cl)CBr H298:39.26 kcal/mol
library:CHOClBr_G4 label:ClCCDC(Cl)CBr smiles:ClCC=C(Cl)CBr H298:-9.63 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)DCOBr smiles:ClCC(Br)=COBr H298:4.81 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)CBr smiles:C=C(Cl)C(Br)CBr H298:-0.44 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Cl)CBr smiles:CC(Cl)=C(Cl)CBr H298:-13.25 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)DCCl smiles:OC(Br)C(Cl)=CCl H298:-40.96 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CBr smiles:ClC=C(Cl)CBr H298:-2.41 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)CCl smiles:CC=C(Br)CCl H298:-4.46 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)CBr smiles:C=C(Cl)CBr H298:2.86 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)DCCl smiles:CC(Br)C(Cl)=CCl H298:-10.89 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(C)Br smiles:C=C(Cl)C(C)Br H298:-5.45 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(O)Br smiles:C=C(Cl)C(O)Br H298:-36.93 kcal/mol
library:CHOClBr_G4 label:ODCDC(Br)CCl smiles:O=C=C(Br)CCl H298:-9.86 kcal/mol
library:CHOClBr_G4 label:CCDC(Cl)CBr smiles:CC=C(Cl)CBr H298:-5.66 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)OBr smiles:C=C(Cl)C(Br)OBr H298:3.30 kcal/mol
library:CHOClBr_G4 label:ClCDCDC(Cl)CBr smiles:ClC=C=C(Cl)CBr H298:35.43 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)DCCBr smiles:ClCC(Br)=CCBr H298:2.04 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Br)CCl smiles:OC(Br)=C(Br)CCl H298:-32.09 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)CCl smiles:OC=C(Br)CCl H298:-39.26 kcal/mol
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
        Cpdata = ([-0.408668,-0.208102,-0.103614,0.0361113,0.0883564,0.124151,0.430623],'cal/(mol*K)','+|-',[0.14464,0.167217,0.171355,0.169054,0.146973,0.126923,0.101077]),
        H298 = (1.35334,'kcal/mol','+|-',0.525246),
        S298 = (-0.200617,'cal/(mol*K)','+|-',0.341099),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:CC(Cl)C(Cl)DCCl smiles:CC(Cl)C(Cl)=CCl H298:-21.92 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-23.64 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)Cl smiles:ClCC(Cl)=C(Cl)Cl H298:-16.31 kcal/mol
library:CHOCl_G4 label:ClCDCDC(Cl)CCl smiles:ClC=C=C(Cl)CCl H298:24.68 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DCC(Cl)Cl smiles:ClCC(Cl)=CC(Cl)Cl H298:-22.70 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)CCl smiles:ClC=C(Cl)C(Cl)CCl H298:-27.32 kcal/mol
library:CHOCl_G4 label:CCDC(Cl)CCl smiles:CC=C(Cl)CCl H298:-16.44 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)Cl H298:-30.04 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)CCl smiles:OC(Cl)=C(Cl)CCl H298:-55.72 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)CCl smiles:ClCC(Cl)=C(Cl)CCl H298:-26.27 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(O)Cl smiles:C=C(Cl)C(O)Cl H298:-47.43 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(C)Cl smiles:C=C(Cl)C(C)Cl H298:-16.59 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DCC(Cl)(Cl)Cl smiles:ClCC(Cl)=CC(Cl)(Cl)Cl H298:-23.20 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-32.82 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)OCl smiles:C=C(Cl)C(Cl)OCl H298:-10.98 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)Cl H298:-30.71 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)C(Cl)Cl smiles:C=C(Cl)C(Cl)C(Cl)Cl H298:-24.03 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DCOCl smiles:ClCC(Cl)=COCl H298:-9.25 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)CCl smiles:OC=C(Cl)CCl H298:-50.65 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)DC(Cl)Cl smiles:ClCC(Cl)C(Cl)=C(Cl)Cl H298:-30.56 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-23.53 kcal/mol
library:CHOCl_G4 label:CDC(Cl)CCl smiles:C=C(Cl)CCl H298:-8.01 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)DC(Cl)Cl smiles:OC(Cl)C(Cl)=C(Cl)Cl H298:-56.83 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)Cl H298:-27.36 kcal/mol
library:CHOCl_G4 label:ODCDC(Cl)CCl smiles:O=C=C(Cl)CCl H298:-19.78 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-29.53 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CCl smiles:ClC=C(Cl)CCl H298:-13.01 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)CCl smiles:C=C(Cl)C(Cl)CCl H298:-20.12 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DCDC(Cl)Cl smiles:ClCC(Cl)=C=C(Cl)Cl H298:21.29 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)OCl smiles:ClCC(Cl)=C(Cl)OCl H298:-15.60 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)CCl smiles:CC(Cl)=C(Cl)CCl H298:-23.69 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)DC(Cl)Cl smiles:ClOC(Cl)C(Cl)=C(Cl)Cl H298:-19.20 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)DC(Cl)Cl smiles:CC(Cl)C(Cl)=C(Cl)Cl H298:-25.17 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)OCl smiles:ClC=C(Cl)C(Cl)OCl H298:-16.60 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)DCCl smiles:OC(Cl)C(Cl)=CCl H298:-53.72 kcal/mol
library:CHOCl_G4 label:ClCCDC(Cl)CCl smiles:ClCC=C(Cl)CCl H298:-20.39 kcal/mol
library:CHOCl_G4 label:CDCDC(Cl)CCl smiles:C=C=C(Cl)CCl H298:28.52 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(Cl)DCF smiles:CC(Cl)C(Cl)=CF H298:-58.79 kcal/mol
library:CHOFCl_G4 label:FCCDC(Cl)CCl smiles:FCC=C(Cl)CCl H298:-57.69 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(Cl)CCl smiles:FC(F)=C(Cl)CCl H298:-96.34 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)DCF smiles:OC(Cl)C(Cl)=CF H298:-89.43 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)CCl smiles:FC=C(Cl)CCl H298:-50.18 kcal/mol
library:CHOFCl_G4 label:FCDCDC(Cl)CCl smiles:FC=C=C(Cl)CCl H298:-11.82 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC(Cl)CCl smiles:FC(Cl)=C(Cl)CCl H298:-55.00 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(Cl)CCl smiles:CC(F)=C(Cl)CCl H298:-63.85 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)CBr smiles:C=C(Cl)C(Cl)CBr H298:-11.03 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)DCCBr smiles:ClCC(Cl)=CCBr H298:-9.78 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)CCl smiles:CC(Br)=C(Cl)CCl H298:-11.54 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)DCOBr smiles:ClCC(Cl)=COBr H298:-6.72 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)CCl smiles:OC(Br)=C(Cl)CCl H298:-43.33 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)OBr smiles:C=C(Cl)C(Cl)OBr H298:-8.81 kcal/mol
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
        Cpdata = ([-0.173117,-0.12812,-0.150642,-0.0507671,-0.0434744,-0.0318139,0.314657],'cal/(mol*K)','+|-',[0.135338,0.156462,0.160334,0.158181,0.13752,0.11876,0.0945764]),
        H298 = (1.92039,'kcal/mol','+|-',0.491464),
        S298 = (0.294818,'cal/(mol*K)','+|-',0.319161),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:OCDC(F)CF smiles:OC=C(F)CF H298:-124.81 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)CF smiles:C=C(F)C(F)CF H298:-136.33 kcal/mol
library:CHOF_G4 label:FCDC(F)CF smiles:FC=C(F)CF H298:-125.01 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)OF smiles:C=C(F)C(F)OF H298:-98.67 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)(F)F smiles:FCC(F)=C(F)C(F)(F)F H298:-280.88 kcal/mol
library:CHOF_G4 label:FCC(F)DCOF smiles:FCC(F)=COF H298:-90.68 kcal/mol
library:CHOF_G4 label:ODCDC(F)CF smiles:O=C=C(F)CF H298:-90.20 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)OF smiles:FC=C(F)C(F)OF H298:-137.80 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)(F)F smiles:FC(F)=C(F)C(F)C(F)(F)F H298:-327.95 kcal/mol
library:CHOF_G4 label:FCDCDC(F)CF smiles:FC=C=C(F)CF H298:-86.82 kcal/mol
library:CHOF_G4 label:CCDC(F)CF smiles:CC=C(F)CF H298:-92.44 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)CF smiles:FC=C(F)C(F)CF H298:-175.27 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)CF smiles:OC(F)=C(F)CF H298:-169.89 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)OF smiles:FCC(F)=C(F)OF H298:-137.23 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)CF smiles:FCC(F)=C(F)CF H298:-174.85 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)C(F)F smiles:C=C(F)C(F)C(F)F H298:-187.04 kcal/mol
library:CHOF_G4 label:CDC(F)C(C)F smiles:C=C(F)C(C)F H298:-95.05 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)F smiles:FCC(F)=C(F)F H298:-169.93 kcal/mol
library:CHOF_G4 label:OC(F)C(F)DC(F)F smiles:OC(F)C(F)=C(F)F H298:-214.83 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)F smiles:FCC(F)=C(F)C(F)F H298:-223.99 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)CF smiles:CC(F)=C(F)CF H298:-136.44 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)DC(F)F smiles:FCC(F)C(F)=C(F)F H298:-219.99 kcal/mol
library:CHOF_G4 label:CDCDC(F)CF smiles:C=C=C(F)CF H298:-45.84 kcal/mol
library:CHOF_G4 label:CC(F)C(F)DC(F)F smiles:CC(F)C(F)=C(F)F H298:-179.62 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)DC(F)F smiles:FOC(F)C(F)=C(F)F H298:-180.69 kcal/mol
library:CHOF_G4 label:FCC(F)DCC(F)(F)F smiles:FCC(F)=CC(F)(F)F H298:-243.02 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)F smiles:FC(F)=C(F)C(F)C(F)F H298:-272.23 kcal/mol
library:CHOF_G4 label:OC(F)C(F)DCF smiles:OC(F)C(F)=CF H298:-170.49 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)F smiles:FC=C(F)C(F)C(F)F H298:-226.59 kcal/mol
library:CHOF_G4 label:CDC(F)C(O)F smiles:C=C(F)C(O)F H298:-130.39 kcal/mol
library:CHOF_G4 label:CDC(F)CF smiles:C=C(F)CF H298:-84.92 kcal/mol
library:CHOF_G4 label:FCC(F)DCC(F)F smiles:FCC(F)=CC(F)F H298:-186.90 kcal/mol
library:CHOF_G4 label:FCC(F)DCDC(F)F smiles:FCC(F)=C=C(F)F H298:-133.91 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)(F)F smiles:FC=C(F)C(F)C(F)(F)F H298:-283.24 kcal/mol
library:CHOF_G4 label:FCCDC(F)CF smiles:FCC=C(F)CF H298:-133.90 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)C(F)(F)F smiles:C=C(F)C(F)C(F)(F)F H298:-243.94 kcal/mol
library:CHOF_G4 label:CC(F)C(F)DCF smiles:CC(F)C(F)=CF H298:-134.86 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(F)CF smiles:OC(Cl)=C(F)CF H298:-128.77 kcal/mol
library:CHOFCl_G4 label:FCC(F)DCCCl smiles:FCC(F)=CCCl H298:-96.29 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)CCl smiles:C=C(F)C(F)CCl H298:-98.42 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(F)CF smiles:CC(Cl)=C(F)CF H298:-98.06 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)OCl smiles:C=C(F)C(F)OCl H298:-93.86 kcal/mol
library:CHOFCl_G4 label:FCC(F)DCOCl smiles:FCC(F)=COCl H298:-83.43 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCC(F)Br smiles:FCC(F)=CC(F)Br H298:-129.39 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)CF smiles:CC(Br)=C(F)CF H298:-85.99 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)OBr smiles:FCC(F)=C(Br)OBr H298:-75.27 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCOBr smiles:FCC(F)=COBr H298:-80.79 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)OBr smiles:C=C(F)C(F)OBr H298:-90.95 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)CBr smiles:FCC(F)=C(F)CBr H298:-127.49 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)OBr smiles:FC=C(F)C(F)OBr H298:-130.47 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)CBr smiles:FC=C(F)C(F)CBr H298:-127.57 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)CF smiles:OC(Br)=C(F)CF H298:-114.91 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCC(Br)Br smiles:FCC(F)=CC(Br)Br H298:-78.73 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(F)Br smiles:C=C(F)C(F)C(F)Br H298:-129.81 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)OBr smiles:FCC(F)=C(F)OBr H298:-127.53 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)CBr smiles:C=C(F)C(F)CBr H298:-87.36 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCCBr smiles:FCC(F)=CCBr H298:-85.58 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)CBr smiles:FCC(F)=C(Br)CBr H298:-78.09 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(Br)Br smiles:C=C(F)C(F)C(Br)Br H298:-78.69 kcal/mol
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
        Cpdata = ([-0.546487,-0.361121,-0.193685,-0.0224338,0.117759,0.190493,0.451822],'cal/(mol*K)','+|-',[0.140851,0.162835,0.166865,0.164624,0.143122,0.123598,0.0984289]),
        H298 = (0.952489,'kcal/mol','+|-',0.511484),
        S298 = (-0.211612,'cal/(mol*K)','+|-',0.332162),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(Br)C(O)Br smiles:C=C(Br)C(O)Br H298:-23.59 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(C)Br smiles:C=C(Br)C(C)Br H298:6.49 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)OBr smiles:C=C(Br)C(Br)OBr H298:14.94 kcal/mol
library:CHOBr_G4 label:OCDC(Br)CBr smiles:OC=C(Br)CBr H298:-28.42 kcal/mol
library:CHOBr_G4 label:OC(Br)DC(Br)CBr smiles:OC(Br)=C(Br)CBr H298:-21.57 kcal/mol
library:CHOBr_G4 label:CDC(Br)CBr smiles:C=C(Br)CBr H298:15.06 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)OBr smiles:BrCC(Br)=C(Br)OBr H298:20.22 kcal/mol
library:CHOBr_G4 label:ODCDC(Br)CBr smiles:O=C=C(Br)CBr H298:1.05 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)OBr smiles:BrC=C(Br)C(Br)OBr H298:21.13 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)DCBr smiles:CC(Br)C(Br)=CBr H298:12.64 kcal/mol
library:CHOBr_G4 label:BrCDCDC(Br)CBr smiles:BrC=C=C(Br)CBr H298:57.43 kcal/mol
library:CHOBr_G4 label:CDCDC(Br)CBr smiles:C=C=C(Br)CBr H298:50.27 kcal/mol
library:CHOBr_G4 label:BrCCDC(Br)CBr smiles:BrCC=C(Br)CBr H298:12.69 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCC(Br)Br smiles:BrCC(Br)=CC(Br)Br H298:19.71 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CBr smiles:BrC=C(Br)CBr H298:20.89 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)Br smiles:BrCC(Br)=C(Br)Br H298:29.22 kcal/mol
library:CHOBr_G4 label:CCDC(Br)CBr smiles:CC=C(Br)CBr H298:6.17 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)CBr smiles:BrC=C(Br)C(Br)CBr H298:17.10 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)CBr smiles:BrCC(Br)=C(Br)CBr H298:17.72 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)CBr smiles:C=C(Br)C(Br)CBr H298:11.40 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)CBr smiles:CC(Br)=C(Br)CBr H298:10.09 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCDC(Br)Br smiles:BrCC(Br)=C=C(Br)Br H298:65.09 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCOBr smiles:BrCC(Br)=COBr H298:15.28 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)CBr smiles:FC(Cl)=C(Br)CBr H298:-33.17 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)CBr smiles:FC=C(Br)C(Br)CBr H298:-31.39 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)CBr smiles:FCC(Br)=C(Br)CBr H298:-28.71 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)F smiles:CC(Br)C(Br)=C(F)F H298:-82.80 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CBr smiles:FC(F)=C(Br)CBr H298:-74.29 kcal/mol
library:CHOFBr_G4 label:FC(F)CDC(Br)CBr smiles:FC(F)C=C(Br)CBr H298:-91.20 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DCF smiles:OC(Br)C(Br)=CF H298:-66.03 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCDC(Br)CBr smiles:FC(Br)=C=C(Br)CBr H298:17.35 kcal/mol
library:CHOFBr_G4 label:FCDCDC(Br)CBr smiles:FC=C=C(Br)CBr H298:10.10 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CBr smiles:FC=C(Br)CBr H298:-27.76 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)Br smiles:OC(Br)C(Br)=C(F)Br H298:-59.50 kcal/mol
library:CHOFBr_G4 label:FC(Br)CDC(Br)CBr smiles:FC(Br)C=C(Br)CBr H298:-31.13 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)CBr smiles:CC(F)=C(Br)CBr H298:-39.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)F smiles:OC(Br)C(Br)=C(F)F H298:-113.48 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)Br smiles:CC(Br)C(Br)=C(F)Br H298:-28.73 kcal/mol
library:CHOFBr_G4 label:FCCDC(Br)CBr smiles:FCC=C(Br)CBr H298:-35.29 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)CBr smiles:FCC(F)=C(Br)CBr H298:-78.09 kcal/mol
library:CHOFBr_G4 label:FC(F)DCDC(Br)CBr smiles:FC(F)=C=C(Br)CBr H298:-35.68 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DCF smiles:CC(Br)C(Br)=CF H298:-36.21 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CBr smiles:FC(Br)=C(Br)CBr H298:-20.76 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)OBr smiles:FC=C(Br)C(Br)OBr H298:-27.80 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CBr smiles:ClC=C(Br)CBr H298:9.29 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)DCCl smiles:OC(Br)C(Br)=CCl H298:-30.40 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Br)CBr smiles:CC(Cl)=C(Br)CBr H298:-1.69 kcal/mol
library:CHOClBr_G4 label:ClCCDC(Br)CBr smiles:ClCC=C(Br)CBr H298:2.21 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)CBr smiles:ClC(Cl)=C(Br)CBr H298:5.67 kcal/mol
library:CHOClBr_G4 label:ClCDCDC(Br)CBr smiles:ClC=C=C(Br)CBr H298:46.41 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)CBr smiles:ClC(Br)=C(Br)CBr H298:17.35 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)DCCl smiles:CC(Br)C(Br)=CCl H298:0.84 kcal/mol
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
        Cpdata = ([0.0568493,0.498284,0.567205,0.66183,0.560029,0.451862,0.210985],'cal/(mol*K)','+|-',[0.118694,0.137221,0.140616,0.138728,0.120608,0.104155,0.0829456]),
        H298 = (1.02903,'kcal/mol','+|-',0.431025),
        S298 = (-0.705478,'cal/(mol*K)','+|-',0.279912),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(F)C(Cl)DCCl smiles:C=C(F)C(Cl)=CCl H298:-32.54 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(F)DCF smiles:C=C(Cl)C(F)=CF H298:-67.03 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(DC)Cl smiles:C=C(F)C(=C)Cl H298:-27.41 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DCBr smiles:C=C(F)C(Cl)=CBr H298:-20.73 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DCF smiles:C=C(Br)C(Cl)=CF H298:-17.66 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DCF smiles:C=C(Br)C(F)=CF H298:-54.93 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)DCBr smiles:FC=C(F)C(Br)=CBr H298:-48.03 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(DC)Br smiles:C=C(F)C(=C)Br H298:-15.24 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DC(Br)Br smiles:C=C(F)C(Br)=C(Br)Br H298:3.56 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DCBr smiles:C=C(F)C(Br)=CBr H298:-8.72 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DC(F)F smiles:C=C(Br)C(F)=C(F)F H298:-96.86 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)DCBr smiles:C=C(Cl)C(Br)=CBr H298:31.07 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(DC)Br smiles:C=C(Cl)C(=C)Br H298:24.56 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)DCCl smiles:C=C(Br)C(Cl)=CCl H298:19.30 kcal/mol
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
        Cpdata = ([0.0231291,0.346025,0.387066,0.491326,0.39547,0.313349,0.185059],'cal/(mol*K)','+|-',[0.161928,0.187203,0.191835,0.189259,0.164539,0.142093,0.113158]),
        H298 = (0.990095,'kcal/mol','+|-',0.588023),
        S298 = (-0.231792,'cal/(mol*K)','+|-',0.381868),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DC(Cl)Cl smiles:ClC=C(Cl)C(Cl)=C(Cl)Cl H298:1.13 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(DC)Cl smiles:C=C(Cl)C(=C)Cl H298:12.43 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)DCCl smiles:C=C(Cl)C(Cl)=CCl H298:7.20 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DCCl smiles:ClC=C(Cl)C(Cl)=CCl H298:2.21 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)DC(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)=C(Cl)Cl H298:-3.12 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)DC(Cl)Cl smiles:C=C(Cl)C(Cl)=C(Cl)Cl H298:6.79 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(Cl)DCF smiles:C=C(Cl)C(Cl)=CF H298:-29.76 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DCBr smiles:C=C(Cl)C(Cl)=CBr H298:19.01 kcal/mol
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
        Cpdata = ([-0.224553,0.233739,0.39757,0.590951,0.598046,0.55743,0.38307],'cal/(mol*K)','+|-',[0.138947,0.160635,0.16461,0.162399,0.141188,0.121927,0.0970987]),
        H298 = (1.33146,'kcal/mol','+|-',0.504571),
        S298 = (-0.72938,'cal/(mol*K)','+|-',0.327673),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:CDC(F)C(F)DC(F)F smiles:C=C(F)C(F)=C(F)F H298:-149.08 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)DC(F)F smiles:FC=C(F)C(F)=C(F)F H298:-187.35 kcal/mol
library:CHOF_G4 label:CDC(F)C(DC)F smiles:C=C(F)C(=C)F H298:-66.88 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)DC(F)F smiles:FC(F)=C(F)C(F)=C(F)F H298:-231.97 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)DCF smiles:C=C(F)C(F)=CF H298:-106.22 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)DCF smiles:FC=C(F)C(F)=CF H298:-144.78 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)DCCl smiles:C=C(F)C(F)=CCl H298:-70.38 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)DCBr smiles:FC=C(F)C(F)=CBr H298:-97.78 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(Br)Br smiles:C=C(F)C(F)=C(Br)Br H298:-45.81 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DCBr smiles:C=C(F)C(F)=CBr H298:-58.88 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(F)Br smiles:C=C(F)C(F)=C(F)Br H298:-95.50 kcal/mol
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
        Cpdata = ([0.161573,0.290224,0.28616,0.351225,0.261773,0.190947,0.0833704],'cal/(mol*K)','+|-',[0.16953,0.195992,0.200841,0.198144,0.172264,0.148764,0.118471]),
        H298 = (1.23118,'kcal/mol','+|-',0.61563),
        S298 = (-0.16381,'cal/(mol*K)','+|-',0.399796),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(Br)C(DC)Br smiles:C=C(Br)C(=C)Br H298:36.64 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)DCBr smiles:C=C(Br)C(Br)=CBr H298:43.12 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)Br smiles:C=C(Br)C(Br)=C(F)Br H298:3.03 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)F smiles:C=C(Br)C(Br)=C(F)F H298:-50.23 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)DCBr smiles:FC=C(Br)C(Br)=CBr H298:0.72 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DCF smiles:C=C(Br)C(Br)=CF H298:-6.06 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DCCl smiles:C=C(Br)C(Br)=CCl H298:31.20 kcal/mol
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
        Cpdata = ([0.173623,0.124799,0.0745592,0.0311234,-0.0173741,-0.0439235,-0.119184],'cal/(mol*K)','+|-',[0.0504982,0.0583803,0.0598249,0.0590216,0.0513125,0.0443126,0.035289]),
        H298 = (1.72139,'kcal/mol','+|-',0.183379),
        S298 = (-0.092972,'cal/(mol*K)','+|-',0.119088),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:OCC(Cl)DCF smiles:OCC(Cl)=CF H298:-81.27 kcal/mol
library:CHOFCl_G4 label:FCDCC(F)DCCl smiles:FC=CC(F)=CCl H298:-69.58 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(F)CF smiles:OC(Cl)=C(F)CF H298:-128.77 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(Cl)OCl smiles:CC(F)=C(Cl)OCl H298:-50.39 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(F)OF smiles:OC(Cl)=C(F)OF H298:-96.73 kcal/mol
library:CHOFCl_G4 label:OC(F)DC(O)Cl smiles:OC(F)=C(O)Cl H298:-119.11 kcal/mol
library:CHOFCl_G4 label:OOC(Cl)DCF smiles:OOC(Cl)=CF H298:-55.52 kcal/mol
library:CHOFCl_G4 label:CDCC(Cl)DCF smiles:C=CC(Cl)=CF H298:-23.93 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(Cl)DCF smiles:C=C(Cl)C(Cl)=CF H298:-29.76 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)C(Cl)Cl smiles:FC=C(Cl)C(Cl)Cl H298:-53.06 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)OCl smiles:FC=C(Cl)OCl H298:-38.44 kcal/mol
library:CHOFCl_G4 label:FC#CC(F)DCCl smiles:FC#CC(F)=CCl H298:-7.55 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)CDCCl smiles:FC=C(Cl)C=CCl H298:-30.08 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)OCCl smiles:FC=C(Cl)OCCl H298:-78.97 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)DCCl smiles:C=C(F)C(F)=CCl H298:-70.38 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(Cl)DCF smiles:CC(Cl)C(Cl)=CF H298:-58.79 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)CCCl smiles:FC=C(Cl)CCCl H298:-58.07 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(C)Cl smiles:CC(F)=C(C)Cl H298:-58.61 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DCF smiles:CC(Cl)=CF H298:-47.11 kcal/mol
library:CHOFCl_G4 label:C#CC(F)DCCl smiles:C#CC(F)=CCl H298:20.61 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(O)Cl smiles:CC(F)=C(O)Cl H298:-87.90 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)DCF smiles:CCC(Cl)=CF H298:-52.36 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DCF smiles:OC(Cl)=CF H298:-76.86 kcal/mol
library:CHOFCl_G4 label:COC(Cl)DCF smiles:COC(Cl)=CF H298:-71.24 kcal/mol
library:CHOFCl_G4 label:CDCC(F)DCCl smiles:C=CC(F)=CCl H298:-25.53 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)DCF smiles:O=CC(Cl)=CF H298:-64.31 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(Cl)DCF smiles:OC(Cl)C(Cl)=CF H298:-89.43 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)COCl smiles:FC=C(Cl)COCl H298:-47.39 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(F)CF smiles:CC(Cl)=C(F)CF H298:-98.06 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)OOCl smiles:FC=C(Cl)OOCl H298:-24.32 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)CCl smiles:FC=C(Cl)CCl H298:-50.18 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(Cl)DCF smiles:O=C(Cl)C(Cl)=CF H298:-78.04 kcal/mol
library:CHOFCl_G4 label:OC(F)DC(Cl)OCl smiles:OC(F)=C(Cl)OCl H298:-83.21 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(Cl)CCl smiles:CC(F)=C(Cl)CCl H298:-63.85 kcal/mol
library:CHOFCl_G4 label:FCDCCl smiles:FC=CCl H298:-37.39 kcal/mol
library:CHOFClBr_G4 label:CC(F)DC(Cl)CBr smiles:CC(F)=C(Cl)CBr H298:-53.13 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)DCF smiles:O=C(Br)C(Cl)=CF H298:-65.38 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CBr smiles:FC=C(Cl)CBr H298:-39.29 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)OOBr smiles:FC=C(Cl)OOBr H298:-20.84 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)COBr smiles:FC=C(Cl)COBr H298:-44.13 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(Cl)CF smiles:OC(Br)=C(Cl)CF H298:-80.74 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)DCF smiles:OC(Br)C(Cl)=CF H298:-77.55 kcal/mol
library:CHOFClBr_G4 label:FC#CC(Cl)DCBr smiles:FC#CC(Cl)=CBr H298:42.13 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)DCF smiles:CC(Br)C(Cl)=CF H298:-47.67 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)CF smiles:CC(Br)=C(Cl)CF H298:-47.90 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Br)Br smiles:FC=C(Cl)C(Br)Br H298:-30.31 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DCBr smiles:C=C(F)C(Cl)=CBr H298:-20.73 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CCBr smiles:FC=C(Cl)CCBr H298:-47.03 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)OCBr smiles:FC=C(Cl)OCBr H298:-67.10 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CDCBr smiles:FC=C(Cl)C=CBr H298:-18.15 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)OBr smiles:FC=C(Cl)OBr H298:-36.23 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Cl)Br smiles:FC=C(Cl)C(Cl)Br H298:-41.49 kcal/mol
library:CHOFClBr_G4 label:CC(F)DC(Cl)OBr smiles:CC(F)=C(Cl)OBr H298:-48.51 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DCF smiles:C=C(Br)C(Cl)=CF H298:-17.66 kcal/mol
library:CHOFClBr_G4 label:FCDCC(Cl)DCBr smiles:FC=CC(Cl)=CBr H298:-19.50 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)CBr smiles:FC=C(Br)C(Br)CBr H298:-31.39 kcal/mol
library:CHOFBr_G4 label:COC(Br)DCF smiles:COC(Br)=CF H298:-59.18 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)DCBr smiles:FC=C(F)C(F)=CBr H298:-97.78 kcal/mol
library:CHOFBr_G4 label:FCDCBr smiles:FC=CBr H298:-25.74 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCF smiles:OC(Br)=CF H298:-64.41 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DCF smiles:OC(Br)C(Br)=CF H298:-66.03 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)CF smiles:CC(Br)=C(F)CF H298:-85.99 kcal/mol
library:CHOFBr_G4 label:CCC(Br)DCF smiles:CCC(Br)=CF H298:-41.54 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)OBr smiles:FCC(F)=C(Br)OBr H298:-75.27 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)Br smiles:FC=C(Br)C(Br)Br H298:-19.12 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)DCBr smiles:FC(F)=CC(F)=CBr H298:-104.46 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)COBr smiles:FC=C(Br)COBr H298:-32.75 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)DCBr smiles:FC=C(Br)C(Br)=CBr H298:0.72 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCF smiles:CC(Br)=CF H298:-35.40 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OOBr smiles:FC=C(Br)OOBr H298:-8.75 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)(Br)Br smiles:FC=C(Br)C(Br)(Br)Br H298:-6.70 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CBr smiles:FC=C(Br)CBr H298:-27.76 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)C(Br)Br smiles:CC(F)=C(Br)C(Br)Br H298:-31.52 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CC(Br)Br smiles:FC=C(Br)CC(Br)Br H298:-28.86 kcal/mol
library:CHOFBr_G4 label:OOC(Br)DCF smiles:OOC(Br)=CF H298:-43.40 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)DCF smiles:C=CC(Br)=CF H298:-12.25 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CDCBr smiles:FC=C(Br)C=CBr H298:-6.56 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)CBr smiles:CC(F)=C(Br)CBr H298:-39.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)C(F)F smiles:OC(Br)=C(F)C(F)F H298:-166.31 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DCF smiles:O=C(Br)C(Br)=CF H298:-54.16 kcal/mol
library:CHOFBr_G4 label:OCC(Br)DCF smiles:OCC(Br)=CF H298:-69.81 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)DCF smiles:CC(Br)(Br)C(Br)=CF H298:-27.79 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)C(F)F smiles:CC(Br)=C(F)C(F)F H298:-136.64 kcal/mol
library:CHOFBr_G4 label:CDCC(F)DCBr smiles:C=CC(F)=CBr H298:-13.99 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DCF smiles:C=C(Br)C(Br)=CF H298:-6.06 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)CF smiles:OC(Br)=C(F)CF H298:-114.91 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)DCF smiles:OC(Br)(Br)C(Br)=CF H298:-59.62 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)OBr smiles:CC(F)=C(Br)OBr H298:-36.51 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(O)Br smiles:CC(F)=C(O)Br H298:-74.83 kcal/mol
library:CHOFBr_G4 label:C#CC(F)DCBr smiles:C#CC(F)=CBr H298:32.22 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(C)Br smiles:CC(F)=C(C)Br H298:-46.60 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OBr smiles:FC=C(Br)OBr H298:-24.07 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DCBr smiles:C=C(F)C(F)=CBr H298:-58.88 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OCBr smiles:FC=C(Br)OCBr H298:-55.16 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)DCBr smiles:FC#CC(F)=CBr H298:4.04 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CCBr smiles:FC=C(Br)CCBr H298:-35.57 kcal/mol
library:CHOFBr_G4 label:FOC(F)DC(Br)OBr smiles:FOC(F)=C(Br)OBr H298:-34.87 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)CBr smiles:FCC(F)=C(Br)CBr H298:-78.09 kcal/mol
library:CHOFBr_G4 label:OC(F)DC(O)Br smiles:OC(F)=C(O)Br H298:-107.23 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DCF smiles:CC(Br)C(Br)=CF H298:-36.21 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CDC(Br)Br smiles:FC=C(Br)C=C(Br)Br H298:3.85 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)DCBr smiles:FC=CC(F)=CBr H298:-58.09 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DCF smiles:O=CC(Br)=CF H298:-52.97 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)OBr smiles:FC=C(Br)C(Br)OBr H298:-27.80 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OC(Br)Br smiles:FC=C(Br)OC(Br)Br H298:-45.90 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DCCl smiles:C=C(Br)C(Br)=CCl H298:31.20 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DCCl smiles:O=CC(Br)=CCl H298:-15.62 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)C(Br)Br smiles:ClC=C(Br)C(Br)Br H298:17.96 kcal/mol
library:CHOClBr_G4 label:CC(Br)DCCl smiles:CC(Br)=CCl H298:1.74 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CBr smiles:ClC=C(Br)CBr H298:9.29 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)DCCl smiles:OC(Br)C(Br)=CCl H298:-30.40 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Cl)DCBr smiles:ClC=CC(Cl)=CBr H298:18.36 kcal/mol
library:CHOClBr_G4 label:OCC(Br)DCCl smiles:OCC(Br)=CCl H298:-32.63 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DCBr smiles:C=C(Cl)C(Cl)=CBr H298:19.01 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)DCCl smiles:C=CC(Br)=CCl H298:24.86 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Br)CBr smiles:CC(Cl)=C(Br)CBr H298:-1.69 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)DCBr smiles:C#CC(Cl)=CBr H298:70.09 kcal/mol
library:CHOClBr_G4 label:OC(Cl)DC(Br)OBr smiles:OC(Cl)=C(Br)OBr H298:-30.59 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(O)Br smiles:CC(Cl)=C(O)Br H298:-39.22 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(C)Br smiles:CC(Cl)=C(C)Br H298:-7.71 kcal/mol
library:CHOClBr_G4 label:OOC(Br)DCCl smiles:OOC(Br)=CCl H298:-6.58 kcal/mol
library:CHOClBr_G4 label:ClCDCBr smiles:ClC=CBr H298:11.77 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)OCBr smiles:ClC=C(Br)OCBr H298:-18.82 kcal/mol
library:CHOClBr_G4 label:OC(Br)DCCl smiles:OC(Br)=CCl H298:-29.88 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CCBr smiles:ClC=C(Br)CCBr H298:1.59 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)CCl smiles:CC(Br)=C(Cl)CCl H298:-11.54 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CDCBr smiles:ClC=C(Br)C=CBr H298:30.40 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)COBr smiles:ClC=C(Br)COBr H298:4.49 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)OOBr smiles:ClC=C(Br)OOBr H298:28.06 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)CCl smiles:OC(Br)=C(Cl)CCl H298:-43.33 kcal/mol
library:CHOClBr_G4 label:CCC(Br)DCCl smiles:CCC(Br)=CCl H298:-3.57 kcal/mol
library:CHOClBr_G4 label:ClC#CC(Cl)DCBr smiles:ClC#CC(Cl)=CBr H298:69.50 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Br)OBr smiles:CC(Cl)=C(Br)OBr H298:1.46 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)DCBr smiles:C=CC(Cl)=CBr H298:24.71 kcal/mol
library:CHOClBr_G4 label:COC(Br)DCCl smiles:COC(Br)=CCl H298:-23.20 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)DCCl smiles:CC(Br)C(Br)=CCl H298:0.84 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)OBr smiles:ClC=C(Br)OBr H298:12.25 kcal/mol
library:CHOClBr_G4 label:OC(Cl)DC(O)Br smiles:OC(Cl)=C(O)Br H298:-66.27 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)DCCl smiles:O=C(Br)C(Br)=CCl H298:-16.71 kcal/mol
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
        Cpdata = ([0.226774,0.168693,0.108956,0.0593441,-0.0161695,-0.046777,-0.0985371],'cal/(mol*K)','+|-',[0.0695033,0.0803518,0.0823402,0.0812345,0.0706241,0.0609898,0.0485702]),
        H298 = (1.38282,'kcal/mol','+|-',0.252394),
        S298 = (-0.0306597,'cal/(mol*K)','+|-',0.163907),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:1,2-Dichloroethene smiles:ClC=CCl H298:-0.44 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)DCCl smiles:CC(Cl)C(Cl)=CCl H298:-21.92 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)COCl smiles:ClC=C(Cl)COCl H298:-9.66 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CDC(Cl)Cl smiles:ClC=C(Cl)C=C(Cl)Cl H298:5.43 kcal/mol
library:CHOCl_G4 label:OC(Cl)DCCl smiles:OC(Cl)=CCl H298:-42.36 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)OOCl smiles:ClC=C(Cl)OOCl H298:12.51 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)Cl H298:-16.23 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DC(Cl)Cl smiles:ClC=C(Cl)C(Cl)=C(Cl)Cl H298:1.13 kcal/mol
library:CHOCl_G4 label:OOC(Cl)DCCl smiles:OOC(Cl)=CCl H298:-18.78 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-14.16 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)DCCl smiles:O=C(Cl)C(Cl)=CCl H298:-40.79 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)CCl smiles:ClC=C(Cl)C(Cl)CCl H298:-27.32 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(O)Cl smiles:OC(Cl)=C(O)Cl H298:-78.79 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)Cl H298:-30.04 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)CCl smiles:OC(Cl)=C(Cl)CCl H298:-55.72 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)OCl smiles:CC(Cl)=C(Cl)OCl H298:-12.67 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)Cl)C(Cl)Cl smiles:ClC(=C(Cl)C(Cl)Cl)C(Cl)Cl H298:-32.21 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)Cl H298:-16.64 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-20.67 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)DCCl smiles:C=CC(Cl)=CCl H298:12.89 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)CCl smiles:ClCC(Cl)=C(Cl)CCl H298:-26.27 kcal/mol
library:CHOCl_G4 label:OCC(Cl)DCCl smiles:OCC(Cl)=CCl H298:-44.11 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)OCl smiles:ClOC(Cl)=C(Cl)OCl H298:-2.85 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)DCCl smiles:ClC#CC(Cl)=CCl H298:57.67 kcal/mol
library:CHOCl_G4 label:CC(Cl)DCCl smiles:CC(Cl)=CCl H298:-10.08 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)OCl smiles:ClC=C(Cl)OCl H298:-2.29 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)DCCl smiles:O=CC(Cl)=CCl H298:-27.27 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)CCl smiles:ClC=C(Cl)C(Cl)(Cl)CCl H298:-29.97 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-31.97 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CC(Cl)Cl smiles:ClC=C(Cl)CC(Cl)Cl H298:-26.45 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)OCl smiles:ClC=C(Cl)C(Cl)(Cl)OCl H298:-19.65 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)C(Cl)Cl smiles:OC(Cl)=C(Cl)C(Cl)Cl H298:-59.29 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-23.53 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(C)Cl smiles:CC(Cl)=C(C)Cl H298:-19.60 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(O)Cl smiles:CC(Cl)=C(O)Cl H298:-51.66 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)Cl H298:-27.36 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)OC(Cl)(Cl)Cl smiles:ClC=C(Cl)OC(Cl)(Cl)Cl H298:-45.98 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-29.53 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CCl smiles:ClC=C(Cl)CCl H298:-13.01 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)DCCl smiles:OC(Cl)(Cl)C(Cl)=CCl H298:-58.64 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)DCCl smiles:C#CC(Cl)=CCl H298:58.20 kcal/mol
library:CHOCl_G4 label:COC(Cl)DCCl smiles:COC(Cl)=CCl H298:-35.27 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-53.77 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)OCl smiles:ClCC(Cl)=C(Cl)OCl H298:-15.60 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)CCl smiles:CC(Cl)=C(Cl)CCl H298:-23.69 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)C(Cl)Cl smiles:CC(Cl)=C(Cl)C(Cl)Cl H298:-25.12 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)DCCl smiles:C=C(Cl)C(Cl)=CCl H298:7.20 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-19.61 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)OC(Cl)Cl smiles:ClC=C(Cl)OC(Cl)Cl H298:-46.19 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)DCCl smiles:ClC=CC(Cl)=CCl H298:6.58 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)C(Cl)Cl smiles:ClOC(Cl)=C(Cl)C(Cl)Cl H298:-17.86 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DCCl smiles:ClC=C(Cl)C(Cl)=CCl H298:2.21 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)OCl smiles:ClC=C(Cl)C(Cl)OCl H298:-16.60 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)Cl H298:-26.83 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-28.39 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)DCCl smiles:OC(Cl)C(Cl)=CCl H298:-53.72 kcal/mol
library:CHOCl_G4 label:CCC(Cl)DCCl smiles:CCC(Cl)=CCl H298:-15.21 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)DCCl smiles:CC(Cl)(Cl)C(Cl)=CCl H298:-25.82 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CC(Cl)(Cl)Cl smiles:ClC=C(Cl)CC(Cl)(Cl)Cl H298:-27.02 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)OCCl smiles:ClC=C(Cl)OCCl H298:-42.79 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CCCl smiles:ClC=C(Cl)CCCl H298:-21.13 kcal/mol
library:CHOFCl_G4 label:FCDCC(Cl)DCCl smiles:FC=CC(Cl)=CCl H298:-31.25 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)DCCl smiles:C=C(F)C(Cl)=CCl H298:-32.54 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(Cl)CF smiles:CC(Cl)=C(Cl)CF H298:-59.88 kcal/mol
library:CHOFCl_G4 label:FC#CC(Cl)DCCl smiles:FC#CC(Cl)=CCl H298:30.34 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(Cl)CF smiles:OC(Cl)=C(Cl)CF H298:-93.25 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CCBr smiles:ClC=C(Cl)CCBr H298:-10.12 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)OCBr smiles:ClC=C(Cl)OCBr H298:-30.97 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CDCBr smiles:ClC=C(Cl)C=CBr H298:18.51 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Cl)CBr smiles:CC(Cl)=C(Cl)CBr H298:-13.25 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)DCCl smiles:OC(Br)C(Cl)=CCl H298:-40.96 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CBr smiles:ClC=C(Cl)CBr H298:-2.41 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)DCCl smiles:C=C(Br)C(Cl)=CCl H298:19.30 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Br)Br smiles:ClC=C(Cl)C(Br)Br H298:6.40 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)DCCl smiles:O=C(Br)C(Cl)=CCl H298:-28.22 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)OBr smiles:ClC=C(Cl)OBr H298:-0.21 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)DCCl smiles:CC(Br)C(Cl)=CCl H298:-10.89 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Cl)OBr smiles:CC(Cl)=C(Cl)OBr H298:-10.74 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Cl)Br smiles:ClC=C(Cl)C(Cl)Br H298:-4.69 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)OOBr smiles:ClC=C(Cl)OOBr H298:15.85 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)COBr smiles:ClC=C(Cl)COBr H298:-6.40 kcal/mol
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
        Cpdata = ([0.117762,0.0326836,-0.0108017,-0.02042,-0.0410457,-0.0503081,-0.0838488],'cal/(mol*K)','+|-',[0.0584045,0.0675207,0.0691915,0.0682624,0.0593464,0.0512505,0.0408141]),
        H298 = (2.96693,'kcal/mol','+|-',0.21209),
        S298 = (0.268529,'cal/(mol*K)','+|-',0.137733),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC#CC(F)DCF smiles:FC#CC(F)=CF H298:-43.70 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)(F)F smiles:FC=C(F)C(F)(F)C(F)(F)F H298:-332.04 kcal/mol
library:CHOF_G4 label:COC(F)DCF smiles:COC(F)=CF H298:-111.63 kcal/mol
library:CHOF_G4 label:FCDC(F)OF smiles:FC=C(F)OF H298:-86.32 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)DCF smiles:O=C(F)C(F)=CF H298:-161.53 kcal/mol
library:CHOF_G4 label:FCDC(F)COF smiles:FC=C(F)COF H298:-88.97 kcal/mol
library:CHOF_G4 label:FCDC(F)CDC(F)F smiles:FC=C(F)C=C(F)F H298:-152.09 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)OF smiles:FOC(F)=C(F)OF H298:-93.51 kcal/mol
library:CHOF_G4 label:OC(F)DC(O)F smiles:OC(F)=C(O)F H298:-157.07 kcal/mol
library:CHOF_G4 label:FCDC(F)CF smiles:FC=C(F)CF H298:-125.01 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)(F)F smiles:FCC(F)=C(F)C(F)(F)F H298:-280.88 kcal/mol
library:CHOF_G4 label:FCDC(F)CCF smiles:FC=C(F)CCF H298:-132.93 kcal/mol
library:CHOF_G4 label:OOC(F)DCF smiles:OOC(F)=CF H298:-95.82 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)(F)F smiles:FC(=C(F)C(F)(F)F)C(F)(F)F H298:-382.97 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)OF smiles:FC=C(F)C(F)OF H298:-137.80 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)OF smiles:OC(F)=C(F)OF H298:-137.60 kcal/mol
library:CHOF_G4 label:CC(F)DCF smiles:CC(F)=CF H298:-84.78 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)F smiles:FC=C(F)C(F)(F)C(F)F H298:-276.56 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)CF smiles:FC=C(F)C(F)CF H298:-175.27 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)C(F)(F)F smiles:CC(F)=C(F)C(F)(F)F H298:-241.68 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)CF smiles:OC(F)=C(F)CF H298:-169.89 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)OF smiles:FCC(F)=C(F)OF H298:-137.23 kcal/mol
library:CHOF_G4 label:CC(F)DC(C)F smiles:CC(F)=C(C)F H298:-95.64 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)F smiles:FC=C(F)C(F)(F)F H298:-231.74 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)CF smiles:FC=C(F)C(F)(F)CF H298:-227.47 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)F smiles:FC=C(F)C(F)F H298:-175.17 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)F)C(F)F smiles:FC(=C(F)C(F)F)C(F)F H298:-274.12 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)DCF smiles:CC(F)(F)C(F)=CF H298:-188.50 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)CF smiles:FCC(F)=C(F)CF H298:-174.85 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)(F)OF smiles:FC=C(F)C(F)(F)OF H298:-188.95 kcal/mol
library:CHOF_G4 label:FCDC(F)CC(F)(F)F smiles:FC=C(F)CC(F)(F)F H298:-244.62 kcal/mol
library:CHOF_G4 label:C#CC(F)DCF smiles:C#CC(F)=CF H298:-15.51 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)F smiles:FC(=C(F)C(F)(F)F)C(F)F H298:-329.07 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)F smiles:FCC(F)=C(F)C(F)F H298:-223.99 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)CF smiles:CC(F)=C(F)CF H298:-136.44 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)C(F)F smiles:OC(F)=C(F)C(F)F H298:-219.73 kcal/mol
library:CHOF_G4 label:FCDC(F)OC(F)(F)F smiles:FC=C(F)OC(F)(F)F H298:-272.26 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)OF smiles:CC(F)=C(F)OF H298:-100.52 kcal/mol
library:CHOF_G4 label:OC(F)DCF smiles:OC(F)=CF H298:-117.60 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)C(F)F smiles:FOC(F)=C(F)C(F)F H298:-183.03 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)DC(F)F smiles:FC=C(F)C(F)=C(F)F H298:-187.35 kcal/mol
library:CHOF_G4 label:OCC(F)DCF smiles:OCC(F)=CF H298:-118.01 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)C(F)F smiles:CC(F)=C(F)C(F)F H298:-186.76 kcal/mol
library:CHOF_G4 label:FCDC(F)OC(F)F smiles:FC=C(F)OC(F)F H298:-216.11 kcal/mol
library:CHOF_G4 label:OC(F)C(F)DCF smiles:OC(F)C(F)=CF H298:-170.49 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)F smiles:FC=C(F)C(F)C(F)F H298:-226.59 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)DCF smiles:OC(F)(F)C(F)=CF H298:-227.38 kcal/mol
library:CHOF_G4 label:FCDCC(F)DCF smiles:FC=CC(F)=CF H298:-105.24 kcal/mol
library:CHOF_G4 label:CCC(F)DCF smiles:CCC(F)=CF H298:-89.63 kcal/mol
library:CHOF_G4 label:ODCC(F)DCF smiles:O=CC(F)=CF H298:-100.36 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)DCF smiles:C=C(F)C(F)=CF H298:-106.22 kcal/mol
library:CHOF_G4 label:CC(F)DC(O)F smiles:CC(F)=C(O)F H298:-127.20 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)(F)F smiles:FC=C(F)C(F)C(F)(F)F H298:-283.24 kcal/mol
library:CHOF_G4 label:FCDC(F)CC(F)F smiles:FC=C(F)CC(F)F H298:-186.68 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)C(F)(F)F smiles:OC(F)=C(F)C(F)(F)F H298:-274.97 kcal/mol
library:CHOF_G4 label:FCDC(F)OCF smiles:FC=C(F)OCF H298:-161.15 kcal/mol
library:CHOF_G4 label:CDCC(F)DCF smiles:C=CC(F)=CF H298:-61.38 kcal/mol
library:CHOF_G4 label:FCDC(F)OOF smiles:FC=C(F)OOF H298:-70.42 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)DCF smiles:FC=C(F)C(F)=CF H298:-144.78 kcal/mol
library:CHOF_G4 label:CC(F)C(F)DCF smiles:CC(F)C(F)=CF H298:-134.86 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)C(F)(F)F smiles:FOC(F)=C(F)C(F)(F)F H298:-238.81 kcal/mol
library:CHOFCl_G4 label:FCDC(F)CCCl smiles:FC=C(F)CCCl H298:-94.92 kcal/mol
library:CHOFCl_G4 label:FCDC(F)OCCl smiles:FC=C(F)OCCl H298:-118.30 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(F)OCl smiles:CC(F)=C(F)OCl H298:-89.81 kcal/mol
library:CHOFCl_G4 label:CC(Cl)C(F)DCF smiles:CC(Cl)C(F)=CF H298:-95.41 kcal/mol
library:CHOFCl_G4 label:FCDC(F)OCl smiles:FC=C(F)OCl H298:-78.19 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)DCF smiles:O=C(Cl)C(F)=CF H298:-114.38 kcal/mol
library:CHOFCl_G4 label:OC(Cl)C(F)DCF smiles:OC(Cl)C(F)=CF H298:-126.01 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(F)DCF smiles:C=C(Cl)C(F)=CF H298:-67.03 kcal/mol
library:CHOFCl_G4 label:FCDC(F)CCl smiles:FC=C(F)CCl H298:-87.06 kcal/mol
library:CHOFCl_G4 label:FCDC(F)C(Cl)Cl smiles:FC=C(F)C(Cl)Cl H298:-89.17 kcal/mol
library:CHOFCl_G4 label:CC(F)DC(F)CCl smiles:CC(F)=C(F)CCl H298:-98.98 kcal/mol
library:CHOFCl_G4 label:FCDC(F)C(F)Cl smiles:FC=C(F)C(F)Cl H298:-129.92 kcal/mol
library:CHOFCl_G4 label:FCDC(F)CDCCl smiles:FC=C(F)C=CCl H298:-67.33 kcal/mol
library:CHOFCl_G4 label:FCDC(F)COCl smiles:FC=C(F)COCl H298:-83.84 kcal/mol
library:CHOFClBr_G4 label:FCDC(F)C(Cl)Br smiles:FC=C(F)C(Cl)Br H298:-77.80 kcal/mol
library:CHOFBr_G4 label:FCDC(F)COBr smiles:FC=C(F)COBr H298:-80.52 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)DCBr smiles:FC=C(F)C(F)=CBr H298:-97.78 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CDCBr smiles:FC=C(F)C=CBr H298:-55.35 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OOBr smiles:FC=C(F)OOBr H298:-60.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DCF smiles:OC(Br)C(F)=CF H298:-114.11 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)(Br)Br smiles:FC=C(F)C(Br)(Br)Br H298:-54.68 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)Br smiles:FC=C(F)C(F)Br H298:-117.56 kcal/mol
library:CHOFBr_G4 label:FOC(F)DC(F)OBr smiles:FOC(F)=C(F)OBr H298:-88.40 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)DCF smiles:CC(Br)(Br)C(F)=CF H298:-75.93 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)CBr smiles:CC(F)=C(F)CBr H298:-88.38 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DCF smiles:C=C(Br)C(F)=CF H298:-54.93 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CBr smiles:FC=C(F)CBr H298:-76.28 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)DCBr smiles:FC=C(F)C(Br)=CBr H298:-48.03 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)Br smiles:FC=C(F)C(Br)Br H298:-66.55 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)CBr smiles:FCC(F)=C(F)CBr H298:-127.49 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)OBr smiles:FC=C(F)C(Br)OBr H298:-74.69 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OC(Br)Br smiles:FC=C(F)OC(Br)Br H298:-96.32 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)DCF smiles:OC(Br)(Br)C(F)=CF H298:-107.58 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(F)Br smiles:FC=C(F)C(F)(F)Br H298:-167.75 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)OBr smiles:FC=C(F)C(F)OBr H298:-130.47 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)DCF smiles:OC(F)(Br)C(F)=CF H298:-161.23 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)CBr smiles:FC=C(F)C(F)CBr H298:-127.57 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OC(F)Br smiles:FC=C(F)OC(F)Br H298:-153.11 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)DCF smiles:CC(F)(Br)C(F)=CF H298:-129.76 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)CBr smiles:FC=C(F)C(Br)CBr H298:-78.41 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)OBr smiles:FCC(F)=C(F)OBr H298:-127.53 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(Br)Br smiles:CC(F)=C(F)C(Br)Br H298:-77.72 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DCF smiles:CC(Br)C(F)=CF H298:-84.38 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CC(F)Br smiles:FC=C(F)CC(F)Br H298:-128.58 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(F)Br smiles:CC(F)=C(F)C(F)Br H298:-130.06 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DCF smiles:O=C(Br)C(F)=CF H298:-101.47 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OBr smiles:FC=C(F)OBr H298:-76.32 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(Br)Br smiles:FC=C(F)C(F)(Br)Br H298:-108.96 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)OBr smiles:CC(F)=C(F)OBr H298:-88.57 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CDC(F)Br smiles:FC=C(F)C=C(F)Br H298:-96.22 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CC(Br)Br smiles:FC=C(F)CC(Br)Br H298:-76.64 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CDC(Br)Br smiles:FC=C(F)C=C(Br)Br H298:-44.58 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OCBr smiles:FC=C(F)OCBr H298:-106.35 kcal/mol
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
        Cpdata = ([0.168502,0.111303,0.0958215,0.0606561,0.0186967,-0.00843522,-0.0800442],'cal/(mol*K)','+|-',[0.0800251,0.0925159,0.0948053,0.0935322,0.0813156,0.0702228,0.055923]),
        H298 = (1.30535,'kcal/mol','+|-',0.290602),
        S298 = (-0.160857,'cal/(mol*K)','+|-',0.18872),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:trans-1,2-Dibromoethene smiles:BrC=CBr H298:24.24 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)OBr smiles:CC(Br)=C(Br)OBr H298:13.13 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)DCBr smiles:BrC#CC(Br)=CBr H298:91.68 kcal/mol
library:CHOBr_G4 label:OC(Br)DC(Br)CBr smiles:OC(Br)=C(Br)CBr H298:-21.57 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)DCBr smiles:O=C(Br)C(Br)=CBr H298:-4.80 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)OBr smiles:BrCC(Br)=C(Br)OBr H298:20.22 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OC(Br)Br smiles:BrC=C(Br)OC(Br)Br H298:1.71 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)OBr smiles:BrC=C(Br)C(Br)OBr H298:21.13 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)DCBr smiles:CC(Br)C(Br)=CBr H298:12.64 kcal/mol
library:CHOBr_G4 label:C#CC(Br)DCBr smiles:C#CC(Br)=CBr H298:81.50 kcal/mol
library:CHOBr_G4 label:COC(Br)DCBr smiles:COC(Br)=CBr H298:-11.92 kcal/mol
library:CHOBr_G4 label:OC(Br)DC(O)Br smiles:OC(Br)=C(O)Br H298:-54.21 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OOBr smiles:BrC=C(Br)OOBr H298:39.97 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OBr smiles:BrC=C(Br)OBr H298:23.60 kcal/mol
library:CHOBr_G4 label:CCC(Br)DCBr smiles:CCC(Br)=CBr H298:7.99 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)COBr smiles:BrC=C(Br)COBr H298:16.29 kcal/mol
library:CHOBr_G4 label:OC(Br)DCBr smiles:OC(Br)=CBr H298:-18.58 kcal/mol
library:CHOBr_G4 label:OOC(Br)DCBr smiles:OOC(Br)=CBr H298:5.33 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CCBr smiles:BrC=C(Br)CCBr H298:13.37 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OCBr smiles:BrC=C(Br)OCBr H298:-7.58 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)DCBr smiles:BrC=CC(Br)=CBr H298:42.08 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CC(Br)Br smiles:BrC=C(Br)CC(Br)Br H298:20.17 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CBr smiles:BrC=C(Br)CBr H298:20.89 kcal/mol
library:CHOBr_G4 label:CDCC(Br)DCBr smiles:C=CC(Br)=CBr H298:36.68 kcal/mol
library:CHOBr_G4 label:OCC(Br)DCBr smiles:OCC(Br)=CBr H298:-20.59 kcal/mol
library:CHOBr_G4 label:BrOC(Br)DC(Br)OBr smiles:BrOC(Br)=C(Br)OBr H298:23.63 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)CBr smiles:BrC=C(Br)C(Br)CBr H298:17.10 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)CBr smiles:BrCC(Br)=C(Br)CBr H298:17.72 kcal/mol
library:CHOBr_G4 label:CC(Br)DCBr smiles:CC(Br)=CBr H298:13.41 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DCBr smiles:O=CC(Br)=CBr H298:-3.72 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)CBr smiles:CC(Br)=C(Br)CBr H298:10.09 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(O)Br smiles:CC(Br)=C(O)Br H298:-27.74 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(C)Br smiles:CC(Br)=C(C)Br H298:4.12 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)DCBr smiles:C=C(Br)C(Br)=CBr H298:43.12 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)Br smiles:BrC=C(Br)C(Br)Br H298:29.46 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)CF smiles:OC(Br)=C(Br)CF H298:-66.57 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)CBr smiles:FCC(Br)=C(Br)CBr H298:-28.71 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)DCBr smiles:FC#CC(Br)=CBr H298:53.39 kcal/mol
library:CHOFBr_G4 label:FOC(Br)DC(Br)OBr smiles:FOC(Br)=C(Br)OBr H298:16.67 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(Br)DCBr smiles:FC(F)=CC(Br)=CBr H298:-53.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)F smiles:OC(Br)=C(Br)C(F)F H298:-118.56 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)DCBr smiles:FC=C(F)C(Br)=CBr H298:-48.03 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)DCBr smiles:FC=C(Br)C(Br)=CBr H298:0.72 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)F smiles:CC(Br)=C(Br)C(F)F H298:-89.02 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)Br smiles:CC(Br)=C(Br)C(F)Br H298:-29.49 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)DCBr smiles:FC=CC(Br)=CBr H298:-7.81 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)Br smiles:OC(Br)=C(Br)C(F)Br H298:-61.66 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DCBr smiles:C=C(F)C(Br)=CBr H298:-8.72 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCC(Br)DCBr smiles:FC(Br)=CC(Br)=CBr H298:1.85 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)CF smiles:CC(Br)=C(Br)CF H298:-36.19 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)OBr smiles:FCC(Br)=C(Br)OBr H298:-26.22 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)CCl smiles:CC(Br)=C(Br)CCl H298:0.38 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)DCBr smiles:C=C(Cl)C(Br)=CBr H298:31.07 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Br)DCBr smiles:ClC=CC(Br)=CBr H298:30.11 kcal/mol
library:CHOClBr_G4 label:ClC#CC(Br)DCBr smiles:ClC#CC(Br)=CBr H298:80.63 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Br)CCl smiles:OC(Br)=C(Br)CCl H298:-32.09 kcal/mol
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
        Cpdata = ([0.648132,0.555764,0.416778,0.281841,0.0987491,0.00736875,-0.151307],'cal/(mol*K)','+|-',[0.0992673,0.114762,0.117601,0.116022,0.100868,0.087108,0.0693698]),
        H298 = (4.23949,'kcal/mol','+|-',0.360478),
        S298 = (-0.307182,'cal/(mol*K)','+|-',0.234098),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDCC(F)DC(Cl)Cl smiles:C=CC(F)=C(Cl)Cl H298:-28.45 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)DC(F)F smiles:CCC(Cl)=C(F)F H298:-98.61 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC(Cl)OCl smiles:FC(Cl)=C(Cl)OCl H298:-42.49 kcal/mol
library:CHOFCl_G4 label:FC(F)DCCl smiles:FC(F)=CCl H298:-83.93 kcal/mol
library:CHOFCl_G4 label:CDCC(Cl)DC(F)Cl smiles:C=CC(Cl)=C(F)Cl H298:-29.05 kcal/mol
library:CHOFCl_G4 label:C#CC(F)DC(Cl)Cl smiles:C#CC(F)=C(Cl)Cl H298:17.90 kcal/mol
library:CHOFCl_G4 label:COC(Cl)DC(F)F smiles:COC(Cl)=C(F)F H298:-115.90 kcal/mol
library:CHOFCl_G4 label:CCC(Cl)DC(F)Cl smiles:CCC(Cl)=C(F)Cl H298:-57.41 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(Cl)OCl smiles:FC(F)=C(Cl)OCl H298:-82.41 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)DC(F)F smiles:O=CC(Cl)=C(F)F H298:-110.20 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(F)Cl smiles:CC(Cl)=C(F)Cl H298:-52.08 kcal/mol
library:CHOFCl_G4 label:FCDC(Cl)Cl smiles:FC=C(Cl)Cl H298:-39.96 kcal/mol
library:CHOFCl_G4 label:C#CC(F)DC(F)Cl smiles:C#CC(F)=C(F)Cl H298:-19.58 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(F)F smiles:OC(Cl)=C(F)F H298:-119.72 kcal/mol
library:CHOFCl_G4 label:CDCC(Cl)DC(F)F smiles:C=CC(Cl)=C(F)F H298:-70.30 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(Cl)CCl smiles:FC(F)=C(Cl)CCl H298:-96.34 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)DC(F)F smiles:OCC(Cl)=C(F)F H298:-127.28 kcal/mol
library:CHOFCl_G4 label:OCC(Cl)DC(F)Cl smiles:OCC(Cl)=C(F)Cl H298:-85.67 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DCCl smiles:FC(Cl)=CCl H298:-42.27 kcal/mol
library:CHOFCl_G4 label:FCDC(F)Cl smiles:FC=C(F)Cl H298:-77.75 kcal/mol
library:CHOFCl_G4 label:CC(Cl)DC(F)F smiles:CC(Cl)=C(F)F H298:-93.45 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC(Cl)CCl smiles:FC(Cl)=C(Cl)CCl H298:-55.00 kcal/mol
library:CHOFCl_G4 label:OC(Cl)DC(F)Cl smiles:OC(Cl)=C(F)Cl H298:-80.02 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)DC(F)Cl smiles:O=CC(Cl)=C(F)Cl H298:-68.16 kcal/mol
library:CHOFCl_G4 label:COC(Cl)DC(F)Cl smiles:COC(Cl)=C(F)Cl H298:-75.90 kcal/mol
library:CHOFCl_G4 label:CDCC(F)DC(F)Cl smiles:C=CC(F)=C(F)Cl H298:-66.15 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)CBr smiles:FC(Cl)=C(Cl)CBr H298:-44.48 kcal/mol
library:CHOFClBr_G4 label:OCC(Br)DC(F)Cl smiles:OCC(Br)=C(F)Cl H298:-74.36 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(F)Cl smiles:OC(Br)=C(F)Cl H298:-68.06 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)DC(F)Cl smiles:O=CC(Br)=C(F)Cl H298:-57.03 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCBr smiles:FC(Cl)=CBr H298:-30.86 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)CBr smiles:FC(Cl)=C(Br)CBr H298:-33.17 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)CBr smiles:FC(F)=C(Cl)CBr H298:-85.61 kcal/mol
library:CHOFClBr_G4 label:COC(Br)DC(F)Cl smiles:COC(Br)=C(F)Cl H298:-64.11 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)Br smiles:FC=C(Cl)Br H298:-28.19 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)OBr smiles:FC(F)=C(Cl)OBr H298:-80.48 kcal/mol
library:CHOFClBr_G4 label:CDCC(Br)DC(F)Cl smiles:C=CC(Br)=C(F)Cl H298:-17.53 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)OBr smiles:FC(Cl)=C(Br)OBr H298:-28.85 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)DC(Cl)Br smiles:C#CC(F)=C(Cl)Br H298:29.62 kcal/mol
library:CHOFClBr_G4 label:CCC(Br)DC(F)Cl smiles:CCC(Br)=C(F)Cl H298:-46.05 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)OBr smiles:FC(Cl)=C(Cl)OBr H298:-40.73 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)DC(Cl)Br smiles:C=CC(F)=C(Cl)Br H298:-16.76 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(F)Cl smiles:CC(Br)=C(F)Cl H298:-40.55 kcal/mol
library:CHOFBr_G4 label:CDCC(F)DC(F)Br smiles:C=CC(F)=C(F)Br H298:-53.64 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)OCBr smiles:FC(F)=C(Br)OCBr H298:-99.64 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)F smiles:CC(Br)C(Br)=C(F)F H298:-82.80 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)Br smiles:CC(Br)=C(F)Br H298:-28.02 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)Br smiles:C=C(Br)C(Br)=C(F)Br H298:3.03 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CCBr smiles:FC(F)=C(Br)CCBr H298:-82.07 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CBr smiles:FC(F)=C(Br)CBr H298:-74.29 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)OBr smiles:FC(Br)=C(Br)OBr H298:-16.63 kcal/mol
library:CHOFBr_G4 label:OCC(Br)DC(F)F smiles:OCC(Br)=C(F)F H298:-115.98 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)DC(Br)Br smiles:FC#CC(F)=C(Br)Br H298:12.85 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)DC(F)F smiles:C=CC(Br)=C(F)F H298:-58.83 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CDCBr smiles:FC(Br)=C(Br)C=CBr H298:0.65 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)F smiles:OC(Br)=C(F)F H298:-107.56 kcal/mol
library:CHOFBr_G4 label:CCC(Br)DC(F)Br smiles:CCC(Br)=C(F)Br H298:-33.66 kcal/mol
library:CHOFBr_G4 label:FCDC(F)Br smiles:FC=C(F)Br H298:-65.07 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)DC(F)Br smiles:FC#CC(F)=C(F)Br H298:-35.25 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCBr smiles:FC(Br)=CBr H298:-18.26 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)F smiles:C=C(Br)C(Br)=C(F)F H298:-50.23 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)C(Br)Br smiles:FC(F)=C(Br)C(Br)Br H298:-65.37 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(Br)Br smiles:C=C(F)C(F)=C(Br)Br H298:-45.81 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)OCBr smiles:FC(Br)=C(Br)OCBr H298:-47.62 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)Br smiles:O=C(Br)C(Br)=C(F)Br H298:-42.46 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)Br smiles:OC(Br)C(Br)=C(F)Br H298:-59.50 kcal/mol
library:CHOFBr_G4 label:OOC(Br)DC(F)F smiles:OOC(Br)=C(F)F H298:-87.91 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CCBr smiles:FC(Br)=C(Br)CCBr H298:-27.86 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)DC(F)Br smiles:C=CC(Br)=C(F)Br H298:-5.01 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)F smiles:CC(Br)=C(F)F H298:-81.92 kcal/mol
library:CHOFBr_G4 label:OOC(Br)DC(F)Br smiles:OOC(Br)=C(F)Br H298:-35.06 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)DC(Br)Br smiles:FC=CC(F)=C(Br)Br H298:-49.31 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)F smiles:OC(Br)C(Br)=C(F)F H298:-113.48 kcal/mol
library:CHOFBr_G4 label:C#CC(F)DC(F)Br smiles:C#CC(F)=C(F)Br H298:-7.02 kcal/mol
library:CHOFBr_G4 label:COC(Br)DC(F)Br smiles:COC(Br)=C(F)Br H298:-51.94 kcal/mol
library:CHOFBr_G4 label:CDCC(F)DC(Br)Br smiles:C=CC(F)=C(Br)Br H298:-5.11 kcal/mol
library:CHOFBr_G4 label:CCC(Br)DC(F)F smiles:CCC(Br)=C(F)F H298:-87.24 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)Br smiles:CC(Br)C(Br)=C(F)Br H298:-28.73 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)COBr smiles:FC(Br)=C(Br)COBr H298:-24.93 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)OOBr smiles:FC(Br)=C(Br)OOBr H298:-0.18 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)Br smiles:O=CC(Br)=C(F)Br H298:-44.39 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)Br smiles:OC(Br)=C(F)Br H298:-55.86 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)DC(F)Br smiles:FC=CC(F)=C(F)Br H298:-97.21 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CDCBr smiles:FC(F)=C(Br)C=CBr H298:-52.94 kcal/mol
library:CHOFBr_G4 label:OCC(Br)DC(F)Br smiles:OCC(Br)=C(F)Br H298:-61.88 kcal/mol
library:CHOFBr_G4 label:C#CC(F)DC(Br)Br smiles:C#CC(F)=C(Br)Br H298:41.16 kcal/mol
library:CHOFBr_G4 label:FC(F)DCBr smiles:FC(F)=CBr H298:-72.56 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)F smiles:O=CC(Br)=C(F)F H298:-99.12 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)F smiles:O=C(Br)C(Br)=C(F)F H298:-97.64 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(F)Br smiles:C=C(F)C(F)=C(F)Br H298:-95.50 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CBr smiles:FC(Br)=C(Br)CBr H298:-20.76 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)C(Br)Br smiles:FC(Br)=C(Br)C(Br)Br H298:-11.97 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)OBr smiles:FC(F)=C(Br)OBr H298:-68.54 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)COBr smiles:FC(F)=C(Br)COBr H298:-79.37 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)OOBr smiles:FC(F)=C(Br)OOBr H298:-53.16 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)Br smiles:FC=C(Br)Br H298:-16.62 kcal/mol
library:CHOFBr_G4 label:COC(Br)DC(F)F smiles:COC(Br)=C(F)F H298:-104.07 kcal/mol
library:CHOClBr_G4 label:OCC(Br)DC(Cl)Cl smiles:OCC(Br)=C(Cl)Cl H298:-35.20 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)DC(Cl)Br smiles:C=CC(Cl)=C(Cl)Br H298:21.50 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)DC(Cl)Br smiles:C#CC(Cl)=C(Cl)Br H298:66.54 kcal/mol
library:CHOClBr_G4 label:COC(Br)DC(Cl)Cl smiles:COC(Br)=C(Cl)Cl H298:-26.13 kcal/mol
library:CHOClBr_G4 label:CCC(Br)DC(Cl)Br smiles:CCC(Br)=C(Cl)Br H298:4.51 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)DC(Cl)Cl smiles:C=CC(Br)=C(Cl)Cl H298:21.49 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)OBr smiles:ClC(Br)=C(Br)OBr H298:20.38 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)Br smiles:ClC=C(Br)Br H298:20.00 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Br smiles:O=CC(Br)=C(Cl)Br H298:-5.60 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)Br smiles:OC(Br)=C(Cl)Br H298:-19.91 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)Cl smiles:CC(Br)=C(Cl)Cl H298:-1.60 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)Br smiles:ClC=C(Cl)Br H298:8.20 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)DC(Br)Br smiles:C=CC(Cl)=C(Br)Br H298:33.36 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)DC(Br)Br smiles:C#CC(Cl)=C(Br)Br H298:78.34 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)CBr smiles:ClC(Cl)=C(Br)CBr H298:5.67 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)OBr smiles:ClC(Cl)=C(Br)OBr H298:9.00 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCBr smiles:ClC(Cl)=CBr H298:8.06 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)Br smiles:CC(Br)=C(Cl)Br H298:10.21 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)Cl smiles:OC(Br)=C(Cl)Cl H298:-31.53 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Cl smiles:O=CC(Br)=C(Cl)Cl H298:-17.53 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)CBr smiles:ClC(Br)=C(Br)CBr H298:17.35 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)DC(Cl)Br smiles:C=CC(Br)=C(Cl)Br H298:33.35 kcal/mol
library:CHOClBr_G4 label:CCC(Br)DC(Cl)Cl smiles:CCC(Br)=C(Cl)Cl H298:-7.15 kcal/mol
library:CHOClBr_G4 label:COC(Br)DC(Cl)Br smiles:COC(Br)=C(Cl)Br H298:-14.79 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DCBr smiles:ClC(Br)=CBr H298:19.82 kcal/mol
library:CHOClBr_G4 label:OCC(Br)DC(Cl)Br smiles:OCC(Br)=C(Cl)Br H298:-23.46 kcal/mol
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
        Cpdata = ([0.743048,0.58745,0.397464,0.224956,-0.0376378,-0.113075,-0.13573],'cal/(mol*K)','+|-',[0.171372,0.198121,0.203024,0.200297,0.174136,0.150381,0.119758]),
        H298 = (4.50741,'kcal/mol','+|-',0.622319),
        S298 = (-0.573056,'cal/(mol*K)','+|-',0.40414),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Trichloroethene smiles:ClC=C(Cl)Cl H298:-3.51 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCC(Cl)DC(Cl)Cl smiles:ClC(Cl)=CC(Cl)=C(Cl)Cl H298:1.72 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-56.21 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)Cl smiles:ClCC(Cl)=C(Cl)Cl H298:-16.31 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)DC(Cl)Cl smiles:O=CC(Cl)=C(Cl)Cl H298:-29.00 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DC(Cl)Cl smiles:ClC=C(Cl)C(Cl)=C(Cl)Cl H298:1.13 kcal/mol
library:CHOCl_G4 label:OOC(Cl)DC(Cl)Cl smiles:OOC(Cl)=C(Cl)Cl H298:-20.81 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-26.72 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)OC(Cl)Cl smiles:ClC(Cl)=C(Cl)OC(Cl)Cl H298:-48.70 kcal/mol
library:CHOCl_G4 label:CCC(Cl)DC(Cl)Cl smiles:CCC(Cl)=C(Cl)Cl H298:-18.83 kcal/mol
library:CHOCl_G4 label:ClCOC(Cl)DC(Cl)Cl smiles:ClCOC(Cl)=C(Cl)Cl H298:-45.47 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-13.38 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-32.82 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)DC(Cl)Cl smiles:ClOCC(Cl)=C(Cl)Cl H298:-13.13 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)Cl smiles:OC(Cl)=C(Cl)Cl H298:-43.93 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)Cl H298:-30.71 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-24.56 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)CC(Cl)Cl smiles:ClC(Cl)=C(Cl)CC(Cl)Cl H298:-29.49 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-24.49 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)C(Cl)DC(Cl)Cl smiles:ClCC(Cl)C(Cl)=C(Cl)Cl H298:-30.56 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-28.26 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)DC(Cl)Cl smiles:O=C(Cl)C(Cl)=C(Cl)Cl H298:-39.86 kcal/mol
library:CHOCl_G4 label:OC(Cl)C(Cl)DC(Cl)Cl smiles:OC(Cl)C(Cl)=C(Cl)Cl H298:-56.83 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)Cl H298:-19.32 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)Cl smiles:CC(Cl)=C(Cl)Cl H298:-13.44 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)DC(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)=C(Cl)Cl H298:-17.72 kcal/mol
library:CHOCl_G4 label:ClOOC(Cl)DC(Cl)Cl smiles:ClOOC(Cl)=C(Cl)Cl H298:10.87 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)CC(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)CC(Cl)(Cl)Cl H298:-30.38 kcal/mol
library:CHOCl_G4 label:ClCCC(Cl)DC(Cl)Cl smiles:ClCCC(Cl)=C(Cl)Cl H298:-24.34 kcal/mol
library:CHOCl_G4 label:COC(Cl)DC(Cl)Cl smiles:COC(Cl)=C(Cl)Cl H298:-38.10 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)C(Cl)DC(Cl)Cl smiles:ClOC(Cl)C(Cl)=C(Cl)Cl H298:-19.20 kcal/mol
library:CHOCl_G4 label:OCC(Cl)DC(Cl)Cl smiles:OCC(Cl)=C(Cl)Cl H298:-46.82 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(Cl)DC(Cl)Cl smiles:CC(Cl)C(Cl)=C(Cl)Cl H298:-25.17 kcal/mol
library:CHOCl_G4 label:ClC#CC(Cl)DC(Cl)Cl smiles:ClC#CC(Cl)=C(Cl)Cl H298:54.05 kcal/mol
library:CHOCl_G4 label:ClCDCC(Cl)DC(Cl)Cl smiles:ClC=CC(Cl)=C(Cl)Cl H298:3.27 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)DC(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)=C(Cl)Cl H298:-3.12 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)Cl smiles:ClOC(Cl)=C(Cl)Cl H298:-4.69 kcal/mol
library:CHOCl_G4 label:C#CC(Cl)DC(Cl)Cl smiles:C#CC(Cl)=C(Cl)Cl H298:54.81 kcal/mol
library:CHOCl_G4 label:CDCC(Cl)DC(Cl)Cl smiles:C=CC(Cl)=C(Cl)Cl H298:9.61 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)OC(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)OC(Cl)(Cl)Cl H298:-49.32 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)DC(Cl)Cl smiles:C=C(Cl)C(Cl)=C(Cl)Cl H298:6.79 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)CBr smiles:ClC(Cl)=C(Cl)CBr H298:-5.94 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)OBr smiles:ClC(Cl)=C(Cl)OBr H298:-3.03 kcal/mol
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
        Cpdata = ([0.556309,0.321641,0.183156,0.076141,-0.0631803,-0.118203,-0.206228],'cal/(mol*K)','+|-',[0.147238,0.17022,0.174433,0.17209,0.149613,0.129203,0.102893]),
        H298 = (9.55458,'kcal/mol','+|-',0.53468),
        S298 = (0.555684,'cal/(mol*K)','+|-',0.347226),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Trifluoroethene smiles:FC=C(F)F H298:-119.07 kcal/mol
library:CHOF_G4 label:FCCC(F)DC(F)F smiles:FCCC(F)=C(F)F H298:-178.20 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)DC(F)F smiles:OC(F)(F)C(F)=C(F)F H298:-269.96 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)(F)F smiles:FC(F)=C(F)C(F)C(F)(F)F H298:-327.95 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)DC(F)F smiles:FOC(F)(F)C(F)=C(F)F H298:-232.08 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)F smiles:CC(F)=C(F)F H298:-129.99 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)F H298:-274.47 kcal/mol
library:CHOF_G4 label:CCC(F)DC(F)F smiles:CCC(F)=C(F)F H298:-134.68 kcal/mol
library:CHOF_G4 label:FCDCC(F)DC(F)F smiles:FC=CC(F)=C(F)F H298:-150.16 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)OC(F)F smiles:FC(F)=C(F)OC(F)F H298:-259.31 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)OC(F)(F)F smiles:FC(F)=C(F)OC(F)(F)F H298:-315.21 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)CC(F)F smiles:FC(F)=C(F)CC(F)F H298:-232.50 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)DC(F)F smiles:C=C(F)C(F)=C(F)F H298:-149.08 kcal/mol
library:CHOF_G4 label:FOCC(F)DC(F)F smiles:FOCC(F)=C(F)F H298:-133.99 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)F smiles:FCC(F)=C(F)F H298:-169.93 kcal/mol
library:CHOF_G4 label:OC(F)C(F)DC(F)F smiles:OC(F)C(F)=C(F)F H298:-214.83 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)CC(F)(F)F smiles:FC(F)=C(F)CC(F)(F)F H298:-289.84 kcal/mol
library:CHOF_G4 label:CDCC(F)DC(F)F smiles:C=CC(F)=C(F)F H298:-106.49 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)DC(F)F smiles:FCC(F)C(F)=C(F)F H298:-219.99 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)F smiles:OC(F)=C(F)F H298:-159.32 kcal/mol
library:CHOF_G4 label:CC(F)C(F)DC(F)F smiles:CC(F)C(F)=C(F)F H298:-179.62 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)DC(F)F smiles:FC=C(F)C(F)=C(F)F H298:-187.35 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)F smiles:FC(F)=C(F)C(F)F H298:-219.25 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)DC(F)F smiles:FOC(F)C(F)=C(F)F H298:-180.69 kcal/mol
library:CHOF_G4 label:COC(F)DC(F)F smiles:COC(F)=C(F)F H298:-154.88 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)F smiles:FC(F)=C(F)C(F)C(F)F H298:-272.23 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)DC(F)F smiles:O=C(F)C(F)=C(F)F H298:-204.75 kcal/mol
library:CHOF_G4 label:FCOC(F)DC(F)F smiles:FCOC(F)=C(F)F H298:-204.13 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)DC(F)F smiles:FC(F)=C(F)C(F)=C(F)F H298:-231.97 kcal/mol
library:CHOF_G4 label:FC#CC(F)DC(F)F smiles:FC#CC(F)=C(F)F H298:-88.30 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)C(F)(F)F H298:-374.89 kcal/mol
library:CHOF_G4 label:ODCC(F)DC(F)F smiles:O=CC(F)=C(F)F H298:-144.95 kcal/mol
library:CHOF_G4 label:OOC(F)DC(F)F smiles:OOC(F)=C(F)F H298:-139.02 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)DC(F)F smiles:FCC(F)(F)C(F)=C(F)F H298:-270.34 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)F smiles:FC(F)=C(F)C(F)(F)C(F)F H298:-319.55 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)DC(F)F smiles:CC(F)(F)C(F)=C(F)F H298:-231.21 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)F smiles:FOC(F)=C(F)F H298:-130.68 kcal/mol
library:CHOF_G4 label:C#CC(F)DC(F)F smiles:C#CC(F)=C(F)F H298:-60.14 kcal/mol
library:CHOF_G4 label:FOOC(F)DC(F)F smiles:FOOC(F)=C(F)F H298:-113.05 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)DC(F)F smiles:FC(F)=CC(F)=C(F)F H298:-196.60 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)CCl smiles:FC(F)=C(F)CCl H298:-132.03 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)OCl smiles:FC(F)=C(F)OCl H298:-120.64 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)OBr smiles:FC(F)=C(F)OBr H298:-119.31 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)COBr smiles:FC(F)=C(F)COBr H298:-125.68 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DC(F)F smiles:OC(Br)C(F)=C(F)F H298:-158.88 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(F)Br smiles:FC(F)=C(F)C(F)Br H298:-162.37 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(Br)Br smiles:FC(F)=C(F)C(Br)Br H298:-111.56 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DC(F)F smiles:CC(Br)C(F)=C(F)F H298:-129.35 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DC(F)F smiles:O=C(Br)C(F)=C(F)F H298:-145.01 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)OCBr smiles:FC(F)=C(F)OCBr H298:-149.25 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CCBr smiles:FC(F)=C(F)CCBr H298:-128.87 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CDCBr smiles:FC(F)=C(F)C=CBr H298:-100.21 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DC(F)F smiles:C=C(Br)C(F)=C(F)F H298:-96.86 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CBr smiles:FC(F)=C(F)CBr H298:-121.31 kcal/mol
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
        Cpdata = ([0.986454,0.822671,0.647888,0.47724,0.170216,0.0275919,-0.0683314],'cal/(mol*K)','+|-',[0.228813,0.264527,0.271073,0.267433,0.232503,0.200785,0.159898]),
        H298 = (3.0138,'kcal/mol','+|-',0.830909),
        S298 = (-1.09046,'cal/(mol*K)','+|-',0.5396),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OC(Br)DC(Br)Br smiles:OC(Br)=C(Br)Br H298:-8.67 kcal/mol
library:CHOBr_G4 label:BrOOC(Br)DC(Br)Br smiles:BrOOC(Br)=C(Br)Br H298:49.34 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DC(Br)Br smiles:O=CC(Br)=C(Br)Br H298:6.39 kcal/mol
library:CHOBr_G4 label:BrOC(Br)DC(Br)Br smiles:BrOC(Br)=C(Br)Br H298:32.21 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)DC(Br)Br smiles:BrCCC(Br)=C(Br)Br H298:21.61 kcal/mol
library:CHOBr_G4 label:OOC(Br)DC(Br)Br smiles:OOC(Br)=C(Br)Br H298:14.59 kcal/mol
library:CHOBr_G4 label:CCC(Br)DC(Br)Br smiles:CCC(Br)=C(Br)Br H298:16.36 kcal/mol
library:CHOBr_G4 label:COC(Br)DC(Br)Br smiles:COC(Br)=C(Br)Br H298:-3.02 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)DC(Br)Br smiles:BrC=CC(Br)=C(Br)Br H298:50.65 kcal/mol
library:CHOBr_G4 label:OCC(Br)DC(Br)Br smiles:OCC(Br)=C(Br)Br H298:-11.59 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)DC(Br)Br smiles:BrC#CC(Br)=C(Br)Br H298:99.64 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)Br smiles:BrCC(Br)=C(Br)Br H298:29.22 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)DC(Br)Br smiles:BrCOC(Br)=C(Br)Br H298:1.18 kcal/mol
library:CHOBr_G4 label:CDCC(Br)DC(Br)Br smiles:C=CC(Br)=C(Br)Br H298:45.32 kcal/mol
library:CHOBr_G4 label:BrOCC(Br)DC(Br)Br smiles:BrOCC(Br)=C(Br)Br H298:25.07 kcal/mol
library:CHOBr_G4 label:C#CC(Br)DC(Br)Br smiles:C#CC(Br)=C(Br)Br H298:89.61 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)Br smiles:CC(Br)=C(Br)Br H298:22.11 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)Br smiles:BrC=C(Br)Br H298:31.70 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)DC(Br)Br smiles:FC=CC(Br)=C(Br)Br H298:1.01 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)DC(Br)Br smiles:FC#CC(Br)=C(Br)Br H298:61.60 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DC(Br)Br smiles:C=C(F)C(Br)=C(Br)Br H298:3.56 kcal/mol
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
        Cpdata = ([0.342064,0.319705,0.189667,0.150953,-0.00104443,-0.0976853,-0.20528],'cal/(mol*K)','+|-',[0.128016,0.147997,0.151659,0.149623,0.13008,0.112335,0.0894596]),
        H298 = (2.54579,'kcal/mol','+|-',0.464875),
        S298 = (0.22529,'cal/(mol*K)','+|-',0.301894),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:FC(F)DC(Cl)Cl smiles:FC(F)=C(Cl)Cl H298:-84.81 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)Cl smiles:FC(F)=C(F)Cl H298:-121.29 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC(Cl)Cl smiles:FC(Cl)=C(Cl)Cl H298:-44.16 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)Br smiles:FC(Cl)=C(Cl)Br H298:-32.62 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)Br smiles:FC(F)=C(Cl)Br H298:-73.28 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)Br smiles:FC(Cl)=C(Br)Br H298:-21.05 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)Br smiles:FC(F)=C(F)Br H298:-108.89 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)Br smiles:FC(F)=C(Br)Br H298:-61.92 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)Br smiles:FC(Br)=C(Br)Br H298:-8.52 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)Br smiles:ClC(Br)=C(Br)Br H298:29.10 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)Br smiles:ClC(Cl)=C(Br)Br H298:17.26 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)Br smiles:ClC(Cl)=C(Cl)Br H298:5.61 kcal/mol
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
        Cpdata = ([0.445464,0.340579,0.161256,0.0827642,-0.0864749,-0.19926,-0.386928],'cal/(mol*K)','+|-',[0.42151,0.487302,0.499361,0.492655,0.428307,0.369879,0.294559]),
        H298 = (2.46051,'kcal/mol','+|-',1.53067),
        S298 = (0.380173,'cal/(mol*K)','+|-',0.994031),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Tetrachloroethene smiles:ClC(Cl)=C(Cl)Cl H298:-5.54 kcal/mol
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
        Cpdata = ([0.128616,0.174084,0.078889,0.017148,-0.0487164,-0.096651,-0.208811],'cal/(mol*K)','+|-',[0.41732,0.482458,0.494397,0.487758,0.42405,0.366202,0.291631]),
        H298 = (6.25504,'kcal/mol','+|-',1.51545),
        S298 = (0.618619,'cal/(mol*K)','+|-',0.984149),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:ATcT_halogens label:Tetrafluoroethylene smiles:FC(F)=C(F)F H298:-161.19 kcal/mol
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
        Cpdata = ([0.470363,0.444907,0.26136,0.253053,0.0251519,-0.130503,-0.243704],'cal/(mol*K)','+|-',[0.42819,0.495025,0.507275,0.500463,0.435095,0.375741,0.299227]),
        H298 = (1.77566,'kcal/mol','+|-',1.55493),
        S298 = (0.0806517,'cal/(mol*K)','+|-',1.00978),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC(Br)DC(Br)Br smiles:BrC(Br)=C(Br)Br H298:40.79 kcal/mol
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
        Cpdata = ([-0.882443,-0.539391,-0.241111,0.0781487,0.230242,0.366988,0.907638],'cal/(mol*K)','+|-',[0.260987,0.301724,0.30919,0.305038,0.265196,0.229019,0.182383]),
        H298 = (3.08554,'kcal/mol','+|-',0.947747),
        S298 = (-2.09347,'cal/(mol*K)','+|-',0.615476),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC(F)C(F)DCF smiles:O=C(F)C(F)=CF H298:-161.53 kcal/mol
library:CHOF_G4 label:CDC(F)C(DO)F smiles:C=C(F)C(=O)F H298:-121.50 kcal/mol
library:CHOF_G4 label:CDC(F)CDO smiles:C=C(F)C=O H298:-60.23 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)DC(F)F smiles:O=C(F)C(F)=C(F)F H298:-204.75 kcal/mol
library:CHOF_G4 label:ODCC(F)DCF smiles:O=CC(F)=CF H298:-100.36 kcal/mol
library:CHOF_G4 label:ODCC(F)DC(F)F smiles:O=CC(F)=C(F)F H298:-144.95 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)DCF smiles:O=C(Cl)C(F)=CF H298:-114.38 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(DO)Cl smiles:C=C(F)C(=O)Cl H298:-74.37 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(DO)Br smiles:C=C(F)C(=O)Br H298:-61.45 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DC(F)F smiles:O=C(Br)C(F)=C(F)F H298:-145.01 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DCF smiles:O=C(Br)C(F)=CF H298:-101.47 kcal/mol
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
        Cpdata = ([-0.0296005,-0.0134012,0.0232277,0.172791,0.10189,0.16798,0.81774],'cal/(mol*K)','+|-',[0.241152,0.278792,0.285691,0.281855,0.24504,0.211613,0.168521]),
        H298 = (3.4905,'kcal/mol','+|-',0.875716),
        S298 = (-0.927135,'cal/(mol*K)','+|-',0.568698),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODCC(Cl)DC(Cl)Cl smiles:O=CC(Cl)=C(Cl)Cl H298:-29.00 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)DCCl smiles:O=C(Cl)C(Cl)=CCl H298:-40.79 kcal/mol
library:CHOCl_G4 label:CDC(Cl)CDO smiles:C=C(Cl)C=O H298:-21.67 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)DCCl smiles:O=CC(Cl)=CCl H298:-27.27 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)DC(Cl)Cl smiles:O=C(Cl)C(Cl)=C(Cl)Cl H298:-39.86 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(DO)Cl smiles:C=C(Cl)C(=O)Cl H298:-35.36 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)DC(F)F smiles:O=CC(Cl)=C(F)F H298:-110.20 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)DCF smiles:O=CC(Cl)=CF H298:-64.31 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(Cl)DCF smiles:O=C(Cl)C(Cl)=CF H298:-78.04 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)DC(F)Cl smiles:O=CC(Cl)=C(F)Cl H298:-68.16 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)DCF smiles:O=C(Br)C(Cl)=CF H298:-65.38 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(DO)Br smiles:C=C(Cl)C(=O)Br H298:-22.77 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)DCCl smiles:O=C(Br)C(Cl)=CCl H298:-28.22 kcal/mol
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
        Cpdata = ([0.19154,0.188858,0.173791,0.269076,0.120617,0.151773,0.868473],'cal/(mol*K)','+|-',[0.219275,0.253501,0.259774,0.256286,0.222811,0.192416,0.153233]),
        H298 = (3.39742,'kcal/mol','+|-',0.796274),
        S298 = (-1.21546,'cal/(mol*K)','+|-',0.517108),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODC(Br)C(Br)DCBr smiles:O=C(Br)C(Br)=CBr H298:-4.80 kcal/mol
library:CHOBr_G4 label:CDC(Br)CDO smiles:C=C(Br)C=O H298:-9.80 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DC(Br)Br smiles:O=CC(Br)=C(Br)Br H298:6.39 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(DO)Br smiles:C=C(Br)C(=O)Br H298:-11.05 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DCBr smiles:O=CC(Br)=CBr H298:-3.72 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)DC(F)Cl smiles:O=CC(Br)=C(F)Cl H298:-57.03 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)Br smiles:O=C(Br)C(Br)=C(F)Br H298:-42.46 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DCF smiles:O=C(Br)C(Br)=CF H298:-54.16 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)Br smiles:O=CC(Br)=C(F)Br H298:-44.39 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)F smiles:O=CC(Br)=C(F)F H298:-99.12 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)F smiles:O=C(Br)C(Br)=C(F)F H298:-97.64 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DCF smiles:O=CC(Br)=CF H298:-52.97 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DCCl smiles:O=CC(Br)=CCl H298:-15.62 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Br smiles:O=CC(Br)=C(Cl)Br H298:-5.60 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Cl smiles:O=CC(Br)=C(Cl)Cl H298:-17.53 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)DCCl smiles:O=C(Br)C(Br)=CCl H298:-16.71 kcal/mol
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
        Cpdata = ([0.813343,0.659631,0.457837,0.259996,-0.0538569,-0.241223,-0.100068],'cal/(mol*K)','+|-',[0.148632,0.171832,0.176084,0.173719,0.151029,0.130426,0.103867]),
        H298 = (7.19518,'kcal/mol','+|-',0.539742),
        S298 = (1.02588,'cal/(mol*K)','+|-',0.350513),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODCC(F)(Cl)Cl smiles:O=CC(F)(Cl)Cl H298:-89.76 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)(F)Cl smiles:O=C(Cl)C(F)(F)Cl H298:-148.76 kcal/mol
library:CHOFCl_G4 label:ODCC(F)(F)Cl smiles:O=CC(F)(F)Cl H298:-135.75 kcal/mol
library:CHOFCl_G4 label:CC(DO)C(F)(Cl)Cl smiles:CC(=O)C(F)(Cl)Cl H298:-103.02 kcal/mol
library:CHOFCl_G4 label:ODC(O)C(F)(Cl)Cl smiles:O=C(O)C(F)(Cl)Cl H298:-148.47 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)(Cl)Cl smiles:O=C(Cl)C(F)(Cl)Cl H298:-102.41 kcal/mol
library:CHOFCl_G4 label:CC(DO)C(F)(F)Cl smiles:CC(=O)C(F)(F)Cl H298:-149.58 kcal/mol
library:CHOFCl_G4 label:ODC(O)C(F)(F)Cl smiles:O=C(O)C(F)(F)Cl H298:-195.29 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)(Cl)Cl smiles:O=C(Br)C(F)(Cl)Cl H298:-90.01 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)(Cl)Br smiles:O=C(Br)C(F)(Cl)Br H298:-77.20 kcal/mol
library:CHOFClBr_G4 label:ODC(O)C(F)(Cl)Br smiles:O=C(O)C(F)(Cl)Br H298:-136.08 kcal/mol
library:CHOFClBr_G4 label:CC(DO)C(F)(Cl)Br smiles:CC(=O)C(F)(Cl)Br H298:-90.57 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)(F)Cl smiles:O=C(Br)C(F)(F)Cl H298:-136.15 kcal/mol
library:CHOFClBr_G4 label:ODCC(F)(Cl)Br smiles:O=CC(F)(Cl)Br H298:-77.50 kcal/mol
library:CHOFBr_G4 label:ODC(O)C(F)(F)Br smiles:O=C(O)C(F)(F)Br H298:-182.10 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)Br smiles:O=C(Br)C(F)(F)Br H298:-123.06 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)(Br)Br smiles:O=C(OBr)C(F)(Br)Br H298:-82.29 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)(F)Br smiles:O=C(OBr)C(F)(F)Br H298:-140.27 kcal/mol
library:CHOFBr_G4 label:CC(DO)C(F)(F)Br smiles:CC(=O)C(F)(F)Br H298:-136.45 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(Br)Br smiles:O=C(CF)C(F)(Br)Br H298:-115.07 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(F)Br smiles:O=C(CF)C(F)(F)Br H298:-173.42 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)Br smiles:O=CC(F)(Br)Br H298:-65.35 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(Br)Br smiles:O=C(CBr)C(F)(Br)Br H298:-67.58 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(F)Br smiles:O=CC(F)(F)Br H298:-122.64 kcal/mol
library:CHOFBr_G4 label:ODC(O)C(F)(Br)Br smiles:O=C(O)C(F)(Br)Br H298:-123.74 kcal/mol
library:CHOFBr_G4 label:CC(DO)C(F)(Br)Br smiles:CC(=O)C(F)(Br)Br H298:-78.42 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)Br smiles:O=C(CBr)C(F)(F)Br H298:-125.44 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)Br smiles:O=C(Br)C(F)(Br)Br H298:-65.37 kcal/mol
library:CHOClBr_G4 label:ODC(O)C(Cl)(Br)Br smiles:O=C(O)C(Cl)(Br)Br H298:-81.09 kcal/mol
library:CHOClBr_G4 label:CC(DO)C(Cl)(Cl)Br smiles:CC(=O)C(Cl)(Cl)Br H298:-47.86 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)(Br)Br smiles:O=C(Br)C(Cl)(Br)Br H298:-23.11 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)Br smiles:O=CC(Cl)(Br)Br H298:-24.13 kcal/mol
library:CHOClBr_G4 label:CC(DO)C(Cl)(Br)Br smiles:CC(=O)C(Cl)(Br)Br H298:-36.21 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Cl)Br smiles:O=CC(Cl)(Cl)Br H298:-35.61 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)(Cl)Br smiles:O=C(Br)C(Cl)(Cl)Br H298:-34.73 kcal/mol
library:CHOClBr_G4 label:ODC(O)C(Cl)(Cl)Br smiles:O=C(O)C(Cl)(Cl)Br H298:-92.76 kcal/mol
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
        Cpdata = ([0.210574,0.168575,0.152436,0.0858227,-0.0704353,-0.143771,-0.0264598],'cal/(mol*K)','+|-',[0.230895,0.266935,0.27354,0.269867,0.234619,0.202613,0.161354]),
        H298 = (12.5682,'kcal/mol','+|-',0.838471),
        S298 = (0.330367,'cal/(mol*K)','+|-',0.544511),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC(F)C(F)(F)F smiles:O=C(F)C(F)(F)F H298:-244.46 kcal/mol
library:CHOF_G4 label:ODC(CF)C(F)(F)F smiles:O=C(CF)C(F)(F)F H298:-235.86 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)F smiles:O=CC(F)(F)F H298:-185.36 kcal/mol
library:CHOF_G4 label:ODC(C(F)(F)F)C(F)(F)F smiles:O=C(C(F)(F)F)C(F)(F)F H298:-339.08 kcal/mol
library:CHOF_G4 label:ODC(C(F)F)C(F)(F)F smiles:O=C(C(F)F)C(F)(F)F H298:-283.71 kcal/mol
library:CHOF_G4 label:CC(DO)C(F)(F)F smiles:CC(=O)C(F)(F)F H298:-199.41 kcal/mol
library:CHOF_G4 label:ODC(O)C(F)(F)F smiles:O=C(O)C(F)(F)F H298:-245.55 kcal/mol
library:CHOF_G4 label:ODC(OF)C(F)(F)F smiles:O=C(OF)C(F)(F)F H298:-204.13 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)(F)F smiles:O=C(Cl)C(F)(F)F H298:-198.57 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)F smiles:O=C(CBr)C(F)(F)F H298:-188.20 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)(F)F smiles:O=C(OBr)C(F)(F)F H298:-203.38 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)F smiles:O=C(Br)C(F)(F)F H298:-185.81 kcal/mol
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
        Cpdata = ([0.951626,0.749798,0.505897,0.291568,-0.0250023,-0.22186,-0.272306],'cal/(mol*K)','+|-',[0.258993,0.299418,0.306828,0.302707,0.263169,0.227269,0.180989]),
        H298 = (9.39697,'kcal/mol','+|-',0.940505),
        S298 = (0.458842,'cal/(mol*K)','+|-',0.610773),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)Cl H298:-58.76 kcal/mol
library:CHOCl_G4 label:ODC(CCl)C(Cl)(Cl)Cl smiles:O=C(CCl)C(Cl)(Cl)Cl H298:-59.61 kcal/mol
library:CHOCl_G4 label:ODC(O)C(Cl)(Cl)Cl smiles:O=C(O)C(Cl)(Cl)Cl H298:-104.44 kcal/mol
library:CHOCl_G4 label:ODC(OCl)C(Cl)(Cl)Cl smiles:O=C(OCl)C(Cl)(Cl)Cl H298:-64.24 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)Cl smiles:O=CC(Cl)(Cl)Cl H298:-47.16 kcal/mol
library:CHOCl_G4 label:ODC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:O=C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-57.79 kcal/mol
library:CHOCl_G4 label:ODC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:O=C(C(Cl)Cl)C(Cl)(Cl)Cl H298:-61.75 kcal/mol
library:CHOCl_G4 label:CC(DO)C(Cl)(Cl)Cl smiles:CC(=O)C(Cl)(Cl)Cl H298:-59.56 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)(Cl)Cl smiles:O=C(Br)C(Cl)(Cl)Cl H298:-46.41 kcal/mol
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
        Cpdata = ([0.892084,0.738966,0.444783,0.113696,-0.37837,-0.591389,-0.343791],'cal/(mol*K)','+|-',[0.390082,0.450969,0.462128,0.455923,0.396373,0.342301,0.272596]),
        H298 = (7.19029,'kcal/mol','+|-',1.41654),
        S298 = (2.23463,'cal/(mol*K)','+|-',0.919915),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODCC(Br)(Br)Br smiles:O=CC(Br)(Br)Br H298:-12.64 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)(Br)Br smiles:O=C(Br)C(Br)(Br)Br H298:-11.61 kcal/mol
library:CHOBr_G4 label:ODC(O)C(Br)(Br)Br smiles:O=C(O)C(Br)(Br)Br H298:-69.36 kcal/mol
library:CHOBr_G4 label:CC(DO)C(Br)(Br)Br smiles:CC(=O)C(Br)(Br)Br H298:-24.59 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)(Br)Br smiles:O=C(CF)C(Br)(Br)Br H298:-61.84 kcal/mol
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
        Cpdata = ([0.885442,0.680214,0.504081,0.312941,0.043014,-0.0790486,0.0272275],'cal/(mol*K)','+|-',[0.121726,0.140726,0.144208,0.142272,0.123689,0.106816,0.0850645]),
        H298 = (5.27354,'kcal/mol','+|-',0.442036),
        S298 = (0.109958,'cal/(mol*K)','+|-',0.287062),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODC(Cl)C(F)Cl smiles:O=C(Cl)C(F)Cl H298:-99.36 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)C(DO)Cl smiles:CC(F)(Cl)C(=O)Cl H298:-111.88 kcal/mol
library:CHOFCl_G4 label:ODC(O)C(F)Cl smiles:O=C(O)C(F)Cl H298:-145.40 kcal/mol
library:CHOFCl_G4 label:ODC(F)C(O)(F)Cl smiles:O=C(F)C(O)(F)Cl H298:-191.81 kcal/mol
library:CHOFCl_G4 label:ODC(CCl)C(F)Cl smiles:O=C(CCl)C(F)Cl H298:-99.47 kcal/mol
library:CHOFCl_G4 label:CC(F)(Cl)CDO smiles:CC(F)(Cl)C=O H298:-98.33 kcal/mol
library:CHOFCl_G4 label:CC(DO)C(F)Cl smiles:CC(=O)C(F)Cl H298:-99.25 kcal/mol
library:CHOFCl_G4 label:ODCC(F)Cl smiles:O=CC(F)Cl H298:-85.54 kcal/mol
library:CHOFCl_G4 label:ODC(OCl)C(F)Cl smiles:O=C(OCl)C(F)Cl H298:-105.24 kcal/mol
library:CHOFCl_G4 label:ODC(CF)C(F)Cl smiles:O=C(CF)C(F)Cl H298:-136.62 kcal/mol
library:CHOFCl_G4 label:ODCC(F)(Cl)OCl smiles:O=CC(F)(Cl)OCl H298:-93.01 kcal/mol
library:CHOFCl_G4 label:ODCC(F)(Cl)CF smiles:O=CC(F)(Cl)CF H298:-137.80 kcal/mol
library:CHOFCl_G4 label:ODCC(O)(F)Cl smiles:O=CC(O)(F)Cl H298:-134.51 kcal/mol
library:CHOFClBr_G4 label:ODC(F)C(O)(Cl)Br smiles:O=C(F)C(O)(Cl)Br H298:-134.36 kcal/mol
library:CHOFClBr_G4 label:ODCC(Cl)(Br)CF smiles:O=CC(Cl)(Br)CF H298:-85.48 kcal/mol
library:CHOFClBr_G4 label:ODCC(F)(Cl)OBr smiles:O=CC(F)(Cl)OBr H298:-91.25 kcal/mol
library:CHOFClBr_G4 label:ODC(CBr)C(F)Cl smiles:O=C(CBr)C(F)Cl H298:-88.71 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)Cl smiles:O=C(Br)C(F)Cl H298:-86.85 kcal/mol
library:CHOFClBr_G4 label:ODC(OBr)C(F)Cl smiles:O=C(OBr)C(F)Cl H298:-103.85 kcal/mol
library:CHOFClBr_G4 label:ODC(CF)C(Cl)Br smiles:O=C(CF)C(Cl)Br H298:-85.20 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(DO)Br smiles:CC(F)(Cl)C(=O)Br H298:-99.47 kcal/mol
library:CHOFBr_G4 label:ODCC(O)(F)Br smiles:O=CC(O)(F)Br H298:-121.72 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(F)(Br)OBr smiles:O=C(F)C(F)(Br)OBr H298:-137.20 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)Br smiles:O=C(OBr)C(F)Br H298:-91.84 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)OBr smiles:O=CC(F)(Br)OBr H298:-78.80 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)Br smiles:O=C(Br)C(F)Br H298:-74.85 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CDO smiles:CC(F)(Br)C=O H298:-86.15 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(DO)Br smiles:CC(F)(Br)C(=O)Br H298:-87.36 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)Br smiles:O=C(CBr)C(F)Br H298:-76.70 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)Br smiles:O=C(CF)C(F)Br H298:-124.56 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(F)Br smiles:O=C(C(F)F)C(F)Br H298:-172.91 kcal/mol
library:CHOFBr_G4 label:ODCC(F)Br smiles:O=CC(F)Br H298:-73.41 kcal/mol
library:CHOFBr_G4 label:CC(DO)C(F)Br smiles:CC(=O)C(F)Br H298:-87.14 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)CF smiles:O=CC(F)(Br)CF H298:-125.89 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)C(F)F smiles:O=CC(F)(Br)C(F)F H298:-174.91 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(O)(F)Br smiles:O=C(F)C(O)(F)Br H298:-178.94 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)CF smiles:O=C(Br)C(F)(Br)CF H298:-127.23 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)Br)C(Br)Br smiles:O=C(C(F)Br)C(Br)Br H298:-66.27 kcal/mol
library:CHOFBr_G4 label:ODC(O)C(F)Br smiles:O=C(O)C(F)Br H298:-133.28 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)Br smiles:O=C(Br)C(Cl)Br H298:-35.35 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(DO)Br smiles:CC(Cl)(Br)C(=O)Br H298:-45.98 kcal/mol
library:CHOClBr_G4 label:CC(DO)C(Cl)Br smiles:CC(=O)C(Cl)Br H298:-47.41 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Br smiles:O=C(CBr)C(Cl)Br H298:-37.03 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)Br smiles:O=CC(Cl)Br H298:-34.49 kcal/mol
library:CHOClBr_G4 label:ODCC(O)(Cl)Br smiles:O=CC(O)(Cl)Br H298:-78.19 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)OBr smiles:O=CC(Cl)(Br)OBr H298:-34.75 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CDO smiles:CC(Cl)(Br)C=O H298:-45.96 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)CCl smiles:O=CC(Cl)(Br)CCl H298:-47.33 kcal/mol
library:CHOClBr_G4 label:ODC(O)C(Cl)Br smiles:O=C(O)C(Cl)Br H298:-93.39 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Cl)Br smiles:O=C(CCl)C(Cl)Br H298:-47.74 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(O)(Cl)Br smiles:O=C(Cl)C(O)(Cl)Br H298:-89.13 kcal/mol
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
        Cpdata = ([0.464471,0.254814,0.141698,0.0160275,-0.107413,-0.167303,0.0679098],'cal/(mol*K)','+|-',[0.15113,0.174719,0.179042,0.176638,0.153567,0.132618,0.105612]),
        H298 = (5.56742,'kcal/mol','+|-',0.548811),
        S298 = (-0.127974,'cal/(mol*K)','+|-',0.356403),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC(OF)C(F)F smiles:O=C(OF)C(F)F H298:-154.18 kcal/mol
library:CHOF_G4 label:ODC(O)C(F)F smiles:O=C(O)C(F)F H298:-189.70 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)C(F)F smiles:O=CC(F)(F)C(F)F H298:-230.22 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)OF smiles:O=C(F)C(F)(F)OF H298:-200.39 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)CF smiles:O=C(F)C(F)(F)CF H298:-240.95 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)C(F)(F)F smiles:O=C(F)C(F)(F)C(F)(F)F H298:-344.15 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)C(F)(F)F smiles:O=CC(F)(F)C(F)(F)F H298:-285.38 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(DO)F smiles:CC(F)(F)C(=O)F H298:-203.70 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)OF smiles:O=CC(F)(F)OF H298:-141.97 kcal/mol
library:CHOF_G4 label:ODC(C(F)F)C(F)(F)F smiles:O=C(C(F)F)C(F)(F)F H298:-283.71 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)CF smiles:O=CC(F)(F)CF H298:-181.03 kcal/mol
library:CHOF_G4 label:ODC(CF)C(F)F smiles:O=C(CF)C(F)F H298:-180.57 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)F smiles:O=C(F)C(F)F H298:-189.41 kcal/mol
library:CHOF_G4 label:ODC(F)C(O)(F)F smiles:O=C(F)C(O)(F)F H298:-241.20 kcal/mol
library:CHOF_G4 label:CC(DO)C(F)F smiles:CC(=O)C(F)F H298:-143.18 kcal/mol
library:CHOF_G4 label:ODCC(O)(F)F smiles:O=CC(O)(F)F H298:-183.24 kcal/mol
library:CHOF_G4 label:ODC(C(F)F)C(F)F smiles:O=C(C(F)F)C(F)F H298:-228.60 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)C(F)F smiles:O=C(F)C(F)(F)C(F)F H298:-289.49 kcal/mol
library:CHOF_G4 label:ODCC(F)F smiles:O=CC(F)F H298:-129.46 kcal/mol
library:CHOF_G4 label:CC(F)(F)CDO smiles:CC(F)(F)C=O H298:-143.13 kcal/mol
library:CHOFCl_G4 label:ODC(CCl)C(F)F smiles:O=C(CCl)C(F)F H298:-143.31 kcal/mol
library:CHOFCl_G4 label:ODC(OCl)C(F)F smiles:O=C(OCl)C(F)F H298:-149.40 kcal/mol
library:CHOFCl_G4 label:CC(F)(F)C(DO)Cl smiles:CC(F)(F)C(=O)Cl H298:-157.27 kcal/mol
library:CHOFCl_G4 label:ODCC(F)(F)OCl smiles:O=CC(F)(F)OCl H298:-140.52 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)F smiles:O=C(Cl)C(F)F H298:-143.47 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)CF smiles:O=C(Br)C(F)(F)CF H298:-182.34 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)F smiles:O=C(Br)C(F)F H298:-130.81 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)F smiles:O=C(CBr)C(F)F H298:-132.07 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(Br)Br smiles:O=C(C(F)F)C(Br)Br H298:-121.87 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(F)OBr smiles:O=CC(F)(F)OBr H298:-138.85 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(F)Br smiles:O=C(C(F)F)C(F)Br H298:-172.91 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)F smiles:O=C(OBr)C(F)F H298:-147.96 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(DO)Br smiles:CC(F)(F)C(=O)Br H298:-144.72 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(F)(F)OBr smiles:O=C(F)C(F)(F)OBr H298:-197.88 kcal/mol
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
        Cpdata = ([0.928696,0.795743,0.646013,0.46323,0.248721,0.110632,0.222768],'cal/(mol*K)','+|-',[0.164775,0.190494,0.195208,0.192587,0.167432,0.144592,0.115148]),
        H298 = (3.09355,'kcal/mol','+|-',0.598363),
        S298 = (-1.16309,'cal/(mol*K)','+|-',0.388583),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC(Cl)C(O)(Cl)Cl smiles:O=C(Cl)C(O)(Cl)Cl H298:-101.31 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)C(Cl)Cl smiles:O=CC(Cl)(Cl)C(Cl)Cl H298:-60.87 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)OCl smiles:O=CC(Cl)(Cl)OCl H298:-48.54 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-70.00 kcal/mol
library:CHOCl_G4 label:ODC(CCl)C(Cl)Cl smiles:O=C(CCl)C(Cl)Cl H298:-58.85 kcal/mol
library:CHOCl_G4 label:ODC(O)C(Cl)Cl smiles:O=C(O)C(Cl)Cl H298:-104.61 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(DO)Cl smiles:CC(Cl)(Cl)C(=O)Cl H298:-69.94 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)C(Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)C(Cl)Cl H298:-74.08 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)CCl smiles:O=C(Cl)C(Cl)(Cl)CCl H298:-72.19 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)Cl smiles:O=C(Cl)C(Cl)Cl H298:-58.96 kcal/mol
library:CHOCl_G4 label:ODCC(O)(Cl)Cl smiles:O=CC(O)(Cl)Cl H298:-90.10 kcal/mol
library:CHOCl_G4 label:ODC(OCl)C(Cl)Cl smiles:O=C(OCl)C(Cl)Cl H298:-68.94 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:O=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-60.22 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)OCl smiles:O=C(Cl)C(Cl)(Cl)OCl H298:-60.85 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)Cl smiles:O=CC(Cl)Cl H298:-45.72 kcal/mol
library:CHOCl_G4 label:ODC(C(Cl)Cl)C(Cl)Cl smiles:O=C(C(Cl)Cl)C(Cl)Cl H298:-60.84 kcal/mol
library:CHOCl_G4 label:CC(DO)C(Cl)Cl smiles:CC(=O)C(Cl)Cl H298:-58.73 kcal/mol
library:CHOCl_G4 label:ODC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:O=C(C(Cl)Cl)C(Cl)(Cl)Cl H298:-61.75 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)CCl smiles:O=CC(Cl)(Cl)CCl H298:-58.99 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)CDO smiles:CC(Cl)(Cl)C=O H298:-57.33 kcal/mol
library:CHOFCl_G4 label:ODC(CF)C(Cl)Cl smiles:O=C(CF)C(Cl)Cl H298:-95.96 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)(Cl)CF smiles:O=CC(Cl)(Cl)CF H298:-96.67 kcal/mol
library:CHOFCl_G4 label:ODC(F)C(O)(Cl)Cl smiles:O=C(F)C(O)(Cl)Cl H298:-146.42 kcal/mol
library:CHOClBr_G4 label:ODC(OBr)C(Cl)Cl smiles:O=C(OBr)C(Cl)Cl H298:-63.33 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Cl smiles:O=C(CBr)C(Cl)Cl H298:-48.27 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(DO)Br smiles:CC(Cl)(Cl)C(=O)Br H298:-57.48 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Cl)OBr smiles:O=CC(Cl)(Cl)OBr H298:-46.53 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)Cl smiles:O=C(Br)C(Cl)Cl H298:-46.53 kcal/mol
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
        Cpdata = ([0.556018,0.527273,0.464056,0.345068,0.215059,0.12491,0.236758],'cal/(mol*K)','+|-',[0.183507,0.212151,0.2174,0.214481,0.186467,0.16103,0.128238]),
        H298 = (3.09273,'kcal/mol','+|-',0.666387),
        S298 = (-0.707153,'cal/(mol*K)','+|-',0.432758),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODCC(Br)(Br)OBr smiles:O=CC(Br)(Br)OBr H298:-22.97 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)CDO smiles:CC(Br)(Br)C=O H298:-34.70 kcal/mol
library:CHOBr_G4 label:ODCC(Br)Br smiles:O=CC(Br)Br H298:-23.42 kcal/mol
library:CHOBr_G4 label:ODCC(O)(Br)Br smiles:O=CC(O)(Br)Br H298:-66.49 kcal/mol
library:CHOBr_G4 label:ODC(CBr)C(Br)Br smiles:O=C(CBr)C(Br)Br H298:-25.79 kcal/mol
library:CHOBr_G4 label:CC(DO)C(Br)Br smiles:CC(=O)C(Br)Br H298:-36.17 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)Br smiles:O=C(Br)C(Br)Br H298:-24.24 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(O)(Br)Br smiles:O=C(Br)C(O)(Br)Br H298:-64.75 kcal/mol
library:CHOBr_G4 label:ODC(OBr)C(Br)Br smiles:O=C(OBr)C(Br)Br H298:-41.14 kcal/mol
library:CHOBr_G4 label:ODC(O)C(Br)Br smiles:O=C(O)C(Br)Br H298:-82.18 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(DO)Br smiles:CC(Br)(Br)C(=O)Br H298:-34.47 kcal/mol
library:CHOBr_G4 label:ODCC(Br)(Br)CBr smiles:O=CC(Br)(Br)CBr H298:-25.71 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)Br smiles:O=CC(Br)(Br)C(F)Br H298:-67.14 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)F smiles:O=CC(Br)(Br)C(F)F H298:-124.59 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(O)(Br)Br smiles:O=C(F)C(O)(Br)Br H298:-122.39 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)Br smiles:O=C(CF)C(Br)Br H298:-73.83 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(Br)Br smiles:O=C(C(F)F)C(Br)Br H298:-121.87 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)(Br)CF smiles:O=C(Br)C(Br)(Br)CF H298:-74.61 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)CF smiles:O=CC(Br)(Br)CF H298:-74.39 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(Br)(Br)OBr smiles:O=C(F)C(Br)(Br)OBr H298:-80.52 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)Br)C(Br)Br smiles:O=C(C(F)Br)C(Br)Br H298:-66.27 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)(Br)CCl smiles:O=CC(Br)(Br)CCl H298:-36.74 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(O)(Br)Br smiles:O=C(Cl)C(O)(Br)Br H298:-77.22 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Br)Br smiles:O=C(CCl)C(Br)Br H298:-36.55 kcal/mol
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
        Cpdata = ([0.691229,0.571634,0.471272,0.367861,0.256118,0.144906,0.251817],'cal/(mol*K)','+|-',[0.134735,0.155765,0.159619,0.157476,0.136907,0.118231,0.094155]),
        H298 = (2.66265,'kcal/mol','+|-',0.489274),
        S298 = (-0.383865,'cal/(mol*K)','+|-',0.317739),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:CC(F)CDO smiles:CC(F)C=O H298:-89.77 kcal/mol
library:CHOF_G4 label:ODC(F)C(O)F smiles:O=C(F)C(O)F H298:-187.24 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)C(F)(F)F smiles:O=C(F)C(F)C(F)(F)F H298:-298.02 kcal/mol
library:CHOF_G4 label:ODC(F)CF smiles:O=C(F)CF H298:-142.40 kcal/mol
library:CHOF_G4 label:ODCCF smiles:O=CCF H298:-79.81 kcal/mol
library:CHOF_G4 label:ODC(CF)OF smiles:O=C(CF)OF H298:-101.68 kcal/mol
library:CHOF_G4 label:ODC(CF)CF smiles:O=C(CF)CF H298:-131.42 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)OF smiles:O=C(F)C(F)OF H298:-151.61 kcal/mol
library:CHOF_G4 label:ODC(CF)C(F)(F)F smiles:O=C(CF)C(F)(F)F H298:-235.86 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)CF smiles:O=C(F)C(F)CF H298:-191.81 kcal/mol
library:CHOF_G4 label:ODCC(O)F smiles:O=CC(O)F H298:-126.37 kcal/mol
library:CHOF_G4 label:ODCC(F)C(F)F smiles:O=CC(F)C(F)F H298:-180.26 kcal/mol
library:CHOF_G4 label:ODCC(F)CF smiles:O=CC(F)CF H298:-130.64 kcal/mol
library:CHOF_G4 label:ODC(CF)C(F)F smiles:O=C(CF)C(F)F H298:-180.57 kcal/mol
library:CHOF_G4 label:ODCC(F)OF smiles:O=CC(F)OF H298:-91.01 kcal/mol
library:CHOF_G4 label:CC(F)C(DO)F smiles:CC(F)C(=O)F H298:-152.03 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)C(F)F smiles:O=C(F)C(F)C(F)F H298:-241.91 kcal/mol
library:CHOF_G4 label:ODCC(F)C(F)(F)F smiles:O=CC(F)C(F)(F)F H298:-237.65 kcal/mol
library:CHOF_G4 label:CC(DO)CF smiles:CC(=O)CF H298:-93.02 kcal/mol
library:CHOF_G4 label:ODC(O)CF smiles:O=C(O)CF H298:-140.50 kcal/mol
library:CHOFCl_G4 label:ODC(CF)C(Cl)Cl smiles:O=C(CF)C(Cl)Cl H298:-95.96 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)CF smiles:O=C(Cl)CF H298:-95.87 kcal/mol
library:CHOFCl_G4 label:ODC(CF)C(F)Cl smiles:O=C(CF)C(F)Cl H298:-136.62 kcal/mol
library:CHOFCl_G4 label:ODC(F)C(F)OCl smiles:O=C(F)C(F)OCl H298:-147.14 kcal/mol
library:CHOFCl_G4 label:ODC(CF)OCl smiles:O=C(CF)OCl H298:-101.15 kcal/mol
library:CHOFCl_G4 label:ODC(CF)CCl smiles:O=C(CF)CCl H298:-93.96 kcal/mol
library:CHOFCl_G4 label:ODCC(F)OCl smiles:O=CC(F)OCl H298:-86.82 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(F)CF smiles:O=C(Cl)C(F)CF H298:-145.69 kcal/mol
library:CHOFCl_G4 label:CC(F)C(DO)Cl smiles:CC(F)C(=O)Cl H298:-106.01 kcal/mol
library:CHOFClBr_G4 label:ODC(CF)C(Cl)Br smiles:O=C(CF)C(Cl)Br H298:-85.20 kcal/mol
library:CHOFBr_G4 label:CC(F)C(DO)Br smiles:CC(F)C(=O)Br H298:-93.34 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CF smiles:O=C(Br)CF H298:-83.39 kcal/mol
library:CHOFBr_G4 label:ODCC(F)OBr smiles:O=CC(F)OBr H298:-84.23 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)CF smiles:O=C(Br)C(F)CF H298:-133.66 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(Br)Br smiles:O=C(CF)C(F)(Br)Br H298:-115.07 kcal/mol
library:CHOFBr_G4 label:ODC(CF)CBr smiles:O=C(CF)CBr H298:-83.42 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)Br smiles:O=C(CF)C(Br)Br H298:-73.83 kcal/mol
library:CHOFBr_G4 label:ODC(CF)OBr smiles:O=C(CF)OBr H298:-99.55 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(F)OBr smiles:O=C(F)C(F)OBr H298:-144.93 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)C(F)F smiles:O=C(Br)C(F)C(F)F H298:-182.79 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(F)Br smiles:O=C(CF)C(F)(F)Br H298:-173.42 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)Br smiles:O=C(CF)C(F)Br H298:-124.56 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)(Br)Br smiles:O=C(CF)C(Br)(Br)Br H298:-61.84 kcal/mol
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
        Cpdata = ([0.80036,0.530663,0.351326,0.175297,-0.0129071,-0.128309,0.0206846],'cal/(mol*K)','+|-',[0.139748,0.161561,0.165559,0.163336,0.142002,0.12263,0.0976585]),
        H298 = (2.61081,'kcal/mol','+|-',0.50748),
        S298 = (-0.00883739,'cal/(mol*K)','+|-',0.329562),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC(O)CCl smiles:O=C(O)CCl H298:-103.07 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)CCl smiles:O=CC(Cl)CCl H298:-54.06 kcal/mol
library:CHOCl_G4 label:ODC(CCl)C(Cl)Cl smiles:O=C(CCl)C(Cl)Cl H298:-58.85 kcal/mol
library:CHOCl_G4 label:CC(Cl)C(DO)Cl smiles:CC(Cl)C(=O)Cl H298:-66.22 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)C(Cl)Cl smiles:O=C(Cl)C(Cl)C(Cl)Cl H298:-73.21 kcal/mol
library:CHOCl_G4 label:ODC(CCl)CCl smiles:O=C(CCl)CCl H298:-56.32 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)CCl smiles:O=C(Cl)C(Cl)CCl H298:-70.40 kcal/mol
library:CHOCl_G4 label:CC(Cl)CDO smiles:CC(Cl)C=O H298:-50.92 kcal/mol
library:CHOCl_G4 label:ODC(CCl)C(Cl)(Cl)Cl smiles:O=C(CCl)C(Cl)(Cl)Cl H298:-59.61 kcal/mol
library:CHOCl_G4 label:CC(DO)CCl smiles:CC(=O)CCl H298:-54.54 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-72.30 kcal/mol
library:CHOCl_G4 label:ODCC(O)Cl smiles:O=CC(O)Cl H298:-84.12 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)OCl smiles:O=C(Cl)C(Cl)OCl H298:-58.03 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)C(Cl)Cl smiles:O=CC(Cl)C(Cl)Cl H298:-57.25 kcal/mol
library:CHOCl_G4 label:ODC(CCl)OCl smiles:O=C(CCl)OCl H298:-63.48 kcal/mol
library:CHOCl_G4 label:ODC(Cl)CCl smiles:O=C(Cl)CCl H298:-57.79 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)C(Cl)(Cl)Cl smiles:O=CC(Cl)C(Cl)(Cl)Cl H298:-59.13 kcal/mol
library:CHOCl_G4 label:ODCCCl smiles:O=CCCl H298:-42.18 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(O)Cl smiles:O=C(Cl)C(O)Cl H298:-98.34 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)OCl smiles:O=CC(Cl)OCl H298:-44.49 kcal/mol
library:CHOFCl_G4 label:ODC(CCl)C(F)F smiles:O=C(CCl)C(F)F H298:-143.31 kcal/mol
library:CHOFCl_G4 label:ODC(CCl)C(F)Cl smiles:O=C(CCl)C(F)Cl H298:-99.47 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)C(F)Cl smiles:O=CC(Cl)C(F)Cl H298:-98.16 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)CF smiles:O=CC(Cl)CF H298:-91.94 kcal/mol
library:CHOFCl_G4 label:ODC(F)C(O)Cl smiles:O=C(F)C(O)Cl H298:-144.19 kcal/mol
library:CHOFCl_G4 label:ODC(CF)CCl smiles:O=C(CF)CCl H298:-93.96 kcal/mol
library:CHOFCl_G4 label:ODCC(Cl)C(F)F smiles:O=CC(Cl)C(F)F H298:-143.65 kcal/mol
library:CHOFCl_G4 label:ODC(F)C(Cl)OCl smiles:O=C(F)C(Cl)OCl H298:-103.93 kcal/mol
library:CHOFCl_G4 label:ODC(Cl)C(Cl)CF smiles:O=C(Cl)C(Cl)CF H298:-107.52 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)CF smiles:O=C(Br)C(Cl)CF H298:-95.04 kcal/mol
library:CHOFClBr_G4 label:ODC(F)C(Cl)OBr smiles:O=C(F)C(Cl)OBr H298:-101.00 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)OBr smiles:O=CC(Cl)OBr H298:-42.02 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)OBr smiles:O=C(CCl)OBr H298:-61.80 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(Cl)OBr smiles:O=C(Cl)C(Cl)OBr H298:-55.19 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)CCl smiles:O=C(Br)C(Cl)CCl H298:-58.00 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Br)Br smiles:O=C(CCl)C(Br)Br H298:-36.55 kcal/mol
library:CHOClBr_G4 label:ODC(Br)CCl smiles:O=C(Br)CCl H298:-45.50 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)CBr smiles:O=C(CCl)CBr H298:-45.77 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(DO)Br smiles:CC(Cl)C(=O)Br H298:-53.73 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Cl)Br smiles:O=C(CCl)C(Cl)Br H298:-47.74 kcal/mol
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
        Cpdata = ([0.518208,0.310468,0.174105,0.029316,-0.0574616,-0.096667,0.0649392],'cal/(mol*K)','+|-',[0.13503,0.156107,0.15997,0.157822,0.137208,0.11849,0.0943617]),
        H298 = (2.31946,'kcal/mol','+|-',0.490348),
        S298 = (-0.0407374,'cal/(mol*K)','+|-',0.318437),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CC(Br)CDO smiles:CC(Br)C=O H298:-40.10 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)CBr smiles:O=C(Br)C(Br)CBr H298:-36.94 kcal/mol
library:CHOBr_G4 label:ODC(CBr)C(Br)Br smiles:O=C(CBr)C(Br)Br H298:-25.79 kcal/mol
library:CHOBr_G4 label:ODC(CBr)OBr smiles:O=C(CBr)OBr H298:-51.23 kcal/mol
library:CHOBr_G4 label:ODCCBr smiles:O=CCBr H298:-31.32 kcal/mol
library:CHOBr_G4 label:CC(Br)C(DO)Br smiles:CC(Br)C(=O)Br H298:-43.01 kcal/mol
library:CHOBr_G4 label:ODC(Br)CBr smiles:O=C(Br)CBr H298:-34.39 kcal/mol
library:CHOBr_G4 label:ODCC(O)Br smiles:O=CC(O)Br H298:-72.90 kcal/mol
library:CHOBr_G4 label:CC(DO)CBr smiles:CC(=O)CBr H298:-43.70 kcal/mol
library:CHOBr_G4 label:ODCC(Br)OBr smiles:O=CC(Br)OBr H298:-30.51 kcal/mol
library:CHOBr_G4 label:ODCC(Br)CBr smiles:O=CC(Br)CBr H298:-33.11 kcal/mol
library:CHOBr_G4 label:ODCC(Br)C(Br)Br smiles:O=CC(Br)C(Br)Br H298:-23.73 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(O)Br smiles:O=C(Br)C(O)Br H298:-74.43 kcal/mol
library:CHOBr_G4 label:ODC(CBr)CBr smiles:O=C(CBr)CBr H298:-35.30 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)OBr smiles:O=C(Br)C(Br)OBr H298:-31.47 kcal/mol
library:CHOBr_G4 label:ODC(O)CBr smiles:O=C(O)CBr H298:-92.21 kcal/mol
library:CHOFClBr_G4 label:ODC(CBr)C(F)Cl smiles:O=C(CBr)C(F)Cl H298:-88.71 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)C(F)Cl smiles:O=CC(Br)C(F)Cl H298:-87.91 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)F smiles:O=C(CBr)C(F)(F)F H298:-188.20 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)Br smiles:O=CC(Br)C(F)Br H298:-75.47 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)Br smiles:O=C(Br)C(Br)C(F)Br H298:-77.95 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)F smiles:O=CC(Br)C(F)F H298:-132.48 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(Br)OBr smiles:O=C(F)C(Br)OBr H298:-90.03 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)CF smiles:O=CC(Br)CF H298:-81.14 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)CF smiles:O=C(Br)C(Br)CF H298:-84.62 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)F smiles:O=C(Br)C(Br)C(F)F H298:-135.56 kcal/mol
library:CHOFBr_G4 label:ODC(CF)CBr smiles:O=C(CF)CBr H298:-83.42 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)Br smiles:O=C(CBr)C(F)Br H298:-76.70 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(O)Br smiles:O=C(F)C(O)Br H298:-132.67 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)F smiles:O=C(CBr)C(F)F H298:-132.07 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(Br)Br smiles:O=C(CBr)C(F)(Br)Br H298:-67.58 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)Br smiles:O=C(CBr)C(F)(F)Br H298:-125.44 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)Br smiles:O=CC(Br)C(F)(F)Br H298:-126.04 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(Br)Br smiles:O=CC(Br)C(F)(Br)Br H298:-66.98 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)F smiles:O=CC(Br)C(F)(F)F H298:-189.47 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(O)Br smiles:O=C(Cl)C(O)Br H298:-86.95 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Cl smiles:O=CC(Br)C(Cl)Cl H298:-46.58 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(Br)OBr smiles:O=C(Cl)C(Br)OBr H298:-44.64 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Br smiles:O=C(CBr)C(Cl)Br H298:-37.03 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)CCl smiles:O=CC(Br)CCl H298:-43.90 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Cl smiles:O=C(CBr)C(Cl)Cl H298:-48.27 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)CBr smiles:O=C(CCl)CBr H298:-45.77 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Br smiles:O=CC(Br)C(Cl)Br H298:-34.82 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)CCl smiles:O=C(Br)C(Br)CCl H298:-47.67 kcal/mol
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
        Cpdata = ([0.0819846,0.104813,0.0988267,0.219879,0.431932,0.438558,0.609446],'cal/(mol*K)','+|-',[0.12737,0.147251,0.150895,0.148868,0.129424,0.111769,0.0890086]),
        H298 = (0.2707,'kcal/mol','+|-',0.462531),
        S298 = (-1.92926,'cal/(mol*K)','+|-',0.300372),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CC(O)C(F)(F)Cl smiles:CC(O)C(F)(F)Cl H298:-170.56 kcal/mol
library:CHOFCl_G4 label:COCC(F)(Cl)Cl smiles:COCC(F)(Cl)Cl H298:-108.08 kcal/mol
library:CHOFCl_G4 label:OCC(F)(F)Cl smiles:OCC(F)(F)Cl H298:-161.10 kcal/mol
library:CHOFCl_G4 label:CC(O)C(F)(Cl)Cl smiles:CC(O)C(F)(Cl)Cl H298:-123.78 kcal/mol
library:CHOFCl_G4 label:COCC(F)(F)Cl smiles:COCC(F)(F)Cl H298:-155.59 kcal/mol
library:CHOFCl_G4 label:FC(F)(Cl)COCl smiles:FC(F)(Cl)COCl H298:-124.09 kcal/mol
library:CHOFCl_G4 label:OC(O)C(F)(Cl)Cl smiles:OC(O)C(F)(Cl)Cl H298:-158.92 kcal/mol
library:CHOFCl_G4 label:OCC(F)(Cl)Cl smiles:OCC(F)(Cl)Cl H298:-114.02 kcal/mol
library:CHOFCl_G4 label:OC(O)C(F)(F)Cl smiles:OC(O)C(F)(F)Cl H298:-205.96 kcal/mol
library:CHOFCl_G4 label:FC(Cl)(Cl)COCl smiles:FC(Cl)(Cl)COCl H298:-76.73 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)COBr smiles:FC(Cl)(Cl)COBr H298:-73.68 kcal/mol
library:CHOFClBr_G4 label:OCC(F)(Cl)Br smiles:OCC(F)(Cl)Br H298:-101.31 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Br)COBr smiles:FC(Cl)(Br)COBr H298:-61.07 kcal/mol
library:CHOFClBr_G4 label:OC(O)C(F)(Cl)Br smiles:OC(O)C(F)(Cl)Br H298:-146.36 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)COBr smiles:FC(F)(Cl)COBr H298:-121.19 kcal/mol
library:CHOFClBr_G4 label:CC(O)C(F)(Cl)Br smiles:CC(O)C(F)(Cl)Br H298:-110.44 kcal/mol
library:CHOFClBr_G4 label:COCC(F)(Cl)Br smiles:COCC(F)(Cl)Br H298:-95.42 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)COBr smiles:FC(F)(Br)COBr H298:-107.55 kcal/mol
library:CHOFBr_G4 label:OC(CBr)C(F)(F)Br smiles:OC(CBr)C(F)(F)Br H298:-149.55 kcal/mol
library:CHOFBr_G4 label:OC(O)C(F)(Br)Br smiles:OC(O)C(F)(Br)Br H298:-133.75 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)COOBr smiles:FC(Br)(Br)COOBr H298:-32.80 kcal/mol
library:CHOFBr_G4 label:OC(CBr)C(F)(Br)Br smiles:OC(CBr)C(F)(Br)Br H298:-90.64 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)COCBr smiles:FC(F)(Br)COCBr H298:-139.26 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)Br smiles:OCC(F)(Br)Br H298:-88.68 kcal/mol
library:CHOFBr_G4 label:OC(O)C(F)(F)Br smiles:OC(O)C(F)(F)Br H298:-192.75 kcal/mol
library:CHOFBr_G4 label:OC(CF)C(F)(F)Br smiles:OC(CF)C(F)(F)Br H298:-197.73 kcal/mol
library:CHOFBr_G4 label:OOCC(F)(Br)Br smiles:OOCC(F)(Br)Br H298:-68.38 kcal/mol
library:CHOFBr_G4 label:CC(OBr)C(F)(F)Br smiles:CC(OBr)C(F)(F)Br H298:-117.74 kcal/mol
library:CHOFBr_G4 label:COCC(F)(F)Br smiles:COCC(F)(F)Br H298:-142.15 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)COBr smiles:FC(Br)(Br)COBr H298:-48.54 kcal/mol
library:CHOFBr_G4 label:OCC(F)(F)Br smiles:OCC(F)(F)Br H298:-147.64 kcal/mol
library:CHOFBr_G4 label:CC(OBr)C(F)(Br)Br smiles:CC(OBr)C(F)(Br)Br H298:-58.57 kcal/mol
library:CHOFBr_G4 label:OC(OBr)C(F)(F)Br smiles:OC(OBr)C(F)(F)Br H298:-153.50 kcal/mol
library:CHOFBr_G4 label:OC(CF)C(F)(Br)Br smiles:OC(CF)C(F)(Br)Br H298:-138.28 kcal/mol
library:CHOFBr_G4 label:CC(O)C(F)(F)Br smiles:CC(O)C(F)(F)Br H298:-157.26 kcal/mol
library:CHOFBr_G4 label:OOCC(F)(F)Br smiles:OOCC(F)(F)Br H298:-127.39 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)COOBr smiles:FC(F)(Br)COOBr H298:-91.59 kcal/mol
library:CHOFBr_G4 label:CC(O)C(F)(Br)Br smiles:CC(O)C(F)(Br)Br H298:-98.36 kcal/mol
library:CHOFBr_G4 label:OC(OBr)C(F)(Br)Br smiles:OC(OBr)C(F)(Br)Br H298:-94.40 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)COCBr smiles:FC(Br)(Br)COCBr H298:-79.94 kcal/mol
library:CHOFBr_G4 label:COCC(F)(Br)Br smiles:COCC(F)(Br)Br H298:-82.87 kcal/mol
library:CHOClBr_G4 label:CC(O)C(Cl)(Br)Br smiles:CC(O)C(Cl)(Br)Br H298:-56.18 kcal/mol
library:CHOClBr_G4 label:CC(O)C(Cl)(Cl)Br smiles:CC(O)C(Cl)(Cl)Br H298:-68.05 kcal/mol
library:CHOClBr_G4 label:ClC(Br)(Br)COBr smiles:ClC(Br)(Br)COBr H298:-6.80 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Cl)Br smiles:OCC(Cl)(Cl)Br H298:-58.72 kcal/mol
library:CHOClBr_G4 label:COCC(Cl)(Cl)Br smiles:COCC(Cl)(Cl)Br H298:-52.80 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Br)COBr smiles:ClC(Cl)(Br)COBr H298:-18.53 kcal/mol
library:CHOClBr_G4 label:OC(O)C(Cl)(Cl)Br smiles:OC(O)C(Cl)(Cl)Br H298:-102.99 kcal/mol
library:CHOClBr_G4 label:COCC(Cl)(Br)Br smiles:COCC(Cl)(Br)Br H298:-41.00 kcal/mol
library:CHOClBr_G4 label:OC(O)C(Cl)(Br)Br smiles:OC(O)C(Cl)(Br)Br H298:-91.38 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Br)Br smiles:OCC(Cl)(Br)Br H298:-46.92 kcal/mol
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
        Cpdata = ([0.281209,0.439821,0.362902,0.387533,0.455686,0.378386,0.225756],'cal/(mol*K)','+|-',[0.168651,0.194976,0.1998,0.197117,0.171371,0.147993,0.117857]),
        H298 = (2.92021,'kcal/mol','+|-',0.612439),
        S298 = (-1.31293,'cal/(mol*K)','+|-',0.397724),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCOCC(F)(F)F smiles:FCOCC(F)(F)F H298:-257.96 kcal/mol
library:CHOF_G4 label:OC(CF)C(F)(F)F smiles:OC(CF)C(F)(F)F H298:-262.70 kcal/mol
library:CHOF_G4 label:OC(C(F)F)C(F)(F)F smiles:OC(C(F)F)C(F)(F)F H298:-312.90 kcal/mol
library:CHOF_G4 label:FOC(OF)C(F)(F)F smiles:FOC(OF)C(F)(F)F H298:-186.82 kcal/mol
library:CHOF_G4 label:COCC(F)(F)F smiles:COCC(F)(F)F H298:-206.19 kcal/mol
library:CHOF_G4 label:OC(O)C(F)(F)F smiles:OC(O)C(F)(F)F H298:-256.11 kcal/mol
library:CHOF_G4 label:CC(OF)C(F)(F)F smiles:CC(OF)C(F)(F)F H298:-190.03 kcal/mol
library:CHOF_G4 label:OC(OF)C(F)(F)F smiles:OC(OF)C(F)(F)F H298:-222.79 kcal/mol
library:CHOF_G4 label:FOOCC(F)(F)F smiles:FOOCC(F)(F)F H298:-169.03 kcal/mol
library:CHOF_G4 label:FOC(C(F)(F)F)C(F)(F)F smiles:FOC(C(F)(F)F)C(F)(F)F H298:-333.30 kcal/mol
library:CHOF_G4 label:FOC(C(F)F)C(F)(F)F smiles:FOC(C(F)F)C(F)(F)F H298:-279.35 kcal/mol
library:CHOF_G4 label:OC(C(F)(F)F)C(F)(F)F smiles:OC(C(F)(F)F)C(F)(F)F H298:-369.50 kcal/mol
library:CHOF_G4 label:FOCC(F)(F)F smiles:FOCC(F)(F)F H298:-180.13 kcal/mol
library:CHOF_G4 label:CC(O)C(F)(F)F smiles:CC(O)C(F)(F)F H298:-221.06 kcal/mol
library:CHOF_G4 label:FCC(OF)C(F)(F)F smiles:FCC(OF)C(F)(F)F H298:-229.04 kcal/mol
library:CHOF_G4 label:FC(F)(F)COC(F)(F)F smiles:FC(F)(F)COC(F)(F)F H298:-372.01 kcal/mol
library:CHOF_G4 label:OCC(F)(F)F smiles:OCC(F)(F)F H298:-211.77 kcal/mol
library:CHOF_G4 label:FC(F)OCC(F)(F)F smiles:FC(F)OCC(F)(F)F H298:-315.99 kcal/mol
library:CHOF_G4 label:OOCC(F)(F)F smiles:OOCC(F)(F)F H298:-191.60 kcal/mol
library:CHOFCl_G4 label:FC(F)(F)COCl smiles:FC(F)(F)COCl H298:-174.74 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)COBr smiles:FC(F)(F)COBr H298:-171.55 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)COCBr smiles:FC(F)(F)COCBr H298:-203.34 kcal/mol
library:CHOFBr_G4 label:CC(OBr)C(F)(F)F smiles:CC(OBr)C(F)(F)F H298:-181.76 kcal/mol
library:CHOFBr_G4 label:OC(OBr)C(F)(F)F smiles:OC(OBr)C(F)(F)F H298:-216.38 kcal/mol
library:CHOFBr_G4 label:OC(CBr)C(F)(F)F smiles:OC(CBr)C(F)(F)F H298:-213.90 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)COOBr smiles:FC(F)(F)COOBr H298:-155.71 kcal/mol
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
        Cpdata = ([-0.20555,-0.0614396,0.0233846,0.113959,0.253601,0.282253,0.38882],'cal/(mol*K)','+|-',[0.187494,0.21676,0.222123,0.219141,0.190518,0.164528,0.131024]),
        H298 = (1.13932,'kcal/mol','+|-',0.680865),
        S298 = (-1.03239,'cal/(mol*K)','+|-',0.44216),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClOC(OCl)C(Cl)(Cl)Cl smiles:ClOC(OCl)C(Cl)(Cl)Cl H298:-39.06 kcal/mol
library:CHOCl_G4 label:ClOOCC(Cl)(Cl)Cl smiles:ClOOCC(Cl)(Cl)Cl H298:-17.71 kcal/mol
library:CHOCl_G4 label:ClC(Cl)OCC(Cl)(Cl)Cl smiles:ClC(Cl)OCC(Cl)(Cl)Cl H298:-79.93 kcal/mol
library:CHOCl_G4 label:OC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-81.22 kcal/mol
library:CHOCl_G4 label:OC(O)C(Cl)(Cl)Cl smiles:OC(O)C(Cl)(Cl)Cl H298:-114.85 kcal/mol
library:CHOCl_G4 label:COCC(Cl)(Cl)Cl smiles:COCC(Cl)(Cl)Cl H298:-64.75 kcal/mol
library:CHOCl_G4 label:ClOC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-42.50 kcal/mol
library:CHOCl_G4 label:OCC(Cl)(Cl)Cl smiles:OCC(Cl)(Cl)Cl H298:-70.71 kcal/mol
library:CHOCl_G4 label:CC(OCl)C(Cl)(Cl)Cl smiles:CC(OCl)C(Cl)(Cl)Cl H298:-42.74 kcal/mol
library:CHOCl_G4 label:OC(CCl)C(Cl)(Cl)Cl smiles:OC(CCl)C(Cl)(Cl)Cl H298:-83.15 kcal/mol
library:CHOCl_G4 label:OC(OCl)C(Cl)(Cl)Cl smiles:OC(OCl)C(Cl)(Cl)Cl H298:-78.78 kcal/mol
library:CHOCl_G4 label:OOCC(Cl)(Cl)Cl smiles:OOCC(Cl)(Cl)Cl H298:-49.51 kcal/mol
library:CHOCl_G4 label:CC(O)C(Cl)(Cl)Cl smiles:CC(O)C(Cl)(Cl)Cl H298:-79.96 kcal/mol
library:CHOCl_G4 label:ClCOCC(Cl)(Cl)Cl smiles:ClCOCC(Cl)(Cl)Cl H298:-74.43 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)COC(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)COC(Cl)(Cl)Cl H298:-81.44 kcal/mol
library:CHOCl_G4 label:ClCC(OCl)C(Cl)(Cl)Cl smiles:ClCC(OCl)C(Cl)(Cl)Cl H298:-45.49 kcal/mol
library:CHOCl_G4 label:ClOCC(Cl)(Cl)Cl smiles:ClOCC(Cl)(Cl)Cl H298:-33.40 kcal/mol
library:CHOCl_G4 label:ClOC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(C(Cl)Cl)C(Cl)(Cl)Cl H298:-45.44 kcal/mol
library:CHOCl_G4 label:OC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(C(Cl)Cl)C(Cl)(Cl)Cl H298:-84.88 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Cl)COBr smiles:ClC(Cl)(Cl)COBr H298:-29.74 kcal/mol
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
        Cpdata = ([-0.10091,-0.0881932,-0.0965894,-0.0822155,-0.00236869,0.0187073,0.285702],'cal/(mol*K)','+|-',[0.290148,0.335437,0.343737,0.339121,0.294827,0.254608,0.202761]),
        H298 = (1.4968,'kcal/mol','+|-',1.05364),
        S298 = (-1.03766,'cal/(mol*K)','+|-',0.684245),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCOCC(Br)(Br)Br smiles:BrCOCC(Br)(Br)Br H298:-26.68 kcal/mol
library:CHOBr_G4 label:OCC(Br)(Br)Br smiles:OCC(Br)(Br)Br H298:-35.23 kcal/mol
library:CHOBr_G4 label:OC(O)C(Br)(Br)Br smiles:OC(O)C(Br)(Br)Br H298:-79.43 kcal/mol
library:CHOBr_G4 label:COCC(Br)(Br)Br smiles:COCC(Br)(Br)Br H298:-29.34 kcal/mol
library:CHOBr_G4 label:OOCC(Br)(Br)Br smiles:OOCC(Br)(Br)Br H298:-13.92 kcal/mol
library:CHOBr_G4 label:BrOCC(Br)(Br)Br smiles:BrOCC(Br)(Br)Br H298:4.80 kcal/mol
library:CHOBr_G4 label:CC(O)C(Br)(Br)Br smiles:CC(O)C(Br)(Br)Br H298:-44.35 kcal/mol
library:CHOBr_G4 label:CC(OBr)C(Br)(Br)Br smiles:CC(OBr)C(Br)(Br)Br H298:-4.47 kcal/mol
library:CHOBr_G4 label:BrOOCC(Br)(Br)Br smiles:BrOOCC(Br)(Br)Br H298:21.05 kcal/mol
library:CHOFBr_G4 label:OC(CF)C(Br)(Br)Br smiles:OC(CF)C(Br)(Br)Br H298:-84.76 kcal/mol
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
        Cpdata = ([0.800599,0.0976876,-0.142021,-0.0318439,0.0529025,0.130235,0.393586],'cal/(mol*K)','+|-',[0.253691,0.293289,0.300547,0.296511,0.257782,0.222617,0.177284]),
        H298 = (8.03492,'kcal/mol','+|-',0.921253),
        S298 = (0.70561,'cal/(mol*K)','+|-',0.59827),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(O)C(F)(F)Cl smiles:C=C(O)C(F)(F)Cl H298:-139.22 kcal/mol
library:CHOFCl_G4 label:CDC(O)C(F)(Cl)Cl smiles:C=C(O)C(F)(Cl)Cl H298:-92.18 kcal/mol
library:CHOFClBr_G4 label:CDC(O)C(F)(Cl)Br smiles:C=C(O)C(F)(Cl)Br H298:-79.77 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)C(F)(F)Br smiles:C=C(OBr)C(F)(F)Br H298:-85.56 kcal/mol
library:CHOFBr_G4 label:CDC(O)C(F)(Br)Br smiles:C=C(O)C(F)(Br)Br H298:-67.53 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(Br)Br smiles:OC(=CF)C(F)(Br)Br H298:-109.26 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(F)Br smiles:OC(=CF)C(F)(F)Br H298:-167.86 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)C(F)(Br)Br smiles:C=C(OBr)C(F)(Br)Br H298:-27.34 kcal/mol
library:CHOFBr_G4 label:CDC(O)C(F)(F)Br smiles:C=C(O)C(F)(F)Br H298:-126.04 kcal/mol
library:CHOClBr_G4 label:CDC(O)C(Cl)(Cl)Br smiles:C=C(O)C(Cl)(Cl)Br H298:-36.08 kcal/mol
library:CHOClBr_G4 label:CDC(O)C(Cl)(Br)Br smiles:C=C(O)C(Cl)(Br)Br H298:-24.27 kcal/mol
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
        Cpdata = ([0.642153,0.414522,0.305835,0.333834,0.233524,0.181,0.204602],'cal/(mol*K)','+|-',[0.33632,0.388816,0.398437,0.393087,0.341744,0.295124,0.235027]),
        H298 = (5.45671,'kcal/mol','+|-',1.22131),
        S298 = (-0.289797,'cal/(mol*K)','+|-',0.793131),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:CDC(OF)C(F)(F)F smiles:C=C(OF)C(F)(F)F H298:-154.46 kcal/mol
library:CHOF_G4 label:CDC(O)C(F)(F)F smiles:C=C(O)C(F)(F)F H298:-189.49 kcal/mol
library:CHOF_G4 label:FOC(DC(F)F)C(F)(F)F smiles:FOC(=C(F)F)C(F)(F)F H298:-242.07 kcal/mol
library:CHOF_G4 label:FCDC(OF)C(F)(F)F smiles:FC=C(OF)C(F)(F)F H298:-195.53 kcal/mol
library:CHOF_G4 label:OC(DCF)C(F)(F)F smiles:OC(=CF)C(F)(F)F H298:-231.90 kcal/mol
library:CHOF_G4 label:OC(DC(F)F)C(F)(F)F smiles:OC(=C(F)F)C(F)(F)F H298:-272.98 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)C(F)(F)F smiles:C=C(OBr)C(F)(F)F H298:-149.16 kcal/mol
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
        Cpdata = ([0.433389,0.374841,0.425523,0.474954,0.352438,0.266971,0.308632],'cal/(mol*K)','+|-',[0.365755,0.422844,0.433308,0.427489,0.371653,0.320953,0.255596]),
        H298 = (2.90063,'kcal/mol','+|-',1.3282),
        S298 = (-1.32502,'cal/(mol*K)','+|-',0.862545),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:OC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-51.59 kcal/mol
library:CHOCl_G4 label:OC(DCCl)C(Cl)(Cl)Cl smiles:OC(=CCl)C(Cl)(Cl)Cl H298:-54.42 kcal/mol
library:CHOCl_G4 label:ClOC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-12.00 kcal/mol
library:CHOCl_G4 label:ClCDC(OCl)C(Cl)(Cl)Cl smiles:ClC=C(OCl)C(Cl)(Cl)Cl H298:-12.27 kcal/mol
library:CHOCl_G4 label:CDC(OCl)C(Cl)(Cl)Cl smiles:C=C(OCl)C(Cl)(Cl)Cl H298:-9.52 kcal/mol
library:CHOCl_G4 label:CDC(O)C(Cl)(Cl)Cl smiles:C=C(O)C(Cl)(Cl)Cl H298:-47.77 kcal/mol
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
        Cpdata = ([0.0907689,-0.566345,-0.644937,-0.539878,-0.397884,-0.173453,0.27329],'cal/(mol*K)','+|-',[0.607143,0.70191,0.71928,0.709621,0.616934,0.532774,0.424283]),
        H298 = (7.09859,'kcal/mol','+|-',2.20478),
        S298 = (0.625874,'cal/(mol*K)','+|-',1.4318),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(O)C(Br)(Br)Br smiles:C=C(O)C(Br)(Br)Br H298:-12.42 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(Br)(Br)Br smiles:OC(=CF)C(Br)(Br)Br H298:-54.40 kcal/mol
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
        Cpdata = ([-0.208322,-0.997262,-1.21406,-1.04156,-0.69522,-0.387709,-0.21912],'cal/(mol*K)','+|-',[0.143003,0.165324,0.169415,0.16714,0.14531,0.125487,0.0999334]),
        H298 = (5.35454,'kcal/mol','+|-',0.519301),
        S298 = (1.66446,'cal/(mol*K)','+|-',0.337239),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:FC(Cl)DCOCCl smiles:FC(Cl)=COCCl H298:-77.72 kcal/mol
library:CHOFCl_G4 label:OC(CCl)DC(F)Cl smiles:OC(CCl)=C(F)Cl H298:-90.12 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DCOCl smiles:FC(Cl)=COCl H298:-37.46 kcal/mol
library:CHOFCl_G4 label:CC(OCl)DC(F)Cl smiles:CC(OCl)=C(F)Cl H298:-48.84 kcal/mol
library:CHOFCl_G4 label:OOCDC(F)Cl smiles:OOC=C(F)Cl H298:-53.48 kcal/mol
library:CHOFCl_G4 label:OC(OCl)DC(F)Cl smiles:OC(OCl)=C(F)Cl H298:-79.43 kcal/mol
library:CHOFCl_G4 label:CC(O)DC(F)Cl smiles:CC(O)=C(F)Cl H298:-87.69 kcal/mol
library:CHOFCl_G4 label:COCDC(F)Cl smiles:COC=C(F)Cl H298:-68.92 kcal/mol
library:CHOFCl_G4 label:OCDC(F)Cl smiles:OC=C(F)Cl H298:-76.50 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DCOOCl smiles:FC(Cl)=COOCl H298:-22.25 kcal/mol
library:CHOFCl_G4 label:OC(O)DC(F)Cl smiles:OC(O)=C(F)Cl H298:-118.39 kcal/mol
library:CHOFClBr_G4 label:OC(OBr)DC(F)Cl smiles:OC(OBr)=C(F)Cl H298:-77.94 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCOOBr smiles:FC(Cl)=COOBr H298:-19.11 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCOBr smiles:FC(Cl)=COBr H298:-34.90 kcal/mol
library:CHOFClBr_G4 label:OC(CBr)DC(F)Cl smiles:OC(CBr)=C(F)Cl H298:-79.60 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCOCBr smiles:FC(Cl)=COCBr H298:-65.81 kcal/mol
library:CHOFClBr_G4 label:CC(OBr)DC(F)Cl smiles:CC(OBr)=C(F)Cl H298:-46.47 kcal/mol
library:CHOFBr_G4 label:CC(OBr)DC(F)Br smiles:CC(OBr)=C(F)Br H298:-34.10 kcal/mol
library:CHOFBr_G4 label:OC(O)DC(F)Br smiles:OC(O)=C(F)Br H298:-106.37 kcal/mol
library:CHOFBr_G4 label:OCDC(F)Br smiles:OC=C(F)Br H298:-64.13 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOC(Br)Br smiles:FC(Br)=COC(Br)Br H298:-46.67 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOBr smiles:FC(Br)=COBr H298:-22.36 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(OBr)OBr smiles:FC(Br)=C(OBr)OBr H298:-26.38 kcal/mol
library:CHOFBr_G4 label:COCDC(F)Br smiles:COC=C(F)Br H298:-56.49 kcal/mol
library:CHOFBr_G4 label:OC(CBr)DC(F)Br smiles:OC(CBr)=C(F)Br H298:-67.27 kcal/mol
library:CHOFBr_G4 label:CC(O)DC(F)Br smiles:CC(O)=C(F)Br H298:-75.43 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOCBr smiles:FC(Br)=COCBr H298:-53.31 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(CBr)OBr smiles:FC(Br)=C(CBr)OBr H298:-26.38 kcal/mol
library:CHOFBr_G4 label:OOCDC(F)Br smiles:OOC=C(F)Br H298:-40.90 kcal/mol
library:CHOFBr_G4 label:OC(DC(F)Br)C(Br)Br smiles:OC(=C(F)Br)C(Br)Br H298:-58.23 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOOBr smiles:FC(Br)=COOBr H298:-6.48 kcal/mol
library:CHOFBr_G4 label:OC(OBr)DC(F)Br smiles:OC(OBr)=C(F)Br H298:-65.75 kcal/mol
library:CHOClBr_G4 label:CC(O)DC(Cl)Br smiles:CC(O)=C(Cl)Br H298:-39.46 kcal/mol
library:CHOClBr_G4 label:OC(CBr)DC(Cl)Br smiles:OC(CBr)=C(Cl)Br H298:-31.49 kcal/mol
library:CHOClBr_G4 label:OCDC(Cl)Br smiles:OC=C(Cl)Br H298:-28.23 kcal/mol
library:CHOClBr_G4 label:OOCDC(Cl)Br smiles:OOC=C(Cl)Br H298:-3.68 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DCOBr smiles:ClC(Br)=COBr H298:14.85 kcal/mol
library:CHOClBr_G4 label:OC(OBr)DC(Cl)Br smiles:OC(OBr)=C(Cl)Br H298:-30.53 kcal/mol
library:CHOClBr_G4 label:COCDC(Cl)Br smiles:COC=C(Cl)Br H298:-20.73 kcal/mol
library:CHOClBr_G4 label:CC(OBr)DC(Cl)Br smiles:CC(OBr)=C(Cl)Br H298:3.47 kcal/mol
library:CHOClBr_G4 label:OC(O)DC(Cl)Br smiles:OC(O)=C(Cl)Br H298:-72.78 kcal/mol
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
        Cpdata = ([-0.239653,-0.924881,-1.02515,-0.853974,-0.497889,-0.174807,-0.00768559],'cal/(mol*K)','+|-',[0.155936,0.180275,0.184736,0.182256,0.158451,0.136835,0.108971]),
        H298 = (8.45595,'kcal/mol','+|-',0.566264),
        S298 = (1.91362,'cal/(mol*K)','+|-',0.367737),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:OC(O)DC(F)F smiles:OC(O)=C(F)F H298:-156.20 kcal/mol
library:CHOF_G4 label:FCOCDC(F)F smiles:FCOC=C(F)F H298:-161.47 kcal/mol
library:CHOF_G4 label:FC(F)DCOC(F)F smiles:FC(F)=COC(F)F H298:-218.90 kcal/mol
library:CHOF_G4 label:FOOCDC(F)F smiles:FOOC=C(F)F H298:-72.28 kcal/mol
library:CHOF_G4 label:FC(F)DCOC(F)(F)F smiles:FC(F)=COC(F)(F)F H298:-275.14 kcal/mol
library:CHOF_G4 label:OC(DC(F)F)C(F)F smiles:OC(=C(F)F)C(F)F H298:-218.20 kcal/mol
library:CHOF_G4 label:OCDC(F)F smiles:OC=C(F)F H298:-116.29 kcal/mol
library:CHOF_G4 label:CC(OF)DC(F)F smiles:CC(OF)=C(F)F H298:-97.63 kcal/mol
library:CHOF_G4 label:FCC(OF)DC(F)F smiles:FCC(OF)=C(F)F H298:-137.07 kcal/mol
library:CHOF_G4 label:FOC(DC(F)F)C(F)F smiles:FOC(=C(F)F)C(F)F H298:-186.64 kcal/mol
library:CHOF_G4 label:CC(O)DC(F)F smiles:CC(O)=C(F)F H298:-127.01 kcal/mol
library:CHOF_G4 label:OOCDC(F)F smiles:OOC=C(F)F H298:-95.03 kcal/mol
library:CHOF_G4 label:FOCDC(F)F smiles:FOC=C(F)F H298:-86.76 kcal/mol
library:CHOF_G4 label:FOC(DC(F)F)C(F)(F)F smiles:FOC(=C(F)F)C(F)(F)F H298:-242.07 kcal/mol
library:CHOF_G4 label:COCDC(F)F smiles:COC=C(F)F H298:-110.48 kcal/mol
library:CHOF_G4 label:OC(CF)DC(F)F smiles:OC(CF)=C(F)F H298:-167.24 kcal/mol
library:CHOF_G4 label:FOC(OF)DC(F)F smiles:FOC(OF)=C(F)F H298:-94.80 kcal/mol
library:CHOF_G4 label:OC(DC(F)F)C(F)(F)F smiles:OC(=C(F)F)C(F)(F)F H298:-272.98 kcal/mol
library:CHOFCl_G4 label:CC(OCl)DC(F)F smiles:CC(OCl)=C(F)F H298:-89.38 kcal/mol
library:CHOFCl_G4 label:FC(F)DCOCCl smiles:FC(F)=COCCl H298:-118.57 kcal/mol
library:CHOFCl_G4 label:FC(F)DCOCl smiles:FC(F)=COCl H298:-78.55 kcal/mol
library:CHOFCl_G4 label:OC(OCl)DC(F)F smiles:OC(OCl)=C(F)F H298:-118.73 kcal/mol
library:CHOFCl_G4 label:FC(F)DCOOCl smiles:FC(F)=COOCl H298:-64.42 kcal/mol
library:CHOFCl_G4 label:OC(CCl)DC(F)F smiles:OC(CCl)=C(F)F H298:-130.01 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(CBr)OBr smiles:FC(F)=C(CBr)OBr H298:-79.12 kcal/mol
library:CHOFBr_G4 label:OC(OBr)DC(F)F smiles:OC(OBr)=C(F)F H298:-117.57 kcal/mol
library:CHOFBr_G4 label:OC(DC(F)F)C(F)Br smiles:OC(=C(F)F)C(F)Br H298:-161.64 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOC(Br)Br smiles:FC(F)=COC(Br)Br H298:-100.07 kcal/mol
library:CHOFBr_G4 label:OC(CBr)DC(F)F smiles:OC(CBr)=C(F)F H298:-119.27 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOOBr smiles:FC(F)=COOBr H298:-60.95 kcal/mol
library:CHOFBr_G4 label:FOC(OBr)DC(F)F smiles:FOC(OBr)=C(F)F H298:-87.16 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(OBr)OBr smiles:FC(F)=C(OBr)OBr H298:-78.60 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOBr smiles:FC(F)=COBr H298:-75.77 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOC(F)Br smiles:FC(F)=COC(F)Br H298:-156.78 kcal/mol
library:CHOFBr_G4 label:CC(OBr)DC(F)F smiles:CC(OBr)=C(F)F H298:-86.81 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOCBr smiles:FC(F)=COCBr H298:-106.66 kcal/mol
library:CHOFBr_G4 label:OC(DC(F)F)C(Br)Br smiles:OC(=C(F)F)C(Br)Br H298:-110.67 kcal/mol
library:CHOFBr_G4 label:FCC(OBr)DC(F)F smiles:FCC(OBr)=C(F)F H298:-127.28 kcal/mol
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
        Cpdata = ([-0.154351,-0.821837,-1.01556,-0.891994,-0.627092,-0.341158,-0.228226],'cal/(mol*K)','+|-',[0.193088,0.223226,0.22875,0.225678,0.196201,0.169436,0.134933]),
        H298 = (5.30026,'kcal/mol','+|-',0.701177),
        S298 = (1.71359,'cal/(mol*K)','+|-',0.455351),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClOOCDC(Cl)Cl smiles:ClOOC=C(Cl)Cl H298:16.29 kcal/mol
library:CHOCl_G4 label:ClCC(OCl)DC(Cl)Cl smiles:ClCC(OCl)=C(Cl)Cl H298:-12.85 kcal/mol
library:CHOCl_G4 label:OC(CCl)DC(Cl)Cl smiles:OC(CCl)=C(Cl)Cl H298:-53.37 kcal/mol
library:CHOCl_G4 label:OC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-51.59 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCOC(Cl)Cl smiles:ClC(Cl)=COC(Cl)Cl H298:-45.66 kcal/mol
library:CHOCl_G4 label:OC(O)DC(Cl)Cl smiles:OC(O)=C(Cl)Cl H298:-84.01 kcal/mol
library:CHOCl_G4 label:COCDC(Cl)Cl smiles:COC=C(Cl)Cl H298:-32.28 kcal/mol
library:CHOCl_G4 label:OC(OCl)DC(Cl)Cl smiles:OC(OCl)=C(Cl)Cl H298:-43.38 kcal/mol
library:CHOCl_G4 label:ClOC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-12.00 kcal/mol
library:CHOCl_G4 label:CC(OCl)DC(Cl)Cl smiles:CC(OCl)=C(Cl)Cl H298:-10.33 kcal/mol
library:CHOCl_G4 label:ClCOCDC(Cl)Cl smiles:ClCOC=C(Cl)Cl H298:-40.12 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCOC(Cl)(Cl)Cl smiles:ClC(Cl)=COC(Cl)(Cl)Cl H298:-46.65 kcal/mol
library:CHOCl_G4 label:OC(DC(Cl)Cl)C(Cl)Cl smiles:OC(=C(Cl)Cl)C(Cl)Cl H298:-55.84 kcal/mol
library:CHOCl_G4 label:OOCDC(Cl)Cl smiles:OOC=C(Cl)Cl H298:-15.34 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)Cl smiles:OC=C(Cl)Cl H298:-39.80 kcal/mol
library:CHOCl_G4 label:ClOCDC(Cl)Cl smiles:ClOC=C(Cl)Cl H298:0.74 kcal/mol
library:CHOCl_G4 label:CC(O)DC(Cl)Cl smiles:CC(O)=C(Cl)Cl H298:-51.01 kcal/mol
library:CHOCl_G4 label:ClOC(OCl)DC(Cl)Cl smiles:ClOC(OCl)=C(Cl)Cl H298:-4.75 kcal/mol
library:CHOCl_G4 label:ClOC(DC(Cl)Cl)C(Cl)Cl smiles:ClOC(=C(Cl)Cl)C(Cl)Cl H298:-14.53 kcal/mol
library:CHOClBr_G4 label:CC(OBr)DC(Cl)Cl smiles:CC(OBr)=C(Cl)Cl H298:-8.08 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCOCBr smiles:ClC(Cl)=COCBr H298:-28.11 kcal/mol
library:CHOClBr_G4 label:OC(OBr)DC(Cl)Cl smiles:OC(OBr)=C(Cl)Cl H298:-41.83 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCOOBr smiles:ClC(Cl)=COOBr H298:19.60 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCOBr smiles:ClC(Cl)=COBr H298:3.23 kcal/mol
library:CHOClBr_G4 label:OC(CBr)DC(Cl)Cl smiles:OC(CBr)=C(Cl)Cl H298:-43.08 kcal/mol
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
        Cpdata = ([-0.272824,-0.794798,-1.00711,-0.784414,-0.509353,-0.246386,-0.152903],'cal/(mol*K)','+|-',[0.252543,0.291962,0.299187,0.295169,0.256616,0.221609,0.176482]),
        H298 = (3.96592,'kcal/mol','+|-',0.917084),
        S298 = (0.962118,'cal/(mol*K)','+|-',0.595563),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrOC(OBr)DC(Br)Br smiles:BrOC(OBr)=C(Br)Br H298:21.09 kcal/mol
library:CHOBr_G4 label:OC(OBr)DC(Br)Br smiles:OC(OBr)=C(Br)Br H298:-19.08 kcal/mol
library:CHOBr_G4 label:OCDC(Br)Br smiles:OC=C(Br)Br H298:-16.77 kcal/mol
library:CHOBr_G4 label:OOCDC(Br)Br smiles:OOC=C(Br)Br H298:7.92 kcal/mol
library:CHOBr_G4 label:OC(CBr)DC(Br)Br smiles:OC(CBr)=C(Br)Br H298:-20.10 kcal/mol
library:CHOBr_G4 label:CC(O)DC(Br)Br smiles:CC(O)=C(Br)Br H298:-27.94 kcal/mol
library:CHOBr_G4 label:BrOOCDC(Br)Br smiles:BrOOC=C(Br)Br H298:42.90 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)Br smiles:BrOC=C(Br)Br H298:26.47 kcal/mol
library:CHOBr_G4 label:BrCOCDC(Br)Br smiles:BrCOC=C(Br)Br H298:-4.91 kcal/mol
library:CHOBr_G4 label:OC(O)DC(Br)Br smiles:OC(O)=C(Br)Br H298:-61.67 kcal/mol
library:CHOBr_G4 label:CC(OBr)DC(Br)Br smiles:CC(OBr)=C(Br)Br H298:15.28 kcal/mol
library:CHOBr_G4 label:COCDC(Br)Br smiles:COC=C(Br)Br H298:-9.24 kcal/mol
library:CHOBr_G4 label:BrC(Br)DCOC(Br)Br smiles:BrC(Br)=COC(Br)Br H298:1.73 kcal/mol
library:CHOBr_G4 label:BrCC(OBr)DC(Br)Br smiles:BrCC(OBr)=C(Br)Br H298:22.63 kcal/mol
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
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""

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
        Cpdata = ([-0.409084,-0.954414,-1.02336,-0.85015,-0.503449,-0.233069,-0.16848],'cal/(mol*K)','+|-',[0.105301,0.121737,0.12475,0.123074,0.106999,0.0924026,0.0735862]),
        H298 = (6.25086,'kcal/mol','+|-',0.382389),
        S298 = (1.43962,'cal/(mol*K)','+|-',0.248327),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCDCOCF smiles:FC=COCF H298:-115.70 kcal/mol
library:CHOF_G4 label:OCDC(F)CF smiles:OC=C(F)CF H298:-124.81 kcal/mol
library:CHOF_G4 label:FCDCOOF smiles:FC=COOF H298:-27.23 kcal/mol
library:CHOF_G4 label:OCDC(F)OF smiles:OC=C(F)OF H298:-91.29 kcal/mol
library:CHOF_G4 label:FCDC(OF)OF smiles:FC=C(OF)OF H298:-48.15 kcal/mol
library:CHOF_G4 label:OOCDCF smiles:OOC=CF H298:-48.06 kcal/mol
library:CHOF_G4 label:CC(O)DCF smiles:CC(O)=CF H298:-83.39 kcal/mol
library:CHOF_G4 label:FCC(F)DCOF smiles:FCC(F)=COF H298:-90.68 kcal/mol
library:CHOF_G4 label:FCDCOF smiles:FC=COF H298:-39.80 kcal/mol
library:CHOF_G4 label:FOCDC(F)C(F)(F)F smiles:FOC=C(F)C(F)(F)F H298:-194.83 kcal/mol
library:CHOF_G4 label:FCDC(OF)C(F)F smiles:FC=C(OF)C(F)F H298:-139.74 kcal/mol
library:CHOF_G4 label:FOCDC(F)C(F)F smiles:FOC=C(F)C(F)F H298:-140.05 kcal/mol
library:CHOF_G4 label:COCDCF smiles:COC=CF H298:-64.72 kcal/mol
library:CHOF_G4 label:OCDCF smiles:OC=CF H298:-72.56 kcal/mol
library:CHOF_G4 label:OCDC(F)C(F)F smiles:OC=C(F)C(F)F H298:-175.43 kcal/mol
library:CHOF_G4 label:OC(DCF)OF smiles:OC(=CF)OF H298:-85.62 kcal/mol
library:CHOF_G4 label:OC(O)DCF smiles:OC(O)=CF H298:-115.10 kcal/mol
library:CHOF_G4 label:OC(DCF)C(F)F smiles:OC(=CF)C(F)F H298:-175.01 kcal/mol
library:CHOF_G4 label:OC(DCF)CF smiles:OC(=CF)CF H298:-123.45 kcal/mol
library:CHOF_G4 label:CC(DCF)OF smiles:CC(=CF)OF H298:-51.58 kcal/mol
library:CHOF_G4 label:OCDC(F)C(F)(F)F smiles:OC=C(F)C(F)(F)F H298:-232.28 kcal/mol
library:CHOF_G4 label:FCDCOC(F)F smiles:FC=COC(F)F H298:-173.05 kcal/mol
library:CHOF_G4 label:FCDCOC(F)(F)F smiles:FC=COC(F)(F)F H298:-229.24 kcal/mol
library:CHOF_G4 label:CC(F)DCOF smiles:CC(F)=COF H298:-55.05 kcal/mol
library:CHOF_G4 label:FCDC(OF)C(F)(F)F smiles:FC=C(OF)C(F)(F)F H298:-195.53 kcal/mol
library:CHOF_G4 label:FOCDC(F)OF smiles:FOC=C(F)OF H298:-49.63 kcal/mol
library:CHOF_G4 label:OC(DCF)C(F)(F)F smiles:OC(=CF)C(F)(F)F H298:-231.90 kcal/mol
library:CHOF_G4 label:OCDC(O)F smiles:OC=C(O)F H298:-114.38 kcal/mol
library:CHOF_G4 label:CC(F)DCO smiles:CC(F)=CO H298:-83.24 kcal/mol
library:CHOF_G4 label:FCDC(CF)OF smiles:FC=C(CF)OF H298:-90.88 kcal/mol
library:CHOFCl_G4 label:FCDC(OF)OCl smiles:FC=C(OF)OCl H298:-43.99 kcal/mol
library:CHOFCl_G4 label:OC(DCF)CCl smiles:OC(=CF)CCl H298:-86.15 kcal/mol
library:CHOFCl_G4 label:FCDCOC(F)Cl smiles:FC=COC(F)Cl H298:-124.05 kcal/mol
library:CHOFCl_G4 label:FCDC(OCl)OCl smiles:FC=C(OCl)OCl H298:-37.81 kcal/mol
library:CHOFCl_G4 label:FCDCOC(Cl)Cl smiles:FC=COC(Cl)Cl H298:-78.68 kcal/mol
library:CHOFCl_G4 label:FCDCOCCl smiles:FC=COCCl H298:-72.74 kcal/mol
library:CHOFCl_G4 label:OC(DCF)C(F)Cl smiles:OC(=CF)C(F)Cl H298:-128.11 kcal/mol
library:CHOFCl_G4 label:FCDC(CCl)OCl smiles:FC=C(CCl)OCl H298:-46.10 kcal/mol
library:CHOFCl_G4 label:FCDC(CF)OCl smiles:FC=C(CF)OCl H298:-83.03 kcal/mol
library:CHOFCl_G4 label:OCDC(F)OCl smiles:OC=C(F)OCl H298:-78.62 kcal/mol
library:CHOFCl_G4 label:FOC(F)DCOCl smiles:FOC(F)=COCl H298:-45.86 kcal/mol
library:CHOFCl_G4 label:CC(F)DCOCl smiles:CC(F)=COCl H298:-44.43 kcal/mol
library:CHOFCl_G4 label:CC(DCF)OCl smiles:CC(=CF)OCl H298:-43.70 kcal/mol
library:CHOFCl_G4 label:FCDCOOCl smiles:FC=COOCl H298:-17.71 kcal/mol
library:CHOFCl_G4 label:FCC(F)DCOCl smiles:FCC(F)=COCl H298:-83.43 kcal/mol
library:CHOFCl_G4 label:FCDCOCl smiles:FC=COCl H298:-31.99 kcal/mol
library:CHOFCl_G4 label:FOCDC(F)OCl smiles:FOC=C(F)OCl H298:-43.55 kcal/mol
library:CHOFCl_G4 label:OC(DCF)OCl smiles:OC(=CF)OCl H298:-73.33 kcal/mol
library:CHOFCl_G4 label:OC(DCF)C(Cl)Cl smiles:OC(=CF)C(Cl)Cl H298:-88.76 kcal/mol
library:CHOFClBr_G4 label:OC(DCF)C(Cl)Br smiles:OC(=CF)C(Cl)Br H298:-76.25 kcal/mol
library:CHOFClBr_G4 label:FCDC(CCl)OBr smiles:FC=C(CCl)OBr H298:-43.48 kcal/mol
library:CHOFClBr_G4 label:FCDCOC(Cl)Br smiles:FC=COC(Cl)Br H298:-66.39 kcal/mol
library:CHOFClBr_G4 label:FCDC(OCl)OBr smiles:FC=C(OCl)OBr H298:-35.83 kcal/mol
library:CHOFBr_G4 label:FCDCOC(Br)(Br)Br smiles:FC=COC(Br)(Br)Br H298:-42.59 kcal/mol
library:CHOFBr_G4 label:OC(DCF)OBr smiles:OC(=CF)OBr H298:-71.84 kcal/mol
library:CHOFBr_G4 label:FOCDC(F)OBr smiles:FOC=C(F)OBr H298:-42.02 kcal/mol
library:CHOFBr_G4 label:FCDCOBr smiles:FC=COBr H298:-29.12 kcal/mol
library:CHOFBr_G4 label:FCDCOC(F)(Br)Br smiles:FC=COC(F)(Br)Br H298:-101.14 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCOBr smiles:FCC(F)=COBr H298:-80.79 kcal/mol
library:CHOFBr_G4 label:FCDCOOBr smiles:FC=COOBr H298:-14.15 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)C(F)F smiles:FC=C(OBr)C(F)F H298:-131.43 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(Br)Br smiles:OC(=CF)C(F)(Br)Br H298:-109.26 kcal/mol
library:CHOFBr_G4 label:CC(DCF)OBr smiles:CC(=CF)OBr H298:-40.89 kcal/mol
library:CHOFBr_G4 label:CC(F)DCOBr smiles:CC(F)=COBr H298:-41.54 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(Br)Br smiles:OC(=CF)C(Br)Br H298:-66.29 kcal/mol
library:CHOFBr_G4 label:FOC(F)DCOBr smiles:FOC(F)=COBr H298:-43.45 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)C(F)Br smiles:FC=C(OBr)C(F)Br H298:-73.84 kcal/mol
library:CHOFBr_G4 label:FCDCOC(F)(F)Br smiles:FC=COC(F)(F)Br H298:-163.54 kcal/mol
library:CHOFBr_G4 label:OCDC(F)OBr smiles:OC=C(F)OBr H298:-77.26 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(F)Br smiles:OC(=CF)C(F)(F)Br H298:-167.86 kcal/mol
library:CHOFBr_G4 label:FCDC(CF)OBr smiles:FC=C(CF)OBr H298:-80.28 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)C(Br)Br smiles:FC=C(OBr)C(Br)Br H298:-23.08 kcal/mol
library:CHOFBr_G4 label:FCDCOC(Br)Br smiles:FC=COC(Br)Br H298:-54.30 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)Br smiles:OC(=CF)C(F)Br H298:-115.59 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)OBr smiles:FC=C(OBr)OBr H298:-34.05 kcal/mol
library:CHOFBr_G4 label:FCDCOCBr smiles:FC=COCBr H298:-60.73 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(Br)(Br)Br smiles:OC(=CF)C(Br)(Br)Br H298:-54.40 kcal/mol
library:CHOFBr_G4 label:FCDCOC(F)Br smiles:FC=COC(F)Br H298:-110.95 kcal/mol
library:CHOFBr_G4 label:FC(DCOBr)C(F)F smiles:FC(=COBr)C(F)F H298:-131.05 kcal/mol
library:CHOFBr_G4 label:FCDC(CBr)OBr smiles:FC=C(CBr)OBr H298:-32.98 kcal/mol
library:CHOFBr_G4 label:OC(DCF)CBr smiles:OC(=CF)CBr H298:-75.46 kcal/mol
library:CHOFBr_G4 label:FCDC(OF)OBr smiles:FC=C(OF)OBr H298:-42.14 kcal/mol
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
        Cpdata = ([-0.585243,-1.11812,-1.18445,-0.983814,-0.548918,-0.220831,-0.145619],'cal/(mol*K)','+|-',[0.121984,0.141024,0.144514,0.142574,0.123951,0.107042,0.0852449]),
        H298 = (4.81129,'kcal/mol','+|-',0.442973),
        S298 = (1.32998,'cal/(mol*K)','+|-',0.287671),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:COCDCCl smiles:COC=CCl H298:-30.43 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)C(Cl)(Cl)Cl smiles:OC=C(Cl)C(Cl)(Cl)Cl H298:-55.01 kcal/mol
library:CHOCl_G4 label:OCDC(O)Cl smiles:OC=C(O)Cl H298:-74.40 kcal/mol
library:CHOCl_G4 label:CC(DCCl)OCl smiles:CC(=CCl)OCl H298:-7.75 kcal/mol
library:CHOCl_G4 label:ClOCDC(Cl)C(Cl)Cl smiles:ClOC=C(Cl)C(Cl)Cl H298:-12.48 kcal/mol
library:CHOCl_G4 label:OCDCCl smiles:OC=CCl H298:-37.21 kcal/mol
library:CHOCl_G4 label:ClCDCOC(Cl)(Cl)Cl smiles:ClC=COC(Cl)(Cl)Cl H298:-43.48 kcal/mol
library:CHOCl_G4 label:ClCDCOOCl smiles:ClC=COOCl H298:19.72 kcal/mol
library:CHOCl_G4 label:OC(DCCl)C(Cl)(Cl)Cl smiles:OC(=CCl)C(Cl)(Cl)Cl H298:-54.42 kcal/mol
library:CHOCl_G4 label:OC(DCCl)CCl smiles:OC(=CCl)CCl H298:-51.01 kcal/mol
library:CHOCl_G4 label:ClOCDC(Cl)C(Cl)(Cl)Cl smiles:ClOC=C(Cl)C(Cl)(Cl)Cl H298:-13.09 kcal/mol
library:CHOCl_G4 label:OOCDCCl smiles:OOC=CCl H298:-12.24 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)OCl smiles:OC=C(Cl)OCl H298:-38.20 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DCOCl smiles:ClCC(Cl)=COCl H298:-9.25 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)CCl smiles:OC=C(Cl)CCl H298:-50.65 kcal/mol
library:CHOCl_G4 label:ClCDC(OCl)OCl smiles:ClC=C(OCl)OCl H298:-2.10 kcal/mol
library:CHOCl_G4 label:CC(Cl)DCO smiles:CC(Cl)=CO H298:-46.49 kcal/mol
library:CHOCl_G4 label:ClCDCOC(Cl)Cl smiles:ClC=COC(Cl)Cl H298:-42.54 kcal/mol
library:CHOCl_G4 label:ClCDCOCl smiles:ClC=COCl H298:4.19 kcal/mol
library:CHOCl_G4 label:ClCDC(OCl)C(Cl)(Cl)Cl smiles:ClC=C(OCl)C(Cl)(Cl)Cl H298:-12.27 kcal/mol
library:CHOCl_G4 label:OC(DCCl)OCl smiles:OC(=CCl)OCl H298:-42.06 kcal/mol
library:CHOCl_G4 label:OC(O)DCCl smiles:OC(O)=CCl H298:-81.59 kcal/mol
library:CHOCl_G4 label:OC(DCCl)C(Cl)Cl smiles:OC(=CCl)C(Cl)Cl H298:-53.59 kcal/mol
library:CHOCl_G4 label:ClCDCOCCl smiles:ClC=COCCl H298:-36.82 kcal/mol
library:CHOCl_G4 label:ClOCDC(Cl)OCl smiles:ClOC=C(Cl)OCl H298:2.58 kcal/mol
library:CHOCl_G4 label:CC(O)DCCl smiles:CC(O)=CCl H298:-48.34 kcal/mol
library:CHOCl_G4 label:CC(Cl)DCOCl smiles:CC(Cl)=COCl H298:-6.38 kcal/mol
library:CHOCl_G4 label:OCDC(Cl)C(Cl)Cl smiles:OC=C(Cl)C(Cl)Cl H298:-54.16 kcal/mol
library:CHOCl_G4 label:ClCDC(CCl)OCl smiles:ClC=C(CCl)OCl H298:-9.68 kcal/mol
library:CHOCl_G4 label:ClCDC(OCl)C(Cl)Cl smiles:ClC=C(OCl)C(Cl)Cl H298:-11.56 kcal/mol
library:CHOFCl_G4 label:FOCDC(Cl)OCl smiles:FOC=C(Cl)OCl H298:-2.53 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)CF smiles:OC=C(Cl)CF H298:-85.17 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)OF smiles:OC=C(Cl)OF H298:-50.31 kcal/mol
library:CHOFCl_G4 label:FOC(Cl)DCOCl smiles:FOC(Cl)=COCl H298:-5.75 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)C(F)Cl smiles:OC=C(Cl)C(F)Cl H298:-95.22 kcal/mol
library:CHOFCl_G4 label:OCDC(Cl)C(F)F smiles:OC=C(Cl)C(F)F H298:-140.56 kcal/mol
library:CHOFCl_G4 label:FCC(Cl)DCOCl smiles:FCC(Cl)=COCl H298:-46.74 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)DCOBr smiles:FCC(Cl)=COBr H298:-44.02 kcal/mol
library:CHOFClBr_G4 label:FOC(Cl)DCOBr smiles:FOC(Cl)=COBr H298:-3.24 kcal/mol
library:CHOFClBr_G4 label:FOCDC(Cl)OBr smiles:FOC=C(Cl)OBr H298:-0.59 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)C(Br)Br smiles:OC(=CCl)C(Br)Br H298:-31.27 kcal/mol
library:CHOClBr_G4 label:ClCDC(OBr)OBr smiles:ClC=C(OBr)OBr H298:1.28 kcal/mol
library:CHOClBr_G4 label:ClCDCOC(Br)Br smiles:ClC=COC(Br)Br H298:-18.25 kcal/mol
library:CHOClBr_G4 label:ClOC(Cl)DCOBr smiles:ClOC(Cl)=COBr H298:5.27 kcal/mol
library:CHOClBr_G4 label:ClCDC(CCl)OBr smiles:ClC=C(CCl)OBr H298:-6.94 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DCOBr smiles:CC(Cl)=COBr H298:-3.64 kcal/mol
library:CHOClBr_G4 label:ClOCDC(Cl)OBr smiles:ClOC=C(Cl)OBr H298:4.73 kcal/mol
library:CHOClBr_G4 label:ClCDCOCBr smiles:ClC=COCBr H298:-24.87 kcal/mol
library:CHOClBr_G4 label:ClCDC(CBr)OBr smiles:ClC=C(CBr)OBr H298:3.34 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)C(Cl)Br smiles:OC(=CCl)C(Cl)Br H298:-40.35 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)OBr smiles:OC(=CCl)OBr H298:-40.18 kcal/mol
library:CHOClBr_G4 label:ClCDCOBr smiles:ClC=COBr H298:7.03 kcal/mol
library:CHOClBr_G4 label:ClCDCOC(Cl)Br smiles:ClC=COC(Cl)Br H298:-30.33 kcal/mol
library:CHOClBr_G4 label:ClCDC(OCl)OBr smiles:ClC=C(OCl)OBr H298:-0.51 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)DCOBr smiles:ClCC(Cl)=COBr H298:-6.72 kcal/mol
library:CHOClBr_G4 label:OCDC(Cl)OBr smiles:OC=C(Cl)OBr H298:-36.74 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)CBr smiles:OC(=CCl)CBr H298:-40.38 kcal/mol
library:CHOClBr_G4 label:ClCDCOOBr smiles:ClC=COOBr H298:23.10 kcal/mol
library:CHOClBr_G4 label:CC(DCCl)OBr smiles:CC(=CCl)OBr H298:-5.14 kcal/mol
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
        Cpdata = ([-0.80803,-1.4232,-1.47799,-1.23546,-0.639719,-0.220328,-0.137386],'cal/(mol*K)','+|-',[0.136174,0.157429,0.161325,0.159158,0.13837,0.119494,0.095161]),
        H298 = (4.96277,'kcal/mol','+|-',0.494502),
        S298 = (1.3119,'cal/(mol*K)','+|-',0.321134),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OCDC(Br)CBr smiles:OC=C(Br)CBr H298:-28.42 kcal/mol
library:CHOBr_G4 label:BrCDCOOBr smiles:BrC=COOBr H298:35.01 kcal/mol
library:CHOBr_G4 label:OC(DCBr)OBr smiles:OC(=CBr)OBr H298:-28.71 kcal/mol
library:CHOBr_G4 label:BrCDC(OBr)C(Br)Br smiles:BrC=C(OBr)C(Br)Br H298:24.65 kcal/mol
library:CHOBr_G4 label:CC(O)DCBr smiles:CC(O)=CBr H298:-36.93 kcal/mol
library:CHOBr_G4 label:OC(O)DCBr smiles:OC(O)=CBr H298:-70.37 kcal/mol
library:CHOBr_G4 label:OOCDCBr smiles:OOC=CBr H298:-0.60 kcal/mol
library:CHOBr_G4 label:OC(DCBr)C(Br)Br smiles:OC(=CBr)C(Br)Br H298:-19.85 kcal/mol
library:CHOBr_G4 label:OCDCBr smiles:OC=CBr H298:-25.74 kcal/mol
library:CHOBr_G4 label:CC(DCBr)OBr smiles:CC(=CBr)OBr H298:6.85 kcal/mol
library:CHOBr_G4 label:BrCDC(CBr)OBr smiles:BrC=C(CBr)OBr H298:14.69 kcal/mol
library:CHOBr_G4 label:OCDC(Br)C(Br)Br smiles:OC=C(Br)C(Br)Br H298:-20.26 kcal/mol
library:CHOBr_G4 label:BrCDCOC(Br)(Br)Br smiles:BrC=COC(Br)(Br)Br H298:4.79 kcal/mol
library:CHOBr_G4 label:OCDC(O)Br smiles:OC=C(O)Br H298:-62.24 kcal/mol
library:CHOBr_G4 label:CC(Br)DCOBr smiles:CC(Br)=COBr H298:8.18 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)OBr smiles:BrOC=C(Br)OBr H298:19.52 kcal/mol
library:CHOBr_G4 label:COCDCBr smiles:COC=CBr H298:-17.41 kcal/mol
library:CHOBr_G4 label:OC(DCBr)CBr smiles:OC(=CBr)CBr H298:-28.90 kcal/mol
library:CHOBr_G4 label:BrCDC(OBr)OBr smiles:BrC=C(OBr)OBr H298:12.73 kcal/mol
library:CHOBr_G4 label:BrCDCOCBr smiles:BrC=COCBr H298:-13.36 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)C(Br)Br smiles:BrOC=C(Br)C(Br)Br H298:23.64 kcal/mol
library:CHOBr_G4 label:BrCDCOBr smiles:BrC=COBr H298:18.47 kcal/mol
library:CHOBr_G4 label:OCDC(Br)OBr smiles:OC=C(Br)OBr H298:-24.86 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCOBr smiles:BrCC(Br)=COBr H298:15.28 kcal/mol
library:CHOBr_G4 label:CC(Br)DCO smiles:CC(Br)=CO H298:-34.93 kcal/mol
library:CHOBr_G4 label:BrCDCOC(Br)Br smiles:BrC=COC(Br)Br H298:-6.68 kcal/mol
library:CHOFClBr_G4 label:OCDC(Br)C(F)Cl smiles:OC=C(Br)C(F)Cl H298:-80.46 kcal/mol
library:CHOFBr_G4 label:FOC(Br)DCOBr smiles:FOC(Br)=COBr H298:8.70 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)DCOBr smiles:FC(Br)C(Br)=COBr H298:-27.31 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)Br smiles:OC=C(Br)C(F)Br H298:-71.62 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)Br smiles:OC=C(Br)C(F)(F)Br H298:-122.10 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)F smiles:OC=C(Br)C(F)(F)F H298:-186.37 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)F smiles:OC=C(Br)C(F)F H298:-129.38 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)DCOBr smiles:FC(F)C(Br)=COBr H298:-84.74 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)CF smiles:OC=C(Br)CF H298:-77.42 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)OF smiles:OC=C(Br)OF H298:-38.62 kcal/mol
library:CHOFBr_G4 label:FOCDC(Br)OBr smiles:FOC=C(Br)OBr H298:11.68 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCOBr smiles:FCC(Br)=COBr H298:-32.74 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(Br)Br smiles:OC=C(Br)C(F)(Br)Br H298:-62.92 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)OCl smiles:OC=C(Br)OCl H298:-26.28 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)DCOBr smiles:ClCC(Br)=COBr H298:4.81 kcal/mol
library:CHOClBr_G4 label:ClOCDC(Br)OBr smiles:ClOC=C(Br)OBr H298:16.75 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Cl smiles:OC=C(Br)C(Cl)Cl H298:-42.93 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Br smiles:OC=C(Br)C(Cl)Br H298:-31.52 kcal/mol
library:CHOClBr_G4 label:ClOC(Br)DCOBr smiles:ClOC(Br)=COBr H298:17.30 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)CCl smiles:OC=C(Br)CCl H298:-39.26 kcal/mol
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
        Cpdata = ([-0.0697326,0.0104131,0.137417,0.21435,0.252668,0.281188,0.335129],'cal/(mol*K)','+|-',[0.0881143,0.101868,0.104389,0.102987,0.0895353,0.0773212,0.0615759]),
        H298 = (1.95954,'kcal/mol','+|-',0.319978),
        S298 = (-0.428866,'cal/(mol*K)','+|-',0.207797),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCC(F)(C(F)(F)F)C(F)(F)F smiles:FCC(F)(C(F)(F)F)C(F)(F)F H298:-421.30 kcal/mol
library:CHOF_G4 label:FC(F)C(C(F)(F)F)C(F)(F)F smiles:FC(F)C(C(F)(F)F)C(F)(F)F H298:-432.23 kcal/mol
library:CHOF_G4 label:OC(F)(C(F)(F)F)C(F)(F)F smiles:OC(F)(C(F)(F)F)C(F)(F)F H298:-417.77 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(C(F)(F)F)C(F)(F)F smiles:FC(F)(F)C(F)(C(F)(F)F)C(F)(F)F H298:-523.90 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)(F)F)C(F)(F)F H298:-469.60 kcal/mol
library:CHOF_G4 label:FC(C(F)(F)F)C(F)(F)F smiles:FC(C(F)(F)F)C(F)(F)F H298:-372.46 kcal/mol
library:CHOF_G4 label:FOC(C(F)(F)F)C(F)(F)F smiles:FOC(C(F)(F)F)C(F)(F)F H298:-333.30 kcal/mol
library:CHOF_G4 label:FOC(F)(C(F)(F)F)C(F)(F)F smiles:FOC(F)(C(F)(F)F)C(F)(F)F H298:-377.83 kcal/mol
library:CHOF_G4 label:OC(C(F)(F)F)C(F)(F)F smiles:OC(C(F)(F)F)C(F)(F)F H298:-369.50 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(C(F)(F)F)C(F)(F)F smiles:FC(F)(F)C(C(F)(F)F)C(F)(F)F H298:-488.14 kcal/mol
library:CHOF_G4 label:CC(F)(C(F)(F)F)C(F)(F)F smiles:CC(F)(C(F)(F)F)C(F)(F)F H298:-384.64 kcal/mol
library:CHOF_G4 label:CC(C(F)(F)F)C(F)(F)F smiles:CC(C(F)(F)F)C(F)(F)F H298:-343.07 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)(F)C(F)(F)C(F)(F)F H298:-420.07 kcal/mol
library:CHOF_G4 label:FCC(C(F)(F)F)C(F)(F)F smiles:FCC(C(F)(F)F)C(F)(F)F H298:-382.12 kcal/mol
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
        Cpdata = ([0.437111,0.331375,0.267122,0.226896,0.16129,0.127955,0.100496],'cal/(mol*K)','+|-',[0.0904328,0.104548,0.107135,0.105697,0.0918911,0.0793557,0.0631961]),
        H298 = (5.34894,'kcal/mol','+|-',0.328397),
        S298 = (-0.607447,'cal/(mol*K)','+|-',0.213264),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-44.60 kcal/mol
library:CHOCl_G4 label:OC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-81.22 kcal/mol
library:CHOCl_G4 label:ClOC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-42.50 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-34.54 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-42.50 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-41.07 kcal/mol
library:CHOCl_G4 label:OC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-83.45 kcal/mol
library:CHOCl_G4 label:CC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-50.37 kcal/mol
library:CHOCl_G4 label:CC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-50.56 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-51.43 kcal/mol
library:CHOCl_G4 label:ClCC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-52.31 kcal/mol
library:CHOCl_G4 label:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-43.74 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-48.72 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-40.31 kcal/mol
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
        Cpdata = ([-0.124038,-0.0362871,0.145397,0.196695,0.137032,0.157984,0.227765],'cal/(mol*K)','+|-',[0.144949,0.167574,0.171721,0.169415,0.147287,0.127195,0.101293]),
        H298 = (2.84159,'kcal/mol','+|-',0.526368),
        S298 = (-0.516204,'cal/(mol*K)','+|-',0.341828),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:OC(F)(F)C(F)(F)C(F)(F)F smiles:OC(F)(F)C(F)(F)C(F)(F)F H298:-416.21 kcal/mol
library:CHOF_G4 label:CC(F)(C(F)F)C(F)(F)F smiles:CC(F)(C(F)F)C(F)(F)F H298:-329.47 kcal/mol
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)(F)F smiles:FCC(F)(C(F)F)C(F)(F)F H298:-365.50 kcal/mol
library:CHOF_G4 label:OC(C(F)F)C(F)(F)F smiles:OC(C(F)F)C(F)(F)F H298:-312.90 kcal/mol
library:CHOF_G4 label:FC(F)C(C(F)(F)F)C(F)(F)F smiles:FC(F)C(C(F)(F)F)C(F)(F)F H298:-432.23 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)(F)C(F)(F)F smiles:FCC(F)(F)C(F)(F)C(F)(F)F H298:-415.15 kcal/mol
library:CHOF_G4 label:CC(C(F)F)C(F)(F)F smiles:CC(C(F)F)C(F)(F)F H298:-286.11 kcal/mol
library:CHOF_G4 label:FC(F)(F)C(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)(F)C(F)(F)C(F)(F)C(F)(F)F H298:-518.11 kcal/mol
library:CHOF_G4 label:FOC(F)(C(F)F)C(F)(F)F smiles:FOC(F)(C(F)F)C(F)(F)F H298:-323.85 kcal/mol
library:CHOF_G4 label:FC(C(F)(F)F)C(F)(F)C(F)(F)F smiles:FC(C(F)(F)F)C(F)(F)C(F)(F)F H298:-471.81 kcal/mol
library:CHOF_G4 label:OC(F)(C(F)F)C(F)(F)F smiles:OC(F)(C(F)F)C(F)(F)F H298:-362.54 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)C(F)(F)F H298:-415.54 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)C(F)(F)F smiles:CC(F)(F)C(F)C(F)(F)F H298:-329.68 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)(F)F)C(F)(F)F H298:-469.60 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)(F)C(F)(F)F smiles:CC(F)(F)C(F)(F)C(F)(F)F H298:-378.68 kcal/mol
library:CHOF_G4 label:FOC(C(F)F)C(F)(F)F smiles:FOC(C(F)F)C(F)(F)F H298:-279.35 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)(F)C(F)(F)F H298:-463.90 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(F)C(F)(F)F smiles:FC(F)C(F)(F)C(F)(F)F H298:-365.14 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)(F)C(F)(F)F smiles:FOC(F)(F)C(F)(F)C(F)(F)F H298:-375.57 kcal/mol
library:CHOF_G4 label:FCC(F)(F)C(F)C(F)(F)F smiles:FCC(F)(F)C(F)C(F)(F)F H298:-368.56 kcal/mol
library:CHOF_G4 label:FCC(C(F)F)C(F)(F)F smiles:FCC(C(F)F)C(F)(F)F H298:-325.75 kcal/mol
library:CHOF_G4 label:FOC(F)(F)C(F)C(F)(F)F smiles:FOC(F)(F)C(F)C(F)(F)F H298:-328.06 kcal/mol
library:CHOF_G4 label:FC(F)C(F)(C(F)F)C(F)(F)F smiles:FC(F)C(F)(C(F)F)C(F)(F)F H298:-414.90 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)C(F)(F)F smiles:OC(F)(F)C(F)C(F)(F)F H298:-367.83 kcal/mol
library:CHOF_G4 label:FC(F)C(C(F)F)C(F)(F)F smiles:FC(F)C(C(F)F)C(F)(F)F H298:-376.30 kcal/mol
library:CHOF_G4 label:FC(F)C(F)C(F)(F)F smiles:FC(F)C(F)C(F)(F)F H298:-317.05 kcal/mol
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
        Cpdata = ([0.223449,-0.0729947,-0.251713,-0.324498,-0.356441,-0.294441,-0.0985339],'cal/(mol*K)','+|-',[0.146739,0.169643,0.173841,0.171507,0.149105,0.128765,0.102544]),
        H298 = (6.25146,'kcal/mol','+|-',0.532867),
        S298 = (-1.09714,'cal/(mol*K)','+|-',0.346049),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.15 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-44.60 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-85.64 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-54.39 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-57.91 kcal/mol
library:CHOCl_G4 label:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-53.17 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-58.28 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-54.38 kcal/mol
library:CHOCl_G4 label:CC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-56.43 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-48.10 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-47.42 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-55.56 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-52.54 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)C(Cl)(Cl)Cl H298:-48.96 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-52.65 kcal/mol
library:CHOCl_G4 label:OC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-86.10 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-51.43 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl H298:-46.21 kcal/mol
library:CHOCl_G4 label:OC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-86.00 kcal/mol
library:CHOCl_G4 label:CC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(C(Cl)Cl)C(Cl)(Cl)Cl H298:-54.65 kcal/mol
library:CHOCl_G4 label:ClOC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(C(Cl)Cl)C(Cl)(Cl)Cl H298:-45.44 kcal/mol
library:CHOCl_G4 label:ClC(Cl)C(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(C(Cl)Cl)C(Cl)(Cl)Cl H298:-56.14 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl H298:-49.19 kcal/mol
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-46.43 kcal/mol
library:CHOCl_G4 label:OC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(C(Cl)Cl)C(Cl)(Cl)Cl H298:-84.88 kcal/mol
library:CHOCl_G4 label:ClCC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(C(Cl)Cl)C(Cl)(Cl)Cl H298:-55.36 kcal/mol
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
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 0.001""",
    longDesc = 
"""
Dervied using the following species:
  CHOBr_G4 BrC(Br)CC(Br)(Br)Br
  CHOBr_G4 BrC(Br)OC(Br)(Br)Br
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
        Cpdata = ([-0.44659,-0.627522,-0.626103,-0.492381,-0.356182,-0.253261,-0.0336473],'cal/(mol*K)','+|-',[0.223432,0.258307,0.264698,0.261144,0.227035,0.196064,0.156138]),
        H298 = (2.19497,'kcal/mol','+|-',0.811368),
        S298 = (0.975573,'cal/(mol*K)','+|-',0.52691),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:CDC(F)OC(F)(F)Br smiles:C=C(F)OC(F)(F)Br H298:-168.73 kcal/mol
library:CHOFBr_G4 label:CC(F)DCC(F)(F)Br smiles:CC(F)=CC(F)(F)Br H298:-139.83 kcal/mol
library:CHOFBr_G4 label:CDC(F)OC(Br)(Br)Br smiles:C=C(F)OC(Br)(Br)Br H298:-46.73 kcal/mol
library:CHOFBr_G4 label:CDC(F)CC(F)(F)Br smiles:C=C(F)CC(F)(F)Br H298:-140.20 kcal/mol
library:CHOFBr_G4 label:CDC(F)CC(Br)(Br)Br smiles:C=C(F)CC(Br)(Br)Br H298:-25.30 kcal/mol
library:CHOFBr_G4 label:CDC(F)OC(F)(Br)Br smiles:C=C(F)OC(F)(Br)Br H298:-105.33 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCC(F)(Br)Br smiles:OC(Br)=CC(F)(Br)Br H298:-61.27 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCC(F)(F)F smiles:CC(Br)=CC(F)(F)F H298:-152.15 kcal/mol
library:CHOFBr_G4 label:CC(F)DCC(F)(Br)Br smiles:CC(F)=CC(F)(Br)Br H298:-80.29 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCC(F)(F)Br smiles:CC(Br)=CC(F)(F)Br H298:-87.35 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCC(F)(Br)Br smiles:CC(Br)=CC(F)(Br)Br H298:-28.19 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCC(F)(F)F smiles:OC(Br)=CC(F)(F)F H298:-184.83 kcal/mol
library:CHOFBr_G4 label:CC(F)DCC(Br)(Br)Br smiles:CC(F)=CC(Br)(Br)Br H298:-25.07 kcal/mol
library:CHOFBr_G4 label:CDC(F)CC(F)(Br)Br smiles:C=C(F)CC(F)(Br)Br H298:-80.81 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCC(F)(F)Br smiles:OC(Br)=CC(F)(F)Br H298:-120.47 kcal/mol
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
        Cpdata = ([-0.58724,-0.456463,-0.242131,-0.0958323,-0.0413474,-0.0238637,0.111622],'cal/(mol*K)','+|-',[0.186127,0.215179,0.220503,0.217542,0.189128,0.163328,0.130069]),
        H298 = (1.24627,'kcal/mol','+|-',0.675899),
        S298 = (0.536197,'cal/(mol*K)','+|-',0.438935),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FCDC(F)C(F)(F)C(F)(F)F smiles:FC=C(F)C(F)(F)C(F)(F)F H298:-332.04 kcal/mol
library:CHOF_G4 label:FCC(F)DC(F)C(F)(F)F smiles:FCC(F)=C(F)C(F)(F)F H298:-280.88 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)(F)F smiles:FC(=C(F)C(F)(F)F)C(F)(F)F H298:-382.97 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)C(F)(F)F smiles:FC(F)=C(F)C(F)C(F)(F)F H298:-327.95 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)C(F)(F)F smiles:C=C(F)C(F)(F)C(F)(F)F H298:-293.10 kcal/mol
library:CHOF_G4 label:CC(F)DC(F)C(F)(F)F smiles:CC(F)=C(F)C(F)(F)F H298:-241.68 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)OC(F)(F)F smiles:FC(F)=C(F)OC(F)(F)F H298:-315.21 kcal/mol
library:CHOF_G4 label:FC(DCC(F)(F)F)C(F)(F)F smiles:FC(=CC(F)(F)F)C(F)(F)F H298:-349.10 kcal/mol
library:CHOF_G4 label:FCDC(F)CC(F)(F)F smiles:FC=C(F)CC(F)(F)F H298:-244.62 kcal/mol
library:CHOF_G4 label:CC(F)DCC(F)(F)F smiles:CC(F)=CC(F)(F)F H298:-204.54 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)CC(F)(F)F smiles:FC(F)=C(F)CC(F)(F)F H298:-289.84 kcal/mol
library:CHOF_G4 label:FC(DC(F)C(F)(F)F)C(F)F smiles:FC(=C(F)C(F)(F)F)C(F)F H298:-329.07 kcal/mol
library:CHOF_G4 label:FOC(F)DCC(F)(F)F smiles:FOC(F)=CC(F)(F)F H298:-201.98 kcal/mol
library:CHOF_G4 label:FCDC(F)OC(F)(F)F smiles:FC=C(F)OC(F)(F)F H298:-272.26 kcal/mol
library:CHOF_G4 label:OC(F)DCC(F)(F)F smiles:OC(F)=CC(F)(F)F H298:-241.78 kcal/mol
library:CHOF_G4 label:CDC(F)OC(F)(F)F smiles:C=C(F)OC(F)(F)F H298:-235.06 kcal/mol
library:CHOF_G4 label:FCC(F)DCC(F)(F)F smiles:FCC(F)=CC(F)(F)F H298:-243.02 kcal/mol
library:CHOF_G4 label:FC(DCC(F)(F)F)C(F)F smiles:FC(=CC(F)(F)F)C(F)F H298:-293.12 kcal/mol
library:CHOF_G4 label:CDC(F)CC(F)(F)F smiles:C=C(F)CC(F)(F)F H298:-204.93 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)C(F)(F)F H298:-374.89 kcal/mol
library:CHOF_G4 label:FCDC(F)C(F)C(F)(F)F smiles:FC=C(F)C(F)C(F)(F)F H298:-283.24 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)C(F)(F)F smiles:OC(F)=C(F)C(F)(F)F H298:-274.97 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)C(F)(F)F smiles:C=C(F)C(F)C(F)(F)F H298:-243.94 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)C(F)(F)F smiles:FOC(F)=C(F)C(F)(F)F H298:-238.81 kcal/mol
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
        Cpdata = ([0.0310318,-0.073957,-0.107888,-0.103127,-0.066072,0.00919709,0.212215],'cal/(mol*K)','+|-',[0.1884,0.217807,0.223197,0.2202,0.191438,0.165323,0.131657]),
        H298 = (2.69545,'kcal/mol','+|-',0.684155),
        S298 = (-0.272392,'cal/(mol*K)','+|-',0.444297),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClOC(Cl)DCC(Cl)(Cl)Cl smiles:ClOC(Cl)=CC(Cl)(Cl)Cl H298:-13.25 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-23.64 kcal/mol
library:CHOCl_G4 label:CC(Cl)DCC(Cl)(Cl)Cl smiles:CC(Cl)=CC(Cl)(Cl)Cl H298:-20.33 kcal/mol
library:CHOCl_G4 label:ClOC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClOC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-14.16 kcal/mol
library:CHOCl_G4 label:ClC(DCC(Cl)(Cl)Cl)C(Cl)Cl smiles:ClC(=CC(Cl)(Cl)Cl)C(Cl)Cl H298:-26.46 kcal/mol
library:CHOCl_G4 label:CC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:CC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-20.67 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DCC(Cl)(Cl)Cl smiles:ClCC(Cl)=CC(Cl)(Cl)Cl H298:-23.20 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-32.82 kcal/mol
library:CHOCl_G4 label:OC(Cl)DCC(Cl)(Cl)Cl smiles:OC(Cl)=CC(Cl)(Cl)Cl H298:-54.11 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-24.56 kcal/mol
library:CHOCl_G4 label:ClCC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClCC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-23.53 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)OC(Cl)(Cl)Cl smiles:ClC=C(Cl)OC(Cl)(Cl)Cl H298:-45.98 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-29.53 kcal/mol
library:CHOCl_G4 label:CDC(Cl)CC(Cl)(Cl)Cl smiles:C=C(Cl)CC(Cl)(Cl)Cl H298:-21.44 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)CC(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)CC(Cl)(Cl)Cl H298:-30.38 kcal/mol
library:CHOCl_G4 label:OC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:OC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-53.77 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-19.61 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:C=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-22.98 kcal/mol
library:CHOCl_G4 label:ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)Cl smiles:ClC(=C(Cl)C(Cl)(Cl)Cl)C(Cl)Cl H298:-26.83 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-28.39 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)CC(Cl)(Cl)Cl smiles:ClC=C(Cl)CC(Cl)(Cl)Cl H298:-27.02 kcal/mol
library:CHOCl_G4 label:ClC(DCC(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(=CC(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-26.55 kcal/mol
library:CHOCl_G4 label:CDC(Cl)OC(Cl)(Cl)Cl smiles:C=C(Cl)OC(Cl)(Cl)Cl H298:-41.91 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)OC(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)OC(Cl)(Cl)Cl H298:-49.32 kcal/mol
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
        Cpdata = ([-0.224102,-0.00125138,0.0344016,-0.0111143,-0.139919,-0.173419,-0.0365788],'cal/(mol*K)','+|-',[0.426345,0.492892,0.505089,0.498307,0.433221,0.374122,0.297938]),
        H298 = (2.55454,'kcal/mol','+|-',1.54823),
        S298 = (1.39216,'cal/(mol*K)','+|-',1.00543),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:FC(Br)DCC(Br)(Br)Br smiles:FC(Br)=CC(Br)(Br)Br H298:-5.03 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)(F)Br smiles:FC(F)=CC(F)(F)Br H298:-176.01 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)(Br)Br smiles:FC(F)=CC(F)(Br)Br H298:-116.14 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(Br)(Br)Br smiles:FC(F)=CC(Br)(Br)Br H298:-60.70 kcal/mol
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
        Cpdata = ([-0.658789,-0.609708,-0.415839,-0.282588,-0.228733,-0.229279,-0.105021],'cal/(mol*K)','+|-',[0.277136,0.320393,0.328322,0.323913,0.281605,0.24319,0.193668]),
        H298 = (1.93111,'kcal/mol','+|-',1.00639),
        S298 = (-0.718938,'cal/(mol*K)','+|-',0.653559),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:CC(DC(F)F)C(F)(F)F smiles:CC(=C(F)F)C(F)(F)F H298:-249.07 kcal/mol
library:CHOF_G4 label:FC(F)DC(F)C(F)(F)F smiles:FC(F)=C(F)C(F)(F)F H298:-274.47 kcal/mol
library:CHOF_G4 label:FCC(DC(F)F)C(F)(F)F smiles:FCC(=C(F)F)C(F)(F)F H298:-292.00 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)(F)F smiles:FC(F)=CC(F)(F)F H298:-240.95 kcal/mol
library:CHOF_G4 label:FC(F)DC(C(F)(F)F)C(F)(F)F smiles:FC(F)=C(C(F)(F)F)C(F)(F)F H298:-394.08 kcal/mol
library:CHOF_G4 label:FC(F)DC(C(F)F)C(F)(F)F smiles:FC(F)=C(C(F)F)C(F)(F)F H298:-339.52 kcal/mol
library:CHOF_G4 label:FOC(DC(F)F)C(F)(F)F smiles:FOC(=C(F)F)C(F)(F)F H298:-242.07 kcal/mol
library:CHOF_G4 label:OC(DC(F)F)C(F)(F)F smiles:OC(=C(F)F)C(F)(F)F H298:-272.98 kcal/mol
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
        Cpdata = ([0.187936,0.289692,0.314885,0.352008,0.36039,0.393313,0.546768],'cal/(mol*K)','+|-',[0.283595,0.327861,0.335974,0.331462,0.288168,0.248858,0.198181]),
        H298 = (7.27733,'kcal/mol','+|-',1.02985),
        S298 = (-1.62632,'cal/(mol*K)','+|-',0.668791),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClCC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:ClCC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-23.61 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(C(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(C(Cl)Cl)C(Cl)(Cl)Cl H298:-23.22 kcal/mol
library:CHOCl_G4 label:OC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:OC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-51.59 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DCC(Cl)(Cl)Cl smiles:ClC(Cl)=CC(Cl)(Cl)Cl H298:-13.86 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)(Cl)Cl H298:-13.38 kcal/mol
library:CHOCl_G4 label:ClOC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:ClOC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-12.00 kcal/mol
library:CHOCl_G4 label:CC(DC(Cl)Cl)C(Cl)(Cl)Cl smiles:CC(=C(Cl)Cl)C(Cl)(Cl)Cl H298:-20.12 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)=C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl H298:-9.79 kcal/mol
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
        Cpdata = ([1.2299,1.53598,1.52692,1.38182,0.960811,0.627291,0.268676],'cal/(mol*K)','+|-',[0.190681,0.220444,0.225899,0.222866,0.193756,0.167325,0.133252]),
        H298 = (2.2492,'kcal/mol','+|-',0.692439),
        S298 = (-1.19053,'cal/(mol*K)','+|-',0.449676),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODCCC(F)(F)Cl smiles:O=CCC(F)(F)Cl H298:-148.27 kcal/mol
library:CHOFCl_G4 label:ODCCC(F)(Cl)Cl smiles:O=CCC(F)(Cl)Cl H298:-100.50 kcal/mol
library:CHOFCl_G4 label:ODCOC(F)(F)Cl smiles:O=COC(F)(F)Cl H298:-190.31 kcal/mol
library:CHOFCl_G4 label:ODCOC(F)(Cl)Cl smiles:O=COC(F)(Cl)Cl H298:-140.04 kcal/mol
library:CHOFClBr_G4 label:ODCOC(F)(Cl)Br smiles:O=COC(F)(Cl)Br H298:-126.97 kcal/mol
library:CHOFClBr_G4 label:ODCCC(F)(Cl)Br smiles:O=CCC(F)(Cl)Br H298:-87.76 kcal/mol
library:CHOFBr_G4 label:ODC(Br)OC(F)(Br)Br smiles:O=C(Br)OC(F)(Br)Br H298:-109.99 kcal/mol
library:CHOFBr_G4 label:ODCOC(F)(Br)Br smiles:O=COC(F)(Br)Br H298:-113.97 kcal/mol
library:CHOFBr_G4 label:ODCOC(F)(F)Br smiles:O=COC(F)(F)Br H298:-176.66 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CC(F)(F)Br smiles:O=C(Br)CC(F)(F)Br H298:-137.64 kcal/mol
library:CHOFBr_G4 label:ODCCC(F)(Br)Br smiles:O=CCC(F)(Br)Br H298:-74.92 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CC(F)(Br)Br smiles:O=C(Br)CC(F)(Br)Br H298:-78.20 kcal/mol
library:CHOFBr_G4 label:ODCCC(F)(F)Br smiles:O=CCC(F)(F)Br H298:-134.93 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)Br smiles:O=CC(Br)C(F)(F)Br H298:-126.04 kcal/mol
library:CHOFBr_G4 label:ODC(Br)OC(F)(F)Br smiles:O=C(Br)OC(F)(F)Br H298:-172.27 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(Br)Br smiles:O=CC(Br)C(F)(Br)Br H298:-66.98 kcal/mol
library:CHOClBr_G4 label:ODCCC(Cl)(Cl)Br smiles:O=CCC(Cl)(Cl)Br H298:-44.37 kcal/mol
library:CHOClBr_G4 label:ODCOC(Cl)(Br)Br smiles:O=COC(Cl)(Br)Br H298:-67.79 kcal/mol
library:CHOClBr_G4 label:ODCOC(Cl)(Cl)Br smiles:O=COC(Cl)(Cl)Br H298:-80.18 kcal/mol
library:CHOClBr_G4 label:ODCCC(Cl)(Br)Br smiles:O=CCC(Cl)(Br)Br H298:-32.39 kcal/mol
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
        Cpdata = ([0.615218,0.675946,0.674741,0.609476,0.435982,0.306617,0.128881],'cal/(mol*K)','+|-',[0.260224,0.300841,0.308285,0.304146,0.26442,0.228349,0.181849]),
        H298 = (1.51641,'kcal/mol','+|-',0.944974),
        S298 = (-0.272395,'cal/(mol*K)','+|-',0.613675),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:ODC(F)C(F)C(F)(F)F smiles:O=C(F)C(F)C(F)(F)F H298:-298.02 kcal/mol
library:CHOF_G4 label:ODC(F)CC(F)(F)F smiles:O=C(F)CC(F)(F)F H298:-262.32 kcal/mol
library:CHOF_G4 label:ODC(F)C(F)(F)C(F)(F)F smiles:O=C(F)C(F)(F)C(F)(F)F H298:-344.15 kcal/mol
library:CHOF_G4 label:ODCC(F)(F)C(F)(F)F smiles:O=CC(F)(F)C(F)(F)F H298:-285.38 kcal/mol
library:CHOF_G4 label:ODC(F)OC(F)(F)F smiles:O=C(F)OC(F)(F)F H298:-297.47 kcal/mol
library:CHOF_G4 label:ODCCC(F)(F)F smiles:O=CCC(F)(F)F H298:-199.40 kcal/mol
library:CHOF_G4 label:ODCOC(F)(F)F smiles:O=COC(F)(F)F H298:-242.91 kcal/mol
library:CHOF_G4 label:ODCC(F)C(F)(F)F smiles:O=CC(F)C(F)(F)F H298:-237.65 kcal/mol
library:CHOFBr_G4 label:ODC(Br)OC(F)(F)F smiles:O=C(Br)OC(F)(F)F H298:-238.07 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CC(F)(F)F smiles:O=C(Br)CC(F)(F)F H298:-202.28 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)F smiles:O=CC(Br)C(F)(F)F H298:-189.47 kcal/mol
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
        Cpdata = ([0.743891,0.882367,0.923973,0.875058,0.684421,0.50893,0.286778],'cal/(mol*K)','+|-',[0.305008,0.352616,0.361341,0.356489,0.309927,0.267648,0.213145]),
        H298 = (1.33477,'kcal/mol','+|-',1.1076),
        S298 = (-0.942521,'cal/(mol*K)','+|-',0.719288),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ODC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl H298:-70.00 kcal/mol
library:CHOCl_G4 label:ODCOC(Cl)(Cl)Cl smiles:O=COC(Cl)(Cl)Cl H298:-92.61 kcal/mol
library:CHOCl_G4 label:ODCCC(Cl)(Cl)Cl smiles:O=CCC(Cl)(Cl)Cl H298:-56.33 kcal/mol
library:CHOCl_G4 label:ODC(Cl)C(Cl)C(Cl)(Cl)Cl smiles:O=C(Cl)C(Cl)C(Cl)(Cl)Cl H298:-72.30 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)(Cl)C(Cl)(Cl)Cl smiles:O=CC(Cl)(Cl)C(Cl)(Cl)Cl H298:-60.22 kcal/mol
library:CHOCl_G4 label:ODC(Cl)OC(Cl)(Cl)Cl smiles:O=C(Cl)OC(Cl)(Cl)Cl H298:-101.49 kcal/mol
library:CHOCl_G4 label:ODCC(Cl)C(Cl)(Cl)Cl smiles:O=CC(Cl)C(Cl)(Cl)Cl H298:-59.13 kcal/mol
library:CHOCl_G4 label:ODC(Cl)CC(Cl)(Cl)Cl smiles:O=C(Cl)CC(Cl)(Cl)Cl H298:-72.03 kcal/mol
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
        Cpdata = ([1.52711,1.80125,1.76276,1.56904,1.03151,0.582797,-0.0787966],'cal/(mol*K)','+|-',[0.588044,0.67983,0.696653,0.687298,0.597527,0.516015,0.410936]),
        H298 = (3.8026,'kcal/mol','+|-',2.13542),
        S298 = (-1.21407,'cal/(mol*K)','+|-',1.38676),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODCOC(Br)(Br)Br smiles:O=COC(Br)(Br)Br H298:-55.46 kcal/mol
library:CHOBr_G4 label:ODCCC(Br)(Br)Br smiles:O=CCC(Br)(Br)Br H298:-20.51 kcal/mol
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

