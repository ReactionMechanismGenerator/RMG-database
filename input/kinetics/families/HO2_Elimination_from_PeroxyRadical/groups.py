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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {C,Si,O,N} U0 {2,S} {5,S}
2 *2 {C,Si,N}   U0 {1,S} {3,S}
3 *3 O          U0 {2,S} {4,S}
4 *4 O          U1 {3,S}
5 *5 H          U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "R2OO_0H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,S} {5,S}
2 *2 C  U0 {1,S} {3,S}
3 *3 O  U0 {2,S} {4,S}
4 *4 O  U1 {3,S}
5 *5 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "R2OO_0H_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,S} {5,S}
2 *2 C  U0 {1,S} {3,S} {6,S} {7,S}
3 *3 O  U0 {2,S} {4,S}
4 *4 O  U1 {3,S}
5 *5 H  U0 {1,S}
6    H  U0 {2,S}
7    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R2OO_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {5,S}
2 *2 C U0 {1,S} {3,S}
3 *3 O U0 {2,S} {4,S}
4 *4 O U1 {3,S}
5 *5 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R2OO_O_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {5,S}
2 *2 C U0 {1,S} {3,S} {6,S} {7,S}
3 *3 O U0 {2,S} {4,S}
4 *4 O U1 {3,S}
5 *5 H U0 {1,S}
6    H U0 {2,S}
7    C U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R2OO_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C U0 {1,S} {3,S}
3 *3 O U0 {2,S} {4,S}
4 *4 O U1 {3,S}
5 *5 H U0 {1,S}
6    H U0 {1,S}
7    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R2OO_2H_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O U0 {2,S} {4,S}
4 *4 O U1 {3,S}
5 *5 H U0 {1,S}
6    H U0 {1,S}
7    H U0 {1,S}
8    H U0 {2,S}
9    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R2OO_2H_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    H      U0 {1,S}
7    H      U0 {1,S}
8    H      U0 {2,S}
9    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R2OO_2H_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    H             U0 {1,S}
8    H             U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R2OO_2H_HCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 C U0 {2,S} {5,S} {6,S} {7,S}
2  *2 C U0 {1,S} {3,S} {8,S} {9,S}
3  *3 O U0 {2,S} {4,S}
4  *4 O U1 {3,S}
5  *5 H U0 {1,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {2,S}
9     C U0 {2,S} {10,D}
10    C U0 {9,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R2OO_2H_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    H      U0 {1,S}
7    H      U0 {1,S}
8    {Cs,O} U0 {2,S}
9    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R2OO_2H_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    H             U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R2OO_2H_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    H             U0 {1,S}
8    {Cd,Ct,Cb,CO} U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R2OO_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    H      U0 {1,S}
7    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R2OO_HNd_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    H      U0 {1,S}
7    {Cs,O} U0 {1,S}
8    H      U0 {2,S}
9    H      U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R2OO_HNd_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    H      U0 {1,S}
7    {Cs,O} U0 {1,S}
8    H      U0 {2,S}
9    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R2OO_HNd_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cs,O}        U0 {1,S}
8    H             U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R2OO_HNd_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    H      U0 {1,S}
7    {Cs,O} U0 {1,S}
8    {Cs,O} U0 {2,S}
9    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R2OO_HNd_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cs,O}        U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R2OO_HNd_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cs,O}        U0 {1,S}
8    {Cd,Ct,Cb,CO} U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R2OO_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "R2OO_HDe_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    H             U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "R2OO_HDe_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "R2OO_HDe_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "R2OO_HDe_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "R2OO_HDe_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "R2OO_HDe_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    H             U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cd,Ct,Cb,CO} U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "R2OO_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    {Cs,O} U0 {1,S}
7    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "R2OO_NdNd_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    {Cs,O} U0 {1,S}
7    {Cs,O} U0 {1,S}
8    H      U0 {2,S}
9    H      U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "R2OO_NdNd_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    {Cs,O} U0 {1,S}
7    {Cs,O} U0 {1,S}
8    H      U0 {2,S}
9    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "R2OO_NdNd_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cs,O}        U0 {1,S}
8    H             U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "R2OO_NdNd_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C      U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O      U0 {2,S} {4,S}
4 *4 O      U1 {3,S}
5 *5 H      U0 {1,S}
6    {Cs,O} U0 {1,S}
7    {Cs,O} U0 {1,S}
8    {Cs,O} U0 {2,S}
9    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "R2OO_NdNd_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cs,O}        U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "R2OO_NdNd_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cs,O}        U0 {1,S}
8    {Cd,Ct,Cb,CO} U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "R2OO_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "R2OO_NdDe_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    H             U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "R2OO_NdDe_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "R2OO_NdDe_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "R2OO_NdDe_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "R2OO_NdDe_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "R2OO_NdDe_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cs,O}        U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cd,Ct,Cb,CO} U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "R2OO_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "R2OO_DeDe_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    H             U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "R2OO_DeDe_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "R2OO_DeDe_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    H             U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "R2OO_DeDe_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "R2OO_DeDe_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cs,O}        U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "R2OO_DeDe_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {5,S} {6,S} {7,S}
2 *2 C             U0 {1,S} {3,S} {8,S} {9,S}
3 *3 O             U0 {2,S} {4,S}
4 *4 O             U1 {3,S}
5 *5 H             U0 {1,S}
6    {Cd,Ct,Cb,CO} U0 {1,S}
7    {Cd,Ct,Cb,CO} U0 {1,S}
8    {Cd,Ct,Cb,CO} U0 {2,S}
9    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R2OO
    L2: R2OO_0H
        L3: R2OO_0H_2H
    L2: R2OO_O
        L3: R2OO_O_HNd
    L2: R2OO_2H
        L3: R2OO_2H_2H
        L3: R2OO_2H_HNd
        L3: R2OO_2H_HDe
            L4: R2OO_2H_HCd
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
"""
)

