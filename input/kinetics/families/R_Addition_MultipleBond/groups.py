#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["R_R", "YJ"], products=["RJ_R_Y"], ownReverse=False)

reverse = "Beta_Scission"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "R_R",
    group = "OR{Cd_R, Ct_R, Od_R, Sd_R, Nd_R, Nt_R}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "YJ",
    group = "OR{HJ, CJ, OJ, SJ, NJ, Y_1centerbirad, Y_1centertrirad, Y_1centerquadrad}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Cd_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 C U0 {2,D}
2 *2 R U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Cdd_Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D}
2 *2 Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CO2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Ck_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    C   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C=S_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    S   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CO_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U0 {2,D}
2 *2 Od U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CO/H2_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U0 {2,D} {3,S} {4,S}
2 *2 Od U0 {1,D}
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
    index = 10,
    label = "CO/H/Nd_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO     U0 {2,D} {3,S} {4,S}
2 *2 Od     U0 {1,D}
3    H      U0 {1,S}
4    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CO/H/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO U0 {2,D} {3,S} {4,S}
2 *2 Od U0 {1,D}
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
    index = 12,
    label = "CO/H/De_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO                    U0 {2,D} {3,S} {4,S}
2 *2 Od                    U0 {1,D}
3    H                     U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CO/Nd2_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO     U0 {2,D} {3,S} {4,S}
2 *2 Od     U0 {1,D}
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
    index = 14,
    label = "CO/Nd/De_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO                    U0 {2,D} {3,S} {4,S}
2 *2 Od                    U0 {1,D}
3    {Cs,O}                U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CO/De2_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 CO                    U0 {2,D} {3,S} {4,S}
2 *2 Od                    U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "Cds_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D}
2 *2 N  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "Cds_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D}
2 *2 N3d U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "Cds-HH_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 N3d U0 {1,D}
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
    index = 309,
    label = "Cds-NonDeH_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                 U0 {2,D} {3,S} {4,S}
2 *2 N3d                U0 {1,D}
3    H                  U0 {1,S}
4    {Cs,Os,N3s,N5s,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "Cds-NonDe2_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                 U0 {2,D} {3,S} {4,S}
2 *2 N3d                U0 {1,D}
3    {Cs,Os,N3s,N5s,Ss} U0 {1,S}
4    {Cs,Os,N3s,N5s,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Cdd_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Sd  U0 {1,D}
3    R   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "Cdd-Sd_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Sd  U0 {1,D}
3    Sd  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "Cds_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0       {2,D} {3,S} {4,S}
2 *2 Cdd U0       {1,D}
3    R   U{0,1,2} {1,S}
4    R   U{0,1,2} {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "Cds_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0       {2,D} {3,S} {4,S}
2 *2 Cdd U0       {1,D} {5,D}
3    R   U{0,1,2} {1,S}
4    R   U{0,1,2} {1,S}
5    C   U0       {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "Cds-HH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Cds-CsH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    Cs  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "Cds-CsCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    Cs  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Cds-OneDeH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cdd                   U0 {1,D} {5,D}
3    H                     U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    C                     U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Cds-CtH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    Ct  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Cds-CbH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    Cb  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Cds-COH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    CO  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Cds-CdH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cds-C=SH_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Cds-OneDeCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cdd                   U0 {1,D} {5,D}
3    Cs                    U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    C                     U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cds-CtCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    Ct  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Cds-CbCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    Cb  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Cds-COCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    CO  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Cds-CdCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "Cds-C=SCs_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Cds-TwoDe_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cdd                   U0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    C                     U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "Cds-CtCt_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Ct  U0 {1,S}
4    Ct  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "Cds-CtCb_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Ct  U0 {1,S}
4    Cb  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cds-CtCO_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Ct  U0 {1,S}
4    CO  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "Cds-CbCb_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cb  U0 {1,S}
4    Cb  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "Cds-CbCO_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cb  U0 {1,S}
4    CO  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cds-COCO_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    CO  U0 {1,S}
4    CO  U0 {1,S}
5    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "Cds-CdCt_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cd  U0 {1,S} {6,D}
4    Ct  U0 {1,S}
5    C   U0 {2,D}
6    C   U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "Cds-CdCb_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cd  U0 {1,S} {6,D}
4    Cb  U0 {1,S}
5    C   U0 {2,D}
6    C   U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "Cds-CdCO_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cd  U0 {1,S} {6,D}
4    CO  U0 {1,S}
5    C   U0 {2,D}
6    C   U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "Cds-CtC=S_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Ct  U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cds-CbC=S_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cb  U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "Cds-COC=S_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    CO  U0 {1,S}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "Cds-CdCd_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    C   U0 {2,D}
6    C   U0 {3,D}
7    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "Cds-CdC=S_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {6,D}
5    C   U0 {2,D}
6    Sd  U0 {4,D}
7    C   U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "Cds-C=SC=S_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    C   U0 {2,D}
6    Sd  U0 {3,D}
7    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "Cds_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0       {2,D} {3,S} {4,S}
2 *2 Cdd U0       {1,D} {5,D}
3    R   U{0,1,2} {1,S}
4    R   U{0,1,2} {1,S}
5    Od  U0       {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "Cds-HH_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "Cds-CsH_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    H   U0 {1,S}
4    Cs  U0 {1,S}
5    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "Cds-CsCs_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd  U0 {2,D} {3,S} {4,S}
2 *2 Cdd U0 {1,D} {5,D}
3    Cs  U0 {1,S}
4    Cs  U0 {1,S}
5    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Cds-OneDeH_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cdd                   U0 {1,D} {5,D}
3    H                     U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    Od                    U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "Cds-OneDeCs_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cdd                   U0 {1,D} {5,D}
3    Cs                    U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    Od                    U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "Cds-TwoDe_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cdd                   U0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    Od                    U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "Cdd_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D}
2 *2 Cd  U0 {1,D} {3,S} {4,S}
3    R   U0 {2,S}
4    R   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "Ca_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    R   U0 {2,S}
5    R   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Ca_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    H   U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "Ca_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cs  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "Ca_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cs  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "Ca_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd                   U0 {2,D} {3,D}
2 *2 Cd                    U0 {1,D} {4,S} {5,S}
3    C                     U0 {1,D}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
5    H                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "Ca_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Ct  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Ca_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cb  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "Ca_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    CO  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "Ca_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    H   U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Ca_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    H   U0 {2,S}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Ca_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd                   U0 {2,D} {3,D}
2 *2 Cd                    U0 {1,D} {4,S} {5,S}
3    C                     U0 {1,D}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
5    Cs                    U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "Ca_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Ct  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "Ca_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cb  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "Ca_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    CO  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "Ca_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cs  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "Ca_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cs  U0 {2,S}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "Ca_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd                   U0 {2,D} {3,D}
2 *2 Cd                    U0 {1,D} {4,S} {5,S}
3    C                     U0 {1,D}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "Ca_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Ct  U0 {2,S}
5    Ct  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "Ca_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Ct  U0 {2,S}
5    Cb  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "Ca_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Ct  U0 {2,S}
5    CO  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "Ca_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cb  U0 {2,S}
5    Cb  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "Ca_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cb  U0 {2,S}
5    CO  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "Ca_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    CO  U0 {2,S}
5    CO  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "Ca_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Ct  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "Ca_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cb  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "Ca_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    CO  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "Ca_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Ct  U0 {2,S}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Ca_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cb  U0 {2,S}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "Ca_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    CO  U0 {2,S}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "Ca_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cd  U0 {2,S} {7,D}
6    C   U0 {4,D}
7    C   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "Ca_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {7,D}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
7    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Ca_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    C   U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cd  U0 {2,S} {7,D}
6    Sd  U0 {4,D}
7    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "Ck_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    R   U0 {2,S}
5    R   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Ck_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    H   U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "Ck_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cs  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "Ck_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cs  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "Ck_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd                   U0 {2,D} {3,D}
2 *2 Cd                    U0 {1,D} {4,S} {5,S}
3    Od                    U0 {1,D}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
5    H                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "Ck_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Ct  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "Ck_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cb  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "Ck_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    CO  U0 {2,S}
5    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "Ck_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    H   U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "Ck_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    H   U0 {2,S}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "Ck_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd                   U0 {2,D} {3,D}
2 *2 Cd                    U0 {1,D} {4,S} {5,S}
3    Od                    U0 {1,D}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
5    Cs                    U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "Ck_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Ct  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "Ck_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cb  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "Ck_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    CO  U0 {2,S}
5    Cs  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "Ck_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cs  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "Ck_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cs  U0 {2,S}
6    Sd  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "Ck_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd                   U0 {2,D} {3,D}
2 *2 Cd                    U0 {1,D} {4,S} {5,S}
3    Od                    U0 {1,D}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "Ck_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Ct  U0 {2,S}
5    Ct  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "Ck_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Ct  U0 {2,S}
5    Cb  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "Ck_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Ct  U0 {2,S}
5    CO  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "Ck_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cb  U0 {2,S}
5    Cb  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "Ck_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cb  U0 {2,S}
5    CO  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "Ck_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    CO  U0 {2,S}
5    CO  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "Ck_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Ct  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "Ck_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cb  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "Ck_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    CO  U0 {2,S}
6    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "Ck_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Ct  U0 {2,S}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "Ck_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cb  U0 {2,S}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "Ck_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    CO  U0 {2,S}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "Ck_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cd  U0 {2,S} {7,D}
6    C   U0 {4,D}
7    C   U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "Ck_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {7,D}
5    Cd  U0 {2,S} {6,D}
6    Sd  U0 {5,D}
7    C   U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "Ck_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cd  U0 {1,D} {4,S} {5,S}
3    Od  U0 {1,D}
4    Cd  U0 {2,S} {6,D}
5    Cd  U0 {2,S} {7,D}
6    Sd  U0 {4,D}
7    Sd  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "Cdd_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cdd U0 {1,D} {4,D}
3    R   U0 {1,D}
4    R   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "Ca_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cdd U0 {1,D} {4,D}
3    C   U0 {1,D}
4    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "Ck_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cdd U0 {1,D} {4,D}
3    Od  U0 {1,D}
4    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "Ca_Ck",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cdd U0 {1,D} {4,D}
3    C   U0 {1,D}
4    Od  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "Ck_Ca",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Cdd U0 {1,D} {4,D}
3    Od  U0 {1,D}
4    C   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "Cds_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0       {2,D} {3,S} {4,S}
2 *2 Sd U0       {1,D}
3    R  U{0,1,2} {1,S}
4    R  U{0,1,2} {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "Cds-HH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 130,
    label = "Cds-CsH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "Cds-CsCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 132,
    label = "Cds-OsH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Os U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "Cds-OsCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Os U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "Cds-SsH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Ss U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "Cds-SsCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Ss U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "Cds-OneDeH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Sd                    U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "Cds-CtH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Ct U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "Cds-CbH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cb U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "Cds-COH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "Cds-CdH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "Cds-C=SH_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "Cds-OneDeCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Sd                    U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Cs                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "Cds-CtCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 144,
    label = "Cds-CbCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 145,
    label = "Cds-COCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 146,
    label = "Cds-CdCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
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
    index = 147,
    label = "Cds-C=SCs_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "Cds-TwoDe_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Sd                    U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "Cds-CtCt_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 150,
    label = "Cds-CtCb_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 151,
    label = "Cds-CtCO_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 152,
    label = "Cds-CbCb_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 153,
    label = "Cds-CbCO_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 154,
    label = "Cds-COCO_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
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
    index = 155,
    label = "Cds-CdCt_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
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
    index = 156,
    label = "Cds-CdCb_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
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
    index = 157,
    label = "Cds-CdCO_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
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
    index = 158,
    label = "Cds-CtC=S_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Ct U0 {1,S}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "Cds-CbC=S_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cb U0 {1,S}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "Cds-COC=S_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    CO U0 {1,S}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "Cds-CdCd_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
4    Cd U0 {1,S} {6,D}
5    C  U0 {3,D}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "Cds-CdC=S_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {6,D}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "Cds-C=SC=S_Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Sd U0 {1,D}
3    Cd U0 {1,S} {5,D}
4    Cd U0 {1,S} {6,D}
5    Sd U0 {3,D}
6    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "Cds_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0       {2,D} {3,S} {4,S}
2 *2 Cd U0       {1,D} {5,S} {6,S}
3    R  U{0,1,2} {1,S}
4    R  U{0,1,2} {1,S}
5    R  U0       {2,S}
6    R  U0       {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "Cds-HH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "Cds-HH_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "Cds-HH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "Cds-HH_Cds-Cs\Os/H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S} {7,S}
6    H  U0 {2,S}
7    Os U0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "Cds-HH_Cds-Cs\H3/H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    C U0 {2,S} {4,S} {5,S} {6,S}
2 *2 C U0 {1,S} {3,D} {7,S}
3 *1 C U0 {2,D} {8,S} {9,S}
4    H U0 {1,S}
5    H U0 {1,S}
6    H U0 {1,S}
7    H U0 {2,S}
8    H U0 {3,S}
9    H U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "Cds-HH_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "Cds-HH_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "Cds-HH_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "Cds-HH_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "Cds-HH_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "Cds-HH_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "Cds-HH_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "Cds-HH_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "Cds-HH_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "Cds-HH_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "Cds-HH_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "Cds-HH_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "Cds-HH_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "Cds-HH_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "Cds-HH_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "Cds-HH_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "Cds-HH_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "Cds-HH_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "Cds-HH_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "Cds-HH_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "Cds-HH_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "Cds-HH_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "Cds-HH_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "Cds-HH_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "Cds-HH_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "Cds-HH_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "Cds-HH_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "Cds-HH_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "Cds-HH_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "Cds-HH_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "Cds-HH_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "Cds-HH_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "Cds-HH_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "Cds-HH_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "Cds-HH_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "Cds-HH_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "Cds-HH_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "Cds-HH_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "Cds-HH_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "Cds-HH_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "Cds-HH_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "Cds-HH_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "Cds-HH_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "Cds-HH_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "Cds-HH_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "Cds-HH_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "Cds-HH_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "Cds-HH_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "Cds-HH_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "Cds-CsH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "Cds-CsH_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "Cds-Cs\Os/H_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S} {7,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    Os U0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "Cds-CsH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "Cds-CsH_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "Cds-CsH_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "Cds-CsH_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "Cds-CsH_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "Cds-CsH_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "Cds-CsH_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "Cds-CsH_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "Cds-CsH_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "Cds-CsH_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "Cds-CsH_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "Cds-CsH_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "Cds-CsH_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "Cds-CsH_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "Cds-CsH_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "Cds-CsH_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "Cds-CsH_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "Cds-CsH_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "Cds-CsH_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "Cds-CsH_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "Cds-CsH_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "Cds-CsH_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "Cds-CsH_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "Cds-CsH_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "Cds-CsH_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "Cds-CsH_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "Cds-CsH_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "Cds-CsH_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "Cds-CsH_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "Cds-CsH_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "Cds-CsH_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "Cds-CsH_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "Cds-CsH_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "Cds-CsH_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "Cds-CsH_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "Cds-CsH_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "Cds-CsH_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "Cds-CsH_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "Cds-CsH_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "Cds-CsH_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "Cds-CsH_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "Cds-CsH_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "Cds-CsH_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "Cds-CsH_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "Cds-CsH_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "Cds-CsH_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "Cds-CsH_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "Cds-CsH_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "Cds-CsH_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "Cds-CsH_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "Cds-CsCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "Cds-CsCs_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "Cds-CsCs_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "Cds-CsCs_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "Cds-CsCs_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "Cds-CsCs_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "Cds-CsCs_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "Cds-CsCs_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "Cds-CsCs_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "Cds-CsCs_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "Cds-CsCs_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "Cds-CsCs_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "Cds-CsCs_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "Cds-CsCs_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "Cds-CsCs_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "Cds-CsCs_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "Cds-CsCs_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "Cds-CsCs_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "Cds-CsCs_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "Cds-CsCs_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "Cds-CsCs_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "Cds-CsCs_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "Cds-CsCs_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "Cds-CsCs_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "Cds-CsCs_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "Cds-CsCs_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "Cds-CsCs_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    label = "Cds-CsCs_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "Cds-CsCs_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "Cds-CsCs_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "Cds-CsCs_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "Cds-CsCs_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "Cds-CsCs_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "Cds-CsCs_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "Cds-CsCs_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "Cds-CsCs_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "Cds-CsCs_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "Cds-CsCs_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "Cds-CsCs_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "Cds-CsCs_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "Cds-CsCs_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "Cds-CsCs_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "Cds-CsCs_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "Cds-CsCs_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "Cds-CsCs_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "Cds-CsCs_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "Cds-CsCs_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "Cds-CsCs_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "Cds-CsCs_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "Cds-CsCs_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "Cds-CsCs_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "Cds-CsCs_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "Cds-SsH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "Cds-SsCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ss U0 {1,S}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "Cds-SsSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "Cds-OsH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Os U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "Cds-OsH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Os U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 329,
    label = "Cds-OsCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Os U0 {1,S}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "Cds-OsOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Os U0 {1,S}
4    Os U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "Cds-OsSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Os U0 {1,S}
4    Ss U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "Cds-OneDe_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    R                     U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "Cds-OneDeH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    H                     U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "Cds-CtH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "Cds-CtH_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "Cds-CtH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "Cds-CtH_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "Cds-CtH_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "Cds-CtH_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "Cds-CtH_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "Cds-CtH_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "Cds-CtH_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "Cds-CtH_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "Cds-CtH_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 345,
    label = "Cds-CtH_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    H                     U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "Cds-CtH_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    H                     U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "Cds-CtH_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "Cds-CtH_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 349,
    label = "Cds-CtH_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "Cds-CtH_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "Cds-CtH_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "Cds-CtH_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    H                     U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "Cds-CtH_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "Cds-CtH_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "Cds-CtH_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "Cds-CtH_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "Cds-CtH_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "Cds-CtH_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    H                     U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "Cds-CtH_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "Cds-CtH_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 361,
    label = "Cds-CtH_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "Cds-CtH_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "Cds-CtH_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "Cds-CtH_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    H                     U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "Cds-CtH_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "Cds-CtH_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "Cds-CtH_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "Cds-CtH_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "Cds-CtH_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "Cds-CtH_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    H                     U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "Cds-CtH_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "Cds-CtH_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "Cds-CtH_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "Cds-CtH_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "Cds-CtH_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "Cds-CtH_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "Cds-CtH_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 378,
    label = "Cds-CtH_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "Cds-CtH_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 380,
    label = "Cds-CtH_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 381,
    label = "Cds-CtH_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 382,
    label = "Cds-CtH_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 383,
    label = "Cds-CtH_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 384,
    label = "Cds-CtH_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 385,
    label = "Cds-CtH_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 386,
    label = "Cds-CbH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 387,
    label = "Cds-CbH_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 388,
    label = "Cds-CbH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 389,
    label = "Cds-CbH_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 390,
    label = "Cds-CbH_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 391,
    label = "Cds-CbH_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 392,
    label = "Cds-CbH_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 393,
    label = "Cds-CbH_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 394,
    label = "Cds-CbH_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 395,
    label = "Cds-CbH_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 396,
    label = "Cds-CbH_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 397,
    label = "Cds-CbH_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    H                     U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 398,
    label = "Cds-CbH_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    H                     U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 399,
    label = "Cds-CbH_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 400,
    label = "Cds-CbH_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 401,
    label = "Cds-CbH_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 402,
    label = "Cds-CbH_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 403,
    label = "Cds-CbH_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 404,
    label = "Cds-CbH_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    H                     U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 405,
    label = "Cds-CbH_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 406,
    label = "Cds-CbH_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 407,
    label = "Cds-CbH_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 408,
    label = "Cds-CbH_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "Cds-CbH_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 410,
    label = "Cds-CbH_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    H                     U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "Cds-CbH_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 412,
    label = "Cds-CbH_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 413,
    label = "Cds-CbH_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 414,
    label = "Cds-CbH_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 415,
    label = "Cds-CbH_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 416,
    label = "Cds-CbH_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    H                     U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "Cds-CbH_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "Cds-CbH_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "Cds-CbH_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 420,
    label = "Cds-CbH_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 421,
    label = "Cds-CbH_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 422,
    label = "Cds-CbH_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    H                     U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 423,
    label = "Cds-CbH_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 424,
    label = "Cds-CbH_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 425,
    label = "Cds-CbH_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 426,
    label = "Cds-CbH_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 427,
    label = "Cds-CbH_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 428,
    label = "Cds-CbH_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 429,
    label = "Cds-CbH_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 430,
    label = "Cds-CbH_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 431,
    label = "Cds-CbH_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 432,
    label = "Cds-CbH_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 433,
    label = "Cds-CbH_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 434,
    label = "Cds-CbH_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 435,
    label = "Cds-CbH_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 436,
    label = "Cds-CbH_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 437,
    label = "Cds-CbH_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 438,
    label = "Cds-COH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 439,
    label = "Cds-CdH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 440,
    label = "Cds-CdH_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 441,
    label = "Cds-CdH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 442,
    label = "Cds-CdH_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 443,
    label = "Cds-CdH_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 444,
    label = "Cds-CdH_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 445,
    label = "Cds-CdH_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 446,
    label = "Cds-CdH_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 447,
    label = "Cds-CdH_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 448,
    label = "Cds-CdH_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 449,
    label = "Cds-CdH_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 450,
    label = "Cds-CdH_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    H                     U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 451,
    label = "Cds-CdH_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    H                     U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 452,
    label = "Cds-CdH_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 453,
    label = "Cds-CdH_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 454,
    label = "Cds-CdH_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 455,
    label = "Cds-CdH_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 456,
    label = "Cds-CdH_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 457,
    label = "Cds-CdH_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    H                     U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 458,
    label = "Cds-CdH_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 459,
    label = "Cds-CdH_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 460,
    label = "Cds-CdH_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 461,
    label = "Cds-CdH_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 462,
    label = "Cds-CdH_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 463,
    label = "Cds-CdH_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    H                     U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 464,
    label = "Cds-CdH_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 465,
    label = "Cds-CdH_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 466,
    label = "Cds-CdH_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 467,
    label = "Cds-CdH_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 468,
    label = "Cds-CdH_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 469,
    label = "Cds-CdH_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    H                     U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 470,
    label = "Cds-CdH_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 471,
    label = "Cds-CdH_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 472,
    label = "Cds-CdH_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 473,
    label = "Cds-CdH_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 474,
    label = "Cds-CdH_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 475,
    label = "Cds-CdH_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    H                     U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 476,
    label = "Cds-CdH_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 477,
    label = "Cds-CdH_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 478,
    label = "Cds-CdH_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 479,
    label = "Cds-CdH_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 480,
    label = "Cds-CdH_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 481,
    label = "Cds-CdH_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "Cds-CdH_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 483,
    label = "Cds-CdH_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 484,
    label = "Cds-CdH_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 485,
    label = "Cds-CdH_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 486,
    label = "Cds-CdH_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "Cds-CdH_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 488,
    label = "Cds-CdH_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    H  U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {5,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 489,
    label = "Cds-CdH_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    H  U0 {1,S}
5    Cd U0 {2,S} {9,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 490,
    label = "Cds-CdH_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {9,D}
4    H  U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
9    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 491,
    label = "Cds-C=SH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 492,
    label = "Cds-OneDeCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Cs                    U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 493,
    label = "Cds-CtCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 494,
    label = "Cds-CtCs_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 495,
    label = "Cds-CtCs_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 496,
    label = "Cds-CtCs_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 497,
    label = "Cds-CtCs_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 498,
    label = "Cds-CtCs_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 499,
    label = "Cds-CtCs_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 500,
    label = "Cds-CtCs_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 501,
    label = "Cds-CtCs_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 502,
    label = "Cds-CtCs_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 503,
    label = "Cds-CtCs_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 504,
    label = "Cds-CtCs_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Cs                    U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 505,
    label = "Cds-CtCs_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Cs                    U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 506,
    label = "Cds-CtCs_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 507,
    label = "Cds-CtCs_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 508,
    label = "Cds-CtCs_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 509,
    label = "Cds-CtCs_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 510,
    label = "Cds-CtCs_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 511,
    label = "Cds-CtCs_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 512,
    label = "Cds-CtCs_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 513,
    label = "Cds-CtCs_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 514,
    label = "Cds-CtCs_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 515,
    label = "Cds-CtCs_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 516,
    label = "Cds-CtCs_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 517,
    label = "Cds-CtCs_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 518,
    label = "Cds-CtCs_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 519,
    label = "Cds-CtCs_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 520,
    label = "Cds-CtCs_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 521,
    label = "Cds-CtCs_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 522,
    label = "Cds-CtCs_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 523,
    label = "Cds-CtCs_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 524,
    label = "Cds-CtCs_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 525,
    label = "Cds-CtCs_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 526,
    label = "Cds-CtCs_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 527,
    label = "Cds-CtCs_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 528,
    label = "Cds-CtCs_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 529,
    label = "Cds-CtCs_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Cs                    U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 530,
    label = "Cds-CtCs_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 531,
    label = "Cds-CtCs_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 532,
    label = "Cds-CtCs_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 533,
    label = "Cds-CtCs_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 534,
    label = "Cds-CtCs_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 535,
    label = "Cds-CtCs_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 536,
    label = "Cds-CtCs_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 537,
    label = "Cds-CtCs_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 538,
    label = "Cds-CtCs_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 539,
    label = "Cds-CtCs_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 540,
    label = "Cds-CtCs_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 541,
    label = "Cds-CtCs_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 542,
    label = "Cds-CtCs_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 543,
    label = "Cds-CtCs_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 544,
    label = "Cds-CtCs_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 545,
    label = "Cds-CbCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 546,
    label = "Cds-CbCs_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 547,
    label = "Cds-CbCs_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 548,
    label = "Cds-CbCs_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 549,
    label = "Cds-CbCs_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 550,
    label = "Cds-CbCs_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 551,
    label = "Cds-CbCs_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 552,
    label = "Cds-CbCs_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 553,
    label = "Cds-CbCs_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 554,
    label = "Cds-CbCs_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 555,
    label = "Cds-CbCs_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 556,
    label = "Cds-CbCs_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    Cs                    U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 557,
    label = "Cds-CbCs_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    Cs                    U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 558,
    label = "Cds-CbCs_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 559,
    label = "Cds-CbCs_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 560,
    label = "Cds-CbCs_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 561,
    label = "Cds-CbCs_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 562,
    label = "Cds-CbCs_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 563,
    label = "Cds-CbCs_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 564,
    label = "Cds-CbCs_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 565,
    label = "Cds-CbCs_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 566,
    label = "Cds-CbCs_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 567,
    label = "Cds-CbCs_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 568,
    label = "Cds-CbCs_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 569,
    label = "Cds-CbCs_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 570,
    label = "Cds-CbCs_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 571,
    label = "Cds-CbCs_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 572,
    label = "Cds-CbCs_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 573,
    label = "Cds-CbCs_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 574,
    label = "Cds-CbCs_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 575,
    label = "Cds-CbCs_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    Cs                    U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 576,
    label = "Cds-CbCs_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 577,
    label = "Cds-CbCs_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 578,
    label = "Cds-CbCs_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 579,
    label = "Cds-CbCs_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 580,
    label = "Cds-CbCs_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 581,
    label = "Cds-CbCs_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cb                    U0 {1,S}
4    Cs                    U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 582,
    label = "Cds-CbCs_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 583,
    label = "Cds-CbCs_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 584,
    label = "Cds-CbCs_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 585,
    label = "Cds-CbCs_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 586,
    label = "Cds-CbCs_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 587,
    label = "Cds-CbCs_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 588,
    label = "Cds-CbCs_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 589,
    label = "Cds-CbCs_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 590,
    label = "Cds-CbCs_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 591,
    label = "Cds-CbCs_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 592,
    label = "Cds-CbCs_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 593,
    label = "Cds-CbCs_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 594,
    label = "Cds-CbCs_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 595,
    label = "Cds-CbCs_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 596,
    label = "Cds-CbCs_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 597,
    label = "Cds-COCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    CO U0 {1,S}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 598,
    label = "Cds-CdCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 599,
    label = "Cds-CdCs_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 600,
    label = "Cds-CdCs_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 601,
    label = "Cds-CdCs_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 602,
    label = "Cds-CdCs_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 603,
    label = "Cds-CdCs_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 604,
    label = "Cds-CdCs_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 605,
    label = "Cds-CdCs_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 606,
    label = "Cds-CdCs_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 607,
    label = "Cds-CdCs_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 608,
    label = "Cds-CdCs_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 609,
    label = "Cds-CdCs_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cs                    U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 610,
    label = "Cds-CdCs_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cs                    U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 611,
    label = "Cds-CdCs_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 612,
    label = "Cds-CdCs_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 613,
    label = "Cds-CdCs_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 614,
    label = "Cds-CdCs_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 615,
    label = "Cds-CdCs_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 616,
    label = "Cds-CdCs_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cs                    U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 617,
    label = "Cds-CdCs_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 618,
    label = "Cds-CdCs_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 619,
    label = "Cds-CdCs_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 620,
    label = "Cds-CdCs_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 621,
    label = "Cds-CdCs_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 622,
    label = "Cds-CdCs_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cs                    U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 623,
    label = "Cds-CdCs_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 624,
    label = "Cds-CdCs_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 625,
    label = "Cds-CdCs_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 626,
    label = "Cds-CdCs_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 627,
    label = "Cds-CdCs_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 628,
    label = "Cds-CdCs_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cs                    U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 629,
    label = "Cds-CdCs_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 630,
    label = "Cds-CdCs_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 631,
    label = "Cds-CdCs_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 632,
    label = "Cds-CdCs_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 633,
    label = "Cds-CdCs_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 634,
    label = "Cds-CdCs_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cs                    U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 635,
    label = "Cds-CdCs_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 636,
    label = "Cds-CdCs_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 637,
    label = "Cds-CdCs_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 638,
    label = "Cds-CdCs_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 639,
    label = "Cds-CdCs_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 640,
    label = "Cds-CdCs_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 641,
    label = "Cds-CdCs_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 642,
    label = "Cds-CdCs_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 643,
    label = "Cds-CdCs_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 644,
    label = "Cds-CdCs_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 645,
    label = "Cds-CdCs_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 646,
    label = "Cds-CdCs_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 647,
    label = "Cds-CdCs_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {5,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 648,
    label = "Cds-CdCs_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {9,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 649,
    label = "Cds-CdCs_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {9,D}
4    Cs U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
9    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 650,
    label = "Cds-C=SCs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 651,
    label = "Cds-OneDeSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Ss                    U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 652,
    label = "Cds-CtSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ss U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 653,
    label = "Cds-CbSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Ss U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 654,
    label = "Cds-COSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    CO U0 {1,S}
4    Ss U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 655,
    label = "Cds-CdSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ss U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 656,
    label = "Cds-C=SSs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Cd U0 {1,S} {5,D}
4    Ss U0 {1,S}
5    Sd U0 {3,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 657,
    label = "Cds-OneDeOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Os                    U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 658,
    label = "Cds-CtOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Os U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 659,
    label = "Cds-CbOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Os U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 660,
    label = "Cds-COOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    CO U0 {1,S}
4    Os U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 661,
    label = "Cds-CdOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Os U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 662,
    label = "Cds-C=SOs_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Cd U0 {1,S} {5,D}
4    Os U0 {1,S}
5    Sd U0 {3,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 663,
    label = "Cds-TwoDe_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 664,
    label = "Cds-CtCt_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 665,
    label = "Cds-CtCt_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 666,
    label = "Cds-CtCt_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 667,
    label = "Cds-CtCt_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 668,
    label = "Cds-CtCt_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 669,
    label = "Cds-CtCt_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 670,
    label = "Cds-CtCt_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 671,
    label = "Cds-CtCt_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 672,
    label = "Cds-CtCt_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 673,
    label = "Cds-CtCt_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 674,
    label = "Cds-CtCt_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 675,
    label = "Cds-CtCt_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Ct                    U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 676,
    label = "Cds-CtCt_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Ct                    U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 677,
    label = "Cds-CtCt_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 678,
    label = "Cds-CtCt_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 679,
    label = "Cds-CtCt_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 680,
    label = "Cds-CtCt_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 681,
    label = "Cds-CtCt_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 682,
    label = "Cds-CtCt_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Ct                    U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 683,
    label = "Cds-CtCt_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 684,
    label = "Cds-CtCt_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 685,
    label = "Cds-CtCt_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 686,
    label = "Cds-CtCt_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 687,
    label = "Cds-CtCt_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 688,
    label = "Cds-CtCt_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Ct                    U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 689,
    label = "Cds-CtCt_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 690,
    label = "Cds-CtCt_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 691,
    label = "Cds-CtCt_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 692,
    label = "Cds-CtCt_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 693,
    label = "Cds-CtCt_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 694,
    label = "Cds-CtCt_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Ct                    U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 695,
    label = "Cds-CtCt_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 696,
    label = "Cds-CtCt_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 697,
    label = "Cds-CtCt_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 698,
    label = "Cds-CtCt_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 699,
    label = "Cds-CtCt_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 700,
    label = "Cds-CtCt_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Ct                    U0 {1,S}
4    Ct                    U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 701,
    label = "Cds-CtCt_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 702,
    label = "Cds-CtCt_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 703,
    label = "Cds-CtCt_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 704,
    label = "Cds-CtCt_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 705,
    label = "Cds-CtCt_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 706,
    label = "Cds-CtCt_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 707,
    label = "Cds-CtCt_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Ct U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 708,
    label = "Cds-CtCt_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cb U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 709,
    label = "Cds-CtCt_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    CO U0 {2,S}
7    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 710,
    label = "Cds-CtCt_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 711,
    label = "Cds-CtCt_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 712,
    label = "Cds-CtCt_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 713,
    label = "Cds-CtCt_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    C  U0 {5,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 714,
    label = "Cds-CtCt_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 715,
    label = "Cds-CtCt_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 716,
    label = "Cds-CtCb_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    Cb U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 717,
    label = "Cds-CtCO_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Ct U0 {1,S}
4    CO U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 718,
    label = "Cds-CbCb_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    Cb U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 719,
    label = "Cds-CbCO_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cb U0 {1,S}
4    CO U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 720,
    label = "Cds-COCO_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    CO U0 {1,S}
4    CO U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 721,
    label = "Cds-CdCt_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 722,
    label = "Cds-CdCt_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 723,
    label = "Cds-CdCt_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 724,
    label = "Cds-CdCt_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 725,
    label = "Cds-CdCt_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 726,
    label = "Cds-CdCt_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 727,
    label = "Cds-CdCt_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 728,
    label = "Cds-CdCt_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 729,
    label = "Cds-CdCt_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 730,
    label = "Cds-CdCt_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 731,
    label = "Cds-CdCt_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 732,
    label = "Cds-CdCt_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Ct                    U0 {1,S}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 733,
    label = "Cds-CdCt_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Ct                    U0 {1,S}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 734,
    label = "Cds-CdCt_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 735,
    label = "Cds-CdCt_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 736,
    label = "Cds-CdCt_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 737,
    label = "Cds-CdCt_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 738,
    label = "Cds-CdCt_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 739,
    label = "Cds-CdCt_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Ct                    U0 {1,S}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 740,
    label = "Cds-CdCt_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 741,
    label = "Cds-CdCt_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 742,
    label = "Cds-CdCt_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 743,
    label = "Cds-CdCt_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 744,
    label = "Cds-CdCt_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 745,
    label = "Cds-CdCt_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Ct                    U0 {1,S}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 746,
    label = "Cds-CdCt_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 747,
    label = "Cds-CdCt_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 748,
    label = "Cds-CdCt_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 749,
    label = "Cds-CdCt_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "Cds-CdCt_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 751,
    label = "Cds-CdCt_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Ct                    U0 {1,S}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 752,
    label = "Cds-CdCt_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 753,
    label = "Cds-CdCt_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 754,
    label = "Cds-CdCt_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 755,
    label = "Cds-CdCt_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {8,D}
7    C  U0 {3,D}
8    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 756,
    label = "Cds-CdCt_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 757,
    label = "Cds-CdCt_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Ct                    U0 {1,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 758,
    label = "Cds-CdCt_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 759,
    label = "Cds-CdCt_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 760,
    label = "Cds-CdCt_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 761,
    label = "Cds-CdCt_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 762,
    label = "Cds-CdCt_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cb U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 763,
    label = "Cds-CdCt_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    CO U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 764,
    label = "Cds-CdCt_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 765,
    label = "Cds-CdCt_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 766,
    label = "Cds-CdCt_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 767,
    label = "Cds-CdCt_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 768,
    label = "Cds-CdCt_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 769,
    label = "Cds-CdCt_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 770,
    label = "Cds-CdCt_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {8,D}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {5,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 771,
    label = "Cds-CdCt_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {9,D}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 772,
    label = "Cds-CdCt_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {9,D}
4    Ct U0 {1,S}
5    Cd U0 {2,S} {7,D}
6    Cd U0 {2,S} {8,D}
7    Sd U0 {5,D}
8    Sd U0 {6,D}
9    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 773,
    label = "Cds-CdCb_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cb U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 774,
    label = "Cds-CdCO_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    CO U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 775,
    label = "Cds-CtC=S_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Ct U0 {1,S}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 776,
    label = "Cds-CbC=S_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Cb U0 {1,S}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 777,
    label = "Cds-COC=S_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    CO U0 {1,S}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 778,
    label = "Cds-CdCd_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    R  U0 {2,S}
6    R  U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 779,
    label = "Cds-CdCd_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    H  U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 780,
    label = "Cds-CdCd_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cs U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 781,
    label = "Cds-CdCd_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 782,
    label = "Cds-CdCd_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 783,
    label = "Cds-CdCd_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 784,
    label = "Cds-CdCd_Cds-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 785,
    label = "Cds-CdCd_Cds-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    H  U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 786,
    label = "Cds-CdCd_Cds-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    Cs U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 787,
    label = "Cds-CdCd_Cds-SsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    Os U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 788,
    label = "Cds-CdCd_Cds-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    Ss U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 789,
    label = "Cds-CdCd_Cds-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cd                    U0 {1,S} {8,D}
5    R                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
8    C                     U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 790,
    label = "Cds-CdCd_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cd                    U0 {1,S} {8,D}
5    H                     U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
8    C                     U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 791,
    label = "Cds-CdCd_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    H  U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 792,
    label = "Cds-CdCd_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    H  U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 793,
    label = "Cds-CdCd_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    H  U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 794,
    label = "Cds-CdCd_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    H  U0 {2,S}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 795,
    label = "Cds-CdCd_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    H  U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 796,
    label = "Cds-CdCd_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cd                    U0 {1,S} {8,D}
5    Cs                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
8    C                     U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 797,
    label = "Cds-CdCd_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cs U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 798,
    label = "Cds-CdCd_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cs U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 799,
    label = "Cds-CdCd_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cs U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 800,
    label = "Cds-CdCd_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 801,
    label = "Cds-CdCd_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    Cs U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 802,
    label = "Cds-CdCd_Cds-OneDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cd                    U0 {1,S} {8,D}
5    Os                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
8    C                     U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 803,
    label = "Cds-CdCd_Cds-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 804,
    label = "Cds-CdCd_Cds-CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 805,
    label = "Cds-CdCd_Cds-COOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 806,
    label = "Cds-CdCd_Cds-CdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Os U0 {2,S}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 807,
    label = "Cds-CdCd_Cds-C=SOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    Os U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 808,
    label = "Cds-CdCd_Cds-OneDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cd                    U0 {1,S} {8,D}
5    Ss                    U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
8    C                     U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 809,
    label = "Cds-CdCd_Cds-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 810,
    label = "Cds-CdCd_Cds-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 811,
    label = "Cds-CdCd_Cds-COSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 812,
    label = "Cds-CdCd_Cds-CdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {9,D}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 813,
    label = "Cds-CdCd_Cds-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    Ss U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 814,
    label = "Cds-CdCd_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    Cd                    U0 {1,S} {7,D}
4    Cd                    U0 {1,S} {8,D}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
6    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
7    C                     U0 {3,D}
8    C                     U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 815,
    label = "Cds-CdCd_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ct U0 {2,S}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 816,
    label = "Cds-CdCd_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ct U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 817,
    label = "Cds-CdCd_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Ct U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 818,
    label = "Cds-CdCd_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cb U0 {2,S}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 819,
    label = "Cds-CdCd_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cb U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 820,
    label = "Cds-CdCd_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    CO U0 {2,S}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 821,
    label = "Cds-CdCd_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cd U0 {2,S} {9,D}
6    Ct U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 822,
    label = "Cds-CdCd_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cd U0 {2,S} {9,D}
6    Cb U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 823,
    label = "Cds-CdCd_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {7,D}
4    Cd U0 {1,S} {8,D}
5    Cd U0 {2,S} {9,D}
6    CO U0 {2,S}
7    C  U0 {3,D}
8    C  U0 {4,D}
9    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 824,
    label = "Cds-CdCd_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    Ct U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 825,
    label = "Cds-CdCd_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    Cb U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 826,
    label = "Cds-CdCd_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {9,D}
5    CO U0 {2,S}
6    Cd U0 {2,S} {7,D}
7    Sd U0 {6,D}
8    C  U0 {3,D}
9    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 827,
    label = "Cds-CdCd_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 Cd U0 {2,D} {3,S} {4,S}
2  *2 Cd U0 {1,D} {5,S} {6,S}
3     Cd U0 {1,S} {7,D}
4     Cd U0 {1,S} {8,D}
5     Cd U0 {2,S} {9,D}
6     Cd U0 {2,S} {10,D}
7     C  U0 {3,D}
8     C  U0 {4,D}
9     C  U0 {5,D}
10    C  U0 {6,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 828,
    label = "Cds-CdCd_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 Cd U0 {2,D} {3,S} {4,S}
2  *2 Cd U0 {1,D} {5,S} {6,S}
3     Cd U0 {1,S} {8,D}
4     Cd U0 {1,S} {9,D}
5     Cd U0 {2,S} {10,D}
6     Cd U0 {2,S} {7,D}
7     Sd U0 {6,D}
8     C  U0 {3,D}
9     C  U0 {4,D}
10    C  U0 {5,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 829,
    label = "Cds-CdCd_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 Cd U0 {2,D} {3,S} {4,S}
2  *2 Cd U0 {1,D} {5,S} {6,S}
3     Cd U0 {1,S} {9,D}
4     Cd U0 {1,S} {10,D}
5     Cd U0 {2,S} {7,D}
6     Cd U0 {2,S} {8,D}
7     Sd U0 {5,D}
8     Sd U0 {6,D}
9     C  U0 {3,D}
10    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 830,
    label = "Cds-CdC=S_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {6,S} {7,S}
3    Cd U0 {1,S} {8,D}
4    Cd U0 {1,S} {5,D}
5    Sd U0 {4,D}
6    R  U0 {2,S}
7    R  U0 {2,S}
8    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 831,
    label = "Cds-C=SC=S_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {7,S} {8,S}
3    Cd U0 {1,S} {5,D}
4    Cd U0 {1,S} {6,D}
5    Sd U0 {3,D}
6    Sd U0 {4,D}
7    R  U0 {2,S}
8    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 832,
    label = "Cds-OJH_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    O  U1 {1,S}
4    H  U0 {1,S}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 833,
    label = "Cds-OJH_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    O  U1 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 834,
    label = "Cds-OJH_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    O  U1 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 835,
    label = "Cds-OJNonDe_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                 U0 {2,D} {3,S} {4,S}
2 *2 Cd                 U0 {1,D} {5,S} {6,S}
3    O                  U1 {1,S}
4    {Cs,Os,Ss,N3s,N5s} U0 {1,S}
5    R                  U0 {2,S}
6    R                  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 836,
    label = "Cds-OJCs_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    O  U1 {1,S}
4    Cs U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 837,
    label = "Cds-OJDe_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cd                    U0 {2,D} {3,S} {4,S}
2 *2 Cd                    U0 {1,D} {5,S} {6,S}
3    O                     U1 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
5    R                     U0 {2,S}
6    R                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 838,
    label = "Ct_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T}
2 *2 R  U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 839,
    label = "Ct_Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T}
2 *2 Ct U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 840,
    label = "Ct-H_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 841,
    label = "Ct-H_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 842,
    label = "Ct-Cs_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 843,
    label = "Ct-Cs_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 844,
    label = "Ct-H_Ct-De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                    U0 {2,T} {3,S}
2 *2 Ct                    U0 {1,T} {4,S}
3    H                     U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 845,
    label = "Ct-H_Ct-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 846,
    label = "Ct-H_Ct-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 847,
    label = "Ct-H_Ct-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 848,
    label = "Ct-H_Ct-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    Cd U0 {2,S} {5,D}
5    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 849,
    label = "Ct-H_Ct-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    H  U0 {1,S}
4    Cd U0 {2,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 850,
    label = "Ct-Cs_Ct-De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                    U0 {2,T} {3,S}
2 *2 Ct                    U0 {1,T} {4,S}
3    Cs                    U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 851,
    label = "Ct-Cs_Ct-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 852,
    label = "Ct-Cs_Ct-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 853,
    label = "Ct-Cs_Ct-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 854,
    label = "Ct-Cs_Ct-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    Cd U0 {2,S} {5,D}
5    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 855,
    label = "Ct-Cs_Ct-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cs U0 {1,S}
4    Cd U0 {2,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 856,
    label = "Ct-De_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                    U0 {2,T} {3,S}
2 *2 Ct                    U0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    H                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 857,
    label = "Ct-Cb_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cb U0 {1,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 858,
    label = "Ct-CO_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    CO U0 {1,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 859,
    label = "Ct-Cd_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 860,
    label = "Ct-Ct_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 861,
    label = "Ct-C=S_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {2,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 862,
    label = "Ct-De_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                    U0 {2,T} {3,S}
2 *2 Ct                    U0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Cs                    U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 863,
    label = "Ct-Cb_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cb U0 {1,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 864,
    label = "Ct-CO_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    CO U0 {1,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 865,
    label = "Ct-Cd_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 866,
    label = "Ct-Ct_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 867,
    label = "Ct-C=S_Ct-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {2,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 868,
    label = "Ct-De_Ct-De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                    U0 {2,T} {3,S}
2 *2 Ct                    U0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 869,
    label = "Ct-Ct_Ct-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Ct U0 {1,S}
4    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 870,
    label = "Ct-Cd_Ct-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    Ct U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 871,
    label = "Ct-Ct_Ct-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Ct U0 {1,S}
4    Cd U0 {2,S} {5,D}
5    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 872,
    label = "Ct-Cd_Ct-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct U0 {2,T} {3,S}
2 *2 Ct U0 {1,T} {4,S}
3    Cd U0 {1,S} {5,D}
4    Cd U0 {2,S} {6,D}
5    C  U0 {3,D}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "Ct_Nt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct        U0 {2,T}
2 *2 {N3t,N5t} U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "Ct_N3t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U0 {2,T}
2 *2 N3t U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "Ct-H_N3t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U0 {2,T} {3,S}
2 *2 N3t U0 {1,T}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "Ct-NonDe_N3t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                 U0 {2,T} {3,S}
2 *2 N3t                U0 {1,T}
3    {Cs,N3s,N5s,Os,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "Ct-OneDe_N3t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct                    U0 {2,T} {3,S}
2 *2 N3t                   U0 {1,T}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "Ct_N5t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Ct  U0 {2,T}
2 *2 N5t U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 873,
    label = "Od_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od    U0 {2,D}
2 *2 {C,S} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "Od_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od U0 {2,D}
2 *2 N  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "Od_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od  U0 {2,D}
2 *2 N3d U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "Od_N5d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od  U0 {2,D}
2 *2 N5d U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 874,
    label = "Od_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od U0 {2,D}
2 *2 C  U0 {1,D} {3,D}
3    R  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 875,
    label = "Od_Cdd-Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od U0 {2,D}
2 *2 C  U0 {1,D} {3,D}
3    O  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 876,
    label = "Od_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od U0 {2,D}
2 *2 C  U0 {1,D} {3,S} {4,S}
3    R  U0 {2,S}
4    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 877,
    label = "Od_Cd-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Od U0 {2,D}
2 *2 CO U0 {1,D} {3,S} {4,S}
3    Cs U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "Nd_R",
    group = "OR{N1d_R, N3d_R}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 394,
    label = "N1d_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N1d U0 L2 {2,D}
2 *2 R!H U0 L0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "N3d_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 R!H U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "N3d_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d      U0 {2,D}
2 *2 {Cd,Cdd} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "N3d_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 Cdd U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "N3d_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 Cd  U0 {1,D} {3,S} {4,S}
3    R   U0 {2,S}
4    R   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "N3d-H_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D} {5,S}
2 *2 Cd  U0 {1,D} {3,S} {4,S}
3    R   U0 {2,S}
4    R   U0 {2,S}
5    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "N3d-H_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D} {5,S}
2 *2 Cd  U0 {1,D} {3,S} {4,S}
3    H   U0 {2,S}
4    H   U0 {2,S}
5    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "N3d-H_Cds-NonDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                U0 {2,D} {5,S}
2 *2 Cd                 U0 {1,D} {3,S} {4,S}
3    {Cs,Os,Ss,N3s,N5s} U0 {2,S}
4    H                  U0 {2,S}
5    H                  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "N3d-H_Cds-NonDe2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                U0 {2,D} {5,S}
2 *2 Cd                 U0 {1,D} {3,S} {4,S}
3    {Cs,Os,Ss,N3s,N5s} U0 {2,S}
4    {Cs,Os,Ss,N3s,N5s} U0 {2,S}
5    H                  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "N3d-NonDe_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                U0 {2,D} {5,S}
2 *2 Cd                 U0 {1,D} {3,S} {4,S}
3    R!H                U0 {2,S}
4    R!H                U0 {2,S}
5    {Cs,N3s,N5s,Os,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "N3d-OneDe_Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                   U0 {2,D} {5,S}
2 *2 Cd                    U0 {1,D} {3,S} {4,S}
3    R!H                   U0 {2,S}
4    R!H                   U0 {2,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "N3d_Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "N3d-H_Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D} {3,S}
2 *2 Od  U0 {1,D}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "N3d-NonDe_Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d            U0 {2,D} {3,S}
2 *2 Od             U0 {1,D}
3    {Cs,N3s,Os,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 329,
    label = "N3d-OneDe_Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                   U0 {2,D} {3,S}
2 *2 Od                    U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "N3d_Nd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 N   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "N3d_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D}
2 *2 N3d U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "N3d-H_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D} {3,S}
2 *2 N3d U0 {1,D}
3    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "N3d-H_N3d-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d U0 {2,D} {3,S}
2 *2 N3d U0 {1,D} {4,S}
3    H   U0 {1,S}
4    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "N3d-H_N3d-NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d            U0 {2,D} {3,S}
2 *2 N3d            U0 {1,D} {4,S}
3    H              U0 {1,S}
4    {Cs,N3s,Os,Ss} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "N3d-H_N3d-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                   U0 {2,D} {3,S}
2 *2 N3d                   U0 {1,D} {4,S}
3    H                     U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "N3d-NonDe_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d            U0 {2,D} {3,S}
2 *2 N3d            U0 {1,D}
3    {Cs,N3s,Os,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "N3d-OneDe_N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d                   U0 {2,D} {3,S}
2 *2 N3d                   U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "N3d_N5d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3d       U0 {2,D}
2 *2 {N5d,N5t} U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "Nt_R",
    group = "OR{N3t_R, N5t_R}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "N3t_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3t U0 {2,T}
2 *2 R!H U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "N3t_Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3t U0 {2,T}
2 *2 Ct  U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "N3t_Ct-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3t U0 {2,T}
2 *2 Ct  U0 {1,T} {3,S}
3    H   U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "N3t_Ct-NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3t                U0 {2,T}
2 *2 Ct                 U0 {1,T} {3,S}
3    {Cs,N3s,N5s,Os,Ss} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "N3t_Ct-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3t                   U0 {2,T}
2 *2 Ct                    U0 {1,T} {3,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "N3t_N3t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N3t U0 {2,T}
2 *2 N3t U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "N5t_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 N5t U0 {2,T}
2 *2 R   U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 878,
    label = "Sd_R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 R  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 879,
    label = "Sd_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd  U0 {2,D}
2 *2 Cdd U0 {1,D} {3,D}
3    R   U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 880,
    label = "Sd_Cdd-Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd  U0 {2,D}
2 *2 Cdd U0 {1,D} {3,D}
3    Sd  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 881,
    label = "Sd_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    R  U0 {2,S}
4    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 882,
    label = "Sd_Cds-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
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
    index = 883,
    label = "Sd_Cds-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cs U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 884,
    label = "Sd_Cds-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Os U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 885,
    label = "Sd_Cds-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Os U0 {2,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 886,
    label = "Sd_Cds-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cs U0 {2,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 887,
    label = "Sd_Cds-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd                    U0 {2,D}
2 *2 Cd                    U0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
4    H                     U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 888,
    label = "Sd_Cds-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Ct U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 889,
    label = "Sd_Cds-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cb U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 890,
    label = "Sd_Cds-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    CO U0 {2,S}
4    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 891,
    label = "Sd_Cds-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    H  U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 892,
    label = "Sd_Cds-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    H  U0 {2,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 893,
    label = "Sd_Cds-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd                    U0 {2,D}
2 *2 Cd                    U0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
4    Cs                    U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 894,
    label = "Sd_Cds-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Ct U0 {2,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 895,
    label = "Sd_Cds-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cb U0 {2,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 896,
    label = "Sd_Cds-COCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    CO U0 {2,S}
4    Cs U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 897,
    label = "Sd_Cds-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    Cs U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 898,
    label = "Sd_Cds-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    Cs U0 {2,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 899,
    label = "Sd_Cds-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd                    U0 {2,D}
2 *2 Cd                    U0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 900,
    label = "Sd_Cds-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Ct U0 {2,S}
4    Ct U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 901,
    label = "Sd_Cds-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Ct U0 {2,S}
4    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 902,
    label = "Sd_Cds-CtCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Ct U0 {2,S}
4    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 903,
    label = "Sd_Cds-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cb U0 {2,S}
4    Cb U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 904,
    label = "Sd_Cds-CbCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cb U0 {2,S}
4    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 905,
    label = "Sd_Cds-COCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    CO U0 {2,S}
4    CO U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 906,
    label = "Sd_Cds-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    Ct U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 907,
    label = "Sd_Cds-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    Cb U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 908,
    label = "Sd_Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    CO U0 {2,S}
5    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 909,
    label = "Sd_Cds-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Ct U0 {2,S}
4    Cd U0 {2,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 910,
    label = "Sd_Cds-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cb U0 {2,S}
4    Cd U0 {2,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 911,
    label = "Sd_Cds-COC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    CO U0 {2,S}
4    Cd U0 {2,S} {5,D}
5    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 912,
    label = "Sd_Cds-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    Cd U0 {2,S} {6,D}
5    C  U0 {3,D}
6    C  U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 913,
    label = "Sd_Cds-CdC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {6,D}
4    Cd U0 {2,S} {5,D}
5    Sd U0 {4,D}
6    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 914,
    label = "Sd_Cds-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Sd U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    Cd U0 {2,S} {5,D}
4    Cd U0 {2,S} {6,D}
5    Sd U0 {3,D}
6    Sd U0 {4,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 915,
    label = "HJ",
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
    index = 916,
    label = "CJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 917,
    label = "CbJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cb U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 918,
    label = "CtJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ct U1 {2,T}
2    C  U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "CtJ_Ct",
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
    index = 356,
    label = "CtJ_N3t",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ct  U1 {2,T}
2    N3t U0 {1,T}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 919,
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
    index = 920,
    label = "C=SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 921,
    label = "C=SJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 922,
    label = "C=SJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 923,
    label = "C=SJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 924,
    label = "C=SJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 925,
    label = "C=SJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 926,
    label = "C=SJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 927,
    label = "C=SJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 928,
    label = "C=SJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 929,
    label = "C=SJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U1 {2,D} {3,S}
2    Sd U0 {1,D}
3    Cd U0 {1,S} {4,D}
4    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 930,
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
    index = 931,
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
    index = 932,
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
    index = 933,
    label = "CO_rad/NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                  U1 {2,D} {3,S}
2    O                  U0 {1,D}
3    {Cs,Ss,N3s,N5s,Os} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 934,
    label = "CO_rad/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,D} {3,S}
2    O                     U0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 935,
    label = "CsJ",
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
    index = 936,
    label = "CsJ-HHH",
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
    index = 937,
    label = "CsJ-CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
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
    index = 938,
    label = "CsJ-CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 939,
    label = "CsJ-CsCsCs",
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
    index = 940,
    label = "CsJ-OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
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
    index = 941,
    label = "CsJ-OsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 942,
    label = "CsJ-OsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
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
    index = 943,
    label = "CsJ-OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Os U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 944,
    label = "CsJ-OsOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Os U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 945,
    label = "CsJ-OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Os U0 {1,S}
3    Os U0 {1,S}
4    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 946,
    label = "CsJ-SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
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
    index = 947,
    label = "CsJ-SsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 948,
    label = "CsJ-SsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
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
    index = 949,
    label = "CsJ-SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    Ss U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 950,
    label = "CsJ-SsSsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    Ss U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 951,
    label = "CsJ-SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ss U0 {1,S}
3    Ss U0 {1,S}
4    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 361,
    label = "CsJ-NsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C         U1 {2,S} {3,S} {4,S}
2    H         U0 {1,S}
3    H         U0 {1,S}
4    {N3s,N5s} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "CsJ-NsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C         U1 {2,S} {3,S} {4,S}
2    H         U0 {1,S}
3    {N3s,N5s} U0 {1,S}
4    Cs        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 952,
    label = "CsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {H,Cs,Os,Ss}          U0 {1,S}
4    {H,Cs,Os,Ss}          U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 953,
    label = "CsJ-OneDeHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    H                     U0 {1,S}
4    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 954,
    label = "CsJ-CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
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
    index = 955,
    label = "CsJ-CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
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
    index = 956,
    label = "CsJ-COHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
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
    index = 957,
    label = "CsJ-CdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 958,
    label = "CsJ-C=SHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 959,
    label = "CsJ-OneDeCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Cs                    U0 {1,S}
4    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 960,
    label = "CsJ-CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 961,
    label = "CsJ-CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 962,
    label = "CsJ-COCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cs U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 963,
    label = "CsJ-CdCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 964,
    label = "CsJ-C=SCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    H  U0 {1,S}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 965,
    label = "CsJ-OneDeOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Os                    U0 {1,S}
4    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 966,
    label = "CsJ-OneDeSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Ss                    U0 {1,S}
4    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 967,
    label = "CsJ-OneDeCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Cs                    U0 {1,S}
4    Cs                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 968,
    label = "CsJ-CtCsCs",
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
    index = 969,
    label = "CsJ-CbCsCs",
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
    index = 970,
    label = "CsJ-COCsCs",
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
    index = 971,
    label = "CsJ-CdCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
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
    index = 972,
    label = "CsJ-C=SCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 973,
    label = "CsJ-OneDeOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Os                    U0 {1,S}
4    Cs                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 974,
    label = "CsJ-OneDeSsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Ss                    U0 {1,S}
4    Cs                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 975,
    label = "CsJ-OneDeOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Os                    U0 {1,S}
4    Os                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 976,
    label = "CsJ-OneDeOsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Os                    U0 {1,S}
4    Ss                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 977,
    label = "CsJ-OneDeSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Ss                    U0 {1,S}
4    Ss                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "CsJ-OneDeNsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    H                     U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {N3s,N5s}             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 394,
    label = "CsJ-OneDeNsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    Cs                    U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {N3s,N5s}             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 978,
    label = "CsJ-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {H,Cs,Os,Ss}          U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 979,
    label = "CsJ-TwoDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 980,
    label = "CsJ-CtCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Ct U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 981,
    label = "CsJ-CtCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 982,
    label = "CsJ-CtCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 983,
    label = "CsJ-CbCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cb U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 984,
    label = "CsJ-CbCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 985,
    label = "CsJ-COCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    CO U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 986,
    label = "CsJ-CdCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Ct U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 987,
    label = "CsJ-CdCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cb U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 988,
    label = "CsJ-CdCOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    CO U0 {1,S}
4    H  U0 {1,S}
5    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 989,
    label = "CsJ-CtC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 990,
    label = "CsJ-CbC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 991,
    label = "CsJ-COC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    H  U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 992,
    label = "CsJ-CdCdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
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
    index = 993,
    label = "CsJ-CdC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    C  U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 994,
    label = "CsJ-C=SC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    H  U0 {1,S}
5    Sd U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 995,
    label = "CsJ-TwoDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Cs                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 996,
    label = "CsJ-CtCtCs",
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
    index = 997,
    label = "CsJ-CtCbCs",
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
    index = 998,
    label = "CsJ-CtCOCs",
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
    index = 999,
    label = "CsJ-CbCbCs",
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
    index = 1000,
    label = "CsJ-CbCOCs",
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
    index = 1001,
    label = "CsJ-COCOCs",
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
    index = 1002,
    label = "CsJ-CdCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
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
    index = 1003,
    label = "CsJ-CdCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
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
    index = 1004,
    label = "CsJ-CdCOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
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
    index = 1005,
    label = "CsJ-CtC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Ct U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1006,
    label = "CsJ-CbC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cb U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1007,
    label = "CsJ-COC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    CO U0 {1,S}
3    Cd U0 {1,S} {5,D}
4    Cs U0 {1,S}
5    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1008,
    label = "CsJ-CdCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
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
    index = 1009,
    label = "CsJ-CdC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    C  U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1010,
    label = "CsJ-C=SC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2    Cd U0 {1,S} {5,D}
3    Cd U0 {1,S} {6,D}
4    Cs U0 {1,S}
5    Sd U0 {2,D}
6    Sd U0 {3,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1011,
    label = "CsJ-TwoDeOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Os                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1012,
    label = "CsJ-TwoDeSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    Ss                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1013,
    label = "CsJ-ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C                     U1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1014,
    label = "CdsJ=Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D} {4,D}
3    R U0 {1,S}
4    R U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1015,
    label = "CdsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D} {4,S} {5,S}
3    R U0 {1,S}
4    R U0 {2,S}
5    R U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1016,
    label = "CdsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C U1 {2,D} {3,S}
2    C U0 {1,D} {4,S} {5,S}
3    H U0 {1,S}
4    R U0 {2,S}
5    R U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1017,
    label = "CdsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    Cs U0 {1,S}
4    R  U0 {2,S}
5    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1018,
    label = "CdsJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    Ct U0 {1,S}
4    R  U0 {2,S}
5    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1019,
    label = "CdsJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    Cb U0 {1,S}
4    R  U0 {2,S}
5    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1020,
    label = "CdsJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    CO U0 {1,S}
4    R  U0 {2,S}
5    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1021,
    label = "CdsJ-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    Os U0 {1,S}
4    R  U0 {2,S}
5    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1022,
    label = "CdsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {4,S} {5,S}
3    Ss U0 {1,S}
4    R  U0 {2,S}
5    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1023,
    label = "CdsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {4,D}
4    C  U0 {3,D}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1024,
    label = "CdsJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U1 {2,D} {3,S}
2    C  U0 {1,D} {5,S} {6,S}
3    Cd U0 {1,S} {4,D}
4    Sd U0 {3,D}
5    R  U0 {2,S}
6    R  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1025,
    label = "OJ",
    group = "OR{OJ_pri, OJ_sec, O2b}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1026,
    label = "OJ_pri",
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
    index = 1027,
    label = "OJ_sec",
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
    index = 1028,
    label = "OJ-NonDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O                  U1 {2,S}
2    {Cs,Os,Ss,N3s,N5s} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1029,
    label = "OJ-Cs",
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
    index = 1030,
    label = "OJ-Os",
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
    index = 357,
    label = "OJ-Ns",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O         U1 {2,S}
2    {N3s,N5s} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "OJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O                     U1 {2,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "OJ-OneDeN",
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
    index = 360,
    label = "OJ-NO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 O         U1 {2,S}
2    {N3d,N5d} U0 {1,S} {3,D}
3    Od        U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1032,
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
    index = 1037,
    label = "SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1038,
    label = "SsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1039,
    label = "SsJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1040,
    label = "SsJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1041,
    label = "SsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Ss U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1042,
    label = "SsJ-OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss                    U1 {2,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1043,
    label = "SsJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Ct U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1044,
    label = "SsJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cb U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1045,
    label = "SsJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    CO U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1046,
    label = "SsJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cd U0 {1,S} {3,D}
3    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1047,
    label = "SsJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Ss U1 {2,S}
2    Cd U0 {1,S} {3,D}
3    Sd U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 395,
    label = "NJ",
    group = "OR{N3J}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "N3J",
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
    index = 365,
    label = "N3sJ",
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
    index = 366,
    label = "NH2J",
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
    index = 367,
    label = "N3sJ-NonDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s                U1 {2,S} {3,S}
2    {Os,Ss,N3s,N5s,Cs} U0 {1,S}
3    H                  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "N3sJ-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U1 {2,S} {3,S}
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
    index = 370,
    label = "N3sJ-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U1 {2,S} {3,S}
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
    index = 371,
    label = "N3sJ-NsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s       U1 {2,S} {3,S}
2    {N3s,N5s} U0 {1,S}
3    H         U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "N3sJ-NonDe2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s                U1 {2,S} {3,S}
2    {Os,Cs,N3s,N5s,Ss} U0 {1,S}
3    {Os,Cs,N3s,N5s,Ss} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "N3sJ-OneDeH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s                   U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    H                     U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "N3sJ-OneDeCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s                   U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    Cs                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "N3sJ-TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s                   U1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "N3dJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 378,
    label = "N3dJ_C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    C   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "N3dJ_O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 380,
    label = "N3dJ_N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3d U1 {2,D}
2    N   U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "Y_1centerbirad",
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
    index = 1034,
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
    index = 1035,
    label = "SJJ_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 S U2
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "CO_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 C  U2 {2,D}
2    Od U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "NH_(T)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 N3s U2 {2,S}
2    H   U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1036,
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
    index = 344,
    label = "Y_1centertrirad",
    group = "OR{N_(Q), N_(D), CH_(Q), CH_(D)}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 386,
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
    index = 387,
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
    index = 388,
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
    index = 389,
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
    index = 393,
    label = "Y_1centerquadrad",
    group = "OR{C_(V), C_(T), C_(S)}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 383,
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
    index = 384,
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
    index = 385,
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

tree(
"""
L1: R_R
    L2: Cd_R
        L3: Cdd_Od
            L4: CO2
            L4: Ck_O
            L4: C=S_O
        L3: CO_O
            L4: CO/H2_O
            L4: CO/H/Nd_O
                L5: CO/H/Cs
            L4: CO/H/De_O
            L4: CO/Nd2_O
            L4: CO/Nd/De_O
            L4: CO/De2_O
        L3: Cds_Nd
            L4: Cds_N3d
                L5: Cds-HH_N3d
                L5: Cds-NonDeH_N3d
                    L6: Cds-NonDe2_N3d
        L3: Cdd_Sd
            L4: Cdd-Sd_Sd
        L3: Cds_Cdd
            L4: Cds_Ca
                L5: Cds-HH_Ca
                L5: Cds-CsH_Ca
                L5: Cds-CsCs_Ca
                L5: Cds-OneDeH_Ca
                    L6: Cds-CtH_Ca
                    L6: Cds-CbH_Ca
                    L6: Cds-COH_Ca
                    L6: Cds-CdH_Ca
                    L6: Cds-C=SH_Ca
                L5: Cds-OneDeCs_Ca
                    L6: Cds-CtCs_Ca
                    L6: Cds-CbCs_Ca
                    L6: Cds-COCs_Ca
                    L6: Cds-CdCs_Ca
                    L6: Cds-C=SCs_Ca
                L5: Cds-TwoDe_Ca
                    L6: Cds-CtCt_Ca
                    L6: Cds-CtCb_Ca
                    L6: Cds-CtCO_Ca
                    L6: Cds-CbCb_Ca
                    L6: Cds-CbCO_Ca
                    L6: Cds-COCO_Ca
                    L6: Cds-CdCt_Ca
                    L6: Cds-CdCb_Ca
                    L6: Cds-CdCO_Ca
                    L6: Cds-CtC=S_Ca
                    L6: Cds-CbC=S_Ca
                    L6: Cds-COC=S_Ca
                    L6: Cds-CdCd_Ca
                    L6: Cds-CdC=S_Ca
                    L6: Cds-C=SC=S_Ca
            L4: Cds_Ck
                L5: Cds-HH_Ck
                L5: Cds-CsH_Ck
                L5: Cds-CsCs_Ck
                L5: Cds-OneDeH_Ck
                L5: Cds-OneDeCs_Ck
                L5: Cds-TwoDe_Ck
        L3: Cdd_Cds
            L4: Ca_Cds
                L5: Ca_Cds-HH
                L5: Ca_Cds-CsH
                L5: Ca_Cds-CsCs
                L5: Ca_Cds-OneDeH
                    L6: Ca_Cds-CtH
                    L6: Ca_Cds-CbH
                    L6: Ca_Cds-COH
                    L6: Ca_Cds-CdH
                    L6: Ca_Cds-C=SH
                L5: Ca_Cds-OneDeCs
                    L6: Ca_Cds-CtCs
                    L6: Ca_Cds-CbCs
                    L6: Ca_Cds-COCs
                    L6: Ca_Cds-CdCs
                    L6: Ca_Cds-C=SCs
                L5: Ca_Cds-TwoDe
                    L6: Ca_Cds-CtCt
                    L6: Ca_Cds-CtCb
                    L6: Ca_Cds-CtCO
                    L6: Ca_Cds-CbCb
                    L6: Ca_Cds-CbCO
                    L6: Ca_Cds-COCO
                    L6: Ca_Cds-CdCt
                    L6: Ca_Cds-CdCb
                    L6: Ca_Cds-CdCO
                    L6: Ca_Cds-CtC=S
                    L6: Ca_Cds-CbC=S
                    L6: Ca_Cds-COC=S
                    L6: Ca_Cds-CdCd
                    L6: Ca_Cds-CdC=S
                    L6: Ca_Cds-C=SC=S
            L4: Ck_Cds
                L5: Ck_Cds-HH
                L5: Ck_Cds-CsH
                L5: Ck_Cds-CsCs
                L5: Ck_Cds-OneDeH
                    L6: Ck_Cds-CtH
                    L6: Ck_Cds-CbH
                    L6: Ck_Cds-COH
                    L6: Ck_Cds-CdH
                    L6: Ck_Cds-C=SH
                L5: Ck_Cds-OneDeCs
                    L6: Ck_Cds-CtCs
                    L6: Ck_Cds-CbCs
                    L6: Ck_Cds-COCs
                    L6: Ck_Cds-CdCs
                    L6: Ck_Cds-C=SCs
                L5: Ck_Cds-TwoDe
                    L6: Ck_Cds-CtCt
                    L6: Ck_Cds-CtCb
                    L6: Ck_Cds-CtCO
                    L6: Ck_Cds-CbCb
                    L6: Ck_Cds-CbCO
                    L6: Ck_Cds-COCO
                    L6: Ck_Cds-CdCt
                    L6: Ck_Cds-CdCb
                    L6: Ck_Cds-CdCO
                    L6: Ck_Cds-CtC=S
                    L6: Ck_Cds-CbC=S
                    L6: Ck_Cds-COC=S
                    L6: Ck_Cds-CdCd
                    L6: Ck_Cds-CdC=S
                    L6: Ck_Cds-C=SC=S
        L3: Cdd_Cdd
            L4: Ca_Ca
            L4: Ck_Ck
            L4: Ca_Ck
            L4: Ck_Ca
        L3: Cds_Sd
            L4: Cds-HH_Sd
            L4: Cds-CsH_Sd
            L4: Cds-CsCs_Sd
            L4: Cds-OsH_Sd
            L4: Cds-OsCs_Sd
            L4: Cds-SsH_Sd
            L4: Cds-SsCs_Sd
            L4: Cds-OneDeH_Sd
                L5: Cds-CtH_Sd
                L5: Cds-CbH_Sd
                L5: Cds-COH_Sd
                L5: Cds-CdH_Sd
                L5: Cds-C=SH_Sd
            L4: Cds-OneDeCs_Sd
                L5: Cds-CtCs_Sd
                L5: Cds-CbCs_Sd
                L5: Cds-COCs_Sd
                L5: Cds-CdCs_Sd
                L5: Cds-C=SCs_Sd
            L4: Cds-TwoDe_Sd
                L5: Cds-CtCt_Sd
                L5: Cds-CtCb_Sd
                L5: Cds-CtCO_Sd
                L5: Cds-CbCb_Sd
                L5: Cds-CbCO_Sd
                L5: Cds-COCO_Sd
                L5: Cds-CdCt_Sd
                L5: Cds-CdCb_Sd
                L5: Cds-CdCO_Sd
                L5: Cds-CtC=S_Sd
                L5: Cds-CbC=S_Sd
                L5: Cds-COC=S_Sd
                L5: Cds-CdCd_Sd
                L5: Cds-CdC=S_Sd
                L5: Cds-C=SC=S_Sd
        L3: Cds_Cds
            L4: Cds-HH_Cds
                L5: Cds-HH_Cds-HH
                L5: Cds-HH_Cds-CsH
                    L6: Cds-HH_Cds-Cs\Os/H
                    L6: Cds-HH_Cds-Cs\H3/H
                L5: Cds-HH_Cds-CsCs
                L5: Cds-HH_Cds-OsH
                L5: Cds-HH_Cds-OsCs
                L5: Cds-HH_Cds-OsOs
                L5: Cds-HH_Cds-SsH
                L5: Cds-HH_Cds-SsCs
                L5: Cds-HH_Cds-SsOs
                L5: Cds-HH_Cds-SsSs
                L5: Cds-HH_Cds-OneDe
                    L6: Cds-HH_Cds-OneDeH
                        L7: Cds-HH_Cds-CtH
                        L7: Cds-HH_Cds-CbH
                        L7: Cds-HH_Cds-COH
                        L7: Cds-HH_Cds-CdH
                        L7: Cds-HH_Cds-C=SH
                    L6: Cds-HH_Cds-OneDeCs
                        L7: Cds-HH_Cds-CtCs
                        L7: Cds-HH_Cds-CbCs
                        L7: Cds-HH_Cds-COCs
                        L7: Cds-HH_Cds-CdCs
                        L7: Cds-HH_Cds-C=SCs
                    L6: Cds-HH_Cds-OneDeOs
                        L7: Cds-HH_Cds-CtOs
                        L7: Cds-HH_Cds-CbOs
                        L7: Cds-HH_Cds-COOs
                        L7: Cds-HH_Cds-CdOs
                        L7: Cds-HH_Cds-C=SOs
                    L6: Cds-HH_Cds-OneDeSs
                        L7: Cds-HH_Cds-CtSs
                        L7: Cds-HH_Cds-CbSs
                        L7: Cds-HH_Cds-COSs
                        L7: Cds-HH_Cds-CdSs
                        L7: Cds-HH_Cds-C=SSs
                L5: Cds-HH_Cds-TwoDe
                    L6: Cds-HH_Cds-CtCt
                    L6: Cds-HH_Cds-CtCb
                    L6: Cds-HH_Cds-CtCO
                    L6: Cds-HH_Cds-CbCb
                    L6: Cds-HH_Cds-CbCO
                    L6: Cds-HH_Cds-COCO
                    L6: Cds-HH_Cds-CdCt
                    L6: Cds-HH_Cds-CdCb
                    L6: Cds-HH_Cds-CdCO
                    L6: Cds-HH_Cds-CtC=S
                    L6: Cds-HH_Cds-CbC=S
                    L6: Cds-HH_Cds-COC=S
                    L6: Cds-HH_Cds-CdCd
                    L6: Cds-HH_Cds-CdC=S
                    L6: Cds-HH_Cds-C=SC=S
            L4: Cds-CsH_Cds
                L5: Cds-CsH_Cds-HH
                    L6: Cds-Cs\Os/H_Cds-HH
                L5: Cds-CsH_Cds-CsH
                L5: Cds-CsH_Cds-CsCs
                L5: Cds-CsH_Cds-OsH
                L5: Cds-CsH_Cds-OsCs
                L5: Cds-CsH_Cds-OsOs
                L5: Cds-CsH_Cds-SsH
                L5: Cds-CsH_Cds-SsCs
                L5: Cds-CsH_Cds-SsOs
                L5: Cds-CsH_Cds-SsSs
                L5: Cds-CsH_Cds-OneDe
                    L6: Cds-CsH_Cds-OneDeH
                        L7: Cds-CsH_Cds-CtH
                        L7: Cds-CsH_Cds-CbH
                        L7: Cds-CsH_Cds-COH
                        L7: Cds-CsH_Cds-CdH
                        L7: Cds-CsH_Cds-C=SH
                    L6: Cds-CsH_Cds-OneDeCs
                        L7: Cds-CsH_Cds-CtCs
                        L7: Cds-CsH_Cds-CbCs
                        L7: Cds-CsH_Cds-COCs
                        L7: Cds-CsH_Cds-CdCs
                        L7: Cds-CsH_Cds-C=SCs
                    L6: Cds-CsH_Cds-OneDeOs
                        L7: Cds-CsH_Cds-CtOs
                        L7: Cds-CsH_Cds-CbOs
                        L7: Cds-CsH_Cds-COOs
                        L7: Cds-CsH_Cds-CdOs
                        L7: Cds-CsH_Cds-C=SOs
                    L6: Cds-CsH_Cds-OneDeSs
                        L7: Cds-CsH_Cds-CtSs
                        L7: Cds-CsH_Cds-CbSs
                        L7: Cds-CsH_Cds-COSs
                        L7: Cds-CsH_Cds-CdSs
                        L7: Cds-CsH_Cds-C=SSs
                L5: Cds-CsH_Cds-TwoDe
                    L6: Cds-CsH_Cds-CtCt
                    L6: Cds-CsH_Cds-CtCb
                    L6: Cds-CsH_Cds-CtCO
                    L6: Cds-CsH_Cds-CbCb
                    L6: Cds-CsH_Cds-CbCO
                    L6: Cds-CsH_Cds-COCO
                    L6: Cds-CsH_Cds-CdCt
                    L6: Cds-CsH_Cds-CdCb
                    L6: Cds-CsH_Cds-CdCO
                    L6: Cds-CsH_Cds-CtC=S
                    L6: Cds-CsH_Cds-CbC=S
                    L6: Cds-CsH_Cds-COC=S
                    L6: Cds-CsH_Cds-CdCd
                    L6: Cds-CsH_Cds-CdC=S
                    L6: Cds-CsH_Cds-C=SC=S
            L4: Cds-CsCs_Cds
                L5: Cds-CsCs_Cds-HH
                L5: Cds-CsCs_Cds-CsH
                L5: Cds-CsCs_Cds-CsCs
                L5: Cds-CsCs_Cds-OsH
                L5: Cds-CsCs_Cds-OsCs
                L5: Cds-CsCs_Cds-OsOs
                L5: Cds-CsCs_Cds-SsH
                L5: Cds-CsCs_Cds-SsCs
                L5: Cds-CsCs_Cds-SsOs
                L5: Cds-CsCs_Cds-SsSs
                L5: Cds-CsCs_Cds-OneDe
                    L6: Cds-CsCs_Cds-OneDeH
                        L7: Cds-CsCs_Cds-CtH
                        L7: Cds-CsCs_Cds-CbH
                        L7: Cds-CsCs_Cds-COH
                        L7: Cds-CsCs_Cds-CdH
                        L7: Cds-CsCs_Cds-C=SH
                    L6: Cds-CsCs_Cds-OneDeCs
                        L7: Cds-CsCs_Cds-CtCs
                        L7: Cds-CsCs_Cds-CbCs
                        L7: Cds-CsCs_Cds-COCs
                        L7: Cds-CsCs_Cds-CdCs
                        L7: Cds-CsCs_Cds-C=SCs
                    L6: Cds-CsCs_Cds-OneDeOs
                        L7: Cds-CsCs_Cds-CtOs
                        L7: Cds-CsCs_Cds-CbOs
                        L7: Cds-CsCs_Cds-COOs
                        L7: Cds-CsCs_Cds-CdOs
                        L7: Cds-CsCs_Cds-C=SOs
                    L6: Cds-CsCs_Cds-OneDeSs
                        L7: Cds-CsCs_Cds-CtSs
                        L7: Cds-CsCs_Cds-CbSs
                        L7: Cds-CsCs_Cds-COSs
                        L7: Cds-CsCs_Cds-CdSs
                        L7: Cds-CsCs_Cds-C=SSs
                L5: Cds-CsCs_Cds-TwoDe
                    L6: Cds-CsCs_Cds-CtCt
                    L6: Cds-CsCs_Cds-CtCb
                    L6: Cds-CsCs_Cds-CtCO
                    L6: Cds-CsCs_Cds-CbCb
                    L6: Cds-CsCs_Cds-CbCO
                    L6: Cds-CsCs_Cds-COCO
                    L6: Cds-CsCs_Cds-CdCt
                    L6: Cds-CsCs_Cds-CdCb
                    L6: Cds-CsCs_Cds-CdCO
                    L6: Cds-CsCs_Cds-CtC=S
                    L6: Cds-CsCs_Cds-CbC=S
                    L6: Cds-CsCs_Cds-COC=S
                    L6: Cds-CsCs_Cds-CdCd
                    L6: Cds-CsCs_Cds-CdC=S
                    L6: Cds-CsCs_Cds-C=SC=S
            L4: Cds-SsH_Cds
            L4: Cds-SsCs_Cds
            L4: Cds-SsSs_Cds
            L4: Cds-OsH_Cds
                L5: Cds-OsH_Cds-CsH
            L4: Cds-OsCs_Cds
            L4: Cds-OsOs_Cds
            L4: Cds-OsSs_Cds
            L4: Cds-OneDe_Cds
                L5: Cds-OneDeH_Cds
                    L6: Cds-CtH_Cds
                        L7: Cds-CtH_Cds-HH
                        L7: Cds-CtH_Cds-CsH
                        L7: Cds-CtH_Cds-CsCs
                        L7: Cds-CtH_Cds-OsH
                        L7: Cds-CtH_Cds-OsCs
                        L7: Cds-CtH_Cds-OsOs
                        L7: Cds-CtH_Cds-SsH
                        L7: Cds-CtH_Cds-SsCs
                        L7: Cds-CtH_Cds-SsOs
                        L7: Cds-CtH_Cds-SsSs
                        L7: Cds-CtH_Cds-OneDe
                            L8: Cds-CtH_Cds-OneDeH
                                L9: Cds-CtH_Cds-CtH
                                L9: Cds-CtH_Cds-CbH
                                L9: Cds-CtH_Cds-COH
                                L9: Cds-CtH_Cds-CdH
                                L9: Cds-CtH_Cds-C=SH
                            L8: Cds-CtH_Cds-OneDeCs
                                L9: Cds-CtH_Cds-CtCs
                                L9: Cds-CtH_Cds-CbCs
                                L9: Cds-CtH_Cds-COCs
                                L9: Cds-CtH_Cds-CdCs
                                L9: Cds-CtH_Cds-C=SCs
                            L8: Cds-CtH_Cds-OneDeOs
                                L9: Cds-CtH_Cds-CtOs
                                L9: Cds-CtH_Cds-CbOs
                                L9: Cds-CtH_Cds-COOs
                                L9: Cds-CtH_Cds-CdOs
                                L9: Cds-CtH_Cds-C=SOs
                            L8: Cds-CtH_Cds-OneDeSs
                                L9: Cds-CtH_Cds-CtSs
                                L9: Cds-CtH_Cds-CbSs
                                L9: Cds-CtH_Cds-COSs
                                L9: Cds-CtH_Cds-CdSs
                                L9: Cds-CtH_Cds-C=SSs
                        L7: Cds-CtH_Cds-TwoDe
                            L8: Cds-CtH_Cds-CtCt
                            L8: Cds-CtH_Cds-CtCb
                            L8: Cds-CtH_Cds-CtCO
                            L8: Cds-CtH_Cds-CbCb
                            L8: Cds-CtH_Cds-CbCO
                            L8: Cds-CtH_Cds-COCO
                            L8: Cds-CtH_Cds-CdCt
                            L8: Cds-CtH_Cds-CdCb
                            L8: Cds-CtH_Cds-CdCO
                            L8: Cds-CtH_Cds-CtC=S
                            L8: Cds-CtH_Cds-CbC=S
                            L8: Cds-CtH_Cds-COC=S
                            L8: Cds-CtH_Cds-CdCd
                            L8: Cds-CtH_Cds-CdC=S
                            L8: Cds-CtH_Cds-C=SC=S
                    L6: Cds-CbH_Cds
                        L7: Cds-CbH_Cds-HH
                        L7: Cds-CbH_Cds-CsH
                        L7: Cds-CbH_Cds-CsCs
                        L7: Cds-CbH_Cds-OsH
                        L7: Cds-CbH_Cds-OsCs
                        L7: Cds-CbH_Cds-OsOs
                        L7: Cds-CbH_Cds-SsH
                        L7: Cds-CbH_Cds-SsCs
                        L7: Cds-CbH_Cds-SsOs
                        L7: Cds-CbH_Cds-SsSs
                        L7: Cds-CbH_Cds-OneDe
                            L8: Cds-CbH_Cds-OneDeH
                                L9: Cds-CbH_Cds-CtH
                                L9: Cds-CbH_Cds-CbH
                                L9: Cds-CbH_Cds-COH
                                L9: Cds-CbH_Cds-CdH
                                L9: Cds-CbH_Cds-C=SH
                            L8: Cds-CbH_Cds-OneDeCs
                                L9: Cds-CbH_Cds-CtCs
                                L9: Cds-CbH_Cds-CbCs
                                L9: Cds-CbH_Cds-COCs
                                L9: Cds-CbH_Cds-CdCs
                                L9: Cds-CbH_Cds-C=SCs
                            L8: Cds-CbH_Cds-OneDeOs
                                L9: Cds-CbH_Cds-CtOs
                                L9: Cds-CbH_Cds-CbOs
                                L9: Cds-CbH_Cds-COOs
                                L9: Cds-CbH_Cds-CdOs
                                L9: Cds-CbH_Cds-C=SOs
                            L8: Cds-CbH_Cds-OneDeSs
                                L9: Cds-CbH_Cds-CtSs
                                L9: Cds-CbH_Cds-CbSs
                                L9: Cds-CbH_Cds-COSs
                                L9: Cds-CbH_Cds-CdSs
                                L9: Cds-CbH_Cds-C=SSs
                        L7: Cds-CbH_Cds-TwoDe
                            L8: Cds-CbH_Cds-CtCt
                            L8: Cds-CbH_Cds-CtCb
                            L8: Cds-CbH_Cds-CtCO
                            L8: Cds-CbH_Cds-CbCb
                            L8: Cds-CbH_Cds-CbCO
                            L8: Cds-CbH_Cds-COCO
                            L8: Cds-CbH_Cds-CdCt
                            L8: Cds-CbH_Cds-CdCb
                            L8: Cds-CbH_Cds-CdCO
                            L8: Cds-CbH_Cds-CtC=S
                            L8: Cds-CbH_Cds-CbC=S
                            L8: Cds-CbH_Cds-COC=S
                            L8: Cds-CbH_Cds-CdCd
                            L8: Cds-CbH_Cds-CdC=S
                            L8: Cds-CbH_Cds-C=SC=S
                    L6: Cds-COH_Cds
                    L6: Cds-CdH_Cds
                        L7: Cds-CdH_Cds-HH
                        L7: Cds-CdH_Cds-CsH
                        L7: Cds-CdH_Cds-CsCs
                        L7: Cds-CdH_Cds-OsH
                        L7: Cds-CdH_Cds-OsCs
                        L7: Cds-CdH_Cds-OsOs
                        L7: Cds-CdH_Cds-SsH
                        L7: Cds-CdH_Cds-SsCs
                        L7: Cds-CdH_Cds-SsOs
                        L7: Cds-CdH_Cds-SsSs
                        L7: Cds-CdH_Cds-OneDe
                            L8: Cds-CdH_Cds-OneDeH
                                L9: Cds-CdH_Cds-CtH
                                L9: Cds-CdH_Cds-CbH
                                L9: Cds-CdH_Cds-COH
                                L9: Cds-CdH_Cds-CdH
                                L9: Cds-CdH_Cds-C=SH
                            L8: Cds-CdH_Cds-OneDeCs
                                L9: Cds-CdH_Cds-CtCs
                                L9: Cds-CdH_Cds-CbCs
                                L9: Cds-CdH_Cds-COCs
                                L9: Cds-CdH_Cds-CdCs
                                L9: Cds-CdH_Cds-C=SCs
                            L8: Cds-CdH_Cds-OneDeOs
                                L9: Cds-CdH_Cds-CtOs
                                L9: Cds-CdH_Cds-CbOs
                                L9: Cds-CdH_Cds-COOs
                                L9: Cds-CdH_Cds-CdOs
                                L9: Cds-CdH_Cds-C=SOs
                            L8: Cds-CdH_Cds-OneDeSs
                                L9: Cds-CdH_Cds-CtSs
                                L9: Cds-CdH_Cds-CbSs
                                L9: Cds-CdH_Cds-COSs
                                L9: Cds-CdH_Cds-CdSs
                                L9: Cds-CdH_Cds-C=SSs
                        L7: Cds-CdH_Cds-TwoDe
                            L8: Cds-CdH_Cds-CtCt
                            L8: Cds-CdH_Cds-CtCb
                            L8: Cds-CdH_Cds-CtCO
                            L8: Cds-CdH_Cds-CbCb
                            L8: Cds-CdH_Cds-CbCO
                            L8: Cds-CdH_Cds-COCO
                            L8: Cds-CdH_Cds-CdCt
                            L8: Cds-CdH_Cds-CdCb
                            L8: Cds-CdH_Cds-CdCO
                            L8: Cds-CdH_Cds-CtC=S
                            L8: Cds-CdH_Cds-CbC=S
                            L8: Cds-CdH_Cds-COC=S
                            L8: Cds-CdH_Cds-CdCd
                            L8: Cds-CdH_Cds-CdC=S
                            L8: Cds-CdH_Cds-C=SC=S
                    L6: Cds-C=SH_Cds
                L5: Cds-OneDeCs_Cds
                    L6: Cds-CtCs_Cds
                        L7: Cds-CtCs_Cds-HH
                        L7: Cds-CtCs_Cds-CsH
                        L7: Cds-CtCs_Cds-CsCs
                        L7: Cds-CtCs_Cds-OsH
                        L7: Cds-CtCs_Cds-OsCs
                        L7: Cds-CtCs_Cds-OsOs
                        L7: Cds-CtCs_Cds-SsH
                        L7: Cds-CtCs_Cds-SsCs
                        L7: Cds-CtCs_Cds-SsOs
                        L7: Cds-CtCs_Cds-SsSs
                        L7: Cds-CtCs_Cds-OneDe
                            L8: Cds-CtCs_Cds-OneDeH
                                L9: Cds-CtCs_Cds-CtH
                                L9: Cds-CtCs_Cds-CbH
                                L9: Cds-CtCs_Cds-COH
                                L9: Cds-CtCs_Cds-CdH
                                L9: Cds-CtCs_Cds-C=SH
                            L8: Cds-CtCs_Cds-OneDeCs
                                L9: Cds-CtCs_Cds-CtCs
                                L9: Cds-CtCs_Cds-CbCs
                                L9: Cds-CtCs_Cds-COCs
                                L9: Cds-CtCs_Cds-CdCs
                                L9: Cds-CtCs_Cds-C=SCs
                            L8: Cds-CtCs_Cds-OneDeOs
                                L9: Cds-CtCs_Cds-CtOs
                                L9: Cds-CtCs_Cds-CbOs
                                L9: Cds-CtCs_Cds-COOs
                                L9: Cds-CtCs_Cds-CdOs
                                L9: Cds-CtCs_Cds-C=SOs
                            L8: Cds-CtCs_Cds-OneDeSs
                                L9: Cds-CtCs_Cds-CtSs
                                L9: Cds-CtCs_Cds-CbSs
                                L9: Cds-CtCs_Cds-COSs
                                L9: Cds-CtCs_Cds-CdSs
                                L9: Cds-CtCs_Cds-C=SSs
                        L7: Cds-CtCs_Cds-TwoDe
                            L8: Cds-CtCs_Cds-CtCt
                            L8: Cds-CtCs_Cds-CtCb
                            L8: Cds-CtCs_Cds-CtCO
                            L8: Cds-CtCs_Cds-CbCb
                            L8: Cds-CtCs_Cds-CbCO
                            L8: Cds-CtCs_Cds-COCO
                            L8: Cds-CtCs_Cds-CdCt
                            L8: Cds-CtCs_Cds-CdCb
                            L8: Cds-CtCs_Cds-CdCO
                            L8: Cds-CtCs_Cds-CtC=S
                            L8: Cds-CtCs_Cds-CbC=S
                            L8: Cds-CtCs_Cds-COC=S
                            L8: Cds-CtCs_Cds-CdCd
                            L8: Cds-CtCs_Cds-CdC=S
                            L8: Cds-CtCs_Cds-C=SC=S
                    L6: Cds-CbCs_Cds
                        L7: Cds-CbCs_Cds-HH
                        L7: Cds-CbCs_Cds-CsH
                        L7: Cds-CbCs_Cds-CsCs
                        L7: Cds-CbCs_Cds-OsH
                        L7: Cds-CbCs_Cds-OsCs
                        L7: Cds-CbCs_Cds-OsOs
                        L7: Cds-CbCs_Cds-SsH
                        L7: Cds-CbCs_Cds-SsCs
                        L7: Cds-CbCs_Cds-SsOs
                        L7: Cds-CbCs_Cds-SsSs
                        L7: Cds-CbCs_Cds-OneDe
                            L8: Cds-CbCs_Cds-OneDeH
                                L9: Cds-CbCs_Cds-CtH
                                L9: Cds-CbCs_Cds-CbH
                                L9: Cds-CbCs_Cds-COH
                                L9: Cds-CbCs_Cds-CdH
                                L9: Cds-CbCs_Cds-C=SH
                            L8: Cds-CbCs_Cds-OneDeCs
                                L9: Cds-CbCs_Cds-CtCs
                                L9: Cds-CbCs_Cds-CbCs
                                L9: Cds-CbCs_Cds-COCs
                                L9: Cds-CbCs_Cds-CdCs
                                L9: Cds-CbCs_Cds-C=SCs
                            L8: Cds-CbCs_Cds-OneDeOs
                                L9: Cds-CbCs_Cds-CtOs
                                L9: Cds-CbCs_Cds-CbOs
                                L9: Cds-CbCs_Cds-COOs
                                L9: Cds-CbCs_Cds-CdOs
                                L9: Cds-CbCs_Cds-C=SOs
                            L8: Cds-CbCs_Cds-OneDeSs
                                L9: Cds-CbCs_Cds-CtSs
                                L9: Cds-CbCs_Cds-CbSs
                                L9: Cds-CbCs_Cds-COSs
                                L9: Cds-CbCs_Cds-CdSs
                                L9: Cds-CbCs_Cds-C=SSs
                        L7: Cds-CbCs_Cds-TwoDe
                            L8: Cds-CbCs_Cds-CtCt
                            L8: Cds-CbCs_Cds-CtCb
                            L8: Cds-CbCs_Cds-CtCO
                            L8: Cds-CbCs_Cds-CbCb
                            L8: Cds-CbCs_Cds-CbCO
                            L8: Cds-CbCs_Cds-COCO
                            L8: Cds-CbCs_Cds-CdCt
                            L8: Cds-CbCs_Cds-CdCb
                            L8: Cds-CbCs_Cds-CdCO
                            L8: Cds-CbCs_Cds-CtC=S
                            L8: Cds-CbCs_Cds-CbC=S
                            L8: Cds-CbCs_Cds-COC=S
                            L8: Cds-CbCs_Cds-CdCd
                            L8: Cds-CbCs_Cds-CdC=S
                            L8: Cds-CbCs_Cds-C=SC=S
                    L6: Cds-COCs_Cds
                    L6: Cds-CdCs_Cds
                        L7: Cds-CdCs_Cds-HH
                        L7: Cds-CdCs_Cds-CsH
                        L7: Cds-CdCs_Cds-CsCs
                        L7: Cds-CdCs_Cds-OsH
                        L7: Cds-CdCs_Cds-OsCs
                        L7: Cds-CdCs_Cds-OsOs
                        L7: Cds-CdCs_Cds-SsH
                        L7: Cds-CdCs_Cds-SsCs
                        L7: Cds-CdCs_Cds-SsOs
                        L7: Cds-CdCs_Cds-SsSs
                        L7: Cds-CdCs_Cds-OneDe
                            L8: Cds-CdCs_Cds-OneDeH
                                L9: Cds-CdCs_Cds-CtH
                                L9: Cds-CdCs_Cds-CbH
                                L9: Cds-CdCs_Cds-COH
                                L9: Cds-CdCs_Cds-CdH
                                L9: Cds-CdCs_Cds-C=SH
                            L8: Cds-CdCs_Cds-OneDeCs
                                L9: Cds-CdCs_Cds-CtCs
                                L9: Cds-CdCs_Cds-CbCs
                                L9: Cds-CdCs_Cds-COCs
                                L9: Cds-CdCs_Cds-CdCs
                                L9: Cds-CdCs_Cds-C=SCs
                            L8: Cds-CdCs_Cds-OneDeOs
                                L9: Cds-CdCs_Cds-CtOs
                                L9: Cds-CdCs_Cds-CbOs
                                L9: Cds-CdCs_Cds-COOs
                                L9: Cds-CdCs_Cds-CdOs
                                L9: Cds-CdCs_Cds-C=SOs
                            L8: Cds-CdCs_Cds-OneDeSs
                                L9: Cds-CdCs_Cds-CtSs
                                L9: Cds-CdCs_Cds-CbSs
                                L9: Cds-CdCs_Cds-COSs
                                L9: Cds-CdCs_Cds-CdSs
                                L9: Cds-CdCs_Cds-C=SSs
                        L7: Cds-CdCs_Cds-TwoDe
                            L8: Cds-CdCs_Cds-CtCt
                            L8: Cds-CdCs_Cds-CtCb
                            L8: Cds-CdCs_Cds-CtCO
                            L8: Cds-CdCs_Cds-CbCb
                            L8: Cds-CdCs_Cds-CbCO
                            L8: Cds-CdCs_Cds-COCO
                            L8: Cds-CdCs_Cds-CdCt
                            L8: Cds-CdCs_Cds-CdCb
                            L8: Cds-CdCs_Cds-CdCO
                            L8: Cds-CdCs_Cds-CtC=S
                            L8: Cds-CdCs_Cds-CbC=S
                            L8: Cds-CdCs_Cds-COC=S
                            L8: Cds-CdCs_Cds-CdCd
                            L8: Cds-CdCs_Cds-CdC=S
                            L8: Cds-CdCs_Cds-C=SC=S
                    L6: Cds-C=SCs_Cds
                L5: Cds-OneDeSs_Cds
                    L6: Cds-CtSs_Cds
                    L6: Cds-CbSs_Cds
                    L6: Cds-COSs_Cds
                    L6: Cds-CdSs_Cds
                    L6: Cds-C=SSs_Cds
                L5: Cds-OneDeOs_Cds
                    L6: Cds-CtOs_Cds
                    L6: Cds-CbOs_Cds
                    L6: Cds-COOs_Cds
                    L6: Cds-CdOs_Cds
                    L6: Cds-C=SOs_Cds
            L4: Cds-TwoDe_Cds
                L5: Cds-CtCt_Cds
                    L6: Cds-CtCt_Cds-HH
                    L6: Cds-CtCt_Cds-CsH
                    L6: Cds-CtCt_Cds-CsCs
                    L6: Cds-CtCt_Cds-OsH
                    L6: Cds-CtCt_Cds-OsCs
                    L6: Cds-CtCt_Cds-OsOs
                    L6: Cds-CtCt_Cds-SsH
                    L6: Cds-CtCt_Cds-SsCs
                    L6: Cds-CtCt_Cds-SsOs
                    L6: Cds-CtCt_Cds-SsSs
                    L6: Cds-CtCt_Cds-OneDe
                        L7: Cds-CtCt_Cds-OneDeH
                            L8: Cds-CtCt_Cds-CtH
                            L8: Cds-CtCt_Cds-CbH
                            L8: Cds-CtCt_Cds-COH
                            L8: Cds-CtCt_Cds-CdH
                            L8: Cds-CtCt_Cds-C=SH
                        L7: Cds-CtCt_Cds-OneDeCs
                            L8: Cds-CtCt_Cds-CtCs
                            L8: Cds-CtCt_Cds-CbCs
                            L8: Cds-CtCt_Cds-COCs
                            L8: Cds-CtCt_Cds-CdCs
                            L8: Cds-CtCt_Cds-C=SCs
                        L7: Cds-CtCt_Cds-OneDeOs
                            L8: Cds-CtCt_Cds-CtOs
                            L8: Cds-CtCt_Cds-CbOs
                            L8: Cds-CtCt_Cds-COOs
                            L8: Cds-CtCt_Cds-CdOs
                            L8: Cds-CtCt_Cds-C=SOs
                        L7: Cds-CtCt_Cds-OneDeSs
                            L8: Cds-CtCt_Cds-CtSs
                            L8: Cds-CtCt_Cds-CbSs
                            L8: Cds-CtCt_Cds-COSs
                            L8: Cds-CtCt_Cds-CdSs
                            L8: Cds-CtCt_Cds-C=SSs
                    L6: Cds-CtCt_Cds-TwoDe
                        L7: Cds-CtCt_Cds-CtCt
                        L7: Cds-CtCt_Cds-CtCb
                        L7: Cds-CtCt_Cds-CtCO
                        L7: Cds-CtCt_Cds-CbCb
                        L7: Cds-CtCt_Cds-CbCO
                        L7: Cds-CtCt_Cds-COCO
                        L7: Cds-CtCt_Cds-CdCt
                        L7: Cds-CtCt_Cds-CdCb
                        L7: Cds-CtCt_Cds-CdCO
                        L7: Cds-CtCt_Cds-CtC=S
                        L7: Cds-CtCt_Cds-CbC=S
                        L7: Cds-CtCt_Cds-COC=S
                        L7: Cds-CtCt_Cds-CdCd
                        L7: Cds-CtCt_Cds-CdC=S
                        L7: Cds-CtCt_Cds-C=SC=S
                L5: Cds-CtCb_Cds
                L5: Cds-CtCO_Cds
                L5: Cds-CbCb_Cds
                L5: Cds-CbCO_Cds
                L5: Cds-COCO_Cds
                L5: Cds-CdCt_Cds
                    L6: Cds-CdCt_Cds-HH
                    L6: Cds-CdCt_Cds-CsH
                    L6: Cds-CdCt_Cds-CsCs
                    L6: Cds-CdCt_Cds-OsH
                    L6: Cds-CdCt_Cds-OsCs
                    L6: Cds-CdCt_Cds-OsOs
                    L6: Cds-CdCt_Cds-SsH
                    L6: Cds-CdCt_Cds-SsCs
                    L6: Cds-CdCt_Cds-SsOs
                    L6: Cds-CdCt_Cds-SsSs
                    L6: Cds-CdCt_Cds-OneDe
                        L7: Cds-CdCt_Cds-OneDeH
                            L8: Cds-CdCt_Cds-CtH
                            L8: Cds-CdCt_Cds-CbH
                            L8: Cds-CdCt_Cds-COH
                            L8: Cds-CdCt_Cds-CdH
                            L8: Cds-CdCt_Cds-C=SH
                        L7: Cds-CdCt_Cds-OneDeCs
                            L8: Cds-CdCt_Cds-CtCs
                            L8: Cds-CdCt_Cds-CbCs
                            L8: Cds-CdCt_Cds-COCs
                            L8: Cds-CdCt_Cds-CdCs
                            L8: Cds-CdCt_Cds-C=SCs
                        L7: Cds-CdCt_Cds-OneDeOs
                            L8: Cds-CdCt_Cds-CtOs
                            L8: Cds-CdCt_Cds-CbOs
                            L8: Cds-CdCt_Cds-COOs
                            L8: Cds-CdCt_Cds-CdOs
                            L8: Cds-CdCt_Cds-C=SOs
                        L7: Cds-CdCt_Cds-OneDeSs
                            L8: Cds-CdCt_Cds-CtSs
                            L8: Cds-CdCt_Cds-CbSs
                            L8: Cds-CdCt_Cds-COSs
                            L8: Cds-CdCt_Cds-CdSs
                            L8: Cds-CdCt_Cds-C=SSs
                    L6: Cds-CdCt_Cds-TwoDe
                        L7: Cds-CdCt_Cds-CtCt
                        L7: Cds-CdCt_Cds-CtCb
                        L7: Cds-CdCt_Cds-CtCO
                        L7: Cds-CdCt_Cds-CbCb
                        L7: Cds-CdCt_Cds-CbCO
                        L7: Cds-CdCt_Cds-COCO
                        L7: Cds-CdCt_Cds-CdCt
                        L7: Cds-CdCt_Cds-CdCb
                        L7: Cds-CdCt_Cds-CdCO
                        L7: Cds-CdCt_Cds-CtC=S
                        L7: Cds-CdCt_Cds-CbC=S
                        L7: Cds-CdCt_Cds-COC=S
                        L7: Cds-CdCt_Cds-CdCd
                        L7: Cds-CdCt_Cds-CdC=S
                        L7: Cds-CdCt_Cds-C=SC=S
                L5: Cds-CdCb_Cds
                L5: Cds-CdCO_Cds
                L5: Cds-CtC=S_Cds
                L5: Cds-CbC=S_Cds
                L5: Cds-COC=S_Cds
                L5: Cds-CdCd_Cds
                    L6: Cds-CdCd_Cds-HH
                    L6: Cds-CdCd_Cds-CsH
                    L6: Cds-CdCd_Cds-CsCs
                    L6: Cds-CdCd_Cds-OsH
                    L6: Cds-CdCd_Cds-OsCs
                    L6: Cds-CdCd_Cds-OsOs
                    L6: Cds-CdCd_Cds-SsH
                    L6: Cds-CdCd_Cds-SsCs
                    L6: Cds-CdCd_Cds-SsOs
                    L6: Cds-CdCd_Cds-SsSs
                    L6: Cds-CdCd_Cds-OneDe
                        L7: Cds-CdCd_Cds-OneDeH
                            L8: Cds-CdCd_Cds-CtH
                            L8: Cds-CdCd_Cds-CbH
                            L8: Cds-CdCd_Cds-COH
                            L8: Cds-CdCd_Cds-CdH
                            L8: Cds-CdCd_Cds-C=SH
                        L7: Cds-CdCd_Cds-OneDeCs
                            L8: Cds-CdCd_Cds-CtCs
                            L8: Cds-CdCd_Cds-CbCs
                            L8: Cds-CdCd_Cds-COCs
                            L8: Cds-CdCd_Cds-CdCs
                            L8: Cds-CdCd_Cds-C=SCs
                        L7: Cds-CdCd_Cds-OneDeOs
                            L8: Cds-CdCd_Cds-CtOs
                            L8: Cds-CdCd_Cds-CbOs
                            L8: Cds-CdCd_Cds-COOs
                            L8: Cds-CdCd_Cds-CdOs
                            L8: Cds-CdCd_Cds-C=SOs
                        L7: Cds-CdCd_Cds-OneDeSs
                            L8: Cds-CdCd_Cds-CtSs
                            L8: Cds-CdCd_Cds-CbSs
                            L8: Cds-CdCd_Cds-COSs
                            L8: Cds-CdCd_Cds-CdSs
                            L8: Cds-CdCd_Cds-C=SSs
                    L6: Cds-CdCd_Cds-TwoDe
                        L7: Cds-CdCd_Cds-CtCt
                        L7: Cds-CdCd_Cds-CtCb
                        L7: Cds-CdCd_Cds-CtCO
                        L7: Cds-CdCd_Cds-CbCb
                        L7: Cds-CdCd_Cds-CbCO
                        L7: Cds-CdCd_Cds-COCO
                        L7: Cds-CdCd_Cds-CdCt
                        L7: Cds-CdCd_Cds-CdCb
                        L7: Cds-CdCd_Cds-CdCO
                        L7: Cds-CdCd_Cds-CtC=S
                        L7: Cds-CdCd_Cds-CbC=S
                        L7: Cds-CdCd_Cds-COC=S
                        L7: Cds-CdCd_Cds-CdCd
                        L7: Cds-CdCd_Cds-CdC=S
                        L7: Cds-CdCd_Cds-C=SC=S
                L5: Cds-CdC=S_Cds
                L5: Cds-C=SC=S_Cds
            L4: Cds-OJH_Cds
                L5: Cds-OJH_Cds-HH
                L5: Cds-OJH_Cds-CsH
            L4: Cds-OJNonDe_Cds
                L5: Cds-OJCs_Cds-HH
            L4: Cds-OJDe_Cds
    L2: Ct_R
        L3: Ct_Ct
            L4: Ct-H_Ct-H
            L4: Ct-H_Ct-Cs
            L4: Ct-Cs_Ct-H
            L4: Ct-Cs_Ct-Cs
            L4: Ct-H_Ct-De
                L5: Ct-H_Ct-Ct
                L5: Ct-H_Ct-Cb
                L5: Ct-H_Ct-CO
                L5: Ct-H_Ct-Cd
                L5: Ct-H_Ct-C=S
            L4: Ct-Cs_Ct-De
                L5: Ct-Cs_Ct-Ct
                L5: Ct-Cs_Ct-Cb
                L5: Ct-Cs_Ct-CO
                L5: Ct-Cs_Ct-Cd
                L5: Ct-Cs_Ct-C=S
            L4: Ct-De_Ct-H
                L5: Ct-Cb_Ct-H
                L5: Ct-CO_Ct-H
                L5: Ct-Cd_Ct-H
                L5: Ct-Ct_Ct-H
                L5: Ct-C=S_Ct-H
            L4: Ct-De_Ct-Cs
                L5: Ct-Cb_Ct-Cs
                L5: Ct-CO_Ct-Cs
                L5: Ct-Cd_Ct-Cs
                L5: Ct-Ct_Ct-Cs
                L5: Ct-C=S_Ct-Cs
            L4: Ct-De_Ct-De
                L5: Ct-Ct_Ct-Ct
                L5: Ct-Cd_Ct-Ct
                L5: Ct-Ct_Ct-Cd
                L5: Ct-Cd_Ct-Cd
        L3: Ct_Nt
            L4: Ct_N3t
                L5: Ct-H_N3t
                L5: Ct-NonDe_N3t
                L5: Ct-OneDe_N3t
            L4: Ct_N5t
    L2: Od_R
        L3: Od_Nd
            L4: Od_N3d
            L4: Od_N5d
        L3: Od_Cdd
            L4: Od_Cdd-Od
        L3: Od_Cd
            L4: Od_Cd-CsH
    L2: Nd_R
        L3: N1d_R
        L3: N3d_R
            L4: N3d_Cd
                L5: N3d_Cdd
                L5: N3d_Cds
                    L6: N3d-H_Cds
                        L7: N3d-H_Cds-HH
                        L7: N3d-H_Cds-NonDeH
                        L7: N3d-H_Cds-NonDe2
                    L6: N3d-NonDe_Cds
                    L6: N3d-OneDe_Cds
            L4: N3d_Od
                L5: N3d-H_Od
                L5: N3d-NonDe_Od
                L5: N3d-OneDe_Od
            L4: N3d_Nd
                L5: N3d_N3d
                    L6: N3d-H_N3d
                        L7: N3d-H_N3d-H
                        L7: N3d-H_N3d-NonDe
                        L7: N3d-H_N3d-OneDe
                    L6: N3d-NonDe_N3d
                    L6: N3d-OneDe_N3d
                L5: N3d_N5d
    L2: Nt_R
        L3: N3t_R
            L4: N3t_Ct
                L5: N3t_Ct-H
                L5: N3t_Ct-NonDe
                L5: N3t_Ct-OneDe
            L4: N3t_N3t
        L3: N5t_R
    L2: Sd_R
        L3: Sd_Cdd
            L4: Sd_Cdd-Sd
        L3: Sd_Cd
            L4: Sd_Cds-HH
            L4: Sd_Cds-CsH
            L4: Sd_Cds-OsH
            L4: Sd_Cds-OsCs
            L4: Sd_Cds-CsCs
            L4: Sd_Cds-OneDeH
                L5: Sd_Cds-CtH
                L5: Sd_Cds-CbH
                L5: Sd_Cds-COH
                L5: Sd_Cds-CdH
                L5: Sd_Cds-C=SH
            L4: Sd_Cds-OneDeCs
                L5: Sd_Cds-CtCs
                L5: Sd_Cds-CbCs
                L5: Sd_Cds-COCs
                L5: Sd_Cds-CdCs
                L5: Sd_Cds-C=SCs
            L4: Sd_Cds-TwoDe
                L5: Sd_Cds-CtCt
                L5: Sd_Cds-CtCb
                L5: Sd_Cds-CtCO
                L5: Sd_Cds-CbCb
                L5: Sd_Cds-CbCO
                L5: Sd_Cds-COCO
                L5: Sd_Cds-CdCt
                L5: Sd_Cds-CdCb
                L5: Sd_Cds-CdCO
                L5: Sd_Cds-CtC=S
                L5: Sd_Cds-CbC=S
                L5: Sd_Cds-COC=S
                L5: Sd_Cds-CdCd
                L5: Sd_Cds-CdC=S
                L5: Sd_Cds-C=SC=S
L1: YJ
    L2: HJ
    L2: CJ
        L3: CbJ
        L3: CtJ
            L4: CtJ_Ct
            L4: CtJ_N3t
        L3: C2b
        L3: C=SJ
            L4: C=SJ-H
            L4: C=SJ-Cs
            L4: C=SJ-Ct
            L4: C=SJ-Cb
            L4: C=SJ-CO
            L4: C=SJ-Os
            L4: C=SJ-Ss
            L4: C=SJ-Cd
            L4: C=SJ-C=S
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CsJ
            L4: CsJ-HHH
            L4: CsJ-CsHH
            L4: CsJ-CsCsH
            L4: CsJ-CsCsCs
            L4: CsJ-OsHH
            L4: CsJ-OsCsH
            L4: CsJ-OsCsCs
            L4: CsJ-OsOsH
            L4: CsJ-OsOsCs
            L4: CsJ-OsOsOs
            L4: CsJ-SsHH
            L4: CsJ-SsCsH
            L4: CsJ-SsCsCs
            L4: CsJ-SsSsH
            L4: CsJ-SsSsCs
            L4: CsJ-SsSsSs
            L4: CsJ-NsHH
            L4: CsJ-NsCsH
            L4: CsJ-OneDe
                L5: CsJ-OneDeHH
                    L6: CsJ-CtHH
                    L6: CsJ-CbHH
                    L6: CsJ-COHH
                    L6: CsJ-CdHH
                    L6: CsJ-C=SHH
                L5: CsJ-OneDeCsH
                    L6: CsJ-CtCsH
                    L6: CsJ-CbCsH
                    L6: CsJ-COCsH
                    L6: CsJ-CdCsH
                    L6: CsJ-C=SCsH
                L5: CsJ-OneDeOsH
                L5: CsJ-OneDeSsH
                L5: CsJ-OneDeCsCs
                    L6: CsJ-CtCsCs
                    L6: CsJ-CbCsCs
                    L6: CsJ-COCsCs
                    L6: CsJ-CdCsCs
                    L6: CsJ-C=SCsCs
                L5: CsJ-OneDeOsCs
                L5: CsJ-OneDeSsCs
                L5: CsJ-OneDeOsOs
                L5: CsJ-OneDeOsSs
                L5: CsJ-OneDeSsSs
                L5: CsJ-OneDeNsH
                L5: CsJ-OneDeNsCs
            L4: CsJ-TwoDe
                L5: CsJ-TwoDeH
                    L6: CsJ-CtCtH
                    L6: CsJ-CtCbH
                    L6: CsJ-CtCOH
                    L6: CsJ-CbCbH
                    L6: CsJ-CbCOH
                    L6: CsJ-COCOH
                    L6: CsJ-CdCtH
                    L6: CsJ-CdCbH
                    L6: CsJ-CdCOH
                    L6: CsJ-CtC=SH
                    L6: CsJ-CbC=SH
                    L6: CsJ-COC=SH
                    L6: CsJ-CdCdH
                    L6: CsJ-CdC=SH
                    L6: CsJ-C=SC=SH
                L5: CsJ-TwoDeCs
                    L6: CsJ-CtCtCs
                    L6: CsJ-CtCbCs
                    L6: CsJ-CtCOCs
                    L6: CsJ-CbCbCs
                    L6: CsJ-CbCOCs
                    L6: CsJ-COCOCs
                    L6: CsJ-CdCtCs
                    L6: CsJ-CdCbCs
                    L6: CsJ-CdCOCs
                    L6: CsJ-CtC=SCs
                    L6: CsJ-CbC=SCs
                    L6: CsJ-COC=SCs
                    L6: CsJ-CdCdCs
                    L6: CsJ-CdC=SCs
                    L6: CsJ-C=SC=SCs
                L5: CsJ-TwoDeOs
                L5: CsJ-TwoDeSs
            L4: CsJ-ThreeDe
        L3: CdsJ=Cdd
        L3: CdsJ
            L4: CdsJ-H
            L4: CdsJ-Cs
            L4: CdsJ-Ct
            L4: CdsJ-Cb
            L4: CdsJ-CO
            L4: CdsJ-Os
            L4: CdsJ-Ss
            L4: CdsJ-Cd
            L4: CdsJ-C=S
    L2: OJ
        L3: OJ_pri
        L3: OJ_sec
            L4: OJ-NonDe
                L5: OJ-Cs
                L5: OJ-Os
                L5: OJ-Ns
            L4: OJ-OneDe
                L5: OJ-OneDeN
                    L6: OJ-NO
        L3: O2b
    L2: SJ
        L3: SsJ
            L4: SsJ-H
            L4: SsJ-Cs
            L4: SsJ-Ss
            L4: SsJ-OneDe
                L5: SsJ-Ct
                L5: SsJ-Cb
                L5: SsJ-CO
                L5: SsJ-Cd
                L5: SsJ-C=S
    L2: NJ
        L3: N3J
            L4: N3sJ
                L5: NH2J
                L5: N3sJ-NonDeH
                    L6: N3sJ-CsH
                    L6: N3sJ-OsH
                    L6: N3sJ-NsH
                L5: N3sJ-NonDe2
                L5: N3sJ-OneDeH
                L5: N3sJ-OneDeCs
                L5: N3sJ-TwoDe
            L4: N3dJ
                L5: N3dJ_C
                L5: N3dJ_O
                L5: N3dJ_N
    L2: Y_1centerbirad
        L3: O_(T)
        L3: SJJ_(T)
        L3: CO_(T)
        L3: NH_(T)
        L3: CH2_(T)
    L2: Y_1centertrirad
        L3: N_(Q)
        L3: N_(D)
        L3: CH_(Q)
        L3: CH_(D)
    L2: Y_1centerquadrad
        L3: C_(V)
        L3: C_(T)
        L3: C_(S)
"""
)

forbidden(
    label = "O2d",
    multiplicity = [1],
    group = 
"""
1 *1 O U0 {2,D}
2 *2 O U0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

