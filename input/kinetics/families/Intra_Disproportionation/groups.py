#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["Y"], ownReverse=False)

reverse = "BiradFromMultipleBond"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Rn",
    group = "OR{R2, R3, R4, R5, R6, R7}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_rad",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
    shortDesc = "The abstracting radical",
)

entry(
    index = 3,
    label = "XH_Rrad",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *2 R!H u0 {1,S} {3,S}
3 *4 H   u0 {2,S}
""",
    kinetics = None,
    shortDesc = "The site with a free hydrogen on an atom adjacent to a radical"
)

entry(
    index = 4,
    label = "R3",
    group = "OR{R3radExo}",
    kinetics = None,
    longDesc = """
Aaron Vandeputte notes:
It is assumed that the other radical site (#3) is not a member of the TS ring; we may eventually want to consider the possibility
for the radical site being in the TS ring, which in certain cases, may give rise to multiple transition states for the same reaction; 
I expect that the number of cases that would be encountered where this reaction would not occur at all due to neglecting this would be small; 
UPDATE: 2,5-pentdiyl radical to 1-pentene can only occur when radical site is included in ring, so maybe this is more important than I thought
UPDATE2: I will consider possibility of Endo case, except for R3radEndo in which case the 2 rads are adjacent to each other, but I will assume 
the rate rules are the same as for the probably more typical exo case (2nd radical site not a part of ring)
    """,
)

entry(
    index = 6,
    label = "R3radExo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B]}
3 *2 R!H u0 {2,[S,D,B]} {4,S} {5,S}
4 *3 R!H u1 {3,S}
5 *4 H   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R4",
    group = "OR{R4radEndo, R4radExo}",
    kinetics = None,
)

entry(
    index = 8,
    label = "R4radEndo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3 *3 R!H u1 {2,[S,D,B,T]} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *4 H   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R4radExo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B]}
4 *2 R!H u0 {3,[S,D,B]} {5,S} {6,S}
5 *3 R!H u1 {4,S}
6 *4 H   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R5",
    group = "OR{R5radEndo, R5radExo}",
    kinetics = None,
)

entry(
    index = 11,
    label = "R5radEndo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4 *3 R!H u1 {3,[S,D,B,T]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *4 H   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R5radExo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4    R!H u0 {3,[S,D,B,T]} {5,[S,D,B]}
5 *2 R!H u0 {4,[S,D,B]} {6,S} {7,S}
6 *3 R!H u1 {5,S}
7 *4 H   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R6",
    group = "OR{R6radEndo, R6radExo}",
    kinetics = None,
)

entry(
    index = 14,
    label = "R6radEndo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4    R!H u0 {3,[S,D,B,T]} {5,[S,D,B,T]}
5 *3 R!H u1 {4,[S,D,B,T]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *4 H   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R6radExo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4    R!H u0 {3,[S,D,B,T]} {5,[S,D,B,T]}
5    R!H u0 {4,[S,D,B,T]} {6,[S,D,B]}
6 *2 R!H u0 {5,[S,D,B]} {7,S} {8,S}
7 *3 R!H u1 {6,S}
8 *4 H   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R7",
    group = "OR{R7radEndo, R7radExo}",
    kinetics = None,
)

entry(
    index = 17,
    label = "R7radEndo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4    R!H u0 {3,[S,D,B,T]} {5,[S,D,B,T]}
5    R!H u0 {4,[S,D,B,T]} {6,[S,D,B,T]}
6 *3 R!H u1 {5,[S,D,B,T]} {7,S}
7 *2 R!H u0 {6,S} {8,S}
8 *4 H   u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R7radExo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B,T]}
2    R!H u0 {1,[S,D,B,T]} {3,[S,D,B,T]}
3    R!H u0 {2,[S,D,B,T]} {4,[S,D,B,T]}
4    R!H u0 {3,[S,D,B,T]} {5,[S,D,B,T]}
5    R!H u0 {4,[S,D,B,T]} {6,[S,D,B,T]}
6    R!H u0 {5,[S,D,B,T]} {7,[S,D,B]}
7 *2 R!H u0 {6,[S,D,B]} {8,S} {9,S}
8 *3 R!H u1 {7,S}
9 *4 H   u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Y_rad_NDe",
    group = 
"""
1 *1 R!H u1 {2,S}
2 [Cs,Os,Ss] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Y_rad_De",
    group = 
"""
1 *1 R!H u1 {2,[S,D]}
2 [Cd,Cdd,Ct,CO,Cb] u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "XH_Rrad_NDe",
    group = 
"""
1 *3 R!H u1 {2,S} {4,S}
2 *2 R!H u0 {1,S} {3,S}
3 *4 H u0 {2,S}
4 [Cs,Os,Ss] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "XH_Rrad_De",
    group = 
"""
1 *3 R!H u1 {2,S} {4,[S,D]}
2 *2 R!H u0 {1,S} {3,S}
3 *4 H u0 {2,S}
4 [Cd,Cdd,Ct,CO,Cb] u0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R2",
    group = "OR{R2radExo}",
    kinetics = None,
)

entry(
    index = 24,
    label = "R2radExo",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B]}
2 *2 R!H u0 {1,[S,D,B]} {3,S} {4,S}
3 *3 R!H u1 {2,S}
4 *4 H   u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R2
	L3: R2radExo
    L2: R3
        L3: R3radExo
    L2: R4
        L3: R4radEndo
        L3: R4radExo
    L2: R5
        L3: R5radEndo
        L3: R5radExo
    L2: R6
        L3: R6radEndo
        L3: R6radExo
    L2: R7
        L3: R7radEndo
        L3: R7radExo
L1: Y_rad
    L2: Y_rad_NDe
    L2: Y_rad_De
L1: XH_Rrad
    L2: XH_Rrad_NDe
    L2: XH_Rrad_De
"""
)

forbidden(
    label = "fused5rings_1",
    group = 
"""
1 C u1 {2,S} {5,S}
2 C u0 {1,S} {3,S}
3 C u0 {2,S} {4,S}
4 C u0 {3,S} {5,S} {8,S}
5 C u0 {1,S} {4,S} {6,S}
6 C u1 {5,S} {7,S}
7 C u0 {6,S} {8,S}
8 C u0 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "fused5rings_2",
    group = 
"""
1 C u1 {2,S} {5,S}
2 C u0 {1,S} {3,S}
3 C u0 {2,S} {4,S}
4 C u0 {3,S} {5,S} {8,S}
5 C u0 {1,S} {4,S} {6,S}
6 C u0 {5,S} {7,S}
7 C u1 {6,S} {8,S}
8 C u0 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "fused5rings_3",
    group = 
"""
1 C u1 {2,S} {5,S}
2 C u0 {1,S} {3,S}
3 C u0 {2,S} {4,S}
4 C u0 {3,S} {5,S} {8,S}
5 C u0 {1,S} {4,S} {6,S}
6 C u0 {5,S} {7,S}
7 C u0 {6,S} {8,S}
8 C u1 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "fused5rings_4",
    group = 
"""
1 C u0 {2,S} {5,S}
2 C u1 {1,S} {3,S}
3 C u0 {2,S} {4,S}
4 C u0 {3,S} {5,S} {8,S}
5 C u0 {1,S} {4,S} {6,S}
6 C u0 {5,S} {7,S}
7 C u1 {6,S} {8,S}
8 C u0 {4,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

#forbidden(
#    label = "Allylicrad1",
#    group = 
#"""
#1 *1 R u1 {2,S}
#2 R u0 {1,S} {3,D}
#3 R u0 {2,D} 
#""",
#    shortDesc = u"""""",
#    longDesc = 
#u"""
#
#""",
#)


#forbidden(
#    label = "Allylicrad2",
#    group = 
#"""
#+1 *3 R u1 {2,S}
#+2 R u0 {1,S} {3,D}
#+3 R u0 {2,D} 
#""",
#    shortDesc = u"""""",
#    longDesc = 
#u"""
#
#""",
#)
