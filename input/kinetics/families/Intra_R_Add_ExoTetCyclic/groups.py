#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_ExoTetcyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["R1_rad_R2_R3"], products=["R1_R2_Cycle", "R3_rad"], ownReverse=False)

reverse = "Ring_Open_Rad_Addition"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "R1_rad_R2_R3",
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
1 *2 {C,O}     0 {2,S}
2 *3 {C,O} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

entry(
    index = 3,
    label = "radadd_intra",
    group =
"""
1 *1 R!H 1
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 4,
    label = "R4",
    group =
"""
1 *1 R!H              1 {2,{S,D,T,B}}
2 *4 R!H              0 {1,{S,D,T,B}} {3,S}
3 *2 {C,O}               0 {2,S} {4,S}
4 *3 {C,O}         0 {3,S}
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
1 *1 R!H              1 {2,S}
2 *4 R!H              0 {1,S} {3,S}
3 *2 {C,O}               0 {2,S} {4,S}
4 *3 {C,O}         0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )



entry(
    index = 7,
    label = "R4_S_Cs",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 {C,O}  0 {2,S} {4,S}
4 *3 C  0 {3,S}
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
    label = "R4_S_O",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 {C,O}  0 {2,S} {4,S}
4 *3 O  0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )


entry(
    index = 9,
    label = "R4_D",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 {C,O} 0 {3,S}
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
    label = "R4_D_Cs",
    group =
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 C 0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 12,
    label = "R4_D_O",
    group =
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 O 0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 13,
    label = "R4_T",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 {C,O} 0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )



entry(
    index = 15,
    label = "R4_T_Cs",
    group =
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 C 0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 16,
    label = "R4_T_O",
    group =
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 O 0 {3,S}
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
    label = "R4_B",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 {C,O} 0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )



entry(
    index = 19,
    label = "R4_B_Cs",
    group =
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 C 0 {3,S}
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
    label = "R4_B_O",
    group =
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 {C,O} 0 {2,S} {4,S}
4 *3 O 0 {3,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 21,
    label = "R5",
    group = 
"""
1 *1 R!H           1           {2,{S,D,T,B}}
2 *4 R!H           X {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *5 R!H           X {2,{S,D,T,B}} {4,S}
4 *2 {C,O}    0           {3,S} {5,S}
5 *3 {C,O} 0           {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 22,
    label = "R5_SS",
    group = 
"""
1 *1 R!H              1 {2,S}
2 *4 R!H              0 {1,S} {3,S}
3 *5 R!H              0 {2,S} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )



entry(
    index = 24,
    label = "R5_SS_Cs",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 25,
    label = "R5_SS_O",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
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
    label = "R5_SD",
    group =
"""
1 *1 R!H              1 {2,S}
2 *4 Cd               0 {1,S} {3,D}
3 *5 Cd               0 {2,D} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )



entry(
    index = 28,
    label = "R5_SD_Cs",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
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
    label = "R5_SD_O",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 30,
    label = "R5_DS",
    group =
"""
1 *1 Cd               1 {2,D}
2 *4 Cd               0 {1,D} {3,S}
3 *5 R!H              0 {2,S} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
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
    label = "R5_DS_Cs",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 33,
    label = "R5_DS_O",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 34,
    label = "R5_ST",
    group =
"""
1 *1 R!H              1 {2,S}
2 *4 Ct               0 {1,S} {3,T}
3 *5 Ct               0 {2,T} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )



entry(
    index = 36,
    label = "R5_ST_Cs",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *5 Ct  0 {2,T} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 37,
    label = "R5_ST_O",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *5 Ct  0 {2,T} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
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
    label = "R5_TS",
    group =
"""
1 *1 Ct               1 {2,T}
2 *4 Ct               0 {1,T} {3,S}
3 *5 R!H              0 {2,S} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
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
    label = "R5_TS_Cs",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
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
    label = "R5_TS_O",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 42,
    label = "R5_SB",
    group =
"""
1 *1 R!H              1 {2,S}
2 *4 Cb               0 {1,S} {3,B}
3 *5 Cb               0 {2,B} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
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
    label = "R5_SB_Cs",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 45,
    label = "R5_SB_O",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 46,
    label = "R5_BS",
    group =
"""
1 *1 Cb               1 {2,B}
2 *4 Cb               0 {1,B} {3,S}
3 *5 R!H              0 {2,S} {4,S}
4 *2 {C,O}     0 {3,S} {5,S}
5 *3 {C,O} 0 {4,S}
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
    label = "R5_BS_Cs",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 C  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 49,
    label = "R5_BS_O",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 {C,O}  0 {3,S} {5,S}
5 *3 O  0 {4,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 50,
    label = "R6",
    group = 
"""
1 *1 R!H           1           {2,{S,D,T,B}}
2 *4 R!H           X {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H           X {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *5 R!H           X {3,{S,D,T,B}} {5,S}
5 *2 {C,O}    0           {4,S} {6,S}
6 *3 {C,O} 0           {5,S}
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
    label = "R6_RSR",
    group = 
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3 *6 R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {C,O}    0           {4,S} {6,S}
6 *3 {C,O} 0           {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 52,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 53,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_SSS_Cs",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O}  0 {4,S} {6,S}
6 *3 C  0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 56,
    label = "R6_SSS_O",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O}  0 {4,S} {6,S}
6 *3 O  0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 57,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 59,
    label = "R6_SSM_Cs",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O}         0 {4,S} {6,S}
6 *3 C         0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 60,
    label = "R6_SSM_O",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O}         0 {4,S} {6,S}
6 *3 O         0 {5,S}
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
    label = "R6_DSR",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_DSS",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 64,
    label = "R6_DSS_Cs",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O}  0 {4,S} {6,S}
6 *3 C  0 {5,S}
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
    label = "R6_DSS_O",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O}  0 {4,S} {6,S}
6 *3 O  0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 66,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_DSM_Cs",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O}         0 {4,S} {6,S}
6 *3 C         0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 69,
    label = "R6_DSM_O",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O}         0 {4,S} {6,S}
6 *3 O         0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 70,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_TSS",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 73,
    label = "R6_TSS_Cs",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
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
    label = "R6_TSS_O",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 75,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_TSM_Cs",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 78,
    label = "R6_TSM_O",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
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
    label = "R6_BSR",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_BSS",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 82,
    label = "R6_BSS_Cs",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
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
    label = "R6_BSS_O",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 84,
    label = "R6_BSM",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_BSM_Cs",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
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
    label = "R6_BSM_O",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 88,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_SMS_Cs",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 91,
    label = "R6_SMS_O",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 92,
    label = "R6_SBB",
    group = 
"""
1 *1 R!H              1 {2,S}
2 *4 Cb               0 {1,S} {3,B}
3 *6 Cbf              0 {2,B} {4,B}
4 *5 Cb               0 {3,B} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
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
    label = "R6_SBB_Cs",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 95,
    label = "R6_SBB_O",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 96,
    label = "R6_BBS",
    group = 
"""
1 *1 Cb               1 {2,B}
2 *4 Cbf              0 {1,B} {3,B}
3 *6 Cb               0 {2,B} {4,S}
4 *5 R!H              0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 {C,O} 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 98,
    label = "R6_BBS_Cs",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 C 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 99,
    label = "R6_BBS_O",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 {C,O} 0 {4,S} {6,S}
6 *3 O 0 {5,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 100,
    label = "R7",
    group = 
"""
1 *1 R!H        1           {2,{S,D,T,B}}
2 *4 R!H        X {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H        X {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *7 R!H        X {3,{S,D,T,B}} {5,{S,D,T,B}}
5 *5 R!H        X {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 101,
    label = "R7_RSSR",
    group = 
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 102,
    label = "R7_SSSR",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_SSSS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 105,
    label = "R7_SSSS_Cs",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_SSSS_O",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_SSSM",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 109,
    label = "R7_SSSM_Cs",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_SSSM_O",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 111,
    label = "R7_DSSR",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 112,
    label = "R7_DSSS",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 114,
    label = "R7_DSSS_Cs",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 115,
    label = "R7_DSSS_O",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_DSSM",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 118,
    label = "R7_DSSM_Cs",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_DSSM_O",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_TSSR",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 121,
    label = "R7_TSSS",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_TSSS_Cs",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 124,
    label = "R7_TSSS_O",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 125,
    label = "R7_TSSM",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_TSSM_Cs",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 128,
    label = "R7_TSSM_O",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 129,
    label = "R7_BSSR",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_BSSS",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 132,
    label = "R7_BSSS_Cs",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_BSSS_O",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_BSSM",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 136,
    label = "R7_BSSM_Cs",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_BSSM_O",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 R!H        0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 138,
    label = "R7_RSMS",
    group = 
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 139,
    label = "R7_SSMS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 141,
    label = "R7_SSMS_Cs",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 142,
    label = "R7_SSMS_O",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_DSMS",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 145,
    label = "R7_DSMS_Cs",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_DSMS_O",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 147,
    label = "R7_TSMS",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_TSMS_Cs",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_TSMS_O",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_BSMS",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )



entry(
    index = 153,
    label = "R7_BSMS_Cs",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 154,
    label = "R7_BSMS_O",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 155,
    label = "R7_SMSR",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 156,
    label = "R7_SMSS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 158,
    label = "R7_SMSS_Cs",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 159,
    label = "R7_SMSS_O",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 160,
    label = "R7_SMSM",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 162,
    label = "R7_SMSM_Cs",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 163,
    label = "R7_SMSM_O",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 164,
    label = "R7_BBSR",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3 *6 Cb         0 {2,B} {4,S}
4 *7 R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 165,
    label = "R7_BBSS",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3 *6 Cb         0 {2,B} {4,S}
4 *7 R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 167,
    label = "R7_BBSS_Cs",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 168,
    label = "R7_BBSS_O",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *7 R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 169,
    label = "R7_BBSM",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3 *6 Cb         0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 171,
    label = "R7_BBSM_Cs",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3 *6 Cb         0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 172,
    label = "R7_BBSM_O",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3 *6 Cb         0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 173,
    label = "R7_RSBB",
    group = 
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3 *6 Cb         0 {2,S} {4,B}
4 *7 Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 174,
    label = "R7_SSBB",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 Cb         0 {2,S} {4,B}
4 *7 Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )


entry(
    index = 176,
    label = "R7_SSBB_Cs",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 177,
    label = "R7_SSBB_O",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 178,
    label = "R7_DSBB",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 Cb         0 {2,S} {4,B}
4 *7 Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_DSBB_Cs",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_DSBB_O",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_TSBB",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 Cb         0 {2,S} {4,B}
4 *7 Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_TSBB_Cs",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_TSBB_O",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_BSBB",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 Cb         0 {2,S} {4,B}
4 *7 Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_BSBB_Cs",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_BSBB_O",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 Cb  0 {2,S} {4,B}
4 *7 Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "R7_SBBS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 Cb         0 {1,S} {3,B}
3 *6 Cbf        0 {2,B} {4,B}
4 *7 Cb         0 {3,B} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 {C,O} 0           {6,S}
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
    label = "R7_SBBS_Cs",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *7 Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 C 0           {6,S}
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
    label = "R7_SBBS_O",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *7 Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 {C,O} 0           {5,S} {7,S}
7 *3 O 0           {6,S}
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
    label = "doublebond_intra",
    group = 
"""
1 *2 {C,O} 0 {2,S}
2 *3 C 0 {1,S}
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
    label = "doublebond_intra_2H",
    group = 
"""
1 *2 {C,O} 0 {2,S}
2 *3 C 0 {1,S} {3,S} {4,S}
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
    index = 196,
    label = "doublebond_intra_2H_pri",
    group =
"""
1 *2 {C,O} 0 {2,S} {3,S}
2 *3 C 0 {1,S} {4,S} {5,S}
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
    index = 197,
    label = "doublebond_intra_2H_secNd",
    group =
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
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
    index = 198,
    label = "doublebond_intra_2H_secDe",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
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
    index = 199,
    label = "doublebond_intra_HNd",
    group =
"""
1 *2 {C,O}     0 {2,S}
2 *3 C     0 {1,S} {3,S} {4,S}
3    H      0 {2,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 200,
    label = "doublebond_intra_HNd_pri",
    group =
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
3    H      0 {1,S}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 201,
    label = "doublebond_intra_HNd_secNd",
    group =
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
3    {Cs,O} 0 {1,S}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 202,
    label = "doublebond_intra_HNd_secDe",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 203,
    label = "doublebond_intra_HDe",
    group =
"""
1 *2 {C,O}            0 {2,S}
2 *3 C            0 {1,S} {3,S} {4,S}
3    H             0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 204,
    label = "doublebond_intra_HDe_pri",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    H             0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 205,
    label = "doublebond_intra_HCd_pri",
    group = 
"""
1 *2 {C,O} 0 {2,S} {3,S}
2 *3 C 0 {1,S} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    Cd 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 206,
    label = "doublebond_intra_HCt_pri",
    group = 
"""
1 *2 {C,O} 0 {2,S} {3,S}
2 *3 C 0 {1,S} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    Ct 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 207,
    label = "doublebond_intra_HDe_secNd",
    group = 
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cs,O}        0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 208,
    label = "doublebond_intra_HDe_secDe",
    group = 
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 209,
    label = "doublebond_intra_NdNd",
    group = 
"""
1 *2 {C,O}     0 {2,S}
2 *3 C     0 {1,S} {3,S} {4,S}
3    {Cs,O} 0 {2,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 210,
    label = "doublebond_intra_NdNd_pri",
    group = 
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
3    H      0 {1,S}
4    {Cs,O} 0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 211,
    label = "doublebond_intra_NdNd_secNd",
    group = 
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 212,
    label = "doublebond_intra_NdNd_secDe",
    group = 
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 213,
    label = "doublebond_intra_NdDe",
    group = 
"""
1 *2 {C,O}            0 {2,S}
2 *3 C            0 {1,S} {3,S} {4,S}
3    {Cs,O}        0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 212,
    label = "doublebond_intra_NdDe_pri",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    H             0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 215,
    label = "doublebond_intra_NdCd_pri",
    group = 
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
3    H      0 {1,S}
4    {Cs,O} 0 {2,S}
5    Cd     0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 216,
    label = "doublebond_intra_NdCt_pri",
    group = 
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 C     0 {1,S} {4,S} {5,S}
3    H      0 {1,S}
4    {Cs,O} 0 {2,S}
5    Ct     0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 217,
    label = "doublebond_intra_NdDe_secNd",
    group = 
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 214,
    label = "doublebond_intra_NdDe_secDe",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 215,
    label = "doublebond_intra_DeDe",
    group =
"""
1 *2 {C,O}            0 {2,S}
2 *3 C            0 {1,S} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 216,
    label = "doublebond_intra_DeDe_pri",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 217,
    label = "doublebond_intra_DeDe_secNd",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 218,
    label = "doublebond_intra_DeDe_secDe",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 C            0 {1,S} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )


entry(
    index = 223,
    label = "carbonylbond_intra",
    group =
"""
1 *2 {C,O} 0 {2,S}
2 *3 O 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 224,
    label = "carbonylbond_intra_H",
    group =
"""
1 *2 {C,O} 0 {2,S} {3,S}
2 *3 O 0 {1,S}
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
    index = 225,
    label = "carbonylbond_intra_Nd",
    group =
"""
1 *2 {C,O}     0 {2,S} {3,S}
2 *3 O    0 {1,S}
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
    index = 226,
    label = "carbonylbond_intra_De",
    group =
"""
1 *2 {C,O}            0 {2,S} {3,S}
2 *3 O            0 {1,S}
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
    index = 227,
    label = "radadd_intra_cs",
    group =
"""
1 *1 Cs 1
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 228,
    label = "radadd_intra_cs2H",
    group =
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
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
    index = 229,
    label = "radadd_intra_csHNd",
    group =
"""
1 *1 Cs     1 {2,S} {3,S}
2    H      0 {1,S}
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
    index = 230,
    label = "radadd_intra_csHDe",
    group =
"""
1 *1 Cs            1 {2,S} {3,S}
2    H             0 {1,S}
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
    index = 231,
    label = "radadd_intra_csHCd",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 232,
    label = "radadd_intra_csHCt",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 233,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs     1 {2,S} {3,S}
2    {Cs,O} 0 {1,S}
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
    index = 243,
    label = "radadd_intra_csNdDe",
    group =
"""
1 *1 Cs            1 {2,S} {3,S}
2    {Cs,O}        0 {1,S}
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
    index = 244,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs     1 {2,S} {3,S}
2    {Cs,O} 0 {1,S}
3    Cd     0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 245,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs     1 {2,S} {3,S}
2    {Cs,O} 0 {1,S}
3    Ct     0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    )

entry(
    index = 246,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 234,
    label = "radadd_intra_O",
    group =
"""
1 *1 O 1
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 235,
    label = "radadd_intra_Cb",
    group =
"""
1 *1 Cb 1
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 236,
    label = "radadd_intra_cdsingle",
    group =
"""
1 *1 Cd 1 {2,S}
2    R  0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 237,
    label = "radadd_intra_cdsingleH",
    group =
"""
1 *1 Cd 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 238,
    label = "radadd_intra_cdsingleNd",
    group =
"""
1 *1 Cd     1 {2,S}
2    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 239,
    label = "radadd_intra_cdsingleDe",
    group =
"""
1 *1 Cd            1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 240,
    label = "radadd_intra_cddouble",
    group =
"""
1 *1 Cd 1 {2,D}
2    Cd 0 {1,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 241,
    label = "radadd_intra_CO",
    group =
"""
1 *1 CO 1 {2,D}
2    O  0 {1,D}
""",
    kinetics = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    )

entry(
    index = 242,
    label = "radadd_intra_Ct",
    group =
"""
1 *1 Ct 1 {2,T}
2    Ct 0 {1,T}
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
L1: R1_rad_R2_R3
    L2: R4
        L3: R4_S
            L4: R4_S_Cs
            L4: R4_S_O
        L3: R4_D
            L4: R4_D_Cs
            L4: R4_D_O
        L3: R4_T
            L4: R4_T_Cs
            L4: R4_T_O
        L3: R4_B
            L4: R4_B_Cs
            L4: R4_B_O
    L2: R5
        L3: R5_SS
            L4: R5_SS_Cs
            L4: R5_SS_O
        L3: R5_SD
            L4: R5_SD_Cs
            L4: R5_SD_O
        L3: R5_DS
            L4: R5_DS_Cs
            L4: R5_DS_O
        L3: R5_ST
            L4: R5_ST_Cs
            L4: R5_ST_O
        L3: R5_TS
            L4: R5_TS_Cs
            L4: R5_TS_O
        L3: R5_SB
            L4: R5_SB_Cs
            L4: R5_SB_O
        L3: R5_BS
            L4: R5_BS_Cs
            L4: R5_BS_O
    L2: R6
        L3: R6_RSR
            L4: R6_SSR
                L5: R6_SSS
                    L6: R6_SSS_Cs
                    L6: R6_SSS_O
                L5: R6_SSM
                    L6: R6_SSM_Cs
                    L6: R6_SSM_O
            L4: R6_DSR
                L5: R6_DSS
                    L6: R6_DSS_Cs
                    L6: R6_DSS_O
                L5: R6_DSM
                    L6: R6_DSM_Cs
                    L6: R6_DSM_O
            L4: R6_TSR
                L5: R6_TSS
                    L6: R6_TSS_Cs
                    L6: R6_TSS_O
                L5: R6_TSM
                    L6: R6_TSM_Cs
                    L6: R6_TSM_O
            L4: R6_BSR
                L5: R6_BSS
                    L6: R6_BSS_Cs
                    L6: R6_BSS_O
                L5: R6_BSM
                    L6: R6_BSM_Cs
                    L6: R6_BSM_O
        L3: R6_SMS
            L4: R6_SMS_Cs
            L4: R6_SMS_O
        L3: R6_SBB
            L4: R6_SBB_Cs
            L4: R6_SBB_O
        L3: R6_BBS
            L4: R6_BBS_Cs
            L4: R6_BBS_O
    L2: R7
        L3: R7_RSSR
            L4: R7_SSSR
                L5: R7_SSSS
                    L6: R7_SSSS_Cs
                    L6: R7_SSSS_O
                L5: R7_SSSM
                    L6: R7_SSSM_Cs
                    L6: R7_SSSM_O
            L4: R7_DSSR
                L5: R7_DSSS
                    L6: R7_DSSS_Cs
                    L6: R7_DSSS_O
                L5: R7_DSSM
                    L6: R7_DSSM_Cs
                    L6: R7_DSSM_O
            L4: R7_TSSR
                L5: R7_TSSS
                    L6: R7_TSSS_Cs
                    L6: R7_TSSS_O
                L5: R7_TSSM
                    L6: R7_TSSM_Cs
                    L6: R7_TSSM_O
            L4: R7_BSSR
                L5: R7_BSSS
                    L6: R7_BSSS_Cs
                    L6: R7_BSSS_O
                L5: R7_BSSM
                    L6: R7_BSSM_Cs
                    L6: R7_BSSM_O
        L3: R7_RSMS
            L4: R7_SSMS
                L5: R7_SSMS_Cs
                L5: R7_SSMS_O
            L4: R7_DSMS
                L5: R7_DSMS_Cs
                L5: R7_DSMS_O
            L4: R7_TSMS
                L5: R7_TSMS_Cs
                L5: R7_TSMS_O
            L4: R7_BSMS
                L5: R7_BSMS_Cs
                L5: R7_BSMS_O
        L3: R7_SMSR
            L4: R7_SMSS
                L5: R7_SMSS_Cs
                L5: R7_SMSS_O
            L4: R7_SMSM
                L5: R7_SMSM_Cs
                L5: R7_SMSM_O
        L3: R7_BBSR
            L4: R7_BBSS
                L5: R7_BBSS_Cs
                L5: R7_BBSS_O
            L4: R7_BBSM
                L5: R7_BBSM_Cs
                L5: R7_BBSM_O
        L3: R7_RSBB
            L4: R7_SSBB
                L5: R7_SSBB_Cs
                L5: R7_SSBB_O
            L4: R7_DSBB
                L5: R7_DSBB_Cs
                L5: R7_DSBB_O
            L4: R7_TSBB
                L5: R7_TSBB_Cs
                L5: R7_TSBB_O
            L4: R7_BSBB
                L5: R7_BSBB_Cs
                L5: R7_BSBB_O
        L3: R7_SBBS
            L4: R7_SBBS_Cs
            L4: R7_SBBS_O
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_2H
            L4: doublebond_intra_2H_pri
            L4: doublebond_intra_2H_secNd
            L4: doublebond_intra_2H_secDe
        L3: doublebond_intra_HNd
            L4: doublebond_intra_HNd_pri
            L4: doublebond_intra_HNd_secNd
            L4: doublebond_intra_HNd_secDe
        L3: doublebond_intra_HDe
            L4: doublebond_intra_HDe_pri
                L5: doublebond_intra_HCd_pri
                L5: doublebond_intra_HCt_pri
            L4: doublebond_intra_HDe_secNd
            L4: doublebond_intra_HDe_secDe
        L3: doublebond_intra_NdNd
            L4: doublebond_intra_NdNd_pri
            L4: doublebond_intra_NdNd_secNd
            L4: doublebond_intra_NdNd_secDe
        L3: doublebond_intra_NdDe
            L4: doublebond_intra_NdDe_pri
                L5: doublebond_intra_NdCd_pri
                L5: doublebond_intra_NdCt_pri
            L4: doublebond_intra_NdDe_secNd
            L4: doublebond_intra_NdDe_secDe
        L3: doublebond_intra_DeDe
            L4: doublebond_intra_DeDe_pri
            L4: doublebond_intra_DeDe_secNd
            L4: doublebond_intra_DeDe_secDe
    L2: carbonylbond_intra
        L3: carbonylbond_intra_H
        L3: carbonylbond_intra_Nd
        L3: carbonylbond_intra_De
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
            L4: radadd_intra_csHCt
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
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

forbidden(
    label = "bond21",
    group =
"""
1 *2 R!H 0 {2,{S,D}}
2 *1 R!H 1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    
)

#forbidden(
#    label = "cdd2",
#    group =
#"""
#1 *2 {C,O}dd 0
#""",
#    shortDesc = u"""""",
#    longDesc =
#u"""
#
#""",
#)
#

forbidden(
    label = "birad_singlet",
    group = 
"""
1 *1 {C,N,Si} 2S 0
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

forbidden(
    label = "OS_birad_singlet",
    group = 
"""
1 *1 {O,S} 2S 2
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

forbidden(
    label = "quadrad_singlet",
    group = 
"""
1 *1 {C,N,Si} 4S 0
""",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)