#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Y_rad", "Y_rad"], products=["Y_Y"], ownReverse=False)

reverse = "Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_rad",
    group = 
"""
1 * R u1
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "H_rad",
    group = 
"""
1 * H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "S_rad",
    group = 
"""
1 * S u1 px
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "S2sJ",
    group = 
"""
1 * S2s u1 p2
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "SsJ-H",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   H   u0    {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "SsJ-C",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   C   u0    {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "SsJ-Cs",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cs  u0    {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "SsJ-Ct",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Ct  u0    {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "SsJ-Cb",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cb  u0    {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "SsJ-Cd",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   Cd  u0    {1,S} {3,D}
3   C   u0    {2,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "SsJ-C=S",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   CS  u0    {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "SsJ-S2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u0 p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "SsJ-O2s",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   O2s  u0 p2 {1,S}
""",
    kinetics = None,
)
 
entry(
    index = 14,
    label = "S2_birad",
    group = 
"""
1 * S2s u1 p2 {2,S}
2   S2s u1 p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Ct_rad",
    group = 
"""
1 * Ct  u1 {2,T}
2   R!H u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Ct_rad/Ct",
    group = 
"""
1 * Ct u1 {2,T}
2   Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Ct_rad/Nt",
    group = 
"""
1 * Ct        u1 {2,T}
2   [N3t,N5tc] u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "O_rad",
    group = 
"""
1 * O u1 {2,S}
2   R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "O_pri_rad",
    group = 
"""
1 * O u1 {2,S}
2   H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "O_sec_rad",
    group = 
"""
1 * O   u1 {2,S}
2   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "O_rad/NonDe",
    group = 
"""
1 * O                           u1 {2,S}
2   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "O_rad/OneDe",
    group = 
"""
1 * O u1 {2,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "O2_birad",
    group = 
"""
1 * O u1 {2,S}
2   O u1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cd_rad",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   C u0 {1,D}
3   R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Cd_pri_rad",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   C u0 {1,D} {4,S} {5,S}
3   H u0 {1,S}
4   R u0 {2,S}
5   R u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Cd_sec_rad",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   C   u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S}
4   R   u0 {2,S}
5   R   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Cd_rad/NonDe",
    group = 
"""
1 * C      u1 {2,D} {3,S}
2   C      u0 {1,D} {4,S} {5,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   R      u0 {2,S}
5   R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cd_rad/OneDe",
    group = 
"""
1 * C      u1 {2,D} {3,S}
2   C      u0 {1,D} {4,S} {5,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   R      u0 {2,S}
5   R      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cd_rad/Cd",
    group = 
"""
1 * C  u1 {2,D} {3,S}
2   C  u0 {1,D} {4,S} {5,S}
3   Cd u0 {1,S}
4   R  u0 {2,S}
5   R  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cd_allenic",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   Cdd u0 {1,D}
3   R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cb_rad",
    group = 
"""
1 * Cb       u1 {2,B} {3,B}
2   [Cb,Cbf] u0 {1,B}
3   [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "CO_rad",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O u0 {1,D}
3   R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "CO_pri_rad",
    group = 
"""
1 * C u1 {2,D} {3,S}
2   O u0 {1,D}
3   H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "CO_sec_rad",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   O   u0 {1,D}
3   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CO_rad/NonDe",
    group = 
"""
1 * C      u1 {2,D} {3,S}
2   O      u0 {1,D}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CO_rad/OneDe",
    group = 
"""
1 * C      u1 {2,D} {3,S}
2   O      u0 {1,D}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CS_rad",
    group = 
"""
1 * CS u1 {2,S}
2   R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "CS_pri_rad",
    group = 
"""
1 * CS u1 {2,S}
2   H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "CS_sec_rad",
    group = 
"""
1 * CS  u1 {2,S}
2   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "CS_rad/NonDe",
    group = 
"""
1 * CS                          u1 {2,S},
2   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "CS_rad/OneDe",
    group = 
"""
1 * CS     u1 {2,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Cs_rad",
    group = 
"""
1 * C u1 {2,S} {3,S} {4,S}
2   R u0 {1,S}
3   R u0 {1,S}
4   R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C_methyl",
    group = 
"""
1 * C u1 {2,S} {3,S} {4,S}
2   H u0 {1,S}
3   H u0 {1,S}
4   H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "C_pri_rad",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "C_rad/H2/Cs",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "C_rad/H2/Cd",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "C_rad/H2/Ct",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "C_rad/H2/Cb",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "C_rad/H2/CO",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "C_rad/H2/O",
    group = 
"""
1 * C u1 {2,S} {3,S} {4,S}
2   H u0 {1,S}
3   H u0 {1,S}
4   O u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "C_rad/H2/CS",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "C_rad/H2/N",
    group = 
"""
1 * C u1 {2,S} {3,S} {4,S}
2   H u0 {1,S}
3   H u0 {1,S}
4   N u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "C_rad/H2/S",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "C_sec_rad",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "C_rad/H/NonDe",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   H                           u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "C_rad/H/NonDeN",
    group = 
"""
1 * C                        u1 {2,S} {3,S} {4,S}
2   H                        u0 {1,S}
3   [Cs,N3s,N5sc,S2s,S4s,S6s] u0 {1,S}
4   [N3s,N5sc]                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   H                           u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   O2s                          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "C_rad/H/CsO",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "C_rad/H/O2",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "C_rad/H/SO",
    group = 
"""
1 * C             u1 {2,S} {3,S} {4,S}
2   H             u0 {1,S}
3   [S2s,S4s,S6s] u0 {1,S}
4   O2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "C_rad/H/NO",
    group = 
"""
1 * C         u1 {2,S} {3,S} {4,S}
2   H         u0 {1,S}
3   [N3s,N5sc] u0 {1,S}
4   O2s        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   H                           u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   [S2s,S4s,S6s]               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "C_rad/H/OneDe",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   H                           u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   H      u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   Cs     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "C_rad/H/CdCs",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Cd u0 {1,S}
4   Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "C_rad/H/CtCs",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   H      u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   O2s     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "C_rad/H/OneDeS",
    group = 
"""
1 * C             u1 {2,S} {3,S} {4,S}
2   H             u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "C_rad/H/OneDeN",
    group = 
"""
1 * C         u1 {2,S} {3,S} {4,S}
2   H         u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   H      u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "C_rad/H/CdCd",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Cd u0 {1,S}
4   Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "C_rad_cyclopentadiene",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {3,D} {6,S}
6   Cd u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "C_ter_rad",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "C_rad/NonDe",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "C_rad/Cs3",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "C_rad/NonDeO",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   O2s                          u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "C_rad/NonDeCO",
    group = 
"""
1 * C       u1 {2,S} {3,S} {4,S}
2   [Cs,O2s] u0 {1,S}
3   [Cs,O2s] u0 {1,S}
4   O2s      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "C_rad/NonDeS",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   [S2s,S4s,S6s]               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "C_rad/NonDe2CsSs",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "C_rad/NonDeCs2Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "C_rad/NonDe3Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "C_rad/NonDeN",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   [N3s,N5sc]                   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "C_rad/OneDe",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "C_rad/OneDeCs2",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   Cs     u0 {1,S}
4   Cs     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "C_rad/OneDeO",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
4   O2s     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "C_rad/OneDeS",
    group = 
"""
1 * C                                                              u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s]                                    u0 {1,S}
4   [S2s,S4s,S6s]                                                  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "C_rad/OneDeCtSs",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "C_rad/OneDeCbSs",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "C_rad/OneDeCdSs",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S} {5,D}
4   S2s u0 {1,S}
5   C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "C_rad/OneDeCSSs",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   CS  u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "C_rad/OneDeCOSs",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   CO  u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "C_rad/OneDeCt2Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "C_rad/OneDeCb2Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "C_rad/OneDeCd2Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "C_rad/OneDeCS2Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   CS  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "C_rad/OneDeCO2Ss",
    group = 
"""
1 * C   u1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "C_rad/OneDeN",
    group = 
"""
1 * C                                                              u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s]                                    u0 {1,S}
4   [N3s,N5sc]                                                      u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "C_rad/TwoDe",
    group = 
"""
1 * C                           u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [Cs,N3s,N5sc,O2s,S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "C_rad/TwoDeCs",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   Cs     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "C_rad/TwoDeO",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   O2s     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "C_rad/TwoDeS",
    group = 
"""
1 * C             u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [S2s,S4s,S6s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "C_rad/TwoDeN",
    group = 
"""
1 * C         u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [N3s,N5sc] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "C_rad/ThreeDe",
    group = 
"""
1 * C      u1 {2,S} {3,S} {4,S}
2   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
4   [Cd,Ct,CO,CS,Cb,Cbf,N3d,N5dc,N5tc,N5b,S4d,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "N1s_rad",
    group = 
"""
1 * N1s u1 p2
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "N3_rad",
    group = 
"""
1 * [N3s,N3d] u1
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "N3s_rad",
    group = 
"""
1 * N3s u1
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "N3s_pri_rad",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   H   u0 {1,S}
3   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "NH2_rad",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    kinetics = None,
)
        
entry(
    index = 109,
    label = "N3s-Cs",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   H   u0 {1,S}
3   Cs  u0 {1,S}
""",
    kinetics = None,
)
        
entry(
    index = 110,
    label = "N3s-O2s",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   H   u0 {1,S}
3   O2s  u0 {1,S}
""",
    kinetics = None,
)
        
entry(
    index = 111,
    label = "N3s-S",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   H   u0 {1,S}
3   S   u0 {1,S}
""",
    kinetics = None,
)
        
entry(
    index = 112,
    label = "N3s-N3s",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   H   u0 {1,S}
3   N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "N3s_sec_rad",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "N3s-CsCs",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "N3s-CsOs",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   Cs  u0 {1,S}
3   O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "N3s-CsN3s",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "N3s-OsOs",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O2s  u0 {1,S}
3   O2s  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "N3s-OsS",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O2s  u0 {1,S}
3   S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "N3s-SS",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   S   u0 {1,S}
3   S   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "N3s-OsN3s",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   O2s  u0 {1,S}
3   N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "N3s-SN3s",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   S   u0 {1,S}
3   N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "N3s-N3sN3s",
    group = 
"""
1 * N3s u1 {2,S} {3,S}
2   N3s u0 {1,S}
3   N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "N3d_rad",
    group = 
"""
1 * N3d u1 {2,D}
2   R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "N3d-Cd",
    group = 
"""
1 * N3d u1 {2,D}
2   Cd  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "N3d-Cdd",
    group = 
"""
1 * N3d u1 {2,D}
2   Cdd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "N3d-O2d",
    group = 
"""
1 * N3d u1 {2,D}
2   O2d  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "N3d-S2d",
    group = 
"""
1 * N3d                           u1 {2,D}
2   [S2d,S4d,S4dd,S6d,S6dd,S6ddd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "N3d-N3d",
    group = 
"""
1 * N3d u1 {2,D}
2   N3d u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "N5_rad",
    group = 
"""
1 * [N5sc,N5dc,N5tc,N5b] u1 p0
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "N5s_rad",
    group = 
"""
1 * N5sc u1 p0
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "N5dc_rad",
    group = 
"""
1 * N5dc u1 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "N5dc-OdOs",
    group = 
"""
1 * N5dc u1 p0 c+1 {2,D} {3,S}
2   O2d  u0 {1,D}
3   O0sc u0 p3 c-1 (1,S)
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "N5t_rad",
    group = 
"""
1 * N5tc u1 p0
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "N5b_rad",
    group = 
"""
1 * N5b u1 p0
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Cd_allenic_Cb",
    group = 
"""
1 * C   u1 {2,D} {3,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "C_rad/H/CdCb",
    group = 
"""
1 * C             u1 {2,S} {3,S} {4,S}
2   H             u0 {1,S}
3   Cd		  u0 {1,S}
4   Cb		  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "C_rad/H/CbCs",
    group = 
"""
1 * C  u1 {2,S} {3,S} {4,S}
2   H  u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Y_rad
    L2: H_rad
    L2: S_rad
        L3: S2sJ
            L4: SsJ-H
            L4: SsJ-C
                L5: SsJ-Cs
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-Cd
                L5: SsJ-C=S
            L4: SsJ-S2s
            L4: SsJ-O2s
            L4: S2_birad
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
        L3: Cd_allenic
	    L4: Cd_allenic_Cb
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: CS_rad
        L3: CS_pri_rad
        L3: CS_sec_rad
            L4: CS_rad/NonDe
            L4: CS_rad/OneDe
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
            L4: C_rad/H2/CS
            L4: C_rad/H2/N
            L4: C_rad/H2/S
        L3: C_sec_rad
            L4: C_rad/H/NonDe
                L5: C_rad/H/NonDeN
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                    L6: C_rad/H/SO
                    L6: C_rad/H/NO
                L5: C_rad/H/NonDeS
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                    L6: C_rad/H/CdCs
                    L6: C_rad/H/CtCs
                    L6: C_rad/H/CbCs
                L5: C_rad/H/OneDeO
                L5: C_rad/H/OneDeS
                L5: C_rad/H/OneDeN
            L4: C_rad/H/TwoDe
                L5: C_rad/H/CdCd
                    L6: C_rad_cyclopentadiene
                L5: C_rad/H/CdCb
        L3: C_ter_rad
            L4: C_rad/NonDe
                L5: C_rad/Cs3
                L5: C_rad/NonDeO
                    L6: C_rad/NonDeCO
                L5: C_rad/NonDeS
                    L6: C_rad/NonDe2CsSs
                    L6: C_rad/NonDeCs2Ss
                    L6: C_rad/NonDe3Ss
                L5: C_rad/NonDeN
            L4: C_rad/OneDe
                L5: C_rad/OneDeCs2
                L5: C_rad/OneDeO
                L5: C_rad/OneDeS
                    L6: C_rad/OneDeCtSs
                    L6: C_rad/OneDeCbSs
                    L6: C_rad/OneDeCdSs
                    L6: C_rad/OneDeCSSs
                    L6: C_rad/OneDeCOSs
                    L6: C_rad/OneDeCt2Ss
                    L6: C_rad/OneDeCb2Ss
                    L6: C_rad/OneDeCd2Ss
                    L6: C_rad/OneDeCS2Ss
                    L6: C_rad/OneDeCO2Ss
                L5: C_rad/OneDeN
            L4: C_rad/TwoDe
                L5: C_rad/TwoDeCs
                L5: C_rad/TwoDeO
                L5: C_rad/TwoDeS
                L5: C_rad/TwoDeN
            L4: C_rad/ThreeDe
    L2: N1s_rad
    L2: N3_rad
        L3: N3s_rad
            L4: NH2_rad
            L4: N3s_pri_rad
                L5: N3s-Cs
                L5: N3s-O2s
                L5: N3s-S
                L5: N3s-N3s
            L4: N3s_sec_rad
                L5: N3s-CsCs
                L5: N3s-CsOs
                L5: N3s-CsN3s
                L5: N3s-OsOs
                L5: N3s-OsS
                L5: N3s-SS
                L5: N3s-OsN3s
                L5: N3s-SN3s
                L5: N3s-N3sN3s
        L3: N3d_rad
            L4: N3d-Cd
            L4: N3d-Cdd
            L4: N3d-O2d
            L4: N3d-S2d
            L4: N3d-N3d
    L2: N5_rad
        L3: N5s_rad
        L3: N5dc_rad
            L4: N5dc-OdOs
        L3: N5t_rad
        L3: N5b_rad
"""
)

forbidden(
    label = "Cl",
    group = 
"""
1 *1 Cl u1
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "Cl_2",
    group = 
"""
1 *2 Cl u1
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "O4",
    group = 
"""
1    O u1 {2,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u0 {2,S} {4,S}
4    O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

