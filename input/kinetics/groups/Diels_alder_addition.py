#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition"
shortDesc = ""
longDesc = """

"""

template(reactants=["ene", "diene_out"], products=["Six_Ring"], ownReverse=False)

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['CHANGE_BOND', '*4', '1', '*5'],
    ['CHANGE_BOND', '*5', '-1', '*6'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*6'],
])

entry(
    index = 1,
    label = "diene_out",
    group = "OR{diene_unsub_unsub_out, diene_unsub_monosub_out, diene_unsub_disub_out, diene_monosub_monosub_out, diene_monosub_disub_out, diene_disub_disub_out}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.42133e-15,2.03714e-10,8.12768e-08,4.40484e-06,0.000647716,0.0129377,0.701167,5.16182],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "diene_in",
    group = 
"""
1  *4 Cd 0 {2,S}
2  *5 Cd 0 {1,S}
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
    label = "ene",
    group = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cd 0 {1,D}
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
    label = "diene_unsub_unsub_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.728646,0.908743,1.03752,1.13335,1.26569,1.3524,1.47732,1.54404],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "diene_unsub_monosub_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     R!H 0 {4,S}
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
    label = "diene_unsub_monosubNd_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     {Cs,O} 0 {4,S}
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
    index = 7,
    label = "diene_unsub_monosubDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    index = 8,
    label = "diene_unsub_disub_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     R!H 0 {4,S}
8     R!H 0 {4,S}
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
    label = "diene_unsub_disubNd2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cs,O} 0 {4,S}
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
    label = "diene_unsub_disubNdDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    index = 11,
    label = "diene_unsub_disubDe2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_monosub_monosub_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     R!H 0 {1,S}
7     R!H 0 {4,S}
8     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.736755,0.73896,0.740287,0.741172,0.742281,0.742947,0.743835,0.74428],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "diene_monosubNd_monosubNd_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.736755,0.73896,0.740287,0.741172,0.742281,0.742947,0.743835,0.74428],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "diene_monosubNd_monosubDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {4,S}
8     H 0 {4,S}
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
    label = "diene_monosubDe_monosubDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {4,S}
8     H 0 {4,S}
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
    label = "diene_monosub_disub_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     R!H 0 {1,S}
7     R!H 0 {4,S}
8     R!H 0 {4,S}
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
    index = 17,
    label = "diene_monosubNd_disubNd2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cs,O} 0 {4,S}
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
    index = 18,
    label = "diene_monosubNd_disubNdDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_monosubNd_disubDe2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_monosubDe_disubNd2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cs,O} 0 {4,S}
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
    label = "diene_monosubDe_disubNdDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_monosubDe_disubDe2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_disub_disub_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     R!H 0 {1,S}
6     R!H 0 {1,S}
7     R!H 0 {4,S}
8     R!H 0 {4,S}
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
    label = "diene_disubNd2_disubNd2_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     {Cs,O} 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     {Cs,O} 0 {4,S}
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
    label = "diene_disubNd2_disubDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     {Cs,O} 0 {1,S}
6     {Cs,O} 0 {1,S}
7     R!H 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_disubDe_disubDe_out",
    group = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     R!H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     R!H 0 {4,S}
8     {Cd,Ct,Cb,CO} 0 {4,S}
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
    label = "diene_in_2H",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.523927,0.605013,0.659571,0.698649,0.750769,0.783889,0.830333,0.854577],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 28,
    label = "diene_in_HNd",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.85266,6.38529,4.92218,4.13817,3.33136,2.92489,2.45901,2.25469],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 29,
    label = "diene_in_HDe",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "diene_in_NdH",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cs,O} 0 {1,S}
4     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([41.0524,18.2092,11.1806,8.07691,5.37926,4.2151,3.04502,2.5881],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "diene_in_DeH",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {2,S}
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
    label = "diene_in_Nd2",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {2,S}
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
    label = "diene_in_NdDe",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "diene_in_DeNd",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {2,S}
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
    label = "diene_in_De2",
    group = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_unsub_unsub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00680279,0.0443743,0.136709,0.289452,0.739262,1.29757,2.74732,3.99759],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 37,
    label = "ene_unsub_monosub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     R!H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0777564,0.137304,0.19313,0.242453,0.322182,0.382107,0.479693,0.537468],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "ene_2H_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00116978,0.0052448,0.0129034,0.0235156,0.0497931,0.0781011,0.142334,0.192147],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 39,
    label = "ene_2H_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.7337,5.40604,4.05404,3.34626,2.63269,2.27984,1.88181,1.70967],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "ene_monosub_unsub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([6.87085,3.97276,2.85984,2.29707,1.74669,1.48197,1.19034,1.06681],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "ene_HNd_2H",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00802401,0.0243923,0.0475301,0.0741504,0.129284,0.180469,0.281544,0.351657],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 42,
    label = "ene_HDe_2H",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([124.122,35.239,16.555,10.0046,5.33076,3.65377,2.20807,1.71652],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 43,
    label = "ene_monosub_monosub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
5     H 0 {2,S}
6     R!H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3675.9,407.661,108.958,45.21,15.0557,7.78363,3.22966,2.08038],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 44,
    label = "ene_HNd_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    label = "ene_HNd_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3675.9,407.661,108.958,45.21,15.0557,7.78363,3.22966,2.08038],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 46,
    label = "ene_HDe_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3675.9,407.661,108.958,45.21,15.0557,7.78363,3.22966,2.08038],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:57 2011","jwallen","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 47,
    label = "ene_HDe_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_unsub_disub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     R!H 0 {2,S}
6     R!H 0 {2,S}
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
    label = "ene_2H_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    label = "ene_2H_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_2H_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_disub_unsub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "ene_Nd2_2H",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "ene_NdDe_2H",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "ene_De2_2H",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "ene_monosub_disub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
5     R!H 0 {2,S}
6     R!H 0 {2,S}
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
    label = "ene_HNd_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    label = "ene_HNd_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_HNd_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 60,
    label = "ene_HDe_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    index = 61,
    label = "ene_HDe_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_HDe_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_disub_monosub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     H 0 {2,S}
6     R!H 0 {2,S}
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
    label = "ene_Nd2_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    label = "ene_Nd2_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_NdDe_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    index = 67,
    label = "ene_NdDe_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 68,
    label = "ene_De2_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    index = 69,
    label = "ene_De2_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 70,
    label = "ene_disub_disub",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {2,S}
6     R!H 0 {2,S}
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
    index = 71,
    label = "ene_Nd2_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    index = 72,
    label = "ene_Nd2_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 73,
    label = "ene_Nd2_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 74,
    label = "ene_NdDe_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    index = 75,
    label = "ene_NdDe_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    index = 76,
    label = "ene_NdDe_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_De2_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
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
    label = "ene_De2_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
    label = "ene_De2_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
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
L1: diene_out
    L2: diene_unsub_unsub_out
    L2: diene_unsub_monosub_out
        L3: diene_unsub_monosubNd_out
        L3: diene_unsub_monosubDe_out
    L2: diene_unsub_disub_out
        L3: diene_unsub_disubNd2_out
        L3: diene_unsub_disubNdDe_out
        L3: diene_unsub_disubDe2_out
    L2: diene_monosub_monosub_out
        L3: diene_monosubNd_monosubNd_out
        L3: diene_monosubNd_monosubDe_out
        L3: diene_monosubDe_monosubDe_out
    L2: diene_monosub_disub_out
        L3: diene_monosubNd_disubNd2_out
        L3: diene_monosubNd_disubNdDe_out
        L3: diene_monosubNd_disubDe2_out
        L3: diene_monosubDe_disubNd2_out
        L3: diene_monosubDe_disubNdDe_out
        L3: diene_monosubDe_disubDe2_out
    L2: diene_disub_disub_out
        L3: diene_disubNd2_disubNd2_out
        L3: diene_disubNd2_disubDe_out
        L3: diene_disubDe_disubDe_out
L1: diene_in
    L2: diene_in_2H
    L2: diene_in_HNd
    L2: diene_in_HDe
    L2: diene_in_NdH
    L2: diene_in_DeH
    L2: diene_in_Nd2
    L2: diene_in_NdDe
    L2: diene_in_DeNd
    L2: diene_in_De2
L1: ene
    L2: ene_unsub_unsub
    L2: ene_unsub_monosub
        L3: ene_2H_HNd
        L3: ene_2H_HDe
    L2: ene_monosub_unsub
        L3: ene_HNd_2H
        L3: ene_HDe_2H
    L2: ene_monosub_monosub
        L3: ene_HNd_HNd
        L3: ene_HNd_HDe
        L3: ene_HDe_HNd
        L3: ene_HDe_HDe
    L2: ene_unsub_disub
        L3: ene_2H_Nd2
        L3: ene_2H_NdDe
        L3: ene_2H_De2
    L2: ene_disub_unsub
        L3: ene_Nd2_2H
        L3: ene_NdDe_2H
        L3: ene_De2_2H
    L2: ene_monosub_disub
        L3: ene_HNd_Nd2
        L3: ene_HNd_NdDe
        L3: ene_HNd_De2
        L3: ene_HDe_Nd2
        L3: ene_HDe_NdDe
        L3: ene_HDe_De2
    L2: ene_disub_monosub
        L3: ene_Nd2_HNd
        L3: ene_Nd2_HDe
        L3: ene_NdDe_HNd
        L3: ene_NdDe_HDe
        L3: ene_De2_HNd
        L3: ene_De2_HDe
    L2: ene_disub_disub
        L3: ene_Nd2_Nd2
        L3: ene_Nd2_NdDe
        L3: ene_Nd2_De2
        L3: ene_NdDe_Nd2
        L3: ene_NdDe_NdDe
        L3: ene_NdDe_De2
        L3: ene_De2_Nd2
        L3: ene_De2_NdDe
        L3: ene_De2_De2
"""
)

forbidden(
    label = "threeMemberedRing_2342",
    group = 
"""
1  *3 Cd 0 {2,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {2,S} {3,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
    ],
)

forbidden(
    label = "threeMemberedRing_3213",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {1,S} {2,S} {4,D}
4  *6 Cd 0 {3,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
    ],
)

