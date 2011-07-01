#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/groups"
shortDesc = ""
longDesc = """

"""

template(reactants=["COm", "Y_rad"], products=["YC.=O"], ownReverse=False)

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "COm",
    group = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([60.7145,453.614,1548.8,3561.98,10346.2,20040.5,50646.5,83456],"m^3/(mol*s)","*|/",[5.95201,4.16789,3.61439,3.47145,3.63426,4.01811,5.2393,6.56202])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=1 label="COm">, <Entry index=32 label="CH[CH3]2">]
[<Entry index=1 label="COm">, <Entry index=23 label="CH2CH3">]
[<Entry index=1 label="COm">, <Entry index=18 label="Cb_rad">]
[<Entry index=1 label="COm">, <Entry index=20 label="C_methyl">]
[<Entry index=1 label="COm">, <Entry index=22 label="C_rad/H2/Cs">]
[<Entry index=1 label="COm">, <Entry index=24 label="CH2CH2CH3">]
[<Entry index=1 label="COm">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=1 label="COm">, <Entry index=14 label="Cd_pri_rad">]
[<Entry index=1 label="COm">, <Entry index=2 label="Y_rad">]
[<Entry index=1 label="COm">, <Entry index=3 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad",
    group = 
"""
1  *2 R 1
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
    label = "H_rad",
    group = 
"""
1  *2 H 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([69.2693,22.6024,11.2993,7.01707,3.77198,2.54416,1.43783,1.0428],"m^3/(mol*s)","*|/",[3.84873e+09,4.3464e+07,2.94996e+06,490842,52161.2,13589.1,2261.08,922.313])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=1 label="COm">, <Entry index=3 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "O_rad",
    group = 
"""
1  *2 O 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00366446,0.00172575,0.0010752,0.00077328,0.000499376,0.000376019,0.000246101,0.000192079],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=7 label="O_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "O_pri_rad",
    group = 
"""
1  *2 O 1 {2,S}
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
    index = 6,
    label = "O_sec_rad",
    group = 
"""
1  *2 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00366446,0.00172575,0.0010752,0.00077328,0.000499376,0.000376019,0.000246101,0.000192079],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=7 label="O_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "O_rad/NonDe",
    group = 
"""
1  *2 O 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00366446,0.00172575,0.0010752,0.00077328,0.000499376,0.000376019,0.000246101,0.000192079],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=7 label="O_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "O_rad/OneDe",
    group = 
"""
1  *2 O 1 {2,S}
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
    index = 9,
    label = "Ct_rad",
    group = 
"""
1  *2 C 1 {2,T}
2     C 0 {1,T}
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
    label = "CO_rad",
    group = 
"""
1  *2 C 1 {2,D}
2     O 0 {1,D}
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
    label = "CO_pri_rad",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     O 0 {1,D}
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
    index = 12,
    label = "CO_sec_rad",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     O 0 {1,D}
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
    index = 13,
    label = "Cd_rad",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.779248,0.783943,0.770153,0.75038,0.708259,0.669678,0.59378,0.539409],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=14 label="Cd_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "Cd_pri_rad",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.779248,0.783943,0.770153,0.75038,0.708259,0.669678,0.59378,0.539409],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=14 label="Cd_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "Cd_sec_rad",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     C 0 {1,D}
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
    index = 16,
    label = "Cd_rad/NonDe",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     C 0 {1,D}
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
    index = 17,
    label = "Cd_rad/OneDe",
    group = 
"""
1  *2 C 1 {2,D} {3,S}
2     C 0 {1,D}
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
    index = 18,
    label = "Cb_rad",
    group = 
"""
1  *2 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([91.436,49.4523,33.4777,25.4474,17.6111,13.8229,9.56184,7.67231],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=18 label="Cb_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "Cs_rad",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.358623,0.644353,0.935595,1.21681,1.73324,2.18933,3.12889,3.87718],"m^3/(mol*s)","*|/",[7.93557,4.89858,4.33343,4.50909,5.67784,7.33774,12.6236,19.1173])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=1 label="COm">, <Entry index=20 label="C_methyl">]
[<Entry index=1 label="COm">, <Entry index=32 label="CH[CH3]2">]
[<Entry index=1 label="COm">, <Entry index=22 label="C_rad/H2/Cs">]
[<Entry index=1 label="COm">, <Entry index=24 label="CH2CH2CH3">]
[<Entry index=1 label="COm">, <Entry index=23 label="CH2CH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "C_methyl",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.245975,0.502311,0.791569,1.09089,1.68059,2.23634,3.46311,4.50512],"m^3/(mol*s)","*|/",[4.58418e+08,2.58274e+07,1.08455e+07,1.07528e+07,2.93576e+07,1.26508e+08,5.54645e+09,1.55398e+11])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=1 label="COm">, <Entry index=20 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "C_pri_rad",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.321656,0.565901,0.801663,1.01744,1.38576,1.6836,2.22641,2.60065],"m^3/(mol*s)","*|/",[14.7625,2.69549,1.12975,2.52522,7.70659,16.5237,55.7564,119.807])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=1 label="COm">, <Entry index=22 label="C_rad/H2/Cs">]
[<Entry index=1 label="COm">, <Entry index=24 label="CH2CH2CH3">]
[<Entry index=1 label="COm">, <Entry index=23 label="CH2CH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "C_rad/H2/Cs",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.321656,0.565901,0.801663,1.01744,1.38576,1.6836,2.22641,2.60065],"m^3/(mol*s)","*|/",[14.7625,2.69549,1.12975,2.52522,7.70659,16.5237,55.7564,119.807])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=1 label="COm">, <Entry index=22 label="C_rad/H2/Cs">]
[<Entry index=1 label="COm">, <Entry index=24 label="CH2CH2CH3">]
[<Entry index=1 label="COm">, <Entry index=23 label="CH2CH3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "CH2CH3",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     H 0 {4,S}
7     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.224791,0.485088,0.80731,1.17039,1.97033,2.82527,5.06024,7.33978],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=23 label="CH2CH3">]
""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "CH2CH2CH3",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     H 0 {4,S}
7     C 0 {4,S} {8,S} {9,S} {10,S}
8     H 0 {7,S}
9     H 0 {7,S}
10    H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.189985,0.476559,0.828626,1.19928,1.90694,2.52226,3.67297,4.44269],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=24 label="CH2CH2CH3">]
""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "C_rad/H2/Cd",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
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
    label = "C_rad/H2/Ct",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
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
    label = "C_rad/H2/Cb",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cb 0 {1,S}
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
    label = "C_rad/H2/CO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     CO 0 {1,S}
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
    label = "C_rad/H2/O",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
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
    index = 30,
    label = "C_sec_rad",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.05651,1.56522,2.07765,2.58962,3.60705,4.614,7.08913,9.51563],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=32 label="CH[CH3]2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C_rad/H/NonDeC",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.05651,1.56522,2.07765,2.58962,3.60705,4.614,7.08913,9.51563],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=32 label="CH[CH3]2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "CH[CH3]2",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     C 0 {1,S} {5,S} {6,S} {7,S}
4     C 0 {1,S} {8,S} {9,S} {10,S}
5     H 0 {3,S}
6     H 0 {3,S}
7     H 0 {3,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.05651,1.56522,2.07765,2.58962,3.60705,4.614,7.08913,9.51563],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="COm">, <Entry index=32 label="CH[CH3]2">]
""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
        ("Mon Jun 20 17:29:32 2011","Richard West <rwest@mit.edu>","action","""Generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 33,
    label = "C_rad/H/NonDeO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
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
    index = 34,
    label = "C_rad/H/CsO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
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
    index = 35,
    label = "C_rad/H/O2",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
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
    label = "C_rad/H/OneDe",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 37,
    label = "C_rad/H/OneDeC",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 38,
    label = "C_rad/H/OneDeO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 39,
    label = "C_rad/H/TwoDe",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C_ter_rad",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
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
    label = "C_rad/NonDeC",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cs,O} 0 {1,S}
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
    index = 42,
    label = "C_rad/Cs3",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
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
    index = 43,
    label = "C_rad/NDMustO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
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
    index = 44,
    label = "C_rad/OneDe",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 45,
    label = "C_rad/OD_Cs2",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 46,
    label = "C_rad/ODMustO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 47,
    label = "C_rad/TwoDe",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 48,
    label = "C_rad/TD_Cs",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 49,
    label = "C_rad/TDMustO",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 50,
    label = "C_rad/ThreeDe",
    group = 
"""
1  *2 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
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
L1: COm
L1: Y_rad
    L2: H_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: Ct_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
                L5: CH2CH3
                L5: CH2CH2CH3
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
        L3: C_sec_rad
            L4: C_rad/H/NonDeC
                L5: CH[CH3]2
            L4: C_rad/H/NonDeO
                L5: C_rad/H/CsO
                L5: C_rad/H/O2
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                L5: C_rad/H/OneDeO
            L4: C_rad/H/TwoDe
        L3: C_ter_rad
            L4: C_rad/NonDeC
                L5: C_rad/Cs3
                L5: C_rad/NDMustO
            L4: C_rad/OneDe
                L5: C_rad/OD_Cs2
                L5: C_rad/ODMustO
            L4: C_rad/TwoDe
                L5: C_rad/TD_Cs
                L5: C_rad/TDMustO
            L4: C_rad/ThreeDe
"""
)

forbidden(
    label = "O2_birad",
    group = 
"""
1  *2 O 1 {2,S}
2     O 1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

