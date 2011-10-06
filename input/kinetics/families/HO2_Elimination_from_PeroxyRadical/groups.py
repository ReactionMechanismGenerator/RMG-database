#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["R2OO"], products=["R=R", "OOH"], ownReverse=False)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*5'],
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['FORM_BOND', '*4', 'S', '*5'],
    ['GAIN_RADICAL', '*3', '1'],
    ['LOSE_RADICAL', '*4', '1'],
])

entry(
    index = 1,
    label = "R2OO",
    group = 
"""
1  *2 {C,Si} 0 {2,S} {3,S}
2  *1 {C,Si,O} 0 {1,S} {5,S}
3  *3 O 0 {1,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {2,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([3.99149e-08,0.00354807,3.44175,346.397,115808,3.94192e+06,4.73868e+08,5.55909e+09],"s^-1","*|/",[15.3284,6.34153,3.71136,2.5861,1.63442,1.23343,1.19567,1.46717]),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [14, 14, 14, 14, 14, 14, 14, 14] rates.
[<Entry index=3 label="R2OO_2H_2H">]
[<Entry index=28 label="R2OO_NdNd_NdNd">]
[<Entry index=25 label="R2OO_NdNd_2H">]
[<Entry index=26 label="R2OO_NdNd_HNd">]
[<Entry index=12 label="R2OO_HNd_HNd">]
[<Entry index=1 label="R2OO">]
[<Entry index=45 label="OCOO">]
[<Entry index=6 label="CH3CH(OO)CHCH2">]
[<Entry index=5 label="R2OO_2H_HDe">]
[<Entry index=14 label="R2OO_HNd_NdNd">]
[<Entry index=46 label="HOCH[OO]CH3">]
[<Entry index=4 label="R2OO_2H_HNd">]
[<Entry index=11 label="R2OO_HNd_2H">]
[<Entry index=7 label="R2OO_2H_NdNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Modified the group definition to allow O at *1 site, after MRHarper's change to old RMG database."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
        ("Thu Oct  6 15:15:53 2011","Josh Allen <jwallen@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "R2OO_2H",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {7,S}
4  *5 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.0418263,0.0780572,0.117725,0.158629,0.240469,0.320141,0.506952,0.678374],"s^-1","*|/",[1,1,1,1,1,1,1,1]),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=5 label="R2OO_2H_HDe">]
[<Entry index=3 label="R2OO_2H_2H">]
[<Entry index=6 label="CH3CH(OO)CHCH2">]
[<Entry index=4 label="R2OO_2H_HNd">]
[<Entry index=7 label="R2OO_2H_NdNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 3,
    label = "R2OO_2H_2H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.00117355,0.0057411,0.0155708,0.0312042,0.0784874,0.142813,0.349379,0.589573],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=3 label="R2OO_2H_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "R2OO_2H_HNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.00229356,0.0109565,0.0285349,0.0546966,0.126153,0.212258,0.442261,0.658989],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=4 label="R2OO_2H_HNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "R2OO_2H_HDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([1.52258,0.755306,0.522537,0.423155,0.345775,0.322729,0.32909,0.362793],"s^-1","*|/",[1,1,1,1,1,1,1,1]),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=6 label="CH3CH(OO)CHCH2">]
[<Entry index=5 label="R2OO_2H_HDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "CH3CH(OO)CHCH2",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {5,S} {6,S}
2  *1 C 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 {1,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5  *3 O 0 {1,S} {13,S}
6     H 0 {1,S}
7  *5 H 0 {2,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13 *4 O 1 {5,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([1.52258,0.755306,0.522537,0.423155,0.345775,0.322729,0.32909,0.362793],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=6 label="CH3CH(OO)CHCH2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "R2OO_2H_NdNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.0205155,0.0807517,0.186391,0.328657,0.67922,1.06512,2.00091,2.8094],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=7 label="R2OO_2H_NdNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "R2OO_2H_NdDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "R2OO_2H_DeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "R2OO_HNd",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {7,S}
4  *5 H 0 {1,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.00487265,0.0172384,0.0363601,0.0593361,0.10793,0.15273,0.236622,0.288757],"s^-1","*|/",[1,1,1,1,1,1,1,1]),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=12 label="R2OO_HNd_HNd">]
[<Entry index=11 label="R2OO_HNd_2H">]
[<Entry index=14 label="R2OO_HNd_NdNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "R2OO_HNd_2H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.00189831,0.00734983,0.0171235,0.0307713,0.0666151,0.109496,0.228184,0.348514],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=11 label="R2OO_HNd_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "R2OO_HNd_HNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.00359016,0.0132809,0.0294298,0.0503824,0.0999296,0.152348,0.27356,0.373294],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=12 label="R2OO_HNd_HNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "R2OO_HNd_HDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "R2OO_HNd_NdNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.0169752,0.052479,0.0953884,0.134751,0.188867,0.213569,0.212241,0.185066],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=14 label="R2OO_HNd_NdNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "R2OO_HNd_NdDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "R2OO_HNd_DeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "R2OO_HDe",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {7,S}
4  *5 H 0 {1,S}
5     H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "R2OO_HDe_2H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "R2OO_HDe_HNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "R2OO_HDe_HDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "R2OO_HDe_NdNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "R2OO_HDe_NdDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "R2OO_HDe_DeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     H 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "R2OO_NdNd",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {7,S}
4  *5 H 0 {1,S}
5     {Cs,O} 0 {1,S}
6     {Cs,O} 0 {1,S}
7  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.0146538,0.0590134,0.130717,0.216215,0.386576,0.526048,0.727409,0.798982],"s^-1","*|/",[1,1,1,1,1,1,1,1]),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=26 label="R2OO_NdNd_HNd">]
[<Entry index=28 label="R2OO_NdNd_NdNd">]
[<Entry index=25 label="R2OO_NdNd_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "R2OO_NdNd_2H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.0018583,0.00821022,0.020424,0.0379962,0.0845206,0.139297,0.282948,0.416986],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=25 label="R2OO_NdNd_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "R2OO_NdNd_HNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.00692988,0.0256155,0.0554887,0.0921956,0.171582,0.246244,0.389005,0.479631],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=26 label="R2OO_NdNd_HNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "R2OO_NdNd_HDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "R2OO_NdNd_NdNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([0.244347,0.977224,1.97083,2.8854,3.98355,4.24395,3.49682,2.55025],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=28 label="R2OO_NdNd_NdNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 29,
    label = "R2OO_NdNd_NdDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "R2OO_NdNd_DeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cs,O} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "R2OO_NdDe",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {7,S}
4  *5 H 0 {1,S}
5     {Cs,O} 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "R2OO_NdDe_2H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "R2OO_NdDe_HNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "R2OO_NdDe_HDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "R2OO_NdDe_NdNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "R2OO_NdDe_NdDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "R2OO_NdDe_DeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cs,O} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "R2OO_DeDe",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {5,S} {6,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {7,S}
4  *5 H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "R2OO_DeDe_2H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *5 H 0 {2,S}
7     {Cd,Ct,Cb,CO} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "R2OO_DeDe_HNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cd,Ct,Cb,CO} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "R2OO_DeDe_HDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cd,Ct,Cb,CO} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "R2OO_DeDe_NdNd",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cd,Ct,Cb,CO} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "R2OO_DeDe_NdDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cd,Ct,Cb,CO} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "R2OO_DeDe_DeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 O 0 {1,S} {9,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
6  *5 H 0 {2,S}
7     {Cd,Ct,Cb,CO} 0 {2,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9  *4 O 1 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "OCOO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 O 0 {1,S} {7,S}
3  *3 O 0 {1,S} {6,S}
4     R 0 {1,S}
5     R 0 {1,S}
6  *4 O 1 {3,S}
7  *5 H 0 {2,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([4.51929e+10,8.45685e+07,1.91714e+06,151732,6235,902.098,65.9276,17.2901],"s^-1","*|/",[1,1,1,1,1,1,1,1]),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=45 label="OCOO">]
[<Entry index=46 label="HOCH[OO]CH3">]
""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 46,
    label = "HOCH[OO]CH3",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3  *1 O 0 {1,S} {10,S}
4  *3 O 0 {1,S} {9,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9  *4 O 1 {4,S}
10 *5 H 0 {3,S}
""",
    kinetics = KineticsData(
        Tdata = ([300,400,500,600,800,1000,1500,2000],"K"),
        kdata = ([4.51929e+10,8.45685e+07,1.91714e+06,151732,6235,902.098,65.9276,17.2901],"s^-1"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=46 label="HOCH[OO]CH3">]
""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

tree(
"""
L1: R2OO
    L2: R2OO_2H
        L3: R2OO_2H_2H
        L3: R2OO_2H_HNd
        L3: R2OO_2H_HDe
            L4: CH3CH(OO)CHCH2
        L3: R2OO_2H_NdNd
        L3: R2OO_2H_NdDe
        L3: R2OO_2H_DeDe
    L2: R2OO_HNd
        L3: R2OO_HNd_2H
        L3: R2OO_HNd_HNd
        L3: R2OO_HNd_HDe
        L3: R2OO_HNd_NdNd
        L3: R2OO_HNd_NdDe
        L3: R2OO_HNd_DeDe
    L2: R2OO_HDe
        L3: R2OO_HDe_2H
        L3: R2OO_HDe_HNd
        L3: R2OO_HDe_HDe
        L3: R2OO_HDe_NdNd
        L3: R2OO_HDe_NdDe
        L3: R2OO_HDe_DeDe
    L2: R2OO_NdNd
        L3: R2OO_NdNd_2H
        L3: R2OO_NdNd_HNd
        L3: R2OO_NdNd_HDe
        L3: R2OO_NdNd_NdNd
        L3: R2OO_NdNd_NdDe
        L3: R2OO_NdNd_DeDe
    L2: R2OO_NdDe
        L3: R2OO_NdDe_2H
        L3: R2OO_NdDe_HNd
        L3: R2OO_NdDe_HDe
        L3: R2OO_NdDe_NdNd
        L3: R2OO_NdDe_NdDe
        L3: R2OO_NdDe_DeDe
    L2: R2OO_DeDe
        L3: R2OO_DeDe_2H
        L3: R2OO_DeDe_HNd
        L3: R2OO_DeDe_HDe
        L3: R2OO_DeDe_NdNd
        L3: R2OO_DeDe_NdDe
        L3: R2OO_DeDe_DeDe
    L2: OCOO
        L3: HOCH[OO]CH3
"""
)

