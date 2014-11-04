#!/usr/bin/env python
# encoding: utf-8

name = "Joback rings"
shortDesc = u"Groups for atoms in a ring to estimate critical point properties according to Joback 1984"
longDesc = u"""
Group definitions to estimate critical point properties via group additivity, from:

Joback, K. G. A unified approach to physical property estimation using multivariate statistical techniques,
PhD Thesis, Massachusetts Institute of Technology: Cambridge, MA, 1984.

Note the Pc contributions are all the negative of what is in Table 3 of Joback's thesis.
The Tb contributions are from table 13.
"""
entry(
    index = 0,
    label = "R_ring",
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
    label = "C_centered_ring",
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
    label = "CsringH2R2",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.01,
        Pc = 0.0025,
        Vc = 48,
        Tb = 27.15,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringH2R2""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "CsringHR3",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
5   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0122,
        Pc = 0.0004,
        Vc = 38,
        Tb = 21.78,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringHR3""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "CsringR4",
    group = 
"""
1 * C   u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
5   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0042,
        Pc = 0.0061,
        Vc = 27,
        Tb = 21.32,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringR4""",
    longDesc = u"""""",
)

entry(
    index = 5,
    label = "CdringR3",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0008,
        Vc = 32,
        Tb = 31.01,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CdringR3""",
    longDesc = u"""""",
)

entry(
    index = 7,
    label = "Ketone_ring",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   O   u0 {1,D}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0284,
        Pc = 0.0028,
        Vc = 55,
        Tb = 94.97,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Ketone_ring""",
    longDesc = u"""""",
)

entry(
    index = 4,
    label = "CdringHR2",
    group = 
"""
1 * C   u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D}
3   R!H u0 {1,S}
4   H   u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0082,
        Pc = 0.0011,
        Vc = 41,
        Tb = 26.73,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CdringHR2""",
    longDesc = u"""""",
)

entry(
    index = 9,
    label = "Cddring",
    group = 
"""
1 * C   u0 {2,D} {3,D}
2   R!H u0 {1,D}
3   R!H u0 {1,D}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0008,
        Vc = 32,
        Tb = 31.01,
        structureIndex = 1,
    ),
    shortDesc = u"""Made up value for R=C=R in ring""",
    longDesc = 
u"""
Made up value for R=C=R in a ring.
Without this existing, we crash.
Joback's thesis has no data for such species.
I'm copying R=CH-R in a ring.
""",
)

entry(
    index = 10,
    label = "Ctring",
    group = 
"""
1 * C   u0 {2,T}
2   R!H u0 {1,T}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0008,
        Vc = 32,
        Tb = 31.01,
        structureIndex = 1,
    ),
    shortDesc = u"""Made up value for C#R (triple bond) in ring""",
    longDesc = 
u"""
Made up value for triple bond in a ring.
Without this existing, we crash.
Joback's thesis has no data for such species.
I'm copying R=CH-R in a ring.
""",
)

entry(
    index = 0,
    label = "O_centered_ring",
    group = 
"""
1 * O ux
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 6,
    label = "Ether_ring",
    group = 
"""
1 * O   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0098,
        Pc = 0.0048,
        Vc = 13,
        Tb = 31.22,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Ether_ring""",
    longDesc = u"""""",
)

entry(
    index = 0,
    label = "S_centered_ring",
    group = 
"""
1 * S ux
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 8,
    label = "Thioether_ring",
    group = 
"""
1 * S   u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0019,
        Pc = 0.0051,
        Vc = 38,
        Tb = 52.1,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Thioether_ring""",
    longDesc = u"""""",
)

tree(
"""
L1: R_ring
    L2: C_centered_ring
        L3: CsringH2R2
        L3: CsringHR3
        L3: CsringR4
        L3: CdringR3
            L4: Ketone_ring
        L3: CdringHR2
        L3: Cddring
        L3: Ctring
    L2: O_centered_ring
        L3: Ether_ring
    L2: S_centered_ring
        L3: Thioether_ring
"""
)

