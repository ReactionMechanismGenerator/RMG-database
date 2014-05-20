#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CO/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CO", "doublebond"], products=["four_ring"], ownReverse=False)

reverse = "Four_Ring_Cleavage_CO"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
])

entry(
    index = 1,
    label = "CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U0 {2,D}
2 *2 Od U0 {1,D}
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
    group = "OR{mb_CO, mb_OC, mb_CCO, mb_COC}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CO_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U0 {2,D} {3,S} {4,S}
2 *2 Od U0 {1,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CO_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO     U0 {2,D} {3,S} {4,S}
2 *2 Od     U0 {1,D}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CO_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO            U0 {2,D} {3,S} {4,S}
2 *2 Od            U0 {1,D}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CO_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO     U0 {2,D} {3,S} {4,S}
2 *2 Od     U0 {1,D}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CO_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO            U0 {2,D} {3,S} {4,S}
2 *2 Od            U0 {1,D}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CO_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO            U0 {2,D} {3,S} {4,S}
2 *2 Od            U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CH2CHO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2 *2 O U0 {1,D}
3    H U0 {1,S}
4    C U1 {1,S} {5,S} {6,S}
5    H U0 {4,S}
6    H U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "mb_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO U0 {2,D}
2 *4 Od U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "mb_CO_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO U0 {2,D} {3,S} {4,S}
2 *4 Od U0 {1,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "mb_CO_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO     U0 {2,D} {3,S} {4,S}
2 *4 Od     U0 {1,D}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "mb_CO_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO            U0 {2,D} {3,S} {4,S}
2 *4 Od            U0 {1,D}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "mb_CO_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO     U0 {2,D} {3,S} {4,S}
2 *4 Od     U0 {1,D}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "mb_CO_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO            U0 {2,D} {3,S} {4,S}
2 *4 Od            U0 {1,D}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "mb_CO_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 CO            U0 {2,D} {3,S} {4,S}
2 *4 Od            U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "mb_OC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od U0 {2,D}
2 *4 CO U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "mb_OC_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od U0 {2,D}
2 *4 CO U0 {1,D} {3,S} {4,S}
3    H  U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "mb_OC_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od     U0 {2,D}
2 *4 CO     U0 {1,D} {3,S} {4,S}
3    H      U0 {2,S}
4    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "mb_OC_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od            U0 {2,D}
2 *4 CO            U0 {1,D} {3,S} {4,S}
3    H             U0 {2,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "mb_OC_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od     U0 {2,D}
2 *4 CO     U0 {1,D} {3,S} {4,S}
3    {Cs,O} U0 {2,S}
4    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "mb_OC_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od            U0 {2,D}
2 *4 CO            U0 {1,D} {3,S} {4,S}
3    {Cs,O}        U0 {2,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "mb_OC_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Od            U0 {2,D}
2 *4 CO            U0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} U0 {2,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "mb_CCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd  U0 {2,D}
2 *4 Cdd U0 {1,D} {3,D}
3    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "mb_CCO_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd  U0 {2,D} {3,S} {4,S}
2 *4 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "mb_CCO_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd     U0 {2,D} {3,S} {4,S}
2 *4 Cdd    U0 {1,D} {5,D}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
5    Od     U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "mb_CCO_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd            U0 {2,D} {3,S} {4,S}
2 *4 Cdd           U0 {1,D} {5,D}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    Od            U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "mb_CCO_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd     U0 {2,D} {3,S} {4,S}
2 *4 Cdd    U0 {1,D} {5,D}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
5    Od     U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "mb_CCO_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd            U0 {2,D} {3,S} {4,S}
2 *4 Cdd           U0 {1,D} {5,D}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    Od            U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "mb_CCO_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd            U0 {2,D} {3,S} {4,S}
2 *4 Cdd           U0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    Od            U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "mb_COC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd U0 {2,D} {3,D}
2 *4 Cd  U0 {1,D}
3    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "mb_COC_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd U0 {2,D} {5,D}
2 *4 Cd  U0 {1,D} {3,S} {4,S}
3    H   U0 {2,S}
4    H   U0 {2,S}
5    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "mb_COC_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd    U0 {2,D} {5,D}
2 *4 Cd     U0 {1,D} {3,S} {4,S}
3    H      U0 {2,S}
4    {Cs,O} U0 {2,S}
5    Od     U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "mb_COC_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd           U0 {2,D} {5,D}
2 *4 Cd            U0 {1,D} {3,S} {4,S}
3    H             U0 {2,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    Od            U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "mb_COC_Nd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd    U0 {2,D} {5,D}
2 *4 Cd     U0 {1,D} {3,S} {4,S}
3    {Cs,O} U0 {2,S}
4    {Cs,O} U0 {2,S}
5    Od     U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "mb_COC_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd           U0 {2,D} {5,D}
2 *4 Cd            U0 {1,D} {3,S} {4,S}
3    {Cs,O}        U0 {2,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    Od            U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "mb_COC_De2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cdd           U0 {2,D} {5,D}
2 *4 Cd            U0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} U0 {2,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    Od            U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: CO
    L2: CO_2H
    L2: CO_HNd
    L2: CO_HDe
    L2: CO_Nd2
    L2: CO_NdDe
    L2: CO_De2
    L2: CH2CHO
L1: doublebond
    L2: mb_CO
        L3: mb_CO_2H
        L3: mb_CO_HNd
        L3: mb_CO_HDe
        L3: mb_CO_Nd2
        L3: mb_CO_NdDe
        L3: mb_CO_De2
    L2: mb_OC
        L3: mb_OC_2H
        L3: mb_OC_HNd
        L3: mb_OC_HDe
        L3: mb_OC_Nd2
        L3: mb_OC_NdDe
        L3: mb_OC_De2
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

