#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration"
shortDesc = ""
longDesc = """

"""

template(reactants=["RnOOH"], products=["HORO."], ownReverse=False)

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "RnOOH",
    group = "OR{ROOH, R2OOH, R3OOH, R4OOH}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.25662e-06,0.0404311,9.84703,384.03,37427.5,584098,2.27796e+07,1.42258e+08],"s^-1","*|/",[4762,445.351,107.623,41.8145,12.8756,6.38377,2.56631,1.713])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=1 label="RnOOH">, <Entry index=2 label="Y_rad_out">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1  *1 {Cd,Cs,Sid,Sis} 1
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
    label = "ROOH",
    group = 
"""
1  *1 {Cd,Cs,Sid,Sis} 1 {2,S}
2  *2 O 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4     H 0 {3,S}
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
    index = 4,
    label = "R2OOH",
    group = 
"""
1  *1 {Cd,Cs,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,Sid,Sis} 0 {1,{S,D}} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0309482,0.124759,0.287963,0.502935,1.00979,1.53413,2.67941,3.541],"s^-1","*|/",[4.5683e+07,551525,39124.5,6727.71,750.769,203.078,36.3737,15.7734])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=5 label="R2OOH_S">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=23 label="C_rad_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "R2OOH_S",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0309482,0.124759,0.287963,0.502935,1.00979,1.53413,2.67941,3.541],"s^-1","*|/",[4.5683e+07,551525,39124.5,6727.71,750.769,203.078,36.3737,15.7734])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=5 label="R2OOH_S">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=23 label="C_rad_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
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
    index = 7,
    label = "R3OOH",
    group = 
"""
1  *1 {Cd,Cs,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,Sid,Sis} 0 {1,{S,D}} {3,{S,D}}
3     {Cd,Cs,Sid,Sis} 0 {2,{S,D}} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000280616,0.0022473,0.00783052,0.0179974,0.0509312,0.0950712,0.218508,0.331267],"s^-1","*|/",[5.52622,3.46309,2.848,2.65767,2.66199,2.79375,3.12132,3.35223])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "R3OOH_SS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000280616,0.0022473,0.00783052,0.0179974,0.0509312,0.0950712,0.218508,0.331267],"s^-1","*|/",[5.52622,3.46309,2.848,2.65767,2.66199,2.79375,3.12132,3.35223])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
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
    index = 10,
    label = "R3OOH_DS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
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
    index = 11,
    label = "R4OOH",
    group = 
"""
1  *1 {Cd,Cs,Sid,Sis} 1 {2,{S,D}}
2  *4 {Cd,Cs,Sid,Sis} 0 {1,{S,D}} {3,{S,D}}
3     {Cd,Cs,Sid,Sis} 0 {2,{S,D}} {4,{S,D}}
4     {Cd,Cs,Sid,Sis} 0 {3,{S,D}} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([11535.7,811.227,164.969,57.0481,15.1283,6.82213,2.35917,1.38733],"s^-1","*|/",[19.5055,8.43552,5.10144,3.64828,2.39939,1.86611,1.33516,1.13052])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=12 label="R4OOH_SSS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "R4OOH_SSS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4     {Cd,Cs} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([11535.7,811.227,164.969,57.0481,15.1283,6.82213,2.35917,1.38733],"s^-1","*|/",[19.5055,8.43552,5.10144,3.64828,2.39939,1.86611,1.33516,1.13052])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=12 label="R4OOH_SSS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
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
    index = 14,
    label = "R4OOH_SDS",
    group = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3     Cd 0 {2,D} {4,S}
4     {Cd,Cs} 0 {3,S} {5,S}
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
    label = "R4OOH_DSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4     {Cd,Cs} 0 {3,S} {5,S}
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
    index = 17,
    label = "Cd_rad_out",
    group = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
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
    label = "Cdsingle_rad_out",
    group = 
"""
1  *1 Cd 1 {2,S}
2     R 0 {1,S}
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
    label = "CdsingleH_rad_out",
    group = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
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
    label = "CdsingleND_rad_out",
    group = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
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
    label = "CdsingleDe_rad_out",
    group = 
"""
1  *1 Cd 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C_rad_out_single",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.6529,0.735795,0.790501,0.829214,0.880281,0.912419,0.957102,0.980258],"s^-1","*|/",[4.94189,3.25148,2.55087,2.18561,1.83079,1.67224,1.53371,1.50149])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "C_rad_out_2H",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.124576,0.22328,0.316884,0.400191,0.535767,0.638265,0.806061,0.90584],"s^-1","*|/",[40.9709,14.9805,8.231,5.54576,3.4221,2.59452,1.87068,1.6617])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=12 label="R4OOH_SSS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=8 label="R3OOH_SS">, <Entry index=23 label="C_rad_out_2H">]
[<Entry index=5 label="R2OOH_S">, <Entry index=23 label="C_rad_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "C_rad_out_1H",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.1875,1.13467,1.1041,1.08419,1.05979,1.04542,1.02657,1.01726],"s^-1","*|/",[48.2549,18.399,10.4877,7.30691,4.78351,3.8093,2.9771,2.73468])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.1875,1.13467,1.1041,1.08419,1.05979,1.04542,1.02657,1.01726],"s^-1","*|/",[48.2549,18.399,10.4877,7.30691,4.78351,3.8093,2.9771,2.73468])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=5 label="R2OOH_S">, <Entry index=25 label="C_rad_out_H/NonDeC">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=25 label="C_rad_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "C_rad_out_H/NonDeO",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
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
    index = 27,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
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
    index = 28,
    label = "C_rad_out_noH",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.19365,2.29852,1.88688,1.65428,1.40342,1.27156,1.11481,1.04384],"s^-1","*|/",[39.0253,9.96894,6.32587,6.3135,8.92686,12.5005,21.3525,28.5822])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 29,
    label = "C_rad_out_NonDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.19365,2.29852,1.88688,1.65428,1.40342,1.27156,1.11481,1.04384],"s^-1","*|/",[39.0253,9.96894,6.32587,6.3135,8.92686,12.5005,21.3525,28.5822])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "C_rad_out_Cs2",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.19365,2.29852,1.88688,1.65428,1.40342,1.27156,1.11481,1.04384],"s^-1","*|/",[39.0253,9.96894,6.32587,6.3135,8.92686,12.5005,21.3525,28.5822])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=8 label="R3OOH_SS">, <Entry index=30 label="C_rad_out_Cs2">]
[<Entry index=12 label="R4OOH_SSS">, <Entry index=30 label="C_rad_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C_rad_out_NDMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     O 0 {1,S}
3     {Cs,O} 0 {1,S}
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
    label = "C_rad_out_OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cs,O} 0 {1,S}
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
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 34,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 35,
    label = "C_rad_out_TwoDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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

tree(
"""
L1: RnOOH
    L2: ROOH
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
L1: Y_rad_out
    L2: Cd_rad_out
    L2: Cdsingle_rad_out
        L3: CdsingleH_rad_out
        L3: CdsingleND_rad_out
        L3: CdsingleDe_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                L5: C_rad_out_NDMustO
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
            L4: C_rad_out_TwoDe
"""
)

