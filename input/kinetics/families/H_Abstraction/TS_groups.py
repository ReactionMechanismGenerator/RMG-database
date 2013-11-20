#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "X_H_or_Xrad_H",
    group = "OR{X_H, Xrad_H}",
    distances = DistanceData(
        distances = {'d12': 1.199551, 'd13': 2.396753, 'd23': 1.201265},
        uncertainties = {'d12': 0.127042, 'd13': 0.142775, 'd23': 0.118363},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=170 label="H_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 3,
    label = "X_H",
    group = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.0, 'd13': -0.0, 'd23': 0.0},
        uncertainties = {'d12': 0.127042, 'd13': 0.142775, 'd23': 0.118363},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=170 label="H_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 4,
    label = "H2",
    group = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.196267, 'd13': -0.14102, 'd23': 0.052908},
        uncertainties = {'d12': 0.18917, 'd13': 0.165938, 'd23': 0.089276},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 28 distances.
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 5,
    label = "Ct_H",
    group = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 6,
    label = "O_H",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.009666, 'd13': -0.025176, 'd23': 0.001104},
        uncertainties = {'d12': 0.141933, 'd13': 0.1348, 'd23': 0.133145},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 7,
    label = "O_pri",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.176593, 'd13': 0.023996, 'd23': -0.110937},
        uncertainties = {'d12': 0.897568, 'd13': 1.191392, 'd23': 0.509759},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 8,
    label = "O_sec",
    group = 
"""
1 *1 O   0 {2,S} {3,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.049296, 'd13': -0.035638, 'd23': 0.024942},
        uncertainties = {'d12': 0.151009, 'd13': 0.13579, 'd23': 0.146452},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 11 distances.
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 9,
    label = "O/H/NonDeC",
    group = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.010302, 'd13': -0.075463, 'd23': -0.037431},
        uncertainties = {'d12': 0.093805, 'd13': 0.172878, 'd23': 0.123928},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 10,
    label = "O/H/NonDeO",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.062244, 'd13': 0.003444, 'd23': 0.068338},
        uncertainties = {'d12': 0.235693, 'd13': 0.157995, 'd23': 0.164828},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 11,
    label = "H2O2",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.049405, 'd13': 0.018836, 'd23': 0.071105},
        uncertainties = {'d12': 0.204041, 'd13': 0.18577, 'd23': 0.125204},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 12,
    label = "ROOH_pri",
    group = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 13,
    label = "ROOH_sec",
    group = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 14,
    label = "ROOH_ter",
    group = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7 *2 H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 15,
    label = "O/H/OneDe",
    group = 
"""
1 *1 O                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.136416, 'd13': -0.188007, 'd23': -0.047427},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 16,
    label = "Orad_O_H",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 1 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 17,
    label = "S_H",
    group = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 18,
    label = "S_pri",
    group = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 19,
    label = "S_sec",
    group = 
"""
1 *1 S   0 {2,S} {3,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 20,
    label = "S/H/NonDeC",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 21,
    label = "S/H/NonDeS",
    group = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 22,
    label = "S/H/OneDe",
    group = 
"""
1 *1 S                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 23,
    label = "S/H/Cd",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 24,
    label = "S/H/CS",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {4,D}
4    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 25,
    label = "S/H/Ct",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 26,
    label = "S/H/Cb",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 27,
    label = "S/H/CO",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 28,
    label = "Cd_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.219716, 'd13': 0.020827, 'd23': -0.201477},
        uncertainties = {'d12': 0.100931, 'd13': 0.173922, 'd23': 0.266221},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=170 label="H_rad">]
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 29,
    label = "Cd_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.229961, 'd13': 0.050938, 'd23': -0.181388},
        uncertainties = {'d12': 0.131466, 'd13': 0.117498, 'd23': 0.242596},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=170 label="H_rad">]
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 30,
    label = "Cd_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    C   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.197519, 'd13': -0.044414, 'd23': -0.245001},
        uncertainties = {'d12': 0.646496, 'd13': 1.74214, 'd23': 2.417364},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 31,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.197519, 'd13': -0.044414, 'd23': -0.245001},
        uncertainties = {'d12': 0.646496, 'd13': 1.74214, 'd23': 2.417364},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 32,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 33,
    label = "Cd/H/NonDeS",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 34,
    label = "Cd/H/OneDe",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 35,
    label = "Cd/H/Cd",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 36,
    label = "Cd/H/CS",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 37,
    label = "Cd/H/Ct",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 38,
    label = "Cd/H/Cb",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 39,
    label = "Cd/H/CO",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 40,
    label = "Cb_H",
    group = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.275559, 'd13': -0.005162, 'd23': -0.28397},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 41,
    label = "CO_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.010397, 'd13': 0.052002, 'd23': 0.05954},
        uncertainties = {'d12': 0.645892, 'd13': 1.742139, 'd23': 2.417238},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 42,
    label = "CO_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.002362, 'd13': 0.024632, 'd23': 0.019094},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 43,
    label = "CO_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    O   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.023156, 'd13': 0.079372, 'd23': 0.099985},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 44,
    label = "CO/H/NonDe",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.023156, 'd13': 0.079372, 'd23': 0.099985},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 45,
    label = "InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {6,S}
2     O 0 {1,D}
3     C 0 {1,S} {4,S} {7,S} {8,S}
4     C 0 {3,S} {5,S} {9,S} {10,S}
5     C 0 {4,S} {11,S} {12,S} {13,S}
6  *2 H 0 {1,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {5,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 46,
    label = "CO/H/OneDe",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    O                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 47,
    label = "CS_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 48,
    label = "CS_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 49,
    label = "CS_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    S   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 50,
    label = "CS/H/NonDeC",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 51,
    label = "CS/H/NonDeO",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 52,
    label = "CS/H/NonDeS",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 53,
    label = "CS/H/OneDe",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    S                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 54,
    label = "CS/H/Cd",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 55,
    label = "CS/H/CS",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 56,
    label = "CS/H/Ct",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 57,
    label = "CS/H/Cb",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 58,
    label = "CS/H/CO",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 59,
    label = "Cs_H",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
5    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.145536, 'd13': 0.128916, 'd23': -0.020001},
        uncertainties = {'d12': 0.083885, 'd13': 0.139467, 'd23': 0.107773},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 38 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 60,
    label = "C_methane",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.182437, 'd13': 0.194935, 'd23': 0.009219},
        uncertainties = {'d12': 0.115979, 'd13': 0.189784, 'd23': 0.125937},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 8 distances.
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 61,
    label = "C_pri",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.128267, 'd13': 0.074021, 'd23': -0.058331},
        uncertainties = {'d12': 0.062134, 'd13': 0.137022, 'd23': 0.123157},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 20 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 62,
    label = "C/H3/Cs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.1339, 'd13': 0.084852, 'd23': -0.053301},
        uncertainties = {'d12': 0.060891, 'd13': 0.128061, 'd23': 0.088026},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 63,
    label = "InChI=1/C2H6/c1-2/h1-2H3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.127007, 'd13': 0.167871, 'd23': 0.037958},
        uncertainties = {'d12': 0.107258, 'd13': 0.214329, 'd23': 0.139775},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 64,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma",
    group = 
"""
1  *1 C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6  *2 H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 65,
    label = "C/H3/Cd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.015377, 'd13': -0.036608, 'd23': -0.053398},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 66,
    label = "C/H3/CS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 67,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3",
    group = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.015377, 'd13': -0.036608, 'd23': -0.053398},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 68,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3",
    group = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 69,
    label = "InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,D} {8,S}
3     C 0 {2,D} {4,S} {9,S}
4     C 0 {3,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 70,
    label = "C/H3/Ct",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 71,
    label = "C/H3/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 72,
    label = "C/H3/CO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 73,
    label = "C/H3/O",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.111592, 'd13': -0.064442, 'd23': -0.178955},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 74,
    label = "C/H3/S",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 75,
    label = "C_sec",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.140588, 'd13': 0.160968, 'd23': 0.018105},
        uncertainties = {'d12': 0.130244, 'd13': 0.166538, 'd23': 0.104049},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 76,
    label = "C/H2/NonDeC",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.130202, 'd13': 0.08508, 'd23': -0.047543},
        uncertainties = {'d12': 0.187028, 'd13': 0.148148, 'd23': 0.101609},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 77,
    label = "InChI=1/C3H8/c1-3-2/h3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *1 C 0 {1,S} {3,S} {7,S} {8,S}
3     C 0 {2,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 78,
    label = "C/H2/NonDeO",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    H        0 {1,S}
4    O        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.148481, 'd13': 0.218643, 'd23': 0.067997},
        uncertainties = {'d12': 0.150052, 'd13': 0.26843, 'd23': 0.162386},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 79,
    label = "C/H2/CsO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.132454, 'd13': 0.213852, 'd23': 0.077005},
        uncertainties = {'d12': 0.285807, 'd13': 0.376315, 'd23': 0.21115},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 80,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *1 C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10 *2 H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 81,
    label = "C/H2/O2",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.172522, 'd13': 0.22583, 'd23': 0.054485},
        uncertainties = {'d12': 0.679331, 'd13': 1.888494, 'd23': 1.196436},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 82,
    label = "C/H2/NonDeS",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    H        0 {1,S}
4    S        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 83,
    label = "C/H2/CsS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 84,
    label = "C/H2/OneDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 85,
    label = "C/H2/OneDeC",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 86,
    label = "C/H2/CdCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 87,
    label = "C/H2/CSCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 88,
    label = "C/H2/CtCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 89,
    label = "C/H2/CbCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 90,
    label = "C/H2/COCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 91,
    label = "InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     O 0 {3,D}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 92,
    label = "InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 93,
    label = "C/H2/OneDeO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 94,
    label = "C/H2/OneDeS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 95,
    label = "C/H2/CdS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 96,
    label = "C/H2/CtS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 97,
    label = "C/H2/TwoDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cd,Ct,CO,Cb,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 98,
    label = "C/H2/CdCd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 99,
    label = "C/H2/CdCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 100,
    label = "C/H2/CSCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cd 0 {1,S} {7,D}
6    S  0 {4,D}
7    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 101,
    label = "C/H2/CdCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 102,
    label = "C/H2/CtCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 103,
    label = "C/H2/CdCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 104,
    label = "C/H2/CbCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 105,
    label = "C/H2/CdCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 106,
    label = "C/H2/COCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 107,
    label = "C/H2/CtCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 108,
    label = "C/H2/CtCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 109,
    label = "C/H2/CtCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 110,
    label = "C/H2/CbCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 111,
    label = "C/H2/CbCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 112,
    label = "C/H2/COCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 113,
    label = "C/H2/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 114,
    label = "C_ter",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 115,
    label = "C/H/NonDeC",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 116,
    label = "C/H/Cs3",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 117,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 118,
    label = "C/H/NDMustO",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 119,
    label = "C/H/Cs2O",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 120,
    label = "C/H/CsO2",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 121,
    label = "C/H/O3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 122,
    label = "C/H/NDMustS",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    S      0 {1,S}
4    {Cs,S} 0 {1,S}
5    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 123,
    label = "C/H/Cs2S",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 124,
    label = "C/H/CsS2",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 125,
    label = "C/H/S3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
5    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 126,
    label = "C/H/NDMustOS",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    O        0 {1,S}
4    S        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 127,
    label = "C/H/CsOS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 128,
    label = "C/H/OneDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 129,
    label = "C/H/Cs2",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 130,
    label = "C/H/Cs2Cd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 131,
    label = "C/H/Cs2CS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
6    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 132,
    label = "C/H/Cs2Ct",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 133,
    label = "C/H/Cs2Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 134,
    label = "C/H/Cs2CO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 135,
    label = "InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     O 0 {3,D}
5     C 0 {2,S} {11,S} {12,S} {13,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {5,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 136,
    label = "C/H/CsO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 137,
    label = "C/H/CsS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 138,
    label = "C/H/CdCsS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 139,
    label = "C/H/CtCsS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 140,
    label = "C/H/OO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
5    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 141,
    label = "C/H/OS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 142,
    label = "C/H/SS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 143,
    label = "C/H/TwoDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 144,
    label = "C/H/Cs",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 145,
    label = "C/H/CdCd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 146,
    label = "C/H/CdCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 147,
    label = "C/H/CSCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {6,D}
4    Cd 0 {1,S} {7,D}
5    Cs 0 {1,S}
6    S  0 {3,D}
7    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 148,
    label = "C/H/CdCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 149,
    label = "C/H/CtCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 150,
    label = "C/H/CdCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 151,
    label = "C/H/CbCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 152,
    label = "C/H/CdCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 153,
    label = "C/H/COCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 154,
    label = "C/H/CtCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 155,
    label = "C/H/CtCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 156,
    label = "C/H/CtCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 157,
    label = "C/H/CbCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 158,
    label = "C/H/CbCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 159,
    label = "C/H/COCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 160,
    label = "C/H/TDMustO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 161,
    label = "C/H/TDMustS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 162,
    label = "C/H/ThreeDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 163,
    label = "C/H/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 164,
    label = "Xrad_H",
    group = 
"""
1 *1 R 1 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 165,
    label = "Srad_H",
    group = 
"""
1 *1 S 1 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 166,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 {Cs,Cd,CO,O,S} 2T
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 167,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O 2T
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 168,
    label = "CH2_triplet",
    group = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 169,
    label = "Y_rad",
    group = 
"""
1 *3 R 1
""",
    distances = DistanceData(
        distances = {'d12': -0.0, 'd13': 0.0, 'd23': 0.0},
        uncertainties = {'d12': 0.127042, 'd13': 0.142775, 'd23': 0.118363},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=170 label="H_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 170,
    label = "H_rad",
    group = 
"""
1 *3 H 1
""",
    distances = DistanceData(
        distances = {'d12': 0.053916, 'd13': -0.145426, 'd23': -0.201781},
        uncertainties = {'d12': 0.107306, 'd13': 0.15555, 'd23': 0.175088},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 28 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=15 label="O/H/OneDe">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 171,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 {Ct,Os,Ss} 1 {2,{S,T}}
2    {Ct,Os,Ss} 1 {1,{S,T}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 172,
    label = "O2b",
    group = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 173,
    label = "C2b",
    group = 
"""
1 *3 C 1 {2,T}
2    C 1 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 174,
    label = "Ct_rad",
    group = 
"""
1 *3 C 1 {2,T}
2    C 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 175,
    label = "O_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.000752, 'd13': -0.026769, 'd23': -0.010727},
        uncertainties = {'d12': 0.139863, 'd13': 0.142507, 'd23': 0.10746},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 176,
    label = "O_pri_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.10996, 'd13': 0.023561, 'd23': 0.175202},
        uncertainties = {'d12': 0.517736, 'd13': 1.195754, 'd23': 0.914752},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 177,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.023817, 'd13': -0.037255, 'd23': -0.049463},
        uncertainties = {'d12': 0.154028, 'd13': 0.14522, 'd23': 0.109172},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 11 distances.
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 178,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.037215, 'd13': -0.075717, 'd23': -0.010755},
        uncertainties = {'d12': 0.131249, 'd13': 0.17387, 'd23': 0.091706},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 179,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4  *3 O 1 {3,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 180,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.068519, 'd13': 0.002407, 'd23': -0.063499},
        uncertainties = {'d12': 0.183808, 'd13': 0.180621, 'd23': 0.16368},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 181,
    label = "OOCH3",
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.045152, 'd13': -0.126295, 'd23': -0.170614},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 182,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.047552, 'd13': -0.189476, 'd23': -0.137794},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 183,
    label = "InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3",
    group = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D} {5,S}
5 *3 O 1 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 184,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o",
    group = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2    C 0 {1,S} {3,D} {8,S}
3    C 0 {2,D} {4,S} {9,S}
4 *3 O 1 {3,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 185,
    label = "S_rad",
    group = 
"""
1 *3 S 1 {2,S}
2    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 186,
    label = "S_pri_rad",
    group = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 187,
    label = "S_sec_rad",
    group = 
"""
1 *3 S   1 {2,S}
2    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 188,
    label = "S_rad/NonDeC",
    group = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 189,
    label = "S_rad/NonDeS",
    group = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 190,
    label = "S_rad/OneDe",
    group = 
"""
1 *3 S                1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 191,
    label = "S_rad/Cd",
    group = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 192,
    label = "S_rad/CS",
    group = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S} {3,D}
3    S  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 193,
    label = "S_rad/Ct",
    group = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 194,
    label = "S_rad/Cb",
    group = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 195,
    label = "S_rad/CO",
    group = 
"""
1 *3 S  1 {2,S}
2    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 196,
    label = "Cd_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.201452, 'd13': 0.01957, 'd23': 0.218397},
        uncertainties = {'d12': 0.22763, 'd13': 0.165574, 'd23': 0.076267},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 197,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.181294, 'd13': 0.049779, 'd23': 0.22867},
        uncertainties = {'d12': 0.129489, 'd13': 0.101755, 'd23': 0.080366},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 198,
    label = "InChI=1/C2H3/c1-2/h1H,2H2",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D} {4,S} {5,S}
3    H 0 {1,S}
4    H 0 {2,S}
5    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.098899, 'd13': 0.107464, 'd23': 0.203974},
        uncertainties = {'d12': 0.642307, 'd13': 0.513985, 'd23': 0.542584},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 199,
    label = "InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4  *3 C 1 {3,D} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 200,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    C   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.245126, 'd13': -0.045883, 'd23': 0.196141},
        uncertainties = {'d12': 2.351187, 'd13': 1.689347, 'd23': 0.633811},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 201,
    label = "Cd_rad/NonDeC",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.245126, 'd13': -0.045883, 'd23': 0.196141},
        uncertainties = {'d12': 2.351187, 'd13': 1.689347, 'd23': 0.633811},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 202,
    label = "InChI=1/C3H5/c1-3-2/h1H2,2H3",
    group = 
"""
1    C 0 {2,D} {4,S} {5,S}
2 *3 C 1 {1,D} {3,S}
3    C 0 {2,S} {6,S} {7,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {3,S}
7    H 0 {3,S}
8    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.243748, 'd13': -0.046022, 'd23': 0.194587},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 203,
    label = "InChI=1/C4H7/c1-3-4-2/h3H,1-2H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,D}
3     C 0 {2,D} {4,S} {8,S}
4     C 0 {3,S} {9,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.246503, 'd13': -0.045744, 'd23': 0.197696},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 204,
    label = "Cd_rad/NonDeO",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 205,
    label = "Cd_rad/NonDeS",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 206,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    C                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 207,
    label = "Cd_rad/Cd",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 208,
    label = "Cd_rad/CS",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S} {4,D}
4    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 209,
    label = "Cd_rad/Ct",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 210,
    label = "Cd_rad/Cb",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 211,
    label = "Cd_rad/CO",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 212,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    distances = DistanceData(
        distances = {'d12': -0.284094, 'd13': -0.006631, 'd23': 0.274181},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 213,
    label = "CO_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.059415, 'd13': 0.050533, 'd23': -0.011774},
        uncertainties = {'d12': 2.351187, 'd13': 1.689347, 'd23': 0.633811},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 214,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.01897, 'd13': 0.023163, 'd23': 0.000985},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 215,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.099861, 'd13': 0.077904, 'd23': -0.024533},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 216,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.099861, 'd13': 0.077904, 'd23': -0.024533},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 217,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    O                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 218,
    label = "CS_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 219,
    label = "CS_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 220,
    label = "CS_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    S   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 221,
    label = "CS_rad/NonDe",
    group = 
"""
1 *3 C        1 {2,D} {3,S}
2    S        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 222,
    label = "CS_rad/Cs",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 223,
    label = "CS_rad/O",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 224,
    label = "CS_rad/S",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 225,
    label = "CS_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    S                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 226,
    label = "CS_rad/Cd",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 227,
    label = "CS_rad/CS",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cd 0 {1,S} {4,D}
4    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 228,
    label = "CS_rad/Ct",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 229,
    label = "CS_rad/Cb",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 230,
    label = "CS_rad/CO",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 231,
    label = "Cs_rad",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.018845, 'd13': 0.127626, 'd23': 0.142981},
        uncertainties = {'d12': 0.12533, 'd13': 0.147148, 'd23': 0.090977},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 38 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 232,
    label = "C_methyl",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.010519, 'd13': 0.194372, 'd23': 0.180481},
        uncertainties = {'d12': 0.140279, 'd13': 0.197183, 'd23': 0.150891},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 8 distances.
[<Entry index=29 label="Cd_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 233,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.056667, 'd13': 0.074301, 'd23': 0.126788},
        uncertainties = {'d12': 0.150485, 'd13': 0.148771, 'd23': 0.063485},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 20 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 234,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.051628, 'd13': 0.084973, 'd23': 0.132254},
        uncertainties = {'d12': 0.12943, 'd13': 0.143201, 'd23': 0.062654},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 235,
    label = "InChI=1/C2H5/c1-2/h1H2,2H3",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.037001, 'd13': 0.165427, 'd23': 0.125356},
        uncertainties = {'d12': 0.144598, 'd13': 0.218684, 'd23': 0.106611},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 236,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2",
    group = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.204566, 'd13': -0.062728, 'd23': 0.138872},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 237,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2  *3 C 1 {4,S} {9,S} {10,S}
3     C 0 {1,S} {4,S} {11,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 238,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3",
    group = 
"""
1  *3 C 1 {3,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,S} {11,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 239,
    label = "InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3",
    group = 
"""
1  *3 C 1 {4,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4     C 0 {1,S} {2,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.210651, 'd13': -0.057039, 'd23': 0.150333},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 240,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {5,S} {8,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 241,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.053523, 'd13': -0.038077, 'd23': 0.013999},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 242,
    label = "InChI=1/C3H5/c1-3-2/h3H,1-2H2",
    group = 
"""
1 *3 C 1 {2,S} {4,S} {5,S}
2    C 0 {1,S} {3,D} {6,S}
3    C 0 {2,D}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.053523, 'd13': -0.038077, 'd23': 0.013999},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 243,
    label = "InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3",
    group = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S} {7,S} {8,S}
4     C 0 {2,S} {9,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 244,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 245,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 246,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 247,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.179079, 'd13': -0.065911, 'd23': 0.110215},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 248,
    label = "C_rad/H2/S",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 249,
    label = "C_sec_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.019772, 'd13': 0.159543, 'd23': 0.137355},
        uncertainties = {'d12': 0.103143, 'd13': 0.169406, 'd23': 0.127546},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 250,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.047323, 'd13': 0.084112, 'd23': 0.128963},
        uncertainties = {'d12': 0.096371, 'd13': 0.154797, 'd23': 0.185284},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 251,
    label = "InChI=1/C3H7/c1-3-2/h3H,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *3 C 1 {1,S} {3,S} {7,S}
3     C 0 {2,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 252,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 253,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3  *3 C 1 {2,S} {4,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 254,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2     C 0 {4,S} {9,S} {10,S} {11,S}
3  *3 C 1 {1,S} {4,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 255,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.068803, 'd13': 0.214666, 'd23': 0.143488},
        uncertainties = {'d12': 0.163616, 'd13': 0.270752, 'd23': 0.14425},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 256,
    label = "C_rad/H/CsO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.077421, 'd13': 0.208012, 'd23': 0.126038},
        uncertainties = {'d12': 0.21197, 'd13': 0.38011, 'd23': 0.270371},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 257,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3     C 0 {2,S} {4,S} {11,S} {12,S}
4  *3 C 1 {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 258,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *3 C 1 {2,S} {4,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 259,
    label = "C_rad/H/O2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.055015, 'd13': 0.225312, 'd23': 0.171407},
        uncertainties = {'d12': 1.207893, 'd13': 1.902951, 'd23': 0.684242},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 260,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    S      0 {1,S}
4    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 261,
    label = "C_rad/H/CsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 262,
    label = "C_rad/H/S2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 263,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 264,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 265,
    label = "C_rad/H/CdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 266,
    label = "C_rad/H/CSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 267,
    label = "C_rad/H/CtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 268,
    label = "C_rad/H/CbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 269,
    label = "C_rad/H/CO/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 270,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c",
    group = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2 *3 C 1 {1,S} {3,S} {8,S}
3    C 0 {2,S} {4,D} {9,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 271,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 272,
    label = "C_rad/H/OneDeS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 273,
    label = "C_rad/H/CdS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 274,
    label = "C_rad/H/CtS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 275,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 276,
    label = "C_rad/H/CdCd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 277,
    label = "C_rad/H/CdCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 278,
    label = "C_rad/H/CSCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cd 0 {1,S} {6,D}
5    S  0 {3,D}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 279,
    label = "C_rad/H/CdCt",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 280,
    label = "C_rad/H/CtCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 281,
    label = "C_rad/H/CdCb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 282,
    label = "C_rad/H/CbCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 283,
    label = "C_rad/H/CdCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 284,
    label = "C_rad/H/COCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    CO 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 285,
    label = "C_rad/H/CtCt",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 286,
    label = "C_rad/H/CtCb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 287,
    label = "C_rad/H/CtCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 288,
    label = "C_rad/H/CbCb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 289,
    label = "C_rad/H/CbCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 290,
    label = "C_rad/H/COCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    CO 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 291,
    label = "C_ter_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 292,
    label = "C_rad/NonDe",
    group = 
"""
1 *3 C        1 {2,S} {3,S} {4,S}
2    {Cs,O,S} 0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 293,
    label = "C_rad/Cs3",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 294,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 295,
    label = "C_rad/NDMustO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    O      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 296,
    label = "C_rad/Cs2O",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 297,
    label = "C_rad/OOH/Cs/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S} {5,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    O  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 298,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2     C 0 {4,S} {9,S} {10,S} {11,S}
3     C 0 {1,S} {4,S} {12,S} {13,S}
4  *3 C 1 {2,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 299,
    label = "C_rad/CsO2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S}
3    O  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 300,
    label = "C_rad/O3",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    O 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 301,
    label = "C_rad/NDMustS",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    S      0 {1,S}
3    {Cs,S} 0 {1,S}
4    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 302,
    label = "C_rad/Cs2S",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 303,
    label = "C_rad/CsS2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 304,
    label = "C_rad/S3",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    S 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 305,
    label = "C_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 306,
    label = "C_rad/Cs2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 307,
    label = "C_rad/CdCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 308,
    label = "C_rad/CSCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    S  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 309,
    label = "C_rad/CtCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 310,
    label = "C_rad/CbCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 311,
    label = "C_rad/COCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 312,
    label = "C_rad/CsO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    O                0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 313,
    label = "C_rad/CsS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    S                0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 314,
    label = "C_rad/CdCsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 315,
    label = "C_rad/CtCsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 316,
    label = "C_rad/O2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    O                0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 317,
    label = "C_rad/OS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    S                0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 318,
    label = "C_rad/S2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    S                0 {1,S}
4    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 319,
    label = "C_rad/TwoDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 320,
    label = "C_rad/Cs",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 321,
    label = "C_rad/CdCdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 322,
    label = "C_rad/CdCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 323,
    label = "C_rad/CSCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    S  0 {2,D}
6    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 324,
    label = "C_rad/CdCtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 325,
    label = "C_rad/CtCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 326,
    label = "C_rad/CdCbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 327,
    label = "C_rad/CbCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 328,
    label = "C_rad/CdCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 329,
    label = "C_rad/COCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 330,
    label = "C_rad/CtCtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 331,
    label = "C_rad/CtCbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 332,
    label = "C_rad/CtCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 333,
    label = "C_rad/CbCbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 334,
    label = "C_rad/CbCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 335,
    label = "C_rad/COCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 336,
    label = "C_rad/TDMustO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 337,
    label = "C_rad/TDMustS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 338,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2013-06-18","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

tree(
"""
L1: X_H_or_Xrad_H
    L2: X_H
        L3: H2
        L3: Ct_H
        L3: O_H
            L4: O_pri
            L4: O_sec
                L5: O/H/NonDeC
                L5: O/H/NonDeO
                    L6: H2O2
                    L6: ROOH_pri
                    L6: ROOH_sec
                    L6: ROOH_ter
                L5: O/H/OneDe
        L3: Orad_O_H
        L3: S_H
            L4: S_pri
            L4: S_sec
                L5: S/H/NonDeC
                L5: S/H/NonDeS
                L5: S/H/OneDe
                    L6: S/H/Cd
                        L7: S/H/CS
                    L6: S/H/Ct
                    L6: S/H/Cb
                    L6: S/H/CO
        L3: Cd_H
            L4: Cd_pri
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/NonDeS
                L5: Cd/H/OneDe
                    L6: Cd/H/Cd
                        L7: Cd/H/CS
                    L6: Cd/H/Ct
                    L6: Cd/H/Cb
                    L6: Cd/H/CO
        L3: Cb_H
        L3: CO_H
            L4: CO_pri
            L4: CO_sec
                L5: CO/H/NonDe
                    L6: InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3
                L5: CO/H/OneDe
        L3: CS_H
            L4: CS_pri
            L4: CS_sec
                L5: CS/H/NonDeC
                L5: CS/H/NonDeO
                L5: CS/H/NonDeS
                L5: CS/H/OneDe
                    L6: CS/H/Cd
                        L7: CS/H/CS
                    L6: CS/H/Ct
                    L6: CS/H/Cb
                    L6: CS/H/CO
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C/H3/Cs
                    L6: InChI=1/C2H6/c1-2/h1-2H3
                    L6: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma
                L5: C/H3/Cd
                    L6: C/H3/CS
                    L6: InChI=1/C3H6/c1-3-2/h3H,1H2,2H3
                    L6: InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3
                    L6: InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+
                L5: C/H3/Ct
                L5: C/H3/Cb
                L5: C/H3/CO
                L5: C/H3/O
                L5: C/H3/S
            L4: C_sec
                L5: C/H2/NonDeC
                    L6: InChI=1/C3H8/c1-3-2/h3H2,1-2H3
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                        L7: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha
                    L6: C/H2/O2
                L5: C/H2/NonDeS
                    L6: C/H2/CsS
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                        L7: C/H2/CdCs
                            L8: C/H2/CSCs
                        L7: C/H2/CtCs
                        L7: C/H2/CbCs
                        L7: C/H2/COCs
                        L7: InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta
                        L7: InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3
                    L6: C/H2/OneDeO
                    L6: C/H2/OneDeS
                        L7: C/H2/CdS
                        L7: C/H2/CtS
                L5: C/H2/TwoDe
                    L6: C/H2/CdCd
                        L7: C/H2/CdCS
                        L7: C/H2/CSCS
                    L6: C/H2/CdCt
                        L7: C/H2/CtCS
                    L6: C/H2/CdCb
                        L7: C/H2/CbCS
                    L6: C/H2/CdCO
                        L7: C/H2/COCS
                    L6: C/H2/CtCt
                    L6: C/H2/CtCb
                    L6: C/H2/CtCO
                    L6: C/H2/CbCb
                    L6: C/H2/CbCO
                    L6: C/H2/COCO
                L5: C/H2/Cb
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                        L7: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta
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
                        L7: C/H/Cs2Cd
                            L8: C/H/Cs2CS
                        L7: C/H/Cs2Ct
                        L7: C/H/Cs2Cb
                        L7: C/H/Cs2CO
                        L7: InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3
                    L6: C/H/CsO
                    L6: C/H/CsS
                        L7: C/H/CdCsS
                        L7: C/H/CtCsS
                    L6: C/H/OO
                    L6: C/H/OS
                    L6: C/H/SS
                L5: C/H/TwoDe
                    L6: C/H/Cs
                        L7: C/H/CdCd
                            L8: C/H/CdCS
                            L8: C/H/CSCS
                        L7: C/H/CdCt
                            L8: C/H/CtCS
                        L7: C/H/CdCb
                            L8: C/H/CbCS
                        L7: C/H/CdCO
                            L8: C/H/COCS
                        L7: C/H/CtCt
                        L7: C/H/CtCb
                        L7: C/H/CtCO
                        L7: C/H/CbCb
                        L7: C/H/CbCO
                        L7: C/H/COCO
                    L6: C/H/TDMustO
                    L6: C/H/TDMustS
                L5: C/H/ThreeDe
                L5: C/H/Cb
    L2: Xrad_H
        L3: Srad_H
L1: Y_rad_birad
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
    L2: Y_rad
        L3: H_rad
        L3: Y_2centeradjbirad
            L4: O2b
            L4: C2b
        L3: Ct_rad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3
                L5: O_rad/NonDeO
                    L6: OOCH3
                L5: O_rad/OneDe
                    L6: InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3
                    L6: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
                    L6: S_rad/Cd
                        L7: S_rad/CS
                    L6: S_rad/Ct
                    L6: S_rad/Cb
                    L6: S_rad/CO
        L3: Cd_rad
            L4: Cd_pri_rad
                L5: InChI=1/C2H3/c1-2/h1H,2H2
                L5: InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: InChI=1/C3H5/c1-3-2/h1H2,2H3
                    L6: InChI=1/C4H7/c1-3-4-2/h3H,1-2H3
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/OneDe
                    L6: Cd_rad/Cd
                        L7: Cd_rad/CS
                    L6: Cd_rad/Ct
                    L6: Cd_rad/Cb
                    L6: Cd_rad/CO
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
                    L6: CS_rad/Cd
                        L7: CS_rad/CS
                    L6: CS_rad/Ct
                    L6: CS_rad/Cb
                    L6: CS_rad/CO
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                    L6: InChI=1/C2H5/c1-2/h1H2,2H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3
                    L6: InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3
                L5: C_rad/H2/Cd
                    L6: InChI=1/C3H5/c1-3-2/h3H,1-2H2
                    L6: InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
                L5: C_rad/H2/S
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                    L6: InChI=1/C3H7/c1-3-2/h3H,1-2H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3
                    L6: InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3
                    L6: InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                        L7: InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                        L7: C_rad/H/CdCs
                            L8: C_rad/H/CSCs
                        L7: C_rad/H/CtCs
                        L7: C_rad/H/CbCs
                        L7: C_rad/H/CO/Cs
                            L8: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeS
                        L7: C_rad/H/CdS
                        L7: C_rad/H/CtS
                L5: C_rad/H/TwoDe
                    L6: C_rad/H/CdCd
                        L7: C_rad/H/CdCS
                        L7: C_rad/H/CSCS
                    L6: C_rad/H/CdCt
                        L7: C_rad/H/CtCS
                    L6: C_rad/H/CdCb
                        L7: C_rad/H/CbCS
                    L6: C_rad/H/CdCO
                        L7: C_rad/H/COCS
                    L6: C_rad/H/CtCt
                    L6: C_rad/H/CtCb
                    L6: C_rad/H/CtCO
                    L6: C_rad/H/CbCb
                    L6: C_rad/H/CbCO
                    L6: C_rad/H/COCO
            L4: C_ter_rad
                L5: C_rad/NonDe
                    L6: C_rad/Cs3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3
                    L6: C_rad/NDMustO
                        L7: C_rad/Cs2O
                            L8: C_rad/OOH/Cs/Cs
                            L8: InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3
                        L7: C_rad/CsO2
                        L7: C_rad/O3
                    L6: C_rad/NDMustS
                        L7: C_rad/Cs2S
                        L7: C_rad/CsS2
                        L7: C_rad/S3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                        L7: C_rad/CdCs2
                            L8: C_rad/CSCs2
                        L7: C_rad/CtCs2
                        L7: C_rad/CbCs2
                        L7: C_rad/COCs2
                    L6: C_rad/CsO
                    L6: C_rad/CsS
                        L7: C_rad/CdCsS
                        L7: C_rad/CtCsS
                    L6: C_rad/O2
                    L6: C_rad/OS
                    L6: C_rad/S2
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                        L7: C_rad/CdCdCs
                            L8: C_rad/CdCSCs
                            L8: C_rad/CSCSCs
                        L7: C_rad/CdCtCs
                            L8: C_rad/CtCSCs
                        L7: C_rad/CdCbCs
                            L8: C_rad/CbCSCs
                        L7: C_rad/CdCOCs
                            L8: C_rad/COCSCs
                        L7: C_rad/CtCtCs
                        L7: C_rad/CtCbCs
                        L7: C_rad/CtCOCs
                        L7: C_rad/CbCbCs
                        L7: C_rad/CbCOCs
                        L7: C_rad/COCOCs
                    L6: C_rad/TDMustO
                    L6: C_rad/TDMustS
                L5: C_rad/ThreeDe
"""
)

