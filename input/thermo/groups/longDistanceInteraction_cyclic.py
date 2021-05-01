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
    label = "halogen",
    group = 
"""
1 *1 R!H  ux {2,[S,D,T]} {3,S}
2 *2 R!H  ux {1,[S,D,T]} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """top of halogen tree""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "halogen-3",
    group = 
"""
1 *1 R!H  ux {2,[S,D]} {3,[S,D,T]} {4,S}
2 *2 R!H  ux {1,[S,D]} {3,[S,D,T]} {5,S}
3    R!H  ux {1,[S,D,T]} {2,[S,D,T]}
4    Val7 u0 {1,S}
5    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """halogen-3""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "3ring-Cs(Val7CsH)-Cs(Val7CsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436187,-0.518008,-0.475131,-0.430801,-0.367708,-0.231508,0.143791],'cal/(mol*K)','+|-',[0.181042,0.199543,0.212396,0.211207,0.177764,0.140977,0.208802]),
        H298 = (3.92932,'kcal/mol','+|-',2.70925),
        S298 = (2.99314,'cal/(mol*K)','+|-',0.559288),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "3ring-Cs(BrCsH)-Cs(BrCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432595,-0.550928,-0.551879,-0.532868,-0.482725,-0.359799,-0.024179],'cal/(mol*K)','+|-',[0.181042,0.199543,0.212396,0.211207,0.177764,0.140977,0.208802]),
        H298 = (2.99563,'kcal/mol','+|-',0.778715),
        S298 = (2.91945,'cal/(mol*K)','+|-',0.597458),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         8
""",
)

entry(
    index = 81,
    label = "3ring-Cs(ClCsH)-Cs(ClCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.40627,-0.532866,-0.523301,-0.512252,-0.492881,-0.352207,0.077302],'cal/(mol*K)','+|-',[0.176464,0.194497,0.207026,0.205866,0.173269,0.137413,0.203522]),
        H298 = (3.30934,'kcal/mol','+|-',0.759025),
        S298 = (3.30225,'cal/(mol*K)','+|-',0.582352),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 82,
    label = "3ring-Cs(FCsH)-Cs(FCsCs)_624",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469696,-0.47023,-0.350213,-0.247283,-0.127519,0.0174823,0.378251],'cal/(mol*K)','+|-',[0.175714,0.19367,0.206145,0.204991,0.172533,0.136828,0.202657]),
        H298 = (5.48298,'kcal/mol','+|-',0.755797),
        S298 = (2.75772,'cal/(mol*K)','+|-',0.579875),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 83,
    label = "3ring-Cs(Val7CsH)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.298782,-0.441915,-0.478958,-0.474583,-0.419368,-0.281652,0.0208283],'cal/(mol*K)','+|-',[0.174239,0.192045,0.204415,0.20327,0.171084,0.13568,0.200956]),
        H298 = (4.01385,'kcal/mol','+|-',2.64545),
        S298 = (2.46878,'cal/(mol*K)','+|-',0.257076),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "3ring-Cs(BrCsH)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.358298,-0.55223,-0.62483,-0.645159,-0.608977,-0.468318,-0.111348],'cal/(mol*K)','+|-',[0.174239,0.192045,0.204415,0.20327,0.171084,0.13568,0.200956]),
        H298 = (3.12054,'kcal/mol','+|-',0.749454),
        S298 = (2.53217,'cal/(mol*K)','+|-',0.575008),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         16
""",
)

entry(
    index = 85,
    label = "3ring-Cs(ClCsH)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.251981,-0.391746,-0.44753,-0.468683,-0.442189,-0.31602,-0.0171671],'cal/(mol*K)','+|-',[0.17291,0.19058,0.202856,0.20172,0.16978,0.134645,0.199424]),
        H298 = (3.38762,'kcal/mol','+|-',0.743739),
        S298 = (2.55331,'cal/(mol*K)','+|-',0.570623),
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
    index = 86,
    label = "3ring-Cs(FCsH)-Cs(FCsH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.286066,-0.381768,-0.364513,-0.309906,-0.206938,-0.0606194,0.191],'cal/(mol*K)','+|-',[0.167495,0.184611,0.196503,0.195403,0.164462,0.130428,0.193178]),
        H298 = (5.5334,'kcal/mol','+|-',0.720445),
        S298 = (2.32086,'cal/(mol*K)','+|-',0.552752),
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
    index = 87,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7CsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.544457,0.522496,0.467446,0.390351,0.233138,0.224993,0.438899],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (4.78868,'kcal/mol','+|-',4.10889),
        S298 = (3.61401,'cal/(mol*K)','+|-',3.45734),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "3ring-Cs(BrCsCs)-Cs(BrCsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.552206,0.445171,0.363102,0.254796,0.0590491,0.018891,0.177896],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (2.4478,'kcal/mol','+|-',1.67569),
        S298 = (3.85512,'cal/(mol*K)','+|-',1.28565),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 89,
    label = "3ring-Cs(ClCsCs)-Cs(ClCsH)_424",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.969117,0.84818,0.657084,0.508653,0.245849,0.236684,0.545361],'cal/(mol*K)','+|-',[0.780807,0.860599,0.916033,0.910905,0.766671,0.608016,0.900533]),
        H298 = (6.29222,'kcal/mol','+|-',3.35849),
        S298 = (5.20946,'cal/(mol*K)','+|-',2.57675),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 90,
    label = "3ring-Cs(FCsCs)-Cs(FCsH)_607",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.112047,0.274138,0.382153,0.407604,0.394517,0.419403,0.593439],'cal/(mol*K)','+|-',[0.342077,0.377035,0.401321,0.399074,0.335884,0.266376,0.39453]),
        H298 = (5.62601,'kcal/mol','+|-',1.47138),
        S298 = (1.77744,'cal/(mol*K)','+|-',1.12889),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 91,
    label = "3ring-Cs(Val7CdH)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.31037,-1.83461,-1.38096,-1.0346,-0.569234,-0.163844,0.593097],'cal/(mol*K)','+|-',[1.46788,1.61788,1.7221,1.71246,1.4413,1.14304,1.69296]),
        H298 = (7.13476,'kcal/mol','+|-',5.48914),
        S298 = (5.01115,'cal/(mol*K)','+|-',1.27282),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "3ring-Cs(BrCdH)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.30768,-1.99896,-1.60528,-1.27261,-0.791702,-0.351685,0.362914],'cal/(mol*K)','+|-',[1.46788,1.61788,1.7221,1.71246,1.4413,1.14304,1.69296]),
        H298 = (5.19405,'kcal/mol','+|-',6.31378),
        S298 = (5.46116,'cal/(mol*K)','+|-',4.84417),
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
    index = 93,
    label = "3ring-Cs(FCdH)-Cd(FCd)_612",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.31306,-1.67026,-1.15663,-0.796598,-0.346766,0.0239968,0.823279],'cal/(mol*K)','+|-',[1.46774,1.61773,1.72194,1.7123,1.44117,1.14293,1.6928]),
        H298 = (9.07546,'kcal/mol','+|-',6.31319),
        S298 = (4.56114,'cal/(mol*K)','+|-',4.84371),
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
    index = 94,
    label = "3ring-Cd(Val7Cs)=Cd(Val7Cs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.304959,-0.318025,-0.358635,-0.319858,-0.212382,-0.125777,-0.0728311],'cal/(mol*K)','+|-',[0.265048,0.292134,0.310952,0.309211,0.26025,0.206394,0.30569]),
        H298 = (4.01891,'kcal/mol','+|-',6.09101),
        S298 = (1.33209,'cal/(mol*K)','+|-',0.681507),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "3ring-Cd(BrCs)=Cd(BrCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.214688,-0.26457,-0.340698,-0.318422,-0.23341,-0.159327,-0.113336],'cal/(mol*K)','+|-',[0.265048,0.292134,0.310952,0.309211,0.26025,0.206394,0.30569]),
        H298 = (1.86256,'kcal/mol','+|-',1.14005),
        S298 = (1.70271,'cal/(mol*K)','+|-',0.87469),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         13
""",
)

entry(
    index = 96,
    label = "3ring-Cd(ClCs)=Cd(ClCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.239963,-0.233991,-0.277575,-0.261366,-0.19091,-0.118522,-0.0842916],'cal/(mol*K)','+|-',[0.264213,0.291213,0.309971,0.308236,0.25943,0.205743,0.304726]),
        H298 = (2.69132,'kcal/mol','+|-',1.13646),
        S298 = (1.26122,'cal/(mol*K)','+|-',0.871933),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         16
""",
)

entry(
    index = 97,
    label = "3ring-Cd(FCs)=Cd(FCs)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.460226,-0.455514,-0.457633,-0.379787,-0.212826,-0.0994828,-0.0208657],'cal/(mol*K)','+|-',[0.261181,0.287872,0.306415,0.304699,0.256453,0.203382,0.30123]),
        H298 = (7.50285,'kcal/mol','+|-',1.12342),
        S298 = (1.03235,'cal/(mol*K)','+|-',0.861928),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         18
""",
)

entry(
    index = 98,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378271,-0.571299,-0.612529,-0.61028,-0.54719,-0.389276,-0.0255598],'cal/(mol*K)','+|-',[0.220133,0.242629,0.258258,0.256812,0.216148,0.171418,0.253888]),
        H298 = (5.35181,'kcal/mol','+|-',4.67864),
        S298 = (2.91842,'cal/(mol*K)','+|-',0.728442),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "3ring-Cs(BrBrCs)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.369235,-0.678769,-0.807667,-0.857273,-0.819367,-0.646032,-0.265096],'cal/(mol*K)','+|-',[0.220133,0.242629,0.258258,0.256812,0.216148,0.171418,0.253888]),
        H298 = (4.04044,'kcal/mol','+|-',0.94686),
        S298 = (3.31055,'cal/(mol*K)','+|-',0.726466),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         11
""",
)

entry(
    index = 100,
    label = "3ring-Cs(ClClCs)-Cs(ClCsH)_385",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347698,-0.540407,-0.594455,-0.604019,-0.567891,-0.424377,-0.0515813],'cal/(mol*K)','+|-',[0.183415,0.202158,0.21518,0.213975,0.180094,0.142825,0.211539]),
        H298 = (3.96235,'kcal/mol','+|-',0.788922),
        S298 = (2.85402,'cal/(mol*K)','+|-',0.60529),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         13
""",
)

entry(
    index = 101,
    label = "3ring-Cs(FFCs)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41788,-0.49472,-0.435466,-0.369547,-0.254313,-0.0974198,0.239998],'cal/(mol*K)','+|-',[0.179565,0.197915,0.210663,0.209484,0.176314,0.139827,0.207098]),
        H298 = (8.05265,'kcal/mol','+|-',0.772361),
        S298 = (2.5907,'cal/(mol*K)','+|-',0.592584),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         15
""",
)

entry(
    index = 102,
    label = "3ring-Cs(Val7Cs)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.332525,-0.372189,-0.355951,-0.325772,-0.245264,-0.101378,0.160737],'cal/(mol*K)','+|-',[0.28837,0.317839,0.338312,0.336418,0.28315,0.224554,0.332588]),
        H298 = (6.01675,'kcal/mol','+|-',2.58646),
        S298 = (1.53465,'cal/(mol*K)','+|-',0.251431),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "3ring-Cs(BrCs)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.346971,-0.464919,-0.501447,-0.48262,-0.380147,-0.225397,0.043951],'cal/(mol*K)','+|-',[0.28837,0.317839,0.338312,0.336418,0.28315,0.224554,0.332588]),
        H298 = (4.92231,'kcal/mol','+|-',1.24037),
        S298 = (1.47817,'cal/(mol*K)','+|-',0.951655),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         9
""",
)

entry(
    index = 104,
    label = "3ring-Cs(ClCs)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.361202,-0.396873,-0.365843,-0.343216,-0.277712,-0.126832,0.168133],'cal/(mol*K)','+|-',[0.287692,0.317093,0.337517,0.335628,0.282484,0.224027,0.331806]),
        H298 = (5.68414,'kcal/mol','+|-',1.23745),
        S298 = (1.6787,'cal/(mol*K)','+|-',0.949418),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 105,
    label = "3ring-Cs(FCs)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.289402,-0.254776,-0.200562,-0.151479,-0.0779337,0.0480944,0.270126],'cal/(mol*K)','+|-',[0.261721,0.288467,0.307048,0.305329,0.256983,0.203803,0.301852]),
        H298 = (7.4438,'kcal/mol','+|-',1.12574),
        S298 = (1.44708,'cal/(mol*K)','+|-',0.863709),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         12
""",
)

entry(
    index = 106,
    label = "3ring-Cs(Val7Cs)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.276629,-0.350377,-0.329647,-0.30763,-0.25625,-0.124313,0.170625],'cal/(mol*K)','+|-',[0.406461,0.447999,0.476856,0.474186,0.399103,0.316512,0.468787]),
        H298 = (7.45825,'kcal/mol','+|-',4.09661),
        S298 = (2.18235,'cal/(mol*K)','+|-',0.7033),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "3ring-Cs(BrCs)-Cs(BrBrCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0960961,-0.258711,-0.303876,-0.320898,-0.31965,-0.212733,0.0330053],'cal/(mol*K)','+|-',[0.406461,0.447999,0.476856,0.474186,0.399103,0.316512,0.468787]),
        H298 = (6.26591,'kcal/mol','+|-',1.74831),
        S298 = (2.53036,'cal/(mol*K)','+|-',1.34137),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 108,
    label = "3ring-Cs(ClCs)-Cs(ClClCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.354153,-0.452523,-0.426691,-0.402198,-0.339363,-0.187277,0.159793],'cal/(mol*K)','+|-',[0.300139,0.330811,0.352119,0.350148,0.294705,0.233719,0.346161]),
        H298 = (6.28543,'kcal/mol','+|-',1.29099),
        S298 = (2.18953,'cal/(mol*K)','+|-',0.990493),
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
    index = 109,
    label = "3ring-Cs(FCs)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.379639,-0.339897,-0.258373,-0.199793,-0.109738,0.0270713,0.319077],'cal/(mol*K)','+|-',[0.280395,0.30905,0.328956,0.327115,0.275319,0.218344,0.32339]),
        H298 = (9.8234,'kcal/mol','+|-',1.20606),
        S298 = (1.82717,'cal/(mol*K)','+|-',0.925337),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         10
""",
)

entry(
    index = 110,
    label = "3ring-Cs(Val7CsH)-Cs(Val7Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.106995,0.0537857,0.0499011,0.0115443,-0.0757191,-0.0592183,0.100968],'cal/(mol*K)','+|-',[0.38845,0.428147,0.455725,0.453174,0.381418,0.302487,0.448014]),
        H298 = (5.67187,'kcal/mol','+|-',0.0929845),
        S298 = (3.41865,'cal/(mol*K)','+|-',2.25198),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "3ring-Cs(BrCsH)-Cs(BrBrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.18112,0.0419643,-0.0177598,-0.0815083,-0.172199,-0.144483,0.0120179],'cal/(mol*K)','+|-',[0.38845,0.428147,0.455725,0.453174,0.381418,0.302487,0.448014]),
        H298 = (5.70474,'kcal/mol','+|-',1.67084),
        S298 = (4.21485,'cal/(mol*K)','+|-',1.28193),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 112,
    label = "3ring-Cs(ClCsH)-Cs(ClClCs)_498",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0328703,0.065607,0.117562,0.104597,0.0207608,0.0260465,0.189919],'cal/(mol*K)','+|-',[0.400668,0.441614,0.470059,0.467428,0.393415,0.312001,0.462105]),
        H298 = (5.63899,'kcal/mol','+|-',1.72339),
        S298 = (2.62246,'cal/(mol*K)','+|-',1.32225),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 113,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.402069,-0.581071,-0.563397,-0.533569,-0.466435,-0.30917,0.116554],'cal/(mol*K)','+|-',[0.411745,0.453823,0.483055,0.48035,0.404291,0.320627,0.474881]),
        H298 = (5.81179,'kcal/mol','+|-',4.07685),
        S298 = (3.66049,'cal/(mol*K)','+|-',1.6773),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "3ring-Cs(BrBrCs)-Cs(BrCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.309918,-0.598703,-0.664265,-0.684144,-0.680956,-0.566913,-0.17035],'cal/(mol*K)','+|-',[0.411745,0.453823,0.483055,0.48035,0.404291,0.320627,0.474881]),
        H298 = (5.49321,'kcal/mol','+|-',1.77104),
        S298 = (4.60216,'cal/(mol*K)','+|-',1.35881),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 115,
    label = "3ring-Cs(ClClCs)-Cs(ClCsCs)_471",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.387751,-0.582045,-0.590618,-0.584213,-0.544388,-0.390162,0.060055],'cal/(mol*K)','+|-',[0.245512,0.270602,0.288032,0.28642,0.241068,0.191181,0.283158]),
        H298 = (3.95142,'kcal/mol','+|-',1.05602),
        S298 = (3.3853,'cal/(mol*K)','+|-',0.810219),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 116,
    label = "3ring-Cs(FFCs)-Cs(FCsCs)_574",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.508537,-0.562465,-0.435307,-0.332349,-0.17396,0.0295643,0.459956],'cal/(mol*K)','+|-',[0.24057,0.265155,0.282234,0.280654,0.236215,0.187332,0.277458]),
        H298 = (7.99075,'kcal/mol','+|-',1.03476),
        S298 = (2.99401,'cal/(mol*K)','+|-',0.793909),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 117,
    label = "3ring-Cs(Val7CdH)-Cd(Val7Cd)_61",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881367,-0.794468,-0.674023,-0.565186,-0.38165,-0.192103,0.189859],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (1.24048,'kcal/mol','+|-',1.64501),
        S298 = (2.92932,'cal/(mol*K)','+|-',0.550979),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "3ring-Cs(BrCdH)-Cd(BrCd)_242",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904522,-0.883729,-0.79682,-0.697731,-0.500443,-0.285519,0.0856742],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (0.732597,'kcal/mol','+|-',1.02682),
        S298 = (3.07337,'cal/(mol*K)','+|-',0.787815),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         8
""",
)

entry(
    index = 119,
    label = "3ring-Cs(ClCdH)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.817538,-0.73994,-0.643428,-0.558089,-0.405507,-0.229105,0.166631],'cal/(mol*K)','+|-',[0.225744,0.248813,0.26484,0.263357,0.221657,0.175787,0.260358]),
        H298 = (0.799395,'kcal/mol','+|-',0.970991),
        S298 = (3.10292,'cal/(mol*K)','+|-',0.74498),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 120,
    label = "3ring-Cs(FCdH)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.922042,-0.759736,-0.58182,-0.439739,-0.238999,-0.0616863,0.317271],'cal/(mol*K)','+|-',[0.238513,0.262887,0.279821,0.278254,0.234195,0.18573,0.275086]),
        H298 = (2.18944,'kcal/mol','+|-',1.02592),
        S298 = (2.61167,'cal/(mol*K)','+|-',0.787121),
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
    index = 121,
    label = "3ring-Cs(Val7CdCs)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.064602,0.089031,0.169781,0.182495,0.080586,0.127511,0.32091],'cal/(mol*K)','+|-',[0.73127,0.806001,0.857918,0.853114,0.718032,0.569441,0.843401]),
        H298 = (0.482817,'kcal/mol','+|-',2.50814),
        S298 = (4.5505,'cal/(mol*K)','+|-',5.83782),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "3ring-Cs(BrCdCs)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.345692,0.440369,0.433913,0.396098,0.236099,0.182697,0.190717],'cal/(mol*K)','+|-',[0.73127,0.806001,0.857918,0.853114,0.718032,0.569441,0.843401]),
        H298 = (-0.403946,'kcal/mol','+|-',3.14541),
        S298 = (2.48652,'cal/(mol*K)','+|-',2.41328),
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
    index = 123,
    label = "3ring-Cs(ClCdCs)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.474896,-0.262307,-0.0943508,-0.0311071,-0.0749269,0.0723242,0.451102],'cal/(mol*K)','+|-',[0.604811,0.666618,0.709557,0.705584,0.593862,0.470967,0.69755]),
        H298 = (1.36958,'kcal/mol','+|-',2.60147),
        S298 = (6.61448,'cal/(mol*K)','+|-',1.99595),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 124,
    label = "3ring-Cs(Val7COH)-Cs(Val7Val7CO)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.181174,-0.452358,-1.14822,-1.82247,-1.65683,-1.47628,-0.752567],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (18.761,'kcal/mol','+|-',18.861),
        S298 = (9.26964,'cal/(mol*K)','+|-',1.23168),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "3ring-Cs(BrCOH)-Cs(BrBrCO)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284598,-1.14814,-1.94835,-2.54741,-2.16244,-1.88051,-1.29436],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (12.3439,'kcal/mol','+|-',5.97046),
        S298 = (9.94055,'cal/(mol*K)','+|-',4.58076),
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
    index = 126,
    label = "3ring-Cs(ClCOH)-Cs(ClClCO)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0755714,-0.505997,-1.2508,-2.01474,-1.88965,-1.70113,-0.80753],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (14.3504,'kcal/mol','+|-',5.97046),
        S298 = (9.13831,'cal/(mol*K)','+|-',4.58076),
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
    index = 127,
    label = "3ring-Cs(FCOH)-Cs(FFCO)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    CO  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.75255,0.297064,-0.245502,-0.905259,-0.918396,-0.847185,-0.155812],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (29.5886,'kcal/mol','+|-',5.97046),
        S298 = (8.73006,'cal/(mol*K)','+|-',4.58076),
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
    index = 128,
    label = "3ring-Cs(Val7O2sCd)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.880505,-0.886535,-0.777152,-0.695124,-0.587148,-0.379028,0.0832794],'cal/(mol*K)','+|-',[0.327987,0.361505,0.384791,0.382637,0.32205,0.255404,0.37828]),
        H298 = (1.88345,'kcal/mol','+|-',2.13764),
        S298 = (4.68619,'cal/(mol*K)','+|-',4.22884),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "3ring-Cs(BrO2sCd)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.624841,-0.625789,-0.560264,-0.528588,-0.480058,-0.34059,-0.0110602],'cal/(mol*K)','+|-',[0.327987,0.361505,0.384791,0.382637,0.32205,0.255404,0.37828]),
        H298 = (1.12768,'kcal/mol','+|-',1.41077),
        S298 = (3.19107,'cal/(mol*K)','+|-',1.0824),
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
    index = 130,
    label = "3ring-Cs(ClO2sCd)-Cd(ClCd)_453",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13617,-1.14728,-0.99404,-0.861659,-0.694239,-0.417467,0.177619],'cal/(mol*K)','+|-',[0.655759,0.722772,0.769329,0.765021,0.643887,0.51064,0.756311]),
        H298 = (2.63922,'kcal/mol','+|-',2.82062),
        S298 = (6.18131,'cal/(mol*K)','+|-',2.16408),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 131,
    label = "3ring-Cs(Val7Val7O2s)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.22295,-1.09812,-1.23069,-1.39964,-1.34803,-1.23482,-2.56631],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (5.20511,'kcal/mol','+|-',6.55682),
        S298 = (3.60032,'cal/(mol*K)','+|-',1.59264),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "3ring-Cs(BrBrO2s)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39685,-1.23423,-1.38855,-1.61038,-1.6461,-1.55976,-2.82032],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (3.23854,'kcal/mol','+|-',2.98523),
        S298 = (4.26202,'cal/(mol*K)','+|-',2.29038),
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
    index = 133,
    label = "3ring-Cs(ClClO2s)-Cs(ClClO2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13122,-1.12282,-1.329,-1.495,-1.43477,-1.32466,-2.67968],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (3.38707,'kcal/mol','+|-',2.98523),
        S298 = (3.82241,'cal/(mol*K)','+|-',2.29038),
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
    index = 134,
    label = "3ring-Cs(FFO2s)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.14078,-0.937296,-0.974515,-1.09354,-0.963216,-0.820046,-2.19892],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (8.98972,'kcal/mol','+|-',2.98523),
        S298 = (2.71653,'cal/(mol*K)','+|-',2.29038),
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
    index = 135,
    label = "3ring-Cd(Val7Cd)-Cs(Val7CdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.881367,-0.794468,-0.674023,-0.565186,-0.38165,-0.192103,0.189859],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (1.24048,'kcal/mol','+|-',1.64501),
        S298 = (2.92932,'cal/(mol*K)','+|-',0.550979),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "3ring-Cd(BrCd)-Cs(BrCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.904522,-0.883729,-0.79682,-0.697731,-0.500443,-0.285519,0.0856742],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (0.732597,'kcal/mol','+|-',1.02682),
        S298 = (3.07337,'cal/(mol*K)','+|-',0.787815),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         8
""",
)

entry(
    index = 137,
    label = "3ring-Cd(ClCd)-Cs(ClCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.817538,-0.73994,-0.643428,-0.558089,-0.405507,-0.229105,0.166631],'cal/(mol*K)','+|-',[0.225744,0.248813,0.26484,0.263357,0.221657,0.175787,0.260358]),
        H298 = (0.799395,'kcal/mol','+|-',0.970991),
        S298 = (3.10292,'cal/(mol*K)','+|-',0.74498),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 138,
    label = "3ring-Cd(FCd)-Cs(FCdH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.922042,-0.759736,-0.58182,-0.439739,-0.238999,-0.0616863,0.317271],'cal/(mol*K)','+|-',[0.238513,0.262887,0.279821,0.278254,0.234195,0.18573,0.275086]),
        H298 = (2.18944,'kcal/mol','+|-',1.02592),
        S298 = (2.61167,'cal/(mol*K)','+|-',0.787121),
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
    index = 139,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.276629,-0.350377,-0.329647,-0.30763,-0.25625,-0.124313,0.170625],'cal/(mol*K)','+|-',[0.406461,0.447999,0.476856,0.474186,0.399103,0.316512,0.468787]),
        H298 = (7.45825,'kcal/mol','+|-',4.09661),
        S298 = (2.18235,'cal/(mol*K)','+|-',0.7033),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "3ring-Cs(BrBrCs)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0960961,-0.258711,-0.303876,-0.320898,-0.31965,-0.212733,0.0330053],'cal/(mol*K)','+|-',[0.406461,0.447999,0.476856,0.474186,0.399103,0.316512,0.468787]),
        H298 = (6.26591,'kcal/mol','+|-',1.74831),
        S298 = (2.53036,'cal/(mol*K)','+|-',1.34137),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 141,
    label = "3ring-Cs(ClClCs)-Cs(ClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.354153,-0.452523,-0.426691,-0.402198,-0.339363,-0.187277,0.159793],'cal/(mol*K)','+|-',[0.300139,0.330811,0.352119,0.350148,0.294705,0.233719,0.346161]),
        H298 = (6.28543,'kcal/mol','+|-',1.29099),
        S298 = (2.18953,'cal/(mol*K)','+|-',0.990493),
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
    index = 142,
    label = "3ring-Cs(FFCs)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.379639,-0.339897,-0.258373,-0.199793,-0.109738,0.0270713,0.319077],'cal/(mol*K)','+|-',[0.280395,0.30905,0.328956,0.327115,0.275319,0.218344,0.32339]),
        H298 = (9.8234,'kcal/mol','+|-',1.20606),
        S298 = (1.82717,'cal/(mol*K)','+|-',0.925337),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         10
""",
)

entry(
    index = 143,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.393599,-0.317987,-0.181331,-0.0786616,0.0226712,0.132631,0.387736],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (7.3723,'kcal/mol','+|-',2.84536),
        S298 = (1.85816,'cal/(mol*K)','+|-',0.126176),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "3ring-Cs(BrCsCs)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.23056,-0.226829,-0.145557,-0.073861,0.00277703,0.094243,0.286762],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (6.36631,'kcal/mol','+|-',1.67569),
        S298 = (1.81355,'cal/(mol*K)','+|-',1.28565),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 145,
    label = "3ring-Cs(FCsCs)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556639,-0.409144,-0.217105,-0.0834623,0.0425654,0.171019,0.488709],'cal/(mol*K)','+|-',[0.322932,0.355933,0.37886,0.376739,0.317086,0.251468,0.372449]),
        H298 = (8.37828,'kcal/mol','+|-',1.38903),
        S298 = (1.90277,'cal/(mol*K)','+|-',1.06571),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 146,
    label = "3ring-Cs(Val7CdH)-Cs(Val7CdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.715291,-0.678918,-0.582487,-0.52257,-0.406855,-0.270279,0.264471],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (3.34625,'kcal/mol','+|-',2.77568),
        S298 = (3.57664,'cal/(mol*K)','+|-',0.551878),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "3ring-Cs(BrCdH)-Cs(BrCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01558,-1.02628,-0.934745,-0.850763,-0.620545,-0.393594,0.124572],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (2.38445,'kcal/mol','+|-',1.72353),
        S298 = (3.72842,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 148,
    label = "3ring-Cs(ClCdH)-Cs(ClCdH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.591383,-0.592093,-0.538057,-0.521374,-0.474002,-0.364087,0.199526],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (2.71705,'kcal/mol','+|-',1.72353),
        S298 = (3.74337,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 149,
    label = "3ring-Cs(FCdH)-Cs(FCdH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.538911,-0.41838,-0.274658,-0.195573,-0.126018,-0.0531567,0.469314],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (4.93724,'kcal/mol','+|-',1.72353),
        S298 = (3.25813,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 150,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.400959,-0.780547,-0.876891,-0.898453,-0.831796,-0.612625,-0.0735877],'cal/(mol*K)','+|-',[0.347015,0.382478,0.407114,0.404835,0.340733,0.270221,0.400225]),
        H298 = (8.49054,'kcal/mol','+|-',4.67982),
        S298 = (3.65219,'cal/(mol*K)','+|-',3.1889),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "3ring-Cs(BrBrCs)-Cs(BrBrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32752,-0.943291,-1.22103,-1.35329,-1.35997,-1.11369,-0.486185],'cal/(mol*K)','+|-',[0.347015,0.382478,0.407114,0.404835,0.340733,0.270221,0.400225]),
        H298 = (7.79336,'kcal/mol','+|-',1.49262),
        S298 = (5.28693,'cal/(mol*K)','+|-',1.14519),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 152,
    label = "3ring-Cs(ClClCs)-Cs(ClClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.444959,-0.864023,-0.945181,-0.949606,-0.865941,-0.630401,-0.0261051],'cal/(mol*K)','+|-',[0.299406,0.330003,0.351259,0.349293,0.293985,0.233148,0.345316]),
        H298 = (6.57846,'kcal/mol','+|-',1.28783),
        S298 = (3.56831,'cal/(mol*K)','+|-',0.988074),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         7
""",
)

entry(
    index = 153,
    label = "3ring-Cs(FFCs)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.430399,-0.534327,-0.464462,-0.392462,-0.269477,-0.0937827,0.291527],'cal/(mol*K)','+|-',[0.180748,0.19922,0.212052,0.210865,0.177476,0.140749,0.208464]),
        H298 = (11.0998,'kcal/mol','+|-',0.777453),
        S298 = (2.10134,'cal/(mol*K)','+|-',0.596491),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         11
""",
)

entry(
    index = 154,
    label = "3ring-Cs(Val7CsH)-Cs(Val7CsCs)_72",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.109097,-0.116214,-0.0776052,-0.0531888,-0.0466689,0.0269395,0.288099],'cal/(mol*K)','+|-',[0.273242,0.301165,0.320564,0.318769,0.268295,0.212774,0.31514]),
        H298 = (3.37746,'kcal/mol','+|-',2.84632),
        S298 = (2.61728,'cal/(mol*K)','+|-',0.491328),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "3ring-Cs(BrCsH)-Cs(BrCsCs)_253",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0851238,-0.155831,-0.161762,-0.167469,-0.185279,-0.117513,0.12418],'cal/(mol*K)','+|-',[0.273242,0.301165,0.320564,0.318769,0.268295,0.212774,0.31514]),
        H298 = (2.39732,'kcal/mol','+|-',1.1753),
        S298 = (2.74968,'cal/(mol*K)','+|-',0.90173),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 156,
    label = "3ring-Cs(ClCsH)-Cs(ClCsCs)_417",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00979017,-0.0509049,-0.036096,-0.0141614,-0.0481653,-0.0065526,0.270137],'cal/(mol*K)','+|-',[0.403121,0.444317,0.472937,0.470289,0.395823,0.313911,0.464934]),
        H298 = (2.72521,'kcal/mol','+|-',1.73394),
        S298 = (2.76835,'cal/(mol*K)','+|-',1.33034),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 157,
    label = "3ring-Cs(FCsH)-Cs(FCsCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u1 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.232378,-0.141905,-0.0349576,0.022064,0.0934376,0.204884,0.469979],'cal/(mol*K)','+|-',[0.245087,0.270134,0.287534,0.285924,0.240651,0.19085,0.282668]),
        H298 = (5.00984,'kcal/mol','+|-',1.0542),
        S298 = (2.33382,'cal/(mol*K)','+|-',0.808817),
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
    index = 158,
    label = "3ring-Cs(Val7Cs)-Cs(Val7O2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.621681,-0.478407,-0.349877,-0.250022,-0.120275,0.0038447,0.26526],'cal/(mol*K)','+|-',[0.584848,0.644616,0.686137,0.682296,0.574261,0.455422,0.674527]),
        H298 = (5.40244,'kcal/mol','+|-',1.88749),
        S298 = (1.50479,'cal/(mol*K)','+|-',0.312608),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "3ring-Cs(BrCs)-Cs(BrO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.662147,-0.555145,-0.428997,-0.341754,-0.230288,-0.102402,0.194361],'cal/(mol*K)','+|-',[0.584848,0.644616,0.686137,0.682296,0.574261,0.455422,0.674527]),
        H298 = (4.58656,'kcal/mol','+|-',2.51561),
        S298 = (1.68519,'cal/(mol*K)','+|-',1.93007),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 160,
    label = "3ring-Cs(ClCs)-Cs(ClO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.730745,-0.582157,-0.429314,-0.292964,-0.116339,0.0214841,0.286705],'cal/(mol*K)','+|-',[0.582196,0.641692,0.683026,0.679202,0.571656,0.453357,0.671468]),
        H298 = (5.18476,'kcal/mol','+|-',2.5042),
        S298 = (1.40973,'cal/(mol*K)','+|-',1.92131),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 161,
    label = "3ring-Cs(FCs)-Cs(FO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.47215,-0.297918,-0.191319,-0.115348,-0.0141981,0.092452,0.314713],'cal/(mol*K)','+|-',[0.576669,0.6356,0.676542,0.672754,0.566229,0.449053,0.665094]),
        H298 = (6.43601,'kcal/mol','+|-',2.48043),
        S298 = (1.41946,'cal/(mol*K)','+|-',1.90307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 162,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7CsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.862918,0.362607,0.140656,0.0345744,-0.0310142,0.0391277,0.317151],'cal/(mol*K)','+|-',[0.634647,0.699503,0.744561,0.740392,0.623158,0.494201,0.731962]),
        H298 = (8.98246,'kcal/mol','+|-',6.79707),
        S298 = (3.65738,'cal/(mol*K)','+|-',3.81146),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "3ring-Cs(BrO2sCs)-Cs(BrCsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.643612,0.265239,0.0966499,-0.0313117,-0.147995,-0.110469,0.150322],'cal/(mol*K)','+|-',[0.634647,0.699503,0.744561,0.740392,0.623158,0.494201,0.731962]),
        H298 = (5.79508,'kcal/mol','+|-',2.72981),
        S298 = (3.24766,'cal/(mol*K)','+|-',2.09441),
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
    index = 164,
    label = "3ring-Cs(ClO2sCs)-Cs(ClCsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.4516,0.582084,0.224823,0.0759412,-0.0223387,0.065722,0.439488],'cal/(mol*K)','+|-',[1.26692,1.39639,1.48634,1.47801,1.24398,0.986553,1.46119]),
        H298 = (12.5587,'kcal/mol','+|-',5.44941),
        S298 = (5.73465,'cal/(mol*K)','+|-',4.18098),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 165,
    label = "3ring-Cs(FO2sCs)-Cs(FCsH)_578",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    O2s u0 p2 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.493543,0.240497,0.100494,0.0590936,0.0772911,0.16213,0.361644],'cal/(mol*K)','+|-',[0.627768,0.691921,0.73649,0.732366,0.616403,0.488844,0.724027]),
        H298 = (8.5936,'kcal/mol','+|-',2.70022),
        S298 = (1.98984,'cal/(mol*K)','+|-',2.07171),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 166,
    label = "3ring-Cd(Val7Cd)-Cs(Val7Val7Cd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.940031,-0.898176,-0.75854,-0.627094,-0.419669,-0.221163,0.173],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (1.59231,'kcal/mol','+|-',5.52095),
        S298 = (2.90827,'cal/(mol*K)','+|-',1.61493),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "3ring-Cd(BrCd)-Cs(BrBrCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.873171,-0.934591,-0.858873,-0.755761,-0.5742,-0.387141,-0.0327787],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (-0.35964,'kcal/mol','+|-',1.02682),
        S298 = (3.47923,'cal/(mol*K)','+|-',0.787816),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         7
""",
)

entry(
    index = 168,
    label = "3ring-Cd(FCd)-Cs(FFCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00689,-0.861762,-0.658207,-0.498428,-0.265137,-0.0551843,0.378778],'cal/(mol*K)','+|-',[0.238513,0.262887,0.279821,0.278254,0.234195,0.185731,0.275086]),
        H298 = (3.54426,'kcal/mol','+|-',1.02592),
        S298 = (2.3373,'cal/(mol*K)','+|-',0.787121),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 169,
    label = "3ring-Cs(Val7CsH)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.332525,-0.372189,-0.355951,-0.325772,-0.245264,-0.101378,0.160737],'cal/(mol*K)','+|-',[0.28837,0.317839,0.338312,0.336418,0.28315,0.224554,0.332588]),
        H298 = (6.01675,'kcal/mol','+|-',2.58646),
        S298 = (1.53465,'cal/(mol*K)','+|-',0.251431),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "3ring-Cs(BrCsH)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.346971,-0.464919,-0.501447,-0.48262,-0.380147,-0.225397,0.043951],'cal/(mol*K)','+|-',[0.28837,0.317839,0.338312,0.336418,0.28315,0.224554,0.332588]),
        H298 = (4.92231,'kcal/mol','+|-',1.24037),
        S298 = (1.47817,'cal/(mol*K)','+|-',0.951655),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         9
""",
)

entry(
    index = 171,
    label = "3ring-Cs(ClCsH)-Cs(ClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.361202,-0.396873,-0.365843,-0.343216,-0.277712,-0.126832,0.168133],'cal/(mol*K)','+|-',[0.287692,0.317093,0.337517,0.335628,0.282484,0.224027,0.331806]),
        H298 = (5.68414,'kcal/mol','+|-',1.23745),
        S298 = (1.6787,'cal/(mol*K)','+|-',0.949418),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 172,
    label = "3ring-Cs(FCsH)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.289402,-0.254776,-0.200562,-0.151479,-0.0779337,0.0480944,0.270126],'cal/(mol*K)','+|-',[0.261721,0.288467,0.307048,0.305329,0.256983,0.203803,0.301852]),
        H298 = (7.4438,'kcal/mol','+|-',1.12574),
        S298 = (1.44708,'cal/(mol*K)','+|-',0.863709),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         12
""",
)

entry(
    index = 173,
    label = "3ring-Cs(Val7Cs)-Cs(Val7CsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.676296,-0.619544,-0.444904,-0.319631,-0.190631,-0.002954,0.454603],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (9.39463,'kcal/mol','+|-',7.28876),
        S298 = (2.91485,'cal/(mol*K)','+|-',3.66157),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "3ring-Cs(BrCs)-Cs(BrCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.23056,-0.226829,-0.145557,-0.073861,0.00277703,0.094243,0.286762],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (6.36631,'kcal/mol','+|-',1.67569),
        S298 = (1.81355,'cal/(mol*K)','+|-',1.28565),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 175,
    label = "3ring-Cs(ClCs)-Cs(ClCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.24169,-1.22266,-0.972049,-0.80157,-0.617234,-0.274124,0.588337],'cal/(mol*K)','+|-',[0.818936,0.902625,0.960766,0.955387,0.80411,0.637707,0.944509]),
        H298 = (13.4393,'kcal/mol','+|-',3.52249),
        S298 = (5.02823,'cal/(mol*K)','+|-',2.70258),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 176,
    label = "3ring-Cs(FCs)-Cs(FCsCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.556639,-0.409144,-0.217105,-0.0834623,0.0425654,0.171019,0.488709],'cal/(mol*K)','+|-',[0.322932,0.355933,0.37886,0.376739,0.317086,0.251468,0.372449]),
        H298 = (8.37828,'kcal/mol','+|-',1.38903),
        S298 = (1.90277,'cal/(mol*K)','+|-',1.06571),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 177,
    label = "3ring-Cs(Val7Val7Cd)-Cs(Val7CdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31544,-1.31589,-1.15454,-1.089,-0.890469,-0.626318,0.299021],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (7.04591,'kcal/mol','+|-',5.39935),
        S298 = (6.55945,'cal/(mol*K)','+|-',6.99952),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "3ring-Cs(BrBrCd)-Cs(BrCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.95787,-2.06846,-1.96488,-1.93392,-1.61925,-1.19422,0.0478036],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (5.13695,'kcal/mol','+|-',5.97046),
        S298 = (9.03415,'cal/(mol*K)','+|-',4.58076),
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
    index = 179,
    label = "3ring-Cs(FFCd)-Cs(FCdH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67302,-0.563322,-0.344209,-0.244085,-0.161688,-0.0584151,0.550238],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (8.95487,'kcal/mol','+|-',1.72353),
        S298 = (4.08474,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 180,
    label = "3ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_83",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378271,-0.571299,-0.612529,-0.61028,-0.54719,-0.389276,-0.0255598],'cal/(mol*K)','+|-',[0.220133,0.242629,0.258258,0.256812,0.216148,0.171418,0.253888]),
        H298 = (5.35181,'kcal/mol','+|-',4.67864),
        S298 = (2.91842,'cal/(mol*K)','+|-',0.728442),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "3ring-Cs(BrCsH)-Cs(BrBrCs)_264",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.369235,-0.678769,-0.807667,-0.857273,-0.819367,-0.646032,-0.265096],'cal/(mol*K)','+|-',[0.220133,0.242629,0.258258,0.256812,0.216148,0.171418,0.253888]),
        H298 = (4.04044,'kcal/mol','+|-',0.94686),
        S298 = (3.31055,'cal/(mol*K)','+|-',0.726466),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         11
""",
)

entry(
    index = 182,
    label = "3ring-Cs(ClCsH)-Cs(ClClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347698,-0.540407,-0.594455,-0.604019,-0.567891,-0.424377,-0.0515813],'cal/(mol*K)','+|-',[0.183415,0.202158,0.21518,0.213975,0.180094,0.142825,0.211539]),
        H298 = (3.96235,'kcal/mol','+|-',0.788922),
        S298 = (2.85402,'cal/(mol*K)','+|-',0.60529),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         13
""",
)

entry(
    index = 183,
    label = "3ring-Cs(FCsH)-Cs(FFCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41788,-0.49472,-0.435466,-0.369547,-0.254313,-0.0974198,0.239998],'cal/(mol*K)','+|-',[0.179565,0.197915,0.210663,0.209484,0.176314,0.139827,0.207098]),
        H298 = (8.05265,'kcal/mol','+|-',0.772361),
        S298 = (2.5907,'cal/(mol*K)','+|-',0.592584),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         15
""",
)

entry(
    index = 184,
    label = "3ring-Cs(Val7CsH)-Cs(Val7CsH)_87",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.146742,0.267659,0.337847,0.355505,0.323218,0.314045,0.342951],'cal/(mol*K)','+|-',[0.367617,0.405185,0.431284,0.42887,0.360962,0.286264,0.423987]),
        H298 = (6.72247,'kcal/mol','+|-',3.94069),
        S298 = (2.09797,'cal/(mol*K)','+|-',1.55218),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "3ring-Cs(BrCsH)-Cs(BrCsH)_268",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.209556,0.235238,0.25402,0.225349,0.136124,0.130213,0.198261],'cal/(mol*K)','+|-',[0.367617,0.405185,0.431284,0.42887,0.360962,0.286264,0.423987]),
        H298 = (5.25965,'kcal/mol','+|-',1.58123),
        S298 = (2.94521,'cal/(mol*K)','+|-',1.21318),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 186,
    label = "3ring-Cs(ClCsH)-Cs(ClCsH)_390",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.207972,0.301031,0.327319,0.320825,0.26256,0.255287,0.283369],'cal/(mol*K)','+|-',[0.367005,0.40451,0.430566,0.428155,0.360361,0.285787,0.42328]),
        H298 = (5.94478,'kcal/mol','+|-',1.5786),
        S298 = (1.92723,'cal/(mol*K)','+|-',1.21116),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 187,
    label = "3ring-Cs(FCsH)-Cs(FCsH)_575",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0226973,0.266709,0.432203,0.520342,0.57097,0.556635,0.547222],'cal/(mol*K)','+|-',[0.316492,0.348835,0.371305,0.369226,0.310762,0.246453,0.365022]),
        H298 = (8.96298,'kcal/mol','+|-',1.36133),
        S298 = (1.42146,'cal/(mol*K)','+|-',1.04446),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 188,
    label = "3ring-Cs(Val7Val7O2s)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.66906,-1.8803,-1.88843,-2.07846,-1.86358,-1.70232,-4.80022],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (15.5828,'kcal/mol','+|-',11.1902),
        S298 = (7.31694,'cal/(mol*K)','+|-',3.61923),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "3ring-Cs(BrBrO2s)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.67042,-2.07634,-2.31327,-2.57046,-2.42853,-2.30052,-5.39168],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (11.6265,'kcal/mol','+|-',8.4435),
        S298 = (8.59653,'cal/(mol*K)','+|-',6.47816),
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
    index = 190,
    label = "3ring-Cs(FFO2s)-Cs(FO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.66771,-1.68425,-1.46358,-1.58646,-1.29863,-1.10412,-4.20877],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (19.5392,'kcal/mol','+|-',8.4435),
        S298 = (6.03735,'cal/(mol*K)','+|-',6.47816),
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
    index = 191,
    label = "3ring-Cd(Val7Cd)-Cs(Val7O2sCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.914045,-0.849444,-0.7229,-0.634235,-0.491086,-0.253453,0.207014],'cal/(mol*K)','+|-',[0.327987,0.361505,0.384791,0.382637,0.32205,0.255404,0.37828]),
        H298 = (3.3613,'kcal/mol','+|-',6.31765),
        S298 = (4.4352,'cal/(mol*K)','+|-',3.51893),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "3ring-Cd(BrCd)-Cs(BrO2sCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.624841,-0.625789,-0.560264,-0.528588,-0.480058,-0.34059,-0.0110602],'cal/(mol*K)','+|-',[0.327987,0.361505,0.384791,0.382637,0.32205,0.255404,0.37828]),
        H298 = (1.12768,'kcal/mol','+|-',1.41077),
        S298 = (3.19107,'cal/(mol*K)','+|-',1.0824),
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
    index = 193,
    label = "3ring-Cd(FCd)-Cs(FO2sCd)_642",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20325,-1.0731,-0.885536,-0.739882,-0.502114,-0.166316,0.425089],'cal/(mol*K)','+|-',[0.654981,0.721915,0.768416,0.764114,0.643124,0.510035,0.755414]),
        H298 = (5.59493,'kcal/mol','+|-',2.81727),
        S298 = (5.67933,'cal/(mol*K)','+|-',2.16151),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 194,
    label = "3ring-Cs(Val7Val7O2s)-Cs(Val7O2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.81925,-2.99841,-3.14598,-3.29545,-3.03328,-2.58173,-4.15426],'cal/(mol*K)','+|-',[0.801397,0.883294,0.94019,0.934926,0.786889,0.624049,0.92428]),
        H298 = (9.02558,'kcal/mol','+|-',13.1096),
        S298 = (9.79684,'cal/(mol*K)','+|-',6.84284),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "3ring-Cs(BrBrO2s)-Cs(BrO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.56564,-4.01755,-4.34518,-4.60358,-4.30281,-3.78779,-5.67679],'cal/(mol*K)','+|-',[0.801397,0.883294,0.94019,0.934926,0.786889,0.624049,0.92428]),
        H298 = (7.01073,'kcal/mol','+|-',3.44705),
        S298 = (12.815,'cal/(mol*K)','+|-',2.6447),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 196,
    label = "3ring-Cs(ClClO2s)-Cs(ClO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6549,-1.75176,-1.90425,-2.05585,-1.92752,-1.66207,-2.58795],'cal/(mol*K)','+|-',[0.400698,0.441647,0.470095,0.467463,0.393444,0.312025,0.46214]),
        H298 = (3.71472,'kcal/mol','+|-',1.72352),
        S298 = (6.08001,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 197,
    label = "3ring-Cs(FFO2s)-Cs(FO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.23722,-3.22592,-3.18852,-3.22692,-2.86951,-2.29534,-4.19803],'cal/(mol*K)','+|-',[0.801397,0.883294,0.94019,0.934926,0.786889,0.624049,0.92428]),
        H298 = (16.3513,'kcal/mol','+|-',3.44705),
        S298 = (10.4955,'cal/(mol*K)','+|-',2.6447),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 198,
    label = "3ring-Cs(Val7O2sO2s)-Cs(Val7O2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.28169,-3.19736,-3.39252,-3.52729,-2.99873,-2.43454,-4.71432],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (6.74173,'kcal/mol','+|-',3.48815),
        S298 = (8.75705,'cal/(mol*K)','+|-',2.74768),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "3ring-Cs(BrO2sO2s)-Cs(BrO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.71535,-3.85808,-4.12315,-4.26852,-3.73621,-3.09598,-5.17672],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (5.61636,'kcal/mol','+|-',5.97046),
        S298 = (9.80688,'cal/(mol*K)','+|-',4.58075),
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
    index = 200,
    label = "3ring-Cs(ClO2sO2s)-Cs(ClO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21745,-3.30962,-3.67204,-3.82867,-3.27975,-2.68627,-4.8733],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (5.85805,'kcal/mol','+|-',5.97046),
        S298 = (9.2621,'cal/(mol*K)','+|-',4.58075),
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
    index = 201,
    label = "3ring-Cs(FO2sO2s)-Cs(FO2sH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    O2s u0 p2 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91228,-2.42439,-2.38236,-2.48469,-1.98023,-1.52137,-4.09293],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (8.75077,'kcal/mol','+|-',5.97046),
        S298 = (7.20217,'cal/(mol*K)','+|-',4.58075),
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
    index = 202,
    label = "3ring-Cs(Val7O2s)-Cs(Val7O2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.80105,-2.52358,-2.5097,-2.60455,-2.32973,-1.96021,-3.85161],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (13.6853,'kcal/mol','+|-',12.6106),
        S298 = (7.24648,'cal/(mol*K)','+|-',5.39847),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "3ring-Cs(BrO2s)-Cs(BrO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.20092,-3.17764,-3.39329,-3.62131,-3.35697,-2.95864,-5.26825],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (13.9621,'kcal/mol','+|-',4.56002),
        S298 = (9.87047,'cal/(mol*K)','+|-',3.49861),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 204,
    label = "3ring-Cs(ClO2s)-Cs(ClO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.85628,-1.74337,-1.71556,-1.76619,-1.59895,-1.36098,-2.40878],'cal/(mol*K)','+|-',[0.601048,0.66247,0.705142,0.701194,0.590167,0.468037,0.69321]),
        H298 = (7.2461,'kcal/mol','+|-',2.58529),
        S298 = (4.47782,'cal/(mol*K)','+|-',1.98353),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 205,
    label = "3ring-Cs(FO2s)-Cs(FO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.34595,-2.64974,-2.42024,-2.42614,-2.03326,-1.56102,-3.87779],'cal/(mol*K)','+|-',[0.981507,1.08181,1.15149,1.14505,0.963738,0.764301,1.13201]),
        H298 = (19.8476,'kcal/mol','+|-',4.22176),
        S298 = (7.39115,'cal/(mol*K)','+|-',3.23909),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 206,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7CsH)_94",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.109097,-0.116214,-0.0776052,-0.0531888,-0.0466689,0.0269395,0.288099],'cal/(mol*K)','+|-',[0.273242,0.301165,0.320564,0.318769,0.268295,0.212774,0.31514]),
        H298 = (3.37746,'kcal/mol','+|-',2.84632),
        S298 = (2.61728,'cal/(mol*K)','+|-',0.491328),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "3ring-Cs(BrCsCs)-Cs(BrCsH)_275",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0851238,-0.155831,-0.161762,-0.167469,-0.185279,-0.117513,0.12418],'cal/(mol*K)','+|-',[0.273242,0.301165,0.320564,0.318769,0.268295,0.212774,0.31514]),
        H298 = (2.39732,'kcal/mol','+|-',1.1753),
        S298 = (2.74968,'cal/(mol*K)','+|-',0.90173),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 208,
    label = "3ring-Cs(ClCsCs)-Cs(ClCsH)_466",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00979017,-0.0509049,-0.036096,-0.0141614,-0.0481653,-0.0065526,0.270137],'cal/(mol*K)','+|-',[0.403121,0.444317,0.472937,0.470289,0.395823,0.313911,0.464934]),
        H298 = (2.72521,'kcal/mol','+|-',1.73394),
        S298 = (2.76835,'cal/(mol*K)','+|-',1.33034),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 209,
    label = "3ring-Cs(FCsCs)-Cs(FCsH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u1 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.232378,-0.141905,-0.0349576,0.022064,0.0934376,0.204884,0.469979],'cal/(mol*K)','+|-',[0.245087,0.270134,0.287534,0.285924,0.240651,0.19085,0.282668]),
        H298 = (5.00984,'kcal/mol','+|-',1.0542),
        S298 = (2.33382,'cal/(mol*K)','+|-',0.808817),
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
    index = 210,
    label = "3ring-Cs(Val7CsH)-Cs(Val7O2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.568578,0.252868,0.098572,0.013891,-0.035352,0.0258305,0.255983],'cal/(mol*K)','+|-',[0.634647,0.699503,0.744561,0.740392,0.623158,0.494201,0.731962]),
        H298 = (7.19434,'kcal/mol','+|-',3.9577),
        S298 = (2.61875,'cal/(mol*K)','+|-',1.77883),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "3ring-Cs(BrCsH)-Cs(BrO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.643612,0.265239,0.0966499,-0.0313117,-0.147995,-0.110469,0.150322],'cal/(mol*K)','+|-',[0.634647,0.699503,0.744561,0.740392,0.623158,0.494201,0.731962]),
        H298 = (5.79508,'kcal/mol','+|-',2.72981),
        S298 = (3.24766,'cal/(mol*K)','+|-',2.09441),
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
    index = 212,
    label = "3ring-Cs(FCsH)-Cs(FO2sCs)_645",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    O2s u0 p2 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.493543,0.240497,0.100494,0.0590936,0.0772911,0.16213,0.361644],'cal/(mol*K)','+|-',[0.627768,0.691921,0.73649,0.732366,0.616403,0.488844,0.724027]),
        H298 = (8.5936,'kcal/mol','+|-',2.70022),
        S298 = (1.98984,'cal/(mol*K)','+|-',2.07171),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 213,
    label = "3ring-Cd(Val7Cd)-Cs(Val7CsCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.852149,-0.720647,-0.549832,-0.450337,-0.371878,-0.202987,0.168928],'cal/(mol*K)','+|-',[0.460774,0.507862,0.540575,0.537549,0.452433,0.358806,0.531428]),
        H298 = (2.06808,'kcal/mol','+|-',1.97568),
        S298 = (4.66264,'cal/(mol*K)','+|-',4.81688),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "3ring-Cd(BrCd)-Cs(BrCsCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09773,-0.956008,-0.769949,-0.666568,-0.623615,-0.435425,0.035498],'cal/(mol*K)','+|-',[0.460774,0.507862,0.540575,0.537549,0.452433,0.358806,0.531428]),
        H298 = (1.8627,'kcal/mol','+|-',1.98193),
        S298 = (7.40796,'cal/(mol*K)','+|-',1.52061),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 215,
    label = "3ring-Cd(ClCd)-Cs(ClCsCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.549959,-0.525325,-0.444794,-0.395951,-0.353602,-0.2154,0.0873492],'cal/(mol*K)','+|-',[0.208041,0.229302,0.244072,0.242705,0.204275,0.162002,0.239942]),
        H298 = (1.19907,'kcal/mol','+|-',0.894849),
        S298 = (3.67465,'cal/(mol*K)','+|-',0.686561),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 216,
    label = "3ring-Cd(FCd)-Cs(FCsCd)_567",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.908759,-0.680609,-0.434752,-0.288492,-0.138417,0.0418626,0.383938],'cal/(mol*K)','+|-',[0.199243,0.219604,0.233749,0.232441,0.195636,0.155151,0.229794]),
        H298 = (3.14246,'kcal/mol','+|-',0.857003),
        S298 = (2.9053,'cal/(mol*K)','+|-',0.657524),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 217,
    label = "3ring-Cd(Val7Cd)=Cd(Val7Cd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.103215,-0.208146,-0.159288,-0.216387,-0.35594,-0.372581,-0.087145],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (0.212737,'kcal/mol','+|-',10.3083),
        S298 = (0.021323,'cal/(mol*K)','+|-',0.867216),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "3ring-Cd(BrCd)=Cd(BrCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.167812,-0.148183,-0.025515,-0.0345929,-0.140123,-0.166473,0.0318751],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (-3.51291,'kcal/mol','+|-',1.72353),
        S298 = (-0.474555,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 219,
    label = "3ring-Cd(ClCd)=Cd(ClCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0965403,-0.189876,-0.140102,-0.216777,-0.39488,-0.420213,-0.107372],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (-1.94379,'kcal/mol','+|-',1.72353),
        S298 = (0.209306,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 220,
    label = "3ring-Cd(FCd)=Cd(FCd)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0452922,-0.28638,-0.312246,-0.39779,-0.532816,-0.531056,-0.185938],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (6.09491,'kcal/mol','+|-',1.72353),
        S298 = (0.329218,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 221,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_104",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0483701,-0.211269,-0.214119,-0.241025,-0.299993,-0.235592,0.057364],'cal/(mol*K)','+|-',[0.601048,0.662471,0.705142,0.701195,0.590167,0.468037,0.693211]),
        H298 = (9.86068,'kcal/mol','+|-',6.6493),
        S298 = (3.26437,'cal/(mol*K)','+|-',3.5449),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "3ring-Cs(BrBrCs)-Cs(BrBrCs)_285",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0479605,-0.392251,-0.597132,-0.75175,-0.931863,-0.894849,-0.624572],'cal/(mol*K)','+|-',[0.601048,0.662471,0.705142,0.701195,0.590167,0.468037,0.693211]),
        H298 = (7.77319,'kcal/mol','+|-',2.58529),
        S298 = (3.84211,'cal/(mol*K)','+|-',1.98353),
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
    index = 223,
    label = "3ring-Cs(ClClCs)-Cs(ClClCs)_413",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00445713,-0.235166,-0.240499,-0.274494,-0.339193,-0.235411,0.214861],'cal/(mol*K)','+|-',[0.47347,0.521855,0.55547,0.55236,0.464899,0.368692,0.54607]),
        H298 = (8.11424,'kcal/mol','+|-',2.03654),
        S298 = (4.67587,'cal/(mol*K)','+|-',1.56251),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 224,
    label = "3ring-Cs(FFCs)-Cs(FFCs)_536",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.197528,-0.00638861,0.195275,0.303169,0.371077,0.423484,0.581803],'cal/(mol*K)','+|-',[0.369359,0.407105,0.433328,0.430902,0.362672,0.287621,0.425995]),
        H298 = (13.6946,'kcal/mol','+|-',1.58872),
        S298 = (1.27514,'cal/(mol*K)','+|-',1.21893),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 225,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7O2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.752172,-1.27705,-1.36381,-1.33467,-1.1467,-0.799397,0.087767],'cal/(mol*K)','+|-',[1.04792,1.15501,1.22941,1.22252,1.02895,0.816016,1.2086]),
        H298 = (14.0641,'kcal/mol','+|-',7.32902),
        S298 = (6.21871,'cal/(mol*K)','+|-',3.57653),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "3ring-Cs(BrBrCs)-Cs(BrO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.835696,-1.57802,-1.7729,-1.83274,-1.71121,-1.35722,-0.354062],'cal/(mol*K)','+|-',[1.04792,1.15501,1.22941,1.22252,1.02895,0.816016,1.2086]),
        H298 = (11.4729,'kcal/mol','+|-',4.50741),
        S298 = (7.48321,'cal/(mol*K)','+|-',3.45825),
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
    index = 227,
    label = "3ring-Cs(FFCs)-Cs(FO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.668647,-0.976073,-0.954726,-0.836608,-0.582196,-0.241575,0.529596],'cal/(mol*K)','+|-',[0.5897,0.649963,0.691829,0.687956,0.579024,0.4592,0.680122]),
        H298 = (16.6553,'kcal/mol','+|-',2.53648),
        S298 = (4.95422,'cal/(mol*K)','+|-',1.94608),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 228,
    label = "3ring-Cs(Val7O2sH)-Cs(Val7O2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.3559,-3.56085,-3.80014,-4.0382,-3.7819,-3.25276,-5.12589],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.809669,0.681466,0.540442,0.80045]),
        H298 = (8.86484,'kcal/mol','+|-',6.57516),
        S298 = (11.6114,'cal/(mol*K)','+|-',1.78952),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "3ring-Cs(BrO2sH)-Cs(BrO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.58139,-4.02692,-4.38466,-4.67413,-4.3951,-3.83665,-5.62018],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.809669,0.681466,0.540442,0.80045]),
        H298 = (6.81413,'kcal/mol','+|-',2.98523),
        S298 = (12.3468,'cal/(mol*K)','+|-',2.29038),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 230,
    label = "3ring-Cs(ClO2sH)-Cs(ClO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.43786,-3.62701,-3.88845,-4.18122,-3.96482,-3.44411,-5.27208],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.809669,0.681466,0.540442,0.80045]),
        H298 = (7.12358,'kcal/mol','+|-',2.98523),
        S298 = (11.8721,'cal/(mol*K)','+|-',2.29038),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 231,
    label = "3ring-Cs(FO2sH)-Cs(FO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.04845,-3.02862,-3.12731,-3.25925,-2.98579,-2.47753,-4.48542],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.809669,0.681466,0.540442,0.80045]),
        H298 = (12.6568,'kcal/mol','+|-',2.98523),
        S298 = (10.6152,'cal/(mol*K)','+|-',2.29038),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 232,
    label = "3ring-Cd(Val7CO)=Cd(Val7CO)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.261893,-0.211709,-0.0879294,-0.149913,-0.32812,-0.24497,0.0910339],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (0.705123,'kcal/mol','+|-',6.60997),
        S298 = (-0.387176,'cal/(mol*K)','+|-',0.893566),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "3ring-Cd(BrCO)=Cd(BrCO)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.352591,-0.134774,0.106867,0.0804023,-0.126641,-0.0875674,0.202849],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (-1.7472,'kcal/mol','+|-',2.98523),
        S298 = (-0.896529,'cal/(mol*K)','+|-',2.29038),
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
    index = 234,
    label = "3ring-Cd(ClCO)=Cd(ClCO)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.228205,-0.187607,-0.0787573,-0.151145,-0.325879,-0.23664,0.0885074],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (-0.60101,'kcal/mol','+|-',2.98523),
        S298 = (-0.203454,'cal/(mol*K)','+|-',2.29038),
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
    index = 235,
    label = "3ring-Cd(FCO)=Cd(FCO)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    CO  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.204883,-0.312747,-0.291898,-0.378996,-0.531839,-0.410703,-0.0182547],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (4.46358,'kcal/mol','+|-',2.98523),
        S298 = (-0.061545,'cal/(mol*K)','+|-',2.29038),
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
    index = 236,
    label = "3ring-Cs(Val7Cd)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {2,S}
5    Val7 u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37915,-1.20663,-0.979643,-0.775354,-0.470681,-0.185255,0.439017],'cal/(mol*K)','+|-',[0.523205,0.576673,0.613819,0.610382,0.513734,0.407421,0.603432]),
        H298 = (0.328615,'kcal/mol','+|-',1.59982),
        S298 = (3.67256,'cal/(mol*K)','+|-',3.49907),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "3ring-Cs(BrCd)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {2,S}
5    Br1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.957421,-0.925553,-0.812704,-0.695414,-0.476832,-0.271059,0.0802761],'cal/(mol*K)','+|-',[0.523205,0.576673,0.613819,0.610382,0.513734,0.407421,0.603432]),
        H298 = (0.608124,'kcal/mol','+|-',2.25046),
        S298 = (3.34308,'cal/(mol*K)','+|-',1.72664),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 238,
    label = "3ring-Cs(ClCd)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05081,-1.78854,-1.46623,-1.17285,-0.734731,-0.289276,0.746707],'cal/(mol*K)','+|-',[0.880814,0.970826,1.03336,1.02757,0.864868,0.685891,1.01587]),
        H298 = (-0.573543,'kcal/mol','+|-',3.78865),
        S298 = (5.56341,'cal/(mol*K)','+|-',2.90679),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 239,
    label = "3ring-Cs(FCd)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {2,S}
5    F1s u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12921,-0.905788,-0.659994,-0.457799,-0.200481,0.00456938,0.490068],'cal/(mol*K)','+|-',[0.425872,0.469393,0.499628,0.496831,0.418162,0.331627,0.491174]),
        H298 = (0.951265,'kcal/mol','+|-',1.8318),
        S298 = (2.11119,'cal/(mol*K)','+|-',1.40543),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 240,
    label = "3ring-Cs(Val7O2sCd)-Cd(Val7Cd)_112",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.8331,-1.57739,-1.18687,-0.90805,-0.606117,-0.265325,0.359608],'cal/(mol*K)','+|-',[1.53526,1.69215,1.80114,1.79106,1.50746,1.19551,1.77067]),
        H298 = (4.0164,'kcal/mol','+|-',5.13266),
        S298 = (5.40209,'cal/(mol*K)','+|-',1.7622),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "3ring-Cs(BrO2sCd)-Cd(BrCd)_293",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.82872,-1.61622,-1.24659,-1.03451,-0.824553,-0.51252,0.155137],'cal/(mol*K)','+|-',[1.53526,1.69215,1.80114,1.79106,1.50746,1.19551,1.77067]),
        H298 = (2.38496,'kcal/mol','+|-',6.6036),
        S298 = (6.06055,'cal/(mol*K)','+|-',5.06652),
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
    index = 242,
    label = "3ring-Cs(ClO2sCd)-Cd(ClCd)_470",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.70519,-1.57545,-1.18501,-0.875499,-0.56192,-0.241428,0.344842],'cal/(mol*K)','+|-',[1.53516,1.69205,1.80104,1.79095,1.50737,1.19543,1.77056]),
        H298 = (2.68973,'kcal/mol','+|-',6.6032),
        S298 = (5.74454,'cal/(mol*K)','+|-',5.06622),
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
    index = 243,
    label = "3ring-Cs(FO2sCd)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.9654,-1.54049,-1.12902,-0.814142,-0.431879,-0.0420279,0.578846],'cal/(mol*K)','+|-',[1.53483,1.69168,1.80065,1.79057,1.50705,1.19518,1.77018]),
        H298 = (6.97452,'kcal/mol','+|-',6.60177),
        S298 = (4.40117,'cal/(mol*K)','+|-',5.06512),
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
    index = 244,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_116",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0528729,0.0844258,0.22232,0.263995,0.252028,0.279533,0.445992],'cal/(mol*K)','+|-',[0.38845,0.428147,0.455725,0.453174,0.381418,0.302487,0.448014]),
        H298 = (11.4287,'kcal/mol','+|-',19.9423),
        S298 = (3.41868,'cal/(mol*K)','+|-',1.59239),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "3ring-Cs(BrBrCs)-Cs(BrCsH)_297",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.18112,0.0419643,-0.0177598,-0.0815083,-0.172199,-0.144483,0.0120179],'cal/(mol*K)','+|-',[0.38845,0.428147,0.455725,0.453174,0.381418,0.302487,0.448014]),
        H298 = (5.70474,'kcal/mol','+|-',1.67084),
        S298 = (4.21485,'cal/(mol*K)','+|-',1.28193),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 246,
    label = "3ring-Cs(ClClCs)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0328703,0.065607,0.117562,0.104597,0.0207608,0.0260465,0.189919],'cal/(mol*K)','+|-',[0.400668,0.441614,0.470059,0.467428,0.393415,0.312001,0.462105]),
        H298 = (5.63899,'kcal/mol','+|-',1.72339),
        S298 = (2.62246,'cal/(mol*K)','+|-',1.32225),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 247,
    label = "3ring-Cs(FFCs)-Cs(FCsH)_586",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.372609,0.145706,0.567158,0.768895,0.907523,0.957037,1.13604],'cal/(mol*K)','+|-',[0.677779,0.747043,0.795162,0.79071,0.665509,0.527788,0.781707]),
        H298 = (22.9423,'kcal/mol','+|-',2.91533),
        S298 = (3.41873,'cal/(mol*K)','+|-',2.23675),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 248,
    label = "3ring-Cs(Val7O2sH)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.96247,-2.29277,-2.35941,-2.55313,-2.28933,-2.06356,-5.06534],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (12.2439,'kcal/mol','+|-',3.5971),
        S298 = (5.39685,'cal/(mol*K)','+|-',1.31368),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "3ring-Cs(BrO2sH)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.98445,-2.38215,-2.6184,-2.86367,-2.63963,-2.41385,-5.41919],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (10.9753,'kcal/mol','+|-',8.4435),
        S298 = (5.81384,'cal/(mol*K)','+|-',6.47816),
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
    index = 250,
    label = "3ring-Cs(ClO2sH)-Cs(ClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.50283,-2.836,-2.81594,-2.96865,-2.62816,-2.33508,-5.14388],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (11.4542,'kcal/mol','+|-',8.4435),
        S298 = (5.73702,'cal/(mol*K)','+|-',6.47816),
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
    index = 251,
    label = "3ring-Cs(FO2sH)-Cs(FO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.40014,-1.66015,-1.64388,-1.82708,-1.6002,-1.44175,-4.63294],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (14.3022,'kcal/mol','+|-',8.4435),
        S298 = (4.6397,'cal/(mol*K)','+|-',6.47816),
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
    index = 252,
    label = "3ring-Cs(Val7O2sO2s)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.97643,-2.91884,-3.11691,-3.23371,-2.7325,-2.2166,-4.54121],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (9.21057,'kcal/mol','+|-',8.42494),
        S298 = (9.22503,'cal/(mol*K)','+|-',3.1476),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "3ring-Cs(BrO2sO2s)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.40589,-3.56645,-3.80544,-3.95295,-3.50302,-2.9758,-5.18084],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (6.51728,'kcal/mol','+|-',5.97046),
        S298 = (10.4869,'cal/(mol*K)','+|-',4.58076),
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
    index = 254,
    label = "3ring-Cs(ClO2sO2s)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.79126,-2.94418,-3.33833,-3.51229,-3.03421,-2.50861,-4.77351],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (7.04943,'kcal/mol','+|-',5.97046),
        S298 = (9.72662,'cal/(mol*K)','+|-',4.58076),
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
    index = 255,
    label = "3ring-Cs(FO2sO2s)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.73213,-2.2459,-2.20696,-2.2359,-1.66027,-1.16538,-3.66927],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62846,1.61934,1.36293,1.08088,1.6009]),
        H298 = (14.065,'kcal/mol','+|-',5.97046),
        S298 = (7.46157,'cal/(mol*K)','+|-',4.58076),
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
    index = 256,
    label = "3ring-Cd(Val7Cd)-Cs(Val7CdCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.520754,-0.137994,0.091975,0.180572,0.202828,0.328983,0.573685],'cal/(mol*K)','+|-',[0.73127,0.806001,0.857918,0.853114,0.718032,0.569441,0.843401]),
        H298 = (2.47313,'kcal/mol','+|-',8.13759),
        S298 = (3.65917,'cal/(mol*K)','+|-',3.31676),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "3ring-Cd(BrCd)-Cs(BrCdCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.345692,0.440369,0.433913,0.396098,0.236099,0.182697,0.190717],'cal/(mol*K)','+|-',[0.73127,0.806001,0.857918,0.853114,0.718032,0.569441,0.843401]),
        H298 = (-0.403946,'kcal/mol','+|-',3.14541),
        S298 = (2.48652,'cal/(mol*K)','+|-',2.41328),
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
    index = 258,
    label = "3ring-Cd(FCd)-Cs(FCdCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u1 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3872,-0.716357,-0.249963,-0.0349542,0.169558,0.47527,0.956653],'cal/(mol*K)','+|-',[0.535946,0.590716,0.628766,0.625246,0.526244,0.417342,0.618126]),
        H298 = (5.3502,'kcal/mol','+|-',2.30527),
        S298 = (4.83182,'cal/(mol*K)','+|-',1.76868),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 259,
    label = "3ring-Cd(Val7Cd)-Cs(Val7Cd)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04332,-0.91567,-0.736349,-0.576606,-0.338656,-0.133245,0.285172],'cal/(mol*K)','+|-',[0.523205,0.576673,0.613819,0.610382,0.513734,0.407421,0.603432]),
        H298 = (0.779695,'kcal/mol','+|-',0.485275),
        S298 = (2.72714,'cal/(mol*K)','+|-',1.74216),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "3ring-Cd(BrCd)-Cs(BrCd)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.957421,-0.925553,-0.812704,-0.695414,-0.476832,-0.271059,0.0802761],'cal/(mol*K)','+|-',[0.523205,0.576673,0.613819,0.610382,0.513734,0.407421,0.603432]),
        H298 = (0.608124,'kcal/mol','+|-',2.25046),
        S298 = (3.34308,'cal/(mol*K)','+|-',1.72664),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 261,
    label = "3ring-Cd(FCd)-Cs(FCd)",
    group = 
"""
1 *2 Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.12921,-0.905788,-0.659994,-0.457799,-0.200481,0.00456938,0.490068],'cal/(mol*K)','+|-',[0.425872,0.469393,0.499628,0.496831,0.418162,0.331627,0.491174]),
        H298 = (0.951265,'kcal/mol','+|-',1.8318),
        S298 = (2.11119,'cal/(mol*K)','+|-',1.40543),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 262,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.857855,0.851297,0.744356,0.502685,0.0831184,0.025064,0.498125],'cal/(mol*K)','+|-',[1.61395,1.77889,1.89347,1.88287,1.58473,1.25679,1.86143]),
        H298 = (8.39287,'kcal/mol','+|-',3.10228),
        S298 = (4.54631,'cal/(mol*K)','+|-',4.96571),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "3ring-Cs(BrCsCs)-Cs(BrBrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.82074,1.78461,1.45558,0.924067,0.0451603,-0.195846,0.367904],'cal/(mol*K)','+|-',[1.61395,1.77889,1.89347,1.88287,1.58473,1.25679,1.86143]),
        H298 = (10.0137,'kcal/mol','+|-',6.9421),
        S298 = (6.79024,'cal/(mol*K)','+|-',5.32623),
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
    index = 264,
    label = "3ring-Cs(ClCsCs)-Cs(ClClCs)_459",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.700989,0.614197,0.504987,0.274942,-0.146171,-0.167671,0.460179],'cal/(mol*K)','+|-',[1.17645,1.29667,1.38019,1.37247,1.15515,0.916101,1.35684]),
        H298 = (6.92237,'kcal/mol','+|-',5.06025),
        S298 = (4.96972,'cal/(mol*K)','+|-',3.88241),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 265,
    label = "3ring-Cs(FCsCs)-Cs(FFCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0518363,0.155084,0.272501,0.309046,0.350366,0.438709,0.666291],'cal/(mol*K)','+|-',[0.413433,0.455683,0.485035,0.482319,0.405948,0.321941,0.476827]),
        H298 = (8.24253,'kcal/mol','+|-',1.7783),
        S298 = (1.87898,'cal/(mol*K)','+|-',1.36438),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 266,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7CsH)_138",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.436187,-0.518008,-0.475131,-0.430801,-0.367708,-0.231508,0.143791],'cal/(mol*K)','+|-',[0.181042,0.199543,0.212396,0.211207,0.177764,0.140977,0.208802]),
        H298 = (3.92932,'kcal/mol','+|-',2.70925),
        S298 = (2.99314,'cal/(mol*K)','+|-',0.559288),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "3ring-Cs(BrCsCs)-Cs(BrCsH)_319",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.432595,-0.550928,-0.551879,-0.532868,-0.482725,-0.359799,-0.024179],'cal/(mol*K)','+|-',[0.181042,0.199543,0.212396,0.211207,0.177764,0.140977,0.208802]),
        H298 = (2.99563,'kcal/mol','+|-',0.778715),
        S298 = (2.91945,'cal/(mol*K)','+|-',0.597458),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         8
""",
)

entry(
    index = 268,
    label = "3ring-Cs(ClCsCs)-Cs(ClCsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.40627,-0.532866,-0.523301,-0.512252,-0.492881,-0.352207,0.077302],'cal/(mol*K)','+|-',[0.176464,0.194497,0.207026,0.205866,0.173269,0.137413,0.203522]),
        H298 = (3.30934,'kcal/mol','+|-',0.759025),
        S298 = (3.30225,'cal/(mol*K)','+|-',0.582352),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         9
""",
)

entry(
    index = 269,
    label = "3ring-Cs(FCsCs)-Cs(FCsH)_554",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469696,-0.47023,-0.350213,-0.247283,-0.127519,0.0174823,0.378251],'cal/(mol*K)','+|-',[0.175714,0.19367,0.206145,0.204991,0.172533,0.136828,0.202657]),
        H298 = (5.48298,'kcal/mol','+|-',0.755797),
        S298 = (2.75772,'cal/(mol*K)','+|-',0.579875),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 270,
    label = "3ring-Cd(Val7Cd)-Cs(Val7CsCd)_140",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.01452,-1.48187,-0.913988,-0.558706,-0.303593,-0.0197135,0.557986],'cal/(mol*K)','+|-',[1.08428,1.19509,1.27207,1.26495,1.06465,0.844333,1.25054]),
        H298 = (7.58092,'kcal/mol','+|-',9.04668),
        S298 = (4.99911,'cal/(mol*K)','+|-',2.27045),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "3ring-Cd(BrCd)-Cs(BrCsCd)_321",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.60803,-1.21083,-0.825857,-0.586766,-0.447257,-0.247511,0.19339],'cal/(mol*K)','+|-',[1.08428,1.19509,1.27207,1.26495,1.06465,0.844333,1.25054]),
        H298 = (4.38243,'kcal/mol','+|-',4.66383),
        S298 = (5.80183,'cal/(mol*K)','+|-',3.57826),
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
    index = 272,
    label = "3ring-Cd(FCd)-Cs(FCsCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.42102,-1.75291,-1.00212,-0.530647,-0.159929,0.208084,0.922582],'cal/(mol*K)','+|-',[0.800293,0.882077,0.938894,0.933638,0.785805,0.623189,0.923007]),
        H298 = (10.7794,'kcal/mol','+|-',3.4423),
        S298 = (4.19638,'cal/(mol*K)','+|-',2.64106),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 273,
    label = "3ring-Cs(Val7O2sCd)-Cd(Val7Cd)_141",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u1 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.298079,-0.667772,-0.800402,-0.91723,-1.15983,-1.1117,-0.6732],'cal/(mol*K)','+|-',[1.53526,1.69215,1.80114,1.79106,1.50746,1.19551,1.77067]),
        H298 = (-6.18749,'kcal/mol','+|-',8.75277),
        S298 = (9.25092,'cal/(mol*K)','+|-',2.97063),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "3ring-Cs(BrO2sCd)-Cd(BrCd)_322",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u1 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0858446,-0.566321,-0.775345,-0.980863,-1.35626,-1.37032,-0.959344],'cal/(mol*K)','+|-',[1.53526,1.69215,1.80114,1.79106,1.50746,1.19551,1.77067]),
        H298 = (-9.28206,'kcal/mol','+|-',6.6036),
        S298 = (10.3012,'cal/(mol*K)','+|-',5.06652),
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
    index = 275,
    label = "3ring-Cs(ClO2sCd)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u1 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.510313,-0.769223,-0.825459,-0.853597,-0.963408,-0.853086,-0.387056],'cal/(mol*K)','+|-',[0.902974,0.995251,1.05936,1.05343,0.886627,0.703147,1.04143]),
        H298 = (-3.09292,'kcal/mol','+|-',3.88396),
        S298 = (8.20065,'cal/(mol*K)','+|-',2.97992),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 276,
    label = "3ring-Cd(Val7Cs)=Cd(Val7Cs)_145",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.149702,-0.00928587,-0.208424,-0.294529,-0.323038,-0.302611,-0.48879],'cal/(mol*K)','+|-',[1.06299,1.17162,1.24708,1.2401,1.04374,0.82775,1.22598]),
        H298 = (5.871,'kcal/mol','+|-',7.9195),
        S298 = (2.39025,'cal/(mol*K)','+|-',1.83595),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "3ring-Cd(BrCs)=Cd(BrCs)_326",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.121855,-0.180164,-0.298643,-0.308185,-0.255173,-0.176279,-0.109881],'cal/(mol*K)','+|-',[1.06299,1.17162,1.24708,1.2401,1.04374,0.82775,1.22598]),
        H298 = (2.04678,'kcal/mol','+|-',4.57223),
        S298 = (1.33095,'cal/(mol*K)','+|-',3.50798),
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
    index = 278,
    label = "3ring-Cd(ClCs)=Cd(ClCs)_392",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.40631,0.208244,-0.0524293,-0.209686,-0.333781,-0.373137,-0.722125],'cal/(mol*K)','+|-',[0.633216,0.697926,0.742881,0.738722,0.621752,0.493086,0.730311]),
        H298 = (5.61261,'kcal/mol','+|-',2.72365),
        S298 = (2.88687,'cal/(mol*K)','+|-',2.08968),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 279,
    label = "3ring-Cd(FCs)=Cd(FCs)_560",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.164652,-0.0559376,-0.2742,-0.365715,-0.380159,-0.358417,-0.634364],'cal/(mol*K)','+|-',[0.622519,0.686136,0.730332,0.726243,0.61125,0.484757,0.717974]),
        H298 = (9.95362,'kcal/mol','+|-',2.67764),
        S298 = (2.95293,'cal/(mol*K)','+|-',2.05439),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 280,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.638862,-0.207314,-0.51905,-0.658638,-0.707752,-0.534431,0.116301],'cal/(mol*K)','+|-',[0.770471,0.849207,0.903907,0.898847,0.756523,0.599967,0.888612]),
        H298 = (11.4958,'kcal/mol','+|-',12.6004),
        S298 = (6.44777,'cal/(mol*K)','+|-',4.37517),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "3ring-Cs(BrO2sCs)-Cs(BrBrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.541777,-0.133492,-0.398226,-0.535352,-0.606504,-0.511246,-0.111961],'cal/(mol*K)','+|-',[0.770471,0.849207,0.903907,0.898847,0.756523,0.599967,0.888612]),
        H298 = (7.0409,'kcal/mol','+|-',3.31403),
        S298 = (4.90091,'cal/(mol*K)','+|-',2.54264),
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
    index = 282,
    label = "3ring-Cs(ClO2sCs)-Cs(ClClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.735947,-0.281136,-0.639874,-0.781925,-0.809,-0.557615,0.344563],'cal/(mol*K)','+|-',[1.5247,1.68051,1.78876,1.77875,1.4971,1.18729,1.75849]),
        H298 = (15.9507,'kcal/mol','+|-',6.55819),
        S298 = (7.99462,'cal/(mol*K)','+|-',5.03169),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 283,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.621681,-0.478407,-0.349877,-0.250022,-0.120275,0.0038447,0.26526],'cal/(mol*K)','+|-',[0.584848,0.644616,0.686137,0.682296,0.574261,0.455422,0.674527]),
        H298 = (5.40244,'kcal/mol','+|-',1.88749),
        S298 = (1.50479,'cal/(mol*K)','+|-',0.312608),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "3ring-Cs(BrO2sCs)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.662147,-0.555145,-0.428997,-0.341754,-0.230288,-0.102402,0.194361],'cal/(mol*K)','+|-',[0.584848,0.644616,0.686137,0.682296,0.574261,0.455422,0.674527]),
        H298 = (4.58656,'kcal/mol','+|-',2.51561),
        S298 = (1.68519,'cal/(mol*K)','+|-',1.93007),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 285,
    label = "3ring-Cs(ClO2sCs)-Cs(ClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.730745,-0.582157,-0.429314,-0.292964,-0.116339,0.0214841,0.286705],'cal/(mol*K)','+|-',[0.582196,0.641692,0.683026,0.679202,0.571656,0.453357,0.671468]),
        H298 = (5.18476,'kcal/mol','+|-',2.5042),
        S298 = (1.40973,'cal/(mol*K)','+|-',1.92131),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 286,
    label = "3ring-Cs(FO2sCs)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.47215,-0.297918,-0.191319,-0.115348,-0.0141981,0.092452,0.314713],'cal/(mol*K)','+|-',[0.576669,0.6356,0.676542,0.672754,0.566229,0.449053,0.665094]),
        H298 = (6.43601,'kcal/mol','+|-',2.48043),
        S298 = (1.41946,'cal/(mol*K)','+|-',1.90307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 287,
    label = "3ring-Cs(Val7COH)-Cs(Val7COH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.152471,-0.102411,-0.465734,-0.807531,-0.718886,-0.656814,-0.346974],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (7.15967,'kcal/mol','+|-',4.38206),
        S298 = (3.34818,'cal/(mol*K)','+|-',0.523142),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "3ring-Cs(BrCOH)-Cs(BrCOH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.256753,-0.557636,-0.872113,-1.14323,-0.966413,-0.864251,-0.487313],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (5.68971,'kcal/mol','+|-',2.98523),
        S298 = (3.4975,'cal/(mol*K)','+|-',2.29038),
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
    index = 289,
    label = "3ring-Cs(ClCOH)-Cs(ClCOH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.18186,-0.0774975,-0.445446,-0.82509,-0.782155,-0.723086,-0.401579],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (6.11139,'kcal/mol','+|-',2.98523),
        S298 = (3.50089,'cal/(mol*K)','+|-',2.29038),
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
    index = 290,
    label = "3ring-Cs(FCOH)-Cs(FCOH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    CO  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.532305,0.3279,-0.0796423,-0.454273,-0.408091,-0.383106,-0.15203],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (9.67791,'kcal/mol','+|-',2.98523),
        S298 = (3.04615,'cal/(mol*K)','+|-',2.29038),
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
    index = 291,
    label = "3ring-Cs(Val7O2sH)-Cs(Val7O2sCs)_150",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.87409,-2.99293,-3.2597,-3.49087,-3.2447,-2.83026,-4.98433],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (6.05555,'kcal/mol','+|-',1.46039),
        S298 = (11.7424,'cal/(mol*K)','+|-',1.1458),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "3ring-Cs(BrO2sH)-Cs(BrO2sCs)_331",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.80577,-3.07903,-3.39609,-3.66873,-3.43355,-3.01446,-5.17485],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (5.53923,'kcal/mol','+|-',4.56002),
        S298 = (12.1475,'cal/(mol*K)','+|-',3.49861),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 293,
    label = "3ring-Cs(ClO2sH)-Cs(ClO2sCs)_389",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.9424,-2.90683,-3.12331,-3.31301,-3.05586,-2.64607,-4.79381],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (6.57188,'kcal/mol','+|-',4.56002),
        S298 = (11.3373,'cal/(mol*K)','+|-',3.49861),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 294,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)_152",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.402069,-0.581071,-0.563397,-0.533569,-0.466435,-0.30917,0.116554],'cal/(mol*K)','+|-',[0.411745,0.453823,0.483055,0.48035,0.404291,0.320627,0.474881]),
        H298 = (5.81179,'kcal/mol','+|-',4.07685),
        S298 = (3.66049,'cal/(mol*K)','+|-',1.6773),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "3ring-Cs(BrCsCs)-Cs(BrBrCs)_333",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.309918,-0.598703,-0.664265,-0.684144,-0.680956,-0.566913,-0.17035],'cal/(mol*K)','+|-',[0.411745,0.453823,0.483055,0.48035,0.404291,0.320627,0.474881]),
        H298 = (5.49321,'kcal/mol','+|-',1.77104),
        S298 = (4.60216,'cal/(mol*K)','+|-',1.35881),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 296,
    label = "3ring-Cs(ClCsCs)-Cs(ClClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.387751,-0.582045,-0.590618,-0.584213,-0.544388,-0.390162,0.060055],'cal/(mol*K)','+|-',[0.245512,0.270602,0.288032,0.28642,0.241068,0.191181,0.283158]),
        H298 = (3.95142,'kcal/mol','+|-',1.05602),
        S298 = (3.3853,'cal/(mol*K)','+|-',0.810219),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 297,
    label = "3ring-Cs(FCsCs)-Cs(FFCs)_605",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.508537,-0.562465,-0.435307,-0.332349,-0.17396,0.0295643,0.459956],'cal/(mol*K)','+|-',[0.24057,0.265155,0.282234,0.280654,0.236215,0.187332,0.277458]),
        H298 = (7.99075,'kcal/mol','+|-',1.03476),
        S298 = (2.99401,'cal/(mol*K)','+|-',0.793909),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 298,
    label = "3ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.738161,-0.822891,-0.735364,-0.706066,-0.601127,-0.429676,0.242297],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (6.97175,'kcal/mol','+|-',10.6328),
        S298 = (3.57466,'cal/(mol*K)','+|-',0.425031),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "3ring-Cs(BrBrCd)-Cs(BrBrCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.731226,-0.94314,-0.974298,-0.971481,-0.833216,-0.668017,-0.123252],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (3.2615,'kcal/mol','+|-',2.98523),
        S298 = (3.78992,'cal/(mol*K)','+|-',2.29038),
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
    index = 300,
    label = "3ring-Cs(ClClCd)-Cs(ClClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.804509,-0.908365,-0.825136,-0.816022,-0.741732,-0.561139,0.240794],'cal/(mol*K)','+|-',[0.490754,0.540905,0.575746,0.572523,0.481869,0.382151,0.566004]),
        H298 = (4.59135,'kcal/mol','+|-',2.11088),
        S298 = (3.56906,'cal/(mol*K)','+|-',1.61954),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 301,
    label = "3ring-Cs(FFCd)-Cs(FFCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.678747,-0.617168,-0.406659,-0.330694,-0.228433,-0.059872,0.609349],'cal/(mol*K)','+|-',[0.490754,0.540905,0.575746,0.572523,0.481869,0.382151,0.566004]),
        H298 = (13.0624,'kcal/mol','+|-',2.11088),
        S298 = (3.365,'cal/(mol*K)','+|-',1.61954),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 302,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7CsH)_156",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.446751,-0.647183,-0.666611,-0.640169,-0.538659,-0.35322,0.108834],'cal/(mol*K)','+|-',[0.302785,0.333728,0.355224,0.353235,0.297304,0.235779,0.349213]),
        H298 = (5.26795,'kcal/mol','+|-',3.59592),
        S298 = (3.13909,'cal/(mol*K)','+|-',2.87572),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "3ring-Cs(BrO2sCs)-Cs(BrCsH)_337",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.435218,-0.574827,-0.585069,-0.589052,-0.561489,-0.430836,-0.0132777],'cal/(mol*K)','+|-',[0.302785,0.333728,0.355224,0.353235,0.297304,0.235779,0.349213]),
        H298 = (3.39021,'kcal/mol','+|-',1.30237),
        S298 = (2.44881,'cal/(mol*K)','+|-',0.999226),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 304,
    label = "3ring-Cs(ClO2sCs)-Cs(ClCsH)_468",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.647868,-0.991832,-1.02314,-0.971382,-0.800726,-0.521717,0.140046],'cal/(mol*K)','+|-',[0.605438,0.667309,0.710293,0.706316,0.594477,0.471456,0.698274]),
        H298 = (6.97378,'kcal/mol','+|-',2.60417),
        S298 = (4.79193,'cal/(mol*K)','+|-',1.99802),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 305,
    label = "3ring-Cs(FO2sCs)-Cs(FCsH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    O2s u0 p2 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.257168,-0.374889,-0.391623,-0.360072,-0.253761,-0.107108,0.199735],'cal/(mol*K)','+|-',[0.294078,0.32413,0.345009,0.343077,0.288754,0.228999,0.339171]),
        H298 = (5.43987,'kcal/mol','+|-',1.26492),
        S298 = (2.17653,'cal/(mol*K)','+|-',0.970491),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 306,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7O2sCs)_157",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.624626,0.006523,-0.214599,-0.289209,-0.282654,-0.124179,0.363024],'cal/(mol*K)','+|-',[0.770471,0.849207,0.903907,0.898847,0.756523,0.599967,0.888612]),
        H298 = (14.8179,'kcal/mol','+|-',21.9967),
        S298 = (4.7112,'cal/(mol*K)','+|-',0.536567),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "3ring-Cs(BrBrCs)-Cs(BrO2sCs)_338",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.541777,-0.133492,-0.398226,-0.535352,-0.606504,-0.511246,-0.111961],'cal/(mol*K)','+|-',[0.770471,0.849207,0.903907,0.898847,0.756523,0.599967,0.888612]),
        H298 = (7.0409,'kcal/mol','+|-',3.31403),
        S298 = (4.90091,'cal/(mol*K)','+|-',2.54264),
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
    index = 308,
    label = "3ring-Cs(FFCs)-Cs(FO2sCs)_602",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    O2s u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.707476,0.146538,-0.0309724,-0.0430658,0.0411958,0.262889,0.838009],'cal/(mol*K)','+|-',[1.25744,1.38594,1.47521,1.46695,1.23468,0.97917,1.45025]),
        H298 = (22.5949,'kcal/mol','+|-',5.40863),
        S298 = (4.5215,'cal/(mol*K)','+|-',4.14969),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 309,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)_158",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.182123,-0.0323558,-0.0964185,-0.1369,-0.20165,-0.098238,0.306436],'cal/(mol*K)','+|-',[0.648725,0.71502,0.761077,0.756816,0.636981,0.505163,0.748199]),
        H298 = (6.28277,'kcal/mol','+|-',2.45461),
        S298 = (3.96188,'cal/(mol*K)','+|-',2.62679),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "3ring-Cs(BrBrCs)-Cs(BrCsCs)_339",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.413415,0.0468343,-0.143015,-0.260987,-0.400886,-0.366184,-0.0385242],'cal/(mol*K)','+|-',[0.648725,0.71502,0.761077,0.756816,0.636981,0.505163,0.748199]),
        H298 = (4.93435,'kcal/mol','+|-',2.79036),
        S298 = (3.9056,'cal/(mol*K)','+|-',2.14087),
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
    index = 311,
    label = "3ring-Cs(ClClCs)-Cs(ClCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.205381,-0.0914395,-0.180864,-0.233094,-0.329301,-0.183616,0.388195],'cal/(mol*K)','+|-',[0.970426,1.0696,1.13849,1.13212,0.952858,0.755673,1.11923]),
        H298 = (6.57937,'kcal/mol','+|-',4.1741),
        S298 = (5.30251,'cal/(mol*K)','+|-',3.20252),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 312,
    label = "3ring-Cs(FFCs)-Cs(FCsCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0724262,-0.0524623,0.0346236,0.0833824,0.125238,0.255086,0.569638],'cal/(mol*K)','+|-',[0.346278,0.381665,0.406249,0.403975,0.340009,0.269647,0.399375]),
        H298 = (7.3346,'kcal/mol','+|-',1.48945),
        S298 = (2.67753,'cal/(mol*K)','+|-',1.14276),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 313,
    label = "3ring-Cs(Val7O2sO2s)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.41063,-2.70729,-2.65059,-2.66867,-2.10714,-1.64864,-4.28485],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (13.5163,'kcal/mol','+|-',3.71398),
        S298 = (6.38531,'cal/(mol*K)','+|-',2.25759),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "3ring-Cs(BrO2sO2s)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.48069,-2.99166,-3.11829,-3.21734,-2.74895,-2.29983,-4.91479],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (12.0654,'kcal/mol','+|-',8.4435),
        S298 = (7.20842,'cal/(mol*K)','+|-',6.47816),
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
    index = 315,
    label = "3ring-Cs(ClO2sO2s)-Cs(ClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63985,-3.14713,-3.19278,-3.19843,-2.56085,-2.02708,-4.47371],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (12.8745,'kcal/mol','+|-',8.4435),
        S298 = (6.849,'cal/(mol*K)','+|-',6.47816),
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
    index = 316,
    label = "3ring-Cs(FO2sO2s)-Cs(FO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.11136,-1.98309,-1.6407,-1.59023,-1.01161,-0.619022,-3.46605],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (15.6091,'kcal/mol','+|-',8.4435),
        S298 = (5.09852,'cal/(mol*K)','+|-',6.47816),
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
    index = 317,
    label = "3ring-Cs(Val7Val7CO)-Cs(Val7Val7CO)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.158811,-0.280753,-0.651141,-0.970302,-0.903636,-0.828381,-0.411401],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (12.0355,'kcal/mol','+|-',13.7419),
        S298 = (4.0538,'cal/(mol*K)','+|-',0.932595),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "3ring-Cs(BrBrCO)-Cs(BrBrCO)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0506977,-0.513242,-0.959619,-1.28234,-1.15179,-1.0637,-0.798058],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (7.35232,'kcal/mol','+|-',2.98523),
        S298 = (4.57411,'cal/(mol*K)','+|-',2.29038),
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
    index = 319,
    label = "3ring-Cs(ClClCO)-Cs(ClClCO)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0430368,-0.367071,-0.794554,-1.15573,-1.06877,-0.950185,-0.415343],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (8.83092,'kcal/mol','+|-',2.98523),
        S298 = (3.67368,'cal/(mol*K)','+|-',2.29038),
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
    index = 320,
    label = "3ring-Cs(FFCO)-Cs(FFCO)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    CO  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.3827,0.0380549,-0.19925,-0.472837,-0.490349,-0.471259,-0.020801],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (19.9234,'kcal/mol','+|-',2.98523),
        S298 = (3.91361,'cal/(mol*K)','+|-',2.29038),
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
    index = 321,
    label = "3ring-Cs(Val7O2sH)-Cs(Val7O2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40813,-1.34074,-1.51467,-1.70447,-1.62422,-1.46388,-2.75408],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (2.3225,'kcal/mol','+|-',1.78253),
        S298 = (3.8656,'cal/(mol*K)','+|-',0.770121),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "3ring-Cs(BrO2sH)-Cs(BrO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66062,-1.60668,-1.76947,-1.95767,-1.86528,-1.66696,-2.86079],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (1.81073,'kcal/mol','+|-',2.98523),
        S298 = (4.15488,'cal/(mol*K)','+|-',2.29038),
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
    index = 323,
    label = "3ring-Cs(ClO2sH)-Cs(ClO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    H    u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.51911,-1.4655,-1.63706,-1.80787,-1.703,-1.53279,-2.7918],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (1.80514,'kcal/mol','+|-',2.98523),
        S298 = (4.01338,'cal/(mol*K)','+|-',2.29038),
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
    index = 324,
    label = "3ring-Cs(FO2sH)-Cs(FO2sH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    H   u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04465,-0.950035,-1.13748,-1.34787,-1.30438,-1.19189,-2.60966],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (3.35164,'kcal/mol','+|-',2.98523),
        S298 = (3.42854,'cal/(mol*K)','+|-',2.29038),
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
    index = 325,
    label = "3ring-Cs(Val7Val7Cd)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.14274,-1.11363,-0.97053,-0.835326,-0.605549,-0.350308,0.20774],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (1.26195,'kcal/mol','+|-',4.06818),
        S298 = (3.80049,'cal/(mol*K)','+|-',3.29495),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "3ring-Cs(BrBrCd)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.873171,-0.934591,-0.858873,-0.755761,-0.5742,-0.387141,-0.0327787],'cal/(mol*K)','+|-',[0.238724,0.263119,0.280068,0.2785,0.234402,0.185894,0.275329]),
        H298 = (-0.35964,'kcal/mol','+|-',1.02682),
        S298 = (3.47923,'cal/(mol*K)','+|-',0.787816),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         7
""",
)

entry(
    index = 327,
    label = "3ring-Cs(ClClCd)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54815,-1.54454,-1.39451,-1.25179,-0.977309,-0.6086,0.277221],'cal/(mol*K)','+|-',[0.508223,0.56016,0.596242,0.592904,0.499023,0.395755,0.586153]),
        H298 = (0.601229,'kcal/mol','+|-',2.18602),
        S298 = (5.58493,'cal/(mol*K)','+|-',1.6772),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 328,
    label = "3ring-Cs(FFCd)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00689,-0.861762,-0.658207,-0.498428,-0.265137,-0.0551843,0.378778],'cal/(mol*K)','+|-',[0.238513,0.262887,0.279821,0.278254,0.234195,0.185731,0.275086]),
        H298 = (3.54426,'kcal/mol','+|-',1.02592),
        S298 = (2.3373,'cal/(mol*K)','+|-',0.787121),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         9
""",
)

entry(
    index = 329,
    label = "3ring-Cs(Val7CsH)-Cs(Val7CsCs)_170",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.332126,0.359654,0.372628,0.3312,0.226783,0.219147,0.385667],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (4.0369,'kcal/mol','+|-',4.49467),
        S298 = (2.81628,'cal/(mol*K)','+|-',2.93828),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "3ring-Cs(BrCsH)-Cs(BrCsCs)_351",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Cs   u0 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.552206,0.445171,0.363102,0.254796,0.0590491,0.018891,0.177896],'cal/(mol*K)','+|-',[0.389578,0.429391,0.457049,0.45449,0.382526,0.303365,0.449315]),
        H298 = (2.4478,'kcal/mol','+|-',1.67569),
        S298 = (3.85512,'cal/(mol*K)','+|-',1.28565),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 331,
    label = "3ring-Cs(FCsH)-Cs(FCsCs)_551",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u0 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.112047,0.274138,0.382153,0.407604,0.394517,0.419403,0.593439],'cal/(mol*K)','+|-',[0.342077,0.377035,0.401321,0.399074,0.335884,0.266376,0.39453]),
        H298 = (5.62601,'kcal/mol','+|-',1.47138),
        S298 = (1.77744,'cal/(mol*K)','+|-',1.12889),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 332,
    label = "3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)_171",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.170494,-0.002814,-0.0541957,-0.0888023,-0.137824,-0.055549,0.265557],'cal/(mol*K)','+|-',[0.648725,0.71502,0.761077,0.756816,0.636981,0.505163,0.748199]),
        H298 = (6.13448,'kcal/mol','+|-',3.39447),
        S298 = (3.29156,'cal/(mol*K)','+|-',1.73675),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "3ring-Cs(BrCsCs)-Cs(BrBrCs)_352",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.413415,0.0468343,-0.143015,-0.260987,-0.400886,-0.366184,-0.0385242],'cal/(mol*K)','+|-',[0.648725,0.71502,0.761077,0.756816,0.636981,0.505163,0.748199]),
        H298 = (4.93435,'kcal/mol','+|-',2.79036),
        S298 = (3.9056,'cal/(mol*K)','+|-',2.14087),
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
    index = 334,
    label = "3ring-Cs(FCsCs)-Cs(FFCs)_610",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0724262,-0.0524623,0.0346236,0.0833824,0.125238,0.255086,0.569638],'cal/(mol*K)','+|-',[0.346278,0.381665,0.406249,0.403975,0.340009,0.269647,0.399375]),
        H298 = (7.3346,'kcal/mol','+|-',1.48945),
        S298 = (2.67753,'cal/(mol*K)','+|-',1.14276),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 335,
    label = "3ring-Cs(Val7Val7Cd)-Cd(Val7Cd)_172",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3822,-2.03871,-1.61114,-1.25027,-0.76937,-0.345773,0.491086],'cal/(mol*K)','+|-',[1.46788,1.61788,1.7221,1.71246,1.4413,1.14304,1.69296]),
        H298 = (5.82322,'kcal/mol','+|-',9.20207),
        S298 = (5.0626,'cal/(mol*K)','+|-',2.19013),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "3ring-Cs(BrBrCd)-Cd(BrCd)_353",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.39664,-2.14933,-1.78247,-1.44878,-1.00226,-0.611179,0.0991765],'cal/(mol*K)','+|-',[1.46788,1.61788,1.7221,1.71246,1.4413,1.14304,1.69296]),
        H298 = (2.67903,'kcal/mol','+|-',6.31378),
        S298 = (6.23413,'cal/(mol*K)','+|-',4.84417),
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
    index = 337,
    label = "3ring-Cs(ClClCd)-Cd(ClCd)_482",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19593,-1.93624,-1.53975,-1.23496,-0.834048,-0.430752,0.448288],'cal/(mol*K)','+|-',[1.47817,1.62923,1.73418,1.72447,1.45141,1.15106,1.70483]),
        H298 = (3.68654,'kcal/mol','+|-',6.35807),
        S298 = (4.88891,'cal/(mol*K)','+|-',4.87815),
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
    index = 338,
    label = "3ring-Cs(FFCd)-Cd(FCd)_637",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.55402,-2.03056,-1.51119,-1.06706,-0.471802,0.00461146,0.925794],'cal/(mol*K)','+|-',[1.46774,1.61773,1.72194,1.7123,1.44117,1.14293,1.6928]),
        H298 = (11.1041,'kcal/mol','+|-',6.31319),
        S298 = (4.06476,'cal/(mol*K)','+|-',4.84371),
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
    index = 339,
    label = "3ring-Cs(Val7O2sH)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.71285,-2.50777,-2.81792,-3.13696,-2.95974,-2.67912,-5.33886],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (7.3398,'kcal/mol','+|-',8.14805),
        S298 = (9.55079,'cal/(mol*K)','+|-',2.43735),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "3ring-Cs(BrO2sH)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.07911,-2.89292,-3.28605,-3.63984,-3.49251,-3.1918,-5.71722],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (4.90482,'kcal/mol','+|-',5.97046),
        S298 = (10.5328,'cal/(mol*K)','+|-',4.58075),
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
    index = 341,
    label = "3ring-Cs(ClO2sH)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.74409,-2.60381,-3.0069,-3.33236,-3.15043,-2.86071,-5.47296],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (5.07149,'kcal/mol','+|-',5.97046),
        S298 = (9.93267,'cal/(mol*K)','+|-',4.58075),
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
    index = 342,
    label = "3ring-Cs(FO2sH)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.31536,-2.02657,-2.16082,-2.43868,-2.23627,-1.98484,-4.82641],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (12.0431,'kcal/mol','+|-',5.97046),
        S298 = (8.18691,'cal/(mol*K)','+|-',4.58075),
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
    index = 343,
    label = "3ring-Cs(Val7CsH)-Cs(Val7O2sCs)_178",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.346193,-0.474858,-0.488346,-0.474562,-0.407625,-0.268972,0.0932286],'cal/(mol*K)','+|-',[0.302785,0.333728,0.355224,0.353235,0.297304,0.235779,0.349213]),
        H298 = (4.41504,'kcal/mol','+|-',2.89866),
        S298 = (2.31267,'cal/(mol*K)','+|-',0.385062),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "3ring-Cs(BrCsH)-Cs(BrO2sCs)_359",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    O2s  u0 p2 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.435218,-0.574827,-0.585069,-0.589052,-0.561489,-0.430836,-0.0132777],'cal/(mol*K)','+|-',[0.302785,0.333728,0.355224,0.353235,0.297304,0.235779,0.349213]),
        H298 = (3.39021,'kcal/mol','+|-',1.30237),
        S298 = (2.44881,'cal/(mol*K)','+|-',0.999226),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 345,
    label = "3ring-Cs(FCsH)-Cs(FO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    O2s u0 p2 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.257168,-0.374889,-0.391623,-0.360072,-0.253761,-0.107108,0.199735],'cal/(mol*K)','+|-',[0.294078,0.32413,0.345009,0.343077,0.288754,0.228999,0.339171]),
        H298 = (5.43987,'kcal/mol','+|-',1.26492),
        S298 = (2.17653,'cal/(mol*K)','+|-',0.970491),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 346,
    label = "3ring-Cs(Val7Val7O2s)-Cs(Val7O2sCs)_180",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.83657,-2.86598,-3.10929,-3.33305,-3.02667,-2.57054,-4.69678],'cal/(mol*K)','+|-',[1.60279,1.76659,1.88038,1.86985,1.57378,1.2481,1.84856]),
        H298 = (8.13152,'kcal/mol','+|-',12.0468),
        S298 = (10.3299,'cal/(mol*K)','+|-',2.74804),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "3ring-Cs(BrBrO2s)-Cs(BrO2sCs)_361",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
6    Br1s u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.91527,-3.39992,-3.81843,-4.0907,-3.80315,-3.3532,-5.38901],'cal/(mol*K)','+|-',[1.60279,1.76659,1.88038,1.86985,1.57378,1.2481,1.84856]),
        H298 = (3.85897,'kcal/mol','+|-',6.89409),
        S298 = (11.3068,'cal/(mol*K)','+|-',5.2894),
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
    index = 348,
    label = "3ring-Cs(ClClO2s)-Cs(ClO2sCs)_492",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.78477,-2.76331,-3.03744,-3.28485,-3.038,-2.62422,-4.78507],'cal/(mol*K)','+|-',[1.26712,1.39661,1.48657,1.47825,1.24418,0.986708,1.46142]),
        H298 = (5.5149,'kcal/mol','+|-',5.45026),
        S298 = (10.9242,'cal/(mol*K)','+|-',4.18164),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 349,
    label = "3ring-Cs(FFO2s)-Cs(FO2sCs)_553",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u1 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.80967,-2.43471,-2.47201,-2.6236,-2.23886,-1.73419,-3.91626],'cal/(mol*K)','+|-',[1.13335,1.24917,1.32963,1.32218,1.11283,0.882539,1.30713]),
        H298 = (15.0207,'kcal/mol','+|-',4.87486),
        S298 = (8.75881,'cal/(mol*K)','+|-',3.74017),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 350,
    label = "3ring-Cs(Val7CsCd)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67799,-1.35515,-0.915198,-0.694165,-0.565855,-0.282752,0.34777],'cal/(mol*K)','+|-',[1.06606,1.175,1.25069,1.24368,1.04676,0.830141,1.22952]),
        H298 = (4.5302,'kcal/mol','+|-',4.58544),
        S298 = (5.81413,'cal/(mol*K)','+|-',3.51812),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "3ring-Cs(ClCsCd)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.67799,-1.35515,-0.915198,-0.694165,-0.565855,-0.282752,0.34777],'cal/(mol*K)','+|-',[1.06606,1.175,1.25069,1.24368,1.04676,0.830141,1.22952]),
        H298 = (4.5302,'kcal/mol','+|-',4.58544),
        S298 = (5.81413,'cal/(mol*K)','+|-',3.51812),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 352,
    label = "3ring-Cs(Val7CdH)-Cs(Val7Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.15115,-1.12652,-0.92623,-0.837672,-0.698304,-0.499211,0.506162],'cal/(mol*K)','+|-',[0.981507,1.08181,1.15149,1.14505,0.963738,0.764301,1.13201]),
        H298 = (8.02911,'kcal/mol','+|-',2.61844),
        S298 = (6.38296,'cal/(mol*K)','+|-',6.50035),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "3ring-Cs(ClCdH)-Cs(ClClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.62928,-1.68971,-1.50825,-1.43126,-1.23492,-0.940007,0.462086],'cal/(mol*K)','+|-',[0.981507,1.08181,1.15149,1.14505,0.963738,0.764301,1.13201]),
        H298 = (7.10335,'kcal/mol','+|-',4.22176),
        S298 = (8.68118,'cal/(mol*K)','+|-',3.23909),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 354,
    label = "3ring-Cs(FCdH)-Cs(FFCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67302,-0.563322,-0.344209,-0.244085,-0.161688,-0.0584151,0.550238],'cal/(mol*K)','+|-',[0.400699,0.441647,0.470095,0.467463,0.393445,0.312025,0.46214]),
        H298 = (8.95487,'kcal/mol','+|-',1.72353),
        S298 = (4.08474,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 355,
    label = "3ring-Cd(Val7Cd)-Cs(Val7CdH)_192",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06803,-1.69093,-1.35205,-1.03664,-0.625273,-0.246521,0.532612],'cal/(mol*K)','+|-',[1.45964,1.6088,1.71243,1.70285,1.43322,1.13662,1.68346]),
        H298 = (5.17064,'kcal/mol','+|-',6.27835),
        S298 = (5.53078,'cal/(mol*K)','+|-',4.81698),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "3ring-Cd(ClCd)-Cs(ClCdH)_427",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06803,-1.69093,-1.35205,-1.03664,-0.625273,-0.246521,0.532612],'cal/(mol*K)','+|-',[1.45964,1.6088,1.71243,1.70285,1.43322,1.13662,1.68346]),
        H298 = (5.17064,'kcal/mol','+|-',6.27835),
        S298 = (5.53078,'cal/(mol*K)','+|-',4.81698),
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
    index = 357,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.85628,-1.74337,-1.71556,-1.76619,-1.59895,-1.36098,-2.40878],'cal/(mol*K)','+|-',[0.601048,0.66247,0.705142,0.701194,0.590167,0.468037,0.69321]),
        H298 = (7.2461,'kcal/mol','+|-',2.58529),
        S298 = (4.47782,'cal/(mol*K)','+|-',1.98353),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "3ring-Cs(ClO2sCs)-Cs(ClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.85628,-1.74337,-1.71556,-1.76619,-1.59895,-1.36098,-2.40878],'cal/(mol*K)','+|-',[0.601048,0.66247,0.705142,0.701194,0.590167,0.468037,0.69321]),
        H298 = (7.2461,'kcal/mol','+|-',2.58529),
        S298 = (4.47782,'cal/(mol*K)','+|-',1.98353),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 359,
    label = "3ring-Cs(Val7CsCd)-Cd(Val7Cd)_196",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.729359,-0.602967,-0.439773,-0.342222,-0.246009,-0.0867687,0.235644],'cal/(mol*K)','+|-',[0.208041,0.229302,0.244072,0.242705,0.204275,0.162002,0.239942]),
        H298 = (2.17076,'kcal/mol','+|-',2.74837),
        S298 = (3.28998,'cal/(mol*K)','+|-',1.08803),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "3ring-Cs(ClCsCd)-Cd(ClCd)_446",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.549959,-0.525325,-0.444794,-0.395951,-0.353602,-0.2154,0.0873492],'cal/(mol*K)','+|-',[0.208041,0.229302,0.244072,0.242705,0.204275,0.162002,0.239942]),
        H298 = (1.19907,'kcal/mol','+|-',0.894849),
        S298 = (3.67465,'cal/(mol*K)','+|-',0.686561),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 361,
    label = "3ring-Cs(FCsCd)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.908759,-0.680609,-0.434752,-0.288492,-0.138417,0.0418626,0.383938],'cal/(mol*K)','+|-',[0.199243,0.219604,0.233749,0.232441,0.195636,0.155151,0.229794]),
        H298 = (3.14246,'kcal/mol','+|-',0.857003),
        S298 = (2.9053,'cal/(mol*K)','+|-',0.657524),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         7
""",
)

entry(
    index = 362,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6549,-1.75176,-1.90425,-2.05585,-1.92752,-1.66207,-2.58795],'cal/(mol*K)','+|-',[0.400698,0.441647,0.470095,0.467463,0.393444,0.312025,0.46214]),
        H298 = (3.71472,'kcal/mol','+|-',1.72352),
        S298 = (6.08001,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "3ring-Cs(ClO2sCs)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.6549,-1.75176,-1.90425,-2.05585,-1.92752,-1.66207,-2.58795],'cal/(mol*K)','+|-',[0.400698,0.441647,0.470095,0.467463,0.393444,0.312025,0.46214]),
        H298 = (3.71472,'kcal/mol','+|-',1.72352),
        S298 = (6.08001,'cal/(mol*K)','+|-',1.32235),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 364,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7Val7Cs)_200",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03139,-1.64852,-1.72734,-1.66965,-1.43123,-1.00585,0.133673],'cal/(mol*K)','+|-',[1.04134,1.14776,1.22169,1.21485,1.02249,0.810895,1.20102]),
        H298 = (12.0206,'kcal/mol','+|-',4.47912),
        S298 = (7.49706,'cal/(mol*K)','+|-',3.43655),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "3ring-Cs(ClO2sCs)-Cs(ClClCs)_462",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
6    Cl1s u0 p3 c0 {2,S}
7    O2s  u0 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03139,-1.64852,-1.72734,-1.66965,-1.43123,-1.00585,0.133673],'cal/(mol*K)','+|-',[1.04134,1.14776,1.22169,1.21485,1.02249,0.810895,1.20102]),
        H298 = (12.0206,'kcal/mol','+|-',4.47912),
        S298 = (7.49706,'cal/(mol*K)','+|-',3.43655),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 366,
    label = "3ring-Cs(Val7O2s)-Cs(Val7Val7O2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.98095,-2.42124,-2.54067,-2.68884,-2.38513,-2.14215,-5.03046],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (12.433,'kcal/mol','+|-',8.4435),
        S298 = (8.06536,'cal/(mol*K)','+|-',6.47816),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "3ring-Cs(ClO2s)-Cs(ClClO2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.98095,-2.42124,-2.54067,-2.68884,-2.38513,-2.14215,-5.03046],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (12.433,'kcal/mol','+|-',8.4435),
        S298 = (8.06536,'cal/(mol*K)','+|-',6.47816),
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
    index = 368,
    label = "3ring-Cs(Val7O2sCs)-Cs(Val7O2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Cs   u1 p0 c0 {1,S}
7    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.73127,-2.29551,-2.38609,-2.6533,-2.37791,-1.92241,-4.19327],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (11.8913,'kcal/mol','+|-',4.56002),
        S298 = (8.80564,'cal/(mol*K)','+|-',3.49861),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "3ring-Cs(FO2sCs)-Cs(FO2sH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    Cs  u1 p0 c0 {1,S}
7    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.73127,-2.29551,-2.38609,-2.6533,-2.37791,-1.92241,-4.19327],'cal/(mol*K)','+|-',[1.06015,1.16849,1.24375,1.23679,1.04096,0.825539,1.22271]),
        H298 = (11.8913,'kcal/mol','+|-',4.56002),
        S298 = (8.80564,'cal/(mol*K)','+|-',3.49861),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 370,
    label = "3ring-Cd(Val7Cd)-Cs(Val7O2sCd)_212",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Val7 u0 p3 c0 {1,S}
5    O2s  u1 p2 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.864461,-0.856398,-0.799088,-0.762583,-0.727306,-0.521054,-0.0487449],'cal/(mol*K)','+|-',[0.954294,1.05182,1.11957,1.1133,0.937018,0.743111,1.10062]),
        H298 = (3.6228,'kcal/mol','+|-',4.10471),
        S298 = (6.50665,'cal/(mol*K)','+|-',3.14928),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "3ring-Cd(FCd)-Cs(FO2sCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    O2s u1 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.864461,-0.856398,-0.799088,-0.762583,-0.727306,-0.521054,-0.0487449],'cal/(mol*K)','+|-',[0.954294,1.05182,1.11957,1.1133,0.937018,0.743111,1.10062]),
        H298 = (3.6228,'kcal/mol','+|-',4.10471),
        S298 = (6.50665,'cal/(mol*K)','+|-',3.14928),
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
    index = 372,
    label = "3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)_213",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Val7 u0 p3 c0 {1,S}
5    Val7 u0 p3 c0 {2,S}
6    Val7 u0 p3 c0 {2,S}
7    Cs   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0518363,0.155084,0.272501,0.309046,0.350366,0.438709,0.666291],'cal/(mol*K)','+|-',[0.413433,0.455683,0.485035,0.482319,0.405948,0.321941,0.476827]),
        H298 = (8.24253,'kcal/mol','+|-',1.7783),
        S298 = (1.87898,'cal/(mol*K)','+|-',1.36438),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "3ring-Cs(FFCs)-Cs(FCsCs)_622",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
6    F1s u0 p3 c0 {2,S}
7    Cs  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0518363,0.155084,0.272501,0.309046,0.350366,0.438709,0.666291],'cal/(mol*K)','+|-',[0.413433,0.455683,0.485035,0.482319,0.405948,0.321941,0.476827]),
        H298 = (8.24253,'kcal/mol','+|-',1.7783),
        S298 = (1.87898,'cal/(mol*K)','+|-',1.36438),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 374,
    label = "halogen-4",
    group = 
"""
1 *1 R!H  ux {2,[S,D]} {3,[S,D,T]} {5,S}
2 *2 R!H  ux {1,[S,D]} {4,[S,D,T]} {6,S}
3    R!H  ux {1,[S,D,T]} {4,[S,D,T]}
4    R!H  ux {2,[S,D,T]} {3,[S,D,T]}
5    Val7 u0 {1,S}
6    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """halogen-4""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "4ring-Cd(Val7Cd)-Cd(Val7Cd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0614065,0.0183786,0.0565194,-0.0117102,-0.145414,-0.18341,-0.000162167],'cal/(mol*K)','+|-',[0.512575,0.564957,0.601347,0.597981,0.503296,0.399143,0.591172]),
        H298 = (-0.417057,'kcal/mol','+|-',3.16769),
        S298 = (0.147266,'cal/(mol*K)','+|-',1.18252),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "4ring-Cd(BrCd)-Cd(BrCd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.000971755,0.0368803,0.12,0.0917542,0.00105311,-0.035156,0.0745815],'cal/(mol*K)','+|-',[0.512575,0.564957,0.601347,0.597981,0.503296,0.399143,0.591172]),
        H298 = (-1.48882,'kcal/mol','+|-',2.20474),
        S298 = (-0.395566,'cal/(mol*K)','+|-',1.69156),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 377,
    label = "4ring-Cd(ClCd)-Cd(ClCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0423023,0.0259615,0.0705198,0.0097063,-0.121638,-0.160942,0.015129],'cal/(mol*K)','+|-',[0.512575,0.564957,0.601347,0.597981,0.503296,0.399143,0.591172]),
        H298 = (-1.16455,'kcal/mol','+|-',2.20474),
        S298 = (0.0600909,'cal/(mol*K)','+|-',1.69156),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 378,
    label = "4ring-Cd(FCd)-Cd(FCd)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd  u0 p0 c0 {1,D} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.142889,-0.00770589,-0.0209617,-0.136591,-0.315656,-0.354131,-0.090197],'cal/(mol*K)','+|-',[0.566673,0.624583,0.664815,0.661092,0.556415,0.44127,0.653565]),
        H298 = (1.4022,'kcal/mol','+|-',2.43743),
        S298 = (0.777274,'cal/(mol*K)','+|-',1.87009),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 379,
    label = "4ring-Cd(Val7Cd)=Cd(Val7Cd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0942309,0.0217522,0.0478091,-0.0187155,-0.146555,-0.179875,0.00766643],'cal/(mol*K)','+|-',[0.512575,0.564957,0.601347,0.597981,0.503296,0.399143,0.591172]),
        H298 = (-0.0570933,'kcal/mol','+|-',4.43438),
        S298 = (0.266524,'cal/(mol*K)','+|-',1.23001),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "4ring-Cd(BrCd)=Cd(BrCd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00830067,0.0112,0.0998188,0.0770401,-0.00389147,-0.0324434,0.0849044],'cal/(mol*K)','+|-',[0.512575,0.564957,0.601347,0.597981,0.503296,0.399143,0.591172]),
        H298 = (-1.57804,'kcal/mol','+|-',2.20474),
        S298 = (-0.28751,'cal/(mol*K)','+|-',1.69156),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 381,
    label = "4ring-Cd(ClCd)=Cd(ClCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0620385,-0.00347022,0.0312671,-0.0180505,-0.133203,-0.163562,0.0156229],'cal/(mol*K)','+|-',[0.512575,0.564957,0.601347,0.597981,0.503296,0.399143,0.591172]),
        H298 = (-1.08015,'kcal/mol','+|-',2.20474),
        S298 = (0.158809,'cal/(mol*K)','+|-',1.69156),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 382,
    label = "4ring-Cd(FCd)=Cd(FCd)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd  u0 p0 c0 {2,S} {4,D}
4    Cd  u0 p0 c0 {1,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.228955,0.0575269,0.0123413,-0.115136,-0.30257,-0.34362,-0.077528],'cal/(mol*K)','+|-',[0.566673,0.624583,0.664815,0.661092,0.556415,0.44127,0.653565]),
        H298 = (2.48691,'kcal/mol','+|-',2.43743),
        S298 = (0.928272,'cal/(mol*K)','+|-',1.87009),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 383,
    label = "4ring-Cs(Val7CdH)-Cs(Val7CdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21576,-0.764224,-0.499939,-0.455525,-0.323792,-0.16261,0.638455],'cal/(mol*K)','+|-',[1.56618,1.72623,1.83743,1.82714,1.53783,1.21959,1.80633]),
        H298 = (1.21492,'kcal/mol','+|-',0.975236),
        S298 = (2.9582,'cal/(mol*K)','+|-',2.07724),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "4ring-Cs(BrCdH)-Cs(BrCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.66918,-1.39385,-1.14386,-1.11044,-0.951001,-0.653044,0.374842],'cal/(mol*K)','+|-',[1.56618,1.72623,1.83743,1.82714,1.53783,1.21959,1.80633]),
        H298 = (1.68194,'kcal/mol','+|-',6.73662),
        S298 = (4.12428,'cal/(mol*K)','+|-',5.16858),
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
    index = 385,
    label = "4ring-Cs(ClCdH)-Cs(ClCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.03696,-0.552701,-0.337288,-0.296956,-0.199023,-0.132943,0.577493],'cal/(mol*K)','+|-',[1.82383,2.01022,2.1397,2.12772,1.79082,1.42022,2.1035]),
        H298 = (0.709031,'kcal/mol','+|-',7.84486),
        S298 = (2.13241,'cal/(mol*K)','+|-',6.01887),
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
    index = 386,
    label = "4ring-Cs(FCdH)-Cs(FCdH)_627",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.941128,-0.346121,-0.0186681,0.0408204,0.178647,0.298156,0.963029],'cal/(mol*K)','+|-',[1.53272,1.68936,1.79817,1.78811,1.50498,1.19354,1.76775]),
        H298 = (1.25379,'kcal/mol','+|-',6.59271),
        S298 = (2.61791,'cal/(mol*K)','+|-',5.05817),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 387,
    label = "4ring-Cd(Val7Cs)=Cd(Val7Cs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0765401,-0.16396,-0.233449,-0.261454,-0.2366,-0.162411,-0.0697041],'cal/(mol*K)','+|-',[0.466403,0.514066,0.547179,0.544115,0.45796,0.363189,0.53792]),
        H298 = (1.28297,'kcal/mol','+|-',3.00431),
        S298 = (1.15673,'cal/(mol*K)','+|-',0.747807),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "4ring-Cd(BrCs)=Cd(BrCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0405581,-0.112825,-0.233873,-0.280894,-0.28694,-0.219125,-0.147696],'cal/(mol*K)','+|-',[0.466403,0.514066,0.547179,0.544115,0.45796,0.363189,0.53792]),
        H298 = (0.301693,'kcal/mol','+|-',2.00614),
        S298 = (1.47599,'cal/(mol*K)','+|-',1.53918),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 389,
    label = "4ring-Cd(ClCs)=Cd(ClCs)_435",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00940152,-0.0576765,-0.120759,-0.182765,-0.222019,-0.177472,-0.0738942],'cal/(mol*K)','+|-',[0.478496,0.527395,0.561366,0.558223,0.469834,0.372606,0.551867]),
        H298 = (0.534935,'kcal/mol','+|-',2.05816),
        S298 = (1.24882,'cal/(mol*K)','+|-',1.57909),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 390,
    label = "4ring-Cd(FCs)=Cd(FCs)_580",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs  u0 p0 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27958,-0.321377,-0.345716,-0.320703,-0.200842,-0.0906357,0.0124778],'cal/(mol*K)','+|-',[0.451646,0.497801,0.529866,0.5269,0.44347,0.351698,0.5209]),
        H298 = (3.01227,'kcal/mol','+|-',1.94267),
        S298 = (0.745391,'cal/(mol*K)','+|-',1.49049),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 391,
    label = "4ring-Cd(Val7Cd)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.203616,-0.190374,-0.179365,-0.169797,-0.138738,-0.0953444,0.0578002],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (0.949067,'kcal/mol','+|-',1.07027),
        S298 = (1.74742,'cal/(mol*K)','+|-',0.658138),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "4ring-Cd(BrCd)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.252509,-0.274418,-0.279567,-0.28149,-0.234063,-0.162555,0.00881567],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (0.663099,'kcal/mol','+|-',1.94798),
        S298 = (2.05437,'cal/(mol*K)','+|-',1.49456),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 393,
    label = "4ring-Cd(ClCd)-Cs(ClCsH)_433",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.108238,-0.0997628,-0.0640231,-0.0458915,-0.070938,-0.0836424,0.0363649],'cal/(mol*K)','+|-',[0.410462,0.452408,0.481549,0.478853,0.403031,0.319627,0.473401]),
        H298 = (0.617671,'kcal/mol','+|-',1.76552),
        S298 = (1.39998,'cal/(mol*K)','+|-',1.35457),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 394,
    label = "4ring-Cd(FCd)-Cs(FCsH)_582",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2501,-0.19694,-0.194505,-0.182011,-0.111212,-0.0398357,0.12822],'cal/(mol*K)','+|-',[0.426263,0.469824,0.500087,0.497287,0.418546,0.331932,0.491625]),
        H298 = (1.56643,'kcal/mol','+|-',1.83349),
        S298 = (1.78792,'cal/(mol*K)','+|-',1.40672),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 395,
    label = "4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.129535,-0.168124,-0.18985,-0.197625,-0.17829,-0.138101,0.0389214],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (0.701041,'kcal/mol','+|-',2.78989),
        S298 = (1.76077,'cal/(mol*K)','+|-',0.737533),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "4ring-Cd(BrCd)-Cs(BrBrCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0789949,-0.211796,-0.250156,-0.241647,-0.220024,-0.214678,-0.115792],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (-0.288343,'kcal/mol','+|-',1.94798),
        S298 = (2.07918,'cal/(mol*K)','+|-',1.49456),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 397,
    label = "4ring-Cd(ClCd)-Cs(ClClCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.118767,-0.14192,-0.183917,-0.223843,-0.239723,-0.194116,0.0447353],'cal/(mol*K)','+|-',[0.450598,0.496646,0.528637,0.525677,0.442441,0.350882,0.519691]),
        H298 = (0.0949558,'kcal/mol','+|-',1.93816),
        S298 = (1.84642,'cal/(mol*K)','+|-',1.48703),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 398,
    label = "4ring-Cd(FCd)-Cs(FFCs)_581",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.190842,-0.150656,-0.135477,-0.127385,-0.0751215,-0.0055093,0.187821],'cal/(mol*K)','+|-',[0.449745,0.495705,0.527635,0.524681,0.441603,0.350217,0.518707]),
        H298 = (2.29651,'kcal/mol','+|-',1.93449),
        S298 = (1.35672,'cal/(mol*K)','+|-',1.48421),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 399,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.533744,-0.44064,-0.342904,-0.352207,-0.33146,-0.256925,0.289057],'cal/(mol*K)','+|-',[0.557458,0.614426,0.654003,0.650341,0.547366,0.434093,0.642936]),
        H298 = (0.892996,'kcal/mol','+|-',0.624106),
        S298 = (2.63791,'cal/(mol*K)','+|-',2.75424),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "4ring-Cs(BrBrCd)-Cs(BrCdH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.570177,-0.546057,-0.441877,-0.405598,-0.345551,-0.303588,0.0398732],'cal/(mol*K)','+|-',[0.557458,0.614426,0.654003,0.650341,0.547366,0.434093,0.642936]),
        H298 = (0.551262,'kcal/mol','+|-',2.39779),
        S298 = (2.08309,'cal/(mol*K)','+|-',1.83968),
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
    index = 401,
    label = "4ring-Cs(ClClCd)-Cs(ClCdH)_479",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.773412,-0.679813,-0.598067,-0.652598,-0.664076,-0.527637,0.421019],'cal/(mol*K)','+|-',[1.09588,1.20787,1.28567,1.27847,1.07604,0.853362,1.26392]),
        H298 = (0.964917,'kcal/mol','+|-',4.7137),
        S298 = (4.2059,'cal/(mol*K)','+|-',3.61653),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 402,
    label = "4ring-Cs(FFCd)-Cs(FCdH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u0 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.257643,-0.0960508,0.0112308,0.00157445,0.0152485,0.0604488,0.40628],'cal/(mol*K)','+|-',[0.489879,0.539941,0.57472,0.571502,0.48101,0.381469,0.564995]),
        H298 = (1.16281,'kcal/mol','+|-',2.10712),
        S298 = (1.62474,'cal/(mol*K)','+|-',1.61666),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 403,
    label = "4ring-Cs(Val7O2sH)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.27213,-3.64927,-4.2429,-4.33621,-3.72243,-2.89148,-1.51667],'cal/(mol*K)','+|-',[1.13334,1.24916,1.32963,1.32218,1.11283,0.882537,1.30713]),
        H298 = (15.2179,'kcal/mol','+|-',8.63935),
        S298 = (10.7911,'cal/(mol*K)','+|-',0.951226),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "4ring-Cs(BrO2sH)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.357,-3.68698,-4.23334,-4.34619,-3.82804,-3.03151,-1.58741],'cal/(mol*K)','+|-',[1.13334,1.24916,1.32963,1.32218,1.11283,0.882537,1.30713]),
        H298 = (11.8056,'kcal/mol','+|-',4.87486),
        S298 = (10.8767,'cal/(mol*K)','+|-',3.74017),
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
    index = 405,
    label = "4ring-Cs(ClO2sH)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.3062,-3.7364,-4.38365,-4.48957,-3.86777,-3.01921,-1.59878],'cal/(mol*K)','+|-',[1.09736,1.2095,1.28741,1.2802,1.07749,0.854513,1.26562]),
        H298 = (13.7733,'kcal/mol','+|-',4.72006),
        S298 = (11.2181,'cal/(mol*K)','+|-',3.6214),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 406,
    label = "4ring-Cs(FO2sH)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.15318,-3.52444,-4.1117,-4.17288,-3.47148,-2.62372,-1.36383],'cal/(mol*K)','+|-',[1.09736,1.2095,1.28741,1.2802,1.07749,0.854513,1.26562]),
        H298 = (20.0747,'kcal/mol','+|-',4.72006),
        S298 = (10.2785,'cal/(mol*K)','+|-',3.6214),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 407,
    label = "4ring-Cd(Val7Cs)=Cd(Val7O2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0721247,-0.05541,-0.150064,-0.237517,-0.318327,-0.320896,-0.194276],'cal/(mol*K)','+|-',[0.566672,0.624582,0.664814,0.661091,0.556414,0.441269,0.653564]),
        H298 = (3.00694,'kcal/mol','+|-',8.30976),
        S298 = (1.4155,'cal/(mol*K)','+|-',0.888004),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "4ring-Cd(BrCs)=Cd(BrO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0677495,-0.16156,-0.312429,-0.396654,-0.439491,-0.399624,-0.259813],'cal/(mol*K)','+|-',[0.566672,0.624582,0.664814,0.661091,0.556414,0.441269,0.653564]),
        H298 = (1.06281,'kcal/mol','+|-',2.43743),
        S298 = (1.66202,'cal/(mol*K)','+|-',1.87008),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 409,
    label = "4ring-Cd(ClCs)=Cd(ClO2s)_445",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0326675,0.0710243,0.0315803,-0.0459456,-0.148374,-0.174795,-0.0933971],'cal/(mol*K)','+|-',[0.490753,0.540904,0.575746,0.572522,0.481869,0.38215,0.566004]),
        H298 = (0.180537,'kcal/mol','+|-',2.11088),
        S298 = (0.902932,'cal/(mol*K)','+|-',1.61954),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 410,
    label = "4ring-Cd(FCs)=Cd(FO2s)_555",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.181292,-0.0756944,-0.169344,-0.26995,-0.367116,-0.38827,-0.229617],'cal/(mol*K)','+|-',[0.981506,1.08181,1.15149,1.14504,0.963737,0.7643,1.13201]),
        H298 = (7.77746,'kcal/mol','+|-',4.22175),
        S298 = (1.68154,'cal/(mol*K)','+|-',3.23908),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 411,
    label = "4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.815212,-0.411581,-0.121514,-0.077358,-0.079726,-0.0111555,0.423771],'cal/(mol*K)','+|-',[1.78038,1.96232,2.08872,2.07702,1.74815,1.38638,2.05337]),
        H298 = (1.64336,'kcal/mol','+|-',0.268248),
        S298 = (2.32872,'cal/(mol*K)','+|-',3.24374),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "4ring-Cs(BrCdH)-Cs(BrBrCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.26185,-0.804369,-0.42559,-0.366024,-0.382448,-0.26229,0.323342],'cal/(mol*K)','+|-',[1.78038,1.96232,2.08872,2.07702,1.74815,1.38638,2.05337]),
        H298 = (1.54852,'kcal/mol','+|-',7.65794),
        S298 = (3.47556,'cal/(mol*K)','+|-',5.87545),
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
    index = 413,
    label = "4ring-Cs(FCdH)-Cs(FFCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.368574,-0.0187932,0.182562,0.211308,0.222996,0.239979,0.524199],'cal/(mol*K)','+|-',[0.849505,0.936318,0.996629,0.991049,0.834126,0.661511,0.979765]),
        H298 = (1.7382,'kcal/mol','+|-',3.65398),
        S298 = (1.18189,'cal/(mol*K)','+|-',2.80346),
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
    index = 414,
    label = "4ring-Cs(Val7Val7O2s)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.859327,-0.663702,-0.602504,-0.844188,-0.894858,-0.808714,-0.534364],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (3.41253,'kcal/mol','+|-',1.3012),
        S298 = (4.38661,'cal/(mol*K)','+|-',2.73299),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "4ring-Cs(BrBrO2s)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.949273,-0.759475,-0.712979,-1.01075,-1.15264,-1.10378,-0.784915],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (3.22911,'kcal/mol','+|-',2.98523),
        S298 = (5.25656,'cal/(mol*K)','+|-',2.29038),
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
    index = 416,
    label = "4ring-Cs(ClClO2s)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.775458,-0.634187,-0.634532,-0.894421,-0.966035,-0.892677,-0.632383],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (2.87333,'kcal/mol','+|-',2.98523),
        S298 = (5.09167,'cal/(mol*K)','+|-',2.29038),
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
    index = 417,
    label = "4ring-Cs(FFO2s)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.85325,-0.597444,-0.46,-0.627393,-0.5659,-0.429684,-0.185794],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (4.13515,'kcal/mol','+|-',2.98523),
        S298 = (2.81159,'cal/(mol*K)','+|-',2.29038),
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
    index = 418,
    label = "4ring-Cs(Val7CsH)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.52849,-0.501197,-0.606843,-0.718125,-0.705507,-0.623323,-1.35349],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.74063,'kcal/mol','+|-',0.984714),
        S298 = (3.07751,'cal/(mol*K)','+|-',1.3418),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "4ring-Cs(BrCsH)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.626539,-0.682816,-0.801583,-0.907096,-0.896646,-0.821493,-1.55457],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.506892,'kcal/mol','+|-',1.236),
        S298 = (3.69259,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 420,
    label = "4ring-Cs(ClCsH)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.487931,-0.443902,-0.573028,-0.733204,-0.775676,-0.704618,-1.40567],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337123,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.408678,'kcal/mol','+|-',1.236),
        S298 = (3.17785,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 421,
    label = "4ring-Cs(FCsH)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.471001,-0.376872,-0.445919,-0.514076,-0.4442,-0.343858,-1.10022],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337123,0.335235,0.282154,0.223764,0.331418]),
        H298 = (1.30632,'kcal/mol','+|-',1.236),
        S298 = (2.36209,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 422,
    label = "4ring-Cs(Val7CsH)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.308865,-0.409165,-0.431626,-0.421684,-0.418287,-0.345514,-0.0983532],'cal/(mol*K)','+|-',[0.140861,0.155256,0.165257,0.164331,0.138311,0.109689,0.16246]),
        H298 = (1.43492,'kcal/mol','+|-',1.17515),
        S298 = (1.74192,'cal/(mol*K)','+|-',0.406952),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "4ring-Cs(BrCsH)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.361061,-0.513787,-0.578728,-0.590326,-0.576506,-0.483152,-0.209003],'cal/(mol*K)','+|-',[0.140861,0.155256,0.165257,0.164331,0.138311,0.109689,0.16246]),
        H298 = (1.03441,'kcal/mol','+|-',0.605886),
        S298 = (1.8641,'cal/(mol*K)','+|-',0.464858),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         5
""",
)

entry(
    index = 424,
    label = "4ring-Cs(ClCsH)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284088,-0.385869,-0.404241,-0.401458,-0.43258,-0.382589,-0.116871],'cal/(mol*K)','+|-',[0.140861,0.155256,0.165257,0.164331,0.138311,0.109689,0.16246]),
        H298 = (1.1609,'kcal/mol','+|-',0.605886),
        S298 = (1.85463,'cal/(mol*K)','+|-',0.464858),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 425,
    label = "4ring-Cs(FCsH)-Cs(FCsH)_568",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.281445,-0.32784,-0.311909,-0.273269,-0.245774,-0.170802,0.0308143],'cal/(mol*K)','+|-',[0.140861,0.155256,0.165257,0.164331,0.138311,0.109689,0.16246]),
        H298 = (2.10945,'kcal/mol','+|-',0.605886),
        S298 = (1.50703,'cal/(mol*K)','+|-',0.464858),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 426,
    label = "4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.391913,-0.543973,-0.584718,-0.606748,-0.622216,-0.524246,-0.16989],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (1.93707,'kcal/mol','+|-',2.24437),
        S298 = (2.5055,'cal/(mol*K)','+|-',0.604539),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "4ring-Cs(BrCsH)-Cs(BrBrCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.327898,-0.613452,-0.738483,-0.785847,-0.822384,-0.746351,-0.434969],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (1.21623,'kcal/mol','+|-',0.811323),
        S298 = (2.67057,'cal/(mol*K)','+|-',0.622477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 428,
    label = "4ring-Cs(ClCsH)-Cs(ClClCs)_467",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378327,-0.540203,-0.611319,-0.660851,-0.704092,-0.604334,-0.191325],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (1.36497,'kcal/mol','+|-',0.811323),
        S298 = (2.6893,'cal/(mol*K)','+|-',0.622477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 429,
    label = "4ring-Cs(FCsH)-Cs(FFCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469514,-0.478264,-0.404351,-0.373545,-0.340172,-0.222053,0.116623],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (3.23001,'kcal/mol','+|-',0.811323),
        S298 = (2.15664,'cal/(mol*K)','+|-',0.622477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 430,
    label = "4ring-Cs(Val7CsH)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.263575,-0.290528,-0.244401,-0.183087,-0.156366,-0.114778,0.0652411],'cal/(mol*K)','+|-',[0.295047,0.325199,0.346146,0.344208,0.289706,0.229754,0.340289]),
        H298 = (1.38169,'kcal/mol','+|-',1.17684),
        S298 = (0.954894,'cal/(mol*K)','+|-',1.19924),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "4ring-Cs(BrCsH)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.173547,-0.234461,-0.243635,-0.223,-0.191438,-0.132948,0.00213761],'cal/(mol*K)','+|-',[0.295047,0.325199,0.346146,0.344208,0.289706,0.229754,0.340289]),
        H298 = (0.745781,'kcal/mol','+|-',1.26909),
        S298 = (0.317212,'cal/(mol*K)','+|-',0.973689),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 432,
    label = "4ring-Cs(ClCsH)-Cs(ClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.254463,-0.32685,-0.278467,-0.191379,-0.140305,-0.125329,0.0884196],'cal/(mol*K)','+|-',[0.271004,0.298699,0.317939,0.316159,0.266098,0.211032,0.312559]),
        H298 = (1.49238,'kcal/mol','+|-',1.16567),
        S298 = (1.50733,'cal/(mol*K)','+|-',0.894346),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 433,
    label = "4ring-Cs(FCsH)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.362714,-0.310273,-0.211102,-0.134882,-0.137356,-0.0860584,0.105166],'cal/(mol*K)','+|-',[0.249793,0.27532,0.293054,0.291414,0.245271,0.194514,0.288096]),
        H298 = (1.9069,'kcal/mol','+|-',1.07444),
        S298 = (1.04014,'cal/(mol*K)','+|-',0.824346),
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
    index = 434,
    label = "4ring-Cd(Val7Cd)-Cs(Val7CsH)_62",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54904,-0.357673,-0.255623,-0.187229,-0.0890487,-0.00424767,0.219191],'cal/(mol*K)','+|-',[1.45082,1.59908,1.70208,1.69255,1.42455,1.12976,1.67328]),
        H298 = (2.92387,'kcal/mol','+|-',4.41919),
        S298 = (2.60048,'cal/(mol*K)','+|-',2.81408),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "4ring-Cd(BrCd)-Cs(BrCsH)_243",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.702292,-0.528968,-0.435951,-0.388648,-0.266865,-0.131059,0.146182],'cal/(mol*K)','+|-',[1.45082,1.59908,1.70208,1.69255,1.42455,1.12976,1.67328]),
        H298 = (2.37159,'kcal/mol','+|-',6.24041),
        S298 = (3.64245,'cal/(mol*K)','+|-',4.78787),
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
    index = 436,
    label = "4ring-Cd(ClCd)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234238,-0.0921238,0.0261451,0.102752,0.102794,0.0774407,0.147096],'cal/(mol*K)','+|-',[0.806323,0.888723,0.945969,0.940672,0.791726,0.627885,0.929962]),
        H298 = (1.0428,'kcal/mol','+|-',3.46824),
        S298 = (0.999917,'cal/(mol*K)','+|-',2.66096),
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
    index = 437,
    label = "4ring-Cd(FCd)-Cs(FCsH)_626",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u1 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.710589,-0.451928,-0.357063,-0.275791,-0.103075,0.0408753,0.364295],'cal/(mol*K)','+|-',[1.30006,1.43292,1.52521,1.51667,1.27652,1.01236,1.49941]),
        H298 = (5.35722,'kcal/mol','+|-',5.59195),
        S298 = (3.15907,'cal/(mol*K)','+|-',4.29035),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 438,
    label = "4ring-Cs(Val7Val7O2s)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13437,-1.41749,-1.12537,-1.53438,-1.62641,-1.50732,-1.15928],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (3.74973,'kcal/mol','+|-',1.17374),
        S298 = (8.85065,'cal/(mol*K)','+|-',1.23457),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "4ring-Cs(BrBrO2s)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00189,-1.23169,-0.944849,-1.4379,-1.68336,-1.635,-1.32587],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (3.33475,'kcal/mol','+|-',8.4435),
        S298 = (9.28713,'cal/(mol*K)','+|-',6.47816),
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
    index = 440,
    label = "4ring-Cs(ClClO2s)-Cs(ClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26684,-1.60329,-1.30589,-1.63087,-1.56946,-1.37964,-0.992693],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (4.16471,'kcal/mol','+|-',8.4435),
        S298 = (8.41416,'cal/(mol*K)','+|-',6.47816),
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
    index = 441,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7O2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.14331,-1.36388,-1.55155,-1.6982,-1.59611,-1.36081,-2.21953],'cal/(mol*K)','+|-',[1.27859,1.40925,1.50002,1.49162,1.25544,0.995638,1.47464]),
        H298 = (3.10112,'kcal/mol','+|-',0.645405),
        S298 = (5.56119,'cal/(mol*K)','+|-',7.41799),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "4ring-Cs(BrBrCs)-Cs(BrO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.43122,-1.90847,-2.25791,-2.50139,-2.41723,-2.11493,-3.15943],'cal/(mol*K)','+|-',[1.27859,1.40925,1.50002,1.49162,1.25544,0.995638,1.47464]),
        H298 = (2.87293,'kcal/mol','+|-',5.49959),
        S298 = (8.18385,'cal/(mol*K)','+|-',4.21948),
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
    index = 443,
    label = "4ring-Cs(FFCs)-Cs(FO2sH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.855394,-0.81928,-0.845188,-0.895016,-0.774996,-0.606699,-1.27963],'cal/(mol*K)','+|-',[0.646107,0.712134,0.758005,0.753761,0.63441,0.503125,0.745179]),
        H298 = (3.3293,'kcal/mol','+|-',2.7791),
        S298 = (2.93854,'cal/(mol*K)','+|-',2.13223),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 444,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7O2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.27717,-1.16332,-1.05505,-1.26273,-1.28209,-1.15051,-0.74978],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (1.86127,'kcal/mol','+|-',0.881493),
        S298 = (4.16025,'cal/(mol*K)','+|-',0.671396),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "4ring-Cs(BrO2sH)-Cs(BrO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54016,-1.45773,-1.31509,-1.47556,-1.49,-1.37279,-0.861485],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (1.5187,'kcal/mol','+|-',2.98523),
        S298 = (4.3944,'cal/(mol*K)','+|-',2.29038),
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
    index = 446,
    label = "4ring-Cs(ClO2sH)-Cs(ClO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.41309,-1.29731,-1.14266,-1.34912,-1.38524,-1.22444,-0.762324],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (1.7066,'kcal/mol','+|-',2.98523),
        S298 = (4.3107,'cal/(mol*K)','+|-',2.29038),
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
    index = 447,
    label = "4ring-Cs(FO2sH)-Cs(FO2sH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87825,-0.73492,-0.707397,-0.963514,-0.971019,-0.854304,-0.62553],'cal/(mol*K)','+|-',[0.69403,0.764954,0.814228,0.809669,0.681465,0.540442,0.80045]),
        H298 = (2.3585,'kcal/mol','+|-',2.98523),
        S298 = (3.77564,'cal/(mol*K)','+|-',2.29038),
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
    index = 448,
    label = "4ring-Cs(Val7Cd)-Cs(Val7CdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.441275,-0.422089,-0.444266,-0.501918,-0.445378,-0.348239,0.0978319],'cal/(mol*K)','+|-',[0.716537,0.789762,0.840633,0.835926,0.703565,0.557968,0.826408]),
        H298 = (3.56312,'kcal/mol','+|-',1.91227),
        S298 = (2.84077,'cal/(mol*K)','+|-',1.56375),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "4ring-Cs(BrCd)-Cs(BrCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.688657,-0.601068,-0.542178,-0.551829,-0.487148,-0.371522,-0.00302736],'cal/(mol*K)','+|-',[0.716537,0.789762,0.840633,0.835926,0.703565,0.557968,0.826408]),
        H298 = (2.79929,'kcal/mol','+|-',3.08204),
        S298 = (3.32346,'cal/(mol*K)','+|-',2.36465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 450,
    label = "4ring-Cs(ClCd)-Cs(ClCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.576183,-0.579539,-0.641644,-0.715048,-0.590969,-0.43571,0.2123],'cal/(mol*K)','+|-',[1.63833,1.80576,1.92208,1.91131,1.60867,1.27577,1.88955]),
        H298 = (3.25466,'kcal/mol','+|-',7.04697),
        S298 = (3.26018,'cal/(mol*K)','+|-',5.40669),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 451,
    label = "4ring-Cs(FCd)-Cs(FCdH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u0 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0589844,-0.0856598,-0.148975,-0.238877,-0.258016,-0.237484,0.084223],'cal/(mol*K)','+|-',[0.707349,0.779635,0.829853,0.825207,0.694543,0.550814,0.815811]),
        H298 = (4.63541,'kcal/mol','+|-',3.04252),
        S298 = (1.93868,'cal/(mol*K)','+|-',2.33433),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 452,
    label = "4ring-Cd(Val7Cs)=Cd(Val7Cs)_84",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.312334,0.167174,0.0187686,-0.0813251,-0.171504,-0.185541,-0.194657],'cal/(mol*K)','+|-',[0.632288,0.696903,0.741793,0.73764,0.620841,0.492364,0.729241]),
        H298 = (1.82897,'kcal/mol','+|-',3.28207),
        S298 = (2.5054,'cal/(mol*K)','+|-',0.827382),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "4ring-Cd(BrCs)=Cd(BrCs)_265",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.435432,0.240499,0.0534464,-0.0629968,-0.196335,-0.234983,-0.279874],'cal/(mol*K)','+|-',[0.632288,0.696903,0.741793,0.73764,0.620841,0.492364,0.729241]),
        H298 = (0.823677,'kcal/mol','+|-',2.71966),
        S298 = (2.87772,'cal/(mol*K)','+|-',2.08662),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 454,
    label = "4ring-Cd(ClCs)=Cd(ClCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41563,0.268552,0.0920187,-0.0284044,-0.14817,-0.181674,-0.188268],'cal/(mol*K)','+|-',[0.64933,0.715687,0.761787,0.757522,0.637575,0.505635,0.748896]),
        H298 = (0.940566,'kcal/mol','+|-',2.79296),
        S298 = (2.57841,'cal/(mol*K)','+|-',2.14286),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 455,
    label = "4ring-Cd(FCs)=Cd(FCs)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0859406,-0.00752882,-0.0891593,-0.152574,-0.170006,-0.139965,-0.115828],'cal/(mol*K)','+|-',[0.614755,0.677578,0.721223,0.717185,0.603626,0.478711,0.709019]),
        H298 = (3.72267,'kcal/mol','+|-',2.64425),
        S298 = (2.06006,'cal/(mol*K)','+|-',2.02876),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 456,
    label = "4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)_85",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.523806,0.386501,0.233211,0.107303,-0.047137,-0.109295,-0.11133],'cal/(mol*K)','+|-',[0.701074,0.772718,0.822491,0.817886,0.688382,0.545927,0.808574]),
        H298 = (1.15221,'kcal/mol','+|-',4.93122),
        S298 = (4.17214,'cal/(mol*K)','+|-',1.28602),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "4ring-Cd(BrCd)-Cs(BrBrCs)_266",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.708952,0.482848,0.238757,0.0550461,-0.141839,-0.233256,-0.319114],'cal/(mol*K)','+|-',[0.701074,0.772718,0.822491,0.817886,0.688382,0.545927,0.808574]),
        H298 = (-0.591241,'kcal/mol','+|-',3.01553),
        S298 = (4.62682,'cal/(mol*K)','+|-',2.31362),
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
    index = 458,
    label = "4ring-Cd(FCd)-Cs(FFCs)_596",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u1 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.338661,0.290153,0.227665,0.15956,0.047565,0.0146653,0.0964535],'cal/(mol*K)','+|-',[0.665664,0.73369,0.78095,0.776577,0.653613,0.518354,0.767735]),
        H298 = (2.89566,'kcal/mol','+|-',2.86322),
        S298 = (3.71747,'cal/(mol*K)','+|-',2.19677),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 459,
    label = "4ring-Cs(Val7Cd)-Cs(Val7Val7Cd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.163464,-0.0628308,-0.0743913,-0.217999,-0.317381,-0.324215,0.035939],'cal/(mol*K)','+|-',[1.78038,1.96232,2.08872,2.07702,1.74815,1.38638,2.05337]),
        H298 = (6.59431,'kcal/mol','+|-',6.03475),
        S298 = (5.04212,'cal/(mol*K)','+|-',4.0358),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "4ring-Cs(BrCd)-Cs(BrBrCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.306105,-0.0610376,-0.0953702,-0.283936,-0.379676,-0.401213,-0.316817],'cal/(mol*K)','+|-',[1.78038,1.96232,2.08872,2.07702,1.74815,1.38638,2.05337]),
        H298 = (4.46071,'kcal/mol','+|-',7.65794),
        S298 = (6.46899,'cal/(mol*K)','+|-',5.87545),
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
    index = 461,
    label = "4ring-Cs(FCd)-Cs(FFCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u0 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0208231,-0.0646239,-0.0534124,-0.152061,-0.255087,-0.247216,0.388695],'cal/(mol*K)','+|-',[1.38682,1.52855,1.627,1.6179,1.36172,1.07992,1.59947]),
        H298 = (8.72792,'kcal/mol','+|-',5.96514),
        S298 = (3.61525,'cal/(mol*K)','+|-',4.57668),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 462,
    label = "4ring-Cs(Val7O2s)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79391,-0.31167,-0.222724,-0.315895,-0.355357,-0.347999,-1.7342],'cal/(mol*K)','+|-',[0.639294,0.704625,0.750012,0.745813,0.62772,0.497819,0.737321]),
        H298 = (2.99866,'kcal/mol','+|-',6.55154),
        S298 = (2.62961,'cal/(mol*K)','+|-',0.0164049),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "4ring-Cs(BrO2s)-Cs(BrBrCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.292351,-0.239092,-0.337491,-0.447706,-0.500669,-0.527271,-1.47078],'cal/(mol*K)','+|-',[0.639294,0.704625,0.750012,0.745813,0.62772,0.497819,0.737321]),
        H298 = (0.682342,'kcal/mol','+|-',2.74979),
        S298 = (2.62381,'cal/(mol*K)','+|-',2.10974),
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
    index = 464,
    label = "4ring-Cs(FO2s)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.29547,-0.384248,-0.107958,-0.184085,-0.210045,-0.168727,-1.99761],'cal/(mol*K)','+|-',[1.29221,1.42427,1.51601,1.50752,1.26882,1.00625,1.49036]),
        H298 = (5.31498,'kcal/mol','+|-',5.5582),
        S298 = (2.63541,'cal/(mol*K)','+|-',4.26445),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 465,
    label = "4ring-Cd(Val7Cs)=Cd(Val7Cs)_96",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.312334,0.167174,0.0187686,-0.0813251,-0.171504,-0.185541,-0.194657],'cal/(mol*K)','+|-',[0.632288,0.696903,0.741793,0.73764,0.620841,0.492364,0.729241]),
        H298 = (1.82897,'kcal/mol','+|-',3.28207),
        S298 = (2.5054,'cal/(mol*K)','+|-',0.827382),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "4ring-Cd(BrCs)=Cd(BrCs)_277",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.435432,0.240499,0.0534464,-0.0629968,-0.196335,-0.234983,-0.279874],'cal/(mol*K)','+|-',[0.632288,0.696903,0.741793,0.73764,0.620841,0.492364,0.729241]),
        H298 = (0.823677,'kcal/mol','+|-',2.71966),
        S298 = (2.87772,'cal/(mol*K)','+|-',2.08662),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 467,
    label = "4ring-Cd(ClCs)=Cd(ClCs)_461",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41563,0.268552,0.0920187,-0.0284044,-0.14817,-0.181674,-0.188268],'cal/(mol*K)','+|-',[0.64933,0.715687,0.761787,0.757522,0.637575,0.505635,0.748896]),
        H298 = (0.940566,'kcal/mol','+|-',2.79296),
        S298 = (2.57841,'cal/(mol*K)','+|-',2.14286),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 468,
    label = "4ring-Cd(FCs)=Cd(FCs)_565",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0859406,-0.00752882,-0.0891593,-0.152574,-0.170006,-0.139965,-0.115828],'cal/(mol*K)','+|-',[0.614755,0.677578,0.721223,0.717185,0.603626,0.478711,0.709019]),
        H298 = (3.72267,'kcal/mol','+|-',2.64425),
        S298 = (2.06006,'cal/(mol*K)','+|-',2.02876),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 469,
    label = "4ring-Cs(Val7CsH)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.354388,0.273389,0.155946,0.0545815,-0.0628774,-0.113523,-0.117715],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (1.38057,'kcal/mol','+|-',2.73937),
        S298 = (3.70714,'cal/(mol*K)','+|-',0.765061),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "4ring-Cs(BrCsH)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.270328,0.155595,0.0372841,-0.0587404,-0.14644,-0.173387,-0.189164],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (0.860071,'kcal/mol','+|-',2.79443),
        S298 = (4.12347,'cal/(mol*K)','+|-',2.14399),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 471,
    label = "4ring-Cs(ClCsH)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.402267,0.319139,0.228487,0.138157,-0.00458927,-0.0801329,-0.108598],'cal/(mol*K)','+|-',[0.646023,0.712042,0.757907,0.753663,0.634328,0.503059,0.745082]),
        H298 = (0.347434,'kcal/mol','+|-',2.77874),
        S298 = (3.37118,'cal/(mol*K)','+|-',2.13195),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 472,
    label = "4ring-Cs(FCsH)-Cd(FCd)_652",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u1 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.390569,0.345434,0.202068,0.0843278,-0.037603,-0.0870504,-0.0553824],'cal/(mol*K)','+|-',[0.62911,0.6934,0.738064,0.733932,0.617721,0.489889,0.725575]),
        H298 = (2.93421,'kcal/mol','+|-',2.70599),
        S298 = (3.62677,'cal/(mol*K)','+|-',2.07613),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 473,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83365,-0.666636,-0.74248,-0.864593,-0.84773,-0.787731,-1.95653],'cal/(mol*K)','+|-',[0.639294,0.704625,0.750012,0.745813,0.62772,0.497819,0.737321]),
        H298 = (0.981591,'kcal/mol','+|-',0.846404),
        S298 = (3.59102,'cal/(mol*K)','+|-',2.73568),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "4ring-Cs(BrBrCs)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.292351,-0.239092,-0.337491,-0.447706,-0.500669,-0.527271,-1.47078],'cal/(mol*K)','+|-',[0.639294,0.704625,0.750012,0.745813,0.62772,0.497819,0.737321]),
        H298 = (0.682342,'kcal/mol','+|-',2.74979),
        S298 = (2.62381,'cal/(mol*K)','+|-',2.10974),
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
    index = 475,
    label = "4ring-Cs(ClClCs)-Cs(ClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37495,-1.09418,-1.14747,-1.28148,-1.19479,-1.04819,-2.44229],'cal/(mol*K)','+|-',[1.50898,1.66319,1.77032,1.76041,1.48166,1.17504,1.74036]),
        H298 = (1.28084,'kcal/mol','+|-',6.49058),
        S298 = (4.55823,'cal/(mol*K)','+|-',4.97981),
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
    index = 476,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.290693,-0.317365,-0.332759,-0.386903,-0.369661,-0.272031,0.213626],'cal/(mol*K)','+|-',[0.540476,0.595709,0.63408,0.63053,0.530692,0.42087,0.623351]),
        H298 = (1.38499,'kcal/mol','+|-',1.60307),
        S298 = (2.04456,'cal/(mol*K)','+|-',1.22063),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "4ring-Cs(BrBrCd)-Cs(BrBrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.231773,-0.376652,-0.469487,-0.574439,-0.611774,-0.53019,-0.0905791],'cal/(mol*K)','+|-',[0.540476,0.595709,0.63408,0.63053,0.530692,0.42087,0.623351]),
        H298 = (1.13558,'kcal/mol','+|-',2.32475),
        S298 = (2.70816,'cal/(mol*K)','+|-',1.78363),
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
    index = 478,
    label = "4ring-Cs(ClClCd)-Cs(ClClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.278731,-0.377519,-0.427328,-0.476159,-0.454191,-0.352387,0.202376],'cal/(mol*K)','+|-',[0.539999,0.595182,0.63352,0.629973,0.530223,0.420498,0.6228]),
        H298 = (0.737809,'kcal/mol','+|-',2.3227),
        S298 = (1.9182,'cal/(mol*K)','+|-',1.78206),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 479,
    label = "4ring-Cs(FFCd)-Cs(FFCd)_646",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D}
4    Cd  u0 p0 c0 {1,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.361574,-0.197925,-0.101463,-0.110111,-0.0430171,0.0664854,0.529081],'cal/(mol*K)','+|-',[0.539821,0.594986,0.633311,0.629766,0.530048,0.420359,0.622595]),
        H298 = (2.28158,'kcal/mol','+|-',2.32193),
        S298 = (1.50731,'cal/(mol*K)','+|-',1.78147),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 480,
    label = "4ring-Cd(Val7O2s)=Cd(Val7Cs)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.187037,-0.307235,-0.392237,-0.425947,-0.376582,-0.263742,-0.0091072],'cal/(mol*K)','+|-',[0.801396,0.883293,0.940189,0.934925,0.786888,0.624048,0.924279]),
        H298 = (-0.755768,'kcal/mol','+|-',1.08081),
        S298 = (2.18105,'cal/(mol*K)','+|-',1.26909),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "4ring-Cd(BrO2s)=Cd(BrCs)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.268453,-0.441978,-0.563056,-0.604936,-0.528336,-0.380037,-0.0885324],'cal/(mol*K)','+|-',[0.801396,0.883293,0.940189,0.934925,0.786888,0.624048,0.924279]),
        H298 = (-0.373645,'kcal/mol','+|-',3.44705),
        S298 = (2.62974,'cal/(mol*K)','+|-',2.6447),
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
    index = 482,
    label = "4ring-Cd(ClO2s)=Cd(ClCs)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.105621,-0.172493,-0.221417,-0.246959,-0.224827,-0.147446,0.070318],'cal/(mol*K)','+|-',[0.749638,0.826245,0.879466,0.874542,0.736067,0.583744,0.864585]),
        H298 = (-1.13789,'kcal/mol','+|-',3.22442),
        S298 = (1.73236,'cal/(mol*K)','+|-',2.47389),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 483,
    label = "4ring-Cs(Val7Val7O2s)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.20615,-1.97536,-2.25605,-2.28323,-1.96368,-1.54351,-0.754406],'cal/(mol*K)','+|-',[1.79198,1.9751,2.10232,2.09055,1.75953,1.39541,2.06675]),
        H298 = (9.18018,'kcal/mol','+|-',5.45185),
        S298 = (6.1683,'cal/(mol*K)','+|-',5.21906),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "4ring-Cs(BrBrO2s)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3654,-2.30196,-2.63893,-2.69014,-2.41356,-1.99446,-1.04845],'cal/(mol*K)','+|-',[1.79198,1.9751,2.10232,2.09055,1.75953,1.39541,2.06675]),
        H298 = (7.25266,'kcal/mol','+|-',7.70783),
        S298 = (8.01351,'cal/(mol*K)','+|-',5.91373),
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
    index = 485,
    label = "4ring-Cs(FFO2s)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04689,-1.64876,-1.87317,-1.87631,-1.51379,-1.09256,-0.460361],'cal/(mol*K)','+|-',[0.548679,0.60475,0.643703,0.640099,0.538746,0.427257,0.632811]),
        H298 = (11.1077,'kcal/mol','+|-',2.36003),
        S298 = (4.32308,'cal/(mol*K)','+|-',1.8107),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 486,
    label = "4ring-Cs(Val7Cs)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.263575,-0.290528,-0.244401,-0.183087,-0.156366,-0.114778,0.0652411],'cal/(mol*K)','+|-',[0.295047,0.325199,0.346146,0.344208,0.289706,0.229754,0.340289]),
        H298 = (1.38169,'kcal/mol','+|-',1.17684),
        S298 = (0.954894,'cal/(mol*K)','+|-',1.19924),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "4ring-Cs(BrCs)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.173547,-0.234461,-0.243635,-0.223,-0.191438,-0.132948,0.00213761],'cal/(mol*K)','+|-',[0.295047,0.325199,0.346146,0.344208,0.289706,0.229754,0.340289]),
        H298 = (0.745781,'kcal/mol','+|-',1.26909),
        S298 = (0.317212,'cal/(mol*K)','+|-',0.973689),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 488,
    label = "4ring-Cs(ClCs)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.254463,-0.32685,-0.278467,-0.191379,-0.140305,-0.125329,0.0884196],'cal/(mol*K)','+|-',[0.271004,0.298699,0.317939,0.316159,0.266098,0.211032,0.312559]),
        H298 = (1.49238,'kcal/mol','+|-',1.16567),
        S298 = (1.50733,'cal/(mol*K)','+|-',0.894346),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 489,
    label = "4ring-Cs(FCs)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.362714,-0.310273,-0.211102,-0.134882,-0.137356,-0.0860584,0.105166],'cal/(mol*K)','+|-',[0.249793,0.27532,0.293054,0.291414,0.245271,0.194514,0.288096]),
        H298 = (1.9069,'kcal/mol','+|-',1.07444),
        S298 = (1.04014,'cal/(mol*K)','+|-',0.824346),
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
    index = 490,
    label = "4ring-Cs(Val7Cs)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378627,-0.403505,-0.253718,-0.18151,-0.287934,-0.240148,0.218548],'cal/(mol*K)','+|-',[0.541498,0.596835,0.635279,0.631723,0.531695,0.421666,0.62453]),
        H298 = (3.28434,'kcal/mol','+|-',6.27008),
        S298 = (3.49457,'cal/(mol*K)','+|-',2.56215),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "4ring-Cs(BrCs)-Cs(BrBrCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.190752,0.0339871,-0.0491533,-0.099449,-0.184761,-0.159625,-0.105511],'cal/(mol*K)','+|-',[0.541498,0.596835,0.635279,0.631723,0.531695,0.421666,0.62453]),
        H298 = (0.402319,'kcal/mol','+|-',2.32915),
        S298 = (2.04375,'cal/(mol*K)','+|-',1.78701),
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
    index = 492,
    label = "4ring-Cs(ClCs)-Cs(ClClCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.524508,-0.651453,-0.46968,-0.345964,-0.493891,-0.496012,0.241417],'cal/(mol*K)','+|-',[0.953042,1.05044,1.1181,1.11184,0.935789,0.742136,1.09918]),
        H298 = (2.82827,'kcal/mol','+|-',4.09932),
        S298 = (4.46997,'cal/(mol*K)','+|-',3.14515),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 493,
    label = "4ring-Cs(FCs)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.802124,-0.59305,-0.242322,-0.0991163,-0.185149,-0.0648075,0.519737],'cal/(mol*K)','+|-',[0.621472,0.684982,0.729103,0.725021,0.610221,0.483941,0.716766]),
        H298 = (6.62244,'kcal/mol','+|-',2.67314),
        S298 = (3.97,'cal/(mol*K)','+|-',2.05093),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 494,
    label = "4ring-Cd(Val7Cd)-Cs(Val7Cs)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0176619,-0.0677351,-0.100232,-0.127401,-0.144506,-0.150461,-0.0925743],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (3.35004,'kcal/mol','+|-',2.4344),
        S298 = (1.72996,'cal/(mol*K)','+|-',1.57793),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "4ring-Cd(BrCd)-Cs(BrCs)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0611581,-0.0409755,-0.075638,-0.102299,-0.103422,-0.102164,-0.133593],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (2.93558,'kcal/mol','+|-',2.79443),
        S298 = (2.55631,'cal/(mol*K)','+|-',2.14399),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 496,
    label = "4ring-Cd(ClCd)-Cs(ClCs)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0892578,-0.0109689,-0.01679,-0.0202117,-0.0630024,-0.110865,-0.0572875],'cal/(mol*K)','+|-',[0.646023,0.712042,0.757907,0.753663,0.634328,0.503059,0.745082]),
        H298 = (2.39419,'kcal/mol','+|-',2.77874),
        S298 = (0.984638,'cal/(mol*K)','+|-',2.13195),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 497,
    label = "4ring-Cd(FCd)-Cs(FCs)",
    group = 
"""
1 *2 Cs  u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0810854,-0.151261,-0.208268,-0.259693,-0.267094,-0.238353,-0.0868424],'cal/(mol*K)','+|-',[0.596355,0.657298,0.699637,0.69572,0.585559,0.464383,0.687798]),
        H298 = (4.72034,'kcal/mol','+|-',2.5651),
        S298 = (1.64892,'cal/(mol*K)','+|-',1.96804),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 498,
    label = "4ring-Cs(Val7CsH)-Cs(Val7O2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86294,-2.134,-2.36144,-2.51919,-2.36166,-1.93317,-3.08049],'cal/(mol*K)','+|-',[1.27073,1.40059,1.49081,1.48246,1.24773,0.989523,1.46558]),
        H298 = (1.00522,'kcal/mol','+|-',5.46581),
        S298 = (7.19048,'cal/(mol*K)','+|-',4.19357),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "4ring-Cs(BrCsH)-Cs(BrO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.86294,-2.134,-2.36144,-2.51919,-2.36166,-1.93317,-3.08049],'cal/(mol*K)','+|-',[1.27073,1.40059,1.49081,1.48246,1.24773,0.989523,1.46558]),
        H298 = (1.00522,'kcal/mol','+|-',5.46581),
        S298 = (7.19048,'cal/(mol*K)','+|-',4.19357),
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
    index = 500,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.751506,0.57785,0.293146,0.00273395,-0.468868,-0.572883,-0.216012],'cal/(mol*K)','+|-',[1.71045,1.88525,2.00668,1.99545,1.67948,1.33193,1.97272]),
        H298 = (6.03311,'kcal/mol','+|-',0.876897),
        S298 = (4.57239,'cal/(mol*K)','+|-',6.95258),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "4ring-Cs(BrBrCs)-Cs(BrBrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.64582,1.16557,0.538422,-0.0553396,-0.952859,-1.2244,-0.819802],'cal/(mol*K)','+|-',[1.71045,1.88525,2.00668,1.99545,1.67948,1.33193,1.97272]),
        H298 = (6.34314,'kcal/mol','+|-',7.35716),
        S298 = (7.0305,'cal/(mol*K)','+|-',5.64468),
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
    index = 502,
    label = "4ring-Cs(FFCs)-Cs(FFCs)_577",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.142809,-0.00987034,0.0478691,0.0608075,0.0151223,0.0786346,0.387778],'cal/(mol*K)','+|-',[0.651525,0.718107,0.764362,0.760083,0.639731,0.507344,0.751428]),
        H298 = (5.72308,'kcal/mol','+|-',2.80241),
        S298 = (2.11428,'cal/(mol*K)','+|-',2.15011),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 503,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.19047,-1.19267,-1.31595,-1.50105,-1.5047,-1.33125,-2.3563],'cal/(mol*K)','+|-',[0.295935,0.326178,0.347188,0.345244,0.290578,0.230445,0.341313]),
        H298 = (3.19716,'kcal/mol','+|-',4.04583),
        S298 = (4.85285,'cal/(mol*K)','+|-',2.97636),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "4ring-Cs(BrO2sH)-Cs(BrBrCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.689065,-0.839539,-0.992925,-1.11629,-1.10789,-1.00481,-1.61753],'cal/(mol*K)','+|-',[0.295935,0.326178,0.347188,0.345244,0.290578,0.230445,0.341313]),
        H298 = (1.42504,'kcal/mol','+|-',1.27291),
        S298 = (3.19947,'cal/(mol*K)','+|-',0.976621),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 505,
    label = "4ring-Cs(ClO2sH)-Cs(ClClCs)_396",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53091,-1.5679,-1.74303,-2.01923,-2.04671,-1.82249,-2.85409],'cal/(mol*K)','+|-',[0.591871,0.652356,0.694376,0.690488,0.581156,0.460891,0.682626]),
        H298 = (2.76532,'kcal/mol','+|-',2.54581),
        S298 = (6.08505,'cal/(mol*K)','+|-',1.95324),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 506,
    label = "4ring-Cs(FO2sH)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.35144,-1.17056,-1.2119,-1.36764,-1.35951,-1.16646,-2.59728],'cal/(mol*K)','+|-',[0.620759,0.684196,0.728268,0.72419,0.609521,0.483386,0.715944]),
        H298 = (5.40113,'kcal/mol','+|-',2.67007),
        S298 = (5.27402,'cal/(mol*K)','+|-',2.04858),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 507,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.19931,-1.84032,-1.6862,-2.16799,-2.2212,-1.96718,-1.28312],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (4.75146,'kcal/mol','+|-',2.11515),
        S298 = (10.1462,'cal/(mol*K)','+|-',2.5987),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
    label = "4ring-Cs(BrO2sH)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.53893,-2.24371,-2.06827,-2.56666,-2.72275,-2.48153,-1.64712],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (4.20137,'kcal/mol','+|-',5.97046),
        S298 = (11.0903,'cal/(mol*K)','+|-',4.58075),
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
    index = 509,
    label = "4ring-Cs(ClO2sH)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26397,-1.91502,-1.80437,-2.32637,-2.39204,-2.13248,-1.39612],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (4.08231,'kcal/mol','+|-',5.97046),
        S298 = (10.6839,'cal/(mol*K)','+|-',4.58075),
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
    index = 510,
    label = "4ring-Cs(FO2sH)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79504,-1.36222,-1.18596,-1.61093,-1.54881,-1.28752,-0.806112],'cal/(mol*K)','+|-',[1.38806,1.52991,1.62845,1.61934,1.36293,1.08088,1.6009]),
        H298 = (5.97071,'kcal/mol','+|-',5.97046),
        S298 = (8.66425,'cal/(mol*K)','+|-',4.58075),
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
    index = 511,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01957,-1.00187,-1.25563,-1.55779,-1.61614,-1.47967,-3.00316],'cal/(mol*K)','+|-',[1.02515,1.12991,1.20269,1.19596,1.00659,0.798286,1.18234]),
        H298 = (4.41828,'kcal/mol','+|-',2.07761),
        S298 = (7.41047,'cal/(mol*K)','+|-',4.34678),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "4ring-Cs(BrBrCs)-Cs(BrBrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.07076,-1.20416,-1.61965,-2.01194,-2.17174,-2.09713,-4.06352],'cal/(mol*K)','+|-',[1.02515,1.12991,1.20269,1.19596,1.00659,0.798286,1.18234]),
        H298 = (4.29651,'kcal/mol','+|-',4.40948),
        S298 = (8.88634,'cal/(mol*K)','+|-',3.38311),
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
    index = 513,
    label = "4ring-Cs(ClClCs)-Cs(ClClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.17245,-1.14954,-1.54504,-1.84985,-1.87065,-1.70607,-3.56182],'cal/(mol*K)','+|-',[1.02515,1.12991,1.20269,1.19596,1.00659,0.798286,1.18234]),
        H298 = (3.44572,'kcal/mol','+|-',4.40948),
        S298 = (8.43037,'cal/(mol*K)','+|-',3.38311),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 514,
    label = "4ring-Cs(FFCs)-Cs(FFO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.815501,-0.651908,-0.602197,-0.811581,-0.806029,-0.635813,-1.38414],'cal/(mol*K)','+|-',[1.52054,1.67593,1.78388,1.77389,1.49301,1.18405,1.7537]),
        H298 = (5.5126,'kcal/mol','+|-',6.54031),
        S298 = (4.9147,'cal/(mol*K)','+|-',5.01796),
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
    index = 515,
    label = "4ring-Cs(Val7CsH)-Cs(Val7O2sH)_119",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.701261,-0.728494,-0.832889,-0.921883,-0.887866,-0.78636,-1.45653],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.715761,'kcal/mol','+|-',1.56202),
        S298 = (2.4315,'cal/(mol*K)','+|-',2.16929),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "4ring-Cs(BrCsH)-Cs(BrO2sH)_300",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.849776,-0.931992,-1.04996,-1.13635,-1.06647,-0.943568,-1.58058],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (-0.0361684,'kcal/mol','+|-',1.236),
        S298 = (1.19659,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 517,
    label = "4ring-Cs(ClCsH)-Cs(ClO2sH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.773793,-0.796826,-0.850856,-0.927682,-0.945725,-0.861071,-1.46778],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.660531,'kcal/mol','+|-',1.236),
        S298 = (3.22979,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 518,
    label = "4ring-Cs(FCsH)-Cs(FO2sH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.480214,-0.456664,-0.597852,-0.701618,-0.651403,-0.554441,-1.32124],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (1.52292,'kcal/mol','+|-',1.236),
        S298 = (2.86812,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 519,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.127574,0.0912263,0.0362896,-0.0341575,-0.176313,-0.183191,0.0230737],'cal/(mol*K)','+|-',[0.343111,0.378174,0.402534,0.40028,0.336899,0.267181,0.395723]),
        H298 = (3.06983,'kcal/mol','+|-',2.12151),
        S298 = (2.2816,'cal/(mol*K)','+|-',0.851171),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "4ring-Cs(BrBrCs)-Cs(BrCsH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.292554,0.127055,-0.0250132,-0.152375,-0.356436,-0.390882,-0.2153],'cal/(mol*K)','+|-',[0.343111,0.378174,0.402534,0.40028,0.336899,0.267181,0.395723]),
        H298 = (2.26304,'kcal/mol','+|-',1.47582),
        S298 = (2.50943,'cal/(mol*K)','+|-',1.13231),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 521,
    label = "4ring-Cs(ClClCs)-Cs(ClCsH)_491",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.188704,0.138727,0.0504063,-0.0253163,-0.186311,-0.208804,0.0205212],'cal/(mol*K)','+|-',[0.34256,0.377567,0.401887,0.399637,0.336358,0.266752,0.395087]),
        H298 = (2.67509,'kcal/mol','+|-',1.47345),
        S298 = (2.54477,'cal/(mol*K)','+|-',1.13049),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 522,
    label = "4ring-Cs(FFCs)-Cs(FCsH)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0985358,0.00789701,0.0834758,0.0752187,0.0138078,0.0501143,0.264],'cal/(mol*K)','+|-',[0.300665,0.331391,0.352737,0.350762,0.295222,0.234129,0.346768]),
        H298 = (4.27136,'kcal/mol','+|-',1.29325),
        S298 = (1.7906,'cal/(mol*K)','+|-',0.99223),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 523,
    label = "4ring-Cs(Val7Cs)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0176619,-0.0677351,-0.100232,-0.127401,-0.144506,-0.150461,-0.0925743],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (3.35004,'kcal/mol','+|-',2.4344),
        S298 = (1.72996,'cal/(mol*K)','+|-',1.57793),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "4ring-Cs(BrCs)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0611581,-0.0409755,-0.075638,-0.102299,-0.103422,-0.102164,-0.133593],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (2.93558,'kcal/mol','+|-',2.79443),
        S298 = (2.55631,'cal/(mol*K)','+|-',2.14399),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 525,
    label = "4ring-Cs(ClCs)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0892578,-0.0109689,-0.01679,-0.0202117,-0.0630024,-0.110865,-0.0572875],'cal/(mol*K)','+|-',[0.646023,0.712042,0.757907,0.753663,0.634328,0.503059,0.745082]),
        H298 = (2.39419,'kcal/mol','+|-',2.77874),
        S298 = (0.984638,'cal/(mol*K)','+|-',2.13195),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 526,
    label = "4ring-Cs(FCs)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0810854,-0.151261,-0.208268,-0.259693,-0.267094,-0.238353,-0.0868424],'cal/(mol*K)','+|-',[0.596355,0.657298,0.699637,0.69572,0.585559,0.464383,0.687798]),
        H298 = (4.72034,'kcal/mol','+|-',2.5651),
        S298 = (1.64892,'cal/(mol*K)','+|-',1.96804),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 527,
    label = "4ring-Cs(Val7CsH)-Cd(Val7Cd)_124",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.203616,-0.190374,-0.179365,-0.169797,-0.138738,-0.0953444,0.0578002],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (0.949067,'kcal/mol','+|-',1.07027),
        S298 = (1.74742,'cal/(mol*K)','+|-',0.658138),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "4ring-Cs(BrCsH)-Cd(BrCd)_305",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.252509,-0.274418,-0.279567,-0.28149,-0.234063,-0.162555,0.00881567],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (0.663099,'kcal/mol','+|-',1.94798),
        S298 = (2.05437,'cal/(mol*K)','+|-',1.49456),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 529,
    label = "4ring-Cs(ClCsH)-Cd(ClCd)_440",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.108238,-0.0997628,-0.0640231,-0.0458915,-0.070938,-0.0836424,0.0363649],'cal/(mol*K)','+|-',[0.410462,0.452408,0.481549,0.478853,0.403031,0.319627,0.473401]),
        H298 = (0.617671,'kcal/mol','+|-',1.76552),
        S298 = (1.39998,'cal/(mol*K)','+|-',1.35457),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 530,
    label = "4ring-Cs(FCsH)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.2501,-0.19694,-0.194505,-0.182011,-0.111212,-0.0398357,0.12822],'cal/(mol*K)','+|-',[0.426263,0.469824,0.500087,0.497287,0.418546,0.331932,0.491625]),
        H298 = (1.56643,'kcal/mol','+|-',1.83349),
        S298 = (1.78792,'cal/(mol*K)','+|-',1.40672),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 531,
    label = "4ring-Cs(Val7CsH)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.96971,-0.58297,-0.498123,-0.602992,-0.700264,-0.703083,-1.9637],'cal/(mol*K)','+|-',[0.635368,0.700297,0.745406,0.741232,0.623865,0.494762,0.732793]),
        H298 = (0.970523,'kcal/mol','+|-',1.0342),
        S298 = (2.87435,'cal/(mol*K)','+|-',1.88011),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "4ring-Cs(BrCsH)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.442709,-0.266901,-0.332682,-0.427974,-0.438965,-0.46144,-1.41708],'cal/(mol*K)','+|-',[0.635368,0.700297,0.745406,0.741232,0.623865,0.494762,0.732793]),
        H298 = (0.604877,'kcal/mol','+|-',2.73291),
        S298 = (2.20963,'cal/(mol*K)','+|-',2.09679),
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
    index = 533,
    label = "4ring-Cs(ClCsH)-Cs(ClO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.49671,-0.899039,-0.663564,-0.77801,-0.961562,-0.944726,-2.51032],'cal/(mol*K)','+|-',[1.13739,1.25362,1.33437,1.3269,1.1168,0.885685,1.31179]),
        H298 = (1.33617,'kcal/mol','+|-',4.89224),
        S298 = (3.53907,'cal/(mol*K)','+|-',3.75351),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 534,
    label = "4ring-Cs(Val7CdH)-Cs(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.373821,-0.343364,-0.345576,-0.395353,-0.372582,-0.304503,0.0405978],'cal/(mol*K)','+|-',[0.716537,0.789762,0.840633,0.835926,0.703565,0.557968,0.826408]),
        H298 = (3.71735,'kcal/mol','+|-',2.59667),
        S298 = (2.63107,'cal/(mol*K)','+|-',1.95837),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 535,
    label = "4ring-Cs(BrCdH)-Cs(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.688657,-0.601068,-0.542178,-0.551829,-0.487148,-0.371522,-0.00302736],'cal/(mol*K)','+|-',[0.716537,0.789762,0.840633,0.835926,0.703565,0.557968,0.826408]),
        H298 = (2.79929,'kcal/mol','+|-',3.08204),
        S298 = (3.32346,'cal/(mol*K)','+|-',2.36465),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 536,
    label = "4ring-Cs(FCdH)-Cs(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u0 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0589844,-0.0856598,-0.148975,-0.238877,-0.258016,-0.237484,0.084223],'cal/(mol*K)','+|-',[0.707349,0.779635,0.829854,0.825207,0.694543,0.550814,0.815811]),
        H298 = (4.63541,'kcal/mol','+|-',3.04252),
        S298 = (1.93868,'cal/(mol*K)','+|-',2.33433),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 537,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.190752,0.0339871,-0.0491533,-0.099449,-0.184761,-0.159625,-0.105511],'cal/(mol*K)','+|-',[0.541498,0.596835,0.635279,0.631723,0.531695,0.421666,0.62453]),
        H298 = (0.402319,'kcal/mol','+|-',2.32915),
        S298 = (2.04375,'cal/(mol*K)','+|-',1.78701),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "4ring-Cs(BrBrCs)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.190752,0.0339871,-0.0491533,-0.099449,-0.184761,-0.159625,-0.105511],'cal/(mol*K)','+|-',[0.541498,0.596835,0.635279,0.631723,0.531695,0.421666,0.62453]),
        H298 = (0.402319,'kcal/mol','+|-',2.32915),
        S298 = (2.04375,'cal/(mol*K)','+|-',1.78701),
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
    index = 539,
    label = "4ring-Cs(Val7Cs)-Cs(Val7O2sH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.504305,-0.373472,-0.396487,-0.465779,-0.480876,-0.446641,-1.23798],'cal/(mol*K)','+|-',[0.422976,0.466201,0.496231,0.493453,0.415319,0.329372,0.487834]),
        H298 = (1.88875,'kcal/mol','+|-',1.55656),
        S298 = (1.98172,'cal/(mol*K)','+|-',0.525898),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "4ring-Cs(BrCs)-Cs(BrO2sH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.522071,-0.44791,-0.500362,-0.574189,-0.548203,-0.494944,-1.32334],'cal/(mol*K)','+|-',[0.422976,0.466201,0.496231,0.493453,0.415319,0.329372,0.487834]),
        H298 = (1.23255,'kcal/mol','+|-',1.81935),
        S298 = (2.25902,'cal/(mol*K)','+|-',1.39587),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 541,
    label = "4ring-Cs(ClCs)-Cs(ClO2sH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62354,-0.51288,-0.50407,-0.55296,-0.564731,-0.525808,-1.23314],'cal/(mol*K)','+|-',[0.412494,0.454648,0.483933,0.481224,0.405026,0.32121,0.475744]),
        H298 = (1.68509,'kcal/mol','+|-',1.77426),
        S298 = (1.95016,'cal/(mol*K)','+|-',1.36128),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 542,
    label = "4ring-Cs(FCs)-Cs(FO2sH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.367305,-0.159625,-0.185028,-0.270188,-0.329693,-0.319171,-1.15745],'cal/(mol*K)','+|-',[0.406382,0.447912,0.476763,0.474094,0.399026,0.316451,0.468696]),
        H298 = (2.74861,'kcal/mol','+|-',1.74797),
        S298 = (1.73597,'cal/(mol*K)','+|-',1.34111),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 543,
    label = "4ring-Cs(Val7Cs)-Cs(Val7Val7O2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.534773,-0.345539,-0.417757,-0.560394,-0.637208,-0.61942,-1.95613],'cal/(mol*K)','+|-',[1.62553,1.79165,1.90705,1.89637,1.5961,1.2658,1.87478]),
        H298 = (1.28594,'kcal/mol','+|-',5.25688),
        S298 = (2.97122,'cal/(mol*K)','+|-',4.29027),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "4ring-Cs(BrCs)-Cs(BrBrO2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.754034,-0.778813,-0.990088,-1.19763,-1.22642,-1.16328,-2.74817],'cal/(mol*K)','+|-',[1.62553,1.79165,1.90705,1.89637,1.5961,1.2658,1.87478]),
        H298 = (-1.74802,'kcal/mol','+|-',6.99189),
        S298 = (2.23452,'cal/(mol*K)','+|-',5.36443),
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
    index = 545,
    label = "4ring-Cs(ClCs)-Cs(ClClO2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.483628,-0.19131,-0.234019,-0.361775,-0.546035,-0.592577,-2.17621],'cal/(mol*K)','+|-',[1.17526,1.29536,1.3788,1.37108,1.15398,0.915174,1.35547]),
        H298 = (2.8738,'kcal/mol','+|-',5.05513),
        S298 = (5.38763,'cal/(mol*K)','+|-',3.87848),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 546,
    label = "4ring-Cs(FCs)-Cs(FFO2s)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.366658,-0.0664933,-0.0291642,-0.121776,-0.139168,-0.102402,-0.944025],'cal/(mol*K)','+|-',[0.406383,0.447912,0.476763,0.474094,0.399026,0.316451,0.468696]),
        H298 = (2.73203,'kcal/mol','+|-',1.74797),
        S298 = (1.29151,'cal/(mol*K)','+|-',1.34111),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 547,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7O2sH)_130",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.689065,-0.839539,-0.992925,-1.11629,-1.10789,-1.00481,-1.61753],'cal/(mol*K)','+|-',[0.295935,0.326178,0.347188,0.345244,0.290578,0.230445,0.341313]),
        H298 = (1.42504,'kcal/mol','+|-',1.27291),
        S298 = (3.19947,'cal/(mol*K)','+|-',0.976621),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "4ring-Cs(BrBrCs)-Cs(BrO2sH)_311",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.689065,-0.839539,-0.992925,-1.11629,-1.10789,-1.00481,-1.61753],'cal/(mol*K)','+|-',[0.295935,0.326178,0.347188,0.345244,0.290578,0.230445,0.341313]),
        H298 = (1.42504,'kcal/mol','+|-',1.27291),
        S298 = (3.19947,'cal/(mol*K)','+|-',0.976621),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 549,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_131",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.4169,-0.701233,-0.840303,-0.897805,-0.939779,-0.809284,-0.303572],'cal/(mol*K)','+|-',[0.499733,0.550802,0.586281,0.582999,0.490686,0.389143,0.576361]),
        H298 = (2.86751,'kcal/mol','+|-',2.60316),
        S298 = (3.4677,'cal/(mol*K)','+|-',0.834754),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "4ring-Cs(BrBrCs)-Cs(BrBrCs)_312",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.144069,-0.607821,-0.904161,-1.08241,-1.27042,-1.20322,-0.732931],'cal/(mol*K)','+|-',[0.499733,0.550802,0.586281,0.582999,0.490686,0.389143,0.576361]),
        H298 = (2.03596,'kcal/mol','+|-',2.1495),
        S298 = (3.88053,'cal/(mol*K)','+|-',1.64918),
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
    index = 551,
    label = "4ring-Cs(ClClCs)-Cs(ClClCs)_423",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.425703,-0.785769,-0.97614,-1.02513,-1.04686,-0.902757,-0.351875],'cal/(mol*K)','+|-',[0.499733,0.550802,0.586281,0.582999,0.490686,0.389143,0.576361]),
        H298 = (2.19908,'kcal/mol','+|-',2.1495),
        S298 = (3.47664,'cal/(mol*K)','+|-',1.64918),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 552,
    label = "4ring-Cs(FFCs)-Cs(FFCs)_600",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.680927,-0.710109,-0.640608,-0.585876,-0.502058,-0.321876,0.17409],'cal/(mol*K)','+|-',[0.499734,0.550803,0.586282,0.582999,0.490687,0.389143,0.576361]),
        H298 = (4.36749,'kcal/mol','+|-',2.1495),
        S298 = (3.04592,'cal/(mol*K)','+|-',1.64918),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 553,
    label = "4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.129535,-0.168124,-0.18985,-0.197625,-0.17829,-0.138101,0.0389214],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (0.701041,'kcal/mol','+|-',2.78989),
        S298 = (1.76077,'cal/(mol*K)','+|-',0.737533),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "4ring-Cs(BrBrCs)-Cd(BrCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0789949,-0.211796,-0.250156,-0.241647,-0.220024,-0.214678,-0.115792],'cal/(mol*K)','+|-',[0.452881,0.499162,0.531315,0.52834,0.444682,0.352659,0.522324]),
        H298 = (-0.288343,'kcal/mol','+|-',1.94798),
        S298 = (2.07918,'cal/(mol*K)','+|-',1.49456),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         4
""",
)

entry(
    index = 555,
    label = "4ring-Cs(ClClCs)-Cd(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.118767,-0.14192,-0.183917,-0.223843,-0.239723,-0.194116,0.0447353],'cal/(mol*K)','+|-',[0.450598,0.496646,0.528637,0.525677,0.442441,0.350882,0.519691]),
        H298 = (0.0949558,'kcal/mol','+|-',1.93816),
        S298 = (1.84642,'cal/(mol*K)','+|-',1.48703),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         4
""",
)

entry(
    index = 556,
    label = "4ring-Cs(FFCs)-Cd(FCd)_552",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.190842,-0.150656,-0.135477,-0.127385,-0.0751215,-0.0055093,0.187821],'cal/(mol*K)','+|-',[0.449745,0.495705,0.527635,0.524681,0.441603,0.350217,0.518707]),
        H298 = (2.29651,'kcal/mol','+|-',1.93449),
        S298 = (1.35672,'cal/(mol*K)','+|-',1.48421),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         4
""",
)

entry(
    index = 557,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7Val7O2s)_133",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.591741,-0.88226,-1.19791,-1.43672,-1.40456,-1.23889,-2.31824],'cal/(mol*K)','+|-',[1.72558,1.90193,2.02443,2.0131,1.69434,1.34371,1.99018]),
        H298 = (4.63162,'kcal/mol','+|-',1.35627),
        S298 = (7.65627,'cal/(mol*K)','+|-',14.0291),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "4ring-Cs(BrBrCs)-Cs(BrBrO2s)_314",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.692882,-1.30398,-1.92218,-2.33029,-2.35478,-2.15243,-3.95557],'cal/(mol*K)','+|-',[1.72558,1.90193,2.02443,2.0131,1.69434,1.34371,1.99018]),
        H298 = (5.11114,'kcal/mol','+|-',7.42225),
        S298 = (12.6163,'cal/(mol*K)','+|-',5.69462),
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
    index = 559,
    label = "4ring-Cs(FFCs)-Cs(FFO2s)_635",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.4906,-0.460541,-0.47364,-0.543159,-0.454335,-0.325347,-0.680903],'cal/(mol*K)','+|-',[1.17508,1.29516,1.37859,1.37087,1.1538,0.915034,1.35526]),
        H298 = (4.15211,'kcal/mol','+|-',5.05436),
        S298 = (2.69623,'cal/(mol*K)','+|-',3.87789),
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
    index = 560,
    label = "4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)_135",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41391,-0.321054,-0.215323,-0.202012,-0.165151,-0.12157,0.223077],'cal/(mol*K)','+|-',[0.557458,0.614426,0.654003,0.650341,0.547366,0.434093,0.642936]),
        H298 = (0.857036,'kcal/mol','+|-',0.864859),
        S298 = (1.85391,'cal/(mol*K)','+|-',0.648205),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "4ring-Cs(BrCdH)-Cs(BrBrCd)_316",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.570177,-0.546057,-0.441877,-0.405598,-0.345551,-0.303588,0.0398732],'cal/(mol*K)','+|-',[0.557458,0.614426,0.654003,0.650341,0.547366,0.434093,0.642936]),
        H298 = (0.551262,'kcal/mol','+|-',2.39779),
        S298 = (2.08309,'cal/(mol*K)','+|-',1.83968),
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
    index = 562,
    label = "4ring-Cs(FCdH)-Cs(FFCd)_650",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D}
4    Cd  u0 p0 c0 {1,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.257643,-0.0960508,0.0112308,0.00157445,0.0152485,0.0604488,0.40628],'cal/(mol*K)','+|-',[0.489879,0.539941,0.57472,0.571502,0.48101,0.381469,0.564995]),
        H298 = (1.16281,'kcal/mol','+|-',2.10712),
        S298 = (1.62474,'cal/(mol*K)','+|-',1.61666),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 563,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.28967,-1.39636,-0.981254,-1.36454,-1.42715,-1.27584,-0.985401],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (5.22314,'kcal/mol','+|-',5.31978),
        S298 = (5.74318,'cal/(mol*K)','+|-',2.04173),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "4ring-Cs(BrO2sH)-Cs(BrO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.61083,-1.82457,-1.4052,-1.80396,-1.9614,-1.8022,-1.36104],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (3.34232,'kcal/mol','+|-',8.4435),
        S298 = (6.46504,'cal/(mol*K)','+|-',6.47816),
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
    index = 565,
    label = "4ring-Cs(FO2sH)-Cs(FO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.96852,-0.968146,-0.557309,-0.925117,-0.892909,-0.74948,-0.609762],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (7.10397,'kcal/mol','+|-',8.4435),
        S298 = (5.02132,'cal/(mol*K)','+|-',6.47816),
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
    index = 566,
    label = "4ring-Cd(Val7Cd)-Cs(Val7CsH)_142",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.354388,0.273389,0.155946,0.0545815,-0.0628774,-0.113523,-0.117715],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (1.38057,'kcal/mol','+|-',2.73937),
        S298 = (3.70714,'cal/(mol*K)','+|-',0.765061),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "4ring-Cd(BrCd)-Cs(BrCsH)_323",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.270328,0.155595,0.0372841,-0.0587404,-0.14644,-0.173387,-0.189164],'cal/(mol*K)','+|-',[0.649671,0.716063,0.762187,0.75792,0.63791,0.5059,0.74929]),
        H298 = (0.860071,'kcal/mol','+|-',2.79443),
        S298 = (4.12347,'cal/(mol*K)','+|-',2.14399),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 568,
    label = "4ring-Cd(ClCd)-Cs(ClCsH)_483",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.402267,0.319139,0.228487,0.138157,-0.00458927,-0.0801329,-0.108598],'cal/(mol*K)','+|-',[0.646023,0.712042,0.757907,0.753663,0.634328,0.503059,0.745082]),
        H298 = (0.347434,'kcal/mol','+|-',2.77874),
        S298 = (3.37118,'cal/(mol*K)','+|-',2.13195),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 569,
    label = "4ring-Cd(FCd)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u1 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.390569,0.345434,0.202068,0.0843278,-0.037603,-0.0870504,-0.0553824],'cal/(mol*K)','+|-',[0.62911,0.6934,0.738064,0.733932,0.617721,0.489889,0.725575]),
        H298 = (2.93421,'kcal/mol','+|-',2.70599),
        S298 = (3.62677,'cal/(mol*K)','+|-',2.07613),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 570,
    label = "4ring-Cs(Val7O2s)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.657658,-0.142937,-0.136325,-0.25226,-0.2737,-0.290705,-1.73737],'cal/(mol*K)','+|-',[0.635368,0.700297,0.745406,0.741232,0.623865,0.494762,0.732793]),
        H298 = (1.48167,'kcal/mol','+|-',2.47996),
        S298 = (2.25067,'cal/(mol*K)','+|-',0.116065),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "4ring-Cs(BrO2s)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.442709,-0.266901,-0.332682,-0.427974,-0.438965,-0.46144,-1.41708],'cal/(mol*K)','+|-',[0.635368,0.700297,0.745406,0.741232,0.623865,0.494762,0.732793]),
        H298 = (0.604877,'kcal/mol','+|-',2.73291),
        S298 = (2.20963,'cal/(mol*K)','+|-',2.09679),
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
    index = 572,
    label = "4ring-Cs(FO2s)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.872607,-0.0189734,0.0600324,-0.0765455,-0.108435,-0.11997,-2.05766],'cal/(mol*K)','+|-',[1.13739,1.25362,1.33437,1.3269,1.1168,0.885685,1.31179]),
        H298 = (2.35847,'kcal/mol','+|-',4.89224),
        S298 = (2.2917,'cal/(mol*K)','+|-',3.75351),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 573,
    label = "4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_144",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.514682,0.483405,0.356955,0.204597,-0.0927819,-0.141155,0.0312416],'cal/(mol*K)','+|-',[1.43841,1.5854,1.68753,1.67808,1.41237,1.12009,1.65897]),
        H298 = (3.72302,'kcal/mol','+|-',2.20753),
        S298 = (2.84497,'cal/(mol*K)','+|-',2.83622),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "4ring-Cs(BrCsH)-Cs(BrBrCs)_325",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.32757,1.2335,0.929079,0.533305,-0.15938,-0.298447,-0.186683],'cal/(mol*K)','+|-',[1.43841,1.5854,1.68753,1.67808,1.41237,1.12009,1.65897]),
        H298 = (4.20025,'kcal/mol','+|-',6.18703),
        S298 = (4.39587,'cal/(mol*K)','+|-',4.74692),
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
    index = 575,
    label = "4ring-Cs(ClCsH)-Cs(ClClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.262135,0.16747,0.0449016,-0.0168143,-0.158458,-0.188178,0.0176148],'cal/(mol*K)','+|-',[0.477072,0.525826,0.559696,0.556562,0.468436,0.371497,0.550225]),
        H298 = (2.46094,'kcal/mol','+|-',2.05203),
        S298 = (2.52456,'cal/(mol*K)','+|-',1.57439),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 576,
    label = "4ring-Cs(FCsH)-Cs(FFCs)_620",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0456603,0.0492439,0.0968855,0.0973006,0.0394923,0.06316,0.262793],'cal/(mol*K)','+|-',[0.319207,0.351827,0.37449,0.372393,0.313428,0.248567,0.368153]),
        H298 = (4.50787,'kcal/mol','+|-',1.37301),
        S298 = (1.61448,'cal/(mol*K)','+|-',1.05342),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 577,
    label = "4ring-Cs(Val7CsH)-Cs(Val7Val7O2s)_146",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.864401,-1.07516,-1.37064,-1.55039,-1.4839,-1.26939,-2.13002],'cal/(mol*K)','+|-',[1.50233,1.65586,1.76252,1.75265,1.47513,1.16987,1.73269]),
        H298 = (1.98801,'kcal/mol','+|-',1.9836),
        S298 = (6.85485,'cal/(mol*K)','+|-',9.41344),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "4ring-Cs(BrCsH)-Cs(BrBrO2s)_327",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1847,-1.48261,-1.83127,-2.11709,-2.14552,-1.86797,-2.87447],'cal/(mol*K)','+|-',[1.50233,1.65586,1.76252,1.75265,1.47513,1.16987,1.73269]),
        H298 = (2.68932,'kcal/mol','+|-',6.46198),
        S298 = (10.183,'cal/(mol*K)','+|-',4.95787),
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
    index = 579,
    label = "4ring-Cs(ClCsH)-Cs(ClClO2s)_485",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.544102,-0.667717,-0.910006,-0.983695,-0.822287,-0.670812,-1.38557],'cal/(mol*K)','+|-',[0.619372,0.682668,0.72664,0.722572,0.608159,0.482306,0.714345]),
        H298 = (1.2867,'kcal/mol','+|-',2.66411),
        S298 = (3.52669,'cal/(mol*K)','+|-',2.044),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 580,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_151",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.391913,-0.543973,-0.584718,-0.606748,-0.622216,-0.524246,-0.16989],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (1.93707,'kcal/mol','+|-',2.24437),
        S298 = (2.5055,'cal/(mol*K)','+|-',0.604539),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "4ring-Cs(BrBrCs)-Cs(BrCsH)_332",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.327898,-0.613452,-0.738483,-0.785847,-0.822384,-0.746351,-0.434969],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (1.21623,'kcal/mol','+|-',0.811323),
        S298 = (2.67057,'cal/(mol*K)','+|-',0.622477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
""",
)

entry(
    index = 582,
    label = "4ring-Cs(ClClCs)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.378327,-0.540203,-0.611319,-0.660851,-0.704092,-0.604334,-0.191325],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (1.36497,'kcal/mol','+|-',0.811323),
        S298 = (2.6893,'cal/(mol*K)','+|-',0.622477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         6
""",
)

entry(
    index = 583,
    label = "4ring-Cs(FFCs)-Cs(FCsH)_559",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469514,-0.478264,-0.404351,-0.373545,-0.340172,-0.222053,0.116623],'cal/(mol*K)','+|-',[0.188623,0.207898,0.22129,0.220051,0.185208,0.146881,0.217545]),
        H298 = (3.23001,'kcal/mol','+|-',0.811323),
        S298 = (2.15664,'cal/(mol*K)','+|-',0.622477),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 584,
    label = "4ring-Cs(Val7CsH)-Cs(Val7CsH)_154",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0529896,0.0482057,0.0235768,-0.0200362,-0.114785,-0.107829,0.0290247],'cal/(mol*K)','+|-',[0.383139,0.422293,0.449495,0.446978,0.376203,0.298351,0.441889]),
        H298 = (1.88849,'kcal/mol','+|-',1.91652),
        S298 = (1.33731,'cal/(mol*K)','+|-',0.952758),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "4ring-Cs(BrCsH)-Cs(BrCsH)_335",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0382685,-0.11845,-0.184365,-0.232113,-0.310778,-0.285041,-0.104606],'cal/(mol*K)','+|-',[0.383139,0.422293,0.449495,0.446978,0.376203,0.298351,0.441889]),
        H298 = (1.06145,'kcal/mol','+|-',1.648),
        S298 = (1.86237,'cal/(mol*K)','+|-',1.2644),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 586,
    label = "4ring-Cs(ClCsH)-Cs(ClCsH)_429",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.135089,0.133851,0.0833175,0.0044104,-0.11622,-0.11299,0.017678],'cal/(mol*K)','+|-',[0.278653,0.307129,0.326912,0.325082,0.273608,0.216988,0.321381]),
        H298 = (1.6654,'kcal/mol','+|-',1.19857),
        S298 = (1.2168,'cal/(mol*K)','+|-',0.919587),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 587,
    label = "4ring-Cs(FCsH)-Cs(FCsH)_619",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0621482,0.129216,0.171778,0.167594,0.0826443,0.0745445,0.174002],'cal/(mol*K)','+|-',[0.268522,0.295963,0.315027,0.313263,0.263661,0.209099,0.309697]),
        H298 = (2.93861,'kcal/mol','+|-',1.15499),
        S298 = (0.932757,'cal/(mol*K)','+|-',0.886154),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 588,
    label = "4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_155",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.127574,0.0912263,0.0362896,-0.0341575,-0.176313,-0.183191,0.0230737],'cal/(mol*K)','+|-',[0.343111,0.378174,0.402534,0.40028,0.336899,0.267181,0.395723]),
        H298 = (3.06983,'kcal/mol','+|-',2.12151),
        S298 = (2.2816,'cal/(mol*K)','+|-',0.851171),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 589,
    label = "4ring-Cs(BrCsH)-Cs(BrBrCs)_336",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.292554,0.127055,-0.0250132,-0.152375,-0.356436,-0.390882,-0.2153],'cal/(mol*K)','+|-',[0.343111,0.378174,0.402534,0.40028,0.336899,0.267181,0.395723]),
        H298 = (2.26304,'kcal/mol','+|-',1.47582),
        S298 = (2.50943,'cal/(mol*K)','+|-',1.13231),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 590,
    label = "4ring-Cs(ClCsH)-Cs(ClClCs)_473",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.188704,0.138727,0.0504063,-0.0253163,-0.186311,-0.208804,0.0205212],'cal/(mol*K)','+|-',[0.34256,0.377567,0.401887,0.399637,0.336358,0.266752,0.395087]),
        H298 = (2.67509,'kcal/mol','+|-',1.47345),
        S298 = (2.54477,'cal/(mol*K)','+|-',1.13049),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 591,
    label = "4ring-Cs(FCsH)-Cs(FFCs)_616",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0985358,0.00789701,0.0834758,0.0752187,0.0138078,0.0501143,0.264],'cal/(mol*K)','+|-',[0.300665,0.331391,0.352737,0.350762,0.295222,0.234129,0.346768]),
        H298 = (4.27136,'kcal/mol','+|-',1.29325),
        S298 = (1.7906,'cal/(mol*K)','+|-',0.99223),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 592,
    label = "4ring-Cs(Val7O2s)-Cd(Val7Cd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cd   u0 p0 c0 {1,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.43744,-2.43815,-2.88651,-2.98685,-2.63362,-2.12055,-1.26409],'cal/(mol*K)','+|-',[1.87944,2.0715,2.20494,2.19259,1.84541,1.46352,2.16763]),
        H298 = (12.0062,'kcal/mol','+|-',6.09856),
        S298 = (7.56272,'cal/(mol*K)','+|-',7.24977),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "4ring-Cs(BrO2s)-Cd(BrCd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cd   u0 p0 c0 {1,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.17987,-3.44812,-3.97048,-4.10308,-3.66182,-2.98121,-1.77757],'cal/(mol*K)','+|-',[1.87944,2.0715,2.20494,2.19259,1.84541,1.46352,2.16763]),
        H298 = (14.1624,'kcal/mol','+|-',8.08403),
        S298 = (10.1259,'cal/(mol*K)','+|-',6.20236),
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
    index = 594,
    label = "4ring-Cs(FO2s)-Cd(FCd)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,S} {4,D} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cd  u0 p0 c0 {1,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.695007,-1.42817,-1.80254,-1.87061,-1.60542,-1.25989,-0.750607],'cal/(mol*K)','+|-',[1.05064,1.15801,1.2326,1.2257,1.03162,0.818134,1.21174]),
        H298 = (9.85007,'kcal/mol','+|-',4.51911),
        S298 = (4.99954,'cal/(mol*K)','+|-',3.46723),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 595,
    label = "4ring-Cd(Val7Cs)=Cd(Val7O2s)_160",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.296375,-0.380696,-0.468386,-0.491528,-0.412954,-0.277262,0.0370842],'cal/(mol*K)','+|-',[0.801396,0.883293,0.940189,0.934925,0.786888,0.624048,0.924279]),
        H298 = (1.7054,'kcal/mol','+|-',8.55992),
        S298 = (2.68382,'cal/(mol*K)','+|-',1.95924),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "4ring-Cd(BrCs)=Cd(BrO2s)_341",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.268453,-0.441978,-0.563056,-0.604936,-0.528336,-0.380037,-0.0885324],'cal/(mol*K)','+|-',[0.801396,0.883293,0.940189,0.934925,0.786888,0.624048,0.924279]),
        H298 = (-0.373645,'kcal/mol','+|-',3.44705),
        S298 = (2.62974,'cal/(mol*K)','+|-',2.6447),
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
    index = 597,
    label = "4ring-Cd(ClCs)=Cd(ClO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.105621,-0.172493,-0.221417,-0.246959,-0.224827,-0.147446,0.070318],'cal/(mol*K)','+|-',[0.749638,0.826245,0.879466,0.874542,0.736067,0.583744,0.864585]),
        H298 = (-1.13789,'kcal/mol','+|-',3.22442),
        S298 = (1.73236,'cal/(mol*K)','+|-',2.47389),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 598,
    label = "4ring-Cd(FCs)=Cd(FO2s)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51505,-0.527616,-0.620684,-0.622689,-0.485699,-0.304302,0.129467],'cal/(mol*K)','+|-',[1.49927,1.65249,1.75893,1.74908,1.47213,1.16749,1.72917]),
        H298 = (6.62774,'kcal/mol','+|-',6.44883),
        S298 = (3.68936,'cal/(mol*K)','+|-',4.94778),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 599,
    label = "4ring-Cd(Val7O2s)=Cd(Val7Cs)_162",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.017541,-0.0452679,-0.140424,-0.2213,-0.293932,-0.28721,-0.176605],'cal/(mol*K)','+|-',[0.566672,0.624582,0.664814,0.661091,0.556414,0.441269,0.653564]),
        H298 = (0.621673,'kcal/mol','+|-',1.24772),
        S298 = (1.28248,'cal/(mol*K)','+|-',1.07351),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "4ring-Cd(BrO2s)=Cd(BrCs)_343",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0677495,-0.16156,-0.312429,-0.396654,-0.439491,-0.399624,-0.259813],'cal/(mol*K)','+|-',[0.566672,0.624582,0.664814,0.661091,0.556414,0.441269,0.653564]),
        H298 = (1.06281,'kcal/mol','+|-',2.43743),
        S298 = (1.66202,'cal/(mol*K)','+|-',1.87008),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 601,
    label = "4ring-Cd(ClO2s)=Cd(ClCs)_448",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0326675,0.0710243,0.0315803,-0.0459456,-0.148374,-0.174795,-0.0933971],'cal/(mol*K)','+|-',[0.490753,0.540904,0.575746,0.572522,0.481869,0.38215,0.566004]),
        H298 = (0.180537,'kcal/mol','+|-',2.11088),
        S298 = (0.902932,'cal/(mol*K)','+|-',1.61954),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 602,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.701261,-0.728494,-0.832889,-0.921883,-0.887866,-0.78636,-1.45653],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.715761,'kcal/mol','+|-',1.56202),
        S298 = (2.4315,'cal/(mol*K)','+|-',2.16929),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 603,
    label = "4ring-Cs(BrO2sH)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.849776,-0.931992,-1.04996,-1.13635,-1.06647,-0.943568,-1.58058],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (-0.0361684,'kcal/mol','+|-',1.236),
        S298 = (1.19659,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 604,
    label = "4ring-Cs(ClO2sH)-Cs(ClCsH)_477",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.773793,-0.796826,-0.850856,-0.927682,-0.945725,-0.861071,-1.46778],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.660531,'kcal/mol','+|-',1.236),
        S298 = (3.22979,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 605,
    label = "4ring-Cs(FO2sH)-Cs(FCsH)_643",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.480214,-0.456664,-0.597852,-0.701618,-0.651403,-0.554441,-1.32124],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (1.52292,'kcal/mol','+|-',1.236),
        S298 = (2.86812,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 606,
    label = "4ring-Cs(Val7CdH)-Cs(Val7CdH)_167",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.512789,-0.438589,-0.381922,-0.387017,-0.325184,-0.229466,0.224361],'cal/(mol*K)','+|-',[0.540476,0.595708,0.63408,0.63053,0.530691,0.420869,0.62335]),
        H298 = (0.426872,'kcal/mol','+|-',0.289005),
        S298 = (1.82293,'cal/(mol*K)','+|-',0.923364),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "4ring-Cs(BrCdH)-Cs(BrCdH)_348",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.759136,-0.762004,-0.694688,-0.67912,-0.605274,-0.455737,0.11002],'cal/(mol*K)','+|-',[0.540476,0.595708,0.63408,0.63053,0.530691,0.420869,0.62335]),
        H298 = (0.521511,'kcal/mol','+|-',2.32475),
        S298 = (2.35199,'cal/(mol*K)','+|-',1.78363),
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
    index = 608,
    label = "4ring-Cs(ClCdH)-Cs(ClCdH)_490",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *2 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.408081,-0.341183,-0.324515,-0.350866,-0.308464,-0.249952,0.170483],'cal/(mol*K)','+|-',[0.591538,0.651989,0.693986,0.6901,0.580829,0.460632,0.682243]),
        H298 = (0.260542,'kcal/mol','+|-',2.54438),
        S298 = (1.50162,'cal/(mol*K)','+|-',1.95214),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 609,
    label = "4ring-Cs(FCdH)-Cs(FCdH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    Cd  u0 p0 c0 {2,S} {4,D}
4    Cd  u0 p0 c0 {1,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.371151,-0.212581,-0.126564,-0.131065,-0.0618147,0.0172916,0.392581],'cal/(mol*K)','+|-',[0.535036,0.589713,0.627698,0.624184,0.52535,0.416634,0.617077]),
        H298 = (0.498564,'kcal/mol','+|-',2.30135),
        S298 = (1.61519,'cal/(mol*K)','+|-',1.76568),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 610,
    label = "4ring-Cs(Val7Val7O2s)-Cd(Val7Cd)_168",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.851102,-1.38618,-1.73214,-1.7343,-1.29094,-0.775357,-0.0717988],'cal/(mol*K)','+|-',[1.76943,1.95026,2.07588,2.06426,1.7374,1.37786,2.04075]),
        H298 = (34.8171,'kcal/mol','+|-',7.61087),
        S298 = (4.1238,'cal/(mol*K)','+|-',5.83934),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "4ring-Cs(BrBrO2s)-Cd(BrCd)_349",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 612,
    label = "4ring-Cs(FFO2s)-Cd(FCd)_641",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cd  u1 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.851102,-1.38618,-1.73214,-1.7343,-1.29094,-0.775357,-0.0717988],'cal/(mol*K)','+|-',[1.76943,1.95026,2.07588,2.06426,1.7374,1.37786,2.04075]),
        H298 = (34.8171,'kcal/mol','+|-',7.61087),
        S298 = (4.1238,'cal/(mol*K)','+|-',5.83934),
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
    index = 613,
    label = "4ring-Cd(Val7O2s)=Cd(Val7O2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.531866,0.661588,0.696359,0.521854,-0.0203362,-0.183726,-0.190826],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (-2.76992,'kcal/mol','+|-',8.72321),
        S298 = (-2.38183,'cal/(mol*K)','+|-',0.240636),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "4ring-Cd(BrO2s)=Cd(BrO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.554183,0.651717,0.647928,0.485428,-0.0374965,-0.184644,-0.190746],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (-5.42037,'kcal/mol','+|-',2.98523),
        S298 = (-2.39698,'cal/(mol*K)','+|-',2.29038),
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
    index = 615,
    label = "4ring-Cd(ClO2s)=Cd(ClO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.561856,0.66139,0.684643,0.526283,0.000982745,-0.150167,-0.153463],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (-5.15346,'kcal/mol','+|-',2.98523),
        S298 = (-2.49385,'cal/(mol*K)','+|-',2.29038),
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
    index = 616,
    label = "4ring-Cd(FO2s)=Cd(FO2s)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.47956,0.671657,0.756506,0.553851,-0.0244948,-0.216366,-0.228269],'cal/(mol*K)','+|-',[0.69403,0.764955,0.814228,0.80967,0.681466,0.540443,0.800451]),
        H298 = (2.26407,'kcal/mol','+|-',2.98523),
        S298 = (-2.25465,'cal/(mol*K)','+|-',2.29038),
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
    index = 617,
    label = "4ring-Cs(Val7CsH)-Cs(Val7CsH)_173",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0529896,0.0482057,0.0235768,-0.0200362,-0.114785,-0.107829,0.0290247],'cal/(mol*K)','+|-',[0.383139,0.422293,0.449495,0.446978,0.376203,0.298351,0.441889]),
        H298 = (1.88849,'kcal/mol','+|-',1.91652),
        S298 = (1.33731,'cal/(mol*K)','+|-',0.952758),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "4ring-Cs(BrCsH)-Cs(BrCsH)_354",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0382685,-0.11845,-0.184365,-0.232113,-0.310778,-0.285041,-0.104606],'cal/(mol*K)','+|-',[0.383139,0.422293,0.449495,0.446978,0.376203,0.298351,0.441889]),
        H298 = (1.06145,'kcal/mol','+|-',1.648),
        S298 = (1.86237,'cal/(mol*K)','+|-',1.2644),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 619,
    label = "4ring-Cs(ClCsH)-Cs(ClCsH)_422",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.135089,0.133851,0.0833175,0.0044104,-0.11622,-0.11299,0.017678],'cal/(mol*K)','+|-',[0.278653,0.307129,0.326912,0.325082,0.273608,0.216988,0.321381]),
        H298 = (1.6654,'kcal/mol','+|-',1.19857),
        S298 = (1.2168,'cal/(mol*K)','+|-',0.919587),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         5
""",
)

entry(
    index = 620,
    label = "4ring-Cs(FCsH)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0621482,0.129216,0.171778,0.167594,0.0826443,0.0745445,0.174002],'cal/(mol*K)','+|-',[0.268522,0.295963,0.315027,0.313263,0.263661,0.209099,0.309697]),
        H298 = (2.93861,'kcal/mol','+|-',1.15499),
        S298 = (0.932757,'cal/(mol*K)','+|-',0.886154),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         6
""",
)

entry(
    index = 621,
    label = "4ring-Cd(Val7Cd)-Cd(Val7Cd)_175",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.151993,0.0715164,0.378169,0.360705,0.164287,0.0795212,0.310843],'cal/(mol*K)','+|-',[0.75449,0.831594,0.885159,0.880203,0.740831,0.587523,0.870181]),
        H298 = (-2.66744,'kcal/mol','+|-',1.29757),
        S298 = (-0.974195,'cal/(mol*K)','+|-',1.44684),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "4ring-Cd(BrCd)-Cd(BrCd)_356",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.151339,0.0814864,0.381563,0.420191,0.314963,0.239835,0.357181],'cal/(mol*K)','+|-',[0.75449,0.831594,0.885159,0.880203,0.740831,0.587523,0.870181]),
        H298 = (-3.1262,'kcal/mol','+|-',3.24529),
        S298 = (-1.48573,'cal/(mol*K)','+|-',2.48991),
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
    index = 623,
    label = "4ring-Cd(ClCd)-Cd(ClCd)_487",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.152646,0.0615465,0.374776,0.301219,0.0136116,-0.0807927,0.264506],'cal/(mol*K)','+|-',[0.75449,0.831594,0.885159,0.880203,0.740831,0.587523,0.870181]),
        H298 = (-2.20868,'kcal/mol','+|-',3.24529),
        S298 = (-0.462659,'cal/(mol*K)','+|-',2.48991),
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
    index = 624,
    label = "4ring-Cd(Val7Cd)=Cd(Val7Cd)_176",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.151993,0.0715164,0.378169,0.360705,0.164287,0.0795212,0.310843],'cal/(mol*K)','+|-',[0.75449,0.831594,0.885159,0.880203,0.740831,0.587523,0.870181]),
        H298 = (-2.66744,'kcal/mol','+|-',1.29757),
        S298 = (-0.974195,'cal/(mol*K)','+|-',1.44684),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "4ring-Cd(BrCd)=Cd(BrCd)_357",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.151339,0.0814864,0.381563,0.420191,0.314963,0.239835,0.357181],'cal/(mol*K)','+|-',[0.75449,0.831594,0.885159,0.880203,0.740831,0.587523,0.870181]),
        H298 = (-3.1262,'kcal/mol','+|-',3.24529),
        S298 = (-1.48573,'cal/(mol*K)','+|-',2.48991),
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
    index = 626,
    label = "4ring-Cd(ClCd)=Cd(ClCd)_488",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.152646,0.0615465,0.374776,0.301219,0.0136116,-0.0807927,0.264506],'cal/(mol*K)','+|-',[0.75449,0.831594,0.885159,0.880203,0.740831,0.587523,0.870181]),
        H298 = (-2.20868,'kcal/mol','+|-',3.24529),
        S298 = (-0.462659,'cal/(mol*K)','+|-',2.48991),
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
    index = 627,
    label = "4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)_177",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.826444,0.60199,0.359411,0.165658,-0.0935827,-0.20444,-0.194327],'cal/(mol*K)','+|-',[0.701074,0.772718,0.822491,0.817886,0.688382,0.545927,0.808574]),
        H298 = (0.854295,'kcal/mol','+|-',3.63641),
        S298 = (5.7582,'cal/(mol*K)','+|-',5.56899),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 628,
    label = "4ring-Cs(BrBrCs)-Cd(BrCd)_358",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.708952,0.482848,0.238757,0.0550461,-0.141839,-0.233256,-0.319114],'cal/(mol*K)','+|-',[0.701074,0.772718,0.822491,0.817886,0.688382,0.545927,0.808574]),
        H298 = (-0.591241,'kcal/mol','+|-',3.01553),
        S298 = (4.62682,'cal/(mol*K)','+|-',2.31362),
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
    index = 629,
    label = "4ring-Cs(ClClCs)-Cd(ClCd)_460",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u1 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.43172,1.03297,0.611811,0.282368,-0.186474,-0.394728,-0.360322],'cal/(mol*K)','+|-',[1.40292,1.54629,1.64589,1.63667,1.37752,1.09245,1.61804]),
        H298 = (0.258467,'kcal/mol','+|-',6.03437),
        S298 = (8.9303,'cal/(mol*K)','+|-',4.62979),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 630,
    label = "4ring-Cs(FFCs)-Cd(FCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u1 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.338661,0.290153,0.227665,0.15956,0.047565,0.0146653,0.0964535],'cal/(mol*K)','+|-',[0.665664,0.73369,0.78095,0.776577,0.653613,0.518354,0.767735]),
        H298 = (2.89566,'kcal/mol','+|-',2.86322),
        S298 = (3.71747,'cal/(mol*K)','+|-',2.19677),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 631,
    label = "4ring-Cs(Val7Val7O2s)-Cs(Val7CsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.52849,-0.501197,-0.606843,-0.718125,-0.705507,-0.623323,-1.35349],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.74063,'kcal/mol','+|-',0.984714),
        S298 = (3.07751,'cal/(mol*K)','+|-',1.3418),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 632,
    label = "4ring-Cs(BrBrO2s)-Cs(BrCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
7    Br1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.626539,-0.682816,-0.801583,-0.907096,-0.896646,-0.821493,-1.55457],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337122,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.506892,'kcal/mol','+|-',1.236),
        S298 = (3.69259,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 633,
    label = "4ring-Cs(ClClO2s)-Cs(ClCsH)_436",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.487931,-0.443902,-0.573028,-0.733204,-0.775676,-0.704618,-1.40567],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337123,0.335235,0.282154,0.223764,0.331418]),
        H298 = (0.408678,'kcal/mol','+|-',1.236),
        S298 = (3.17785,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 634,
    label = "4ring-Cs(FFO2s)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.471001,-0.376872,-0.445919,-0.514076,-0.4442,-0.343858,-1.10022],'cal/(mol*K)','+|-',[0.287356,0.316721,0.337123,0.335235,0.282154,0.223764,0.331418]),
        H298 = (1.30632,'kcal/mol','+|-',1.236),
        S298 = (2.36209,'cal/(mol*K)','+|-',0.948307),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 635,
    label = "4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)_181",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.483679,-0.303725,-0.174044,-0.100208,-0.0484872,0.0085535,0.235397],'cal/(mol*K)','+|-',[1.65744,1.82682,1.94449,1.9336,1.62744,1.29065,1.91159]),
        H298 = (3.89565,'kcal/mol','+|-',10.293),
        S298 = (2.89414,'cal/(mol*K)','+|-',1.92083),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 636,
    label = "4ring-Cd(BrCd)-Cs(BrBrCs)_362",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.355155,-0.268468,-0.173543,-0.117441,-0.143737,-0.147423,-0.0271524],'cal/(mol*K)','+|-',[1.65744,1.82682,1.94449,1.9336,1.62744,1.29065,1.91159]),
        H298 = (0.256533,'kcal/mol','+|-',7.12915),
        S298 = (3.57325,'cal/(mol*K)','+|-',5.46975),
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
    index = 637,
    label = "4ring-Cd(FCd)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u1 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.612203,-0.338983,-0.174545,-0.0829752,0.0467626,0.16453,0.497946],'cal/(mol*K)','+|-',[1.44691,1.59477,1.6975,1.688,1.42072,1.12671,1.66878]),
        H298 = (7.53477,'kcal/mol','+|-',6.2236),
        S298 = (2.21502,'cal/(mol*K)','+|-',4.77497),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 638,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.504305,-0.373472,-0.396487,-0.465779,-0.480876,-0.446641,-1.23798],'cal/(mol*K)','+|-',[0.422976,0.466201,0.496231,0.493453,0.415319,0.329372,0.487834]),
        H298 = (1.88875,'kcal/mol','+|-',1.55656),
        S298 = (1.98172,'cal/(mol*K)','+|-',0.525898),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 639,
    label = "4ring-Cs(BrO2sH)-Cs(BrCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.522071,-0.44791,-0.500362,-0.574189,-0.548203,-0.494944,-1.32334],'cal/(mol*K)','+|-',[0.422976,0.466201,0.496231,0.493453,0.415319,0.329372,0.487834]),
        H298 = (1.23255,'kcal/mol','+|-',1.81935),
        S298 = (2.25902,'cal/(mol*K)','+|-',1.39587),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         3
""",
)

entry(
    index = 640,
    label = "4ring-Cs(ClO2sH)-Cs(ClCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62354,-0.51288,-0.50407,-0.55296,-0.564731,-0.525808,-1.23314],'cal/(mol*K)','+|-',[0.412494,0.454648,0.483933,0.481224,0.405026,0.32121,0.475744]),
        H298 = (1.68509,'kcal/mol','+|-',1.77426),
        S298 = (1.95016,'cal/(mol*K)','+|-',1.36128),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 641,
    label = "4ring-Cs(FO2sH)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.367305,-0.159625,-0.185028,-0.270188,-0.329693,-0.319171,-1.15745],'cal/(mol*K)','+|-',[0.406382,0.447912,0.476763,0.474094,0.399026,0.316451,0.468696]),
        H298 = (2.74861,'kcal/mol','+|-',1.74797),
        S298 = (1.73597,'cal/(mol*K)','+|-',1.34111),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 642,
    label = "4ring-Cs(Val7O2sH)-Cd(Val7Cd)_183",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.97648,-1.54433,-1.89783,-2.05412,-1.83704,-1.39554,-0.61593],'cal/(mol*K)','+|-',[1.79197,1.9751,2.10232,2.09055,1.75953,1.39541,2.06675]),
        H298 = (29.0295,'kcal/mol','+|-',6.77589),
        S298 = (6.41849,'cal/(mol*K)','+|-',1.19214),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 643,
    label = "4ring-Cs(BrO2sH)-Cd(BrCd)_364",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Br1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.998261,-1.52963,-1.81095,-1.96788,-1.86435,-1.48246,-0.684985],'cal/(mol*K)','+|-',[1.79197,1.9751,2.10232,2.09055,1.75953,1.39541,2.06675]),
        H298 = (26.4646,'kcal/mol','+|-',7.70782),
        S298 = (6.63679,'cal/(mol*K)','+|-',5.91372),
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
    index = 644,
    label = "4ring-Cs(ClO2sH)-Cd(ClCd)_500",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.06176,-1.65188,-1.98217,-2.16451,-1.95834,-1.50391,-0.668436],'cal/(mol*K)','+|-',[1.76943,1.95026,2.07588,2.06426,1.7374,1.37786,2.04075]),
        H298 = (27.7538,'kcal/mol','+|-',7.61087),
        S298 = (6.87464,'cal/(mol*K)','+|-',5.83934),
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
    index = 645,
    label = "4ring-Cs(FO2sH)-Cd(FCd)_649",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cd  u1 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    H   u0 p0 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.869418,-1.45147,-1.90038,-2.02997,-1.68844,-1.20024,-0.494368],'cal/(mol*K)','+|-',[1.76943,1.95026,2.07588,2.06426,1.7374,1.37786,2.04075]),
        H298 = (32.8701,'kcal/mol','+|-',7.61087),
        S298 = (5.74405,'cal/(mol*K)','+|-',5.83934),
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
    index = 646,
    label = "4ring-Cd(Val7Cd)-Cs(Val7O2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cd   u0 p0 c0 {1,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.40186,-2.48551,-2.981,-3.06554,-2.66103,-2.12148,-1.26961],'cal/(mol*K)','+|-',[1.85796,2.04783,2.17974,2.16753,1.82432,1.4468,2.14285]),
        H298 = (13.0087,'kcal/mol','+|-',8.93391),
        S298 = (7.82252,'cal/(mol*K)','+|-',7.98459),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 647,
    label = "4ring-Cd(ClCd)-Cs(ClO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cd   u0 p0 c0 {1,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.10871,-3.54285,-4.15947,-4.26046,-3.71664,-2.98308,-1.78862],'cal/(mol*K)','+|-',[1.85796,2.04783,2.17974,2.16753,1.82432,1.4468,2.14285]),
        H298 = (16.1673,'kcal/mol','+|-',7.99164),
        S298 = (10.6455,'cal/(mol*K)','+|-',6.13148),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 648,
    label = "4ring-Cd(FCd)-Cs(FO2s)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,S} {4,D} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cd  u0 p0 c0 {1,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.695007,-1.42817,-1.80254,-1.87061,-1.60542,-1.25989,-0.750607],'cal/(mol*K)','+|-',[1.05064,1.15801,1.2326,1.2257,1.03162,0.818134,1.21174]),
        H298 = (9.85007,'kcal/mol','+|-',4.51911),
        S298 = (4.99954,'cal/(mol*K)','+|-',3.46723),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 649,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7Val7Cs)_185",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.16011,-1.43759,-1.6774,-1.74473,-1.4912,-1.19832,-2.05559],'cal/(mol*K)','+|-',[1.50898,1.66319,1.77032,1.76041,1.48166,1.17504,1.74036]),
        H298 = (3.14364,'kcal/mol','+|-',0.525126),
        S298 = (5.34668,'cal/(mol*K)','+|-',6.81126),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 650,
    label = "4ring-Cs(ClO2sH)-Cs(ClClCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46482,-2.0559,-2.50961,-2.59445,-2.20741,-1.78995,-2.83155],'cal/(mol*K)','+|-',[1.50898,1.66319,1.77032,1.76041,1.48166,1.17504,1.74036]),
        H298 = (2.95798,'kcal/mol','+|-',6.49058),
        S298 = (7.75483,'cal/(mol*K)','+|-',4.97981),
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
    index = 651,
    label = "4ring-Cs(FO2sH)-Cs(FFCs)_644",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.855394,-0.81928,-0.845188,-0.895016,-0.774996,-0.606699,-1.27963],'cal/(mol*K)','+|-',[0.646107,0.712134,0.758005,0.753761,0.63441,0.503125,0.745179]),
        H298 = (3.3293,'kcal/mol','+|-',2.7791),
        S298 = (2.93854,'cal/(mol*K)','+|-',2.13223),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 652,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_187",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.515695,0.382445,0.209308,0.0744487,-0.206296,-0.23356,0.170837],'cal/(mol*K)','+|-',[1.71045,1.88525,2.00668,1.99545,1.67948,1.33193,1.97272]),
        H298 = (6.82867,'kcal/mol','+|-',3.12708),
        S298 = (4.21734,'cal/(mol*K)','+|-',5.94835),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 653,
    label = "4ring-Cs(ClClCs)-Cs(ClClCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.1742,0.77476,0.370746,0.0880899,-0.427714,-0.545755,-0.0461042],'cal/(mol*K)','+|-',[1.71045,1.88525,2.00668,1.99545,1.67948,1.33193,1.97272]),
        H298 = (7.93426,'kcal/mol','+|-',7.35716),
        S298 = (6.3204,'cal/(mol*K)','+|-',5.64468),
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
    index = 654,
    label = "4ring-Cs(FFCs)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.142809,-0.00987034,0.0478691,0.0608075,0.0151223,0.0786346,0.387778],'cal/(mol*K)','+|-',[0.651525,0.718107,0.764362,0.760083,0.639731,0.507344,0.751428]),
        H298 = (5.72308,'kcal/mol','+|-',2.80241),
        S298 = (2.11428,'cal/(mol*K)','+|-',2.15011),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 655,
    label = "4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)_188",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01031,-0.583663,-0.318665,-0.26114,-0.242151,-0.156364,0.645042],'cal/(mol*K)','+|-',[1.76852,1.94925,2.0748,2.06319,1.7365,1.37715,2.0397]),
        H298 = (2.18825,'kcal/mol','+|-',7.60693),
        S298 = (3.30825,'cal/(mol*K)','+|-',5.83631),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 656,
    label = "4ring-Cs(ClCdH)-Cs(ClClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01031,-0.583663,-0.318665,-0.26114,-0.242151,-0.156364,0.645042],'cal/(mol*K)','+|-',[1.76852,1.94925,2.0748,2.06319,1.7365,1.37715,2.0397]),
        H298 = (2.18825,'kcal/mol','+|-',7.60693),
        S298 = (3.30825,'cal/(mol*K)','+|-',5.83631),
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
    index = 657,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)_190",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.623656,-0.264879,-0.0465525,-0.0102445,-0.005686,0.0383725,0.574782],'cal/(mol*K)','+|-',[1.76852,1.94925,2.0748,2.06319,1.7365,1.37715,2.0397]),
        H298 = (1.72331,'kcal/mol','+|-',0.0421011),
        S298 = (2.29869,'cal/(mol*K)','+|-',3.15879),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 658,
    label = "4ring-Cs(ClClCd)-Cs(ClCdH)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.878737,-0.510965,-0.275667,-0.231797,-0.234368,-0.163234,0.625364],'cal/(mol*K)','+|-',[1.76852,1.94925,2.0748,2.06319,1.7365,1.37715,2.0397]),
        H298 = (1.70843,'kcal/mol','+|-',7.60693),
        S298 = (3.41549,'cal/(mol*K)','+|-',5.83631),
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
    index = 659,
    label = "4ring-Cs(FFCd)-Cs(FCdH)_606",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.368574,-0.0187932,0.182562,0.211308,0.222996,0.239979,0.524199],'cal/(mol*K)','+|-',[0.849505,0.936318,0.996629,0.991049,0.834126,0.661511,0.979765]),
        H298 = (1.7382,'kcal/mol','+|-',3.65398),
        S298 = (1.18189,'cal/(mol*K)','+|-',2.80346),
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
    index = 660,
    label = "4ring-Cs(Val7Val7O2s)-Cs(Val7CsH)_191",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.00321,-1.0348,-1.20848,-1.24989,-0.962433,-0.703392,-1.76462],'cal/(mol*K)','+|-',[0.619372,0.682668,0.72664,0.722572,0.608159,0.482306,0.714345]),
        H298 = (3.23384,'kcal/mol','+|-',5.50734),
        S298 = (4.42702,'cal/(mol*K)','+|-',2.54652),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 661,
    label = "4ring-Cs(ClClO2s)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.544102,-0.667717,-0.910006,-0.983695,-0.822287,-0.670812,-1.38557],'cal/(mol*K)','+|-',[0.619372,0.682668,0.72664,0.722572,0.608159,0.482306,0.714345]),
        H298 = (1.2867,'kcal/mol','+|-',2.66411),
        S298 = (3.52669,'cal/(mol*K)','+|-',2.044),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 662,
    label = "4ring-Cs(FFO2s)-Cs(FCsH)_636",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.46232,-1.40188,-1.50695,-1.51608,-1.10258,-0.735972,-2.14366],'cal/(mol*K)','+|-',[1.23874,1.36533,1.45328,1.44514,1.21632,0.964612,1.42869]),
        H298 = (5.18098,'kcal/mol','+|-',5.32821),
        S298 = (5.32735,'cal/(mol*K)','+|-',4.088),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 663,
    label = "4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_193",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.108237,0.108357,0.0708935,0.0402431,-0.0594828,-0.062509,0.140204],'cal/(mol*K)','+|-',[0.477072,0.525826,0.559696,0.556562,0.468436,0.371497,0.550225]),
        H298 = (3.4844,'kcal/mol','+|-',2.8948),
        S298 = (2.06952,'cal/(mol*K)','+|-',1.28705),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 664,
    label = "4ring-Cs(ClClCs)-Cs(ClCsH)_428",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    Cl1s u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.262135,0.16747,0.0449016,-0.0168143,-0.158458,-0.188178,0.0176148],'cal/(mol*K)','+|-',[0.477072,0.525826,0.559696,0.556562,0.468436,0.371497,0.550225]),
        H298 = (2.46094,'kcal/mol','+|-',2.05203),
        S298 = (2.52456,'cal/(mol*K)','+|-',1.57439),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         3
""",
)

entry(
    index = 665,
    label = "4ring-Cs(FFCs)-Cs(FCsH)_579",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0456603,0.0492439,0.0968855,0.0973006,0.0394923,0.06316,0.262793],'cal/(mol*K)','+|-',[0.319207,0.351827,0.37449,0.372393,0.313428,0.248567,0.368153]),
        H298 = (4.50787,'kcal/mol','+|-',1.37301),
        S298 = (1.61448,'cal/(mol*K)','+|-',1.05342),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         5
""",
)

entry(
    index = 666,
    label = "4ring-Cs(Val7O2sH)-Cs(Val7CsH)_194",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.55804,-1.65953,-1.91504,-2.07404,-1.79554,-1.43132,-2.73351],'cal/(mol*K)','+|-',[1.23874,1.36533,1.45328,1.44514,1.21632,0.964612,1.42869]),
        H298 = (2.71391,'kcal/mol','+|-',3.14749),
        S298 = (6.33726,'cal/(mol*K)','+|-',1.71755),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 667,
    label = "4ring-Cs(ClO2sH)-Cs(ClCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
7    H    u0 p0 c0 {1,S}
8    H    u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.72185,-1.89276,-2.14671,-2.33001,-2.07993,-1.6879,-2.88419],'cal/(mol*K)','+|-',[1.23874,1.36533,1.45328,1.44514,1.21632,0.964612,1.42869]),
        H298 = (1.6011,'kcal/mol','+|-',5.32821),
        S298 = (6.94451,'cal/(mol*K)','+|-',4.088),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 668,
    label = "4ring-Cs(FO2sH)-Cs(FCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    H   u0 p0 c0 {1,S}
8    H   u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.39422,-1.42629,-1.68337,-1.81807,-1.51114,-1.17474,-2.58284],'cal/(mol*K)','+|-',[1.23874,1.36533,1.45328,1.44514,1.21632,0.964612,1.42869]),
        H298 = (3.82671,'kcal/mol','+|-',5.32821),
        S298 = (5.73002,'cal/(mol*K)','+|-',4.088),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 669,
    label = "4ring-Cd(Val7Cd)-Cs(Val7Val7O2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.37635,-2.40548,-2.89789,-2.96482,-2.51131,-1.92081,-0.965956],'cal/(mol*K)','+|-',[1.09736,1.2095,1.28741,1.2802,1.07749,0.854514,1.26562]),
        H298 = (12.4631,'kcal/mol','+|-',3.83365),
        S298 = (7.43739,'cal/(mol*K)','+|-',8.8086),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 670,
    label = "4ring-Cd(ClCd)-Cs(ClClO2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.70581,-3.16219,-3.92261,-4.05334,-3.50883,-2.74905,-1.47155],'cal/(mol*K)','+|-',[1.09736,1.2095,1.28741,1.2802,1.07749,0.854514,1.26562]),
        H298 = (13.8185,'kcal/mol','+|-',4.72006),
        S298 = (10.5517,'cal/(mol*K)','+|-',3.62141),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         2
""",
)

entry(
    index = 671,
    label = "4ring-Cd(FCd)-Cs(FFO2s)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.04689,-1.64876,-1.87317,-1.87631,-1.51379,-1.09256,-0.460361],'cal/(mol*K)','+|-',[0.548679,0.60475,0.643703,0.640099,0.538746,0.427257,0.632811]),
        H298 = (11.1077,'kcal/mol','+|-',2.36003),
        S298 = (4.32308,'cal/(mol*K)','+|-',1.8107),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 672,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7Cd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.68699,0.456533,0.243095,-0.0298391,-0.374368,-0.528116,-0.0553107],'cal/(mol*K)','+|-',[1.76852,1.94925,2.0748,2.06319,1.7365,1.37715,2.0397]),
        H298 = (3.20044,'kcal/mol','+|-',7.60693),
        S298 = (5.77002,'cal/(mol*K)','+|-',5.83631),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 673,
    label = "4ring-Cs(ClClCd)-Cs(ClCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u0 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.68699,0.456533,0.243095,-0.0298391,-0.374368,-0.528116,-0.0553107],'cal/(mol*K)','+|-',[1.76852,1.94925,2.0748,2.06319,1.7365,1.37715,2.0397]),
        H298 = (3.20044,'kcal/mol','+|-',7.60693),
        S298 = (5.77002,'cal/(mol*K)','+|-',5.83631),
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
    index = 674,
    label = "4ring-Cs(Val7CsH)-Cd(Val7Cd)_201",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234238,-0.0921238,0.0261451,0.102752,0.102794,0.0774407,0.147096],'cal/(mol*K)','+|-',[0.806323,0.888723,0.945969,0.940672,0.791726,0.627885,0.929962]),
        H298 = (1.0428,'kcal/mol','+|-',3.46824),
        S298 = (0.999917,'cal/(mol*K)','+|-',2.66096),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 675,
    label = "4ring-Cs(ClCsH)-Cd(ClCd)_472",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234238,-0.0921238,0.0261451,0.102752,0.102794,0.0774407,0.147096],'cal/(mol*K)','+|-',[0.806323,0.888723,0.945969,0.940672,0.791726,0.627885,0.929962]),
        H298 = (1.0428,'kcal/mol','+|-',3.46824),
        S298 = (0.999917,'cal/(mol*K)','+|-',2.66096),
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
    index = 676,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)_202",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.741204,-0.600809,-0.529903,-0.544048,-0.504301,-0.364293,0.609958],'cal/(mol*K)','+|-',[1.75872,1.93845,2.06331,2.05176,1.72688,1.36952,2.0284]),
        H298 = (3.35113,'kcal/mol','+|-',7.56479),
        S298 = (3.04652,'cal/(mol*K)','+|-',5.80398),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 677,
    label = "4ring-Cs(ClClCd)-Cs(ClClCd)_475",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
8    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.741204,-0.600809,-0.529903,-0.544048,-0.504301,-0.364293,0.609958],'cal/(mol*K)','+|-',[1.75872,1.93845,2.06331,2.05176,1.72688,1.36952,2.0284]),
        H298 = (3.35113,'kcal/mol','+|-',7.56479),
        S298 = (3.04652,'cal/(mol*K)','+|-',5.80398),
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
    index = 678,
    label = "4ring-Cs(Val7O2s)-Cs(Val7O2sH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.97945,-2.24088,-1.76048,-2.06934,-1.93294,-1.6444,-1.08711],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (3.90332,'kcal/mol','+|-',8.4435),
        S298 = (6.11382,'cal/(mol*K)','+|-',6.47816),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 679,
    label = "4ring-Cs(ClO2s)-Cs(ClO2sH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    H    u0 p0 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.97945,-2.24088,-1.76048,-2.06934,-1.93294,-1.6444,-1.08711],'cal/(mol*K)','+|-',[1.96301,2.16362,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (3.90332,'kcal/mol','+|-',8.4435),
        S298 = (6.11382,'cal/(mol*K)','+|-',6.47816),
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
    index = 680,
    label = "4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)_204",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.430554,-0.21586,-0.144109,-0.120997,-0.129775,-0.0864394,0.27069],'cal/(mol*K)','+|-',[1.65495,1.82407,1.94157,1.9307,1.62499,1.28871,1.90872]),
        H298 = (1.6945,'kcal/mol','+|-',7.11844),
        S298 = (2.98537,'cal/(mol*K)','+|-',5.46153),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 681,
    label = "4ring-Cs(ClClCs)-Cd(ClCd)_495",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.430554,-0.21586,-0.144109,-0.120997,-0.129775,-0.0864394,0.27069],'cal/(mol*K)','+|-',[1.65495,1.82407,1.94157,1.9307,1.62499,1.28871,1.90872]),
        H298 = (1.6945,'kcal/mol','+|-',7.11844),
        S298 = (2.98537,'cal/(mol*K)','+|-',5.46153),
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
    index = 682,
    label = "4ring-Cd(Val7Cd)-Cs(Val7Val7O2s)_206",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.518945,-1.17562,-1.68459,-1.85643,-1.68352,-1.30373,-0.617699],'cal/(mol*K)','+|-',[1.76943,1.95026,2.07588,2.06426,1.7374,1.37786,2.04075]),
        H298 = (27.3522,'kcal/mol','+|-',7.61087),
        S298 = (6.28379,'cal/(mol*K)','+|-',5.83934),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 683,
    label = "4ring-Cd(ClCd)-Cs(ClClO2s)_499",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {1,S}
7    Cl1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.518945,-1.17562,-1.68459,-1.85643,-1.68352,-1.30373,-0.617699],'cal/(mol*K)','+|-',[1.76943,1.95026,2.07588,2.06426,1.7374,1.37786,2.04075]),
        H298 = (27.3522,'kcal/mol','+|-',7.61087),
        S298 = (6.28379,'cal/(mol*K)','+|-',5.83934),
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
    index = 684,
    label = "4ring-Cs(Val7Val7O2s)-Cs(Val7Cs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    Cs   u0 p0 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.366658,-0.0664933,-0.0291642,-0.121776,-0.139168,-0.102402,-0.944025],'cal/(mol*K)','+|-',[0.406383,0.447912,0.476763,0.474094,0.399026,0.316451,0.468696]),
        H298 = (2.73203,'kcal/mol','+|-',1.74797),
        S298 = (1.29151,'cal/(mol*K)','+|-',1.34111),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 685,
    label = "4ring-Cs(FFO2s)-Cs(FCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *2 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    Cs  u0 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.366658,-0.0664933,-0.0291642,-0.121776,-0.139168,-0.102402,-0.944025],'cal/(mol*K)','+|-',[0.406383,0.447912,0.476763,0.474094,0.399026,0.316451,0.468696]),
        H298 = (2.73203,'kcal/mol','+|-',1.74797),
        S298 = (1.29151,'cal/(mol*K)','+|-',1.34111),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         3
""",
)

entry(
    index = 686,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)_208",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.973026,-0.424227,-0.108082,-0.0361404,0.147553,0.357051,1.21331],'cal/(mol*K)','+|-',[1.56528,1.72524,1.83637,1.82608,1.53694,1.21888,1.80529]),
        H298 = (6.60619,'kcal/mol','+|-',6.73273),
        S298 = (2.36247,'cal/(mol*K)','+|-',5.1656),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 687,
    label = "4ring-Cs(FFCd)-Cs(FFCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.973026,-0.424227,-0.108082,-0.0361404,0.147553,0.357051,1.21331],'cal/(mol*K)','+|-',[1.56528,1.72524,1.83637,1.82608,1.53694,1.21888,1.80529]),
        H298 = (6.60619,'kcal/mol','+|-',6.73273),
        S298 = (2.36247,'cal/(mol*K)','+|-',5.1656),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 688,
    label = "4ring-Cs(Val7O2s)-Cs(Val7Val7O2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs   u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00597,-0.87435,-0.337387,-0.604055,-0.487248,-0.321,-0.179995],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (8.67447,'kcal/mol','+|-',8.4435),
        S298 = (6.19108,'cal/(mol*K)','+|-',6.47816),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 689,
    label = "4ring-Cs(FO2s)-Cs(FFO2s)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 *1 Cs  u1 p0 c0 {1,S} {4,S} {7,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.00597,-0.87435,-0.337387,-0.604055,-0.487248,-0.321,-0.179995],'cal/(mol*K)','+|-',[1.96301,2.16361,2.30298,2.29009,1.92747,1.5286,2.26401]),
        H298 = (8.67447,'kcal/mol','+|-',8.4435),
        S298 = (6.19108,'cal/(mol*K)','+|-',6.47816),
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
    index = 690,
    label = "4ring-Cs(Val7Val7O2s)-Cs(Val7Val7Cs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs   u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {1,S}
7    Val7 u0 p3 c0 {2,S}
8    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.4906,-0.460541,-0.47364,-0.543159,-0.454335,-0.325347,-0.680903],'cal/(mol*K)','+|-',[1.17508,1.29516,1.37859,1.37087,1.1538,0.915034,1.35526]),
        H298 = (4.15211,'kcal/mol','+|-',5.05436),
        S298 = (2.69623,'cal/(mol*K)','+|-',3.87789),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 691,
    label = "4ring-Cs(FFO2s)-Cs(FFCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 Cs  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {1,S}
7    F1s u0 p3 c0 {2,S}
8    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.4906,-0.460541,-0.47364,-0.543159,-0.454335,-0.325347,-0.680903],'cal/(mol*K)','+|-',[1.17508,1.29516,1.37859,1.37087,1.1538,0.915034,1.35526]),
        H298 = (4.15211,'kcal/mol','+|-',5.05436),
        S298 = (2.69623,'cal/(mol*K)','+|-',3.87789),
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
    index = 692,
    label = "4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)_214",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs   u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
7    Val7 u0 p3 c0 {2,S}
8    H    u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.822086,-0.207702,0.183284,0.249799,0.309164,0.376533,0.990252],'cal/(mol*K)','+|-',[1.47109,1.62143,1.72587,1.71621,1.44446,1.14554,1.69667]),
        H298 = (3.21777,'kcal/mol','+|-',6.32762),
        S298 = (2.50647,'cal/(mol*K)','+|-',4.85478),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 693,
    label = "4ring-Cs(FFCd)-Cs(FCdH)_632",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2 *1 Cs  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
7    F1s u0 p3 c0 {2,S}
8    H   u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.822086,-0.207702,0.183284,0.249799,0.309164,0.376533,0.990252],'cal/(mol*K)','+|-',[1.47109,1.62143,1.72587,1.71621,1.44446,1.14554,1.69667]),
        H298 = (3.21777,'kcal/mol','+|-',6.32762),
        S298 = (2.50647,'cal/(mol*K)','+|-',4.85478),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         2
""",
)

entry(
    index = 694,
    label = "4ring-Cd(Val7Cd)=Cd(Val7Cd)_215",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.265723,-0.313904,-0.174731,-0.322853,-0.592547,-0.620139,-0.0381819],'cal/(mol*K)','+|-',[0.895989,0.987552,1.05116,1.04528,0.879768,0.697708,1.03338]),
        H298 = (3.13569,'kcal/mol','+|-',3.85392),
        S298 = (0.533865,'cal/(mol*K)','+|-',2.95687),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 695,
    label = "4ring-Cd(FCd)=Cd(FCd)_638",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.265723,-0.313904,-0.174731,-0.322853,-0.592547,-0.620139,-0.0381819],'cal/(mol*K)','+|-',[0.895989,0.987552,1.05116,1.04528,0.879768,0.697708,1.03338]),
        H298 = (3.13569,'kcal/mol','+|-',3.85392),
        S298 = (0.533865,'cal/(mol*K)','+|-',2.95687),
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
    index = 696,
    label = "4ring-Cd(Val7Cd)-Cd(Val7Cd)_216",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Val7 u0 p3 c0 {1,S}
6    Val7 u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.265723,-0.313904,-0.174731,-0.322853,-0.592547,-0.620139,-0.0381819],'cal/(mol*K)','+|-',[0.895989,0.987552,1.05116,1.04528,0.879768,0.697708,1.03338]),
        H298 = (3.13569,'kcal/mol','+|-',3.85392),
        S298 = (0.533865,'cal/(mol*K)','+|-',2.95687),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 697,
    label = "4ring-Cd(FCd)-Cd(FCd)_639",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd  u0 p0 c0 {1,D} {4,S}
4    Cd  u1 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.265723,-0.313904,-0.174731,-0.322853,-0.592547,-0.620139,-0.0381819],'cal/(mol*K)','+|-',[0.895989,0.987552,1.05116,1.04528,0.879768,0.697708,1.03338]),
        H298 = (3.13569,'kcal/mol','+|-',3.85392),
        S298 = (0.533865,'cal/(mol*K)','+|-',2.95687),
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
    index = 698,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 699,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 700,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 701,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 702,
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
    index = 703,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 704,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 705,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 706,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 707,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 708,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 709,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 710,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 711,
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
    index = 712,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 713,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 714,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 715,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 716,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 717,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 718,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 719,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 720,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 721,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 722,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 723,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 724,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 725,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 726,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

""",
)

entry(
    index = 727,
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
    shortDesc = """noncylic group""",
    longDesc = 
"""

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
    L2: halogen
        L3: halogen-3
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsCs)
                L5: 3ring-Cs(BrCsH)-Cs(BrCsCs)
                L5: 3ring-Cs(ClCsH)-Cs(ClCsCs)
                L5: 3ring-Cs(FCsH)-Cs(FCsCs)_624
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsH)
                L5: 3ring-Cs(BrCsH)-Cs(BrCsH)
                L5: 3ring-Cs(ClCsH)-Cs(ClCsH)
                L5: 3ring-Cs(FCsH)-Cs(FCsH)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7CsH)
                L5: 3ring-Cs(BrCsCs)-Cs(BrCsH)
                L5: 3ring-Cs(ClCsCs)-Cs(ClCsH)_424
                L5: 3ring-Cs(FCsCs)-Cs(FCsH)_607
            L4: 3ring-Cs(Val7CdH)-Cd(Val7Cd)
                L5: 3ring-Cs(BrCdH)-Cd(BrCd)
                L5: 3ring-Cs(FCdH)-Cd(FCd)_612
            L4: 3ring-Cd(Val7Cs)=Cd(Val7Cs)
                L5: 3ring-Cd(BrCs)=Cd(BrCs)
                L5: 3ring-Cd(ClCs)=Cd(ClCs)
                L5: 3ring-Cd(FCs)=Cd(FCs)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsH)
                L5: 3ring-Cs(BrBrCs)-Cs(BrCsH)
                L5: 3ring-Cs(ClClCs)-Cs(ClCsH)_385
                L5: 3ring-Cs(FFCs)-Cs(FCsH)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7CsH)
                L5: 3ring-Cs(BrCs)-Cs(BrCsH)
                L5: 3ring-Cs(ClCs)-Cs(ClCsH)
                L5: 3ring-Cs(FCs)-Cs(FCsH)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(BrCs)-Cs(BrBrCs)
                L5: 3ring-Cs(ClCs)-Cs(ClClCs)
                L5: 3ring-Cs(FCs)-Cs(FFCs)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(BrCsH)-Cs(BrBrCs)
                L5: 3ring-Cs(ClCsH)-Cs(ClClCs)_498
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)
                L5: 3ring-Cs(BrBrCs)-Cs(BrCsCs)
                L5: 3ring-Cs(ClClCs)-Cs(ClCsCs)_471
                L5: 3ring-Cs(FFCs)-Cs(FCsCs)_574
            L4: 3ring-Cs(Val7CdH)-Cd(Val7Cd)_61
                L5: 3ring-Cs(BrCdH)-Cd(BrCd)_242
                L5: 3ring-Cs(ClCdH)-Cd(ClCd)
                L5: 3ring-Cs(FCdH)-Cd(FCd)
            L4: 3ring-Cs(Val7CdCs)-Cd(Val7Cd)
                L5: 3ring-Cs(BrCdCs)-Cd(BrCd)
                L5: 3ring-Cs(ClCdCs)-Cd(ClCd)
            L4: 3ring-Cs(Val7COH)-Cs(Val7Val7CO)
                L5: 3ring-Cs(BrCOH)-Cs(BrBrCO)
                L5: 3ring-Cs(ClCOH)-Cs(ClClCO)
                L5: 3ring-Cs(FCOH)-Cs(FFCO)
            L4: 3ring-Cs(Val7O2sCd)-Cd(Val7Cd)
                L5: 3ring-Cs(BrO2sCd)-Cd(BrCd)
                L5: 3ring-Cs(ClO2sCd)-Cd(ClCd)_453
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(BrBrO2s)-Cs(BrBrO2s)
                L5: 3ring-Cs(ClClO2s)-Cs(ClClO2s)
                L5: 3ring-Cs(FFO2s)-Cs(FFO2s)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CdH)
                L5: 3ring-Cd(BrCd)-Cs(BrCdH)
                L5: 3ring-Cd(ClCd)-Cs(ClCdH)
                L5: 3ring-Cd(FCd)-Cs(FCdH)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7Cs)
                L5: 3ring-Cs(BrBrCs)-Cs(BrCs)
                L5: 3ring-Cs(ClClCs)-Cs(ClCs)
                L5: 3ring-Cs(FFCs)-Cs(FCs)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Cs)
                L5: 3ring-Cs(BrCsCs)-Cs(BrCs)
                L5: 3ring-Cs(FCsCs)-Cs(FCs)
            L4: 3ring-Cs(Val7CdH)-Cs(Val7CdH)
                L5: 3ring-Cs(BrCdH)-Cs(BrCdH)
                L5: 3ring-Cs(ClCdH)-Cs(ClCdH)
                L5: 3ring-Cs(FCdH)-Cs(FCdH)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(BrBrCs)-Cs(BrBrCs)
                L5: 3ring-Cs(ClClCs)-Cs(ClClCs)
                L5: 3ring-Cs(FFCs)-Cs(FFCs)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsCs)_72
                L5: 3ring-Cs(BrCsH)-Cs(BrCsCs)_253
                L5: 3ring-Cs(ClCsH)-Cs(ClCsCs)_417
                L5: 3ring-Cs(FCsH)-Cs(FCsCs)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7O2sCs)
                L5: 3ring-Cs(BrCs)-Cs(BrO2sCs)
                L5: 3ring-Cs(ClCs)-Cs(ClO2sCs)
                L5: 3ring-Cs(FCs)-Cs(FO2sCs)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7CsH)
                L5: 3ring-Cs(BrO2sCs)-Cs(BrCsH)
                L5: 3ring-Cs(ClO2sCs)-Cs(ClCsH)
                L5: 3ring-Cs(FO2sCs)-Cs(FCsH)_578
            L4: 3ring-Cd(Val7Cd)-Cs(Val7Val7Cd)
                L5: 3ring-Cd(BrCd)-Cs(BrBrCd)
                L5: 3ring-Cd(FCd)-Cs(FFCd)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7Cs)
                L5: 3ring-Cs(BrCsH)-Cs(BrCs)
                L5: 3ring-Cs(ClCsH)-Cs(ClCs)
                L5: 3ring-Cs(FCsH)-Cs(FCs)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7CsCs)
                L5: 3ring-Cs(BrCs)-Cs(BrCsCs)
                L5: 3ring-Cs(ClCs)-Cs(ClCsCs)
                L5: 3ring-Cs(FCs)-Cs(FCsCs)
            L4: 3ring-Cs(Val7Val7Cd)-Cs(Val7CdH)
                L5: 3ring-Cs(BrBrCd)-Cs(BrCdH)
                L5: 3ring-Cs(FFCd)-Cs(FCdH)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_83
                L5: 3ring-Cs(BrCsH)-Cs(BrBrCs)_264
                L5: 3ring-Cs(ClCsH)-Cs(ClClCs)
                L5: 3ring-Cs(FCsH)-Cs(FFCs)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsH)_87
                L5: 3ring-Cs(BrCsH)-Cs(BrCsH)_268
                L5: 3ring-Cs(ClCsH)-Cs(ClCsH)_390
                L5: 3ring-Cs(FCsH)-Cs(FCsH)_575
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7O2s)
                L5: 3ring-Cs(BrBrO2s)-Cs(BrO2s)
                L5: 3ring-Cs(FFO2s)-Cs(FO2s)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7O2sCd)
                L5: 3ring-Cd(BrCd)-Cs(BrO2sCd)
                L5: 3ring-Cd(FCd)-Cs(FO2sCd)_642
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7O2sCs)
                L5: 3ring-Cs(BrBrO2s)-Cs(BrO2sCs)
                L5: 3ring-Cs(ClClO2s)-Cs(ClO2sCs)
                L5: 3ring-Cs(FFO2s)-Cs(FO2sCs)
            L4: 3ring-Cs(Val7O2sO2s)-Cs(Val7O2sH)
                L5: 3ring-Cs(BrO2sO2s)-Cs(BrO2sH)
                L5: 3ring-Cs(ClO2sO2s)-Cs(ClO2sH)
                L5: 3ring-Cs(FO2sO2s)-Cs(FO2sH)
            L4: 3ring-Cs(Val7O2s)-Cs(Val7O2sCs)
                L5: 3ring-Cs(BrO2s)-Cs(BrO2sCs)
                L5: 3ring-Cs(ClO2s)-Cs(ClO2sCs)
                L5: 3ring-Cs(FO2s)-Cs(FO2sCs)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7CsH)_94
                L5: 3ring-Cs(BrCsCs)-Cs(BrCsH)_275
                L5: 3ring-Cs(ClCsCs)-Cs(ClCsH)_466
                L5: 3ring-Cs(FCsCs)-Cs(FCsH)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7O2sCs)
                L5: 3ring-Cs(BrCsH)-Cs(BrO2sCs)
                L5: 3ring-Cs(FCsH)-Cs(FO2sCs)_645
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CsCd)
                L5: 3ring-Cd(BrCd)-Cs(BrCsCd)
                L5: 3ring-Cd(ClCd)-Cs(ClCsCd)
                L5: 3ring-Cd(FCd)-Cs(FCsCd)_567
            L4: 3ring-Cd(Val7Cd)=Cd(Val7Cd)
                L5: 3ring-Cd(BrCd)=Cd(BrCd)
                L5: 3ring-Cd(ClCd)=Cd(ClCd)
                L5: 3ring-Cd(FCd)=Cd(FCd)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_104
                L5: 3ring-Cs(BrBrCs)-Cs(BrBrCs)_285
                L5: 3ring-Cs(ClClCs)-Cs(ClClCs)_413
                L5: 3ring-Cs(FFCs)-Cs(FFCs)_536
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7O2sCs)
                L5: 3ring-Cs(BrBrCs)-Cs(BrO2sCs)
                L5: 3ring-Cs(FFCs)-Cs(FO2sCs)
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2sCs)
                L5: 3ring-Cs(BrO2sH)-Cs(BrO2sCs)
                L5: 3ring-Cs(ClO2sH)-Cs(ClO2sCs)
                L5: 3ring-Cs(FO2sH)-Cs(FO2sCs)
            L4: 3ring-Cd(Val7CO)=Cd(Val7CO)
                L5: 3ring-Cd(BrCO)=Cd(BrCO)
                L5: 3ring-Cd(ClCO)=Cd(ClCO)
                L5: 3ring-Cd(FCO)=Cd(FCO)
            L4: 3ring-Cs(Val7Cd)-Cd(Val7Cd)
                L5: 3ring-Cs(BrCd)-Cd(BrCd)
                L5: 3ring-Cs(ClCd)-Cd(ClCd)
                L5: 3ring-Cs(FCd)-Cd(FCd)
            L4: 3ring-Cs(Val7O2sCd)-Cd(Val7Cd)_112
                L5: 3ring-Cs(BrO2sCd)-Cd(BrCd)_293
                L5: 3ring-Cs(ClO2sCd)-Cd(ClCd)_470
                L5: 3ring-Cs(FO2sCd)-Cd(FCd)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_116
                L5: 3ring-Cs(BrBrCs)-Cs(BrCsH)_297
                L5: 3ring-Cs(ClClCs)-Cs(ClCsH)
                L5: 3ring-Cs(FFCs)-Cs(FCsH)_586
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2s)
                L5: 3ring-Cs(BrO2sH)-Cs(BrO2s)
                L5: 3ring-Cs(ClO2sH)-Cs(ClO2s)
                L5: 3ring-Cs(FO2sH)-Cs(FO2s)
            L4: 3ring-Cs(Val7O2sO2s)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(BrO2sO2s)-Cs(BrBrO2s)
                L5: 3ring-Cs(ClO2sO2s)-Cs(ClClO2s)
                L5: 3ring-Cs(FO2sO2s)-Cs(FFO2s)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CdCs)
                L5: 3ring-Cd(BrCd)-Cs(BrCdCs)
                L5: 3ring-Cd(FCd)-Cs(FCdCs)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7Cd)
                L5: 3ring-Cd(BrCd)-Cs(BrCd)
                L5: 3ring-Cd(FCd)-Cs(FCd)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(BrCsCs)-Cs(BrBrCs)
                L5: 3ring-Cs(ClCsCs)-Cs(ClClCs)_459
                L5: 3ring-Cs(FCsCs)-Cs(FFCs)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7CsH)_138
                L5: 3ring-Cs(BrCsCs)-Cs(BrCsH)_319
                L5: 3ring-Cs(ClCsCs)-Cs(ClCsH)
                L5: 3ring-Cs(FCsCs)-Cs(FCsH)_554
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CsCd)_140
                L5: 3ring-Cd(BrCd)-Cs(BrCsCd)_321
                L5: 3ring-Cd(FCd)-Cs(FCsCd)
            L4: 3ring-Cs(Val7O2sCd)-Cd(Val7Cd)_141
                L5: 3ring-Cs(BrO2sCd)-Cd(BrCd)_322
                L5: 3ring-Cs(ClO2sCd)-Cd(ClCd)
            L4: 3ring-Cd(Val7Cs)=Cd(Val7Cs)_145
                L5: 3ring-Cd(BrCs)=Cd(BrCs)_326
                L5: 3ring-Cd(ClCs)=Cd(ClCs)_392
                L5: 3ring-Cd(FCs)=Cd(FCs)_560
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(BrO2sCs)-Cs(BrBrCs)
                L5: 3ring-Cs(ClO2sCs)-Cs(ClClCs)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Cs)
                L5: 3ring-Cs(BrO2sCs)-Cs(BrCs)
                L5: 3ring-Cs(ClO2sCs)-Cs(ClCs)
                L5: 3ring-Cs(FO2sCs)-Cs(FCs)
            L4: 3ring-Cs(Val7COH)-Cs(Val7COH)
                L5: 3ring-Cs(BrCOH)-Cs(BrCOH)
                L5: 3ring-Cs(ClCOH)-Cs(ClCOH)
                L5: 3ring-Cs(FCOH)-Cs(FCOH)
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2sCs)_150
                L5: 3ring-Cs(BrO2sH)-Cs(BrO2sCs)_331
                L5: 3ring-Cs(ClO2sH)-Cs(ClO2sCs)_389
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)_152
                L5: 3ring-Cs(BrCsCs)-Cs(BrBrCs)_333
                L5: 3ring-Cs(ClCsCs)-Cs(ClClCs)
                L5: 3ring-Cs(FCsCs)-Cs(FFCs)_605
            L4: 3ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)
                L5: 3ring-Cs(BrBrCd)-Cs(BrBrCd)
                L5: 3ring-Cs(ClClCd)-Cs(ClClCd)
                L5: 3ring-Cs(FFCd)-Cs(FFCd)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7CsH)_156
                L5: 3ring-Cs(BrO2sCs)-Cs(BrCsH)_337
                L5: 3ring-Cs(ClO2sCs)-Cs(ClCsH)_468
                L5: 3ring-Cs(FO2sCs)-Cs(FCsH)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7O2sCs)_157
                L5: 3ring-Cs(BrBrCs)-Cs(BrO2sCs)_338
                L5: 3ring-Cs(FFCs)-Cs(FO2sCs)_602
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)_158
                L5: 3ring-Cs(BrBrCs)-Cs(BrCsCs)_339
                L5: 3ring-Cs(ClClCs)-Cs(ClCsCs)
                L5: 3ring-Cs(FFCs)-Cs(FCsCs)
            L4: 3ring-Cs(Val7O2sO2s)-Cs(Val7O2s)
                L5: 3ring-Cs(BrO2sO2s)-Cs(BrO2s)
                L5: 3ring-Cs(ClO2sO2s)-Cs(ClO2s)
                L5: 3ring-Cs(FO2sO2s)-Cs(FO2s)
            L4: 3ring-Cs(Val7Val7CO)-Cs(Val7Val7CO)
                L5: 3ring-Cs(BrBrCO)-Cs(BrBrCO)
                L5: 3ring-Cs(ClClCO)-Cs(ClClCO)
                L5: 3ring-Cs(FFCO)-Cs(FFCO)
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2sH)
                L5: 3ring-Cs(BrO2sH)-Cs(BrO2sH)
                L5: 3ring-Cs(ClO2sH)-Cs(ClO2sH)
                L5: 3ring-Cs(FO2sH)-Cs(FO2sH)
            L4: 3ring-Cs(Val7Val7Cd)-Cd(Val7Cd)
                L5: 3ring-Cs(BrBrCd)-Cd(BrCd)
                L5: 3ring-Cs(ClClCd)-Cd(ClCd)
                L5: 3ring-Cs(FFCd)-Cd(FCd)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsCs)_170
                L5: 3ring-Cs(BrCsH)-Cs(BrCsCs)_351
                L5: 3ring-Cs(FCsH)-Cs(FCsCs)_551
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)_171
                L5: 3ring-Cs(BrCsCs)-Cs(BrBrCs)_352
                L5: 3ring-Cs(FCsCs)-Cs(FFCs)_610
            L4: 3ring-Cs(Val7Val7Cd)-Cd(Val7Cd)_172
                L5: 3ring-Cs(BrBrCd)-Cd(BrCd)_353
                L5: 3ring-Cs(ClClCd)-Cd(ClCd)_482
                L5: 3ring-Cs(FFCd)-Cd(FCd)_637
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(BrO2sH)-Cs(BrBrO2s)
                L5: 3ring-Cs(ClO2sH)-Cs(ClClO2s)
                L5: 3ring-Cs(FO2sH)-Cs(FFO2s)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7O2sCs)_178
                L5: 3ring-Cs(BrCsH)-Cs(BrO2sCs)_359
                L5: 3ring-Cs(FCsH)-Cs(FO2sCs)
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7O2sCs)_180
                L5: 3ring-Cs(BrBrO2s)-Cs(BrO2sCs)_361
                L5: 3ring-Cs(ClClO2s)-Cs(ClO2sCs)_492
                L5: 3ring-Cs(FFO2s)-Cs(FO2sCs)_553
            L4: 3ring-Cs(Val7CsCd)-Cd(Val7Cd)
                L5: 3ring-Cs(ClCsCd)-Cd(ClCd)
            L4: 3ring-Cs(Val7CdH)-Cs(Val7Val7Cd)
                L5: 3ring-Cs(ClCdH)-Cs(ClClCd)
                L5: 3ring-Cs(FCdH)-Cs(FFCd)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CdH)_192
                L5: 3ring-Cd(ClCd)-Cs(ClCdH)_427
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7O2s)
                L5: 3ring-Cs(ClO2sCs)-Cs(ClO2s)
            L4: 3ring-Cs(Val7CsCd)-Cd(Val7Cd)_196
                L5: 3ring-Cs(ClCsCd)-Cd(ClCd)_446
                L5: 3ring-Cs(FCsCd)-Cd(FCd)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(ClO2sCs)-Cs(ClClO2s)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Val7Cs)_200
                L5: 3ring-Cs(ClO2sCs)-Cs(ClClCs)_462
            L4: 3ring-Cs(Val7O2s)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(ClO2s)-Cs(ClClO2s)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7O2sH)
                L5: 3ring-Cs(FO2sCs)-Cs(FO2sH)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7O2sCd)_212
                L5: 3ring-Cd(FCd)-Cs(FO2sCd)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)_213
                L5: 3ring-Cs(FFCs)-Cs(FCsCs)_622
        L3: halogen-4
            L4: 4ring-Cd(Val7Cd)-Cd(Val7Cd)
                L5: 4ring-Cd(BrCd)-Cd(BrCd)
                L5: 4ring-Cd(ClCd)-Cd(ClCd)
                L5: 4ring-Cd(FCd)-Cd(FCd)
            L4: 4ring-Cd(Val7Cd)=Cd(Val7Cd)
                L5: 4ring-Cd(BrCd)=Cd(BrCd)
                L5: 4ring-Cd(ClCd)=Cd(ClCd)
                L5: 4ring-Cd(FCd)=Cd(FCd)
            L4: 4ring-Cs(Val7CdH)-Cs(Val7CdH)
                L5: 4ring-Cs(BrCdH)-Cs(BrCdH)
                L5: 4ring-Cs(ClCdH)-Cs(ClCdH)
                L5: 4ring-Cs(FCdH)-Cs(FCdH)_627
            L4: 4ring-Cd(Val7Cs)=Cd(Val7Cs)
                L5: 4ring-Cd(BrCs)=Cd(BrCs)
                L5: 4ring-Cd(ClCs)=Cd(ClCs)_435
                L5: 4ring-Cd(FCs)=Cd(FCs)_580
            L4: 4ring-Cd(Val7Cd)-Cs(Val7CsH)
                L5: 4ring-Cd(BrCd)-Cs(BrCsH)
                L5: 4ring-Cd(ClCd)-Cs(ClCsH)_433
                L5: 4ring-Cd(FCd)-Cs(FCsH)_582
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)
                L5: 4ring-Cd(BrCd)-Cs(BrBrCs)
                L5: 4ring-Cd(ClCd)-Cs(ClClCs)
                L5: 4ring-Cd(FCd)-Cs(FFCs)_581
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)
                L5: 4ring-Cs(BrBrCd)-Cs(BrCdH)
                L5: 4ring-Cs(ClClCd)-Cs(ClCdH)_479
                L5: 4ring-Cs(FFCd)-Cs(FCdH)
            L4: 4ring-Cs(Val7O2sH)-Cd(Val7Cd)
                L5: 4ring-Cs(BrO2sH)-Cd(BrCd)
                L5: 4ring-Cs(ClO2sH)-Cd(ClCd)
                L5: 4ring-Cs(FO2sH)-Cd(FCd)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7O2s)
                L5: 4ring-Cd(BrCs)=Cd(BrO2s)
                L5: 4ring-Cd(ClCs)=Cd(ClO2s)_445
                L5: 4ring-Cd(FCs)=Cd(FO2s)_555
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)
                L5: 4ring-Cs(BrCdH)-Cs(BrBrCd)
                L5: 4ring-Cs(FCdH)-Cs(FFCd)
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(BrBrO2s)-Cs(BrBrO2s)
                L5: 4ring-Cs(ClClO2s)-Cs(ClClO2s)
                L5: 4ring-Cs(FFO2s)-Cs(FFO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(BrCsH)-Cs(BrBrO2s)
                L5: 4ring-Cs(ClCsH)-Cs(ClClO2s)
                L5: 4ring-Cs(FCsH)-Cs(FFO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7CsH)
                L5: 4ring-Cs(BrCsH)-Cs(BrCsH)
                L5: 4ring-Cs(ClCsH)-Cs(ClCsH)
                L5: 4ring-Cs(FCsH)-Cs(FCsH)_568
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(BrCsH)-Cs(BrBrCs)
                L5: 4ring-Cs(ClCsH)-Cs(ClClCs)_467
                L5: 4ring-Cs(FCsH)-Cs(FFCs)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Cs)
                L5: 4ring-Cs(BrCsH)-Cs(BrCs)
                L5: 4ring-Cs(ClCsH)-Cs(ClCs)
                L5: 4ring-Cs(FCsH)-Cs(FCs)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7CsH)_62
                L5: 4ring-Cd(BrCd)-Cs(BrCsH)_243
                L5: 4ring-Cd(ClCd)-Cs(ClCsH)
                L5: 4ring-Cd(FCd)-Cs(FCsH)_626
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7O2s)
                L5: 4ring-Cs(BrBrO2s)-Cs(BrO2s)
                L5: 4ring-Cs(ClClO2s)-Cs(ClO2s)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7O2sH)
                L5: 4ring-Cs(BrBrCs)-Cs(BrO2sH)
                L5: 4ring-Cs(FFCs)-Cs(FO2sH)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7O2sH)
                L5: 4ring-Cs(BrO2sH)-Cs(BrO2sH)
                L5: 4ring-Cs(ClO2sH)-Cs(ClO2sH)
                L5: 4ring-Cs(FO2sH)-Cs(FO2sH)
            L4: 4ring-Cs(Val7Cd)-Cs(Val7CdH)
                L5: 4ring-Cs(BrCd)-Cs(BrCdH)
                L5: 4ring-Cs(ClCd)-Cs(ClCdH)
                L5: 4ring-Cs(FCd)-Cs(FCdH)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7Cs)_84
                L5: 4ring-Cd(BrCs)=Cd(BrCs)_265
                L5: 4ring-Cd(ClCs)=Cd(ClCs)
                L5: 4ring-Cd(FCs)=Cd(FCs)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)_85
                L5: 4ring-Cd(BrCd)-Cs(BrBrCs)_266
                L5: 4ring-Cd(FCd)-Cs(FFCs)_596
            L4: 4ring-Cs(Val7Cd)-Cs(Val7Val7Cd)
                L5: 4ring-Cs(BrCd)-Cs(BrBrCd)
                L5: 4ring-Cs(FCd)-Cs(FFCd)
            L4: 4ring-Cs(Val7O2s)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(BrO2s)-Cs(BrBrCs)
                L5: 4ring-Cs(FO2s)-Cs(FFCs)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7Cs)_96
                L5: 4ring-Cd(BrCs)=Cd(BrCs)_277
                L5: 4ring-Cd(ClCs)=Cd(ClCs)_461
                L5: 4ring-Cd(FCs)=Cd(FCs)_565
            L4: 4ring-Cs(Val7CsH)-Cd(Val7Cd)
                L5: 4ring-Cs(BrCsH)-Cd(BrCd)
                L5: 4ring-Cs(ClCsH)-Cd(ClCd)
                L5: 4ring-Cs(FCsH)-Cd(FCd)_652
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7O2s)
                L5: 4ring-Cs(BrBrCs)-Cs(BrO2s)
                L5: 4ring-Cs(ClClCs)-Cs(ClO2s)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)
                L5: 4ring-Cs(BrBrCd)-Cs(BrBrCd)
                L5: 4ring-Cs(ClClCd)-Cs(ClClCd)
                L5: 4ring-Cs(FFCd)-Cs(FFCd)_646
            L4: 4ring-Cd(Val7O2s)=Cd(Val7Cs)
                L5: 4ring-Cd(BrO2s)=Cd(BrCs)
                L5: 4ring-Cd(ClO2s)=Cd(ClCs)
            L4: 4ring-Cs(Val7Val7O2s)-Cd(Val7Cd)
                L5: 4ring-Cs(BrBrO2s)-Cd(BrCd)
                L5: 4ring-Cs(FFO2s)-Cd(FCd)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7CsH)
                L5: 4ring-Cs(BrCs)-Cs(BrCsH)
                L5: 4ring-Cs(ClCs)-Cs(ClCsH)
                L5: 4ring-Cs(FCs)-Cs(FCsH)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(BrCs)-Cs(BrBrCs)
                L5: 4ring-Cs(ClCs)-Cs(ClClCs)
                L5: 4ring-Cs(FCs)-Cs(FFCs)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Cs)
                L5: 4ring-Cd(BrCd)-Cs(BrCs)
                L5: 4ring-Cd(ClCd)-Cs(ClCs)
                L5: 4ring-Cd(FCd)-Cs(FCs)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7O2sH)
                L5: 4ring-Cs(BrCsH)-Cs(BrO2sH)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(BrBrCs)-Cs(BrBrCs)
                L5: 4ring-Cs(FFCs)-Cs(FFCs)_577
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(BrO2sH)-Cs(BrBrCs)
                L5: 4ring-Cs(ClO2sH)-Cs(ClClCs)_396
                L5: 4ring-Cs(FO2sH)-Cs(FFCs)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(BrO2sH)-Cs(BrBrO2s)
                L5: 4ring-Cs(ClO2sH)-Cs(ClClO2s)
                L5: 4ring-Cs(FO2sH)-Cs(FFO2s)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(BrBrCs)-Cs(BrBrO2s)
                L5: 4ring-Cs(ClClCs)-Cs(ClClO2s)
                L5: 4ring-Cs(FFCs)-Cs(FFO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7O2sH)_119
                L5: 4ring-Cs(BrCsH)-Cs(BrO2sH)_300
                L5: 4ring-Cs(ClCsH)-Cs(ClO2sH)
                L5: 4ring-Cs(FCsH)-Cs(FO2sH)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)
                L5: 4ring-Cs(BrBrCs)-Cs(BrCsH)
                L5: 4ring-Cs(ClClCs)-Cs(ClCsH)_491
                L5: 4ring-Cs(FFCs)-Cs(FCsH)
            L4: 4ring-Cs(Val7Cs)-Cd(Val7Cd)
                L5: 4ring-Cs(BrCs)-Cd(BrCd)
                L5: 4ring-Cs(ClCs)-Cd(ClCd)
                L5: 4ring-Cs(FCs)-Cd(FCd)
            L4: 4ring-Cs(Val7CsH)-Cd(Val7Cd)_124
                L5: 4ring-Cs(BrCsH)-Cd(BrCd)_305
                L5: 4ring-Cs(ClCsH)-Cd(ClCd)_440
                L5: 4ring-Cs(FCsH)-Cd(FCd)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7O2s)
                L5: 4ring-Cs(BrCsH)-Cs(BrO2s)
                L5: 4ring-Cs(ClCsH)-Cs(ClO2s)
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Cd)
                L5: 4ring-Cs(BrCdH)-Cs(BrCd)
                L5: 4ring-Cs(FCdH)-Cs(FCd)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Cs)
                L5: 4ring-Cs(BrBrCs)-Cs(BrCs)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7O2sH)
                L5: 4ring-Cs(BrCs)-Cs(BrO2sH)
                L5: 4ring-Cs(ClCs)-Cs(ClO2sH)
                L5: 4ring-Cs(FCs)-Cs(FO2sH)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(BrCs)-Cs(BrBrO2s)
                L5: 4ring-Cs(ClCs)-Cs(ClClO2s)
                L5: 4ring-Cs(FCs)-Cs(FFO2s)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7O2sH)_130
                L5: 4ring-Cs(BrBrCs)-Cs(BrO2sH)_311
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_131
                L5: 4ring-Cs(BrBrCs)-Cs(BrBrCs)_312
                L5: 4ring-Cs(ClClCs)-Cs(ClClCs)_423
                L5: 4ring-Cs(FFCs)-Cs(FFCs)_600
            L4: 4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)
                L5: 4ring-Cs(BrBrCs)-Cd(BrCd)
                L5: 4ring-Cs(ClClCs)-Cd(ClCd)
                L5: 4ring-Cs(FFCs)-Cd(FCd)_552
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7O2s)_133
                L5: 4ring-Cs(BrBrCs)-Cs(BrBrO2s)_314
                L5: 4ring-Cs(FFCs)-Cs(FFO2s)_635
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)_135
                L5: 4ring-Cs(BrCdH)-Cs(BrBrCd)_316
                L5: 4ring-Cs(FCdH)-Cs(FFCd)_650
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7O2s)
                L5: 4ring-Cs(BrO2sH)-Cs(BrO2s)
                L5: 4ring-Cs(FO2sH)-Cs(FO2s)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7CsH)_142
                L5: 4ring-Cd(BrCd)-Cs(BrCsH)_323
                L5: 4ring-Cd(ClCd)-Cs(ClCsH)_483
                L5: 4ring-Cd(FCd)-Cs(FCsH)
            L4: 4ring-Cs(Val7O2s)-Cs(Val7CsH)
                L5: 4ring-Cs(BrO2s)-Cs(BrCsH)
                L5: 4ring-Cs(FO2s)-Cs(FCsH)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_144
                L5: 4ring-Cs(BrCsH)-Cs(BrBrCs)_325
                L5: 4ring-Cs(ClCsH)-Cs(ClClCs)
                L5: 4ring-Cs(FCsH)-Cs(FFCs)_620
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7O2s)_146
                L5: 4ring-Cs(BrCsH)-Cs(BrBrO2s)_327
                L5: 4ring-Cs(ClCsH)-Cs(ClClO2s)_485
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_151
                L5: 4ring-Cs(BrBrCs)-Cs(BrCsH)_332
                L5: 4ring-Cs(ClClCs)-Cs(ClCsH)
                L5: 4ring-Cs(FFCs)-Cs(FCsH)_559
            L4: 4ring-Cs(Val7CsH)-Cs(Val7CsH)_154
                L5: 4ring-Cs(BrCsH)-Cs(BrCsH)_335
                L5: 4ring-Cs(ClCsH)-Cs(ClCsH)_429
                L5: 4ring-Cs(FCsH)-Cs(FCsH)_619
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_155
                L5: 4ring-Cs(BrCsH)-Cs(BrBrCs)_336
                L5: 4ring-Cs(ClCsH)-Cs(ClClCs)_473
                L5: 4ring-Cs(FCsH)-Cs(FFCs)_616
            L4: 4ring-Cs(Val7O2s)-Cd(Val7Cd)
                L5: 4ring-Cs(BrO2s)-Cd(BrCd)
                L5: 4ring-Cs(FO2s)-Cd(FCd)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7O2s)_160
                L5: 4ring-Cd(BrCs)=Cd(BrO2s)_341
                L5: 4ring-Cd(ClCs)=Cd(ClO2s)
                L5: 4ring-Cd(FCs)=Cd(FO2s)
            L4: 4ring-Cd(Val7O2s)=Cd(Val7Cs)_162
                L5: 4ring-Cd(BrO2s)=Cd(BrCs)_343
                L5: 4ring-Cd(ClO2s)=Cd(ClCs)_448
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7CsH)
                L5: 4ring-Cs(BrO2sH)-Cs(BrCsH)
                L5: 4ring-Cs(ClO2sH)-Cs(ClCsH)_477
                L5: 4ring-Cs(FO2sH)-Cs(FCsH)_643
            L4: 4ring-Cs(Val7CdH)-Cs(Val7CdH)_167
                L5: 4ring-Cs(BrCdH)-Cs(BrCdH)_348
                L5: 4ring-Cs(ClCdH)-Cs(ClCdH)_490
                L5: 4ring-Cs(FCdH)-Cs(FCdH)
            L4: 4ring-Cs(Val7Val7O2s)-Cd(Val7Cd)_168
                L5: 4ring-Cs(BrBrO2s)-Cd(BrCd)_349
                L5: 4ring-Cs(FFO2s)-Cd(FCd)_641
            L4: 4ring-Cd(Val7O2s)=Cd(Val7O2s)
                L5: 4ring-Cd(BrO2s)=Cd(BrO2s)
                L5: 4ring-Cd(ClO2s)=Cd(ClO2s)
                L5: 4ring-Cd(FO2s)=Cd(FO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7CsH)_173
                L5: 4ring-Cs(BrCsH)-Cs(BrCsH)_354
                L5: 4ring-Cs(ClCsH)-Cs(ClCsH)_422
                L5: 4ring-Cs(FCsH)-Cs(FCsH)
            L4: 4ring-Cd(Val7Cd)-Cd(Val7Cd)_175
                L5: 4ring-Cd(BrCd)-Cd(BrCd)_356
                L5: 4ring-Cd(ClCd)-Cd(ClCd)_487
            L4: 4ring-Cd(Val7Cd)=Cd(Val7Cd)_176
                L5: 4ring-Cd(BrCd)=Cd(BrCd)_357
                L5: 4ring-Cd(ClCd)=Cd(ClCd)_488
            L4: 4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)_177
                L5: 4ring-Cs(BrBrCs)-Cd(BrCd)_358
                L5: 4ring-Cs(ClClCs)-Cd(ClCd)_460
                L5: 4ring-Cs(FFCs)-Cd(FCd)
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7CsH)
                L5: 4ring-Cs(BrBrO2s)-Cs(BrCsH)
                L5: 4ring-Cs(ClClO2s)-Cs(ClCsH)_436
                L5: 4ring-Cs(FFO2s)-Cs(FCsH)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)_181
                L5: 4ring-Cd(BrCd)-Cs(BrBrCs)_362
                L5: 4ring-Cd(FCd)-Cs(FFCs)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Cs)
                L5: 4ring-Cs(BrO2sH)-Cs(BrCs)
                L5: 4ring-Cs(ClO2sH)-Cs(ClCs)
                L5: 4ring-Cs(FO2sH)-Cs(FCs)
            L4: 4ring-Cs(Val7O2sH)-Cd(Val7Cd)_183
                L5: 4ring-Cs(BrO2sH)-Cd(BrCd)_364
                L5: 4ring-Cs(ClO2sH)-Cd(ClCd)_500
                L5: 4ring-Cs(FO2sH)-Cd(FCd)_649
            L4: 4ring-Cd(Val7Cd)-Cs(Val7O2s)
                L5: 4ring-Cd(ClCd)-Cs(ClO2s)
                L5: 4ring-Cd(FCd)-Cs(FO2s)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Val7Cs)_185
                L5: 4ring-Cs(ClO2sH)-Cs(ClClCs)
                L5: 4ring-Cs(FO2sH)-Cs(FFCs)_644
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_187
                L5: 4ring-Cs(ClClCs)-Cs(ClClCs)
                L5: 4ring-Cs(FFCs)-Cs(FFCs)
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)_188
                L5: 4ring-Cs(ClCdH)-Cs(ClClCd)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)_190
                L5: 4ring-Cs(ClClCd)-Cs(ClCdH)
                L5: 4ring-Cs(FFCd)-Cs(FCdH)_606
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7CsH)_191
                L5: 4ring-Cs(ClClO2s)-Cs(ClCsH)
                L5: 4ring-Cs(FFO2s)-Cs(FCsH)_636
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_193
                L5: 4ring-Cs(ClClCs)-Cs(ClCsH)_428
                L5: 4ring-Cs(FFCs)-Cs(FCsH)_579
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7CsH)_194
                L5: 4ring-Cs(ClO2sH)-Cs(ClCsH)
                L5: 4ring-Cs(FO2sH)-Cs(FCsH)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7O2s)
                L5: 4ring-Cd(ClCd)-Cs(ClClO2s)
                L5: 4ring-Cd(FCd)-Cs(FFO2s)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Cd)
                L5: 4ring-Cs(ClClCd)-Cs(ClCd)
            L4: 4ring-Cs(Val7CsH)-Cd(Val7Cd)_201
                L5: 4ring-Cs(ClCsH)-Cd(ClCd)_472
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)_202
                L5: 4ring-Cs(ClClCd)-Cs(ClClCd)_475
            L4: 4ring-Cs(Val7O2s)-Cs(Val7O2sH)
                L5: 4ring-Cs(ClO2s)-Cs(ClO2sH)
            L4: 4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)_204
                L5: 4ring-Cs(ClClCs)-Cd(ClCd)_495
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7O2s)_206
                L5: 4ring-Cd(ClCd)-Cs(ClClO2s)_499
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7Cs)
                L5: 4ring-Cs(FFO2s)-Cs(FCs)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)_208
                L5: 4ring-Cs(FFCd)-Cs(FFCd)
            L4: 4ring-Cs(Val7O2s)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(FO2s)-Cs(FFO2s)
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(FFO2s)-Cs(FFCs)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)_214
                L5: 4ring-Cs(FFCd)-Cs(FCdH)_632
            L4: 4ring-Cd(Val7Cd)=Cd(Val7Cd)_215
                L5: 4ring-Cd(FCd)=Cd(FCd)_638
            L4: 4ring-Cd(Val7Cd)-Cd(Val7Cd)_216
                L5: 4ring-Cd(FCd)-Cd(FCd)_639
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
"""
)

