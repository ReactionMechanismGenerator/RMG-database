#!/usr/bin/env python
# encoding: utf-8

name = "1,2_XY_interchange/groups"
shortDesc = u""
longDesc = u"""

X1-R2-R3-Y4    ->    Y4-R2-R3-X1

Y = F,Cl,Br,I
X = F,Cl,Br,I,O
"""

template(reactants=["XY"], products=["YX"], ownReverse=True)

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 0,
    label = "XY",
    group = "OR{YY,OY}",
    kinetics = None,
)

entry(
    index = 1,
    label = "YY",
    group =
"""
1 *1 Val7   u0 {2,S}
2 *2 Cs     u0 {1,S} {3,S}
3 *3 Cs     u0 {2,S} {4,S}
4 *4 Val7   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "FF",
    group =
"""
1 *1 F1s   u0 {2,S}
2 *2 Cs    u0 {1,S} {3,S}
3 *3 Cs    u0 {2,S} {4,S}
4 *4 F1s   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "ClCl",
    group =
"""
1 *1 Cl1s  u0 {2,S}
2 *2 Cs    u0 {1,S} {3,S}
3 *3 Cs    u0 {2,S} {4,S}
4 *4 Cl1s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "BrBr",
    group =
"""
1 *1 Br1s  u0 {2,S}
2 *2 Cs    u0 {1,S} {3,S}
3 *3 Cs    u0 {2,S} {4,S}
4 *4 Br1s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "FCl",
    group =
"""
1 *1 F1s  u0 {2,S}
2 *2 Cs   u0 {1,S} {3,S}
3 *3 Cs   u0 {2,S} {4,S}
4 *4 Cl1s u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "FBr",
    group =
"""
1 *1 F1s   u0 {2,S}
2 *2 Cs  u0 {1,S} {3,S}
3 *3 Cs  u0 {2,S} {4,S}
4 *4 Br1s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "ClBr",
    group =
"""
1 *1 Cl1s  u0 {2,S}
2 *2 Cs    u0 {1,S} {3,S}
3 *3 Cs    u0 {2,S} {4,S}
4 *4 Br1s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "OY",
    group =
"""
1 *1 O2s    u0 {2,S}
2 *2 Cs     u0 {1,S} {3,S}
3 *3 Cs     u0 {2,S} {4,S}
4 *4 Val7   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "OF",
    group =
"""
1 *1 O2s  u0 {2,S}
2 *2 Cs   u0 {1,S} {3,S}
3 *3 Cs   u0 {2,S} {4,S}
4 *4 F1s  u0 {3,S}
""",
    kinetics = None,
)


entry(
    index = 10,
    label = "OCl",
    group =
"""
1 *1 O2s  u0 {2,S}
2 *2 Cs   u0 {1,S} {3,S}
3 *3 Cs   u0 {2,S} {4,S}
4 *4 Cl1s u0 {3,S}
""",
    kinetics = None,
)


entry(
    index = 11,
    label = "OBr",
    group =
"""
1 *1 O2s  u0 {2,S}
2 *2 Cs   u0 {1,S} {3,S}
3 *3 Cs   u0 {2,S} {4,S}
4 *4 Br1s u0 {3,S}
""",
    kinetics = None,
)


tree(
"""
L1: XY
    L2: YY
        L3: FF
        L3: ClCl
        L3: BrBr
        L3: FCl
        L3: FBr
        L3: ClBr
    L2: OY
        L3: OF
        L3: OBr
        L3: OCl
"""
)

forbidden(
    label = "BrF",
    group = 
"""
1 *1 Br1s   u0 {2,S}
2 *2 Cs  u0 {1,S} {3,S}
3 *3 Cs  u0 {2,S} {4,S}
4 *4 F1s  u0 {3,S}
""",
    shortDesc = """""",
    longDesc = 
"""
Avoid duplicate reactions
""",
)

forbidden(
    label = "BrCl",
    group = 
"""
1 *1 Br1s  u0 {2,S}
2 *2 Cs    u0 {1,S} {3,S}
3 *3 Cs    u0 {2,S} {4,S}
4 *4 Cl1s  u0 {3,S}
""",
    shortDesc = """""",
    longDesc = 
"""
Avoid duplicate reactions
""",
)

forbidden(
    label = "ClF",
    group =
"""
1 *1 Cl1s  u0 {2,S}
2 *2 Cs   u0 {1,S} {3,S}
3 *3 Cs   u0 {2,S} {4,S}
4 *4 F1s u0 {3,S}
""",    
    shortDesc = """""",
    longDesc = 
"""
Avoid duplicate reactions
""",

)
