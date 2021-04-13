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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sCsCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCsCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "3ring-Cs(F1sCsH)-Cs(F1sCsCs)_624",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "3ring-Cs(F1sCsH)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "3ring-Cs(Cl1sCsCs)-Cs(Cl1sCsH)_424",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sCsH)_607",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "3ring-Cs(Br1sCdH)-Cd(Br1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "3ring-Cs(F1sCdH)-Cd(F1sCd)_612",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "3ring-Cd(Br1sCs)=Cd(Br1sCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "3ring-Cd(Cl1sCs)=Cd(Cl1sCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "3ring-Cd(F1sCs)=Cd(F1sCs)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)_385",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "3ring-Cs(Br1sCs)-Cs(Br1sCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "3ring-Cs(Cl1sCs)-Cs(Cl1sCsH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "3ring-Cs(F1sCs)-Cs(F1sCsH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "3ring-Cs(Br1sCs)-Cs(Br1sBr1sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "3ring-Cs(Cl1sCs)-Cs(Cl1sCl1sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "3ring-Cs(F1sCs)-Cs(F1sF1sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)_498",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsCs)_471",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sCsCs)_574",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "3ring-Cs(Br1sCdH)-Cd(Br1sCd)_242",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "3ring-Cs(Cl1sCdH)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "3ring-Cs(F1sCdH)-Cd(F1sCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "3ring-Cs(Br1sCdCs)-Cd(Br1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "3ring-Cs(Cl1sCdCs)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "3ring-Cs(Br1sCOH)-Cs(Br1sBr1sCO)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "3ring-Cs(Cl1sCOH)-Cs(Cl1sCl1sCO)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "3ring-Cs(F1sCOH)-Cs(F1sF1sCO)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "3ring-Cs(Br1sO2sCd)-Cd(Br1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "3ring-Cs(Cl1sO2sCd)-Cd(Cl1sCd)_453",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "3ring-Cs(Br1sBr1sO2s)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "3ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "3ring-Cs(F1sF1sO2s)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "3ring-Cd(Cl1sCd)-Cs(Cl1sCdH)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "3ring-Cd(F1sCd)-Cs(F1sCdH)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "3ring-Cs(Br1sCdH)-Cs(Br1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "3ring-Cs(Cl1sCdH)-Cs(Cl1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "3ring-Cs(F1sCdH)-Cs(F1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sCsCs)_253",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCsCs)_417",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "3ring-Cs(F1sCsH)-Cs(F1sCsCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "3ring-Cs(Br1sCs)-Cs(Br1sO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "3ring-Cs(Cl1sCs)-Cs(Cl1sO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "3ring-Cs(F1sCs)-Cs(F1sO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "3ring-Cs(Br1sO2sCs)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "3ring-Cs(F1sO2sCs)-Cs(F1sCsH)_578",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sBr1sCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "3ring-Cd(F1sCd)-Cs(F1sF1sCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "3ring-Cs(F1sCsH)-Cs(F1sCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "3ring-Cs(Br1sCs)-Cs(Br1sCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "3ring-Cs(Cl1sCs)-Cs(Cl1sCsCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "3ring-Cs(F1sCs)-Cs(F1sCsCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "3ring-Cs(Br1sBr1sCd)-Cs(Br1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "3ring-Cs(F1sF1sCd)-Cs(F1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)_264",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "3ring-Cs(F1sCsH)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sCsH)_268",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "3ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)_390",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "3ring-Cs(F1sCsH)-Cs(F1sCsH)_575",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "3ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "3ring-Cs(F1sF1sO2s)-Cs(F1sO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sO2sCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "3ring-Cd(F1sCd)-Cs(F1sO2sCd)_642",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "3ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "3ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "3ring-Cs(F1sF1sO2s)-Cs(F1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "3ring-Cs(Br1sO2sO2s)-Cs(Br1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "3ring-Cs(Cl1sO2sO2s)-Cs(Cl1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "3ring-Cs(F1sO2sO2s)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "3ring-Cs(Br1sO2s)-Cs(Br1sO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "3ring-Cs(Cl1sO2s)-Cs(Cl1sO2sCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "3ring-Cs(F1sO2s)-Cs(F1sO2sCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sCsH)_275",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "3ring-Cs(Cl1sCsCs)-Cs(Cl1sCsH)_466",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "3ring-Cs(F1sCsH)-Cs(F1sO2sCs)_645",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sCsCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "3ring-Cd(Cl1sCd)-Cs(Cl1sCsCd)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "3ring-Cd(F1sCd)-Cs(F1sCsCd)_567",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "3ring-Cd(Br1sCd)=Cd(Br1sCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "3ring-Cd(Cl1sCd)=Cd(Cl1sCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "3ring-Cd(F1sCd)=Cd(F1sCd)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    Cd  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)_285",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)_413",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)_536",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "3ring-Cs(Br1sO2sH)-Cs(Br1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "3ring-Cs(F1sO2sH)-Cs(F1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "3ring-Cd(Br1sCO)=Cd(Br1sCO)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "3ring-Cd(Cl1sCO)=Cd(Cl1sCO)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    CO   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "3ring-Cd(F1sCO)=Cd(F1sCO)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    CO  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "3ring-Cs(Br1sCd)-Cd(Br1sCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {2,S}
5    Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "3ring-Cs(Cl1sCd)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "3ring-Cs(F1sCd)-Cd(F1sCd)",
    group = 
"""
1 *1 Cs  u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {2,S}
5    F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "3ring-Cs(Br1sO2sCd)-Cd(Br1sCd)_293",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "3ring-Cs(Cl1sO2sCd)-Cd(Cl1sCd)_470",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "3ring-Cs(F1sO2sCd)-Cd(F1sCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)_297",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sCsH)_586",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "3ring-Cs(Br1sO2sH)-Cs(Br1sO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "3ring-Cs(F1sO2sH)-Cs(F1sO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    H   u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "3ring-Cs(Br1sO2sO2s)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "3ring-Cs(Cl1sO2sO2s)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "3ring-Cs(F1sO2sO2s)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sCdCs)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u1 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "3ring-Cd(F1sCd)-Cs(F1sCdCs)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u1 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sCd)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "3ring-Cd(F1sCd)-Cs(F1sCd)",
    group = 
"""
1 *2 Cs  u1 p0 c0 {2,S} {3,S} {4,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {5,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "3ring-Cs(Cl1sCsCs)-Cs(Cl1sCl1sCs)_459",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sCsH)_319",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "3ring-Cs(Cl1sCsCs)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sCsH)_554",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "3ring-Cd(Br1sCd)-Cs(Br1sCsCd)_321",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "3ring-Cd(F1sCd)-Cs(F1sCsCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "3ring-Cs(Br1sO2sCd)-Cd(Br1sCd)_322",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u1 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "3ring-Cs(Cl1sO2sCd)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u1 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "3ring-Cd(Br1sCs)=Cd(Br1sCs)_326",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "3ring-Cd(Cl1sCs)=Cd(Cl1sCs)_392",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs   u1 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "3ring-Cd(F1sCs)=Cd(F1sCs)_560",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {5,S}
3    Cs  u1 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "3ring-Cs(Br1sO2sCs)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "3ring-Cs(Br1sO2sCs)-Cs(Br1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCs)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "3ring-Cs(F1sO2sCs)-Cs(F1sCs)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "3ring-Cs(Br1sCOH)-Cs(Br1sCOH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "3ring-Cs(Cl1sCOH)-Cs(Cl1sCOH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "3ring-Cs(F1sCOH)-Cs(F1sCOH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "3ring-Cs(Br1sO2sH)-Cs(Br1sO2sCs)_331",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sCs)_389",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sBr1sCs)_333",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "3ring-Cs(Cl1sCsCs)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sF1sCs)_605",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "3ring-Cs(Br1sBr1sCd)-Cs(Br1sBr1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "3ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "3ring-Cs(F1sF1sCd)-Cs(F1sF1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "3ring-Cs(Br1sO2sCs)-Cs(Br1sCsH)_337",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCsH)_468",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "3ring-Cs(F1sO2sCs)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sCs)_338",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sO2sCs)_602",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsCs)_339",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sCsCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "3ring-Cs(Br1sO2sO2s)-Cs(Br1sO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Br1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "3ring-Cs(Cl1sO2sO2s)-Cs(Cl1sO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    O2s  u0 p2 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "3ring-Cs(F1sO2sO2s)-Cs(F1sO2s)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {1,S} {2,S}
4    F1s u0 p3 c0 {1,S}
5    O2s u0 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "3ring-Cs(Br1sBr1sCO)-Cs(Br1sBr1sCO)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "3ring-Cs(Cl1sCl1sCO)-Cs(Cl1sCl1sCO)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "3ring-Cs(F1sF1sCO)-Cs(F1sF1sCO)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "3ring-Cs(Br1sO2sH)-Cs(Br1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "3ring-Cs(F1sO2sH)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "3ring-Cs(Br1sBr1sCd)-Cd(Br1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "3ring-Cs(Cl1sCl1sCd)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "3ring-Cs(F1sF1sCd)-Cd(F1sCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sCsCs)_351",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "3ring-Cs(F1sCsH)-Cs(F1sCsCs)_551",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "3ring-Cs(Br1sCsCs)-Cs(Br1sBr1sCs)_352",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "3ring-Cs(F1sCsCs)-Cs(F1sF1sCs)_610",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "3ring-Cs(Br1sBr1sCd)-Cd(Br1sCd)_353",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Br1s u0 p3 c0 {1,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "3ring-Cs(Cl1sCl1sCd)-Cd(Cl1sCd)_482",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "3ring-Cs(F1sF1sCd)-Cd(F1sCd)_637",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u1 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "3ring-Cs(Br1sO2sH)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "3ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "3ring-Cs(F1sO2sH)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "3ring-Cs(Br1sCsH)-Cs(Br1sO2sCs)_359",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "3ring-Cs(F1sCsH)-Cs(F1sO2sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "3ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2sCs)_361",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "3ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sO2sCs)_492",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "3ring-Cs(F1sF1sO2s)-Cs(F1sO2sCs)_553",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "3ring-Cs(Cl1sCsCd)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "3ring-Cs(Cl1sCdH)-Cs(Cl1sCl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "3ring-Cs(F1sCdH)-Cs(F1sF1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "3ring-Cd(Cl1sCd)-Cs(Cl1sCdH)_427",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u1 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    H    u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sO2s)",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "3ring-Cs(Cl1sCsCd)-Cd(Cl1sCd)_446",
    group = 
"""
1 *1 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd   u0 p0 c0 {1,S} {2,D}
4    Cl1s u0 p3 c0 {1,S}
5    Cs   u0 p0 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "3ring-Cs(F1sCsCd)-Cd(F1sCd)",
    group = 
"""
1 *1 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    Cs  u0 p0 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCl1sCs)_462",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "3ring-Cs(Cl1sO2s)-Cs(Cl1sCl1sO2s)",
    group = 
"""
1 *2 Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {2,S}
4    Cl1s u0 p3 c0 {1,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "3ring-Cs(F1sO2sCs)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "3ring-Cd(F1sCd)-Cs(F1sO2sCd)",
    group = 
"""
1 *2 Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3    Cd  u0 p0 c0 {1,S} {2,D}
4    F1s u0 p3 c0 {1,S}
5    O2s u1 p2 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "3ring-Cs(F1sF1sCs)-Cs(F1sCsCs)_622",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "4ring-Cd(Br1sCd)-Cd(Br1sCd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "4ring-Cd(Cl1sCd)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "4ring-Cd(F1sCd)-Cd(F1sCd)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd  u0 p0 c0 {1,D} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "4ring-Cd(Br1sCd)=Cd(Br1sCd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "4ring-Cd(Cl1sCd)=Cd(Cl1sCd)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd   u0 p0 c0 {2,S} {4,D}
4    Cd   u0 p0 c0 {1,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "4ring-Cd(F1sCd)=Cd(F1sCd)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    Cd  u0 p0 c0 {2,S} {4,D}
4    Cd  u0 p0 c0 {1,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "4ring-Cs(Br1sCdH)-Cs(Br1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "4ring-Cs(Cl1sCdH)-Cs(Cl1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "4ring-Cs(F1sCdH)-Cs(F1sCdH)_627",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "4ring-Cd(Br1sCs)=Cd(Br1sCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "4ring-Cd(Cl1sCs)=Cd(Cl1sCs)_435",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs   u0 p0 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "4ring-Cd(F1sCs)=Cd(F1sCs)_580",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    Cs  u0 p0 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCsH)_433",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "4ring-Cd(F1sCd)-Cs(F1sCsH)_582",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "4ring-Cd(F1sCd)-Cs(F1sF1sCs)_581",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "4ring-Cs(Br1sBr1sCd)-Cs(Br1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCdH)_479",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "4ring-Cs(F1sF1sCd)-Cs(F1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "4ring-Cs(Br1sO2sH)-Cd(Br1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "4ring-Cs(Cl1sO2sH)-Cd(Cl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "4ring-Cs(F1sO2sH)-Cd(F1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "4ring-Cd(Br1sCs)=Cd(Br1sO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "4ring-Cd(Cl1sCs)=Cd(Cl1sO2s)_445",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "4ring-Cd(F1sCs)=Cd(F1sO2s)_555",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u0 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "4ring-Cs(Br1sCdH)-Cs(Br1sBr1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "4ring-Cs(F1sCdH)-Cs(F1sF1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "4ring-Cs(Br1sBr1sO2s)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "4ring-Cs(F1sF1sO2s)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "4ring-Cs(F1sCsH)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "4ring-Cs(F1sCsH)-Cs(F1sCsH)_568",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)_467",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "4ring-Cs(F1sCsH)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "4ring-Cs(F1sCsH)-Cs(F1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sCsH)_243",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "4ring-Cd(F1sCd)-Cs(F1sCsH)_626",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "4ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "4ring-Cs(Br1sO2sH)-Cs(Br1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "4ring-Cs(Br1sCd)-Cs(Br1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "4ring-Cs(Cl1sCd)-Cs(Cl1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "4ring-Cs(F1sCd)-Cs(F1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "4ring-Cd(Br1sCs)=Cd(Br1sCs)_265",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "4ring-Cd(Cl1sCs)=Cd(Cl1sCs)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "4ring-Cd(F1sCs)=Cd(F1sCs)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sBr1sCs)_266",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "4ring-Cd(F1sCd)-Cs(F1sF1sCs)_596",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "4ring-Cs(Br1sCd)-Cs(Br1sBr1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "4ring-Cs(F1sCd)-Cs(F1sF1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "4ring-Cs(Br1sO2s)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "4ring-Cs(F1sO2s)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "4ring-Cd(Br1sCs)=Cd(Br1sCs)_277",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "4ring-Cd(Cl1sCs)=Cd(Cl1sCs)_461",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cs   u1 p0 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "4ring-Cd(F1sCs)=Cd(F1sCs)_565",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cs  u1 p0 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "4ring-Cs(Br1sCsH)-Cd(Br1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "4ring-Cs(Cl1sCsH)-Cd(Cl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "4ring-Cs(F1sCsH)-Cd(F1sCd)_652",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "4ring-Cs(Br1sBr1sCd)-Cs(Br1sBr1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "4ring-Cs(F1sF1sCd)-Cs(F1sF1sCd)_646",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "4ring-Cd(Br1sO2s)=Cd(Br1sCs)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "4ring-Cd(Cl1sO2s)=Cd(Cl1sCs)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "4ring-Cs(Br1sBr1sO2s)-Cd(Br1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "4ring-Cs(F1sF1sO2s)-Cd(F1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "4ring-Cs(Br1sCs)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "4ring-Cs(Cl1sCs)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "4ring-Cs(F1sCs)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "4ring-Cs(Br1sCs)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "4ring-Cs(Cl1sCs)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "4ring-Cs(F1sCs)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sCs)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 496,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCs)",
    group = 
"""
1 *2 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 497,
    label = "4ring-Cd(F1sCd)-Cs(F1sCs)",
    group = 
"""
1 *2 Cs  u1 p0 c0 {2,S} {3,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)_577",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "4ring-Cs(Br1sO2sH)-Cs(Br1sBr1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sCs)_396",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 506,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
    label = "4ring-Cs(Br1sO2sH)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 509,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 510,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 513,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sO2sH)_300",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "4ring-Cs(F1sCsH)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)_491",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "4ring-Cs(Br1sCs)-Cd(Br1sCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "4ring-Cs(Cl1sCs)-Cd(Cl1sCd)",
    group = 
"""
1 *1 Cs   u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs   u0 p0 c0 {1,S} {4,S}
4    Cd   u0 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "4ring-Cs(F1sCs)-Cd(F1sCd)",
    group = 
"""
1 *1 Cs  u1 p0 c0 {2,S} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cs  u0 p0 c0 {1,S} {4,S}
4    Cd  u0 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "4ring-Cs(Br1sCsH)-Cd(Br1sCd)_305",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "4ring-Cs(Cl1sCsH)-Cd(Cl1sCd)_440",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 530,
    label = "4ring-Cs(F1sCsH)-Cd(F1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 533,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 535,
    label = "4ring-Cs(Br1sCdH)-Cs(Br1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "4ring-Cs(F1sCdH)-Cs(F1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "4ring-Cs(Br1sCs)-Cs(Br1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "4ring-Cs(Cl1sCs)-Cs(Cl1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "4ring-Cs(F1sCs)-Cs(F1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "4ring-Cs(Br1sCs)-Cs(Br1sBr1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "4ring-Cs(Cl1sCs)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "4ring-Cs(F1sCs)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sH)_311",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)_312",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)_423",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)_600",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "4ring-Cs(Br1sBr1sCs)-Cd(Br1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "4ring-Cs(Cl1sCl1sCs)-Cd(Cl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 556,
    label = "4ring-Cs(F1sF1sCs)-Cd(F1sCd)_552",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sO2s)_314",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 559,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sF1sO2s)_635",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "4ring-Cs(Br1sCdH)-Cs(Br1sBr1sCd)_316",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "4ring-Cs(F1sCdH)-Cs(F1sF1sCd)_650",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "4ring-Cs(Br1sO2sH)-Cs(Br1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sCsH)_323",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCsH)_483",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "4ring-Cd(F1sCd)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "4ring-Cs(Br1sO2s)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "4ring-Cs(F1sO2s)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)_325",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "4ring-Cs(F1sCsH)-Cs(F1sF1sCs)_620",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sBr1sO2s)_327",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 579,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sO2s)_485",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "4ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)_332",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sCsH)_559",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sCsH)_335",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)_429",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 587,
    label = "4ring-Cs(F1sCsH)-Cs(F1sCsH)_619",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 589,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)_336",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 590,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)_473",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 591,
    label = "4ring-Cs(F1sCsH)-Cs(F1sF1sCs)_616",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "4ring-Cs(Br1sO2s)-Cd(Br1sCd)",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 *1 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cd   u0 p0 c0 {1,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 594,
    label = "4ring-Cs(F1sO2s)-Cd(F1sCd)",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,S} {4,D} {5,S}
2 *1 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cd  u0 p0 c0 {1,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "4ring-Cd(Br1sCs)=Cd(Br1sO2s)_341",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 597,
    label = "4ring-Cd(Cl1sCs)=Cd(Cl1sO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u1 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "4ring-Cd(F1sCs)=Cd(F1sO2s)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {4,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cs  u1 p0 c0 {1,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "4ring-Cd(Br1sO2s)=Cd(Br1sCs)_343",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "4ring-Cd(Cl1sO2s)=Cd(Cl1sCs)_448",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 Cd   u0 p0 c0 {1,D} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cs   u0 p0 c0 {1,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 603,
    label = "4ring-Cs(Br1sO2sH)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 604,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sCsH)_477",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sCsH)_643",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "4ring-Cs(Br1sCdH)-Cs(Br1sCdH)_348",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "4ring-Cs(Cl1sCdH)-Cs(Cl1sCdH)_490",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "4ring-Cs(F1sCdH)-Cs(F1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "4ring-Cs(Br1sBr1sO2s)-Cd(Br1sCd)_349",
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
    label = "4ring-Cs(F1sF1sO2s)-Cd(F1sCd)_641",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "4ring-Cd(Br1sO2s)=Cd(Br1sO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 615,
    label = "4ring-Cd(Cl1sO2s)=Cd(Cl1sO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s  u0 p2 c0 {1,S} {4,S}
4    O2s  u0 p2 c0 {2,S} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 616,
    label = "4ring-Cd(F1sO2s)=Cd(F1sO2s)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    O2s u0 p2 c0 {1,S} {4,S}
4    O2s u0 p2 c0 {2,S} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "4ring-Cs(Br1sCsH)-Cs(Br1sCsH)_354",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "4ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)_422",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "4ring-Cs(F1sCsH)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "4ring-Cd(Br1sCd)-Cd(Br1sCd)_356",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "4ring-Cd(Cl1sCd)-Cd(Cl1sCd)_487",
    group = 
"""
1 *2 Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 *1 Cd   u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd   u0 p0 c0 {1,D} {4,S}
4    Cd   u1 p0 c0 {2,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "4ring-Cd(Br1sCd)=Cd(Br1sCd)_357",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Br1s u0 p3 c0 {1,S}
6    Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 626,
    label = "4ring-Cd(Cl1sCd)=Cd(Cl1sCd)_488",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 *2 Cd   u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd   u0 p0 c0 {1,S} {4,D}
4    Cd   u1 p0 c0 {2,S} {3,D}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 628,
    label = "4ring-Cs(Br1sBr1sCs)-Cd(Br1sCd)_358",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 629,
    label = "4ring-Cs(Cl1sCl1sCs)-Cd(Cl1sCd)_460",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 630,
    label = "4ring-Cs(F1sF1sCs)-Cd(F1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 632,
    label = "4ring-Cs(Br1sBr1sO2s)-Cs(Br1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 633,
    label = "4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCsH)_436",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 634,
    label = "4ring-Cs(F1sF1sO2s)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 636,
    label = "4ring-Cd(Br1sCd)-Cs(Br1sBr1sCs)_362",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 637,
    label = "4ring-Cd(F1sCd)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 639,
    label = "4ring-Cs(Br1sO2sH)-Cs(Br1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 640,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 641,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 643,
    label = "4ring-Cs(Br1sO2sH)-Cd(Br1sCd)_364",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 644,
    label = "4ring-Cs(Cl1sO2sH)-Cd(Cl1sCd)_500",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 645,
    label = "4ring-Cs(F1sO2sH)-Cd(F1sCd)_649",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 647,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sO2s)",
    group = 
"""
1 *1 Cd   u0 p0 c0 {2,S} {4,D} {5,S}
2 *2 Cs   u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s  u0 p2 c0 {2,S} {4,S}
4    Cd   u0 p0 c0 {1,D} {3,S}
5    Cl1s u0 p3 c0 {1,S}
6    Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 648,
    label = "4ring-Cd(F1sCd)-Cs(F1sO2s)",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,S} {4,D} {5,S}
2 *2 Cs  u1 p0 c0 {1,S} {3,S} {6,S}
3    O2s u0 p2 c0 {2,S} {4,S}
4    Cd  u0 p0 c0 {1,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 650,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 651,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sF1sCs)_644",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 653,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 654,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 656,
    label = "4ring-Cs(Cl1sCdH)-Cs(Cl1sCl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 658,
    label = "4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCdH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 659,
    label = "4ring-Cs(F1sF1sCd)-Cs(F1sCdH)_606",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 661,
    label = "4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 662,
    label = "4ring-Cs(F1sF1sO2s)-Cs(F1sCsH)_636",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 664,
    label = "4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)_428",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 665,
    label = "4ring-Cs(F1sF1sCs)-Cs(F1sCsH)_579",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 667,
    label = "4ring-Cs(Cl1sO2sH)-Cs(Cl1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 668,
    label = "4ring-Cs(F1sO2sH)-Cs(F1sCsH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 670,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCl1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 671,
    label = "4ring-Cd(F1sCd)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 673,
    label = "4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 675,
    label = "4ring-Cs(Cl1sCsH)-Cd(Cl1sCd)_472",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 677,
    label = "4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCl1sCd)_475",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 679,
    label = "4ring-Cs(Cl1sO2s)-Cs(Cl1sO2sH)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 681,
    label = "4ring-Cs(Cl1sCl1sCs)-Cd(Cl1sCd)_495",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 683,
    label = "4ring-Cd(Cl1sCd)-Cs(Cl1sCl1sO2s)_499",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 685,
    label = "4ring-Cs(F1sF1sO2s)-Cs(F1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 687,
    label = "4ring-Cs(F1sF1sCd)-Cs(F1sF1sCd)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 689,
    label = "4ring-Cs(F1sO2s)-Cs(F1sF1sO2s)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 691,
    label = "4ring-Cs(F1sF1sO2s)-Cs(F1sF1sCs)",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 693,
    label = "4ring-Cs(F1sF1sCd)-Cs(F1sCdH)_632",
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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 695,
    label = "4ring-Cd(F1sCd)=Cd(F1sCd)_638",
    group = 
"""
1 *2 Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 Cd  u0 p0 c0 {1,D} {4,S} {6,S}
3    Cd  u0 p0 c0 {1,S} {4,D}
4    Cd  u1 p0 c0 {2,S} {3,D}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

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
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 697,
    label = "4ring-Cd(F1sCd)-Cd(F1sCd)_639",
    group = 
"""
1 *1 Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 *2 Cd  u0 p0 c0 {1,S} {4,D} {6,S}
3    Cd  u0 p0 c0 {1,D} {4,S}
4    Cd  u1 p0 c0 {2,D} {3,S}
5    F1s u0 p3 c0 {1,S}
6    F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
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
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sCsCs)
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCsCs)
                L5: 3ring-Cs(F1sCsH)-Cs(F1sCsCs)_624
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsH)
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sCsH)
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)
                L5: 3ring-Cs(F1sCsH)-Cs(F1sCsH)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7CsH)
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sCsH)
                L5: 3ring-Cs(Cl1sCsCs)-Cs(Cl1sCsH)_424
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sCsH)_607
            L4: 3ring-Cs(Val7CdH)-Cd(Val7Cd)
                L5: 3ring-Cs(Br1sCdH)-Cd(Br1sCd)
                L5: 3ring-Cs(F1sCdH)-Cd(F1sCd)_612
            L4: 3ring-Cd(Val7Cs)=Cd(Val7Cs)
                L5: 3ring-Cd(Br1sCs)=Cd(Br1sCs)
                L5: 3ring-Cd(Cl1sCs)=Cd(Cl1sCs)
                L5: 3ring-Cd(F1sCs)=Cd(F1sCs)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsH)
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)_385
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sCsH)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7CsH)
                L5: 3ring-Cs(Br1sCs)-Cs(Br1sCsH)
                L5: 3ring-Cs(Cl1sCs)-Cs(Cl1sCsH)
                L5: 3ring-Cs(F1sCs)-Cs(F1sCsH)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(Br1sCs)-Cs(Br1sBr1sCs)
                L5: 3ring-Cs(Cl1sCs)-Cs(Cl1sCl1sCs)
                L5: 3ring-Cs(F1sCs)-Cs(F1sF1sCs)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)_498
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsCs)
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsCs)_471
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sCsCs)_574
            L4: 3ring-Cs(Val7CdH)-Cd(Val7Cd)_61
                L5: 3ring-Cs(Br1sCdH)-Cd(Br1sCd)_242
                L5: 3ring-Cs(Cl1sCdH)-Cd(Cl1sCd)
                L5: 3ring-Cs(F1sCdH)-Cd(F1sCd)
            L4: 3ring-Cs(Val7CdCs)-Cd(Val7Cd)
                L5: 3ring-Cs(Br1sCdCs)-Cd(Br1sCd)
                L5: 3ring-Cs(Cl1sCdCs)-Cd(Cl1sCd)
            L4: 3ring-Cs(Val7COH)-Cs(Val7Val7CO)
                L5: 3ring-Cs(Br1sCOH)-Cs(Br1sBr1sCO)
                L5: 3ring-Cs(Cl1sCOH)-Cs(Cl1sCl1sCO)
                L5: 3ring-Cs(F1sCOH)-Cs(F1sF1sCO)
            L4: 3ring-Cs(Val7O2sCd)-Cd(Val7Cd)
                L5: 3ring-Cs(Br1sO2sCd)-Cd(Br1sCd)
                L5: 3ring-Cs(Cl1sO2sCd)-Cd(Cl1sCd)_453
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(Br1sBr1sO2s)-Cs(Br1sBr1sO2s)
                L5: 3ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCl1sO2s)
                L5: 3ring-Cs(F1sF1sO2s)-Cs(F1sF1sO2s)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CdH)
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sCdH)
                L5: 3ring-Cd(Cl1sCd)-Cs(Cl1sCdH)
                L5: 3ring-Cd(F1sCd)-Cs(F1sCdH)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7Cs)
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sCs)
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCs)
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sCs)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Cs)
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sCs)
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sCs)
            L4: 3ring-Cs(Val7CdH)-Cs(Val7CdH)
                L5: 3ring-Cs(Br1sCdH)-Cs(Br1sCdH)
                L5: 3ring-Cs(Cl1sCdH)-Cs(Cl1sCdH)
                L5: 3ring-Cs(F1sCdH)-Cs(F1sCdH)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsCs)_72
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sCsCs)_253
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCsCs)_417
                L5: 3ring-Cs(F1sCsH)-Cs(F1sCsCs)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7O2sCs)
                L5: 3ring-Cs(Br1sCs)-Cs(Br1sO2sCs)
                L5: 3ring-Cs(Cl1sCs)-Cs(Cl1sO2sCs)
                L5: 3ring-Cs(F1sCs)-Cs(F1sO2sCs)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7CsH)
                L5: 3ring-Cs(Br1sO2sCs)-Cs(Br1sCsH)
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCsH)
                L5: 3ring-Cs(F1sO2sCs)-Cs(F1sCsH)_578
            L4: 3ring-Cd(Val7Cd)-Cs(Val7Val7Cd)
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sBr1sCd)
                L5: 3ring-Cd(F1sCd)-Cs(F1sF1sCd)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7Cs)
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sCs)
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCs)
                L5: 3ring-Cs(F1sCsH)-Cs(F1sCs)
            L4: 3ring-Cs(Val7Cs)-Cs(Val7CsCs)
                L5: 3ring-Cs(Br1sCs)-Cs(Br1sCsCs)
                L5: 3ring-Cs(Cl1sCs)-Cs(Cl1sCsCs)
                L5: 3ring-Cs(F1sCs)-Cs(F1sCsCs)
            L4: 3ring-Cs(Val7Val7Cd)-Cs(Val7CdH)
                L5: 3ring-Cs(Br1sBr1sCd)-Cs(Br1sCdH)
                L5: 3ring-Cs(F1sF1sCd)-Cs(F1sCdH)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_83
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)_264
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)
                L5: 3ring-Cs(F1sCsH)-Cs(F1sF1sCs)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsH)_87
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sCsH)_268
                L5: 3ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)_390
                L5: 3ring-Cs(F1sCsH)-Cs(F1sCsH)_575
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7O2s)
                L5: 3ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2s)
                L5: 3ring-Cs(F1sF1sO2s)-Cs(F1sO2s)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7O2sCd)
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sO2sCd)
                L5: 3ring-Cd(F1sCd)-Cs(F1sO2sCd)_642
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7O2sCs)
                L5: 3ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2sCs)
                L5: 3ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sO2sCs)
                L5: 3ring-Cs(F1sF1sO2s)-Cs(F1sO2sCs)
            L4: 3ring-Cs(Val7O2sO2s)-Cs(Val7O2sH)
                L5: 3ring-Cs(Br1sO2sO2s)-Cs(Br1sO2sH)
                L5: 3ring-Cs(Cl1sO2sO2s)-Cs(Cl1sO2sH)
                L5: 3ring-Cs(F1sO2sO2s)-Cs(F1sO2sH)
            L4: 3ring-Cs(Val7O2s)-Cs(Val7O2sCs)
                L5: 3ring-Cs(Br1sO2s)-Cs(Br1sO2sCs)
                L5: 3ring-Cs(Cl1sO2s)-Cs(Cl1sO2sCs)
                L5: 3ring-Cs(F1sO2s)-Cs(F1sO2sCs)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7CsH)_94
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sCsH)_275
                L5: 3ring-Cs(Cl1sCsCs)-Cs(Cl1sCsH)_466
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sCsH)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7O2sCs)
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sO2sCs)
                L5: 3ring-Cs(F1sCsH)-Cs(F1sO2sCs)_645
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CsCd)
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sCsCd)
                L5: 3ring-Cd(Cl1sCd)-Cs(Cl1sCsCd)
                L5: 3ring-Cd(F1sCd)-Cs(F1sCsCd)_567
            L4: 3ring-Cd(Val7Cd)=Cd(Val7Cd)
                L5: 3ring-Cd(Br1sCd)=Cd(Br1sCd)
                L5: 3ring-Cd(Cl1sCd)=Cd(Cl1sCd)
                L5: 3ring-Cd(F1sCd)=Cd(F1sCd)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_104
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)_285
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)_413
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)_536
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7O2sCs)
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sCs)
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sO2sCs)
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2sCs)
                L5: 3ring-Cs(Br1sO2sH)-Cs(Br1sO2sCs)
                L5: 3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sCs)
                L5: 3ring-Cs(F1sO2sH)-Cs(F1sO2sCs)
            L4: 3ring-Cd(Val7CO)=Cd(Val7CO)
                L5: 3ring-Cd(Br1sCO)=Cd(Br1sCO)
                L5: 3ring-Cd(Cl1sCO)=Cd(Cl1sCO)
                L5: 3ring-Cd(F1sCO)=Cd(F1sCO)
            L4: 3ring-Cs(Val7Cd)-Cd(Val7Cd)
                L5: 3ring-Cs(Br1sCd)-Cd(Br1sCd)
                L5: 3ring-Cs(Cl1sCd)-Cd(Cl1sCd)
                L5: 3ring-Cs(F1sCd)-Cd(F1sCd)
            L4: 3ring-Cs(Val7O2sCd)-Cd(Val7Cd)_112
                L5: 3ring-Cs(Br1sO2sCd)-Cd(Br1sCd)_293
                L5: 3ring-Cs(Cl1sO2sCd)-Cd(Cl1sCd)_470
                L5: 3ring-Cs(F1sO2sCd)-Cd(F1sCd)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_116
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)_297
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sCsH)_586
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2s)
                L5: 3ring-Cs(Br1sO2sH)-Cs(Br1sO2s)
                L5: 3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2s)
                L5: 3ring-Cs(F1sO2sH)-Cs(F1sO2s)
            L4: 3ring-Cs(Val7O2sO2s)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(Br1sO2sO2s)-Cs(Br1sBr1sO2s)
                L5: 3ring-Cs(Cl1sO2sO2s)-Cs(Cl1sCl1sO2s)
                L5: 3ring-Cs(F1sO2sO2s)-Cs(F1sF1sO2s)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CdCs)
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sCdCs)
                L5: 3ring-Cd(F1sCd)-Cs(F1sCdCs)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7Cd)
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sCd)
                L5: 3ring-Cd(F1sCd)-Cs(F1sCd)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sBr1sCs)
                L5: 3ring-Cs(Cl1sCsCs)-Cs(Cl1sCl1sCs)_459
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sF1sCs)
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7CsH)_138
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sCsH)_319
                L5: 3ring-Cs(Cl1sCsCs)-Cs(Cl1sCsH)
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sCsH)_554
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CsCd)_140
                L5: 3ring-Cd(Br1sCd)-Cs(Br1sCsCd)_321
                L5: 3ring-Cd(F1sCd)-Cs(F1sCsCd)
            L4: 3ring-Cs(Val7O2sCd)-Cd(Val7Cd)_141
                L5: 3ring-Cs(Br1sO2sCd)-Cd(Br1sCd)_322
                L5: 3ring-Cs(Cl1sO2sCd)-Cd(Cl1sCd)
            L4: 3ring-Cd(Val7Cs)=Cd(Val7Cs)_145
                L5: 3ring-Cd(Br1sCs)=Cd(Br1sCs)_326
                L5: 3ring-Cd(Cl1sCs)=Cd(Cl1sCs)_392
                L5: 3ring-Cd(F1sCs)=Cd(F1sCs)_560
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Val7Cs)
                L5: 3ring-Cs(Br1sO2sCs)-Cs(Br1sBr1sCs)
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCl1sCs)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Cs)
                L5: 3ring-Cs(Br1sO2sCs)-Cs(Br1sCs)
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCs)
                L5: 3ring-Cs(F1sO2sCs)-Cs(F1sCs)
            L4: 3ring-Cs(Val7COH)-Cs(Val7COH)
                L5: 3ring-Cs(Br1sCOH)-Cs(Br1sCOH)
                L5: 3ring-Cs(Cl1sCOH)-Cs(Cl1sCOH)
                L5: 3ring-Cs(F1sCOH)-Cs(F1sCOH)
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2sCs)_150
                L5: 3ring-Cs(Br1sO2sH)-Cs(Br1sO2sCs)_331
                L5: 3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sCs)_389
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)_152
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sBr1sCs)_333
                L5: 3ring-Cs(Cl1sCsCs)-Cs(Cl1sCl1sCs)
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sF1sCs)_605
            L4: 3ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)
                L5: 3ring-Cs(Br1sBr1sCd)-Cs(Br1sBr1sCd)
                L5: 3ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCl1sCd)
                L5: 3ring-Cs(F1sF1sCd)-Cs(F1sF1sCd)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7CsH)_156
                L5: 3ring-Cs(Br1sO2sCs)-Cs(Br1sCsH)_337
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCsH)_468
                L5: 3ring-Cs(F1sO2sCs)-Cs(F1sCsH)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7O2sCs)_157
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sCs)_338
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sO2sCs)_602
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)_158
                L5: 3ring-Cs(Br1sBr1sCs)-Cs(Br1sCsCs)_339
                L5: 3ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsCs)
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sCsCs)
            L4: 3ring-Cs(Val7O2sO2s)-Cs(Val7O2s)
                L5: 3ring-Cs(Br1sO2sO2s)-Cs(Br1sO2s)
                L5: 3ring-Cs(Cl1sO2sO2s)-Cs(Cl1sO2s)
                L5: 3ring-Cs(F1sO2sO2s)-Cs(F1sO2s)
            L4: 3ring-Cs(Val7Val7CO)-Cs(Val7Val7CO)
                L5: 3ring-Cs(Br1sBr1sCO)-Cs(Br1sBr1sCO)
                L5: 3ring-Cs(Cl1sCl1sCO)-Cs(Cl1sCl1sCO)
                L5: 3ring-Cs(F1sF1sCO)-Cs(F1sF1sCO)
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7O2sH)
                L5: 3ring-Cs(Br1sO2sH)-Cs(Br1sO2sH)
                L5: 3ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sH)
                L5: 3ring-Cs(F1sO2sH)-Cs(F1sO2sH)
            L4: 3ring-Cs(Val7Val7Cd)-Cd(Val7Cd)
                L5: 3ring-Cs(Br1sBr1sCd)-Cd(Br1sCd)
                L5: 3ring-Cs(Cl1sCl1sCd)-Cd(Cl1sCd)
                L5: 3ring-Cs(F1sF1sCd)-Cd(F1sCd)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7CsCs)_170
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sCsCs)_351
                L5: 3ring-Cs(F1sCsH)-Cs(F1sCsCs)_551
            L4: 3ring-Cs(Val7CsCs)-Cs(Val7Val7Cs)_171
                L5: 3ring-Cs(Br1sCsCs)-Cs(Br1sBr1sCs)_352
                L5: 3ring-Cs(F1sCsCs)-Cs(F1sF1sCs)_610
            L4: 3ring-Cs(Val7Val7Cd)-Cd(Val7Cd)_172
                L5: 3ring-Cs(Br1sBr1sCd)-Cd(Br1sCd)_353
                L5: 3ring-Cs(Cl1sCl1sCd)-Cd(Cl1sCd)_482
                L5: 3ring-Cs(F1sF1sCd)-Cd(F1sCd)_637
            L4: 3ring-Cs(Val7O2sH)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(Br1sO2sH)-Cs(Br1sBr1sO2s)
                L5: 3ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sO2s)
                L5: 3ring-Cs(F1sO2sH)-Cs(F1sF1sO2s)
            L4: 3ring-Cs(Val7CsH)-Cs(Val7O2sCs)_178
                L5: 3ring-Cs(Br1sCsH)-Cs(Br1sO2sCs)_359
                L5: 3ring-Cs(F1sCsH)-Cs(F1sO2sCs)
            L4: 3ring-Cs(Val7Val7O2s)-Cs(Val7O2sCs)_180
                L5: 3ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2sCs)_361
                L5: 3ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sO2sCs)_492
                L5: 3ring-Cs(F1sF1sO2s)-Cs(F1sO2sCs)_553
            L4: 3ring-Cs(Val7CsCd)-Cd(Val7Cd)
                L5: 3ring-Cs(Cl1sCsCd)-Cd(Cl1sCd)
            L4: 3ring-Cs(Val7CdH)-Cs(Val7Val7Cd)
                L5: 3ring-Cs(Cl1sCdH)-Cs(Cl1sCl1sCd)
                L5: 3ring-Cs(F1sCdH)-Cs(F1sF1sCd)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7CdH)_192
                L5: 3ring-Cd(Cl1sCd)-Cs(Cl1sCdH)_427
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7O2s)
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sO2s)
            L4: 3ring-Cs(Val7CsCd)-Cd(Val7Cd)_196
                L5: 3ring-Cs(Cl1sCsCd)-Cd(Cl1sCd)_446
                L5: 3ring-Cs(F1sCsCd)-Cd(F1sCd)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCl1sO2s)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7Val7Cs)_200
                L5: 3ring-Cs(Cl1sO2sCs)-Cs(Cl1sCl1sCs)_462
            L4: 3ring-Cs(Val7O2s)-Cs(Val7Val7O2s)
                L5: 3ring-Cs(Cl1sO2s)-Cs(Cl1sCl1sO2s)
            L4: 3ring-Cs(Val7O2sCs)-Cs(Val7O2sH)
                L5: 3ring-Cs(F1sO2sCs)-Cs(F1sO2sH)
            L4: 3ring-Cd(Val7Cd)-Cs(Val7O2sCd)_212
                L5: 3ring-Cd(F1sCd)-Cs(F1sO2sCd)
            L4: 3ring-Cs(Val7Val7Cs)-Cs(Val7CsCs)_213
                L5: 3ring-Cs(F1sF1sCs)-Cs(F1sCsCs)_622
        L3: halogen-4
            L4: 4ring-Cd(Val7Cd)-Cd(Val7Cd)
                L5: 4ring-Cd(Br1sCd)-Cd(Br1sCd)
                L5: 4ring-Cd(Cl1sCd)-Cd(Cl1sCd)
                L5: 4ring-Cd(F1sCd)-Cd(F1sCd)
            L4: 4ring-Cd(Val7Cd)=Cd(Val7Cd)
                L5: 4ring-Cd(Br1sCd)=Cd(Br1sCd)
                L5: 4ring-Cd(Cl1sCd)=Cd(Cl1sCd)
                L5: 4ring-Cd(F1sCd)=Cd(F1sCd)
            L4: 4ring-Cs(Val7CdH)-Cs(Val7CdH)
                L5: 4ring-Cs(Br1sCdH)-Cs(Br1sCdH)
                L5: 4ring-Cs(Cl1sCdH)-Cs(Cl1sCdH)
                L5: 4ring-Cs(F1sCdH)-Cs(F1sCdH)_627
            L4: 4ring-Cd(Val7Cs)=Cd(Val7Cs)
                L5: 4ring-Cd(Br1sCs)=Cd(Br1sCs)
                L5: 4ring-Cd(Cl1sCs)=Cd(Cl1sCs)_435
                L5: 4ring-Cd(F1sCs)=Cd(F1sCs)_580
            L4: 4ring-Cd(Val7Cd)-Cs(Val7CsH)
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sCsH)
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCsH)_433
                L5: 4ring-Cd(F1sCd)-Cs(F1sCsH)_582
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sBr1sCs)
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCl1sCs)
                L5: 4ring-Cd(F1sCd)-Cs(F1sF1sCs)_581
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)
                L5: 4ring-Cs(Br1sBr1sCd)-Cs(Br1sCdH)
                L5: 4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCdH)_479
                L5: 4ring-Cs(F1sF1sCd)-Cs(F1sCdH)
            L4: 4ring-Cs(Val7O2sH)-Cd(Val7Cd)
                L5: 4ring-Cs(Br1sO2sH)-Cd(Br1sCd)
                L5: 4ring-Cs(Cl1sO2sH)-Cd(Cl1sCd)
                L5: 4ring-Cs(F1sO2sH)-Cd(F1sCd)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7O2s)
                L5: 4ring-Cd(Br1sCs)=Cd(Br1sO2s)
                L5: 4ring-Cd(Cl1sCs)=Cd(Cl1sO2s)_445
                L5: 4ring-Cd(F1sCs)=Cd(F1sO2s)_555
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)
                L5: 4ring-Cs(Br1sCdH)-Cs(Br1sBr1sCd)
                L5: 4ring-Cs(F1sCdH)-Cs(F1sF1sCd)
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(Br1sBr1sO2s)-Cs(Br1sBr1sO2s)
                L5: 4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCl1sO2s)
                L5: 4ring-Cs(F1sF1sO2s)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sBr1sO2s)
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sO2s)
                L5: 4ring-Cs(F1sCsH)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7CsH)
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sCsH)
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)
                L5: 4ring-Cs(F1sCsH)-Cs(F1sCsH)_568
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)_467
                L5: 4ring-Cs(F1sCsH)-Cs(F1sF1sCs)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Cs)
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sCs)
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCs)
                L5: 4ring-Cs(F1sCsH)-Cs(F1sCs)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7CsH)_62
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sCsH)_243
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCsH)
                L5: 4ring-Cd(F1sCd)-Cs(F1sCsH)_626
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7O2s)
                L5: 4ring-Cs(Br1sBr1sO2s)-Cs(Br1sO2s)
                L5: 4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sO2s)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7O2sH)
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sH)
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sO2sH)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7O2sH)
                L5: 4ring-Cs(Br1sO2sH)-Cs(Br1sO2sH)
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sO2sH)
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sO2sH)
            L4: 4ring-Cs(Val7Cd)-Cs(Val7CdH)
                L5: 4ring-Cs(Br1sCd)-Cs(Br1sCdH)
                L5: 4ring-Cs(Cl1sCd)-Cs(Cl1sCdH)
                L5: 4ring-Cs(F1sCd)-Cs(F1sCdH)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7Cs)_84
                L5: 4ring-Cd(Br1sCs)=Cd(Br1sCs)_265
                L5: 4ring-Cd(Cl1sCs)=Cd(Cl1sCs)
                L5: 4ring-Cd(F1sCs)=Cd(F1sCs)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)_85
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sBr1sCs)_266
                L5: 4ring-Cd(F1sCd)-Cs(F1sF1sCs)_596
            L4: 4ring-Cs(Val7Cd)-Cs(Val7Val7Cd)
                L5: 4ring-Cs(Br1sCd)-Cs(Br1sBr1sCd)
                L5: 4ring-Cs(F1sCd)-Cs(F1sF1sCd)
            L4: 4ring-Cs(Val7O2s)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(Br1sO2s)-Cs(Br1sBr1sCs)
                L5: 4ring-Cs(F1sO2s)-Cs(F1sF1sCs)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7Cs)_96
                L5: 4ring-Cd(Br1sCs)=Cd(Br1sCs)_277
                L5: 4ring-Cd(Cl1sCs)=Cd(Cl1sCs)_461
                L5: 4ring-Cd(F1sCs)=Cd(F1sCs)_565
            L4: 4ring-Cs(Val7CsH)-Cd(Val7Cd)
                L5: 4ring-Cs(Br1sCsH)-Cd(Br1sCd)
                L5: 4ring-Cs(Cl1sCsH)-Cd(Cl1sCd)
                L5: 4ring-Cs(F1sCsH)-Cd(F1sCd)_652
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7O2s)
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sO2s)
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sO2s)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)
                L5: 4ring-Cs(Br1sBr1sCd)-Cs(Br1sBr1sCd)
                L5: 4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCl1sCd)
                L5: 4ring-Cs(F1sF1sCd)-Cs(F1sF1sCd)_646
            L4: 4ring-Cd(Val7O2s)=Cd(Val7Cs)
                L5: 4ring-Cd(Br1sO2s)=Cd(Br1sCs)
                L5: 4ring-Cd(Cl1sO2s)=Cd(Cl1sCs)
            L4: 4ring-Cs(Val7Val7O2s)-Cd(Val7Cd)
                L5: 4ring-Cs(Br1sBr1sO2s)-Cd(Br1sCd)
                L5: 4ring-Cs(F1sF1sO2s)-Cd(F1sCd)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7CsH)
                L5: 4ring-Cs(Br1sCs)-Cs(Br1sCsH)
                L5: 4ring-Cs(Cl1sCs)-Cs(Cl1sCsH)
                L5: 4ring-Cs(F1sCs)-Cs(F1sCsH)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(Br1sCs)-Cs(Br1sBr1sCs)
                L5: 4ring-Cs(Cl1sCs)-Cs(Cl1sCl1sCs)
                L5: 4ring-Cs(F1sCs)-Cs(F1sF1sCs)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Cs)
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sCs)
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCs)
                L5: 4ring-Cd(F1sCd)-Cs(F1sCs)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7O2sH)
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sO2sH)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)_577
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(Br1sO2sH)-Cs(Br1sBr1sCs)
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sCs)_396
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sF1sCs)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(Br1sO2sH)-Cs(Br1sBr1sO2s)
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sO2s)
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sO2s)
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sO2s)
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7O2sH)_119
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sO2sH)_300
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sO2sH)
                L5: 4ring-Cs(F1sCsH)-Cs(F1sO2sH)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)_491
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sCsH)
            L4: 4ring-Cs(Val7Cs)-Cd(Val7Cd)
                L5: 4ring-Cs(Br1sCs)-Cd(Br1sCd)
                L5: 4ring-Cs(Cl1sCs)-Cd(Cl1sCd)
                L5: 4ring-Cs(F1sCs)-Cd(F1sCd)
            L4: 4ring-Cs(Val7CsH)-Cd(Val7Cd)_124
                L5: 4ring-Cs(Br1sCsH)-Cd(Br1sCd)_305
                L5: 4ring-Cs(Cl1sCsH)-Cd(Cl1sCd)_440
                L5: 4ring-Cs(F1sCsH)-Cd(F1sCd)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7O2s)
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sO2s)
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sO2s)
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Cd)
                L5: 4ring-Cs(Br1sCdH)-Cs(Br1sCd)
                L5: 4ring-Cs(F1sCdH)-Cs(F1sCd)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Cs)
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sCs)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7O2sH)
                L5: 4ring-Cs(Br1sCs)-Cs(Br1sO2sH)
                L5: 4ring-Cs(Cl1sCs)-Cs(Cl1sO2sH)
                L5: 4ring-Cs(F1sCs)-Cs(F1sO2sH)
            L4: 4ring-Cs(Val7Cs)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(Br1sCs)-Cs(Br1sBr1sO2s)
                L5: 4ring-Cs(Cl1sCs)-Cs(Cl1sCl1sO2s)
                L5: 4ring-Cs(F1sCs)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7O2sH)_130
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sO2sH)_311
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_131
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sCs)_312
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)_423
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)_600
            L4: 4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)
                L5: 4ring-Cs(Br1sBr1sCs)-Cd(Br1sCd)
                L5: 4ring-Cs(Cl1sCl1sCs)-Cd(Cl1sCd)
                L5: 4ring-Cs(F1sF1sCs)-Cd(F1sCd)_552
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7O2s)_133
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sBr1sO2s)_314
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sF1sO2s)_635
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)_135
                L5: 4ring-Cs(Br1sCdH)-Cs(Br1sBr1sCd)_316
                L5: 4ring-Cs(F1sCdH)-Cs(F1sF1sCd)_650
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7O2s)
                L5: 4ring-Cs(Br1sO2sH)-Cs(Br1sO2s)
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sO2s)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7CsH)_142
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sCsH)_323
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCsH)_483
                L5: 4ring-Cd(F1sCd)-Cs(F1sCsH)
            L4: 4ring-Cs(Val7O2s)-Cs(Val7CsH)
                L5: 4ring-Cs(Br1sO2s)-Cs(Br1sCsH)
                L5: 4ring-Cs(F1sO2s)-Cs(F1sCsH)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_144
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)_325
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)
                L5: 4ring-Cs(F1sCsH)-Cs(F1sF1sCs)_620
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7O2s)_146
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sBr1sO2s)_327
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sO2s)_485
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_151
                L5: 4ring-Cs(Br1sBr1sCs)-Cs(Br1sCsH)_332
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sCsH)_559
            L4: 4ring-Cs(Val7CsH)-Cs(Val7CsH)_154
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sCsH)_335
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)_429
                L5: 4ring-Cs(F1sCsH)-Cs(F1sCsH)_619
            L4: 4ring-Cs(Val7CsH)-Cs(Val7Val7Cs)_155
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sBr1sCs)_336
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCl1sCs)_473
                L5: 4ring-Cs(F1sCsH)-Cs(F1sF1sCs)_616
            L4: 4ring-Cs(Val7O2s)-Cd(Val7Cd)
                L5: 4ring-Cs(Br1sO2s)-Cd(Br1sCd)
                L5: 4ring-Cs(F1sO2s)-Cd(F1sCd)
            L4: 4ring-Cd(Val7Cs)=Cd(Val7O2s)_160
                L5: 4ring-Cd(Br1sCs)=Cd(Br1sO2s)_341
                L5: 4ring-Cd(Cl1sCs)=Cd(Cl1sO2s)
                L5: 4ring-Cd(F1sCs)=Cd(F1sO2s)
            L4: 4ring-Cd(Val7O2s)=Cd(Val7Cs)_162
                L5: 4ring-Cd(Br1sO2s)=Cd(Br1sCs)_343
                L5: 4ring-Cd(Cl1sO2s)=Cd(Cl1sCs)_448
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7CsH)
                L5: 4ring-Cs(Br1sO2sH)-Cs(Br1sCsH)
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sCsH)_477
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sCsH)_643
            L4: 4ring-Cs(Val7CdH)-Cs(Val7CdH)_167
                L5: 4ring-Cs(Br1sCdH)-Cs(Br1sCdH)_348
                L5: 4ring-Cs(Cl1sCdH)-Cs(Cl1sCdH)_490
                L5: 4ring-Cs(F1sCdH)-Cs(F1sCdH)
            L4: 4ring-Cs(Val7Val7O2s)-Cd(Val7Cd)_168
                L5: 4ring-Cs(Br1sBr1sO2s)-Cd(Br1sCd)_349
                L5: 4ring-Cs(F1sF1sO2s)-Cd(F1sCd)_641
            L4: 4ring-Cd(Val7O2s)=Cd(Val7O2s)
                L5: 4ring-Cd(Br1sO2s)=Cd(Br1sO2s)
                L5: 4ring-Cd(Cl1sO2s)=Cd(Cl1sO2s)
                L5: 4ring-Cd(F1sO2s)=Cd(F1sO2s)
            L4: 4ring-Cs(Val7CsH)-Cs(Val7CsH)_173
                L5: 4ring-Cs(Br1sCsH)-Cs(Br1sCsH)_354
                L5: 4ring-Cs(Cl1sCsH)-Cs(Cl1sCsH)_422
                L5: 4ring-Cs(F1sCsH)-Cs(F1sCsH)
            L4: 4ring-Cd(Val7Cd)-Cd(Val7Cd)_175
                L5: 4ring-Cd(Br1sCd)-Cd(Br1sCd)_356
                L5: 4ring-Cd(Cl1sCd)-Cd(Cl1sCd)_487
            L4: 4ring-Cd(Val7Cd)=Cd(Val7Cd)_176
                L5: 4ring-Cd(Br1sCd)=Cd(Br1sCd)_357
                L5: 4ring-Cd(Cl1sCd)=Cd(Cl1sCd)_488
            L4: 4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)_177
                L5: 4ring-Cs(Br1sBr1sCs)-Cd(Br1sCd)_358
                L5: 4ring-Cs(Cl1sCl1sCs)-Cd(Cl1sCd)_460
                L5: 4ring-Cs(F1sF1sCs)-Cd(F1sCd)
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7CsH)
                L5: 4ring-Cs(Br1sBr1sO2s)-Cs(Br1sCsH)
                L5: 4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCsH)_436
                L5: 4ring-Cs(F1sF1sO2s)-Cs(F1sCsH)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7Cs)_181
                L5: 4ring-Cd(Br1sCd)-Cs(Br1sBr1sCs)_362
                L5: 4ring-Cd(F1sCd)-Cs(F1sF1sCs)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Cs)
                L5: 4ring-Cs(Br1sO2sH)-Cs(Br1sCs)
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sCs)
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sCs)
            L4: 4ring-Cs(Val7O2sH)-Cd(Val7Cd)_183
                L5: 4ring-Cs(Br1sO2sH)-Cd(Br1sCd)_364
                L5: 4ring-Cs(Cl1sO2sH)-Cd(Cl1sCd)_500
                L5: 4ring-Cs(F1sO2sH)-Cd(F1sCd)_649
            L4: 4ring-Cd(Val7Cd)-Cs(Val7O2s)
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sO2s)
                L5: 4ring-Cd(F1sCd)-Cs(F1sO2s)
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7Val7Cs)_185
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sCl1sCs)
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sF1sCs)_644
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7Val7Cs)_187
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCl1sCs)
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sF1sCs)
            L4: 4ring-Cs(Val7CdH)-Cs(Val7Val7Cd)_188
                L5: 4ring-Cs(Cl1sCdH)-Cs(Cl1sCl1sCd)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)_190
                L5: 4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCdH)
                L5: 4ring-Cs(F1sF1sCd)-Cs(F1sCdH)_606
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7CsH)_191
                L5: 4ring-Cs(Cl1sCl1sO2s)-Cs(Cl1sCsH)
                L5: 4ring-Cs(F1sF1sO2s)-Cs(F1sCsH)_636
            L4: 4ring-Cs(Val7Val7Cs)-Cs(Val7CsH)_193
                L5: 4ring-Cs(Cl1sCl1sCs)-Cs(Cl1sCsH)_428
                L5: 4ring-Cs(F1sF1sCs)-Cs(F1sCsH)_579
            L4: 4ring-Cs(Val7O2sH)-Cs(Val7CsH)_194
                L5: 4ring-Cs(Cl1sO2sH)-Cs(Cl1sCsH)
                L5: 4ring-Cs(F1sO2sH)-Cs(F1sCsH)
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7O2s)
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCl1sO2s)
                L5: 4ring-Cd(F1sCd)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Cd)
                L5: 4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCd)
            L4: 4ring-Cs(Val7CsH)-Cd(Val7Cd)_201
                L5: 4ring-Cs(Cl1sCsH)-Cd(Cl1sCd)_472
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)_202
                L5: 4ring-Cs(Cl1sCl1sCd)-Cs(Cl1sCl1sCd)_475
            L4: 4ring-Cs(Val7O2s)-Cs(Val7O2sH)
                L5: 4ring-Cs(Cl1sO2s)-Cs(Cl1sO2sH)
            L4: 4ring-Cs(Val7Val7Cs)-Cd(Val7Cd)_204
                L5: 4ring-Cs(Cl1sCl1sCs)-Cd(Cl1sCd)_495
            L4: 4ring-Cd(Val7Cd)-Cs(Val7Val7O2s)_206
                L5: 4ring-Cd(Cl1sCd)-Cs(Cl1sCl1sO2s)_499
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7Cs)
                L5: 4ring-Cs(F1sF1sO2s)-Cs(F1sCs)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7Val7Cd)_208
                L5: 4ring-Cs(F1sF1sCd)-Cs(F1sF1sCd)
            L4: 4ring-Cs(Val7O2s)-Cs(Val7Val7O2s)
                L5: 4ring-Cs(F1sO2s)-Cs(F1sF1sO2s)
            L4: 4ring-Cs(Val7Val7O2s)-Cs(Val7Val7Cs)
                L5: 4ring-Cs(F1sF1sO2s)-Cs(F1sF1sCs)
            L4: 4ring-Cs(Val7Val7Cd)-Cs(Val7CdH)_214
                L5: 4ring-Cs(F1sF1sCd)-Cs(F1sCdH)_632
            L4: 4ring-Cd(Val7Cd)=Cd(Val7Cd)_215
                L5: 4ring-Cd(F1sCd)=Cd(F1sCd)_638
            L4: 4ring-Cd(Val7Cd)-Cd(Val7Cd)_216
                L5: 4ring-Cd(F1sCd)-Cd(F1sCd)_639
"""
)

