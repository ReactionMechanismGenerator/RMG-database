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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "multiplebond_intra",
    group =
"""
1 *2 {Cd,Ct,CO} 0 {2,{D,T}}
2 *3 {Cd,Ct,Od,Cdd} 0 {1,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 3,
    label = "radadd_intra",
    group =
"""
1 *1 R!H 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "R4",
    group =
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3 *2 {Cd,Ct,CO} 0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 5,
    label = "R4_S",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *2 {Cd,Ct,CO} 0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 6,
    label = "R4_S_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 Cd  0 {2,S} {4,D}
4 *3 {Cd,Cdd}  0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 7,
    label = "R4_S_T",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 Ct  0 {2,S} {4,T}
4 *3 Ct  0 {3,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "R4_S_CO",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 CO  0 {2,S} {4,D}
4 *3 Od  0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "R4_D",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *2 {Cd,Ct,CO} 0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 10,
    label = "R4_D_D",
    group =
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 Cd 0 {2,S} {4,D}
4 *3 {Cd,Cdd} 0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 11,
    label = "R4_D_T",
    group =
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 Ct 0 {2,S} {4,T}
4 *3 Ct 0 {3,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "R4_D_CO",
    group =
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *2 CO 0 {2,S} {4,D}
4 *3 Od 0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "R4_T",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *2 {Cd,Ct,CO} 0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 14,
    label = "R4_T_D",
    group =
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 Cd 0 {2,S} {4,D}
4 *3 {Cd,Cdd} 0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 15,
    label = "R4_T_T",
    group =
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 Ct 0 {2,S} {4,T}
4 *3 Ct 0 {3,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "R4_T_CO",
    group =
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *2 CO 0 {2,S} {4,D}
4 *3 Od 0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "R4_B",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *2 {Cd,Ct,CO} 0 {2,S} {4,{D,T}}
4 *3 {Cd,Ct,Od,Cdd} 0 {3,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 18,
    label = "R4_B_D",
    group =
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 Cd 0 {2,S} {4,D}
4 *3 {Cd,Cdd} 0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 19,
    label = "R4_B_T",
    group =
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 Ct 0 {2,S} {4,T}
4 *3 Ct 0 {3,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "R4_B_CO",
    group =
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *2 CO 0 {2,S} {4,D}
4 *3 Od 0 {3,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "R5",
    group = "OR{R5_SS, R5_SD, R5_DS, R5_ST, R5_TS, R5_SB, R5_BS}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "R5_SS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3 *5 R!H        0 {2,S} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 23,
    label = "R5_SS_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 {Cd,Cdd}  0 {4,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 24,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "R5_SD",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 Cd         0 {1,S} {3,D}
3 *5 Cd         0 {2,D} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 27,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 28,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "R5_DS",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3 *5 R!H        0 {2,S} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 31,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 32,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "R5_ST",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 Ct         0 {1,S} {3,T}
3 *5 Ct         0 {2,T} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 35,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 36,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "R5_TS",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3 *5 R!H        0 {2,S} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 39,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 40,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "R5_SB",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 Cb         0 {1,S} {3,B}
3 *5 Cb         0 {2,B} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 43,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 44,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "R5_BS",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3 *5 R!H        0 {2,S} {4,S}
4 *2 {Cd,Ct,CO} 0 {3,S} {5,{D,T}}
5 *3 {Cd,Ct,Od,Cdd} 0 {4,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 47,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 48,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "R6",
    group = "OR{R6_RSR, R6_SMS, R6_SBB, R6_BBS}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "R6_RSR",
    group =
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3    R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 52,
    label = "R6_SSR",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 53,
    label = "R6_SSS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 54,
    label = "R6_SSS_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 55,
    label = "R6_SSS_T",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "R6_SSS_CO",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "R6_SSM",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 58,
    label = "R6_SSM_D",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 59,
    label = "R6_SSM_T",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "R6_SSM_CO",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "R6_DSR",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 62,
    label = "R6_DSS",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 63,
    label = "R6_DSS_D",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 64,
    label = "R6_DSS_T",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "R6_DSS_CO",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "R6_DSM",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 67,
    label = "R6_DSM_D",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 68,
    label = "R6_DSM_T",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "R6_DSM_CO",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "R6_TSR",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 71,
    label = "R6_TSS",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 72,
    label = "R6_TSS_D",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 73,
    label = "R6_TSS_T",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "R6_TSS_CO",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "R6_TSM",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 76,
    label = "R6_TSM_D",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 77,
    label = "R6_TSM_T",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "R6_TSM_CO",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "R6_BSR",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,{S,D,T,B}}
4 *5 R!H        0 {3,{S,D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 80,
    label = "R6_BSS",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 81,
    label = "R6_BSS_D",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 82,
    label = "R6_BSS_T",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "R6_BSS_CO",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "R6_BSM",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 85,
    label = "R6_BSM_D",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 86,
    label = "R6_BSM_T",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "R6_BSM_CO",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4 *5 {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "R6_SMS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 89,
    label = "R6_SMS_D",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 Cd         0 {4,S} {6,D}
6 *3 {Cd,Cdd}         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 90,
    label = "R6_SMS_T",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 Ct         0 {4,S} {6,T}
6 *3 Ct         0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "R6_SMS_CO",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 CO         0 {4,S} {6,D}
6 *3 Od         0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "R6_SBB",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 Cb         0 {1,S} {3,B}
3    Cbf        0 {2,B} {4,B}
4 *5 Cb         0 {3,B} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 93,
    label = "R6_SBB_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 94,
    label = "R6_SBB_T",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "R6_SBB_CO",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "R6_BBS",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4 *5 R!H        0 {3,S} {5,S}
5 *2 {Cd,Ct,CO} 0 {4,S} {6,{D,T}}
6 *3 {Cd,Ct,Od,Cdd} 0 {5,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 97,
    label = "R6_BBS_D",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 {Cd,Cdd}  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 98,
    label = "R6_BBS_T",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Ct  0 {4,S} {6,T}
6 *3 Ct  0 {5,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "R6_BBS_CO",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 CO  0 {4,S} {6,D}
6 *3 Od  0 {5,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "R7",
    group = "OR{R7_RSSR, R7_RSMS, R7_SMSR, R7_BBSR, R7_RSBB, R7_SBBS}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "R7_RSSR",
    group =
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 102,
    label = "R7_SSSR",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 103,
    label = "R7_SSSS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 104,
    label = "R7_SSSS_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 105,
    label = "R7_SSSS_T",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "R7_SSSS_CO",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "R7_SSSM",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 108,
    label = "R7_SSSM_D",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 109,
    label = "R7_SSSM_T",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "R7_SSSM_CO",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "R7_DSSR",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 112,
    label = "R7_DSSS",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 113,
    label = "R7_DSSS_D",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 114,
    label = "R7_DSSS_T",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "R7_DSSS_CO",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "R7_DSSM",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 117,
    label = "R7_DSSM_D",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}   0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 118,
    label = "R7_DSSM_T",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "R7_DSSM_CO",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "R7_TSSR",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 121,
    label = "R7_TSSS",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 122,
    label = "R7_TSSS_D",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 123,
    label = "R7_TSSS_T",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "R7_TSSS_CO",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "R7_TSSM",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 126,
    label = "R7_TSSM_D",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 127,
    label = "R7_TSSM_T",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "R7_TSSM_CO",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "R7_BSSR",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 130,
    label = "R7_BSSS",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 131,
    label = "R7_BSSS_D",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 132,
    label = "R7_BSSS_T",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "R7_BSSS_CO",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "R7_BSSM",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 135,
    label = "R7_BSSM_D",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 136,
    label = "R7_BSSM_T",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "R7_BSSM_CO",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    R!H        0 {2,S} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "R7_RSMS",
    group =
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 139,
    label = "R7_SSMS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 140,
    label = "R7_SSMS_D",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 141,
    label = "R7_SSMS_T",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "R7_SSMS_CO",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "R7_DSMS",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 144,
    label = "R7_DSMS_D",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 145,
    label = "R7_DSMS_T",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "R7_DSMS_CO",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "R7_TSMS",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 148,
    label = "R7_TSMS_D",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 149,
    label = "R7_TSMS_T",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "R7_TSMS_CO",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "R7_BSMS",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 152,
    label = "R7_BSMS_D",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 153,
    label = "R7_BSMS_T",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "R7_BSMS_CO",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    {Cd,Ct,Cb} 0 {2,S} {4,{D,T,B}}
4    {Cd,Ct,Cb} 0 {3,{D,T,B}} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "R7_SMSR",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 156,
    label = "R7_SMSS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 157,
    label = "R7_SMSS_D",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 158,
    label = "R7_SMSS_T",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    label = "R7_SMSS_CO",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    label = "R7_SMSM",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 161,
    label = "R7_SMSM_D",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 162,
    label = "R7_SMSM_T",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    label = "R7_SMSM_CO",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3    {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "R7_BBSR",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4    R!H        0 {3,S} {5,{S,D,T,B}}
5 *5 R!H        0 {4,{S,D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 165,
    label = "R7_BBSS",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4    R!H        0 {3,S} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 166,
    label = "R7_BBSS_D",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 167,
    label = "R7_BBSS_T",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    label = "R7_BBSS_CO",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    label = "R7_BBSM",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 170,
    label = "R7_BBSM_D",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Cd         0 {5,S} {7,D}
7 *3 {Cd,Cdd}         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "R7_BBSM_T",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 Ct         0 {5,S} {7,T}
7 *3 Ct         0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    label = "R7_BBSM_CO",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cbf        0 {1,B} {3,B}
3    Cb         0 {2,B} {4,S}
4    {Cd,Ct,Cb} 0 {3,S} {5,{D,T,B}}
5 *5 {Cd,Ct,Cb} 0 {4,{D,T,B}} {6,S}
6 *2 CO         0 {5,S} {7,D}
7 *3 Od         0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    label = "R7_RSBB",
    group =
"""
1 *1 R!H        1 {2,{S,D,T,B}}
2 *4 R!H        0 {1,{S,D,T,B}} {3,S}
3    Cb         0 {2,S} {4,B}
4    Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 174,
    label = "R7_SSBB",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 R!H        0 {1,S} {3,S}
3    Cb         0 {2,S} {4,B}
4    Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 175,
    label = "R7_SSBB_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 176,
    label = "R7_SSBB_T",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    label = "R7_SSBB_CO",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    label = "R7_DSBB",
    group =
"""
1 *1 Cd         1 {2,D}
2 *4 Cd         0 {1,D} {3,S}
3    Cb         0 {2,S} {4,B}
4    Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 179,
    label = "R7_DSBB_D",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 180,
    label = "R7_DSBB_T",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "R7_DSBB_CO",
    group =
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "R7_TSBB",
    group =
"""
1 *1 Ct         1 {2,T}
2 *4 Ct         0 {1,T} {3,S}
3    Cb         0 {2,S} {4,B}
4    Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 183,
    label = "R7_TSBB_D",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 184,
    label = "R7_TSBB_T",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "R7_TSBB_CO",
    group =
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "R7_BSBB",
    group =
"""
1 *1 Cb         1 {2,B}
2 *4 Cb         0 {1,B} {3,S}
3    Cb         0 {2,S} {4,B}
4    Cbf        0 {3,B} {5,B}
5 *5 Cb         0 {4,B} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 187,
    label = "R7_BSBB_D",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 188,
    label = "R7_BSBB_T",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    label = "R7_BSBB_CO",
    group =
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    label = "R7_SBBS",
    group =
"""
1 *1 R!H        1 {2,S}
2 *4 Cb         0 {1,S} {3,B}
3    Cbf        0 {2,B} {4,B}
4    Cb         0 {3,B} {5,S}
5 *5 R!H        0 {4,S} {6,S}
6 *2 {Cd,Ct,CO} 0 {5,S} {7,{D,T}}
7 *3 {Cd,Ct,Od,Cdd} 0 {6,{D,T}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 191,
    label = "R7_SBBS_D",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Cd  0 {5,S} {7,D}
7 *3 {Cd,Cdd}  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("May 2 2013","Fariba Seyedzadeh Khanshan <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba added Cdd atom type to *3."""),
    ],
)

entry(
    index = 192,
    label = "R7_SBBS_T",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 Ct  0 {5,S} {7,T}
7 *3 Ct  0 {6,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    label = "R7_SBBS_CO",
    group =
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 CO  0 {5,S} {7,D}
7 *3 Od  0 {6,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    label = "doublebond_intra",
    group =
"""
1 *2 Cd 0 {2,D}
2 *3 {Cd,Cdd} 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    label = "doublebond_intra_2H",
    group =
"""
1 *2 Cd 0 {2,D}
2 *3 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    label = "doublebond_intra_2H_pri",
    group =
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    label = "doublebond_intra_2H_secNd",
    group =
"""
1 *2 Cd     0 {2,D} {3,S}
2 *3 Cd     0 {1,D} {4,S} {5,S}
3    {Cs,O} 0 {1,S}
4    H      0 {2,S}
5    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    label = "doublebond_intra_2H_secDe",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    label = "doublebond_intra_HNd",
    group =
"""
1 *2 Cd     0 {2,D}
2 *3 Cd     0 {1,D} {3,S} {4,S}
3    H      0 {2,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    label = "doublebond_intra_HNd_pri",
    group =
"""
1 *2 Cd     0 {2,D} {3,S}
2 *3 Cd     0 {1,D} {4,S} {5,S}
3    H      0 {1,S}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    label = "doublebond_intra_HNd_secNd",
    group =
"""
1 *2 Cd     0 {2,D} {3,S}
2 *3 Cd     0 {1,D} {4,S} {5,S}
3    {Cs,O} 0 {1,S}
4    H      0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    label = "doublebond_intra_HNd_secDe",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    label = "doublebond_intra_HDe",
    group =
"""
1 *2 Cd            0 {2,D}
2 *3 Cd            0 {1,D} {3,S} {4,S}
3    H             0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    label = "doublebond_intra_HDe_pri",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    label = "doublebond_intra_HDe_secNd",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cs,O}        0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    label = "doublebond_intra_HDe_secDe",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    label = "doublebond_intra_NdNd",
    group =
"""
1 *2 Cd     0 {2,D}
2 *3 Cd     0 {1,D} {3,S} {4,S}
3    {Cs,O} 0 {2,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 208,
    label = "doublebond_intra_NdNd_pri",
    group =
"""
1 *2 Cd     0 {2,D} {3,S}
2 *3 Cd     0 {1,D} {4,S} {5,S}
3    H      0 {1,S}
4    {Cs,O} 0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    label = "doublebond_intra_NdNd_secNd",
    group =
"""
1 *2 Cd     0 {2,D} {3,S}
2 *3 Cd     0 {1,D} {4,S} {5,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {2,S}
5    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    label = "doublebond_intra_NdNd_secDe",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    label = "doublebond_intra_NdDe",
    group =
"""
1 *2 Cd            0 {2,D}
2 *3 Cd            0 {1,D} {3,S} {4,S}
3    {Cs,O}        0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    label = "doublebond_intra_NdDe_pri",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    label = "doublebond_intra_NdDe_secNd",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    label = "doublebond_intra_NdDe_secDe",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    label = "doublebond_intra_DeDe",
    group =
"""
1 *2 Cd            0 {2,D}
2 *3 Cd            0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    label = "doublebond_intra_DeDe_pri",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    label = "doublebond_intra_DeDe_secNd",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    label = "doublebond_intra_DeDe_secDe",
    group =
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 219,
    label = "triplebond_intra",
    group =
"""
1 *2 Ct 0 {2,T}
2 *3 Ct 0 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    label = "triplebond_intra_H",
    group =
"""
1 *2 Ct 0 {2,T}
2 *3 Ct 0 {1,T} {3,S}
3    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    label = "triplebond_intra_Nd",
    group =
"""
1 *2 Ct     0 {2,T}
2 *3 Ct     0 {1,T} {3,S}
3    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    label = "triplebond_intra_De",
    group =
"""
1 *2 Ct            0 {2,T}
2 *3 Ct            0 {1,T} {3,S}
3    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    label = "carbonylbond_intra",
    group =
"""
1 *2 CO 0 {2,D}
2 *3 Od 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    label = "carbonylbond_intra_H",
    group =
"""
1 *2 CO 0 {2,D} {3,S}
2 *3 Od 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    label = "carbonylbond_intra_Nd",
    group =
"""
1 *2 CO     0 {2,D} {3,S}
2 *3 Od     0 {1,D}
3    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    label = "carbonylbond_intra_De",
    group =
"""
1 *2 CO            0 {2,D} {3,S}
2 *3 Od            0 {1,D}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    label = "radadd_intra_cs",
    group =
"""
1 *1 Cs 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    label = "radadd_intra_csNdNd",
    group =
"""
1 *1 Cs     1 {2,S} {3,S}
2    {Cs,O} 0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    label = "radadd_intra_csNdDe",
    group =
"""
1 *1 Cs            1 {2,S} {3,S}
2    {Cs,O}        0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    label = "radadd_intra_csDeDe",
    group =
"""
1 *1 Cs            1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    label = "radadd_intra_O",
    group =
"""
1 *1 O 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    label = "radadd_intra_Cb",
    group =
"""
1 *1 Cb 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
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
            L4: doublebond_intra_HDe_secNd
            L4: doublebond_intra_HDe_secDe
        L3: doublebond_intra_NdNd
            L4: doublebond_intra_NdNd_pri
            L4: doublebond_intra_NdNd_secNd
            L4: doublebond_intra_NdNd_secDe
        L3: doublebond_intra_NdDe
            L4: doublebond_intra_NdDe_pri
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
    history = [
    ],
)

forbidden(
    label = "cdd2",
    group =
"""
1 *2 Cdd 0
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
    history = [
    ],
)

