#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CCO", "doublebond"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage_CCO"

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
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "doublebond",
    group = "OR{mb_CCO, mb_COC}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CCO_2H",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CCO_HNd",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cdd    0 {1,D} {5,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CCO_HDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CCO_Nd2",
    group = 
"""
1 *1 Cd     0 {2,D} {3,S} {4,S}
2 *2 Cdd    0 {1,D} {5,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CCO_NdDe",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CCO_De2",
    group = 
"""
1 *1 Cd            0 {2,D} {3,S} {4,S}
2 *2 Cdd           0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "mb_CCO",
    group = 
"""
1 *3 Cd  0 {2,D}
2 *4 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "mb_CCO_2H",
    group = 
"""
1 *3 Cd  0 {2,D} {3,S} {4,S}
2 *4 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "mb_CCO_HNd",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cdd    0 {1,D} {5,D}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "mb_CCO_HDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cdd           0 {1,D} {5,D}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "mb_CCO_Nd2",
    group = 
"""
1 *3 Cd     0 {2,D} {3,S} {4,S}
2 *4 Cdd    0 {1,D} {5,D}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    Od     0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "mb_CCO_NdDe",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cdd           0 {1,D} {5,D}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "mb_CCO_De2",
    group = 
"""
1 *3 Cd            0 {2,D} {3,S} {4,S}
2 *4 Cdd           0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    Od            0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "mb_COC",
    group = 
"""
1 *3 Cdd 0 {2,D} {3,D}
2 *4 Cd  0 {1,D}
3    Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "mb_COC_2H",
    group = 
"""
1 *3 Cdd 0 {2,D} {5,D}
2 *4 Cd  0 {1,D} {3,S} {4,S}
3    H   0 {2,S}
4    H   0 {2,S}
5    Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "mb_COC_HNd",
    group = 
"""
1 *3 Cdd    0 {2,D} {5,D}
2 *4 Cd     0 {1,D} {3,S} {4,S}
3    H      0 {2,S}
4    {Cs,O} 0 {2,S}
5    Od     0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "mb_COC_HDe",
    group = 
"""
1 *3 Cdd           0 {2,D} {5,D}
2 *4 Cd            0 {1,D} {3,S} {4,S}
3    H             0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    Od            0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "mb_COC_Nd2",
    group = 
"""
1 *3 Cdd    0 {2,D} {5,D}
2 *4 Cd     0 {1,D} {3,S} {4,S}
3    {Cs,O} 0 {2,S}
4    {Cs,O} 0 {2,S}
5    Od     0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "mb_COC_NdDe",
    group = 
"""
1 *3 Cdd           0 {2,D} {5,D}
2 *4 Cd            0 {1,D} {3,S} {4,S}
3    {Cs,O}        0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    Od            0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "mb_COC_De2",
    group = 
"""
1 *3 Cdd           0 {2,D} {5,D}
2 *4 Cd            0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    Od            0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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

