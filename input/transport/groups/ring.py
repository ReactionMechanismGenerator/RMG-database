#!/usr/bin/env python
# encoding: utf-8

"""
Note the Pc contributions are all the negative of what is in Table 3 of Joback's thesis.
The Tb contributions are from table 13.
"""

entry(
    index = 0,
    label = "R_ring",
    group =
"""
1 * R U{0,1,2}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = 
u"""

""",
)

entry(
    index = 0, # another 0!!
    label = "C_centered_ring",
    group =
"""
1 * C U{0,1,2}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)

entry(
    index = 0, # another 0!!
    label = "O_centered_ring",
    group =
"""
1 * O U{0,1}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
)
entry(
    index = 0, # another 0!!
    label = "S_centered_ring",
    group =
"""
1 * S U{0,1}
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
1 * C U0 {2,S} {3,S} {4,S} {5,S}
2 R!H U0 {1,S}
3 R!H U0 {1,S}
4 H   U0 {1,S}
5 H   U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0100,
        Pc = 0.0025,
        Vc = 48,
        Tb = 27.15,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringH2R2""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CsringHR3",
    group =
"""
1 * C U0 {2,S} {3,S} {4,S} {5,S}
2 R!H U0 {1,S}
3 R!H U0 {1,S}
4 R!H U0 {1,S}
5 H   U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0122,
        Pc = 0.0004,
        Vc = 38,
        Tb = 21.78,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringHR3""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CsringR4",
    group =
"""
1 * C U0 {2,S} {3,S} {4,S} {5,S}
2 R!H U0 {1,S}
3 R!H U0 {1,S}
4 R!H U0 {1,S}
5 R!H U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0042,
        Pc = 0.0061,
        Vc = 27,
        Tb = 21.32,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringR4""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CdringHR2",
    group =
"""
1 * C U0 {2,D} {3,S} {4,S}
2 R!H U0 {1,D}
3 R!H U0 {1,S}
4 H   U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0082,
        Pc = 0.0011,
        Vc = 41,
        Tb = 26.73,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CdringHR2""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CdringR3",
    group =
"""
1 * C U0 {2,D} {3,S} {4,S}
2 R!H U0 {1,D}
3 R!H U0 {1,S}
4 R!H U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0008,
        Vc = 32,
        Tb = 31.01,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CdringR3""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Cddring",
    group =
"""
1 * C U0 {2,D} {3,D}
2 R!H U0 {1,D}
3 R!H U0 {1,D}
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
1 * C U0 {2,T}
2 R!H U0 {1,T}
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
    index = 6,
    label = "Ether_ring",
    group =
"""
1 * O U0 {2,S} {3,S}
2 R!H U0 {1,S}
3 R!H U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0098,
        Pc = 0.0048,
        Vc = 13,
        Tb = 31.22,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Ether_ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Ketone_ring",
    group =
"""
1 * C U0 {2,D} {3,S} {4,S}
2 O   U0 {1,D}
3 R!H U0 {1,S}
4 R!H U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0284,
        Pc = 0.0028,
        Vc = 55,
        Tb = 94.97,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Ketone_ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Thioether_ring",
    group =
"""
1 * S U0 {2,S} {3,S}
2 R!H U0 {1,S}
3 R!H U0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0019,
        Pc = 0.0051,
        Vc = 38,
        Tb = 52.10,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Thioether_ring""",
    longDesc = 
u"""

""",
)


tree(
"""
L0: R_ring
    L1: C_centered_ring
        L2: CsringH2R2
        L2: CsringHR3
        L2: CsringR4
        L2: CdringR3
            L3: Ketone_ring
        L2: CdringHR2
        L2: Cddring
        L2: Ctring
    
    L1: O_centered_ring
        L2: Ether_ring
        
    L1: S_centered_ring
        L2: Thioether_ring
"""
)