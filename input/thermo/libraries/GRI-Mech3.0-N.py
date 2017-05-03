#!/usr/bin/env python
# encoding: utf-8

name = "GRI-Mech3.0-N"
shortDesc = u"An optimized detailed reaction mechanism for natural gas combustion in flames and ignition."
longDesc = u"""
The thermodynamic and kinetic parameters in the GRI-Mech 3.0 mechanism have 
been collectively estimated from literature search and then optimized to a set 
of representative experimental targets. For this reason you should generally
use GRI-Mech in its entirety, and generally should not tweak any of its
parameter values.

GRI-Mech is the result of collaborative research of the Gas Research Institute
and carried out at The University of California at Berkeley, Stanford 
University, The University of Texas at Austin, and SRI International.

This method seems to use direct thermo data instead of NASA Polynomials (that GRI-Mech3.0 uses)
"""
entry(
    index = 0,
    label = "C(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9798,4.9734,4.9715,4.9711,4.9692,4.9691,4.9742],'cal/(mol*K)'),
        H298 = (171.271,'kcal/mol'),
        S298 = (37.7801,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u1 p0 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.0485,10.5393,10.8828,11.1958,11.9369,12.6543,14.1032],'cal/(mol*K)'),
        H298 = (135.31,'kcal/mol'),
        S298 = (50.9787,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C2H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.5476,12.0136,13.0765,13.8878,15.1592,16.2292,18.1726],'cal/(mol*K)'),
        H298 = (54.5337,'kcal/mol'),
        S298 = (48.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CH2CO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.4027,14.2004,15.6747,16.8939,18.7914,20.2463,22.5514],'cal/(mol*K)'),
        H298 = (-11.4012,'kcal/mol'),
        S298 = (57.7998,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "HCCOH",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.9828,15.7658,17.0442,18.0315,19.6529,21.0031,23.2596],'cal/(mol*K)'),
        H298 = (18.7002,'kcal/mol'),
        S298 = (56.2443,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.2397,12.0282,13.7085,15.1698,17.3442,19.0697,21.8125],'cal/(mol*K)'),
        H298 = (71.6303,'kcal/mol'),
        S298 = (55.8909,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 O u1 p2 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.1758,15.1461,16.9608,18.5959,21.3009,23.3432,26.3517],'cal/(mol*K)'),
        H298 = (5.997,'kcal/mol'),
        S298 = (63.9953,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C2H4",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.2892,12.5808,14.8838,16.9528,20.0509,22.4865,26.3011],'cal/(mol*K)'),
        H298 = (12.5449,'kcal/mol'),
        S298 = (52.4085,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CH3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p0 c0 {1,S} {6,S} {7,D}
6 H u0 p0 c0 {5,S}
7 O u0 p2 c0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.265,15.7804,18.2902,20.5798,24.1643,26.911,30.9565],'cal/(mol*K)'),
        H298 = (-39.718,'kcal/mol'),
        S298 = (63.073,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.1085,14.5881,17.0748,19.349,22.9308,25.7757,30.295],'cal/(mol*K)'),
        H298 = (28.3551,'kcal/mol'),
        S298 = (59.0506,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.5989,15.5691,18.5786,21.3595,25.8037,29.3182,34.8751],'cal/(mol*K)'),
        H298 = (-20.0407,'kcal/mol'),
        S298 = (54.7727,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 O u1 p2 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.6001,12.9016,13.8887,14.6586,15.815,16.6647,17.9598],'cal/(mol*K)'),
        H298 = (42.3961,'kcal/mol'),
        S298 = (58.9514,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.6729,22.488,26.8645,30.7445,37.0108,41.7294,48.8319],'cal/(mol*K)'),
        H298 = (-24.8216,'kcal/mol'),
        S298 = (64.5594,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9722,6.9853,7.0277,7.1072,7.3738,7.7111,8.5599],'cal/(mol*K)'),
        H298 = (142.751,'kcal/mol'),
        S298 = (43.7385,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.0767,8.3274,8.6613,9.0402,9.8277,10.5707,11.8972],'cal/(mol*K)'),
        H298 = (102.734,'kcal/mol'),
        S298 = (45.2159,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.3744,8.7312,9.0805,9.4126,10.0265,10.6563,11.8659],'cal/(mol*K)'),
        H298 = (93.759,'kcal/mol'),
        S298 = (46.4583,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "H2CN",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 N u1 p1 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1619,10.3151,11.4244,12.4654,14.2394,15.4197,17.1343],'cal/(mol*K)'),
        H298 = (59.1066,'kcal/mol'),
        S298 = (53.5877,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.4703,9.3623,10.4367,11.524,13.3741,14.8153,17.0067],'cal/(mol*K)'),
        H298 = (-25.9497,'kcal/mol'),
        S298 = (52.2757,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1952,9.9751,10.7531,11.5019,12.8632,14.0828,16.2904],'cal/(mol*K)'),
        H298 = (35.1048,'kcal/mol'),
        S298 = (46.3598,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.0791,10.7854,12.432,13.9755,16.6291,18.5968,21.5101],'cal/(mol*K)'),
        H298 = (3.8949,'kcal/mol'),
        S298 = (54.5988,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.5842,12.9049,14.1314,15.2327,17.0407,18.4987,20.9633],'cal/(mol*K)'),
        H298 = (-3.4975,'kcal/mol'),
        S298 = (58.286,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.5461,9.686,11.1112,12.6016,15.2944,17.593,21.6069],'cal/(mol*K)'),
        H298 = (-17.8292,'kcal/mol'),
        S298 = (44.5349,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {1,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.5521,12.2835,14.2254,16.0912,19.0716,21.4265,25.1953],'cal/(mol*K)'),
        H298 = (-48.0222,'kcal/mol'),
        S298 = (57.3045,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "HCN",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.5853,9.3626,9.9746,10.4771,11.3044,12.0051,13.1955],'cal/(mol*K)'),
        H298 = (31.2611,'kcal/mol'),
        S298 = (48.2276,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p0 c+1 {2,T} {4,S}
4 N u1 p2 c-1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.7637,13.0971,14.1362,14.9562,16.1623,17.0055,18.2178],'cal/(mol*K)'),
        H298 = (110.436,'kcal/mol'),
        S298 = (59.7661,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "HNCO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,D}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.1305,12.2284,13.218,14.0994,15.5453,16.8291,17.9957],'cal/(mol*K)'),
        H298 = (-28.22,'kcal/mol'),
        S298 = (57.5248,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "HOCN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 N u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.081,12.0406,12.8977,13.6585,14.9174,16.1235,17.2462],'cal/(mol*K)'),
        H298 = (-2.8221,'kcal/mol'),
        S298 = (57.8538,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "HCNO",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p0 c+1 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.2117,12.586,13.7252,14.6656,16.0776,17.3086,18.37],'cal/(mol*K)'),
        H298 = (40.8726,'kcal/mol'),
        S298 = (57.9949,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.2736,8.7177,9.2417,9.78,10.7402,11.4859,12.5894],'cal/(mol*K)'),
        H298 = (10.0359,'kcal/mol'),
        S298 = (53.6078,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "NCO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.6022,10.4921,11.2263,11.8335,12.7501,13.3444,14.0726],'cal/(mol*K)'),
        H298 = (31.4954,'kcal/mol'),
        S298 = (55.5305,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9646,7.02,7.1241,7.2685,7.622,7.9253,8.4148],'cal/(mol*K)'),
        H298 = (-26.4155,'kcal/mol'),
        S298 = (47.2322,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.8944,9.8646,10.6635,11.3172,12.2908,12.9818,13.9559],'cal/(mol*K)'),
        H298 = (-94.0423,'kcal/mol'),
        S298 = (51.0868,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9675,4.9675,4.9675,4.9675,4.9675,4.9675,4.9675],'cal/(mol*K)'),
        H298 = (52.0965,'kcal/mol'),
        S298 = (27.4128,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.8947,6.9967,7.0015,6.9912,7.0775,7.2085,7.7142],'cal/(mol*K)'),
        H298 = (-0.0010521,'kcal/mol'),
        S298 = (31.2263,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "NH2",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.0942,8.3088,8.6017,8.9411,9.6723,10.4063,11.8559],'cal/(mol*K)'),
        H298 = (45.8949,'kcal/mol'),
        S298 = (46.596,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.0289,8.1893,8.4154,8.6799,9.2564,9.8687,11.3017],'cal/(mol*K)'),
        H298 = (-57.7928,'kcal/mol'),
        S298 = (45.1219,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "H2O2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.1468,11.0801,11.9818,12.7799,13.9821,14.9309,16.604],'cal/(mol*K)'),
        H298 = (-32.4741,'kcal/mol'),
        S298 = (56.0421,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "NH3",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.5315,9.2368,10.0361,10.8347,12.2487,13.5096,15.8722],'cal/(mol*K)'),
        H298 = (-10.9701,'kcal/mol'),
        S298 = (46.0646,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "NH",
    molecule = 
"""
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9764,6.9777,6.9982,7.0454,7.2242,7.4742,8.0656],'cal/(mol*K)'),
        H298 = (85.2952,'kcal/mol'),
        S298 = (43.3053,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "NNH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.2915,8.7969,9.3698,9.9216,10.7975,11.4748,12.4736],'cal/(mol*K)'),
        H298 = (59.6283,'kcal/mol'),
        S298 = (53.6481,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "HNO",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.1018,8.4776,8.9841,9.5359,10.5665,11.4163,13.2067],'cal/(mol*K)'),
        H298 = (25.3925,'kcal/mol'),
        S298 = (52.7907,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.1402,7.0675,7.0458,7.0581,7.1493,7.3353,7.8741],'cal/(mol*K)'),
        H298 = (9.4021,'kcal/mol'),
        S298 = (43.9063,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.3476,8.8852,9.4641,9.9944,10.7704,11.3791,12.4826],'cal/(mol*K)'),
        H298 = (2.9984,'kcal/mol'),
        S298 = (54.7475,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "N",
    molecule = 
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9675,4.9675,4.9675,4.9675,4.9675,4.9674,4.9718],'cal/(mol*K)'),
        H298 = (112.96,'kcal/mol'),
        S298 = (36.6336,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9485,7.0068,7.0824,7.1901,7.5026,7.8294,8.3178],'cal/(mol*K)'),
        H298 = (-0.00069005,'kcal/mol'),
        S298 = (45.7646,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "N2O",
    molecule = 
"""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2514,10.2062,10.9663,11.5845,12.535,13.1973,14.1027],'cal/(mol*K)'),
        H298 = (19.4994,'kcal/mol'),
        S298 = (52.574,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.1356,7.1606,7.2872,7.4644,7.8324,8.1228,8.5354],'cal/(mol*K)'),
        H298 = (21.8094,'kcal/mol'),
        S298 = (50.3605,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "NO2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.8983,9.6673,10.424,11.0924,12.0469,12.6693,13.4292],'cal/(mol*K)'),
        H298 = (8.1701,'kcal/mol'),
        S298 = (57.3913,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2338,5.1292,5.0777,5.0517,5.0156,5.0005,4.9819],'cal/(mol*K)'),
        H298 = (59.547,'kcal/mol'),
        S298 = (38.4879,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.0233,7.1986,7.4285,7.6673,8.0656,8.3363,8.7407],'cal/(mol*K)'),
        H298 = (-0.0010244,'kcal/mol'),
        S298 = (49.0236,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "CN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9683,7.0374,7.1588,7.3187,7.6883,7.9923,8.4849],'cal/(mol*K)'),
        H298 = (104.835,'kcal/mol'),
        S298 = (48.4238,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

