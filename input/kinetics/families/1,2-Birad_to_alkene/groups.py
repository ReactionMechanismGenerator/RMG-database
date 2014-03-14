#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_12birad"], products=["Y_alkene"], ownReverse=False)

reverse = "Alkene_to_1,2-birad"

recipe(actions=[
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_12birad",
    multiplicity = [1,2],
    group = "OR{Y_12_00, Y_12_10, Y_12_20, Y_12_30, Y_12_40, Y_12_01, Y_12_02, Y_12_03, Y_12_04, Y_12_11, Y_12_12, Y_12_21, Y_12_22, Y_12_13, Y_12_31}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Y_12_00",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs 1 {2,S} {3,S} {4,S}
2 *2 Cs 1 {1,S} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Y_12_10",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    H       0 {1,S}
5    H       0 {2,S}
6    H       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Y_12_20",
    multiplicity = [1,2],
    group = "OR{Y_12_20a, Y_12_20b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Y_12_30",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    {Cs,Os} 0 {1,S}
5    {Cs,Os} 0 {2,S}
6    H       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Y_12_40",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    {Cs,Os} 0 {1,S}
5    {Cs,Os} 0 {2,S}
6    {Cs,Os} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Y_12_01",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Y_12_02",
    multiplicity = [1,2],
    group = "OR{Y_12_02a, Y_12_02b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Y_12_03",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Y_12_04",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Y_12_11",
    multiplicity = [1,2],
    group = "OR{Y_12_11a, Y_12_11b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Y_12_12",
    multiplicity = [1,2],
    group = "OR{Y_12_12a, Y_12_12b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Y_12_21",
    multiplicity = [1,2],
    group = "OR{Y_12_21a, Y_12_21b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Y_12_22",
    multiplicity = [1,2],
    group = "OR{Y_12_22a, Y_12_22b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Y_12_13",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cs,Os}       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Y_12_31",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cs,Os}       0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cs,Os}       0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_20a",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    {Cs,Os} 0 {1,S}
5    H       0 {2,S}
6    H       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_20b",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs      1 {2,S} {3,S} {4,S}
2 *2 Cs      1 {1,S} {5,S} {6,S}
3    {Cs,Os} 0 {1,S}
4    H       0 {1,S}
5    {Cs,Os} 0 {2,S}
6    H       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_02a",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_02b",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_11a",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,Os}       0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_11b",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cs,Os}       0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_12a",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,Os}       0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_12b",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_21a",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cs,Os}       0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_21b",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cs,Os}       0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,Os}       0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_22a",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,Os}       0 {2,S}
6    {Cs,Os}       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Y_12_22b",
    multiplicity = [1,2],
    group = 
"""
1 *1 Cs            1 {2,S} {3,S} {4,S}
2 *2 Cs            1 {1,S} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,Os}       0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cs,Os}       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Y_12birad
    L2: Y_12_00
    L2: Y_12_10
    L2: Y_12_20
    L2: Y_12_30
    L2: Y_12_40
    L2: Y_12_01
    L2: Y_12_02
    L2: Y_12_03
    L2: Y_12_04
    L2: Y_12_11
    L2: Y_12_12
    L2: Y_12_21
    L2: Y_12_22
    L2: Y_12_13
    L2: Y_12_31
"""
)

