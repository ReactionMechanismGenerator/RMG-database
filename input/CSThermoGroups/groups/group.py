#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Additivity Values"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = -1,
    label = "C=S-C=SSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Ss u0 {1,S}
5   Sd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Sd)Cs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cs  u0 {1,S}
5   Cdd u0 {3,D} {6,D}
6   Sd  u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)H",
    group = 
"""
1 * CS          u0 {2,D} {3,S} {4,S}
2   Sd          u0 {1,D}
3   Cd          u0 {1,S} {5,D}
4   H           u0 {1,S}
5   [Cd,Cdd,CO] u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbC=S",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Sd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Cd  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cdd-Sd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   Sd  u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)Cs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cs u0 {1,S}
5   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)H",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   H   u0 {1,S}
5   Cdd u0 {3,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Ss u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbCds",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)C=S",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Sd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cds)",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CdsSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S}
4   Ss u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,D} {3,S} {4,S}
2   Sd          u0 {1,D}
3   Cd          u0 {1,S} {5,D}
4   Cd          u0 {1,S} {6,D}
5   [Cd,Cdd,CO] u0 {3,D}
6   [Cd,Cdd,CO] u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)C=S",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {3,D}
6   Sd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)H",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   H   u0 {1,S}
5   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {3,D}
6   Cd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtCt",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cd  u0 {4,D}
7   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)C=S",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {3,D} {6,D}
6   C   u0 {5,D}
7   Sd  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-SsSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ss u0 {1,S}
4   Ss u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbCb",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,D} {3,S} {4,S}
2   Sd          u0 {1,D}
3   Ct          u0 {1,S}
4   Cd          u0 {1,S} {5,D}
5   [Cd,Cdd,CO] u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)Cs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cs  u0 {1,S}
5   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   C   u0 {5,D}
8   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,D} {3,S} {4,S}
2   Sd          u0 {1,D}
3   Cb          u0 {1,S}
4   Cd          u0 {1,S} {5,D}
5   [Cd,Cdd,CO] u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)Ss",
    group = 
"""
1 * CS          u0 {2,D} {3,S} {4,S}
2   Sd          u0 {1,D}
3   Cd          u0 {1,S} {5,D}
4   Ss          u0 {1,S}
5   [Cd,Cdd,CO] u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cds)",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CC",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtC=S",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Sd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cs  u0 {1,S}
5   Cdd u0 {3,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CdsCds",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S}
4   Cd u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   Sd  u0 {5,D}
8   Sd  u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   Ss u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)Ss",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Ss u0 {1,S}
5   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Sd)H",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   H   u0 {1,S}
5   Cdd u0 {3,D} {6,D}
6   Sd  u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)C=S",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Sd  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-Sd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   C   u0 {5,D}
8   Sd  u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)Ss",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Ss  u0 {1,S}
5   Cdd u0 {3,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)H",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   H  u0 {1,S}
5   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)Ss",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Ss  u0 {1,S}
5   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cdd-Sd)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   Sd  u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Sd)Ss",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Ss  u0 {1,S}
5   Cdd u0 {3,D} {6,D}
6   Sd  u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtCds",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   Cd u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)Cs",
    group = 
"""
1 * CS          u0 {2,D} {3,S} {4,S}
2   Sd          u0 {1,D}
3   Cd          u0 {1,S} {5,D}
4   Cs          u0 {1,S}
5   [Cd,Cdd,CO] u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Sd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cd  u0 {4,D}
7   Sd  u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Sd)C=S",
    group = 
"""
1 * CS  u0 {2,D} {3,S} {4,S}
2   Sd  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {3,D} {6,D}
6   Sd  u0 {5,D}
7   Sd  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbCt",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-C=SC=S",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Sd u0 {3,D}
6   Sd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1183,
    label = "C=S-HH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.08,10.34,11.51,12.5,14.07,15.25,17.14],'cal/(mol*K)'),
        H298 = (27.71,'kcal/mol'),
        S298 = (56.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1184,
    label = "C=S-CsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.11,9.03,9.88,10.61,11.74,12.55,13.82],'cal/(mol*K)'),
        H298 = (27.32,'kcal/mol'),
        S298 = (37.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1185,
    label = "C=S-CdsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.59,9.38,10.81,11.85,13.18,13.95,14.81],'cal/(mol*K)'),
        H298 = (24.05,'kcal/mol'),
        S298 = (34.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1186,
    label = "C=S-CtH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.46,8.91,10.01,10.83,11.98,12.74,13.87],'cal/(mol*K)'),
        H298 = (30.83,'kcal/mol'),
        S298 = (37.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1187,
    label = "C=S-CbH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.45,9.84,10.94,11.78,12.97,13.76,14.77],'cal/(mol*K)'),
        H298 = (24.71,'kcal/mol'),
        S298 = (34.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1188,
    label = "C=S-C=SH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   H  u0 {1,S}
5   Sd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,9.18,10.41,11.42,12.82,13.63,14.54],'cal/(mol*K)'),
        H298 = (26.96,'kcal/mol'),
        S298 = (35.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1189,
    label = "C=S-SsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ss u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.38,9.78,10.83,11.66,12.86,13.71,14.87],'cal/(mol*K)'),
        H298 = (21.55,'kcal/mol'),
        S298 = (34.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1190,
    label = "C=S-CsCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.7,7.44,8.14,8.72,9.52,9.98,10.51],'cal/(mol*K)'),
        H298 = (27.2,'kcal/mol'),
        S298 = (18,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1191,
    label = "C=S-CdsCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,9.21,10.13,10.71,11.25,11.42,11.35],'cal/(mol*K)'),
        H298 = (26.19,'kcal/mol'),
        S298 = (13.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1192,
    label = "C=S-CtCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.87,7.88,8.6,9.13,9.8,10.17,10.59],'cal/(mol*K)'),
        H298 = (30.12,'kcal/mol'),
        S298 = (17.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1193,
    label = "C=S-CbCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.02,9.02,9.75,10.23,10.75,10.96,11.04],'cal/(mol*K)'),
        H298 = (26.6,'kcal/mol'),
        S298 = (14.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1194,
    label = "C=S-C=SCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cs u0 {1,S}
5   Sd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.93,7.93,8.76,9.37,10.11,10.45,10.71],'cal/(mol*K)'),
        H298 = (27.48,'kcal/mol'),
        S298 = (16.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1205,
    label = "C=S-CSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   C  u0 {1,S}
4   Ss u0 {1,S}
""",
    thermo = u'C=S-CsSs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1206,
    label = "C=S-CsSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Cs u0 {1,S}
4   Ss u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.4,8.38,9.16,9.8,10.72,11.25,11.66],'cal/(mol*K)'),
        H298 = (21.35,'kcal/mol'),
        S298 = (14.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1457,
    label = "CS-OsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Os u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.48,5.3,6.09,6.82,8.05,8.99,10.37],'cal/(mol*K)'),
        H298 = (2.85,'kcal/mol'),
        S298 = (30.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC 1d-HR calc""",
    longDesc = 
u"""

""",
)

entry(
    index = 1458,
    label = "CS-CsOs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Os u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.17,4.6,5.1,6.08,6.76,7.44],'cal/(mol*K)'),
        H298 = (-1.32,'kcal/mol'),
        S298 = (8.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC 1d-HR calc""",
    longDesc = 
u"""

""",
)

entry(
    index = 1459,
    label = "CS-OsOs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   Sd u0 {1,D}
3   Os u0 {1,S}
4   Os u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.08,3.59,3.9,4.03,3.99,3.75,3.23],'cal/(mol*K)'),
        H298 = (-22.72,'kcal/mol'),
        S298 = (2.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC CBS-QB3 1Dhr calc""",
    longDesc = 
u"""

""",
)

