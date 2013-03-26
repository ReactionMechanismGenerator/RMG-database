#!/usr/bin/env python
# encoding: utf-8

entry(
    index = 1,
    label = "CsringH2R2",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0100,
        Pc = 0.0025,
        Vc = 48,
        Tb = 27.15,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringH2R2""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 2,
    label = "CsringHR3",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
5 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0122,
        Pc = 0.0004,
        Vc = 38,
        Tb = 21.78,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringHR3""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 3,
    label = "CsringR4",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
5 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0042,
        Pc = 0.0061,
        Vc = 27,
        Tb = 21.32,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CsringR4""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 4,
    label = "CdringHR2",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 R!H 0 {1,D}
3 R!H 0 {1,S}
4 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0082,
        Pc = 0.0011,
        Vc = 41,
        Tb = 26.73,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CdringHR2""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 5,
    label = "CdringR3",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 R!H 0 {1,D}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0008,
        Vc = 32,
        Tb = 31.01,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for CdringR3""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 6,
    label = "Ether_ring",
    group =
"""
1 * O 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0098,
        Pc = 0.0048,
        Vc = 13,
        Tb = 31.22,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Ether_ring""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 7,
    label = "Ketone_ring",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0284,
        Pc = 0.0028,
        Vc = 55,
        Tb = 94.97,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Ketone_ring""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 8,
    label = "Thioether_ring",
    group =
"""
1 * S 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0019,
        Pc = 0.0051,
        Vc = 38,
        Tb = 52.10,
        structureIndex = 1,
    ),
    shortDesc = u"""ring_library value for Thioether_ring""",
    LongDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
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
        //L2: CddringR2 (?) The lack of this node is causing RMG to throw a warning message: "Transport Group not found"
    
    L1: O_centered_ring
        L2: Ether_ring
        
    L1: S_centered_ring
        L2: Thioether_ring
"""
)