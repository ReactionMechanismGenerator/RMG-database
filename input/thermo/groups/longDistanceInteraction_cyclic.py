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
1 *1 C    ux {2,[S,D]} {3,S}
2 *2 C    ux {1,[S,D]}
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
1 *1 Cs          ux {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          ux {1,S} {4,S} {6,S} {8,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
6    Val7        u0 {2,S}
7    [C,H,N,O,S] ux {1,S}
8    [C,H,N,O,S] ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.041475,-0.131714,-0.161302,-0.191793,-0.233629,-0.208333,0.00619743],'cal/(mol*K)','+|-',[0.105625,0.117244,0.113822,0.10943,0.0988174,0.0839162,0.0595212]),
        H298 = (2.8807,'kcal/mol','+|-',2.52118),
        S298 = (0.427255,'cal/(mol*K)','+|-',0.175449),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "Cs(Cl)2-Cs(Cl)2",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          ux {1,S} {4,S} {6,S} {8,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
6    Cl1s        u0 {2,S}
7    [C,H,N,O,S] ux {1,S}
8    [C,H,N,O,S] ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0604356,-0.196952,-0.246734,-0.244787,-0.248332,-0.21854,-0.0162777],'cal/(mol*K)','+|-',[0.105625,0.117244,0.113822,0.10943,0.0988174,0.0839162,0.0595212]),
        H298 = (2.78784,'kcal/mol','+|-',0.617032),
        S298 = (0.391358,'cal/(mol*K)','+|-',0.326017),
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
    index = 80,
    label = "Cs(F)2-Cs(F)2",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          ux {1,S} {4,S} {6,S} {8,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
6    F1s         u0 {2,S}
7    [C,H,N,O,S] ux {1,S}
8    [C,H,N,O,S] ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16045,-0.142085,-0.0922643,-0.0996005,-0.131505,-0.0926992,0.189776],'cal/(mol*K)','+|-',[0.107184,0.118975,0.115502,0.111045,0.100276,0.0851549,0.0603998]),
        H298 = (4.18515,'kcal/mol','+|-',0.62614),
        S298 = (0.363172,'cal/(mol*K)','+|-',0.330829),
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
    index = 81,
    label = "Cs(Br)2-Cs(Br)2",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S} {7,S}
2 *2 Cs          ux {1,S} {4,S} {6,S} {8,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
6    Br1s        u0 {2,S}
7    [C,H,N,O,S] ux {1,S}
8    [C,H,N,O,S] ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0964607,-0.0561054,-0.144907,-0.230992,-0.321051,-0.313759,-0.154906],'cal/(mol*K)','+|-',[0.103413,0.114789,0.111439,0.107139,0.0967485,0.0821593,0.058275]),
        H298 = (1.66911,'kcal/mol','+|-',0.604114),
        S298 = (0.527235,'cal/(mol*K)','+|-',0.319191),
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
    index = 82,
    label = "3ring-Cs(Val7)2-Cs(Val7)2",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S] ux {1,S} {2,S}
4    Val7        u0 {1,S}
5    Val7        u0 {2,S}
6    Val7        u0 {1,S}
7    Val7        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.213165,-0.379222,-0.37313,-0.377491,-0.39731,-0.344927,-0.0466521],'cal/(mol*K)','+|-',[0.0971216,0.107805,0.104659,0.10062,0.0908622,0.0771606,0.0547295]),
        H298 = (5.3081,'kcal/mol','+|-',4.67574),
        S298 = (0.662505,'cal/(mol*K)','+|-',0.67801),
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
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S] ux {1,S} {2,S}
4    Cl1s        u0 {1,S}
5    Cl1s        u0 {2,S}
6    Cl1s        u0 {1,S}
7    Cl1s        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.270952,-0.470596,-0.447481,-0.440043,-0.460947,-0.394694,-0.0153192],'cal/(mol*K)','+|-',[0.0971216,0.107805,0.104659,0.10062,0.0908622,0.0771606,0.0547295]),
        H298 = (4.10854,'kcal/mol','+|-',0.567358),
        S298 = (0.48576,'cal/(mol*K)','+|-',0.299771),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         10
""",
)

entry(
    index = 84,
    label = "3ring-Cs(F)2-Cs(F)2",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S] ux {1,S} {2,S}
4    F1s         u0 {1,S}
5    F1s         u0 {2,S}
6    F1s         u0 {1,S}
7    F1s         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.179391,-0.284923,-0.255856,-0.212267,-0.168419,-0.100064,0.150286],'cal/(mol*K)','+|-',[0.0654137,0.0726095,0.0704899,0.0677702,0.0611978,0.0519694,0.0368616]),
        H298 = (8.00226,'kcal/mol','+|-',0.382129),
        S298 = (0.448396,'cal/(mol*K)','+|-',0.201903),
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
    index = 85,
    label = "3ring-Cs(Br)2-Cs(Br)2",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S} {7,S}
3    [C,N,O,S] ux {1,S} {2,S}
4    Br1s        u0 {1,S}
5    Br1s        u0 {2,S}
6    Br1s        u0 {1,S}
7    Br1s        u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.189152,-0.382148,-0.416053,-0.480162,-0.562563,-0.540023,-0.274923],'cal/(mol*K)','+|-',[0.117897,0.130866,0.127046,0.122144,0.110299,0.093666,0.0664367]),
        H298 = (3.8135,'kcal/mol','+|-',0.688722),
        S298 = (1.05336,'cal/(mol*K)','+|-',0.363895),
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
    index = 86,
    label = "Cs(Val7)2-C(Val7)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S}
2 *2 [Cs,Cd]     ux {1,S} {5,S}
3    Val7        u0 {1,S}
4    Val7        u0 {1,S}
5    Val7        u0 {2,S}
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
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 [Cs,Cd]     ux {1,S} {3,[S,D]} {6,S}
3    [C,N,O,S] ux {1,S} {2,[S,D]}
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
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S}
3    [C,N,O,S]   ux {1,S} {2,S}
4    Val7        u0 {1,S}
5    Val7        u0 {2,S}
6    Val7        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.284985,-0.439344,-0.429026,-0.424502,-0.418023,-0.360429,-0.106761],'cal/(mol*K)','+|-',[0.0936327,0.103933,0.100899,0.0970058,0.0875981,0.0743887,0.0527634]),
        H298 = (4.43802,'kcal/mol','+|-',2.5597),
        S298 = (0.97775,'cal/(mol*K)','+|-',1.16591),
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
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S}
3    [C,N,O,S]   ux {1,S} {2,S}
4    Cl1s        u0 {1,S}
5    Cl1s        u0 {2,S}
6    Cl1s        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.296851,-0.467241,-0.467526,-0.467845,-0.463482,-0.385287,-0.067649],'cal/(mol*K)','+|-',[0.0936327,0.103933,0.100899,0.0970058,0.0875981,0.0743887,0.0527634]),
        H298 = (3.9882,'kcal/mol','+|-',0.546977),
        S298 = (0.779937,'cal/(mol*K)','+|-',0.289002),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         23
""",
)

entry(
    index = 90,
    label = "3ring-Cs(F)2-Cs(F)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S}
3    [C,N,O,S]   ux {1,S} {2,S}
4    F1s         u0 {1,S}
5    F1s         u0 {2,S}
6    F1s         u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.166035,-0.279829,-0.273319,-0.233777,-0.179284,-0.137178,0.0500421],'cal/(mol*K)','+|-',[0.107195,0.118987,0.115514,0.111057,0.100286,0.0851636,0.060406]),
        H298 = (5.88205,'kcal/mol','+|-',0.626204),
        S298 = (0.519444,'cal/(mol*K)','+|-',0.330863),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         25
""",
)

entry(
    index = 91,
    label = "3ring-Cs(Br)2-Cs(Br)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {6,S}
2 *2 Cs          ux {1,S} {3,S} {5,S}
3    [C,N,O,S]   ux {1,S} {2,S}
4    Br1s        u0 {1,S}
5    Br1s        u0 {2,S}
6    Br1s        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.392068,-0.570962,-0.546233,-0.571883,-0.611303,-0.558821,-0.302676],'cal/(mol*K)','+|-',[0.127879,0.141946,0.137803,0.132486,0.119637,0.101597,0.0720617]),
        H298 = (3.4438,'kcal/mol','+|-',0.747035),
        S298 = (1.63387,'cal/(mol*K)','+|-',0.394706),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         18
""",
)

entry(
    index = 92,
    label = "3ring-Cs(Val7)2-Cds(Val7)",
    group = 
"""
1 *1 Cs        ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        ux {1,S} {3,D} {6,S}
3    [C,N,O,S] ux {1,S} {2,D}
4    Val7      u0 {1,S}
5    Val7      u0 {1,S}
6    Val7      u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.318418,-0.354565,-0.35186,-0.317813,-0.256506,-0.202419,-0.0598305],'cal/(mol*K)','+|-',[0.193322,0.214589,0.208325,0.200287,0.180863,0.153589,0.10894]),
        H298 = (3.76982,'kcal/mol','+|-',6.19868),
        S298 = (0.951725,'cal/(mol*K)','+|-',0.180036),
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
1 *1 Cs        ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        ux {1,S} {3,D} {6,S}
3    [C,N,O,S] ux {1,S} {2,D}
4    Cl1s      u0 {1,S}
5    Cl1s      u0 {1,S}
6    Cl1s      u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.234914,-0.236318,-0.232562,-0.248852,-0.274493,-0.245606,-0.0370014],'cal/(mol*K)','+|-',[0.193322,0.214589,0.208325,0.200287,0.180863,0.153589,0.10894]),
        H298 = (1.53412,'kcal/mol','+|-',1.12934),
        S298 = (0.961768,'cal/(mol*K)','+|-',0.5967),
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
    index = 94,
    label = "3ring-Cs(F)2-Cds(F)",
    group = 
"""
1 *1 Cs        ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        ux {1,S} {3,D} {6,S}
3    [C,N,O,S] ux {1,S} {2,D}
4    F1s       u0 {1,S}
5    F1s       u0 {1,S}
6    F1s       u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.386038,-0.357432,-0.402926,-0.366802,-0.233396,-0.146126,0.014982],'cal/(mol*K)','+|-',[0.22835,0.25347,0.246071,0.236576,0.213633,0.181418,0.128679]),
        H298 = (7.30782,'kcal/mol','+|-',1.33396),
        S298 = (0.857106,'cal/(mol*K)','+|-',0.704816),
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
    index = 95,
    label = "3ring-Cs(Br)2-Cds(Br)",
    group = 
"""
1 *1 Cs        ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd        ux {1,S} {3,D} {6,S}
3    [C,N,O,S] ux {1,S} {2,D}
4    Br1s      u0 {1,S}
5    Br1s      u0 {1,S}
6    Br1s      u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.334302,-0.469946,-0.420092,-0.337786,-0.26163,-0.215526,-0.157472],'cal/(mol*K)','+|-',[0.228912,0.254094,0.246677,0.237159,0.214159,0.181865,0.128996]),
        H298 = (2.46751,'kcal/mol','+|-',1.33725),
        S298 = (1.0363,'cal/(mol*K)','+|-',0.706551),
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
    index = 96,
    label = "Cs(Val7)2-Cs(Val7)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S}
2 *2 Cs          ux {1,S} {4,S}
3    Val7        u0 {1,S}
4    Val7        u0 {2,S}
5    Val7        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.100336,-0.168263,-0.178979,-0.2172,-0.25244,-0.20973,-0.0310533],'cal/(mol*K)','+|-',[0.11871,0.131768,0.127922,0.122986,0.111059,0.0943118,0.0668948]),
        H298 = (1.51215,'kcal/mol','+|-',2.1556),
        S298 = (0.610029,'cal/(mol*K)','+|-',0.631676),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "Cs(Cl)2-Cs(Cl)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S}
2 *2 Cs          ux {1,S} {4,S}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {2,S}
5    Cl1s        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.125446,-0.158463,-0.169349,-0.228102,-0.274736,-0.233989,-0.0243899],'cal/(mol*K)','+|-',[0.11871,0.131768,0.127922,0.122986,0.111059,0.0943118,0.0668948]),
        H298 = (1.45716,'kcal/mol','+|-',0.693471),
        S298 = (0.422834,'cal/(mol*K)','+|-',0.366404),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         15
""",
)

entry(
    index = 98,
    label = "Cs(F)2-Cs(F)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S}
2 *2 Cs          ux {1,S} {4,S}
3    F1s         u0 {1,S}
4    F1s         u0 {2,S}
5    F1s         u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.13951,-0.110261,-0.0704955,-0.0931502,-0.144017,-0.0940878,0.129969],'cal/(mol*K)','+|-',[0.119184,0.132295,0.128433,0.123478,0.111503,0.0946889,0.0671622]),
        H298 = (2.61639,'kcal/mol','+|-',0.696243),
        S298 = (0.432569,'cal/(mol*K)','+|-',0.367869),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         16
""",
)

entry(
    index = 99,
    label = "Cs(Br)2-Cs(Br)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {5,S}
2 *2 Cs          ux {1,S} {4,S}
3    Br1s        u0 {1,S}
4    Br1s        u0 {2,S}
5    Br1s        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0360528,-0.236064,-0.297091,-0.330348,-0.338568,-0.301112,-0.198739],'cal/(mol*K)','+|-',[0.11516,0.127828,0.124097,0.119308,0.107738,0.0914914,0.0648943]),
        H298 = (0.462898,'kcal/mol','+|-',0.672733),
        S298 = (0.974684,'cal/(mol*K)','+|-',0.355447),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         15
""",
)

entry(
    index = 100,
    label = "Cs(Val7)2-Cds(Val7)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          ux {1,S} {6,S} {7,D}
3    Val7        u0 {1,S}
4    Val7        u0 {1,S}
5    [C,H,N,O,S] ux {1,S}
6    Val7        u0 {2,S}
7    [C,N,O,S]   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0235263,0.045163,0.0148047,0.00409321,-0.0350716,-0.049263,0.0328782],'cal/(mol*K)','+|-',[0.24811,0.275404,0.267364,0.257048,0.23212,0.197117,0.139814]),
        H298 = (0.653313,'kcal/mol','+|-',4.29337),
        S298 = (0.280982,'cal/(mol*K)','+|-',0.852722),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "Cs(Cl)2-Cds(Cl)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          ux {1,S} {6,S} {7,D}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {1,S}
5    [C,H,N,O,S] ux {1,S}
6    Cl1s        u0 {2,S}
7    [C,N,O,S]   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.110683,-0.0112073,0.0296284,0.000343126,-0.111712,-0.125798,0.188943],'cal/(mol*K)','+|-',[0.24811,0.275404,0.267364,0.257048,0.23212,0.197117,0.139814]),
        H298 = (-0.571293,'kcal/mol','+|-',1.44939),
        S298 = (0.687245,'cal/(mol*K)','+|-',0.765806),
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
    index = 102,
    label = "Cs(F)2-Cds(F)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          ux {1,S} {6,S} {7,D}
3    F1s         u0 {1,S}
4    F1s         u0 {1,S}
5    [C,H,N,O,S] ux {1,S}
6    F1s         u0 {2,S}
7    [C,N,O,S]   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.127556,0.0123544,-0.0618796,-0.0881295,-0.0534642,0.0141777,0.0949325],'cal/(mol*K)','+|-',[0.270538,0.300299,0.291533,0.280284,0.253102,0.214936,0.152452]),
        H298 = (3.13203,'kcal/mol','+|-',1.58041),
        S298 = (0.318676,'cal/(mol*K)','+|-',0.835031),
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
    index = 103,
    label = "Cs(Br)2-Cds(Br)",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 Cd          ux {1,S} {6,S} {7,D}
3    Br1s        u0 {1,S}
4    Br1s        u0 {1,S}
5    [C,H,N,O,S] ux {1,S}
6    Br1s        u0 {2,S}
7    [C,N,O,S]   ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.308818,0.134342,0.0766654,0.100066,0.0599615,-0.0361687,-0.185241],'cal/(mol*K)','+|-',[0.261578,0.290353,0.281878,0.271002,0.24472,0.207817,0.147403]),
        H298 = (-0.600798,'kcal/mol','+|-',1.52807),
        S298 = (-0.162974,'cal/(mol*K)','+|-',0.807376),
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
    index = 104,
    label = "Cs(Val7)-Cs(Val7)",
    group = 
"""
1 *1 Cs   ux {2,S} {3,S}
2 *2 Cs   ux {1,S} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.210782,-0.254467,-0.234539,-0.221601,-0.225229,-0.190617,-0.00518765],'cal/(mol*K)','+|-',[0.0288784,0.0320552,0.0311195,0.0299188,0.0270172,0.0229431,0.0162734]),
        H298 = (2.03579,'kcal/mol','+|-',1.64795),
        S298 = (1.02642,'cal/(mol*K)','+|-',0.0413935),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "Cs(Cl)-Cs(Cl)",
    group = 
"""
1 *1 Cs   ux {2,S} {3,S}
2 *2 Cs   ux {1,S} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.187014,-0.237138,-0.216954,-0.205376,-0.226112,-0.202471,-0.00984336],'cal/(mol*K)','+|-',[0.0288784,0.0320552,0.0311195,0.0299188,0.0270172,0.0229431,0.0162734]),
        H298 = (1.76714,'kcal/mol','+|-',0.1687),
        S298 = (1.04433,'cal/(mol*K)','+|-',0.0891348),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         71
""",
)

entry(
    index = 106,
    label = "Cs(F)-Cs(F)",
    group = 
"""
1 *1 Cs  ux {2,S} {3,S}
2 *2 Cs  ux {1,S} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.15534,-0.165218,-0.132093,-0.109874,-0.112332,-0.0873999,0.0798339],'cal/(mol*K)','+|-',[0.0307386,0.03412,0.033124,0.031846,0.0287575,0.024421,0.0173217]),
        H298 = (2.96056,'kcal/mol','+|-',0.179567),
        S298 = (1.03116,'cal/(mol*K)','+|-',0.0948765),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         75
""",
)

entry(
    index = 107,
    label = "Cs(Br)-Cs(Br)",
    group = 
"""
1 *1 Cs   ux {2,S} {3,S}
2 *2 Cs   ux {1,S} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.289993,-0.361046,-0.35457,-0.349553,-0.337243,-0.281979,-0.0855535],'cal/(mol*K)','+|-',[0.0317925,0.0352898,0.0342597,0.0329378,0.0297435,0.0252583,0.0179156]),
        H298 = (1.37967,'kcal/mol','+|-',0.185723),
        S298 = (1.00376,'cal/(mol*K)','+|-',0.0981293),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         66
""",
)

entry(
    index = 108,
    label = "Cs(Val7)-Cds(Val7)",
    group = 
"""
1 *1 Cs   ux {2,S} {3,S}
2 *2 Cd   ux {1,S} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.377829,-0.31936,-0.228499,-0.189183,-0.200691,-0.161847,0.0403436],'cal/(mol*K)','+|-',[0.105579,0.117193,0.113772,0.109382,0.0987742,0.0838795,0.0594952]),
        H298 = (2.43666,'kcal/mol','+|-',2.03251),
        S298 = (1.5755,'cal/(mol*K)','+|-',0.785398),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "Cs(Cl)-Cds(Cl)",
    group = 
"""
1 *1 Cs ux {2,S} {3,S}
2 *2 Cd ux {1,S} {4,S}
3    Cl u0 {1,S}
4    Cl u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.36921,-0.293557,-0.186585,-0.158911,-0.216433,-0.181459,0.111175],'cal/(mol*K)','+|-',[0.105579,0.117193,0.113772,0.109382,0.0987742,0.0838795,0.0594952]),
        H298 = (1.46703,'kcal/mol','+|-',0.616762),
        S298 = (1.89004,'cal/(mol*K)','+|-',0.325874),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         21
""",
)

entry(
    index = 110,
    label = "Cs(F)-Cds(F)",
    group = 
"""
1 *1 Cs ux {2,S} {3,S}
2 *2 Cd ux {1,S} {4,S}
3    F  u0 {1,S}
4    F  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.590067,-0.436507,-0.305133,-0.250341,-0.183823,-0.124454,0.0433442],'cal/(mol*K)','+|-',[0.121962,0.135379,0.131427,0.126356,0.114102,0.0968957,0.0687275]),
        H298 = (3.49387,'kcal/mol','+|-',0.71247),
        S298 = (1.7011,'cal/(mol*K)','+|-',0.376443),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         22
""",
)

entry(
    index = 111,
    label = "Cs(Br)-Cds(Br)",
    group = 
"""
1 *1 Cs ux {2,S} {3,S}
2 *2 Cd ux {1,S} {4,S}
3    Br u0 {1,S}
4    Br u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.174211,-0.228016,-0.19378,-0.158296,-0.201817,-0.179628,-0.0334884],'cal/(mol*K)','+|-',[0.11858,0.131624,0.127782,0.122852,0.110937,0.0942086,0.0668215]),
        H298 = (2.34909,'kcal/mol','+|-',0.692712),
        S298 = (1.13537,'cal/(mol*K)','+|-',0.366003),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         19
""",
)

entry(
    index = 112,
    label = "Cds(Val7)-Cds(Val7)",
    group = 
"""
1 *1 Cd   ux {2,S} {3,S}
2 *2 Cd   ux {1,S} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0521848,0.0434248,0.0985422,0.0648942,-0.0411751,-0.0853693,0.0452771],'cal/(mol*K)','+|-',[0.135046,0.149902,0.145526,0.139911,0.126343,0.107291,0.0761006]),
        H298 = (-0.304357,'kcal/mol','+|-',3.35421),
        S298 = (0.014271,'cal/(mol*K)','+|-',0.628843),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "Cds(Cl)-Cds(Cl)",
    group = 
"""
1 *1 Cd   ux {2,S} {3,S}
2 *2 Cd   ux {1,S} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0444945,0.0209223,0.0828467,0.0447868,-0.0648154,-0.11066,0.0259138],'cal/(mol*K)','+|-',[0.135046,0.149902,0.145526,0.139911,0.126343,0.107291,0.0761006]),
        H298 = (-1.23802,'kcal/mol','+|-',0.788904),
        S298 = (0.115151,'cal/(mol*K)','+|-',0.416828),
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
    index = 114,
    label = "Cds(F)-Cds(F)",
    group = 
"""
1 *1 Cd  ux {2,S} {3,S}
2 *2 Cd  ux {1,S} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.116609,0.0519914,0.036115,-0.0184311,-0.131531,-0.167828,-0.0117954],'cal/(mol*K)','+|-',[0.20821,0.231115,0.224368,0.215711,0.194791,0.165418,0.11733]),
        H298 = (1.63179,'kcal/mol','+|-',1.21631),
        S298 = (0.265871,'cal/(mol*K)','+|-',0.642653),
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
    index = 115,
    label = "Cds(Br)-Cds(Br)",
    group = 
"""
1 *1 Cd   ux {2,S} {3,S}
2 *2 Cd   ux {1,S} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.00454919,0.0573606,0.176665,0.168327,0.0728212,0.0223801,0.121713],'cal/(mol*K)','+|-',[0.134204,0.148967,0.144619,0.139039,0.125555,0.106622,0.0756262]),
        H298 = (-1.30684,'kcal/mol','+|-',0.783986),
        S298 = (-0.338209,'cal/(mol*K)','+|-',0.414229),
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
    index = 116,
    label = "Cds(Val7)=Cds(Val7)",
    group = 
"""
1 *1 Cd   ux {2,D} {3,S}
2 *2 Cd   ux {1,D} {4,S}
3    Val7 u0 {1,S}
4    Val7 u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0464406,-0.0933087,-0.0882718,-0.0746957,-0.0828051,-0.0776049,0.00935976],'cal/(mol*K)','+|-',[0.0739822,0.0821206,0.0797234,0.0766474,0.0692141,0.0587769,0.0416901]),
        H298 = (2.43656,'kcal/mol','+|-',4.86423),
        S298 = (0.175868,'cal/(mol*K)','+|-',0.259889),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "Cds(Cl)=Cds(Cl)",
    group = 
"""
1 *1 Cd   ux {2,D} {3,S}
2 *2 Cd   ux {1,D} {4,S}
3    Cl1s u0 {1,S}
4    Cl1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0310293,-0.0551521,-0.0349506,-0.0327209,-0.0675794,-0.0671067,0.0391955],'cal/(mol*K)','+|-',[0.0739822,0.0821206,0.0797234,0.0766474,0.0692141,0.0587769,0.0416901]),
        H298 = (1.45634,'kcal/mol','+|-',0.432184),
        S298 = (0.260454,'cal/(mol*K)','+|-',0.22835),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOCl_G4 |         27
""",
)

entry(
    index = 118,
    label = "Cds(F)=Cds(F)",
    group = 
"""
1 *1 Cd  ux {2,D} {3,S}
2 *2 Cd  ux {1,D} {4,S}
3    F1s u0 {1,S}
4    F1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0298238,-0.114143,-0.137328,-0.112467,-0.105966,-0.0974533,0.00575039],'cal/(mol*K)','+|-',[0.0714422,0.0793011,0.0769863,0.0740158,0.0668377,0.0567589,0.0402587]),
        H298 = (5.20583,'kcal/mol','+|-',0.417346),
        S298 = (0.0262459,'cal/(mol*K)','+|-',0.22051),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library | Number of Species
CHOF_G4 |         25
""",
)

entry(
    index = 119,
    label = "Cds(Br)=Cds(Br)",
    group = 
"""
1 *1 Cd   ux {2,D} {3,S}
2 *2 Cd   ux {1,D} {4,S}
3    Br1s u0 {1,S}
4    Br1s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0784687,-0.110631,-0.0925369,-0.0788993,-0.07487,-0.0682546,-0.0168666],'cal/(mol*K)','+|-',[0.0707868,0.0785737,0.0762801,0.0733369,0.0662246,0.0562383,0.0398894]),
        H298 = (0.64752,'kcal/mol','+|-',0.413517),
        S298 = (0.240903,'cal/(mol*K)','+|-',0.218487),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         25
""",
)

entry(
    index = 120,
    label = "Cd(Val7)-CO",
    group = 
"""
1 *1 Cd   ux {2,S} {3,S}
2 *2 CO   ux {1,S} {4,D}
3    Val7 u0 {1,S}
4    O2d  ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.204607,-0.647876,-0.689153,-0.708696,-0.720393,-0.62961,-0.137257],'cal/(mol*K)','+|-',[0.659715,0.732287,0.710911,0.683481,0.617197,0.524127,0.371759]),
        H298 = (-0.900295,'kcal/mol','+|-',1.42164),
        S298 = (1.68793,'cal/(mol*K)','+|-',1.31358),
    ),
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
1 *1 Cd  ux {2,S} {3,S}
2 *2 CO  ux {1,S} {4,D}
3    F1s u0 {1,S}
4    O2d ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.0711591,-0.586483,-0.793018,-0.8899,-0.885747,-0.744585,-0.233672],'cal/(mol*K)','+|-',[0.659715,0.732287,0.710911,0.683481,0.617197,0.524127,0.371759]),
        H298 = (-1.7178,'kcal/mol','+|-',3.85388),
        S298 = (2.32778,'cal/(mol*K)','+|-',2.03625),
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
    index = 122,
    label = "Cd(Cl)-CO",
    group = 
"""
1 *1 Cd   ux {2,S} {3,S}
2 *2 CO   ux {1,S} {4,D}
3    Cl1s u0 {1,S}
4    O2d  ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.177336,-0.71766,-0.8306,-0.828413,-0.749411,-0.624048,-0.205877],'cal/(mol*K)','+|-',[0.660834,0.733529,0.712117,0.684641,0.618244,0.525015,0.37239]),
        H298 = (-0.555017,'kcal/mol','+|-',3.86042),
        S298 = (1.72059,'cal/(mol*K)','+|-',2.0397),
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
    index = 123,
    label = "Cd(Br)-CO",
    group = 
"""
1 *1 Cd   ux {2,S} {3,S}
2 *2 CO   ux {1,S} {4,D}
3    Br1s u0 {1,S}
4    O2d  ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.365325,-0.639484,-0.44384,-0.407774,-0.526022,-0.520197,0.0277766],'cal/(mol*K)','+|-',[0.659433,0.731974,0.710607,0.683189,0.616933,0.523902,0.3716]),
        H298 = (-0.428067,'kcal/mol','+|-',3.85223),
        S298 = (1.01542,'cal/(mol*K)','+|-',2.03538),
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
    index = 124,
    label = "Cs(Val7)3-CO",
    group = 
"""
1 *1 Cs   ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO   ux {1,S} {6,D}
3    Val7 u0 {1,S}
4    Val7 u0 {1,S}
5    Val7 u0 {1,S}
6    O2d  ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "Cs(F)3-CO",
    group = 
"""
1 *1 Cs  ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO  ux {1,S} {6,D}
3    F1s u0 {1,S}
4    F1s u0 {1,S}
5    F1s u0 {1,S}
6    O2d ux {2,D}
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
1 *1 Cs   ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO   ux {1,S} {6,D}
3    Cl1s u0 {1,S}
4    Cl1s u0 {1,S}
5    Cl1s u0 {1,S}
6    O2d  ux {2,D}
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
1 *1 Cs   ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO   ux {1,S} {6,D}
3    Br1s u0 {1,S}
4    Br1s u0 {1,S}
5    Br1s u0 {1,S}
6    O2d  ux {2,D}
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
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    Val7        u0 {1,S}
4    Val7        u0 {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.926811,0.267797,0.015232,-0.0998764,-0.180617,-0.218985,0.110552],'cal/(mol*K)','+|-',[0.616252,0.684043,0.664075,0.638453,0.576535,0.489596,0.347267]),
        H298 = (3.81506,'kcal/mol','+|-',6.56653),
        S298 = (1.5235,'cal/(mol*K)','+|-',1.20033),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "Cs(F)2-CO",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    F1s         u0 {1,S}
4    F1s         u0 {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.03319,0.295091,0.126585,0.00898979,-0.283139,-0.413817,0.0988257],'cal/(mol*K)','+|-',[0.616252,0.684043,0.664075,0.638453,0.576535,0.489596,0.347267]),
        H298 = (7.5286,'kcal/mol','+|-',3.59998),
        S298 = (2.20275,'cal/(mol*K)','+|-',1.9021),
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
    index = 130,
    label = "Cs(Cl)2-CO",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    Cl1s        u0 {1,S}
4    Cl1s        u0 {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.956137,0.43572,0.056715,-0.165037,-0.215222,-0.207231,0.0700284],'cal/(mol*K)','+|-',[0.63316,0.70281,0.682295,0.655969,0.592353,0.503029,0.356795]),
        H298 = (2.6194,'kcal/mol','+|-',3.69875),
        S298 = (1.30289,'cal/(mol*K)','+|-',1.95428),
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
    index = 131,
    label = "Cs(Br)2-CO",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    Br1s        u0 {1,S}
4    Br1s        u0 {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.791105,0.0725798,-0.137604,-0.143582,-0.0434897,-0.0359075,0.162802],'cal/(mol*K)','+|-',[0.643811,0.714634,0.693773,0.667005,0.602318,0.511491,0.362797]),
        H298 = (1.29719,'kcal/mol','+|-',3.76097),
        S298 = (1.06487,'cal/(mol*K)','+|-',1.98716),
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
    index = 132,
    label = "Cs(Val7)-CO",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    Val7        u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.881268,0.287094,0.0281108,-0.146237,-0.223619,-0.218464,0.179447],'cal/(mol*K)','+|-',[0.458816,0.509288,0.494422,0.475345,0.429246,0.364517,0.25855]),
        H298 = (2.81291,'kcal/mol','+|-',2.60914),
        S298 = (1.83386,'cal/(mol*K)','+|-',0.667673),
    ),
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
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    F1s         u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.04542,0.438465,0.141274,-0.0803466,-0.26832,-0.282561,0.150643],'cal/(mol*K)','+|-',[0.458816,0.509288,0.494422,0.475345,0.429246,0.364517,0.25855]),
        H298 = (4.3193,'kcal/mol','+|-',2.68028),
        S298 = (2.07831,'cal/(mol*K)','+|-',1.41616),
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
    index = 134,
    label = "Cs(Cl)-CO",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    Cl1s        u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.907955,0.373877,0.0973013,-0.151715,-0.259263,-0.250296,0.12894],'cal/(mol*K)','+|-',[0.458921,0.509404,0.494534,0.475453,0.429343,0.3646,0.258609]),
        H298 = (2.05692,'kcal/mol','+|-',2.68089),
        S298 = (1.96977,'cal/(mol*K)','+|-',1.41648),
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
    index = 135,
    label = "Cs(Br)-CO",
    group = 
"""
1 *1 Cs          ux {2,S} {3,S} {4,S} {5,S}
2 *2 CO          ux {1,S} {6,D}
3    Br1s        u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    [C,H,O,N,S] ux {1,S}
6    O2d         ux {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.690428,0.0489385,-0.154243,-0.206649,-0.143274,-0.122535,0.258757],'cal/(mol*K)','+|-',[0.460985,0.511696,0.496759,0.477592,0.431275,0.366241,0.259772]),
        H298 = (2.06252,'kcal/mol','+|-',2.69295),
        S298 = (1.45351,'cal/(mol*K)','+|-',1.42286),
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
    index = 136,
    label = "Cd(Val7)=CdOs",
    group = 
"""
1 *1 Cd          ux {2,D} {3,S} {4,S}
2 *2 Cd          ux {1,D} {5,S}
3    Val7        u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    O2s         ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.395131,-1.09762,-1.313,-1.21017,-0.819763,-0.493962,-0.251683],'cal/(mol*K)','+|-',[0.267954,0.29743,0.288748,0.277607,0.250684,0.212882,0.150996]),
        H298 = (7.86289,'kcal/mol','+|-',6.92752),
        S298 = (1.36782,'cal/(mol*K)','+|-',0.334722),
    ),
    shortDesc = """Average of children""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "Cd(F)=CdOs",
    group = 
"""
1 *1 Cd          ux {2,D} {3,S} {4,S}
2 *2 Cd          ux {1,D} {5,S}
3    F           u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    O2s         ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.327737,-0.999998,-1.2469,-1.15162,-0.79169,-0.482397,-0.239318],'cal/(mol*K)','+|-',[0.267954,0.29743,0.288748,0.277607,0.250684,0.212882,0.150996]),
        H298 = (9.103,'kcal/mol','+|-',1.56531),
        S298 = (1.17775,'cal/(mol*K)','+|-',0.827054),
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
    index = 138,
    label = "Cd(Cl)=CdOs",
    group = 
"""
1 *1 Cd          ux {2,D} {3,S} {4,S}
2 *2 Cd          ux {1,D} {5,S}
3    Cl          u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    O2s         ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.509746,-1.48927,-1.74531,-1.54988,-0.997751,-0.555139,-0.241881],'cal/(mol*K)','+|-',[0.248689,0.276046,0.267988,0.257648,0.232661,0.197577,0.14014]),
        H298 = (10.5359,'kcal/mol','+|-',1.45277),
        S298 = (1.4931,'cal/(mol*K)','+|-',0.767592),
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
    index = 139,
    label = "Cd(Br)=CdOs",
    group = 
"""
1 *1 Cd          ux {2,D} {3,S} {4,S}
2 *2 Cd          ux {1,D} {5,S}
3    Br          u0 {1,S}
4    [C,H,O,N,S] ux {1,S}
5    O2s         ux {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.347909,-0.803591,-0.946777,-0.929001,-0.669847,-0.444349,-0.27385],'cal/(mol*K)','+|-',[0.320948,0.356254,0.345855,0.33251,0.300263,0.254985,0.180859]),
        H298 = (3.94978,'kcal/mol','+|-',1.87489),
        S298 = (1.43261,'cal/(mol*K)','+|-',0.990625),
    ),
    shortDesc = """Derived from RMG Thermo Libraries""",
    longDesc = 
"""
Fitted using sklearn Ridge regression with alpha = 1e-06
Library  | Number of Species
CHOBr_G4 |         6
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
        L3: Cd(Val7)=CdOs
            L4: Cd(F)=CdOs
            L4: Cd(Cl)=CdOs
            L4: Cd(Br)=CdOs
"""
)

