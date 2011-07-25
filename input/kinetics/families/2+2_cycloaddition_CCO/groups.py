#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["CCO", "doublebond"], products=["four_ring"], ownReverse=False)

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
])

entry(
    index = 1,
    label = "CCO",
    group = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.79e-28,8.97663e-20,5.37665e-15,8.23084e-12,7.88152e-08,1.9289e-05,0.0295285,1.15533],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=1 label="CCO">, <Entry index=2 label="doublebond">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:48 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "doublebond",
    group = "OR{mb_CCO, mb_COC}",
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
    label = "CCO_2H",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
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
    label = "CCO_HNd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     Od 0 {2,D}
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
    index = 5,
    label = "CCO_HDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
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
    label = "CCO_Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     Od 0 {2,D}
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
    label = "CCO_NdDe",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
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
    label = "CCO_De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_CCO",
    group = 
"""
1  *3 Cd 0 {2,D}
2  *4 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
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
    label = "mb_CCO_2H",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S} {4,S}
2  *4 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_CCO_HNd",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S} {4,S}
2  *4 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_CCO_HDe",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S} {4,S}
2  *4 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_CCO_Nd2",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S} {4,S}
2  *4 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_CCO_NdDe",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S} {4,S}
2  *4 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_CCO_De2",
    group = 
"""
1  *3 Cd 0 {2,D} {3,S} {4,S}
2  *4 Cdd 0 {1,D} {5,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
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
    label = "mb_COC",
    group = 
"""
1  *3 Cdd 0 {2,D} {3,D}
2  *4 Cd 0 {1,D}
3     Od 0 {1,D}
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
    label = "mb_COC_2H",
    group = 
"""
1  *3 Cdd 0 {2,D} {5,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3     H 0 {2,S}
4     H 0 {2,S}
5     Od 0 {1,D}
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
    label = "mb_COC_HNd",
    group = 
"""
1  *3 Cdd 0 {2,D} {5,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3     H 0 {2,S}
4     {Cs,O} 0 {2,S}
5     Od 0 {1,D}
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
    label = "mb_COC_HDe",
    group = 
"""
1  *3 Cdd 0 {2,D} {5,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3     H 0 {2,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
5     Od 0 {1,D}
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
    label = "mb_COC_Nd2",
    group = 
"""
1  *3 Cdd 0 {2,D} {5,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3     {Cs,O} 0 {2,S}
4     {Cs,O} 0 {2,S}
5     Od 0 {1,D}
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
    label = "mb_COC_NdDe",
    group = 
"""
1  *3 Cdd 0 {2,D} {5,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3     {Cs,O} 0 {2,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
5     Od 0 {1,D}
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
    label = "mb_COC_De2",
    group = 
"""
1  *3 Cdd 0 {2,D} {5,D}
2  *4 Cd 0 {1,D} {3,S} {4,S}
3     {Cd,Ct,Cb,CO} 0 {2,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
5     Od 0 {1,D}
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
L1: CCO
    L2: CCO_2H
    L2: CCO_HNd
    L2: CCO_HDe
    L2: CCO_Nd2
    L2: CCO_NdDe
    L2: CCO_De2
L1: doublebond
    L2: mb_CCO
        L3: mb_CCO_2H
        L3: mb_CCO_HNd
        L3: mb_CCO_HDe
        L3: mb_CCO_Nd2
        L3: mb_CCO_NdDe
        L3: mb_CCO_De2
    L2: mb_COC
        L3: mb_COC_2H
        L3: mb_COC_HNd
        L3: mb_COC_HDe
        L3: mb_COC_Nd2
        L3: mb_COC_NdDe
        L3: mb_COC_De2
"""
)

