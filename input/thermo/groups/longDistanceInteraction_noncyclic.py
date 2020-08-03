#!/usr/bin/env python
# encoding: utf-8

name = "Long distance interaction correction for non-cyclic molecule"
shortDesc = u""
longDesc = u"""
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
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
    shortDesc = u"""Lumped PP/PS/PT/PQ, because they all counted as 0 as long as the first carbon is primary carbon""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
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
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 10,
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
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 11,
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
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 12,
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
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI) / 2 + (1 GI) / 3 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 13,
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
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 14,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
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
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 17,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
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
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 35,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
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
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 38,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
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
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 41,
    label = "intCl",
    group = 
"""
1 *1 [Cs,Cd,CO] u0 {2,[S,D]} {3,S}
2 *2 [Cs,Cd,CO] u0 {1,[S,D]}
3    Cl1s       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by 2 to avoid overcounting
""",
)

entry(
    index = 43,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by 2 to avoid overcounting
""",
)

entry(
    index = 45,
    label = "Cs(Cl)3-C(Cl)",
    group = 
"""
1 *1 Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd] u0 {1,S} {6,S}
3    Cl1s    u0 {1,S}
4    Cl1s    u0 {1,S}
5    Cl1s    u0 {1,S}
6    Cl1s    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "Cs(Cl)2-C(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd]     u0 {1,S} {6,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Cl1s        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C(Cl)-C(Cl)",
    group = 
"""
1 *1 [Cs,Cd] u0 {2,S} {3,S}
2 *2 [Cs,Cd] u0 {1,S} {4,S}
3    Cl1s    u0 {1,S}
4    Cl1s    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by two to avoid overcounting
""",
)

entry(
    index = 53,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by two to avoid overcounting
""",
)

entry(
    index = 54,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by two to avoid overcounting
""",
)

entry(
    index = 55,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by two to avoid overcounting
""",
)

entry(
    index = 56,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""
Divided by two to avoid doublecounting
""",
)

entry(
    index = 58,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Cs(Cl)-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S}
2 *2 CO   u0 {1,S} {4,D}
3    Cl1s u0 {1,S}
4    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.82865,1.44161,0.833956,0.302595,-0.0498998,-0.359348,0.397952],'J/(mol*K)'),
        H298 = (9.67318,'kJ/mol'),
        S298 = (0.809872,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cs(Cl)2-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S}
2 *2 CO   u0 {1,S} {5,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.90501,3.54115,2.92691,2.14794,1.21308,0.57418,0.86693],'J/(mol*K)'),
        H298 = (11.039,'kJ/mol'),
        S298 = (-5.77323,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
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
    shortDesc = u"""Derived from Chlorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "intF",
    group = 
"""
1 *1 [Cs,Cd,CO] u0 {2,[S,D]} {3,S}
2 *2 [Cs,Cd,CO] u0 {1,[S,D]}
3    F1s        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Cs(F)3-C(F)",
    group = 
"""
1 *1 Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd] u0 {1,S} {6,S}
3    F1s     u0 {1,S}
4    F1s     u0 {1,S}
5    F1s     u0 {1,S}
6    F1s     u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Cs(F)2-C(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd]     u0 {1,S} {6,S}
3    F1s         u0 {1,S}
4    F1s         u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    F1s         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C(F)-C(F)",
    group = 
"""
1 *1 [Cs,Cd] u0 {2,S} {3,S}
2 *2 [Cs,Cd] u0 {1,S} {4,S}
3    F1s     u0 {1,S}
4    F1s     u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "Cs(F)-CO",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S}
2 *2 CO  u0 {1,S} {4,D}
3    F1s u0 {1,S}
4    O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.02754,1.83455,1.79212,1.52065,1.3104,0.985188,1.55713],'J/(mol*K)'),
        H298 = (14.3551,'kJ/mol'),
        S298 = (-1.1458,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "Cs(F)2-CO",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S}
2 *2 CO  u0 {1,S} {5,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.79873,1.52268,0.889428,0.197554,-0.370686,-0.638744,0.376926],'J/(mol*K)'),
        H298 = (25.5004,'kJ/mol'),
        S298 = (-2.9804,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
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
    shortDesc = u"""Derived from Fluorine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "intBr",
    group = 
"""
1 *1 [Cs,Cd,CO] u0 {2,[S,D]} {3,S}
2 *2 [Cs,Cd,CO] u0 {1,[S,D]}
3    Br1s       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Cs(Br)3-C(Br)",
    group = 
"""
1 *1 Cs      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd] u0 {1,S} {6,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {1,S}
5    Br1s    u0 {1,S}
6    Br1s    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "Cs(Br)3-Cds(Br)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cd        u0 {1,S} {4,S} {6,D}
3    Br1s      u0 {1,S}
4    Br1s      u0 {2,S}
5    Br1s      u0 {1,S}
6    [C,N,O,S] u0 {2,D}
7    Br1s      u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Cs(Br)2-C(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd]     u0 {1,S} {6,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {1,S}
5    [C,H,N,O,S] u0 {1,S}
6    Br1s        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C(Br)-C(Br)",
    group = 
"""
1 *1 [Cs,Cd] u0 {2,S} {3,S}
2 *2 [Cs,Cd] u0 {1,S} {4,S}
3    Br1s    u0 {1,S}
4    Br1s    u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

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
        Cpdata = ([-0.0558217,0.122408,0.161036,0.879168,0.513532,0.712393,3.78075],'J/(mol*K)'),
        H298 = (11.0867,'kJ/mol'),
        S298 = (-4.66996,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "Cs(Br)-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S}
2 *2 CO   u0 {1,S} {4,D}
3    Br1s u0 {1,S}
4    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.23266,1.36458,0.943371,0.376736,-0.139231,-0.439512,0.637492],'J/(mol*K)'),
        H298 = (8.57038,'kJ/mol'),
        S298 = (0.231177,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "Cs(Br)2-CO",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S} {4,S}
2 *2 CO   u0 {1,S} {5,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.8799,1.58349,1.18728,0.671541,0.141805,-0.173482,1.00635],'J/(mol*K)'),
        H298 = (7.89011,'kJ/mol'),
        S298 = (-3.44795,'J/(mol*K)'),
    ),
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
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
    shortDesc = u"""Derived from Bromine species in thermo libraries""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R
    L2: intCl
        L3: Cs(Cl)3-Cs(Cl)3
        L3: Cs(Cl)3-Cs(Cl)2
        L3: Cs(Cl)3-C(Cl)
            L4: Cs(Cl)3-Cs(Cl)
            L4: Cs(Cl)3-Cds(Cl)
        L3: Cs(Cl)2-Cs(Cl)2
        L3: Cs(Cl)2-C(Cl)
            L4: Cs(Cl)2-Cs(Cl)
            L4: Cs(Cl)2-Cds(Cl)
        L3: C(Cl)-C(Cl)
            L4: Cs(Cl)-Cs(Cl)
            L4: Cs(Cl)-Cds(Cl)
            L4: Cds(Cl)-Cds(Cl)
        L3: Cds(Cl)=Cds(Cl)
        L3: Cds(Cl)2=Cds(Cl)
        L3: Cds(Cl)2=Cds(Cl)2
        L3: Cd(Cl)-CO
        L3: Cs(Cl)-CO
            L4: Cs(Cl)2-CO
                L5: Cs(Cl)3-CO
    L2: intF
        L3: Cs(F)3-Cs(F)3
        L3: Cs(F)3-Cs(F)2
        L3: Cs(F)3-C(F)
            L4: Cs(F)3-Cs(F)
            L4: Cs(F)3-Cds(F)
        L3: Cs(F)2-Cs(F)2
        L3: Cs(F)2-C(F)
            L4: Cs(F)2-Cs(F)
            L4: Cs(F)2-Cds(F)
        L3: C(F)-C(F)
            L4: Cs(F)-Cs(F)
            L4: Cs(F)-Cds(F)
            L4: Cds(F)-Cds(F)
        L3: Cds(F)=Cds(F)
        L3: Cds(F)2=Cds(F)
        L3: Cds(F)2=Cds(F)2
        L3: Cd(F)-CO
        L3: Cs(F)-CO
            L4: Cs(F)2-CO
                L5: Cs(F)3-CO
    L2: intBr
        L3: Cs(Br)3-Cs(Br)3
        L3: Cs(Br)3-Cs(Br)2
        L3: Cs(Br)3-C(Br)
            L4: Cs(Br)3-Cs(Br)
            L4: Cs(Br)3-Cds(Br)
        L3: Cs(Br)2-Cs(Br)2
        L3: Cs(Br)2-C(Br)
            L4: Cs(Br)2-Cs(Br)
            L4: Cs(Br)2-Cds(Br)
        L3: C(Br)-C(Br)
            L4: Cs(Br)-Cs(Br)
            L4: Cs(Br)-Cds(Br)
            L4: Cds(Br)-Cds(Br)
        L3: Cds(Br)=Cds(Br)
        L3: Cds(Br)2=Cds(Br)
        L3: Cds(Br)2=Cds(Br)2
        L3: Cd(Br)-CO
        L3: Cs(Br)-CO
            L4: Cs(Br)2-CO
                L5: Cs(Br)3-CO
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
