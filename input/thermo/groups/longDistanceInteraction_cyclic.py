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
    index = 11111,
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
    index = 21111,
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
    index = 113,
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
    index = 114,
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
    index = 115,
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
    index = 116,
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
    index = 117,
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
    index = 118,
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
    index = 119,
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
    index = 1110,
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
    index = 1111,
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
    index = 1112,
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
    index = 1113,
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
    index = 1114,
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
    index = 1115,
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
    index = 1116,
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
    index = 1117,
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
    index = 1118,
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
    index = 1119,
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
    index = 1120,
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
    index = 1121,
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
    index = 1122,
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
    index = 1123,
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
    index = 1124,
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
    index = 1125,
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
    index = 1126,
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
    index = 1127,
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
    index = 1128,
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
    index = 1129,
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
    index = 1130,
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
    index = 1131,
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
    index = 1132,
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
    index = 1133,
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
    index = 1134,
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
    index = 1135,
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
    index = 1136,
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
    index = 1137,
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
    index = 1138,
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
    index = 1139,
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
    index = 1140,
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
    index = 1141,
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
    index = 1142,
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
    index = 1143,
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
    index = 1144,
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
    index = 1145,
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
    index = 1146,
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
    index = 1147,
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
    index = 1148,
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
    index = 1149,
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
    index = 1150,
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
    index = 1151,
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
    index = 1152,
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
    index = 1153,
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
    index = 1154,
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
    index = 1155,
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
    index = 1156,
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
    index = 1157,
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
    index = 1158,
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
    index = 1159,
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
    index = 1160,
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
    index = 1161,
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
    index = 1162,
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
    index = 1163,
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
    index = 1164,
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
    index = 1165,
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
    index = 1166,
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
    index = 1167,
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
    index = 1168,
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
    index = 1169,
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
    index = 1170,
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
    index = 1171,
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
    index = 1172,
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
    index = 1173,
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
    index = 1174,
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
    index = 1175,
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
    index = 1176,
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
"""
)

