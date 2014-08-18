#!/usr/bin/env python
# encoding: utf-8

name = "Intra_RH_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open+H_Migration"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*4'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
    ['CHANGE_BOND', '*2', '-1', '*3'],
])


entry(
    index = 1,
    label = "Rn",
    group = "OR{R4, R5, R6, R7}",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",

    
)

 
entry(
    index = 2,
    label = "multiplebond_intra",
    group =
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

#entry(
#    index = 3,
#    label = "RHadd_intra",
#    group =
#"""
#1 *1 R!H 0 {2,S}
#2 *4 H 0 {1,S}
#""",
#    kinetics = None,
#    referenceType = "",
#    shortDesc = u"""""",
#    longDesc = 
#u"""
#
#""",
#    
#)

entry(
    index = 4,
    label = "R4",
    group = 
"""
1 *1 R!H      0 {2,S} {3,{S,D,T,B}}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,{S,D,T,B}} {4,S}
4 *2 C 0 {3,S} {5,D}
5 *3 C 0 {4,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 5,
    label = "R4_S",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *2 C 0 {3,S} {5,D}
5 *3 C 0 {4,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 8,
    label = "R4_D",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *2 C 0 {3,S} {5,D}
5 *3 C 0 {4,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 11,
    label = "R4_T",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *2 C 0 {3,S} {5,D}
5 *3 C 0 {4,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 14,
    label = "R4_B",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *2 C 0 {3,S} {5,D}
5 *3 C 0 {4,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =  
u"""

""",
    
)



entry(
    index = 17,
    label = "R5",
    group = "OR{R5_SS, R5_SD, R5_DS, R5_ST, R5_TS, R5_SB, R5_BS}",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)



entry(
    index = 18,
    label = "R5_SS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 20,
    label = "R5_SD",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,D}
4 *6 R!H      0 {3,D} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 23,
    label = "R5_DS",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 26,
    label = "R5_ST",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,S} {4,T}
4 *6 Ct      0 {3,T} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 29,
    label = "R5_TS",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 32,
    label = "R5_SB",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,S} {4,B}
4 *6 Cb      0 {3,B} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 35,
    label = "R5_BS",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *2 C 0 {4,S} {6,D}
6 *3 C 0 {5,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 38,
    label = "R6",
    group = "OR{R6_RSR, R6_SMS, R6_SBB, R6_BBS}",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 39,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H      0 {2,S} {3,{S,D,T,B}}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,{S,D,T,B}} {4,S}
4 *6 R!H      0 {3,S} {5,{S,D,T,B}}
5 *7 R!H      0 {4,{S,D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 40,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 R!H      0 {3,S} {5,{S,D,T,B}}
5 *7 R!H      0 {4,{S,D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 41,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *7 R!H      0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 44,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 {Cd,Ct,Cb}     0 {3,S} {5,{S,D,T,B}}
5 *7 {Cd,Ct,Cb}      0 {4,{S,D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 47,
    label = "R6_DSR",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 R!H     0 {3,S} {5,{S,D,T,B}}
5 *7 R!H      0 {4,{S,D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 48,
    label = "R6_DSS",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 R!H     0 {3,S} {5,S}
5 *7 R!H      0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 51,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H       0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 {Cd,Ct,Cb}     0 {3,S} {5,{D,T,B}}
5 *7 {Cd,Ct,Cb}     0 {4,{D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 54,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 R!H     0 {3,S} {5,{S,D,T,B}}
5 *7 R!H      0 {4,{S,D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 55,
    label = "R6_TSS",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 R!H     0 {3,S} {5,S}
5 *7 R!H      0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 58,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 {Cd,Ct,Cb}     0 {3,S} {5,{D,T,B}}
5 *7 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 61,
    label = "R6_BSR",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 R!H     0 {3,S} {5,{S,D,T,B}}
5 *7 R!H      0 {4,{S,D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 62,
    label = "R6_BSS",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 R!H     0 {3,S} {5,S}
5 *7 R!H      0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 65,
    label = "R6_BSM",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 {Cd,Ct,Cb}     0 {3,S} {5,{D,T,B}}
5 *7 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 68,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 {Cd,Ct,Cb}      0 {1,S} {4,{D,T,B}}
4 *6 {Cd,Ct,Cb}     0 {3,{D,T,B}} {5,S}
5 *7 R!H      0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 71,
    label = "R6_SBB",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,S} {4,B}
4 *6 Cbf     0 {3,B} {5,B}
5 *7 Cb      0 {4,B} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)





entry(
    index = 74,
    label = "R6_BBS",
    group = 
"""
1 *1 Cb     0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cbf      0 {1,B} {4,B}
4 *6 Cb     0 {3,B} {5,S}
5 *7 R!H      0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,D}
7 *3 C 0 {6,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 77,
    label = "R7",
    group = "OR{R7_RSSR, R7_RSMS, R7_SMSR, R7_BBSR, R7_RSBB, R7_SBBS}",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 78,
    label = "R7_RSSR",
    group = 
"""
1 *1 R!H      0 {2,S} {3,{S,D,T,B}}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,{S,D,T,B}} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 79,
    label = "R7_SSSR",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 80,
    label = "R7_SSSS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)




entry(
    index = 83,
    label = "R7_SSSM",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 {Cd,Ct,Cb}      0 {4,S} {6,{D,T,B}}
6 *7 {Cd,Ct,Cb}      0 {5,{D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 86,
    label = "R7_DSSR",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 87,
    label = "R7_DSSS",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 90,
    label = "R7_DSSM",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 {Cd,Ct,Cb}      0 {4,S} {6,{D,T,B}}
6 *7 {Cd,Ct,Cb}      0 {5,{D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 93,
    label = "R7_TSSR",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 94,
    label = "R7_TSSS",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 97,
    label = "R7_TSSM",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 {Cd,Ct,Cb}      0 {4,S} {6,{D,T,B}}
6 *7 {Cd,Ct,Cb}      0 {5,{D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)






entry(
    index = 197,
    label = "R7_BSSR",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 196,
    label = "R7_BSSS",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 R!H      0 {4,S} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 103,
    label = "R7_BSSM",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 R!H      0 {3,S} {5,S}
5 *8 {Cd,Ct,Cb}      0 {4,S} {6,{D,T,B}}
6 *7 {Cd,Ct,Cb}      0 {5,{D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 106,
    label = "R7_RSMS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,{S,D,T,B}}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,{S,D,T,B}} {4,S}
4 *6 {Cd,Ct,Cb}      0 {3,S} {5,{D,T,B}}
5 *8 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 107,
    label = "R7_SSMS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 {Cd,Ct,Cb}      0 {3,S} {5,{D,T,B}}
5 *8 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 110,
    label = "R7_DSMS",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 {Cd,Ct,Cb}      0 {3,S} {5,{D,T,B}}
5 *8 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 113,
    label = "R7_TSMS",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 {Cd,Ct,Cb}      0 {3,S} {5,{D,T,B}}
5 *8 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 116,
    label = "R7_BSMS",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 {Cd,Ct,Cb}      0 {3,S} {5,{D,T,B}}
5 *8 {Cd,Ct,Cb}      0 {4,{D,T,B}} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 119,
    label = "R7_SMSR",
    group = 
"""
1 *1 R!H       0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 {Cd,Ct,Cb}      0 {1,S} {4,{D,T,B}}
4 *6 {Cd,Ct,Cb}      0 {3,{D,T,B}} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 120,
    label = "R7_SMSS",
    group =
"""
1 *1 R!H       0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 {Cd,Ct,Cb}      0 {1,S} {4,{D,T,B}}
4 *6 {Cd,Ct,Cb}      0 {3,{D,T,B}} {5,S}
5 *8 R!H      0 {4,S} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 123,
    label = "R7_SMSM",
    group = 
"""
1 *1 R!H       0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 {Cd,Ct,Cb}      0 {1,S} {4,{D,T,B}}
4 *6 {Cd,Ct,Cb}      0 {3,{D,T,B}} {5,S}
5 *8 {Cd,Ct,Cb}      0 {4,S} {6,{D,T,B}}
6 *7 {Cd,Ct,Cb}      0 {5,{D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)



entry(
    index = 126,
    label = "R7_BBSR",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cbf      0 {1,B} {4,B}
4 *6 Cb      0 {3,B} {5,S}
5 *8 R!H      0 {4,S} {6,{S,D,T,B}}
6 *7 R!H      0 {5,{S,D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 127,
    label = "R7_BBSS",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cbf      0 {1,B} {4,B}
4 *6 Cb      0 {3,B} {5,S}
5 *8 R!H      0 {4,S} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)



entry(
    index = 130,
    label = "R7_BBSM",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cbf      0 {1,B} {4,B}
4 *6 Cb      0 {3,B} {5,S}
5 *8 {Cd,Ct,Cb}      0 {4,S} {6,{D,T,B}}
6 *7 {Cd,Ct,Cb}      0 {5,{D,T,B}} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)



entry(
    index = 133,
    label = "R7_RSBB",
    group = 
"""
1 *1 R!H      0 {2,S} {3,{S,D,T,B}}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,{S,D,T,B}} {4,S}
4 *6 Cb      0 {3,S} {5,B}
5 *8 Cbf      0 {4,B} {6,B}
6 *7 Cb      0 {5,B} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 134,
    label = "R7_SSBB",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 R!H      0 {1,S} {4,S}
4 *6 Cb      0 {3,S} {5,B}
5 *8 Cbf      0 {4,B} {6,B}
6 *7 Cb      0 {5,B} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 137,
    label = "R7_DSBB",
    group = 
"""
1 *1 Cd      0 {2,S} {3,D}
2 *4 H        0 {1,S}
3 *5 Cd      0 {1,D} {4,S}
4 *6 Cb      0 {3,S} {5,B}
5 *8 Cbf      0 {4,B} {6,B}
6 *7 Cb      0 {5,B} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 140,
    label = "R7_TSBB",
    group = 
"""
1 *1 Ct      0 {2,S} {3,T}
2 *4 H        0 {1,S}
3 *5 Ct      0 {1,T} {4,S}
4 *6 Cb      0 {3,S} {5,B}
5 *8 Cbf      0 {4,B} {6,B}
6 *7 Cb      0 {5,B} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 143,
    label = "R7_BSBB",
    group = 
"""
1 *1 Cb      0 {2,S} {3,B}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,B} {4,S}
4 *6 Cb      0 {3,S} {5,B}
5 *8 Cbf      0 {4,B} {6,B}
6 *7 Cb      0 {5,B} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)


entry(
    index = 146,
    label = "R7_SBBS",
    group = 
"""
1 *1 R!H      0 {2,S} {3,S}
2 *4 H        0 {1,S}
3 *5 Cb      0 {1,S} {4,B}
4 *6 Cbf      0 {3,B} {5,B}
5 *8 Cb      0 {4,B} {6,S}
6 *7 R!H      0 {5,S} {7,S}
7 *2 C        0 {6,S} {8,D}
8 *3 C   0 {7,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)








entry(
    index = 149,
    label = "doublebond_intra_2H",
    group =
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 150,
    label = "doublebond_intra_2H_pri",
    group = 
"""
1 *2 C 0 {2,D} {3,S}
2 *3 C 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)
entry(
    index = 151,
    label = "doublebond_intra_2H_secNd",
    group =
"""
1 *2 C     0 {2,D} {3,S}
2 *3 C     0 {1,D} {4,S} {5,S}
3    {Cs,O} 0 {1,S}
4    H      0 {2,S}
5    H      0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    
)

entry(
    index = 152,
    label = "doublebond_intra_2H_secDe",
    group =
"""
1 *2 C            0 {2,D} {3,S}
2 *3 C            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    H             0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 198,
    label = "radadd_intra",
    group =
"""
1 *1 R!H 0
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)



entry(
    index = 180,
    label = "radadd_intra_cs",
    group =
"""
1 *1 Cs 0       
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 181,
    label = "radadd_intra_cs2H",
    group =
"""
1 *1 Cs 0       {2,S} {3,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 182,
    label = "radadd_intra_csHNd",
    group =
"""
1 *1 Cs     0 {2,S} {3,S}
2 *2   H      0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 183,
    label = "radadd_intra_csHDe",
    group =
"""
1 *1 Cs            0 {2,S} {3,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 184,
    label = "radadd_intra_csNdNd",
    group =
"""
1 *1 Cs     0 {2,S} {3,S} {4,S}
2 *2 H      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 185,
    label = "radadd_intra_csNdDe",
    group =
"""
1 *1 Cs            0 {2,S} {3,S} {4,S}
2 *2 H             0 {1,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 186,
    label = "radadd_intra_csDeDe",
    group =
"""
1 *1 Cs            0 {2,S} {3,S} {4,S}
2 *2 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 187,
    label = "radadd_intra_O",
    group =
"""
1 *1 O 0
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 188,
    label = "radadd_intra_Cb",
    group =
"""
1 *1 Cb 0
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 189,
    label = "radadd_intra_cdsingle",
    group =
"""
1 *1 Cd 0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    R  0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 190,
    label = "radadd_intra_cdsingleH",
    group =
"""
1 *1 Cd 0 {2,S} {3,S}
2 *2   H  0 {1,S}
3     H  0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 191,
    label = "radadd_intra_cdsingleNd",
    group =
"""
1 *1 Cd     0 {2,S} {3,S}
2 *2   H  0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 192,
    label = "radadd_intra_cdsingleDe",
    group =
"""
1 *1 Cd            0 {2,S} {3,S}
2 *2   H  0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 193,
    label = "radadd_intra_cddouble",
    group =
"""
1 *1 Cd 0 {3,D} {2,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 194,
    label = "radadd_intra_CO",
    group =
"""
1 *1 CO 0 {3,D} {2,S}
2 *2 H  0 {1,S}
3    O  0 {1,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 195,
    label = "radadd_intra_Ct",
    group =
"""
1 *1 Ct 0 {3,T} {2,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,T}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
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
                L5: R6_SSS
                L5: R6_SSM
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
        L3: doublebond_intra_2H_pri
        L3: doublebond_intra_2H_secNd
        L3: doublebond_intra_2H_secDe
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
        L3: radadd_intra_csHDe
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
        L3: radadd_intra_csDeDe
    L2: radadd_intra_O
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
    
"""
)


#forbidden(
#    label = "bond21",
#    group =
#"""
#1 *2 R 0 {2,{S,D}}
#2 *1 R 0 {1,{S,D}}
#""",
#    shortDesc = u"""""",
#    longDesc =
#u"""
#
#""",
#    ],
#)
#
#forbidden(
#    label = "bond31",
#    group =
#"""
#1 *3 R 0 {2,{S,D}}
#2 *1 R 0 {1,{S,D}}
#""",
#    shortDesc = u"""""",
#    longDesc =
#u"""
#
#""",
#    ],
#)
#
#forbidden(
#    label = "bond34",
#    group =
#"""
#1 *3 R 0 {2,S}
#2 *4 H 0 {1,S}
#""",
#    shortDesc = u"""""",
#    longDesc =
#u"""
#
#""",
#    ],
#)
#
#
#forbidden(
#    label = "cdd2",
#    group =
#"""
#1 *2 Cdd 0
#""",
#    shortDesc = u"""""",
#    longDesc =
#u"""
#
#""",
#    ],
#)
#
#
#