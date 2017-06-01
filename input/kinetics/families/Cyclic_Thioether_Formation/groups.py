#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Thioether_Formation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RnSS"], products=["RS", "SR"], ownReverse=False)

reverse = "SH+CyclicThioether_Form_Alkyl-disulfide"

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['GAIN_RADICAL', '*3', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 1,
    label = "RnSS",
    group = "OR{R2SS, R3SS, R4SS, R5SS}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_rad_intra",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R2SS",
    group = 
"""
1 *1 R!H    u1 {2,[S,D]}
2 *4 R!H    u0 {1,[S,D]} {3,S}
3 *2 S      u0 {2,S} {4,S}
4 *3 [Os,S] ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R2SS_S",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Cs,CO] u0 {1,S} {3,S}
3 *2 S          u0 {2,S} {4,S}
4 *3 [Os,S]     ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R2SS_SCO",
    group = 
"""
1 *1 R!H    u1 {2,S}
2 *4 CO     u0 {1,S} {3,S}
3 *2 S      u0 {2,S} {4,S}
4 *3 [Os,S] ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R2SS_D",
    group = 
"""
1 *1 R!H    u1 {2,D}
2 *4 Cd     u0 {1,D} {3,S}
3 *2 S      u0 {2,S} {4,S}
4 *3 [Os,S] ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R3SS",
    group =
"""
1 *1 R!H    u1 {2,[S,D]}
2 *4 R!H    u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H    u0 {2,[S,D]} {4,S}
4 *2 S      u0 {3,S} {5,S}
5 *3 [Os,S] ux {4,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R3SS_SS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3 *5 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *2 S          u0 {3,S} {5,S}
5 *3 [Os,S]     ux {4,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R3SS_SSCO",
    group = 
"""
1 *1 R!H     u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *5 CO      u0 {2,S} {4,S}
4 *2 S       u0 {3,S} {5,S}
5 *3 [Os,S]  ux {4,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R3SS_SD",
    group = 
"""
1 *1 R!H     u1 {2,S}
2 *4 Cd      u0 {1,S} {3,D}
3 *5 Cd      u0 {2,D} {4,S}
4 *2 S       u0 {3,S} {5,S}
5 *3 [Os,S]  ux {4,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R3SS_DS",
    group = 
"""
1 *1 R!H        u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *5 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *2 S          u0 {3,S} {5,S}
5 *3 [Os,S]     ux {4,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R4SS",
    group = 
"""
1 *1 R!H    u1 {2,[S,D]}
2 *4 R!H    u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H    u0 {2,[S,D]} {4,[S,D]}
4 *5 R!H    u0 {3,[S,D]} {5,S}
5 *2 S      u0 {4,S} {6,S}
6 *3 [Os,S] ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R4SS_SSS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3 *6 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *5 [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 S          u0 {4,S} {6,S}
6 *3 [Os,S]     ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R4SS_SSSCO",
    group = 
"""
1 *1 R!H     u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *6 [Cd,Cs] u0 {2,S} {4,S}
4 *5 CO      u0 {3,S} {5,S}
5 *2 S       u0 {4,S} {6,S}
6 *3 [Os,S]  ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R4SS_SSD",
    group = 
"""
1 *1 R!H     u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *6 Cd      u0 {2,S} {4,D}
4 *5 Cd      u0 {3,D} {5,S}
5 *2 S       u0 {4,S} {6,S}
6 *3 [Os,S]  ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R4SS_SDS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3 *6 Cd         u0 {2,D} {4,S}
4 *5 [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 S          u0 {4,S} {6,S}
6 *3 [Os,S]     ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R4SS_DSS",
    group = 
"""
1 *1 R!H        u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *5 [Cd,Cs,CO] u0 {3,S} {5,S}
5 *2 S          u0 {4,S} {6,S}
6 *3 [Os,S]     ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R4SS_DSD",
    group = 
"""
1 *1 R!H    u1 {2,D}
2 *4 Cd     u0 {1,D} {3,S}
3 *6 Cd     u0 {2,S} {4,D}
4 *5 Cd     u0 {3,D} {5,S}
5 *2 S      u0 {4,S} {6,S}
6 *3 [Os,S] ux {5,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "R5SS",
    group =
"""
1 *1 R!H    u1 {2,[S,D]}
2 *4 R!H    u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H    u0 {2,[S,D]} {4,[S,D]}
4 *7 R!H    u0 {3,[S,D]} {5,[S,D]}
5 *5 R!H    u0 {4,[S,D]} {6,S}
6 *2 S      u0 {5,S} {7,S}
7 *3 [Os,S] ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "R5SS_SSSS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3 *6 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *7 [Cd,Cs,CO] u0 {3,S} {5,S}
5 *5 [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 S          u0 {5,S} {7,S}
7 *3 [Os,S]     ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R5SS_SSSSCO",
    group = 
"""
1 *1 R!H     u1 {2,S}
2 *4 [Cd,Cs] u0 {1,S} {3,S}
3 *6 [Cd,Cs] u0 {2,S} {4,S}
4 *7 [Cd,Cs] u0 {3,S} {5,S}
5 *5 CO      u0 {4,S} {6,S}
6 *2 S       u0 {5,S} {7,S}
7 *3 [Os,S]  ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R5SS_SSSD",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3 *6 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *7 Cd         u0 {3,S} {5,D}
5 *5 Cd         u0 {4,D} {6,S}
6 *2 S          u0 {5,S} {7,S}
7 *3 [Os,S]     ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "R5SS_SSDS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Cs]    u0 {1,S} {3,S}
3 *6 Cd         u0 {2,S} {4,D}
4 *7 Cd         u0 {3,D} {5,S}
5 *5 [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 S          u0 {5,S} {7,S}
7 *3 [Os,S]     ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "R5SS_SDSS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3 *6 Cd         u0 {2,D} {4,S}
4 *7 [Cd,Cs,CO] u0 {3,S} {5,S}
5 *5 [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 S          u0 {5,S} {7,S}
7 *3 [Os,S]     ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "R5SS_DSSS",
    group = 
"""
1 *1 R!H        u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Cs,CO] u0 {2,S} {4,S}
4 *7 [Cd,Cs,CO] u0 {3,S} {5,S}
5 *5 [Cd,Cs,CO] u0 {4,S} {6,S}
6 *2 S          u0 {5,S} {7,S}
7 *3 [Os,S]     ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "R5SS_SDSD",
    group = 
"""
1 *1 R!H    u1 {2,S}
2 *4 Cd     u0 {1,S} {3,D}
3 *6 Cd     u0 {2,D} {4,S}
4 *7 Cd     u0 {3,S} {5,D}
5 *5 Cd     u0 {4,D} {6,S}
6 *2 S      u0 {5,S} {7,S}
7 *3 [Os,S] ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "R5SS_DSDS",
    group = 
"""
1 *1 R!H    u1 {2,D}
2 *4 Cd     u0 {1,D} {3,S}
3 *6 Cd     u0 {2,S} {4,D}
4 *7 Cd     u0 {3,D} {5,S}
5 *5 Cd     u0 {4,S} {6,S}
6 *2 S      u0 {5,S} {7,S}
7 *3 [Os,S] ux {6,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cd_rad_out",
    group = 
"""
1 *1 Cd  u1 {2,D}
2    R!H u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cd_rad_in",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cd_pri_rad_in",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cd_sec_rad_in",
    group = 
"""
1 *1 Cd   u1 {2,S}
2    R!H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cd_rad_in/NonDeC",
    group = 
"""
1 *1 Cd u1 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cd_rad_in/NonDeO",
    group = 
"""
1 *1 Cd u1 {2,S}
2    O  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cd_rad_in/NonDeN",
    group = 
"""
1 *1 Cd  u1 {2,S}
2    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cd_rad_in/OneDe",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cs_rad_intra",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "C_pri_rad_intra",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "C_sec_rad_intra",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "C_rad/H/NonDeC_intra",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "C_rad/H/NonDeO_intra",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "C_rad/H/NonDeN_intra",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S}
2    H   u0 {1,S}
3    N3s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "C_rad/H/OneDe_intra",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "C_ter_rad_intra",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "C_rad/NonDeC_intra",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "C_rad/Cs3_intra",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "C_rad/NDMustO_intra",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    O      u0 {1,S}
3    [Cs,O] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "C_rad/OneDe_intra",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cs,O]        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "C_rad/Cs2_intra",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "C_rad/ODMustO_intra",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    O             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "C_rad/TwoDe_intra",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "N_rad",
    group = 
"""
1 *1 N u1
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "SS_intra",
    group = 
"""
1 *2 S      u0 {2,S}
2 *3 [Os,S] ux {1,S}  
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "SS",
    group = "OR{SSJ, SSH, SSR}",
    kinetics = None,
)

entry(
    index = 76,
    label = "SSJ",
    group = 
"""
1 *2 S u0 {2,S}
2 *3 S u1 {1,S}  
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "SSH",
    group = 
"""
1 *2 S u0 {2,S}
2 *3 S u0 {1,S} {3,S}
3    H u0 {2,S}  
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "SSR",
    group = 
"""
1 *2 S   u0 {2,S}
2 *3 S   u0 {1,S} {3,S}
3    R!H u0 {2,S}  
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "SO",
    group = "OR{SOJ, SOH, SOR}",
    kinetics = None,
)

entry(
    index = 76,
    label = "SOJ",
    group = 
"""
1 *2 S  u0 {2,S}
2 *3 Os u1 {1,S}  
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "SOH",
    group = 
"""
1 *2 S  u0 {2,S}
2 *3 Os u0 {1,S} {3,S}
3    H  u0 {2,S}  
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "SOR",
    group = 
"""
1 *2 S   u0 {2,S}
2 *3 Os  u0 {1,S} {3,S}
3    R!H u0 {2,S}  
""",
    kinetics = None,
)

tree(
"""
L1: RnSS
    L2: R2SS
        L3: R2SS_S
            L4: R2SS_SCO
        L3: R2SS_D
    L2: R3SS
        L3: R3SS_SS
            L4: R3SS_SSCO
        L3: R3SS_SD
        L3: R3SS_DS
    L2: R4SS
        L3: R4SS_SSS
            L4: R4SS_SSSCO
        L3: R4SS_SSD
        L3: R4SS_SDS
        L3: R4SS_DSS
        L3: R4SS_DSD
    L2: R5SS
        L3: R5SS_SSSS
            L4: R5SS_SSSSCO
        L3: R5SS_SSSD
        L3: R5SS_SSDS
        L3: R5SS_SDSS
        L3: R5SS_DSSS
        L3: R5SS_SDSD
        L3: R5SS_DSDS
L1: Y_rad_intra
    L2: Cd_rad_out
    L2: Cd_rad_in
        L3: Cd_pri_rad_in
        L3: Cd_sec_rad_in
            L4: Cd_rad_in/NonDeC
            L4: Cd_rad_in/NonDeO
            L4: Cd_rad_in/NonDeN
            L4: Cd_rad_in/OneDe
    L2: Cs_rad_intra
        L3: C_ter_rad_intra
            L4: C_rad/NonDeC_intra
                L5: C_rad/Cs3_intra
                L5: C_rad/NDMustO_intra
            L4: C_rad/OneDe_intra
                L5: C_rad/Cs2_intra
                L5: C_rad/ODMustO_intra
            L4: C_rad/TwoDe_intra
        L3: C_sec_rad_intra
            L4: C_rad/H/NonDeC_intra
            L4: C_rad/H/NonDeO_intra
            L4: C_rad/H/NonDeN_intra
            L4: C_rad/H/OneDe_intra
        L3: C_pri_rad_intra
    L2: N_rad
L1: SS_intra
    L2: SS
        L3: SSJ
        L3: SSH
        L3: SSR
    L2: SO
        L3: SOJ
        L3: SOH
        L3: SOR
"""
)

