#!/usr/bin/env python
# encoding: utf-8

name = "Intra_RH_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open+H_Migration"

reversible = True

only_reverse = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*2', '-1', '*3'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Rn",
    group = "OR{R4, R5, R6, R7}",
    kinetics = None,
)

entry(
    index = 1,
    label = "multiplebond_intra",
    group = 
"""
1 *2 C u0 {2,D}
2 *3 C u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "radadd_intra",
    group = 
"""
1 *1 R!H u0 {2,S}
2 *4 H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R4",
    group = 
"""
1 *1 R!H u0 {2,S} {3,[S,D,T,B]}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,[S,D,T,B]} {4,S}
4 *2 C   u0 {3,S} {5,D}
5 *3 C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R4_S",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *2 C   u0 {3,S} {5,D}
5 *3 C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R4_D",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *2 C   u0 {3,S} {5,D}
5 *3 C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R4_T",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *2 C   u0 {3,S} {5,D}
5 *3 C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R4_B",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *2 C   u0 {3,S} {5,D}
5 *3 C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R5",
    group = "OR{R5_SS, R5_SD, R5_DS, R5_ST, R5_TS, R5_SB, R5_BS}",
    kinetics = None,
)

entry(
    index = 9,
    label = "R5_SS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R5_SD",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,D}
4 *6 R!H u0 {3,D} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "R5_DS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R5_ST",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,S} {4,T}
4 *6 Ct  u0 {3,T} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R5_TS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R5_SB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,S} {4,B}
4 *6 Cb  u0 {3,B} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R5_BS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *2 C   u0 {4,S} {6,D}
6 *3 C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R6",
    group = "OR{R6_RSR, R6_SMS, R6_SBB, R6_BBS}",
    kinetics = None,
)

entry(
    index = 17,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,[S,D,T,B]}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,[S,D,T,B]} {4,S}
4 *6 R!H u0 {3,S} {5,[S,D,T,B]}
5 *7 R!H u0 {4,[S,D,T,B]} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *6 R!H u0 {3,S} {5,[S,D,T,B]}
5 *7 R!H u0 {4,[S,D,T,B]} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 R!H        u0 {1,S} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[S,D,T,B]}
5 *7 [Cd,Ct,Cb] u0 {4,[S,D,T,B]} {6,S}
6 *2 C          u0 {5,S} {7,D}
7 *3 C          u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *7 R!H u0 {4,S} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "R6_DSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *6 R!H u0 {3,S} {5,[S,D,T,B]}
5 *7 R!H u0 {4,[S,D,T,B]} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R6_DSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *7 R!H u0 {4,S} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R6_DSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,D}
2 *4 H          u0 {1,S}
3 *5 Cd         u0 {1,D} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *7 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 C          u0 {5,S} {7,D}
7 *3 C          u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R6_TSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *6 R!H u0 {3,S} {5,[S,D,T,B]}
5 *7 R!H u0 {4,[S,D,T,B]} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R6_TSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *7 R!H u0 {4,S} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R6_TSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,T}
2 *4 H          u0 {1,S}
3 *5 Ct         u0 {1,T} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *7 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 C          u0 {5,S} {7,D}
7 *3 C          u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R6_BSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *6 R!H u0 {3,S} {5,[S,D,T,B]}
5 *7 R!H u0 {4,[S,D,T,B]} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R6_BSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *7 R!H u0 {4,S} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R6_BSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,B}
2 *4 H          u0 {1,S}
3 *5 Cb         u0 {1,B} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *7 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 C          u0 {5,S} {7,D}
7 *3 C          u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 [Cd,Ct,Cb] u0 {1,S} {4,[D,T,B]}
4 *6 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *7 R!H        u0 {4,S} {6,S}
6 *2 C          u0 {5,S} {7,D}
7 *3 C          u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R6_SBB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,S} {4,B}
4 *6 Cbf u0 {3,B} {5,B}
5 *7 Cb  u0 {4,B} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "R6_BBS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cbf u0 {1,B} {4,B}
4 *6 Cb  u0 {3,B} {5,S}
5 *7 R!H u0 {4,S} {6,S}
6 *2 C   u0 {5,S} {7,D}
7 *3 C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "R7",
    group = "OR{R7_RSSR, R7_RSMS, R7_SMSR, R7_BBSR, R7_RSBB, R7_SBBS}",
    kinetics = None,
)

entry(
    index = 34,
    label = "R7_RSSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,[S,D,T,B]}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,[S,D,T,B]} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H u0 {5,[S,D,T,B]} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "R7_SSSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H u0 {5,[S,D,T,B]} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "R7_SSSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,S}
6 *7 R!H u0 {5,S} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R7_SSSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 R!H        u0 {1,S} {4,S}
4 *6 R!H        u0 {3,S} {5,S}
5 *8 [Cd,Ct,Cb] u0 {4,S} {6,[D,T,B]}
6 *7 [Cd,Ct,Cb] u0 {5,[D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R7_DSSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H u0 {5,[S,D,T,B]} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "R7_DSSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,S}
6 *7 R!H u0 {5,S} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "R7_DSSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,D}
2 *4 H          u0 {1,S}
3 *5 Cd         u0 {1,D} {4,S}
4 *6 R!H        u0 {3,S} {5,S}
5 *8 [Cd,Ct,Cb] u0 {4,S} {6,[D,T,B]}
6 *7 [Cd,Ct,Cb] u0 {5,[D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "R7_TSSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H u0 {5,[S,D,T,B]} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "R7_TSSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,S}
6 *7 R!H u0 {5,S} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "R7_TSSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,T}
2 *4 H          u0 {1,S}
3 *5 Ct         u0 {1,T} {4,S}
4 *6 R!H        u0 {3,S} {5,S}
5 *8 [Cd,Ct,Cb] u0 {4,S} {6,[D,T,B]}
6 *7 [Cd,Ct,Cb] u0 {5,[D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "R7_BSSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H u0 {5,[S,D,T,B]} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "R7_BSSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *6 R!H u0 {3,S} {5,S}
5 *8 R!H u0 {4,S} {6,S}
6 *7 R!H u0 {5,S} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "R7_BSSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,B}
2 *4 H          u0 {1,S}
3 *5 Cb         u0 {1,B} {4,S}
4 *6 R!H        u0 {3,S} {5,S}
5 *8 [Cd,Ct,Cb] u0 {4,S} {6,[D,T,B]}
6 *7 [Cd,Ct,Cb] u0 {5,[D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "R7_RSMS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,[S,D,T,B]}
2 *4 H          u0 {1,S}
3 *5 R!H        u0 {1,[S,D,T,B]} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *8 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *7 R!H        u0 {5,S} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "R7_SSMS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 R!H        u0 {1,S} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *8 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *7 R!H        u0 {5,S} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "R7_DSMS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,D}
2 *4 H          u0 {1,S}
3 *5 Cd         u0 {1,D} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *8 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *7 R!H        u0 {5,S} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "R7_TSMS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,T}
2 *4 H          u0 {1,S}
3 *5 Ct         u0 {1,T} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *8 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *7 R!H        u0 {5,S} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "R7_BSMS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,B}
2 *4 H          u0 {1,S}
3 *5 Cb         u0 {1,B} {4,S}
4 *6 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *8 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *7 R!H        u0 {5,S} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "R7_SMSR",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 [Cd,Ct,Cb] u0 {1,S} {4,[D,T,B]}
4 *6 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *8 R!H        u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H        u0 {5,[S,D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "R7_SMSS",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 [Cd,Ct,Cb] u0 {1,S} {4,[D,T,B]}
4 *6 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *8 R!H        u0 {4,S} {6,S}
6 *7 R!H        u0 {5,S} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "R7_SMSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,S}
2 *4 H          u0 {1,S}
3 *5 [Cd,Ct,Cb] u0 {1,S} {4,[D,T,B]}
4 *6 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *8 [Cd,Ct,Cb] u0 {4,S} {6,[D,T,B]}
6 *7 [Cd,Ct,Cb] u0 {5,[D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "R7_BBSR",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cbf u0 {1,B} {4,B}
4 *6 Cb  u0 {3,B} {5,S}
5 *8 R!H u0 {4,S} {6,[S,D,T,B]}
6 *7 R!H u0 {5,[S,D,T,B]} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "R7_BBSS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cbf u0 {1,B} {4,B}
4 *6 Cb  u0 {3,B} {5,S}
5 *8 R!H u0 {4,S} {6,S}
6 *7 R!H u0 {5,S} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "R7_BBSM",
    group = 
"""
1 *1 R!H        u0 {2,S} {3,B}
2 *4 H          u0 {1,S}
3 *5 Cbf        u0 {1,B} {4,B}
4 *6 Cb         u0 {3,B} {5,S}
5 *8 [Cd,Ct,Cb] u0 {4,S} {6,[D,T,B]}
6 *7 [Cd,Ct,Cb] u0 {5,[D,T,B]} {7,S}
7 *2 C          u0 {6,S} {8,D}
8 *3 C          u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "R7_RSBB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,[S,D,T,B]}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,[S,D,T,B]} {4,S}
4 *6 Cb  u0 {3,S} {5,B}
5 *8 Cbf u0 {4,B} {6,B}
6 *7 Cb  u0 {5,B} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "R7_SSBB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 R!H u0 {1,S} {4,S}
4 *6 Cb  u0 {3,S} {5,B}
5 *8 Cbf u0 {4,B} {6,B}
6 *7 Cb  u0 {5,B} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "R7_DSBB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3 *5 Cd  u0 {1,D} {4,S}
4 *6 Cb  u0 {3,S} {5,B}
5 *8 Cbf u0 {4,B} {6,B}
6 *7 Cb  u0 {5,B} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "R7_TSBB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,T}
2 *4 H   u0 {1,S}
3 *5 Ct  u0 {1,T} {4,S}
4 *6 Cb  u0 {3,S} {5,B}
5 *8 Cbf u0 {4,B} {6,B}
6 *7 Cb  u0 {5,B} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R7_BSBB",
    group = 
"""
1 *1 R!H u0 {2,S} {3,B}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,B} {4,S}
4 *6 Cb  u0 {3,S} {5,B}
5 *8 Cbf u0 {4,B} {6,B}
6 *7 Cb  u0 {5,B} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R7_SBBS",
    group = 
"""
1 *1 R!H u0 {2,S} {3,S}
2 *4 H   u0 {1,S}
3 *5 Cb  u0 {1,S} {4,B}
4 *6 Cbf u0 {3,B} {5,B}
5 *8 Cb  u0 {4,B} {6,S}
6 *7 R!H u0 {5,S} {7,S}
7 *2 C   u0 {6,S} {8,D}
8 *3 C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "doublebond_intra_2H",
    group = 
"""
1 *2 C u0 {2,D}
2 *3 C u0 {1,D} {3,S} {4,S}
3    H u0 {2,S}
4    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "doublebond_intra_2H_secDe",
    group = 
"""
1 *2 C                u0 {2,D} {3,S}
2 *3 C                u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "doublebond_intra_2H_secNd",
    group = 
"""
1 *2 C        u0 {2,D} {3,S}
2 *3 C        u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "doublebond_intra_2H_pri",
    group = 
"""
1 *2 C u0 {2,D} {3,S}
2 *3 C u0 {1,D} {4,S} {5,S}
3    H u0 {1,S}
4    H u0 {2,S}
5    H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u0 {2,S}
2 *4 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs         u0 {2,S} {3,S} {4,S}
2 *4 H          u0 {1,S}
3    [Cs,O,S2s] u0 {1,S}
4    [Cs,O,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs               u0 {2,S} {3,S} {4,S}
2 *4 H                u0 {1,S}
3    [Cs,O,S2s]       u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs               u0 {2,S} {3,S} {4,S}
2 *4 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "radadd_intra_cs2H",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S}
2 *4 H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "radadd_intra_csHHNd",
    group = 
"""
1 *1 Cs         u0 {2,S} {3,S} {4,S}
2 *4 H          u0 {1,S}
3    [Cs,O,S2s] u0 {1,S}
4    H          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "radadd_intra_csHHDe",
    group = 
"""
1 *1 Cs               u0 {2,S} {3,S} {4,S}
2 *4 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u0 {2,S}
2 *4 H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u0 {2,S}
2 *4 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u0 {2,S} {3,S}
2 *4 H  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd  u0 {2,S} {3,D}
2 *4 H   u0 {1,S}
3    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u0 {2,S} {3,D}
2 *4 H  u0 {1,S}
3    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct u0 {2,S}
2 *4 H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "radadd_intra_CS",
    group = 
"""
1 *1 CS u0 {2,S} {3,D}
2 *4 H  u0 {1,S}
3    S  u0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R4
        L3: R4_S
        L3: R4_D
        L3: R4_T
        L3: R4_B
    L2: R5
        L3: R5_SS
        L3: R5_SD
        L3: R5_DS
        L3: R5_ST
        L3: R5_TS
        L3: R5_SB
        L3: R5_BS
    L2: R6
        L3: R6_RSR
            L4: R6_SSR
                L5: R6_SSM
                L5: R6_SSS
            L4: R6_DSR
                L5: R6_DSS
                L5: R6_DSM
            L4: R6_TSR
                L5: R6_TSS
                L5: R6_TSM
            L4: R6_BSR
                L5: R6_BSS
                L5: R6_BSM
        L3: R6_SMS
        L3: R6_SBB
        L3: R6_BBS
    L2: R7
        L3: R7_RSSR
            L4: R7_SSSR
                L5: R7_SSSS
                L5: R7_SSSM
            L4: R7_DSSR
                L5: R7_DSSS
                L5: R7_DSSM
            L4: R7_TSSR
                L5: R7_TSSS
                L5: R7_TSSM
            L4: R7_BSSR
                L5: R7_BSSS
                L5: R7_BSSM
        L3: R7_RSMS
            L4: R7_SSMS
            L4: R7_DSMS
            L4: R7_TSMS
            L4: R7_BSMS
        L3: R7_SMSR
            L4: R7_SMSS
            L4: R7_SMSM
        L3: R7_BBSR
            L4: R7_BBSS
            L4: R7_BBSM
        L3: R7_RSBB
            L4: R7_SSBB
            L4: R7_DSBB
            L4: R7_TSBB
            L4: R7_BSBB
        L3: R7_SBBS
L1: multiplebond_intra
    L2: doublebond_intra_2H
        L3: doublebond_intra_2H_secDe
        L3: doublebond_intra_2H_secNd
        L3: doublebond_intra_2H_pri
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
        L3: radadd_intra_csDeDe
        L3: radadd_intra_cs2H
            L4: radadd_intra_csHHNd
            L4: radadd_intra_csHHDe
    L2: radadd_intra_O
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
    L2: radadd_intra_CS
"""
)

