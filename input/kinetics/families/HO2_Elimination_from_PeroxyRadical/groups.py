#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["R2OO"], products=["R=R", "OOH"], ownReverse=False)

reverse = "HO2_concerted_addition"

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
1 *1 {C,Si,O} 0 {2,S} {5,S}
2 *2 {C,Si}   0 {1,S} {3,S}
3 *3 O        0 {2,S} {4,S}
4 *4 O        1 {3,S}
5 *5 H        0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "R2OO_2H",
    group = 
"""
1 *1 C 0 {2,S} {5,S} {6,S} {7,S}
2 *2 C 0 {1,S} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 O 1 {3,S}
5 *5 H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "R2OO_2H_2H",
    group = 
"""
1 *1 C 0 {2,S} {5,S} {6,S} {7,S}
2 *2 C 0 {1,S} {3,S} {8,S} {9,S}
3 *3 O 0 {2,S} {4,S}
4 *4 O 1 {3,S}
5 *5 H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "R2OO_2H_HNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    H      0 {1,S}
7    H      0 {1,S}
8    H      0 {2,S}
9    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "R2OO_2H_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    H             0 {1,S}
8    H             0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
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
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "R2OO_2H_NdNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    H      0 {1,S}
7    H      0 {1,S}
8    {Cs,O} 0 {2,S}
9    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "R2OO_2H_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    H             0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "R2OO_2H_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    H             0 {1,S}
8    {Cd,Ct,Cb,CO} 0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "R2OO_HNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    H      0 {1,S}
7    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "R2OO_HNd_2H",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    H      0 {1,S}
7    {Cs,O} 0 {1,S}
8    H      0 {2,S}
9    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "R2OO_HNd_HNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    H      0 {1,S}
7    {Cs,O} 0 {1,S}
8    H      0 {2,S}
9    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "R2OO_HNd_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cs,O}        0 {1,S}
8    H             0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "R2OO_HNd_NdNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    H      0 {1,S}
7    {Cs,O} 0 {1,S}
8    {Cs,O} 0 {2,S}
9    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "R2OO_HNd_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cs,O}        0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "R2OO_HNd_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cs,O}        0 {1,S}
8    {Cd,Ct,Cb,CO} 0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "R2OO_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "R2OO_HDe_2H",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "R2OO_HDe_HNd",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "R2OO_HDe_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "R2OO_HDe_NdNd",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "R2OO_HDe_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "R2OO_HDe_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cd,Ct,Cb,CO} 0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "R2OO_NdNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "R2OO_NdNd_2H",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {1,S}
8    H      0 {2,S}
9    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "R2OO_NdNd_HNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {1,S}
8    H      0 {2,S}
9    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "R2OO_NdNd_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cs,O}        0 {1,S}
8    H             0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "R2OO_NdNd_NdNd",
    group = 
"""
1 *1 C      0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      0 {2,S} {4,S}
4 *4 O      1 {3,S}
5 *5 H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {1,S}
8    {Cs,O} 0 {2,S}
9    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "R2OO_NdNd_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cs,O}        0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "R2OO_NdNd_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cs,O}        0 {1,S}
8    {Cd,Ct,Cb,CO} 0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "R2OO_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "R2OO_NdDe_2H",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "R2OO_NdDe_HNd",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "R2OO_NdDe_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "R2OO_NdDe_NdNd",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "R2OO_NdDe_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "R2OO_NdDe_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cd,Ct,Cb,CO} 0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "R2OO_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "R2OO_DeDe_2H",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "R2OO_DeDe_HNd",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "R2OO_DeDe_HDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    H             0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "R2OO_DeDe_NdNd",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "R2OO_DeDe_NdDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cs,O}        0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "R2OO_DeDe_DeDe",
    group = 
"""
1 *1 C             0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             0 {2,S} {4,S}
4 *4 O             1 {3,S}
5 *5 H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {1,S}
8    {Cd,Ct,Cb,CO} 0 {2,S}
9    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "OCOO",
    group = 
"""
1 *1 O 0 {2,S} {5,S}
2 *2 C 0 {1,S} {3,S} {6,S} {7,S}
3 *3 O 0 {2,S} {4,S}
4 *4 O 1 {3,S}
5 *5 H 0 {1,S}
6    R 0 {2,S}
7    R 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
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

