#!/usr/bin/env python
# encoding: utf-8

name = "GRI-Mech3.0"
shortDesc = ""
longDesc = """

"""

entry(
    index = 1,
    label = "s00000208",
    molecule = 
"""
1     C     4
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.9798,4.9734,4.9715,4.9711,4.9692,4.9691,4.9742],"cal/(mol*K)"),
        H298 = (171.271,"kcal/mol"),
        S298 = (37.7801,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "s00002295",
    molecule = 
"""
1     C     0 {2,T}
2     C     1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.0485,10.5393,10.8828,11.1958,11.9369,12.6543,14.1032],"cal/(mol*K)"),
        H298 = (135.31,"kcal/mol"),
        S298 = (50.9787,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "s00002305",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.5476,12.0136,13.0765,13.8878,15.1592,16.2292,18.1726],"cal/(mol*K)"),
        H298 = (54.5337,"kcal/mol"),
        S298 = (48.01,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "s00002431",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.4027,14.2004,15.6747,16.8939,18.7914,20.2463,22.5514],"cal/(mol*K)"),
        H298 = (-11.4012,"kcal/mol"),
        S298 = (57.7998,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "s00002432",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.9828,15.7658,17.0442,18.0315,19.6529,21.0031,23.2596],"cal/(mol*K)"),
        H298 = (18.7002,"kcal/mol"),
        S298 = (56.2443,"cal/(mol*K)"),
    ),
    shortDesc = """Neither TRange included 298K!""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "s00002447",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.2397,12.0282,13.7085,15.1698,17.3442,19.0697,21.8125],"cal/(mol*K)"),
        H298 = (71.6303,"kcal/mol"),
        S298 = (55.8909,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "s00002559",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.1758,15.1461,16.9608,18.5959,21.3009,23.3432,26.3517],"cal/(mol*K)"),
        H298 = (5.997,"kcal/mol"),
        S298 = (63.9953,"cal/(mol*K)"),
    ),
    shortDesc = """Neither TRange included 298K!""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "s00002577",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.2892,12.5808,14.8838,16.9528,20.0509,22.4865,26.3011],"cal/(mol*K)"),
        H298 = (12.5449,"kcal/mol"),
        S298 = (52.4085,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "s00002656",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.265,15.7804,18.2902,20.5798,24.1643,26.911,30.9565],"cal/(mol*K)"),
        H298 = (-39.718,"kcal/mol"),
        S298 = (63.073,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "s00002703",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.1085,14.5881,17.0748,19.349,22.9308,25.7757,30.295],"cal/(mol*K)"),
        H298 = (28.3551,"kcal/mol"),
        S298 = (59.0506,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "s00002784",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.5989,15.5691,18.5786,21.3595,25.8037,29.3182,34.8751],"cal/(mol*K)"),
        H298 = (-20.0407,"kcal/mol"),
        S298 = (54.7727,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "s00003017",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.6001,12.9016,13.8887,14.6586,15.815,16.6647,17.9598],"cal/(mol*K)"),
        H298 = (42.3961,"kcal/mol"),
        S298 = (58.9514,"cal/(mol*K)"),
    ),
    shortDesc = """Neither TRange included 298K!""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "s00003749",
    molecule = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.6729,22.488,26.8645,30.7445,37.0108,41.7294,48.8319],"cal/(mol*K)"),
        H298 = (-24.8216,"kcal/mol"),
        S298 = (64.5594,"cal/(mol*K)"),
    ),
    shortDesc = """Neither TRange included 298K!""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "s00009010",
    molecule = 
"""
1     C     3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.9722,6.9853,7.0277,7.1072,7.3738,7.7111,8.5599],"cal/(mol*K)"),
        H298 = (142.751,"kcal/mol"),
        S298 = (43.7385,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "s00009012",
    molecule = 
"""
1     C     2S
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.0767,8.3274,8.6613,9.0402,9.8277,10.5707,11.8972],"cal/(mol*K)"),
        H298 = (102.734,"kcal/mol"),
        S298 = (45.2159,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "s00009015",
    molecule = 
"""
1     C     2T
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.3744,8.7312,9.0805,9.4126,10.0265,10.6563,11.8659],"cal/(mol*K)"),
        H298 = (93.759,"kcal/mol"),
        S298 = (46.4583,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "s00009076",
    molecule = 
"""
1     C     0 {2,D}
2     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.4703,9.3623,10.4367,11.524,13.3741,14.8153,17.0067],"cal/(mol*K)"),
        H298 = (-25.9497,"kcal/mol"),
        S298 = (52.2757,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "s00009089",
    molecule = 
"""
1     C     1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.1952,9.9751,10.7531,11.5019,12.8632,14.0828,16.2904],"cal/(mol*K)"),
        H298 = (35.1048,"kcal/mol"),
        S298 = (46.3598,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "s00009173",
    molecule = 
"""
1     C     0 {2,S}
2     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.0791,10.7854,12.432,13.9755,16.6291,18.5968,21.5101],"cal/(mol*K)"),
        H298 = (3.8949,"kcal/mol"),
        S298 = (54.5988,"cal/(mol*K)"),
    ),
    shortDesc = """Neither TRange included 298K!""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "s00009174",
    molecule = 
"""
1     C     1 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.5842,12.9049,14.1314,15.2327,17.0407,18.4987,20.9633],"cal/(mol*K)"),
        H298 = (-3.4975,"kcal/mol"),
        S298 = (58.286,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "s00009193",
    molecule = 
"""
1     C     0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.5461,9.686,11.1112,12.6016,15.2944,17.593,21.6069],"cal/(mol*K)"),
        H298 = (-17.8292,"kcal/mol"),
        S298 = (44.5349,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "s00009219",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.5521,12.2835,14.2254,16.0912,19.0716,21.4265,25.1953],"cal/(mol*K)"),
        H298 = (-48.0222,"kcal/mol"),
        S298 = (57.3045,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "s00009325",
    molecule = 
"""
1     C     1 {2,D}
2     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.2736,8.7177,9.2417,9.78,10.7402,11.4859,12.5894],"cal/(mol*K)"),
        H298 = (10.0359,"kcal/mol"),
        S298 = (53.6078,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "s00009358",
    molecule = 
"""
1     C     2T {2,D}
2     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.9646,7.02,7.1241,7.2685,7.622,7.9253,8.4148],"cal/(mol*K)"),
        H298 = (-26.4155,"kcal/mol"),
        S298 = (47.2322,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "s00009360",
    molecule = 
"""
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.8944,9.8646,10.6635,11.3172,12.2908,12.9818,13.9559],"cal/(mol*K)"),
        H298 = (-94.0423,"kcal/mol"),
        S298 = (51.0868,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "s00009800",
    molecule = 
"""
1     H     1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.9675,4.9675,4.9675,4.9675,4.9675,4.9675,4.9675],"cal/(mol*K)"),
        H298 = (52.0965,"kcal/mol"),
        S298 = (27.4128,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "s00009809",
    molecule = 
"""
1     H     0 {2,S}
2     H     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.8947,6.9967,7.0015,6.9912,7.0775,7.2085,7.7142],"cal/(mol*K)"),
        H298 = (-0.0010521,"kcal/mol"),
        S298 = (31.2263,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "s00009881",
    molecule = 
"""
1     O     0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.0289,8.1893,8.4154,8.6799,9.2564,9.8687,11.3017],"cal/(mol*K)"),
        H298 = (-57.7928,"kcal/mol"),
        S298 = (45.1219,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "s00009882",
    molecule = 
"""
1     O     0 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.1468,11.0801,11.9818,12.7799,13.9821,14.9309,16.604],"cal/(mol*K)"),
        H298 = (-32.4741,"kcal/mol"),
        S298 = (56.0421,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "s00010102",
    molecule = 
"""
1     O     1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.1402,7.0675,7.0458,7.0581,7.1493,7.3353,7.8741],"cal/(mol*K)"),
        H298 = (9.4021,"kcal/mol"),
        S298 = (43.9063,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "s00010103",
    molecule = 
"""
1     O     0 {2,S}
2     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.3476,8.8852,9.4641,9.9944,10.7704,11.3791,12.4826],"cal/(mol*K)"),
        H298 = (2.9984,"kcal/mol"),
        S298 = (54.7475,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "s00010285",
    molecule = 
"""
1     O     2T
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.2338,5.1292,5.0777,5.0517,5.0156,5.0005,4.9819],"cal/(mol*K)"),
        H298 = (59.547,"kcal/mol"),
        S298 = (38.4879,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "s00010295",
    molecule = 
"""
1     O     1 {2,S}
2     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.0233,7.1986,7.4285,7.6673,8.0656,8.3363,8.7407],"cal/(mol*K)"),
        H298 = (-0.0010244,"kcal/mol"),
        S298 = (49.0236,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

