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
        Cpdata = ([0.58395,0.422438,0.329857,0.265712,0.142862,0.039853,-0.000261073],'cal/(mol*K)','+|-',[0.426923,0.490661,0.501576,0.494217,0.428553,0.369623,0.301235]),
        H298 = (4.083,'kcal/mol','+|-',1.52195),
        S298 = (-0.560747,'cal/(mol*K)','+|-',1.0373),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClC(Cl)(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)(Cl)C(Cl)(Cl)Cl H298:-38.94 kcal/mol
""",
)

entry(
    index = 2,
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
        Cpdata = ([-0.0562964,-0.279006,-0.263713,-0.232479,-0.195939,-0.109275,0.408085],'cal/(mol*K)','+|-',[0.172022,0.197704,0.202102,0.199137,0.172679,0.148934,0.121378]),
        H298 = (9.19951,'kcal/mol','+|-',0.613244),
        S298 = (0.302736,'cal/(mol*K)','+|-',0.417963),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClC(Cl)C(Cl)(Cl)Cl smiles:ClC(Cl)C(Cl)(Cl)Cl H298:-38.92 kcal/mol
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
    index = 3,
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
        Cpdata = ([-0.218209,-0.313114,-0.280043,-0.250572,-0.215988,-0.129575,0.282924],'cal/(mol*K)','+|-',[0.138067,0.15868,0.162209,0.15983,0.138594,0.119536,0.0974192]),
        H298 = (5.43337,'kcal/mol','+|-',0.492196),
        S298 = (1.24034,'cal/(mol*K)','+|-',0.335461),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClCC(Cl)(Cl)Cl smiles:ClCC(Cl)(Cl)Cl H298:-37.44 kcal/mol
""",
)

entry(
    index = 4,
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
        Cpdata = ([-0.333743,-0.0133789,0.172704,0.254693,0.327201,0.376529,0.492609],'cal/(mol*K)','+|-',[0.241826,0.27793,0.284113,0.279944,0.242749,0.209369,0.170631]),
        H298 = (3.7534,'kcal/mol','+|-',0.86209),
        S298 = (0.760007,'cal/(mol*K)','+|-',0.587566),
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
    index = 5,
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
        Cpdata = ([-0.504428,-0.552738,-0.463401,-0.415572,-0.331486,-0.179609,0.259167],'cal/(mol*K)','+|-',[0.0679905,0.0781412,0.0798795,0.0787075,0.0682501,0.0588651,0.0479737]),
        H298 = (3.08883,'kcal/mol','+|-',0.24238),
        S298 = (0.151144,'cal/(mol*K)','+|-',0.165197),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClC(Cl)C(Cl)Cl smiles:ClC(Cl)C(Cl)Cl H298:-37.69 kcal/mol
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
    index = 6,
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
        Cpdata = ([-0.715291,-0.645127,-0.434825,-0.333433,-0.221158,-0.035405,0.469835],'cal/(mol*K)','+|-',[0.0836012,0.0960826,0.09822,0.096779,0.0839204,0.0723806,0.0589886]),
        H298 = (3.56967,'kcal/mol','+|-',0.298031),
        S298 = (0.8342,'cal/(mol*K)','+|-',0.203126),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClCC(Cl)Cl smiles:ClCC(Cl)Cl H298:-35.37 kcal/mol
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
library:CHOClBr_G4 label:ClCC(Cl)(Cl)CBr smiles:ClCC(Cl)(Cl)CBr H298:-39.12 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)OBr smiles:ClC(Cl)C(Cl)OBr H298:-35.44 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)CBr smiles:ClC(Cl)C(Cl)CBr H298:-36.54 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)OBr smiles:ClCC(Cl)(Cl)OBr H298:-38.16 kcal/mol
""",
)

entry(
    index = 7,
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
        Cpdata = ([-0.357494,-0.0502204,0.173519,0.285409,0.374694,0.435673,0.733549],'cal/(mol*K)','+|-',[0.164481,0.189038,0.193243,0.190408,0.165109,0.142405,0.116057]),
        H298 = (2.93915,'kcal/mol','+|-',0.586362),
        S298 = (0.37319,'cal/(mol*K)','+|-',0.399641),
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
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Cl)OBr smiles:C=C(Cl)C(Cl)(Cl)OBr H298:-12.98 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)C(Cl)Cl smiles:CC(Br)=C(Cl)C(Cl)Cl H298:-11.76 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Cl)CBr smiles:C=C(Cl)C(Cl)(Cl)CBr H298:-13.98 kcal/mol
""",
)

entry(
    index = 8,
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
        Cpdata = ([-0.212013,-0.139086,-0.0392286,0.0215442,0.0690026,0.110935,0.206044],'cal/(mol*K)','+|-',[0.0486654,0.055931,0.0571752,0.0563364,0.0488512,0.0421337,0.0343381]),
        H298 = (1.15744,'kcal/mol','+|-',0.173488),
        S298 = (0.660503,'cal/(mol*K)','+|-',0.118243),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClCCCl smiles:ClCCCl H298:-31.46 kcal/mol
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
library:CHOClBr_G4 label:ClCC(Cl)CBr smiles:ClCC(Cl)CBr H298:-33.48 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)CCl smiles:CC(Br)C(Cl)CCl H298:-42.23 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Br)Br smiles:ClCC(Cl)C(Br)Br H298:-24.39 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)CBr smiles:CC(Cl)C(Cl)CBr H298:-41.84 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(Cl)OBr smiles:OC(Cl)C(Cl)OBr H298:-71.61 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Cl)Br smiles:ClCC(Cl)C(Cl)Br H298:-35.75 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)COBr smiles:ClCC(Cl)COBr H298:-36.93 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CCl)CBr smiles:CC(Cl)(CCl)CBr H298:-43.25 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(CCl)OBr smiles:OC(Cl)(CCl)OBr H298:-78.89 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)OOBr smiles:ClCC(Cl)OOBr H298:-16.59 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)OCBr smiles:ClCC(Cl)OCBr H298:-65.04 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)CCl smiles:CC(Br)(Br)C(Cl)CCl H298:-34.51 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)CCBr smiles:ClCC(Cl)CCBr H298:-40.55 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(CCl)CBr smiles:OC(Cl)(CCl)CBr H298:-76.20 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CCl)OBr smiles:CC(Cl)(CCl)OBr H298:-44.83 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)CCl smiles:O=C(Br)C(Cl)CCl H298:-57.99 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)OBr smiles:CC(Cl)C(Cl)OBr H298:-41.11 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)CCl smiles:OC(Br)C(Cl)CCl H298:-72.03 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)OBr smiles:ClCC(Cl)OBr H298:-33.46 kcal/mol
""",
)

entry(
    index = 9,
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
        Cpdata = ([-0.370477,-0.128165,0.0193874,0.0781517,0.147875,0.195604,0.451944],'cal/(mol*K)','+|-',[0.148707,0.170908,0.17471,0.172147,0.149275,0.128748,0.104927]),
        H298 = (1.80547,'kcal/mol','+|-',0.530128),
        S298 = (1.18089,'cal/(mol*K)','+|-',0.361314),
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
library:CHOClBr_G4 label:CDC(Cl)C(Cl)CBr smiles:C=C(Cl)C(Cl)CBr H298:-10.99 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)DCCBr smiles:ClCC(Cl)=CCBr H298:-9.76 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)CCl smiles:CC(Br)=C(Cl)CCl H298:-11.56 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)DCOBr smiles:ClCC(Cl)=COBr H298:-6.73 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)C(Cl)Br smiles:C=C(Cl)C(Cl)C(Cl)Br H298:-10.34 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)CCl smiles:OC(Br)=C(Cl)CCl H298:-43.32 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)OBr smiles:C=C(Cl)C(Cl)OBr H298:-8.81 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)C(Br)Br smiles:C=C(Cl)C(Cl)C(Br)Br H298:1.08 kcal/mol
""",
)

entry(
    index = 10,
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
        Cpdata = ([-0.143088,-0.103202,0.0161273,-0.00344065,-0.0986115,-0.130257,0.110146],'cal/(mol*K)','+|-',[0.199631,0.229435,0.234539,0.231098,0.200393,0.172837,0.140858]),
        H298 = (0.0446388,'kcal/mol','+|-',0.711667),
        S298 = (-0.247106,'cal/(mol*K)','+|-',0.485044),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DC(Cl)Cl smiles:ClC=C(Cl)C(Cl)=C(Cl)Cl H298:1.13 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(DC)Cl smiles:C=C(Cl)C(=C)Cl H298:12.44 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)DCCl smiles:C=C(Cl)C(Cl)=CCl H298:7.20 kcal/mol
library:CHOCl_G4 label:ClCDC(Cl)C(Cl)DCCl smiles:ClC=C(Cl)C(Cl)=CCl H298:2.21 kcal/mol
library:CHOCl_G4 label:ClC(Cl)DC(Cl)C(Cl)DC(Cl)Cl smiles:ClC(Cl)=C(Cl)C(Cl)=C(Cl)Cl H298:-3.12 kcal/mol
library:CHOCl_G4 label:CDC(Cl)C(Cl)DC(Cl)Cl smiles:C=C(Cl)C(Cl)=C(Cl)Cl H298:6.79 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(Cl)DCF smiles:C=C(Cl)C(Cl)=CF H298:-29.76 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DC(Cl)Br smiles:C=C(Cl)C(Cl)=C(Cl)Br H298:18.38 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DCBr smiles:C=C(Cl)C(Cl)=CBr H298:19.00 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DC(Br)Br smiles:C=C(Cl)C(Cl)=C(Br)Br H298:30.14 kcal/mol
""",
)

entry(
    index = 11,
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
        Cpdata = ([0.275328,0.248766,0.186314,0.14346,0.0567248,0.00969829,-0.0904599],'cal/(mol*K)','+|-',[0.0687438,0.079007,0.0807645,0.0795796,0.0690062,0.0595173,0.0485052]),
        H298 = (1.36086,'kcal/mol','+|-',0.245066),
        S298 = (-0.0401011,'cal/(mol*K)','+|-',0.167027),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClCDCCl smiles:ClC=CCl H298:-0.09 kcal/mol
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
library:CHOClBr_G4 label:ClCDC(Cl)CCBr smiles:ClC=C(Cl)CCBr H298:-10.09 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)OCBr smiles:ClC=C(Cl)OCBr H298:-30.95 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CDCBr smiles:ClC=C(Cl)C=CBr H298:18.49 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Cl)CBr smiles:CC(Cl)=C(Cl)CBr H298:-13.27 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)DCCl smiles:OC(Br)C(Cl)=CCl H298:-40.93 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CBr smiles:ClC=C(Cl)CBr H298:-2.39 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)DCCl smiles:C=C(Br)C(Cl)=CCl H298:19.31 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Br)Br smiles:ClC=C(Cl)C(Br)Br H298:6.43 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)DCCl smiles:O=C(Br)C(Cl)=CCl H298:-28.22 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)OBr smiles:ClC=C(Cl)OBr H298:-0.22 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)DCCl smiles:CC(Br)C(Cl)=CCl H298:-10.86 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)DCCl smiles:CC(Br)(Br)C(Cl)=CCl H298:-2.44 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Cl)OBr smiles:CC(Cl)=C(Cl)OBr H298:-10.74 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Cl)Br smiles:ClC=C(Cl)C(Cl)Br H298:-4.68 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)OOBr smiles:ClC=C(Cl)OOBr H298:15.83 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)COBr smiles:ClC=C(Cl)COBr H298:-6.41 kcal/mol
""",
)

entry(
    index = 12,
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
        Cpdata = ([0.808793,0.68909,0.477174,0.340111,0.0580189,-0.0518429,-0.180425],'cal/(mol*K)','+|-',[0.169171,0.194428,0.198753,0.195837,0.169817,0.146466,0.119366]),
        H298 = (4.48625,'kcal/mol','+|-',0.603081),
        S298 = (-0.0854678,'cal/(mol*K)','+|-',0.411036),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOCl_G4 label:ClCDC(Cl)Cl smiles:ClC=C(Cl)Cl H298:-3.61 kcal/mol
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
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)CBr smiles:ClC(Cl)=C(Cl)CBr H298:-5.92 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)DC(Cl)Cl smiles:C=C(Br)C(Cl)=C(Cl)Cl H298:18.22 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)OBr smiles:ClC(Cl)=C(Cl)OBr H298:-3.03 kcal/mol
""",
)

entry(
    index = 13,
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
        Cpdata = ([0.481327,0.388344,0.196757,0.1248,-0.0466784,-0.169316,-0.413763],'cal/(mol*K)','+|-',[0.425606,0.489148,0.500029,0.492693,0.427231,0.368483,0.300305]),
        H298 = (2.30214,'kcal/mol','+|-',1.51725),
        S298 = (-0.714443,'cal/(mol*K)','+|-',1.0341),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOCl_G4 label:ClC(Cl)DC(Cl)Cl smiles:ClC(Cl)=C(Cl)Cl H298:-6.15 kcal/mol
""",
)

entry(
    index = 14,
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
    index = 15,
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
    index = 16,
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
    index = 17,
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
    index = 18,
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
    index = 19,
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
    index = 20,
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
    index = 21,
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
    index = 22,
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
    index = 23,
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
    index = 24,
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
    index = 25,
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
    index = 26,
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
    index = 27,
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
    index = 28,
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
    index = 29,
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
    index = 30,
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
    index = 31,
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
    index = 32,
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
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
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
    index = 45,
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
    index = 46,
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
    index = 47,
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
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 51,
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
    index = 52,
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
    index = 53,
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

entry(
    index = 54,
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
    index = 55,
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
        Cpdata = ([-0.0259703,0.145361,0.228419,0.264736,0.272031,0.260902,0.386662],'cal/(mol*K)','+|-',[0.194594,0.223646,0.228621,0.225267,0.195337,0.168476,0.137305]),
        H298 = (4.00851,'kcal/mol','+|-',0.693711),
        S298 = (0.213049,'cal/(mol*K)','+|-',0.472806),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:FC(F)(F)C(F)(F)Br smiles:FC(F)(F)C(F)(F)Br H298:-257.37 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)(Br)Br smiles:FC(F)(Br)C(Br)(Br)Br H298:-80.93 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)(Br)Br smiles:FC(F)(F)C(Br)(Br)Br H298:-144.62 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)(Br)Br smiles:FC(Br)(Br)C(Br)(Br)Br H298:-21.72 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(F)(Br)Br smiles:FC(F)(F)C(F)(Br)Br H298:-198.32 kcal/mol
""",
)

entry(
    index = 56,
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
        Cpdata = ([0.120285,0.291299,0.303352,0.332491,0.374215,0.363645,0.297872],'cal/(mol*K)','+|-',[0.424188,0.487518,0.498363,0.491051,0.425808,0.367255,0.299305]),
        H298 = (5.51679,'kcal/mol','+|-',1.5122),
        S298 = (-0.927557,'cal/(mol*K)','+|-',1.03065),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC(F)(F)C(F)(F)F smiles:FC(F)(F)C(F)(F)F H298:-321.37 kcal/mol
""",
)

entry(
    index = 57,
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
    index = 58,
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
        Cpdata = ([-0.641264,-0.611657,-0.463313,-0.410666,-0.367564,-0.278016,0.26121],'cal/(mol*K)','+|-',[0.12587,0.144662,0.14788,0.145711,0.126351,0.108977,0.0888134]),
        H298 = (4.63192,'kcal/mol','+|-',0.448717),
        S298 = (1.83946,'cal/(mol*K)','+|-',0.305828),
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
library:CHOFClBr_G4 label:FC(Cl)C(Cl)(Br)Br smiles:FC(Cl)C(Cl)(Br)Br H298:-56.51 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)(Br)Br smiles:FC(F)C(Cl)(Br)Br H298:-101.77 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(F)(Cl)Br smiles:CC(Br)(Br)C(F)(Cl)Br H298:-56.60 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Br)C(Br)Br smiles:FC(Cl)(Br)C(Br)Br H298:-46.72 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)(Cl)Br smiles:FC(F)C(Cl)(Cl)Br H298:-113.63 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)(Cl)Br smiles:FC(Cl)C(Cl)(Cl)Br H298:-68.27 kcal/mol
library:CHOFClBr_G4 label:FC(F)(F)C(Cl)Br smiles:FC(F)(F)C(Cl)Br H298:-168.43 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)C(Cl)Br smiles:FC(F)(Cl)C(Cl)Br H298:-118.09 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(F)(F)Cl smiles:CC(Br)(Br)C(F)(F)Cl H298:-116.84 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(F)(Cl)Br smiles:FC(F)C(F)(Cl)Br H298:-156.05 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)C(Cl)Br smiles:FC(Cl)(Cl)C(Cl)Br H298:-70.89 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)(Br)Br smiles:FC(Cl)C(Br)(Br)Br H298:-44.77 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(F)(Cl)Cl smiles:CC(Br)(Br)C(F)(Cl)Cl H298:-69.25 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)C(Br)Br smiles:FC(Cl)(Cl)C(Br)Br H298:-59.34 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)C(Br)Br smiles:FC(F)(Cl)C(Br)Br H298:-106.33 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)(F)F smiles:OC(Br)(Br)C(F)(F)F H298:-196.37 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)(Br)Br smiles:CC(F)(Br)C(Br)(Br)Br H298:-42.92 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(F)(F)F smiles:FC(Br)C(F)(F)F H298:-208.43 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)(F)Br smiles:OC(Br)(Br)C(F)(F)Br H298:-132.83 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)(Br)Br smiles:OC(Br)(Br)C(F)(Br)Br H298:-73.60 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)(Br)Br smiles:CC(Br)(Br)C(F)(Br)Br H298:-43.79 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)(Br)Br smiles:CC(F)(F)C(Br)(Br)Br H298:-102.14 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)(F)Br smiles:CC(F)(F)C(F)(F)Br H298:-215.97 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)(F)Br smiles:CC(Br)(Br)C(F)(F)Br H298:-103.36 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)Br smiles:FC(F)(Br)C(Br)Br H298:-92.95 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)Br smiles:FC(Br)C(Br)(Br)Br H298:-32.25 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)Br smiles:FC(F)C(F)(F)Br H298:-202.33 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)Br smiles:FC(Br)(Br)C(Br)Br H298:-34.14 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)Br smiles:FC(F)C(Br)(Br)Br H298:-90.02 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)(F)F smiles:OC(F)(Br)C(F)(F)F H298:-254.51 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)(Br)Br smiles:CC(F)(F)C(F)(Br)Br H298:-156.39 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)Br smiles:FC(F)C(F)(Br)Br H298:-143.45 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)Br smiles:FC(F)(F)C(Br)Br H298:-156.89 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)(F)F smiles:CC(Br)(Br)C(F)(F)F H298:-167.46 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)(F)F smiles:CC(F)(Br)C(F)(F)F H298:-220.86 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Cl)C(Br)Br smiles:ClC(Cl)(Cl)C(Br)Br H298:-15.65 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)(Cl)Cl smiles:CC(Br)(Br)C(Cl)(Cl)Cl H298:-25.16 kcal/mol
library:CHOClBr_G4 label:ClC(Br)(Br)C(Br)Br smiles:ClC(Br)(Br)C(Br)Br H298:8.01 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)(Br)Br smiles:ClC(Cl)C(Br)(Br)Br H298:-3.43 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)(Br)Br smiles:CC(Br)(Br)C(Cl)(Br)Br H298:-1.28 kcal/mol
library:CHOClBr_G4 label:ClC(Br)C(Cl)(Cl)Cl smiles:ClC(Br)C(Cl)(Cl)Cl H298:-27.18 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Br)C(Br)Br smiles:ClC(Cl)(Br)C(Br)Br H298:-3.76 kcal/mol
library:CHOClBr_G4 label:ClC(Br)C(Br)(Br)Br smiles:ClC(Br)C(Br)(Br)Br H298:8.10 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)(Cl)Br smiles:ClC(Cl)C(Cl)(Cl)Br H298:-27.03 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)(Br)Br smiles:ClC(Cl)C(Cl)(Br)Br H298:-15.17 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)(Cl)Br smiles:CC(Br)(Br)C(Cl)(Cl)Br H298:-13.23 kcal/mol
""",
)

entry(
    index = 59,
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
        Cpdata = ([-0.227608,-0.224725,-0.105533,-0.0413895,-0.021153,0.0368277,0.363019],'cal/(mol*K)','+|-',[0.162497,0.186757,0.190911,0.18811,0.163117,0.140687,0.114657]),
        H298 = (10.1314,'kcal/mol','+|-',0.579287),
        S298 = (1.73408,'cal/(mol*K)','+|-',0.394819),
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
    index = 60,
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
        Cpdata = ([-0.174914,-0.468033,-0.577286,-0.695076,-0.868638,-0.895252,-0.406172],'cal/(mol*K)','+|-',[0.840736,0.966255,0.987749,0.973258,0.843946,0.727896,0.593219]),
        H298 = (5.01486,'kcal/mol','+|-',2.99715),
        S298 = (2.35415,'cal/(mol*K)','+|-',2.04274),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC(Br)C(Br)(Br)Br smiles:BrC(Br)C(Br)(Br)Br H298:19.72 kcal/mol
""",
)

entry(
    index = 61,
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
    index = 62,
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
        Cpdata = ([-0.272434,-0.28022,-0.208647,-0.165339,-0.112686,-0.0594042,0.277132],'cal/(mol*K)','+|-',[0.0941099,0.10816,0.110566,0.108944,0.0944692,0.0814789,0.0664035]),
        H298 = (2.92929,'kcal/mol','+|-',0.335494),
        S298 = (1.94606,'cal/(mol*K)','+|-',0.228659),
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
library:CHOFClBr_G4 label:CC(F)C(Cl)(Cl)Br smiles:CC(F)C(Cl)(Cl)Br H298:-73.45 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)CBr smiles:FC(F)(Cl)CBr H298:-117.44 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Br)CBr smiles:FC(Cl)(Br)CBr H298:-57.11 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)(Cl)Br smiles:OC(Br)C(F)(Cl)Br H298:-96.19 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)C(F)(Cl)Br smiles:C=CC(F)C(F)(Cl)Br H298:-89.37 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Cl)CBr smiles:FC(Cl)(Cl)CBr H298:-70.04 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)(Cl)Cl smiles:CC(Br)C(F)(Cl)Cl H298:-78.39 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)(Br)Br smiles:CC(F)C(Cl)(Br)Br H298:-61.54 kcal/mol
library:CHOFClBr_G4 label:FCC(F)(Cl)Br smiles:FCC(F)(Cl)Br H298:-106.32 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)(F)Cl smiles:OC(Br)C(F)(F)Cl H298:-155.81 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)(F)Cl smiles:CC(Br)C(F)(F)Cl H298:-125.92 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)(Cl)Br smiles:CC(Br)C(F)(Cl)Br H298:-65.69 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)(Cl)Cl smiles:OC(Br)C(F)(Cl)Cl H298:-108.73 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Br)Br smiles:FCC(Cl)(Br)Br H298:-51.70 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)C(Cl)(Cl)Br smiles:C#CC(F)C(Cl)(Cl)Br H298:-1.03 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)C(Cl)(Br)Br smiles:C=CC(F)C(Cl)(Br)Br H298:-34.60 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(F)(Cl)Br smiles:CC(F)C(F)(Cl)Br H298:-116.58 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)C(Cl)(Br)Br smiles:C#CC(F)C(Cl)(Br)Br H298:10.78 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)C(Cl)(Cl)Br smiles:C=CC(F)C(Cl)(Cl)Br H298:-46.46 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Cl)Br smiles:FCC(Cl)(Cl)Br H298:-63.59 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)C(F)(Cl)Br smiles:C#CC(F)C(F)(Cl)Br H298:-43.99 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(Br)(Br)Br smiles:C=CC(F)C(Br)(Br)Br H298:-22.75 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)Br smiles:FCC(Br)(Br)Br H298:-39.87 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)Br smiles:FCC(F)(Br)Br H298:-93.72 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)OBr smiles:FC(F)(F)C(Br)OBr H298:-165.05 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)CBr smiles:FC(Br)(Br)C(Br)CBr H298:-45.15 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(F)(F)Br smiles:CC(C)(F)C(F)(F)Br H298:-174.05 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)(Br)Br smiles:FCC(F)C(Br)(Br)Br H298:-89.47 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)(F)F smiles:OC(O)(Br)C(F)(F)F H298:-250.33 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)(F)Br smiles:CC(C)(Br)C(F)(F)Br H298:-121.54 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)(F)Br smiles:OC(O)(Br)C(F)(F)Br H298:-186.73 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)(Br)Br smiles:CCC(Br)C(F)(Br)Br H298:-58.65 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)CBr smiles:FC(F)(Br)C(Br)CBr H298:-103.92 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(F)(Br)Br smiles:C=CC(F)C(F)(Br)Br H298:-76.98 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)Br smiles:OC(Br)C(F)(Br)Br H298:-83.72 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(Br)Br smiles:FCC(F)C(F)(Br)Br H298:-143.49 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)(F)F smiles:COC(Br)C(F)(F)F H298:-201.85 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(Br)(Br)Br smiles:CC(C)(F)C(Br)(Br)Br H298:-59.08 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(Br)(Br)Br smiles:CCC(F)C(Br)(Br)Br H298:-54.77 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)(F)F smiles:OCC(Br)C(F)(F)F H298:-210.65 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)(F)Br smiles:OCC(Br)C(F)(F)Br H298:-146.32 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)(F)Br smiles:COC(Br)C(F)(F)Br H298:-138.16 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)(Br)Br smiles:CC(C)(Br)C(F)(Br)Br H298:-61.57 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(F)(Br)Br smiles:CC(O)(F)C(F)(Br)Br H298:-152.56 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(F)Br smiles:FCC(F)C(F)(F)Br H298:-202.74 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)(Br)Br smiles:OCC(Br)C(F)(Br)Br H298:-86.72 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)CBr smiles:FC(F)(F)CBr H298:-168.24 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(F)(F)Br smiles:CCC(F)C(F)(F)Br H298:-168.13 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)(F)F smiles:CC(O)(Br)C(F)(F)F H298:-217.60 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)Br smiles:CC(Br)C(F)(F)Br H298:-112.41 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(F)(Br)Br smiles:CCC(F)C(F)(Br)Br H298:-108.59 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)CBr smiles:FC(F)(Br)CBr H298:-104.14 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(Br)(Br)Br smiles:C#CC(F)C(Br)(Br)Br H298:22.57 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)F smiles:CC(Br)C(F)(F)F H298:-176.74 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)F smiles:OC(Br)C(F)(F)F H298:-205.72 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)Br smiles:OC(Br)C(F)(F)Br H298:-142.59 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(F)(Br)Br smiles:C#CC(F)C(F)(Br)Br H298:-31.13 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(F)(F)Br smiles:C=CC(F)C(F)(F)Br H298:-136.32 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)(Br)Br smiles:OC(O)(Br)C(F)(Br)Br H298:-127.83 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(F)(F)Br smiles:C#CC(F)C(F)(F)Br H298:-89.99 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)(F)F smiles:CC(C)(Br)C(F)(F)F H298:-186.06 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(F)(Br)Br smiles:CC(C)(F)C(F)(Br)Br H298:-114.04 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)(Br)Br smiles:OOC(Br)C(F)(Br)Br H298:-62.29 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)CBr smiles:FC(Br)(Br)CBr H298:-44.76 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(Br)Br smiles:CC(Br)C(F)(Br)Br H298:-53.14 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(Br)(Br)Br smiles:CC(O)(F)C(Br)(Br)Br H298:-98.15 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)(F)F smiles:OOC(Br)C(F)(F)F H298:-184.57 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)(Br)Br smiles:COC(Br)C(F)(Br)Br H298:-79.68 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)(Br)Br smiles:CC(O)(Br)C(F)(Br)Br H298:-94.55 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)Br smiles:FCC(F)(F)Br H298:-152.82 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)(F)Br smiles:OOC(Br)C(F)(F)Br H298:-120.82 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)(F)F smiles:CCC(Br)C(F)(F)F H298:-181.82 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)OBr smiles:FC(F)(Br)C(Br)OBr H298:-101.62 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)Br smiles:CC(F)C(Br)(Br)Br H298:-49.65 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)(F)Br smiles:CCC(Br)C(F)(F)Br H298:-117.86 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(Br)Br smiles:CC(F)C(F)(Br)Br H298:-103.85 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)Br smiles:O=CC(Br)C(F)(F)Br H298:-125.99 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(F)(F)Br smiles:CC(O)(F)C(F)(F)Br H298:-212.13 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(Br)Br smiles:O=CC(Br)C(F)(Br)Br H298:-66.91 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)Br smiles:CC(F)C(F)(F)Br H298:-163.28 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)F smiles:O=CC(Br)C(F)(F)F H298:-189.44 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)OBr smiles:FC(Br)(Br)C(Br)OBr H298:-43.29 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)CBr smiles:FC(F)(F)C(Br)CBr H298:-167.92 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)(F)Br smiles:CC(O)(Br)C(F)(F)Br H298:-154.12 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)Br smiles:ClCC(Cl)(Cl)Br H298:-25.50 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)(Cl)Cl smiles:OC(Br)C(Cl)(Cl)Cl H298:-65.30 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Cl)(Br)Br smiles:C=CC(Cl)C(Cl)(Br)Br H298:4.16 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Cl)(Br)Br smiles:C#CC(Cl)C(Cl)(Br)Br H298:49.53 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)(Br)Br smiles:CC(Cl)C(Cl)(Br)Br H298:-21.84 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)(Cl)Br smiles:CC(Cl)C(Cl)(Cl)Br H298:-33.70 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Cl)(Cl)Br smiles:C#CC(Cl)C(Cl)(Cl)Br H298:37.81 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Br)Br smiles:ClCC(Cl)(Br)Br H298:-13.61 kcal/mol
library:CHOClBr_G4 label:ClC(Br)(Br)CBr smiles:ClC(Br)(Br)CBr H298:-2.48 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Cl)(Cl)Br smiles:C=CC(Cl)C(Cl)(Cl)Br H298:-7.53 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)(Cl)Cl smiles:CC(Br)C(Cl)(Cl)Cl H298:-34.24 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)(Cl)Br smiles:CC(Br)C(Cl)(Cl)Br H298:-22.21 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Cl)CBr smiles:ClC(Cl)(Cl)CBr H298:-26.25 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)(Br)Br smiles:OC(Br)C(Cl)(Br)Br H298:-41.68 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)(Br)Br smiles:CC(Cl)C(Br)(Br)Br H298:-9.93 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Br)(Br)Br smiles:C#CC(Cl)C(Br)(Br)Br H298:61.38 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Br)(Br)Br smiles:C=CC(Cl)C(Br)(Br)Br H298:15.98 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)Br smiles:ClCC(Br)(Br)Br H298:-1.82 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)(Br)Br smiles:CC(Br)C(Cl)(Br)Br H298:-10.42 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Br)CBr smiles:ClC(Cl)(Br)CBr H298:-14.33 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)(Cl)Br smiles:OC(Br)C(Cl)(Cl)Br H298:-53.43 kcal/mol
""",
)

entry(
    index = 63,
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
        Cpdata = ([0.0765787,0.195496,0.229714,0.210363,0.151387,0.122269,0.252817],'cal/(mol*K)','+|-',[0.129835,0.149219,0.152538,0.1503,0.130331,0.112409,0.091611]),
        H298 = (6.64698,'kcal/mol','+|-',0.462851),
        S298 = (1.38455,'cal/(mol*K)','+|-',0.315461),
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
library:CHOFBr_G4 label:FC(CBr)C(F)(F)F smiles:FC(CBr)C(F)(F)F H298:-218.22 kcal/mol
library:CHOFBr_G4 label:FC(OBr)C(F)(F)F smiles:FC(OBr)C(F)(F)F H298:-220.63 kcal/mol
""",
)

entry(
    index = 64,
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
        Cpdata = ([-0.468657,-0.616864,-0.632656,-0.67907,-0.720854,-0.606538,0.0468072],'cal/(mol*K)','+|-',[0.322397,0.37053,0.378773,0.373216,0.323628,0.279127,0.227482]),
        H298 = (3.36394,'kcal/mol','+|-',1.14932),
        S298 = (1.47743,'cal/(mol*K)','+|-',0.783331),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCC(Br)(Br)Br smiles:BrCC(Br)(Br)Br H298:9.29 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)(Br)Br smiles:OC(Br)C(Br)(Br)Br H298:-29.94 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)(Br)Br smiles:CC(Br)C(Br)(Br)Br H298:1.46 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)(Br)Br smiles:BrCC(Br)C(Br)(Br)Br H298:9.04 kcal/mol
library:CHOBr_G4 label:COC(Br)C(Br)(Br)Br smiles:COC(Br)C(Br)(Br)Br H298:-25.77 kcal/mol
library:CHOBr_G4 label:CCC(Br)C(Br)(Br)Br smiles:CCC(Br)C(Br)(Br)Br H298:-4.07 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C(Br)(Br)Br smiles:BrOC(Br)C(Br)(Br)Br H298:10.31 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)(Br)Br smiles:FCC(Br)C(Br)(Br)Br H298:-38.66 kcal/mol
""",
)

entry(
    index = 65,
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
        Cpdata = ([0.0473653,0.373771,0.469393,0.502914,0.486225,0.452641,0.477837],'cal/(mol*K)','+|-',[0.162985,0.187318,0.191484,0.188675,0.163607,0.141109,0.115001]),
        H298 = (4.68074,'kcal/mol','+|-',0.581026),
        S298 = (1.5466,'cal/(mol*K)','+|-',0.396004),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(F)C(F)(F)Cl smiles:C=C(F)C(F)(F)Cl H298:-142.24 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(F)(Cl)Cl smiles:C=C(F)C(F)(Cl)Cl H298:-95.11 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(Cl)(Cl)Cl smiles:C=C(F)C(Cl)(Cl)Cl H298:-50.75 kcal/mol
library:CHOFClBr_G4 label:CDCDC(F)C(Cl)(Br)Br smiles:C=C=C(F)C(Cl)(Br)Br H298:11.05 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Br)Br smiles:C=C(F)C(Cl)(Br)Br H298:-27.23 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Cl)Br smiles:C=C(F)C(Cl)(Cl)Br H298:-38.98 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)(Cl)Br smiles:C=C(F)C(F)(Cl)Br H298:-82.63 kcal/mol
library:CHOFClBr_G4 label:CDCDC(F)C(Cl)(Cl)Br smiles:C=C=C(F)C(Cl)(Cl)Br H298:-0.47 kcal/mol
library:CHOFClBr_G4 label:CDCDC(F)C(F)(Cl)Br smiles:C=C=C(F)C(F)(Cl)Br H298:-43.51 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(Br)(Br)Br smiles:CC=C(F)C(Br)(Br)Br H298:-23.82 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)(Br)Br smiles:FC=C(F)C(Br)(Br)Br H298:-54.64 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)Br smiles:C=C(F)C(F)(Br)Br H298:-70.28 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)(Br)Br smiles:CC=C(Br)C(F)(Br)Br H298:-28.54 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(F)(F)Br smiles:CC=C(F)C(F)(F)Br H298:-137.20 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)Br smiles:OC=C(Br)C(F)(F)Br H298:-122.08 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)F smiles:OC=C(Br)C(F)(F)F H298:-186.35 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)(F)Br smiles:CC=C(Br)C(F)(F)Br H298:-87.61 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(F)Br smiles:FC=C(F)C(F)(F)Br H298:-167.73 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(F)(F)Br smiles:C=C=C(F)C(F)(F)Br H298:-89.60 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)(F)F smiles:O=C=C(Br)C(F)(F)F H298:-156.64 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)Br smiles:C=C(F)C(F)(F)Br H298:-128.93 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)Br smiles:C=C(F)C(Br)(Br)Br H298:-15.40 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)(F)Br smiles:O=C=C(Br)C(F)(F)Br H298:-93.21 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(Br)(Br)Br smiles:C=C=C(F)C(Br)(Br)Br H298:22.89 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)(F)F smiles:CC=C(Br)C(F)(F)F H298:-151.58 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(F)(Br)Br smiles:C=C=C(F)C(F)(Br)Br H298:-30.84 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(Br)Br smiles:FC=C(F)C(F)(Br)Br H298:-108.92 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)(Br)Br smiles:O=C=C(Br)C(F)(Br)Br H298:-34.34 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(F)(Br)Br smiles:CC=C(F)C(F)(Br)Br H298:-78.52 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(Br)Br smiles:OC=C(Br)C(F)(Br)Br H298:-62.88 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Br)Br smiles:C=C(Cl)C(Cl)(Br)Br H298:11.93 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Br)(Br)Br smiles:C=C=C(Cl)C(Br)(Br)Br H298:59.05 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Cl)Br smiles:C=C(Cl)C(Cl)(Cl)Br H298:0.10 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)(Br)Br smiles:C=C(Cl)C(Br)(Br)Br H298:23.78 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Cl)(Cl)Br smiles:C=C=C(Cl)C(Cl)(Cl)Br H298:35.64 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Cl)(Br)Br smiles:C=C=C(Cl)C(Cl)(Br)Br H298:47.24 kcal/mol
""",
)

entry(
    index = 66,
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
        Cpdata = ([-0.143786,-0.0464458,-0.0301482,-0.0290795,0.0102118,0.0731887,0.186089],'cal/(mol*K)','+|-',[0.238741,0.274385,0.280488,0.276373,0.239653,0.206699,0.168455]),
        H298 = (6.2676,'kcal/mol','+|-',0.851093),
        S298 = (1.75859,'cal/(mol*K)','+|-',0.580071),
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
library:CHOF_G4 label:OCDC(F)C(F)(F)F smiles:OC=C(F)C(F)(F)F H298:-232.26 kcal/mol
library:CHOF_G4 label:OC(F)DC(F)C(F)(F)F smiles:OC(F)=C(F)C(F)(F)F H298:-274.97 kcal/mol
library:CHOF_G4 label:CDC(F)C(F)(F)F smiles:C=C(F)C(F)(F)F H298:-192.87 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)C(F)(F)F smiles:FOC(F)=C(F)C(F)(F)F H298:-238.81 kcal/mol
""",
)

entry(
    index = 67,
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
        Cpdata = ([0.0440436,0.466065,0.580598,0.605073,0.553519,0.469747,0.238252],'cal/(mol*K)','+|-',[0.614817,0.706607,0.722326,0.711729,0.617165,0.532299,0.433812]),
        H298 = (3.94376,'kcal/mol','+|-',2.19177),
        S298 = (1.81077,'cal/(mol*K)','+|-',1.49382),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(Br)C(Br)(Br)Br smiles:C=C(Br)C(Br)(Br)Br H298:35.68 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)(Br)Br smiles:FC=C(Br)C(Br)(Br)Br H298:-6.67 kcal/mol
""",
)

entry(
    index = 68,
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
        Cpdata = ([-0.287996,-0.400491,-0.353923,-0.331456,-0.281032,-0.201107,0.0592729],'cal/(mol*K)','+|-',[0.0499868,0.0574497,0.0587276,0.0578661,0.0501777,0.0432778,0.0352704]),
        H298 = (1.88891,'kcal/mol','+|-',0.178199),
        S298 = (1.11734,'cal/(mol*K)','+|-',0.121453),
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
library:CHOFClBr_G4 label:CC(Cl)(Br)C(F)Cl smiles:CC(Cl)(Br)C(F)Cl H298:-78.09 kcal/mol
library:CHOFClBr_G4 label:OC(Br)(Br)C(F)Cl smiles:OC(Br)(Br)C(F)Cl H298:-96.26 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)(Cl)C(Cl)Br smiles:C=CC(F)(Cl)C(Cl)Br H298:-51.57 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)(Cl)C(Br)Br smiles:C#CC(F)(Cl)C(Br)Br H298:7.45 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)Br smiles:FC(Cl)C(Cl)Br H298:-67.23 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)C(F)F smiles:CC(Cl)(Br)C(F)F H298:-123.48 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)Br smiles:FC(F)C(Cl)Br H298:-113.15 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)(F)C(Cl)Br smiles:C=CC(F)(F)C(Cl)Br H298:-97.05 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)Br smiles:FC(Cl)C(Br)Br H298:-55.60 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)(Cl)C(Br)Br smiles:C=CC(F)(Cl)C(Br)Br H298:-40.13 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)(Cl)C(Cl)Br smiles:C#CC(F)(Cl)C(Cl)Br H298:-3.97 kcal/mol
library:CHOFClBr_G4 label:CC(F)(F)C(Cl)Br smiles:CC(F)(F)C(Cl)Br H298:-125.49 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(Br)Br smiles:CC(F)(Cl)C(Br)Br H298:-67.57 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)(F)C(Cl)Br smiles:C#CC(F)(F)C(Cl)Br H298:-49.49 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(Cl)Br smiles:CC(F)(Cl)C(Cl)Br H298:-79.11 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)C(F)Cl smiles:OC(Cl)(Br)C(F)Cl H298:-108.53 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(F)Cl smiles:CC(Br)(Br)C(F)Cl H298:-66.26 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)C(F)F smiles:OC(Cl)(Br)C(F)F H298:-153.74 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(Br)Br smiles:FCC(F)(F)C(Br)Br H298:-152.82 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(F)C(Br)Br smiles:C=CC(F)(F)C(Br)Br H298:-85.19 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)Br smiles:CC(Br)(Br)C(F)Br H298:-53.75 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)C(F)F smiles:OOC(Br)(Br)C(F)F H298:-119.44 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)Br smiles:FC(F)C(F)Br H298:-152.49 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)C(F)F smiles:CCC(Br)(Br)C(F)F H298:-116.99 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)OBr smiles:FC(Br)C(Br)(Br)OBr H298:-43.90 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)C(F)Br smiles:COC(Br)(Br)C(F)Br H298:-81.83 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)Br smiles:O=CC(Br)(Br)C(F)Br H298:-67.07 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)Br smiles:CC(F)(Br)C(Br)Br H298:-55.00 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)F smiles:O=CC(Br)(Br)C(F)F H298:-124.54 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)Br smiles:FC(F)C(Br)Br H298:-100.93 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(O)(Br)Br smiles:CC(F)(F)C(O)(Br)Br H298:-154.31 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)F smiles:CC(F)(Br)C(F)F H298:-165.00 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)OBr smiles:FC(F)C(Br)(Br)OBr H298:-101.32 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)Br smiles:CC(F)(F)C(F)Br H298:-165.88 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)F smiles:OC(Br)(Br)C(F)F H298:-141.48 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(C)(Br)Br smiles:CC(F)(Br)C(C)(Br)Br H298:-64.63 kcal/mol
library:CHOFBr_G4 label:CCC(F)(F)C(Br)Br smiles:CCC(F)(F)C(Br)Br H298:-118.17 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)C(F)Br smiles:C#CC(F)(F)C(F)Br H298:-89.12 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(F)C(F)Br smiles:C=CC(F)(F)C(F)Br H298:-136.80 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)OBr smiles:FC(F)C(F)(Br)OBr H298:-157.76 kcal/mol
library:CHOFBr_G4 label:COC(F)(Br)C(F)F smiles:COC(F)(Br)C(F)F H298:-195.67 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)C(F)Br smiles:OOC(Br)(Br)C(F)Br H298:-62.09 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)C(F)F smiles:OCC(F)(Br)C(F)F H298:-198.70 kcal/mol
library:CHOFBr_G4 label:OOC(F)(Br)C(F)F smiles:OOC(F)(Br)C(F)F H298:-175.80 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)C(F)Br smiles:OCC(Br)(Br)C(F)Br H298:-90.08 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(C)(F)Br smiles:CC(F)(F)C(C)(F)Br H298:-177.96 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(C)(Br)Br smiles:CC(F)(F)C(C)(Br)Br H298:-123.92 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(F)Br smiles:FCC(F)(F)C(F)Br H298:-204.60 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(Br)C(Br)Br smiles:C#CC(F)(Br)C(Br)Br H298:19.77 kcal/mol
library:CHOFBr_G4 label:CCC(F)(F)C(F)Br smiles:CCC(F)(F)C(F)Br H298:-170.54 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)C(F)F smiles:CCC(F)(Br)C(F)F H298:-169.92 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(O)(F)Br smiles:OC(F)(F)C(O)(F)Br H298:-249.84 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)CBr smiles:FC(F)C(F)(Br)CBr H298:-154.71 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)C(Br)Br smiles:C#CC(F)(F)C(Br)Br H298:-37.74 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)F smiles:CC(Br)(Br)C(F)F H298:-111.67 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(O)(Br)Br smiles:OC(F)(Br)C(O)(Br)Br H298:-128.92 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)C(F)F smiles:O=CC(F)(Br)C(F)F H298:-174.88 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)CBr smiles:FC(F)C(Br)(Br)CBr H298:-103.62 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)C(Br)Br smiles:CCC(F)(Br)C(Br)Br H298:-60.28 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)F smiles:OC(F)(Br)C(F)F H298:-199.34 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(O)(Br)Br smiles:OC(F)(F)C(O)(Br)Br H298:-191.80 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(O)(F)Br smiles:CC(F)(F)C(O)(F)Br H298:-212.77 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)C(Br)Br smiles:FCC(F)(Br)C(Br)Br H298:-94.18 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)CBr smiles:FC(Br)C(Br)(Br)CBr H298:-46.71 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)Br smiles:CC(F)(F)C(Br)Br H298:-113.82 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)C(F)F smiles:OCC(Br)(Br)C(F)F H298:-147.69 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)Br smiles:FC(Br)C(Br)Br H298:-43.24 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(O)(Br)Br smiles:CC(F)(Br)C(O)(Br)Br H298:-95.05 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(Br)C(Br)Br smiles:C=CC(F)(Br)C(Br)Br H298:-27.56 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)C(F)Br smiles:CCC(Br)(Br)C(F)Br H298:-59.24 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)Br smiles:OC(Br)(Br)C(F)Br H298:-83.82 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)C(F)F smiles:COC(Br)(Br)C(F)F H298:-139.03 kcal/mol
library:CHOClBr_G4 label:ClC(Br)C(Br)Br smiles:ClC(Br)C(Br)Br H298:-3.18 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)Cl smiles:CC(Br)(Br)C(Cl)Cl H298:-24.22 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)C(Cl)Cl smiles:OC(Br)(Br)C(Cl)Cl H298:-54.98 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Br)C(Br)Br smiles:C=CC(Cl)(Br)C(Br)Br H298:14.50 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Br)C(Br)Br smiles:C#CC(Cl)(Br)C(Br)Br H298:60.40 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(Br)Br smiles:CC(Cl)(Br)C(Br)Br H298:-13.19 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)C(Cl)Cl smiles:OC(Cl)(Br)C(Cl)Cl H298:-67.26 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Cl)C(Cl)Br smiles:C#CC(Cl)(Cl)C(Cl)Br H298:37.78 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(Cl)Br smiles:CC(Cl)(Cl)C(Cl)Br H298:-36.57 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Cl)C(Cl)Br smiles:C=CC(Cl)(Cl)C(Cl)Br H298:-8.91 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)C(Cl)Br smiles:OC(Br)(Br)C(Cl)Br H298:-43.39 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)Br smiles:ClC(Cl)C(Br)Br H298:-14.60 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)Br smiles:CC(Br)(Br)C(Cl)Br H298:-13.01 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Cl)C(Br)Br smiles:C=CC(Cl)(Cl)C(Br)Br H298:2.59 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)Br smiles:ClC(Cl)C(Cl)Br H298:-26.12 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(Br)Br smiles:CC(Cl)(Cl)C(Br)Br H298:-24.98 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Cl)C(Br)Br smiles:C#CC(Cl)(Cl)C(Br)Br H298:49.19 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(Cl)Cl smiles:CC(Cl)(Br)C(Cl)Cl H298:-36.41 kcal/mol
""",
)

entry(
    index = 69,
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
        Cpdata = ([-0.293681,-0.334611,-0.249395,-0.210793,-0.189,-0.125573,0.129855],'cal/(mol*K)','+|-',[0.063146,0.0725735,0.0741879,0.0730995,0.0633871,0.0546708,0.0445555]),
        H298 = (3.74925,'kcal/mol','+|-',0.22511),
        S298 = (1.0306,'cal/(mol*K)','+|-',0.153426),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC(F)C(F)(F)C(F)F smiles:FC(F)C(F)(F)C(F)F H298:-310.38 kcal/mol
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
library:CHOFBr_G4 label:FC(F)C(F)(F)CBr smiles:FC(F)C(F)(F)CBr H298:-213.09 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)OBr smiles:FC(F)C(F)(F)OBr H298:-219.14 kcal/mol
""",
)

entry(
    index = 70,
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
        Cpdata = ([-0.528564,-0.604058,-0.532782,-0.484116,-0.397119,-0.309744,-0.101087],'cal/(mol*K)','+|-',[0.165342,0.190026,0.194254,0.191404,0.165973,0.14315,0.116664]),
        H298 = (1.48754,'kcal/mol','+|-',0.589429),
        S298 = (0.529359,'cal/(mol*K)','+|-',0.401731),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrOC(Br)(Br)C(Br)Br smiles:BrOC(Br)(Br)C(Br)Br H298:7.64 kcal/mol
library:CHOBr_G4 label:CCC(Br)(Br)C(Br)Br smiles:CCC(Br)(Br)C(Br)Br H298:-7.36 kcal/mol
library:CHOBr_G4 label:COC(Br)(Br)C(Br)Br smiles:COC(Br)(Br)C(Br)Br H298:-29.69 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(Br)Br smiles:CC(Br)(Br)C(Br)Br H298:-0.99 kcal/mol
library:CHOBr_G4 label:OC(Br)(Br)C(Br)Br smiles:OC(Br)(Br)C(Br)Br H298:-31.83 kcal/mol
library:CHOBr_G4 label:BrC(Br)C(Br)Br smiles:BrC(Br)C(Br)Br H298:8.22 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)C(Br)Br smiles:FCC(Br)(Br)C(Br)Br H298:-43.33 kcal/mol
""",
)

entry(
    index = 71,
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
    index = 72,
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
        Cpdata = ([-0.405196,-0.351636,-0.24263,-0.206045,-0.159053,-0.0808746,0.215826],'cal/(mol*K)','+|-',[0.0554138,0.0636869,0.0651036,0.0641485,0.0556254,0.0479764,0.0390997]),
        H298 = (2.3345,'kcal/mol','+|-',0.197546),
        S298 = (1.69175,'cal/(mol*K)','+|-',0.134639),
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
library:CHOFClBr_G4 label:FC(Cl)CBr smiles:FC(Cl)CBr H298:-65.68 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)C(Br)Br smiles:C=C(F)C(Cl)C(Br)Br H298:-38.34 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)CBr smiles:FC(F)C(Cl)CBr H298:-122.74 kcal/mol
library:CHOFClBr_G4 label:FCC(F)C(Cl)Br smiles:FCC(F)C(Cl)Br H298:-112.49 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Cl)OBr smiles:FCC(Cl)(Cl)OBr H298:-76.01 kcal/mol
library:CHOFClBr_G4 label:ODCC(Cl)(Br)CF smiles:O=CC(Cl)(Br)CF H298:-85.46 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(F)Cl smiles:OC(Br)C(F)Cl H298:-105.05 kcal/mol
library:CHOFClBr_G4 label:OC(O)(Br)C(F)Cl smiles:OC(O)(Br)C(F)Cl H298:-149.92 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)Br smiles:CC(F)C(Cl)Br H298:-71.46 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)(Cl)CBr smiles:C=CC(F)(Cl)CBr H298:-49.30 kcal/mol
library:CHOFClBr_G4 label:OCC(Br)C(F)Cl smiles:OCC(Br)C(F)Cl H298:-108.93 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)CBr smiles:FC(Cl)C(Br)CBr H298:-66.70 kcal/mol
library:CHOFClBr_G4 label:COC(Cl)(Br)CF smiles:COC(Cl)(Br)CF H298:-103.61 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(O)(Cl)Br smiles:CC(F)C(O)(Cl)Br H298:-113.89 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Cl)CBr smiles:C=C(F)C(Cl)(Cl)CBr H298:-52.77 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Br)CBr smiles:C=C(F)C(Cl)(Br)CBr H298:-39.39 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(O)Br smiles:CC(F)(Cl)C(O)Br H298:-116.70 kcal/mol
library:CHOFClBr_G4 label:FCC(F)(Cl)CBr smiles:FCC(F)(Cl)CBr H298:-118.28 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(F)Cl smiles:CC(Br)C(F)Cl H298:-73.90 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)CBr smiles:FC(Cl)C(Cl)CBr H298:-77.48 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)Br smiles:FCC(Cl)Br H298:-61.57 kcal/mol
library:CHOFClBr_G4 label:OOC(Br)C(F)Cl smiles:OOC(Br)C(F)Cl H298:-83.65 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Br)OBr smiles:FCC(Cl)(Br)OBr H298:-63.62 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)C(Cl)Br smiles:C=C(F)C(Cl)C(Cl)Br H298:-50.05 kcal/mol
library:CHOFClBr_G4 label:CCC(Cl)(Br)CF smiles:CCC(Cl)(Br)CF H298:-77.28 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)C(Cl)Br smiles:C=CC(F)C(Cl)Br H298:-44.22 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)CBr smiles:CC(F)(Cl)CBr H298:-77.33 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(C)(F)Cl smiles:CC(Br)C(C)(F)Cl H298:-85.15 kcal/mol
library:CHOFClBr_G4 label:CCC(Br)C(F)Cl smiles:CCC(Br)C(F)Cl H298:-79.19 kcal/mol
library:CHOFClBr_G4 label:OOC(Cl)(Br)CF smiles:OOC(Cl)(Br)CF H298:-82.22 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)C(Cl)Br smiles:C=C(F)C(F)C(Cl)Br H298:-88.95 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(C)(Cl)Br smiles:CC(F)C(C)(Cl)Br H298:-81.83 kcal/mol
library:CHOFClBr_G4 label:CC(C)(Br)C(F)Cl smiles:CC(C)(Br)C(F)Cl H298:-83.14 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Br)CBr smiles:FCC(Cl)(Br)CBr H298:-65.08 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(Br)CF smiles:CC(Cl)(Br)CF H298:-72.27 kcal/mol
library:CHOFClBr_G4 label:CC(O)(F)C(Cl)Br smiles:CC(O)(F)C(Cl)Br H298:-120.86 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)OBr smiles:FC(Cl)C(Cl)OBr H298:-76.27 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Cl)Br smiles:FCC(Cl)C(Cl)Br H298:-73.00 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)(Cl)CBr smiles:C#CC(F)(Cl)CBr H298:-2.37 kcal/mol
library:CHOFClBr_G4 label:FCC(F)(Cl)OBr smiles:FCC(F)(Cl)OBr H298:-121.19 kcal/mol
library:CHOFClBr_G4 label:CCC(F)(Cl)CBr smiles:CCC(F)(Cl)CBr H298:-83.08 kcal/mol
library:CHOFClBr_G4 label:CC(O)(Br)C(F)Cl smiles:CC(O)(Br)C(F)Cl H298:-116.35 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)OBr smiles:FC(Cl)C(Br)OBr H298:-64.00 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(O)(F)Cl smiles:OC(Br)C(O)(F)Cl H298:-152.59 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Br)Br smiles:FCC(Cl)C(Br)Br H298:-61.59 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)(Cl)CBr smiles:C=C(F)C(F)(Cl)CBr H298:-92.04 kcal/mol
library:CHOFClBr_G4 label:COC(Br)C(F)Cl smiles:COC(Br)C(F)Cl H298:-100.52 kcal/mol
library:CHOFClBr_G4 label:OC(F)C(O)(Cl)Br smiles:OC(F)C(O)(Cl)Br H298:-150.24 kcal/mol
library:CHOFClBr_G4 label:OCC(Cl)(Br)CF smiles:OCC(Cl)(Br)CF H298:-108.70 kcal/mol
library:CHOFClBr_G4 label:CCC(F)C(Cl)Br smiles:CCC(F)C(Cl)Br H298:-76.42 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)C(Cl)Br smiles:C#CC(F)C(Cl)Br H298:0.77 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)(Cl)CBr smiles:FCC(Cl)(Cl)CBr H298:-76.66 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(Cl)CF smiles:CC(Br)(Br)C(Cl)CF H298:-71.91 kcal/mol
library:CHOFClBr_G4 label:FC(F)C(Cl)OBr smiles:FC(F)C(Cl)OBr H298:-121.35 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(Br)CF smiles:OC(Cl)(Br)CF H298:-103.46 kcal/mol
library:CHOFClBr_G4 label:CC(C)(F)C(Cl)Br smiles:CC(C)(F)C(Cl)Br H298:-81.90 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)C(F)Cl smiles:O=CC(Br)C(F)Cl H298:-87.89 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CBr smiles:CC(F)(Br)CBr H298:-64.90 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)CF smiles:OC(Br)C(F)(Br)CF H298:-144.66 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)CBr smiles:FCC(Br)(Br)CBr H298:-53.54 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)Br smiles:O=CC(Br)C(F)Br H298:-75.41 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)CF smiles:OC(Br)C(Br)(Br)CF H298:-92.56 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(F)CBr smiles:FC(F)C(F)(F)CBr H298:-213.09 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(Br)Br smiles:C=CC(F)C(Br)Br H298:-32.61 kcal/mol
library:CHOFBr_G4 label:OC(Br)(OBr)C(F)F smiles:OC(Br)(OBr)C(F)F H298:-153.80 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)Br smiles:O=C(Br)C(Br)C(F)Br H298:-77.92 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)CBr smiles:CC(F)(Br)C(Br)CBr H298:-65.48 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(Br)OBr smiles:CC(F)C(F)(Br)OBr H298:-118.70 kcal/mol
library:CHOFBr_G4 label:CC(F)C(C)(F)Br smiles:CC(F)C(C)(F)Br H298:-123.45 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)OBr smiles:FC(Br)C(Br)OBr H298:-51.47 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(Br)OF smiles:OC(Br)C(F)(Br)OF H298:-103.21 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)CF smiles:CC(Br)(Br)CF H298:-60.45 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)F smiles:OOC(Br)C(F)F H298:-128.42 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)CBr smiles:CC(F)C(F)(F)CBr H298:-173.99 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)F smiles:O=CC(Br)C(F)F H298:-132.46 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)CF smiles:OCC(F)(Br)CF H298:-149.21 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)OBr smiles:CC(F)C(Br)(Br)OBr H298:-61.48 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)CF smiles:CC(F)(Br)C(F)CF H298:-164.23 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(O)(F)F smiles:OC(Br)C(O)(F)F H298:-200.99 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)(F)CBr smiles:FC#CC(F)(F)CBr H298:-76.78 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(F)Br smiles:C#CC(F)C(F)Br H298:-39.16 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)F smiles:OC(Br)(CBr)C(F)F H298:-153.43 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)Br smiles:COC(Br)C(F)Br H298:-87.48 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)Br smiles:CC(F)(CBr)C(F)Br H298:-114.66 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(Br)Br smiles:CC(F)(CBr)C(Br)Br H298:-62.17 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)COBr smiles:FC(F)C(Br)COBr H298:-116.18 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)C(Br)Br smiles:FC#CC(F)C(Br)Br H298:-16.72 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(F)Br smiles:OC(F)(CF)C(F)Br H298:-202.40 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)OOBr smiles:FC(F)C(Br)OOBr H298:-91.98 kcal/mol
library:CHOFBr_G4 label:FCC(F)Br smiles:FCC(F)Br H298:-102.08 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)C(Br)Br smiles:FCC(Br)(Br)C(Br)Br H298:-43.33 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(O)(F)Br smiles:OC(Br)C(O)(F)Br H298:-139.47 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)OCBr smiles:FC(Br)C(Br)OCBr H298:-84.15 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)Br smiles:CC(O)(Br)C(F)Br H298:-103.82 kcal/mol
library:CHOFBr_G4 label:OOC(Br)(Br)CF smiles:OOC(Br)(Br)CF H298:-70.13 kcal/mol
library:CHOFBr_G4 label:FCC(Br)Br smiles:FCC(Br)Br H298:-49.93 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)CF smiles:CC(Br)(Br)C(F)CF H298:-110.86 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(Br)Br smiles:OC(F)(CF)C(Br)Br H298:-148.17 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)CBr smiles:FCC(F)(Br)CBr H298:-105.73 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)CCBr smiles:FC(Br)C(Br)CCBr H298:-62.71 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)OCBr smiles:FCC(F)(Br)OCBr H298:-137.90 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(Br)CBr smiles:C=CC(F)(Br)CBr H298:-37.42 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)CCBr smiles:FCC(F)(Br)CCBr H298:-112.84 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)F smiles:CC(Br)C(Br)C(F)F H298:-120.45 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(F)Br smiles:FC(F)C(F)C(F)Br H298:-203.50 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)OOBr smiles:FCC(Br)(Br)OOBr H298:-33.40 kcal/mol
library:CHOFBr_G4 label:CC(F)C(O)(F)Br smiles:CC(F)C(O)(F)Br H298:-159.75 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)CF smiles:OC(Br)(Br)CF H298:-91.29 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)OBr smiles:CC(F)(F)C(Br)OBr H298:-122.94 kcal/mol
library:CHOFBr_G4 label:COC(Br)C(F)F smiles:COC(Br)C(F)F H298:-145.64 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)Br smiles:CC(F)C(Br)Br H298:-59.94 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)CF smiles:CC(Br)C(F)(F)CF H298:-170.18 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)CF smiles:CCC(F)(Br)CF H298:-117.83 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(F)Br smiles:CC(F)C(F)C(F)Br H298:-162.99 kcal/mol
library:CHOFBr_G4 label:CC(F)C(O)(Br)Br smiles:CC(F)C(O)(Br)Br H298:-101.52 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CF smiles:CC(F)(Br)CF H298:-114.03 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)F smiles:OC(Br)C(F)F H298:-149.43 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(F)CBr smiles:C#CC(F)(F)CBr H298:-47.87 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)CBr smiles:FC(F)C(Br)CBr H298:-111.45 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)C(F)Br smiles:FC#CC(F)C(F)Br H298:-67.69 kcal/mol
library:CHOFBr_G4 label:OC(F)C(Br)(Br)OBr smiles:OC(F)C(Br)(Br)OBr H298:-98.03 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)C(F)Br smiles:CC(C)(Br)C(F)Br H298:-70.68 kcal/mol
library:CHOFBr_G4 label:OCC(Br)(Br)CF smiles:OCC(Br)(Br)CF H298:-97.02 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)Br smiles:FCC(F)C(Br)Br H298:-100.89 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(F)Br smiles:CC(O)(F)C(F)Br H298:-161.32 kcal/mol
library:CHOFBr_G4 label:FC(Br)CBr smiles:FC(Br)CBr H298:-53.30 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)F smiles:O=C(Br)C(Br)C(F)F H298:-135.53 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)C(F)F smiles:CC(O)(Br)C(F)F H298:-161.07 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)Br smiles:CCC(Br)C(F)Br H298:-66.74 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)C(F)Br smiles:CC(F)(OBr)C(F)Br H298:-120.06 kcal/mol
library:CHOFBr_G4 label:FC(F)CBr smiles:FC(F)CBr H298:-110.81 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)(Br)CBr smiles:FC#CC(F)(Br)CBr H298:-19.05 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)(Br)CF smiles:CC(Br)C(Br)(Br)CF H298:-61.63 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)F smiles:OC(O)(Br)C(F)F H298:-194.95 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(C)(F)Br smiles:CC(Br)C(C)(F)Br H298:-72.52 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(Br)OBr smiles:OC(F)(Br)C(Br)OBr H298:-98.46 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(Br)Br smiles:CCC(F)C(Br)Br H298:-64.86 kcal/mol
library:CHOFBr_G4 label:FCCC(F)(Br)CBr smiles:FCCC(F)(Br)CBr H298:-113.30 kcal/mol
library:CHOFBr_G4 label:OC(Br)(OBr)C(F)Br smiles:OC(Br)(OBr)C(F)Br H298:-96.83 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)C(Br)Br smiles:FC(F)C(Br)C(Br)Br H298:-102.73 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)Br smiles:FCC(F)C(F)Br H298:-152.56 kcal/mol
library:CHOFBr_G4 label:COC(Br)(Br)CF smiles:COC(Br)(Br)CF H298:-89.73 kcal/mol
library:CHOFBr_G4 label:C#CC(F)C(Br)Br smiles:C#CC(F)C(Br)Br H298:12.14 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(Br)Br smiles:CC(C)(F)C(Br)Br H298:-70.27 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(F)Br smiles:C=C(F)C(F)C(F)Br H298:-129.78 kcal/mol
library:CHOFBr_G4 label:FCCC(F)(F)CBr smiles:FCCC(F)(F)CBr H298:-171.41 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)OBr smiles:FC(F)C(Br)OBr H298:-108.88 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)C(Br)Br smiles:CC(F)(OBr)C(Br)Br H298:-68.38 kcal/mol
library:CHOFBr_G4 label:OOC(Br)C(F)Br smiles:OOC(Br)C(F)Br H298:-70.87 kcal/mol
library:CHOFBr_G4 label:CDCC(F)C(F)Br smiles:C=CC(F)C(F)Br H298:-84.46 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)(F)CBr smiles:FC=CC(F)(F)CBr H298:-139.21 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(Br)Br smiles:CC(F)C(F)C(Br)Br H298:-111.37 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)(Br)CBr smiles:FC(F)C(F)(Br)CBr H298:-154.71 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(Br)OBr smiles:OC(F)(F)C(Br)OBr H298:-160.18 kcal/mol
library:CHOFBr_G4 label:CCC(F)(F)CBr smiles:CCC(F)(F)CBr H298:-128.46 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)CBr smiles:C=C(F)C(F)(Br)CBr H298:-83.22 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)C(Br)Br smiles:FC(Br)C(Br)C(Br)Br H298:-45.59 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)(Br)CF smiles:O=C(Br)C(Br)(Br)CF H298:-74.56 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)CF smiles:OC(Br)C(F)(F)CF H298:-201.11 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(C)(F)F smiles:CC(Br)C(C)(F)F H298:-131.65 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)CF smiles:O=CC(Br)(Br)CF H298:-74.33 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)Br smiles:CC(Br)(CBr)C(F)Br H298:-63.05 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)Br smiles:OC(Br)C(Br)C(F)Br H298:-94.35 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)F smiles:OC(Br)C(Br)C(F)F H298:-152.41 kcal/mol
library:CHOFBr_G4 label:OOC(F)(Br)CF smiles:OOC(F)(Br)CF H298:-126.65 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)C(Br)Br smiles:FC=CC(F)C(Br)Br H298:-77.79 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)CBr smiles:CC(F)(F)CBr H298:-123.45 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)CF smiles:O=CC(F)(Br)CF H298:-125.86 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)Br smiles:CC(Br)C(F)Br H298:-61.25 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)CBr smiles:CC(F)(F)C(Br)CBr H298:-123.94 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)F smiles:OCC(Br)C(F)F H298:-154.15 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)COBr smiles:FCC(F)(Br)COBr H298:-109.70 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)OCBr smiles:FCC(Br)(Br)OCBr H298:-81.35 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)OF smiles:OC(Br)C(F)(F)OF H298:-162.25 kcal/mol
library:CHOFBr_G4 label:OC(F)C(O)(F)Br smiles:OC(F)C(O)(F)Br H298:-195.75 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)CCBr smiles:FCC(Br)(Br)CCBr H298:-60.02 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)OOBr smiles:FCC(F)(Br)OOBr H298:-89.52 kcal/mol
library:CHOFBr_G4 label:OC(F)C(O)(Br)Br smiles:OC(F)C(O)(Br)Br H298:-138.12 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)F smiles:CC(Br)(CBr)C(F)F H298:-120.70 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)CBr smiles:FCC(F)(F)CBr H298:-163.39 kcal/mol
library:CHOFBr_G4 label:C#CC(F)(Br)CBr smiles:C#CC(F)(Br)CBr H298:9.56 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)OBr smiles:FCC(F)(Br)OBr H298:-108.24 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)COBr smiles:FC(Br)C(Br)COBr H298:-58.24 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)C(Br)Br smiles:CC(O)(F)C(Br)Br H298:-109.22 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)OOBr smiles:FC(Br)C(Br)OOBr H298:-34.32 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)CF smiles:OC(F)(Br)C(F)CF H298:-199.92 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)OF smiles:OC(Br)(Br)C(F)OF H298:-101.91 kcal/mol
library:CHOFBr_G4 label:FCCC(F)C(Br)Br smiles:FCCC(F)C(Br)Br H298:-109.63 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)OCBr smiles:FC(F)C(Br)OCBr H298:-141.36 kcal/mol
library:CHOFBr_G4 label:CCC(F)(Br)CBr smiles:CCC(F)(Br)CBr H298:-69.68 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(O)Br smiles:CC(F)(F)C(O)Br H298:-162.13 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)CCBr smiles:FC(F)C(Br)CCBr H298:-119.88 kcal/mol
library:CHOFBr_G4 label:OCC(Br)C(F)Br smiles:OCC(Br)C(F)Br H298:-96.47 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)CF smiles:O=C(Br)C(F)(Br)CF H298:-127.21 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(F)Br smiles:CC(F)(CF)C(F)Br H298:-163.90 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(Br)Br smiles:CC(F)(CF)C(Br)Br H298:-112.11 kcal/mol
library:CHOFBr_G4 label:FCCC(F)C(F)Br smiles:FCCC(F)C(F)Br H298:-161.40 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)CBr smiles:C=C(F)C(F)(F)CBr H298:-139.80 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)CF smiles:OC(Br)(Br)C(F)CF H298:-141.65 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)OF smiles:OC(F)(Br)C(F)OF H298:-160.00 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)C(F)Br smiles:CC(C)(F)C(F)Br H298:-122.17 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)Br smiles:OC(Br)(CBr)C(F)Br H298:-95.28 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)Br smiles:CC(Br)C(Br)C(F)Br H298:-62.55 kcal/mol
library:CHOFBr_G4 label:CCC(Br)(Br)CF smiles:CCC(Br)(Br)CF H298:-66.05 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)C(F)Br smiles:OC(O)(Br)C(F)Br H298:-137.50 kcal/mol
library:CHOFBr_G4 label:FCC(F)(Br)C(Br)Br smiles:FCC(F)(Br)C(Br)Br H298:-94.18 kcal/mol
library:CHOFBr_G4 label:COC(F)(Br)CF smiles:COC(F)(Br)CF H298:-145.95 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)CBr smiles:CC(F)C(Br)(Br)CBr H298:-63.51 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)Br smiles:OC(Br)C(F)Br H298:-92.60 kcal/mol
library:CHOFBr_G4 label:CCC(Br)C(F)F smiles:CCC(Br)C(F)F H298:-124.48 kcal/mol
library:CHOFBr_G4 label:CC(Br)(OBr)C(F)F smiles:CC(Br)(OBr)C(F)F H298:-121.07 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(Br)Br smiles:C=C(F)C(F)C(Br)Br H298:-78.64 kcal/mol
library:CHOFBr_G4 label:CCC(F)C(F)Br smiles:CCC(F)C(F)Br H298:-117.38 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)CBr smiles:FC(Br)C(Br)CBr H298:-53.80 kcal/mol
library:CHOFBr_G4 label:CC(F)C(C)(Br)Br smiles:CC(F)C(C)(Br)Br H298:-70.01 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(Br)CBr smiles:CC(F)C(F)(Br)CBr H298:-116.04 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(Br)CF smiles:CC(Br)C(F)(Br)CF H298:-111.84 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(Br)Br smiles:FC(F)C(F)C(Br)Br H298:-151.22 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)C(F)Br smiles:FC=CC(F)C(F)Br H298:-129.02 kcal/mol
library:CHOFBr_G4 label:CDCC(F)(F)CBr smiles:C=CC(F)(F)CBr H298:-94.60 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)F smiles:CC(Br)C(F)F H298:-119.22 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)OBr smiles:CC(F)(Br)C(Br)OBr H298:-63.82 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)CF smiles:OC(F)(Br)CF H298:-149.25 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)OBr smiles:FCC(Br)(Br)OBr H298:-51.63 kcal/mol
library:CHOFBr_G4 label:OC(F)C(F)(Br)OBr smiles:OC(F)C(F)(Br)OBr H298:-154.78 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)(Br)CBr smiles:FC=CC(F)(Br)CBr H298:-81.43 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)Br smiles:CC(F)C(F)Br H298:-111.34 kcal/mol
library:CHOFBr_G4 label:CC(Br)(OBr)C(F)Br smiles:CC(Br)(OBr)C(F)Br H298:-63.34 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(O)Br smiles:CC(F)(Br)C(O)Br H298:-104.16 kcal/mol
library:CHOClBr_G4 label:OC(Br)(Br)CCl smiles:OC(Br)(Br)CCl H298:-53.39 kcal/mol
library:CHOClBr_G4 label:ClC(Br)CBr smiles:ClC(Br)CBr H298:-12.64 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)C(Cl)Br smiles:CC(O)(Br)C(Cl)Br H298:-63.26 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)(Br)CCl smiles:O=CC(Br)(Br)CCl H298:-36.69 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)OBr smiles:ClCC(Br)(Br)OBr H298:-13.85 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(O)Br smiles:CC(Cl)(Br)C(O)Br H298:-62.68 kcal/mol
library:CHOClBr_G4 label:COC(Br)C(Cl)Cl smiles:COC(Br)C(Cl)Cl H298:-59.80 kcal/mol
library:CHOClBr_G4 label:OC(O)(Br)C(Cl)Cl smiles:OC(O)(Br)C(Cl)Cl H298:-108.86 kcal/mol
library:CHOClBr_G4 label:OOC(Br)C(Cl)Br smiles:OOC(Br)C(Cl)Br H298:-31.38 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Br)CCl smiles:CCC(Cl)(Br)CCl H298:-39.80 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Cl)CBr smiles:ClCC(Cl)(Cl)CBr H298:-39.12 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(C)(Br)Br smiles:CC(Cl)C(C)(Br)Br H298:-30.47 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Br)Br smiles:ClCC(Cl)C(Br)Br H298:-24.39 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(O)(Cl)Br smiles:OC(Cl)C(O)(Cl)Br H298:-106.64 kcal/mol
library:CHOClBr_G4 label:CC(C)(Cl)C(Cl)Br smiles:CC(C)(Cl)C(Cl)Br H298:-41.12 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)Cl smiles:OC(Br)C(Cl)Cl H298:-64.12 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)Br smiles:ClCC(Cl)Br H298:-23.71 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Cl smiles:O=CC(Br)C(Cl)Cl H298:-46.56 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CCl smiles:CC(Cl)(Br)CCl H298:-34.20 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)OBr smiles:ClC(Cl)C(Br)OBr H298:-23.52 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(O)(Cl)Cl smiles:OC(Br)C(O)(Cl)Cl H298:-106.78 kcal/mol
library:CHOClBr_G4 label:COC(Br)(Br)CCl smiles:COC(Br)(Br)CCl H298:-51.11 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(O)(Br)Br smiles:OC(Cl)C(O)(Br)Br H298:-94.40 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)C(Cl)Br smiles:ClCC(Cl)C(Cl)Br H298:-35.75 kcal/mol
library:CHOClBr_G4 label:CC(C)(Cl)C(Br)Br smiles:CC(C)(Cl)C(Br)Br H298:-29.65 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)Br smiles:ClCC(Br)Br H298:-12.12 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)C(Cl)Cl smiles:CC(C)(Br)C(Cl)Cl H298:-41.41 kcal/mol
library:CHOClBr_G4 label:CCC(Br)C(Cl)Br smiles:CCC(Br)C(Cl)Br H298:-26.54 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CBr)C(Cl)Br smiles:CC(Br)(CBr)C(Cl)Br H298:-21.80 kcal/mol
library:CHOClBr_G4 label:OCC(Br)C(Cl)Cl smiles:OCC(Br)C(Cl)Cl H298:-67.83 kcal/mol
library:CHOClBr_G4 label:OOC(Cl)(Br)CCl smiles:OOC(Cl)(Br)CCl H298:-44.56 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)Br smiles:CC(Br)C(Cl)Br H298:-21.02 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(C)(Cl)Cl smiles:CC(Br)C(C)(Cl)Cl H298:-42.64 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Br)CBr smiles:ClCC(Cl)(Br)CBr H298:-27.55 kcal/mol
library:CHOClBr_G4 label:OCC(Br)(Br)CCl smiles:OCC(Br)(Br)CCl H298:-59.18 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)CBr smiles:ClC(Cl)CBr H298:-24.27 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(C)(Cl)Br smiles:CC(Cl)C(C)(Cl)Br H298:-42.20 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)C(Cl)Br smiles:C=C(Cl)C(Cl)C(Cl)Br H298:-10.34 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Br)CBr smiles:C=CC(Cl)(Br)CBr H298:4.44 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)CCl smiles:CC(Br)(Br)C(Cl)CCl H298:-34.51 kcal/mol
library:CHOClBr_G4 label:CCC(Br)(Br)CCl smiles:CCC(Br)(Br)CCl H298:-28.01 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)(Br)OBr smiles:ClCC(Cl)(Br)OBr H298:-25.96 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(C)(Cl)Br smiles:CC(Br)C(C)(Cl)Br H298:-30.82 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Br)Br smiles:C#CC(Cl)C(Br)Br H298:50.74 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(Br)CCl smiles:OC(Cl)(Br)CCl H298:-65.67 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)Cl smiles:CC(Br)C(Cl)Cl H298:-32.71 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)CCl smiles:O=CC(Cl)(Br)CCl H298:-47.31 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)Br smiles:CC(Cl)C(Br)Br H298:-20.87 kcal/mol
library:CHOClBr_G4 label:CC(O)(Cl)C(Cl)Br smiles:CC(O)(Cl)C(Cl)Br H298:-75.31 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Cl)CBr smiles:CCC(Cl)(Cl)CBr H298:-40.67 kcal/mol
library:CHOClBr_G4 label:COC(Cl)(Br)CCl smiles:COC(Cl)(Br)CCl H298:-63.04 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)CBr smiles:CC(Cl)(Cl)CBr H298:-34.85 kcal/mol
library:CHOClBr_G4 label:OCC(Br)C(Cl)Br smiles:OCC(Br)C(Cl)Br H298:-56.24 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)C(Br)Br smiles:CCC(Cl)C(Br)Br H298:-26.35 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CBr)C(Cl)Cl smiles:CC(Br)(CBr)C(Cl)Cl H298:-33.52 kcal/mol
library:CHOClBr_G4 label:CCC(Br)C(Cl)Cl smiles:CCC(Br)C(Cl)Cl H298:-38.11 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Br)CBr smiles:C=C(Cl)C(Cl)(Br)CBr H298:-0.42 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(O)(Br)Br smiles:CC(Cl)C(O)(Br)Br H298:-61.98 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Cl)Br smiles:C=CC(Cl)C(Cl)Br H298:-5.71 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Cl)CBr smiles:C#CC(Cl)(Cl)CBr H298:39.23 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)C(Cl)Br smiles:CC(C)(Br)C(Cl)Br H298:-29.69 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)CCl smiles:CC(Br)(Br)CCl H298:-22.44 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(O)Br smiles:CC(Cl)(Cl)C(O)Br H298:-74.41 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)C(Cl)Br smiles:CCC(Cl)C(Cl)Br H298:-37.66 kcal/mol
library:CHOClBr_G4 label:OOC(Br)(Br)CCl smiles:OOC(Br)(Br)CCl H298:-32.79 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)C(Br)Br smiles:C=CC(Cl)C(Br)Br H298:5.80 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)CBr smiles:ClC(Cl)C(Br)CBr H298:-25.18 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(O)(Cl)Br smiles:OC(Br)C(O)(Cl)Br H298:-94.52 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(O)(Cl)Br smiles:CC(Cl)C(O)(Cl)Br H298:-74.16 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CBr smiles:CC(Cl)(Br)CBr H298:-22.78 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Br smiles:O=CC(Br)C(Cl)Br H298:-34.77 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)Br smiles:OC(Br)C(Cl)Br H298:-52.56 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)(Br)CBr smiles:C#CC(Cl)(Br)CBr H298:50.71 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Cl)CBr smiles:C=C(Cl)C(Cl)(Cl)CBr H298:-13.98 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)C(Br)Br smiles:C=C(Cl)C(Cl)C(Br)Br H298:1.08 kcal/mol
library:CHOClBr_G4 label:ClC(Br)C(Br)OBr smiles:ClC(Br)C(Br)OBr H298:-12.21 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Br)CCl smiles:OCC(Cl)(Br)CCl H298:-70.57 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)(Br)CBr smiles:CCC(Cl)(Br)CBr H298:-28.82 kcal/mol
library:CHOClBr_G4 label:OC(O)(Br)C(Cl)Br smiles:OC(O)(Br)C(Cl)Br H298:-97.09 kcal/mol
library:CHOClBr_G4 label:OOC(Br)C(Cl)Cl smiles:OOC(Br)C(Cl)Cl H298:-42.82 kcal/mol
library:CHOClBr_G4 label:COC(Br)C(Cl)Br smiles:COC(Br)C(Cl)Br H298:-47.98 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)(Cl)CBr smiles:C=CC(Cl)(Cl)CBr H298:-6.91 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)C(Cl)Br smiles:C#CC(Cl)C(Cl)Br H298:39.29 kcal/mol
library:CHOClBr_G4 label:CC(Br)(OBr)C(Cl)Br smiles:CC(Br)(OBr)C(Cl)Br H298:-22.46 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)CBr smiles:ClCC(Br)(Br)CBr H298:-16.12 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)C(Cl)Cl smiles:CC(O)(Br)C(Cl)Cl H298:-74.95 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)Br smiles:CC(Cl)C(Cl)Br H298:-32.28 kcal/mol
library:CHOClBr_G4 label:CC(O)(Cl)C(Br)Br smiles:CC(O)(Cl)C(Br)Br H298:-63.94 kcal/mol
""",
)

entry(
    index = 73,
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
        Cpdata = ([-0.295076,-0.152037,0.0132143,0.0659162,0.0716455,0.123005,0.327998],'cal/(mol*K)','+|-',[0.0771869,0.0887106,0.090684,0.0893535,0.0774816,0.0668272,0.0544626]),
        H298 = (4.6743,'kcal/mol','+|-',0.275165),
        S298 = (1.61147,'cal/(mol*K)','+|-',0.187541),
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
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)F smiles:FCC(F)(C(F)F)C(F)F H298:-312.22 kcal/mol
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
library:CHOF_G4 label:FCC(F)(F)CF smiles:FCC(F)(F)CF H298:-212.41 kcal/mol
library:CHOF_G4 label:OC(F)(F)C(F)OF smiles:OC(F)(F)C(F)OF H298:-222.38 kcal/mol
library:CHOF_G4 label:FCDCC(F)(F)CF smiles:FC=CC(F)(F)CF H298:-187.81 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)CCl smiles:FC(F)C(F)CCl H298:-172.53 kcal/mol
library:CHOFCl_G4 label:FCC(F)(F)CCl smiles:FCC(F)(F)CCl H298:-174.61 kcal/mol
library:CHOFCl_G4 label:FCC(F)(F)OCl smiles:FCC(F)(F)OCl H298:-171.79 kcal/mol
library:CHOFCl_G4 label:FC(F)C(F)OCl smiles:FC(F)C(F)OCl H298:-167.37 kcal/mol
library:CHOFBr_G4 label:OC(F)C(F)(F)OBr smiles:OC(F)C(F)(F)OBr H298:-215.95 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(Br)Br smiles:FCC(F)(F)C(Br)Br H298:-152.82 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)OBr smiles:FC(F)C(F)OBr H298:-164.76 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)CBr smiles:CC(F)C(F)(F)CBr H298:-173.99 kcal/mol
library:CHOFBr_G4 label:OC(F)(OBr)C(F)F smiles:OC(F)(OBr)C(F)F H298:-214.44 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)COBr smiles:FC(F)C(F)COBr H298:-165.68 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)OOBr smiles:FC(F)C(F)OOBr H298:-147.39 kcal/mol
library:CHOFBr_G4 label:OC(F)(F)C(F)OBr smiles:OC(F)(F)C(F)OBr H298:-216.02 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)CBr smiles:CC(F)(F)C(F)CBr H298:-174.68 kcal/mol
library:CHOFBr_G4 label:OC(F)(CBr)C(F)F smiles:OC(F)(CBr)C(F)F H298:-210.80 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)OBr smiles:FCC(F)(F)OBr H298:-169.86 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(F)Br smiles:FC(F)C(F)C(F)Br H298:-203.50 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)C(F)F smiles:OC(Br)C(F)C(F)F H298:-201.12 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)(F)CF smiles:CC(Br)C(F)(F)CF H298:-170.18 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)CF smiles:O=C(Br)C(F)(F)CF H298:-182.34 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)COBr smiles:FCC(F)(F)COBr H298:-166.80 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)OOBr smiles:FCC(F)(F)OOBr H298:-150.32 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)OCBr smiles:FCC(F)(F)OCBr H298:-200.45 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)C(F)Br smiles:FCC(F)(F)C(F)Br H298:-204.60 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)CCBr smiles:FCC(F)(F)CCBr H298:-170.66 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)C(F)F smiles:O=C(Br)C(F)C(F)F H298:-182.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)(F)CF smiles:OC(Br)C(F)(F)CF H298:-201.11 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)C(F)F smiles:CC(Br)C(F)C(F)F H298:-170.06 kcal/mol
library:CHOFBr_G4 label:FCC(F)(F)CBr smiles:FCC(F)(F)CBr H298:-163.39 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)OBr smiles:CC(F)(F)C(F)OBr H298:-178.85 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)CCBr smiles:FC(F)C(F)CCBr H298:-169.39 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)F smiles:CC(F)(CBr)C(F)F H298:-172.69 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)(F)OBr smiles:CC(F)C(F)(F)OBr H298:-180.54 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)C(Br)Br smiles:FC(F)C(F)C(Br)Br H298:-151.22 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)CBr smiles:FC(F)C(F)CBr H298:-161.37 kcal/mol
library:CHOFBr_G4 label:CC(F)(OBr)C(F)F smiles:CC(F)(OBr)C(F)F H298:-177.53 kcal/mol
""",
)

entry(
    index = 74,
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
        Cpdata = ([-0.533259,-0.489383,-0.315142,-0.21834,-0.131172,-0.0481284,0.187158],'cal/(mol*K)','+|-',[0.109232,0.12554,0.128332,0.12645,0.109649,0.0945712,0.0770734]),
        H298 = (2.39313,'kcal/mol','+|-',0.389402),
        S298 = (0.774199,'cal/(mol*K)','+|-',0.265401),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CC(Br)(Br)C(Br)CBr smiles:CC(Br)(Br)C(Br)CBr H298:-12.26 kcal/mol
library:CHOBr_G4 label:BrOOC(Br)C(Br)Br smiles:BrOOC(Br)C(Br)Br H298:16.33 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)(Br)CBr smiles:BrCCC(Br)(Br)CBr H298:-11.09 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)Br smiles:CC(Br)C(Br)Br H298:-9.68 kcal/mol
library:CHOBr_G4 label:C#CC(Br)C(Br)Br smiles:C#CC(Br)C(Br)Br H298:61.37 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)(Br)OBr smiles:CC(Br)C(Br)(Br)OBr H298:-11.13 kcal/mol
library:CHOBr_G4 label:CDCC(Br)(Br)CBr smiles:C=CC(Br)(Br)CBr H298:16.10 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)C(Br)Br smiles:BrC#CC(Br)C(Br)Br H298:71.51 kcal/mol
library:CHOBr_G4 label:OOC(Br)(Br)CBr smiles:OOC(Br)(Br)CBr H298:-21.46 kcal/mol
library:CHOBr_G4 label:CCC(Br)C(Br)Br smiles:CCC(Br)C(Br)Br H298:-15.29 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)C(Br)Br smiles:CC(Br)(CBr)C(Br)Br H298:-12.30 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)(Br)CBr smiles:BrC=CC(Br)(Br)CBr H298:21.57 kcal/mol
library:CHOBr_G4 label:C#CC(Br)(Br)CBr smiles:C#CC(Br)(Br)CBr H298:61.53 kcal/mol
library:CHOBr_G4 label:CC(Br)C(O)(Br)Br smiles:CC(Br)C(O)(Br)Br H298:-50.54 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)C(Br)Br smiles:BrCCC(Br)C(Br)Br H298:-11.02 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)CBr smiles:CC(Br)(Br)CBr H298:-11.36 kcal/mol
library:CHOBr_G4 label:CDCC(Br)C(Br)Br smiles:C=CC(Br)C(Br)Br H298:16.64 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)(Br)CBr smiles:BrC#CC(Br)(Br)CBr H298:71.55 kcal/mol
library:CHOBr_G4 label:CC(O)(Br)C(Br)Br smiles:CC(O)(Br)C(Br)Br H298:-51.76 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)C(Br)Br smiles:BrC=CC(Br)C(Br)Br H298:20.31 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C(Br)Br smiles:BrOC(Br)C(Br)Br H298:-0.73 kcal/mol
library:CHOBr_G4 label:CCC(Br)(Br)CBr smiles:CCC(Br)(Br)CBr H298:-17.40 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)OBr smiles:BrCC(Br)(Br)OBr H298:-2.97 kcal/mol
library:CHOBr_G4 label:OOC(Br)C(Br)Br smiles:OOC(Br)C(Br)Br H298:-20.37 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)CBr smiles:BrCC(Br)(Br)CBr H298:-5.20 kcal/mol
library:CHOBr_G4 label:OC(O)(Br)C(Br)Br smiles:OC(O)(Br)C(Br)Br H298:-85.64 kcal/mol
library:CHOBr_G4 label:COC(Br)C(Br)Br smiles:COC(Br)C(Br)Br H298:-36.80 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)OOBr smiles:BrCC(Br)(Br)OOBr H298:15.24 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(Br)COBr smiles:BrCC(Br)(Br)COBr H298:-9.18 kcal/mol
library:CHOBr_G4 label:OCC(Br)(Br)CBr smiles:OCC(Br)(Br)CBr H298:-48.18 kcal/mol
library:CHOBr_G4 label:CC(Br)(OBr)C(Br)Br smiles:CC(Br)(OBr)C(Br)Br H298:-12.59 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)C(Br)Br smiles:CC(Br)C(Br)C(Br)Br H298:-10.95 kcal/mol
library:CHOBr_G4 label:OC(Br)C(O)(Br)Br smiles:OC(Br)C(O)(Br)Br H298:-82.41 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)(Br)CBr smiles:BrCOC(Br)(Br)CBr H298:-33.86 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)Br smiles:OC(Br)C(Br)Br H298:-41.19 kcal/mol
library:CHOBr_G4 label:BrOCC(Br)C(Br)Br smiles:BrOCC(Br)C(Br)Br H298:-6.98 kcal/mol
library:CHOBr_G4 label:ODCC(Br)C(Br)Br smiles:O=CC(Br)C(Br)Br H298:-23.66 kcal/mol
library:CHOBr_G4 label:OCC(Br)C(Br)Br smiles:OCC(Br)C(Br)Br H298:-44.97 kcal/mol
library:CHOBr_G4 label:COC(Br)(Br)CBr smiles:COC(Br)(Br)CBr H298:-40.37 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)Br smiles:BrCC(Br)C(Br)Br H298:-2.37 kcal/mol
library:CHOBr_G4 label:CC(C)(Br)C(Br)Br smiles:CC(C)(Br)C(Br)Br H298:-18.11 kcal/mol
library:CHOBr_G4 label:BrCC(Br)Br smiles:BrCC(Br)Br H298:-1.09 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(O)Br smiles:CC(Br)(Br)C(O)Br H298:-51.12 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)(Br)CBr smiles:CC(Br)C(Br)(Br)CBr H298:-11.31 kcal/mol
library:CHOBr_G4 label:CC(Br)C(C)(Br)Br smiles:CC(Br)C(C)(Br)Br H298:-19.17 kcal/mol
library:CHOBr_G4 label:BrC(Br)C(Br)C(Br)Br smiles:BrC(Br)C(Br)C(Br)Br H298:9.13 kcal/mol
library:CHOBr_G4 label:ODCC(Br)(Br)CBr smiles:O=CC(Br)(Br)CBr H298:-25.64 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(Br)OBr smiles:CC(Br)(Br)C(Br)OBr H298:-11.14 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)C(Br)Br smiles:BrCOC(Br)C(Br)Br H298:-33.21 kcal/mol
library:CHOBr_G4 label:OC(Br)(Br)CBr smiles:OC(Br)(Br)CBr H298:-42.42 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(Br)CBr smiles:FCC(Br)(Br)CBr H298:-53.54 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)CF smiles:OC(Br)C(Br)(Br)CF H298:-92.56 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)(Br)OF smiles:OC(Br)C(Br)(Br)OF H298:-46.14 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)C(Br)Br smiles:OC(Br)(CF)C(Br)Br H298:-93.15 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)Br smiles:FCC(Br)C(Br)Br H298:-50.43 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)C(Br)Br smiles:CC(Br)(CF)C(Br)Br H298:-60.41 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)(Br)CF smiles:CC(Br)C(Br)(Br)CF H298:-61.63 kcal/mol
library:CHOFBr_G4 label:FCCC(Br)C(Br)Br smiles:FCCC(Br)C(Br)Br H298:-59.68 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)C(Br)Br smiles:FC(F)C(Br)C(Br)Br H298:-102.73 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)CF smiles:CC(Br)(Br)C(Br)CF H298:-60.25 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)C(Br)Br smiles:C=C(F)C(Br)C(Br)Br H298:-29.62 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)C(Br)Br smiles:FC=CC(Br)C(Br)Br H298:-28.75 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)C(Br)Br smiles:FC(Br)C(Br)C(Br)Br H298:-45.59 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)C(Br)Br smiles:CC(F)C(Br)C(Br)Br H298:-61.28 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)(Br)CBr smiles:FC#CC(Br)(Br)CBr H298:33.28 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)(Br)CBr smiles:FC(F)C(Br)(Br)CBr H298:-103.62 kcal/mol
library:CHOFBr_G4 label:FCCC(Br)(Br)CBr smiles:FCCC(Br)(Br)CBr H298:-59.59 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)CBr smiles:C=C(F)C(Br)(Br)CBr H298:-29.58 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)(Br)CBr smiles:CC(F)C(Br)(Br)CBr H298:-63.51 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)(Br)CBr smiles:FC(Br)C(Br)(Br)CBr H298:-46.71 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)(Br)CBr smiles:FC=CC(Br)(Br)CBr H298:-27.87 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)OF smiles:OC(Br)(Br)C(Br)OF H298:-46.26 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)CF smiles:OC(Br)(Br)C(Br)CF H298:-90.95 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)C(Br)Br smiles:FC#CC(Br)C(Br)Br H298:32.99 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)(Br)CBr smiles:C=C(Cl)C(Br)(Br)CBr H298:9.07 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)C(Br)Br smiles:C=C(Cl)C(Br)C(Br)Br H298:8.65 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)C(Br)Br smiles:CC(Br)(CCl)C(Br)Br H298:-21.40 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)C(Br)Br smiles:ClCC(Br)C(Br)Br H298:-13.29 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)(Br)CBr smiles:ClCC(Br)(Br)CBr H298:-16.12 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Br)CCl smiles:CC(Br)(Br)C(Br)CCl H298:-23.29 kcal/mol
""",
)

entry(
    index = 75,
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
        Cpdata = ([-0.511483,-0.332273,-0.19635,-0.126283,-0.0451817,0.0556001,0.404346],'cal/(mol*K)','+|-',[0.105956,0.121775,0.124484,0.122657,0.10636,0.091735,0.0747619]),
        H298 = (3.57833,'kcal/mol','+|-',0.377724),
        S298 = (1.83172,'cal/(mol*K)','+|-',0.257442),
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
library:CHOFClBr_G4 label:CC(Br)(Br)C(Cl)DCF smiles:CC(Br)(Br)C(Cl)=CF H298:-39.29 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)C(F)Cl smiles:CC(Br)=C(Cl)C(F)Cl H298:-53.16 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)(Cl)OBr smiles:C=C(F)C(F)(Cl)OBr H298:-96.25 kcal/mol
library:CHOFClBr_G4 label:FCDC(F)C(Cl)Br smiles:FC=C(F)C(Cl)Br H298:-77.79 kcal/mol
library:CHOFClBr_G4 label:CDCDC(F)C(Cl)Br smiles:C=C=C(F)C(Cl)Br H298:0.37 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Cl)CBr smiles:C=C(F)C(Cl)(Cl)CBr H298:-52.77 kcal/mol
library:CHOFClBr_G4 label:CCDC(Br)C(F)Cl smiles:CC=C(Br)C(F)Cl H298:-49.23 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(C)(Cl)Br smiles:C=C(F)C(C)(Cl)Br H298:-48.28 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Br)CBr smiles:C=C(F)C(Cl)(Br)CBr H298:-39.39 kcal/mol
library:CHOFClBr_G4 label:CCDC(F)C(Cl)Br smiles:CC=C(F)C(Cl)Br H298:-46.68 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)Br smiles:C=C(F)C(Cl)Br H298:-38.58 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Br)C(F)Cl smiles:CC(Br)=C(Br)C(F)Cl H298:-41.42 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Br)Br smiles:FC=C(Cl)C(Br)Br H298:-30.28 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Br)OBr smiles:C=C(F)C(Cl)(Br)OBr H298:-39.16 kcal/mol
library:CHOFClBr_G4 label:ODCDC(Br)C(F)Cl smiles:O=C=C(Br)C(F)Cl H298:-54.97 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)(Cl)OBr smiles:C=C(F)C(Cl)(Cl)OBr H298:-51.80 kcal/mol
library:CHOFClBr_G4 label:OCDC(Br)C(F)Cl smiles:OC=C(Br)C(F)Cl H298:-80.45 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Cl)Br smiles:FC=C(Cl)C(Cl)Br H298:-41.48 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)(Cl)CBr smiles:C=C(F)C(F)(Cl)CBr H298:-92.04 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)C(F)F smiles:CC(Br)=C(Cl)C(F)F H298:-99.96 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(O)(Cl)Br smiles:C=C(F)C(O)(Cl)Br H298:-80.30 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)Br smiles:C=C(F)C(Br)Br H298:-27.26 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)Br smiles:FC=C(F)C(F)Br H298:-117.54 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)DCF smiles:CC(Br)(Br)C(F)=CF H298:-75.88 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)Br smiles:C=C(F)C(F)Br H298:-78.76 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(C)(Br)Br smiles:C=C(F)C(C)(Br)Br H298:-36.67 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(O)(F)Br smiles:C=C(F)C(O)(F)Br H298:-125.64 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)DCOBr smiles:FC(Br)C(Br)=COBr H298:-27.33 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)OBr smiles:C=C(F)C(Br)(Br)OBr H298:-27.67 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)F smiles:OC(Br)=C(Br)C(F)F H298:-118.56 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)Br smiles:OC=C(Br)C(F)Br H298:-71.60 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(Br)Br smiles:CC=C(F)C(Br)Br H298:-35.46 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)F smiles:CC(Br)=C(Br)C(F)F H298:-88.20 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)Br smiles:FC=C(F)C(Br)Br H298:-66.53 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)Br smiles:O=C=C(Br)C(F)Br H298:-42.71 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(Br)Br smiles:C=C=C(F)C(Br)Br H298:11.55 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)F smiles:OC=C(Br)C(F)F H298:-129.37 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)OBr smiles:C=C(F)C(F)(Br)OBr H298:-84.36 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)Br smiles:CC(Br)=C(Br)C(F)Br H298:-29.21 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)C(F)Br smiles:C=C=C(F)C(F)Br H298:-39.55 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)DCF smiles:OC(Br)(Br)C(F)=CF H298:-107.53 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)DCOBr smiles:FC(F)C(Br)=COBr H298:-84.85 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)DCF smiles:OC(F)(Br)C(F)=CF H298:-161.23 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(C)(F)Br smiles:C=C(F)C(C)(F)Br H298:-90.75 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(F)Br smiles:FC(F)=C(F)C(F)Br H298:-162.36 kcal/mol
library:CHOFBr_G4 label:FCCDC(F)C(Br)Br smiles:FCC=C(F)C(Br)Br H298:-77.01 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(Br)Br smiles:FC(F)=C(F)C(Br)Br H298:-111.54 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)DCCBr smiles:FC(F)C(Br)=CCBr H298:-86.94 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)C(F)F smiles:O=C=C(Br)C(F)F H298:-99.69 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(O)(Br)Br smiles:C=C(F)C(O)(Br)Br H298:-68.30 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)DCF smiles:CC(F)(Br)C(F)=CF H298:-129.74 kcal/mol
library:CHOFBr_G4 label:FCCDC(F)C(F)Br smiles:FCC=C(F)C(F)Br H298:-128.18 kcal/mol
library:CHOFBr_G4 label:FCDCDC(F)C(Br)Br smiles:FC=C=C(F)C(Br)Br H298:-29.62 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(Br)CBr smiles:C=C(F)C(F)(Br)CBr H298:-83.22 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(Br)Br smiles:CC(F)=C(F)C(Br)Br H298:-77.69 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)Br smiles:OC(Br)=C(Br)C(F)Br H298:-61.64 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)Br smiles:CC=C(Br)C(F)Br H298:-37.05 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(F)Br smiles:CC(F)=C(F)C(F)Br H298:-130.05 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)(Br)CBr smiles:C=C(F)C(Br)(Br)CBr H298:-29.58 kcal/mol
library:CHOFBr_G4 label:FCDCDC(F)C(F)Br smiles:FC=C=C(F)C(F)Br H298:-80.41 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)C(F)F smiles:CC=C(Br)C(F)F H298:-94.64 kcal/mol
library:CHOFBr_G4 label:CCDC(F)C(F)Br smiles:CC=C(F)C(F)Br H298:-87.10 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Cl)Br smiles:C=C=C(Cl)C(Cl)Br H298:36.41 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)Br smiles:C=C(Cl)C(Br)Br H298:11.53 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)(Br)CBr smiles:C=C(Cl)C(Br)(Br)CBr H298:9.07 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(C)(Cl)Br smiles:C=C(Cl)C(C)(Cl)Br H298:-8.99 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)C(Cl)Br smiles:CC=C(Br)C(Cl)Br H298:3.04 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)C(Cl)Br smiles:CC(Br)=C(Br)C(Cl)Br H298:8.01 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(C)(Br)Br smiles:C=C(Cl)C(C)(Br)Br H298:2.87 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Br)OBr smiles:C=C(Cl)C(Cl)(Br)OBr H298:-0.55 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Cl smiles:OC=C(Br)C(Cl)Cl H298:-42.92 kcal/mol
library:CHOClBr_G4 label:ODCDC(Br)C(Cl)Br smiles:O=C=C(Br)C(Cl)Br H298:-1.91 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)Br smiles:C=C(Cl)C(Cl)Br H298:0.19 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)C(Br)Br smiles:C=C=C(Cl)C(Br)Br H298:47.67 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Br)Br smiles:ClC=C(Cl)C(Br)Br H298:6.43 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(O)(Cl)Br smiles:C=C(Cl)C(O)(Cl)Br H298:-41.20 kcal/mol
library:CHOClBr_G4 label:ODCDC(Br)C(Cl)Cl smiles:O=C=C(Br)C(Cl)Cl H298:-13.40 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Br smiles:OC=C(Br)C(Cl)Br H298:-31.50 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)(Br)CBr smiles:C=C(Cl)C(Cl)(Br)CBr H298:-0.42 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)C(Cl)Cl smiles:CC(Br)=C(Br)C(Cl)Cl H298:-3.20 kcal/mol
library:CHOClBr_G4 label:CCDC(Cl)C(Br)Br smiles:CC=C(Cl)C(Br)Br H298:2.58 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)C(Cl)Cl smiles:CC=C(Br)C(Cl)Cl H298:-8.35 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Cl)DCCl smiles:CC(Br)(Br)C(Cl)=CCl H298:-2.44 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)(Br)OBr smiles:C=C(Cl)C(Br)(Br)OBr H298:11.04 kcal/mol
library:CHOClBr_G4 label:CCDC(Cl)C(Cl)Br smiles:CC=C(Cl)C(Cl)Br H298:-8.74 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(O)(Br)Br smiles:C=C(Cl)C(O)(Br)Br H298:-29.15 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)C(Cl)Br smiles:ClC=C(Cl)C(Cl)Br H298:-4.68 kcal/mol
""",
)

entry(
    index = 76,
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
        Cpdata = ([-0.00832893,0.0830613,0.0886107,0.0715734,0.0730917,0.104164,0.38665],'cal/(mol*K)','+|-',[0.158614,0.182295,0.18635,0.183616,0.15922,0.137326,0.111917]),
        H298 = (3.9659,'kcal/mol','+|-',0.565446),
        S298 = (1.36426,'cal/(mol*K)','+|-',0.385386),
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
library:CHOFBr_G4 label:CDC(F)C(F)(F)OBr smiles:C=C(F)C(F)(F)OBr H298:-145.73 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)C(F)F smiles:OC(Br)=C(F)C(F)F H298:-166.31 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)C(F)F smiles:CC(Br)=C(F)C(F)F H298:-136.61 kcal/mol
library:CHOFBr_G4 label:FC(DCCBr)C(F)F smiles:FC(=CCBr)C(F)F H298:-136.43 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)(F)CBr smiles:C=C(F)C(F)(F)CBr H298:-139.80 kcal/mol
library:CHOFBr_G4 label:FC(DCOBr)C(F)F smiles:FC(=COBr)C(F)F H298:-131.07 kcal/mol
""",
)

entry(
    index = 77,
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
        Cpdata = ([-0.374639,-0.200608,-0.0350328,0.0673066,0.188528,0.21298,0.282395],'cal/(mol*K)','+|-',[0.212482,0.244205,0.249637,0.245975,0.213293,0.183963,0.149926]),
        H298 = (1.7071,'kcal/mol','+|-',0.75748),
        S298 = (1.73968,'cal/(mol*K)','+|-',0.516268),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCCDC(Br)C(Br)Br smiles:BrCC=C(Br)C(Br)Br H298:21.10 kcal/mol
library:CHOBr_G4 label:ODCDC(Br)C(Br)Br smiles:O=C=C(Br)C(Br)Br H298:9.26 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(O)(Br)Br smiles:C=C(Br)C(O)(Br)Br H298:-16.94 kcal/mol
library:CHOBr_G4 label:CCDC(Br)C(Br)Br smiles:CC=C(Br)C(Br)Br H298:14.35 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)Br smiles:C=C(Br)C(Br)Br H298:23.21 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(C)(Br)Br smiles:C=C(Br)C(C)(Br)Br H298:14.86 kcal/mol
library:CHOBr_G4 label:OCDC(Br)C(Br)Br smiles:OC=C(Br)C(Br)Br H298:-20.23 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)C(Br)Br smiles:BrOC=C(Br)C(Br)Br H298:23.66 kcal/mol
library:CHOBr_G4 label:CDCDC(Br)C(Br)Br smiles:C=C=C(Br)C(Br)Br H298:58.54 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)Br smiles:BrC=C(Br)C(Br)Br H298:29.50 kcal/mol
library:CHOFBr_G4 label:FCDCDC(Br)C(Br)Br smiles:FC=C=C(Br)C(Br)Br H298:18.81 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)Br smiles:FC=C(Br)C(Br)Br H298:-19.13 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)C(Br)Br smiles:FC(F)=C(Br)C(Br)Br H298:-65.34 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)C(Br)Br smiles:CC(F)=C(Br)C(Br)Br H298:-31.49 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)DCF smiles:CC(Br)(Br)C(Br)=CF H298:-27.75 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)DCF smiles:OC(Br)(Br)C(Br)=CF H298:-59.58 kcal/mol
library:CHOFBr_G4 label:FCCDC(Br)C(Br)Br smiles:FCC=C(Br)C(Br)Br H298:-26.83 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)C(Br)Br smiles:FC(Br)=C(Br)C(Br)Br H298:-11.92 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)C(Br)Br smiles:ClC=C(Br)C(Br)Br H298:17.97 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Br)DCCl smiles:CC(Br)(Br)C(Br)=CCl H298:9.32 kcal/mol
""",
)

entry(
    index = 78,
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
    index = 79,
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
        Cpdata = ([-0.145298,-0.119167,-0.0859063,-0.0789092,-0.0736843,-0.0466396,0.0579328],'cal/(mol*K)','+|-',[0.0367753,0.0422657,0.0432059,0.042572,0.0369157,0.0318395,0.0259484]),
        H298 = (1.211,'kcal/mol','+|-',0.131101),
        S298 = (1.08994,'cal/(mol*K)','+|-',0.0893531),
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
library:CHOFClBr_G4 label:FC(F)C(Cl)CBr smiles:FC(F)C(Cl)CBr H298:-122.74 kcal/mol
library:CHOFClBr_G4 label:FC#CC(Cl)CBr smiles:FC#CC(Cl)CBr H298:13.52 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)OBr smiles:CC(F)C(Cl)OBr H298:-80.70 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)OOBr smiles:FCC(Cl)OOBr H298:-54.17 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(CF)OBr smiles:CC(Cl)(CF)OBr H298:-82.24 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)COBr smiles:FCC(Cl)COBr H298:-74.65 kcal/mol
library:CHOFClBr_G4 label:FCDCC(Cl)CBr smiles:FC=CC(Cl)CBr H298:-47.43 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)OBr smiles:FCC(Cl)OBr H298:-71.02 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)CF smiles:O=C(Br)C(Cl)CF H298:-95.03 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)CF smiles:CC(Br)C(Cl)CF H298:-79.44 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Cl)CBr smiles:FC(Cl)C(Cl)CBr H298:-77.48 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(CF)CBr smiles:OC(Cl)(CF)CBr H298:-114.31 kcal/mol
library:CHOFClBr_G4 label:CC(F)(CCl)OBr smiles:CC(F)(CCl)OBr H298:-87.83 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)CBr smiles:C=C(F)C(Cl)CBr H298:-48.10 kcal/mol
library:CHOFClBr_G4 label:FCCC(Cl)CBr smiles:FCCC(Cl)CBr H298:-78.34 kcal/mol
library:CHOFClBr_G4 label:OC(Cl)(CF)OBr smiles:OC(Cl)(CF)OBr H298:-116.46 kcal/mol
library:CHOFClBr_G4 label:CC(F)(CCl)CBr smiles:CC(F)(CCl)CBr H298:-82.81 kcal/mol
library:CHOFClBr_G4 label:OC(F)C(Cl)OBr smiles:OC(F)C(Cl)OBr H298:-117.38 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Cl)Br smiles:FCC(Cl)C(Cl)Br H298:-73.00 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)CBr smiles:FCC(Cl)CBr H298:-70.76 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)C(Br)Br smiles:FCC(Cl)C(Br)Br H298:-61.59 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)CCBr smiles:FCC(Cl)CCBr H298:-78.21 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)OCBr smiles:FCC(Cl)OCBr H298:-102.55 kcal/mol
library:CHOFClBr_G4 label:CC(F)C(Cl)CBr smiles:CC(F)C(Cl)CBr H298:-79.52 kcal/mol
library:CHOFClBr_G4 label:CC(Cl)(CF)CBr smiles:CC(Cl)(CF)CBr H298:-80.72 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)OF smiles:OC(Br)C(Cl)OF H298:-67.47 kcal/mol
library:CHOFClBr_G4 label:CC(Br)(Br)C(Cl)CF smiles:CC(Br)(Br)C(Cl)CF H298:-71.91 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)CF smiles:OC(Br)C(Cl)CF H298:-111.52 kcal/mol
library:CHOFBr_G4 label:FCCBr smiles:FCCBr H298:-58.00 kcal/mol
library:CHOFBr_G4 label:OCC(Br)CF smiles:OCC(Br)CF H298:-102.26 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CF)CBr smiles:FCC(F)(CF)CBr H298:-161.22 kcal/mol
library:CHOFBr_G4 label:CC(F)C(C)Br smiles:CC(F)C(C)Br H298:-76.98 kcal/mol
library:CHOFBr_G4 label:CC(F)C(O)Br smiles:CC(F)C(O)Br H298:-107.95 kcal/mol
library:CHOFBr_G4 label:OC(Br)CF smiles:OC(Br)CF H298:-97.30 kcal/mol
library:CHOFBr_G4 label:CCC(Br)CF smiles:CCC(Br)CF H298:-71.86 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)OBr smiles:FCC(F)C(Br)OBr H298:-109.69 kcal/mol
library:CHOFBr_G4 label:C#CC(F)CBr smiles:C#CC(F)CBr H298:3.38 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)C(Br)Br smiles:OC(Br)(CF)C(Br)Br H298:-93.15 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)OBr smiles:CC(F)(CBr)OBr H298:-77.46 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)CBr smiles:FCC(Br)C(Br)CBr H298:-60.01 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)CF smiles:O=CC(Br)CF H298:-81.11 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)CF smiles:CC(Br)C(Br)CF H298:-68.47 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)Br smiles:CC(F)(CBr)C(F)Br H298:-114.66 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(Br)Br smiles:CC(F)(CBr)C(Br)Br H298:-62.17 kcal/mol
library:CHOFBr_G4 label:FC(CBr)C(F)(F)F smiles:FC(CBr)C(F)(F)F H298:-218.22 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(F)CBr smiles:CC(F)(F)C(F)CBr H298:-174.68 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)OBr smiles:OC(Br)(CF)OBr H298:-103.83 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)CBr smiles:CC(F)(CF)CBr H298:-119.96 kcal/mol
library:CHOFBr_G4 label:CC(O)(F)CBr smiles:CC(O)(F)CBr H298:-118.11 kcal/mol
library:CHOFBr_G4 label:FCCC(F)CBr smiles:FCCC(F)CBr H298:-117.00 kcal/mol
library:CHOFBr_G4 label:OC(F)(CBr)C(F)F smiles:OC(F)(CBr)C(F)F H298:-210.80 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OBr smiles:FCC(Br)OBr H298:-59.12 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)C(F)F smiles:OC(Br)C(F)C(F)F H298:-201.12 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)Br smiles:FCC(Br)C(Br)Br H298:-50.43 kcal/mol
library:CHOFBr_G4 label:CC(F)CBr smiles:CC(F)CBr H298:-68.03 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)C(Br)Br smiles:CC(Br)(CF)C(Br)Br H298:-60.41 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)CF smiles:O=C(Br)C(Br)CF H298:-84.59 kcal/mol
library:CHOFBr_G4 label:FCC(Br)COBr smiles:FCC(Br)COBr H298:-63.57 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OOBr smiles:FCC(Br)OOBr H298:-42.28 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)CBr smiles:OC(F)(CF)CBr H298:-158.96 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)OBr smiles:FCC(F)(CBr)OBr H298:-117.96 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CC(Br)Br smiles:FCC(Br)CC(Br)Br H298:-60.39 kcal/mol
library:CHOFBr_G4 label:CC(C)(Br)CF smiles:CC(C)(Br)CF H298:-76.14 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)CBr smiles:FCC(Br)(CBr)CBr H298:-62.39 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)OBr smiles:CC(F)C(Br)OBr H298:-67.90 kcal/mol
library:CHOFBr_G4 label:OC(O)(Br)CF smiles:OC(O)(Br)CF H298:-144.54 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)CBr smiles:CC(Br)(CF)CBr H298:-69.37 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)CBr smiles:FC#CC(F)CBr H298:-25.35 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)OBr smiles:CC(Br)(CF)OBr H298:-70.29 kcal/mol
library:CHOFBr_G4 label:CC(C)(F)CBr smiles:CC(C)(F)CBr H298:-78.61 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)CBr smiles:CC(F)C(F)CBr H298:-120.04 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)CF smiles:CC(Br)(Br)C(Br)CF H298:-60.25 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)CBr smiles:FC=C(F)C(F)CBr H298:-127.55 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)OBr smiles:FCC(Br)(CBr)OBr H298:-62.07 kcal/mol
library:CHOFBr_G4 label:CDCC(F)CBr smiles:C=CC(F)CBr H298:-40.31 kcal/mol
library:CHOFBr_G4 label:COC(Br)CF smiles:COC(Br)CF H298:-94.72 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)CBr smiles:CC(F)C(Br)CBr H298:-69.65 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)CBr smiles:FCC(F)(CBr)CBr H298:-112.76 kcal/mol
library:CHOFBr_G4 label:FOC(F)C(Br)OBr smiles:FOC(F)C(Br)OBr H298:-70.70 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OCBr smiles:FCC(Br)OCBr H298:-90.84 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)CBr smiles:FC(F)=CC(F)CBr H298:-134.82 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)CF smiles:CC(Br)C(F)CF H298:-118.24 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CCBr smiles:FCC(Br)CCBr H298:-67.13 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)CF smiles:OC(Br)C(Br)CF H298:-100.47 kcal/mol
library:CHOFBr_G4 label:OC(F)C(O)Br smiles:OC(F)C(O)Br H298:-145.97 kcal/mol
library:CHOFBr_G4 label:CC(Br)CF smiles:CC(Br)CF H298:-66.66 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)C(Br)Br smiles:CC(F)C(Br)C(Br)Br H298:-61.28 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)C(F)F smiles:CC(Br)C(F)C(F)F H298:-170.06 kcal/mol
library:CHOFBr_G4 label:OOC(Br)CF smiles:OOC(Br)CF H298:-78.49 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)CBr smiles:FCC(F)C(F)CBr H298:-159.76 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CBr smiles:FCC(Br)CBr H298:-59.66 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)(Br)Br smiles:FCC(Br)C(Br)(Br)Br H298:-38.66 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)CBr smiles:C=C(F)C(F)CBr H298:-87.34 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(OBr)OBr smiles:FCC(Br)(OBr)OBr H298:-63.74 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)CBr smiles:OC(Br)(CF)CBr H298:-101.20 kcal/mol
library:CHOFBr_G4 label:CCC(F)CBr smiles:CCC(F)CBr H298:-73.04 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)CF smiles:OC(Br)C(F)CF H298:-148.67 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)CBr smiles:FC=CC(F)CBr H298:-85.36 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)CBr smiles:CC(F)(CBr)CBr H298:-71.80 kcal/mol
library:CHOFBr_G4 label:FCC(Br)OC(Br)Br smiles:FCC(Br)OC(Br)Br H298:-82.37 kcal/mol
library:CHOFBr_G4 label:OC(F)C(Br)OBr smiles:OC(F)C(Br)OBr H298:-105.42 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)OBr smiles:FCC(Br)C(Br)OBr H298:-60.29 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)OF smiles:OC(Br)C(F)OF H298:-109.78 kcal/mol
library:CHOFBr_G4 label:CC(O)(Br)CF smiles:CC(O)(Br)CF H298:-108.80 kcal/mol
library:CHOFBr_G4 label:CC(F)(CBr)C(F)F smiles:CC(F)(CBr)C(F)F H298:-172.69 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)CBr smiles:FCC(F)C(Br)CBr H298:-109.95 kcal/mol
library:CHOFBr_G4 label:FC(F)C(F)CBr smiles:FC(F)C(F)CBr H298:-161.37 kcal/mol
library:CHOFBr_G4 label:FC(F)CC(F)CBr smiles:FC(F)CC(F)CBr H298:-169.97 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)CF smiles:OC(Br)(Br)C(Br)CF H298:-90.95 kcal/mol
library:CHOFBr_G4 label:FCC(F)CBr smiles:FCC(F)CBr H298:-108.81 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CBr)CBr smiles:CC(Cl)(CBr)CBr H298:-32.30 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)CBr smiles:ClCC(Cl)CBr H298:-33.48 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)OOBr smiles:ClCC(Br)OOBr H298:-4.76 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)COBr smiles:ClCC(Br)COBr H298:-25.98 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)CCl smiles:CC(Br)C(Cl)CCl H298:-42.23 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)OCl smiles:OC(Br)C(Cl)OCl H298:-64.08 kcal/mol
library:CHOClBr_G4 label:ClCCC(Cl)CBr smiles:ClCCC(Cl)CBr H298:-40.60 kcal/mol
library:CHOClBr_G4 label:CCC(Cl)CBr smiles:CCC(Cl)CBr H298:-34.41 kcal/mol
library:CHOClBr_G4 label:CC(Cl)CBr smiles:CC(Cl)CBr H298:-29.10 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Cl)CBr smiles:CC(Cl)C(Cl)CBr H298:-41.84 kcal/mol
library:CHOClBr_G4 label:CC(C)(Cl)CBr smiles:CC(C)(Cl)CBr H298:-38.57 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)CBr smiles:CC(Cl)C(Br)CBr H298:-30.61 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(Br)OBr smiles:OC(Cl)C(Br)OBr H298:-59.79 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)CBr smiles:C=C(Cl)C(Cl)CBr H298:-10.99 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)CBr smiles:C=CC(Cl)CBr H298:-2.46 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)OBr smiles:CC(Br)(CCl)OBr H298:-32.98 kcal/mol
library:CHOClBr_G4 label:OC(Br)(CCl)CBr smiles:OC(Br)(CCl)CBr H298:-64.26 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)CCl smiles:CC(Br)C(Br)CCl H298:-31.26 kcal/mol
library:CHOClBr_G4 label:CC(O)(Cl)CBr smiles:CC(O)(Cl)CBr H298:-72.65 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)CBr smiles:C#CC(Cl)CBr H298:41.79 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CCl)CBr smiles:CC(Cl)(CCl)CBr H298:-43.25 kcal/mol
library:CHOClBr_G4 label:ClCCBr smiles:ClCCBr H298:-20.47 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)CCl smiles:O=CC(Br)CCl H298:-43.86 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)CBr smiles:ClCC(Br)CBr H298:-22.57 kcal/mol
library:CHOClBr_G4 label:COC(Br)CCl smiles:COC(Br)CCl H298:-57.22 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)OBr smiles:ClCC(Br)OBr H298:-21.56 kcal/mol
library:CHOClBr_G4 label:OC(Cl)(CCl)CBr smiles:OC(Cl)(CCl)CBr H298:-76.20 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Cl)CBr smiles:ClC=CC(Cl)CBr H298:-9.48 kcal/mol
library:CHOClBr_G4 label:OC(Br)CCl smiles:OC(Br)CCl H298:-60.18 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)CCl smiles:OC(Br)C(Br)CCl H298:-60.39 kcal/mol
library:CHOClBr_G4 label:OC(Br)(CCl)OBr smiles:OC(Br)(CCl)OBr H298:-66.40 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)CBr smiles:CC(Br)(CCl)CBr H298:-31.97 kcal/mol
library:CHOClBr_G4 label:OC(Cl)C(O)Br smiles:OC(Cl)C(O)Br H298:-102.25 kcal/mol
library:CHOClBr_G4 label:ClC#CC(Cl)CBr smiles:ClC#CC(Cl)CBr H298:41.26 kcal/mol
library:CHOClBr_G4 label:CCC(Br)CCl smiles:CCC(Br)CCl H298:-34.32 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)C(Br)Br smiles:CC(Br)(CCl)C(Br)Br H298:-21.40 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)OBr smiles:CC(Cl)C(Br)OBr H298:-29.03 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)C(Br)Br smiles:ClCC(Br)C(Br)Br H298:-13.29 kcal/mol
library:CHOClBr_G4 label:CC(Br)CCl smiles:CC(Br)CCl H298:-28.97 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Cl)CBr smiles:ClC(Cl)C(Cl)CBr H298:-36.54 kcal/mol
library:CHOClBr_G4 label:OC(O)(Br)CCl smiles:OC(O)(Br)CCl H298:-107.04 kcal/mol
library:CHOClBr_G4 label:CC(C)(Br)CCl smiles:CC(C)(Br)CCl H298:-38.27 kcal/mol
library:CHOClBr_G4 label:OOC(Br)CCl smiles:OOC(Br)CCl H298:-40.85 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)CCl smiles:OC(Br)C(Cl)CCl H298:-72.03 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)CCl smiles:O=C(Br)C(Br)CCl H298:-47.62 kcal/mol
library:CHOClBr_G4 label:CC(O)(Br)CCl smiles:CC(O)(Br)CCl H298:-71.50 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)CCBr smiles:ClCC(Br)CCBr H298:-32.10 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(C)Br smiles:CC(Cl)C(C)Br H298:-36.96 kcal/mol
library:CHOClBr_G4 label:OCC(Br)CCl smiles:OCC(Br)CCl H298:-64.59 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(O)Br smiles:CC(Cl)C(O)Br H298:-67.88 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)OCBr smiles:ClCC(Br)OCBr H298:-53.44 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(CBr)OBr smiles:CC(Cl)(CBr)OBr H298:-33.92 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Br)CCl smiles:CC(Br)(Br)C(Br)CCl H298:-23.29 kcal/mol
""",
)

entry(
    index = 80,
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
        Cpdata = ([-0.148682,-0.0760222,0.0144627,0.0592617,0.0805109,0.10537,0.176623],'cal/(mol*K)','+|-',[0.0437049,0.0502299,0.0513473,0.050594,0.0438718,0.037839,0.030838]),
        H298 = (1.71275,'kcal/mol','+|-',0.155804),
        S298 = (0.707187,'cal/(mol*K)','+|-',0.10619),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOF_G4 label:FCC(F)(C(F)F)C(F)F smiles:FCC(F)(C(F)F)C(F)F H298:-312.22 kcal/mol
library:CHOF_G4 label:OC(F)C(F)OF smiles:OC(F)C(F)OF H298:-167.37 kcal/mol
library:CHOF_G4 label:CC(F)(CF)OF smiles:CC(F)(CF)OF H298:-133.59 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)(F)OF smiles:FCC(F)C(F)(F)OF H298:-223.34 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)DC(F)F smiles:FCC(F)C(F)=C(F)F H298:-219.99 kcal/mol
library:CHOF_G4 label:COC(F)CF smiles:COC(F)CF H298:-149.37 kcal/mol
library:CHOF_G4 label:FOC(F)C(F)C(F)F smiles:FOC(F)C(F)C(F)F H298:-222.80 kcal/mol
library:CHOF_G4 label:FCC(F)(OF)C(F)(F)F smiles:FCC(F)(OF)C(F)(F)F H298:-275.95 kcal/mol
library:CHOF_G4 label:FCC(F)CC(F)(F)F smiles:FCC(F)CC(F)(F)F H298:-277.64 kcal/mol
library:CHOF_G4 label:OC(F)C(F)CF smiles:OC(F)C(F)CF H298:-204.94 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)C(F)F smiles:FCC(F)C(F)C(F)F H298:-261.79 kcal/mol
library:CHOF_G4 label:OC(F)C(O)F smiles:OC(F)C(O)F H298:-201.91 kcal/mol
library:CHOF_G4 label:ODCC(F)CF smiles:O=CC(F)CF H298:-130.64 kcal/mol
library:CHOF_G4 label:OCC(F)CF smiles:OCC(F)CF H298:-151.68 kcal/mol
library:CHOF_G4 label:FCCC(F)CF smiles:FCCC(F)CF H298:-165.49 kcal/mol
library:CHOF_G4 label:C#CC(F)CF smiles:C#CC(F)CF H298:-45.83 kcal/mol
library:CHOF_G4 label:FCC(F)C(F)CF smiles:FCC(F)C(F)CF H298:-209.28 kcal/mol
library:CHOF_G4 label:FCCF smiles:FCCF H298:-106.96 kcal/mol
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
library:CHOFClBr_G4 label:FCC(F)C(Cl)Br smiles:FCC(F)C(Cl)Br H298:-112.49 kcal/mol
library:CHOFBr_G4 label:FCC(F)OCBr smiles:FCC(F)OCBr H298:-145.13 kcal/mol
library:CHOFBr_G4 label:FCC(F)OBr smiles:FCC(F)OBr H298:-113.64 kcal/mol
library:CHOFBr_G4 label:FCC(F)CCBr smiles:FCC(F)CCBr H298:-116.78 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CF)CBr smiles:FCC(F)(CF)CBr H298:-161.22 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)(Br)Br smiles:FCC(F)C(Br)(Br)Br H298:-89.47 kcal/mol
library:CHOFBr_G4 label:FOC(F)C(F)OBr smiles:FOC(F)C(F)OBr H298:-126.19 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)CF smiles:CC(F)(Br)C(F)CF H298:-164.23 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)OBr smiles:FCC(F)C(Br)OBr H298:-109.69 kcal/mol
library:CHOFBr_G4 label:FCC(F)OC(Br)Br smiles:FCC(F)OC(Br)Br H298:-135.78 kcal/mol
library:CHOFBr_G4 label:OC(F)C(F)OBr smiles:OC(F)C(F)OBr H298:-158.72 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(Br)Br smiles:FCC(F)C(F)(Br)Br H298:-143.49 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)CBr smiles:CC(F)(CF)CBr H298:-119.96 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(F)Br smiles:OC(F)(CF)C(F)Br H298:-202.40 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)CF smiles:CC(Br)(Br)C(F)CF H298:-110.86 kcal/mol
library:CHOFBr_G4 label:FCC(F)(OBr)OBr smiles:FCC(F)(OBr)OBr H298:-121.21 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)C(Br)Br smiles:OC(F)(CF)C(Br)Br H298:-148.17 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)OBr smiles:FCC(F)C(F)OBr H298:-165.62 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)(F)Br smiles:FCC(F)C(F)(F)Br H298:-202.74 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(F)Br smiles:CC(F)C(F)C(F)Br H298:-162.99 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)CF smiles:O=C(Br)C(F)CF H298:-133.66 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)CBr smiles:OC(F)(CF)CBr H298:-158.96 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)OBr smiles:FCC(F)(CBr)OBr H298:-117.96 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)Br smiles:FCC(F)C(Br)Br H298:-100.89 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)OBr smiles:CC(F)C(F)OBr H298:-124.17 kcal/mol
library:CHOFBr_G4 label:FCC(F)(OF)OBr smiles:FCC(F)(OF)OBr H298:-126.89 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)CBr smiles:CC(F)C(F)CBr H298:-120.04 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)Br smiles:FCC(F)C(F)Br H298:-152.56 kcal/mol
library:CHOFBr_G4 label:FCC(F)CC(Br)Br smiles:FCC(F)CC(Br)Br H298:-112.92 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CBr)CBr smiles:FCC(F)(CBr)CBr H298:-112.76 kcal/mol
library:CHOFBr_G4 label:OC(F)(CF)OBr smiles:OC(F)(CF)OBr H298:-163.95 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)CF smiles:CC(Br)C(F)CF H298:-118.24 kcal/mol
library:CHOFBr_G4 label:CC(F)C(F)C(Br)Br smiles:CC(F)C(F)C(Br)Br H298:-111.37 kcal/mol
library:CHOFBr_G4 label:FCC(F)OC(F)Br smiles:FCC(F)OC(F)Br H298:-192.78 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(F)CBr smiles:FCC(F)C(F)CBr H298:-159.76 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)CF smiles:OC(F)(Br)C(F)CF H298:-199.92 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)OBr smiles:CC(F)(CF)OBr H298:-125.86 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)CF smiles:OC(Br)C(F)CF H298:-148.67 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(F)Br smiles:CC(F)(CF)C(F)Br H298:-163.90 kcal/mol
library:CHOFBr_G4 label:CC(F)(CF)C(Br)Br smiles:CC(F)(CF)C(Br)Br H298:-112.11 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)CF smiles:OC(Br)(Br)C(F)CF H298:-141.65 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)CBr smiles:FCC(F)C(Br)CBr H298:-109.95 kcal/mol
library:CHOFBr_G4 label:FCC(F)(CF)OBr smiles:FCC(F)(CF)OBr H298:-166.08 kcal/mol
library:CHOFBr_G4 label:FCC(F)COBr smiles:FCC(F)COBr H298:-113.33 kcal/mol
library:CHOFBr_G4 label:FCC(F)CC(F)Br smiles:FCC(F)CC(F)Br H298:-161.96 kcal/mol
library:CHOFBr_G4 label:FCC(F)OOBr smiles:FCC(F)OOBr H298:-97.12 kcal/mol
library:CHOFBr_G4 label:FCC(F)CBr smiles:FCC(F)CBr H298:-108.81 kcal/mol
""",
)

entry(
    index = 81,
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
        Cpdata = ([-0.241659,-0.152083,-0.0407121,0.0220502,0.0720941,0.108305,0.194193],'cal/(mol*K)','+|-',[0.0497913,0.0572249,0.0584979,0.0576397,0.0499813,0.0431085,0.0351324]),
        H298 = (0.907176,'kcal/mol','+|-',0.177502),
        S298 = (0.311152,'cal/(mol*K)','+|-',0.120978),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CC(Br)(Br)C(Br)CBr smiles:CC(Br)(Br)C(Br)CBr H298:-12.26 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)CBr smiles:BrC=CC(Br)CBr H298:13.55 kcal/mol
library:CHOBr_G4 label:BrCCBr smiles:BrCCBr H298:-9.56 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(OBr)OBr smiles:BrCC(Br)(OBr)OBr H298:-16.16 kcal/mol
library:CHOBr_G4 label:OCC(Br)CBr smiles:OCC(Br)CBr H298:-53.69 kcal/mol
library:CHOBr_G4 label:CC(O)(Br)CBr smiles:CC(O)(Br)CBr H298:-60.42 kcal/mol
library:CHOBr_G4 label:OC(Br)C(O)Br smiles:OC(Br)C(O)Br H298:-91.05 kcal/mol
library:CHOBr_G4 label:C#CC(Br)CBr smiles:C#CC(Br)CBr H298:52.37 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)CBr smiles:O=C(Br)C(Br)CBr H298:-37.86 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)OBr smiles:BrCC(Br)C(Br)OBr H298:-11.11 kcal/mol
library:CHOBr_G4 label:BrCC(Br)OC(Br)Br smiles:BrCC(Br)OC(Br)Br H298:-33.92 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)OBr smiles:CC(Br)(CBr)OBr H298:-22.15 kcal/mol
library:CHOBr_G4 label:OC(Br)(CBr)CBr smiles:OC(Br)(CBr)CBr H298:-53.34 kcal/mol
library:CHOBr_G4 label:CDCC(Br)CBr smiles:C=CC(Br)CBr H298:8.20 kcal/mol
library:CHOBr_G4 label:OOC(Br)CBr smiles:OOC(Br)CBr H298:-29.86 kcal/mol
library:CHOBr_G4 label:CC(C)(Br)CBr smiles:CC(C)(Br)CBr H298:-27.26 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)CBr smiles:BrC#CC(Br)CBr H298:62.77 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)C(Br)Br smiles:CC(Br)(CBr)C(Br)Br H298:-12.30 kcal/mol
library:CHOBr_G4 label:OC(O)(Br)CBr smiles:OC(O)(Br)CBr H298:-95.76 kcal/mol
library:CHOBr_G4 label:CC(Br)CBr smiles:CC(Br)CBr H298:-17.98 kcal/mol
library:CHOBr_G4 label:CC(Br)C(O)Br smiles:CC(Br)C(O)Br H298:-56.48 kcal/mol
library:CHOBr_G4 label:CC(Br)C(C)Br smiles:CC(Br)C(C)Br H298:-25.79 kcal/mol
library:CHOBr_G4 label:BrCC(Br)OBr smiles:BrCC(Br)OBr H298:-10.71 kcal/mol
library:CHOBr_G4 label:CCC(Br)CBr smiles:CCC(Br)CBr H298:-23.38 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(CBr)OBr smiles:BrCC(Br)(CBr)OBr H298:-14.61 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)OBr smiles:CC(Br)C(Br)OBr H298:-18.36 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)CBr smiles:OC(Br)C(Br)CBr H298:-52.04 kcal/mol
library:CHOBr_G4 label:OC(Br)CBr smiles:OC(Br)CBr H298:-49.15 kcal/mol
library:CHOBr_G4 label:COC(Br)CBr smiles:COC(Br)CBr H298:-46.41 kcal/mol
library:CHOBr_G4 label:ODCC(Br)CBr smiles:O=CC(Br)CBr H298:-33.05 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)OBr smiles:OC(Br)C(Br)OBr H298:-49.49 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)CBr smiles:CC(Br)C(Br)CBr H298:-20.43 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)(Br)Br smiles:BrCC(Br)C(Br)(Br)Br H298:9.04 kcal/mol
library:CHOBr_G4 label:BrCC(Br)(CBr)CBr smiles:BrCC(Br)(CBr)CBr H298:-14.07 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)C(Br)Br smiles:CC(Br)C(Br)C(Br)Br H298:-10.95 kcal/mol
library:CHOBr_G4 label:BrCC(Br)CC(Br)Br smiles:BrCC(Br)CC(Br)Br H298:-11.99 kcal/mol
library:CHOBr_G4 label:BrCC(Br)CBr smiles:BrCC(Br)CBr H298:-11.57 kcal/mol
library:CHOBr_G4 label:BrCC(Br)COBr smiles:BrCC(Br)COBr H298:-15.04 kcal/mol
library:CHOBr_G4 label:BrCC(Br)OOBr smiles:BrCC(Br)OOBr H298:6.10 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)Br smiles:BrCC(Br)C(Br)Br H298:-2.37 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)CBr smiles:BrC=C(Br)C(Br)CBr H298:17.17 kcal/mol
library:CHOBr_G4 label:OC(Br)(CBr)OBr smiles:OC(Br)(CBr)OBr H298:-55.51 kcal/mol
library:CHOBr_G4 label:CC(Br)(CBr)CBr smiles:CC(Br)(CBr)CBr H298:-21.11 kcal/mol
library:CHOBr_G4 label:BrCC(Br)CDC(Br)Br smiles:BrCC(Br)C=C(Br)Br H298:19.51 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)CBr smiles:BrCCC(Br)CBr H298:-20.28 kcal/mol
library:CHOBr_G4 label:BrOC(Br)C(Br)OBr smiles:BrOC(Br)C(Br)OBr H298:-9.68 kcal/mol
library:CHOBr_G4 label:BrCC(Br)C(Br)CBr smiles:BrCC(Br)C(Br)CBr H298:-12.07 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)CBr smiles:C=C(Br)C(Br)CBr H298:11.46 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)CBr smiles:BrCOC(Br)CBr H298:-42.66 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)C(Br)CBr smiles:FC(Cl)C(Br)CBr H298:-66.70 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)CBr smiles:FC=C(Br)C(Br)CBr H298:-31.33 kcal/mol
library:CHOFBr_G4 label:FCCC(Br)CBr smiles:FCCC(Br)CBr H298:-67.29 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)C(Br)CBr smiles:FC(Br)(Br)C(Br)CBr H298:-45.15 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(Br)CBr smiles:CC(F)(Br)C(Br)CBr H298:-65.48 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)CBr smiles:FCC(Br)C(Br)CBr H298:-60.01 kcal/mol
library:CHOFBr_G4 label:FOC(Br)C(Br)OBr smiles:FOC(Br)C(Br)OBr H298:-15.52 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)CF smiles:CC(Br)C(Br)CF H298:-68.47 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)C(Br)CBr smiles:FC(F)(Br)C(Br)CBr H298:-103.92 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)F smiles:OC(Br)(CBr)C(F)F H298:-153.43 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)F smiles:CC(Br)C(Br)C(F)F H298:-120.45 kcal/mol
library:CHOFBr_G4 label:FC(F)CC(Br)CBr smiles:FC(F)CC(Br)CBr H298:-121.34 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)CBr smiles:FC=CC(Br)CBr H298:-36.36 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)CBr smiles:FC#CC(Br)CBr H298:24.15 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)CBr smiles:FC(F)C(Br)CBr H298:-111.45 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)CBr smiles:FCC(Br)(CBr)CBr H298:-62.39 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CF)CBr smiles:CC(Br)(CF)CBr H298:-69.37 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)OF smiles:OC(Br)C(Br)OF H298:-55.44 kcal/mol
library:CHOFBr_G4 label:FCC(Br)(CBr)OBr smiles:FCC(Br)(CBr)OBr H298:-62.07 kcal/mol
library:CHOFBr_G4 label:CC(F)C(Br)CBr smiles:CC(F)C(Br)CBr H298:-69.65 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(Br)CBr smiles:FC(F)=CC(Br)CBr H298:-85.37 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)CF smiles:OC(Br)C(Br)CF H298:-100.47 kcal/mol
library:CHOFBr_G4 label:FC(Br)CC(Br)CBr smiles:FC(Br)CC(Br)CBr H298:-61.87 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)CBr smiles:FC=C(F)C(Br)CBr H298:-78.36 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)Br smiles:CC(Br)(CBr)C(F)Br H298:-63.05 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)Br smiles:OC(Br)C(Br)C(F)Br H298:-94.35 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)C(F)F smiles:OC(Br)C(Br)C(F)F H298:-152.41 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(Br)CBr smiles:CC(F)(F)C(Br)CBr H298:-123.94 kcal/mol
library:CHOFBr_G4 label:FCC(Br)CBr smiles:FCC(Br)CBr H298:-59.66 kcal/mol
library:CHOFBr_G4 label:CC(Br)(CBr)C(F)F smiles:CC(Br)(CBr)C(F)F H298:-120.70 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CF)CBr smiles:OC(Br)(CF)CBr H298:-101.20 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCC(Br)CBr smiles:FC(Br)=CC(Br)CBr H298:-30.63 kcal/mol
library:CHOFBr_G4 label:OC(Br)(CBr)C(F)Br smiles:OC(Br)(CBr)C(F)Br H298:-95.28 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)C(F)Br smiles:CC(Br)C(Br)C(F)Br H298:-62.55 kcal/mol
library:CHOFBr_G4 label:FCC(Br)C(Br)OBr smiles:FCC(Br)C(Br)OBr H298:-60.29 kcal/mol
library:CHOFBr_G4 label:FCC(F)C(Br)CBr smiles:FCC(F)C(Br)CBr H298:-109.95 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)CBr smiles:FC(Br)C(Br)CBr H298:-53.80 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)C(Br)CBr smiles:FC(F)(F)C(Br)CBr H298:-167.92 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)CBr smiles:C=C(Cl)C(Br)CBr H298:-0.38 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(Br)CBr smiles:CC(Cl)C(Br)CBr H298:-30.61 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CBr)C(Cl)Br smiles:CC(Br)(CBr)C(Cl)Br H298:-21.80 kcal/mol
library:CHOClBr_G4 label:OC(Br)(CCl)CBr smiles:OC(Br)(CCl)CBr H298:-64.26 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)CCl smiles:CC(Br)C(Br)CCl H298:-31.26 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)OCl smiles:OC(Br)C(Br)OCl H298:-52.02 kcal/mol
library:CHOClBr_G4 label:ClCCC(Br)CBr smiles:ClCCC(Br)CBr H298:-29.63 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)CBr smiles:ClCC(Br)CBr H298:-22.57 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)CCl smiles:OC(Br)C(Br)CCl H298:-60.39 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CCl)CBr smiles:CC(Br)(CCl)CBr H298:-31.97 kcal/mol
library:CHOClBr_G4 label:CC(Br)(CBr)C(Cl)Cl smiles:CC(Br)(CBr)C(Cl)Cl H298:-33.52 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)C(Br)CBr smiles:ClC(Cl)C(Br)CBr H298:-25.18 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Br)CBr smiles:ClC=CC(Br)CBr H298:1.65 kcal/mol
""",
)

entry(
    index = 82,
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
        Cpdata = ([-0.487245,-0.366436,-0.26625,-0.211496,-0.0949754,-0.000924522,0.319447],'cal/(mol*K)','+|-',[0.112658,0.129477,0.132358,0.130416,0.113088,0.0975375,0.0794909]),
        H298 = (2.0618,'kcal/mol','+|-',0.401616),
        S298 = (2.25071,'cal/(mol*K)','+|-',0.273726),
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
library:CHOFClBr_G4 label:CDC(F)C(Cl)C(Br)Br smiles:C=C(F)C(Cl)C(Br)Br H298:-38.34 kcal/mol
library:CHOFClBr_G4 label:CC(F)DC(Cl)CBr smiles:CC(F)=C(Cl)CBr H298:-51.39 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)CBr smiles:FC(Cl)=C(Cl)CBr H298:-44.45 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)DCOBr smiles:FCC(Cl)=COBr H298:-44.04 kcal/mol
library:CHOFClBr_G4 label:FCDCDC(Cl)CBr smiles:FC=C=C(Cl)CBr H298:-1.12 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CBr smiles:FC=C(Cl)CBr H298:-39.27 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)CBr smiles:FC(F)=C(Cl)CBr H298:-85.59 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(Cl)CF smiles:OC(Br)=C(Cl)CF H298:-80.74 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)C(Cl)Br smiles:C=C(F)C(Cl)C(Cl)Br H298:-50.05 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)CBr smiles:C=C(F)C(Cl)CBr H298:-48.10 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)DCF smiles:OC(Br)C(Cl)=CF H298:-77.52 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)DCF smiles:CC(Br)C(Cl)=CF H298:-47.65 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)OBr smiles:C=C(F)C(Cl)OBr H298:-47.17 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)CF smiles:CC(Br)=C(Cl)CF H298:-47.88 kcal/mol
library:CHOFClBr_G4 label:FCCDC(Cl)CBr smiles:FCC=C(Cl)CBr H298:-47.03 kcal/mol
library:CHOFClBr_G4 label:FCC(Cl)DCCBr smiles:FCC(Cl)=CCBr H298:-47.72 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)CF smiles:OC(Br)=C(Br)CF H298:-66.56 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)CBr smiles:FCC(Br)=C(Br)CBr H298:-28.66 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DCF smiles:OC(Br)C(F)=CF H298:-114.08 kcal/mol
library:CHOFBr_G4 label:FC(F)DCDC(F)CBr smiles:FC(F)=C=C(F)CBr H298:-85.82 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)CBr smiles:CC(F)=C(F)CBr H298:-88.35 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CBr smiles:FC=C(F)CBr H298:-76.26 kcal/mol
library:CHOFBr_G4 label:CCDC(Br)CF smiles:CC=C(Br)CF H298:-42.36 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCC(Br)Br smiles:FCC(Br)=CC(Br)Br H298:-28.84 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)CBr smiles:FCC(F)=C(F)CBr H298:-127.47 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)OBr smiles:FC=C(F)C(Br)OBr H298:-74.68 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCCBr smiles:FCC(Br)=CCBr H298:-35.96 kcal/mol
library:CHOFBr_G4 label:FC(DCC(F)F)CBr smiles:FC(=CC(F)F)CBr H298:-138.94 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)CF smiles:OC=C(Br)CF H298:-77.41 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DC(F)F smiles:OC(Br)C(F)=C(F)F H298:-158.85 kcal/mol
library:CHOFBr_G4 label:FCCDC(F)CBr smiles:FCC=C(F)CBr H298:-85.96 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DC(F)F smiles:CC(Br)C(F)=C(F)F H298:-129.33 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)C(Br)Br smiles:C=C(F)C(Br)C(Br)Br H298:-29.62 kcal/mol
library:CHOFBr_G4 label:CDCDC(F)CBr smiles:C=C=C(F)CBr H298:2.48 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)CBr smiles:FC=C(F)C(Br)CBr H298:-78.36 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCOBr smiles:FCC(Br)=COBr H298:-32.76 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DCF smiles:CC(Br)C(F)=CF H298:-84.36 kcal/mol
library:CHOFBr_G4 label:CDC(F)CBr smiles:C=C(F)CBr H298:-36.59 kcal/mol
library:CHOFBr_G4 label:FCDCDC(F)CBr smiles:FC=C=C(F)CBr H298:-39.14 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(C)Br smiles:C=C(F)C(C)Br H298:-44.43 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(O)Br smiles:C=C(F)C(O)Br H298:-75.09 kcal/mol
library:CHOFBr_G4 label:CCDC(F)CBr smiles:CC=C(F)CBr H298:-44.32 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)OBr smiles:C=C(F)C(Br)OBr H298:-35.30 kcal/mol
library:CHOFBr_G4 label:ODCDC(Br)CF smiles:O=C=C(Br)CF H298:-48.63 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CBr smiles:FC(F)=C(F)CBr H298:-121.28 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)CF smiles:CC(Br)=C(Br)CF H298:-36.17 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)OBr smiles:FCC(Br)=C(Br)OBr H298:-26.22 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)CCl smiles:CC(Br)=C(Br)CCl H298:-0.16 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)CBr smiles:ClC(Cl)=C(Cl)CBr H298:-5.92 kcal/mol
library:CHOClBr_G4 label:CDCDC(Cl)CBr smiles:C=C=C(Cl)CBr H298:39.29 kcal/mol
library:CHOClBr_G4 label:ClCCDC(Cl)CBr smiles:ClCC=C(Cl)CBr H298:-9.61 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)DCOBr smiles:ClCC(Br)=COBr H298:4.74 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)CBr smiles:C=C(Cl)C(Br)CBr H298:-0.38 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Cl)CBr smiles:CC(Cl)=C(Cl)CBr H298:-13.27 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Cl)DCCl smiles:OC(Br)C(Cl)=CCl H298:-40.93 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)CBr smiles:ClC=C(Cl)CBr H298:-2.39 kcal/mol
library:CHOClBr_G4 label:CCDC(Br)CCl smiles:CC=C(Br)CCl H298:-4.45 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)CBr smiles:C=C(Cl)CBr H298:2.88 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)C(Br)Br smiles:C=C(Cl)C(Br)C(Br)Br H298:8.65 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Cl)DCCl smiles:CC(Br)C(Cl)=CCl H298:-10.86 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(C)Br smiles:C=C(Cl)C(C)Br H298:-5.41 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(O)Br smiles:C=C(Cl)C(O)Br H298:-36.89 kcal/mol
library:CHOClBr_G4 label:ODCDC(Br)CCl smiles:O=C=C(Br)CCl H298:-9.84 kcal/mol
library:CHOClBr_G4 label:CCDC(Cl)CBr smiles:CC=C(Cl)CBr H298:-5.64 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)OBr smiles:C=C(Cl)C(Br)OBr H298:3.31 kcal/mol
library:CHOClBr_G4 label:ClCDCDC(Cl)CBr smiles:ClC=C=C(Cl)CBr H298:35.44 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)DCCBr smiles:ClCC(Br)=CCBr H298:2.08 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Br)CCl smiles:OC(Br)=C(Br)CCl H298:-32.08 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)CCl smiles:OC=C(Br)CCl H298:-39.24 kcal/mol
""",
)

entry(
    index = 83,
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
        Cpdata = ([-0.251678,-0.133366,-0.0656162,-0.0246591,0.0483949,0.101528,0.422424],'cal/(mol*K)','+|-',[0.140526,0.161506,0.165098,0.162676,0.141062,0.121665,0.0991542]),
        H298 = (2.40802,'kcal/mol','+|-',0.500963),
        S298 = (1.49949,'cal/(mol*K)','+|-',0.341436),
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
library:CHOFClBr_G4 label:CDC(F)C(F)C(Cl)Br smiles:C=C(F)C(F)C(Cl)Br H298:-88.95 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCC(F)Br smiles:FCC(F)=CC(F)Br H298:-129.38 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)CF smiles:CC(Br)=C(F)CF H298:-85.96 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)OBr smiles:FCC(F)=C(Br)OBr H298:-75.26 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCOBr smiles:FCC(F)=COBr H298:-80.65 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)OBr smiles:C=C(F)C(F)OBr H298:-90.97 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)CBr smiles:FCC(F)=C(F)CBr H298:-127.47 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)OBr smiles:FC=C(F)C(F)OBr H298:-130.48 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)CBr smiles:FC=C(F)C(F)CBr H298:-127.55 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)CF smiles:OC(Br)=C(F)CF H298:-114.90 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCC(Br)Br smiles:FCC(F)=CC(Br)Br H298:-77.93 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(F)Br smiles:C=C(F)C(F)C(F)Br H298:-129.78 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)OBr smiles:FCC(F)=C(F)OBr H298:-127.53 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)CBr smiles:C=C(F)C(F)CBr H298:-87.34 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCCBr smiles:FCC(F)=CCBr H298:-85.56 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)CBr smiles:FCC(F)=C(Br)CBr H298:-78.05 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)C(Br)Br smiles:C=C(F)C(F)C(Br)Br H298:-78.64 kcal/mol
""",
)

entry(
    index = 84,
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
        Cpdata = ([-0.452812,-0.282992,-0.116251,-0.0195095,0.116198,0.185973,0.374584],'cal/(mol*K)','+|-',[0.143756,0.165218,0.168893,0.166415,0.144304,0.124461,0.101433]),
        H298 = (1.40742,'kcal/mol','+|-',0.512477),
        S298 = (1.55969,'cal/(mol*K)','+|-',0.349284),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(Br)C(O)Br smiles:C=C(Br)C(O)Br H298:-23.55 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(C)Br smiles:C=C(Br)C(C)Br H298:6.53 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)OBr smiles:C=C(Br)C(Br)OBr H298:14.96 kcal/mol
library:CHOBr_G4 label:OCDC(Br)CBr smiles:OC=C(Br)CBr H298:-28.39 kcal/mol
library:CHOBr_G4 label:OC(Br)DC(Br)CBr smiles:OC(Br)=C(Br)CBr H298:-21.54 kcal/mol
library:CHOBr_G4 label:CDC(Br)CBr smiles:C=C(Br)CBr H298:15.10 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)OBr smiles:BrCC(Br)=C(Br)OBr H298:20.20 kcal/mol
library:CHOBr_G4 label:ODCDC(Br)CBr smiles:O=C=C(Br)CBr H298:1.08 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)OBr smiles:BrC=C(Br)C(Br)OBr H298:21.14 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)DCBr smiles:CC(Br)C(Br)=CBr H298:12.68 kcal/mol
library:CHOBr_G4 label:BrCDCDC(Br)CBr smiles:BrC=C=C(Br)CBr H298:57.39 kcal/mol
library:CHOBr_G4 label:CDCDC(Br)CBr smiles:C=C=C(Br)CBr H298:50.30 kcal/mol
library:CHOBr_G4 label:BrCCDC(Br)CBr smiles:BrCC=C(Br)CBr H298:12.76 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCC(Br)Br smiles:BrCC(Br)=CC(Br)Br H298:19.78 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CBr smiles:BrC=C(Br)CBr H298:20.92 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)Br smiles:BrCC(Br)=C(Br)Br H298:29.27 kcal/mol
library:CHOBr_G4 label:CCDC(Br)CBr smiles:CC=C(Br)CBr H298:6.21 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)CBr smiles:BrC=C(Br)C(Br)CBr H298:17.17 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)CBr smiles:BrCC(Br)=C(Br)CBr H298:17.71 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)DCBr smiles:OC(Br)C(Br)=CBr H298:-17.42 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)CBr smiles:C=C(Br)C(Br)CBr H298:11.46 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)CBr smiles:CC(Br)=C(Br)CBr H298:10.73 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCDC(Br)Br smiles:BrCC(Br)=C=C(Br)Br H298:65.11 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCOBr smiles:BrCC(Br)=COBr H298:15.22 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)CBr smiles:FC(Cl)=C(Br)CBr H298:-33.13 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)CBr smiles:FC=C(Br)C(Br)CBr H298:-31.33 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)CBr smiles:FCC(Br)=C(Br)CBr H298:-28.66 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)F smiles:CC(Br)C(Br)=C(F)F H298:-82.76 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CBr smiles:FC(F)=C(Br)CBr H298:-74.25 kcal/mol
library:CHOFBr_G4 label:FC(F)CDC(Br)CBr smiles:FC(F)C=C(Br)CBr H298:-87.67 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DCF smiles:OC(Br)C(Br)=CF H298:-66.00 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCDC(Br)CBr smiles:FC(Br)=C=C(Br)CBr H298:17.39 kcal/mol
library:CHOFBr_G4 label:FCDCDC(Br)CBr smiles:FC=C=C(Br)CBr H298:10.09 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CBr smiles:FC=C(Br)CBr H298:-27.74 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)Br smiles:OC(Br)C(Br)=C(F)Br H298:-59.45 kcal/mol
library:CHOFBr_G4 label:FC(Br)CDC(Br)CBr smiles:FC(Br)C=C(Br)CBr H298:-31.07 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)CBr smiles:CC(F)=C(Br)CBr H298:-39.75 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)F smiles:OC(Br)C(Br)=C(F)F H298:-113.44 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)Br smiles:CC(Br)C(Br)=C(F)Br H298:-28.67 kcal/mol
library:CHOFBr_G4 label:FCCDC(Br)CBr smiles:FCC=C(Br)CBr H298:-35.25 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)CBr smiles:FCC(F)=C(Br)CBr H298:-78.05 kcal/mol
library:CHOFBr_G4 label:FC(F)DCDC(Br)CBr smiles:FC(F)=C=C(Br)CBr H298:-35.68 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DCF smiles:CC(Br)C(Br)=CF H298:-36.18 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CBr smiles:FC(Br)=C(Br)CBr H298:-20.72 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)OBr smiles:FC=C(Br)C(Br)OBr H298:-27.80 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CBr smiles:ClC=C(Br)CBr H298:9.32 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)DCCl smiles:OC(Br)C(Br)=CCl H298:-30.36 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Br)CBr smiles:CC(Cl)=C(Br)CBr H298:-1.75 kcal/mol
library:CHOClBr_G4 label:ClCCDC(Br)CBr smiles:ClCC=C(Br)CBr H298:2.26 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)CBr smiles:ClC(Cl)=C(Br)CBr H298:5.70 kcal/mol
library:CHOClBr_G4 label:ClCDCDC(Br)CBr smiles:ClC=C=C(Br)CBr H298:46.42 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)CBr smiles:ClC(Br)=C(Br)CBr H298:17.40 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)DCCl smiles:CC(Br)C(Br)=CCl H298:0.89 kcal/mol
""",
)

entry(
    index = 85,
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
        Cpdata = ([-0.112012,0.0156249,0.139183,0.111374,0.0182028,-0.0224149,0.149256],'cal/(mol*K)','+|-',[0.12984,0.149225,0.152545,0.150307,0.130336,0.112414,0.0916147]),
        H298 = (0.238343,'kcal/mol','+|-',0.46287),
        S298 = (-0.323271,'cal/(mol*K)','+|-',0.315474),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(F)C(Cl)DCCl smiles:C=C(F)C(Cl)=CCl H298:-32.54 kcal/mol
library:CHOFCl_G4 label:CDC(Cl)C(F)DCF smiles:C=C(Cl)C(F)=CF H298:-67.03 kcal/mol
library:CHOFCl_G4 label:CDC(F)C(DC)Cl smiles:C=C(F)C(=C)Cl H298:-27.41 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DC(Cl)Br smiles:C=C(F)C(Cl)=C(Cl)Br H298:-19.86 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DC(Br)Br smiles:C=C(F)C(Cl)=C(Br)Br H298:-8.02 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DC(F)Cl smiles:C=C(Br)C(Cl)=C(F)Cl H298:-20.34 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DC(F)F smiles:C=C(Br)C(Cl)=C(F)F H298:-61.50 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DCBr smiles:C=C(F)C(Cl)=CBr H298:-20.74 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DCF smiles:C=C(Br)C(Cl)=CF H298:-17.65 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DCF smiles:C=C(Br)C(F)=CF H298:-54.93 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)DCBr smiles:FC=C(F)C(Br)=CBr H298:-48.03 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(DC)Br smiles:C=C(F)C(=C)Br H298:-15.23 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DC(Br)Br smiles:C=C(F)C(Br)=C(Br)Br H298:3.61 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DCBr smiles:C=C(F)C(Br)=CBr H298:-8.72 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DC(F)F smiles:C=C(Br)C(F)=C(F)F H298:-96.86 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)DC(Cl)Cl smiles:C=C(Br)C(Cl)=C(Cl)Cl H298:18.22 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)DCBr smiles:C=C(Cl)C(Br)=CBr H298:31.08 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(DC)Br smiles:C=C(Cl)C(=C)Br H298:24.57 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Cl)DCCl smiles:C=C(Br)C(Cl)=CCl H298:19.31 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)DC(Br)Br smiles:C=C(Cl)C(Br)=C(Br)Br H298:41.41 kcal/mol
""",
)

entry(
    index = 86,
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
        Cpdata = ([-0.0595707,-0.0266998,0.078211,0.0517162,-0.0393957,-0.0704583,0.121822],'cal/(mol*K)','+|-',[0.181454,0.208545,0.213184,0.210056,0.182147,0.1571,0.128033]),
        H298 = (0.675509,'kcal/mol','+|-',0.646869),
        S298 = (-0.234891,'cal/(mol*K)','+|-',0.44088),
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
library:CHOFClBr_G4 label:CDC(F)C(F)DC(Cl)Br smiles:C=C(F)C(F)=C(Cl)Br H298:-57.86 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)DCBr smiles:FC=C(F)C(F)=CBr H298:-97.80 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(Br)Br smiles:C=C(F)C(F)=C(Br)Br H298:-45.80 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DCBr smiles:C=C(F)C(F)=CBr H298:-58.90 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(F)Br smiles:C=C(F)C(F)=C(F)Br H298:-95.49 kcal/mol
""",
)

entry(
    index = 87,
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
        Cpdata = ([-0.158306,-0.131038,0.00641817,0.0123105,-0.0231755,-0.0296819,0.16498],'cal/(mol*K)','+|-',[0.194308,0.223318,0.228285,0.224936,0.19505,0.168229,0.137103]),
        H298 = (-0.0544732,'kcal/mol','+|-',0.692693),
        S298 = (-0.698698,'cal/(mol*K)','+|-',0.472112),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(Br)C(DC)Br smiles:C=C(Br)C(=C)Br H298:36.66 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)DCBr smiles:C=C(Br)C(Br)=CBr H298:43.12 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Br)DC(F)Cl smiles:C=C(Br)C(Br)=C(F)Cl H298:-9.34 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)Br smiles:C=C(Br)C(Br)=C(F)Br H298:3.06 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)F smiles:C=C(Br)C(Br)=C(F)F H298:-50.22 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)DCBr smiles:FC=C(Br)C(Br)=CBr H298:0.71 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DCF smiles:C=C(Br)C(Br)=CF H298:-6.05 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DCCl smiles:C=C(Br)C(Br)=CCl H298:31.22 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DC(Cl)Br smiles:C=C(Br)C(Br)=C(Cl)Br H298:41.02 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DC(Cl)Cl smiles:C=C(Br)C(Br)=C(Cl)Cl H298:29.46 kcal/mol
""",
)

entry(
    index = 88,
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
        Cpdata = ([0.192955,0.160487,0.102905,0.0777284,0.0301348,0.000628366,-0.0942518],'cal/(mol*K)','+|-',[0.0504065,0.057932,0.0592207,0.0583519,0.050599,0.0436412,0.0355666]),
        H298 = (1.72557,'kcal/mol','+|-',0.179695),
        S298 = (0.0587532,'cal/(mol*K)','+|-',0.122473),
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
library:CHOFClBr_G4 label:CC(Br)(Br)C(Cl)DCF smiles:CC(Br)(Br)C(Cl)=CF H298:-39.29 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)C(F)Cl smiles:CC(Br)=C(Cl)C(F)Cl H298:-53.16 kcal/mol
library:CHOFClBr_G4 label:CC(F)DC(Cl)CBr smiles:CC(F)=C(Cl)CBr H298:-51.39 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(Cl)DCF smiles:O=C(Br)C(Cl)=CF H298:-65.38 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CBr smiles:FC=C(Cl)CBr H298:-39.27 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)OOBr smiles:FC=C(Cl)OOBr H298:-20.85 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)COBr smiles:FC=C(Cl)COBr H298:-44.14 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(Cl)CF smiles:OC(Br)=C(Cl)CF H298:-80.74 kcal/mol
library:CHOFClBr_G4 label:OC(Br)C(Cl)DCF smiles:OC(Br)C(Cl)=CF H298:-77.52 kcal/mol
library:CHOFClBr_G4 label:FC#CC(Cl)DCBr smiles:FC#CC(Cl)=CBr H298:42.14 kcal/mol
library:CHOFClBr_G4 label:CC(Br)C(Cl)DCF smiles:CC(Br)C(Cl)=CF H298:-47.65 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)CF smiles:CC(Br)=C(Cl)CF H298:-47.88 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Br)Br smiles:FC=C(Cl)C(Br)Br H298:-30.28 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DCBr smiles:C=C(F)C(Cl)=CBr H298:-20.74 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CCBr smiles:FC=C(Cl)CCBr H298:-47.00 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)OCBr smiles:FC=C(Cl)OCBr H298:-67.07 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)CDCBr smiles:FC=C(Cl)C=CBr H298:-18.16 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)OBr smiles:FC=C(Cl)OBr H298:-36.23 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)C(Cl)Br smiles:FC=C(Cl)C(Cl)Br H298:-41.48 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Cl)C(F)F smiles:CC(Br)=C(Cl)C(F)F H298:-99.96 kcal/mol
library:CHOFClBr_G4 label:CC(F)DC(Cl)OBr smiles:CC(F)=C(Cl)OBr H298:-48.51 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DCF smiles:C=C(Br)C(Cl)=CF H298:-17.65 kcal/mol
library:CHOFClBr_G4 label:FCDCC(Cl)DCBr smiles:FC=CC(Cl)=CBr H298:-19.50 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)CBr smiles:FC=C(Br)C(Br)CBr H298:-31.33 kcal/mol
library:CHOFBr_G4 label:COC(Br)DCF smiles:COC(Br)=CF H298:-59.17 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)DCBr smiles:FC=C(F)C(F)=CBr H298:-97.80 kcal/mol
library:CHOFBr_G4 label:FCDCBr smiles:FC=CBr H298:-25.76 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCF smiles:OC(Br)=CF H298:-64.41 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DCF smiles:OC(Br)C(Br)=CF H298:-66.00 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)CF smiles:CC(Br)=C(F)CF H298:-85.96 kcal/mol
library:CHOFBr_G4 label:CCC(Br)DCF smiles:CCC(Br)=CF H298:-41.71 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)OBr smiles:FCC(F)=C(Br)OBr H298:-75.26 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)Br smiles:FC=C(Br)C(Br)Br H298:-19.13 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)DCBr smiles:FC(F)=CC(F)=CBr H298:-104.47 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)COBr smiles:FC=C(Br)COBr H298:-32.77 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)DCBr smiles:FC=C(Br)C(Br)=CBr H298:0.71 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCF smiles:CC(Br)=CF H298:-35.38 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OOBr smiles:FC=C(Br)OOBr H298:-8.76 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)(Br)Br smiles:FC=C(Br)C(Br)(Br)Br H298:-6.67 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CBr smiles:FC=C(Br)CBr H298:-27.74 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)C(Br)Br smiles:CC(F)=C(Br)C(Br)Br H298:-31.49 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CC(Br)Br smiles:FC=C(Br)CC(Br)Br H298:-28.82 kcal/mol
library:CHOFBr_G4 label:OOC(Br)DCF smiles:OOC(Br)=CF H298:-43.36 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)DCF smiles:C=CC(Br)=CF H298:-12.23 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CDCBr smiles:FC=C(Br)C=CBr H298:-6.57 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)CBr smiles:CC(F)=C(Br)CBr H298:-39.75 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)C(F)F smiles:OC(Br)=C(F)C(F)F H298:-166.31 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DCF smiles:O=C(Br)C(Br)=CF H298:-54.16 kcal/mol
library:CHOFBr_G4 label:OCC(Br)DCF smiles:OCC(Br)=CF H298:-69.80 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(Br)DCF smiles:CC(Br)(Br)C(Br)=CF H298:-27.75 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)C(F)F smiles:CC(Br)=C(F)C(F)F H298:-136.61 kcal/mol
library:CHOFBr_G4 label:CDCC(F)DCBr smiles:C=CC(F)=CBr H298:-14.01 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DCF smiles:C=C(Br)C(Br)=CF H298:-6.05 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)CF smiles:OC(Br)=C(F)CF H298:-114.90 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(Br)DCF smiles:OC(Br)(Br)C(Br)=CF H298:-59.58 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(Br)OBr smiles:CC(F)=C(Br)OBr H298:-36.49 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(O)Br smiles:CC(F)=C(O)Br H298:-74.82 kcal/mol
library:CHOFBr_G4 label:C#CC(F)DCBr smiles:C#CC(F)=CBr H298:32.19 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(C)Br smiles:CC(F)=C(C)Br H298:-46.58 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OBr smiles:FC=C(Br)OBr H298:-24.06 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DCBr smiles:C=C(F)C(F)=CBr H298:-58.90 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OCBr smiles:FC=C(Br)OCBr H298:-55.14 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)DCBr smiles:FC#CC(F)=CBr H298:4.01 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CCBr smiles:FC=C(Br)CCBr H298:-35.54 kcal/mol
library:CHOFBr_G4 label:FOC(F)DC(Br)OBr smiles:FOC(F)=C(Br)OBr H298:-34.86 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(Br)CBr smiles:FCC(F)=C(Br)CBr H298:-78.05 kcal/mol
library:CHOFBr_G4 label:OC(F)DC(O)Br smiles:OC(F)=C(O)Br H298:-107.21 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DCF smiles:CC(Br)C(Br)=CF H298:-36.18 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)CDC(Br)Br smiles:FC=C(Br)C=C(Br)Br H298:3.86 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)DCBr smiles:FC=CC(F)=CBr H298:-58.11 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DCF smiles:O=CC(Br)=CF H298:-52.97 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)OBr smiles:FC=C(Br)C(Br)OBr H298:-27.80 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)OC(Br)Br smiles:FC=C(Br)OC(Br)Br H298:-45.89 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DCCl smiles:C=C(Br)C(Br)=CCl H298:31.22 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DCCl smiles:O=CC(Br)=CCl H298:-15.61 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)C(Br)Br smiles:ClC=C(Br)C(Br)Br H298:17.97 kcal/mol
library:CHOClBr_G4 label:CC(Br)DCCl smiles:CC(Br)=CCl H298:1.76 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CBr smiles:ClC=C(Br)CBr H298:9.32 kcal/mol
library:CHOClBr_G4 label:OC(Br)C(Br)DCCl smiles:OC(Br)C(Br)=CCl H298:-30.36 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Cl)DCBr smiles:ClC=CC(Cl)=CBr H298:18.35 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)C(Cl)Cl smiles:CC(Br)=C(Cl)C(Cl)Cl H298:-11.76 kcal/mol
library:CHOClBr_G4 label:OCC(Br)DCCl smiles:OCC(Br)=CCl H298:-32.60 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DCBr smiles:C=C(Cl)C(Cl)=CBr H298:19.00 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)DCCl smiles:C=CC(Br)=CCl H298:24.88 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Br)CBr smiles:CC(Cl)=C(Br)CBr H298:-1.75 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)DCBr smiles:C#CC(Cl)=CBr H298:70.06 kcal/mol
library:CHOClBr_G4 label:OC(Cl)DC(Br)OBr smiles:OC(Cl)=C(Br)OBr H298:-30.55 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(O)Br smiles:CC(Cl)=C(O)Br H298:-39.22 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(C)Br smiles:CC(Cl)=C(C)Br H298:-7.69 kcal/mol
library:CHOClBr_G4 label:OOC(Br)DCCl smiles:OOC(Br)=CCl H298:-6.53 kcal/mol
library:CHOClBr_G4 label:ClCDCBr smiles:ClC=CBr H298:11.77 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)OCBr smiles:ClC=C(Br)OCBr H298:-18.80 kcal/mol
library:CHOClBr_G4 label:OC(Br)DCCl smiles:OC(Br)=CCl H298:-29.89 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CCBr smiles:ClC=C(Br)CCBr H298:1.63 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)CCl smiles:CC(Br)=C(Cl)CCl H298:-11.56 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)CDCBr smiles:ClC=C(Br)C=CBr H298:30.38 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)COBr smiles:ClC=C(Br)COBr H298:4.48 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)OOBr smiles:ClC=C(Br)OOBr H298:28.06 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)CCl smiles:OC(Br)=C(Cl)CCl H298:-43.32 kcal/mol
library:CHOClBr_G4 label:CCC(Br)DCCl smiles:CCC(Br)=CCl H298:-3.56 kcal/mol
library:CHOClBr_G4 label:ClC#CC(Cl)DCBr smiles:ClC#CC(Cl)=CBr H298:69.48 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DC(Br)OBr smiles:CC(Cl)=C(Br)OBr H298:1.49 kcal/mol
library:CHOClBr_G4 label:CC(Br)(Br)C(Br)DCCl smiles:CC(Br)(Br)C(Br)=CCl H298:9.32 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)DCBr smiles:C=CC(Cl)=CBr H298:24.70 kcal/mol
library:CHOClBr_G4 label:COC(Br)DCCl smiles:COC(Br)=CCl H298:-23.18 kcal/mol
library:CHOClBr_G4 label:CC(Br)C(Br)DCCl smiles:CC(Br)C(Br)=CCl H298:0.89 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)OBr smiles:ClC=C(Br)OBr H298:12.25 kcal/mol
library:CHOClBr_G4 label:OC(Cl)DC(O)Br smiles:OC(Cl)=C(O)Br H298:-66.24 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)DCCl smiles:O=C(Br)C(Br)=CCl H298:-16.71 kcal/mol
""",
)

entry(
    index = 89,
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
        Cpdata = ([0.143061,0.084595,0.0485554,0.0373149,0.0157509,0.00236969,-0.0605414],'cal/(mol*K)','+|-',[0.058502,0.0672361,0.0687318,0.0677234,0.0587253,0.0506501,0.0412787]),
        H298 = (3.00962,'kcal/mol','+|-',0.208555),
        S298 = (0.220095,'cal/(mol*K)','+|-',0.142143),
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
library:CHOFClBr_G4 label:FCDC(F)C(Cl)Br smiles:FC=C(F)C(Cl)Br H298:-77.79 kcal/mol
library:CHOFBr_G4 label:FCDC(F)COBr smiles:FC=C(F)COBr H298:-80.53 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)DCBr smiles:FC=C(F)C(F)=CBr H298:-97.80 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CDCBr smiles:FC=C(F)C=CBr H298:-55.36 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OOBr smiles:FC=C(F)OOBr H298:-60.80 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DCF smiles:OC(Br)C(F)=CF H298:-114.08 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)(Br)Br smiles:FC=C(F)C(Br)(Br)Br H298:-54.64 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)Br smiles:FC=C(F)C(F)Br H298:-117.54 kcal/mol
library:CHOFBr_G4 label:FOC(F)DC(F)OBr smiles:FOC(F)=C(F)OBr H298:-88.41 kcal/mol
library:CHOFBr_G4 label:CC(Br)(Br)C(F)DCF smiles:CC(Br)(Br)C(F)=CF H298:-75.88 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)CBr smiles:CC(F)=C(F)CBr H298:-88.35 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DCF smiles:C=C(Br)C(F)=CF H298:-54.93 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CBr smiles:FC=C(F)CBr H298:-76.26 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)DCBr smiles:FC=C(F)C(Br)=CBr H298:-48.03 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)Br smiles:FC=C(F)C(Br)Br H298:-66.53 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)CBr smiles:FCC(F)=C(F)CBr H298:-127.47 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)OBr smiles:FC=C(F)C(Br)OBr H298:-74.68 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OC(Br)Br smiles:FC=C(F)OC(Br)Br H298:-96.27 kcal/mol
library:CHOFBr_G4 label:OC(Br)(Br)C(F)DCF smiles:OC(Br)(Br)C(F)=CF H298:-107.53 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(F)Br smiles:FC=C(F)C(F)(F)Br H298:-167.73 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)OBr smiles:FC=C(F)C(F)OBr H298:-130.48 kcal/mol
library:CHOFBr_G4 label:OC(F)(Br)C(F)DCF smiles:OC(F)(Br)C(F)=CF H298:-161.23 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)CBr smiles:FC=C(F)C(F)CBr H298:-127.55 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OC(F)Br smiles:FC=C(F)OC(F)Br H298:-153.10 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(F)DCF smiles:CC(F)(Br)C(F)=CF H298:-129.74 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)CBr smiles:FC=C(F)C(Br)CBr H298:-78.36 kcal/mol
library:CHOFBr_G4 label:FCC(F)DC(F)OBr smiles:FCC(F)=C(F)OBr H298:-127.53 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(Br)Br smiles:CC(F)=C(F)C(Br)Br H298:-77.69 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DCF smiles:CC(Br)C(F)=CF H298:-84.36 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CC(F)Br smiles:FC=C(F)CC(F)Br H298:-128.56 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)C(F)Br smiles:CC(F)=C(F)C(F)Br H298:-130.05 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DCF smiles:O=C(Br)C(F)=CF H298:-101.47 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OBr smiles:FC=C(F)OBr H298:-76.32 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(F)(Br)Br smiles:FC=C(F)C(F)(Br)Br H298:-108.92 kcal/mol
library:CHOFBr_G4 label:CC(F)DC(F)OBr smiles:CC(F)=C(F)OBr H298:-88.56 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CDC(F)Br smiles:FC=C(F)C=C(F)Br H298:-96.22 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CC(Br)Br smiles:FC=C(F)CC(Br)Br H298:-76.59 kcal/mol
library:CHOFBr_G4 label:FCDC(F)CDC(Br)Br smiles:FC=C(F)C=C(Br)Br H298:-44.57 kcal/mol
library:CHOFBr_G4 label:FCDC(F)OCBr smiles:FC=C(F)OCBr H298:-106.33 kcal/mol
""",
)

entry(
    index = 90,
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
        Cpdata = ([0.191068,0.135447,0.086284,0.0841781,0.0456014,0.0200424,-0.0716922],'cal/(mol*K)','+|-',[0.0793219,0.0911644,0.0931923,0.0918251,0.0796247,0.0686756,0.0559691]),
        H298 = (1.36026,'kcal/mol','+|-',0.282776),
        S298 = (-0.219487,'cal/(mol*K)','+|-',0.192729),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CC(Br)DC(Br)OBr smiles:CC(Br)=C(Br)OBr H298:13.11 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)DCBr smiles:BrC#CC(Br)=CBr H298:91.64 kcal/mol
library:CHOBr_G4 label:BrCDCBr smiles:BrC=CBr H298:23.74 kcal/mol
library:CHOBr_G4 label:OC(Br)DC(Br)CBr smiles:OC(Br)=C(Br)CBr H298:-21.54 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)DCBr smiles:O=C(Br)C(Br)=CBr H298:-4.80 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)OBr smiles:BrCC(Br)=C(Br)OBr H298:20.20 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OC(Br)Br smiles:BrC=C(Br)OC(Br)Br H298:1.72 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)OBr smiles:BrC=C(Br)C(Br)OBr H298:21.14 kcal/mol
library:CHOBr_G4 label:CC(Br)C(Br)DCBr smiles:CC(Br)C(Br)=CBr H298:12.68 kcal/mol
library:CHOBr_G4 label:C#CC(Br)DCBr smiles:C#CC(Br)=CBr H298:81.53 kcal/mol
library:CHOBr_G4 label:COC(Br)DCBr smiles:COC(Br)=CBr H298:-11.90 kcal/mol
library:CHOBr_G4 label:OC(Br)DC(O)Br smiles:OC(Br)=C(O)Br H298:-54.18 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OOBr smiles:BrC=C(Br)OOBr H298:39.95 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OBr smiles:BrC=C(Br)OBr H298:23.60 kcal/mol
library:CHOBr_G4 label:CCC(Br)DCBr smiles:CCC(Br)=CBr H298:8.04 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)COBr smiles:BrC=C(Br)COBr H298:16.28 kcal/mol
library:CHOBr_G4 label:OC(Br)DCBr smiles:OC(Br)=CBr H298:-18.60 kcal/mol
library:CHOBr_G4 label:OOC(Br)DCBr smiles:OOC(Br)=CBr H298:5.37 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CCBr smiles:BrC=C(Br)CCBr H298:13.41 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)OCBr smiles:BrC=C(Br)OCBr H298:-7.56 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)DCBr smiles:BrC=CC(Br)=CBr H298:42.05 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CC(Br)Br smiles:BrC=C(Br)CC(Br)Br H298:20.22 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)CBr smiles:BrC=C(Br)CBr H298:20.92 kcal/mol
library:CHOBr_G4 label:CDCC(Br)DCBr smiles:C=CC(Br)=CBr H298:36.68 kcal/mol
library:CHOBr_G4 label:OCC(Br)DCBr smiles:OCC(Br)=CBr H298:-20.58 kcal/mol
library:CHOBr_G4 label:BrOC(Br)DC(Br)OBr smiles:BrOC(Br)=C(Br)OBr H298:23.66 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)CBr smiles:BrC=C(Br)C(Br)CBr H298:17.17 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)CBr smiles:BrCC(Br)=C(Br)CBr H298:17.71 kcal/mol
library:CHOBr_G4 label:OC(Br)C(Br)DCBr smiles:OC(Br)C(Br)=CBr H298:-17.42 kcal/mol
library:CHOBr_G4 label:CC(Br)DCBr smiles:CC(Br)=CBr H298:13.40 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DCBr smiles:O=CC(Br)=CBr H298:-3.70 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)CBr smiles:CC(Br)=C(Br)CBr H298:10.73 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(O)Br smiles:CC(Br)=C(O)Br H298:-27.73 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(C)Br smiles:CC(Br)=C(C)Br H298:2.61 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(Br)DCBr smiles:C=C(Br)C(Br)=CBr H298:43.12 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)C(Br)Br smiles:BrC=C(Br)C(Br)Br H298:29.50 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(Br)C(F)Cl smiles:CC(Br)=C(Br)C(F)Cl H298:-41.42 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)CF smiles:OC(Br)=C(Br)CF H298:-66.56 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)CBr smiles:FCC(Br)=C(Br)CBr H298:-28.66 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)DCBr smiles:FC#CC(Br)=CBr H298:53.40 kcal/mol
library:CHOFBr_G4 label:FOC(Br)DC(Br)OBr smiles:FOC(Br)=C(Br)OBr H298:16.70 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(Br)DCBr smiles:FC(F)=CC(Br)=CBr H298:-53.78 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)F smiles:OC(Br)=C(Br)C(F)F H298:-118.56 kcal/mol
library:CHOFBr_G4 label:FCDC(F)C(Br)DCBr smiles:FC=C(F)C(Br)=CBr H298:-48.03 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)C(Br)DCBr smiles:FC=C(Br)C(Br)=CBr H298:0.71 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)F smiles:CC(Br)=C(Br)C(F)F H298:-88.20 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)C(F)Br smiles:CC(Br)=C(Br)C(F)Br H298:-29.21 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)DCBr smiles:FC=CC(Br)=CBr H298:-7.81 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(Br)C(F)Br smiles:OC(Br)=C(Br)C(F)Br H298:-61.64 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DCBr smiles:C=C(F)C(Br)=CBr H298:-8.72 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCC(Br)DCBr smiles:FC(Br)=CC(Br)=CBr H298:1.85 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(Br)CF smiles:CC(Br)=C(Br)CF H298:-36.17 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DC(Br)OBr smiles:FCC(Br)=C(Br)OBr H298:-26.22 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)CCl smiles:CC(Br)=C(Br)CCl H298:-0.16 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)DCBr smiles:C=C(Cl)C(Br)=CBr H298:31.08 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)C(Cl)Br smiles:CC(Br)=C(Br)C(Cl)Br H298:8.01 kcal/mol
library:CHOClBr_G4 label:ClCDCC(Br)DCBr smiles:ClC=CC(Br)=CBr H298:30.11 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Br)C(Cl)Cl smiles:CC(Br)=C(Br)C(Cl)Cl H298:-3.20 kcal/mol
library:CHOClBr_G4 label:ClC#CC(Br)DCBr smiles:ClC#CC(Br)=CBr H298:80.65 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Br)CCl smiles:OC(Br)=C(Br)CCl H298:-32.08 kcal/mol
""",
)

entry(
    index = 91,
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
        Cpdata = ([0.673678,0.59465,0.424297,0.347296,0.147457,0.0428921,-0.140663],'cal/(mol*K)','+|-',[0.0987443,0.113486,0.116011,0.114309,0.0991213,0.0854912,0.0696735]),
        H298 = (4.13515,'kcal/mol','+|-',0.352015),
        S298 = (0.090778,'cal/(mol*K)','+|-',0.239919),
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
library:CHOFClBr_G4 label:CDC(F)C(Cl)DC(Cl)Br smiles:C=C(F)C(Cl)=C(Cl)Br H298:-19.86 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)CBr smiles:FC(Cl)=C(Cl)CBr H298:-44.45 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(F)DC(Cl)Br smiles:C=C(F)C(F)=C(Cl)Br H298:-57.86 kcal/mol
library:CHOFClBr_G4 label:OCC(Br)DC(F)Cl smiles:OCC(Br)=C(F)Cl H298:-74.34 kcal/mol
library:CHOFClBr_G4 label:OC(Br)DC(F)Cl smiles:OC(Br)=C(F)Cl H298:-68.08 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)DC(F)Cl smiles:O=CC(Br)=C(F)Cl H298:-57.02 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCBr smiles:FC(Cl)=CBr H298:-30.87 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)CBr smiles:FC(Cl)=C(Br)CBr H298:-33.13 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)CBr smiles:FC(F)=C(Cl)CBr H298:-85.59 kcal/mol
library:CHOFClBr_G4 label:CDC(F)C(Cl)DC(Br)Br smiles:C=C(F)C(Cl)=C(Br)Br H298:-8.02 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DC(F)Cl smiles:C=C(Br)C(Cl)=C(F)Cl H298:-20.34 kcal/mol
library:CHOFClBr_G4 label:COC(Br)DC(F)Cl smiles:COC(Br)=C(F)Cl H298:-64.09 kcal/mol
library:CHOFClBr_G4 label:OOC(Br)DC(F)Cl smiles:OOC(Br)=C(F)Cl H298:-46.89 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Cl)DC(F)F smiles:C=C(Br)C(Cl)=C(F)F H298:-61.50 kcal/mol
library:CHOFClBr_G4 label:FCDC(Cl)Br smiles:FC=C(Cl)Br H298:-28.19 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)OBr smiles:FC(F)=C(Cl)OBr H298:-80.48 kcal/mol
library:CHOFClBr_G4 label:CDCC(Br)DC(F)Cl smiles:C=CC(Br)=C(F)Cl H298:-17.51 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)OBr smiles:FC(Cl)=C(Br)OBr H298:-28.83 kcal/mol
library:CHOFClBr_G4 label:C#CC(F)DC(Cl)Br smiles:C#CC(F)=C(Cl)Br H298:29.61 kcal/mol
library:CHOFClBr_G4 label:CCC(Br)DC(F)Cl smiles:CCC(Br)=C(F)Cl H298:-46.03 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)OBr smiles:FC(Cl)=C(Cl)OBr H298:-40.73 kcal/mol
library:CHOFClBr_G4 label:CDCC(F)DC(Cl)Br smiles:C=CC(F)=C(Cl)Br H298:-16.75 kcal/mol
library:CHOFClBr_G4 label:CDC(Br)C(Br)DC(F)Cl smiles:C=C(Br)C(Br)=C(F)Cl H298:-9.34 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DC(F)Cl smiles:CC(Br)=C(F)Cl H298:-40.53 kcal/mol
library:CHOFBr_G4 label:CDCC(F)DC(F)Br smiles:C=CC(F)=C(F)Br H298:-53.64 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)OCBr smiles:FC(F)=C(Br)OCBr H298:-99.62 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)F smiles:CC(Br)C(Br)=C(F)F H298:-82.76 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)Br smiles:CC(Br)=C(F)Br H298:-27.99 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)Br smiles:C=C(Br)C(Br)=C(F)Br H298:3.06 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CCBr smiles:FC(F)=C(Br)CCBr H298:-82.03 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CBr smiles:FC(F)=C(Br)CBr H298:-74.25 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)OBr smiles:FC(Br)=C(Br)OBr H298:-16.61 kcal/mol
library:CHOFBr_G4 label:OCC(Br)DC(F)F smiles:OCC(Br)=C(F)F H298:-115.96 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)DC(Br)Br smiles:FC#CC(F)=C(Br)Br H298:12.85 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)DC(F)F smiles:C=CC(Br)=C(F)F H298:-58.81 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CDCBr smiles:FC(Br)=C(Br)C=CBr H298:0.64 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)F smiles:OC(Br)=C(F)F H298:-107.54 kcal/mol
library:CHOFBr_G4 label:CCC(Br)DC(F)Br smiles:CCC(Br)=C(F)Br H298:-33.62 kcal/mol
library:CHOFBr_G4 label:FCDC(F)Br smiles:FC=C(F)Br H298:-65.08 kcal/mol
library:CHOFBr_G4 label:FC#CC(F)DC(F)Br smiles:FC#CC(F)=C(F)Br H298:-35.25 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCBr smiles:FC(Br)=CBr H298:-18.26 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(Br)DC(F)F smiles:C=C(Br)C(Br)=C(F)F H298:-50.22 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)C(Br)Br smiles:FC(F)=C(Br)C(Br)Br H298:-65.34 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(Br)Br smiles:C=C(F)C(F)=C(Br)Br H298:-45.80 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)OCBr smiles:FC(Br)=C(Br)OCBr H298:-47.58 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)Br smiles:O=C(Br)C(Br)=C(F)Br H298:-42.46 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)Br smiles:OC(Br)C(Br)=C(F)Br H298:-59.45 kcal/mol
library:CHOFBr_G4 label:OOC(Br)DC(F)F smiles:OOC(Br)=C(F)F H298:-87.86 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CCBr smiles:FC(Br)=C(Br)CCBr H298:-27.82 kcal/mol
library:CHOFBr_G4 label:CDCC(Br)DC(F)Br smiles:C=CC(Br)=C(F)Br H298:-4.98 kcal/mol
library:CHOFBr_G4 label:CC(Br)DC(F)F smiles:CC(Br)=C(F)F H298:-81.90 kcal/mol
library:CHOFBr_G4 label:OOC(Br)DC(F)Br smiles:OOC(Br)=C(F)Br H298:-34.99 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)DC(Br)Br smiles:FC=CC(F)=C(Br)Br H298:-49.30 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(Br)DC(F)F smiles:OC(Br)C(Br)=C(F)F H298:-113.44 kcal/mol
library:CHOFBr_G4 label:C#CC(F)DC(F)Br smiles:C#CC(F)=C(F)Br H298:-7.02 kcal/mol
library:CHOFBr_G4 label:COC(Br)DC(F)Br smiles:COC(Br)=C(F)Br H298:-51.90 kcal/mol
library:CHOFBr_G4 label:CDCC(F)DC(Br)Br smiles:C=CC(F)=C(Br)Br H298:-5.10 kcal/mol
library:CHOFBr_G4 label:CCC(Br)DC(F)F smiles:CCC(Br)=C(F)F H298:-87.22 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(Br)DC(F)Br smiles:CC(Br)C(Br)=C(F)Br H298:-28.67 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)COBr smiles:FC(Br)=C(Br)COBr H298:-24.92 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)OOBr smiles:FC(Br)=C(Br)OOBr H298:-0.17 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)Br smiles:O=CC(Br)=C(F)Br H298:-44.37 kcal/mol
library:CHOFBr_G4 label:OC(Br)DC(F)Br smiles:OC(Br)=C(F)Br H298:-55.87 kcal/mol
library:CHOFBr_G4 label:FCDCC(F)DC(F)Br smiles:FC=CC(F)=C(F)Br H298:-97.20 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)CDCBr smiles:FC(F)=C(Br)C=CBr H298:-52.94 kcal/mol
library:CHOFBr_G4 label:OCC(Br)DC(F)Br smiles:OCC(Br)=C(F)Br H298:-61.84 kcal/mol
library:CHOFBr_G4 label:C#CC(F)DC(Br)Br smiles:C#CC(F)=C(Br)Br H298:41.16 kcal/mol
library:CHOFBr_G4 label:FC(F)DCBr smiles:FC(F)=CBr H298:-72.57 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)F smiles:O=CC(Br)=C(F)F H298:-99.11 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)F smiles:O=C(Br)C(Br)=C(F)F H298:-97.65 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(F)DC(F)Br smiles:C=C(F)C(F)=C(F)Br H298:-95.49 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)CBr smiles:FC(Br)=C(Br)CBr H298:-20.72 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)C(Br)Br smiles:FC(Br)=C(Br)C(Br)Br H298:-11.92 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)OBr smiles:FC(F)=C(Br)OBr H298:-68.52 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)COBr smiles:FC(F)=C(Br)COBr H298:-79.38 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)OOBr smiles:FC(F)=C(Br)OOBr H298:-53.17 kcal/mol
library:CHOFBr_G4 label:FCDC(Br)Br smiles:FC=C(Br)Br H298:-16.62 kcal/mol
library:CHOFBr_G4 label:COC(Br)DC(F)F smiles:COC(Br)=C(F)F H298:-104.05 kcal/mol
library:CHOClBr_G4 label:OOC(Br)DC(Cl)Br smiles:OOC(Br)=C(Cl)Br H298:2.97 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DC(Cl)Br smiles:C=C(Cl)C(Cl)=C(Cl)Br H298:18.38 kcal/mol
library:CHOClBr_G4 label:OCC(Br)DC(Cl)Cl smiles:OCC(Br)=C(Cl)Cl H298:-35.18 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)DC(Cl)Br smiles:C=CC(Cl)=C(Cl)Br H298:21.50 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)DC(Cl)Br smiles:C#CC(Cl)=C(Cl)Br H298:66.56 kcal/mol
library:CHOClBr_G4 label:COC(Br)DC(Cl)Cl smiles:COC(Br)=C(Cl)Cl H298:-26.11 kcal/mol
library:CHOClBr_G4 label:CCC(Br)DC(Cl)Br smiles:CCC(Br)=C(Cl)Br H298:4.55 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)DC(Cl)Cl smiles:C=CC(Br)=C(Cl)Cl H298:21.51 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)OBr smiles:ClC(Br)=C(Br)OBr H298:20.41 kcal/mol
library:CHOClBr_G4 label:ClCDC(Br)Br smiles:ClC=C(Br)Br H298:20.01 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DC(Cl)Br smiles:C=C(Br)C(Br)=C(Cl)Br H298:41.02 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Br smiles:O=CC(Br)=C(Cl)Br H298:-5.59 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)Br smiles:OC(Br)=C(Cl)Br H298:-19.91 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)Cl smiles:CC(Br)=C(Cl)Cl H298:-1.58 kcal/mol
library:CHOClBr_G4 label:ClCDC(Cl)Br smiles:ClC=C(Cl)Br H298:8.20 kcal/mol
library:CHOClBr_G4 label:CDCC(Cl)DC(Br)Br smiles:C=CC(Cl)=C(Br)Br H298:33.38 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Cl)DC(Br)Br smiles:C=C(Cl)C(Cl)=C(Br)Br H298:30.14 kcal/mol
library:CHOClBr_G4 label:C#CC(Cl)DC(Br)Br smiles:C#CC(Cl)=C(Br)Br H298:78.35 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)CBr smiles:ClC(Cl)=C(Br)CBr H298:5.70 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)OBr smiles:ClC(Cl)=C(Br)OBr H298:9.00 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCBr smiles:ClC(Cl)=CBr H298:8.05 kcal/mol
library:CHOClBr_G4 label:CC(Br)DC(Cl)Br smiles:CC(Br)=C(Cl)Br H298:10.24 kcal/mol
library:CHOClBr_G4 label:OC(Br)DC(Cl)Cl smiles:OC(Br)=C(Cl)Cl H298:-31.53 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Cl smiles:O=CC(Br)=C(Cl)Cl H298:-17.52 kcal/mol
library:CHOClBr_G4 label:CDC(Br)C(Br)DC(Cl)Cl smiles:C=C(Br)C(Br)=C(Cl)Cl H298:29.46 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)CBr smiles:ClC(Br)=C(Br)CBr H298:17.40 kcal/mol
library:CHOClBr_G4 label:CDCC(Br)DC(Cl)Br smiles:C=CC(Br)=C(Cl)Br H298:33.38 kcal/mol
library:CHOClBr_G4 label:CCC(Br)DC(Cl)Cl smiles:CCC(Br)=C(Cl)Cl H298:-7.13 kcal/mol
library:CHOClBr_G4 label:COC(Br)DC(Cl)Br smiles:COC(Br)=C(Cl)Br H298:-14.75 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DCBr smiles:ClC(Br)=CBr H298:19.82 kcal/mol
library:CHOClBr_G4 label:OCC(Br)DC(Cl)Br smiles:OCC(Br)=C(Cl)Br H298:-23.42 kcal/mol
library:CHOClBr_G4 label:OOC(Br)DC(Cl)Cl smiles:OOC(Br)=C(Cl)Cl H298:-9.07 kcal/mol
""",
)

entry(
    index = 92,
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
        Cpdata = ([0.625181,0.428351,0.277535,0.202859,0.0484448,-0.0283806,-0.182571],'cal/(mol*K)','+|-',[0.147336,0.169333,0.1731,0.17056,0.147899,0.127561,0.10396]),
        H298 = (9.53999,'kcal/mol','+|-',0.525241),
        S298 = (0.805085,'cal/(mol*K)','+|-',0.357983),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOF_G4 label:OCC(F)DC(F)F smiles:OCC(F)=C(F)F H298:-162.82 kcal/mol
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
library:CHOF_G4 label:FCDC(F)F smiles:FC=C(F)F H298:-118.80 kcal/mol
library:CHOF_G4 label:CC(F)(F)C(F)DC(F)F smiles:CC(F)(F)C(F)=C(F)F H298:-231.21 kcal/mol
library:CHOF_G4 label:FOC(F)DC(F)F smiles:FOC(F)=C(F)F H298:-130.68 kcal/mol
library:CHOF_G4 label:C#CC(F)DC(F)F smiles:C#CC(F)=C(F)F H298:-60.14 kcal/mol
library:CHOF_G4 label:FOOC(F)DC(F)F smiles:FOOC(F)=C(F)F H298:-113.05 kcal/mol
library:CHOF_G4 label:FC(F)DCC(F)DC(F)F smiles:FC(F)=CC(F)=C(F)F H298:-196.60 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)CCl smiles:FC(F)=C(F)CCl H298:-132.03 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)OCl smiles:FC(F)=C(F)OCl H298:-120.64 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)OBr smiles:FC(F)=C(F)OBr H298:-119.30 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)COBr smiles:FC(F)=C(F)COBr H298:-125.69 kcal/mol
library:CHOFBr_G4 label:OC(Br)C(F)DC(F)F smiles:OC(Br)C(F)=C(F)F H298:-158.85 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(F)Br smiles:FC(F)=C(F)C(F)Br H298:-162.36 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)C(Br)Br smiles:FC(F)=C(F)C(Br)Br H298:-111.54 kcal/mol
library:CHOFBr_G4 label:CC(Br)C(F)DC(F)F smiles:CC(Br)C(F)=C(F)F H298:-129.33 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DC(F)F smiles:O=C(Br)C(F)=C(F)F H298:-145.00 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)OCBr smiles:FC(F)=C(F)OCBr H298:-149.23 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CCBr smiles:FC(F)=C(F)CCBr H298:-128.85 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CDCBr smiles:FC(F)=C(F)C=CBr H298:-100.23 kcal/mol
library:CHOFBr_G4 label:CDC(Br)C(F)DC(F)F smiles:C=C(Br)C(F)=C(F)F H298:-96.86 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)CBr smiles:FC(F)=C(F)CBr H298:-121.28 kcal/mol
""",
)

entry(
    index = 93,
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
        Cpdata = ([0.931498,0.846831,0.626012,0.543721,0.243418,0.0913837,-0.0829819],'cal/(mol*K)','+|-',[0.226475,0.260287,0.266077,0.262173,0.22734,0.196078,0.1598]),
        H298 = (3.28324,'kcal/mol','+|-',0.807364),
        S298 = (-0.702183,'cal/(mol*K)','+|-',0.550267),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OC(Br)DC(Br)Br smiles:OC(Br)=C(Br)Br H298:-8.66 kcal/mol
library:CHOBr_G4 label:BrOOC(Br)DC(Br)Br smiles:BrOOC(Br)=C(Br)Br H298:49.35 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DC(Br)Br smiles:O=CC(Br)=C(Br)Br H298:6.40 kcal/mol
library:CHOBr_G4 label:BrOC(Br)DC(Br)Br smiles:BrOC(Br)=C(Br)Br H298:32.24 kcal/mol
library:CHOBr_G4 label:BrCCC(Br)DC(Br)Br smiles:BrCCC(Br)=C(Br)Br H298:21.67 kcal/mol
library:CHOBr_G4 label:OOC(Br)DC(Br)Br smiles:OOC(Br)=C(Br)Br H298:14.66 kcal/mol
library:CHOBr_G4 label:CCC(Br)DC(Br)Br smiles:CCC(Br)=C(Br)Br H298:16.41 kcal/mol
library:CHOBr_G4 label:COC(Br)DC(Br)Br smiles:COC(Br)=C(Br)Br H298:-2.97 kcal/mol
library:CHOBr_G4 label:BrCDCC(Br)DC(Br)Br smiles:BrC=CC(Br)=C(Br)Br H298:50.66 kcal/mol
library:CHOBr_G4 label:OCC(Br)DC(Br)Br smiles:OCC(Br)=C(Br)Br H298:-11.54 kcal/mol
library:CHOBr_G4 label:BrC#CC(Br)DC(Br)Br smiles:BrC#CC(Br)=C(Br)Br H298:99.61 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DC(Br)Br smiles:BrCC(Br)=C(Br)Br H298:29.27 kcal/mol
library:CHOBr_G4 label:BrCOC(Br)DC(Br)Br smiles:BrCOC(Br)=C(Br)Br H298:1.21 kcal/mol
library:CHOBr_G4 label:CDCC(Br)DC(Br)Br smiles:C=CC(Br)=C(Br)Br H298:45.35 kcal/mol
library:CHOBr_G4 label:BrOCC(Br)DC(Br)Br smiles:BrOCC(Br)=C(Br)Br H298:25.08 kcal/mol
library:CHOBr_G4 label:C#CC(Br)DC(Br)Br smiles:C#CC(Br)=C(Br)Br H298:89.65 kcal/mol
library:CHOBr_G4 label:CC(Br)DC(Br)Br smiles:CC(Br)=C(Br)Br H298:22.15 kcal/mol
library:CHOBr_G4 label:BrCDC(Br)Br smiles:BrC=C(Br)Br H298:31.71 kcal/mol
library:CHOFBr_G4 label:FCDCC(Br)DC(Br)Br smiles:FC=CC(Br)=C(Br)Br H298:1.03 kcal/mol
library:CHOFBr_G4 label:FC#CC(Br)DC(Br)Br smiles:FC#CC(Br)=C(Br)Br H298:61.65 kcal/mol
library:CHOFBr_G4 label:CDC(F)C(Br)DC(Br)Br smiles:C=C(F)C(Br)=C(Br)Br H298:3.61 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)C(Br)DC(Br)Br smiles:C=C(Cl)C(Br)=C(Br)Br H298:41.41 kcal/mol
""",
)

entry(
    index = 94,
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
        Cpdata = ([0.366857,0.381128,0.254896,0.214348,0.0477577,-0.064955,-0.228799],'cal/(mol*K)','+|-',[0.129073,0.148343,0.151643,0.149418,0.129566,0.111749,0.0910733]),
        H298 = (2.69645,'kcal/mol','+|-',0.460135),
        S298 = (0.209895,'cal/(mol*K)','+|-',0.31361),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:FC(F)DC(Cl)Cl smiles:FC(F)=C(Cl)Cl H298:-84.81 kcal/mol
library:CHOFCl_G4 label:FC(F)DC(F)Cl smiles:FC(F)=C(F)Cl H298:-121.29 kcal/mol
library:CHOFCl_G4 label:FC(Cl)DC(Cl)Cl smiles:FC(Cl)=C(Cl)Cl H298:-44.16 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Cl)Br smiles:FC(Cl)=C(Cl)Br H298:-32.62 kcal/mol
library:CHOFClBr_G4 label:FC(F)DC(Cl)Br smiles:FC(F)=C(Cl)Br H298:-73.27 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DC(Br)Br smiles:FC(Cl)=C(Br)Br H298:-21.04 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(F)Br smiles:FC(F)=C(F)Br H298:-108.88 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(Br)Br smiles:FC(F)=C(Br)Br H298:-61.92 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(Br)Br smiles:FC(Br)=C(Br)Br H298:-8.49 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DC(Br)Br smiles:ClC(Br)=C(Br)Br H298:29.12 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Br)Br smiles:ClC(Cl)=C(Br)Br H298:17.28 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DC(Cl)Br smiles:ClC(Cl)=C(Cl)Br H298:5.62 kcal/mol
""",
)

entry(
    index = 95,
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
        Cpdata = ([0.139807,0.220789,0.119538,0.0837255,0.012029,-0.0449159,-0.192433],'cal/(mol*K)','+|-',[0.421938,0.484932,0.495719,0.488447,0.423549,0.365307,0.297717]),
        H298 = (6.56934,'kcal/mol','+|-',1.50417),
        S298 = (-0.699783,'cal/(mol*K)','+|-',1.02519),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOF_G4 label:FC(F)DC(F)F smiles:FC(F)=C(F)F H298:-160.66 kcal/mol
""",
)

entry(
    index = 96,
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
        Cpdata = ([0.479746,0.529404,0.381618,0.348283,0.122474,-0.0464348,-0.235161],'cal/(mol*K)','+|-',[0.431171,0.495544,0.506567,0.499135,0.432818,0.373301,0.304232]),
        H298 = (2.03071,'kcal/mol','+|-',1.53709),
        S298 = (-0.870439,'cal/(mol*K)','+|-',1.04762),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrC(Br)DC(Br)Br smiles:BrC(Br)=C(Br)Br H298:40.84 kcal/mol
""",
)

entry(
    index = 97,
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
    index = 98,
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
        Cpdata = ([-1.06386,-1.20862,-0.943059,-0.789355,-0.620847,-0.373784,0.753352],'cal/(mol*K)','+|-',[0.297735,0.342185,0.349797,0.344665,0.298871,0.257774,0.21008]),
        H298 = (1.12112,'kcal/mol','+|-',1.0614),
        S298 = (-0.692179,'cal/(mol*K)','+|-',0.723407),
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
library:CHOFBr_G4 label:CDC(F)C(DO)Br smiles:C=C(F)C(=O)Br H298:-61.44 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DC(F)F smiles:O=C(Br)C(F)=C(F)F H298:-145.00 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)DCF smiles:O=C(Br)C(F)=CF H298:-101.47 kcal/mol
""",
)

entry(
    index = 99,
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
        Cpdata = ([-0.422772,-0.744553,-0.613767,-0.56569,-0.556662,-0.380805,0.784709],'cal/(mol*K)','+|-',[0.283564,0.325899,0.333148,0.328261,0.284646,0.245505,0.200081]),
        H298 = (1.50026,'kcal/mol','+|-',1.01088),
        S298 = (-0.468017,'cal/(mol*K)','+|-',0.688976),
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
    index = 100,
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
        Cpdata = ([-0.20967,-0.406407,-0.293647,-0.27708,-0.33155,-0.20493,0.914061],'cal/(mol*K)','+|-',[0.259266,0.297974,0.304602,0.300134,0.260256,0.224469,0.182937]),
        H298 = (1.5797,'kcal/mol','+|-',0.924263),
        S298 = (-1.67374,'cal/(mol*K)','+|-',0.629941),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODC(Br)C(Br)DCBr smiles:O=C(Br)C(Br)=CBr H298:-4.80 kcal/mol
library:CHOBr_G4 label:CDC(Br)CDO smiles:C=C(Br)C=O H298:-9.79 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DC(Br)Br smiles:O=CC(Br)=C(Br)Br H298:6.40 kcal/mol
library:CHOBr_G4 label:CDC(Br)C(DO)Br smiles:C=C(Br)C(=O)Br H298:-11.04 kcal/mol
library:CHOBr_G4 label:ODCC(Br)DCBr smiles:O=CC(Br)=CBr H298:-3.70 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)DC(F)Cl smiles:O=CC(Br)=C(F)Cl H298:-57.02 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)Br smiles:O=C(Br)C(Br)=C(F)Br H298:-42.46 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DCF smiles:O=C(Br)C(Br)=CF H298:-54.16 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)Br smiles:O=CC(Br)=C(F)Br H298:-44.37 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DC(F)F smiles:O=CC(Br)=C(F)F H298:-99.11 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)DC(F)F smiles:O=C(Br)C(Br)=C(F)F H298:-97.65 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)DCF smiles:O=CC(Br)=CF H298:-52.97 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DCCl smiles:O=CC(Br)=CCl H298:-15.61 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Br smiles:O=CC(Br)=C(Cl)Br H298:-5.59 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)DC(Cl)Cl smiles:O=CC(Br)=C(Cl)Cl H298:-17.52 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)DCCl smiles:O=C(Br)C(Br)=CCl H298:-16.71 kcal/mol
""",
)

entry(
    index = 101,
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
        Cpdata = ([0.953551,0.775975,0.542237,0.323105,-0.028744,-0.256398,-0.244508],'cal/(mol*K)','+|-',[0.149953,0.17234,0.176174,0.173589,0.150525,0.129827,0.105806]),
        H298 = (7.42177,'kcal/mol','+|-',0.534568),
        S298 = (1.27642,'cal/(mol*K)','+|-',0.364341),
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
library:CHOFClBr_G4 label:ODC(Br)C(F)(Cl)Cl smiles:O=C(Br)C(F)(Cl)Cl H298:-90.00 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)(Cl)Br smiles:O=C(Br)C(F)(Cl)Br H298:-77.18 kcal/mol
library:CHOFClBr_G4 label:ODC(O)C(F)(Cl)Br smiles:O=C(O)C(F)(Cl)Br H298:-136.05 kcal/mol
library:CHOFClBr_G4 label:CC(DO)C(F)(Cl)Br smiles:CC(=O)C(F)(Cl)Br H298:-90.56 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)(F)Cl smiles:O=C(Br)C(F)(F)Cl H298:-136.14 kcal/mol
library:CHOFClBr_G4 label:ODCC(F)(Cl)Br smiles:O=CC(F)(Cl)Br H298:-77.47 kcal/mol
library:CHOFBr_G4 label:ODC(O)C(F)(F)Br smiles:O=C(O)C(F)(F)Br H298:-182.08 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)Br smiles:O=C(Br)C(F)(F)Br H298:-123.03 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)(Br)Br smiles:O=C(OBr)C(F)(Br)Br H298:-82.27 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)(F)Br smiles:O=C(OBr)C(F)(F)Br H298:-140.27 kcal/mol
library:CHOFBr_G4 label:CC(DO)C(F)(F)Br smiles:CC(=O)C(F)(F)Br H298:-136.43 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(Br)Br smiles:O=C(CF)C(F)(Br)Br H298:-115.02 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(F)Br smiles:O=C(CF)C(F)(F)Br H298:-173.40 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)Br smiles:O=CC(F)(Br)Br H298:-65.30 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(Br)Br smiles:O=C(CBr)C(F)(Br)Br H298:-67.54 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(F)Br smiles:O=CC(F)(F)Br H298:-122.61 kcal/mol
library:CHOFBr_G4 label:ODC(O)C(F)(Br)Br smiles:O=C(O)C(F)(Br)Br H298:-123.69 kcal/mol
library:CHOFBr_G4 label:CC(DO)C(F)(Br)Br smiles:CC(=O)C(F)(Br)Br H298:-78.37 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)Br smiles:O=C(CBr)C(F)(F)Br H298:-125.40 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)Br smiles:O=C(Br)C(F)(Br)Br H298:-65.31 kcal/mol
library:CHOClBr_G4 label:ODC(O)C(Cl)(Br)Br smiles:O=C(O)C(Cl)(Br)Br H298:-81.04 kcal/mol
library:CHOClBr_G4 label:CC(DO)C(Cl)(Cl)Br smiles:CC(=O)C(Cl)(Cl)Br H298:-47.85 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)(Br)Br smiles:O=C(Br)C(Cl)(Br)Br H298:-23.07 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)Br smiles:O=CC(Cl)(Br)Br H298:-24.09 kcal/mol
library:CHOClBr_G4 label:CC(DO)C(Cl)(Br)Br smiles:CC(=O)C(Cl)(Br)Br H298:-36.14 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Cl)Br smiles:O=CC(Cl)(Cl)Br H298:-35.59 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)(Cl)Br smiles:O=C(Br)C(Cl)(Cl)Br H298:-34.71 kcal/mol
library:CHOClBr_G4 label:ODC(O)C(Cl)(Cl)Br smiles:O=C(O)C(Cl)(Cl)Br H298:-92.73 kcal/mol
""",
)

entry(
    index = 102,
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
        Cpdata = ([6.53889,7.49653,8.158,8.63821,9.28364,9.68885,10.1414],'cal/(mol*K)','+|-',[0.107436,0.123475,0.126222,0.12437,0.107846,0.093016,0.075806]),
        H298 = (-76.744,'kcal/mol','+|-',0.382999),
        S298 = (20.38,'cal/(mol*K)','+|-',0.261037),
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
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)F smiles:O=C(CBr)C(F)(F)F H298:-188.19 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)(F)F smiles:O=C(OBr)C(F)(F)F H298:-203.40 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(F)F smiles:O=C(Br)C(F)(F)F H298:-185.80 kcal/mol
""",
)

entry(
    index = 103,
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
        Cpdata = ([8.53339,9.22218,9.62585,9.92838,10.3325,10.5418,10.642],'cal/(mol*K)','+|-',[0.120048,0.137971,0.14104,0.138971,0.120507,0.103936,0.0847056]),
        H298 = (-7.01806,'kcal/mol','+|-',0.427963),
        S298 = (23.8027,'cal/(mol*K)','+|-',0.291682),
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
library:CHOClBr_G4 label:ODC(Br)C(Cl)(Cl)Cl smiles:O=C(Br)C(Cl)(Cl)Cl H298:-46.40 kcal/mol
""",
)

entry(
    index = 104,
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
        Cpdata = ([9.16903,9.69012,9.97127,10.1569,10.3976,10.5269,10.5789],'cal/(mol*K)','+|-',[0.186043,0.213819,0.218575,0.215368,0.186753,0.161073,0.131271]),
        H298 = (9.71679,'kcal/mol','+|-',0.663228),
        S298 = (28.7196,'cal/(mol*K)','+|-',0.45203),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODCC(Br)(Br)Br smiles:O=CC(Br)(Br)Br H298:-12.59 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)(Br)Br smiles:O=C(Br)C(Br)(Br)Br H298:-11.54 kcal/mol
library:CHOBr_G4 label:ODC(O)C(Br)(Br)Br smiles:O=C(O)C(Br)(Br)Br H298:-69.31 kcal/mol
library:CHOBr_G4 label:CC(DO)C(Br)(Br)Br smiles:CC(=O)C(Br)(Br)Br H298:-24.52 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)(Br)Br smiles:O=C(CF)C(Br)(Br)Br H298:-61.84 kcal/mol
""",
)

entry(
    index = 105,
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
        Cpdata = ([1.00173,0.803673,0.610895,0.405257,0.0980061,-0.0583939,-0.0230311],'cal/(mol*K)','+|-',[0.123289,0.141696,0.144848,0.142723,0.12376,0.106742,0.0869924]),
        H298 = (5.35662,'kcal/mol','+|-',0.439516),
        S298 = (0.478493,'cal/(mol*K)','+|-',0.299557),
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
library:CHOFClBr_G4 label:ODC(F)C(O)(Cl)Br smiles:O=C(F)C(O)(Cl)Br H298:-134.34 kcal/mol
library:CHOFClBr_G4 label:ODCC(Cl)(Br)CF smiles:O=CC(Cl)(Br)CF H298:-85.46 kcal/mol
library:CHOFClBr_G4 label:ODCC(F)(Cl)OBr smiles:O=CC(F)(Cl)OBr H298:-91.26 kcal/mol
library:CHOFClBr_G4 label:ODC(CBr)C(F)Cl smiles:O=C(CBr)C(F)Cl H298:-88.70 kcal/mol
library:CHOFClBr_G4 label:ODC(Br)C(F)Cl smiles:O=C(Br)C(F)Cl H298:-86.84 kcal/mol
library:CHOFClBr_G4 label:ODC(OBr)C(F)Cl smiles:O=C(OBr)C(F)Cl H298:-103.88 kcal/mol
library:CHOFClBr_G4 label:ODC(CF)C(Cl)Br smiles:O=C(CF)C(Cl)Br H298:-85.17 kcal/mol
library:CHOFClBr_G4 label:CC(F)(Cl)C(DO)Br smiles:CC(F)(Cl)C(=O)Br H298:-99.47 kcal/mol
library:CHOFBr_G4 label:ODCC(O)(F)Br smiles:O=CC(O)(F)Br H298:-121.69 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(F)(Br)OBr smiles:O=C(F)C(F)(Br)OBr H298:-137.18 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)Br smiles:O=C(OBr)C(F)Br H298:-91.83 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)OBr smiles:O=CC(F)(Br)OBr H298:-78.78 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)Br smiles:O=C(Br)C(F)Br H298:-74.82 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)CDO smiles:CC(F)(Br)C=O H298:-86.12 kcal/mol
library:CHOFBr_G4 label:CC(F)(Br)C(DO)Br smiles:CC(F)(Br)C(=O)Br H298:-87.33 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)Br smiles:O=C(CBr)C(F)Br H298:-76.67 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)Br smiles:O=C(CF)C(F)Br H298:-124.54 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(F)Br smiles:O=C(C(F)F)C(F)Br H298:-172.88 kcal/mol
library:CHOFBr_G4 label:ODCC(F)Br smiles:O=CC(F)Br H298:-73.38 kcal/mol
library:CHOFBr_G4 label:CC(DO)C(F)Br smiles:CC(=O)C(F)Br H298:-87.11 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)CF smiles:O=CC(F)(Br)CF H298:-125.86 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(Br)C(F)F smiles:O=CC(F)(Br)C(F)F H298:-174.88 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(O)(F)Br smiles:O=C(F)C(O)(F)Br H298:-178.91 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)(Br)CF smiles:O=C(Br)C(F)(Br)CF H298:-127.21 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)Br)C(Br)Br smiles:O=C(C(F)Br)C(Br)Br H298:-66.25 kcal/mol
library:CHOFBr_G4 label:ODC(O)C(F)Br smiles:O=C(O)C(F)Br H298:-133.25 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)Br smiles:O=C(Br)C(Cl)Br H298:-35.32 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)C(DO)Br smiles:CC(Cl)(Br)C(=O)Br H298:-45.94 kcal/mol
library:CHOClBr_G4 label:CC(DO)C(Cl)Br smiles:CC(=O)C(Cl)Br H298:-47.40 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Br smiles:O=C(CBr)C(Cl)Br H298:-37.01 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)Br smiles:O=CC(Cl)Br H298:-34.47 kcal/mol
library:CHOClBr_G4 label:ODCC(O)(Cl)Br smiles:O=CC(O)(Cl)Br H298:-78.16 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)OBr smiles:O=CC(Cl)(Br)OBr H298:-34.74 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Br)CDO smiles:CC(Cl)(Br)C=O H298:-45.93 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Br)CCl smiles:O=CC(Cl)(Br)CCl H298:-47.31 kcal/mol
library:CHOClBr_G4 label:ODC(O)C(Cl)Br smiles:O=C(O)C(Cl)Br H298:-93.36 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Cl)Br smiles:O=C(CCl)C(Cl)Br H298:-47.73 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(O)(Cl)Br smiles:O=C(Cl)C(O)(Cl)Br H298:-89.10 kcal/mol
""",
)

entry(
    index = 106,
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
        Cpdata = ([0.553053,0.359619,0.23948,0.102061,-0.0455756,-0.126411,0.0661729],'cal/(mol*K)','+|-',[0.155228,0.178402,0.182371,0.179695,0.15582,0.134394,0.109528]),
        H298 = (5.69302,'kcal/mol','+|-',0.553373),
        S298 = (0.255621,'cal/(mol*K)','+|-',0.377157),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
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
library:CHOFBr_G4 label:ODC(Br)C(F)F smiles:O=C(Br)C(F)F H298:-130.80 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)F smiles:O=C(CBr)C(F)F H298:-132.04 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(Br)Br smiles:O=C(C(F)F)C(Br)Br H298:-121.83 kcal/mol
library:CHOFBr_G4 label:ODCC(F)(F)OBr smiles:O=CC(F)(F)OBr H298:-138.86 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(F)Br smiles:O=C(C(F)F)C(F)Br H298:-172.88 kcal/mol
library:CHOFBr_G4 label:ODC(OBr)C(F)F smiles:O=C(OBr)C(F)F H298:-147.99 kcal/mol
library:CHOFBr_G4 label:CC(F)(F)C(DO)Br smiles:CC(F)(F)C(=O)Br H298:-144.70 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(F)(F)OBr smiles:O=C(F)C(F)(F)OBr H298:-197.89 kcal/mol
""",
)

entry(
    index = 107,
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
        Cpdata = ([1.03875,0.946333,0.783166,0.574621,0.293886,0.112986,0.159695],'cal/(mol*K)','+|-',[0.166279,0.191104,0.195355,0.192489,0.166914,0.143962,0.117325]),
        H298 = (3.32449,'kcal/mol','+|-',0.59277),
        S298 = (-1.03523,'cal/(mol*K)','+|-',0.404009),
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
library:CHOClBr_G4 label:ODC(OBr)C(Cl)Cl smiles:O=C(OBr)C(Cl)Cl H298:-63.36 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Cl smiles:O=C(CBr)C(Cl)Cl H298:-48.29 kcal/mol
library:CHOClBr_G4 label:CC(Cl)(Cl)C(DO)Br smiles:CC(Cl)(Cl)C(=O)Br H298:-57.47 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)(Cl)OBr smiles:O=CC(Cl)(Cl)OBr H298:-46.55 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)Cl smiles:O=C(Br)C(Cl)Cl H298:-46.51 kcal/mol
""",
)

entry(
    index = 108,
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
        Cpdata = ([0.72324,0.70693,0.609928,0.457264,0.256316,0.115386,0.119257],'cal/(mol*K)','+|-',[0.183947,0.211409,0.216112,0.212941,0.184649,0.159258,0.129792]),
        H298 = (3.28059,'kcal/mol','+|-',0.655754),
        S298 = (-0.42528,'cal/(mol*K)','+|-',0.446936),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODCC(Br)(Br)OBr smiles:O=CC(Br)(Br)OBr H298:-22.93 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)CDO smiles:CC(Br)(Br)C=O H298:-34.63 kcal/mol
library:CHOBr_G4 label:ODCC(Br)Br smiles:O=CC(Br)Br H298:-23.38 kcal/mol
library:CHOBr_G4 label:ODCC(O)(Br)Br smiles:O=CC(O)(Br)Br H298:-66.44 kcal/mol
library:CHOBr_G4 label:ODC(CBr)C(Br)Br smiles:O=C(CBr)C(Br)Br H298:-25.78 kcal/mol
library:CHOBr_G4 label:CC(DO)C(Br)Br smiles:CC(=O)C(Br)Br H298:-36.12 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)Br smiles:O=C(Br)C(Br)Br H298:-24.22 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(O)(Br)Br smiles:O=C(Br)C(O)(Br)Br H298:-64.69 kcal/mol
library:CHOBr_G4 label:ODC(OBr)C(Br)Br smiles:O=C(OBr)C(Br)Br H298:-41.13 kcal/mol
library:CHOBr_G4 label:ODC(O)C(Br)Br smiles:O=C(O)C(Br)Br H298:-82.14 kcal/mol
library:CHOBr_G4 label:CC(Br)(Br)C(DO)Br smiles:CC(Br)(Br)C(=O)Br H298:-34.40 kcal/mol
library:CHOBr_G4 label:ODCC(Br)(Br)CBr smiles:O=CC(Br)(Br)CBr H298:-25.64 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)Br smiles:O=CC(Br)(Br)C(F)Br H298:-67.07 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)C(F)F smiles:O=CC(Br)(Br)C(F)F H298:-124.54 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(O)(Br)Br smiles:O=C(F)C(O)(Br)Br H298:-122.34 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)Br smiles:O=C(CF)C(Br)Br H298:-73.80 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)F)C(Br)Br smiles:O=C(C(F)F)C(Br)Br H298:-121.83 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)(Br)CF smiles:O=C(Br)C(Br)(Br)CF H298:-74.56 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)(Br)CF smiles:O=CC(Br)(Br)CF H298:-74.33 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(Br)(Br)OBr smiles:O=C(F)C(Br)(Br)OBr H298:-80.48 kcal/mol
library:CHOFBr_G4 label:ODC(C(F)Br)C(Br)Br smiles:O=C(C(F)Br)C(Br)Br H298:-66.25 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)(Br)CCl smiles:O=CC(Br)(Br)CCl H298:-36.69 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(O)(Br)Br smiles:O=C(Cl)C(O)(Br)Br H298:-77.16 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Br)Br smiles:O=C(CCl)C(Br)Br H298:-36.52 kcal/mol
""",
)

entry(
    index = 109,
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
    index = 110,
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
        Cpdata = ([0.766257,0.642872,0.526694,0.407388,0.264391,0.129391,0.199383],'cal/(mol*K)','+|-',[0.136672,0.157077,0.160571,0.158215,0.137194,0.118328,0.096435]),
        H298 = (2.88294,'kcal/mol','+|-',0.487224),
        S298 = (-0.429316,'cal/(mol*K)','+|-',0.332073),
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
library:CHOFClBr_G4 label:ODC(CF)C(Cl)Br smiles:O=C(CF)C(Cl)Br H298:-85.17 kcal/mol
library:CHOFBr_G4 label:CC(F)C(DO)Br smiles:CC(F)C(=O)Br H298:-93.33 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CF smiles:O=C(Br)CF H298:-83.38 kcal/mol
library:CHOFBr_G4 label:ODCC(F)OBr smiles:O=CC(F)OBr H298:-84.25 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)CF smiles:O=C(Br)C(F)CF H298:-133.66 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(Br)Br smiles:O=C(CF)C(F)(Br)Br H298:-115.02 kcal/mol
library:CHOFBr_G4 label:ODC(CF)CBr smiles:O=C(CF)CBr H298:-83.38 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)Br smiles:O=C(CF)C(Br)Br H298:-73.80 kcal/mol
library:CHOFBr_G4 label:ODC(CF)OBr smiles:O=C(CF)OBr H298:-99.57 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(F)OBr smiles:O=C(F)C(F)OBr H298:-144.94 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(F)C(F)F smiles:O=C(Br)C(F)C(F)F H298:-182.78 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)(F)Br smiles:O=C(CF)C(F)(F)Br H298:-173.40 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(F)Br smiles:O=C(CF)C(F)Br H298:-124.54 kcal/mol
library:CHOFBr_G4 label:ODC(CF)C(Br)(Br)Br smiles:O=C(CF)C(Br)(Br)Br H298:-61.84 kcal/mol
""",
)

entry(
    index = 111,
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
        Cpdata = ([0.907799,0.657924,0.459162,0.259969,0.0188469,-0.137679,-0.0584824],'cal/(mol*K)','+|-',[0.141474,0.162596,0.166213,0.163774,0.142014,0.122486,0.0998235]),
        H298 = (2.82528,'kcal/mol','+|-',0.504344),
        S298 = (0.119868,'cal/(mol*K)','+|-',0.343741),
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
library:CHOFClBr_G4 label:ODC(Br)C(Cl)CF smiles:O=C(Br)C(Cl)CF H298:-95.03 kcal/mol
library:CHOFClBr_G4 label:ODC(F)C(Cl)OBr smiles:O=C(F)C(Cl)OBr H298:-101.00 kcal/mol
library:CHOClBr_G4 label:ODCC(Cl)OBr smiles:O=CC(Cl)OBr H298:-42.03 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)OBr smiles:O=C(CCl)OBr H298:-61.83 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(Cl)OBr smiles:O=C(Cl)C(Cl)OBr H298:-55.20 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Cl)CCl smiles:O=C(Br)C(Cl)CCl H298:-57.99 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Br)Br smiles:O=C(CCl)C(Br)Br H298:-36.52 kcal/mol
library:CHOClBr_G4 label:ODC(Br)CCl smiles:O=C(Br)CCl H298:-45.49 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)CBr smiles:O=C(CCl)CBr H298:-45.75 kcal/mol
library:CHOClBr_G4 label:CC(Cl)C(DO)Br smiles:CC(Cl)C(=O)Br H298:-53.72 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)C(Cl)Br smiles:O=C(CCl)C(Cl)Br H298:-47.73 kcal/mol
""",
)

entry(
    index = 112,
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
        Cpdata = ([0.623537,0.409917,0.257852,0.105523,-0.0121101,-0.0816768,0.0108625],'cal/(mol*K)','+|-',[0.136675,0.157081,0.160575,0.158219,0.137197,0.118331,0.0964375]),
        H298 = (2.4411,'kcal/mol','+|-',0.487237),
        S298 = (-0.19929,'cal/(mol*K)','+|-',0.332081),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CC(Br)CDO smiles:CC(Br)C=O H298:-39.97 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)CBr smiles:O=C(Br)C(Br)CBr H298:-37.86 kcal/mol
library:CHOBr_G4 label:ODC(CBr)C(Br)Br smiles:O=C(CBr)C(Br)Br H298:-25.78 kcal/mol
library:CHOBr_G4 label:ODC(CBr)OBr smiles:O=C(CBr)OBr H298:-51.24 kcal/mol
library:CHOBr_G4 label:ODCCBr smiles:O=CCBr H298:-31.30 kcal/mol
library:CHOBr_G4 label:CC(Br)C(DO)Br smiles:CC(Br)C(=O)Br H298:-42.98 kcal/mol
library:CHOBr_G4 label:ODC(Br)CBr smiles:O=C(Br)CBr H298:-34.36 kcal/mol
library:CHOBr_G4 label:ODCC(O)Br smiles:O=CC(O)Br H298:-72.86 kcal/mol
library:CHOBr_G4 label:CC(DO)CBr smiles:CC(=O)CBr H298:-43.67 kcal/mol
library:CHOBr_G4 label:ODCC(Br)OBr smiles:O=CC(Br)OBr H298:-30.49 kcal/mol
library:CHOBr_G4 label:ODCC(Br)CBr smiles:O=CC(Br)CBr H298:-33.05 kcal/mol
library:CHOBr_G4 label:ODCC(Br)C(Br)Br smiles:O=CC(Br)C(Br)Br H298:-23.66 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(O)Br smiles:O=C(Br)C(O)Br H298:-74.38 kcal/mol
library:CHOBr_G4 label:ODC(CBr)CBr smiles:O=C(CBr)CBr H298:-35.27 kcal/mol
library:CHOBr_G4 label:ODC(Br)C(Br)OBr smiles:O=C(Br)C(Br)OBr H298:-31.46 kcal/mol
library:CHOBr_G4 label:ODC(O)CBr smiles:O=C(O)CBr H298:-92.18 kcal/mol
library:CHOFClBr_G4 label:ODC(CBr)C(F)Cl smiles:O=C(CBr)C(F)Cl H298:-88.70 kcal/mol
library:CHOFClBr_G4 label:ODCC(Br)C(F)Cl smiles:O=CC(Br)C(F)Cl H298:-87.89 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)F smiles:O=C(CBr)C(F)(F)F H298:-188.19 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)Br smiles:O=CC(Br)C(F)Br H298:-75.41 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)Br smiles:O=C(Br)C(Br)C(F)Br H298:-77.92 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)F smiles:O=CC(Br)C(F)F H298:-132.46 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(Br)OBr smiles:O=C(F)C(Br)OBr H298:-90.02 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)CF smiles:O=CC(Br)CF H298:-81.11 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)CF smiles:O=C(Br)C(Br)CF H298:-84.59 kcal/mol
library:CHOFBr_G4 label:ODC(Br)C(Br)C(F)F smiles:O=C(Br)C(Br)C(F)F H298:-135.53 kcal/mol
library:CHOFBr_G4 label:ODC(CF)CBr smiles:O=C(CF)CBr H298:-83.38 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)Br smiles:O=C(CBr)C(F)Br H298:-76.67 kcal/mol
library:CHOFBr_G4 label:ODC(F)C(O)Br smiles:O=C(F)C(O)Br H298:-132.63 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)F smiles:O=C(CBr)C(F)F H298:-132.04 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(Br)Br smiles:O=C(CBr)C(F)(Br)Br H298:-67.54 kcal/mol
library:CHOFBr_G4 label:ODC(CBr)C(F)(F)Br smiles:O=C(CBr)C(F)(F)Br H298:-125.40 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)Br smiles:O=CC(Br)C(F)(F)Br H298:-125.99 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(Br)Br smiles:O=CC(Br)C(F)(Br)Br H298:-66.91 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)F smiles:O=CC(Br)C(F)(F)F H298:-189.44 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(O)Br smiles:O=C(Cl)C(O)Br H298:-86.91 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Cl smiles:O=CC(Br)C(Cl)Cl H298:-46.56 kcal/mol
library:CHOClBr_G4 label:ODC(Cl)C(Br)OBr smiles:O=C(Cl)C(Br)OBr H298:-44.63 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Br smiles:O=C(CBr)C(Cl)Br H298:-37.01 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)CCl smiles:O=CC(Br)CCl H298:-43.86 kcal/mol
library:CHOClBr_G4 label:ODC(CBr)C(Cl)Cl smiles:O=C(CBr)C(Cl)Cl H298:-48.29 kcal/mol
library:CHOClBr_G4 label:ODC(CCl)CBr smiles:O=C(CCl)CBr H298:-45.75 kcal/mol
library:CHOClBr_G4 label:ODCC(Br)C(Cl)Br smiles:O=CC(Br)C(Cl)Br H298:-34.77 kcal/mol
library:CHOClBr_G4 label:ODC(Br)C(Br)CCl smiles:O=C(Br)C(Br)CCl H298:-47.62 kcal/mol
""",
)

entry(
    index = 113,
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
    index = 114,
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
        Cpdata = ([0.0670598,0.0484804,0.0276092,0.140954,0.356983,0.353706,0.503953],'cal/(mol*K)','+|-',[0.124756,0.143381,0.146571,0.14442,0.125232,0.108011,0.0880269]),
        H298 = (0.345464,'kcal/mol','+|-',0.444744),
        S298 = (-1.2655,'cal/(mol*K)','+|-',0.303119),
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
library:CHOFClBr_G4 label:FC(Cl)(Cl)COBr smiles:FC(Cl)(Cl)COBr H298:-73.70 kcal/mol
library:CHOFClBr_G4 label:OOCC(F)(Cl)Br smiles:OOCC(F)(Cl)Br H298:-80.47 kcal/mol
library:CHOFClBr_G4 label:OCC(F)(Cl)Br smiles:OCC(F)(Cl)Br H298:-101.29 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)(Br)COBr smiles:FC(Cl)(Br)COBr H298:-61.06 kcal/mol
library:CHOFClBr_G4 label:OC(O)C(F)(Cl)Br smiles:OC(O)C(F)(Cl)Br H298:-146.34 kcal/mol
library:CHOFClBr_G4 label:FC(F)(Cl)COBr smiles:FC(F)(Cl)COBr H298:-121.20 kcal/mol
library:CHOFClBr_G4 label:CC(O)C(F)(Cl)Br smiles:CC(O)C(F)(Cl)Br H298:-110.42 kcal/mol
library:CHOFClBr_G4 label:COCC(F)(Cl)Br smiles:COCC(F)(Cl)Br H298:-95.40 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)COBr smiles:FC(F)(Br)COBr H298:-107.55 kcal/mol
library:CHOFBr_G4 label:OC(CBr)C(F)(F)Br smiles:OC(CBr)C(F)(F)Br H298:-149.50 kcal/mol
library:CHOFBr_G4 label:OC(O)C(F)(Br)Br smiles:OC(O)C(F)(Br)Br H298:-133.70 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)COOBr smiles:FC(Br)(Br)COOBr H298:-32.79 kcal/mol
library:CHOFBr_G4 label:OC(CBr)C(F)(Br)Br smiles:OC(CBr)C(F)(Br)Br H298:-90.57 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)COCBr smiles:FC(F)(Br)COCBr H298:-139.23 kcal/mol
library:CHOFBr_G4 label:OCC(F)(Br)Br smiles:OCC(F)(Br)Br H298:-88.63 kcal/mol
library:CHOFBr_G4 label:OC(O)C(F)(F)Br smiles:OC(O)C(F)(F)Br H298:-192.73 kcal/mol
library:CHOFBr_G4 label:OC(CF)C(F)(F)Br smiles:OC(CF)C(F)(F)Br H298:-197.71 kcal/mol
library:CHOFBr_G4 label:OOCC(F)(Br)Br smiles:OOCC(F)(Br)Br H298:-68.33 kcal/mol
library:CHOFBr_G4 label:CC(OBr)C(F)(F)Br smiles:CC(OBr)C(F)(F)Br H298:-117.73 kcal/mol
library:CHOFBr_G4 label:COCC(F)(F)Br smiles:COCC(F)(F)Br H298:-142.13 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)COBr smiles:FC(Br)(Br)COBr H298:-48.52 kcal/mol
library:CHOFBr_G4 label:OCC(F)(F)Br smiles:OCC(F)(F)Br H298:-147.61 kcal/mol
library:CHOFBr_G4 label:CC(OBr)C(F)(Br)Br smiles:CC(OBr)C(F)(Br)Br H298:-58.57 kcal/mol
library:CHOFBr_G4 label:OC(OBr)C(F)(F)Br smiles:OC(OBr)C(F)(F)Br H298:-153.50 kcal/mol
library:CHOFBr_G4 label:OC(CF)C(F)(Br)Br smiles:OC(CF)C(F)(Br)Br H298:-138.22 kcal/mol
library:CHOFBr_G4 label:CC(O)C(F)(F)Br smiles:CC(O)C(F)(F)Br H298:-157.23 kcal/mol
library:CHOFBr_G4 label:OOCC(F)(F)Br smiles:OOCC(F)(F)Br H298:-127.37 kcal/mol
library:CHOFBr_G4 label:FC(F)(Br)COOBr smiles:FC(F)(Br)COOBr H298:-91.61 kcal/mol
library:CHOFBr_G4 label:CC(O)C(F)(Br)Br smiles:CC(O)C(F)(Br)Br H298:-98.31 kcal/mol
library:CHOFBr_G4 label:OC(OBr)C(F)(Br)Br smiles:OC(OBr)C(F)(Br)Br H298:-94.38 kcal/mol
library:CHOFBr_G4 label:FC(Br)(Br)COCBr smiles:FC(Br)(Br)COCBr H298:-79.90 kcal/mol
library:CHOFBr_G4 label:COCC(F)(Br)Br smiles:COCC(F)(Br)Br H298:-82.82 kcal/mol
library:CHOClBr_G4 label:CC(O)C(Cl)(Br)Br smiles:CC(O)C(Cl)(Br)Br H298:-56.15 kcal/mol
library:CHOClBr_G4 label:OOCC(Cl)(Br)Br smiles:OOCC(Cl)(Br)Br H298:-26.12 kcal/mol
library:CHOClBr_G4 label:CC(O)C(Cl)(Cl)Br smiles:CC(O)C(Cl)(Cl)Br H298:-68.03 kcal/mol
library:CHOClBr_G4 label:OOCC(Cl)(Cl)Br smiles:OOCC(Cl)(Cl)Br H298:-38.03 kcal/mol
library:CHOClBr_G4 label:ClC(Br)(Br)COBr smiles:ClC(Br)(Br)COBr H298:-6.80 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Cl)Br smiles:OCC(Cl)(Cl)Br H298:-58.70 kcal/mol
library:CHOClBr_G4 label:COCC(Cl)(Cl)Br smiles:COCC(Cl)(Cl)Br H298:-52.78 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)(Br)COBr smiles:ClC(Cl)(Br)COBr H298:-18.54 kcal/mol
library:CHOClBr_G4 label:OC(O)C(Cl)(Cl)Br smiles:OC(O)C(Cl)(Cl)Br H298:-102.98 kcal/mol
library:CHOClBr_G4 label:COCC(Cl)(Br)Br smiles:COCC(Cl)(Br)Br H298:-40.96 kcal/mol
library:CHOClBr_G4 label:OC(O)C(Cl)(Br)Br smiles:OC(O)C(Cl)(Br)Br H298:-91.35 kcal/mol
library:CHOClBr_G4 label:OCC(Cl)(Br)Br smiles:OCC(Cl)(Br)Br H298:-46.89 kcal/mol
""",
)

entry(
    index = 115,
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
        Cpdata = ([0.298108,0.432618,0.341545,0.365618,0.427909,0.349086,0.201933],'cal/(mol*K)','+|-',[0.170439,0.195885,0.200243,0.197305,0.17109,0.147564,0.120261]),
        H298 = (2.90335,'kcal/mol','+|-',0.607602),
        S298 = (-0.832571,'cal/(mol*K)','+|-',0.414117),
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
library:CHOFBr_G4 label:FC(F)(F)COBr smiles:FC(F)(F)COBr H298:-171.56 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)COCBr smiles:FC(F)(F)COCBr H298:-203.33 kcal/mol
library:CHOFBr_G4 label:CC(OBr)C(F)(F)F smiles:CC(OBr)C(F)(F)F H298:-181.77 kcal/mol
library:CHOFBr_G4 label:OC(OBr)C(F)(F)F smiles:OC(OBr)C(F)(F)F H298:-216.39 kcal/mol
library:CHOFBr_G4 label:OC(CBr)C(F)(F)F smiles:OC(CBr)C(F)(F)F H298:-213.88 kcal/mol
library:CHOFBr_G4 label:FC(F)(F)COOBr smiles:FC(F)(F)COOBr H298:-155.74 kcal/mol
""",
)

entry(
    index = 116,
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
        Cpdata = ([-0.216391,-0.0684263,0.0158986,0.110809,0.248751,0.277267,0.388703],'cal/(mol*K)','+|-',[0.189039,0.217262,0.222095,0.218837,0.189761,0.163667,0.133385]),
        H298 = (1.09963,'kcal/mol','+|-',0.673909),
        S298 = (-0.532953,'cal/(mol*K)','+|-',0.45931),
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
library:CHOClBr_G4 label:ClC(Cl)(Cl)COBr smiles:ClC(Cl)(Cl)COBr H298:-29.78 kcal/mol
""",
)

entry(
    index = 117,
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
        Cpdata = ([-0.112183,-0.111612,-0.130547,-0.107409,0.00609918,0.0755697,0.431962],'cal/(mol*K)','+|-',[0.280196,0.322029,0.329192,0.324363,0.281266,0.24259,0.197705]),
        H298 = (1.4366,'kcal/mol','+|-',0.998877),
        S298 = (-1.22448,'cal/(mol*K)','+|-',0.680795),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrCOCC(Br)(Br)Br smiles:BrCOCC(Br)(Br)Br H298:-26.62 kcal/mol
library:CHOBr_G4 label:OCC(Br)(Br)Br smiles:OCC(Br)(Br)Br H298:-35.17 kcal/mol
library:CHOBr_G4 label:OC(O)C(Br)(Br)Br smiles:OC(O)C(Br)(Br)Br H298:-79.38 kcal/mol
library:CHOBr_G4 label:COCC(Br)(Br)Br smiles:COCC(Br)(Br)Br H298:-29.28 kcal/mol
library:CHOBr_G4 label:OOCC(Br)(Br)Br smiles:OOCC(Br)(Br)Br H298:-13.85 kcal/mol
library:CHOBr_G4 label:BrOCC(Br)(Br)Br smiles:BrOCC(Br)(Br)Br H298:4.79 kcal/mol
library:CHOBr_G4 label:CC(O)C(Br)(Br)Br smiles:CC(O)C(Br)(Br)Br H298:-44.30 kcal/mol
library:CHOBr_G4 label:CC(OBr)C(Br)(Br)Br smiles:CC(OBr)C(Br)(Br)Br H298:-4.45 kcal/mol
library:CHOBr_G4 label:OC(CBr)C(Br)(Br)Br smiles:OC(CBr)C(Br)(Br)Br H298:-37.28 kcal/mol
library:CHOBr_G4 label:BrOOCC(Br)(Br)Br smiles:BrOOCC(Br)(Br)Br H298:21.07 kcal/mol
library:CHOFBr_G4 label:OC(CF)C(Br)(Br)Br smiles:OC(CF)C(Br)(Br)Br H298:-84.72 kcal/mol
""",
)

entry(
    index = 118,
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
        Cpdata = ([0.42524,0.0449695,-0.0076727,0.164389,0.288088,0.420841,0.797181],'cal/(mol*K)','+|-',[0.214491,0.246514,0.251998,0.248301,0.21531,0.185703,0.151344]),
        H298 = (7.07575,'kcal/mol','+|-',0.764643),
        S298 = (0.378738,'cal/(mol*K)','+|-',0.52115),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:CDC(O)C(F)(F)Cl smiles:C=C(O)C(F)(F)Cl H298:-139.22 kcal/mol
library:CHOFCl_G4 label:CDC(O)C(F)(Cl)Cl smiles:C=C(O)C(F)(Cl)Cl H298:-92.18 kcal/mol
library:CHOFClBr_G4 label:CDC(OBr)C(F)(Cl)Cl smiles:C=C(OBr)C(F)(Cl)Cl H298:-52.05 kcal/mol
library:CHOFClBr_G4 label:CDC(O)C(F)(Cl)Br smiles:C=C(O)C(F)(Cl)Br H298:-79.77 kcal/mol
library:CHOFClBr_G4 label:CDC(OBr)C(F)(Cl)Br smiles:C=C(OBr)C(F)(Cl)Br H298:-39.63 kcal/mol
library:CHOFClBr_G4 label:CDC(OBr)C(F)(F)Cl smiles:C=C(OBr)C(F)(F)Cl H298:-98.95 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)C(F)(F)Br smiles:C=C(OBr)C(F)(F)Br H298:-85.59 kcal/mol
library:CHOFBr_G4 label:CDC(O)C(F)(Br)Br smiles:C=C(O)C(F)(Br)Br H298:-67.47 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(Br)Br smiles:OC(=CF)C(F)(Br)Br H298:-109.22 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(F)Br smiles:OC(=CF)C(F)(F)Br H298:-167.85 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)C(F)(Br)Br smiles:C=C(OBr)C(F)(Br)Br H298:-27.33 kcal/mol
library:CHOFBr_G4 label:CDC(O)C(F)(F)Br smiles:C=C(O)C(F)(F)Br H298:-126.05 kcal/mol
library:CHOClBr_G4 label:CDC(O)C(Cl)(Cl)Br smiles:C=C(O)C(Cl)(Cl)Br H298:-36.04 kcal/mol
library:CHOClBr_G4 label:CDC(O)C(Cl)(Br)Br smiles:C=C(O)C(Cl)(Br)Br H298:-24.24 kcal/mol
library:CHOClBr_G4 label:CDC(OBr)C(Cl)(Br)Br smiles:C=C(OBr)C(Cl)(Br)Br H298:15.97 kcal/mol
library:CHOClBr_G4 label:CDC(OBr)C(Cl)(Cl)Br smiles:C=C(OBr)C(Cl)(Cl)Br H298:4.49 kcal/mol
""",
)

entry(
    index = 119,
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
        Cpdata = ([0.434852,0.304563,0.258223,0.298993,0.188632,0.134846,0.239834],'cal/(mol*K)','+|-',[0.340055,0.390823,0.399517,0.393656,0.341353,0.294414,0.239941]),
        H298 = (5.41042,'kcal/mol','+|-',1.21227),
        S298 = (0.422543,'cal/(mol*K)','+|-',0.826232),
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
library:CHOF_G4 label:OC(DC(F)F)C(F)(F)F smiles:OC(=C(F)F)C(F)(F)F H298:-273.17 kcal/mol
library:CHOFBr_G4 label:CDC(OBr)C(F)(F)F smiles:C=C(OBr)C(F)(F)F H298:-149.20 kcal/mol
""",
)

entry(
    index = 120,
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
        Cpdata = ([0.281472,0.226703,0.308853,0.405078,0.369993,0.35266,0.465835],'cal/(mol*K)','+|-',[0.342954,0.394156,0.402924,0.397013,0.344263,0.296924,0.241987]),
        H298 = (2.92725,'kcal/mol','+|-',1.2226),
        S298 = (-1.01438,'cal/(mol*K)','+|-',0.833277),
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
library:CHOClBr_G4 label:CDC(OBr)C(Cl)(Cl)Cl smiles:C=C(OBr)C(Cl)(Cl)Cl H298:-7.09 kcal/mol
""",
)

entry(
    index = 121,
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
        Cpdata = ([0.269679,-0.339568,-0.437638,-0.37155,-0.316557,-0.150457,0.25956],'cal/(mol*K)','+|-',[0.610177,0.701274,0.716874,0.706357,0.612506,0.528281,0.430538]),
        H298 = (6.86856,'kcal/mol','+|-',2.17523),
        S298 = (0.944778,'cal/(mol*K)','+|-',1.48255),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:CDC(O)C(Br)(Br)Br smiles:C=C(O)C(Br)(Br)Br H298:-12.38 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(Br)(Br)Br smiles:OC(=CF)C(Br)(Br)Br H298:-54.37 kcal/mol
""",
)

entry(
    index = 122,
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
        Cpdata = ([-0.241633,-0.997631,-1.22081,-1.04804,-0.705698,-0.387207,-0.230067],'cal/(mol*K)','+|-',[0.141318,0.162416,0.166029,0.163593,0.141857,0.122351,0.0997132]),
        H298 = (5.4645,'kcal/mol','+|-',0.503787),
        S298 = (1.47032,'cal/(mol*K)','+|-',0.343361),
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
library:CHOFClBr_G4 label:OC(OBr)DC(F)Cl smiles:OC(OBr)=C(F)Cl H298:-77.93 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCOOBr smiles:FC(Cl)=COOBr H298:-19.13 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCOBr smiles:FC(Cl)=COBr H298:-34.90 kcal/mol
library:CHOFClBr_G4 label:OC(CBr)DC(F)Cl smiles:OC(CBr)=C(F)Cl H298:-79.58 kcal/mol
library:CHOFClBr_G4 label:FC(Cl)DCOCBr smiles:FC(Cl)=COCBr H298:-65.82 kcal/mol
library:CHOFClBr_G4 label:CC(OBr)DC(F)Cl smiles:CC(OBr)=C(F)Cl H298:-46.46 kcal/mol
library:CHOFBr_G4 label:CC(OBr)DC(F)Br smiles:CC(OBr)=C(F)Br H298:-34.09 kcal/mol
library:CHOFBr_G4 label:OC(O)DC(F)Br smiles:OC(O)=C(F)Br H298:-106.37 kcal/mol
library:CHOFBr_G4 label:OCDC(F)Br smiles:OC=C(F)Br H298:-64.13 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOC(Br)Br smiles:FC(Br)=COC(Br)Br H298:-46.68 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOBr smiles:FC(Br)=COBr H298:-22.37 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(OBr)OBr smiles:FC(Br)=C(OBr)OBr H298:-26.38 kcal/mol
library:CHOFBr_G4 label:COCDC(F)Br smiles:COC=C(F)Br H298:-56.49 kcal/mol
library:CHOFBr_G4 label:OC(CBr)DC(F)Br smiles:OC(CBr)=C(F)Br H298:-67.25 kcal/mol
library:CHOFBr_G4 label:CC(O)DC(F)Br smiles:CC(O)=C(F)Br H298:-75.43 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOCBr smiles:FC(Br)=COCBr H298:-53.34 kcal/mol
library:CHOFBr_G4 label:FC(Br)DC(CBr)OBr smiles:FC(Br)=C(CBr)OBr H298:-26.35 kcal/mol
library:CHOFBr_G4 label:OOCDC(F)Br smiles:OOC=C(F)Br H298:-40.89 kcal/mol
library:CHOFBr_G4 label:OC(DC(F)Br)C(Br)Br smiles:OC(=C(F)Br)C(Br)Br H298:-58.20 kcal/mol
library:CHOFBr_G4 label:FC(Br)DCOOBr smiles:FC(Br)=COOBr H298:-6.50 kcal/mol
library:CHOFBr_G4 label:OC(OBr)DC(F)Br smiles:OC(OBr)=C(F)Br H298:-65.74 kcal/mol
library:CHOClBr_G4 label:CC(O)DC(Cl)Br smiles:CC(O)=C(Cl)Br H298:-39.46 kcal/mol
library:CHOClBr_G4 label:OC(CBr)DC(Cl)Br smiles:OC(CBr)=C(Cl)Br H298:-31.46 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DCOOBr smiles:ClC(Br)=COOBr H298:30.97 kcal/mol
library:CHOClBr_G4 label:OCDC(Cl)Br smiles:OC=C(Cl)Br H298:-28.23 kcal/mol
library:CHOClBr_G4 label:OOCDC(Cl)Br smiles:OOC=C(Cl)Br H298:-3.68 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DCOBr smiles:ClC(Br)=COBr H298:14.84 kcal/mol
library:CHOClBr_G4 label:OC(OBr)DC(Cl)Br smiles:OC(OBr)=C(Cl)Br H298:-30.53 kcal/mol
library:CHOClBr_G4 label:COCDC(Cl)Br smiles:COC=C(Cl)Br H298:-20.72 kcal/mol
library:CHOClBr_G4 label:CC(OBr)DC(Cl)Br smiles:CC(OBr)=C(Cl)Br H298:3.48 kcal/mol
library:CHOClBr_G4 label:OC(O)DC(Cl)Br smiles:OC(O)=C(Cl)Br H298:-72.78 kcal/mol
library:CHOClBr_G4 label:ClC(Br)DCOCBr smiles:ClC(Br)=COCBr H298:-16.56 kcal/mol
""",
)

entry(
    index = 123,
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
        Cpdata = ([-0.243726,-0.892465,-1.00432,-0.809524,-0.465755,-0.153704,-0.00762763],'cal/(mol*K)','+|-',[0.157451,0.180958,0.184984,0.18227,0.158053,0.136319,0.111097]),
        H298 = (8.49439,'kcal/mol','+|-',0.561301),
        S298 = (1.84388,'cal/(mol*K)','+|-',0.38256),
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
library:CHOF_G4 label:OCDC(F)F smiles:OC=C(F)F H298:-116.21 kcal/mol
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
library:CHOF_G4 label:OC(DC(F)F)C(F)(F)F smiles:OC(=C(F)F)C(F)(F)F H298:-273.17 kcal/mol
library:CHOFCl_G4 label:CC(OCl)DC(F)F smiles:CC(OCl)=C(F)F H298:-89.38 kcal/mol
library:CHOFCl_G4 label:FC(F)DCOCCl smiles:FC(F)=COCCl H298:-118.57 kcal/mol
library:CHOFCl_G4 label:FC(F)DCOCl smiles:FC(F)=COCl H298:-78.55 kcal/mol
library:CHOFCl_G4 label:OC(OCl)DC(F)F smiles:OC(OCl)=C(F)F H298:-118.73 kcal/mol
library:CHOFCl_G4 label:FC(F)DCOOCl smiles:FC(F)=COOCl H298:-64.42 kcal/mol
library:CHOFCl_G4 label:OC(CCl)DC(F)F smiles:OC(CCl)=C(F)F H298:-130.01 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(CBr)OBr smiles:FC(F)=C(CBr)OBr H298:-79.09 kcal/mol
library:CHOFBr_G4 label:OC(OBr)DC(F)F smiles:OC(OBr)=C(F)F H298:-117.53 kcal/mol
library:CHOFBr_G4 label:OC(DC(F)F)C(F)Br smiles:OC(=C(F)F)C(F)Br H298:-161.65 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOC(Br)Br smiles:FC(F)=COC(Br)Br H298:-100.05 kcal/mol
library:CHOFBr_G4 label:OC(CBr)DC(F)F smiles:OC(CBr)=C(F)F H298:-119.27 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOOBr smiles:FC(F)=COOBr H298:-60.95 kcal/mol
library:CHOFBr_G4 label:FOC(OBr)DC(F)F smiles:FOC(OBr)=C(F)F H298:-87.17 kcal/mol
library:CHOFBr_G4 label:FC(F)DC(OBr)OBr smiles:FC(F)=C(OBr)OBr H298:-78.61 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOBr smiles:FC(F)=COBr H298:-75.77 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOC(F)Br smiles:FC(F)=COC(F)Br H298:-156.77 kcal/mol
library:CHOFBr_G4 label:CC(OBr)DC(F)F smiles:CC(OBr)=C(F)F H298:-86.79 kcal/mol
library:CHOFBr_G4 label:FC(F)DCOCBr smiles:FC(F)=COCBr H298:-106.65 kcal/mol
library:CHOFBr_G4 label:OC(DC(F)F)C(Br)Br smiles:OC(=C(F)F)C(Br)Br H298:-110.66 kcal/mol
library:CHOFBr_G4 label:FCC(OBr)DC(F)F smiles:FCC(OBr)=C(F)F H298:-127.29 kcal/mol
""",
)

entry(
    index = 124,
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
        Cpdata = ([-0.105823,-0.766456,-0.977777,-0.85146,-0.597257,-0.327485,-0.276673],'cal/(mol*K)','+|-',[0.19363,0.222538,0.227488,0.224151,0.194369,0.167641,0.136624]),
        H298 = (5.42706,'kcal/mol','+|-',0.690273),
        S298 = (1.79238,'cal/(mol*K)','+|-',0.470463),
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
library:CHOClBr_G4 label:ClC(Cl)DCOCBr smiles:ClC(Cl)=COCBr H298:-28.10 kcal/mol
library:CHOClBr_G4 label:OC(OBr)DC(Cl)Cl smiles:OC(OBr)=C(Cl)Cl H298:-41.83 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCOOBr smiles:ClC(Cl)=COOBr H298:19.59 kcal/mol
library:CHOClBr_G4 label:ClC(Cl)DCOBr smiles:ClC(Cl)=COBr H298:3.21 kcal/mol
library:CHOClBr_G4 label:OC(CBr)DC(Cl)Cl smiles:OC(CBr)=C(Cl)Cl H298:-43.06 kcal/mol
""",
)

entry(
    index = 125,
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
        Cpdata = ([-0.239894,-0.712398,-0.893193,-0.690186,-0.406386,-0.16506,-0.163833],'cal/(mol*K)','+|-',[0.252213,0.289867,0.296315,0.291968,0.253176,0.218362,0.17796]),
        H298 = (4.18013,'kcal/mol','+|-',0.899118),
        S298 = (0.317992,'cal/(mol*K)','+|-',0.612803),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:BrOC(OBr)DC(Br)Br smiles:BrOC(OBr)=C(Br)Br H298:21.09 kcal/mol
library:CHOBr_G4 label:OC(OBr)DC(Br)Br smiles:OC(OBr)=C(Br)Br H298:-19.08 kcal/mol
library:CHOBr_G4 label:OCDC(Br)Br smiles:OC=C(Br)Br H298:-16.76 kcal/mol
library:CHOBr_G4 label:OOCDC(Br)Br smiles:OOC=C(Br)Br H298:7.93 kcal/mol
library:CHOBr_G4 label:OC(CBr)DC(Br)Br smiles:OC(CBr)=C(Br)Br H298:-20.06 kcal/mol
library:CHOBr_G4 label:CC(O)DC(Br)Br smiles:CC(O)=C(Br)Br H298:-27.93 kcal/mol
library:CHOBr_G4 label:BrOOCDC(Br)Br smiles:BrOOC=C(Br)Br H298:42.87 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)Br smiles:BrOC=C(Br)Br H298:26.46 kcal/mol
library:CHOBr_G4 label:BrCOCDC(Br)Br smiles:BrCOC=C(Br)Br H298:-4.91 kcal/mol
library:CHOBr_G4 label:OC(O)DC(Br)Br smiles:OC(O)=C(Br)Br H298:-61.66 kcal/mol
library:CHOBr_G4 label:CC(OBr)DC(Br)Br smiles:CC(OBr)=C(Br)Br H298:15.26 kcal/mol
library:CHOBr_G4 label:COCDC(Br)Br smiles:COC=C(Br)Br H298:-9.23 kcal/mol
library:CHOBr_G4 label:BrC(Br)DCOC(Br)Br smiles:BrC(Br)=COC(Br)Br H298:1.72 kcal/mol
library:CHOBr_G4 label:BrCC(OBr)DC(Br)Br smiles:BrCC(OBr)=C(Br)Br H298:22.63 kcal/mol
""",
)

entry(
    index = 126,
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
    index = 127,
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
        Cpdata = ([-0.380226,-0.90248,-0.976221,-0.797113,-0.449641,-0.181964,-0.152742],'cal/(mol*K)','+|-',[0.106406,0.122292,0.125012,0.123178,0.106812,0.0921247,0.0750796]),
        H298 = (6.39782,'kcal/mol','+|-',0.379329),
        S298 = (1.32798,'cal/(mol*K)','+|-',0.258535),
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
library:CHOF_G4 label:OCDC(F)C(F)(F)F smiles:OC=C(F)C(F)(F)F H298:-232.26 kcal/mol
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
library:CHOFClBr_G4 label:OC(DCF)C(Cl)Br smiles:OC(=CF)C(Cl)Br H298:-76.22 kcal/mol
library:CHOFClBr_G4 label:FCDC(CCl)OBr smiles:FC=C(CCl)OBr H298:-43.48 kcal/mol
library:CHOFClBr_G4 label:FCDCOC(Cl)Br smiles:FC=COC(Cl)Br H298:-66.36 kcal/mol
library:CHOFClBr_G4 label:FCDC(OCl)OBr smiles:FC=C(OCl)OBr H298:-35.84 kcal/mol
library:CHOFBr_G4 label:FCDCOC(Br)(Br)Br smiles:FC=COC(Br)(Br)Br H298:-42.55 kcal/mol
library:CHOFBr_G4 label:OC(DCF)OBr smiles:OC(=CF)OBr H298:-71.81 kcal/mol
library:CHOFBr_G4 label:FOCDC(F)OBr smiles:FOC=C(F)OBr H298:-42.02 kcal/mol
library:CHOFBr_G4 label:FCDCOBr smiles:FC=COBr H298:-29.13 kcal/mol
library:CHOFBr_G4 label:FCDCOC(F)(Br)Br smiles:FC=COC(F)(Br)Br H298:-101.11 kcal/mol
library:CHOFBr_G4 label:FCC(F)DCOBr smiles:FCC(F)=COBr H298:-80.65 kcal/mol
library:CHOFBr_G4 label:FCDCOOBr smiles:FC=COOBr H298:-14.15 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)C(F)F smiles:FC=C(OBr)C(F)F H298:-131.43 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(Br)Br smiles:OC(=CF)C(F)(Br)Br H298:-109.22 kcal/mol
library:CHOFBr_G4 label:CC(DCF)OBr smiles:CC(=CF)OBr H298:-40.89 kcal/mol
library:CHOFBr_G4 label:CC(F)DCOBr smiles:CC(F)=COBr H298:-41.53 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(Br)Br smiles:OC(=CF)C(Br)Br H298:-66.27 kcal/mol
library:CHOFBr_G4 label:FOC(F)DCOBr smiles:FOC(F)=COBr H298:-43.48 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)C(F)Br smiles:FC=C(OBr)C(F)Br H298:-73.84 kcal/mol
library:CHOFBr_G4 label:FCDCOC(F)(F)Br smiles:FC=COC(F)(F)Br H298:-163.52 kcal/mol
library:CHOFBr_G4 label:OCDC(F)OBr smiles:OC=C(F)OBr H298:-77.24 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)(F)Br smiles:OC(=CF)C(F)(F)Br H298:-167.85 kcal/mol
library:CHOFBr_G4 label:FCDC(CF)OBr smiles:FC=C(CF)OBr H298:-80.28 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)C(Br)Br smiles:FC=C(OBr)C(Br)Br H298:-23.07 kcal/mol
library:CHOFBr_G4 label:FCDCOC(Br)Br smiles:FC=COC(Br)Br H298:-54.26 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(F)Br smiles:OC(=CF)C(F)Br H298:-115.56 kcal/mol
library:CHOFBr_G4 label:FCDC(OBr)OBr smiles:FC=C(OBr)OBr H298:-34.05 kcal/mol
library:CHOFBr_G4 label:FCDCOCBr smiles:FC=COCBr H298:-60.70 kcal/mol
library:CHOFBr_G4 label:OC(DCF)C(Br)(Br)Br smiles:OC(=CF)C(Br)(Br)Br H298:-54.37 kcal/mol
library:CHOFBr_G4 label:FCDCOC(F)Br smiles:FC=COC(F)Br H298:-110.92 kcal/mol
library:CHOFBr_G4 label:FC(DCOBr)C(F)F smiles:FC(=COBr)C(F)F H298:-131.07 kcal/mol
library:CHOFBr_G4 label:FCDC(CBr)OBr smiles:FC=C(CBr)OBr H298:-32.96 kcal/mol
library:CHOFBr_G4 label:OC(DCF)CBr smiles:OC(=CF)CBr H298:-75.44 kcal/mol
library:CHOFBr_G4 label:FCDC(OF)OBr smiles:FC=C(OF)OBr H298:-42.15 kcal/mol
""",
)

entry(
    index = 128,
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
        Cpdata = ([-0.514656,-1.01793,-1.0856,-0.88761,-0.466709,-0.160292,-0.152415],'cal/(mol*K)','+|-',[0.123048,0.141419,0.144565,0.142444,0.123518,0.106533,0.0868221]),
        H298 = (4.85599,'kcal/mol','+|-',0.438656),
        S298 = (1.34987,'cal/(mol*K)','+|-',0.298971),
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
library:CHOFClBr_G4 label:FCC(Cl)DCOBr smiles:FCC(Cl)=COBr H298:-44.04 kcal/mol
library:CHOFClBr_G4 label:FOC(Cl)DCOBr smiles:FOC(Cl)=COBr H298:-3.27 kcal/mol
library:CHOFClBr_G4 label:FOCDC(Cl)OBr smiles:FOC=C(Cl)OBr H298:-0.59 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)C(Br)Br smiles:OC(=CCl)C(Br)Br H298:-31.24 kcal/mol
library:CHOClBr_G4 label:ClCDC(OBr)OBr smiles:ClC=C(OBr)OBr H298:1.27 kcal/mol
library:CHOClBr_G4 label:ClCDCOC(Br)Br smiles:ClC=COC(Br)Br H298:-18.63 kcal/mol
library:CHOClBr_G4 label:ClOC(Cl)DCOBr smiles:ClOC(Cl)=COBr H298:5.25 kcal/mol
library:CHOClBr_G4 label:ClCDC(CCl)OBr smiles:ClC=C(CCl)OBr H298:-6.95 kcal/mol
library:CHOClBr_G4 label:CC(Cl)DCOBr smiles:CC(Cl)=COBr H298:-3.64 kcal/mol
library:CHOClBr_G4 label:ClOCDC(Cl)OBr smiles:ClOC=C(Cl)OBr H298:4.72 kcal/mol
library:CHOClBr_G4 label:ClCDCOCBr smiles:ClC=COCBr H298:-24.85 kcal/mol
library:CHOClBr_G4 label:ClCDC(CBr)OBr smiles:ClC=C(CBr)OBr H298:3.35 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)C(Cl)Br smiles:OC(=CCl)C(Cl)Br H298:-40.31 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)OBr smiles:OC(=CCl)OBr H298:-40.18 kcal/mol
library:CHOClBr_G4 label:ClCDCOBr smiles:ClC=COBr H298:7.00 kcal/mol
library:CHOClBr_G4 label:ClCDCOC(Cl)Br smiles:ClC=COC(Cl)Br H298:-30.31 kcal/mol
library:CHOClBr_G4 label:ClCDC(OCl)OBr smiles:ClC=C(OCl)OBr H298:-0.52 kcal/mol
library:CHOClBr_G4 label:ClCC(Cl)DCOBr smiles:ClCC(Cl)=COBr H298:-6.73 kcal/mol
library:CHOClBr_G4 label:OCDC(Cl)OBr smiles:OC=C(Cl)OBr H298:-36.72 kcal/mol
library:CHOClBr_G4 label:OC(DCCl)CBr smiles:OC(=CCl)CBr H298:-40.36 kcal/mol
library:CHOClBr_G4 label:ClCDCOOBr smiles:ClC=COOBr H298:23.09 kcal/mol
library:CHOClBr_G4 label:CC(DCCl)OBr smiles:CC(=CCl)OBr H298:-5.20 kcal/mol
""",
)

entry(
    index = 129,
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
        Cpdata = ([-0.734756,-1.3408,-1.43206,-1.19224,-0.627405,-0.225675,-0.182377],'cal/(mol*K)','+|-',[0.138363,0.159021,0.162558,0.160173,0.138892,0.119793,0.0976285]),
        H298 = (5.01034,'kcal/mol','+|-',0.493254),
        S298 = (1.41174,'cal/(mol*K)','+|-',0.336182),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:OCDC(Br)CBr smiles:OC=C(Br)CBr H298:-28.39 kcal/mol
library:CHOBr_G4 label:BrCDCOOBr smiles:BrC=COOBr H298:34.99 kcal/mol
library:CHOBr_G4 label:OC(DCBr)OBr smiles:OC(=CBr)OBr H298:-28.73 kcal/mol
library:CHOBr_G4 label:BrCDC(OBr)C(Br)Br smiles:BrC=C(OBr)C(Br)Br H298:24.67 kcal/mol
library:CHOBr_G4 label:CC(O)DCBr smiles:CC(O)=CBr H298:-36.94 kcal/mol
library:CHOBr_G4 label:OC(O)DCBr smiles:OC(O)=CBr H298:-70.39 kcal/mol
library:CHOBr_G4 label:OOCDCBr smiles:OOC=CBr H298:-0.62 kcal/mol
library:CHOBr_G4 label:OC(DCBr)C(Br)Br smiles:OC(=CBr)C(Br)Br H298:-19.83 kcal/mol
library:CHOBr_G4 label:OCDCBr smiles:OC=CBr H298:-25.75 kcal/mol
library:CHOBr_G4 label:CC(DCBr)OBr smiles:CC(=CBr)OBr H298:6.81 kcal/mol
library:CHOBr_G4 label:BrCDC(CBr)OBr smiles:BrC=C(CBr)OBr H298:14.68 kcal/mol
library:CHOBr_G4 label:OCDC(Br)C(Br)Br smiles:OC=C(Br)C(Br)Br H298:-20.23 kcal/mol
library:CHOBr_G4 label:BrCDCOC(Br)(Br)Br smiles:BrC=COC(Br)(Br)Br H298:4.75 kcal/mol
library:CHOBr_G4 label:OCDC(O)Br smiles:OC=C(O)Br H298:-62.21 kcal/mol
library:CHOBr_G4 label:CC(Br)DCOBr smiles:CC(Br)=COBr H298:8.19 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)OBr smiles:BrOC=C(Br)OBr H298:19.50 kcal/mol
library:CHOBr_G4 label:COCDCBr smiles:COC=CBr H298:-17.42 kcal/mol
library:CHOBr_G4 label:OC(DCBr)CBr smiles:OC(=CBr)CBr H298:-28.89 kcal/mol
library:CHOBr_G4 label:BrCDC(OBr)OBr smiles:BrC=C(OBr)OBr H298:12.71 kcal/mol
library:CHOBr_G4 label:BrCDCOCBr smiles:BrC=COCBr H298:-13.37 kcal/mol
library:CHOBr_G4 label:BrOCDC(Br)C(Br)Br smiles:BrOC=C(Br)C(Br)Br H298:23.66 kcal/mol
library:CHOBr_G4 label:BrCDCOBr smiles:BrC=COBr H298:18.44 kcal/mol
library:CHOBr_G4 label:OCDC(Br)OBr smiles:OC=C(Br)OBr H298:-24.84 kcal/mol
library:CHOBr_G4 label:BrCC(Br)DCOBr smiles:BrCC(Br)=COBr H298:15.22 kcal/mol
library:CHOBr_G4 label:CC(Br)DCO smiles:CC(Br)=CO H298:-34.91 kcal/mol
library:CHOBr_G4 label:BrCDCOC(Br)Br smiles:BrC=COC(Br)Br H298:-6.69 kcal/mol
library:CHOFClBr_G4 label:OCDC(Br)C(F)Cl smiles:OC=C(Br)C(F)Cl H298:-80.45 kcal/mol
library:CHOFBr_G4 label:FOC(Br)DCOBr smiles:FOC(Br)=COBr H298:8.68 kcal/mol
library:CHOFBr_G4 label:FC(Br)C(Br)DCOBr smiles:FC(Br)C(Br)=COBr H298:-27.33 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)Br smiles:OC=C(Br)C(F)Br H298:-71.60 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)Br smiles:OC=C(Br)C(F)(F)Br H298:-122.08 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(F)F smiles:OC=C(Br)C(F)(F)F H298:-186.35 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)F smiles:OC=C(Br)C(F)F H298:-129.37 kcal/mol
library:CHOFBr_G4 label:FC(F)C(Br)DCOBr smiles:FC(F)C(Br)=COBr H298:-84.85 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)CF smiles:OC=C(Br)CF H298:-77.41 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)OF smiles:OC=C(Br)OF H298:-38.61 kcal/mol
library:CHOFBr_G4 label:FOCDC(Br)OBr smiles:FOC=C(Br)OBr H298:11.69 kcal/mol
library:CHOFBr_G4 label:FCC(Br)DCOBr smiles:FCC(Br)=COBr H298:-32.76 kcal/mol
library:CHOFBr_G4 label:OCDC(Br)C(F)(Br)Br smiles:OC=C(Br)C(F)(Br)Br H298:-62.88 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)OCl smiles:OC=C(Br)OCl H298:-26.27 kcal/mol
library:CHOClBr_G4 label:ClCC(Br)DCOBr smiles:ClCC(Br)=COBr H298:4.74 kcal/mol
library:CHOClBr_G4 label:ClOCDC(Br)OBr smiles:ClOC=C(Br)OBr H298:16.77 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Cl smiles:OC=C(Br)C(Cl)Cl H298:-42.92 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)C(Cl)Br smiles:OC=C(Br)C(Cl)Br H298:-31.50 kcal/mol
library:CHOClBr_G4 label:ClOC(Br)DCOBr smiles:ClOC(Br)=COBr H298:17.28 kcal/mol
library:CHOClBr_G4 label:OCDC(Br)CCl smiles:OC=C(Br)CCl H298:-39.24 kcal/mol
""",
)

entry(
    index = 130,
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
    index = 131,
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
    index = 132,
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
        Cpdata = ([-0.0613148,0.014087,0.137551,0.213407,0.248535,0.276004,0.330381],'cal/(mol*K)','+|-',[0.0890667,0.102364,0.104641,0.103106,0.0894067,0.0771125,0.062845]),
        H298 = (1.96277,'kcal/mol','+|-',0.317515),
        S298 = (-0.694615,'cal/(mol*K)','+|-',0.216406),
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
    index = 133,
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
        Cpdata = ([0.429706,0.325512,0.262386,0.223978,0.159683,0.128005,0.103564],'cal/(mol*K)','+|-',[0.0912715,0.104898,0.107231,0.105658,0.09162,0.0790214,0.0644007]),
        H298 = (5.36116,'kcal/mol','+|-',0.325375),
        S298 = (-0.831813,'cal/(mol*K)','+|-',0.221763),
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
    index = 134,
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
    index = 135,
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
    index = 136,
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
        Cpdata = ([-0.124569,-0.0414804,0.137115,0.18829,0.127109,0.148913,0.223763],'cal/(mol*K)','+|-',[0.146534,0.168411,0.172157,0.169631,0.147093,0.126867,0.103394]),
        H298 = (2.86687,'kcal/mol','+|-',0.522381),
        S298 = (-0.0461551,'cal/(mol*K)','+|-',0.356034),
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
    index = 137,
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
        Cpdata = ([0.211057,-0.0849622,-0.261928,-0.331928,-0.359998,-0.293467,-0.0908236],'cal/(mol*K)','+|-',[0.14824,0.170371,0.174161,0.171606,0.148806,0.128344,0.104597]),
        H298 = (6.29532,'kcal/mol','+|-',0.528462),
        S298 = (-0.542737,'cal/(mol*K)','+|-',0.360179),
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
    index = 138,
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
    index = 139,
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
    index = 140,
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
        Cpdata = ([-0.432377,-0.382519,-0.280526,-0.140557,0.0752877,0.282769,0.68794],'cal/(mol*K)','+|-',[0.158644,0.182329,0.186385,0.18365,0.15925,0.137351,0.111938]),
        H298 = (2.57853,'kcal/mol','+|-',0.565552),
        S298 = (0.805811,'cal/(mol*K)','+|-',0.385458),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFClBr_G4 label:CDC(F)OC(F)(Cl)Br smiles:C=C(F)OC(F)(Cl)Br H298:-119.53 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DCC(F)(Cl)Cl smiles:CC(Br)=CC(F)(Cl)Cl H298:-52.66 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DCC(F)(F)Cl smiles:CC(Br)=CC(F)(F)Cl H298:-100.71 kcal/mol
library:CHOFClBr_G4 label:CDC(F)OC(Cl)(Br)Br smiles:C=C(F)OC(Cl)(Br)Br H298:-59.46 kcal/mol
library:CHOFClBr_G4 label:CDC(F)CC(F)(Cl)Br smiles:C=C(F)CC(F)(Cl)Br H298:-93.03 kcal/mol
library:CHOFClBr_G4 label:CDC(F)CC(Cl)(Cl)Br smiles:C=C(F)CC(Cl)(Cl)Br H298:-49.45 kcal/mol
library:CHOFClBr_G4 label:CDC(F)CC(Cl)(Br)Br smiles:C=C(F)CC(Cl)(Br)Br H298:-37.48 kcal/mol
library:CHOFClBr_G4 label:CDC(F)OC(Cl)(Cl)Br smiles:C=C(F)OC(Cl)(Cl)Br H298:-71.82 kcal/mol
library:CHOFClBr_G4 label:CC(Br)DCC(F)(Cl)Br smiles:CC(Br)=CC(F)(Cl)Br H298:-40.73 kcal/mol
library:CHOFBr_G4 label:CDC(F)OC(F)(F)Br smiles:C=C(F)OC(F)(F)Br H298:-168.71 kcal/mol
library:CHOFBr_G4 label:CC(F)DCC(F)(F)Br smiles:CC(F)=CC(F)(F)Br H298:-139.80 kcal/mol
library:CHOFBr_G4 label:CDC(F)OC(Br)(Br)Br smiles:C=C(F)OC(Br)(Br)Br H298:-46.67 kcal/mol
library:CHOFBr_G4 label:CDC(F)CC(F)(F)Br smiles:C=C(F)CC(F)(F)Br H298:-140.17 kcal/mol
library:CHOFBr_G4 label:CDC(F)CC(Br)(Br)Br smiles:C=C(F)CC(Br)(Br)Br H298:-25.23 kcal/mol
library:CHOFBr_G4 label:CDC(F)OC(F)(Br)Br smiles:C=C(F)OC(F)(Br)Br H298:-105.27 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCC(F)(Br)Br smiles:OC(Br)=CC(F)(Br)Br H298:-61.23 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCC(F)(F)F smiles:CC(Br)=CC(F)(F)F H298:-152.14 kcal/mol
library:CHOFBr_G4 label:CC(F)DCC(F)(Br)Br smiles:CC(F)=CC(F)(Br)Br H298:-80.28 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCC(F)(F)Br smiles:CC(Br)=CC(F)(F)Br H298:-87.31 kcal/mol
library:CHOFBr_G4 label:CC(Br)DCC(F)(Br)Br smiles:CC(Br)=CC(F)(Br)Br H298:-28.12 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCC(F)(F)F smiles:OC(Br)=CC(F)(F)F H298:-184.84 kcal/mol
library:CHOFBr_G4 label:CC(F)DCC(Br)(Br)Br smiles:CC(F)=CC(Br)(Br)Br H298:-25.02 kcal/mol
library:CHOFBr_G4 label:CDC(F)CC(F)(Br)Br smiles:C=C(F)CC(F)(Br)Br H298:-80.84 kcal/mol
library:CHOFBr_G4 label:OC(Br)DCC(F)(F)Br smiles:OC(Br)=CC(F)(F)Br H298:-120.45 kcal/mol
library:CHOClBr_G4 label:CC(Br)DCC(Cl)(Cl)Br smiles:CC(Br)=CC(Cl)(Cl)Br H298:3.44 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)OC(Cl)(Cl)Br smiles:C=C(Cl)OC(Cl)(Cl)Br H298:-29.82 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)CC(Cl)(Br)Br smiles:C=C(Cl)CC(Cl)(Br)Br H298:2.45 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)CC(Cl)(Cl)Br smiles:C=C(Cl)CC(Cl)(Cl)Br H298:-9.56 kcal/mol
library:CHOClBr_G4 label:CC(Br)DCC(Cl)(Br)Br smiles:CC(Br)=CC(Cl)(Br)Br H298:15.17 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)OC(Cl)(Br)Br smiles:C=C(Cl)OC(Cl)(Br)Br H298:-17.53 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)CC(Br)(Br)Br smiles:C=C(Cl)CC(Br)(Br)Br H298:14.51 kcal/mol
library:CHOClBr_G4 label:CDC(Cl)OC(Br)(Br)Br smiles:C=C(Cl)OC(Br)(Br)Br H298:-5.06 kcal/mol
library:CHOClBr_G4 label:CC(Br)DCC(Cl)(Cl)Cl smiles:CC(Br)=CC(Cl)(Cl)Cl H298:-8.37 kcal/mol
""",
)

entry(
    index = 141,
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
        Cpdata = ([-0.602376,-0.448942,-0.211492,-0.0750071,-0.0052189,0.0217937,0.151667],'cal/(mol*K)','+|-',[0.188299,0.216411,0.221225,0.21798,0.189018,0.163026,0.132863]),
        H298 = (1.33119,'kcal/mol','+|-',0.67127),
        S298 = (0.806138,'cal/(mol*K)','+|-',0.457511),
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
    index = 142,
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
        Cpdata = ([0.0789662,-0.00826367,-0.031511,-0.047384,-0.02161,0.0392074,0.200236],'cal/(mol*K)','+|-',[0.190223,0.218623,0.223486,0.220207,0.190949,0.164692,0.13422]),
        H298 = (2.70883,'kcal/mol','+|-',0.678129),
        S298 = (0.0802435,'cal/(mol*K)','+|-',0.462186),
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
    index = 143,
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
    index = 144,
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
        Cpdata = ([-0.11987,0.154996,0.179495,0.136543,-0.0362736,-0.102538,-0.023355],'cal/(mol*K)','+|-',[0.429544,0.493673,0.504655,0.497251,0.431184,0.371892,0.303084]),
        H298 = (2.51094,'kcal/mol','+|-',1.53129),
        S298 = (1.71964,'cal/(mol*K)','+|-',1.04367),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFBr_G4 label:FC(Br)DCC(Br)(Br)Br smiles:FC(Br)=CC(Br)(Br)Br H298:-5.00 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)(F)Br smiles:FC(F)=CC(F)(F)Br H298:-175.99 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(F)(Br)Br smiles:FC(F)=CC(F)(Br)Br H298:-116.09 kcal/mol
library:CHOFBr_G4 label:FC(F)DCC(Br)(Br)Br smiles:FC(F)=CC(Br)(Br)Br H298:-60.65 kcal/mol
""",
)

entry(
    index = 145,
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
        Cpdata = ([-0.774085,-0.642314,-0.412453,-0.260714,-0.21398,-0.217231,-0.0639702],'cal/(mol*K)','+|-',[0.280127,0.321949,0.32911,0.324282,0.281196,0.242529,0.197656]),
        H298 = (1.96179,'kcal/mol','+|-',0.998628),
        S298 = (-0.52294,'cal/(mol*K)','+|-',0.680625),
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
library:CHOF_G4 label:OC(DC(F)F)C(F)(F)F smiles:OC(=C(F)F)C(F)(F)F H298:-273.17 kcal/mol
""",
)

entry(
    index = 146,
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
        Cpdata = ([0.245379,0.333856,0.340188,0.362121,0.345499,0.354879,0.459335],'cal/(mol*K)','+|-',[0.284009,0.326411,0.333672,0.328776,0.285093,0.245891,0.200395]),
        H298 = (7.38508,'kcal/mol','+|-',1.01247),
        S298 = (-1.56652,'cal/(mol*K)','+|-',0.690058),
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
    index = 147,
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
    index = 148,
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
        Cpdata = ([1.28858,1.60873,1.59757,1.44213,0.990463,0.627,0.204682],'cal/(mol*K)','+|-',[0.192635,0.221395,0.22632,0.222999,0.19337,0.16678,0.135922]),
        H298 = (2.34139,'kcal/mol','+|-',0.686728),
        S298 = (-0.572184,'cal/(mol*K)','+|-',0.468046),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOFCl_G4 label:ODCCC(F)(F)Cl smiles:O=CCC(F)(F)Cl H298:-148.27 kcal/mol
library:CHOFCl_G4 label:ODCCC(F)(Cl)Cl smiles:O=CCC(F)(Cl)Cl H298:-100.50 kcal/mol
library:CHOFCl_G4 label:ODCOC(F)(F)Cl smiles:O=COC(F)(F)Cl H298:-190.31 kcal/mol
library:CHOFCl_G4 label:ODCOC(F)(Cl)Cl smiles:O=COC(F)(Cl)Cl H298:-140.04 kcal/mol
library:CHOFClBr_G4 label:ODCOC(F)(Cl)Br smiles:O=COC(F)(Cl)Br H298:-126.94 kcal/mol
library:CHOFClBr_G4 label:ODCCC(F)(Cl)Br smiles:O=CCC(F)(Cl)Br H298:-87.72 kcal/mol
library:CHOFBr_G4 label:ODC(Br)OC(F)(Br)Br smiles:O=C(Br)OC(F)(Br)Br H298:-109.95 kcal/mol
library:CHOFBr_G4 label:ODCOC(F)(Br)Br smiles:O=COC(F)(Br)Br H298:-113.92 kcal/mol
library:CHOFBr_G4 label:ODCOC(F)(F)Br smiles:O=COC(F)(F)Br H298:-176.64 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CC(F)(F)Br smiles:O=C(Br)CC(F)(F)Br H298:-137.60 kcal/mol
library:CHOFBr_G4 label:ODCCC(F)(Br)Br smiles:O=CCC(F)(Br)Br H298:-74.87 kcal/mol
library:CHOFBr_G4 label:ODC(Br)CC(F)(Br)Br smiles:O=C(Br)CC(F)(Br)Br H298:-78.14 kcal/mol
library:CHOFBr_G4 label:ODCCC(F)(F)Br smiles:O=CCC(F)(F)Br H298:-134.89 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)Br smiles:O=CC(Br)C(F)(F)Br H298:-125.99 kcal/mol
library:CHOFBr_G4 label:ODC(Br)OC(F)(F)Br smiles:O=C(Br)OC(F)(F)Br H298:-172.26 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(Br)Br smiles:O=CC(Br)C(F)(Br)Br H298:-66.91 kcal/mol
library:CHOClBr_G4 label:ODCCC(Cl)(Cl)Br smiles:O=CCC(Cl)(Cl)Br H298:-44.33 kcal/mol
library:CHOClBr_G4 label:ODCOC(Cl)(Br)Br smiles:O=COC(Cl)(Br)Br H298:-67.75 kcal/mol
library:CHOClBr_G4 label:ODCOC(Cl)(Cl)Br smiles:O=COC(Cl)(Cl)Br H298:-80.16 kcal/mol
library:CHOClBr_G4 label:ODCCC(Cl)(Br)Br smiles:O=CCC(Cl)(Br)Br H298:-32.34 kcal/mol
""",
)

entry(
    index = 149,
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
        Cpdata = ([0.692902,0.748947,0.732154,0.654874,0.448645,0.294028,0.0858244],'cal/(mol*K)','+|-',[0.263639,0.302999,0.30974,0.305195,0.264646,0.228255,0.186022]),
        H298 = (1.68467,'kcal/mol','+|-',0.939851),
        S298 = (-0.143794,'cal/(mol*K)','+|-',0.640565),
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
library:CHOFBr_G4 label:ODC(Br)CC(F)(F)F smiles:O=C(Br)CC(F)(F)F H298:-202.26 kcal/mol
library:CHOFBr_G4 label:ODCC(Br)C(F)(F)F smiles:O=CC(Br)C(F)(F)F H298:-189.44 kcal/mol
""",
)

entry(
    index = 150,
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
        Cpdata = ([0.815477,0.963953,0.996605,0.942743,0.729321,0.528441,0.248787],'cal/(mol*K)','+|-',[0.309083,0.355228,0.36313,0.357803,0.310263,0.267599,0.218087]),
        H298 = (1.52396,'kcal/mol','+|-',1.10186),
        S298 = (-0.764091,'cal/(mol*K)','+|-',0.750981),
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
    index = 151,
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
        Cpdata = ([1.5681,1.85074,1.80473,1.61193,1.06923,0.615793,-0.054756],'cal/(mol*K)','+|-',[0.594257,0.682977,0.69817,0.687927,0.596526,0.514498,0.419305]),
        H298 = (3.76862,'kcal/mol','+|-',2.11848),
        S298 = (-1.1101,'cal/(mol*K)','+|-',1.44387),
    ),
    shortDesc = """Fitted using sklearn Ridge regression with alpha = 1e-06""",
    longDesc = 
"""
Dervied using the following species:
library:CHOBr_G4 label:ODCOC(Br)(Br)Br smiles:O=COC(Br)(Br)Br H298:-55.40 kcal/mol
library:CHOBr_G4 label:ODCCC(Br)(Br)Br smiles:O=CCC(Br)(Br)Br H298:-20.45 kcal/mol
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

