#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad_birad_trirad_quadrad", "XH_Rrad_birad"], products=["Y_H", "X_R"], ownReverse=False)

reverse = "Molecular_Addition"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*2', 'S', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_1centerquadrad, Y_1centertrirad, Y_2centerbirad, Y_1centerbirad, Y_rad, H_rad}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "XH_Rrad_birad",
    group = "OR{XH_Rrad, XH_Rbirad}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "Y_1centerquadrad",
    group = "OR{C_(V), C_(T), C_(S)}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "C_(V)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U4
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "C_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U4
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "C_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U4
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "Y_1centertrirad",
    group = "OR{N_(Q), N_(D), CH_(Q), CH_(D)}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "N_(Q)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N U3
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "N_(D)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N U3
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "CH_(Q)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U3 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "CH_(D)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U3 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "Y_2centerbirad",
    group = "OR{O2b, C2b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "O2b",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2    O U1 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "C2b",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,T}
2    C U1 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Y_1centerbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R!H U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "O_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "O_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "CO_birad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U2 {2,D}
2    Od U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "NH_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U2 {2,S}
2    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "NH_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N U2 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CH2_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U2 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "CH2_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U2 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "H_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Y_rad",
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
    index = 215,
    label = "N3_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {N3s,N3d} U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "N3s_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "NH2_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2    H   U0 {1,S}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "N3s_rad_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2    R!H U0 {1,S}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "N3s_rad/H/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s         U1 {2,S} {3,S}
2    {Cs,N3s,Os} U0 {1,S}
3    H           U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "N3s_rad/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2    Cs  U0 {1,S}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "N3s_rad/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2    Os  U0 {1,S}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "N3s_rad/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2    N3s U0 {1,S}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "N3s_rad/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s                      U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} U0 {1,S}
3    H                        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "N3s_rad_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2    R!H U0 {1,S}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "N3s_rad/NonDe2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s         U1 {2,S} {3,S}
2    {Cs,N3s,Os} U0 {1,S}
3    {Cs,N3s,Os} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "N3s_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s                      U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} U0 {1,S}
3    {Cs,N3s,Os}              U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "N3s_rad/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s                      U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,CS,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "N3d_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "N3d_rad/C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U1 {2,D}
2    C   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "N3d_rad/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U1 {2,D}
2    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "N3d_rad/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U1 {2,D}
2    N   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "N5_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {N5d,N5dd,N5t} U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "N5d_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N5d U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "Ct_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U1 {2,T}
2    R!H U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Ct_rad/Ct",
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

entry(
    index = 209,
    label = "Ct_rad/Nt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct        U1 {2,T}
2    {N3t,N5t} U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "O_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "O_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "O_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O   U1 {2,S}
2    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "O_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O  U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "O_rad/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "O_rad/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O   U1 {2,S}
2    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "O_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O             U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "S_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U1 {2,S}
2    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "S_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U1 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "S_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S   U1 {2,S}
2    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "S_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S  U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "S_rad/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U1 {2,S}
2    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "S_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S             U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Cd_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Cd_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Cd_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2    C   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Cd_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "Cd_rad/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2    C   U0 {1,D}
3    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Cd_rad/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cd_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,D} {3,S}
2    C             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Cb_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U1 {2,B} {3,B}
2    {Cb,Cbf} U0 {1,B}
3    {Cb,Cbf} U0 {1,B}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CO_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    O U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CO_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,D} {3,S}
2    O U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "CO_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,D} {3,S}
2    O   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CO_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U1 {2,D} {3,S}
2    O        U0 {1,D}
3    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "CO_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,D} {3,S}
2    O             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Cs_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    R U0 {1,S}
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
    index = 36,
    label = "C_methyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    H   U0 {1,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C_rad/H2/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C_rad/H2/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C_rad/H2/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C_rad/H2/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C_rad/H2/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    H  U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C_rad/H2/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "C_rad/H2/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    H   U0 {1,S}
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
    index = 45,
    label = "C_rad/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
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
    index = 46,
    label = "C_rad/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U1 {2,S} {3,S} {4,S}
2    H        U0 {1,S}
3    O        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C_rad/H/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
4    O  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C_rad/H/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    O U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "C_rad/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U1 {2,S} {3,S} {4,S}
2    H        U0 {1,S}
3    N        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C_rad/H/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U1 {2,S} {3,S} {4,S}
2    H      U0 {1,S}
3    S      U0 {1,S}
4    {Cs,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C_rad/H/CsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    S  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C_rad/H/S2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    S U0 {1,S}
4    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C_rad/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O,S,N}    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C_rad/H/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C_rad/H/OneDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "C_rad/H/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    N             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C_rad/H/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C_ter_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U1 {2,S} {3,S} {4,S}
2    R!H U0 {1,S}
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
    index = 57,
    label = "C_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U1 {2,S} {3,S} {4,S}
2    {Cs,O,S} U0 {1,S}
3    {Cs,O,S} U0 {1,S}
4    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C_rad/Cs3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U1 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
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
    index = 59,
    label = "C_rad/NDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U1 {2,S} {3,S} {4,S}
2    O        U0 {1,S}
3    {Cs,O,S} U0 {1,S}
4    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cs,O,S}      U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C_rad/Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    Cs            U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C_rad/ODMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    O             U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C_rad/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C_rad/TDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C_rad/ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "XH_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,{S,D}} {3,S}
2 *3 R!H U1 {1,{S,D}}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "XH_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,S} {3,S}
2 *3 R!H U1 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "Cdpri_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd               U0 {2,S} {3,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Cdpri_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,S} {3,S}
2 *3 Cs U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Cdpri_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,S} {3,S}
2 *3 Cd U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "Cdpri_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,S} {3,S}
2 *3 CO U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "Cdpri_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,S} {3,S}
2 *3 O  U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "Cdpri_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cd U0 {2,S} {3,S}
2 *3 N  U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "COpri_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO               U0 {2,S} {3,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "COpri_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,S} {3,S}
2 *3 Cs U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "COpri_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,S} {3,S}
2 *3 Cd U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "COpri_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,S} {3,S}
2 *3 CO U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "COpri_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,S} {3,S}
2 *3 O  U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "COpri_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 CO U0 {2,S} {3,S}
2 *3 N  U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "O_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O                U0 {2,S} {3,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "O_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O  U0 {2,S} {3,S}
2 *3 Cs U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "O_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O  U0 {2,S} {3,S}
2 *3 Cd U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "O_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O  U0 {2,S} {3,S}
2 *3 CO U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "O_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O U0 {2,S} {3,S}
2 *3 O U1 {1,S}
3 *4 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "O_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O U0 {2,S} {3,S}
2 *3 N U1 {1,S}
3 *4 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "S_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 S         U0 {2,S} {3,S}
2 *3 {Cs,Cd,S} U1 {1,S}
3 *4 H         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "S_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 S  U0 {2,S} {3,S}
2 *3 Cs U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "S_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 S  U0 {2,S} {3,S}
2 *3 Cd U1 {1,S}
3 *4 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "S_Srad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 S U0 {2,S} {3,S}
2 *3 S U1 {1,S}
3 *4 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "NH_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N   U0 {2,S} {3,S}
2 *3 R!H U1 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "N3H_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S}
2 *3 R!H U1 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "N3s/H2_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 R!H U1 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "N3s/H2_s_Crad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 C   U1 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "N3s/H2_s_Cssrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 Cs  U1 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "N3s/H2_s_Cdsrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 Cd  U1 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "N3s/H2_s_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 O   U1 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "N3s/H2_s_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 N   U1 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "N3s/H/NonDe_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s         U0 {2,S} {3,S} {4,S}
2 *3 R!H         U1 {1,S}
3 *4 H           U0 {1,S}
4    {Cs,N3s,Os} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "N3s/H/Deloc_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s           U0 {2,S} {3,S} {4,S}
2 *3 R!H           U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "N5H_s_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 {N5s,N5d} U0 {2,S} {3,S}
2 *3 R!H       U1 {1,S}
3 *4 H         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Cmethyl_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    H                U0 {1,S}
5    H                U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "Cmethyl_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs U1 {1,S}
3 *4 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "Cmethyl_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd U1 {1,S}
3 *4 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "Cmethyl_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO U1 {1,S}
3 *4 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Cmethyl_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C U0 {2,S} {3,S} {4,S} {5,S}
2 *3 O U1 {1,S}
3 *4 H U0 {1,S}
4    H U0 {1,S}
5    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "Cmethyl_Srad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C U0 {2,S} {3,S} {4,S} {5,S}
2 *3 S U1 {1,S}
3 *4 H U0 {1,S}
4    H U0 {1,S}
5    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "Cmethyl_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C U0 {2,S} {3,S} {4,S} {5,S}
2 *3 N U1 {1,S}
3 *4 H U0 {1,S}
4    H U0 {1,S}
5    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Cpri_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    H                U0 {1,S}
5    R!H              U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C/H2/Nd_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    H                U0 {1,S}
5    {Cs,O,S}         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C/H2/Nd_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs       U1 {1,S}
3 *4 H        U0 {1,S}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C/H2/Nd_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd       U1 {1,S}
3 *4 H        U0 {1,S}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C/H2/Nd_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO       U1 {1,S}
3 *4 H        U0 {1,S}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C/H2/Nd_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 O        U1 {1,S}
3 *4 H        U0 {1,S}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "C/H2/Nd_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 N3s      U1 {1,S}
3 *4 H        U0 {1,S}
4    H        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C/H2/De_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    H                U0 {1,S}
5    {Cd,Ct,Cb,CO}    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C/H2/De_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs            U1 {1,S}
3 *4 H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C/H2/De_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd            U1 {1,S}
3 *4 H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C/H2/De_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO            U1 {1,S}
3 *4 H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C/H2/De_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 O             U1 {1,S}
3 *4 H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "C/H2/De_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 N             U1 {1,S}
3 *4 H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "Csec_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    R!H              U0 {1,S}
5    R!H              U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C/H/NdNd_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    {Cs,O,S}         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C/H/NdNd_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs       U1 {1,S}
3 *4 H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C/H/NdNd_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd       U1 {1,S}
3 *4 H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C/H/NdNd_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO       U1 {1,S}
3 *4 H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C/H/NdNd_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 O        U1 {1,S}
3 *4 H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "C/H/NdNd_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *3 N        U1 {1,S}
3 *4 H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C/H/NdDe_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    {Cs,O,S}         U0 {1,S}
5    {Cd,Ct,Cb,CO}    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C/H/NdDe_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs            U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C/H/NdDe_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd            U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C/H/NdDe_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO            U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C/H/NdDe_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 O             U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "C/H/NdDe_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 N             U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C/H/DeDe_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C                U0 {2,S} {3,S} {4,S} {5,S}
2 *3 {Cs,Cd,CO,O,S,N} U1 {1,S}
3 *4 H                U0 {1,S}
4    {Cd,Ct,Cb,CO}    U0 {1,S}
5    {Cd,Ct,Cb,CO}    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "C/H/DeDe_Csrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs            U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C/H/DeDe_Cdrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd            U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C/H/DeDe_COrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 CO            U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C/H/DeDe_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 O             U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "C/H/DeDe_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *3 N             U1 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "XH_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,D} {3,S}
2 *3 R!H U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "CH_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C   U0 {2,D} {3,S}
2 *3 R!H U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "Cds/H2_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C   U0 {2,D} {3,S} {4,S}
2 *3 R!H U1 {1,D}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "Cds/H2_d_Crad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C U0 {2,D} {3,S} {4,S}
2 *3 C U1 {1,D}
3 *4 H U0 {1,S}
4    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "Cds/H2_d_N3rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C   U0 {2,D} {3,S} {4,S}
2 *3 N3d U1 {1,D}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "Cds/H2_d_N5rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C              U0 {2,D} {3,S} {4,S}
2 *3 {N5d,N5dd,N5t} U1 {1,D}
3 *4 H              U0 {1,S}
4    H              U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "Cds/H2_d_N5drad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C   U0 {2,D} {3,S} {4,S}
2 *3 N5d U1 {1,D}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "Cds/H2_d_N5ddrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C    U0 {2,D} {3,S} {4,S}
2 *3 N5dd U1 {1,D}
3 *4 H    U0 {1,S}
4    H    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "Cds/H2_d_N5ddrad/C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C    U0 {2,D} {3,S} {4,S}
2 *3 N5dd U1 {1,D} {5,D}
3 *4 H    U0 {1,S}
4    H    U0 {1,S}
5    C    U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "Cds/H2_d_N5ddrad/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C    U0 {2,D} {3,S} {4,S}
2 *3 N5dd U1 {1,D} {5,D}
3 *4 H    U0 {1,S}
4    H    U0 {1,S}
5    O    U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "Cds/H2_d_N5ddrad/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C    U0 {2,D} {3,S} {4,S}
2 *3 N5dd U1 {1,D} {5,D}
3 *4 H    U0 {1,S}
4    H    U0 {1,S}
5    N    U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "Cds/H/NonDe_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C           U0 {2,D} {3,S} {4,S}
2 *3 R!H         U1 {1,D}
3 *4 H           U0 {1,S}
4    {Cs,N3s,Os} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "Cds/H/Deloc_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C             U0 {2,D} {3,S} {4,S}
2 *3 R!H           U1 {1,D}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "NH_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N   U0 {2,D} {3,S}
2 *3 R!H U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "N3d/H_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3d U0 {2,D} {3,S}
2 *3 R!H U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "N3d/H_d_Crad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3d U0 {2,D} {3,S}
2 *3 C   U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "N3d/H_d_Nrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3d U0 {2,D} {3,S}
2 *3 N   U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "N5d/H_d_Rrad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N5d U0 {2,D} {3,S}
2 *3 R!H U1 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "XH_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,{S,D}} {3,S}
2 *3 R!H U2 {1,{S,D}}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "XH_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,S} {3,S}
2 *3 R!H U2 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "CH_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 C   U0 {2,S} {3,S}
2 *3 R!H U2 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "NH_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N   U0 {2,S} {3,S}
2 *3 R!H U2 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "N3H_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S}
2 *3 R!H U2 {1,S}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "N3s/H2_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 R!H U2 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "N3s/H2_s_Cbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 C   U2 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "N3s/H2_s_Nbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s U0 {2,S} {3,S} {4,S}
2 *3 N   U2 {1,S}
3 *4 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "N3s/H/NonDe_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s         U0 {2,S} {3,S} {4,S}
2 *3 N           U2 {1,S}
3 *4 H           U0 {1,S}
4    {Cs,N3s,Os} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "N3s/H/Deloc_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 N3s           U0 {2,S} {3,S} {4,S}
2 *3 N             U2 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "N5H_s_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 {N5s,N5d}     U0 {2,S} {3,S} {4,S}
2 *3 N             U2 {1,S}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "XH_d_Rbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 R!H U0 {2,D} {3,S}
2 *3 R!H U2 {1,D}
3 *4 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_(V)
        L3: C_(T)
        L3: C_(S)
    L2: Y_1centertrirad
        L3: N_(Q)
        L3: N_(D)
        L3: CH_(Q)
        L3: CH_(D)
    L2: Y_2centerbirad
        L3: O2b
        L3: C2b
    L2: Y_1centerbirad
        L3: O_(T)
        L3: O_(S)
        L3: CO_birad
        L3: NH_(T)
        L3: NH_(S)
        L3: CH2_(T)
        L3: CH2_(S)
    L2: H_rad
    L2: Y_rad
        L3: N3_rad
            L4: N3s_rad
                L5: NH2_rad
                L5: N3s_rad_pri
                    L6: N3s_rad/H/NonDe
                        L7: N3s_rad/H/NonDeC
                        L7: N3s_rad/H/NonDeO
                        L7: N3s_rad/H/NonDeN
                    L6: N3s_rad/H/OneDe
                L5: N3s_rad_sec
                    L6: N3s_rad/NonDe2
                    L6: N3s_rad/OneDe
                    L6: N3s_rad/TwoDe
            L4: N3d_rad
                L5: N3d_rad/C
                L5: N3d_rad/O
                L5: N3d_rad/N
        L3: N5_rad
            L4: N5d_rad
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/Nt
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                L5: O_rad/NonDeO
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
        L3: Cd_rad
            L4: Cd_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                L5: Cd_rad/NonDeN
                L5: Cd_rad/NonDeO
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                L5: C_rad/H2/Cd
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
                L5: C_rad/H2/N
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeN
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeN
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                    L6: C_rad/NDMustO
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
L1: XH_Rrad_birad
    L2: XH_Rrad
        L3: XH_s_Rrad
            L4: Cdpri_Rrad
                L5: Cdpri_Csrad
                L5: Cdpri_Cdrad
                L5: Cdpri_COrad
                L5: Cdpri_Orad
                L5: Cdpri_Nrad
            L4: COpri_Rrad
                L5: COpri_Csrad
                L5: COpri_Cdrad
                L5: COpri_COrad
                L5: COpri_Orad
                L5: COpri_Nrad
            L4: O_Rrad
                L5: O_Csrad
                L5: O_Cdrad
                L5: O_COrad
                L5: O_Orad
                L5: O_Nrad
            L4: S_Rrad
                L5: S_Csrad
                L5: S_Cdrad
                L5: S_Srad
            L4: NH_s_Rrad
                L5: N3H_s_Rrad
                    L6: N3s/H2_s_Rrad
                        L7: N3s/H2_s_Crad
                            L8: N3s/H2_s_Cssrad
                            L8: N3s/H2_s_Cdsrad
                        L7: N3s/H2_s_Orad
                        L7: N3s/H2_s_Nrad
                    L6: N3s/H/NonDe_s_Rrad
                    L6: N3s/H/Deloc_s_Rrad
                L5: N5H_s_Rrad
            L4: Cmethyl_Rrad
                L5: Cmethyl_Csrad
                L5: Cmethyl_Cdrad
                L5: Cmethyl_COrad
                L5: Cmethyl_Orad
                L5: Cmethyl_Srad
                L5: Cmethyl_Nrad
            L4: Cpri_Rrad
                L5: C/H2/Nd_Rrad
                    L6: C/H2/Nd_Csrad
                    L6: C/H2/Nd_Cdrad
                    L6: C/H2/Nd_COrad
                    L6: C/H2/Nd_Orad
                    L6: C/H2/Nd_Nrad
                L5: C/H2/De_Rrad
                    L6: C/H2/De_Csrad
                    L6: C/H2/De_Cdrad
                    L6: C/H2/De_COrad
                    L6: C/H2/De_Orad
                    L6: C/H2/De_Nrad
            L4: Csec_Rrad
                L5: C/H/NdNd_Rrad
                    L6: C/H/NdNd_Csrad
                    L6: C/H/NdNd_Cdrad
                    L6: C/H/NdNd_COrad
                    L6: C/H/NdNd_Orad
                    L6: C/H/NdNd_Nrad
                L5: C/H/NdDe_Rrad
                    L6: C/H/NdDe_Csrad
                    L6: C/H/NdDe_Cdrad
                    L6: C/H/NdDe_COrad
                    L6: C/H/NdDe_Orad
                    L6: C/H/NdDe_Nrad
                L5: C/H/DeDe_Rrad
                    L6: C/H/DeDe_Csrad
                    L6: C/H/DeDe_Cdrad
                    L6: C/H/DeDe_COrad
                    L6: C/H/DeDe_Orad
                    L6: C/H/DeDe_Nrad
        L3: XH_d_Rrad
            L4: CH_d_Rrad
                L5: Cds/H2_d_Rrad
                    L6: Cds/H2_d_Crad
                    L6: Cds/H2_d_N3rad
                    L6: Cds/H2_d_N5rad
                        L7: Cds/H2_d_N5drad
                        L7: Cds/H2_d_N5ddrad
                            L8: Cds/H2_d_N5ddrad/C
                            L8: Cds/H2_d_N5ddrad/O
                            L8: Cds/H2_d_N5ddrad/N
                L5: Cds/H/NonDe_d_Rrad
                L5: Cds/H/Deloc_d_Rrad
            L4: NH_d_Rrad
                L5: N3d/H_d_Rrad
                    L6: N3d/H_d_Crad
                    L6: N3d/H_d_Nrad
                L5: N5d/H_d_Rrad
    L2: XH_Rbirad
        L3: XH_s_Rbirad
            L4: CH_s_Rbirad
            L4: NH_s_Rbirad
                L5: N3H_s_Rbirad
                    L6: N3s/H2_s_Rbirad
                        L7: N3s/H2_s_Cbirad
                        L7: N3s/H2_s_Nbirad
                    L6: N3s/H/NonDe_s_Rbirad
                    L6: N3s/H/Deloc_s_Rbirad
                L5: N5H_s_Rbirad
        L3: XH_d_Rbirad
"""
)

forbidden(
    label = "O2d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O U0 {2,D}
2 *3 O U0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "O_Orad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 O U0 {2,S} {3,S}
2 *3 O U1 {1,S}
3 *4 H U0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

