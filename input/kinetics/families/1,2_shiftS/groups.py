#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XYSJ"], ownReverse=False)

reverse = "1,2_S_radical_shift"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*3"]

entry(
    index = 1,
    label = "XSYJ",
    group = 
"""
1 *1 C   u0 {2,S}
2 *2 S   u0 {1,S} {3,S}
3 *3 R!H u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "YJ-S2s",
    group = 
"""
1 *3 R!H u1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CJ-S2s",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CdsJ-S2s",
    group = 
"""
1 *3 Cd u1 {2,D}
2    C  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CsJ-S2s",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CsJ-SsHH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CsJ-SsCsH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CsJ-SsCsCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CsJ-SsSsH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "CsJ-SsSsSs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CsJ-SsCsSs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CsJ-SsOneDe",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    R                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CsJ-SsOneDeH",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CsJ-SsCdH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "CsJ-SsOneDeCs",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "CsJ-SsCdCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "CsJ-SsOneDeSs",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "CsJ-SsCdSs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "SJ-S2s",
    group = 
"""
1 *3 S2s u1
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C-S2s",
    group = 
"""
1 *1 C u0
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cb-S2s",
    group = 
"""
1 *1 Cb u0
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Ct-S2s",
    group = 
"""
1 *1 Ct u0 {2,T}
2    C  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cds-S2s",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Cds-SsH",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2    C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Cds-SsCs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Cds-SsCt",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cds-SsCb",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cds-SsCO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cds-SsOs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cds-SsSs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cds-SsCd",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cds-SsC=S",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C=S-S2s",
    group = 
"""
1 *1 CS u0 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C=S-SsH",
    group = 
"""
1 *1 CS u0 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C=S-SsCs",
    group = 
"""
1 *1 CS u0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C=S-SsCt",
    group = 
"""
1 *1 CS u0 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C=S-SsCb",
    group = 
"""
1 *1 CS u0 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C=S-SsCO",
    group = 
"""
1 *1 CS u0 {2,S}
2    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C=S-SsOs",
    group = 
"""
1 *1 CS u0 {2,S}
2    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C=S-SsSs",
    group = 
"""
1 *1 CS u0 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C=S-SsCd",
    group = 
"""
1 *1 CS u0 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C=S-SsC=S",
    group = 
"""
1 *1 CS u0 {2,S}
2    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cs-S2s",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Cs-SsHHH",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Cs-SsCsHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Cs-SsCsCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cs-SsCsCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cs-SsOsHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Cs-SsOsCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Cs-SsOsCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cs-SsOsOsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Os u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cs-SsOsOsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Os u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cs-SsOsOsOs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Os u0 {1,S}
4    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cs-SsSsHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cs-SsSsCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cs-SsSsCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cs-SsSsSsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cs-SsSsSsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cs-SsSsSsSs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cs-SsOneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [H,Cs,Os,S2s]     u0 {1,S}
4    [H,Cs,Os,S2s]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cs-SsOneDeHH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Cs-SsCtHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Cs-SsCbHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Cs-SsCOHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Cs-SsCdHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Cs-SsC=SHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Cs-SsOneDeCsH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Cs-SsCtCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Cs-SsCbCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Cs-SsCOCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Cs-SsCdCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Cs-SsC=SCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cs-SsOneDeOsH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cs-SsOneDeSsH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Cs-SsOneDeCsCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Cs-SsCtCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Cs-SsCbCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Cs-SsCOCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Cs-SsCdCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Cs-SsC=SCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Cs-SsOneDeOsCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Cs-SsOneDeSsCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Cs-SsOneDeOsOs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    Os               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Cs-SsOneDeOsSs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    S2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Cs-SsOneDeSsSs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s               u0 {1,S}
4    S2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Cs-SsTwoDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [H,Cs,Os,S2s]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Cs-SsTwoDeH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Cs-SsCtCtH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Cs-SsCtCbH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Cs-SsCtCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Cs-SsCbCbH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Cs-SsCbCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Cs-SsCOCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Cs-SsCdCtH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Cs-SsCdCbH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Cs-SsCdCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Cs-SsCtC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Cs-SsCbC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Cs-SsCOC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Cs-SsCdCdH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Cs-SsCdC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Cs-SsC=SC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Cs-SsTwoDeCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Cs-SsCtCtCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Cs-SsCtCbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Cs-SsCtCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Cs-SsCbCbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Cs-SsCbCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Cs-SsCOCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Cs-SsCdCtCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Cs-SsCdCbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Cs-SsCdCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Cs-SsCtC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Cs-SsCbC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Cs-SsCOC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Cs-SsCdCdCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Cs-SsCdC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Cs-SsC=SC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Cs-SsTwoDeOs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Os               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Cs-SsTwoDeSs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Cs-SsThreeDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
L1: YJ-S2s
    L2: CJ-S2s
        L3: CdsJ-S2s
        L3: CsJ-S2s
            L4: CsJ-SsOneDe
                L5: CsJ-SsOneDeCs
                    L6: CsJ-SsCdCs
                L5: CsJ-SsOneDeSs
                    L6: CsJ-SsCdSs
                L5: CsJ-SsOneDeH
                    L6: CsJ-SsCdH
            L4: CsJ-SsSsSs
            L4: CsJ-SsCsSs
            L4: CsJ-SsCsCs
            L4: CsJ-SsCsH
            L4: CsJ-SsSsH
            L4: CsJ-SsHH 
    L2: SJ-S2s
L1: C-S2s
    L2: Cb-S2s
    L2: Ct-S2s
    L2: Cds-S2s
        L3: Cds-SsCs
        L3: Cds-SsCt
        L3: Cds-SsCb
        L3: Cds-SsCO
        L3: Cds-SsOs
        L3: Cds-SsSs
        L3: Cds-SsCd
        L3: Cds-SsC=S
        L3: Cds-SsH
    L2: C=S-S2s
        L3: C=S-SsCs
        L3: C=S-SsCt
        L3: C=S-SsCb
        L3: C=S-SsCO
        L3: C=S-SsOs
        L3: C=S-SsSs
        L3: C=S-SsCd
        L3: C=S-SsC=S
        L3: C=S-SsH
    L2: Cs-S2s
        L3: Cs-SsCsCsCs
        L3: Cs-SsOsCsCs
        L3: Cs-SsOsOsCs
        L3: Cs-SsOsOsOs
        L3: Cs-SsSsCsCs
        L3: Cs-SsSsSsCs
        L3: Cs-SsSsSsSs
        L3: Cs-SsThreeDe
        L3: Cs-SsTwoDe
            L4: Cs-SsTwoDeCs
                L5: Cs-SsCtCtCs
                L5: Cs-SsCtCbCs
                L5: Cs-SsCtCOCs
                L5: Cs-SsCbCbCs
                L5: Cs-SsCbCOCs
                L5: Cs-SsCOCOCs
                L5: Cs-SsCdCtCs
                L5: Cs-SsCdCbCs
                L5: Cs-SsCdCOCs
                L5: Cs-SsCtC=SCs
                L5: Cs-SsCbC=SCs
                L5: Cs-SsCOC=SCs
                L5: Cs-SsCdCdCs
                L5: Cs-SsCdC=SCs
                L5: Cs-SsC=SC=SCs
            L4: Cs-SsTwoDeOs
            L4: Cs-SsTwoDeSs
            L4: Cs-SsTwoDeH
                L5: Cs-SsCtCtH
                L5: Cs-SsCtCbH
                L5: Cs-SsCtCOH
                L5: Cs-SsCbCbH
                L5: Cs-SsCbCOH
                L5: Cs-SsCOCOH
                L5: Cs-SsCdCtH
                L5: Cs-SsCdCbH
                L5: Cs-SsCdCOH
                L5: Cs-SsCtC=SH
                L5: Cs-SsCbC=SH
                L5: Cs-SsCOC=SH
                L5: Cs-SsCdCdH
                L5: Cs-SsCdC=SH
                L5: Cs-SsC=SC=SH
        L3: Cs-SsOneDe
            L4: Cs-SsOneDeCsCs
                L5: Cs-SsCtCsCs
                L5: Cs-SsCbCsCs
                L5: Cs-SsCOCsCs
                L5: Cs-SsCdCsCs
                L5: Cs-SsC=SCsCs
            L4: Cs-SsOneDeOsCs
            L4: Cs-SsOneDeSsCs
            L4: Cs-SsOneDeOsOs
            L4: Cs-SsOneDeOsSs
            L4: Cs-SsOneDeSsSs
            L4: Cs-SsOneDeOsH
            L4: Cs-SsOneDeSsH
            L4: Cs-SsOneDeCsH
                L5: Cs-SsCtCsH
                L5: Cs-SsCbCsH
                L5: Cs-SsCOCsH
                L5: Cs-SsCdCsH
                L5: Cs-SsC=SCsH
            L4: Cs-SsOneDeHH
                L5: Cs-SsCtHH
                L5: Cs-SsCbHH
                L5: Cs-SsCOHH
                L5: Cs-SsCdHH
                L5: Cs-SsC=SHH
        L3: Cs-SsCsCsH
        L3: Cs-SsOsOsH
        L3: Cs-SsOsCsH
        L3: Cs-SsSsSsH
        L3: Cs-SsSsCsH
        L3: Cs-SsOsHH
        L3: Cs-SsCsHH
        L3: Cs-SsSsHH
        L3: Cs-SsHHH
        
"""
)

