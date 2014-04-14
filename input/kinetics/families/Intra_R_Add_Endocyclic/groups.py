#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCyclic"], ownReverse=False)

reverse = "Ring_Open_Endo_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', '-1', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "Rn",
    group = "OR{R3, R4, R5, R6, R7, R8, R9}",
    kinetics = None,
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
1 *2 {Cd,Cdd,Ct,CO,N}    0 {2,{D,T}}
2 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {1,{D,T}}
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
    group = 
"""
1 *1 R!H 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R3",
    group = 
"""
1 *1 R!H                 1 {2,S}
2 *2 {Cd,Ct,CO,N}        0 {1,S} {3,{D,T}}
3 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {2,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R3_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *2 Cd  0 {1,S} {3,D}
3 *3 {Cd,Cdd}  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "R3_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *2 Ct  0 {1,S} {3,T}
3 *3 Ct  0 {2,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "R3_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *2 CO  0 {1,S} {3,D}
3 *3 Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "R3_C=S",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *2 Cd  0 {1,S} {3,D}
3 *3 Sd  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "R4",
    group = 
"""
1 *1 R!H                 1           {2,{S,D,T,B}}
2 *4 R!H                 {0,1,2S,2T} {1,{S,D,T,B}} {3,S}
3 *2 {Cd,Ct,CO,N}        0           {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Sd,Cdd,N} 0           {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "R4_S",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 R!H           0 {1,S} {3,S}
3 *2 {Cd,Ct,CO}    0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Sd,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "R4_S_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 Cd  0 {2,S} {4,D}
4 *3 {Cd,Cdd}  0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "R4_S_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 Ct  0 {2,S} {4,T}
4 *3 Ct  0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "R4_S_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 CO  0 {2,S} {4,D}
4 *3 Od  0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "R4_D",
    group = 
"""
1 *1 Cd            1 {2,D}
2 *4 Cd            0 {1,D} {3,S}
3 *2 {Cd,Ct,CO}    0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Sd,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "R4_D_D",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 Cd 0 {2,S} {4,D}
4 *3 {Cd,Cdd} 0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "R4_D_T",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 Ct 0 {2,S} {4,T}
4 *3 Ct 0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "R4_D_CO",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 CO 0 {2,S} {4,D}
4 *3 Od 0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "R4_T",
    group = 
"""
1 *1 Ct            1 {2,T}
2 *4 Ct            0 {1,T} {3,S}
3 *2 {Cd,Ct,CO}    0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Sd,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "R4_T_D",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 Cd 0 {2,S} {4,D}
4 *3 {Cd,Cdd} 0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "R4_T_T",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 Ct 0 {2,S} {4,T}
4 *3 Ct 0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "R4_T_CO",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 CO 0 {2,S} {4,D}
4 *3 Od 0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "R4_B",
    group = 
"""
1 *1 Cb            1 {2,B}
2 *4 Cb            0 {1,B} {3,S}
3 *2 {Cd,Ct,CO}    0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Sd,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "R4_B_D",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 Cd 0 {2,S} {4,D}
4 *3 {Cd,Cdd} 0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "R4_B_T",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 Ct 0 {2,S} {4,T}
4 *3 Ct 0 {3,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "R4_B_CO",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 CO 0 {2,S} {4,D}
4 *3 Od 0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "R5",
    group = 
"""
1 *1 R!H           1           {2,{S,D,T,B}}
2 *4 R!H           {0,1,2S,2T} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *5 R!H           {0,1,2S,2T} {2,{S,D,T,B}} {4,S}
4 *2 {Cd,Ct,CO,N}    0           {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0           {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 27,
    label = "R5_SS",
    group = 
"""
1 *1 R!H                 1 {2,S}
2 *4 R!H                 0 {1,S} {3,S}
3 *5 R!H                 0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
""",
)

entry(
    index = 28,
    label = "R5_SS_D",
    group = 
"""
1 *1 R!H       1 {2,S}
2 *4 R!H       0 {1,S} {3,S}
3 *5 R!H       0 {2,S} {4,S}
4 *2 Cd        0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 29,
    label = "R5_SS_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 30,
    label = "R5_SS_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 31,
    label = "R5_SD",
    group = 
"""
1 *1 R!H                 1 {2,S}
2 *4 Cd                  0 {1,S} {3,D}
3 *5 Cd                  0 {2,D} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
""",
)

entry(
    index = 32,
    label = "R5_SD_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 33,
    label = "R5_SD_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 34,
    label = "R5_SD_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 35,
    label = "R5_DS",
    group = 
"""
1 *1 Cd                  1 {2,D}
2 *4 Cd                  0 {1,D} {3,S}
3 *5 R!H                 0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Cdd,Ct,Od,Sd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
""",
)

entry(
    index = 36,
    label = "R5_DS_D",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 37,
    label = "R5_DS_T",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 38,
    label = "R5_DS_CO",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 39,
    label = "R5_ST",
    group = 
"""
1 *1 R!H                 1 {2,S}
2 *4 Ct                  0 {1,S} {3,T}
3 *5 Ct                  0 {2,T} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
""",
)

entry(
    index = 40,
    label = "R5_ST_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *5 Ct  0 {2,T} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 44,
    label = "R5_ST_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *5 Ct  0 {2,T} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 45,
    label = "R5_ST_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *5 Ct  0 {2,T} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 46,
    label = "R5_TS",
    group = 
"""
1 *1 Ct                  1 {2,T}
2 *4 Ct                  0 {1,T} {3,S}
3 *5 R!H                 0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
""",
)

entry(
    index = 47,
    label = "R5_TS_D",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 48,
    label = "R5_TS_T",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 49,
    label = "R5_TS_CO",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 50,
    label = "R5_SB",
    group = 
"""
1 *1 R!H                 1 {2,S}
2 *4 Cb                  0 {1,S} {3,B}
3 *5 Cb                  0 {2,B} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then aromatic. (The next is a single)
""",
)

entry(
    index = 51,
    label = "R5_SB_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then aromatic. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 52,
    label = "R5_SB_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then aromatic. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 53,
    label = "R5_SB_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then aromatic. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 54,
    label = "R5_BS",
    group = 
"""
1 *1 Cb                  1 {2,B}
2 *4 Cb                  0 {1,B} {3,S}
3 *5 R!H                 0 {2,S} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "R5_BS_D",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "R5_BS_T",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "R5_BS_CO",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "R5_BB",
    group = 
"""
1 *1 Cb                  1 {2,B}
2 *4 Cbf                 0 {1,B} {3,B}
3 *5 Cb                  0 {2,B} {4,S}
4 *2 {Cd,Ct,CO,N}        0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {4,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "R5_BB_D",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "R5_BB_T",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 Ct  0 {3,S} {5,T}
5 *3 Ct  0 {4,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "R5_BB_CO",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 CO  0 {3,S} {5,D}
5 *3 Od  0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "R6",
    group = 
"""
1 *1 R!H                 1           {2,{S,D,T,B}}
2 *4 R!H                 {0,1,2S,2T} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H                 {0,1,2S,2T} {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *5 R!H                 {0,1,2S,2T} {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO,N}        0           {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd,N} 0           {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H                 1 {2,{S,D,T,B}}
2 *4 R!H                 0 {1,{S,D,T,B}} {3,S}
3 *6 R!H                 0 {2,S} {4,{S,D,T,B}}
4 *5 R!H                 0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO,N}        0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 R!H           0 {1,S} {3,S}
3 *6 R!H           0 {2,S} {4,{S,D,T,B}}
4 *5 R!H           0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 R!H           0 {1,S} {3,S}
3 *6 R!H           0 {2,S} {4,S}
4 *5 R!H           0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "R6_SSS_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "R6_SSS_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "R6_SSS_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 R!H           0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb}    0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}    0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "R6_SSM_D",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "R6_SSM_T",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "R6_SSM_CO",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "R6_DSR",
    group = 
"""
1 *1 Cd            1 {2,D}
2 *4 Cd            0 {1,D} {3,S}
3 *6 R!H           0 {2,S} {4,{S,D,T,B}}
4 *5 R!H           0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "R6_DSS",
    group = 
"""
1 *1 Cd            1 {2,D}
2 *4 Cd            0 {1,D} {3,S}
3 *6 R!H           0 {2,S} {4,S}
4 *5 R!H           0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "R6_DSS_D",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "R6_DSS_T",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "R6_DSS_CO",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd            1 {2,D}
2 *4 Cd            0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb}    0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}    0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "R6_DSM_D",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "R6_DSM_T",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "R6_DSM_CO",
    group = 
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct            1 {2,T}
2 *4 Ct            0 {1,T} {3,S}
3 *6 R!H           0 {2,S} {4,{S,D,T,B}}
4 *5 R!H           0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "R6_TSS",
    group = 
"""
1 *1 Ct            1 {2,T}
2 *4 Ct            0 {1,T} {3,S}
3 *6 R!H           0 {2,S} {4,S}
4 *5 R!H           0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "R6_TSS_D",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "R6_TSS_T",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "R6_TSS_CO",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct            1 {2,T}
2 *4 Ct            0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb}    0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}    0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "R6_TSM_D",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "R6_TSM_T",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "R6_TSM_CO",
    group = 
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "R6_BSR",
    group = 
"""
1 *1 Cb            1 {2,B}
2 *4 Cb            0 {1,B} {3,S}
3 *6 R!H           0 {2,S} {4,{S,D,T,B}}
4 *5 R!H           0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "R6_BSS",
    group = 
"""
1 *1 Cb            1 {2,B}
2 *4 Cb            0 {1,B} {3,S}
3 *6 R!H           0 {2,S} {4,S}
4 *5 R!H           0 {3,S} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "R6_BSS_D",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "R6_BSS_T",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "R6_BSS_CO",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *6 R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "R6_BSM",
    group = 
"""
1 *1 Cb            1 {2,B}
2 *4 Cb            0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb}    0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb}    0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "R6_BSM_D",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "R6_BSM_T",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "R6_BSM_CO",
    group = 
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *6 {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 {Cd,Ct,Cb}    0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb}    0 {2,{D,T,B}} {4,S}
4 *5 R!H           0 {3,S} {5,S}
5 *2 {Cd,Ct,CO,N}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "R6_SMS_D",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "R6_SMS_T",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "R6_SMS_CO",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *6 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "R6_SBB",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 Cb            0 {1,S} {3,B}
3 *6 Cbf           0 {2,B} {4,B}
4 *5 Cb            0 {3,B} {5,S}
5 *2 {Cd,Ct,CO,N}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "R6_SBB_D",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "R6_SBB_T",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "R6_SBB_CO",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *6 Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "R6_BBS",
    group = 
"""
1 *1 Cb            1 {2,B}
2 *4 Cbf           0 {1,B} {3,B}
3 *6 Cb            0 {2,B} {4,S}
4 *5 R!H           0 {3,S} {5,S}
5 *2 {Cd,Ct,CO,N}    0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {5,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "R6_BBS_D",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "R6_BBS_T",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "R6_BBS_CO",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *6 Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "R7",
    group = 
"""
1 *1 R!H           1           {2,{S,D,T,B}}
2 *4 R!H           {0,1,2S,2T} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H           {0,1,2S,2T} {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *7 R!H           {0,1,2S,2T} {3,{S,D,T,B}} {5,{S,D,T,B}}
5 *5 R!H           {0,1,2S,2T} {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO,N}    0           {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Sd,Cdd,N} 0           {6,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "R8",
    group = 
"""
1 *1 R!H           1           {2,{S,D,T,B}}
2 *4 R!H           {0,1,2S,2T} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H           {0,1,2S,2T} {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *7 R!H           {0,1,2S,2T} {3,{S,D,T,B}} {5,{S,D,T,B}}
5 *8 R!H           {0,1,2S,2T} {4,{S,D,T,B}} {6,{S,D,T,B}}
6 *5 R!H           {0,1,2S,2T} {5,{S,D,T,B}} {7,S}
7 *2 {Cd,Ct,CO,N}    0           {6,S} {8,{D,T}}
8 *3 {Cd,Ct,Od,Sd,Cdd,N} 0           {7,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "R9",
    group = 
"""
1 *1 R!H           1           {2,{S,D,T,B}}
2 *4 R!H           {0,1,2S,2T} {1,{S,D,T,B}} {3,{S,D,T,B}}
3 *6 R!H           {0,1,2S,2T} {2,{S,D,T,B}} {4,{S,D,T,B}}
4 *7 R!H           {0,1,2S,2T} {3,{S,D,T,B}} {5,{S,D,T,B}}
5 *8 R!H           {0,1,2S,2T} {4,{S,D,T,B}} {6,{S,D,T,B}}
6 *9 R!H           {0,1,2S,2T} {5,{S,D,T,B}} {7,{S,D,T,B}}
7 *5 R!H           {0,1,2S,2T} {6,{S,D,T,B}} {8,S}
8 *2 {Cd,Ct,CO,N}    0           {7,S} {9,{D,T}}
9 *3 {Cd,Ct,Od,Sd,Cdd,N} 0           {8,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "R9_SSSSSD",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 R!H           0 {1,S} {3,S}
3 *6 R!H           0 {2,S} {4,S}
4 *7 R!H           0 {3,S} {5,S}
5 *8 R!H           0 {4,S} {6,S}
6 *9 R!H           0 {5,S} {7,D}
7 *5 R!H           0 {6,D} {8,S}
8 *2 {Cd,Ct,CO,N}    0 {7,S} {9,{D,T}}
9 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {8,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "R9_SDSSSD",
    group = 
"""
1 *1 R!H           1 {2,S}
2 *4 R!H           0 {1,S} {3,D}
3 *6 R!H           0 {2,D} {4,S}
4 *7 R!H           0 {3,S} {5,S}
5 *8 R!H           0 {4,S} {6,S}
6 *9 R!H           0 {5,S} {7,D}
7 *5 R!H           0 {6,D} {8,S}
8 *2 {Cd,Ct,CO,N}    0 {7,S} {9,{D,T}}
9 *3 {Cd,Ct,Od,Sd,Cdd,N} 0 {8,{D,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "doublebond_intra",
    group = 
"""
1 *2 Cd 0 {2,D}
2 *3 {Cd,Cdd} 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
Note that nodes below this currently do not match allenic type Cdd atoms for *3,
so this is the most specific group that will match such a molecule.
""",
)

entry(
    index = 115,
    label = "doublebond_intra_pri",
    group = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "doublebond_intra_pri_2H",
    group = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "doublebond_intra_pri_HNd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    H        0 {1,S}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "doublebond_intra_pri_HDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "doublebond_intra_pri_HCd",
    group = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    Cd 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "doublebond_intra_pri_HCt",
    group = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    Ct 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "doublebond_intra_pri_NdNd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "doublebond_intra_pri_NdDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    {Cs,O,S}      0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "doublebond_intra_pri_NdCd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {2,S}
5    Cd       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "doublebond_intra_pri_NdCt",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {2,S}
5    Ct       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "doublebond_intra_pri_DeDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "doublebond_intra_secNd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "doublebond_intra_secNd_2H",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
5    H        0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "doublebond_intra_secNd_HNd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "doublebond_intra_secNd_HDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cs,O,S}      0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "doublebond_intra_secNd_HCd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
5    Cd       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "doublebond_intra_secNd_HCt",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
5    Ct       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "doublebond_intra_secNd_NdNd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "doublebond_intra_secNd_NdDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cs,O,S}      0 {1,S}
4    {Cs,O,S}      0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "doublebond_intra_secNd_NdCd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {2,S}
5    Cd       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "doublebond_intra_secNd_NdCt",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Cd       0 {1,D} {4,S} {5,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {2,S}
5    Ct       0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "doublebond_intra_secNd_DeDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cs,O,S}      0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "doublebond_intra_secDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "doublebond_intra_secDe_2H",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    H             0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "doublebond_intra_secDe_HNd",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    {Cs,O,S}      0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "doublebond_intra_secDe_HDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "doublebond_intra_secDe_HCd",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    Cd            0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "doublebond_intra_secDe_HCt",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    Ct            0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "doublebond_intra_secDe_NdNd",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O,S}      0 {2,S}
5    {Cs,O,S}      0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "doublebond_intra_secDe_NdDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O,S}      0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "doublebond_intra_secDe_NdCd",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O,S}      0 {2,S}
5    Cd            0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "doublebond_intra_secDe_NdCt",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O,S}      0 {2,S}
5    Ct            0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "doublebond_intra_secDe_DeDe",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct 0 {2,T}
2 *3 Ct 0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "triplebond_intra_H",
    group = 
"""
1 *2 Ct 0 {2,T}
2 *3 Ct 0 {1,T} {3,S}
3    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "triplebond_intra_Nd",
    group = 
"""
1 *2 Ct       0 {2,T}
2 *3 Ct       0 {1,T} {3,S}
3    {Cs,O,S} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "triplebond_intra_De",
    group = 
"""
1 *2 Ct            0 {2,T}
2 *3 Ct            0 {1,T} {3,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "carbonyl_intra",
    group = 
"""
1 *2 CO 0 {2,D}
2 *3 Od  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "carbonyl_intra_H",
    group = 
"""
1 *2 CO 0 {2,D} {3,S}
2 *3 Od  0 {1,D}
3    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "carbonyl_intra_Nd",
    group = 
"""
1 *2 CO       0 {2,D} {3,S}
2 *3 Od        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "carbonyl_intra_De",
    group = 
"""
1 *2 CO            0 {2,D} {3,S}
2 *3 Od             0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "thiyl_intra",
    group = 
"""
1 *2 Cd 0 {2,D}
2 *3 Sd 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "thiyl_intra_H",
    group = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Sd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "thiyl_intra_Nd",
    group = 
"""
1 *2 Cd       0 {2,D} {3,S}
2 *3 Sd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "thiyl_intra_De",
    group = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Sd            0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "radadd_intra_cs2H",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "radadd_intra_csHNd",
    group = 
"""
1 *1 Cs       1 {2,S} {3,S}
2    H        0 {1,S}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "radadd_intra_csHDe",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "radadd_intra_csHCd",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "radadd_intra_csHCt",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs       1 {2,S} {3,S}
2    {Cs,O,S} 0 {1,S}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S}
2    {Cs,O,S}      0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs       1 {2,S} {3,S}
2    {Cs,O,S} 0 {1,S}
3    Cd       0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs       1 {2,S} {3,S}
2    {Cs,O,S} 0 {1,S}
3    Ct       0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs            1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "radadd_intra_S",
    group = 
"""
1 *1 S 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb 1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd 1 {2,S}
2    R  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd       1 {2,S}
2    {Cs,O,S} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd            1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd 1 {2,D}
2    Cd 0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO 1 {2,D}
2    O  0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct 1 {2,T}
2    Ct 0 {1,T}
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
    L2: R3
        L3: R3_D
        L3: R3_T
        L3: R3_CO
        L3: R3_C=S
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
        L3: R5_BB
            L4: R5_BB_D
            L4: R5_BB_T
            L4: R5_BB_CO
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
    L2: R8
    L2: R9
        L3: R9_SSSSSD
        L3: R9_SDSSSD
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_pri
            L4: doublebond_intra_pri_2H
            L4: doublebond_intra_pri_HNd
            L4: doublebond_intra_pri_HDe
                L5: doublebond_intra_pri_HCd
                L5: doublebond_intra_pri_HCt
            L4: doublebond_intra_pri_NdNd
            L4: doublebond_intra_pri_NdDe
                L5: doublebond_intra_pri_NdCd
                L5: doublebond_intra_pri_NdCt
            L4: doublebond_intra_pri_DeDe
        L3: doublebond_intra_secNd
            L4: doublebond_intra_secNd_2H
            L4: doublebond_intra_secNd_HNd
            L4: doublebond_intra_secNd_HDe
                L5: doublebond_intra_secNd_HCd
                L5: doublebond_intra_secNd_HCt
            L4: doublebond_intra_secNd_NdNd
            L4: doublebond_intra_secNd_NdDe
                L5: doublebond_intra_secNd_NdCd
                L5: doublebond_intra_secNd_NdCt
            L4: doublebond_intra_secNd_DeDe
        L3: doublebond_intra_secDe
            L4: doublebond_intra_secDe_2H
            L4: doublebond_intra_secDe_HNd
            L4: doublebond_intra_secDe_HDe
                L5: doublebond_intra_secDe_HCd
                L5: doublebond_intra_secDe_HCt
            L4: doublebond_intra_secDe_NdNd
            L4: doublebond_intra_secDe_NdDe
                L5: doublebond_intra_secDe_NdCd
                L5: doublebond_intra_secDe_NdCt
            L4: doublebond_intra_secDe_DeDe
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
    L2: carbonyl_intra
        L3: carbonyl_intra_H
        L3: carbonyl_intra_Nd
        L3: carbonyl_intra_De
    L2: thiyl_intra
        L3: thiyl_intra_H
        L3: thiyl_intra_Nd
        L3: thiyl_intra_De
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
    L2: radadd_intra_S
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
    label = "bond31",
    group = 
"""
1 *3 R!H 0 {2,{S,D}}
2 *1 R!H 1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "bond31rad",
    group = 
"""
1 *3 R!H 1 {2,{S,D}}
2 *1 R!H 1 {1,{S,D}}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

