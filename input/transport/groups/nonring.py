#!/usr/bin/env python
# encoding: utf-8

name = "Joback non-rings"
shortDesc = u"Groups for atoms not in a ring to estimate critical point properties according to Joback 1984"
longDesc = u"""
Group definitions to estimate critical point properties via group additivity, from:

Joback, K. G. A unified approach to physical property estimation using multivariate statistical techniques,
PhD Thesis, Massachusetts Institute of Technology: Cambridge, MA, 1984.

Note the Pc contributions are all the negative of what is in Table 3 of Joback's thesis.
The Tb contributions are from table 13.
"""
entry(
    index = 0,
    label = "R",
    group = 
"""
1 * R ux
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 0,
    label = "C_centered",
    group = 
"""
1 * C ux
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 1,
    label = "CsH3R",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0141,
        Pc = -0.0012,
        Vc = 65,
        Tb = 23.58,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsH3R""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "CsH2R2",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0189,
        Pc = 0,
        Vc = 56,
        Tb = 22.88,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsH2R2""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "CsHR3",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
5   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0164,
        Pc = 0.002,
        Vc = 41,
        Tb = 21.74,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsHR3""",
    longDesc = u"""""",
)

entry(
    index = 4,
    label = "CsR4",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
5   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0067,
        Pc = 0.0043,
        Vc = 27,
        Tb = 18.25,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsR4""",
    longDesc = u"""""",
)

entry(
    index = 5,
    label = "CdH2R",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0113,
        Pc = -0.0028,
        Vc = 56,
        Tb = 18.18,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CdH2R""",
    longDesc = u"""""",
)

entry(
    index = 7,
    label = "CdR3",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0117,
        Pc = 0.0011,
        Vc = 38,
        Tb = 24.14,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CdR3""",
    longDesc = u"""""",
)

entry(
    index = 14,
    label = "Ketone_Ccentered",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   O   u0 {1,D}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.038,
        Pc = 0.0031,
        Vc = 62,
        Tb = 76.75,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ketone_Ccentered""",
    longDesc = u"""""",
)

entry(
    index = 18,
    label = "Acid_Ccentered",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   O   u0 {1,D}
3   O   u0 {1,S} {5,S}
4   R!H u0 {1,S}
5   H   u0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0791,
        Pc = 0.0077,
        Vc = 89,
        Tb = 169.09,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Acid_Ccentered""",
    longDesc = u"""""",
)

entry(
    index = 21,
    label = "Ester_Ccentered",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   O   u0 {1,D}
3   O   u0 {1,S} {5,S}
4   R!H u0 {1,S}
5   R!H u0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0481,
        Pc = 0.0005,
        Vc = 82,
        Tb = 81.1,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ester_Ccentered""",
    longDesc = u"""""",
)

entry(
    index = 6,
    label = "CdHR2",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D}
3   R!H u0 {1,S}
4   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0129,
        Pc = -0.0006,
        Vc = 46,
        Tb = 24.96,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CdHR2""",
    longDesc = u"""""",
)

entry(
    index = 16,
    label = "Aldehyde_Ccentered",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   O   u0 {1,D}
3   R!H u0 {1,S}
4   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0379,
        Pc = 0.003,
        Vc = 82,
        Tb = 72.24,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Aldehyde_Ccentered""",
    longDesc = u"""""",
)

entry(
    index = 8,
    label = "CddR2",
    group = 
"""
1 * C   u0 {2,D} {3,D}
2   R!H u0 {1,D}
3   R!H u0 {1,D}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0026,
        Pc = 0.0028,
        Vc = 36,
        Tb = 26.15,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for CddR2""",
    longDesc = u"""""",
)

entry(
    index = 9,
    label = "CtHR",
    group = 
"""
1 * C   u0 {2,T} {3,S}
2   R!H u0 {1,T}
3   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0027,
        Pc = -0.0008,
        Vc = 46,
        Tb = 9.2,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for CtHR""",
    longDesc = u"""""",
)

entry(
    index = 10,
    label = "CtR2",
    group = 
"""
1 * C   u0 {2,T} {3,S}
2   R!H u0 {1,T}
3   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.002,
        Pc = 0.0016,
        Vc = 37,
        Tb = 27.38,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for CtR2""",
    longDesc = u"""""",
)

entry(
    index = 0,
    label = "O_centered",
    group = 
"""
1 * O ux
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 11,
    label = "Alcohol",
    group = 
"""
1 * O   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0741,
        Pc = 0.0112,
        Vc = 28,
        Tb = 92.88,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Alcohol""",
    longDesc = u"""""",
)

entry(
    index = 12,
    label = "Phenol",
    group = 
"""
1 * O  u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.024,
        Pc = 0.0184,
        Vc = -25,
        Tb = 76.34,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Phenol""",
    longDesc = u"""""",
)

entry(
    index = 19,
    label = "Acid_Ocentered1",
    group = 
"""
1 * O   u0 {2,S} {3,S}
2   H   u0 {1,S}
3   C   u0 {1,S} {4,D} {5,S}
4   O   u0 {3,D}
5   R!H u0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Acid_Ocentered1""",
    longDesc = u"""""",
)

entry(
    index = 13,
    label = "Ether",
    group = 
"""
1 * O   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0168,
        Pc = 0.0015,
        Vc = 18,
        Tb = 22.42,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ether""",
    longDesc = u"""""",
)

entry(
    index = 22,
    label = "Ester_Ocentered1",
    group = 
"""
1 * O   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   C   u0 {1,S} {4,D} {5,S}
4   O   u0 {3,D}
5   R!H u0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ester_Ocentered1""",
    longDesc = u"""""",
)

entry(
    index = 24,
    label = "Od",
    group = 
"""
1 * O   u0 {2,D}
2   R!H u0 {1,D}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0101,
        Vc = 36,
        Tb = -10.5,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for Od""",
    longDesc = u"""""",
)

entry(
    index = 15,
    label = "Ketone_Ocentered",
    group = 
"""
1 * O   u0 {2,D}
2   C   u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S}
4   R!H u0 {2,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ketone_Ocentered""",
    longDesc = u"""""",
)

entry(
    index = 17,
    label = "Aldehyde_Ocentered",
    group = 
"""
1 * O   u0 {2,D}
2   C   u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S}
4   H   u0 {2,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Aldehyde_Ocentered""",
    longDesc = u"""""",
)

entry(
    index = 20,
    label = "Acid_Ocentered2",
    group = 
"""
1 * O   u0 {2,D}
2   C   u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S}
4   O   u0 {2,S} {5,S}
5   H   u0 {4,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Acid_Ocentered2""",
    longDesc = u"""""",
)

entry(
    index = 23,
    label = "Ester_Ocentered2",
    group = 
"""
1 * O   u0 {2,D}
2   C   u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S}
4   O   u0 {2,S} {5,S}
5   R!H u0 {4,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ester_Ocentered2""",
    longDesc = u"""""",
)

entry(
    index = 0,
    label = "S_centered",
    group = 
"""
1 * S ux
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 25,
    label = "Thiol",
    group = 
"""
1 * S   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0031,
        Pc = 0.0084,
        Vc = 63,
        Tb = 63.56,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Thiol""",
    longDesc = u"""""",
)

entry(
    index = 26,
    label = "Thioether",
    group = 
"""
1 * S   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0119,
        Pc = 0.0049,
        Vc = 54,
        Tb = 68.78,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Thioether""",
    longDesc = u"""""",
)

tree(
"""
L1: R
    L2: C_centered
        L3: CsH3R
        L3: CsH2R2
        L3: CsHR3
        L3: CsR4
        L3: CdH2R
        L3: CdR3
            L4: Ketone_Ccentered
                L5: Acid_Ccentered
                L5: Ester_Ccentered
        L3: CdHR2
            L4: Aldehyde_Ccentered
        L3: CddR2
        L3: CtHR
        L3: CtR2
    L2: O_centered
        L3: Alcohol
            L4: Phenol
            L4: Acid_Ocentered1
        L3: Ether
            L4: Ester_Ocentered1
        L3: Od
            L4: Ketone_Ocentered
                L5: Acid_Ocentered2
                L5: Ester_Ocentered2
            L4: Aldehyde_Ocentered
    L2: S_centered
        L3: Thiol
        L3: Thioether
"""
)

