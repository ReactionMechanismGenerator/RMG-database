#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["X_H_or_Xrad_H_Xbirad_H_Xtrirad_H", "Y_rad_birad_trirad_quadrad"], products=["X_H_or_Xrad_H_Xbirad_H_Xtrirad_H", "Y_rad_birad_trirad_quadrad"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H",
    group = "OR{X_H, Xrad_H, Xbirad_H, Xtrirad_H}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "X_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U0 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 H U0 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "N3_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {N3s,N3d} U0 {2,S}
2 *2 H         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 413,
    label = "N3d_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,S} {3,D}
2 *2 H   U0 {1,S}
3    R!H U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 465,
    label = "N3d/H/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d      U0 {2,S} {3,D}
2 *2 H        U0 {1,S}
3    {N3d,Od} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 447,
    label = "N3d/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,S} {3,D}
2 *2 H   U0 {1,S}
3    O   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 448,
    label = "N3d/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,S} {3,D}
2 *2 H   U0 {1,S}
3    N3d U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 446,
    label = "N3d/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,S} {3,D}
2 *2 H   U0 {1,S}
3    Cd  U0 {1,D} {4,S} {5,S}
4    R   U0 {3,S}
5    R   U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 466,
    label = "N3d/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                U0 {2,S} {3,D}
2 *2 H                  U0 {1,S}
3    {Cd,Ct,Cb,N5d,N5t} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 467,
    label = "N3d/H/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d        U0 {2,S} {3,D}
2 *2 H          U0 {1,S}
3    {Cd,Ct,Cb} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 468,
    label = "N3d/H/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d       U0 {2,S} {3,D}
2 *2 H         U0 {1,S}
3    {N5d,N5t} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 402,
    label = "N3s_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
3    R   U0 {1,S}
4    R   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 410,
    label = "NH3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "N3s_pri_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
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
    index = 450,
    label = "N3s/H2/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s         U0 {2,S} {3,S} {4,S}
2 *2 H           U0 {1,S}
3    H           U0 {1,S}
4    {N3s,Cs,Os} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 451,
    label = "N3s/H2/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
4    Cs  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 452,
    label = "N3s/H2/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
4    Os  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 453,
    label = "N3s/H2/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
4    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 472,
    label = "N3s/H2/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s       U0 {2,S} {3,S} {4,S}
2 *2 H         U0 {1,S}
3    H         U0 {1,S}
4    {N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 473,
    label = "N3s/H2/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s       U0 {2,S} {3,S} {4,S}
2 *2 H         U0 {1,S}
3    H         U0 {1,S}
4    {N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 412,
    label = "N3s_sec_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U0 {2,S} {3,S} {4,S}
2 *2 H   U0 {1,S}
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
    index = 414,
    label = "N5_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 {N5s,N5d,N5dd,N5t,N5b} U0 {2,S}
2 *2 H                      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 415,
    label = "N5d_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N5d U0 {2,S}
2 *2 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 456,
    label = "N5d/H/NonDeOO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N5d U0 {2,S} {3,S} {4,D}
2 *2 H   U0 {1,S}
3    Os  U0 {1,S}
4    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Ct_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct    U0 {2,T} {3,S}
2    {C,N} U0 {1,T}
3 *2 H     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 457,
    label = "Ct/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,S} {3,T}
2 *2 H  U0 {1,S}
3    Ct U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 458,
    label = "Ct/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U0 {2,S} {3,T}
2 *2 H   U0 {1,S}
3    N3t U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "O_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "O_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "O_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O   U0 {2,S} {3,S}
2 *2 H   U0 {1,S}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "O/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O  U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "O/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "H2O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {3,S}
2    O U0 {1,S} {4,S}
3 *2 H U0 {1,S}
4    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "ROOH_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O  U0 {2,S} {7,S}
2    O  U0 {1,S} {3,S}
3    C  U0 {2,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7 *2 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "ROOH_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O  U0 {2,S} {7,S}
2    O  U0 {1,S} {3,S}
3    C  U0 {2,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
7 *2 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "ROOH_ter",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O  U0 {2,S} {7,S}
2    O  U0 {1,S} {3,S}
3    C  U0 {2,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
7 *2 H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 471,
    label = "O/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O   U0 {2,S} {3,S}
2 *2 H   U0 {1,S}
3    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "O/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O                        U0 {2,S} {3,S}
2 *2 H                        U0 {1,S}
3    {Cd,Ct,Cb,CO,CS,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 454,
    label = "O/H/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O                U0 {2,S} {3,S}
2 *2 H                U0 {1,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 455,
    label = "O/H/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O         U0 {2,S} {3,S}
2 *2 H         U0 {1,S}
3    {N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Orad_O_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    O U1 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "S_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "S_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "S_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S   U0 {2,S} {3,S}
2 *2 H   U0 {1,S}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "S/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S  U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "S/H/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "S/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S                U0 {2,S} {3,S}
2 *2 H                U0 {1,S}
3    {Cd,Ct,Cb,CO,CS} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "S/H/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S  U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "S/H/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S  U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "S/H/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S  U0 {2,S} {3,S}
2 *2 H  U0 {1,S}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "S/H/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    C U0 {1,S} {4,D}
4    C U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "S/H/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U0 {2,S} {3,S}
2 *2 H U0 {1,S}
3    C U0 {1,S} {4,D}
4    S U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cd_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Cd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C     U0 {2,D} {3,S} {4,S}
2    {C,N} U0 {1,D}
3 *2 H     U0 {1,S}
4    H     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 459,
    label = "Cd/H2/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 460,
    label = "Cd/H2/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,D} {3,S} {4,S}
2    N3d U0 {1,D}
3 *2 H   U0 {1,S}
4    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cd_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,D} {3,S} {4,S}
2    C   U0 {1,D}
3 *2 H   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Cd/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    C  U0 {1,D}
3 *2 H  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Cd/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Cd/H/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 404,
    label = "Cd/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "Cd/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C                U0 {2,D} {3,S} {4,S}
2    C                U0 {1,D}
3 *2 H                U0 {1,S}
4    {Cd,Ct,Cb,CO,CS} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Cd/H/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    C  U0 {1,D}
3 *2 H  U0 {1,S}
4    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "Cd/H/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    C  U0 {1,D}
3 *2 H  U0 {1,S}
4    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "Cd/H/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    C  U0 {1,D}
3 *2 H  U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 405,
    label = "Cd/H/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cd/H/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    C U0 {1,S} {5,D}
5    C U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "Cd/H/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    C U0 {1,D}
3 *2 H U0 {1,S}
4    C U0 {1,S} {5,D}
5    S U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "Cb_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cb       U0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} U0 {1,B}
3    {Cb,Cbf} U0 {1,B}
4 *2 H        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "CO_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    O U0 {1,D}
3 *2 H U0 {1,S}
4    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "CO_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    O U0 {1,D}
3 *2 H U0 {1,S}
4    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "CO_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,D} {3,S} {4,S}
2    O   U0 {1,D}
3 *2 H   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "CO/H/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2    O        U0 {1,D}
3 *2 H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "CO/H/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    O  U0 {1,D}
3 *2 H  U0 {1,S}
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
    label = "CO/H/Cs\Cs|Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    O  U0 {1,D}
3 *2 H  U0 {1,S}
4    Cs U0 {1,S} {5,S}
5    Cs U0 {4,S} {6,S}
6    Cs U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CO/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,D} {3,S} {4,S}
2    O             U0 {1,D}
3 *2 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "CS_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    S U0 {1,D}
3 *2 H U0 {1,S}
4    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "CS_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    S U0 {1,D}
3 *2 H U0 {1,S}
4    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "CS_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,D} {3,S} {4,S}
2    S   U0 {1,D}
3 *2 H   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CS/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    S  U0 {1,D}
3 *2 H  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "CS/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    S U0 {1,D}
3 *2 H U0 {1,S}
4    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CS/H/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    S U0 {1,D}
3 *2 H U0 {1,S}
4    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "CS/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,D} {3,S} {4,S}
2    S             U0 {1,D}
3 *2 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CS/H/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    S  U0 {1,D}
3 *2 H  U0 {1,S}
4    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CS/H/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    S  U0 {1,D}
3 *2 H  U0 {1,S}
4    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CS/H/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2    S  U0 {1,D}
3 *2 H  U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CS/H/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    S U0 {1,D}
3 *2 H U0 {1,S}
4    C U0 {1,S} {5,D}
5    C U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "CS/H/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D} {3,S} {4,S}
2    S U0 {1,D}
3 *2 H U0 {1,S}
4    C U0 {1,S} {5,D}
5    S U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cs_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    R U0 {1,S}
4    R U0 {1,S}
5    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C_methane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
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
    index = 62,
    label = "C_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C/H3/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C/H3/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2    C U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H U0 {1,S}
4    H U0 {1,S}
5    H U0 {1,S}
6    H U0 {2,S}
7    H U0 {2,S}
8    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C/H3/CsNonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,S} {3,S} {4,S} {5,S}
2    C        U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        U0 {1,S}
4    H        U0 {1,S}
5    H        U0 {1,S}
6    {Cs,O,S} U0 {2,S}
7    H        U0 {2,S}
8    H        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C/H3/Cs\H2\Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2    C  U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    Cs U0 {2,S}
7    H  U0 {2,S}
8    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C/H3/Cs\H2\Cs|O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2    C  U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    Cs U0 {2,S} {9,S}
7    H  U0 {2,S}
8    H  U0 {2,S}
9    O  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C/H3/Cs\H2\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2    C U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H U0 {1,S}
4    H U0 {1,S}
5    H U0 {1,S}
6    O U0 {2,S}
7    H U0 {2,S}
8    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C/H3/CsNonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,S} {3,S} {4,S} {5,S}
2    C        U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        U0 {1,S}
4    H        U0 {1,S}
5    H        U0 {1,S}
6    {Cs,O,S} U0 {2,S}
7    {Cs,O,S} U0 {2,S}
8    H        U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C/H3/Cs\H\Cs\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2    C  U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    Cs U0 {2,S}
7    O  U0 {2,S}
8    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C/H3/Cs\H\Cs\Cs|O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2    C  U0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    Cs U0 {2,S} {9,S}
7    Cs U0 {2,S}
8    H  U0 {2,S}
9    O  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C/H3/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
5    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C/H3/S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
5    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C/H3/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    H             U0 {1,S}
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
    index = 75,
    label = "C/H3/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C/H3/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C/H3/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C/H3/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
5    C U0 {1,S} {6,D}
6    C U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C/H3/Cd\H_Cd\H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
5    C U0 {1,S} {6,D} {7,S}
6    C U0 {5,D} {8,S} {9,S}
7    H U0 {5,S}
8    H U0 {6,S}
9    H U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C/H3/Cd\H_Cd\H\Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {1,S} {6,D} {7,S}
6    C  U0 {5,D} {8,S} {9,S}
7    H  U0 {5,S}
8    Cs U0 {6,S}
9    H  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C/H3/Cd\Cs_Cd\H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {1,S} {6,D} {7,S}
6    C  U0 {5,D} {8,S} {9,S}
7    Cs U0 {5,S}
8    H  U0 {6,S}
9    H  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C/H3/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
5    C U0 {1,S} {6,D}
6    S U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 461,
    label = "Cs/H3/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,S} {3,S} {4,S} {5,S}
2    N3s U0 {1,S}
3 *2 H   U0 {1,S}
4    H   U0 {1,S}
5    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 471,
    label = "Cs/H3/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C         U0 {2,S} {3,S} {4,S} {5,S}
2    {N3d,N5d} U0 {1,S}
3 *2 H         U0 {1,S}
4    H         U0 {1,S}
5    H         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
5    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C/H2/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C/H2/Cs/Cs\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S} {6,S}
6    O  U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C/H2/Cs/Cs\Cs|O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S} {6,S}
6    Cs U0 {5,S} {7,S}
7    O  U0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C/H2/NonDeC_5ring",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S} {6,S}
5    Cs U0 {1,S} {7,S}
6    Cs U0 {4,S} {7,S}
7    Cs U0 {5,S} {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C/H2/NonDeC_5ring_fused6_1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S} {6,S} {8,S}
5    Cs U0 {1,S} {7,S}
6    Cs U0 {4,S} {7,S}
7    Cs U0 {5,S} {6,S} {9,S}
8    Cs U0 {4,S} {9,S}
9    Cs U0 {7,S} {8,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C/H2/NonDeC_5ring_fused6_2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S} {6,S} {8,S}
5    Cs U0 {1,S} {7,S} {9,S}
6    Cs U0 {4,S} {7,S}
7    Cs U0 {5,S} {6,S}
8    Cs U0 {4,S} {9,S}
9    Cs U0 {5,S} {8,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C/H2/NonDeC_5ring_alpha6ring",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2  *2 H  U0 {1,S}
3     H  U0 {1,S}
4     Cs U0 {1,S} {6,S} {8,S}
5     Cs U0 {1,S} {7,S}
6     Cs U0 {4,S} {7,S} {11,S}
7     Cs U0 {5,S} {6,S}
8     C  U0 {4,S} {9,S}
9     C  U0 {8,S} {10,S}
10    C  U0 {9,S} {11,S}
11    C  U0 {6,S} {10,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C/H2/NonDeC_5ring_beta6ring",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2  *2 H  U0 {1,S}
3     H  U0 {1,S}
4     Cs U0 {1,S} {6,S}
5     Cs U0 {1,S} {7,S}
6     Cs U0 {4,S} {7,S} {8,S}
7     Cs U0 {5,S} {6,S} {11,S}
8     C  U0 {6,S} {9,S}
9     C  U0 {8,S} {10,S}
10    C  U0 {9,S} {11,S}
11    C  U0 {7,S} {10,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C/H2/Cs\H3/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {4,S} {5,S} {6,S}
2  *1 C U0 {1,S} {3,S} {7,S} {8,S}
3     C U0 {2,S} {9,S} {10,S} {11,S}
4     H U0 {1,S}
5     H U0 {1,S}
6     H U0 {1,S}
7  *2 H U0 {2,S}
8     H U0 {2,S}
9     H U0 {3,S}
10    H U0 {3,S}
11    H U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C/H2/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        U0 {1,S}
3    H        U0 {1,S}
4    O        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C/H2/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    O  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C/H2/Cs\Cs2/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {6,S} {7,S} {8,S}
2     C U0 {1,S} {3,S} {5,S} {9,S}
3  *1 C U0 {2,S} {4,S} {10,S} {11,S}
4     O U0 {3,S} {12,S}
5     C U0 {2,S} {13,S} {14,S} {15,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10 *2 H U0 {3,S}
11    H U0 {3,S}
12    H U0 {4,S}
13    H U0 {5,S}
14    H U0 {5,S}
15    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C/H2/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    O U0 {1,S}
5    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C/H2/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        U0 {1,S}
3    H        U0 {1,S}
4    S        U0 {1,S}
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
    label = "C/H2/CsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    S  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 407,
    label = "C/H2/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C          U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          U0 {1,S}
3    H          U0 {1,S}
4    N          U0 {1,S}
5    {Cs,O,S,N} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C/H2/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    {Cs,O,S}      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C/H2/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C/H2/CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C/H2/CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C/H2/COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    CO U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C/H2/CO\H/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {5,S} {6,S} {7,S}
2  *1 C U0 {1,S} {3,S} {8,S} {9,S}
3     C U0 {2,S} {4,D} {10,S}
4     O U0 {3,D}
5     H U0 {1,S}
6     H U0 {1,S}
7     H U0 {1,S}
8  *2 H U0 {2,S}
9     H U0 {2,S}
10    H U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C/H2/CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Cs U0 {1,S}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {5,S} {6,S} {7,S}
2  *1 C U0 {1,S} {3,S} {8,S} {9,S}
3     C U0 {2,S} {4,D} {10,S}
4     C U0 {3,D} {11,S} {12,S}
5     H U0 {1,S}
6     H U0 {1,S}
7     H U0 {1,S}
8  *2 H U0 {2,S}
9     H U0 {2,S}
10    H U0 {3,S}
11    H U0 {4,S}
12    H U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C/H2/CSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Cs U0 {1,S}
6    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C/H2/OneDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C/H2/OneDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C/H2/CbS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
5    S  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C/H2/CtS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
5    S  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C/H2/CdS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {6,D}
5    S U0 {1,S}
6    C U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C/H2/CSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {6,D}
5    S U0 {1,S}
6    S U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C/H2/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    {Cd,Ct,CO,Cb} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "C/H2/CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
5    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C/H2/CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
5    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C/H2/CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
5    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C/H2/CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
5    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C/H2/CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
5    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C/H2/COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    CO U0 {1,S}
5    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C/H2/CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Ct U0 {1,S}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C/H2/CtCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Ct U0 {1,S}
5    C  U0 {1,S} {6,D}
6    S  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C/H2/CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Cb U0 {1,S}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C/H2/CbCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    Cb U0 {1,S}
5    C  U0 {1,S} {6,D}
6    S  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C/H2/CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    C  U0 {1,S} {6,D}
5    CO U0 {1,S}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C/H2/COCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    CO U0 {1,S}
5    C  U0 {1,S} {6,D}
6    S  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C/H2/CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {6,D}
5    C U0 {1,S} {7,D}
6    C U0 {4,D}
7    C U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C/H2/CdCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {6,D}
5    C U0 {1,S} {7,D}
6    C U0 {4,D}
7    S U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C/H2/CSCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {6,D}
5    C U0 {1,S} {7,D}
6    S U0 {4,D}
7    S U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C/H2/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    C  U0 {1,S}
5    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "C_ter",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C   U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   U0 {1,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
5    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "C/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        U0 {1,S}
3    {Cs,O,S} U0 {1,S}
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
    index = 133,
    label = "C/H/Cs3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C/H/Cs3_5ring",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {6,S}
4    Cs U0 {1,S} {7,S}
5    Cs U0 {1,S}
6    Cs U0 {3,S} {7,S}
7    Cs U0 {4,S} {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C/H/Cs3_5ring_fused6",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {6,S}
4    Cs U0 {1,S} {7,S}
5    Cs U0 {1,S} {8,S}
6    Cs U0 {3,S} {7,S}
7    Cs U0 {4,S} {6,S} {8,S}
8    Cs U0 {5,S} {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C/H/Cs3_5ring_adj5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cs U0 {1,S} {6,S}
4    Cs U0 {1,S} {7,S} {9,S}
5    Cs U0 {1,S} {8,S}
6    Cs U0 {3,S} {7,S}
7    Cs U0 {4,S} {6,S}
8    Cs U0 {5,S} {9,S}
9    Cs U0 {4,S} {8,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C/H/Cs2/Cs\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {6,S} {7,S} {8,S}
2  *1 C U0 {1,S} {3,S} {5,S} {9,S}
3     C U0 {2,S} {4,S} {10,S} {11,S}
4     O U0 {3,S} {12,S}
5     C U0 {2,S} {13,S} {14,S} {15,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9  *2 H U0 {2,S}
10    H U0 {3,S}
11    H U0 {3,S}
12    H U0 {4,S}
13    H U0 {5,S}
14    H U0 {5,S}
15    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 408,
    label = "C/H/Cs2N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    N  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "C/H/NDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      U0 {1,S}
3    O      U0 {1,S}
4    {Cs,O} U0 {1,S}
5    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "C/H/Cs2O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    O  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "C/H/CsO2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    O  U0 {1,S}
4    O  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "C/H/O3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    O U0 {1,S}
4    O U0 {1,S}
5    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "C/H/NDMustS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C      U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      U0 {1,S}
3    S      U0 {1,S}
4    {Cs,S} U0 {1,S}
5    {Cs,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "C/H/Cs2S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    S  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "C/H/CsS2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    S  U0 {1,S}
4    S  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C/H/S3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H U0 {1,S}
3    S U0 {1,S}
4    S U0 {1,S}
5    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C/H/NDMustOS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C        U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        U0 {1,S}
3    O        U0 {1,S}
4    S        U0 {1,S}
5    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C/H/CsOS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    O  U0 {1,S}
4    S  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O,S}      U0 {1,S}
5    {Cs,O,S}      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "C/H/Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "C/H/Cs2Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "C/H/Cs2Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "C/H/Cs2CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "C/H/Cs2Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "C/H/Cs2CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
6    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "C/H/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "C/H/CsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    S             U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "C/H/CbCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
4    S  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "C/H/CtCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
4    S  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "C/H/CdCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    S  U0 {1,S}
5    Cs U0 {1,S}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "C/H/CSCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    S  U0 {1,S}
5    Cs U0 {1,S}
6    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "C/H/OO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
5    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "C/H/OS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
5    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "C/H/SS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    S             U0 {1,S}
5    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "C/H/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cs,O,S}      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "C/H/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "C/H/CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R!H U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "C/H/CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
4    Cb U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "C/H/CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
4    CO U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "C/H/CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
4    Cb U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "C/H/CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
4    CO U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "C/H/COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    CO U0 {1,S}
4    CO U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "C/H/CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    Ct U0 {1,S}
5    Cs U0 {1,S}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "C/H/CtCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Ct U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Cs U0 {1,S}
6    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "C/H/CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    Cb U0 {1,S}
5    Cs U0 {1,S}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "C/H/CbCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    Cb U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Cs U0 {1,S}
6    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "C/H/CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    CO U0 {1,S}
5    Cs U0 {1,S}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "C/H/COCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    CO U0 {1,S}
4    C  U0 {1,S} {6,D}
5    Cs U0 {1,S}
6    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "C/H/CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    C  U0 {1,S} {7,D}
5    Cs U0 {1,S}
6    C  U0 {3,D}
7    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "C/H/CdCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    C  U0 {1,S} {7,D}
5    Cs U0 {1,S}
6    C  U0 {3,D}
7    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "C/H/CSCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S} {6,D}
4    C  U0 {1,S} {7,D}
5    Cs U0 {1,S}
6    S  U0 {3,D}
7    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "C/H/TDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "C/H/TDMustS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "C/H/ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C             U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
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
    index = 184,
    label = "C/H/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C  U0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  U0 {1,S}
3    C  U0 {1,S}
4    C  U0 {1,S}
5    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "Xrad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U1 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 469,
    label = "C_rad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U1 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 442,
    label = "CH3_rad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cs U1 {2,S} {3,S} {4,S}
2 *2 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 470,
    label = "Cs/H2/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C         U1 {2,S} {3,S} {4,S}
2 *2 H         U0 {1,S}
3    H         U0 {1,S}
4    {N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 443,
    label = "OH_rad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 O U1 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "Srad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 S U1 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 416,
    label = "N3s_rad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S}
2 *2 H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "NH2_rad_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2 *2 H   U0 {1,S}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "N3s_rad_H_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s     U1 {2,S} {3,S}
2 *2 H       U0 {1,S}
3    {C,N,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 449,
    label = "N3s_rad_H/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3s U1 {2,S} {3,S}
2 *2 H   U0 {1,S}
3    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 444,
    label = "Xbirad_H",
    group = "OR{CH2_(T)_H, CH2_(S)_H, NH_(T)_H, NH_(S)_H}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 478,
    label = "NH_(T)_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N U2 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 479,
    label = "NH_(S)_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N U2 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 476,
    label = "CH2_(T)_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U2 {2,S} {3,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 477,
    label = "CH2_(S)_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U2 {2,S} {3,S}
2 *2 H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 474,
    label = "Xtrirad_H",
    group = "OR{C_(Q)_H, C_(D)_H}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 480,
    label = "C_(Q)_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U3 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 481,
    label = "C_(D)_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U3 {2,S}
2 *2 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 475,
    label = "Y_1centerquadrad",
    group = "OR{C_(V), C_(T), C_(S)}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "C_(V)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U4
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 483,
    label = "C_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U4
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 484,
    label = "C_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U4
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "Y_1centertrirad",
    group = "OR{N_(Q), N_(D), CH_(Q), CH_(D)}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 485,
    label = "N_(Q)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N U3
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 486,
    label = "N_(D)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N U3
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "CH_(Q)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U3 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "CH_(D)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U3 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "Y_1centerbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Cs,Cd,CO,CS,O,S,N} U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "O_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 488,
    label = "O_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 422,
    label = "NH_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U2 {2,s}
2    H   U0 {1,s}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 490,
    label = "NH_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N U2 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "CH2_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U2 {2,S} {3,S}
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
    index = 489,
    label = "CH2_(S)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U2 {2,S} {3,S}
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
    index = 191,
    label = "Y_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 R U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "H_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 434,
    label = "N3_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {N3s,N3d} U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 435,
    label = "N3s_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 436,
    label = "NH2_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U1 {2,S} {3,S}
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
    index = 437,
    label = "N3s_rad_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U1 {2,S} {3,S}
2    H   U0 {1,S}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 438,
    label = "N3s_rad_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U1 {2,S} {3,S}
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
    index = 439,
    label = "N3d_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    R!H U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 462,
    label = "N3d_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    Cd  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 463,
    label = "N3d_rad/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    Cd  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 464,
    label = "N3d_rad/OneDeCdd_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    Cd  U0 {1,D} {3,D}
3    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 440,
    label = "N5_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {N5s,N5d,N5t} U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 441,
    label = "N5d_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N5d U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "Y_2centeradjbirad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Ct,Os,Ss} U1 {2,{S,T}}
2    {Ct,Os,Ss} U1 {1,{S,T}}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "O2b",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    O U1 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "C2b",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,T}
2    C U1 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "Ct_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C     U1 {2,T}
2    {C,N} U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 423,
    label = "Ct_rad/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ct U1 {2,T}
2    Ct U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 424,
    label = "Ct_rad/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ct        U1 {2,T}
2    {N3t,N5t} U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "O_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "O_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "O_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O   U1 {2,S}
2    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "O_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "O_rad/Cs\H2\Cs|H|Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {6,S} {7,S} {8,S}
2     C U0 {1,S} {3,S} {5,S} {9,S}
3     C U0 {2,S} {4,S} {10,S} {11,S}
4  *3 O U1 {3,S}
5     C U0 {2,S} {12,S} {13,S} {14,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10    H U0 {3,S}
11    H U0 {3,S}
12    H U0 {5,S}
13    H U0 {5,S}
14    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "O_rad/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "OOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    O U0 {1,S} {3,S}
3    C U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 425,
    label = "O_rad/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O   U1 {2,S}
2    N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "O_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O                        U1 {2,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 426,
    label = "O_rad/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O         U1 {2,S}
2    {N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "O_rad/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    C U0 {1,S} {3,D}
3    C U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "O_rad/Cd\H_Cd\H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O U1 {2,S}
2    C U0 {1,S} {3,D} {4,S}
3    C U0 {2,D} {5,S} {6,S}
4    H U0 {2,S}
5    H U0 {3,S}
6    H U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "O_rad/Cd\H_Cd\H\Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    C  U0 {1,S} {3,D} {4,S}
3    C  U0 {2,D} {5,S} {6,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "O_rad/Cd\H_Cd\Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    C  U0 {1,S} {3,D} {4,S}
3    C  U0 {2,D} {5,S} {6,S}
4    H  U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "O_rad/Cd\Cs_Cd\H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    C  U0 {1,S} {3,D} {4,S}
3    C  U0 {2,D} {5,S} {6,S}
4    Cs U0 {2,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "O_rad/Cd\Cs_Cd\H\Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    C  U0 {1,S} {3,D} {4,S}
3    C  U0 {2,D} {5,S} {6,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "O_rad/Cd\Cs_Cd\Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O  U1 {2,S}
2    C  U0 {1,S} {3,D} {4,S}
3    C  U0 {2,D} {5,S} {6,S}
4    Cs U0 {2,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 403,
    label = "InChI=1S/NO3/c2-1(3)4",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Os  U1 {2,S}
2    N5d U0 {1,S} {3,D} {4,S}
3    Od  U0 {2,D}
4    Os  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "S_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S U1 {2,S}
2    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "S_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S U1 {2,S}
2    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "S_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S   U1 {2,S}
2    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "S_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S  U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "S_rad/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S U1 {2,S}
2    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "S_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S             U1 {2,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "S_rad/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S  U1 {2,S}
2    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "S_rad/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S  U1 {2,S}
2    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "S_rad/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S  U1 {2,S}
2    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "S_rad/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S U1 {2,S}
2    C U0 {1,S} {3,D}
3    C U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "S_rad/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S U1 {2,S}
2    C U0 {1,S} {3,D}
3    S U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "Cd_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 224,
    label = "Cd_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 225,
    label = "Cd_Cd\H2_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D} {4,S} {5,S}
3    H U0 {1,S}
4    H U0 {2,S}
5    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "Cd_Cd\H\Cs_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    H  U0 {1,S}
4    Cs U0 {2,S}
5    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C U0 {2,S}
2    C U0 {1,S} {3,S} {5,S} {6,S}
3    C U0 {2,S} {4,D} {7,S}
4 *3 C U1 {3,D} {8,S}
5    H U0 {2,S}
6    H U0 {2,S}
7    H U0 {3,S}
8    H U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "Cd_Cd\Cs2_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    H  U0 {1,S}
4    Cs U0 {2,S}
5    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "Cd_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,D} {3,S}
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
    index = 230,
    label = "Cd_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
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
    index = 231,
    label = "Cd_Cd\H2_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C  U0 {2,D} {4,S} {5,S}
2 *3 C  U1 {1,D} {3,S}
3    Cs U0 {2,S}
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
    index = 232,
    label = "Cd_Cd\H\Cs_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C  U0 {2,S} {5,S} {6,S} {7,S}
2 *3 C  U1 {1,S} {3,D}
3    C  U0 {2,D} {4,S} {8,S}
4    Cs U0 {3,S}
5    H  U0 {1,S}
6    H  U0 {1,S}
7    H  U0 {1,S}
8    H  U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "Cd_rad/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 234,
    label = "Cd_rad/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 427,
    label = "Cd_rad/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "Cd_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,D} {3,S}
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
    index = 236,
    label = "Cd_rad/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
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
    label = "Cd_rad/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "Cd_rad/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "Cd_rad/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    C U0 {1,S} {4,D}
4    C U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "Cd_rad/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D}
3    C U0 {1,S} {4,D}
4    S U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "Cb_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cb       U1 {2,B} {3,B}
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
    index = 242,
    label = "CO_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 243,
    label = "CO_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
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
    index = 244,
    label = "CO_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,D} {3,S}
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
    index = 245,
    label = "CO_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C        U1 {2,D} {3,S}
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
    index = 246,
    label = "CO_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,D} {3,S}
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
    index = 247,
    label = "CS_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3    R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "CS_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "CS_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,D} {3,S}
2    S   U0 {1,D}
3    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "CS_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C        U1 {2,D} {3,S}
2    S        U0 {1,D}
3    {Cs,O,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "CS_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    S  U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "CS_rad/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3    O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "CS_rad/S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "CS_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,D} {3,S}
2    S             U0 {1,D}
3    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "CS_rad/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    S  U0 {1,D}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "CS_rad/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    S  U0 {1,D}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "CS_rad/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    S  U0 {1,D}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "CS_rad/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3    C U0 {1,S} {4,D}
4    C U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "CS_rad/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    S U0 {1,D}
3    C U0 {1,S} {4,D}
4    S U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "Cs_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 261,
    label = "C_methyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 262,
    label = "C_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,S} {3,S} {4,S}
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
    index = 263,
    label = "C_rad/H2/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 264,
    label = "C_rad/H2/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    C U0 {1,S} {5,S} {6,S} {7,S}
3    H U0 {1,S}
4    H U0 {1,S}
5    H U0 {2,S}
6    H U0 {2,S}
7    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "C_rad/H2/Cs\Cs2\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {6,S} {7,S}
2    C U0 {1,S} {3,S} {4,S} {5,S}
3    C U0 {2,S}
4    O U0 {2,S}
5    C U0 {2,S}
6    H U0 {1,S}
7    H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "C_rad/H2/Cs\H\Cs\Cs|O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {6,S} {7,S}
2    C U0 {1,S} {3,S} {5,S} {8,S}
3    C U0 {2,S} {4,S}
4    O U0 {3,S}
5    C U0 {2,S}
6    H U0 {1,S}
7    H U0 {1,S}
8    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "C_rad/H2/Cs\H\Cs|Cs\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {6,S} {7,S}
2    C U0 {1,S} {3,S} {4,S} {8,S}
3    C U0 {2,S} {5,S}
4    O U0 {2,S}
5    C U0 {3,S}
6    H U0 {1,S}
7    H U0 {1,S}
8    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {6,S} {7,S}
2    C U0 {1,S} {3,S} {8,S} {9,S}
3    C U0 {2,S} {4,S} {5,S}
4    C U0 {3,S}
5    O U0 {3,S}
6    H U0 {1,S}
7    H U0 {1,S}
8    H U0 {2,S}
9    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {6,S} {7,S}
2    C U0 {1,S} {3,S} {8,S} {9,S}
3    C U0 {2,S} {4,S}
4    C U0 {3,S} {5,S}
5    O U0 {4,S}
6    H U0 {1,S}
7    H U0 {1,S}
8    H U0 {2,S}
9    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "C_rad/H2/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 271,
    label = "C_rad/H2/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 272,
    label = "C_rad/H2/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 273,
    label = "C_rad/H2/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 274,
    label = "C_rad/H2/S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    S U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 428,
    label = "C_rad/H2/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 275,
    label = "C_rad/H2/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {5,D}
5    C U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "C_rad/H2/Cd\H_Cd\H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {4,S} {5,S}
2    C U0 {1,S} {3,D} {6,S}
3    C U0 {2,D}
4    H U0 {1,S}
5    H U0 {1,S}
6    H U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "C_rad/H2/Cd\Cs_Cd\H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,D} {5,S} {6,S}
2     C U0 {1,D} {3,S} {4,S}
3  *3 C U1 {2,S} {7,S} {8,S}
4     C U0 {2,S} {9,S} {10,S} {11,S}
5     H U0 {1,S}
6     H U0 {1,S}
7     H U0 {3,S}
8     H U0 {3,S}
9     H U0 {4,S}
10    H U0 {4,S}
11    H U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "C_rad/H2/CS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    C U0 {1,S} {5,D}
5    S U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "C_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,S} {3,S} {4,S}
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
    index = 280,
    label = "C_rad/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 281,
    label = "C_rad/H/NonDeC_5ring_fused6_1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S} {5,S} {7,S}
4    Cs U0 {1,S} {6,S}
5    Cs U0 {3,S} {6,S}
6    Cs U0 {4,S} {5,S} {8,S}
7    Cs U0 {3,S} {8,S}
8    Cs U0 {6,S} {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "C_rad/H/NonDeC_5ring_fused6_2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S} {5,S} {7,S}
4    Cs U0 {1,S} {6,S} {8,S}
5    Cs U0 {3,S} {6,S}
6    Cs U0 {4,S} {5,S}
7    Cs U0 {3,S} {8,S}
8    Cs U0 {4,S} {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "C_rad/H/Cs\H3/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {4,S} {5,S} {6,S}
2  *3 C U1 {1,S} {3,S} {7,S}
3     C U0 {2,S} {8,S} {9,S} {10,S}
4     H U0 {1,S}
5     H U0 {1,S}
6     H U0 {1,S}
7     H U0 {2,S}
8     H U0 {3,S}
9     H U0 {3,S}
10    H U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "C_rad/H/NonDeC_5ring_alpha6ring",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *3 C  U1 {2,S} {3,S} {4,S}
2     H  U0 {1,S}
3     Cs U0 {1,S} {5,S} {7,S}
4     Cs U0 {1,S} {6,S}
5     Cs U0 {3,S} {6,S} {10,S}
6     Cs U0 {4,S} {5,S}
7     C  U0 {3,S} {8,S}
8     C  U0 {7,S} {9,S}
9     C  U0 {8,S} {10,S}
10    C  U0 {5,S} {9,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "C_rad/H/NonDeC_5ring_beta6ring",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *3 C  U1 {2,S} {3,S} {4,S}
2     H  U0 {1,S}
3     Cs U0 {1,S} {5,S}
4     Cs U0 {1,S} {6,S}
5     Cs U0 {3,S} {6,S} {7,S}
6     Cs U0 {4,S} {5,S} {10,S}
7     C  U0 {5,S} {8,S}
8     C  U0 {7,S} {9,S}
9     C  U0 {8,S} {10,S}
10    C  U0 {6,S} {9,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "C_rad/H/Cs\H2\Cs/Cs\H2\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {6,S} {7,S} {8,S}
2     C U0 {1,S} {3,S} {9,S} {10,S}
3  *3 C U1 {2,S} {4,S} {11,S}
4     C U0 {3,S} {5,S} {12,S} {13,S}
5     O U0 {4,S} {14,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10    H U0 {2,S}
11    H U0 {3,S}
12    H U0 {4,S}
13    H U0 {4,S}
14    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "C_rad/H/Cs\H\Cs\O/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {3,S} {6,S} {7,S} {8,S}
2     C U0 {4,S} {9,S} {10,S} {11,S}
3  *3 C U1 {1,S} {4,S} {12,S}
4     C U0 {2,S} {3,S} {5,S} {13,S}
5     O U0 {4,S} {14,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10    H U0 {2,S}
11    H U0 {2,S}
12    H U0 {3,S}
13    H U0 {4,S}
14    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "C_rad/H/Cs\H2\Cs|O/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {6,S} {7,S} {8,S}
2  *3 C U1 {1,S} {3,S} {9,S}
3     C U0 {2,S} {4,S} {10,S} {11,S}
4     C U0 {3,S} {5,S} {12,S} {13,S}
5     O U0 {4,S} {14,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10    H U0 {3,S}
11    H U0 {3,S}
12    H U0 {4,S}
13    H U0 {4,S}
14    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "C_rad/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C      U1 {2,S} {3,S} {4,S}
2    H      U0 {1,S}
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
    index = 290,
    label = "C_rad/H/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 291,
    label = "C_rad/H/Cs\H2\Cs/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S} {5,S} {6,S} {7,S}
4    O  U0 {1,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
7    Cs U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {6,S} {7,S} {8,S}
2     C U0 {1,S} {3,S} {9,S} {10,S}
3     C U0 {2,S} {4,S} {11,S} {12,S}
4  *3 C U1 {3,S} {5,S} {13,S}
5     O U0 {4,S} {14,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10    H U0 {2,S}
11    H U0 {3,S}
12    H U0 {3,S}
13    H U0 {4,S}
14    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "C_rad/H/Cs\H\Cs2/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C U0 {2,S}
2    C U0 {1,S} {3,S} {5,S} {6,S}
3 *3 C U1 {2,S} {4,S} {7,S}
4    O U0 {3,S} {8,S}
5    C U0 {2,S}
6    H U0 {2,S}
7    H U0 {3,S}
8    H U0 {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "C_rad/H/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 295,
    label = "C_rad/H/NonDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C      U1 {2,S} {3,S} {4,S}
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
    index = 296,
    label = "C_rad/H/CsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 297,
    label = "C_rad/H/S2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
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
    index = 430,
    label = "C_rad/H/NonDeCN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 431,
    label = "C_rad/H/NonDeON",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    O U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 432,
    label = "C_rad/H/NonDeNN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    N U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "C_rad/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
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
    index = 299,
    label = "C_rad/H/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 300,
    label = "C_rad/H/CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "C_rad/H/CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "C_rad/H/CO/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "C_rad/H/CO\H/Cs\H3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C U0 {2,S} {5,S} {6,S} {7,S}
2 *3 C U1 {1,S} {3,S} {8,S}
3    C U0 {2,S} {4,D} {9,S}
4    O U0 {3,D}
5    H U0 {1,S}
6    H U0 {1,S}
7    H U0 {1,S}
8    H U0 {2,S}
9    H U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "C_rad/H/CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "C_rad/H/CSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "C_rad/H/OneDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 307,
    label = "C_rad/H/OneDeS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "C_rad/H/CtS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
4    S  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "C_rad/H/CbS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cb U0 {1,S}
4    S  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "C_rad/H/CdS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S} {5,D}
4    S U0 {1,S}
5    C U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "C_rad/H/CSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S} {5,D}
4    S U0 {1,S}
5    S U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 433,
    label = "C_rad/H/OneDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S}
4    N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "C_rad/H/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 313,
    label = "C_rad/H/CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "C_rad/H/CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
4    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "C_rad/H/CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "C_rad/H/CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cb U0 {1,S}
4    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "C_rad/H/CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cb U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "C_rad/H/COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    CO U0 {1,S}
4    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "C_rad/H/CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Ct U0 {1,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "C_rad/H/CtCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Ct U0 {1,S}
4    C  U0 {1,S} {5,D}
5    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "C_rad/H/CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Cb U0 {1,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "C_rad/H/CbCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    Cb U0 {1,S}
4    C  U0 {1,S} {5,D}
5    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "C_rad/H/CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    C  U0 {1,S} {5,D}
4    CO U0 {1,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "C_rad/H/COCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    H  U0 {1,S}
3    CO U0 {1,S}
4    C  U0 {1,S} {5,D}
5    S  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "C_rad/H/CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S} {5,D}
4    C U0 {1,S} {6,D}
5    C U0 {3,D}
6    C U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "C_rad/H/CdCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S} {5,D}
4    C U0 {1,S} {6,D}
5    C U0 {3,D}
6    S U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "C_rad/H/CSCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    C U0 {1,S} {5,D}
4    C U0 {1,S} {6,D}
5    S U0 {3,D}
6    S U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "C_ter_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C   U1 {2,S} {3,S} {4,S}
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
    index = 329,
    label = "C_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C        U1 {2,S} {3,S} {4,S}
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
    index = 330,
    label = "C_rad/Cs3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
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
    index = 331,
    label = "C_rad/Cs2/Cs\O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    Cs U0 {2,S}
2 *3 C  U1 {1,S} {3,S} {5,S}
3    Cs U0 {2,S} {4,S}
4    O  U0 {3,S}
5    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "C_rad/Cs3_5ring_fused6",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cs U0 {1,S} {5,S}
3    Cs U0 {1,S} {6,S}
4    Cs U0 {1,S} {7,S}
5    Cs U0 {2,S} {6,S}
6    Cs U0 {3,S} {5,S} {7,S}
7    Cs U0 {4,S} {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "C_rad/Cs3_5ring_adj5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cs U0 {1,S} {5,S}
3    Cs U0 {1,S} {6,S} {8,S}
4    Cs U0 {1,S} {7,S}
5    Cs U0 {2,S} {6,S}
6    Cs U0 {3,S} {5,S}
7    Cs U0 {4,S} {8,S}
8    Cs U0 {3,S} {7,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "C_rad/NDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C      U1 {2,S} {3,S} {4,S}
2    O      U0 {1,S}
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
    index = 335,
    label = "C_rad/Cs2O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    O  U0 {1,S}
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
    index = 336,
    label = "C_rad/OOH/Cs/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    O  U0 {1,S} {5,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    O  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "C_rad/O/Cs/Cs\Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {3,S} {6,S} {7,S} {8,S}
2     C U0 {4,S} {9,S} {10,S} {11,S}
3     C U0 {1,S} {4,S} {12,S} {13,S}
4  *3 C U1 {2,S} {3,S} {5,S}
5     O U0 {4,S} {14,S}
6     H U0 {1,S}
7     H U0 {1,S}
8     H U0 {1,S}
9     H U0 {2,S}
10    H U0 {2,S}
11    H U0 {2,S}
12    H U0 {3,S}
13    H U0 {3,S}
14    H U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "C_rad/CsO2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    O  U0 {1,S}
3    O  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "C_rad/O3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    O U0 {1,S}
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
    index = 340,
    label = "C_rad/NDMustS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C      U1 {2,S} {3,S} {4,S}
2    S      U0 {1,S}
3    {Cs,S} U0 {1,S}
4    {Cs,S} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "C_rad/Cs2S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    S  U0 {1,S}
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
    index = 342,
    label = "C_rad/CsS2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    S  U0 {1,S}
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
    index = 343,
    label = "C_rad/S3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,S} {3,S} {4,S}
2    S U0 {1,S}
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
    index = 344,
    label = "C_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 345,
    label = "C_rad/Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 346,
    label = "C_rad/CtCs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
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
    index = 347,
    label = "C_rad/CbCs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
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
    index = 348,
    label = "C_rad/COCs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
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
    index = 349,
    label = "C_rad/CdCs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "C_rad/CSCs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    S  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "C_rad/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    O             U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "C_rad/CsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    S             U0 {1,S}
4    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "C_rad/CtCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
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
    index = 354,
    label = "C_rad/CbCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
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
    index = 355,
    label = "C_rad/CdCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    S  U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "C_rad/CSCsS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    S  U0 {1,S}
4    Cs U0 {1,S}
5    S  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "C_rad/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    O             U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "C_rad/OS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    S             U0 {1,S}
4    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "C_rad/S2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    S             U0 {1,S}
4    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "C_rad/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 361,
    label = "C_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 362,
    label = "C_rad/CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "C_rad/CtCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "C_rad/CtCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "C_rad/CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "C_rad/CbCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "C_rad/COCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "C_rad/CdCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "C_rad/CtCSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "C_rad/CdCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "C_rad/CbCSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "C_rad/CdCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    CO U0 {1,S}
4    Cs U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "C_rad/COCSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    C  U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "C_rad/CdCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    C  U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    C  U0 {2,D}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "C_rad/CdCSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    C  U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    C  U0 {2,D}
6    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "C_rad/CSCSCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    C  U0 {1,S} {5,D}
3    C  U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    S  U0 {2,D}
6    S  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "C_rad/TDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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
    index = 378,
    label = "C_rad/TDMustS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO} U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    S             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "C_rad/ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C             U1 {2,S} {3,S} {4,S}
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

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
    L2: X_H
        L3: H2
        L3: N3_H
            L4: N3d_H
                L5: N3d/H/NonDe
                    L6: N3d/H/NonDeO
                    L6: N3d/H/NonDeN
                    L6: N3d/H/NonDeC
                L5: N3d/H/OneDe
                    L6: N3d/H/OneDeC
                    L6: N3d/H/OneDeN
            L4: N3s_H
                L5: NH3
                L5: N3s_pri_H
                    L6: N3s/H2/NonDe
                        L7: N3s/H2/NonDeC
                        L7: N3s/H2/NonDeO
                        L7: N3s/H2/NonDeN
                    L6: N3s/H2/OneDe
                        L7: N3s/H2/OneDeN
                L5: N3s_sec_H
        L3: N5_H
            L4: N5d_H
                L5: N5d/H/NonDeOO
        L3: Ct_H
            L4: Ct/H/NonDeC
            L4: Ct/H/NonDeN
        L3: O_H
            L4: O_pri
            L4: O_sec
                L5: O/H/NonDeC
                L5: O/H/NonDeO
                    L6: H2O2
                    L6: ROOH_pri
                    L6: ROOH_sec
                    L6: ROOH_ter
                L5: O/H/NonDeN
                L5: O/H/OneDe
                    L6: O/H/OneDeC
                    L6: O/H/OneDeN
        L3: Orad_O_H
        L3: S_H
            L4: S_pri
            L4: S_sec
                L5: S/H/NonDeC
                L5: S/H/NonDeS
                L5: S/H/OneDe
                    L6: S/H/Ct
                    L6: S/H/Cb
                    L6: S/H/CO
                    L6: S/H/Cd
                    L6: S/H/CS
        L3: Cd_H
            L4: Cd_pri
                L5: Cd/H2/NonDeC
                L5: Cd/H2/NonDeN
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/NonDeS
                L5: Cd/H/NonDeN
                L5: Cd/H/OneDe
                    L6: Cd/H/Ct
                    L6: Cd/H/Cb
                    L6: Cd/H/CO
                    L6: Cd/H/N
                    L6: Cd/H/Cd
                    L6: Cd/H/CS
        L3: Cb_H
        L3: CO_H
            L4: CO_pri
            L4: CO_sec
                L5: CO/H/NonDe
                    L6: CO/H/Cs
                        L7: CO/H/Cs\Cs|Cs
                L5: CO/H/OneDe
        L3: CS_H
            L4: CS_pri
            L4: CS_sec
                L5: CS/H/NonDeC
                L5: CS/H/NonDeO
                L5: CS/H/NonDeS
                L5: CS/H/OneDe
                    L6: CS/H/Ct
                    L6: CS/H/Cb
                    L6: CS/H/CO
                    L6: CS/H/Cd
                    L6: CS/H/CS
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C/H3/Cs
                    L6: C/H3/Cs\H3
                    L6: C/H3/CsNonDe
                        L7: C/H3/Cs\H2\Cs
                            L8: C/H3/Cs\H2\Cs|O
                        L7: C/H3/Cs\H2\O
                    L6: C/H3/CsNonDe
                        L7: C/H3/Cs\H\Cs\O
                        L7: C/H3/Cs\H\Cs\Cs|O
                L5: C/H3/O
                L5: C/H3/S
                L5: C/H3/OneDe
                    L6: C/H3/Ct
                    L6: C/H3/Cb
                    L6: C/H3/CO
                    L6: C/H3/Cd
                        L7: C/H3/Cd\H_Cd\H2
                        L7: C/H3/Cd\H_Cd\H\Cs
                        L7: C/H3/Cd\Cs_Cd\H2
                    L6: C/H3/CS
                L5: Cs/H3/NonDeN
                L5: Cs/H3/OneDeN
            L4: C_sec
                L5: C/H2/NonDeC
                    L6: C/H2/Cs/Cs\O
                    L6: C/H2/Cs/Cs\Cs|O
                    L6: C/H2/NonDeC_5ring
                        L7: C/H2/NonDeC_5ring_fused6_1
                        L7: C/H2/NonDeC_5ring_fused6_2
                        L7: C/H2/NonDeC_5ring_alpha6ring
                        L7: C/H2/NonDeC_5ring_beta6ring
                    L6: C/H2/Cs\H3/Cs\H3
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                        L7: C/H2/Cs\Cs2/O
                    L6: C/H2/O2
                L5: C/H2/NonDeS
                    L6: C/H2/CsS
                L5: C/H2/NonDeN
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                        L7: C/H2/CtCs
                        L7: C/H2/CbCs
                        L7: C/H2/COCs
                            L8: C/H2/CO\H/Cs\H3
                        L7: C/H2/CdCs
                            L8: C/H2/Cd\H_Cd\H2/Cs\H3
                        L7: C/H2/CSCs
                    L6: C/H2/OneDeO
                    L6: C/H2/OneDeS
                        L7: C/H2/CbS
                        L7: C/H2/CtS
                        L7: C/H2/CdS
                        L7: C/H2/CSS
                L5: C/H2/TwoDe
                    L6: C/H2/CtCt
                    L6: C/H2/CtCb
                    L6: C/H2/CtCO
                    L6: C/H2/CbCb
                    L6: C/H2/CbCO
                    L6: C/H2/COCO
                    L6: C/H2/CdCt
                    L6: C/H2/CtCS
                    L6: C/H2/CdCb
                    L6: C/H2/CbCS
                    L6: C/H2/CdCO
                    L6: C/H2/COCS
                    L6: C/H2/CdCd
                    L6: C/H2/CdCS
                    L6: C/H2/CSCS
                L5: C/H2/Cb
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                        L7: C/H/Cs3_5ring
                            L8: C/H/Cs3_5ring_fused6
                            L8: C/H/Cs3_5ring_adj5
                        L7: C/H/Cs2/Cs\O
                    L6: C/H/Cs2N
                    L6: C/H/NDMustO
                        L7: C/H/Cs2O
                        L7: C/H/CsO2
                        L7: C/H/O3
                    L6: C/H/NDMustS
                        L7: C/H/Cs2S
                        L7: C/H/CsS2
                        L7: C/H/S3
                    L6: C/H/NDMustOS
                        L7: C/H/CsOS
                L5: C/H/OneDe
                    L6: C/H/Cs2
                        L7: C/H/Cs2Ct
                        L7: C/H/Cs2Cb
                        L7: C/H/Cs2CO
                        L7: C/H/Cs2Cd
                        L7: C/H/Cs2CS
                    L6: C/H/CsO
                    L6: C/H/CsS
                        L7: C/H/CbCsS
                        L7: C/H/CtCsS
                        L7: C/H/CdCsS
                        L7: C/H/CSCsS
                    L6: C/H/OO
                    L6: C/H/OS
                    L6: C/H/SS
                L5: C/H/TwoDe
                    L6: C/H/Cs
                        L7: C/H/CtCt
                        L7: C/H/CtCb
                        L7: C/H/CtCO
                        L7: C/H/CbCb
                        L7: C/H/CbCO
                        L7: C/H/COCO
                        L7: C/H/CdCt
                        L7: C/H/CtCS
                        L7: C/H/CdCb
                        L7: C/H/CbCS
                        L7: C/H/CdCO
                        L7: C/H/COCS
                        L7: C/H/CdCd
                        L7: C/H/CdCS
                        L7: C/H/CSCS
                    L6: C/H/TDMustO
                    L6: C/H/TDMustS
                L5: C/H/ThreeDe
                L5: C/H/Cb
    L2: Xrad_H
        L3: C_rad_H
            L4: CH3_rad_H
            L4: Cs/H2/OneDeN
        L3: OH_rad_H
        L3: Srad_H
        L3: N3s_rad_H
            L4: NH2_rad_H
            L4: N3s_rad_H_pri
                L5: N3s_rad_H/H/NonDeN
    L2: Xbirad_H
        L3: NH_(T)_H
        L3: NH_(S)_H
        L3: CH2_(T)_H
        L3: CH2_(S)_H
    L2: Xtrirad_H
        L3: C_(Q)_H
        L3: C_(D)_H
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
    L2: Y_1centerbirad
        L3: O_(T)
        L3: O_(S)
        L3: NH_(T)
        L3: NH_(S)
        L3: CH2_(T)
        L3: CH2_(S)
    L2: Y_rad
        L3: H_rad
        L3: N3_rad
            L4: N3s_rad
                L5: NH2_rad
                L5: N3s_rad_pri
                L5: N3s_rad_sec
            L4: N3d_rad
                L5: N3d_rad/OneDe
                    L6: N3d_rad/OneDeC
                        L7: N3d_rad/OneDeCdd_O
        L3: N5_rad
            L4: N5d_rad
        L3: Y_2centeradjbirad
            L4: O2b
            L4: C2b
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/N
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                    L6: O_rad/Cs\H2\Cs|H|Cs2
                L5: O_rad/NonDeO
                    L6: OOC
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
                    L6: O_rad/OneDeN
                    L6: O_rad/Cd
                        L7: O_rad/Cd\H_Cd\H2
                        L7: O_rad/Cd\H_Cd\H\Cs
                        L7: O_rad/Cd\H_Cd\Cs2
                        L7: O_rad/Cd\Cs_Cd\H2
                        L7: O_rad/Cd\Cs_Cd\H\Cs
                        L7: O_rad/Cd\Cs_Cd\Cs2
                    L6: InChI=1S/NO3/c2-1(3)4
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
                    L6: S_rad/Ct
                    L6: S_rad/Cb
                    L6: S_rad/CO
                    L6: S_rad/Cd
                    L6: S_rad/CS
        L3: Cd_rad
            L4: Cd_pri_rad
                L5: Cd_Cd\H2_pri_rad
                L5: Cd_Cd\H\Cs_pri_rad
                    L6: Cd_Cd\H\Cs|H2|Cs_pri_rad
                L5: Cd_Cd\Cs2_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: Cd_Cd\H2_rad/Cs
                    L6: Cd_Cd\H\Cs_rad/Cs
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/NonDeN
                L5: Cd_rad/OneDe
                    L6: Cd_rad/Ct
                    L6: Cd_rad/Cb
                    L6: Cd_rad/CO
                    L6: Cd_rad/Cd
                    L6: Cd_rad/CS
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CS_rad
            L4: CS_pri_rad
            L4: CS_sec_rad
                L5: CS_rad/NonDe
                    L6: CS_rad/Cs
                    L6: CS_rad/O
                    L6: CS_rad/S
                L5: CS_rad/OneDe
                    L6: CS_rad/Ct
                    L6: CS_rad/Cb
                    L6: CS_rad/CO
                    L6: CS_rad/Cd
                    L6: CS_rad/CS
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                    L6: C_rad/H2/Cs\H3
                    L6: C_rad/H2/Cs\Cs2\O
                    L6: C_rad/H2/Cs\H\Cs\Cs|O
                    L6: C_rad/H2/Cs\H\Cs|Cs\O
                    L6: C_rad/H2/Cs\H2\Cs|Cs|O
                    L6: C_rad/H2/Cs\H2\Cs|Cs#O
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
                L5: C_rad/H2/S
                L5: C_rad/H2/N
                L5: C_rad/H2/Cd
                    L6: C_rad/H2/Cd\H_Cd\H2
                    L6: C_rad/H2/Cd\Cs_Cd\H2
                L5: C_rad/H2/CS
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                    L6: C_rad/H/NonDeC_5ring_fused6_1
                    L6: C_rad/H/NonDeC_5ring_fused6_2
                    L6: C_rad/H/Cs\H3/Cs\H3
                    L6: C_rad/H/NonDeC_5ring_alpha6ring
                    L6: C_rad/H/NonDeC_5ring_beta6ring
                    L6: C_rad/H/Cs\H2\Cs/Cs\H2\O
                    L6: C_rad/H/Cs\H\Cs\O/Cs
                    L6: C_rad/H/Cs\H2\Cs|O/Cs
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                        L7: C_rad/H/Cs\H2\Cs/O
                            L8: C_rad/H/Cs\H2\Cs|H2|Cs/O
                        L7: C_rad/H/Cs\H\Cs2/O
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/NonDeCN
                L5: C_rad/H/NonDeON
                L5: C_rad/H/NonDeNN
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                        L7: C_rad/H/CtCs
                        L7: C_rad/H/CbCs
                        L7: C_rad/H/CO/Cs
                            L8: C_rad/H/CO\H/Cs\H3
                        L7: C_rad/H/CdCs
                        L7: C_rad/H/CSCs
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeS
                        L7: C_rad/H/CtS
                        L7: C_rad/H/CbS
                        L7: C_rad/H/CdS
                        L7: C_rad/H/CSS
                    L6: C_rad/H/OneDeN
                L5: C_rad/H/TwoDe
                    L6: C_rad/H/CtCt
                    L6: C_rad/H/CtCb
                    L6: C_rad/H/CtCO
                    L6: C_rad/H/CbCb
                    L6: C_rad/H/CbCO
                    L6: C_rad/H/COCO
                    L6: C_rad/H/CdCt
                    L6: C_rad/H/CtCS
                    L6: C_rad/H/CdCb
                    L6: C_rad/H/CbCS
                    L6: C_rad/H/CdCO
                    L6: C_rad/H/COCS
                    L6: C_rad/H/CdCd
                    L6: C_rad/H/CdCS
                    L6: C_rad/H/CSCS
            L4: C_ter_rad
                L5: C_rad/NonDe
                    L6: C_rad/Cs3
                        L7: C_rad/Cs2/Cs\O
                        L7: C_rad/Cs3_5ring_fused6
                        L7: C_rad/Cs3_5ring_adj5
                    L6: C_rad/NDMustO
                        L7: C_rad/Cs2O
                            L8: C_rad/OOH/Cs/Cs
                            L8: C_rad/O/Cs/Cs\Cs
                        L7: C_rad/CsO2
                        L7: C_rad/O3
                    L6: C_rad/NDMustS
                        L7: C_rad/Cs2S
                        L7: C_rad/CsS2
                        L7: C_rad/S3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                        L7: C_rad/CtCs2
                        L7: C_rad/CbCs2
                        L7: C_rad/COCs2
                        L7: C_rad/CdCs2
                        L7: C_rad/CSCs2
                    L6: C_rad/CsO
                    L6: C_rad/CsS
                        L7: C_rad/CtCsS
                        L7: C_rad/CbCsS
                        L7: C_rad/CdCsS
                        L7: C_rad/CSCsS
                    L6: C_rad/O2
                    L6: C_rad/OS
                    L6: C_rad/S2
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                        L7: C_rad/CtCtCs
                        L7: C_rad/CtCbCs
                        L7: C_rad/CtCOCs
                        L7: C_rad/CbCbCs
                        L7: C_rad/CbCOCs
                        L7: C_rad/COCOCs
                        L7: C_rad/CdCtCs
                        L7: C_rad/CtCSCs
                        L7: C_rad/CdCbCs
                        L7: C_rad/CbCSCs
                        L7: C_rad/CdCOCs
                        L7: C_rad/COCSCs
                        L7: C_rad/CdCdCs
                        L7: C_rad/CdCSCs
                        L7: C_rad/CSCSCs
                    L6: C_rad/TDMustO
                    L6: C_rad/TDMustS
                L5: C_rad/ThreeDe
"""
)

