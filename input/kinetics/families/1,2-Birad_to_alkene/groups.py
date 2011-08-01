#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["Y_12birad"], products=["Y_alkene"], ownReverse=False)

recipe(actions=[
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_12birad",
    group = "OR{Y_12_00, Y_12_10, Y_12_20, Y_12_30, Y_12_40, Y_12_01, Y_12_02, Y_12_03, Y_12_04, Y_12_11, Y_12_12, Y_12_21, Y_12_22, Y_12_13, Y_12_31}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.3706e+07,2.3706e+07,2.3706e+07,2.3706e+07,2.3706e+07,2.3706e+07,2.3706e+07,2.3706e+07],"s^-1","*|/",[2.20821,2.20821,2.20821,2.20821,2.20821,2.20821,2.20821,2.20821])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 16 rates.
[<Entry index=11 label="Y_12_11">]
[<Entry index=9 label="Y_12_03">]
[<Entry index=4 label="Y_12_20">]
[<Entry index=6 label="Y_12_40">]
[<Entry index=10 label="Y_12_04">]
[<Entry index=16 label="Y_12_31">]
[<Entry index=12 label="Y_12_12">]
[<Entry index=2 label="Y_12_00">]
[<Entry index=13 label="Y_12_21">]
[<Entry index=15 label="Y_12_13">]
[<Entry index=8 label="Y_12_02">]
[<Entry index=14 label="Y_12_22">]
[<Entry index=5 label="Y_12_30">]
[<Entry index=7 label="Y_12_01">]
[<Entry index=1 label="Y_12birad">]
[<Entry index=3 label="Y_12_10">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_12_00",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.21835,4.21835,4.21835,4.21835,4.21835,4.21835,4.21835,4.21835],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=2 label="Y_12_00">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 3,
    label = "Y_12_10",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.66178,2.66178,2.66178,2.66178,2.66178,2.66178,2.66178,2.66178],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=3 label="Y_12_10">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "Y_12_20",
    group = "OR{Y_12_20a, Y_12_20b}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.6789,1.6789,1.6789,1.6789,1.6789,1.6789,1.6789,1.6789],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=4 label="Y_12_20">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "Y_12_30",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.05881,1.05881,1.05881,1.05881,1.05881,1.05881,1.05881,1.05881],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=5 label="Y_12_30">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "Y_12_40",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     {Cs,Os} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.666499,0.666499,0.666499,0.666499,0.666499,0.666499,0.666499,0.666499],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Y_12_40">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "Y_12_01",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.11339,2.11339,2.11339,2.11339,2.11339,2.11339,2.11339,2.11339],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=7 label="Y_12_01">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "Y_12_02",
    group = "OR{Y_12_02a, Y_12_02b}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.05881,1.05881,1.05881,1.05881,1.05881,1.05881,1.05881,1.05881],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=8 label="Y_12_02">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "Y_12_03",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.531512,0.531512,0.531512,0.531512,0.531512,0.531512,0.531512,0.531512],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=9 label="Y_12_03">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "Y_12_04",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.266178,0.266178,0.266178,0.266178,0.266178,0.266178,0.266178,0.266178],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=10 label="Y_12_04">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "Y_12_11",
    group = "OR{Y_12_11a, Y_12_11b}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.333,1.333,1.333,1.333,1.333,1.333,1.333,1.333],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=11 label="Y_12_11">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Y_12_12",
    group = "OR{Y_12_12a, Y_12_12b}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.666499,0.666499,0.666499,0.666499,0.666499,0.666499,0.666499,0.666499],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=12 label="Y_12_12">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "Y_12_21",
    group = "OR{Y_12_21a, Y_12_21b}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.84367,0.84367,0.84367,0.84367,0.84367,0.84367,0.84367,0.84367],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=13 label="Y_12_21">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "Y_12_22",
    group = "OR{Y_12_22a, Y_12_22b}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.421835,0.421835,0.421835,0.421835,0.421835,0.421835,0.421835,0.421835],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=14 label="Y_12_22">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "Y_12_13",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cs,Os} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.334937,0.334937,0.334937,0.334937,0.334937,0.334937,0.334937,0.334937],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=15 label="Y_12_13">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "Y_12_31",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.531512,0.531512,0.531512,0.531512,0.531512,0.531512,0.531512,0.531512],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=16 label="Y_12_31">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = -1,
    label = "Y_12_20a",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_20b",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     H 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_02a",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_02b",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_11a",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_11b",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_12a",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_12b",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_21a",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_21b",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     H 0 {2,S}
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
    index = -1,
    label = "Y_12_22a",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     {Cs,Os} 0 {2,S}
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
    index = -1,
    label = "Y_12_22b",
    group = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cs,Os} 0 {2,S}
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
L1: Y_12birad
    L2: Y_12_00
    L2: Y_12_10
    L2: Y_12_20
    L2: Y_12_30
    L2: Y_12_40
    L2: Y_12_01
    L2: Y_12_02
    L2: Y_12_03
    L2: Y_12_04
    L2: Y_12_11
    L2: Y_12_12
    L2: Y_12_21
    L2: Y_12_22
    L2: Y_12_13
    L2: Y_12_31
"""
)

