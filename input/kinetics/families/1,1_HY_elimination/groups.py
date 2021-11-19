#!/usr/bin/env python
# encoding: utf-8

name = "1,1_HY_elimination/groups"
shortDesc = u""
longDesc = u"""

    Y
    |
H*2-C*1-R   ->  Y-C*1:-R + H*2-Y*3
    |
    Y*3

Y = F,Cl,Br

The second halogen (unlabeled Y) is required to stabilize the carbene
"""

template(reactants=["Root"], products=["HY","YCR"], ownReverse=False)

reversible = True

reactantNum = 1

productNum = 2

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*1', 1, '*3'],
    ['GAIN_PAIR', '*1', '1'],
    ['FORM_BOND', '*2', 1, '*3'],
])



entry(
    index = 1,
    label = "Root",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3 *3 [F1s,Cl1s,Br1s] u0 {1,S}
4    [F1s,Cl1s,Br1s] u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "HF",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3 *3 F1s        u0 {1,S}
4    [F1s,Cl1s,Br1s] u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "HCl",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3 *3 Cl1s       u0 {1,S}
4   [F1s,Cl1s,Br1s] u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "HBr",
    group =
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3 *3 Br1s       u0 {1,S}
4   [F1s,Cl1s,Br1s] u0 {1,S}
5    R!H!Val7 u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: HF
    L2: HCl
    L2: HBr
"""
)