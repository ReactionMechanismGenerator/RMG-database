#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation"
shortDesc = ""
longDesc = """

"""

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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.38459e-07,0.0188259,7.18059,377.656,53489.2,1.04464e+06,5.4942e+07,3.98449e+08],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.04278e-06,9.90328e-05,0.00101651,0.00480105,0.0334283,0.107098,0.50583,1.0993],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.04278e-06,9.90328e-05,0.00101651,0.00480105,0.0334283,0.107098,0.50583,1.0993],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.75704e-07,1.64324e-05,0.000158567,0.000718712,0.00475316,0.0147652,0.0669238,0.142479],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.75704e-07,1.64324e-05,0.000158567,0.000718712,0.00475316,0.0147652,0.0669238,0.142479],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.0147e+08,2.12723e+06,80233.7,9023.7,587.719,114.141,12.8371,4.30509],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.0147e+08,2.12723e+06,80233.7,9023.7,587.719,114.141,12.8371,4.30509],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.1172e+13,7.99971e+09,3.157e+07,788392,7826.66,491.674,12.2785,1.94034],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.1172e+13,7.99971e+09,3.157e+07,788392,7826.66,491.674,12.2785,1.94034],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.562582,0.651336,0.711174,0.754091,0.811396,0.847849,0.899013,0.925741],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000384873,0.00342462,0.0127113,0.0304724,0.0908979,0.175123,0.419817,0.650008],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00050751,0.00351128,0.0112067,0.0242934,0.0638997,0.114158,0.247465,0.364349],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00160862,0.00902434,0.0253976,0.0506264,0.119911,0.201162,0.400987,0.566138],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
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

