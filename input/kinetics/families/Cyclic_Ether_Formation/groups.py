#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["RnOOH"], products=["RO", "OH"], ownReverse=False)

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['GAIN_RADICAL', '*3', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "RnOOH",
    group = "OR{R2OOH, R3OOH, R4OOH, R5OOH}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([64.3876,9675.81,195803,1.45403e+06,1.78244e+07,8.01828e+07,5.95436e+08,1.6226e+09],"s^-1","*|/",[1413.1,220.185,73.3829,35.7752,15.0422,9.24215,5.25012,4.23699])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=32 label="C_pri_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=37 label="C_ter_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=31 label="Cs_rad_intra">]
[<Entry index=17 label="R5OOH_SSSS">, <Entry index=31 label="Cs_rad_intra">]
[<Entry index=7 label="R3OOH_SS">, <Entry index=31 label="Cs_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=33 label="C_sec_rad_intra">]
[<Entry index=1 label="RnOOH">, <Entry index=2 label="Y_rad_intra">]
[<Entry index=4 label="R2OOH_S">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_intra",
    group = 
"""
1  *1 R 1
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
    index = 3,
    label = "R2OOH",
    group = 
"""
1  *1 {Cd,Cs,CO,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,CO,Sid,Sis} 0 {1,{S,D}} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.72947e-07,6.44759e-05,0.000798331,0.00427274,0.0347825,0.122392,0.655053,1.51544],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=4 label="R2OOH_S">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "R2OOH_S",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.72947e-07,6.44759e-05,0.000798331,0.00427274,0.0347825,0.122392,0.655053,1.51544],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=4 label="R2OOH_S">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "R2OOH_D",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
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
    index = 6,
    label = "R3OOH",
    group = 
"""
1  *1 {Cd,Cs,CO,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,CO,Sid,Sis} 0 {1,{S,D}} {3,{S,D}}
3     {Cd,Cs,CO,Sid,Sis} 0 {2,{S,D}} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0100523,0.0392879,0.089013,0.15355,0.303561,0.456923,0.788206,1.03523],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=7 label="R3OOH_SS">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "R3OOH_SS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0100523,0.0392879,0.089013,0.15355,0.303561,0.456923,0.788206,1.03523],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=7 label="R3OOH_SS">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "R3OOH_SD",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3     Cd 0 {2,D} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
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
    label = "R3OOH_DS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
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
    label = "R4OOH",
    group = 
"""
1  *1 {Cd,Cs,CO,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,CO,Sid,Sis} 0 {1,{S,D}} {3,{S,D}}
3     {Cd,Cs,CO,Sid,Sis} 0 {2,{S,D}} {4,{S,D}}
4     {Cd,Cs,CO,Sid,Sis} 0 {3,{S,D}} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.56051,1.33215,1.2115,1.1372,1.05071,1.002,0.940549,0.911253],"s^-1","*|/",[278822,7611.26,877.364,207.829,34.3549,11.6719,2.77421,1.36983])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=33 label="C_sec_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=32 label="C_pri_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=37 label="C_ter_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "R4OOH_SSS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.56051,1.33215,1.2115,1.1372,1.05071,1.002,0.940549,0.911253],"s^-1","*|/",[278822,7611.26,877.364,207.829,34.3549,11.6719,2.77421,1.36983])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=33 label="C_sec_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=32 label="C_pri_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=37 label="C_ter_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "R4OOH_SSD",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     Cd 0 {2,S} {4,D}
4     Cd 0 {3,D} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
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
    index = 13,
    label = "R4OOH_SDS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3     Cd 0 {2,D} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
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
    label = "R4OOH_DSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
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
    index = 15,
    label = "R4OOH_DSD",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     Cd 0 {2,S} {4,D}
4     Cd 0 {3,D} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
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
    label = "R5OOH",
    group = 
"""
1  *1 {Cd,Cs,CO,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,CO,Sid,Sis} 0 {1,{S,D}} {3,{S,D}}
3     {Cd,Cs,CO,Sid,Sis} 0 {2,{S,D}} {4,{S,D}}
4     {Cd,Cs,CO,Sid,Sis} 0 {3,{S,D}} {5,{S,D}}
5     {Cd,Cs,CO,Sid,Sis} 0 {4,{S,D}} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([985149,13676.2,1050.62,189.858,22.3698,6.20013,1.12043,0.476299],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=17 label="R5OOH_SSSS">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "R5OOH_SSSS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5     {Cd,Cs,CO} 0 {4,S} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([985149,13676.2,1050.62,189.858,22.3698,6.20013,1.12043,0.476299],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=17 label="R5OOH_SSSS">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "R5OOH_SSSD",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     Cd 0 {3,S} {5,D}
5     Cd 0 {4,D} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
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
    label = "R5OOH_SSDS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     Cd 0 {2,S} {4,D}
4     Cd 0 {3,D} {5,S}
5     {Cd,Cs,CO} 0 {4,S} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
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
    label = "R5OOH_SDSS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3     Cd 0 {2,D} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5     {Cd,Cs,CO} 0 {4,S} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
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
    label = "R5OOH_DSSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5     {Cd,Cs,CO} 0 {4,S} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
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
    label = "R5OOH_SDSD",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3     Cd 0 {2,D} {4,S}
4     Cd 0 {3,S} {5,D}
5     Cd 0 {4,D} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
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
    label = "R5OOH_DSDS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     Cd 0 {2,S} {4,D}
4     Cd 0 {3,D} {5,S}
5     Cd 0 {4,S} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
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
    label = "Cd_rad_in",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2  *4 C 0 {1,D}
3     R 0 {1,S}
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
    index = 25,
    label = "Cd_pri_rad_in",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2  *4 C 0 {1,D}
3     H 0 {1,S}
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
    index = 26,
    label = "Cd_sec_rad_in",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2  *4 C 0 {1,D}
3     R!H 0 {1,S}
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
    index = 27,
    label = "Cd_rad_in/NonDeC",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2  *4 C 0 {1,D}
3     Cs 0 {1,S}
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
    label = "Cd_rad_in/NonDeO",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2  *4 C 0 {1,D}
3     O 0 {1,S}
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
    index = 29,
    label = "Cd_rad_in/OneDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2  *4 C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "Cd_rad_out",
    group = 
"""
1  *1 C 1 {2,S} {3,D}
2  *4 C 0 {1,S}
3     Cd 0 {1,D}
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
    label = "Cs_rad_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.811374,0.843642,0.863615,0.877193,0.894465,0.904991,0.919219,0.926417],"s^-1","*|/",[915.269,129.191,39.9109,18.241,6.85701,3.81411,1.74983,1.20132])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=32 label="C_pri_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=37 label="C_ter_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=31 label="Cs_rad_intra">]
[<Entry index=17 label="R5OOH_SSSS">, <Entry index=31 label="Cs_rad_intra">]
[<Entry index=7 label="R3OOH_SS">, <Entry index=31 label="Cs_rad_intra">]
[<Entry index=11 label="R4OOH_SSS">, <Entry index=33 label="C_sec_rad_intra">]
[<Entry index=4 label="R2OOH_S">, <Entry index=31 label="Cs_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C_pri_rad_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4  *4 C 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0097928,0.0359105,0.0783089,0.131685,0.25217,0.372382,0.626202,0.81204],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=32 label="C_pri_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 33,
    label = "C_sec_rad_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3  *4 C 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.141895,0.244605,0.339127,0.421659,0.553618,0.651868,0.81051,0.903769],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=33 label="C_sec_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 34,
    label = "C_rad/H/NonDeC_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3  *4 C 0 {1,S}
4     Cs 0 {1,S}
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
    label = "C_rad/H/NonDeO_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3  *4 C 0 {1,S}
4     O 0 {1,S}
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
    label = "C_rad/H/OneDe_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4  *4 C 0 {1,S}
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
    label = "C_ter_rad_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.24371,1.14297,1.08649,1.05039,1.00695,0.981756,0.949139,0.933239],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=11 label="R4OOH_SSS">, <Entry index=37 label="C_ter_rad_intra">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:30 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "C_rad/NonDeC_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
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
    label = "C_rad/Cs3_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
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
    label = "C_rad/NDMustO_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
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
    label = "C_rad/OneDe_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3  *4 C 0 {1,S}
4     {Cs,O} 0 {1,S}
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
    label = "C_rad/Cs2_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3  *4 C 0 {1,S}
4     Cs 0 {1,S}
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
    label = "C_rad/ODMustO_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3  *4 C 0 {1,S}
4     O 0 {1,S}
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
    label = "C_rad/TwoDe_intra",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4  *4 C 0 {1,S}
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

tree(
"""
L1: RnOOH
    L2: R2OOH
        L3: R2OOH_S
        L3: R2OOH_D
    L2: R3OOH
        L3: R3OOH_SS
        L3: R3OOH_SD
        L3: R3OOH_DS
    L2: R4OOH
        L3: R4OOH_SSS
        L3: R4OOH_SSD
        L3: R4OOH_SDS
        L3: R4OOH_DSS
        L3: R4OOH_DSD
    L2: R5OOH
        L3: R5OOH_SSSS
        L3: R5OOH_SSSD
        L3: R5OOH_SSDS
        L3: R5OOH_SDSS
        L3: R5OOH_DSSS
        L3: R5OOH_SDSD
        L3: R5OOH_DSDS
L1: Y_rad_intra
    L2: Cd_rad_in
        L3: Cd_pri_rad_in
        L3: Cd_sec_rad_in
            L4: Cd_rad_in/NonDeC
            L4: Cd_rad_in/NonDeO
            L4: Cd_rad_in/OneDe
    L2: Cd_rad_out
    L2: Cs_rad_intra
        L3: C_pri_rad_intra
        L3: C_sec_rad_intra
            L4: C_rad/H/NonDeC_intra
            L4: C_rad/H/NonDeO_intra
            L4: C_rad/H/OneDe_intra
        L3: C_ter_rad_intra
            L4: C_rad/NonDeC_intra
                L5: C_rad/Cs3_intra
                L5: C_rad/NDMustO_intra
            L4: C_rad/OneDe_intra
                L5: C_rad/Cs2_intra
                L5: C_rad/ODMustO_intra
            L4: C_rad/TwoDe_intra
"""
)

