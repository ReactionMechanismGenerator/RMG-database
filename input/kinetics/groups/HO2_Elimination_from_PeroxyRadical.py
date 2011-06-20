#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical"
shortDesc = ""
longDesc = """

"""

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
1  *1 {C,Si,O} 0 {2,S} {5,S}
2  *2 {C,Si} 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([6.68789e-16,1.69352e-10,3.08795e-07,4.74309e-05,0.0269938,1.26814,235.765,3457.04],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Modified the group definition to allow O at *1 site, after MRHarper's change to old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "R2OO_2H",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.49629,1.63536,1.31213,1.1585,1.03165,0.99514,1.01893,1.09086],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 3,
    label = "R2OO_2H_2H",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0700398,0.120281,0.173548,0.227891,0.336723,0.443927,0.702222,0.948063],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "R2OO_2H_HNd",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.136885,0.229549,0.318042,0.39946,0.541215,0.65979,0.888907,1.05969],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "R2OO_2H_HDe",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([90.8707,15.8243,5.82406,3.09039,1.48343,1.00318,0.661444,0.583389],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "CH3CH(OO)CHCH2",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     C 0 {2,S} {10,S} {11,D}
10    H 0 {9,S}
11    C 0 {9,D} {12,S} {13,S}
12    H 0 {11,S}
13    H 0 {11,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([90.8707,15.8243,5.82406,3.09039,1.48343,1.00318,0.661444,0.583389],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "R2OO_2H_NdNd",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.22441,1.69182,2.07746,2.40024,2.91396,3.31087,4.02166,4.51766],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "R2OO_2H_NdDe",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.290811,0.361159,0.405261,0.433343,0.463035,0.474752,0.475591,0.464336],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "R2OO_HNd_2H",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.113295,0.153985,0.190855,0.224729,0.285789,0.340361,0.458631,0.560429],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "R2OO_HNd_HNd",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.214269,0.278245,0.328017,0.367952,0.428713,0.473565,0.549833,0.600276],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "R2OO_HNd_HDe",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.01312,1.09948,1.06317,0.984111,0.810266,0.663866,0.426587,0.297595],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "R2OO_HNd_NdDe",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.874571,1.23638,1.45694,1.57906,1.65847,1.63519,1.46203,1.2848],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "R2OO_NdNd_2H",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.110908,0.172011,0.227641,0.277493,0.362606,0.432995,0.568702,0.670534],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "R2OO_NdNd_HNd",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.413591,0.536665,0.618463,0.673323,0.736112,0.765433,0.781867,0.771271],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "R2OO_NdNd_HDe",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([14.5832,20.4737,21.9663,21.0726,17.09,13.1921,7.02831,4.10093],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 29,
    label = "R2OO_NdNd_NdDe",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cd,Ct,Cb,CO} 0 {1,S}
7     {Cd,Ct,Cb,CO} 0 {1,S}
8     {Cd,Ct,Cb,CO} 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
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
1  *1 O 0 {2,S} {5,S}
2  *2 C 0 {1,S} {3,S} {6,S} {7,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     R 0 {2,S}
7     R 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "HOCH[OO]CH3",
    group = 
"""
1  *1 O 0 {2,S} {5,S}
2  *2 C 0 {1,S} {3,S} {6,S} {7,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {2,S}
7     C 0 {2,S} {8,S} {9,S} {10,S}
8     H 0 {7,S}
9     H 0 {7,S}
10    H 0 {7,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jun 20 10:40:16 2011","Richard West <rwest@mit.edu>","action","""Added this group definition, which MRHarper recently added to the old RMG database."""),
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

