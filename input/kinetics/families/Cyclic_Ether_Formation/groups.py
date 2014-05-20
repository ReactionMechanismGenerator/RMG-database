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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Y_rad_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "R2OO",
    group = "OR{R2OOH, R2OOR, R2OOJ}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R2OOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,S}
3 *2 O                    U0 {2,S} {4,S}
4 *3 O                    U1 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R2OOJ_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U1 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R2OOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,S}
3 *2 O                    U0 {2,S} {4,S}
4 *3 O                    U0 {3,S} {5,S}
5    H                    U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R2OOH_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U0 {3,S} {5,S}
5    H       U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R2OOH_SCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 CO      U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U0 {3,S} {5,S}
5    H       U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R2OOH_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,D}
2 *4 Cd U0 {1,D} {3,S}
3 *2 O  U0 {2,S} {4,S}
4 *3 O  U0 {3,S} {5,S}
5    H  U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R2OOR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,S}
3 *2 O                    U0 {2,S} {4,S}
4 *3 O                    U0 {3,S} {5,S}
5    R!H                  U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R2OOR_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U0 {3,S} {5,S}
5    R!H     U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R2OOR_SCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 CO      U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U0 {3,S} {5,S}
5    R!H     U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R2OOR_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *2 O   U0 {2,S} {4,S}
4 *3 O   U0 {3,S} {5,S}
5    R!H U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R3OO",
    group = "OR{R3OOH, R3OOR, R3OOJ}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R3OOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,S}
4 *2 O                    U0 {3,S} {5,S}
5 *3 O                    U1 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R3OOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,S}
4 *2 O                    U0 {3,S} {5,S}
5 *3 O                    U0 {4,S} {6,S}
6    H                    U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R3OOH_SS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4 *2 O          U0 {3,S} {5,S}
5 *3 O          U0 {4,S} {6,S}
6    H          U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R3OOH_SSCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    CO      U0 {2,S} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    H       U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R3OOH_SD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 Cd      U0 {1,S} {3,D}
3    Cd      U0 {2,D} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    H       U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R3OOH_DS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4 *2 O          U0 {3,S} {5,S}
5 *3 O          U0 {4,S} {6,S}
6    H          U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R3OOR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,S}
4 *2 O                    U0 {3,S} {5,S}
5 *3 O                    U0 {4,S} {6,S}
6    R!H                  U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R3OOR_SS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4 *2 O          U0 {3,S} {5,S}
5 *3 O          U0 {4,S} {6,S}
6    R!H        U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "R3OOR_SSCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    CO      U0 {2,S} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    R!H     U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "R3OOR_SD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 Cd      U0 {1,S} {3,D}
3    Cd      U0 {2,D} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    R!H     U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "R3OOR_DS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4 *2 O          U0 {3,S} {5,S}
5 *3 O          U0 {4,S} {6,S}
6    R!H        U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "R4OO",
    group = "OR{R4OOH, R4OOR, R4OOJ}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "R4OOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,{S,D}}
4    {CO,Cd,Cs,Sid,Sis,N} U0 {3,{S,D}} {5,S}
5 *2 O                    U0 {4,S} {6,S}
6 *3 O                    U1 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "R4OOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,{S,D}}
4    {CO,Cd,Cs,Sid,Sis,N} U0 {3,{S,D}} {5,S}
5 *2 O                    U0 {4,S} {6,S}
6 *3 O                    U0 {5,S} {7,S}
7    H                    U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "R4OOH_SSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5 *2 O          U0 {4,S} {6,S}
6 *3 O          U0 {5,S} {7,S}
7    H          U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "R4OOH_SSSCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    CO      U0 {3,S} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    H       U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "R4OOH_SSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    Cd      U0 {2,S} {4,D}
4    Cd      U0 {3,D} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    H       U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "R4OOH_SDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 Cd         U0 {1,S} {3,D}
3    Cd         U0 {2,D} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5 *2 O          U0 {4,S} {6,S}
6 *3 O          U0 {5,S} {7,S}
7    H          U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "R4OOH_DSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5 *2 O          U0 {4,S} {6,S}
6 *3 O          U0 {5,S} {7,S}
7    H          U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "R4OOH_DSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,D}
2 *4 Cd U0 {1,D} {3,S}
3    Cd U0 {2,S} {4,D}
4    Cd U0 {3,D} {5,S}
5 *2 O  U0 {4,S} {6,S}
6 *3 O  U0 {5,S} {7,S}
7    H  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "R4OOR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,{S,D}}
4    {CO,Cd,Cs,Sid,Sis,N} U0 {3,{S,D}} {5,S}
5 *2 O                    U0 {4,S} {6,S}
6 *3 O                    U0 {5,S} {7,S}
7    R!H                  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "R4OOR_SSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5 *2 O          U0 {4,S} {6,S}
6 *3 O          U0 {5,S} {7,S}
7    R!H        U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "R4OOR_SSSCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    CO      U0 {3,S} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    R!H     U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "R4OOR_SSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    Cd      U0 {2,S} {4,D}
4    Cd      U0 {3,D} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    R!H     U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "R4OOR_SDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 Cd         U0 {1,S} {3,D}
3    Cd         U0 {2,D} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5 *2 O          U0 {4,S} {6,S}
6 *3 O          U0 {5,S} {7,S}
7    R!H        U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "R4OOR_DSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5 *2 O          U0 {4,S} {6,S}
6 *3 O          U0 {5,S} {7,S}
7    R!H        U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "R4OOR_DSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3    Cd  U0 {2,S} {4,D}
4    Cd  U0 {3,D} {5,S}
5 *2 O   U0 {4,S} {6,S}
6 *3 O   U0 {5,S} {7,S}
7    R!H U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "R5OO",
    group = "OR{R5OOH, R5OOR, R5OOJ}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "R5OOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,{S,D}}
4    {CO,Cd,Cs,Sid,Sis,N} U0 {3,{S,D}} {5,{S,D}}
5    {CO,Cd,Cs,Sid,Sis,N} U0 {4,{S,D}} {6,S}
6 *2 O                    U0 {5,S} {7,S}
7 *3 O                    U1 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "R5OOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,{S,D}}
4    {CO,Cd,Cs,Sid,Sis,N} U0 {3,{S,D}} {5,{S,D}}
5    {CO,Cd,Cs,Sid,Sis,N} U0 {4,{S,D}} {6,S}
6 *2 O                    U0 {5,S} {7,S}
7 *3 O                    U0 {6,S} {8,S}
8    H                    U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "R5OOH_SSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    H          U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "R5OOH_SSSSCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    {Cd,Cs} U0 {3,S} {5,S}
5    CO      U0 {4,S} {6,S}
6 *2 O       U0 {5,S} {7,S}
7 *3 O       U0 {6,S} {8,S}
8    H       U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "R5OOH_SSSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    Cd         U0 {3,S} {5,D}
5    Cd         U0 {4,D} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    H          U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "R5OOH_SSDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    Cd         U0 {2,S} {4,D}
4    Cd         U0 {3,D} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    H          U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "R5OOH_SDSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 Cd         U0 {1,S} {3,D}
3    Cd         U0 {2,D} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    H          U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "R5OOH_DSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    H          U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "R5OOH_SDSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 Cd      U0 {1,S} {3,D}
3    Cd      U0 {2,D} {4,S}
4    Cd      U0 {3,S} {5,D}
5    Cd      U0 {4,D} {6,S}
6 *2 O       U0 {5,S} {7,S}
7 *3 O       U0 {6,S} {8,S}
8    H       U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "R5OOH_DSDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,D}
2 *4 Cd U0 {1,D} {3,S}
3    Cd U0 {2,S} {4,D}
4    Cd U0 {3,D} {5,S}
5    Cd U0 {4,S} {6,S}
6 *2 O  U0 {5,S} {7,S}
7 *3 O  U0 {6,S} {8,S}
8    H  U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "R5OOR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {CO,Cd,Cs,Sid,Sis,N} U1 {2,{S,D}}
2 *4 {CO,Cd,Cs,Sid,Sis,N} U0 {1,{S,D}} {3,{S,D}}
3    {CO,Cd,Cs,Sid,Sis,N} U0 {2,{S,D}} {4,{S,D}}
4    {CO,Cd,Cs,Sid,Sis,N} U0 {3,{S,D}} {5,{S,D}}
5    {CO,Cd,Cs,Sid,Sis,N} U0 {4,{S,D}} {6,S}
6 *2 O                    U0 {5,S} {7,S}
7 *3 O                    U0 {6,S} {8,S}
8    R!H                  U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "R5OOR_SSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    R!H        U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "R5OOR_SSSSCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    {Cd,Cs} U0 {3,S} {5,S}
5    CO      U0 {4,S} {6,S}
6 *2 O       U0 {5,S} {7,S}
7 *3 O       U0 {6,S} {8,S}
8    R!H     U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "R5OOR_SSSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    Cd         U0 {3,S} {5,D}
5    Cd         U0 {4,D} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    R!H        U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "R5OOR_SSDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 {Cd,Cs}    U0 {1,S} {3,S}
3    Cd         U0 {2,S} {4,D}
4    Cd         U0 {3,D} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    R!H        U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "R5OOR_SDSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs}    U1 {2,S}
2 *4 Cd         U0 {1,S} {3,D}
3    Cd         U0 {2,D} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    R!H        U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "R5OOR_DSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3    {Cd,Cs,CO} U0 {2,S} {4,S}
4    {Cd,Cs,CO} U0 {3,S} {5,S}
5    {Cd,Cs,CO} U0 {4,S} {6,S}
6 *2 O          U0 {5,S} {7,S}
7 *3 O          U0 {6,S} {8,S}
8    R!H        U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "R5OOR_SDSD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 Cd      U0 {1,S} {3,D}
3    Cd      U0 {2,D} {4,S}
4    Cd      U0 {3,S} {5,D}
5    Cd      U0 {4,D} {6,S}
6 *2 O       U0 {5,S} {7,S}
7 *3 O       U0 {6,S} {8,S}
8    R!H     U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "R5OOR_DSDS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3    Cd  U0 {2,S} {4,D}
4    Cd  U0 {3,D} {5,S}
5    Cd  U0 {4,S} {6,S}
6 *2 O   U0 {5,S} {7,S}
7 *3 O   U0 {6,S} {8,S}
8    R!H U0 {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "N_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "Cd_rad_in",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2 *4 C U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "Cd_pri_rad_in",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2 *4 C U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Cd_sec_rad_in",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2 *4 C   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "Cd_rad_in/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,D} {3,S}
2 *4 C  U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "Cd_rad_in/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2 *4 C U0 {1,D}
3    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "Cd_rad_in/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2 *4 C   U0 {1,D}
3    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "Cd_rad_in/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,D} {3,S}
2 *4 C             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Cd_rad_out",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,D}
2 *4 C  U0 {1,S}
3    Cd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cs_rad_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2 *4 C U0 {1,S}
3    R U0 {1,S}
4    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C_pri_rad_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4 *4 C U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C_sec_rad_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    H   U0 {1,S}
3 *4 C   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C_rad/H/NonDeC_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3 *4 C  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C_rad/H/NonDeO_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3 *4 C U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C_rad/H/NonDeN_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    H   U0 {1,S}
3 *4 C   U0 {1,S}
4    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C_rad/H/OneDe_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4 *4 C             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C_ter_rad_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2 *4 C   U0 {1,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C_rad/NonDeC_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,S} {3,S} {4,S}
2 *4 C      U0 {1,S}
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
    index = 68,
    label = "C_rad/Cs3_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2 *4 C  U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C_rad/NDMustO_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,S} {3,S} {4,S}
2 *4 C      U0 {1,S}
3    O      U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C_rad/OneDe_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3 *4 C             U0 {1,S}
4    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C_rad/Cs2_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3 *4 C             U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C_rad/ODMustO_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3 *4 C             U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C_rad/TwoDe_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4 *4 C             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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
            L4: R3OOH_SSCO
            L4: R3OOH_SD
            L4: R3OOH_DS
        L3: R3OOR
            L4: R3OOR_SS
            L4: R3OOR_SSCO
            L4: R3OOR_SD
            L4: R3OOR_DS
    L2: R4OO
        L3: R4OOJ
        L3: R4OOH
            L4: R4OOH_SSS
            L4: R4OOH_SSSCO
            L4: R4OOH_SSD
            L4: R4OOH_SDS
            L4: R4OOH_DSS
            L4: R4OOH_DSD
        L3: R4OOR
            L4: R4OOR_SSS
            L4: R4OOR_SSSCO
            L4: R4OOR_SSD
            L4: R4OOR_SDS
            L4: R4OOR_DSS
            L4: R4OOR_DSD
    L2: R5OO
        L3: R5OOJ
        L3: R5OOH
            L4: R5OOH_SSSS
            L4: R5OOH_SSSSCO
            L4: R5OOH_SSSD
            L4: R5OOH_SSDS
            L4: R5OOH_SDSS
            L4: R5OOH_DSSS
            L4: R5OOH_SDSD
            L4: R5OOH_DSDS
        L3: R5OOR
            L4: R5OOR_SSSS
            L4: R5OOR_SSSSCO
            L4: R5OOR_SSSD
            L4: R5OOR_SSDS
            L4: R5OOR_SDSS
            L4: R5OOR_DSSS
            L4: R5OOR_SDSD
            L4: R5OOR_DSDS
L1: Y_rad_intra
    L2: N_rad
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
"""
)

