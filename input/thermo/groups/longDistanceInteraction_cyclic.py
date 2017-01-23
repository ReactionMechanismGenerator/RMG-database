#!/usr/bin/env python
# encoding: utf-8

name = "Long distance interaction correction for cyclic molecule"
shortDesc = u""
longDesc = u"""
Designed to account for the long distance interaction for cyclic molecule.
Currently we only have the data for aromatic ortho/meta/para corrections.
Watch out:  if the groups on the two labeled atoms are identical, it's value should be halved because it'll be counted twice.
            For example, for the interaction of ortho OH and OH, which is labeled as 'o_OH_OH' in this database,
            it'll be counted in both {'*1': atom1, '*2'atom2} and {'*2': atom1, '*1'atom2}.
            It should be claimed in the 'longDesc' if a entry was halved.

Source: 
For aromatic molecule: [1] Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008
For aromatic radical: [2] A paper from the same group but still under reviewing.

Sep-29-2016 PZ
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
    shortDesc = u"""ROOT""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
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
    shortDesc = u"""Aromatics NNI correction for ortho position.""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "o_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    C u0 {2,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49, -2.15, -1.77, -1.43, -0.81, -0.33, 0.43],'cal/(mol*K)'),
        H298 = (-6.55,'kcal/mol'),
        S298 = (-5.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 3,
    label = "o_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
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
    label = "o_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C u0 {1,S} {4,S} {8,D}
4    H u0 {3,S}
5    C u0 {2,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
8    O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.20, 0.19, 0.17, 0.05, -0.10, -0.30],'cal/(mol*K)'),
        H298 = (2.52,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 4,
    label = "o_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {5,S} {6,S} {7,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    H u0 {4,S}
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
    index = 4,
    label = "o_MeO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {5,S} {6,S} {7,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    H u0 {4,S}
8    O u0 {2,S} {9,S}
9    C u0 {8,S} {10,S} {11,S} {12,S}
10   H u0 {9,S}
11   H u0 {9,S}
12   H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00, -0.41, -0.56, -0.60, -0.53, -0.44, -0.26],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (0.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 5,
    label = "o_CHO_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,D} {8,S}
7    C u0 {6,D} {9,S} {10,S}
8    H u0 {6,S}
9    H u0 {7,S}
10   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31, 0.38, 0.50, 0.60, 0.57, 0.43, 0.07],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (-0.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 6,
    label = "o_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6   H u0 {5,S}
7   H u0 {5,S}
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
    label = "o_vinyl_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {11,S} {12,S}
6    C u0 {2,S} {7,D} {8,S}
7    C u0 {6,D} {9,S} {10,S}
8    H u0 {6,S}
9    H u0 {7,S}
10   H u0 {7,S}
11   H u0 {5,S}
12   H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55, 0.38, 0.25, 0.16, 0.02, -0.02, -0.06],'cal/(mol*K)'),
        H298 = (0.97,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 7,
    label = "o_CHO_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    label = "o_CHO_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    C u0 {6,S} {10,S} {11,S} {12,S}
10    H u0 {9,S}
11    H u0 {9,S}
12    H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    label = "o_vinyl_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    C u0 {2,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 10,
    label = "o_vinyl_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    C u0 {2,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   C u0 {8,S} {12,S} {13,S} {14,S}
12   H u0 {11,S}
13   H u0 {11,S}
14   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 11,
    label = "o_CHO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    O u0 {2,S} {7,S}
7    C u0 {6,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62, 0.07, 0.62, 0.93, 0.98, 0.79, 0.31],'cal/(mol*K)'),
        H298 = (1.89,'kcal/mol'),
        S298 = (-0.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 12,
    label = "o_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
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
    index = 12,
    label = "o_CH3_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 13,
    label = "o_CH3_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   C u0 {7,S} {11,S} {12,S} {13,S}
11   H u0 {10,S}
12   H u0 {10,S}
13   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.79, 0.69, 0.62, 0.60, 0.55, 0.48, 0.36],'cal/(mol*K)'),
        H298 = (1.00,'kcal/mol'),
        S298 = (-1.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 14,
    label = "o_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    C u0 {3,S} {7,S} {8,S} {9,S}
7   H u0 {6,S}
8   H u0 {6,S}
9   H u0 {6,S}
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
    label = "o_C2H5_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    C u0 {3,S} {14,S} {15,S} {16,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   C u0 {7,S} {11,S} {12,S} {13,S}
11   H u0 {10,S}
12   H u0 {10,S}
13   H u0 {10,S}
14   H u0 {6,S}
15   H u0 {6,S}
16   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 15,
    label = "o_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
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
    label = "o_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    O u0 {2,S} {6,S}
6    H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32, -0.18, 0.02, 0.24, 0.50, 0.57, 0.44],'cal/(mol*K)'),
        H298 = (-0.36,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 16,
    label = "o_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    O u0 {2,S} {6,S}
6    C u0 {5,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65, -0.36, 0.05, 0.48, 1.00, 1.15, 0.88],'cal/(mol*K)'),
        H298 = (-0.72,'kcal/mol'),
        S298 = (-1.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 17,
    label = "o_OH_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    C u0 {2,S} {6,D} {7,S}
6    C u0 {5,D} {8,S} {9,S}
7    H u0 {5,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 18,
    label = "o_MeO_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {10,S} {11,S} {12,S}
5    C u0 {2,S} {6,D} {7,S}
6    C u0 {5,D} {8,S} {9,S}
7    H u0 {5,S}
8    H u0 {6,S}
9    H u0 {6,S}
10    H u0 {4,S}
11    H u0 {4,S}
12    H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 2,
    label = "o_OCH2j",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O u0 {1,S} {4,S}
4    C u1 {3,S} {5,S} {6,S}
5    H u0 {4,S}
6    H u0 {4,S}
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
    label = "o_OCH2j_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    O u0 {1,S} {4,S}
4    C u1 {3,S} {5,S} {6,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    C u0 {2,S} {8,S} {9,D}
8    H u0 {7,S}
9    O u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.53, 1.20, 1.43, 1.39, 1.00, 0.62, 0.12],'cal/(mol*K)'),
        H298 = (1.67,'kcal/mol'),
        S298 = (-1.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI2. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 3,
    label = "o_OCH2j_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    O u0 {1,S} {4,S}
4    C u1 {3,S} {5,S} {6,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    O u0 {2,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10    H u0 {8,S}
11    H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.93, 0.22, -0.22, -0.36, -0.33, -0.29, -0.14],'cal/(mol*K)'),
        H298 = (2.75,'kcal/mol'),
        S298 = (0.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI3. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 4,
    label = "o_Oj",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O u1 {1,S}
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
    index = 4,
    label = "o_Oj_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O u1 {1,S}
4    O u0 {2,S} {5,S}
5    H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.06, -1.84, -1.58, -1.27, -0.74, -0.31, 0.38],'cal/(mol*K)'),
        H298 = (-8.87,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI4. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 5,
    label = "o_Oj_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O u1 {1,S}
4    O u0 {2,S} {5,S}
5    C u0 {4,S} {6,S} {7,S} {8,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.60, -0.62, -0.53, -0.33, -0.07, 0.05, 0.12],'cal/(mol*K)'),
        H298 = (-1.53,'kcal/mol'),
        S298 = (-0.10,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI5. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 6,
    label = "o_Oj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O u1 {1,S}
4    C u0 {2,S} {5,S} {6,D}
5    H u0 {4,S}
6    O u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.22, -0.02, 0.19, 0.41, 0.69, 0.69, 0.41],'cal/(mol*K)'),
        H298 = (1.36,'kcal/mol'),
        S298 = (-0.10,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI8. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 7,
    label = "o_Oj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O u1 {1,S}
4    C u0 {2,S} {5,S} {6,D}
5    H u0 {4,S}
6    C u0 {4,D} {7,S} {8,S}
7    H u0 {6,S}
8    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0, 0, 0.02, 0.10, 0.24, 0.31, 0.36],'cal/(mol*K)'),
        H298 = (-1.53,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI10. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    label = "o_Oj_Cs",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {4,S}
3    O u1 {1,S}
4    C u0 {2,S} {5,S} {6,S} {7,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    [H,Cs] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.14, -0.12, -0.10, -0.05, -0.05, -0.02, -0.05],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (0.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI12. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    label = "o_Cj=O",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u1 {1,S} {4,D}
4    O u0 {3,D}
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
    label = "o_Cj=O_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C u1 {1,S} {4,D}
4    O u0 {3,D}
5    O u0 {2,S} {6,S}
6    H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.53, -1.08, -0.69, -0.24, 0.55, 1.12, 1.65],'cal/(mol*K)'),
        H298 = (-4.02,'kcal/mol'),
        S298 = (-4.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI14. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    label = "o_Cj=O_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C u1 {1,S} {4,D}
4    O u0 {3,D}
5    O u0 {2,S} {6,S}
6    C u0 {5,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.33, 0.10, 0, -0.14, -0.19, -0.17],'cal/(mol*K)'),
        H298 = (1.77,'kcal/mol'),
        S298 = (0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI16. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 10,
    label = "o_Cj=O_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C u1 {1,S} {4,D}
4    O u0 {3,D}
5    C u0 {2,S} {6,D} {9,S}
6    C u0 {5,D} {7,S} {8,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.76, 0.84, 0.76, 0.62, 0.36, 0.14, 0.02],'cal/(mol*K)'),
        H298 = (0.96,'kcal/mol'),
        S298 = (-1.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI19. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 11,
    label = "o_C=Cj",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,D} {5,S}
4    C u1 {3,D} {6,S}
5    H u0 {3,S}
6    H u0 {4,S}
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
    label = "o_C=Cj_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,D} {5,S}
4    C u1 {3,D} {6,S}
5    H u0 {3,S}
6    H u0 {4,S}
7    O u0 {2,S} {8,S}
8    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31, -0.69, 0.14, 1.10, 2.41, 2.87, 2.25],'cal/(mol*K)'),
        H298 = (-3.39,'kcal/mol'),
        S298 = (-4.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI20. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 12,
    label = "o_C=Cj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,D} {5,S}
4    C u1 {3,D} {6,S}
5    H u0 {3,S}
6    H u0 {4,S}
7    C u0 {2,S} {8,S} {9,D}
8    H u0 {7,S}
9    O u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.53, 0.81, 0.86, 0.79, 0.57, 0.43, 0.24],'cal/(mol*K)'),
        H298 = (3.49,'kcal/mol'),
        S298 = (-1.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI21. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 13,
    label = "o_C=Cj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,D} {5,S}
4    C u1 {3,D} {6,S}
5    H u0 {3,S}
6    H u0 {4,S}
7    C u0 {2,S} {8,S} {9,D}
8    H u0 {7,S}
9    C u0 {7,D} {10,S} {11,S}
10    H u0 {9,S}
11    H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.48, 0.60, 0.53, 0.43, 0.26, 0.17, 0.07],'cal/(mol*K)'),
        H298 = (1.82,'kcal/mol'),
        S298 = (-1.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI22. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 14,
    label = "o_C=Cj_Cs",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,D} {5,S}
4    C u1 {3,D} {6,S}
5    H u0 {3,S}
6    H u0 {4,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10    [H,Cs] u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.69, 0.65, 0.50, 0.36, 0.14, 0.07, -0.02],'cal/(mol*K)'),
        H298 = (1.00,'kcal/mol'),
        S298 = (-0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI23. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 15,
    label = "o_Csj",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u1 {1,S} {4,S} {5,S}
4    H u0 {3,S}
5    [H,Cs] u0 {3,S}
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
    label = "o_Csj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u1 {1,S} {4,S} {5,S}
4    H u0 {3,S}
5    [H,Cs] u0 {3,S}
6    C u0 {2,S} {7,S} {8,D}
7    H u0 {6,S}
8    C u0 {6,D} {9,S} {10,S}
9    H u0 {8,S}
10    H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.43, 0.29, 0.14, 0.02, -0.12, -0.17, -0.17],'cal/(mol*K)'),
        H298 = (1.60,'kcal/mol'),
        S298 = (-0.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI26. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 16,
    label = "o_Csj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u1 {1,S} {4,S} {5,S}
4    H u0 {3,S}
5    [H,Cs] u0 {3,S}
6    C u0 {2,S} {7,S} {8,D}
7    H u0 {6,S}
8    O u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.43, 0.50, 0.43, 0.29, 0.10, -0.05, -0.12],'cal/(mol*K)'),
        H298 = (1.31,'kcal/mol'),
        S298 = (0.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI28. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 17,
    label = "o_Csj_Cs",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u1 {1,S} {4,S} {5,S}
4    H u0 {3,S}
5    [H,Cs] u0 {3,S}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    [H,Cs] u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.81, 0.62, 0.43, 0.29, 0.12, 0.07, 0.00],'cal/(mol*K)'),
        H298 = (0.65,'kcal/mol'),
        S298 = (-0.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI29. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
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
    shortDesc = u"""Aromatics NNI correction for meta position""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
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
        Cpdata = ([0.20, 0.12, 0.06, 0.01, -0.05, -0.08, -0.10],'cal/(mol*K)'),
        H298 = (0.57,'kcal/mol'),
        S298 = (0.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. Aromatics NNI correction.""",
    longDesc = 
u"""
""",
)

entry(
    index = 19,
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
        Cpdata = ([0.22, 0.76, 0.98, 1.03, 0.81, 0.55, 0.22],'cal/(mol*K)'),
        H298 = (-1.65,'kcal/mol'),
        S298 = (-1.00,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI6. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 20,
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
        Cpdata = ([0.38, -0.38, -0.38, -0.38, 0.29, 0.22, 0.12],'cal/(mol*K)'),
        H298 = (1.12,'kcal/mol'),
        S298 = (0.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI9. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 21,
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
        Cpdata = ([0.07, 0.17, 0.17, 0.12, 0.00, -0.07, 0.02],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (0.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI17. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
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
    shortDesc = u"""Aromatics NNI correction for para position.""",
    longDesc = 
u"""
""",
)

entry(
    index = 22,
    label = "p_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
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
    label = "p_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    O u0 {4,S} {8,S}
8    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 23,
    label = "p_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    O u0 {4,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41, 0.10, -0.19, -0.41, -0.55, -0.55, -0.41],'cal/(mol*K)'),
        H298 = (1.74,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 24,
    label = "p_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
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
    label = "p_MeO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {12,S} {13,S} {14,S}
7    O u0 {4,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
12   H u0 {6,S}
13   H u0 {6,S}
14   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
    label = "p_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C u0 {1,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
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
    label = "p_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C u0 {1,S} {6,S} {10,D}
6    H u0 {5,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
10   O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22, 0.17, 0.12, 0.08, 0.01, -0.04, -0.11],'cal/(mol*K)'),
        H298 = (1.18,'kcal/mol'),
        S298 = (-0.10,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 26,
    label = "p_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 27,
    label = "p_MeO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {10,S} {11,S} {12,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
10   H u0 {6,S}
11   H u0 {6,S}
12   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 23,
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
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 23,
    label = "p_OCH2j_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {9,S}
5    O  u0 {1,S} {6,S}
6    C  u1 {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    O  u0 {4,S} {10,S}
10    H  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.10, -0.19, -0.43, -0.57, -0.65, -0.60, -0.33],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI1. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 24,
    label = "p_OCH2j_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {9,S}
5    O  u0 {1,S} {6,S}
6    C  u1 {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    O  u0 {4,S} {10,S}
10    C  u0 {9,S} {11,S} {12,S} {13,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
13    H  u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.10, -0.19, -0.43, -0.57, -0.65, -0.60, -0.33],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI1. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
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
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
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
        Cpdata = ([-0.67, -0.60, -0.45, -0.29, -0.02, 0.17, 0.38],'cal/(mol*K)'),
        H298 = (-3.78,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI7. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 26,
    label = "p_Oj_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    O  u0 {4,S} {7,S}
7    C  u0 {6,S} {8,S} {9,S} {10,S}
8    H  u0 {7,S}
9    H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67, -0.60, -0.45, -0.29, -0.02, 0.17, 0.38],'cal/(mol*K)'),
        H298 = (-3.78,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI7. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 27,
    label = "p_Oj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    C  u0 {4,S} {7,D} {8,S}
7    C  u0 {6,D} {9,S} {10,S}
8    H  u0 {6,S}
9    H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.07, 0.05, 0.05, 0.12, 0.22, 0.29, 0.26],'cal/(mol*K)'),
        H298 = (-3.08,'kcal/mol'),
        S298 = (-0.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI11. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 28,
    label = "p_Oj_Cs",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    C  u0 {4,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    [H,Cs]  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.17, -0.12, -0.10, -0.10, -0.07, -0.05, -0.05],'cal/(mol*K)'),
        H298 = (-1.39,'kcal/mol'),
        S298 = (0.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI13. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 29,
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
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 29,
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
        Cpdata = ([-0.79, -0.65, -0.48, -0.24, 0.05, 0.19, 0.36],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI15. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 30,
    label = "p_Cj=O_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
7    O  u0 {4,S} {8,S}
8    C  u0 {7,S} {9,S} {10,S} {11,S}
9    H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79, -0.65, -0.48, -0.24, 0.05, 0.19, 0.36],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI15. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 31,
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
        Cpdata = ([-0.24, -0.57, -0.84, -0.98, -1.08, -1.03, -0.76],'cal/(mol*K)'),
        H298 = (1.29,'kcal/mol'),
        S298 = (3.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI18. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 32,
    label = "p_Csj",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C  u1 {1,S} {6,S} {7,S}
6    H  u0 {5,S}
7    [H,Cs]  u0 {5,S}
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
    label = "p_Csj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {8,S}
5    C  u1 {1,S} {6,S} {7,S}
6    H  u0 {5,S}
7    [H,Cs]  u0 {5,S}
8    C  u0 {4,S} {9,S} {10,D}
9    H  u0 {8,S}
10    C  u0 {8,D} {11,S} {12,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22, 0.26, 0.29, 0.33, 0.38, 0.38, 0.31],'cal/(mol*K)'),
        H298 = (-1.39,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI25. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 33,
    label = "p_Csj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {8,S}
5    C  u1 {1,S} {6,S} {7,S}
6    H  u0 {5,S}
7    [H,Cs]  u0 {5,S}
8    C  u0 {4,S} {9,S} {10,D}
9    H  u0 {8,S}
10    O  u0 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.29, -0.22, -0.14, -0.10, -0.07, -0.02, 0.07],'cal/(mol*K)'),
        H298 = (-1.24,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI27. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
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
"""
)

