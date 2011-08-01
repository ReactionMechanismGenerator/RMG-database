#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["CO_birad", "RR'"], products=["R_CO_R'"], ownReverse=False)

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['LOSE_RADICAL', '*1', '2'],
])

entry(
    index = 1,
    label = "CO_birad",
    group = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.00287e-55,3.04218e-40,4.41121e-31,6.12312e-25,3.36544e-17,1.67315e-12,3.95881e-06,0.00746027],"m^3/(mol*s)","*|/",[2.15844,1.02477,1.55285,2.14148,3.26772,4.28562,6.38818,8.03376])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 8 rates.
[<Entry index=1 label="CO_birad">, <Entry index=21 label="C/H2/NonDeC">]
[<Entry index=1 label="CO_birad">, <Entry index=17 label="C_pri/NonDeC">]
[<Entry index=1 label="CO_birad">, <Entry index=31 label="C/H/Cs3">]
[<Entry index=1 label="CO_birad">, <Entry index=15 label="C_methane">]
[<Entry index=1 label="CO_birad">, <Entry index=42 label="C_methyl_C_methyl">]
[<Entry index=1 label="CO_birad">, <Entry index=2 label="RR'">]
[<Entry index=1 label="CO_birad">, <Entry index=6 label="CsO_H">]
[<Entry index=1 label="CO_birad">, <Entry index=4 label="H2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "RR'",
    group = "OR{R_H, R_R'}",
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
    label = "R_H",
    group = 
"""
1  *2 {H,Cs,Cd,Cb,O,Sis,Sid} 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([496.185,111.117,45.0811,24.6358,11.5166,7.2663,3.89626,2.83256],"m^3/(mol*s)","*|/",[1,1,1,1,1,1,1,1])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=1 label="CO_birad">, <Entry index=21 label="C/H2/NonDeC">]
[<Entry index=1 label="CO_birad">, <Entry index=17 label="C_pri/NonDeC">]
[<Entry index=1 label="CO_birad">, <Entry index=4 label="H2">]
[<Entry index=1 label="CO_birad">, <Entry index=15 label="C_methane">]
[<Entry index=1 label="CO_birad">, <Entry index=6 label="CsO_H">]
[<Entry index=1 label="CO_birad">, <Entry index=31 label="C/H/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "H2",
    group = 
"""
1  *2 H 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([16.7558,13.7942,11.5351,9.82447,7.46857,5.95388,3.85381,2.79291],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=4 label="H2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "RO_H",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.24621e+18,1.24253e+13,1.32522e+10,1.44556e+08,551098,20830.3,304.365,41.1219],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=6 label="CsO_H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "CsO_H",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.24621e+18,1.24253e+13,1.32522e+10,1.44556e+08,551098,20830.3,304.365,41.1219],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=6 label="CsO_H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "Cd_H",
    group = 
"""
1  *2 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *3 H 0 {1,S}
4     R 0 {1,S}
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
    index = 8,
    label = "Cd_pri",
    group = 
"""
1  *2 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *3 H 0 {1,S}
4     H 0 {1,S}
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
    label = "Cd_sec",
    group = 
"""
1  *2 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *3 H 0 {1,S}
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
    index = 10,
    label = "Cd/H/NonDeC",
    group = 
"""
1  *2 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *3 H 0 {1,S}
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
    index = 11,
    label = "Cd/H/NonDeO",
    group = 
"""
1  *2 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *3 H 0 {1,S}
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
    index = 12,
    label = "Cd/H/OneDe",
    group = 
"""
1  *2 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *3 H 0 {1,S}
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
    index = 13,
    label = "Cb_H",
    group = 
"""
1  *2 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *3 H 0 {1,S}
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
    label = "Cs_H",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
5     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.163503,0.323719,0.484078,0.629888,0.8677,1.04375,1.31417,1.45625],"m^3/(mol*s)","*|/",[1,1,1,1,1,1,1,1])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=1 label="CO_birad">, <Entry index=17 label="C_pri/NonDeC">]
[<Entry index=1 label="CO_birad">, <Entry index=21 label="C/H2/NonDeC">]
[<Entry index=1 label="CO_birad">, <Entry index=31 label="C/H/Cs3">]
[<Entry index=1 label="CO_birad">, <Entry index=15 label="C_methane">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "C_methane",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000492598,0.00494995,0.0202386,0.0525715,0.178306,0.379952,1.09609,1.93752],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=15 label="C_methane">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "C_pri",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00437545,0.0222296,0.0593676,0.114816,0.26406,0.438323,0.87461,1.25023],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=17 label="C_pri/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "C_pri/NonDeC",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00437545,0.0222296,0.0593676,0.114816,0.26406,0.438323,0.87461,1.25023],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=17 label="C_pri/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "C_pri/NonDeO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {1,S}
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
    label = "C_pri/De",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C_sec",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.674259,0.752081,0.790141,0.807855,0.814821,0.805891,0.767175,0.728447],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=21 label="C/H2/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "C/H2/NonDeC",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.674259,0.752081,0.790141,0.807855,0.814821,0.805891,0.767175,0.728447],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=21 label="C/H2/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "C/H2/NonDeO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H2/CsO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
5     Cs 0 {1,S}
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
    label = "C/H2/O2",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
5     O 0 {1,S}
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
    label = "C/H2/OneDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H2/OneDeC",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
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
    label = "C/H2/OneDeO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     O 0 {1,S}
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
    label = "C/H2/TwoDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cd,Ct,CO,Cb} 0 {1,S}
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
    label = "C_ter",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([491.773,132.701,57.8396,32.2826,14.7757,8.84271,4.05552,2.54866],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=31 label="C/H/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "C/H/NonDeC",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([491.773,132.701,57.8396,32.2826,14.7757,8.84271,4.05552,2.54866],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=31 label="C/H/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C/H/Cs3",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([491.773,132.701,57.8396,32.2826,14.7757,8.84271,4.05552,2.54866],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=31 label="C/H/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C/H/NDMustO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H/OneDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H/Cs2",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
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
    label = "C/H/ODMustO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H/TwoDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H/Cs",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Cs 0 {1,S}
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
    label = "C/H/TDMustO",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     O 0 {1,S}
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
    label = "C/H/ThreeDe",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "R_R'",
    group = 
"""
1  *2 {Cs,Sis} 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,Cb,Sis,Sid} 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.83318e-17,5.16934e-13,1.94933e-10,1.04866e-08,1.61227e-06,3.46156e-05,0.00227636,0.0199264],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=42 label="C_methyl_C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "Cs_Cs",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.83318e-17,5.16934e-13,1.94933e-10,1.04866e-08,1.61227e-06,3.46156e-05,0.00227636,0.0199264],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=42 label="C_methyl_C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "C_methyl_C_methyl",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.83318e-17,5.16934e-13,1.94933e-10,1.04866e-08,1.61227e-06,3.46156e-05,0.00227636,0.0199264],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=1 label="CO_birad">, <Entry index=42 label="C_methyl_C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:07 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 43,
    label = "C_methyl_C_pri",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     C 0 {2,S}
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
    label = "C_methyl_C_sec",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     C 0 {2,S}
8     C 0 {2,S}
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
    label = "C_methyl_C_ter",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     C 0 {2,S}
7     C 0 {2,S}
8     C 0 {2,S}
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
    label = "Cs_Cd",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
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
    label = "C_methyl_Cd_pri",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 0 {1,S} {6,S} {7,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     C 0 {2,D}
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
    label = "C_methyl_Cd_sec",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 0 {1,S} {6,S} {7,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     C 0 {2,S}
7     C 0 {2,D}
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
    label = "Cs_Cb",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cb 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
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
L1: CO_birad
L1: RR'
    L2: R_H
        L3: H2
        L3: RO_H
            L4: CsO_H
        L3: Cd_H
            L4: Cd_pri
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/OneDe
        L3: Cb_H
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C_pri/NonDeC
                L5: C_pri/NonDeO
                L5: C_pri/De
            L4: C_sec
                L5: C/H2/NonDeC
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                    L6: C/H2/O2
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                    L6: C/H2/OneDeO
                L5: C/H2/TwoDe
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                    L6: C/H/NDMustO
                L5: C/H/OneDe
                    L6: C/H/Cs2
                    L6: C/H/ODMustO
                L5: C/H/TwoDe
                    L6: C/H/Cs
                    L6: C/H/TDMustO
                L5: C/H/ThreeDe
    L2: R_R'
        L3: Cs_Cs
            L4: C_methyl_C_methyl
            L4: C_methyl_C_pri
            L4: C_methyl_C_sec
            L4: C_methyl_C_ter
        L3: Cs_Cd
            L4: C_methyl_Cd_pri
            L4: C_methyl_Cd_sec
        L3: Cs_Cb
"""
)

