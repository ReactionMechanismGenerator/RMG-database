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
    index = 0,
    label = "int14_gauche",
    group = 
"""
1 *1 [Cs,Os,Cd,Ss] u0 {2,S}
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
    index = 1,
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
    index = 2,
    label = "CsCs-P",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
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
    index = 2,
    label = "CsCs-S",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   Cs u0 {1,S}
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
    label = "CsCs-SS",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
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
    index = 7,
    label = "CsCs-ST",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
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
    index = 8,
    label = "CsCs-SQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
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
    index = 2,
    label = "CsCs-T",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
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
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
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
    index = 9,
    label = "CsCs-T(TTP)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
13   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
14   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
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
    index = 9,
    label = "CsCs-T(TTS)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   Cs u0 {4,S}
13   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
14   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
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
    index = 9,
    label = "CsCs-T(TTT)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   Cs u0 {4,S}
13   Cs u0 {4,S}
14   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
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
    index = 9,
    label = "CsCs-T(TTQ)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   Cs u0 {4,S}
13   Cs u0 {4,S}
14   Cs u0 {4,S}
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
    index = 10,
    label = "CsCs-TQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
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
    index = 2,
    label = "CsCs-Q",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
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
    index = 11,
    label = "CsCs-QQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {1,S}
5   Cs                         u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
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
    index = 12,
    label = "OsCs",
    group = 
"""
1 *1 Os u0 {2,S}
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
    index = 13,
    label = "OsCs-P",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
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
    index = 14,
    label = "OsCs-S",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S}
3    Cs                         u0 {1,S}
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
    index = 14,
    label = "OsCs-SP",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
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
    index = 15,
    label = "OsCs-SS",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {2,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
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
    label = "OsCs-ST",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {2,S}
5   Cs                         u0 {2,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
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
    index = 17,
    label = "OsCs-SQ",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {2,S}
5   Cs                         u0 {2,S}
6   Cs                         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 18,
    label = "CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2   Cd u0 {1,D}
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
    index = 18,
    label = "CdCs-P",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
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
    index = 19,
    label = "CdCs-S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
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
    index = 19,
    label = "CdCs-SP",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
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
    label = "CdCs-SS",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   Cs                         u0 {4,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
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
    label = "CdCs-ST",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   Cs                         u0 {4,S}
6   Cs                         u0 {4,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
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
    index = 22,
    label = "CdCs-SQ",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   Cs                         u0 {4,S}
6   Cs                         u0 {4,S}
7   Cs                         u0 {4,S}
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
    index = 23,
    label = "SsCs",
    group = 
"""
1 *1 Ss u0 {2,S}
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
    index = 24,
    label = "Ss(Cs(CsHH)H)",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Cs u0 {1,S} {4,S} {5,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
5   H  u0 {2,S}
6   Cs u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.33,0.62,0.67,0.59,0.38,0.21,-0.01],'cal/(mol*K)'),
        H298 = (-0.97,'kcal/mol'),
        S298 = (-1.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""From old version - gauche.py""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "int15",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S}
2    [Cs,Os,Ss] u0 {1,S} {3,S}
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
    index = 0,
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
    index = 0,
    label = "CsCsCs-TQ",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S} {9,S}
2    Cs u0 {1,S} {3,S}
3 *2 Cs u0 {2,S} {6,S} {7,S} {8,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {3,S}
7    Cs u0 {3,S}
8    Cs u0 {3,S}
9    [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
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
    index = 0,
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
    index = 0,
    label = "CsOsCs",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S}
2    Os u0 {1,S} {3,S}
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
    index = 0,
    label = "CsOsCs-TQ",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S} {9,S}
2    Os u0 {1,S} {3,S}
3 *2 Cs u0 {2,S} {6,S} {7,S} {8,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {3,S}
7    Cs u0 {3,S}
8    Cs u0 {3,S}
9    [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
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
    index = 0,
    label = "CsOsCs-QQ",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Os u0 {1,S} {3,S}
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
    index = 0,
    label = "CsSsCs",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S}
2    Ss u0 {1,S} {3,S}
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
    index = 0,
    label = "CsSsCs-TQ",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S} {9,S}
2    Ss u0 {1,S} {3,S}
3 *2 Cs u0 {2,S} {6,S} {7,S} {8,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    Cs u0 {3,S}
7    Cs u0 {3,S}
8    Cs u0 {3,S}
9    [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
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
    index = 0,
    label = "CsSsCs-QQ",
    group = 
"""
1 *1 Cs u0 {2,S} {4,S} {5,S} {6,S}
2    Ss u0 {1,S} {3,S}
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

tree(
"""
L1: R
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
        L3: SsCs
            L4: Ss(Cs(CsHH)H)
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
