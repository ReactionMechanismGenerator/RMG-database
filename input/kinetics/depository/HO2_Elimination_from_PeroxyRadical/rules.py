#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""

entry(
    index = 835,
    label = "R2OO",
    group1 = 
"""
1  *1 {C,Si} 0 {2,S} {5,S}
2  *2 {C,Si} 0 {1,S} {3,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"cm^3/(mol*s)"),
        n = 1,
        alpha = 0,
        E0 = (30,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 836,
    label = "R2OO_2H_2H",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.56e+07,"cm^3/(mol*s)"),
        n = 1.69,
        alpha = 0,
        E0 = (29.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 837,
    label = "R2OO_HNd_2H",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (4.79e+07,"cm^3/(mol*s)"),
        n = 1.46,
        alpha = 0,
        E0 = (29.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 838,
    label = "R2OO_NdNd_2H",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.06e+08,"cm^3/(mol*s)"),
        n = 1.19,
        alpha = 0,
        E0 = (29.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 839,
    label = "R2OO_2H_HNd",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (9.79e+08,"cm^3/(mol*s)"),
        n = 1.17,
        alpha = 0,
        E0 = (30.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 840,
    label = "R2OO_HNd_HNd",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.65e+09,"cm^3/(mol*s)"),
        n = 1.01,
        alpha = 0,
        E0 = (29.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 841,
    label = "R2OO_NdNd_HNd",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     H 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (6.48e+10,"cm^3/(mol*s)"),
        n = 0.57,
        alpha = 0,
        E0 = (29.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 842,
    label = "R2OO_2H_NdNd",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7.48e+09,"cm^3/(mol*s)"),
        n = 1.08,
        alpha = 0,
        E0 = (29.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 843,
    label = "R2OO_HNd_NdNd",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (8.11e+14,"cm^3/(mol*s)"),
        n = -0.78,
        alpha = 0,
        E0 = (30.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 844,
    label = "R2OO_NdNd_NdNd",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {1,S}
8     {Cs,O} 0 {2,S}
9     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3.1e+19,"cm^3/(mol*s)"),
        n = -1.78,
        alpha = 0,
        E0 = (31.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 845,
    label = "CH3CH(OO)CHCH2",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     C 0 {2,S} {10,S} {11,D}
10    H 0 {9,S}
11    C 0 {9,D} {12,S} {13,S}
12    H 0 {11,S}
13    H 0 {11,S}
""",
    kinetics = ArrheniusEP(
        A = (825300,"cm^3/(mol*s)","*|/",5),
        n = 1.829,
        alpha = 0,
        E0 = (24.247,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections.""",
    longDesc = 
u"""
MRH CBS-QB3 calculations for the reaction CH3-CH(OO)-CH=CH2 => CH2=CH-CH=CH2 + HO2

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to CH3-*CH-CH=CHOH => CH2=CH-CH=CHOH + HO2.
The high-p limit kinetics were necessary to estimate a k(T,P) for this PES.  MRH could not find a 
stable TS geometry for the exact reaction.  Instead, I removed the OH group and found
a stable TS for that reaction (the titled reaction for this node).

Reactant: 3 hindered rotors were considered (the -OO, -CH3, and -CH=CH2 torsions)
TS: 0 hindered rotors were considered (MRH attempted to treat the -CH=CH2 torsion as a hindered rotor,
	but with no luck.  The complete 360 degree spin would interfere with the HO2 elimination).
Product: 1 hindered rotor was considered (the -CH=CH2 torsion of 1,3-butadiene)

All external symmetry numbers were set equal to one, with the exception of 1,3-butadience which was set to two.
The k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.476e+06 * (T/1K)^1.829 * exp(-24.247 kcal/mol / RT) cm3/mol/s.  MRH divided this rate coefficient by
three to account for the reaction path degeneracy, yielding the value stored in the rateLibrary.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 846,
    label = "R2OO_2H_HDe",
    group1 = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2  *2 C 0 {1,S} {3,S} {8,S} {9,S}
3  *3 O 0 {2,S} {4,S}
4  *4 O 1 {3,S}
5  *5 H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (825300,"cm^3/(mol*s)","*|/",5),
        n = 1.829,
        alpha = 0,
        E0 = (24.247,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Same as node 845 (MRH assumption)""",
    longDesc = 
u"""
MRH approximation for the general R2OO_2H_HDe node

MRH computed the rate coefficient for the reaction CH3-CH(OO)-CH=CH2 => CH2=CH-CH=CH2 + HO2 (see node 845).
The difference between the R2OO_2H_HDe and CH3CH(OO)CHCH2 nodes is defining the delocalized group (in the
case of the CH3CH(OO)CHCH2 node, the -CH=CH2 functional group).  MRH thinks using the kinetics for node 845
in the event node 846 is hit is reasonable, considering this part of the molecule does not play a role in the
TS (and it is certainly better than leaving RMG to estimate via "Average of Average").
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

