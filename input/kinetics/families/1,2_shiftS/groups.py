#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XYSJ"], ownReverse=False)

reverse = "1,2_S_radical_shift"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

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
    label = "YJ-Ss",
    group = 
"""
1 *3 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "X-Ss",
    group = "OR{C-Ss}",
    kinetics = None,
)

entry(
    index = 4,
    label = "CJ-Ss",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CdsJ-Ss",
    group = 
"""
1 *3 Cd u1 {2,D}
2    C  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CsJ-Ss",
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
2    Ss u0 {1,S}
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
2    Ss u0 {1,S}
3    Ss u0 {1,S}
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
3    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CsJ-SsOneDe",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    R             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CsJ-SsOneDeH",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
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
3    [Cd,Ct,Cb,CO] u0 {1,S}
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
2    Ss            u0 {1,S}
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
2    Ss u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "SJ-Ss",
    group = 
"""
1 *3 Ss u1
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C-Ss",
    group = 
"""
1 *1 C u0
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cb-Ss",
    group = 
"""
1 *1 Cb u0
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Ct-Ss",
    group = 
"""
1 *1 Ct u0 {2,T}
2    C  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cds-Ss",
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
3    Ss u0 {1,S}
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
3    Cd u0 {1,S} {4,D}
4    Sd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C=S-Ss",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C=S-SsH",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C=S-SsCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C=S-SsCt",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C=S-SsCb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C=S-SsCO",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C=S-SsOs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C=S-SsSs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C=S-SsCd",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C=S-SsC=S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2    Sd u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    Sd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cs-Ss",
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
2    Ss u0 {1,S}
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
2    Ss u0 {1,S}
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
2    Ss u0 {1,S}
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
2    Ss u0 {1,S}
3    Ss u0 {1,S}
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
2    Ss u0 {1,S}
3    Ss u0 {1,S}
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
2    Ss u0 {1,S}
3    Ss u0 {1,S}
4    Ss u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cs-SsOneDe",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [H,Cs,Os,Ss]  u0 {1,S}
4    [H,Cs,Os,Ss]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cs-SsOneDeHH",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    H             u0 {1,S}
4    H             u0 {1,S}
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
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Sd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Cs-SsOneDeCsH",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
4    H             u0 {1,S}
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
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    Sd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cs-SsOneDeOsH",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Os            u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cs-SsOneDeSsH",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Ss            u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Cs-SsOneDeCsCs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
4    Cs            u0 {1,S}
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
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Sd u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Cs-SsOneDeOsCs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Os            u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Cs-SsOneDeSsCs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Ss            u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Cs-SsOneDeOsOs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Os            u0 {1,S}
4    Os            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Cs-SsOneDeOsSs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Os            u0 {1,S}
4    Ss            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Cs-SsOneDeSsSs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Ss            u0 {1,S}
4    Ss            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Cs-SsTwoDe",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,Ss]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Cs-SsTwoDeH",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
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
3    Cd u0 {1,S} {5,D}
4    H  u0 {1,S}
5    Sd u0 {3,D}
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
3    Cd u0 {1,S} {5,D}
4    H  u0 {1,S}
5    Sd u0 {3,D}
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
3    Cd u0 {1,S} {5,D}
4    H  u0 {1,S}
5    Sd u0 {3,D}
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
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    Sd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Cs-SsC=SC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    Sd u0 {2,D}
6    Sd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Cs-SsTwoDeCs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
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
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    Sd u0 {3,D}
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
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    Sd u0 {3,D}
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
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    Sd u0 {3,D}
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
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    Sd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Cs-SsC=SC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    Sd u0 {2,D}
6    Sd u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Cs-SsTwoDeOs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Os            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Cs-SsTwoDeSs",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Ss            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Cs-SsThreeDe",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
L1: YJ-Ss
    L2: CJ-Ss
        L3: CdsJ-Ss
        L3: CsJ-Ss
            L4: CsJ-SsHH
            L4: CsJ-SsCsH
            L4: CsJ-SsCsCs
            L4: CsJ-SsSsH
            L4: CsJ-SsSsSs
            L4: CsJ-SsCsSs
            L4: CsJ-SsOneDe
                L5: CsJ-SsOneDeH
                    L6: CsJ-SsCdH
                L5: CsJ-SsOneDeCs
                    L6: CsJ-SsCdCs
                L5: CsJ-SsOneDeSs
                    L6: CsJ-SsCdSs
    L2: SJ-Ss
L1: X-Ss
    L2: C-Ss
        L3: Cb-Ss
        L3: Ct-Ss
        L3: Cds-Ss
            L4: Cds-SsH
            L4: Cds-SsCs
            L4: Cds-SsCt
            L4: Cds-SsCb
            L4: Cds-SsCO
            L4: Cds-SsOs
            L4: Cds-SsSs
            L4: Cds-SsCd
            L4: Cds-SsC=S
        L3: C=S-Ss
            L4: C=S-SsH
            L4: C=S-SsCs
            L4: C=S-SsCt
            L4: C=S-SsCb
            L4: C=S-SsCO
            L4: C=S-SsOs
            L4: C=S-SsSs
            L4: C=S-SsCd
            L4: C=S-SsC=S
        L3: Cs-Ss
            L4: Cs-SsHHH
            L4: Cs-SsCsHH
            L4: Cs-SsCsCsH
            L4: Cs-SsCsCsCs
            L4: Cs-SsOsHH
            L4: Cs-SsOsCsH
            L4: Cs-SsOsCsCs
            L4: Cs-SsOsOsH
            L4: Cs-SsOsOsCs
            L4: Cs-SsOsOsOs
            L4: Cs-SsSsHH
            L4: Cs-SsSsCsH
            L4: Cs-SsSsCsCs
            L4: Cs-SsSsSsH
            L4: Cs-SsSsSsCs
            L4: Cs-SsSsSsSs
            L4: Cs-SsOneDe
                L5: Cs-SsOneDeHH
                    L6: Cs-SsCtHH
                    L6: Cs-SsCbHH
                    L6: Cs-SsCOHH
                    L6: Cs-SsCdHH
                    L6: Cs-SsC=SHH
                L5: Cs-SsOneDeCsH
                    L6: Cs-SsCtCsH
                    L6: Cs-SsCbCsH
                    L6: Cs-SsCOCsH
                    L6: Cs-SsCdCsH
                    L6: Cs-SsC=SCsH
                L5: Cs-SsOneDeOsH
                L5: Cs-SsOneDeSsH
                L5: Cs-SsOneDeCsCs
                    L6: Cs-SsCtCsCs
                    L6: Cs-SsCbCsCs
                    L6: Cs-SsCOCsCs
                    L6: Cs-SsCdCsCs
                    L6: Cs-SsC=SCsCs
                L5: Cs-SsOneDeOsCs
                L5: Cs-SsOneDeSsCs
                L5: Cs-SsOneDeOsOs
                L5: Cs-SsOneDeOsSs
                L5: Cs-SsOneDeSsSs
            L4: Cs-SsTwoDe
                L5: Cs-SsTwoDeH
                    L6: Cs-SsCtCtH
                    L6: Cs-SsCtCbH
                    L6: Cs-SsCtCOH
                    L6: Cs-SsCbCbH
                    L6: Cs-SsCbCOH
                    L6: Cs-SsCOCOH
                    L6: Cs-SsCdCtH
                    L6: Cs-SsCdCbH
                    L6: Cs-SsCdCOH
                    L6: Cs-SsCtC=SH
                    L6: Cs-SsCbC=SH
                    L6: Cs-SsCOC=SH
                    L6: Cs-SsCdCdH
                    L6: Cs-SsCdC=SH
                    L6: Cs-SsC=SC=SH
                L5: Cs-SsTwoDeCs
                    L6: Cs-SsCtCtCs
                    L6: Cs-SsCtCbCs
                    L6: Cs-SsCtCOCs
                    L6: Cs-SsCbCbCs
                    L6: Cs-SsCbCOCs
                    L6: Cs-SsCOCOCs
                    L6: Cs-SsCdCtCs
                    L6: Cs-SsCdCbCs
                    L6: Cs-SsCdCOCs
                    L6: Cs-SsCtC=SCs
                    L6: Cs-SsCbC=SCs
                    L6: Cs-SsCOC=SCs
                    L6: Cs-SsCdCdCs
                    L6: Cs-SsCdC=SCs
                    L6: Cs-SsC=SC=SCs
                L5: Cs-SsTwoDeOs
                L5: Cs-SsTwoDeSs
            L4: Cs-SsThreeDe
"""
)

