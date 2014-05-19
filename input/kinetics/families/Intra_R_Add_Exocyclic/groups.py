#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open_Exo_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', '-1', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Rn",
    group = "OR{R4, R5, R6, R7}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "multiplebond_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 {Cd,Ct,CO,N}     U0 {2,{D,T}}
2 *3 {Cd,Ct,Od,Cdd,N} U0 {1,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "radadd_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R4",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,{S,D,T,B}}
2 *4 R!H              U0 {1,{S,D,T,B}} {3,S}
3 *2 {Cd,Ct,CO,N}     U0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd,N} U0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R4_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *2 {Cd,Ct,CO}     U0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} U0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R4_S_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 R!H      U0 {1,S} {3,S}
3 *2 Cd       U0 {2,S} {4,D}
4 *3 {Cd,Cdd} U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R4_S_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *2 Ct  U0 {2,S} {4,T}
4 *3 Ct  U0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R4_S_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *2 CO  U0 {2,S} {4,D}
4 *3 Od  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R4_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *2 {Cd,Ct,CO}     U0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} U0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R4_D_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U1 {2,D}
2 *4 Cd       U0 {1,D} {3,S}
3 *2 Cd       U0 {2,S} {4,D}
4 *3 {Cd,Cdd} U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R4_D_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,D}
2 *4 Cd U0 {1,D} {3,S}
3 *2 Ct U0 {2,S} {4,T}
4 *3 Ct U0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R4_D_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,D}
2 *4 Cd U0 {1,D} {3,S}
3 *2 CO U0 {2,S} {4,D}
4 *3 Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R4_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *2 {Cd,Ct,CO}     U0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} U0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R4_T_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct       U1 {2,T}
2 *4 Ct       U0 {1,T} {3,S}
3 *2 Cd       U0 {2,S} {4,D}
4 *3 {Cd,Cdd} U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R4_T_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U1 {2,T}
2 *4 Ct U0 {1,T} {3,S}
3 *2 Ct U0 {2,S} {4,T}
4 *3 Ct U0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R4_T_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U1 {2,T}
2 *4 Ct U0 {1,T} {3,S}
3 *2 CO U0 {2,S} {4,D}
4 *3 Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R4_B",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *2 {Cd,Ct,CO}     U0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} U0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "R4_B_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cb       U0 {1,B} {3,S}
3 *2 Cd       U0 {2,S} {4,D}
4 *3 {Cd,Cdd} U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "R4_B_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb U1 {2,B}
2 *4 Cb U0 {1,B} {3,S}
3 *2 Ct U0 {2,S} {4,T}
4 *3 Ct U0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "R4_B_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb U1 {2,B}
2 *4 Cb U0 {1,B} {3,S}
3 *2 CO U0 {2,S} {4,D}
4 *3 Od U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "R5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H                 U1       {2,{S,D,T,B}}
2 *4 R!H                 U{0,1,2} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *5 R!H                 U{0,1,2} {2,{S,D,T,B}} {4,S}
4 *2 {Cd,Ct,CO,N}        U0       {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} U0       {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "R5_SS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 R!H              U0 {1,S} {3,S}
3 *5 R!H              U0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "R5_SS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 R!H      U0 {1,S} {3,S}
3 *5 R!H      U0 {2,S} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "R5_SS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "R5_SS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "R5_SD",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 Cd               U0 {1,S} {3,D}
3 *5 Cd               U0 {2,D} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "R5_SD_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 Cd       U0 {1,S} {3,D}
3 *5 Cd       U0 {2,D} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "R5_SD_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cd  U0 {1,S} {3,D}
3 *5 Cd  U0 {2,D} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "R5_SD_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cd  U0 {1,S} {3,D}
3 *5 Cd  U0 {2,D} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "R5_DS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd               U1 {2,D}
2 *4 Cd               U0 {1,D} {3,S}
3 *5 R!H              U0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "R5_DS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U1 {2,D}
2 *4 Cd       U0 {1,D} {3,S}
3 *5 R!H      U0 {2,S} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "R5_DS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "R5_DS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "R5_ST",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 Ct               U0 {1,S} {3,T}
3 *5 Ct               U0 {2,T} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "R5_ST_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 Ct       U0 {1,S} {3,T}
3 *5 Ct       U0 {2,T} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "R5_ST_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Ct  U0 {1,S} {3,T}
3 *5 Ct  U0 {2,T} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "R5_ST_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Ct  U0 {1,S} {3,T}
3 *5 Ct  U0 {2,T} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "R5_TS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct               U1 {2,T}
2 *4 Ct               U0 {1,T} {3,S}
3 *5 R!H              U0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "R5_TS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct       U1 {2,T}
2 *4 Ct       U0 {1,T} {3,S}
3 *5 R!H      U0 {2,S} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "R5_TS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "R5_TS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "R5_SB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 Cb               U0 {1,S} {3,B}
3 *5 Cb               U0 {2,B} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "R5_SB_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 Cb       U0 {1,S} {3,B}
3 *5 Cb       U0 {2,B} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "R5_SB_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cb  U0 {1,S} {3,B}
3 *5 Cb  U0 {2,B} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "R5_SB_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cb  U0 {1,S} {3,B}
3 *5 Cb  U0 {2,B} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "R5_BS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb               U1 {2,B}
2 *4 Cb               U0 {1,B} {3,S}
3 *5 R!H              U0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}     U0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd,N} U0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "R5_BS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cb       U0 {1,B} {3,S}
3 *5 R!H      U0 {2,S} {4,S}
4 *2 Cd       U0 {3,S} {5,D}
5 *3 {Cd,Cdd} U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "R5_BS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 Ct  U0 {3,S} {5,T}
5 *3 Ct  U0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "R5_BS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *5 R!H U0 {2,S} {4,S}
4 *2 CO  U0 {3,S} {5,D}
5 *3 Od  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "R6",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H                 U1       {2,{S,D,T,B}}
2 *4 R!H                 U{0,1,2} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H                 U{0,1,2} {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *5 R!H                 U{0,1,2} {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO,N}        U0       {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd,N} U0       {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "R6_RSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,{S,D,T,B}}
2 *4 R!H              U0 {1,{S,D,T,B}} {3,S}
3 *6 R!H              U0 {2,S} {4,{S,D,T,B}}
4 *5 R!H              U0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO,N}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd,N} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "R6_SSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 R!H            U0 {2,S} {4,{S,D,T,B}}
4 *5 R!H            U0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "R6_SSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *5 R!H            U0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "R6_SSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 R!H      U0 {1,S} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *5 R!H      U0 {3,S} {5,S}
5 *2 Cd       U0 {4,S} {6,D}
6 *3 {Cd,Cdd} U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "R6_SSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 Ct  U0 {4,S} {6,T}
6 *3 Ct  U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "R6_SSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 CO  U0 {4,S} {6,D}
6 *3 Od  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "R6_SSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "R6_SSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Cd         U0 {4,S} {6,D}
6 *3 {Cd,Cdd}   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "R6_SSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Ct         U0 {4,S} {6,T}
6 *3 Ct         U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "R6_SSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 CO         U0 {4,S} {6,D}
6 *3 Od         U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "R6_DSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 R!H            U0 {2,S} {4,{S,D,T,B}}
4 *5 R!H            U0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "R6_DSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *5 R!H            U0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "R6_DSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U1 {2,D}
2 *4 Cd       U0 {1,D} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *5 R!H      U0 {3,S} {5,S}
5 *2 Cd       U0 {4,S} {6,D}
6 *3 {Cd,Cdd} U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "R6_DSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 Ct  U0 {4,S} {6,T}
6 *3 Ct  U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "R6_DSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 CO  U0 {4,S} {6,D}
6 *3 Od  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "R6_DSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "R6_DSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Cd         U0 {4,S} {6,D}
6 *3 {Cd,Cdd}   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "R6_DSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Ct         U0 {4,S} {6,T}
6 *3 Ct         U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "R6_DSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 CO         U0 {4,S} {6,D}
6 *3 Od         U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "R6_TSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 R!H            U0 {2,S} {4,{S,D,T,B}}
4 *5 R!H            U0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "R6_TSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *5 R!H            U0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "R6_TSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct       U1 {2,T}
2 *4 Ct       U0 {1,T} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *5 R!H      U0 {3,S} {5,S}
5 *2 Cd       U0 {4,S} {6,D}
6 *3 {Cd,Cdd} U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "R6_TSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 Ct  U0 {4,S} {6,T}
6 *3 Ct  U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "R6_TSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 CO  U0 {4,S} {6,D}
6 *3 Od  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "R6_TSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "R6_TSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Cd         U0 {4,S} {6,D}
6 *3 {Cd,Cdd}   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "R6_TSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Ct         U0 {4,S} {6,T}
6 *3 Ct         U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "R6_TSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 CO         U0 {4,S} {6,D}
6 *3 Od         U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "R6_BSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 R!H            U0 {2,S} {4,{S,D,T,B}}
4 *5 R!H            U0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "R6_BSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *5 R!H            U0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "R6_BSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cb       U0 {1,B} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *5 R!H      U0 {3,S} {5,S}
5 *2 Cd       U0 {4,S} {6,D}
6 *3 {Cd,Cdd} U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "R6_BSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 Ct  U0 {4,S} {6,T}
6 *3 Ct  U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "R6_BSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 CO  U0 {4,S} {6,D}
6 *3 Od  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "R6_BSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "R6_BSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Cd         U0 {4,S} {6,D}
6 *3 {Cd,Cdd}   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "R6_BSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 Ct         U0 {4,S} {6,T}
6 *3 Ct         U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "R6_BSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *2 CO         U0 {4,S} {6,D}
6 *3 Od         U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "R6_SMS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 {Cd,Ct,Cb}       U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb}       U0 {2,{D,T,B}} {4,S}
4 *5 R!H              U0 {3,S} {5,S}
5 *2 {Cd,Ct,CO,N}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd,N} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "R6_SMS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *5 R!H        U0 {3,S} {5,S}
5 *2 Cd         U0 {4,S} {6,D}
6 *3 {Cd,Cdd}   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "R6_SMS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *5 R!H        U0 {3,S} {5,S}
5 *2 Ct         U0 {4,S} {6,T}
6 *3 Ct         U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "R6_SMS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *5 R!H        U0 {3,S} {5,S}
5 *2 CO         U0 {4,S} {6,D}
6 *3 Od         U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "R6_SBB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 Cb               U0 {1,S} {3,B}
3 *6 Cbf              U0 {2,B} {4,B}
4 *5 Cb               U0 {3,B} {5,S}
5 *2 {Cd,Ct,CO,N}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd,N} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "R6_SBB_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 Cb       U0 {1,S} {3,B}
3 *6 Cbf      U0 {2,B} {4,B}
4 *5 Cb       U0 {3,B} {5,S}
5 *2 Cd       U0 {4,S} {6,D}
6 *3 {Cd,Cdd} U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "R6_SBB_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cb  U0 {1,S} {3,B}
3 *6 Cbf U0 {2,B} {4,B}
4 *5 Cb  U0 {3,B} {5,S}
5 *2 Ct  U0 {4,S} {6,T}
6 *3 Ct  U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "R6_SBB_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cb  U0 {1,S} {3,B}
3 *6 Cbf U0 {2,B} {4,B}
4 *5 Cb  U0 {3,B} {5,S}
5 *2 CO  U0 {4,S} {6,D}
6 *3 Od  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "R6_BBS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb               U1 {2,B}
2 *4 Cbf              U0 {1,B} {3,B}
3 *6 Cb               U0 {2,B} {4,S}
4 *5 R!H              U0 {3,S} {5,S}
5 *2 {Cd,Ct,CO,N}     U0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd,N} U0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "R6_BBS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cbf      U0 {1,B} {3,B}
3 *6 Cb       U0 {2,B} {4,S}
4 *5 R!H      U0 {3,S} {5,S}
5 *2 Cd       U0 {4,S} {6,D}
6 *3 {Cd,Cdd} U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "R6_BBS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cbf U0 {1,B} {3,B}
3 *6 Cb  U0 {2,B} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 Ct  U0 {4,S} {6,T}
6 *3 Ct  U0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "R6_BBS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cbf U0 {1,B} {3,B}
3 *6 Cb  U0 {2,B} {4,S}
4 *5 R!H U0 {3,S} {5,S}
5 *2 CO  U0 {4,S} {6,D}
6 *3 Od  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "R7",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1       {2,{S,D,T,B}}
2 *4 R!H              U{0,1,2} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H              U{0,1,2} {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *7 R!H              U{0,1,2} {3,{S,D,T,B}} {5,{S,D,T,B}}
5 *5 R!H              U{0,1,2} {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO,N}     U0       {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0       {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "R7_RSSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,{S,D,T,B}}
2 *4 R!H              U0 {1,{S,D,T,B}} {3,S}
3 *6 R!H              U0 {2,S} {4,S}
4 *7 R!H              U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H              U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO,N}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "R7_SSSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H            U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "R7_SSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "R7_SSSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 R!H      U0 {1,S} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *7 R!H      U0 {3,S} {5,S}
5 *5 R!H      U0 {4,S} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "R7_SSSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "R7_SSSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "R7_SSSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb}     U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb}     U0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "R7_SSSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "R7_SSSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "R7_SSSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "R7_DSSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H            U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "R7_DSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "R7_DSSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U1 {2,D}
2 *4 Cd       U0 {1,D} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *7 R!H      U0 {3,S} {5,S}
5 *5 R!H      U0 {4,S} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "R7_DSSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "R7_DSSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "R7_DSSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb}     U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb}     U0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "R7_DSSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "R7_DSSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "R7_DSSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "R7_TSSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H            U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "R7_TSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "R7_TSSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct       U1 {2,T}
2 *4 Ct       U0 {1,T} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *7 R!H      U0 {3,S} {5,S}
5 *5 R!H      U0 {4,S} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "R7_TSSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "R7_TSSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "R7_TSSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb}     U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb}     U0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "R7_TSSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "R7_TSSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "R7_TSSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "R7_BSSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H            U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "R7_BSSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 R!H            U0 {3,S} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "R7_BSSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cb       U0 {1,B} {3,S}
3 *6 R!H      U0 {2,S} {4,S}
4 *7 R!H      U0 {3,S} {5,S}
5 *5 R!H      U0 {4,S} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "R7_BSSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "R7_BSSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *6 R!H U0 {2,S} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "R7_BSSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 R!H            U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb}     U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb}     U0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "R7_BSSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "R7_BSSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "R7_BSSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 R!H        U0 {2,S} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "R7_RSMS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,{S,D,T,B}}
2 *4 R!H              U0 {1,{S,D,T,B}} {3,S}
3 *6 {Cd,Ct,Cb}       U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb}       U0 {3,{D,T,B}} {5,S}
5 *5 R!H              U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO,N}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "R7_SSMS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "R7_SSMS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "R7_SSMS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "R7_SSMS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 R!H        U0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "R7_DSMS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "R7_DSMS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "R7_DSMS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "R7_DSMS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd         U1 {2,D}
2 *4 Cd         U0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "R7_TSMS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "R7_TSMS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "R7_TSMS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "R7_TSMS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct         U1 {2,T}
2 *4 Ct         U0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "R7_BSMS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb}     U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb}     U0 {3,{D,T,B}} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "R7_BSMS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "R7_BSMS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "R7_BSMS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cb         U0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} U0 {2,S} {4,{D,T,B}}
4 *7 {Cd,Ct,Cb} U0 {3,{D,T,B}} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "R7_SMSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 {Cd,Ct,Cb}       U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb}       U0 {2,{D,T,B}} {4,S}
4 *7 R!H              U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H              U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO,N}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "R7_SMSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 {Cd,Ct,Cb}     U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb}     U0 {2,{D,T,B}} {4,S}
4 *7 R!H            U0 {3,S} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "R7_SMSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *7 R!H        U0 {3,S} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "R7_SMSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *7 R!H        U0 {3,S} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "R7_SMSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *7 R!H        U0 {3,S} {5,S}
5 *5 R!H        U0 {4,S} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "R7_SMSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 {Cd,Ct,Cb}     U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb}     U0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb}     U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb}     U0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "R7_SMSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "R7_SMSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "R7_SMSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H        U1 {2,S}
2 *4 {Cd,Ct,Cb} U0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} U0 {2,{D,T,B}} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "R7_BBSR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb               U1 {2,B}
2 *4 Cbf              U0 {1,B} {3,B}
3 *6 Cb               U0 {2,B} {4,S}
4 *7 R!H              U0 {3,S} {5,{S,D,T,B}}
5 *5 R!H              U0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO,N}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "R7_BBSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cbf            U0 {1,B} {3,B}
3 *6 Cb             U0 {2,B} {4,S}
4 *7 R!H            U0 {3,S} {5,S}
5 *5 R!H            U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "R7_BBSS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cbf      U0 {1,B} {3,B}
3 *6 Cb       U0 {2,B} {4,S}
4 *7 R!H      U0 {3,S} {5,S}
5 *5 R!H      U0 {4,S} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "R7_BBSS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cbf U0 {1,B} {3,B}
3 *6 Cb  U0 {2,B} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "R7_BBSS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cbf U0 {1,B} {3,B}
3 *6 Cb  U0 {2,B} {4,S}
4 *7 R!H U0 {3,S} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "R7_BBSM",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cbf            U0 {1,B} {3,B}
3 *6 Cb             U0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb}     U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb}     U0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "R7_BBSM_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cbf        U0 {1,B} {3,B}
3 *6 Cb         U0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Cd         U0 {5,S} {7,D}
7 *3 {Cd,Cdd}   U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "R7_BBSM_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cbf        U0 {1,B} {3,B}
3 *6 Cb         U0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 Ct         U0 {5,S} {7,T}
7 *3 Ct         U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "R7_BBSM_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb         U1 {2,B}
2 *4 Cbf        U0 {1,B} {3,B}
3 *6 Cb         U0 {2,B} {4,S}
4 *7 {Cd,Ct,Cb} U0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} U0 {4,{D,T,B}} {6,S}
6 *2 CO         U0 {5,S} {7,D}
7 *3 Od         U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "R7_RSBB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,{S,D,T,B}}
2 *4 R!H              U0 {1,{S,D,T,B}} {3,S}
3 *6 Cb               U0 {2,S} {4,B}
4 *7 Cbf              U0 {3,B} {5,B}
5 *5 Cb               U0 {4,B} {6,S}
6 *2 {Cd,Ct,CO,N}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "R7_SSBB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H            U1 {2,S}
2 *4 R!H            U0 {1,S} {3,S}
3 *6 Cb             U0 {2,S} {4,B}
4 *7 Cbf            U0 {3,B} {5,B}
5 *5 Cb             U0 {4,B} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "R7_SSBB_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 R!H      U0 {1,S} {3,S}
3 *6 Cb       U0 {2,S} {4,B}
4 *7 Cbf      U0 {3,B} {5,B}
5 *5 Cb       U0 {4,B} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "R7_SSBB_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "R7_SSBB_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "R7_DSBB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd             U1 {2,D}
2 *4 Cd             U0 {1,D} {3,S}
3 *6 Cb             U0 {2,S} {4,B}
4 *7 Cbf            U0 {3,B} {5,B}
5 *5 Cb             U0 {4,B} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "R7_DSBB_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd       U1 {2,D}
2 *4 Cd       U0 {1,D} {3,S}
3 *6 Cb       U0 {2,S} {4,B}
4 *7 Cbf      U0 {3,B} {5,B}
5 *5 Cb       U0 {4,B} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "R7_DSBB_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "R7_DSBB_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U1 {2,D}
2 *4 Cd  U0 {1,D} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "R7_TSBB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct             U1 {2,T}
2 *4 Ct             U0 {1,T} {3,S}
3 *6 Cb             U0 {2,S} {4,B}
4 *7 Cbf            U0 {3,B} {5,B}
5 *5 Cb             U0 {4,B} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "R7_TSBB_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct       U1 {2,T}
2 *4 Ct       U0 {1,T} {3,S}
3 *6 Cb       U0 {2,S} {4,B}
4 *7 Cbf      U0 {3,B} {5,B}
5 *5 Cb       U0 {4,B} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "R7_TSBB_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "R7_TSBB_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2 *4 Ct  U0 {1,T} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "R7_BSBB",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb             U1 {2,B}
2 *4 Cb             U0 {1,B} {3,S}
3 *6 Cb             U0 {2,S} {4,B}
4 *7 Cbf            U0 {3,B} {5,B}
5 *5 Cb             U0 {4,B} {6,S}
6 *2 {Cd,Ct,CO}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "R7_BSBB_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B}
2 *4 Cb       U0 {1,B} {3,S}
3 *6 Cb       U0 {2,S} {4,B}
4 *7 Cbf      U0 {3,B} {5,B}
5 *5 Cb       U0 {4,B} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "R7_BSBB_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "R7_BSBB_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb  U1 {2,B}
2 *4 Cb  U0 {1,B} {3,S}
3 *6 Cb  U0 {2,S} {4,B}
4 *7 Cbf U0 {3,B} {5,B}
5 *5 Cb  U0 {4,B} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "R7_SBBS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H              U1 {2,S}
2 *4 Cb               U0 {1,S} {3,B}
3 *6 Cbf              U0 {2,B} {4,B}
4 *7 Cb               U0 {3,B} {5,S}
5 *5 R!H              U0 {4,S} {6,S}
6 *2 {Cd,Ct,CO,N}     U0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd,N} U0 {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "R7_SBBS_D",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H      U1 {2,S}
2 *4 Cb       U0 {1,S} {3,B}
3 *6 Cbf      U0 {2,B} {4,B}
4 *7 Cb       U0 {3,B} {5,S}
5 *5 R!H      U0 {4,S} {6,S}
6 *2 Cd       U0 {5,S} {7,D}
7 *3 {Cd,Cdd} U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "R7_SBBS_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cb  U0 {1,S} {3,B}
3 *6 Cbf U0 {2,B} {4,B}
4 *7 Cb  U0 {3,B} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 Ct  U0 {5,S} {7,T}
7 *3 Ct  U0 {6,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "R7_SBBS_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U1 {2,S}
2 *4 Cb  U0 {1,S} {3,B}
3 *6 Cbf U0 {2,B} {4,B}
4 *7 Cb  U0 {3,B} {5,S}
5 *5 R!H U0 {4,S} {6,S}
6 *2 CO  U0 {5,S} {7,D}
7 *3 Od  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "doublebond_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd       U0 {2,D}
2 *3 {Cd,Cdd} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "doublebond_intra_2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,D}
2 *3 Cd U0 {1,D} {3,S} {4,S}
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
    index = 196,
    label = "doublebond_intra_2H_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,D} {3,S}
2 *3 Cd U0 {1,D} {4,S} {5,S}
3    H  U0 {1,S}
4    H  U0 {2,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "doublebond_intra_2H_secNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    {Cs,O} U0 {1,S}
4    H      U0 {2,S}
5    H      U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "doublebond_intra_2H_secDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {2,S}
5    H             U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "doublebond_intra_HNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D}
2 *3 Cd     U0 {1,D} {3,S} {4,S}
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
    index = 200,
    label = "doublebond_intra_HNd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    H      U0 {1,S}
4    H      U0 {2,S}
5    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "doublebond_intra_HNd_secNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    {Cs,O} U0 {1,S}
4    H      U0 {2,S}
5    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "doublebond_intra_HNd_secDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {2,S}
5    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "doublebond_intra_HDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D}
2 *3 Cd            U0 {1,D} {3,S} {4,S}
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
    index = 204,
    label = "doublebond_intra_HDe_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    H             U0 {1,S}
4    H             U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "doublebond_intra_HCd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,D} {3,S}
2 *3 Cd U0 {1,D} {4,S} {5,S}
3    H  U0 {1,S}
4    H  U0 {2,S}
5    Cd U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "doublebond_intra_HCt_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,D} {3,S}
2 *3 Cd U0 {1,D} {4,S} {5,S}
3    H  U0 {1,S}
4    H  U0 {2,S}
5    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "doublebond_intra_HDe_secNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cs,O}        U0 {1,S}
4    H             U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "doublebond_intra_HDe_secDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    H             U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "doublebond_intra_NdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D}
2 *3 Cd     U0 {1,D} {3,S} {4,S}
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
    index = 210,
    label = "doublebond_intra_NdNd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    H      U0 {1,S}
4    {Cs,O} U0 {2,S}
5    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "doublebond_intra_NdNd_secNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {2,S}
5    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "doublebond_intra_NdNd_secDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O}        U0 {2,S}
5    {Cs,O}        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "doublebond_intra_NdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D}
2 *3 Cd            U0 {1,D} {3,S} {4,S}
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
    index = 212,
    label = "doublebond_intra_NdDe_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    H             U0 {1,S}
4    {Cs,O}        U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "doublebond_intra_NdCd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    H      U0 {1,S}
4    {Cs,O} U0 {2,S}
5    Cd     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "doublebond_intra_NdCt_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd     U0 {2,D} {3,S}
2 *3 Cd     U0 {1,D} {4,S} {5,S}
3    H      U0 {1,S}
4    {Cs,O} U0 {2,S}
5    Ct     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "doublebond_intra_NdDe_secNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cs,O}        U0 {1,S}
4    {Cs,O}        U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "doublebond_intra_NdDe_secDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O}        U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "doublebond_intra_DeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D}
2 *3 Cd            U0 {1,D} {3,S} {4,S}
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
    index = 216,
    label = "doublebond_intra_DeDe_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "doublebond_intra_DeDe_secNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cs,O}        U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "doublebond_intra_DeDe_secDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd            U0 {2,D} {3,S}
2 *3 Cd            U0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {2,S}
5    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "triplebond_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Ct U0 {2,T}
2 *3 Ct U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "triplebond_intra_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Ct U0 {2,T}
2 *3 Ct U0 {1,T} {3,S}
3    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "triplebond_intra_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Ct     U0 {2,T}
2 *3 Ct     U0 {1,T} {3,S}
3    {Cs,O} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "triplebond_intra_De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Ct            U0 {2,T}
2 *3 Ct            U0 {1,T} {3,S}
3    {Cd,Ct,Cb,CO} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "carbonylbond_intra",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,D}
2 *3 Od U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "carbonylbond_intra_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,D} {3,S}
2 *3 Od U0 {1,D}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "carbonylbond_intra_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO     U0 {2,D} {3,S}
2 *3 Od     U0 {1,D}
3    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "carbonylbond_intra_De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO            U0 {2,D} {3,S}
2 *3 Od            U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "radadd_intra_cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "radadd_intra_cs2H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs U1 {2,S} {3,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "radadd_intra_csHNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs     U1 {2,S} {3,S}
2    H      U0 {1,S}
3    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "radadd_intra_csHDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs            U1 {2,S} {3,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "radadd_intra_csHCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs U1 {2,S} {3,S}
2    H  U0 {1,S}
3    Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "radadd_intra_csHCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs U1 {2,S} {3,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "radadd_intra_csNdNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs     U1 {2,S} {3,S}
2    {Cs,O} U0 {1,S}
3    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "radadd_intra_csNdDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs            U1 {2,S} {3,S}
2    {Cs,O}        U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "radadd_intra_csNdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs     U1 {2,S} {3,S}
2    {Cs,O} U0 {1,S}
3    Cd     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "radadd_intra_csNdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs     U1 {2,S} {3,S}
2    {Cs,O} U0 {1,S}
3    Ct     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "radadd_intra_csDeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs            U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "radadd_intra_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "radadd_intra_Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "radadd_intra_cdsingle",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,S}
2    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "radadd_intra_cdsingleH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,S}
2    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "radadd_intra_cdsingleNd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd     U1 {2,S}
2    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "radadd_intra_cdsingleDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd            U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "radadd_intra_cddouble",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U1 {2,D}
2    Cd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "radadd_intra_CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U1 {2,D}
2    O  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "radadd_intra_Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U1 {2,T}
2    Ct U0 {1,T}
""",
    kinetics = None,
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
            L4: R4_S_D
            L4: R4_S_T
            L4: R4_S_CO
        L3: R4_D
            L4: R4_D_D
            L4: R4_D_T
            L4: R4_D_CO
        L3: R4_T
            L4: R4_T_D
            L4: R4_T_T
            L4: R4_T_CO
        L3: R4_B
            L4: R4_B_D
            L4: R4_B_T
            L4: R4_B_CO
    L2: R5
        L3: R5_SS
            L4: R5_SS_D
            L4: R5_SS_T
            L4: R5_SS_CO
        L3: R5_SD
            L4: R5_SD_D
            L4: R5_SD_T
            L4: R5_SD_CO
        L3: R5_DS
            L4: R5_DS_D
            L4: R5_DS_T
            L4: R5_DS_CO
        L3: R5_ST
            L4: R5_ST_D
            L4: R5_ST_T
            L4: R5_ST_CO
        L3: R5_TS
            L4: R5_TS_D
            L4: R5_TS_T
            L4: R5_TS_CO
        L3: R5_SB
            L4: R5_SB_D
            L4: R5_SB_T
            L4: R5_SB_CO
        L3: R5_BS
            L4: R5_BS_D
            L4: R5_BS_T
            L4: R5_BS_CO
    L2: R6
        L3: R6_RSR
            L4: R6_SSR
                L5: R6_SSS
                    L6: R6_SSS_D
                    L6: R6_SSS_T
                    L6: R6_SSS_CO
                L5: R6_SSM
                    L6: R6_SSM_D
                    L6: R6_SSM_T
                    L6: R6_SSM_CO
            L4: R6_DSR
                L5: R6_DSS
                    L6: R6_DSS_D
                    L6: R6_DSS_T
                    L6: R6_DSS_CO
                L5: R6_DSM
                    L6: R6_DSM_D
                    L6: R6_DSM_T
                    L6: R6_DSM_CO
            L4: R6_TSR
                L5: R6_TSS
                    L6: R6_TSS_D
                    L6: R6_TSS_T
                    L6: R6_TSS_CO
                L5: R6_TSM
                    L6: R6_TSM_D
                    L6: R6_TSM_T
                    L6: R6_TSM_CO
            L4: R6_BSR
                L5: R6_BSS
                    L6: R6_BSS_D
                    L6: R6_BSS_T
                    L6: R6_BSS_CO
                L5: R6_BSM
                    L6: R6_BSM_D
                    L6: R6_BSM_T
                    L6: R6_BSM_CO
        L3: R6_SMS
            L4: R6_SMS_D
            L4: R6_SMS_T
            L4: R6_SMS_CO
        L3: R6_SBB
            L4: R6_SBB_D
            L4: R6_SBB_T
            L4: R6_SBB_CO
        L3: R6_BBS
            L4: R6_BBS_D
            L4: R6_BBS_T
            L4: R6_BBS_CO
    L2: R7
        L3: R7_RSSR
            L4: R7_SSSR
                L5: R7_SSSS
                    L6: R7_SSSS_D
                    L6: R7_SSSS_T
                    L6: R7_SSSS_CO
                L5: R7_SSSM
                    L6: R7_SSSM_D
                    L6: R7_SSSM_T
                    L6: R7_SSSM_CO
            L4: R7_DSSR
                L5: R7_DSSS
                    L6: R7_DSSS_D
                    L6: R7_DSSS_T
                    L6: R7_DSSS_CO
                L5: R7_DSSM
                    L6: R7_DSSM_D
                    L6: R7_DSSM_T
                    L6: R7_DSSM_CO
            L4: R7_TSSR
                L5: R7_TSSS
                    L6: R7_TSSS_D
                    L6: R7_TSSS_T
                    L6: R7_TSSS_CO
                L5: R7_TSSM
                    L6: R7_TSSM_D
                    L6: R7_TSSM_T
                    L6: R7_TSSM_CO
            L4: R7_BSSR
                L5: R7_BSSS
                    L6: R7_BSSS_D
                    L6: R7_BSSS_T
                    L6: R7_BSSS_CO
                L5: R7_BSSM
                    L6: R7_BSSM_D
                    L6: R7_BSSM_T
                    L6: R7_BSSM_CO
        L3: R7_RSMS
            L4: R7_SSMS
                L5: R7_SSMS_D
                L5: R7_SSMS_T
                L5: R7_SSMS_CO
            L4: R7_DSMS
                L5: R7_DSMS_D
                L5: R7_DSMS_T
                L5: R7_DSMS_CO
            L4: R7_TSMS
                L5: R7_TSMS_D
                L5: R7_TSMS_T
                L5: R7_TSMS_CO
            L4: R7_BSMS
                L5: R7_BSMS_D
                L5: R7_BSMS_T
                L5: R7_BSMS_CO
        L3: R7_SMSR
            L4: R7_SMSS
                L5: R7_SMSS_D
                L5: R7_SMSS_T
                L5: R7_SMSS_CO
            L4: R7_SMSM
                L5: R7_SMSM_D
                L5: R7_SMSM_T
                L5: R7_SMSM_CO
        L3: R7_BBSR
            L4: R7_BBSS
                L5: R7_BBSS_D
                L5: R7_BBSS_T
                L5: R7_BBSS_CO
            L4: R7_BBSM
                L5: R7_BBSM_D
                L5: R7_BBSM_T
                L5: R7_BBSM_CO
        L3: R7_RSBB
            L4: R7_SSBB
                L5: R7_SSBB_D
                L5: R7_SSBB_T
                L5: R7_SSBB_CO
            L4: R7_DSBB
                L5: R7_DSBB_D
                L5: R7_DSBB_T
                L5: R7_DSBB_CO
            L4: R7_TSBB
                L5: R7_TSBB_D
                L5: R7_TSBB_T
                L5: R7_TSBB_CO
            L4: R7_BSBB
                L5: R7_BSBB_D
                L5: R7_BSBB_T
                L5: R7_BSBB_CO
        L3: R7_SBBS
            L4: R7_SBBS_D
            L4: R7_SBBS_T
            L4: R7_SBBS_CO
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
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,{S,D}}
2 *1 R!H U1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "cdd2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cdd U0
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

