#!/usr/bin/env python
# encoding: utf-8

name = "Other Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "R",
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
    shortDesc = u"""dummy root""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "ketene",
    group = 
"""
1 * C u0 {2,D} {3,S} {4,S}
2   C u0 {1,D} {5,D}
3   R u0 {1,S}
4   R u0 {1,S}
5   O u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""All the corrections from this family are from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "ketene_2C-C",
    group = 
"""
1 * C       u0 {2,D} {3,S} {4,S}
2   C       u0 {1,D} {5,D}
3   [Cs,Cd] u0 {1,S} {6,S}
4   [Cs,Cd] u0 {1,S} {7,S}
5   O       u0 {2,D}
6   C       u0 {3,S}
7   C       u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN2 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "ketene_1C-C_1C-H",
    group = 
"""
1 * C       u0 {2,D} {3,S} {4,S}
2   C       u0 {1,D} {5,D}
3   [Cs,Cd] u0 {1,S} {6,S}
4   C       u0 {1,S} {7,S} {8,S} {9,S}
5   O       u0 {2,D}
6   C       u0 {3,S}
7   H       u0 {4,S}
8   H       u0 {4,S}
9   H       u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN1 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "biketene",
    group = 
"""
1    C   u0 {2,S} {3,S} {4,S} {5,S}
2    C   u0 {1,S} {6,D}
3  * C   u0 {1,S} {7,D} {10,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
6    C   u0 {2,D} {8,D}
7    C   u0 {3,D} {9,D}
8    O   u0 {6,D}
9    O   u0 {7,D}
10   R   u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN3 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "ketene_2C-H",
    group = 
"""
1  * C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D} {5,D}
3    C u0 {1,S} {6,S} {7,S} {8,S}
4    C u0 {1,S} {9,S} {10,S} {11,S}
5    O u0 {2,D}
6    H u0 {3,S}
7    H u0 {3,S}
8    H u0 {3,S}
9    H u0 {4,S}
10   H u0 {4,S}
11   H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is correction NN0 from Sumathi & Green, J. Phys. Chem. A, 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "ThreeMember-Val7",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   Val7 u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "ThreeMember-F",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "ThreeMember-Cl",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "ThreeMember-Br",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "ThreeMember-F2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   F1s u0 {1,S}
5   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "ThreeMember-Cl2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235117,
    label = "ThreeMember-CdVal7",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S}
5   Val7 u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = 'ThreeMember-CdF',
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S}
5   F u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "ThreeMember-CdCl",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S}
5   Cl u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


entry(
    index = 120,
    label = "ThreeMember-CdBr",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S}
5   Br u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "ThreeMember-CdF2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S} {6,S}
5   F u0 {4,S}
6   F u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "ThreeMember-CdCl2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S} {6,S}
5   Cl u0 {4,S}
6   Cl u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "ThreeMember-CdBr2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,D}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,D} {5,S} {6,S}
5   Br u0 {4,S}
6   Br u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "ThreeMember-CVal7",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   Val7 u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "ThreeMember-CF",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   F u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1111,
    label = "ThreeMember-CCl",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   Cl u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117123,
    label = "ThreeMember-CBr",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   Br u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "ThreeMember-CF2",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S} {6,S}
5   F u0 {4,S}
6   F u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 517,
    label = "ThreeMember-CCl2",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S} {6,S}
5   Cl u0 {4,S}
6   Cl u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 617,
    label = "ThreeMember-CBr2",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S} {6,S}
5   Br u0 {4,S}
6   Br u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 717,
    label = "ThreeMember-CF3",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S} {6,S} {7,S}
5   F u0 {4,S}
6   F u0 {4,S}
7   F u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 817,
    label = "ThreeMember-CCl3",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S} {6,S} {7,S}
5   Cl u0 {4,S}
6   Cl u0 {4,S}
7   Cl u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11700,
    label = "ThreeMember-CBr3",
    group = 
"""
1 * R!H u0 {2,[S,D]} {3,S} {4,S}
2   R!H u0 {1,[S,D]} {3,S}
3   R!H u0 {1,S} {2,S}
4   C u0 {1,S} {5,S} {6,S} {7,S}
5   Br u0 {4,S}
6   Br u0 {4,S}
7   Br u0 {4,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "ThreeMember-Br2",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {1,S} {2,[S,D]}
4   Br1s u0 {1,S}
5   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "FourMember-Val7",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,S} {5,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   Val7 u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "FourMember-F",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,S} {5,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "FourMember-Cl",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,S} {5,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "FourMember-Br",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,S} {5,S}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "FourMember-F2",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   F1s u0 {1,S}
6   F1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "FourMember-Cl2",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   Cl1s u0 {1,S}
6   Cl1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "FourMember-Br2",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,S} {3,[S,D]}
5   Br1s u0 {1,S}
6   Br1s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


tree(
"""
L1: R
    L2: ketene
        L3: ketene_2C-C
        L3: ketene_1C-C_1C-H
        L3: biketene
        L3: ketene_2C-H
    L2: ThreeMember-Val7
        L3: ThreeMember-F
            L4: ThreeMember-F2
        L3: ThreeMember-Cl
            L4: ThreeMember-Cl2
        L3: ThreeMember-Br
            L4: ThreeMember-Br2
    L2: ThreeMember-CdVal7
        L3: ThreeMember-CdF
            L4: ThreeMember-CdF2
        L3: ThreeMember-CdCl
            L4: ThreeMember-CdCl2
        L3: ThreeMember-CdBr
            L4: ThreeMember-CdBr2
    L2: ThreeMember-CVal7
        L3: ThreeMember-CF
            L4: ThreeMember-CF2
                L5: ThreeMember-CF3
        L3: ThreeMember-CCl
            L4: ThreeMember-CCl2
                L5: ThreeMember-CCl3
        L3: ThreeMember-CBr
            L4: ThreeMember-CBr2
                L5: ThreeMember-CBr3
    L2: FourMember-Val7
        L3: FourMember-F
            L4: FourMember-F2
        L3: FourMember-Cl
            L4: FourMember-Cl2
        L3: FourMember-Br
            L4: FourMember-Br2
"""
)

