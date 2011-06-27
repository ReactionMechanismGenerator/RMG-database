#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination"
shortDesc = ""
longDesc = """

"""

template(reactants=["Y_rad", "Y_rad"], products=["Y_Y"], ownReverse=False)

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_rad",
    group = 
"""
1  *  R 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.34854e+07,1.2883e+07,1.24039e+07,1.20107e+07,1.13945e+07,1.09251e+07,1.01006e+07,9.54248e+06],"m^3/(mol*s)","*|/",[13.3415,11.9479,11.8499,12.1271,12.9715,13.8584,15.8329,17.4759])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [68, 68, 68, 68, 68, 68, 68, 68] rates.
[<Entry index=11 label="Cd_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=2 label="H_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=22 label="C_methyl">, <Entry index=15 label="Cb_rad">]
[<Entry index=5 label="O_pri_rad">, <Entry index=6 label="O_sec_rad">]
[<Entry index=2 label="H_rad">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=2 label="H_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=5 label="O_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=5 label="O_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=9 label="O2_birad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=5 label="O_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=21 label="Cs_rad">]
[<Entry index=15 label="Cb_rad">, <Entry index=15 label="Cb_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=22 label="C_methyl">, <Entry index=30 label="C_sec_rad">]
[<Entry index=2 label="H_rad">, <Entry index=15 label="Cb_rad">]
[<Entry index=19 label="CO_rad/NonDe">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=22 label="C_methyl">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=23 label="C_pri_rad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=1 label="Y_rad">, <Entry index=2 label="H_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=23 label="C_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=11 label="Cd_pri_rad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=22 label="C_methyl">]
[<Entry index=22 label="C_methyl">, <Entry index=39 label="C_ter_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O2_birad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=1 label="Y_rad">, <Entry index=1 label="Y_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=9 label="O2_birad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=2 label="H_rad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=3 label="Ct_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=2 label="H_rad">]
[<Entry index=11 label="Cd_pri_rad">, <Entry index=3 label="Ct_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=7 label="O_rad/NonDe">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=9 label="O2_birad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=15 label="Cb_rad">]
[<Entry index=23 label="C_pri_rad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=5 label="O_pri_rad">, <Entry index=5 label="O_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=22 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "H_rad",
    group = 
"""
1  *  H 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.50275,2.58814,2.6749,2.75777,2.90882,3.04221,3.31943,3.54303],"m^3/(mol*s)","*|/",[1246.04,807.893,681.344,636.2,620.19,635.039,697.559,761.006])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [17, 17, 17, 17, 17, 17, 17, 17] rates.
[<Entry index=2 label="H_rad">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=2 label="H_rad">, <Entry index=5 label="O_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=2 label="H_rad">]
[<Entry index=2 label="H_rad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=3 label="Ct_rad">]
[<Entry index=1 label="Y_rad">, <Entry index=2 label="H_rad">]
[<Entry index=2 label="H_rad">, <Entry index=21 label="Cs_rad">]
[<Entry index=2 label="H_rad">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=2 label="H_rad">, <Entry index=15 label="Cb_rad">]
[<Entry index=2 label="H_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=2 label="H_rad">]
[<Entry index=2 label="H_rad">, <Entry index=22 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 3,
    label = "Ct_rad",
    group = 
"""
1  *  C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.25181,5.29261,5.34408,5.39669,5.49582,5.58422,5.76599,5.90889],"m^3/(mol*s)","*|/",[3984.63,6648.76,9212.65,11608,15937.8,19813.7,28401.1,36233.6])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=11 label="Cd_pri_rad">, <Entry index=3 label="Ct_rad">]
[<Entry index=2 label="H_rad">, <Entry index=3 label="Ct_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "O_rad",
    group = 
"""
1  *  O 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.978571,1.0365,1.08579,1.12887,1.20199,1.26312,1.38436,1.47868],"m^3/(mol*s)","*|/",[6.6402,7.22368,7.73962,8.20782,9.04437,9.78774,11.3905,12.7618])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=5 label="O_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=5 label="O_pri_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=7 label="O_rad/NonDe">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=5 label="O_pri_rad">, <Entry index=6 label="O_sec_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=5 label="O_pri_rad">]
[<Entry index=5 label="O_pri_rad">, <Entry index=5 label="O_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "O_pri_rad",
    group = 
"""
1  *  O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.63119,2.74343,2.83626,2.91575,3.04773,3.15558,3.36384,3.52137],"m^3/(mol*s)","*|/",[19.7343,20.9882,21.9471,22.7287,23.977,24.9753,26.9077,28.4098])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=5 label="O_pri_rad">]
[<Entry index=5 label="O_pri_rad">, <Entry index=5 label="O_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=5 label="O_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=5 label="O_pri_rad">]
[<Entry index=5 label="O_pri_rad">, <Entry index=6 label="O_sec_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "O_sec_rad",
    group = 
"""
1  *  O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.476861,0.50786,0.534575,0.558135,0.598516,0.632603,0.700982,0.754804],"m^3/(mol*s)","*|/",[3.91215,4.81096,5.696,6.56521,8.26117,9.91041,13.8837,17.7036])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=7 label="O_rad/NonDe">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=5 label="O_pri_rad">, <Entry index=6 label="O_sec_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "O_rad/NonDe",
    group = 
"""
1  *  O 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.412661,0.443411,0.470038,0.493627,0.534303,0.568878,0.638884,0.694569],"m^3/(mol*s)","*|/",[5.10793,6.62611,8.15925,9.70037,12.7982,15.9118,23.7482,31.6447])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=7 label="O_rad/NonDe">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=7 label="O_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "O_rad/OneDe",
    group = 
"""
1  *  O 1 {2,S}
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
    label = "O2_birad",
    group = 
"""
1  *  O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.183617,0.207416,0.226395,0.242314,0.268338,0.289422,0.330156,0.361284],"m^3/(mol*s)","*|/",[6.30612,6.76358,7.44337,8.16897,9.60159,10.9595,14.049,16.8218])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [10, 10, 10, 10, 10, 10, 10, 10] rates.
[<Entry index=9 label="O2_birad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=9 label="O2_birad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=23 label="C_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=2 label="H_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=15 label="Cb_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=22 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "Cd_rad",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.71043,2.93068,3.09345,3.22227,3.41978,3.56956,3.83791,4.02785],"m^3/(mol*s)","*|/",[3.63782,4.32478,5.00119,5.59028,6.53013,7.2425,8.47377,9.30274])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=11 label="Cd_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=11 label="Cd_pri_rad">, <Entry index=3 label="Ct_rad">]
[<Entry index=11 label="Cd_pri_rad">, <Entry index=11 label="Cd_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "Cd_pri_rad",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.71043,2.93068,3.09345,3.22227,3.41978,3.56956,3.83791,4.02785],"m^3/(mol*s)","*|/",[3.63782,4.32478,5.00119,5.59028,6.53013,7.2425,8.47377,9.30274])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=11 label="Cd_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=11 label="Cd_pri_rad">, <Entry index=3 label="Ct_rad">]
[<Entry index=11 label="Cd_pri_rad">, <Entry index=11 label="Cd_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Cd_sec_rad",
    group = 
"""
1  *  C 1 {2,D} {3,S}
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
    index = 13,
    label = "Cd_rad/NonDe",
    group = 
"""
1  *  C 1 {2,D} {3,S}
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
    index = 14,
    label = "Cd_rad/OneDe",
    group = 
"""
1  *  C 1 {2,D} {3,S}
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
    index = 15,
    label = "Cb_rad",
    group = 
"""
1  *  Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.851826,0.914364,0.964275,1.00614,1.07447,1.12963,1.23536,1.31519],"m^3/(mol*s)","*|/",[8.0929,8.13402,8.15604,8.17398,8.21417,8.26477,8.42446,8.60696])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=22 label="C_methyl">, <Entry index=15 label="Cb_rad">]
[<Entry index=15 label="Cb_rad">, <Entry index=15 label="Cb_rad">]
[<Entry index=2 label="H_rad">, <Entry index=15 label="Cb_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=15 label="Cb_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "CO_rad",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.10991,1.06082,1.0381,1.02696,1.01981,1.02113,1.03496,1.0516],"m^3/(mol*s)","*|/",[2.42165,2.49435,3.82112,5.41678,8.73571,11.8899,18.6108,23.951])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=11 label="Cd_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=19 label="CO_rad/NonDe">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=19 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "CO_pri_rad",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.15813,1.07526,1.04149,1.02816,1.02698,1.03932,1.08491,1.13225],"m^3/(mol*s)","*|/",[3.21959,3.4007,7.16018,12.7361,27.426,44.5377,88.755,129.482])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=11 label="Cd_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=17 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "CO_sec_rad",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.0677,1.05394,1.0446,1.03764,1.02763,1.02053,1.0087,1.00093],"m^3/(mol*s)","*|/",[2.19579,2.20147,2.29046,2.40756,2.66325,2.91806,3.51108,4.04457])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=19 label="CO_rad/NonDe">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=9 label="O2_birad">, <Entry index=19 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "CO_rad/NonDe",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.0677,1.05394,1.0446,1.03764,1.02763,1.02053,1.0087,1.00093],"m^3/(mol*s)","*|/",[2.19579,2.20147,2.29046,2.40756,2.66325,2.91806,3.51108,4.04457])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=17 label="CO_pri_rad">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=19 label="CO_rad/NonDe">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=9 label="O2_birad">, <Entry index=19 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "CO_rad/OneDe",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
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
    index = 21,
    label = "Cs_rad",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.10176,1.05441,1.01661,0.985497,0.936631,0.899307,0.833577,0.788958],"m^3/(mol*s)","*|/",[3.14512,3.20051,3.31696,3.45078,3.727,3.99637,4.62071,5.18461])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [56, 56, 56, 56, 56, 56, 56, 56] rates.
[<Entry index=22 label="C_methyl">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=22 label="C_methyl">, <Entry index=15 label="Cb_rad">]
[<Entry index=2 label="H_rad">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=22 label="C_methyl">, <Entry index=5 label="O_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=30 label="C_sec_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=5 label="O_pri_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=2 label="H_rad">, <Entry index=21 label="Cs_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O2_birad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=2 label="H_rad">, <Entry index=22 label="C_methyl">]
[<Entry index=2 label="H_rad">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=23 label="C_pri_rad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=9 label="O2_birad">, <Entry index=23 label="C_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=22 label="C_methyl">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=22 label="C_methyl">]
[<Entry index=22 label="C_methyl">, <Entry index=39 label="C_ter_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=9 label="O2_birad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=23 label="C_pri_rad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=22 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "C_methyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.00933,2.04222,2.05232,2.05252,2.04112,2.02456,1.98222,1.9456],"m^3/(mol*s)","*|/",[2.87914,2.77596,2.78073,2.82898,2.98474,3.17853,3.72473,4.29751])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [20, 20, 20, 20, 20, 20, 20, 20] rates.
[<Entry index=22 label="C_methyl">, <Entry index=11 label="Cd_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=30 label="C_sec_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=22 label="C_methyl">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=22 label="C_methyl">, <Entry index=39 label="C_ter_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=22 label="C_methyl">, <Entry index=15 label="Cb_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=22 label="C_methyl">]
[<Entry index=22 label="C_methyl">, <Entry index=22 label="C_methyl">]
[<Entry index=22 label="C_methyl">, <Entry index=5 label="O_pri_rad">]
[<Entry index=2 label="H_rad">, <Entry index=22 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "C_pri_rad",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.0946,1.07977,1.06995,1.06278,1.05269,1.04569,1.03433,1.02705],"m^3/(mol*s)","*|/",[3.0038,3.03667,3.08,3.12454,3.21033,3.29024,3.46836,3.62356])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=23 label="C_pri_rad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=5 label="O_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=2 label="H_rad">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=9 label="O2_birad">, <Entry index=23 label="C_pri_rad">]
[<Entry index=23 label="C_pri_rad">, <Entry index=30 label="C_sec_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "C_rad/H2/Cs",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.39525,1.4075,1.41818,1.42754,1.44326,1.45615,1.48081,1.49911],"m^3/(mol*s)","*|/",[3.34108,3.25449,3.20615,3.17544,3.14122,3.12683,3.13097,3.16065])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=22 label="C_methyl">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=5 label="O_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=24 label="C_rad/H2/Cs">]
[<Entry index=2 label="H_rad">, <Entry index=24 label="C_rad/H2/Cs">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "C_rad/H2/Cd",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
1  *  C 1 {2,S} {3,S} {4,S}
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
1  *  C 1 {2,S} {3,S} {4,S}
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
1  *  C 1 {2,S} {3,S} {4,S}
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
1  *  C 1 {2,S} {3,S} {4,S}
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
1  *  C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.797711,0.735925,0.692934,0.66047,0.613381,0.579858,0.524575,0.489123],"m^3/(mol*s)","*|/",[4.07886,4.34896,4.58337,4.78966,5.14158,5.43725,6.02865,6.49442])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=2 label="H_rad">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=22 label="C_methyl">, <Entry index=30 label="C_sec_rad">]
[<Entry index=9 label="O2_birad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=22 label="C_methyl">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=23 label="C_pri_rad">, <Entry index=30 label="C_sec_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=31 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C_rad/H/NonDeC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.855421,0.796279,0.754506,0.722631,0.675902,0.642288,0.586245,0.549915],"m^3/(mol*s)","*|/",[4.65434,4.89755,5.10149,5.27653,5.56714,5.80473,6.26545,6.61729])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=2 label="H_rad">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=22 label="C_methyl">, <Entry index=31 label="C_rad/H/NonDeC">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=31 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C_rad/H/NonDeO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 33,
    label = "C_rad/H/CsO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 34,
    label = "C_rad/H/O2",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 35,
    label = "C_rad/H/OneDe",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 36,
    label = "C_rad/H/OneDeC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 37,
    label = "C_rad/H/OneDeO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 38,
    label = "C_rad/H/TwoDe",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 39,
    label = "C_ter_rad",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.526136,0.464744,0.421344,0.388551,0.34146,0.308623,0.256445,0.224674],"m^3/(mol*s)","*|/",[5.46356,5.76352,6.33193,6.99183,8.38945,9.79472,13.1893,16.4011])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [11, 11, 11, 11, 11, 11, 11, 11] rates.
[<Entry index=23 label="C_pri_rad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
[<Entry index=9 label="O2_birad">, <Entry index=39 label="C_ter_rad">]
[<Entry index=22 label="C_methyl">, <Entry index=39 label="C_ter_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "C_rad/NonDeC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.542077,0.455879,0.398955,0.357937,0.301835,0.264574,0.208407,0.176027],"m^3/(mol*s)","*|/",[3.55068,4.37082,5.18863,5.97681,7.45848,8.83262,11.9311,14.7015])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=22 label="C_methyl">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "C_rad/Cs3",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.542077,0.455879,0.398955,0.357937,0.301835,0.264574,0.208407,0.176027],"m^3/(mol*s)","*|/",[3.55068,4.37082,5.18863,5.97681,7.45848,8.83262,11.9311,14.7015])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=22 label="C_methyl">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=7 label="O_rad/NonDe">]
[<Entry index=24 label="C_rad/H2/Cs">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=17 label="CO_pri_rad">]
[<Entry index=31 label="C_rad/H/NonDeC">, <Entry index=41 label="C_rad/Cs3">]
[<Entry index=41 label="C_rad/Cs3">, <Entry index=19 label="CO_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:17:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "C_rad/NDMustO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 43,
    label = "C_rad/OneDe",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 44,
    label = "C_rad/Cs2",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 45,
    label = "C_rad/ODMustO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 46,
    label = "C_rad/TwoDe",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 47,
    label = "C_rad/Cs",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 48,
    label = "C_rad/TDMustO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
    index = 49,
    label = "C_rad/ThreeDe",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
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
L1: Y_rad
    L2: H_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: O2_birad
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
        L3: C_sec_rad
            L4: C_rad/H/NonDeC
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
                L5: C_rad/Cs2
                L5: C_rad/ODMustO
            L4: C_rad/TwoDe
                L5: C_rad/Cs
                L5: C_rad/TDMustO
            L4: C_rad/ThreeDe
"""
)

forbidden(
    label = "O4",
    group = 
"""
1     O 1 {2,S}
2  *1 O 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4     O 1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

