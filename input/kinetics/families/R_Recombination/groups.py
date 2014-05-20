#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad", "Y_rad"], products=["Y_Y"], ownReverse=False)

reverse = "Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * R U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "H_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * H U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "S_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * S U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "SsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "SsJ-C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   C  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "SsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "SsJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "SsJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "SsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cd U0 {1,S} {3,D}
3   C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "SsJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cd U0 {1,S} {3,D}
3   Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "SsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "SsJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "N3_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {N3s,N3d} U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "N3s_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "NH2_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U1 {2,S} {3,S}
2   H   U0 {1,S}
3   H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "N3s_rad_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U1 {2,S} {3,S}
2   H   U0 {1,S}
3   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "N3s_rad_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U1 {2,S} {3,S}
2   R!H U0 {1,S}
3   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "N3d_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U1 {2,D}
2   R!H U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "N5_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {N5s,N5d,N5t} U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "Ct_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U1 {2,T}
2   R!H U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Ct_rad/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,T}
2   C U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "Ct_rad/Nt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct        U1 {2,T}
2   {N3t,N5t} U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "O_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "O_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "O_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O   U1 {2,S}
2   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "O_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O      U1 {2,S}
2   {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "O_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O             U1 {2,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "O2_birad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   O U1 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Cd_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   C U0 {1,D}
3   R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "Cd_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   C U0 {1,D}
3   H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Cd_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U1 {2,D} {3,S}
2   C   U0 {1,D}
3   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Cd_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C      U1 {2,D} {3,S}
2   C      U0 {1,D}
3   {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Cd_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,D} {3,S}
2   C             U0 {1,D}
3   {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Cd_rad/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,D} {3,S}
2   C  U0 {1,D}
3   Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Cb_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb       U1 {2,B} {3,B}
2   {Cb,Cbf} U0 {1,B}
3   {Cb,Cbf} U0 {1,B}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "CO_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "CO_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CO_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U1 {2,D} {3,S}
2   O   U0 {1,D}
3   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CO_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C      U1 {2,D} {3,S}
2   O      U0 {1,D}
3   {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "CO_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,D} {3,S}
2   O             U0 {1,D}
3   {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C=SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,D} {3,S}
2   Sd U0 {1,D}
3   R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C=SJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   H  U0 {1,S}
3   Sd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C=SJ-C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   C  U0 {1,S}
3   Sd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C=SJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   Cs U0 {1,S}
3   Sd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C=SJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   Ss U0 {1,S}
3   Sd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cs_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   R U0 {1,S}
3   R U0 {1,S}
4   R U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C_methyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   H U0 {1,S}
3   H U0 {1,S}
4   H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C_pri_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U1 {2,S} {3,S} {4,S}
2   H   U0 {1,S}
3   H   U0 {1,S}
4   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C_rad/H2/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
4   Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C_rad/H2/Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
4   Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C_rad/H2/Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
4   Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C_rad/H2/Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
4   Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C_rad/H2/CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
4   CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C_rad/H2/O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   H U0 {1,S}
3   H U0 {1,S}
4   O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C_rad/H2/N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   H U0 {1,S}
3   H U0 {1,S}
4   N U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CsJ-SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C_sec_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U1 {2,S} {3,S} {4,S}
2   H   U0 {1,S}
3   R!H U0 {1,S}
4   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C_rad/H/NonDeN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U1 {2,S} {3,S} {4,S}
2   H   U0 {1,S}
3   Cs  U0 {1,S}
4   N3s U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C_rad/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C_rad/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C      U1 {2,S} {3,S} {4,S}
2   H      U0 {1,S}
3   O      U0 {1,S}
4   {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C_rad/H/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   Cs U0 {1,S}
4   O  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C_rad/H/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   H U0 {1,S}
3   O U0 {1,S}
4   O U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C_rad/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   H             U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C_rad/H/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   H             U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C_rad/H/CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C_rad/H/CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C_rad/H/OneDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   H             U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C_rad/H/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   H             U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C_rad/H/CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   H  U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CsJ-CSH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "CsJ-CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "CsJ-CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "CsJ-CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "CsJ-CdSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "CsJ-C=SSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "CsJ-SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C_ter_rad",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U1 {2,S} {3,S} {4,S}
2   R!H U0 {1,S}
3   R!H U0 {1,S}
4   R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C_rad/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C      U1 {2,S} {3,S} {4,S}
2   {Cs,O} U0 {1,S}
3   {Cs,O} U0 {1,S}
4   {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C_rad/Cs3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C_rad/NDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C      U1 {2,S} {3,S} {4,S}
2   O      U0 {1,S}
3   {Cs,O} U0 {1,S}
4   {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   {Cs,O}        U0 {1,S}
4   {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C_rad/Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   Cs            U0 {1,S}
4   Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C_rad/ODMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   O             U0 {1,S}
4   {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C_rad/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C_rad/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C_rad/TDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C_rad/ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C             U1 {2,S} {3,S} {4,S}
2   {Cd,Ct,Cb,CO} U0 {1,S}
3   {Cd,Ct,Cb,CO} U0 {1,S}
4   {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "CsJ-CSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "CsJ-CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "CsJ-CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "CsJ-CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "CsJ-CdSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "CsJ-C=SSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "CsJ-CCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "CsJ-CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "CsJ-CsCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "CsJ-CsCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "CsJ-CsCdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "CsJ-CsC=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "CsJ-SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Y_rad
    L2: H_rad
    L2: S_rad
        L3: SJ
            L4: SsJ-H
            L4: SsJ-C
                L5: SsJ-Cs
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-Cd
                L5: SsJ-C=S
            L4: SsJ-Ss
            L4: SsJ-Os
    L2: N3_rad
        L3: N3s_rad
            L4: NH2_rad
            L4: N3s_rad_pri
            L4: N3s_rad_sec
        L3: N3d_rad
    L2: N5_rad
    L2: Ct_rad
        L3: Ct_rad/Ct
        L3: Ct_rad/Nt
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: O2_birad
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
                L5: Cd_rad/Cd
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: C=SJ
        L3: C=SJ-H
        L3: C=SJ-C
            L4: C=SJ-Cs
        L3: C=SJ-Ss
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
            L4: C_rad/H2/N
            L4: CsJ-SsHH
        L3: C_sec_rad
            L4: C_rad/H/NonDeN
            L4: C_rad/H/NonDeC
            L4: C_rad/H/NonDeO
                L5: C_rad/H/CsO
                L5: C_rad/H/O2
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                    L6: C_rad/H/CdCs
                    L6: C_rad/H/CtCs
                L5: C_rad/H/OneDeO
            L4: C_rad/H/TwoDe
                L5: C_rad/H/CdCd
            L4: CsJ-CSH
                L5: CsJ-CsSsH
                L5: CsJ-CtSsH
                L5: CsJ-CbSsH
                L5: CsJ-CdSsH
                L5: CsJ-C=SSsH
            L4: CsJ-SsSsH
        L3: C_ter_rad
            L4: C_rad/NonDeC
                L5: C_rad/Cs3
                L5: C_rad/NDMustO
            L4: C_rad/OneDe
                L5: C_rad/Cs2
                L5: C_rad/ODMustO
            L4: C_rad/TwoDe
                L5: C_rad/Cs
                L5: C_rad/TDMustO
            L4: C_rad/ThreeDe
            L4: CsJ-CSS
                L5: CsJ-CsSsSs
                L5: CsJ-CtSsSs
                L5: CsJ-CbSsSs
                L5: CsJ-CdSsSs
                L5: CsJ-C=SSsSs
            L4: CsJ-CCS
                L5: CsJ-CsCsSs
                L5: CsJ-CsCtSs
                L5: CsJ-CsCbSs
                L5: CsJ-CsCdSs
                L5: CsJ-CsC=SSs
            L4: CsJ-SsSsSs
"""
)

forbidden(
    label = "O4",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    O U1 {2,S}
2 *1 O U0 {1,S} {3,S}
3 *2 O U0 {2,S} {4,S}
4    O U1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

