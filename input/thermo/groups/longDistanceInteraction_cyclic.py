#!/usr/bin/env python
# encoding: utf-8

name = "Long distance interaction correction for cyclic molecule"
shortDesc = ""
longDesc = """
Designed to account for the long distance interaction for cyclic molecule.
Currently we only have the data for aromatic ortho/meta/para corrections.
Watch out:  if the groups on the two labeled atoms are identical, it's value should be halved because it'll be counted twice.
            For example, for the interaction of ortho OH and OH, which is labeled as 'o_OH_OH' in this database,
            it'll be counted in both {'*1': atom1, '*2'atom2} and {'*2': atom1, '*1'atom2}.
            It should be claimed in the 'longDesc' if a entry was halved.

Source: 
For aromatic molecule: [1] Ince et al., AIChE 2015, DOI 10.1002/aic.15008
For aromatic radical: [2] Ince et al., AIChE 2016, DOI 10.1002/aic.15588

Jan-23-2017 PZ
"""
entry(
    index = 0,
    label = "R",
    group = 
"""
1 *1 R ux
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """ROOT""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "aromatic-ortho",
    group = 
"""
1 *1 Cb u0 {2,B}
2 *2 Cb u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatics NNI correction for ortho position.""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "o_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O  u0 {1,S} {4,S}
4    H  u0 {3,S}
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
    index = 3,
    label = "o_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O  u0 {1,S} {4,S}
4    H  u0 {3,S}
5    O  u0 {2,S} {6,S}
6    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.18,0.02,0.24,0.5,0.57,0.44],'cal/(mol*K)'),
        H298 = (-0.36,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "o_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O  u0 {1,S} {4,S}
4    H  u0 {3,S}
5    O  u0 {2,S} {6,S}
6    C  u0 {5,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-0.36,0.05,0.48,1,1.15,0.88],'cal/(mol*K)'),
        H298 = (-0.72,'kcal/mol'),
        S298 = (-1.34,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "o_OH_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O  u0 {1,S} {4,S}
4    H  u0 {3,S}
5    C  u0 {2,S} {6,D} {7,S}
6    C  u0 {5,D} {8,S} {9,S}
7    H  u0 {5,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.6,0.65,0.62,0.6,0.5,0.43,0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "o_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O  u0 {1,S} {4,S}
4    H  u0 {3,S}
5    C  u0 {2,S} {6,S} {7,D}
6    H  u0 {5,S}
7    O  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49,-2.15,-1.77,-1.43,-0.81,-0.33,0.43],'cal/(mol*K)'),
        H298 = (-6.55,'kcal/mol'),
        S298 = (-5.09,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "o_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C  u0 {1,S} {4,S} {5,D}
4    H  u0 {3,S}
5    O  u0 {3,D}
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
    index = 8,
    label = "o_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C  u0 {1,S} {4,S} {8,D}
4    H  u0 {3,S}
5    C  u0 {2,S} {6,S} {7,D}
6    H  u0 {5,S}
7    O  u0 {5,D}
8    O  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,0.2,0.19,0.17,0.05,-0.1,-0.3],'cal/(mol*K)'),
        H298 = (2.52,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "o_CHO_vinyl",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {6,S}
3     C  u0 {1,S} {4,S} {5,D}
4     H  u0 {3,S}
5     O  u0 {3,D}
6     C  u0 {2,S} {7,D} {8,S}
7     C  u0 {6,D} {9,S} {10,S}
8     H  u0 {6,S}
9     H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,0.38,0.5,0.6,0.57,0.43,0.07],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (-0.62,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "o_CHO_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C  u0 {1,S} {4,S} {5,D}
4    H  u0 {3,S}
5    O  u0 {3,D}
6    C  u0 {2,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96,0.72,0.48,0.26,0,-0.14,-0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "o_CHO_C2H5",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {6,S}
3     C  u0 {1,S} {4,S} {5,D}
4     H  u0 {3,S}
5     O  u0 {3,D}
6     C  u0 {2,S} {7,S} {8,S} {9,S}
7     H  u0 {6,S}
8     H  u0 {6,S}
9     C  u0 {6,S} {10,S} {11,S} {12,S}
10    H  u0 {9,S}
11    H  u0 {9,S}
12    H  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96,0.72,0.48,0.26,0,-0.14,-0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "o_CHO_MeO",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {6,S}
3     C  u0 {1,S} {4,S} {5,D}
4     H  u0 {3,S}
5     O  u0 {3,D}
6     O  u0 {2,S} {7,S}
7     C  u0 {6,S} {8,S} {9,S} {10,S}
8     H  u0 {7,S}
9     H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,0.07,0.62,0.93,0.98,0.79,0.31],'cal/(mol*K)'),
        H298 = (1.89,'kcal/mol'),
        S298 = (-0.41,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "o_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C  u0 {1,S} {4,S} {5,D}
4    H  u0 {3,S}
5    C  u0 {3,D} {6,S} {7,S}
6    H  u0 {5,S}
7    H  u0 {5,S}
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
    index = 14,
    label = "o_vinyl_vinyl",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {6,S}
3     C  u0 {1,S} {4,S} {5,D}
4     H  u0 {3,S}
5     C  u0 {3,D} {11,S} {12,S}
6     C  u0 {2,S} {7,D} {8,S}
7     C  u0 {6,D} {9,S} {10,S}
8     H  u0 {6,S}
9     H  u0 {7,S}
10    H  u0 {7,S}
11    H  u0 {5,S}
12    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55,0.38,0.25,0.16,0.02,-0.02,-0.06],'cal/(mol*K)'),
        H298 = (0.97,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "o_vinyl_CH3",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {8,S}
3     C  u0 {1,S} {4,S} {5,D}
4     H  u0 {3,S}
5     C  u0 {3,D} {6,S} {7,S}
6     H  u0 {5,S}
7     H  u0 {5,S}
8     C  u0 {2,S} {9,S} {10,S} {11,S}
9     H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36,1.34,1.17,1,0.69,0.5,0.24],'cal/(mol*K)'),
        H298 = (1.1,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "o_vinyl_C2H5",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {8,S}
3     C  u0 {1,S} {4,S} {5,D}
4     H  u0 {3,S}
5     C  u0 {3,D} {6,S} {7,S}
6     H  u0 {5,S}
7     H  u0 {5,S}
8     C  u0 {2,S} {9,S} {10,S} {11,S}
9     H  u0 {8,S}
10    H  u0 {8,S}
11    C  u0 {8,S} {12,S} {13,S} {14,S}
12    H  u0 {11,S}
13    H  u0 {11,S}
14    H  u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36,1.34,1.17,1,0.69,0.5,0.24],'cal/(mol*K)'),
        H298 = (1.1,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "o_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O  u0 {1,S} {4,S}
4    C  u0 {3,S} {5,S} {6,S} {7,S}
5    H  u0 {4,S}
6    H  u0 {4,S}
7    H  u0 {4,S}
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
    label = "o_MeO_MeO",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {8,S}
3     O  u0 {1,S} {4,S}
4     C  u0 {3,S} {5,S} {6,S} {7,S}
5     H  u0 {4,S}
6     H  u0 {4,S}
7     H  u0 {4,S}
8     O  u0 {2,S} {9,S}
9     C  u0 {8,S} {10,S} {11,S} {12,S}
10    H  u0 {9,S}
11    H  u0 {9,S}
12    H  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,-0.41,-0.56,-0.6,-0.53,-0.44,-0.26],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (0.93,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "o_MeO_vinyl",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {5,S}
3     O  u0 {1,S} {4,S}
4     C  u0 {3,S} {10,S} {11,S} {12,S}
5     C  u0 {2,S} {6,D} {7,S}
6     C  u0 {5,D} {8,S} {9,S}
7     H  u0 {5,S}
8     H  u0 {6,S}
9     H  u0 {6,S}
10    H  u0 {4,S}
11    H  u0 {4,S}
12    H  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.6,0.65,0.62,0.6,0.5,0.43,0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "o_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C  u0 {1,S} {4,S} {5,S} {6,S}
4    H  u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
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
    index = 21,
    label = "o_CH3_CH3",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {7,S}
3     C  u0 {1,S} {4,S} {5,S} {6,S}
4     H  u0 {3,S}
5     H  u0 {3,S}
6     H  u0 {3,S}
7     C  u0 {2,S} {8,S} {9,S} {10,S}
8     H  u0 {7,S}
9     H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39,0.35,0.31,0.3,0.27,0.24,0.18],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "o_CH3_C2H5",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {7,S}
3     C  u0 {1,S} {4,S} {5,S} {6,S}
4     H  u0 {3,S}
5     H  u0 {3,S}
6     H  u0 {3,S}
7     C  u0 {2,S} {8,S} {9,S} {10,S}
8     H  u0 {7,S}
9     H  u0 {7,S}
10    C  u0 {7,S} {11,S} {12,S} {13,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
13    H  u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.79,0.69,0.62,0.6,0.55,0.48,0.36],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (-1.58,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "o_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C  u0 {1,S} {4,S} {5,S} {6,S}
4    H  u0 {3,S}
5    H  u0 {3,S}
6    C  u0 {3,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
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
    label = "o_C2H5_C2H5",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {7,S}
3     C  u0 {1,S} {4,S} {5,S} {6,S}
4     H  u0 {3,S}
5     H  u0 {3,S}
6     C  u0 {3,S} {14,S} {15,S} {16,S}
7     C  u0 {2,S} {8,S} {9,S} {10,S}
8     H  u0 {7,S}
9     H  u0 {7,S}
10    C  u0 {7,S} {11,S} {12,S} {13,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
13    H  u0 {10,S}
14    H  u0 {6,S}
15    H  u0 {6,S}
16    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39,0.35,0.31,0.3,0.27,0.24,0.18],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "o_Oj",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O  u1 {1,S}
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
    index = 26,
    label = "o_Oj_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O  u1 {1,S}
4    O  u0 {2,S} {5,S}
5    H  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06,-1.84,-1.58,-1.27,-0.74,-0.31,0.38],'cal/(mol*K)'),
        H298 = (-8.87,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = """NNI4. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "o_Oj_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O  u1 {1,S}
4    O  u0 {2,S} {5,S}
5    C  u0 {4,S} {6,S} {7,S} {8,S}
6    H  u0 {5,S}
7    H  u0 {5,S}
8    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.6,-0.62,-0.53,-0.33,-0.07,0.05,0.12],'cal/(mol*K)'),
        H298 = (-1.53,'kcal/mol'),
        S298 = (-0.1,'cal/(mol*K)'),
    ),
    shortDesc = """NNI5. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "o_Oj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O  u1 {1,S}
4    C  u0 {2,S} {5,S} {6,D}
5    H  u0 {4,S}
6    O  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.22,-0.02,0.19,0.41,0.69,0.69,0.41],'cal/(mol*K)'),
        H298 = (1.36,'kcal/mol'),
        S298 = (-0.1,'cal/(mol*K)'),
    ),
    shortDesc = """NNI8. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "o_Oj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O  u1 {1,S}
4    C  u0 {2,S} {5,S} {6,D}
5    H  u0 {4,S}
6    C  u0 {4,D} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0.02,0.1,0.24,0.31,0.36],'cal/(mol*K)'),
        H298 = (-1.53,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = """NNI10. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "o_Oj_Cs",
    group = 
"""
1 *1 Cb     u0 {2,B} {3,S}
2 *2 Cb     u0 {1,B} {4,S}
3    O      u1 {1,S}
4    C      u0 {2,S} {5,S} {6,S} {7,S}
5    H      u0 {4,S}
6    H      u0 {4,S}
7    [H,Cs] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14,-0.12,-0.1,-0.05,-0.05,-0.02,-0.05],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (0.26,'cal/(mol*K)'),
    ),
    shortDesc = """NNI12. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "o_OCH2j",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O  u0 {1,S} {4,S}
4    C  u1 {3,S} {5,S} {6,S}
5    H  u0 {4,S}
6    H  u0 {4,S}
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
    label = "o_OCH2j_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    O  u0 {1,S} {4,S}
4    C  u1 {3,S} {5,S} {6,S}
5    H  u0 {4,S}
6    H  u0 {4,S}
7    C  u0 {2,S} {8,S} {9,D}
8    H  u0 {7,S}
9    O  u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.53,1.2,1.43,1.39,1,0.62,0.12],'cal/(mol*K)'),
        H298 = (1.67,'kcal/mol'),
        S298 = (-1.15,'cal/(mol*K)'),
    ),
    shortDesc = """NNI2. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "o_OCH2j_OCH3",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {7,S}
3     O  u0 {1,S} {4,S}
4     C  u1 {3,S} {5,S} {6,S}
5     H  u0 {4,S}
6     H  u0 {4,S}
7     O  u0 {2,S} {8,S}
8     C  u0 {7,S} {9,S} {10,S} {11,S}
9     H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.93,0.22,-0.22,-0.36,-0.33,-0.29,-0.14],'cal/(mol*K)'),
        H298 = (2.75,'kcal/mol'),
        S298 = (0.29,'cal/(mol*K)'),
    ),
    shortDesc = """NNI3. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "o_Cj=O",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C  u1 {1,S} {4,D}
4    O  u0 {3,D}
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
    label = "o_Cj=O_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C  u1 {1,S} {4,D}
4    O  u0 {3,D}
5    O  u0 {2,S} {6,S}
6    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53,-1.08,-0.69,-0.24,0.55,1.12,1.65],'cal/(mol*K)'),
        H298 = (-4.02,'kcal/mol'),
        S298 = (-4.57,'cal/(mol*K)'),
    ),
    shortDesc = """NNI14. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "o_Cj=O_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C  u1 {1,S} {4,D}
4    O  u0 {3,D}
5    O  u0 {2,S} {6,S}
6    C  u0 {5,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.6,0.33,0.1,0,-0.14,-0.19,-0.17],'cal/(mol*K)'),
        H298 = (1.77,'kcal/mol'),
        S298 = (0.57,'cal/(mol*K)'),
    ),
    shortDesc = """NNI16. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "o_Cj=O_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C  u1 {1,S} {4,D}
4    O  u0 {3,D}
5    C  u0 {2,S} {6,D} {9,S}
6    C  u0 {5,D} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.76,0.84,0.76,0.62,0.36,0.14,0.02],'cal/(mol*K)'),
        H298 = (0.96,'kcal/mol'),
        S298 = (-1.39,'cal/(mol*K)'),
    ),
    shortDesc = """NNI19. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "o_C=Cj",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C  u0 {1,S} {4,D} {5,S}
4    C  u1 {3,D} {6,S}
5    H  u0 {3,S}
6    H  u0 {4,S}
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
    label = "o_C=Cj_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C  u0 {1,S} {4,D} {5,S}
4    C  u1 {3,D} {6,S}
5    H  u0 {3,S}
6    H  u0 {4,S}
7    O  u0 {2,S} {8,S}
8    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-0.69,0.14,1.1,2.41,2.87,2.25],'cal/(mol*K)'),
        H298 = (-3.39,'kcal/mol'),
        S298 = (-4.21,'cal/(mol*K)'),
    ),
    shortDesc = """NNI20. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "o_C=Cj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C  u0 {1,S} {4,D} {5,S}
4    C  u1 {3,D} {6,S}
5    H  u0 {3,S}
6    H  u0 {4,S}
7    C  u0 {2,S} {8,S} {9,D}
8    H  u0 {7,S}
9    O  u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.53,0.81,0.86,0.79,0.57,0.43,0.24],'cal/(mol*K)'),
        H298 = (3.49,'kcal/mol'),
        S298 = (-1.29,'cal/(mol*K)'),
    ),
    shortDesc = """NNI21. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "o_C=Cj_C=C",
    group = 
"""
1  *1 Cb u0 {2,B} {3,S}
2  *2 Cb u0 {1,B} {7,S}
3     C  u0 {1,S} {4,D} {5,S}
4     C  u1 {3,D} {6,S}
5     H  u0 {3,S}
6     H  u0 {4,S}
7     C  u0 {2,S} {8,S} {9,D}
8     H  u0 {7,S}
9     C  u0 {7,D} {10,S} {11,S}
10    H  u0 {9,S}
11    H  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.48,0.6,0.53,0.43,0.26,0.17,0.07],'cal/(mol*K)'),
        H298 = (1.82,'kcal/mol'),
        S298 = (-1.31,'cal/(mol*K)'),
    ),
    shortDesc = """NNI22. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "o_C=Cj_Cs",
    group = 
"""
1  *1 Cb     u0 {2,B} {3,S}
2  *2 Cb     u0 {1,B} {7,S}
3     C      u0 {1,S} {4,D} {5,S}
4     C      u1 {3,D} {6,S}
5     H      u0 {3,S}
6     H      u0 {4,S}
7     C      u0 {2,S} {8,S} {9,S} {10,S}
8     H      u0 {7,S}
9     H      u0 {7,S}
10    [H,Cs] u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.69,0.65,0.5,0.36,0.14,0.07,-0.02],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = """NNI23. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "o_Csj",
    group = 
"""
1 *1 Cb     u0 {2,B} {3,S}
2 *2 Cb     u0 {1,B}
3    C      u1 {1,S} {4,S} {5,S}
4    H      u0 {3,S}
5    [H,Cs] u0 {3,S}
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
    index = 44,
    label = "o_Csj_C=C",
    group = 
"""
1  *1 Cb     u0 {2,B} {3,S}
2  *2 Cb     u0 {1,B} {6,S}
3     C      u1 {1,S} {4,S} {5,S}
4     H      u0 {3,S}
5     [H,Cs] u0 {3,S}
6     C      u0 {2,S} {7,S} {8,D}
7     H      u0 {6,S}
8     C      u0 {6,D} {9,S} {10,S}
9     H      u0 {8,S}
10    H      u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.43,0.29,0.14,0.02,-0.12,-0.17,-0.17],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (-0.12,'cal/(mol*K)'),
    ),
    shortDesc = """NNI26. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "o_Csj_CHO",
    group = 
"""
1 *1 Cb     u0 {2,B} {3,S}
2 *2 Cb     u0 {1,B} {6,S}
3    C      u1 {1,S} {4,S} {5,S}
4    H      u0 {3,S}
5    [H,Cs] u0 {3,S}
6    C      u0 {2,S} {7,S} {8,D}
7    H      u0 {6,S}
8    O      u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.43,0.5,0.43,0.29,0.1,-0.05,-0.12],'cal/(mol*K)'),
        H298 = (1.31,'kcal/mol'),
        S298 = (0.45,'cal/(mol*K)'),
    ),
    shortDesc = """NNI28. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "o_Csj_Cs",
    group = 
"""
1 *1 Cb     u0 {2,B} {3,S}
2 *2 Cb     u0 {1,B} {6,S}
3    C      u1 {1,S} {4,S} {5,S}
4    H      u0 {3,S}
5    [H,Cs] u0 {3,S}
6    C      u0 {2,S} {7,S} {8,S} {9,S}
7    H      u0 {6,S}
8    H      u0 {6,S}
9    [H,Cs] u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.81,0.62,0.43,0.29,0.12,0.07,0],'cal/(mol*K)'),
        H298 = (0.65,'kcal/mol'),
        S298 = (-0.86,'cal/(mol*K)'),
    ),
    shortDesc = """NNI29. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "aromatic-meta",
    group = 
"""
1 *1 Cb u0 {2,B}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatics NNI correction for meta position""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "m_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {7,S}
4    C  u0 {1,S} {5,D} {6,S}
5    O  u0 {4,D}
6    H  u0 {4,S}
7    C  u0 {3,S} {8,D} {9,S}
8    O  u0 {7,D}
9    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,0.12,0.06,0.01,-0.05,-0.08,-0.1],'cal/(mol*K)'),
        H298 = (0.57,'kcal/mol'),
        S298 = (0.01,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. Aromatics NNI correction.""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "m_Oj_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {5,S}
4    O  u1 {1,S}
5    O  u0 {3,S} {6,S}
6    C  u0 {5,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22,0.76,0.98,1.03,0.81,0.55,0.22],'cal/(mol*K)'),
        H298 = (-1.65,'kcal/mol'),
        S298 = (-1,'cal/(mol*K)'),
    ),
    shortDesc = """NNI6. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "m_Oj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {5,S}
4    O  u1 {1,S}
5    C  u0 {3,S} {6,D} {7,S}
6    O  u0 {5,D}
7    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.38,-0.38,-0.38,-0.38,0.29,0.22,0.12],'cal/(mol*K)'),
        H298 = (1.12,'kcal/mol'),
        S298 = (0.86,'cal/(mol*K)'),
    ),
    shortDesc = """NNI9. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "m_Cj=O_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {6,S}
4    C  u1 {1,S} {5,D}
5    O  u0 {4,D}
6    C  u0 {3,S} {7,D} {8,S}
7    O  u0 {6,D}
8    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.07,0.17,0.17,0.12,0,-0.07,0.02],'cal/(mol*K)'),
        H298 = (1.1,'kcal/mol'),
        S298 = (0.81,'cal/(mol*K)'),
    ),
    shortDesc = """NNI17. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "aromatic-para",
    group = 
"""
1 *1 Cb u0 {2,B}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatics NNI correction for para position.""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "p_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O  u0 {1,S} {6,S}
6    H  u0 {5,S}
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
    index = 54,
    label = "p_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O  u0 {1,S} {6,S}
6    H  u0 {5,S}
7    O  u0 {4,S} {8,S}
8    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,0.05,-0.1,-0.2,-0.27,-0.27,-0.2],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "p_OH_MeO",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {7,S}
5     O  u0 {1,S} {6,S}
6     H  u0 {5,S}
7     O  u0 {4,S} {8,S}
8     C  u0 {7,S} {9,S} {10,S} {11,S}
9     H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41,0.1,-0.19,-0.41,-0.55,-0.55,-0.41],'cal/(mol*K)'),
        H298 = (1.74,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "p_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O  u0 {1,S} {6,S}
6    H  u0 {5,S}
7    C  u0 {4,S} {8,D} {9,S}
8    O  u0 {7,D}
9    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38,-0.24,-0.07,0.05,0.22,0.29,0.36],'cal/(mol*K)'),
        H298 = (-1.1,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "p_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
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
    index = 58,
    label = "p_MeO_MeO",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {7,S}
5     O  u0 {1,S} {6,S}
6     C  u0 {5,S} {12,S} {13,S} {14,S}
7     O  u0 {4,S} {8,S}
8     C  u0 {7,S} {9,S} {10,S} {11,S}
9     H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
12    H  u0 {6,S}
13    H  u0 {6,S}
14    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,0.05,-0.1,-0.2,-0.27,-0.27,-0.2],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "p_MeO_CHO",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {7,S}
5     O  u0 {1,S} {6,S}
6     C  u0 {5,S} {10,S} {11,S} {12,S}
7     C  u0 {4,S} {8,D} {9,S}
8     O  u0 {7,D}
9     H  u0 {7,S}
10    H  u0 {6,S}
11    H  u0 {6,S}
12    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38,-0.24,-0.07,0.05,0.22,0.29,0.36],'cal/(mol*K)'),
        H298 = (-1.1,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = """This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "p_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C  u0 {1,S} {6,S} {7,D}
6    H  u0 {5,S}
7    O  u0 {5,D}
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
    index = 61,
    label = "p_CHO_CHO",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {7,S}
5     C  u0 {1,S} {6,S} {10,D}
6     H  u0 {5,S}
7     C  u0 {4,S} {8,D} {9,S}
8     O  u0 {7,D}
9     H  u0 {7,S}
10    O  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22,0.17,0.12,0.08,0.01,-0.04,-0.11],'cal/(mol*K)'),
        H298 = (1.18,'kcal/mol'),
        S298 = (-0.1,'cal/(mol*K)'),
    ),
    shortDesc = """Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "p_Oj",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O  u1 {1,S}
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
    index = 63,
    label = "p_Oj_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    O  u0 {4,S} {7,S}
7    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67,-0.6,-0.45,-0.29,-0.02,0.17,0.38],'cal/(mol*K)'),
        H298 = (-3.78,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = """NNI7. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "p_Oj_OCH3",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {6,S}
5     O  u1 {1,S}
6     O  u0 {4,S} {7,S}
7     C  u0 {6,S} {8,S} {9,S} {10,S}
8     H  u0 {7,S}
9     H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67,-0.6,-0.45,-0.29,-0.02,0.17,0.38],'cal/(mol*K)'),
        H298 = (-3.78,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = """NNI7. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "p_Oj_C=C",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {6,S}
5     O  u1 {1,S}
6     C  u0 {4,S} {7,D} {8,S}
7     C  u0 {6,D} {9,S} {10,S}
8     H  u0 {6,S}
9     H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.07,0.05,0.05,0.12,0.22,0.29,0.26],'cal/(mol*K)'),
        H298 = (-3.08,'kcal/mol'),
        S298 = (-0.72,'cal/(mol*K)'),
    ),
    shortDesc = """NNI11. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "p_Oj_Cs",
    group = 
"""
1 *1 Cb     u0 {2,B} {5,S}
2    Cb     u0 {1,B} {3,B}
3    Cb     u0 {2,B} {4,B}
4 *2 Cb     u0 {3,B} {6,S}
5    O      u1 {1,S}
6    C      u0 {4,S} {7,S} {8,S} {9,S}
7    H      u0 {6,S}
8    H      u0 {6,S}
9    [H,Cs] u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.17,-0.12,-0.1,-0.1,-0.07,-0.05,-0.05],'cal/(mol*K)'),
        H298 = (-1.39,'kcal/mol'),
        S298 = (0.07,'cal/(mol*K)'),
    ),
    shortDesc = """NNI13. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "p_OCH2j",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O  u0 {1,S} {6,S}
6    C  u1 {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
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
    index = 68,
    label = "p_OCH2j_OH",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {9,S}
5     O  u0 {1,S} {6,S}
6     C  u1 {5,S} {7,S} {8,S}
7     H  u0 {6,S}
8     H  u0 {6,S}
9     O  u0 {4,S} {10,S}
10    H  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.1,-0.19,-0.43,-0.57,-0.65,-0.6,-0.33],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = """NNI1. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "p_OCH2j_OCH3",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {9,S}
5     O  u0 {1,S} {6,S}
6     C  u1 {5,S} {7,S} {8,S}
7     H  u0 {6,S}
8     H  u0 {6,S}
9     O  u0 {4,S} {10,S}
10    C  u0 {9,S} {11,S} {12,S} {13,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
13    H  u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.1,-0.19,-0.43,-0.57,-0.65,-0.6,-0.33],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = """NNI1. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "p_Cj=O",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
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
    index = 71,
    label = "p_Cj=O_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
7    O  u0 {4,S} {8,S}
8    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-0.65,-0.48,-0.24,0.05,0.19,0.36],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = """NNI15. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "p_Cj=O_OCH3",
    group = 
"""
1  *1 Cb u0 {2,B} {5,S}
2     Cb u0 {1,B} {3,B}
3     Cb u0 {2,B} {4,B}
4  *2 Cb u0 {3,B} {7,S}
5     C  u1 {1,S} {6,D}
6     O  u0 {5,D}
7     O  u0 {4,S} {8,S}
8     C  u0 {7,S} {9,S} {10,S} {11,S}
9     H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79,-0.65,-0.48,-0.24,0.05,0.19,0.36],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = """NNI15. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "p_Cj=O_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
7    C  u0 {4,S} {8,D} {9,S}
8    O  u0 {7,D}
9    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24,-0.57,-0.84,-0.98,-1.08,-1.03,-0.76],'cal/(mol*K)'),
        H298 = (1.29,'kcal/mol'),
        S298 = (3.25,'cal/(mol*K)'),
    ),
    shortDesc = """NNI18. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "p_Csj",
    group = 
"""
1 *1 Cb     u0 {2,B} {5,S}
2    Cb     u0 {1,B} {3,B}
3    Cb     u0 {2,B} {4,B}
4 *2 Cb     u0 {3,B}
5    C      u1 {1,S} {6,S} {7,S}
6    H      u0 {5,S}
7    [H,Cs] u0 {5,S}
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
    index = 75,
    label = "p_Csj_C=C",
    group = 
"""
1  *1 Cb     u0 {2,B} {5,S}
2     Cb     u0 {1,B} {3,B}
3     Cb     u0 {2,B} {4,B}
4  *2 Cb     u0 {3,B} {8,S}
5     C      u1 {1,S} {6,S} {7,S}
6     H      u0 {5,S}
7     [H,Cs] u0 {5,S}
8     C      u0 {4,S} {9,S} {10,D}
9     H      u0 {8,S}
10    C      u0 {8,D} {11,S} {12,S}
11    H      u0 {10,S}
12    H      u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22,0.26,0.29,0.33,0.38,0.38,0.31],'cal/(mol*K)'),
        H298 = (-1.39,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = """NNI25. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "p_Csj_CHO",
    group = 
"""
1  *1 Cb     u0 {2,B} {5,S}
2     Cb     u0 {1,B} {3,B}
3     Cb     u0 {2,B} {4,B}
4  *2 Cb     u0 {3,B} {8,S}
5     C      u1 {1,S} {6,S} {7,S}
6     H      u0 {5,S}
7     [H,Cs] u0 {5,S}
8     C      u0 {4,S} {9,S} {10,D}
9     H      u0 {8,S}
10    O      u0 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.29,-0.22,-0.14,-0.1,-0.07,-0.02,0.07],'cal/(mol*K)'),
        H298 = (-1.24,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = """NNI27. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
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
    index = 78,
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
        S298 = (0.67956,'cal/(mol*K)','+|-',0.116932),
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
    index = 79,
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
        S298 = (-0.560854,'cal/(mol*K)','+|-',0.159047),
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
    index = 80,
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
        S298 = (0.383691,'cal/(mol*K)','+|-',0.147714),
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
    index = 81,
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
        S298 = (0.532593,'cal/(mol*K)','+|-',0.386775),
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
    index = 82,
    label = "3ring-Cs(Val7)2-Cs(Val7)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,H,N,O,S] u0 {1,S} {2,S}
4    Val7        u0 {1,S}
5    Val7        u0 {2,S}
6    Val7        u0 {1,S}
7    Val7        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.59132,0.398617,0.432198,0.437949,0.265727,0.165963,0.656101],'cal/(mol*K)','+|-',[0.232183,0.243631,0.28074,0.288399,0.247734,0.214168,0.448033]),
        H298 = (4.65189,'kcal/mol','+|-',3.05811),
        S298 = (-1.30202,'cal/(mol*K)','+|-',1.06276),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "3ring-Cs(Cl)2-Cs(Cl)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,H,N,O,S] u0 {1,S} {2,S}
4    Cl1s        u0 {1,S}
5    Cl1s        u0 {2,S}
6    Cl1s        u0 {1,S}
7    Cl1s        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.632941,0.405579,0.479952,0.524674,0.36498,0.256557,0.748332],'cal/(mol*K)','+|-',[0.232183,0.243631,0.28074,0.288399,0.247734,0.214168,0.448033]),
        H298 = (3.63542,'kcal/mol','+|-',1.27661),
        S298 = (-1.61346,'cal/(mol*K)','+|-',0.702335),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         10
""",
)

entry(
    index = 84,
    label = "3ring-Cs(F)2-Cs(F)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,H,N,O,S] u0 {1,S} {2,S}
4    F1s         u0 {1,S}
5    F1s         u0 {2,S}
6    F1s         u0 {1,S}
7    F1s         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.388895,0.227591,0.226941,0.269136,0.179437,0.117268,0.588238],'cal/(mol*K)','+|-',[0.164698,0.172818,0.199141,0.204574,0.175729,0.151919,0.31781]),
        H298 = (6.41036,'kcal/mol','+|-',0.905553),
        S298 = (-0.688462,'cal/(mol*K)','+|-',0.498197),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         12
""",
)

entry(
    index = 85,
    label = "3ring-Cs(Br)2-Cs(Br)2",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,H,N,O,S] u0 {1,S} {2,S}
4    Br1s        u0 {1,S}
5    Br1s        u0 {2,S}
6    Br1s        u0 {1,S}
7    Br1s        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.752123,0.56268,0.5897,0.520037,0.252765,0.124064,0.631734],'cal/(mol*K)','+|-',[0.278916,0.292668,0.337246,0.346448,0.297598,0.257275,0.538212]),
        H298 = (3.90988,'kcal/mol','+|-',1.53356),
        S298 = (-1.60415,'cal/(mol*K)','+|-',0.843699),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         7
""",
)

entry(
    index = 86,
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
    index = 87,
    label = "3ring-Cs(Val7)2-C(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd]     u0 {1,S} {3,[S,D]} {6,S}
3    [C,H,N,O,S] u0 {1,S} {2,[S,D]}
4    Val7        u0 {1,S}
5    Val7        u0 {1,S}
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
    index = 88,
    label = "3ring-Cs(Val7)2-Cs(Val7)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S]   u0 {1,S} {2,S}
4    Val7        u0 {1,S}
5    Val7        u0 {2,S}
6    Val7        u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.654673,0.289199,0.194016,0.142786,-0.047627,-0.127424,0.278206],'cal/(mol*K)','+|-',[0.208125,0.218387,0.25165,0.258516,0.222065,0.191977,0.401609]),
        H298 = (5.58291,'kcal/mol','+|-',2.04998),
        S298 = (-1.23185,'cal/(mol*K)','+|-',0.817197),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "3ring-Cs(Cl)2-Cs(Cl)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S]   u0 {1,S} {2,S}
4    Cl1s        u0 {1,S}
5    Cl1s        u0 {2,S}
6    Cl1s        u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.6639,0.30411,0.223223,0.18223,-0.0194462,-0.10263,0.303512],'cal/(mol*K)','+|-',[0.208125,0.218387,0.25165,0.258516,0.222065,0.191977,0.401609]),
        H298 = (4.78016,'kcal/mol','+|-',1.14433),
        S298 = (-1.68008,'cal/(mol*K)','+|-',0.629561),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         23
""",
)

entry(
    index = 90,
    label = "3ring-Cs(F)2-Cs(F)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S]   u0 {1,S} {2,S}
4    F1s         u0 {1,S}
5    F1s         u0 {2,S}
6    F1s         u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.581084,0.244418,0.152527,0.156392,0.0435641,-0.0193261,0.453625],'cal/(mol*K)','+|-',[0.195935,0.205596,0.236912,0.243376,0.209059,0.180733,0.378088]),
        H298 = (6.73748,'kcal/mol','+|-',1.07731),
        S298 = (-1.13529,'cal/(mol*K)','+|-',0.592689),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         25
""",
)

entry(
    index = 91,
    label = "3ring-Cs(Br)2-Cs(Br)",
    group = 
"""
1 *1 Cs          u0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          u0 {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S]   u0 {1,S} {2,S}
4    Br1s        u0 {1,S}
5    Br1s        u0 {2,S}
6    Br1s        u0 {1,S}
7    [C,H,N,O,S] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.719035,0.319068,0.206297,0.0897363,-0.166999,-0.260315,0.0774824],'cal/(mol*K)','+|-',[0.258404,0.271145,0.312445,0.32097,0.275712,0.238355,0.498631]),
        H298 = (5.23109,'kcal/mol','+|-',1.42078),
        S298 = (-0.88018,'cal/(mol*K)','+|-',0.781652),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         18
""",
)

entry(
    index = 92,
    label = "3ring-Cs(Val7)2-Cds(Val7)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {3,D} {6,S}
3    [C,N,O,S] u0 {1,S} {2,D}
4    Val7      u0 {1,S}
5    Val7      u0 {1,S}
6    Val7      u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0321042,0.410515,0.832681,1.06861,1.01097,0.847777,1.63748],'cal/(mol*K)','+|-',[0.386192,0.405234,0.466957,0.479698,0.412059,0.356228,0.745218]),
        H298 = (-3.51415,'kcal/mol','+|-',1.75756),
        S298 = (-1.57406,'cal/(mol*K)','+|-',0.634561),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "3ring-Cs(Cl)2-Cds(Cl)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {3,D} {6,S}
3    [C,N,O,S] u0 {1,S} {2,D}
4    Cl1s      u0 {1,S}
5    Cl1s      u0 {1,S}
6    Cl1s      u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.113755,0.474914,0.894815,1.13638,1.08259,0.932673,1.69048],'cal/(mol*K)','+|-',[0.386192,0.405234,0.466957,0.479698,0.412059,0.356228,0.745218]),
        H298 = (-3.26364,'kcal/mol','+|-',2.12339),
        S298 = (-1.50529,'cal/(mol*K)','+|-',1.1682),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOCl_G4 |         5
""",
)

entry(
    index = 94,
    label = "3ring-Cs(F)2-Cds(F)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {3,D} {6,S}
3    [C,N,O,S] u0 {1,S} {2,D}
4    F1s       u0 {1,S}
5    F1s       u0 {1,S}
6    F1s       u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0947649,0.264295,0.573717,0.761629,0.702552,0.539439,1.40592],'cal/(mol*K)','+|-',[0.364344,0.382308,0.440539,0.452559,0.388747,0.336074,0.703057]),
        H298 = (-2.78782,'kcal/mol','+|-',2.00326),
        S298 = (-1.29681,'cal/(mol*K)','+|-',1.10211),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library         | Number of Species
library:CHOF_G4 |         6
""",
)

entry(
    index = 95,
    label = "3ring-Cs(Br)2-Cds(Br)",
    group = 
"""
1 *1 Cs        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        u0 {1,S} {3,D} {6,S}
3    [C,N,O,S] u0 {1,S} {2,D}
4    Br1s      u0 {1,S}
5    Br1s      u0 {1,S}
6    Br1s      u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0773224,0.492336,1.02951,1.30781,1.24778,1.07122,1.81604],'cal/(mol*K)','+|-',[0.374942,0.393428,0.453354,0.465723,0.400055,0.34585,0.723508]),
        H298 = (-4.49098,'kcal/mol','+|-',2.06153),
        S298 = (-1.92009,'cal/(mol*K)','+|-',1.13417),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library          | Number of Species
library:CHOBr_G4 |         6
""",
)

entry(
    index = 96,
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
        S298 = (0.601587,'cal/(mol*K)','+|-',0.129627),
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
    index = 97,
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
        S298 = (-0.747445,'cal/(mol*K)','+|-',0.195564),
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
    index = 98,
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
        S298 = (0.193894,'cal/(mol*K)','+|-',0.180559),
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
    index = 99,
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
        S298 = (-0.368531,'cal/(mol*K)','+|-',0.25552),
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
    index = 100,
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
        S298 = (0.449729,'cal/(mol*K)','+|-',0.247856),
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
    index = 101,
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
        S298 = (-1.18741,'cal/(mol*K)','+|-',0.384763),
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
    index = 102,
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
        S298 = (-0.0682301,'cal/(mol*K)','+|-',0.371038),
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
    index = 103,
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
        S298 = (-0.0247292,'cal/(mol*K)','+|-',0.497043),
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
    index = 104,
    label = "Cs(Val7)-Cs(Val7)",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S}
2 *2 Cs   u0 {1,S} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.145298,-0.119167,-0.0859063,-0.0789092,-0.0736843,-0.0466396,0.0579328],'cal/(mol*K)','+|-',[0.0367635,0.0422522,0.0431921,0.0425584,0.0369039,0.0318293,0.0259401]),
        H298 = (1.211,'kcal/mol','+|-',0.131059),
        S298 = (0.409324,'cal/(mol*K)','+|-',0.0860265),
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
    index = 105,
    label = "Cs(Cl)-Cs(Cl)",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S}
2 *2 Cs   u0 {1,S} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.212013,-0.139086,-0.0392286,0.0215442,0.0690026,0.110935,0.206044],'cal/(mol*K)','+|-',[0.0486499,0.0559131,0.0571569,0.0563184,0.0488356,0.0421203,0.0343271]),
        H298 = (1.15744,'kcal/mol','+|-',0.173433),
        S298 = (-0.127883,'cal/(mol*K)','+|-',0.113841),
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
    index = 106,
    label = "Cs(F)-Cs(F)",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S}
2 *2 Cs  u0 {1,S} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.148682,-0.0760222,0.0144627,0.0592617,0.0805109,0.10537,0.176623],'cal/(mol*K)','+|-',[0.043691,0.0502139,0.0513309,0.0505778,0.0438578,0.037827,0.0308281]),
        H298 = (1.71275,'kcal/mol','+|-',0.155755),
        S298 = (-0.00541025,'cal/(mol*K)','+|-',0.102237),
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
    index = 107,
    label = "Cs(Br)-Cs(Br)",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S}
2 *2 Cs   u0 {1,S} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.241659,-0.152083,-0.0407121,0.0220502,0.0720941,0.108305,0.194193],'cal/(mol*K)','+|-',[0.0497753,0.0572066,0.0584791,0.0576212,0.0499653,0.0430947,0.0351212]),
        H298 = (0.907176,'kcal/mol','+|-',0.177445),
        S298 = (-0.292531,'cal/(mol*K)','+|-',0.116474),
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
    index = 108,
    label = "Cs(Val7)-Cds(Val7)",
    group = 
"""
1 *1 Cs   u0 {2,S} {3,S}
2 *2 Cd   u0 {1,S} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.487245,-0.366436,-0.26625,-0.211496,-0.0949754,-0.000924551,0.319447],'cal/(mol*K)','+|-',[0.112622,0.129436,0.132315,0.130374,0.113052,0.0975059,0.0794652]),
        H298 = (2.0618,'kcal/mol','+|-',0.401486),
        S298 = (0.867885,'cal/(mol*K)','+|-',0.263534),
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
    index = 109,
    label = "Cs(Cl)-Cds(Cl)",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Cd u0 {1,S} {4,S}
3    Cl u0 {1,S}
4    Cl u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.370477,-0.128165,0.0193874,0.0781517,0.147875,0.195604,0.451944],'cal/(mol*K)','+|-',[0.148659,0.170854,0.174654,0.172092,0.149227,0.128707,0.104893]),
        H298 = (1.80547,'kcal/mol','+|-',0.529958),
        S298 = (-0.292118,'cal/(mol*K)','+|-',0.347863),
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
    index = 110,
    label = "Cs(F)-Cds(F)",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Cd u0 {1,S} {4,S}
3    F  u0 {1,S}
4    F  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.251678,-0.133366,-0.0656162,-0.0246591,0.0483949,0.101528,0.422424],'cal/(mol*K)','+|-',[0.140481,0.161454,0.165046,0.162624,0.141017,0.121626,0.0991226]),
        H298 = (2.40802,'kcal/mol','+|-',0.500803),
        S298 = (0.154638,'cal/(mol*K)','+|-',0.328725),
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
    index = 111,
    label = "Cs(Br)-Cds(Br)",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2 *2 Cd u0 {1,S} {4,S}
3    Br u0 {1,S}
4    Br u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.452812,-0.282992,-0.116251,-0.0195095,0.116198,0.185973,0.374584],'cal/(mol*K)','+|-',[0.143709,0.165164,0.168838,0.166361,0.144257,0.124421,0.1014]),
        H298 = (1.40742,'kcal/mol','+|-',0.51231),
        S298 = (-0.18706,'cal/(mol*K)','+|-',0.336278),
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
    index = 112,
    label = "Cds(Val7)-Cds(Val7)",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 Cd   u0 {1,S} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.112012,0.0156248,0.139183,0.111374,0.0182027,-0.022415,0.149256],'cal/(mol*K)','+|-',[0.129797,0.149176,0.152494,0.150257,0.130293,0.112376,0.0915843]),
        H298 = (0.238344,'kcal/mol','+|-',0.462717),
        S298 = (-0.231313,'cal/(mol*K)','+|-',0.303725),
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
    index = 113,
    label = "Cds(Cl)-Cds(Cl)",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 Cd   u0 {1,S} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.143088,-0.103202,0.0161273,-0.00344062,-0.0986116,-0.130257,0.110146],'cal/(mol*K)','+|-',[0.199567,0.229361,0.234463,0.231023,0.200328,0.172782,0.140813]),
        H298 = (0.0446388,'kcal/mol','+|-',0.711438),
        S298 = (0.0777874,'cal/(mol*K)','+|-',0.466985),
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
    index = 114,
    label = "Cds(F)-Cds(F)",
    group = 
"""
1 *1 Cd  u0 {2,S} {3,S}
2 *2 Cd  u0 {1,S} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0595707,-0.0266998,0.078211,0.0517162,-0.0393958,-0.0704584,0.121822],'cal/(mol*K)','+|-',[0.181395,0.208477,0.213114,0.209988,0.182088,0.157049,0.127991]),
        H298 = (0.675509,'kcal/mol','+|-',0.646659),
        S298 = (0.0504908,'cal/(mol*K)','+|-',0.424464),
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
    index = 115,
    label = "Cds(Br)-Cds(Br)",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 Cd   u0 {1,S} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.158306,-0.131038,0.00641817,0.0123105,-0.0231756,-0.0296819,0.16498],'cal/(mol*K)','+|-',[0.194245,0.223245,0.228211,0.224863,0.194987,0.168174,0.137058]),
        H298 = (-0.0544731,'kcal/mol','+|-',0.692468),
        S298 = (-0.54781,'cal/(mol*K)','+|-',0.454533),
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
    index = 116,
    label = "Cds(Val7)=Cds(Val7)",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S}
2 *2 Cd   u0 {1,D} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.192955,0.160487,0.102905,0.0777284,0.0301348,0.000628364,-0.0942518],'cal/(mol*K)','+|-',[0.0503904,0.0579135,0.0592018,0.0583333,0.0505828,0.0436272,0.0355552]),
        H298 = (1.72557,'kcal/mol','+|-',0.179638),
        S298 = (-0.0266367,'cal/(mol*K)','+|-',0.117913),
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
    index = 117,
    label = "Cds(Cl)=Cds(Cl)",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S}
2 *2 Cd   u0 {1,D} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.275328,0.248766,0.186314,0.14346,0.0567248,0.00969829,-0.0904599],'cal/(mol*K)','+|-',[0.0687218,0.0789817,0.0807387,0.0795542,0.0689842,0.0594983,0.0484898]),
        H298 = (1.36086,'kcal/mol','+|-',0.244988),
        S298 = (-0.0825674,'cal/(mol*K)','+|-',0.160809),
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
    index = 118,
    label = "Cds(F)=Cds(F)",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S}
2 *2 Cd  u0 {1,D} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.143061,0.084595,0.0485554,0.0373149,0.0157509,0.00236969,-0.0605414],'cal/(mol*K)','+|-',[0.0584833,0.0672147,0.0687098,0.0677018,0.0587066,0.0506339,0.0412655]),
        H298 = (3.00962,'kcal/mol','+|-',0.208488),
        S298 = (0.192645,'cal/(mol*K)','+|-',0.136851),
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
    index = 119,
    label = "Cds(Br)=Cds(Br)",
    group = 
"""
1 *1 Cd   u0 {2,D} {3,S}
2 *2 Cd   u0 {1,D} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.191068,0.135447,0.086284,0.0841781,0.0456014,0.0200424,-0.0716922],'cal/(mol*K)','+|-',[0.0792966,0.0911353,0.0931626,0.0917958,0.0795993,0.0686537,0.0559512]),
        H298 = (1.36026,'kcal/mol','+|-',0.282686),
        S298 = (-0.385388,'cal/(mol*K)','+|-',0.185554),
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
    index = 120,
    label = "Cd(Val7)-CO",
    group = 
"""
1 *1 Cd   u0 {2,S} {3,S}
2 *2 CO   u0 {1,S} {4,D}
3    Val7 u0 {1,S}
4    O2d  u0 {2,D}
""",
    thermo = None,
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
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
        S298 = (-0.618867,'cal/(mol*K)','+|-',0.696472),
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
    index = 122,
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
        S298 = (-0.336434,'cal/(mol*K)','+|-',0.663324),
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
    index = 123,
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
        S298 = (-1.53298,'cal/(mol*K)','+|-',0.606486),
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
    index = 124,
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
        S298 = (1.08441,'cal/(mol*K)','+|-',0.350777),
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
    index = 125,
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
    index = 126,
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
    index = 127,
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
    index = 128,
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
        S298 = (0.145431,'cal/(mol*K)','+|-',0.288405),
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
    index = 129,
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
        S298 = (0.213347,'cal/(mol*K)','+|-',0.363116),
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
    index = 130,
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
        S298 = (-1.1699,'cal/(mol*K)','+|-',0.388968),
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
    index = 131,
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
        S298 = (-0.795188,'cal/(mol*K)','+|-',0.430296),
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
    index = 132,
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
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
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
        S298 = (-0.388485,'cal/(mol*K)','+|-',0.31971),
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
    index = 134,
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
        S298 = (0.00170779,'cal/(mol*K)','+|-',0.330943),
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
    index = 135,
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
        S298 = (-0.453872,'cal/(mol*K)','+|-',0.319716),
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
    index = 136,
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
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
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
        S298 = (-1.57257,'cal/(mol*K)','+|-',0.291835),
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
    index = 138,
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
        S298 = (-1.22528,'cal/(mol*K)','+|-',0.3987),
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
    index = 139,
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
        S298 = (-0.964637,'cal/(mol*K)','+|-',0.44221),
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
    index = 140,
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
        S298 = (-1.51255,'cal/(mol*K)','+|-',0.655449),
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
    index = 141,
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
        S298 = (-0.193804,'cal/(mol*K)','+|-',0.501749),
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
    index = 142,
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
        S298 = (-0.0115696,'cal/(mol*K)','+|-',0.795472),
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
    index = 143,
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
        S298 = (-1.41611,'cal/(mol*K)','+|-',0.802255),
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
    index = 144,
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
        S298 = (0.371415,'cal/(mol*K)','+|-',1.42736),
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
    index = 145,
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
        S298 = (1.70899,'cal/(mol*K)','+|-',0.33045),
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
    index = 146,
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
        S298 = (1.94891,'cal/(mol*K)','+|-',0.368314),
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
    index = 147,
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
        S298 = (1.85519,'cal/(mol*K)','+|-',0.452945),
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
    index = 148,
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
        S298 = (0.572499,'cal/(mol*K)','+|-',0.589987),
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
    index = 149,
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
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
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
        S298 = (1.49382,'cal/(mol*K)','+|-',0.24891),
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
    index = 151,
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
        S298 = (1.4257,'cal/(mol*K)','+|-',0.28784),
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
    index = 152,
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
        S298 = (1.25761,'cal/(mol*K)','+|-',0.323667),
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

tree(
"""
L1: R
    L2: aromatic-ortho
        L3: o_OH
            L4: o_OH_OH
            L4: o_OH_MeO
            L4: o_OH_vinyl
            L4: o_OH_CHO
        L3: o_CHO
            L4: o_CHO_CHO
            L4: o_CHO_vinyl
            L4: o_CHO_CH3
            L4: o_CHO_C2H5
            L4: o_CHO_MeO
        L3: o_vinyl
            L4: o_vinyl_vinyl
            L4: o_vinyl_CH3
            L4: o_vinyl_C2H5
        L3: o_MeO
            L4: o_MeO_MeO
            L4: o_MeO_vinyl
        L3: o_CH3
            L4: o_CH3_CH3
            L4: o_CH3_C2H5
        L3: o_C2H5
            L4: o_C2H5_C2H5
        L3: o_Oj
            L4: o_Oj_OH
            L4: o_Oj_OCH3
            L4: o_Oj_CHO
            L4: o_Oj_C=C
            L4: o_Oj_Cs
        L3: o_OCH2j
            L4: o_OCH2j_CHO
            L4: o_OCH2j_OCH3
        L3: o_Cj=O
            L4: o_Cj=O_OH
            L4: o_Cj=O_OCH3
            L4: o_Cj=O_C=C
        L3: o_C=Cj
            L4: o_C=Cj_OH
            L4: o_C=Cj_CHO
            L4: o_C=Cj_C=C
            L4: o_C=Cj_Cs
        L3: o_Csj
            L4: o_Csj_C=C
            L4: o_Csj_CHO
            L4: o_Csj_Cs
    L2: aromatic-meta
        L3: m_CHO_CHO
        L3: m_Oj_OCH3
        L3: m_Oj_CHO
        L3: m_Cj=O_CHO
    L2: aromatic-para
        L3: p_OH
            L4: p_OH_OH
            L4: p_OH_MeO
            L4: p_OH_CHO
        L3: p_MeO
            L4: p_MeO_MeO
            L4: p_MeO_CHO
        L3: p_CHO
            L4: p_CHO_CHO
        L3: p_Oj
            L4: p_Oj_OH
            L4: p_Oj_OCH3
            L4: p_Oj_C=C
            L4: p_Oj_Cs
        L3: p_OCH2j
            L4: p_OCH2j_OH
            L4: p_OCH2j_OCH3
        L3: p_Cj=O
            L4: p_Cj=O_OH
            L4: p_Cj=O_OCH3
            L4: p_Cj=O_CHO
        L3: p_Csj
            L4: p_Csj_C=C
            L4: p_Csj_CHO
    L2: intVal7
        L3: Cs(Val7)2-Cs(Val7)2
            L4: Cs(Cl)2-Cs(Cl)2
            L4: Cs(F)2-Cs(F)2
            L4: Cs(Br)2-Cs(Br)2
        L3: 3ring-Cs(Val7)2-Cs(Val7)2
            L4: 3ring-Cs(Cl)2-Cs(Cl)2
            L4: 3ring-Cs(F)2-Cs(F)2
            L4: 3ring-Cs(Br)2-Cs(Br)2
        L3: Cs(Val7)2-C(Val7)
            L4: 3ring-Cs(Val7)2-C(Val7)
                L5: 3ring-Cs(Val7)2-Cs(Val7)
                    L6: 3ring-Cs(Cl)2-Cs(Cl)
                    L6: 3ring-Cs(F)2-Cs(F)
                    L6: 3ring-Cs(Br)2-Cs(Br)
                L5: 3ring-Cs(Val7)2-Cds(Val7)
                    L6: 3ring-Cs(Cl)2-Cds(Cl)
                    L6: 3ring-Cs(F)2-Cds(F)
                    L6: 3ring-Cs(Br)2-Cds(Br)
            L4: Cs(Val7)2-Cs(Val7)
                L5: Cs(Cl)2-Cs(Cl)
                L5: Cs(F)2-Cs(F)
                L5: Cs(Br)2-Cs(Br)
            L4: Cs(Val7)2-Cds(Val7)
                L5: Cs(Cl)2-Cds(Cl)
                L5: Cs(F)2-Cds(F)
                L5: Cs(Br)2-Cds(Br)
        L3: Cs(Val7)-Cs(Val7)
            L4: Cs(Cl)-Cs(Cl)
            L4: Cs(F)-Cs(F)
            L4: Cs(Br)-Cs(Br)
        L3: Cs(Val7)-Cds(Val7)
            L4: Cs(Cl)-Cds(Cl)
            L4: Cs(F)-Cds(F)
            L4: Cs(Br)-Cds(Br)
        L3: Cds(Val7)-Cds(Val7)
            L4: Cds(Cl)-Cds(Cl)
            L4: Cds(F)-Cds(F)
            L4: Cds(Br)-Cds(Br)
        L3: Cds(Val7)=Cds(Val7)
            L4: Cds(Cl)=Cds(Cl)
            L4: Cds(F)=Cds(F)
            L4: Cds(Br)=Cds(Br)
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
"""
)

