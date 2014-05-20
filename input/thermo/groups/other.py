#!/usr/bin/env python
# encoding: utf-8

name = "Other Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 0,
    label        = "R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * R U0
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
    index        = 10,
    label        = "ketene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0 {2,D} {3,S} {4,S}
2   C U0 {1,D} {5,D}
3   R U0 {1,S}
4   R U0 {1,S}
5   O U0 {2,D}
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
    index        = 13,
    label        = "ketene_2C-C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   C       U0 {1,D} {5,D}
3   {Cs,Cd} U0 {1,S} {6,S}
4   {Cs,Cd} U0 {1,S} {7,S}
5   O       U0 {2,D}
6   C       U0 {3,S}
7   C       U0 {4,S}
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
    index        = 11,
    label        = "ketene_1C-C_1C-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   C       U0 {1,D} {5,D}
3   {Cs,Cd} U0 {1,S} {6,S}
4   C       U0 {1,S} {7,S} {8,S} {9,S}
5   O       U0 {2,D}
6   C       U0 {3,S}
7   H       U0 {4,S}
8   H       U0 {4,S}
9   H       U0 {4,S}
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
    index        = 14,
    label        = "biketene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C   U0 {2,S} {3,S} {4,S} {5,S}
2    C   U0 {1,S} {6,D}
3  * C   U0 {1,S} {7,D} {10,S}
4    R!H U0 {1,S}
5    R!H U0 {1,S}
6    C   U0 {2,D} {8,D}
7    C   U0 {3,D} {9,D}
8    O   U0 {6,D}
9    O   U0 {7,D}
10   R   U0 {3,S}
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
    index        = 12,
    label        = "ketene_2C-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D} {5,D}
3    C U0 {1,S} {6,S} {7,S} {8,S}
4    C U0 {1,S} {9,S} {10,S} {11,S}
5    O U0 {2,D}
6    H U0 {3,S}
7    H U0 {3,S}
8    H U0 {3,S}
9    H U0 {4,S}
10   H U0 {4,S}
11   H U0 {4,S}
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
    index        = 1,
    label        = "cis",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,Dcis} {3,S} {4,S}
2 * C   U0 {1,Dcis} {5,S} {6,S}
3   R!H U0 {1,S}
4   H   U0 {1,S}
5   R!H U0 {2,S}
6   H   U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cis double bond interaction BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "2-ene_cis",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,Dcis} {3,S} {4,S}
2 * C   U0 {1,Dcis} {5,S} {6,S}
3   C   U0 {1,S} {7,S} {8,S} {9,S}
4   H   U0 {1,S}
5   R!H U0 {2,S}
6   H   U0 {2,S}
7   H   U0 {3,S}
8   H   U0 {3,S}
9   H   U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    label        = "2-butene_cis",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U0 {2,Dcis} {3,S} {4,S}
2  * C U0 {1,Dcis} {5,S} {6,S}
3    C U0 {1,S} {7,S} {8,S} {9,S}
4    H U0 {1,S}
5    C U0 {2,S} {10,S} {11,S} {12,S}
6    H U0 {2,S}
7    H U0 {3,S}
8    H U0 {3,S}
9    H U0 {3,S}
10   H U0 {5,S}
11   H U0 {5,S}
12   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (1.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""The entropy correction for 2-cis-butene is not zero BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    label        = "t-butyl_cis_2-ene",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C   U0 {2,Dcis} {3,S} {4,S}
2  * C   U0 {1,Dcis} {5,S} {6,S}
3    C   U0 {1,S} {7,S} {8,S} {9,S}
4    H   U0 {1,S}
5    C   U0 {2,S} {10,S} {11,S} {12,S}
6    H   U0 {2,S}
7    H   U0 {3,S}
8    H   U0 {3,S}
9    H   U0 {3,S}
10   R!H U0 {5,S}
11   R!H U0 {5,S}
12   R!H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cis double bond interaction involving tertiary butyl group BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    label        = "higher-ene_cis",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C   U0 {2,Dcis} {3,S} {4,S}
2  * C   U0 {1,Dcis} {5,S} {6,S}
3    C   U0 {1,S} {7,S} {8,S} {9,S}
4    H   U0 {1,S}
5    C   U0 {2,S} {10,S} {11,S} {12,S}
6    H   U0 {2,S}
7    R!H U0 {3,S}
8    R   U0 {3,S}
9    R   U0 {3,S}
10   R!H U0 {5,S}
11   R   U0 {5,S}
12   R   U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (-0.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""The entropy correction for 2-cis-butene is not zero BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 7,
    label        = "t-butyl_cis",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C   U0 {2,Dcis} {3,S} {4,S}
2  * C   U0 {1,Dcis} {5,S} {6,S}
3    C   U0 {1,S} {7,S} {8,S} {9,S}
4    H   U0 {1,S}
5    C   U0 {2,S} {10,S} {11,S} {12,S}
6    H   U0 {2,S}
7    R!H U0 {3,S}
8    R!H U0 {3,S}
9    R!H U0 {3,S}
10   R!H U0 {5,S}
11   R   U0 {5,S}
12   R   U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cis double bond interaction involving tertiary butyl group BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    label        = "t-butyl_cis_t-butyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C   U0 {2,Dcis} {3,S} {4,S}
2  * C   U0 {1,Dcis} {5,S} {6,S}
3    C   U0 {1,S} {7,S} {8,S} {9,S}
4    H   U0 {1,S}
5    C   U0 {2,S} {10,S} {11,S} {12,S}
6    H   U0 {2,S}
7    R!H U0 {3,S}
8    R!H U0 {3,S}
9    R!H U0 {3,S}
10   R!H U0 {5,S}
11   R!H U0 {5,S}
12   R!H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cis double bond interaction invloving two tertiary butyl groups BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 8,
    label        = "double_cis",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,Dcis} {3,S} {4,S}
2 * C   U0 {1,Dcis} {5,S} {6,S}
3   R!H U0 {1,S}
4   R!H U0 {1,S}
5   R!H U0 {2,S}
6   R!H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.09,-0.81,-0.61,-0.39,-0.26,0],'cal/(mol*K)'),
        H298 = (3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""2 Cis interactions around a double bond BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 9,
    label        = "ortho",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,B} {3,B} {4,S}
2 * C   U0 {1,B} {5,B} {6,S}
3   C   U0 {1,B}
4   R!H U0 {1,S}
5   C   U0 {2,B}
6   R!H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.12,1.35,1.3,1.17,0.88,0.66,-0.05],'cal/(mol*K)'),
        H298 = (0.57,'kcal/mol'),
        S298 = (-1.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""Ortho correction from BENSON""",
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
    L2: cis
        L3: 2-ene_cis
            L4: 2-butene_cis
            L4: t-butyl_cis_2-ene
        L3: higher-ene_cis
            L4: t-butyl_cis
                L5: t-butyl_cis_t-butyl
    L2: double_cis
    L2: ortho
"""
)

