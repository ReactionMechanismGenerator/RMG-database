#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RnOO"], products=["RO", "OR"], ownReverse=False)

reverse = "OH+CyclicEther_Form_Alkyl-hydroperoxyl"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['GAIN_RADICAL', '*3', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "RnOO",
    group = "OR{R2OO, R3OO, R4OO, R5OO}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_rad_intra",
    group = 
"""
1 *1 R u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R2OO",
    group = "OR{R2OOH, R2OOR, R2OOJ}",
    kinetics = None,
)

entry(
    index = 4,
    label = "R2OOJ",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,S}
3 *2 O                    u0 {2,S} {4,S}
4 *3 O                    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R2OOJ_S",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *2 O       u0 {2,S} {4,S}
4 *3 O       u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R2OOH",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,S}
3 *2 O                    u0 {2,S} {4,S}
4 *3 O                    u0 {3,S} {5,S}
5    H                    u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R2OOH_S",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *2 O       u0 {2,S} {4,S}
4 *3 O       u0 {3,S} {5,S}
5    H       u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R2OOH_SCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 CO      u0 {1,S} {3,S}
3 *2 O       u0 {2,S} {4,S}
4 *3 O       u0 {3,S} {5,S}
5    H       u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R2OOH_D",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 O  u0 {2,S} {4,S}
4 *3 O  u0 {3,S} {5,S}
5    H  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R2OOR",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,S}
3 *2 O                    u0 {2,S} {4,S}
4 *3 O                    u0 {3,S} {5,S}
5    R!H                  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R2OOR_S",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *2 O       u0 {2,S} {4,S}
4 *3 O       u0 {3,S} {5,S}
5    R!H     u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R2OOR_SCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 CO      u0 {1,S} {3,S}
3 *2 O       u0 {2,S} {4,S}
4 *3 O       u0 {3,S} {5,S}
5    R!H     u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R2OOR_D",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 O   u0 {2,S} {4,S}
4 *3 O   u0 {3,S} {5,S}
5    R!H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R3OO",
    group = "OR{R3OOH, R3OOR, R3OOJ}",
    kinetics = None,
)

entry(
    index = 15,
    label = "R3OOJ",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,S}
4 *2 O                    u0 {3,S} {5,S}
5 *3 O                    u1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R3OOH",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,S}
4 *2 O                    u0 {3,S} {5,S}
5 *3 O                    u0 {4,S} {6,S}
6    H                    u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R3OOH_SS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4 *2 O          u0 {3,S} {5,S}
5 *3 O          u0 {4,S} {6,S}
6    H          u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R3OOH_SSCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    CO      u0 {2,S} {4,S}
4 *2 O       u0 {3,S} {5,S}
5 *3 O       u0 {4,S} {6,S}
6    H       u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R3OOH_SD",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 Cd      u0 {1,S} {3,D}
3    Cd      u0 {2,D} {4,S}
4 *2 O       u0 {3,S} {5,S}
5 *3 O       u0 {4,S} {6,S}
6    H       u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R3OOH_DS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4 *2 O          u0 {3,S} {5,S}
5 *3 O          u0 {4,S} {6,S}
6    H          u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R3OOR",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,S}
4 *2 O                    u0 {3,S} {5,S}
5 *3 O                    u0 {4,S} {6,S}
6    R!H                  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R3OOR_SS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4 *2 O          u0 {3,S} {5,S}
5 *3 O          u0 {4,S} {6,S}
6    R!H        u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R3OOR_SSCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    CO      u0 {2,S} {4,S}
4 *2 O       u0 {3,S} {5,S}
5 *3 O       u0 {4,S} {6,S}
6    R!H     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "R3OOR_SD",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 Cd      u0 {1,S} {3,D}
3    Cd      u0 {2,D} {4,S}
4 *2 O       u0 {3,S} {5,S}
5 *3 O       u0 {4,S} {6,S}
6    R!H     u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "R3OOR_DS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4 *2 O          u0 {3,S} {5,S}
5 *3 O          u0 {4,S} {6,S}
6    R!H        u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R4OO",
    group = "OR{R4OOH, R4OOR, R4OOJ}",
    kinetics = None,
)

entry(
    index = 27,
    label = "R4OOJ",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,[S,D]}
4    [CO,Cd,Cs,Sid,Sis,N] u0 {3,[S,D]} {5,S}
5 *2 O                    u0 {4,S} {6,S}
6 *3 O                    u1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R4OOH",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,[S,D]}
4    [CO,Cd,Cs,Sid,Sis,N] u0 {3,[S,D]} {5,S}
5 *2 O                    u0 {4,S} {6,S}
6 *3 O                    u0 {5,S} {7,S}
7    H                    u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R4OOH_SSS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 O          u0 {4,S} {6,S}
6 *3 O          u0 {5,S} {7,S}
7    H          u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R4OOH_SSSCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    [Cd,Cs] u0 {2,S} {4,S}
4    CO      u0 {3,S} {5,S}
5 *2 O       u0 {4,S} {6,S}
6 *3 O       u0 {5,S} {7,S}
7    H       u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R4OOH_SSD",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    Cd      u0 {2,S} {4,D}
4    Cd      u0 {3,D} {5,S}
5 *2 O       u0 {4,S} {6,S}
6 *3 O       u0 {5,S} {7,S}
7    H       u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R4OOH_SDS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3    Cd         u0 {2,D} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 O          u0 {4,S} {6,S}
6 *3 O          u0 {5,S} {7,S}
7    H          u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R4OOH_DSS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 O          u0 {4,S} {6,S}
6 *3 O          u0 {5,S} {7,S}
7    H          u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R4OOH_DSD",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3    Cd u0 {2,S} {4,D}
4    Cd u0 {3,D} {5,S}
5 *2 O  u0 {4,S} {6,S}
6 *3 O  u0 {5,S} {7,S}
7    H  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R4OOR",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,[S,D]}
4    [CO,Cd,Cs,Sid,Sis,N] u0 {3,[S,D]} {5,S}
5 *2 O                    u0 {4,S} {6,S}
6 *3 O                    u0 {5,S} {7,S}
7    R!H                  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R4OOR_SSS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 O          u0 {4,S} {6,S}
6 *3 O          u0 {5,S} {7,S}
7    R!H        u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "R4OOR_SSSCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    [Cd,Cs] u0 {2,S} {4,S}
4    CO      u0 {3,S} {5,S}
5 *2 O       u0 {4,S} {6,S}
6 *3 O       u0 {5,S} {7,S}
7    R!H     u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R4OOR_SSD",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    Cd      u0 {2,S} {4,D}
4    Cd      u0 {3,D} {5,S}
5 *2 O       u0 {4,S} {6,S}
6 *3 O       u0 {5,S} {7,S}
7    R!H     u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "R4OOR_SDS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3    Cd         u0 {2,D} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 O          u0 {4,S} {6,S}
6 *3 O          u0 {5,S} {7,S}
7    R!H        u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "R4OOR_DSS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 O          u0 {4,S} {6,S}
6 *3 O          u0 {5,S} {7,S}
7    R!H        u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "R4OOR_DSD",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3    Cd  u0 {2,S} {4,D}
4    Cd  u0 {3,D} {5,S}
5 *2 O   u0 {4,S} {6,S}
6 *3 O   u0 {5,S} {7,S}
7    R!H u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "R5OO",
    group = "OR{R5OOH, R5OOR, R5OOJ}",
    kinetics = None,
)

entry(
    index = 43,
    label = "R5OOJ",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,[S,D]}
4    [CO,Cd,Cs,Sid,Sis,N] u0 {3,[S,D]} {5,[S,D]}
5    [CO,Cd,Cs,Sid,Sis,N] u0 {4,[S,D]} {6,S}
6 *2 O                    u0 {5,S} {7,S}
7 *3 O                    u1 {6,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "R5OOH",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,[S,D]}
4    [CO,Cd,Cs,Sid,Sis,N] u0 {3,[S,D]} {5,[S,D]}
5    [CO,Cd,Cs,Sid,Sis,N] u0 {4,[S,D]} {6,S}
6 *2 O                    u0 {5,S} {7,S}
7 *3 O                    u0 {6,S} {8,S}
8    H                    u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "R5OOH_SSSS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    H          u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R5OOH_SSSSCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    [Cd,Cs] u0 {2,S} {4,S}
4    [Cd,Cs] u0 {3,S} {5,S}
5    CO      u0 {4,S} {6,S}
6 *2 O       u0 {5,S} {7,S}
7 *3 O       u0 {6,S} {8,S}
8    H       u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R5OOH_SSSD",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    Cd         u0 {3,S} {5,D}
5    Cd         u0 {4,D} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    H          u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "R5OOH_SSDS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    Cd         u0 {2,S} {4,D}
4    Cd         u0 {3,D} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    H          u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "R5OOH_SDSS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3    Cd         u0 {2,D} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    H          u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "R5OOH_DSSS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    H          u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "R5OOH_SDSD",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 Cd      u0 {1,S} {3,D}
3    Cd      u0 {2,D} {4,S}
4    Cd      u0 {3,S} {5,D}
5    Cd      u0 {4,D} {6,S}
6 *2 O       u0 {5,S} {7,S}
7 *3 O       u0 {6,S} {8,S}
8    H       u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "R5OOH_DSDS",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3    Cd u0 {2,S} {4,D}
4    Cd u0 {3,D} {5,S}
5    Cd u0 {4,S} {6,S}
6 *2 O  u0 {5,S} {7,S}
7 *3 O  u0 {6,S} {8,S}
8    H  u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "R5OOR",
    group = 
"""
1 *1 [CO,Cd,Cs,Sid,Sis,N] u1 {2,[S,D]}
2 *4 [CO,Cd,Cs,Sid,Sis,N] u0 {1,[S,D]} {3,[S,D]}
3    [CO,Cd,Cs,Sid,Sis,N] u0 {2,[S,D]} {4,[S,D]}
4    [CO,Cd,Cs,Sid,Sis,N] u0 {3,[S,D]} {5,[S,D]}
5    [CO,Cd,Cs,Sid,Sis,N] u0 {4,[S,D]} {6,S}
6 *2 O                    u0 {5,S} {7,S}
7 *3 O                    u0 {6,S} {8,S}
8    R!H                  u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "R5OOR_SSSS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    R!H        u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "R5OOR_SSSSCO",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3    [Cd,Cs] u0 {2,S} {4,S}
4    [Cd,Cs] u0 {3,S} {5,S}
5    CO      u0 {4,S} {6,S}
6 *2 O       u0 {5,S} {7,S}
7 *3 O       u0 {6,S} {8,S}
8    R!H     u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "R5OOR_SSSD",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    Cd         u0 {3,S} {5,D}
5    Cd         u0 {4,D} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    R!H        u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "R5OOR_SSDS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3    Cd         u0 {2,S} {4,D}
4    Cd         u0 {3,D} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    R!H        u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "R5OOR_SDSS",
    group = 
"""
1 *1 [Cd,Cs]    u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3    Cd         u0 {2,D} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    R!H        u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "R5OOR_DSSS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3    [Cd,Cs,CO] u0 {2,S} {4,S}
4    [Cd,Cs,CO] u0 {3,S} {5,S}
5    [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 O          u0 {5,S} {7,S}
7 *3 O          u0 {6,S} {8,S}
8    R!H        u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "R5OOR_SDSD",
    group = 
"""
1 *1 [Cd,Cs] u1 {2,S}
2 *4 Cd      u0 {1,S} {3,D}
3    Cd      u0 {2,D} {4,S}
4    Cd      u0 {3,S} {5,D}
5    Cd      u0 {4,D} {6,S}
6 *2 O       u0 {5,S} {7,S}
7 *3 O       u0 {6,S} {8,S}
8    R!H     u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "R5OOR_DSDS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3    Cd  u0 {2,S} {4,D}
4    Cd  u0 {3,D} {5,S}
5    Cd  u0 {4,S} {6,S}
6 *2 O   u0 {5,S} {7,S}
7 *3 O   u0 {6,S} {8,S}
8    R!H u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cd_rad_in",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cd_pri_rad_in",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cd_sec_rad_in",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2 *4 C   u0 {1,D}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cd_rad_in/NonDeC",
    group = 
"""
1 *1 C  u1 {2,D} {3,S}
2 *4 C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cd_rad_in/NonDeO",
    group = 
"""
1 *1 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cd_rad_in/NonDeN",
    group = 
"""
1 *1 C   u1 {2,D} {3,S}
2 *4 C   u0 {1,D}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cd_rad_in/OneDe",
    group = 
"""
1 *1 C             u1 {2,D} {3,S}
2 *4 C             u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cd_rad_out",
    group = 
"""
1 *1 C  u1 {2,S} {3,D}
2 *4 C  u0 {1,S}
3    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cs_rad_intra",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2 *4 C u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "C_pri_rad_intra",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4 *4 C u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "C_sec_rad_intra",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3 *4 C   u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "C_rad/H/NonDeC_intra",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3 *4 C  u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "C_rad/H/NonDeO_intra",
    group = 
"""
1 *1 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3 *4 C u0 {1,S}
4    O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "C_rad/H/NonDeN_intra",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3 *4 C   u0 {1,S}
4    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "C_rad/H/OneDe_intra",
    group = 
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4 *4 C             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "C_ter_rad_intra",
    group = 
"""
1 *1 C   u1 {2,S} {3,S} {4,S}
2 *4 C   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "C_rad/NonDeC_intra",
    group = 
"""
1 *1 C      u1 {2,S} {3,S} {4,S}
2 *4 C      u0 {1,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "C_rad/Cs3_intra",
    group = 
"""
1 *1 C  u1 {2,S} {3,S} {4,S}
2 *4 C  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "C_rad/NDMustO_intra",
    group = 
"""
1 *1 C      u1 {2,S} {3,S} {4,S}
2 *4 C      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "C_rad/OneDe_intra",
    group = 
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3 *4 C             u0 {1,S}
4    [Cs,O]        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "C_rad/Cs2_intra",
    group = 
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3 *4 C             u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "C_rad/ODMustO_intra",
    group = 
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3 *4 C             u0 {1,S}
4    O             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "C_rad/TwoDe_intra",
    group = 
"""
1 *1 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4 *4 C             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "N_rad",
    group = 
"""
1 *1 N u1
""",
    kinetics = None,
)

tree(
"""
L1: RnOO
    L2: R2OO
        L3: R2OOJ
            L4: R2OOJ_S
        L3: R2OOH
            L4: R2OOH_S
            L4: R2OOH_SCO
            L4: R2OOH_D
        L3: R2OOR
            L4: R2OOR_S
            L4: R2OOR_SCO
            L4: R2OOR_D
    L2: R3OO
        L3: R3OOJ
        L3: R3OOH
            L4: R3OOH_SS
                L5: R3OOH_SSCO
            L4: R3OOH_SD
            L4: R3OOH_DS
        L3: R3OOR
            L4: R3OOR_SS
                L5: R3OOR_SSCO
            L4: R3OOR_SD
            L4: R3OOR_DS
    L2: R4OO
        L3: R4OOJ
        L3: R4OOH
            L4: R4OOH_SSS
                L5: R4OOH_SSSCO
            L4: R4OOH_SSD
            L4: R4OOH_SDS
            L4: R4OOH_DSS
            L4: R4OOH_DSD
        L3: R4OOR
            L4: R4OOR_SSS
                L5: R4OOR_SSSCO
            L4: R4OOR_SSD
            L4: R4OOR_SDS
            L4: R4OOR_DSS
            L4: R4OOR_DSD
    L2: R5OO
        L3: R5OOJ
        L3: R5OOH
            L4: R5OOH_SSSS
                L5: R5OOH_SSSSCO
            L4: R5OOH_SSSD
            L4: R5OOH_SSDS
            L4: R5OOH_SDSS
            L4: R5OOH_DSSS
            L4: R5OOH_SDSD
            L4: R5OOH_DSDS
        L3: R5OOR
            L4: R5OOR_SSSS
                L5: R5OOR_SSSSCO
            L4: R5OOR_SSSD
            L4: R5OOR_SSDS
            L4: R5OOR_SDSS
            L4: R5OOR_DSSS
            L4: R5OOR_SDSD
            L4: R5OOR_DSDS
L1: Y_rad_intra
    L2: Cd_rad_in
        L3: Cd_pri_rad_in
        L3: Cd_sec_rad_in
            L4: Cd_rad_in/NonDeC
            L4: Cd_rad_in/NonDeO
            L4: Cd_rad_in/NonDeN
            L4: Cd_rad_in/OneDe
    L2: Cd_rad_out
    L2: Cs_rad_intra
        L3: C_pri_rad_intra
        L3: C_sec_rad_intra
            L4: C_rad/H/NonDeC_intra
            L4: C_rad/H/NonDeO_intra
            L4: C_rad/H/NonDeN_intra
            L4: C_rad/H/OneDe_intra
        L3: C_ter_rad_intra
            L4: C_rad/NonDeC_intra
                L5: C_rad/Cs3_intra
                L5: C_rad/NDMustO_intra
            L4: C_rad/OneDe_intra
                L5: C_rad/Cs2_intra
                L5: C_rad/ODMustO_intra
            L4: C_rad/TwoDe_intra
    L2: N_rad
"""
)

