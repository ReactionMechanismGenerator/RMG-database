#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_DoubleBond/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["doublebond", "X_Y"], products=["X_doublebond_Y"], ownReverse=False)

reverse = "XY_Elimination_DoubleBond"
reversible = True

recipe(actions=[
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "doublebond",
    group = "OR{Cd_Cd}",
    kinetics = None,
)

entry(
    index = 2,
    label = "X_Y",
    group = "OR{H_Val7, Val7_Val7}",
    kinetics = None,
)
entry(
    index = 17,
    label = "Cd_Cd",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
5    R  u0 {2,S}
6    R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Cd/unsub_Cd/unsub",
    group =
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Cd/unsub_Cd/monosub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    [H,Val7] u0 {2,S}
6    R!H!Val7 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Cd/(H2,Val72,HVal7)_Cd/H,Val7/Nd",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [H,Val7]      u0 {1,S}
4    [H,Val7]      u0 {1,S}
5    [H,Val7]      u0 {2,S}
6    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Cd/(H2,Val72,HVal7)_Cd/H,Val7/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [H,Val7]              u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [Cd,Ct]          u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cd/monosub_Cd/unsub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    [H,Val7] u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Cd/H,Val7/Nd_Cd/(H2,Val72,HVal7)",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [H,Val7]      u0 {1,S}
4    Cs       u0 {1,S}
5    [H,Val7]      u0 {2,S}
6    [H,Val7]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cd/H,Val7/De_Cd/(H2,Val72,HVal7)",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [Cd,Ct] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [H,Val7]              u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Cd/unsub_Cd/disub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    [H,Val7] u0 {1,S}
5    R!H!Val7 u0 {2,S}
6    R!H!Val7 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Cd/(H2,Val72,HVal7)_Cd/Nd2",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [H,Val7]      u0 {1,S}
4    [H,Val7]      u0 {1,S}
5    Cs       u0 {2,S}
6    Cs       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Cd/(H2,Val72,HVal7)_Cd/Nd/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [H,Val7]              u0 {1,S}
5    Cs               u0 {2,S}
6    [Cd,Ct,CS]       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cd/(H2,Val72,HVal7)_Cd/De2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [H,Val7]              u0 {1,S}
5    [Cd,Ct,CS]       u0 {2,S}
6    [Cd,Ct,CS]       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cd/disub_Cd/unsub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    [H,Val7] u0 {2,S}
6    [H,Val7] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cd/Nd2_Cd/(H2,Val72,HVal7)",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    [H,Val7]      u0 {2,S}
6    [H,Val7]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cd/NdDe_Cd/(H2,Val72,HVal7)",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [H,Val7]              u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cd/De2_Cd/(H2,Val72,HVal7)",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,CS] u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [H,Val7]              u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cd/monosub_Cd/monosub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    [H,Val7] u0 {2,S}
6    R!H!Val7 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Cd/H,Val7/Nd_Cd/H,Val7/Nd",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [H,Val7]      u0 {1,S}
4    Cs u0 {1,S}
5    [H,Val7]      u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Cd/H,Val7/Nd_Cd/H,Val7/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    Cs         u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Cd/H,Val7/De_Cd/H,Val7/Nd",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    Cs         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Cd/H,Val7/De_Cd/H,Val7/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Cd/monosub_Cd/disub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    [H,Val7] u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    R!H!Val7 u0 {2,S}
6    R!H!Val7 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Cd/H,Val7/Nd_Cd/Nd2",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    [H,Val7]      u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cd/H,Val7/Nd_Cd/Nd/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    Cs         u0 {1,S}
5    Cs         u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Cd/H,Val7/Nd_Cd/De2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    Cs         u0 {1,S}
5    [Cd,Ct,CS] u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Cd/H,Val7/De_Cd/Nd2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    Cs         u0 {2,S}
6    Cs         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Cd/H,Val7/De_Cd/Nd/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    Cs         u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cd/H,Val7/De_Cd/De2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [H,Val7]              u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [Cd,Ct,CS] u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cd/disub_Cd/monosub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    [H,Val7] u0 {2,S}
6    R!H!Val7 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Cd/Nd2_Cd/H,Val7/Nd",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    [H,Val7]      u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Cd/Nd2_Cd/H,Val7/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    Cs         u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cd/De2_Cd/H,Val7/Nd",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,CS] u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    Cs         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cd/De2_Cd/H,Val7/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,CS] u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cd/Nd/De_Cd/H,Val7/Nd",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    Cs         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cd/Nd/De_Cd/H,Val7/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [H,Val7]              u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cd/disub_Cd/disub",
    group =
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cd  u0 {1,D} {5,S} {6,S}
3    R!H!Val7 u0 {1,S}
4    R!H!Val7 u0 {1,S}
5    R!H!Val7 u0 {2,S}
6    R!H!Val7 u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cd/Nd2_Cd/Nd2",
    group =
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 Cd       u0 {1,D} {5,S} {6,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {2,S}
6    Cs u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cd/Nd2_Cd/Nd/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    Cs         u0 {1,S}
5    Cs         u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cd/Nd2_Cd/De2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    Cs         u0 {1,S}
5    [Cd,Ct,CS] u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cd/Nd/De_Cd/Nd2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    Cs         u0 {2,S}
6    Cs         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cd/Nd/De_Cd/Nd/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    Cs         u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cd/Nd/De_Cd/De2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    Cs         u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [Cd,Ct,CS] u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Cd/De2_Cd/Nd2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,CS] u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    Cs         u0 {2,S}
6    Cs         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Cd/De2_Cd/Nd/De",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,CS] u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    Cs         u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Cd/De2_Cd/De2",
    group =
"""
1 *1 Cd               u0 {2,D} {3,S} {4,S}
2 *2 Cd               u0 {1,D} {5,S} {6,S}
3    [Cd,Ct,CS] u0 {1,S}
4    [Cd,Ct,CS] u0 {1,S}
5    [Cd,Ct,CS] u0 {2,S}
6    [Cd,Ct,CS] u0 {2,S}
""",
    kinetics = None,
)



entry(
    index = 78,
    label = "H_Val7",
    group =
"""
1 *3 H                   u0 {2,S}
2 *4 Val7                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Val7_Val7",
    group =
"""
1 *3 Val7  u0 {2,S}
2 *4 Val7 u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "HF",
    group =
"""
1 *3 H u0 {2,S}
2 *4 F1s u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: doublebond
    L2: Cd_Cd
        L3: Cd/unsub_Cd/unsub
        L3: Cd/unsub_Cd/monosub
            L4: Cd/(H2,Val72,HVal7)_Cd/H,Val7/Nd
            L4: Cd/(H2,Val72,HVal7)_Cd/H,Val7/De
        L3: Cd/monosub_Cd/unsub
            L4: Cd/H,Val7/Nd_Cd/(H2,Val72,HVal7)
            L4: Cd/H,Val7/De_Cd/(H2,Val72,HVal7)
        L3: Cd/unsub_Cd/disub
            L4: Cd/(H2,Val72,HVal7)_Cd/Nd2
            L4: Cd/(H2,Val72,HVal7)_Cd/Nd/De
            L4: Cd/(H2,Val72,HVal7)_Cd/De2
        L3: Cd/disub_Cd/unsub
            L4: Cd/Nd2_Cd/(H2,Val72,HVal7)
            L4: Cd/NdDe_Cd/(H2,Val72,HVal7)
            L4: Cd/De2_Cd/(H2,Val72,HVal7)
        L3: Cd/monosub_Cd/monosub
            L4: Cd/H,Val7/Nd_Cd/H,Val7/Nd
            L4: Cd/H,Val7/Nd_Cd/H,Val7/De
            L4: Cd/H,Val7/De_Cd/H,Val7/Nd
            L4: Cd/H,Val7/De_Cd/H,Val7/De
        L3: Cd/monosub_Cd/disub
            L4: Cd/H,Val7/Nd_Cd/Nd2
            L4: Cd/H,Val7/Nd_Cd/Nd/De
            L4: Cd/H,Val7/Nd_Cd/De2
            L4: Cd/H,Val7/De_Cd/Nd2
            L4: Cd/H,Val7/De_Cd/Nd/De
            L4: Cd/H,Val7/De_Cd/De2
        L3: Cd/disub_Cd/monosub
            L4: Cd/Nd2_Cd/H,Val7/Nd
            L4: Cd/Nd2_Cd/H,Val7/De
            L4: Cd/De2_Cd/H,Val7/Nd
            L4: Cd/De2_Cd/H,Val7/De
            L4: Cd/Nd/De_Cd/H,Val7/Nd
            L4: Cd/Nd/De_Cd/H,Val7/De
        L3: Cd/disub_Cd/disub
            L4: Cd/Nd2_Cd/Nd2
            L4: Cd/Nd2_Cd/Nd/De
            L4: Cd/Nd2_Cd/De2
            L4: Cd/Nd/De_Cd/Nd2
            L4: Cd/Nd/De_Cd/Nd/De
            L4: Cd/Nd/De_Cd/De2
            L4: Cd/De2_Cd/Nd2
            L4: Cd/De2_Cd/Nd/De
            L4: Cd/De2_Cd/De2
L1: X_Y
    L2: H_Val7
        L3: HF
    L2: Val7_Val7
       """
)
