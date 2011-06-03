#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration"
shortDesc = ""
longDesc = """

"""

template(reactants=["RnH"], products=["RnH"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "RnH",
    group = "OR{R2H, R3H, R4H, R5H, R6H, R7H}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.50795e-16,3.28444e-09,4.50549e-05,0.0266116,81.7796,10592,7.65066e+06,2.21987e+08],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1  *1 R!H 1
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
    label = "XH_out",
    group = 
"""
1  *2 R!H 0 {2,S}
2  *3 H 0 {1,S}
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
    index = 4,
    label = "R2H",
    group = 
"""
1  *1 R!H 1 {2,{S,D,B}}
2  *2 R!H 0 {1,{S,D,B}} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0363224,0.117974,0.238977,0.382359,0.687297,0.976226,1.55563,1.96072],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "R2H_S",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *2 R!H 0 {1,S} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0309418,0.104162,0.215619,0.350046,0.640903,0.920601,1.48967,1.8926],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "R2H_S_cy3",
    group = 
"""
1  *1 R!H 1 {2,S} {4,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000728418,0.00844974,0.0361362,0.0941117,0.305004,0.606911,1.4634,2.20671],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "R2H_S_cy4",
    group = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {1,{S,D,B}} {4,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00998073,0.0454988,0.111,0.198718,0.402662,0.603924,0.996917,1.24189],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "R2H_S_cy5",
    group = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {4,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0484948,0.20463,0.474975,0.8207,1.58446,2.30055,3.61035,4.36011],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "Others-R2H_S",
    group = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0401239,0.120949,0.234979,0.366365,0.63987,0.89599,1.40989,1.7748],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "R2H_D",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *2 Cd 0 {1,D} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([11.8723,10.582,9.80425,9.27272,8.57427,8.12119,7.43722,7.03032],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "R2H_B",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *2 Cb 0 {1,B} {3,S}
3  *3 H 0 {2,S}
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
    index = 12,
    label = "R3H",
    group = "OR{R3H_SR, R3H_MS, R3H_BB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0479365,0.103609,0.164574,0.224092,0.329731,0.415843,0.566976,0.66237],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "R3H_SR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{S,D,T,B}}
3  *2 R!H 0 {2,{S,D,T,B}} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0452537,0.0990406,0.158515,0.216946,0.321287,0.406799,0.55767,0.653354],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "R3H_SS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0865619,0.15979,0.230934,0.29529,0.401737,0.483462,0.619478,0.70178],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "R3H_SS_12cy3",
    group = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.14891e+06,48721.4,7099.74,1927.52,364.663,130.344,31.0256,14.3975],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "R3H_SS_23cy3",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.61675e-05,0.000234441,0.00117585,0.00346372,0.0134944,0.0307614,0.0938824,0.166238],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "R3H_SS_12cy4",
    group = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.152589,0.245056,0.319559,0.376694,0.452517,0.49575,0.537863,0.542825],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "R3H_SS_23cy4",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0176927,0.0489706,0.0917466,0.141011,0.246209,0.349868,0.579581,0.767555],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "R3H_SS_13cy4",
    group = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.5053e-12,6.43745e-09,3.12518e-07,4.08152e-06,9.79988e-05,0.000641464,0.00739369,0.0239359],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "R3H_SS_12cy5",
    group = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.154085,0.277325,0.388397,0.481118,0.617119,0.705326,0.814932,0.853048],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "R3H_SS_23cy5",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.817903,0.735947,0.704053,0.692263,0.693249,0.707183,0.756352,0.807655],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "R3H_SS_13cy5",
    group = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.48126e-06,0.000105037,0.000797944,0.00305015,0.0159888,0.042499,0.151086,0.27711],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "R3H_SS_2Cd",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.06016e-08,3.77147e-06,6.82515e-05,0.000472716,0.00535708,0.0231562,0.165589,0.448224],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "R3H_SS_OC",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0121551,0.0482077,0.111444,0.196314,0.403783,0.629491,1.16582,1.61707],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "Others-R3H_SS",
    group = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.44009,4.17782,2.75623,2.09711,1.50084,1.23529,0.965104,0.861699],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "R3H_SD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.26376e-09,4.08675e-07,9.21262e-06,7.3413e-05,0.00098043,0.00463318,0.0365753,0.102397],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "R3H_ST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Ct 0 {1,S} {3,T}
3  *2 Ct 0 {2,T} {4,S}
4  *3 H 0 {3,S}
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
    label = "R3H_SB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3  *2 Cb 0 {2,B} {4,S}
4  *3 H 0 {3,S}
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
    label = "R3H_MS",
    group = 
"""
1  *1 R!H 1 {2,{D,T,B}}
2  *4 R!H 0 {1,{D,T,B}} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.225935,0.34877,0.451769,0.536207,0.662915,0.751583,0.885225,0.957901],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "R3H_DS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.225935,0.34877,0.451769,0.536207,0.662915,0.751583,0.885225,0.957901],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "R3H_TS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
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
    index = 32,
    label = "R3H_BS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
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
    index = 33,
    label = "R3H_BB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3  *2 Cb 0 {2,B} {4,S}
4  *3 H 0 {3,S}
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
    index = 34,
    label = "R4H",
    group = "OR{R4H_RSR, R4H_SMS, R4H_SBB, R4H_BBS, R4H_BBB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.97615e+07,452297,20325.7,2570.93,194.165,41.2537,5.24167,1.87163],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 35,
    label = "R4H_RSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 R!H 0 {2,S} {4,{S,D,T,B}}
4  *2 R!H 0 {3,{S,D,T,B}} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.14217e+08,937067,35947.5,4084.77,269.012,52.5148,5.92794,1.98664],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 36,
    label = "R4H_RSS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.14217e+08,937067,35947.5,4084.77,269.012,52.5148,5.92794,1.98664],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 37,
    label = "R4H_SSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.14217e+08,937067,35947.5,4084.77,269.012,52.5148,5.92794,1.98664],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "R4H_SSS_OOCsCs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([54765,2908.72,496.024,151.763,34.2234,13.8963,4.11069,2.20722],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 39,
    label = "R4H_SSS_OO(Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([74648.8,3793.08,628.866,188.626,41.415,16.5225,4.75764,2.51362],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S} {7,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([36785.1,2190.83,398.894,127.221,30.1032,12.541,3.81261,2.06417],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "R4H_DSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
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
    label = "R4H_TSS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
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
    label = "R4H_BSS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
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
    label = "R4H_RSD",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
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
    index = 45,
    label = "R4H_SSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
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
    index = 46,
    label = "R4H_DSD",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
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
    index = 47,
    label = "R4H_TSD",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
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
    index = 48,
    label = "R4H_BSD",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
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
    index = 49,
    label = "R4H_RST",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
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
    index = 50,
    label = "R4H_SST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
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
    index = 51,
    label = "R4H_DST",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
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
    index = 52,
    label = "R4H_TST",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
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
    index = 53,
    label = "R4H_BST",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
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
    index = 54,
    label = "R4H_RSB",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
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
    index = 55,
    label = "R4H_SSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
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
    index = 56,
    label = "R4H_DSB",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
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
    index = 57,
    label = "R4H_TSB",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
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
    index = 58,
    label = "R4H_BSB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
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
    index = 59,
    label = "R4H_SMS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3  *5 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2238.79,199.249,47.9842,18.9198,6.10902,3.18769,1.42103,0.994171],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 60,
    label = "R4H_SDS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *5 Cd 0 {2,D} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2238.79,199.249,47.9842,18.9198,6.10902,3.18769,1.42103,0.994171],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 61,
    label = "R4H_STS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Ct 0 {1,S} {3,T}
3  *5 Ct 0 {2,T} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
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
    index = 62,
    label = "R4H_SBS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3  *5 Cb 0 {2,B} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
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
    index = 63,
    label = "R4H_SBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3  *5 Cbf 0 {2,B} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
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
    index = 64,
    label = "R4H_BBS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3  *5 Cb 0 {2,B} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
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
    index = 65,
    label = "R4H_BBB",
    group = 
"""
1  *1 Cb 1 {2,B} {15,B}
2  *4 Cbf 0 {1,B} {3,B} {12,B}
3  *5 Cbf 0 {2,B} {4,B} {9,B}
4  *2 Cb 0 {3,B} {5,S} {6,B}
5  *3 H 0 {4,S}
6     {Cb,Cbf} 0 {4,B} {7,B}
7     {Cb,Cbf} 0 {6,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     Cbf 0 {3,B} {8,B} {10,B}
10    {Cb,Cbf} 0 {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    Cbf 0 {2,B} {11,B} {13,B}
13    {Cb,Cbf} 0 {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {1,B} {14,B}
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
    index = 66,
    label = "R5H",
    group = "OR{R5H_RSSR, R5H_RSMS, R5H_SMSR, R5H_BBSR, R5H_RSBB, R5H_SBBS, R5H_SBBB, R5H_BBBS, R5H_BBBB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.12553e+11,2.30581e+08,2.57914e+06,129044,3055.68,323.573,16.2299,3.6383],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 67,
    label = "R5H_RSSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.56623e+11,2.95247e+08,3.1808e+06,154583,3504.09,359.253,17.0342,3.6746],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 68,
    label = "R5H_SSSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.56623e+11,2.95247e+08,3.1808e+06,154583,3504.09,359.253,17.0342,3.6746],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 69,
    label = "R5H_SSSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.39879e+11,2.91669e+08,3.17162e+06,154920,3526.91,361.912,17.118,3.67753],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 70,
    label = "R5H_SSSS_OOCCC",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.861e+11,4.97113e+08,6.04903e+06,322297,8355.35,943.699,52.7122,12.684],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 71,
    label = "R5H_SSSS_OO(Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.73929e+12,1.06568e+09,1.24918e+07,641298,15528.8,1652.83,82.0067,18.031],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 72,
    label = "R5H_SSSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S} {8,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
8     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.95621e+09,4.70179e+06,127131,11513.9,577.505,96.6575,9.06938,2.81579],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 73,
    label = "R5H_SSSS_OOCs(Cs/Cs)",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S} {7,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.29993e+09,1.60418e+07,414281,36578.7,1793.85,298.541,28.2702,8.93431],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 74,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs)",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S} {7,S} {8,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {4,S}
8     Cs 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.41985e+10,3.15851e+07,819823,72520.5,3555.17,590.194,55.4327,17.3805],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 75,
    label = "R5H_SSSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.04638e+12,3.79864e+08,3.37667e+06,147784,3064.14,308.472,15.3924,3.61439],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 76,
    label = "R5H_SSST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
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
    index = 77,
    label = "R5H_SSSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 78,
    label = "R5H_DSSR",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
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
    index = 79,
    label = "R5H_DSSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 80,
    label = "R5H_DSSD",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
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
    index = 81,
    label = "R5H_DSST",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
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
    index = 82,
    label = "R5H_DSSB",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 83,
    label = "R5H_TSSR",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
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
    index = 84,
    label = "R5H_TSSS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 85,
    label = "R5H_TSSD",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
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
    index = 86,
    label = "R5H_TSST",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
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
    index = 87,
    label = "R5H_TSSB",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 88,
    label = "R5H_BSSR",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
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
    index = 89,
    label = "R5H_BSSS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 90,
    label = "R5H_BSSD",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
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
    index = 91,
    label = "R5H_BSST",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
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
    index = 92,
    label = "R5H_BSSB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 93,
    label = "R5H_RSMS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.86828e+17,6.66514e+12,9.70148e+09,1.28717e+08,614157,26104.6,429.898,59.8986],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 94,
    label = "R5H_SSMS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 95,
    label = "R5H_DSMS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.86828e+17,6.66514e+12,9.70148e+09,1.28717e+08,614157,26104.6,429.898,59.8986],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 96,
    label = "R5H_TSMS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 97,
    label = "R5H_BSMS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 98,
    label = "R5H_SMSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5814.19,224.42,33.1728,9.52944,2.10355,0.885239,0.304678,0.191476],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 99,
    label = "R5H_SMSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 100,
    label = "R5H_SMSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5814.19,224.42,33.1728,9.52944,2.10355,0.885239,0.304678,0.191476],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 101,
    label = "R5H_SMST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
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
    index = 102,
    label = "R5H_SMSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 103,
    label = "R5H_BBSR",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
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
    index = 104,
    label = "R5H_BBSS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 105,
    label = "R5H_BBSD",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
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
    index = 106,
    label = "R5H_BBST",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
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
    index = 107,
    label = "R5H_BBSB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 108,
    label = "R5H_RSBB",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 109,
    label = "R5H_SSBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 110,
    label = "R5H_DSBB",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 111,
    label = "R5H_TSBB",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 112,
    label = "R5H_BSBB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
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
    index = 113,
    label = "R5H_SBBS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4  *5 Cb 0 {3,B} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
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
    index = 114,
    label = "R5H_SBBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B} {16,B}
3     Cbf 0 {2,B} {4,B} {13,B}
4  *5 Cbf 0 {3,B} {5,B} {10,B}
5  *2 Cb 0 {4,B} {6,S} {7,B}
6  *3 H 0 {5,S}
7     {Cb,Cbf} 0 {5,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf 0 {4,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf 0 {3,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    {Cb,Cbf} 0 {2,B} {15,B}
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
    index = 115,
    label = "R5H_BBBS",
    group = 
"""
1  *1 Cb 1 {2,B} {16,B}
2  *4 Cbf 0 {1,B} {3,B} {13,B}
3     Cbf 0 {2,B} {4,B} {10,B}
4  *5 Cb 0 {3,B} {5,S} {7,B}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     {Cb,Cbf} 0 {4,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf 0 {3,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf 0 {2,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    {Cb,Cbf} 0 {1,B} {15,B}
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
    index = 116,
    label = "R5H_BBBB",
    group = 
"""
1  *1 Cb 1 {2,B} {19,B}
2  *4 Cbf 0 {1,B} {3,B} {16,B}
3     Cbf 0 {2,B} {4,B} {13,B}
4  *5 Cbf 0 {3,B} {5,B} {10,B}
5  *2 Cb 0 {4,B} {6,S} {7,B}
6  *3 H 0 {5,S}
7     {Cb,Cbf} 0 {5,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf 0 {4,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf 0 {3,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    Cbf 0 {2,B} {15,B} {17,B}
17    {Cb,Cbf} 0 {16,B} {18,B}
18    {Cb,Cbf} 0 {17,B} {19,B}
19    {Cb,Cbf} 0 {1,B} {18,B}
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
    index = 117,
    label = "R6H",
    group = "OR{R6H_RSSSR, R6H_RSSMS, R6H_RSMSR, R6H_SMSSR, R6H_SMSMS, R6H_BBSRS, R6H_BBSSM, R6H_BBSBB, R6H_SBBSR, R6H_RSBBS, R6H_BBBSR, R6H_SBBBS, R6H_RSBBB, R6H_SBBBB, R6H_BBBBS, R6H_BBBBB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 118,
    label = "R6H_RSSSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 119,
    label = "R6H_SSSSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 120,
    label = "R6H_SSSSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 121,
    label = "R6H_SSSSS_OO",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.53812e+12,3.49201e+08,2.34953e+06,85582,1415.78,124.859,5.25731,1.13998],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 122,
    label = "R6H_SSSSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
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
    index = 123,
    label = "R6H_SSSST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
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
    index = 124,
    label = "R6H_SSSSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 125,
    label = "R6H_DSSSR",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 126,
    label = "R6H_DSSSS",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 127,
    label = "R6H_DSSSD",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
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
    index = 128,
    label = "R6H_DSSST",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
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
    index = 129,
    label = "R6H_DSSSB",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 130,
    label = "R6H_TSSSR",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 131,
    label = "R6H_TSSSS",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 132,
    label = "R6H_TSSSD",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
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
    index = 133,
    label = "R6H_TSSST",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
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
    index = 134,
    label = "R6H_TSSSB",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 135,
    label = "R6H_BSSSR",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 136,
    label = "R6H_BSSSS",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 137,
    label = "R6H_BSSSD",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
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
    index = 138,
    label = "R6H_BSSST",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
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
    index = 139,
    label = "R6H_BSSSB",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 140,
    label = "R6H_RSSMS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,{D,T,B}}
5  *5 R!H 0 {4,{D,T,B}} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 141,
    label = "R6H_RSMSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4     R!H 0 {3,{D,T,B}} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 142,
    label = "R6H_SMSSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 143,
    label = "R6H_SMSMS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4     R!H 0 {3,S} {5,{D,T,B}}
5  *5 R!H 0 {4,{D,T,B}} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 144,
    label = "R6H_BBSRS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4     R!H 0 {3,S} {5,{S,D,T,B}}
5  *5 R!H 0 {4,{S,D,T,B}} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 145,
    label = "R6H_BBSSM",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{D,T,B}}
6  *2 R!H 0 {5,{D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 146,
    label = "R6H_BBSBB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4     Cb 0 {3,S} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 147,
    label = "R6H_SBBSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cb 0 {3,B} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 148,
    label = "R6H_RSBBS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     Cb 0 {2,S} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cb 0 {4,B} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 149,
    label = "R6H_BBBSR",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cb 0 {3,B} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
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
    index = 150,
    label = "R6H_SBBBS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cb 0 {4,B} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 151,
    label = "R6H_RSBBB",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     Cb 0 {2,S} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 152,
    label = "R6H_SBBBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 153,
    label = "R6H_BBBBS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cb 0 {4,B} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
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
    index = 154,
    label = "R6H_BBBBB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
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
    index = 155,
    label = "R7H",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3     R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.79802e+09,1.85789e+06,22872.6,1213.9,30.6695,3.35131,0.172505,0.0386849],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 156,
    label = "R7H_OOCs4",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.14659e+11,9.00437e+07,575997,19967.7,301.881,24.6292,0.888419,0.171306],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 157,
    label = "O_rad_out",
    group = 
"""
1  *1 O 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.73852,5.58191,3.99931,3.20335,2.42883,2.05826,1.65243,1.48189],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 158,
    label = "Cd_rad_out_double",
    group = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([70.538,27.1027,15.2911,10.4513,6.50698,4.90431,3.37504,2.80712],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 159,
    label = "Cd_rad_out_single",
    group = 
"""
1  *1 Cd 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([124.506,43.5597,23.2041,15.2516,9.02962,6.59518,4.34119,3.52404],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 160,
    label = "Cd_rad_out_singleH",
    group = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3078.61,473.668,153.919,72.7003,28.4318,16.1701,7.60241,5.20366],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 161,
    label = "Cd_rad_out_singleNd",
    group = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([69.088,29.3126,17.5422,12.4661,8.14346,6.31388,4.50698,3.81435],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 162,
    label = "Cd_rad_out_singleDe",
    group = 
"""
1  *1 Cd 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.16771e-06,3.63589e-05,0.000287786,0.00114736,0.00650781,0.0185426,0.0758252,0.15482],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 163,
    label = "Ct_rad_out",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T}
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
    index = 164,
    label = "Cb_rad_out",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 {Cb,Cbf} 0 {1,B}
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
    index = 165,
    label = "CO_rad_out",
    group = 
"""
1  *1 C 1 {2,D}
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "C_rad_out_single",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.328103,0.427434,0.500824,0.556541,0.634813,0.686808,0.76245,0.803032],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 167,
    label = "C_rad_out_2H",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.835,2.90572,2.45697,2.19517,1.90395,1.74591,1.55122,1.45908],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 168,
    label = "C_rad_out_1H",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0369305,0.0849599,0.139089,0.192313,0.285979,0.36034,0.483173,0.553],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 169,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.105936,0.184194,0.255054,0.315518,0.408528,0.473979,0.569988,0.618362],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 170,
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.65239e-06,7.69895e-05,0.000574058,0.00217379,0.0113226,0.0301185,0.108228,0.20111],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 172,
    label = "C_rad_out_noH",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.310057,0.399718,0.469389,0.525337,0.610687,0.673968,0.782361,0.854732],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 173,
    label = "C_rad_out_NonDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.538708,0.598649,0.643705,0.679779,0.735746,0.778694,0.856665,0.912632],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 174,
    label = "C_rad_out_Cs2",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.538708,0.598649,0.643705,0.679779,0.735746,0.778694,0.856665,0.912632],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 175,
    label = "C_rad_out_Cs2_cy3",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([84.8371,29.2995,15.2905,9.82972,5.57568,3.91876,2.38456,1.8216],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 176,
    label = "C_rad_out_Cs2_cy4",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.220396,0.256499,0.280143,0.296545,0.317337,0.329568,0.344515,0.350563],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 177,
    label = "C_rad_out_Cs2_cy5",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0828613,0.195662,0.329461,0.46802,0.730606,0.959706,1.39705,1.70133],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 178,
    label = "Others-C_rad_out_Cs2",
    group = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.422464,0.488182,0.539519,0.581803,0.649441,0.702988,0.803728,0.878731],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 179,
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "C_rad_out_OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.08944e-06,4.10869e-05,0.000357611,0.00149889,0.00883878,0.0252682,0.0994462,0.192613],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 181,
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.08944e-06,4.10869e-05,0.000357611,0.00149889,0.00883878,0.0252682,0.0994462,0.192613],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 182,
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "CO_H_out",
    group = 
"""
1  *2 CO 0 {2,S}
2  *3 H 0 {1,S}
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
    index = 185,
    label = "O_H_out",
    group = 
"""
1  *2 O 0 {2,S}
2  *3 H 0 {1,S}
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
    index = 186,
    label = "Ct_H_out",
    group = 
"""
1  *2 Ct 0 {2,S}
2  *3 H 0 {1,S}
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
    index = 187,
    label = "Cb_H_out",
    group = 
"""
1  *2 Cb 0 {2,S}
2  *3 H 0 {1,S}
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
    index = 188,
    label = "Cd_H_out_double",
    group = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     {Cd,O} 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.90825e-09,3.84739e-07,7.33957e-06,5.30122e-05,0.000640808,0.00290886,0.0226941,0.0652761],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 189,
    label = "Cd_H_out_doubleC",
    group = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.90825e-09,3.84739e-07,7.33957e-06,5.30122e-05,0.000640808,0.00290886,0.0226941,0.0652761],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 190,
    label = "Cd_H_out_doubleO",
    group = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     O 0 {1,D}
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
    index = 191,
    label = "Cd_H_out_single",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.20069e-11,1.40926e-08,6.82109e-07,9.0732e-06,0.000231115,0.00161611,0.0217172,0.0799197],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 192,
    label = "Cd_H_out_singleH",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.81125e-10,1.5436e-07,4.42587e-06,4.16459e-05,0.000691795,0.00375948,0.0364365,0.114717],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 193,
    label = "Cd_H_out_singleNd",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.18281e-12,8.96871e-09,5.53445e-07,8.59623e-06,0.000262543,0.00202594,0.0303648,0.11597],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 194,
    label = "Cd_H_out_singleDe",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.53956e-20,2.10879e-15,1.37074e-12,1.04875e-10,2.45672e-08,6.68151e-07,5.81714e-05,0.000570152],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 195,
    label = "Cs_H_out",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.71032,3.15909,2.48436,2.11583,1.72987,1.53206,1.30142,1.19829],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 196,
    label = "Cs_H_out_2H",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.268488,0.406636,0.526277,0.62869,0.793424,0.920421,1.14331,1.29331],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 197,
    label = "Cs_H_out_1H",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.32963,2.18443,1.69988,1.44018,1.17354,1.04007,0.889418,0.825409],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 198,
    label = "Cs_H_out_H/NonDeC",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.0429,0.950815,0.901731,0.871849,0.838325,0.820852,0.80233,0.796517],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 199,
    label = "Cs_H_out_H/(NonDeC/Cs)",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.367142,0.702751,1.04311,1.3622,1.91385,2.3597,3.156,3.68319],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 200,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs)",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S} {6,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
6     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.458274,0.840015,1.21161,1.54951,2.11411,2.55426,3.30595,3.77827],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 201,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs/Cs)",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S} {6,S} {7,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.523111,0.919707,1.29574,1.63299,2.19149,2.62559,3.37132,3.84745],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 202,
    label = "Cs_H_out_H/NonDeO",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([283.109,60.239,24.335,13.4951,6.62918,4.42415,2.70495,2.19513],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 203,
    label = "Cs_H_out_H/OneDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([255573,7896.1,986.92,247.822,44.4047,15.9343,4.12219,2.12056],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 204,
    label = "Cs_H_out_noH",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([33.7072,15.0159,9.1609,6.55039,4.26141,3.26299,2.24224,1.83081],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 205,
    label = "Cs_H_out_NonDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([21.1848,10.881,7.23916,5.4886,3.84763,3.08505,2.26025,1.90958],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 206,
    label = "Cs_H_out_Cs2",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([15.6379,8.62494,5.98609,4.66699,3.38604,2.7703,2.08305,1.78157],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 207,
    label = "Cs_H_out_Cs2_cy3",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([11364.6,960.83,221.155,83.8006,25.3099,12.5059,5.02642,3.25893],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 208,
    label = "Cs_H_out_Cs2_cy4",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([25.8703,11.1077,6.74153,4.85809,3.25589,2.58127,1.92634,1.68642],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 209,
    label = "Cs_H_out_Cs2_cy5",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([283.159,57.5767,22.2412,11.8326,5.40539,3.39357,1.84216,1.3677],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 210,
    label = "Others-Cs_H_out_Cs2",
    group = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.04501,3.96363,3.38213,3.01471,2.56843,2.30081,1.92869,1.72505],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 211,
    label = "Cs_H_out_NDMustO",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([10221.1,1231.9,346.515,148.874,51.8545,27.5719,11.9064,7.83933],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 212,
    label = "Cs_H_out_OneDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.93907e+06,38246.4,3567.14,725.513,97.1522,28.5935,5.40124,2.28237],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 213,
    label = "Cs_H_out_TwoDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
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
L1: RnH
    L2: R2H
        L3: R2H_S
            L4: R2H_S_cy3
            L4: R2H_S_cy4
            L4: R2H_S_cy5
            L4: Others-R2H_S
        L3: R2H_D
        L3: R2H_B
    L2: R3H
        L3: R3H_SR
            L4: R3H_SS
                L5: R3H_SS_12cy3
                L5: R3H_SS_23cy3
                L5: R3H_SS_12cy4
                L5: R3H_SS_23cy4
                L5: R3H_SS_13cy4
                L5: R3H_SS_12cy5
                L5: R3H_SS_23cy5
                L5: R3H_SS_13cy5
                L5: R3H_SS_2Cd
                L5: R3H_SS_OC
                L5: Others-R3H_SS
            L4: R3H_SD
            L4: R3H_ST
            L4: R3H_SB
        L3: R3H_MS
            L4: R3H_DS
            L4: R3H_TS
            L4: R3H_BS
        L3: R3H_BB
    L2: R4H
        L3: R4H_RSR
            L4: R4H_RSS
                L5: R4H_SSS
                    L6: R4H_SSS_OOCsCs
                        L7: R4H_SSS_OO(Cs/Cs)Cs
                            L8: R4H_SSS_OO(Cs/Cs/Cs)Cs
                L5: R4H_DSS
                L5: R4H_TSS
                L5: R4H_BSS
            L4: R4H_RSD
                L5: R4H_SSD
                L5: R4H_DSD
                L5: R4H_TSD
                L5: R4H_BSD
            L4: R4H_RST
                L5: R4H_SST
                L5: R4H_DST
                L5: R4H_TST
                L5: R4H_BST
            L4: R4H_RSB
                L5: R4H_SSB
                L5: R4H_DSB
                L5: R4H_TSB
                L5: R4H_BSB
        L3: R4H_SMS
            L4: R4H_SDS
            L4: R4H_STS
            L4: R4H_SBS
        L3: R4H_SBB
        L3: R4H_BBS
        L3: R4H_BBB
    L2: R5H
        L3: R5H_RSSR
            L4: R5H_SSSR
                L5: R5H_SSSS
                    L6: R5H_SSSS_OOCCC
                        L7: R5H_SSSS_OO(Cs/Cs)Cs
                            L8: R5H_SSSS_OO(Cs/Cs/Cs)Cs
                        L7: R5H_SSSS_OOCs(Cs/Cs)
                            L8: R5H_SSSS_OOCs(Cs/Cs/Cs)
                L5: R5H_SSSD
                L5: R5H_SSST
                L5: R5H_SSSB
            L4: R5H_DSSR
                L5: R5H_DSSS
                L5: R5H_DSSD
                L5: R5H_DSST
                L5: R5H_DSSB
            L4: R5H_TSSR
                L5: R5H_TSSS
                L5: R5H_TSSD
                L5: R5H_TSST
                L5: R5H_TSSB
            L4: R5H_BSSR
                L5: R5H_BSSS
                L5: R5H_BSSD
                L5: R5H_BSST
                L5: R5H_BSSB
        L3: R5H_RSMS
            L4: R5H_SSMS
            L4: R5H_DSMS
            L4: R5H_TSMS
            L4: R5H_BSMS
        L3: R5H_SMSR
            L4: R5H_SMSS
            L4: R5H_SMSD
            L4: R5H_SMST
            L4: R5H_SMSB
        L3: R5H_BBSR
            L4: R5H_BBSS
            L4: R5H_BBSD
            L4: R5H_BBST
            L4: R5H_BBSB
        L3: R5H_RSBB
            L4: R5H_SSBB
            L4: R5H_DSBB
            L4: R5H_TSBB
            L4: R5H_BSBB
        L3: R5H_SBBS
        L3: R5H_SBBB
        L3: R5H_BBBS
        L3: R5H_BBBB
    L2: R6H
        L3: R6H_RSSSR
            L4: R6H_SSSSR
                L5: R6H_SSSSS
                    L6: R6H_SSSSS_OO
                L5: R6H_SSSSD
                L5: R6H_SSSST
                L5: R6H_SSSSB
            L4: R6H_DSSSR
                L5: R6H_DSSSS
                L5: R6H_DSSSD
                L5: R6H_DSSST
                L5: R6H_DSSSB
            L4: R6H_TSSSR
                L5: R6H_TSSSS
                L5: R6H_TSSSD
                L5: R6H_TSSST
                L5: R6H_TSSSB
            L4: R6H_BSSSR
                L5: R6H_BSSSS
                L5: R6H_BSSSD
                L5: R6H_BSSST
                L5: R6H_BSSSB
        L3: R6H_RSSMS
        L3: R6H_RSMSR
        L3: R6H_SMSSR
        L3: R6H_SMSMS
        L3: R6H_BBSRS
        L3: R6H_BBSSM
        L3: R6H_BBSBB
        L3: R6H_SBBSR
        L3: R6H_RSBBS
        L3: R6H_BBBSR
        L3: R6H_SBBBS
        L3: R6H_RSBBB
        L3: R6H_SBBBB
        L3: R6H_BBBBS
        L3: R6H_BBBBB
    L2: R7H
        L3: R7H_OOCs4
L1: Y_rad_out
    L2: O_rad_out
    L2: Cd_rad_out_double
    L2: Cd_rad_out_single
        L3: Cd_rad_out_singleH
        L3: Cd_rad_out_singleNd
        L3: Cd_rad_out_singleDe
    L2: Ct_rad_out
    L2: Cb_rad_out
    L2: CO_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                    L6: C_rad_out_Cs2_cy3
                    L6: C_rad_out_Cs2_cy4
                    L6: C_rad_out_Cs2_cy5
                    L6: Others-C_rad_out_Cs2
                L5: C_rad_out_NDMustO
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
            L4: C_rad_out_TwoDe
L1: XH_out
    L2: CO_H_out
    L2: O_H_out
    L2: Ct_H_out
    L2: Cb_H_out
    L2: Cd_H_out_double
        L3: Cd_H_out_doubleC
        L3: Cd_H_out_doubleO
    L2: Cd_H_out_single
        L3: Cd_H_out_singleH
        L3: Cd_H_out_singleNd
        L3: Cd_H_out_singleDe
    L2: Cs_H_out
        L3: Cs_H_out_2H
        L3: Cs_H_out_1H
            L4: Cs_H_out_H/NonDeC
                L5: Cs_H_out_H/(NonDeC/Cs)
                    L6: Cs_H_out_H/(NonDeC/Cs/Cs)
                        L7: Cs_H_out_H/(NonDeC/Cs/Cs/Cs)
            L4: Cs_H_out_H/NonDeO
            L4: Cs_H_out_H/OneDe
        L3: Cs_H_out_noH
            L4: Cs_H_out_NonDe
                L5: Cs_H_out_Cs2
                    L6: Cs_H_out_Cs2_cy3
                    L6: Cs_H_out_Cs2_cy4
                    L6: Cs_H_out_Cs2_cy5
                    L6: Others-Cs_H_out_Cs2
                L5: Cs_H_out_NDMustO
            L4: Cs_H_out_OneDe
            L4: Cs_H_out_TwoDe
"""
)

