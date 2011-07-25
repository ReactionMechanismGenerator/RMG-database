#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
recommended = True

entry(
    index = 1,
    label = "X_H;Y_rad_birad",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = "OR{Y_1centerbirad, Y_rad}",
    kinetics = ArrheniusEP(
        A = (100000,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "X_H;H_rad",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.4e+08,"cm^3/(mol*s)"),
        n = 1.5,
        alpha = 0.65,
        E0 = (9.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "X_H;O_atom_triplet",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (1.7e+08,"cm^3/(mol*s)"),
        n = 1.5,
        alpha = 0.75,
        E0 = (6.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "X_H;O_pri_rad",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.2e+06,"cm^3/(mol*s)"),
        n = 2,
        alpha = 0.5,
        E0 = (10.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "X_H;O_sec_rad",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14000,"cm^3/(mol*s)"),
        n = 2.69,
        alpha = 0.6,
        E0 = (11.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "X_H;C_methyl",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (810000,"cm^3/(mol*s)"),
        n = 1.87,
        alpha = 0.65,
        E0 = (13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "C/H/Cs3;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.13,"cm^3/(mol*s)"),
        n = 3.71,
        alpha = 0,
        E0 = (6.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "C/H2/NonDeC;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26,"cm^3/(mol*s)"),
        n = 3.55,
        alpha = 0,
        E0 = (8.31,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "C/H3/Cs;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.85,"cm^3/(mol*s)"),
        n = 3.62,
        alpha = 0,
        E0 = (11.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "C/H/Cs3;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (55.8,"cm^3/(mol*s)"),
        n = 3.01,
        alpha = 0,
        E0 = (7.34,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "C/H2/NonDeC;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (15.2,"cm^3/(mol*s)"),
        n = 3.19,
        alpha = 0,
        E0 = (10.31,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "C/H3/Cs;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (47.1,"cm^3/(mol*s)"),
        n = 3.23,
        alpha = 0,
        E0 = (12.27,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "C/H/Cs3;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4220,"cm^3/(mol*s)"),
        n = 2.51,
        alpha = 0,
        E0 = (8.06,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "C/H2/NonDeC;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1540,"cm^3/(mol*s)"),
        n = 2.66,
        alpha = 0,
        E0 = (10.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "C/H3/Cs;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (659,"cm^3/(mol*s)"),
        n = 2.71,
        alpha = 0,
        E0 = (12.92,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (574000,"cm^3/(mol*s)"),
        n = 1.83,
        alpha = 0,
        E0 = (6.94,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.45e+06,"cm^3/(mol*s)"),
        n = 1.77,
        alpha = 0,
        E0 = (8.53,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (278000,"cm^3/(mol*s)"),
        n = 1.9,
        alpha = 0,
        E0 = (11.05,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "C_methane;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10100,"cm^3/(mol*s)"),
        n = 2.47,
        alpha = 0,
        E0 = (13.96,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "C/H/Cs3;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (4.83e+08,"cm^3/(mol*s)"),
        n = 1.54,
        alpha = 0,
        E0 = (2.98,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "C/H2/NonDeC;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.3e+08,"cm^3/(mol*s)"),
        n = 1.69,
        alpha = 0,
        E0 = (4.78,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "C/H3/Cs;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (6.28e+07,"cm^3/(mol*s)"),
        n = 1.75,
        alpha = 0,
        E0 = (7.51,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "C_methane;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3.06e+07,"cm^3/(mol*s)"),
        n = 1.87,
        alpha = 0,
        E0 = (10.59,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "O/H/NonDeC;H_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (8.7e+08,"cm^3/(mol*s)"),
        n = 1.39,
        alpha = 0,
        E0 = (10.07,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

ROH + H --> RO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "CO_pri;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (5.48e+07,"cm^3/(mol*s)"),
        n = 1.82,
        alpha = 0,
        E0 = (2.44,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

HCHO + H --> HCO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "CO/H/NonDe;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (8.07e+07,"cm^3/(mol*s)"),
        n = 1.76,
        alpha = 0,
        E0 = (0.67,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCHO + H --> RCO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.53e+07,"cm^3/(mol*s)"),
        n = 1.98,
        alpha = 0,
        E0 = (11.78,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Primary vinylic {Cd/H2}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CH2 + H --> R2C=CH + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (4530,"cm^3/(mol*s)"),
        n = 2.43,
        alpha = 0,
        E0 = (8.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Ketene hydrogen {CCO/H2}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.46e+07,"cm^3/(mol*s)"),
        n = 2.09,
        alpha = 0,
        E0 = (5.49,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Allene hydrogen {Cd/H2/Ca}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "Cd/H/NonDeC;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.98e+07,"cm^3/(mol*s)"),
        n = 1.95,
        alpha = 0,
        E0 = (8.65,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCH=CR2 + H --> RC=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "C/H3/Cd;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (433000,"cm^3/(mol*s)"),
        n = 2.38,
        alpha = 0,
        E0 = (2.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CRCH3 + H --> R2C=CRCH2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "C/H2/OneDeC;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (699000,"cm^3/(mol*s)"),
        n = 2.36,
        alpha = 0,
        E0 = (1.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Primary allylic hydrogen {C/Cd/C/H2}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RR2C=CRCH2R + H --> R2C=CRCHR + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "C/H2/OneDeC;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7.79e+07,"cm^3/(mol*s)"),
        n = 1.78,
        alpha = 0,
        E0 = (2.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Primary propergylic {C/Ct/C/H2}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCCH2R + H --> RCCCHR + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "C/H/Cs2;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3.02e+06,"cm^3/(mol*s)"),
        n = 2.16,
        alpha = 0,
        E0 = (-0.45,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Secondary allylic hydrogen {C/Cd/C2/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CRCHR2 + H --> R2C=CRCR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "C/H/Cs2;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.21e+08,"cm^3/(mol*s)"),
        n = 1.72,
        alpha = 0,
        E0 = (-0.73,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Secondary propergylic {C/Ct/C2/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCCHR2 + H --> RCCCR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C/H2/TwoDe;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cd,Ct,CO,Cb} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7090,"cm^3/(mol*s)"),
        n = 2.85,
        alpha = 0,
        E0 = (-1.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CH-CH2-CH=CR2 + H --> R2C=CH-CH-CH=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "Cd/H/OneDe;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.93e+08,"cm^3/(mol*s)"),
        n = 1.74,
        alpha = 0,
        E0 = (10.28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Dienylic {Cd/Cd/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

R2C=CRCH=CR2 + H --> R2C=CRC=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "Cd/H/OneDe;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.18e+06,"cm^3/(mol*s)"),
        n = 2.4,
        alpha = 0,
        E0 = (6.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Eneynic {Cd/Ct/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCC-CH=CR2 + H --> RCC-C=CR2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "Ct_H;H_rad",
    group1 = 
"""
1  *1 C 0 {2,T} {3,S}
2     C 0 {1,T}
3  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.65e+08,"cm^3/(mol*s)"),
        n = 1.85,
        alpha = 0,
        E0 = (26.52,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCH + H --> RCC + H2

NOTE: There was a discrepancy in the rate values. The published values were: A = 1.30E+08, n = 1.88, 

E0 = 1.34E+04

RMG values: A=1.65E+08, n=1.85, E0=	26.52.

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "C/H3/Ct;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Ct 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.7e+07,"cm^3/(mol*s)"),
        n = 1.91,
        alpha = 0,
        E0 = (5.99,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCCCH3 + H --> RCCCH2 + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "Cd/H/NonDeO;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     O 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9.67e+09,"cm^3/(mol*s)"),
        n = 1.23,
        alpha = 0,
        E0 = (11.69,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "O/H/OneDe;H_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.3e+11,"cm^3/(mol*s)"),
        n = 0.82,
        alpha = 0,
        E0 = (7.75,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "Cd_pri;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3240,"cm^3/(mol*s)"),
        n = 2.58,
        alpha = 0,
        E0 = (14.04,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "C/H3/Cd;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (80.4,"cm^3/(mol*s)"),
        n = 2.92,
        alpha = 0,
        E0 = (7.16,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "O/H/NonDeC;C_methyl",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (254000,"cm^3/(mol*s)"),
        n = 1.89,
        alpha = 0,
        E0 = (8.97,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "CO/H/NonDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (29200,"cm^3/(mol*s)"),
        n = 2.29,
        alpha = 0,
        E0 = (5.44,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "O/H/OneDe;C_methyl",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (90700,"cm^3/(mol*s)"),
        n = 2.04,
        alpha = 0,
        E0 = (10.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Olefinic alcohol {O/Cd/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "O/H/OneDe;H_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3.3e+08,"cm^3/(mol*s)"),
        n = 1.56,
        alpha = 0,
        E0 = (13.94,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom. Acid O-H {O/CO/H}""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
Sumathi, R.; Carstensen, H.-H.; Green, W.H. Jr.; J. Phys. Chem. A. 2001, 105, 8978

Table 8: Modified ArrHenius Fitted Parameters for GA Predicted Rates.

RCOOOH + H --> RCOOO + H2

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "CO/H/NonDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4530,"cm^3/(mol*s)"),
        n = 2.43,
        alpha = 0,
        E0 = (8.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations. Rate expression per H atom.""",
    longDesc = 
u"""
Sumathy CBS-Q calculations. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "C_methane;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (19,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom. 
Same reaction as #19. 

Saeys, M.; Reyniers, M.-F.; Marin, G.B.; Van Speybroeck, V.; Waroquier, M. J. Phys. Chem. A 2003, 107, 9147 - 9159.

CH3 + CH4 --> CH4 + CH3

pg 9156 Table 6: Calculated and Experimental Activation Energies(kJ/mol) at 0 K, deltaE (0 k), 

for Three Families of Radical Reactions from Various Levels of Theory.

From reference: E0 = 71.0/4.185 = 16.97, @ 0 K, from database: E0 = 19.0 @ 300 - 1500 K

Experimental values from reference @ 0 K = 55.4 kJ/mol, 60.7 kJ/mol, 61.9 kJ/mol
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.8e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.15e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (15.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "C/H3/Cs;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.71e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.02e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.02e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.42e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C/H3/Cd;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.62e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.73e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "C/H/Cs2;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.73e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "C/H2/TwoDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cd,Ct,CO,Cb} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.54e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C/H/Cs;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.32e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "C/H3/Cb;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cb 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.9e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.7e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "C/H/Cs2;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.17e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "C/H3/Ct;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Ct 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.6e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.81e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "C/H2/TwoDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     {Cd,Ct,CO,Cb} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.38e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "C/H/Cs;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.43e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "C/H/Cs2;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.03e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Cd_pri;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.88e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Cd/H/NonDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.43e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "Cd/H/OneDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.78e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "Cd/H/OneDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.26e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (15.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Cd/H/OneDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.37e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "Ct_H;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,T} {3,S}
2     C 0 {1,T}
3  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.33e+18,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "Cb_H;C_methyl",
    group1 = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.17e+15,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (19.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.87e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "C/H2/NonDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.51e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.46e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "C/H2/OneDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.98e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "C_methane;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.87e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "C_methane;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (19,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "C_methane;C_rad/H2/Cd",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.53e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (30.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "C_methane;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.59e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "C_methane;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.86e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "C/H/Cs3;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (5.31e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "C/H/Cs3;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.02e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "C/H/Cs3;C_rad/H2/Cd",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.02e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "C/H/Cs3;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.95e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "C/H/Cs3;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.43e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "C/H/Cs3;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.03e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "C/H/Cs3;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.44e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "C/H/Cs3;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.46e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (21.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "C/H/Cs3;C_rad/Cs2",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.1e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (21.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "C/H/Cs3;Cd_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "C/H/Cs3;Cd_rad/OneDe",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.16e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "C/H/Cs3;C_rad/H2/Ct",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.14e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (17,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "C/H/Cs3;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.53e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "C/H/Cs3;C_rad/Cs2",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.78e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "Cd_pri;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3.39e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (15.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "Cd_pri;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.88e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "Cd_pri;C_rad/H2/Cd",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.36e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (30.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "Cd_pri;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.47e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "Cd_pri;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.93e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "Cd_pri;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.82e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (19.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "Cd_pri;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.25e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "Cd_pri;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.51e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (31.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "Cd_pri;C_rad/Cs2",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.39e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (38.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "Cd_pri;Cd_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.04e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "Cd_pri;Cd_rad/OneDe",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.3e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "Cd_pri;C_rad/H2/Ct",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.55e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (26.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "Cd_pri;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.41e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (28.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "Cd_pri;C_rad/Cs2",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.59e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (35.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "C/H3/Cd;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3.13e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "C/H3/Cd;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.62e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "C/H3/Cd;C_rad/H2/Cd",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.78e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (21.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "C/H3/Cd;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.73e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "C/H3/Cd;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.18e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "C/H3/Cd;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.6e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "C/H3/Cd;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.87e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "C/H3/Cd;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.52e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (21.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "C/H3/Cd;C_rad/Cs2",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.13e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (21.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "C/H3/Cd;Cd_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.52e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "C/H3/Cd;Cd_rad/OneDe",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.95e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "C/H3/Cd;C_rad/H2/Ct",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.58e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "C/H3/Cd;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.09e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "C/H3/Cd;C_rad/Cs2",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.32e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "H2;H_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.37e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "H2;C_methyl",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.95e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    label = "H2;C_rad/H2/Cd",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.87e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (25.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.49e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "H2;C_rad/Cs3",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.08e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.57e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "H2;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.04e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (15.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "H2;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.82e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (27,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "H2;C_rad/Cs2",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (27.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "H2;Cd_rad/NonDeC",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "H2;Cd_rad/OneDe",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.37e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    label = "H2;C_rad/H2/Ct",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.91e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (23,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "H2;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.34e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (24,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "H2;C_rad/Cs2",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.2e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (24.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment. Rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "C/H3/Cs;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.93e+06,"cm^3/(mol*s)"),
        n = 1.8,
        alpha = 0,
        E0 = (1.431,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. Fixed by RWest (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels. 
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: primary (a)
Verified by Karma James

**HOWEVER** This entry should probably use the numbers for primary(d) not primary(a).
Primary(a) is for a primary on neopentane; primary(d) is for a primary on propane.
Richard West. (Updated accordingly).

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206

Rate expression is changed to per H.(divided by 3)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "C/H2/NonDeC;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (450000,"cm^3/(mol*s)"),
        n = 2,
        alpha = 0,
        E0 = (-1.133,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels. 
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: secondary (b)

Verified by Karma James

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206


Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "C/H/Cs3;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.7e+06,"cm^3/(mol*s)"),
        n = 1.9,
        alpha = 0,
        E0 = (-1.451,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
http://dx.doi.org/10.1016/S0010-2180(01)00373-X

Rate expressions for H atom abstraction from fuels.
pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:OH, Site: tertiary (c)

Verified by Karma James

These numbers reported by Curran et al. were apparently taken from
N. Cohen, *Intl. J. Chem. Kinet.* 14 (1982), p. 1339 http://dx.doi.org/10.1002/kin.550141206
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "C/H3/Cs;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (950,"cm^3/(mol*s)"),
        n = 3.05,
        alpha = 0,
        E0 = (3.123,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "C/H2/NonDeC;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (23900,"cm^3/(mol*s)"),
        n = 2.71,
        alpha = 0,
        E0 = (2.106,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: secondary (b)

Verified by Karma James


Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "C/H/Cs3;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (383000,"cm^3/(mol*s)"),
        n = 2.41,
        alpha = 0,
        E0 = (1.14,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O, Site: tertiary (c)

Verified by Karma James


This rate parameter actually comes from following new mechanism for PRF.

https://www-pls.llnl.gov/data/docs/science_and_technology/chemistry/combustion/prf_2d_mech.txt

Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "C/H3/Cs;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20.435,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: primary (a)
Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "C/H2/NonDeC;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (17.686,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "C/H/Cs3;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.8e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.013,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:HO2, Site: tertiary (c)

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "C/H3/Cs;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.27e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "C/H2/NonDeC;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "C/H/Cs3;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.9e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:CH3O, Site: tertiary (c)

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "C/H3/Cs;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (50.76,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: primary (a)

Verified by Karma James

Rate expression is changed to per H.(divided by 9)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "C/H2/NonDeC;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (48.21,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels. (changed to per H)""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: secondary (b)

Verified by Karma James

Rate expression is changed to per H.(divided by 2)
Yushi Suzuki
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    label = "C/H/Cs3;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (46.06,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] Rate expressions for H atom abstraction from fuels.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Rate expressions for H atom abstraction from fuels.

pg 257 A Comprehensive Modelling Study of iso-Octane Oxidation, Table 1. Radical:O2, Site: tertiary (c)

Verified by Karma James
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    label = "H2;O2b",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.25e+13,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (56.64,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (800,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + O2 --> H + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1091, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 3,2.

Verified by Karma James

pg. 1109: Discussion of evaluated data

Recommended value computed using reverse rate and thermodynamics

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4730,"cm^3/(mol*s)"),
        n = 2.56,
        alpha = 0,
        E0 = (5.03,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (3000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Knyazev et al. [119] Transition state theory.""",
    longDesc = 
u"""
[119] Knyazev, V.D; Bencsura, A.; Stoliarov, S.I.; Slagle, I.R. J. Phys. Chem. 1996, 100, 11346.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2 ( from A = 9.45E+03), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11100,"cm^3/(mol*s)"),
        n = 2.48,
        alpha = 0,
        E0 = (7.13,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (3500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mebel et al. [120] Transition state theory.""",
    longDesc = 
u"""
[120] Mebel, A.M.; Morokuma, K.; Lin, M.C. J Chem. Phys. 1995, 103, 3440.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2, to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    label = "H2;Cd_pri_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.58e+09,"cm^3/(mol*s)"),
        n = 0.7,
        alpha = 0,
        E0 = (5.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Weissman et al. [121] Transition state theory.""",
    longDesc = 
u"""
[121] Weissman, M.A.; Benson, S.W. J. Phys. Chem. 1988, 92, 4080.
H2 + C2H3 --> H + C2H4 C.D.W divided original rate expression by 2 ( from A = 3.15E+09), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    label = "H2;Ct_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (5.4e+12,"cm^3/(mol*s)","*|/",3.16),
        n = 0,
        alpha = 0,
        E0 = (2.17,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

H2 + C2H --> H + C2H2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 863 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 1. Bimolecular reactions - C2H Radical Reactions.

Verified by Karma James

pg.1013-1014: Discussion on evaluated data

C2H+H2-->C2H2+H: Recommended rate coefficient is that reported by Koshi et al.  Rate

coefficient was computed for low temperatures, but extrapolation to higher temperatures
fits other reported data reasonably well.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    label = "H2;Cb_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (28600,"cm^3/(mol*s)"),
        n = 2.43,
        alpha = 0,
        E0 = (6.28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (5000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mebel et al. [122] Transition state theory.""",
    longDesc = 
u"""
[122] Mebel, A.M.; Lin, M.C.; Yu, T.; Morokuma, K. J. Phys. Chem. A. 1997, 101, 3189.
H2 + phenyl --> H + benzene C.D.W divided original rate expression by 2 ( from A = 5.71E+04), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    label = "H2;CO_pri_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (900000,"cm^3/(mol*s)","*|/",5),
        n = 2,
        alpha = 0,
        E0 = (17.83,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + HCO --> H + CH2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,2.

Verified by Karma James

pg. 1147: Discussion of evaluated data

Recommended value computed using reverse rate and thermodynamics

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "H2;CO_rad/NonDe",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.06e+06,"cm^3/(mol*s)","*|/",3),
        n = 1.82,
        alpha = 0,
        E0 = (17.61,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2 + CH3CO --> H + CH3CHO C.D.W divided original rate expression by 2, to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 1229: Discussion on evaluated data

No experimental data for forward rxn, at the time

Reviewers noticed that k(H+HCHO=H2+HCO) / k(H+CH3CHO=H2+CH3CO) ~ 2, due to double the number of H atoms available

Used 0.5*k(H+HCHO=H2+HCO) and equilibrium constant to compute recommended rate expression

Verified by MRH on 10Aug2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    label = "H2;O_pri_rad",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.1e+08,"cm^3/(mol*s)"),
        n = 1.21,
        alpha = 0,
        E0 = (4.71,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (2400,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Isaacson [123] Transition state theory.""",
    longDesc = 
u"""
[123] Isaacson, A.D. J. Chem. Phys. 1997, 107, 3832.
H2 + O2 --> H + H2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

166. [100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.

H2 + CH3O --> H + CH3OH The calculated reverse rate constants are in good agreement with experiment. (This is -R1 in the paper)

C.D.W divided original rate expression by 2, to get rate expression per H atom.

Verified by Greg Magoon; maximum error of fitted expression from tabular data for forward rate constant, kr1 is 15% (cf. p. 3758)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "H2;O_rad/NonDeC",
    group1 = 
"""
1  *1 H 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0632,"cm^3/(mol*s)"),
        n = 4,
        alpha = 0,
        E0 = (4.91,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    label = "C_methane;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.925e+12,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (56.83,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH4 + O2 --> CH3 + HO2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 417 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O2 Reactions.

Verified by Karma James

pg.483: Discussion on evaluated data

O2+CH4 --> HO2+CH3: Recommended data based on experimental value for CH2O + O2 -->

HO2 + HCO.  Assumes equal A factor per C-H bond and Ea = deltaH.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    label = "C_methane;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.0216,"cm^3/(mol*s)","*|/",2),
        n = 4.14,
        alpha = 0,
        E0 = (12.56,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + C2H5 --> CH3 + C2H6 C.D.W divided original rate expression by 4, to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 1177: Discussion on evaluated data

No experimental data for forward rxn, at the time

Recommended data from reverse rate and equilibrium constant

Verified by MRH on 10Aug2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    label = "C_methane;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000181,"cm^3/(mol*s)","*|/",2),
        n = 4.4,
        alpha = 0,
        E0 = (10.79,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH4 + iso-C3H7 --> CH3 + C3H8 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,10.

Verified by Karma James

pg. 935: Discussion on evaluated data

Entry 42,10: No data available at the time.  Author recommends rate coefficient

expression based on reverse rate and equilibrium constant.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    label = "C_methane;Ct_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (4.53e+11,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (0.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + C2H --> CH3 + C2H2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,10.

Verified by Karma James

pg. 1220: Discussion of evaluated data

Recommended data is expression given by Brown and Laufer (1981).

They computed the pre-exponential factor by the bond energy-bond order (BEBO) method

and combined that with experimental k at room temperature to yield Arrhenius expression
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "C_methane;Cb_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (5e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.6,"kcal/mol"),
        Tmin = (560,"K"),
        Tmax = (1410,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Heckmann et al. [124]""",
    longDesc = 
u"""
[124] Heckmann, E.; Hippler, H. Troe, J. Sypm. Int. Combust. Proc. 1996, 26, 543.
Absolute value measured directly (excitation technique: thermal, analytical technique: vis-UV absorption) CH4 + phenyl --> benzene

C.D.W divided original rate expression by 4, to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    label = "C_methane;CO_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1820,"cm^3/(mol*s)","*|/",5),
        n = 2.85,
        alpha = 0,
        E0 = (22.46,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + HCO --> CH3 + CH2O C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,10.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data computed using reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    label = "C_methane;CO_rad/NonDe",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (543,"cm^3/(mol*s)","*|/",5),
        n = 2.88,
        alpha = 0,
        E0 = (21.46,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + CH3CO --> CH3 + CH3CHO C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,10.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended number computed from reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    label = "C_methane;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.385,"cm^3/(mol*s)"),
        n = 3.95,
        alpha = 0,
        E0 = (0.55,"kcal/mol"),
        Tmin = (223,"K"),
        Tmax = (2400,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Melissas and Truhlar [125] Transition state theory.""",
    longDesc = 
u"""
[125] Melissas, V.S.; Truhlar, D.G. J. Chem. Phys. 1993,99,1010.
CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    label = "C_methane;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.93e+06,"cm^3/(mol*s)","*|/",1.41),
        n = 1.83,
        alpha = 0,
        E0 = (2.78,"kcal/mol"),
        Tmin = (240,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 419 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.571-572: Discussion on evaluated data

OH+CH4 --> H2O+CH3: "The preferred value of k is that obtained experimentally by

Madronich and Felder which predicts very precisely the data obtained between
240 and 2000K."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    label = "C_methane;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.55e+07,"cm^3/(mol*s)"),
        n = 1.6,
        alpha = 0,
        E0 = (3.12,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1510,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Cohen et al. [101] Transition state theory.""",
    longDesc = 
u"""
[101] Cohen, N. Int. J. Chem. Kinet. 1991, 23, 397.
CH4 + OH --> CH3 + H2O C.D.W divided original rate expression by 4, to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    label = "C_methane;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000155,"cm^3/(mol*s)"),
        n = 5,
        alpha = 0,
        E0 = (5.58,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH4 + CH3O --> CH3 + CH3OH The calculated reverse rate constants are in good agreement with experiment. (Rxn. -R3 in paper)

C.D.W divided original rate expression by 4 ( from A= 1.51E+09), to get rate expression per H atom.

Verified by Greg Magoon; cf. reverse reaction, #261, below
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    label = "C_methane;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.53e+10,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (18.58,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH4 + HO2 --> CH3 + H2O2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1093, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 10,7.

Verified by Karma James

pg. 1131: Discussion on evaluated data

Recommended data is based on expression for HO2 attach on alkanes (Walker)

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    label = "C/H3/Cs;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.005e+13,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (51.87,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

C2H6 + O2 --> C2H5 + HO2 C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 417 Evaluated Kinetic Data for Combustion Modelling  Table 1. Bimolecular reactions - O2 Reactions. (The value for E0 does not 

match the value in the reference, E0 RMG = 1.87; E0 Reference = 51.86)

Verified by Karma James

pg.484: Discussion on evaluated data

O2+C2H6 --> HO2+C2H5: "The value given in the Walker review has been modified slightly

to allow for the higher heat of formation of the C2H5 radical now recommended
and for an assumed equal A factor per C-H bond in CH2O+O2 and C2H6+O2."
*** NOTE: MRH agrees with KJ on discrepancy in RMG-stored E0.  MRH is changing the value

of E0 in RMG from 1.87 kcal/mol to 51.87 kcal/mol. ***
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "C/H3/Cs;Ct_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (6.02e+11,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + C2H --> C2H5 + C2H2 C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,11.

Verified by Karma James

pg. 1221: Discussion on evaluated data

Recommended data is based on expression given by Brown and Laufer (1981).

Brown and Laufer calculated pre-exponential factor by BEBO method and
combined calculation with experimental measurement of k at room temperature.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "C/H3/Cs;Cb_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (3.48e+10,"cm^3/(mol*s)","*|/",2.35),
        n = 0,
        alpha = 0,
        E0 = (4.44,"kcal/mol","+|-",0.18),
        Tmin = (565,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Park et al. [126]""",
    longDesc = 
u"""
[126] Park, J.; Gheyas, S.; Lin, M.C. Int. J. Chem. Kinet. 2001, 33, 64.
Absolute value measured directly. Static or low flow, flash photolysis excitation, Vis-UV absoprtion analysis. 

Phenyl radicals are produced from 193 nm photolysis of C6H5COCH3. The cavity ringdown spectroscopy and/or mass spectroscopy

have been used to monitor reactant and/or products. C2H6 + phenyl --> C2H5 + benzene.

C.D.W divided original rate expression by 6 ( from A= 2.09E+11), to get rate expression per H atom. Original delta A = 2.0E+10.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "C/H3/Cs;CO_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7820,"cm^3/(mol*s)","*|/",5),
        n = 2.72,
        alpha = 0,
        E0 = (18.24,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + HCO --> C2H5 + CH2O C.D.W divided original rate expression by 6(from A = 4.69E+04), to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,11.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data computed from reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "C/H3/Cs;CO_rad/NonDe",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3020,"cm^3/(mol*s)","*|/",5),
        n = 2.75,
        alpha = 0,
        E0 = (17.53,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H6 + CH3CO --> C2H5 + CH3CHO C.D.W divided original rate expression by 6(from A = 1.81E+04), to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,11.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended data computed using rate of C2H5+CH2O divided by 2 (since only one O=C-H

hydrogen is present in CH3CHO) and equilibrium constant
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "C/H3/Cs;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.2e+06,"cm^3/(mol*s)","*|/",1.41),
        n = 2,
        alpha = 0,
        E0 = (0.86,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

C2H6 + OH --> C2H5 + H2O C.D.W divided original rate expression by 6, to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.589-590: Discussion on evaluated data

OH+C2H6 --> H2O+C2H5: "The preferred value of k is almost indistinguishable from the

value obtained by Cohen from transition state calculations carried out for
temperatures between 300 and 2000K."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "C/H3/CO;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     CO 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (517000,"cm^3/(mol*s)"),
        n = 2.2,
        alpha = 0,
        E0 = (1,"kcal/mol"),
        Tmin = (295,"K"),
        Tmax = (600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Taylor et al. [127] Transition state theory.""",
    longDesc = 
u"""
[127] Taylor, P.H.; Rahman, M.S.; Arif, M.; Dellinger, B.; Marshall, P. Sypm. Int. Combust. Proc. 1996, 26, 497.
CH3CHO + OH --> CH2CHO + H2O Rate constant is high pressure limit (pressure 0.13-0.97atm?) 

C.D.W divided original rate expression by 3(from A = 1.55E+06), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "C/H3/O;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000205,"cm^3/(mol*s)"),
        n = 4.9,
        alpha = 0,
        E0 = (6.72,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH3OH + CH3 --> CH2OH + CH4 The calculated rate constants are in good agreement with experiment. (Rxn. R4 in paper)

C.D.W divided original rate expression by 3 ( from A= 8.43E+08), to get rate expression per H atom.

Verified by Greg Magoon
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    label = "C/H3/O;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8140,"cm^3/(mol*s)"),
        n = 2.8,
        alpha = 0,
        E0 = (-0.42,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
CH3OH + OH --> CH2OH + H2O The calculated rate constants are in good agreement with experiment. (Rxn. R6 in paper)

C.D.W divided original rate expression by 3 ( from A= 2.11E+11), to get rate expression per H atom.

Verified by Greg Magoon
**Note that R2 from this paper appears to be missing from the RMG library, so I have added it as 1001**
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    label = "C/H2/NonDeC;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.985e+13,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (47.69,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + O2 --> iso-C3H7 + HO2  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,3.

//NOTE: For A value, Database value = 1.985E+13 and Reference value = 1.65E+13

Verified by Karma James

NOTE: MRH computed Reference A value of 1.99E+13 (11Aug2009)

pg. 899: Discussion on evaluated data

Entry 40,3 (b): No data available at the time.  The author "estimates" the rate

coefficient expressions (no indication of how).
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    label = "C/H2/NonDeC;CH2_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.755,"cm^3/(mol*s)","*|/",10),
        n = 3.46,
        alpha = 0,
        E0 = (7.47,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH2 --> iso-C3H7 + CH3  C.D.W divided original rate expression by 2(from A = 1.51), to get rate expression per H atom.

pg 892, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,26.
Verified by Karma James

pg. 910: Discussion on evaluated data

Entry 40,26 (b): No data available at the time.  Author estimates the rate coefficient

expression as that of CH3+C3H8=i-C3H7+CH4.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    label = "C/H2/NonDeC;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (23900,"cm^3/(mol*s)","*|/",2),
        n = 2.71,
        alpha = 0,
        E0 = (2.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + O --> iso-C3H7 + OH  C.D.W divided original rate expression by 2(from A = 4.77E+04), to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,5.

Verified by Karma James

pg. 901: Discussion on evaluated data

Entry 40,5 (b): The author notes "considerable scatter" among the existing data.  The

author computed Arrhenius A and n parameters using a BEBO calculation and performed
a "fit" on the data reported by Herron and Huie to obtain the Arrhenius E.  This
rate coefficient expression is stated to fit 3 (of the 5) raw data reported.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    label = "C/H2/NonDeC;C_rad/H2/O",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (30.2,"cm^3/(mol*s)","*|/",5),
        n = 2.95,
        alpha = 0,
        E0 = (11.98,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH2OH --> iso-C3H7 + CH3OH  C.D.W divided original rate expression by 2(from A = 6.03E+01), to get rate expression per H atom.

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

pg. 910: Discussion on evaluated data

Entry 40,39 (b)

No experimental data, at the time

Recommended value for C3H8+CH2OH-->n-C3H7+CH3OH comes from rate for C2H6+CH2OH-->C2H5+CH3OH

No discussion on where rate for C3H8+CH2OH-->i-C3H7+CH3OH comes from:

A is ~ factor of 3 smaller (6 hydrogens vs 2 ... seems reasonable to MRH)
E is 1 kcal/mol smaller (more stable to form secondary radical than primary)
Verified by MRH on 10Aug2009

MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    label = "C/H2/NonDeC;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (510,"cm^3/(mol*s)","*|/",10),
        n = 3.1,
        alpha = 0,
        E0 = (8.82,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + C2H3 --> iso-C3H7 + C2H4  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,19.

Verified by Karma James

pg. 906: Discussion on evaluated data

Entry 40,19 (b): No data available at the time.  The author recommends the rate coefficient

expression of C2H3+C2H6=C2H5+C2H4 for the rxn C2H3+C3H8=n-C3H7+C2H4.  The author
assumes the ratio of secondary-to-primary H-atom abstraction for the rxn CH3+C3H8
to obtain the recommended rate coefficient expression.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    label = "C/H2/NonDeC;Ct_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (6.05e+11,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + C2H --> iso-C3H7 + C2H2  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,21.

Verified by Karma James

pg. 906-907: Discussion on evaluated data

Entry 40,21 (b): No data available at the time.  The author recommends the rate coefficient

of C2H6+C2H=C2H2+C2H5 for the rxn C3H8+C2H=C2H2+n-C3H7.  Due to the high exothermicity
of the rxn, the author assumes the H-atom abstraction rxn is limited to the number
of H-atoms available, thus recommedning a rate coefficient equal to one-third that
recommended for C3H8+C2H=C2H2+n-C3H7.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    label = "C/H2/NonDeC;CO_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.4e+06,"cm^3/(mol*s)","*|/",3),
        n = 1.9,
        alpha = 0,
        E0 = (17.01,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + HCO --> iso-C3H7 + CH2O  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,15.

Verified by Karma James

pg. 904: Discussion on evaluated data

Entry 40,15 (b): No data available at the time.  The author recommends a rate coefficient

expression based on the reverse rxn (note: the author uses the rate of the rxn
n-C3H7+CH2O=HCO+C3H8 instead of i-C3H7+CH2O=HCO+C3H8) and equilibrium constant.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    label = "C/H2/NonDeC;CO_rad/NonDe",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.65e+06,"cm^3/(mol*s)","*|/",3),
        n = 2,
        alpha = 0,
        E0 = (16.24,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH3CO --> iso-C3H7 + CH3CHO  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,22.

Verified by Karma James

pg. 907: Discussion on evaluated data

Entry 40,22 (b): No data available at the time.  The author recommends a rate coefficient

expression based on the equilibrium constant and the reverse rate (note: the author
estimates this reverse rate using the suggestions of Kerr, J.A. and Trotman-Dickenson, A.F.).
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    label = "C/H2/NonDeC;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.95e+06,"cm^3/(mol*s)"),
        n = 1.9,
        alpha = 0,
        E0 = (0.16,"kcal/mol"),
        Tmin = (295,"K"),
        Tmax = (1220,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Cohen et al. [101] Transition state theory.""",
    longDesc = 
u"""
[101] Cohen, N. Int. J. Chem. Kinet. 1991, 23, 397.
C3H8 + OH --> iso-C3H7 + H20  C.D.W divided original rate expression by 2, to get rate expression per H atom.

Not yet checked
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    label = "C/H2/NonDeC;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.25e+10,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (4.57,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
C3H8 + CH3O --> iso-C3H7 + CH3OH  C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 891, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 40,24.

Verified by Karma James

pg. 908: Discussion on evaluated data

Entry 40,24 (b): The author assumes the Arrhenius A parameter should follow:

A(C3H8+CH3O=CH3OH+n-C3H7) / A(C3H8+CH3O=CH3OH+i-C3H7) = 3
The author also demands that the recommended data fit both sets of experiments
reported.  These assumptions (plus one unwritten one, as we still have 3
unknown parameters [A1, E1, E2 ... A2=f(A1)]) produce the reported rate
coefficient expression.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    label = "C/H/Cs3;O2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.97e+13,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (43.92,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + O2 --> tert-C4H9 + HO2

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,3.

Verified by Karma James

pg.14: Discussion on evaluated data

Entry 43,3(b): No direct measurements at the time.  A review article reported a rate

coefficient expression for iC4H10+O2-->tC4H9+HO2.  An experiment performed by
Baldwin, Drewery, and Walker reported a rate coefficient expression for O2 abstracting
a tertiary H-atom from 2,3-dimethylbutane.  The experiment's value matched well
with the review's value, so Tsang recommended the review's value.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    label = "C/H/Cs3;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (157000,"cm^3/(mol*s)","*|/",2),
        n = 2.5,
        alpha = 0,
        E0 = (1.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + O --> tert-C4H9 + OH

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,5.

Verified by Karma James

pg.15: Discussion on evaluated data

Entry 43,5(b): Michael et al. reported the rate coefficient expression for iC4H10+O=OH+C4H9 isomer.

Tsang subtracted from this expression the contributions from iC4H10+O=OH+iC4H9 (What
rate expression was used?  The one recommended here?) to obtain an expression for
iC4H10+O=OH+tC4H9.  Tsang then adjusted the rate expression such that the A-factor's
temperature dependence was 2.5 (was this 2.5 based on the review by Cohen and Westberg?).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    label = "C/H/Cs3;CH2_triplet",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.09e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (4.91,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH2 --> tert-C4H9 + CH3

pg 6, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,25.

Verified by Karma James

pg.23-24: Discussion on evaluated data

Entry 43,25(b): Tsang recommends the rate coefficient expression reported by Bohland et al.

Tsang notes that the rate for CH2_triplet abstracting a H-atom is faster than
the recommended value for CH3 abstracting a H-atom.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    label = "C/H/Cs3;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.904,"cm^3/(mol*s)","*|/",5),
        n = 3.46,
        alpha = 0,
        E0 = (2.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + C2H3 --> tert-C4H9 + C2H4

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,19.

Verified by Karma James

pg.20: Discussion on evaluated data

Entry 43,19(b): No data available at the time.  Author recommends rate coefficient expression

based on the rxn CH3+iC4H10=CH4+tC4H9: same Arrhenius A and n parameters, Ea decreased
by 8.5 kJ/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    label = "C/H/Cs3;Ct_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (6.62e+11,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + C2H --> tert-C4H9 + C2H2

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,21.

Verified by Karma James

pg.21: Discussion on evaluated data

Entry 43,21(b): No data available at the time.  For the rxn iC4H10+C2H=C2H2+iC4H9, author

recommends 1.5x the rate of the rxn C2H6+C2H=C2H2+C2H5 (9 vs. 6 primary H-atoms).
The author then recommends a rate coefficient for iC4H10+C2H=C2H2+tC4H9 that appears
to be 1/9 the rate of iC4H10+C2H=C2H2+iC4H9 (9 vs. 1 H-atom).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    label = "C/H/Cs3;CO_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (34300,"cm^3/(mol*s)","*|/",5),
        n = 2.5,
        alpha = 0,
        E0 = (13.51,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + HCO --> tert-C4H9 + CH2O

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,15.

Verified by Karma James

pg.18: Discussion on evaluated data

Entry 43,15(b): No data available at the time.  For the rxn iC4H10+HCO=CH2O+iC4H9, author

recommends 1.5x the rate of the rxn C3H8+HCO+CH2O+nC3H7 (9 vs. 6 primary H-atoms).
The author then recommends the rate coefficient for iC4H10+HCO=CH2O+tC4H9 to be the 
rate coefficient of iC4H10+HCO=CH2O+iC4H9, with the A factor divided by 9 (9 vs. 1
H-atoms) and the Ea decreased by 20 kJ/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    label = "C/H/Cs3;CO_rad/NonDe",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (34300,"cm^3/(mol*s)","*|/",10),
        n = 2.5,
        alpha = 0,
        E0 = (13.51,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH3CO --> tert-C4H9 + CH3CHO

pg 5, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,22.

Verified by Karma James

pg.21: Discussion on evaluated data

Entry 43,22(b): No data available at the time.  Author recommends rate coefficient expression

based on the rxn iC4H10+HCO=CH2O+tC4H9.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    label = "C/H/Cs3;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.57e+06,"cm^3/(mol*s)"),
        n = 1.9,
        alpha = 0,
        E0 = (1.45,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1150,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Cohen et al. [101] Transition state theory.""",
    longDesc = 
u"""
[101] Cohen, N. Int. J. Chem. Kinet. 1991, 23, 397.
Iso-C4H10 + OH --> tert-C4H9 + H2O

Not yet checked
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    label = "C/H/Cs3;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.29e+10,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (2.88,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
Iso-C4H10 + CH3O --> tert-C4H9 + CH3OH

pg 6, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 43,24.

Verified by Karma James

pg.22: Discussion on evaluated data

Entry 43,24(b): A study by Berces and Trotman-Dickenson reported a rate coefficient

for the rxn iC4H10+CH3O=CH3OH+C4H9 isomer.  Tsang used the rate coefficient for
the rxn CH3O+C(CH3)4=CH3OH+H2C*-C(CH3)3 determined by Shaw and Trotman-Dickenson
as a characteristic for CH3O+primary H-atom abstraction to recommend a rate coefficient
for iC4H10+CH3O=CH3OH+iC4H9.  This rate expression was subtracted from the rate
coefficient reported by Berces and Trotman-Dickenson to yield the rate coefficient
for iC4H10+CH3O=CH3OH+tC4H9.  Lastly, the pre-exponential factor was cut in half,
due to Tsang's correcting an arithmetic error by Kerr and Parsonage (perhaps this
work was referenced in the Berces and Trotman-Dickenson study?)
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    label = "Cd_pri;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.792e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (60.01,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Hua, Ruscic, and Wang 2005, transition state theory.""",
    longDesc = 
u"""
FORMER RATES
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H4 + O2 --> C2H3 + HO2 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1097, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 18,3.

Verified by Karma James

pg. 1184: Discussion on evaluated data

Recommended data follows Walker's estimates for O2+alkane

Note: The authors note that a lower lying channel, involving addition and
rearrangement prior to decomposition, may exist.
MRH 28-Aug-2009


CURRENT RATES
Hua, H.; B. Ruscic; B. Wang.  Chemical Physics 2005, 311, 335-341.
C2H4 + O2 --> C2H3 + HO2.

Divided rate expression by 4 to get the rate expression per H atom.  See page 338.
Overall, this agrees with the earlier rate that we used.
JDM 15-Jun-2010.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    label = "Cd_pri;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (3.78e+06,"cm^3/(mol*s)"),
        n = 1.91,
        alpha = 0,
        E0 = (3.74,"kcal/mol"),
        Tmin = (290,"K"),
        Tmax = (1510,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mahmud et al. [128] Transition state theory""",
    longDesc = 
u"""
[128] Mahmud, K.; Marshall, P.; Fontijn, A. J Phys. Chem. 1987, 91, `568.
C2H4 + O --> C2H3 + OH C.D.W divided original rate expression by 4(from A= 1.51E+07), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    label = "Cd_pri;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (158,"cm^3/(mol*s)","*|/",10),
        n = 3.13,
        alpha = 0,
        E0 = (18,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H4 + C2H5 --> C2H3 + C2H6 C.D.W divided original rate expression by 4, to get rate expression per H atom.

pg 1098, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 18,17.

Verified by Karma James

pgs. 1191-1192: Discussion on evaluated data

Recommended data based on study performed by Halstead and Quinn

Tsang fit the data against BEBO calculations (to attain the Arrhenius A, n)
and manually adjusted the E.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    label = "Cd_pri;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.13e+12,"cm^3/(mol*s)","*|/",3.16),
        n = 0,
        alpha = 0,
        E0 = (5.94,"kcal/mol"),
        Tmin = (650,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

C2H4 + OH --> C2H3 + H2O C.D.W divided original rate expression by 4(from A= 2.05E+13), to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.586-587: Discussion on evaluated data

OH+C2H4 --> H2O+C2H3: Recommended rate taken from expression reported by Tully (1988).

MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    label = "Cd/H/NonDeC;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (6.02e+10,"cm^3/(mol*s)","*|/",3),
        n = 0.7,
        alpha = 0,
        E0 = (7.63,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + O --> CH3C=CH2 + OH

pg 233-234: Discussion on evaluated data

Verified by MRH on 6Aug2009

Entry 46,5(f): No measurements on H-atom abstraction rxns. Recommended rate coefficient

is computed as follows:

The rate of O + C3H6 --> OH + H2C=CH-*CH2 is computed using the expression:
[k(O+C2H6-->C2H5+HO)/k(OH+C2H6-->C2H5+H2O)] * k(OH+C3H6-->H2C=CH-*CH2+H2O).
The author uses this expression because he notes that OH and O H-atom abstraction
rxns generally follow the same trend.  The O+C2H6, OH+C2H6, and OH+C3H6
are from other Tsang review articles.
The rate of O+C3H6 --> OH+CH3C=CH2 is computed by adjusting the O+C3H6 --> OH+H2C=CH-*CH2
rate coefficient: increasing the Ea/R by 880 Kelvin and multiplying the A
by ~0.345; these values come from the relative difference between the rxns
OH+C3H6 --> H2O+H2C=CH-*CH2 and OH+C3H6 --> H2O+CH3C=CH2
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    label = "Cd/H/NonDeC;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (409000,"cm^3/(mol*s)","*|/",4),
        n = 2.5,
        alpha = 0,
        E0 = (9.79,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + H --> CH3C=CH2 + H2

pg 231: Discussion on evaluated data

Previous modified Arrhenius parameters were for RELATIVE rate (kc/ka)

Multipled kc/ka by ka to get kc (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,4(c): No data available for H-atom abstraction rxns.  The recommended rate

coefficient is based on the author's assumption that methyl substitution has the
same influence in olefins as in alkanes.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    label = "Cd/H/NonDeC;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.842,"cm^3/(mol*s)","*|/",6),
        n = 3.5,
        alpha = 0,
        E0 = (11.66,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + CH3 --> CH3C=CH2 + CH4

pg 237-239

Previous modified Arrhenius parameters were for RELATIVE rate (ke/kc)

Multiplied ke/kc by kc to get ke (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,16(e): Recommended rate coefficient is based on the author's assumption

that methyl substitution has the same influence in olefins as in alkanes.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    label = "Cd/H/NonDeC;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.842,"cm^3/(mol*s)","*|/",6),
        n = 3.5,
        alpha = 0,
        E0 = (9.67,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + C2H3 --> CH3C=CH2 + C2H4

pg 240-241

Previous modified Arrhenius parameters were for RELATIVE rate (kc/ka)

Multiplied kc/ka by ka to get kc (only one H to abstract, so no division necessary)

Certified by MRH on 6Aug2009

Entry 46,19(c): No data available at the time.  The recommended rate coefficient

is based on the rate expressions for CH3 abstracting a H-atom from C3H6; all of
the Ea's have been decreased by 4kJ/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    label = "Cd/H/NonDeC;Ct_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + C2H --> CH3C=CH2 + C2H2 

pg 241

Verified by MRH on 6Aug2009

Entry 46,21(e): No data available at the time.  Recommended rate expression is "somewhat

smaller" than the rate of rxn C3H6+C2H --> C2H2+H2C=CH-*CH2.  The rate of this rxn
is assumed to be the rate of the rxn C2H+C2H6 --> C2H2+C2H5.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    label = "Cd/H/NonDeC;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.11e+06,"cm^3/(mol*s)","*|/",2),
        n = 2,
        alpha = 0,
        E0 = (1.45,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang, W. J. Phys. Chem. Ref. Data 1991, 20, 221.
CH3CH=CH2 + OH --> CH3C=CH2 + H2O

pg 235-236

Valid T range in reference suggested 700-2500K

Uncertainty stated in reference was *2.0

Verified by MRH on 6Aug2009

Entry 46,6(d): No direct measurements of H-atom abstraction rxns.  The recommended

H-atom abstraction rxns are based on "the results of Tully (1988) for the rxn
of OH + C2H4 and the rate constant ratio of OH + primary Hydrogens in ethane by
Tully et al. (1986) to OH + secondary Hydrogens by Droege and Tully (1986)".  The
author has also introduced a T^2 dependence in the A-factor.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    label = "Ct_H;O2b",
    group1 = 
"""
1  *1 C 0 {2,T} {3,S}
2     C 0 {1,T}
3  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.05e+12,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (74.52,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + O2 --> C2H + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,3.

Verified by Karma James

pg. 1209: Discussion on evaluated data

Recommended data based on report by Walker

NOTE: Authors note that a lower-lying channel of O2 addition, rearrangement,
and decomposition may exist.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    label = "Ct_H;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,T} {3,S}
2     C 0 {1,T}
3  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.36e+11,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (23.45,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + C2H5 --> C2H + C2H6 C.D.W divided original rate expression by 2 (from A= 2.71E+11), to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,17.

Verified by Karma James

pg. 1215: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    label = "Ct_H;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,T} {3,S}
2     C 0 {1,T}
3  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7250,"cm^3/(mol*s)","*|/",10),
        n = 2.68,
        alpha = 0,
        E0 = (12.04,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
C2H2 + OH --> C2H + H2O C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1100, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 20,6.

Verified by Karma James

pg. 1213: Discussion on evaluated data

Recommended data is derived from BEBO method calculation

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    label = "Cb_H;O2b",
    group1 = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.052e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (60.01,"kcal/mol"),
        Tmin = (1200,"K"),
        Tmax = (1700,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Asaba et al. [129]. Data are estimated.""",
    longDesc = 
u"""
[129] Asaba, T.; Fujii, N.; Proc. Int. Symp. Shock Tubes Waves 1971, 8, 1.
Benzene + O2 --> phenyl + HO2 C.D.W divided original rate expression by 6(from A = 6.31E+13), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    label = "Cb_H;H_rad",
    group1 = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+08,"cm^3/(mol*s)"),
        n = 1.8,
        alpha = 0,
        E0 = (16.35,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (800,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Mebel et al. [122] RRK(M) extrapolation.""",
    longDesc = 
u"""
[122] Mebel, A.M.; Lin, M.C.; Yu, T.; Morokuma, K. J. Phys. Chem. A. 1997, 101, 3189.
Rate constant is high pressure limit. Benzene + H --> phenyl + H2

C.D.W divided original rate expression by 6(from A = 6.02E+08), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    label = "Cb_H;H_rad",
    group1 = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (5.02e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.11,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Nicovich et al. [130]""",
    longDesc = 
u"""
[130] Nicovich, J.M.; Ravishankara, A.R. J. Phys. Chem. 1984, 88, 2534.
Pressure 0.01-0.26 atm Excitation: flash photolysis, analysis: resonance fluorescence. Benzene + H --> phenyl + H2

C.D.W divided original rate expression by 6(from A = 3.01E+12), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    label = "Cb_H;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.05e+11,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (14.86,"kcal/mol","+|-",1.19),
        Tmin = (650,"K"),
        Tmax = (770,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Zhang et al. [131]""",
    longDesc = 
u"""
[131] Zhang, H.X.; Ahonkhai, S.I. Back, H.M. Can. J. Chem. 1989, 67, 1541.
Pressure 0.30-0.50 atm Excitation: thermal, analysis: GC. Benzene + C2H5 --> phenyl + C2H6

C.D.W divided original rate expression by 6(from A = 6.31E+11), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    label = "Cb_H;O_pri_rad",
    group1 = 
"""
1  *1 Cb 0 {2,B} {3,B} {4,S}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
4  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.72e+07,"cm^3/(mol*s)","*|/",2),
        n = 1.42,
        alpha = 0,
        E0 = (1.45,"kcal/mol"),
        Tmin = (400,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

Benzene + OH --> phenyl + H2O  C.D.W divided original rate expression by 6(from A = 1.63E+08), to get rate expression per H atom.

pg 420 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.595-597: Discussion on evaluated data

OH+C6H6 --> H2O+C6H5: Authors note that this rxn should be dominant at temperatures

above 500K.  No other comment on where the recommended rate expression comes from
(although MRH believes it is a best-fit to the available data, based on graph).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    label = "CO_pri;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.34e+07,"cm^3/(mol*s)"),
        n = 2.05,
        alpha = 0,
        E0 = (37.93,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2200,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Michael et al. [132] Transition state theory.""",
    longDesc = 
u"""
[132] Michael, J.V.; Kumaran, S.S.; Su, M.-C. J. Phys. Chem. A. 1999, 103, 5942.
CH2O + O2 --> HCO + HO2 C.D.W divided original rate expression by 2, to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 228,
    label = "CO_pri;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (2.08e+11,"cm^3/(mol*s)","*|/",2),
        n = 0.57,
        alpha = 0,
        E0 = (2.76,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (2200,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH2O + O --> HCO + OH C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 416 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O Atom Reactions.

Verified by Karma James

pg.449-450: Discussion on evaluated data

O+CH2O --> OH+HCO: "The preferred values are based on the low temperature data which are

all in good agreement, and on the higher temperature value of Bowman."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 229,
    label = "CO_pri;CH2_triplet",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.02e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
Rate constant is an upper limit. CH2O + CH2 --> HCO + CH3

C.D.W divided original rate expression by 2 (from A= 6.03E+09), to get rate expression per H atom.

pg 1106, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 26,12.

Verified by Karma James

pg. 1267: Discussion on evaluated data

Recommended data based on triplet methylene's general lack of reactivity in H-atom abstractions

NOTE: Rate coefficient is an upper limit
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 230,
    label = "CO_pri;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.89e-08,"cm^3/(mol*s)","*|/",1.58),
        n = 6.1,
        alpha = 0,
        E0 = (1.97,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Frank, P.; Hayman, G,; Just, T.; Kerr, J.A.; Murrells, T.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.

CH2O + CH3 --> HCO + CH4 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 862 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 1. Bimolecular reactions - CH3 Radical Reactions.

Verified by Karma James

pg.989-990: Discussion on evaluated data

CH3+HCHO --> CH4+HCO: The recommended value is a "best fit to the data of Choudhury et al.,

the reworked data from Anastasi, together with those at lower temperatures from
Refs. 4, 5, and 7."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    label = "CO_pri;C_rad/H2/Cs",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2750,"cm^3/(mol*s)","*|/",5),
        n = 2.81,
        alpha = 0,
        E0 = (5.86,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + C2H5 --> HCO + C2H6 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1096, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,12.

Verified by Karma James

pg. 1178: Discussion on evaluated data

Recommended data is the rate of CH2O+CH3-->HCO+CH4.

Authors note that rate coefficients for alkyl radicals w/aldehydic H-atoms are
similar (as noted by Kerr, J.A. and Trotman-Dickenson, A.F.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    label = "CO_pri;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.4e+10,"cm^3/(mol*s)","*|/",2.5),
        n = 0,
        alpha = 0,
        E0 = (6.96,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH2O + iso-C3H7 --> HCO + C3H8 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,12.

Verified by Karma James

pg. 936: Discussion on evaluated data

Entry 42,12: No data available at the time.  The author recommends a rate coefficient

expression that is twice that of the rxn i-C3H7+(CH3)2CHCHO, taken from a study
by Kerr, J.A. and Trotman-Dickenson, A.F. (1959).  The author states that a correction
was made to the 1959 report, taking the recommended rate of i-C3H7 recombination
(reported by Tsang) into consideration.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    label = "CO_pri;C_rad/Cs3",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.63e+09,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (3.56,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
CH2O + tert-C4H9 --> HCO + iso-C4H10 C.D.W divided original rate expression by 2 (from A= 3.25E+09), to get rate expression per H atom.

pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 44,12.

Verified by Karma James

pg.35: Discussion on evaluated data

Entry 44,12: No data available at the time.  The author recommends 2x the rate coefficient

of the rxn tC4H9+tC4H9-CHO=iC4H10+tC4H9-CO (2 vs. 1 aldehydic H-atoms); this value
was reported by Birrell and Trotman-Dickenson.  The author also notes that he has
taken into account tC4H9 combination (perhaps meaning he used a geometric mean rule
to derive the final form of the expression?)
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    label = "CO_pri;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2710,"cm^3/(mol*s)","*|/",5),
        n = 2.81,
        alpha = 0,
        E0 = (5.86,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + C2H3 --> HCO + C2H4 C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,12.

Verified by Karma James

pg. 1197: Discussion on evaluated data

Recommended data is the rate of CH2O+CH3-->HCO+CH4.

Authors note that rate coefficients for alkyl radicals w/aldehydic H-atoms are
similar (as noted by Kerr, J.A. and Trotman-Dickenson, A.F.
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    label = "CO_pri;CO_rad/NonDe",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.05e+10,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (12.92,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + CH3CO --> HCO + CH3CHO C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,12.

Verified by Karma James

pg. 1231: Discussion on evaluated data

Recommended data based on "analogous systems"

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 236,
    label = "CO_pri;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.72e+09,"cm^3/(mol*s)","*|/",5),
        n = 1.18,
        alpha = 0,
        E0 = (-0.45,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (3000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH2O + OH --> HCO + H2O C.D.W divided original rate expression by 2 (from A= 3.43E+09), to get rate expression per H atom.

pg 419 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - OH Radical Reactions.

Verified by Karma James

pg.575-576: Discussion on evaluated data

OH+CH2O --> H2O+HCO: The recommended rate coefficient is the value reported by Tsang

and Hampson.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 237,
    label = "CO_pri;O_rad/NonDeC",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.1e+10,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (2.98,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
CH2O + CH3O --> HCO + CH3OH C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 1104, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,12.

Verified by Karma James

pg. 1245: Discussion on evaluated data

Recommended data based on review by Gray, based on experiments performed by Hoare and Wellington.

Authors note that experimental conditions were such that rxn of interest was
in competition with the disproportionation of two CH3O radicals (CH3O+CH3O-->CH3OH+CH2O)
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 238,
    label = "CO_pri;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (20600,"cm^3/(mol*s)"),
        n = 2.5,
        alpha = 0,
        E0 = (10.21,"kcal/mol"),
        Tmin = (641,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Eiteneer et al. [133] literature review.""",
    longDesc = 
u"""
[133] Eiteneer, B.; Yu, C.-L.; Goldenberg, M.; Frenklach, M. J. Phys. Chem. A. 1998, 102, 5196.
CH2O + HO2 --> HCO + H2O2 C.D.W divided original rate expression by 2 (from A= 4.11E+04), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 239,
    label = "CO/H/NonDe;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+13,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (39.15,"kcal/mol"),
        Tmin = (600,"K"),
        Tmax = (1100,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + O2 --> CH3CO + HO2

pg 417 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - O2 Reactions.

Verified by Karma James

pg.485: Discussion on evaluated data

O2+CH3CHO --> HO2+CH3CO: "For this evaluation we prefer the approach of Walker and

the recommended value is based on the best current deltaH298 value (=163.8 kJ/mol
using deltaHf(CH3CO)=11.0 kJ/mol and deltaHf(HO2)=14.6 kJ/mol) and A=5.0x10^-11
cm3/molecule/s."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 240,
    label = "CO/H/NonDe;O_atom_triplet",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (5e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (1.79,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + O --> CH3CO + OH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 241,
    label = "CO/H/NonDe;H_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (4e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        alpha = 0,
        E0 = (4.21,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + H --> CH3CO + H2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    label = "CO/H/NonDe;C_methyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.99e-06,"cm^3/(mol*s)","*|/",2),
        n = 5.64,
        alpha = 0,
        E0 = (2.46,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1250,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + CH3 --> CH3CO + CH4

pg 423 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - CH3 Radical Reactions.

Verified by Karma James

pg.671: Discussion on evaluated data

CH3+CH3CHO --> CH4+CH3CO: "There are no direct studies of the kinetics of this reaction

and all of the k values are relative to methyl recombination ... The preferred values
are based on a line constructed through the mean of the low temperature data and the
data of Liu and Laidler and Colket et al."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    label = "CO/H/NonDe;C_rad/H2/Cd",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.8e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.21,"kcal/mol"),
        Tmin = (790,"K"),
        Tmax = (810,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Loser et al. [135] bond strength-bond length method.""",
    longDesc = 
u"""
[135] Loser, U.; Scherzer, K.; Weber, K. Z. Phys. Chem. (Leipzig) 1989, 270, 237.
CH3CHO + CH2CH=CH2 --> CH3CO + CH3CH=CH2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    label = "CO/H/NonDe;Cd_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.13e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.68,"kcal/mol"),
        Tmin = (480,"K"),
        Tmax = (520,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Scherzer et al. [136] bond energy-bond order method.""",
    longDesc = 
u"""
[136] Scherzer, K.; Loser, U.; Stiller, W. Z. Phys. Chem. 1987, 27, 300.
CH3CHO + C2H3 --> CH3CO + C2H4
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    label = "CO/H/NonDe;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2e+06,"cm^3/(mol*s)"),
        n = 1.8,
        alpha = 0,
        E0 = (-1.3,"kcal/mol"),
        Tmin = (295,"K"),
        Tmax = (600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Taylor et al. [127] Transition state theory.""",
    longDesc = 
u"""
[127] Taylor, P.H.; Rahman, M.S.; Arif, M.; Dellinger, B.; Marshall, P. Sypm. Int. Combust. Proc. 1996, 26, 497.
CH3CHO + OH --> CH3CO + H2O Pressure 0.13-0.97 atm. Rate constant is high pressure limit.

pg 501, Table 1, k2 = 2.00x10^6 T^1.8 exp(1300/RT)

Previous modified Arrhenius parameters had E=1.3 kcal/mol; it should be E=-1.3 kcal/mol

Certified by MRH on 6Aug2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    label = "CO/H/NonDe;O_pri_rad",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)","*|/",2.51),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3CHO + OH --> CH3CO + H2O
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    label = "CO/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     O 0 {1,D}
3  *2 H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.01e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (11.92,"kcal/mol"),
        Tmin = (900,"K"),
        Tmax = (1200,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

CH3CHO + HO2 --> CH3CO + H2O2

pg 421 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - HO2 Radical Reactions.

Verified by Karma James

pg.614-615: Discussion on evaluated data

HO2+CH3CHO --> CH3CO+H2O2: "The preferred expression is based on a value of 1.7x10^-14

cm3/molecule/s at 1050K from a study performed by Colket et al. and an assumed A
factor of 5.0x10^-12 cm3/molecule/s."
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    label = "O_pri;O2b",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.325e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (74.12,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Mayer et al. [137] Bond energy-bond order.""",
    longDesc = 
u"""
[137] Mayer, S.W.; Schieler, L. J. Phys. Chem. 1968, 72, 2628.
http://dx.doi.org/10.1021/j100853a066

H2O + O2 --> OH + HO2. 
C.D.W divided original rate expression by 2, to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 249,
    label = "O_pri;O_atom_triplet",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (2.63e+09,"cm^3/(mol*s)"),
        n = 1.2,
        alpha = 0,
        E0 = (17.83,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Karach et al. [138] Transition state theory.""",
    longDesc = 
u"""
[138] Karach, S.P.; Oscherov, V.I. J. Phys. Chem. 1999, 110, 11918.
H2O + O --> OH + OH. C.D.W divided original rate expression by 2 (from A= 2.95E+39), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 250,
    label = "O_pri;O_atom_triplet",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (74000,"cm^3/(mol*s)"),
        n = 2.6,
        alpha = 0,
        E0 = (15.18,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Harding et al. [139] Transition state theory.""",
    longDesc = 
u"""
[139] Harding, L.B.; Wagner, A.F. Symp. Int. Combust. proc. 1989, 22, 983.
H2O + O --> OH + OH. C.D.W divided original rate expression by 2 (from A= 1.48E+05), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 251,
    label = "O_pri;H_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.26e+08,"cm^3/(mol*s)","*|/",1.6),
        n = 1.6,
        alpha = 0,
        E0 = (19.32,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; 
Troe, J.; Walker, R.W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.

H2O + H --> OH + H2. C.D.W divided original rate expression by 2, to get rate expression per H atom.

pg 418 Evaluated Kinetic Data for Combustion Modelling, Table 1. Bimolecular reactions - H Atom Reactions.

NOTE: E0 Rference = 18.4, E0 RMG database = 19.32

Verified by Karma James

pg.504: Discussion on evaluated data

H+H2O --> OH+H2: "The recommended rate coefficient is based on the spare high temperature

measurements and rate data of the reverse rxn combined with the equilibrium constant."
MRH agrees with Karma.  However, the discrepancy is small and NIST's online database Webbook

has an E = 19.32 kcal/mol.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 252,
    label = "O_pri;C_methyl",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.2,"cm^3/(mol*s)"),
        n = 3.31,
        alpha = 0,
        E0 = (12.56,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Ma et al. [140] Transition state theory.""",
    longDesc = 
u"""
[140] Ma, S.; Liu, R.; Sci. China Ser. S: 1996, 39, 37.
H2O + CH3 --> OH + CH4. C.D.W divided original rate expression by 2 (from A= 6.39), to get rate expression per H atom.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 253,
    label = "O_pri;C_methyl",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (242,"cm^3/(mol*s)","*|/",1.6),
        n = 2.9,
        alpha = 0,
        E0 = (14.86,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + CH3 --> OH + CH4. C.D.W divided original rate expression by 2 (from A= 4.83E+02), to get rate expression per H atom.

pg 1095, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 16,9.

Verified by Karma James

pg. 1163: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 254,
    label = "O_pri;C_rad/H2/Cs",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.7e+06,"cm^3/(mol*s)","*|/",2),
        n = 1.44,
        alpha = 0,
        E0 = (20.27,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + C2H5 --> OH + C2H6. C.D.W divided original rate expression by 2 (from A= 3.39E+06), to get rate expression per H atom.

pg 1096, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,9.

Verified by Karma James

pg. 1177: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 255,
    label = "O_pri;Cd_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (242,"cm^3/(mol*s)","*|/",5),
        n = 2.9,
        alpha = 0,
        E0 = (14.86,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + C2H3 --> OH + C2H4. C.D.W divided original rate expression by 2 (from A= 4.83E+02), to get rate expression per H atom.

pg 1098, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,9.

Verified by Karma James

pg. 1196: Discussion on evaluated data

Recommended data based on expression for CH3+H2O=CH4+OH

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 256,
    label = "O_pri;CO_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.18e+08,"cm^3/(mol*s)","*|/",5),
        n = 1.35,
        alpha = 0,
        E0 = (26.03,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087.
H2O + HCO --> OH + CH2O. C.D.W divided original rate expression by 2 (from A= 2.35E+08), to get rate expression per H atom.

pg 1094, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 15,9.

Verified by Karma James

pg. 1150: Discussion on evaluated data

Recommended data based on reverse rate and equilibrium constant

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 257,
    label = "O_pri;O_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.417e-07,"cm^3/(mol*s)"),
        n = 5.48,
        alpha = 0,
        E0 = (0.274,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (700,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Masgrau et al. [141] Transition state theory.""",
    longDesc = 
u"""
[141] Masgrau, L.; Gonzalez-Lafont, A.; Lluch, J.M. J. Phys. Chem. A. 1999, 103, 1044.
H2O + OH --> OH + H2O . C.D.W refitted their k(T) to get A, n, and Ea, and divided original rate expression by 2, to get rate expression per H atom.

pg 1050, Table 4, Section: HO + HOH = HOH + OH(1), Column k_ab_CVT/SCT

MRH computed modified Arrhenius parameters using least-squares regression: ln(k) = ln(A) + n*ln(T) - (E/R)*(1/T)

E: Multiplied (E/R) expression by 1.987e-3

A: exp(ln(A)), multiplied by 6.02e23 (to convert /molecule to /mol) and divided by 2 (to get rate per H atom)

Certified by MRH on 7Aug2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 258,
    label = "O_pri;O_rad/NonDeC",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.174,"cm^3/(mol*s)"),
        n = 3.8,
        alpha = 0,
        E0 = (11.49,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
H2O + CH3O --> OH + CH3OH C.D.W divided original rate expression by 2 (from A= 9.03E+08), to get rate expression per H atom.; This is Rxn. -R5 from mpaper

Verified by Greg Magoon: note that this reaction is endothermic; the reverse (R5), appears as #267, below
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 259,
    label = "O/H/NonDeC;O_atom_triplet",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)","*|/",2.51),
        n = 0,
        alpha = 0,
        E0 = (4.69,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3OH + O --> CH3O + OH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 260,
    label = "O/H/NonDeC;CH2_triplet",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.4,"cm^3/(mol*s)","*|/",3),
        n = 3.1,
        alpha = 0,
        E0 = (6.94,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + CH2 --> CH3O + CH3

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

//Index of Reactions and Summary of Recommended Rate Expressions. No. 38,25.

Verified by Karma James

Data for Rate Expression 38,26 (pg. 493)

Stated uncertainty factor is 3

Verified by MRH on 11Aug2009

Entry 38,26 (b): No data available at the time.  Author suggests the rate coefficient

expression for CH3+CH3OH=CH4+CH3O
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 261,
    label = "O/H/NonDeC;C_methyl",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00037,"cm^3/(mol*s)"),
        n = 4.7,
        alpha = 0,
        E0 = (5.78,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
The calculated rate constants are in good agreement with experiment. CH3OH + CH3 --> CH3O + CH4 (Rxn. R3 from paper)

Verified by Greg Magoon: I changed upper temperature to 2000 K (was 2500) in line with other reactions from same paper; note that according to the paper, this reaction is very slightly endothermic; the exothermic reverse (-R3) is included above as #177
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 262,
    label = "O/H/NonDeC;C_rad/H2/Cs",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.4,"cm^3/(mol*s)","*|/",3),
        n = 3.1,
        alpha = 0,
        E0 = (8.94,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H5 --> CH3O + C2H6

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,17.

Verified by Karma James

pg. 489: Discussion on evaluated data

Entry 38,17 (b): No data available at the time.  Author notes ethyl radicals are known

to be considerably less reactive than methyl.  Author recommends the rate coefficient
expression of CH3+CH3OH=CH4+CH3O, with a slight adjustment (based on the observed
trends in methyl vs. ethyl radical reactivity with hydrocarbons).
MRH 30-Aug-2009

//263: [90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    label = "O/H/NonDeC;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.5,"cm^3/(mol*s)","*|/",5),
        n = 3.1,
        alpha = 0,
        E0 = (10.33,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [91] literature review.""",
    longDesc = 
u"""
[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.
CH3OH + iso-C3H7 --> CH3O + C3H8

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

Ref[90] was incorrect; rate matches that reported in Ref[91].

pg. 944: Discussion on evaluated data

Entry 42,38 (b)

No experimental data, at the time

Recommended rate is based on C2H5+CH3OH=C2H6+CH3O

Verified by MRH on 10Aug2009

MRH 30-Aug-2009

//264: [90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 264,
    label = "O/H/NonDeC;C_rad/Cs3",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1510,"cm^3/(mol*s)","*|/",10),
        n = 1.8,
        alpha = 0,
        E0 = (9.36,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [92] literature review.""",
    longDesc = 
u"""
[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.
CH3OH + tert-C4H9 --> CH3O + iso-C4H10

//WAS UNABLE TO VERIFY DATA!!! DATA NOT FOUND IN REFERENCE.

Ref[90] was incorrect; rate matches that reported in Ref[92].

pg.44: Discussion on evaluated data

Entry 44,38(b)

Reference reports reaction as: t-C4H9+CH3OH=t-C4H10+CH3O

This is a typo: no t-C4H10 molecule exists (should be i-C4H10)
No experimental data, at the time

Recommended rate is based on reverse rxn and equilibrium constant

Verified by MRH on 10Aug2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 265,
    label = "O/H/NonDeC;Cd_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14.4,"cm^3/(mol*s)","*|/",10),
        n = 3.1,
        alpha = 0,
        E0 = (6.94,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H3 --> CH3O + C2H4

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,19.

Verified by Karma James

pg. 489: Discussion on evaluated data

Entry 38,19 (b): No data available at the time.  Author recommends the rate coefficient

expression for CH3+CH3OH=CH4+CH3O.
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    label = "O/H/NonDeC;Ct_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+12,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [90] literature review.""",
    longDesc = 
u"""
[90] Tsang, W. J. Phys. Chem. Ref. Data 1987, 16, 471.
CH3OH + C2H --> CH3O + C2H2

pg 475, Chemical Kinetic Database For Combustion Chemistry, Part 2 - Methanol. 

Index of Reactions and Summary of Recommended Rate Expressions. No. 38,21.

Verified by Karma James

pg. 490: Discussion on evaluated data

Entry 38,21 (b): No data available at the time.  Author recommends a rate coefficient

expression based on measurements of C2H+CH4 and C2H+C2H6 rxns
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 267,
    label = "O/H/NonDeC;O_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17.3,"cm^3/(mol*s)"),
        n = 3.4,
        alpha = 0,
        E0 = (-1.14,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations.""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.
The calculated rate constants are in good agreement with experiment. CH3OH + OH --> CH3O + H2O (Rxn. R5 from paper)

Verified by Greg Magoon (cf. reverse, #258, above)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 268,
    label = "O/H/NonDeC;O_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)","*|/",3.16),
        n = 0,
        alpha = 0,
        E0 = (1.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review""",
    longDesc = 
u"""
[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.
CH3OH + OH --> CH3O + H2O
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    label = "Cd_pri;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (60.36,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Increased rate 154 Ea by 9.6 kcal/mol (vinyl versus methyl)""",
    longDesc = 
u"""
JDM increased the activation energy for the abstraction of a vinyl-H hydrogen by O2.  August 2010.
Using the Evans-Polanyi principle with alpha = 1, the activation energy was increased by delta(vinyl radical - alkyl radical) = 9.6 kcal/mol.
Reaction rate 154 was the basis for this.

Previously, rates had been calculated by an averaging-of-averages technique, which resulted in the abstraction of vinyl-H's being orders of magnitude faster than the abstraction of alkyl-H's.

These rates have been calculated based on rates of primary- and secondary-alkyl H-abstractions by O2. 
The A-factors have remained the same.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    label = "Cd_pri;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.005e+13,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (61.47,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Increased rate 179 Ea by 9.6 kcal/mol (vinyl versus methyl)""",
    longDesc = 
u"""
JDM increased the activation energy for the abstraction of a vinyl-H hydrogen by O2.  August 2010.
Using the Evans-Polanyi principle with alpha = 1, the activation energy was increased by delta(vinyl radical - alkyl radical) = 9.6 kcal/mol.
Reaction rate 179 was the basis for this.

Previously, rates had been calculated by an averaging-of-averages technique, which resulted in the abstraction of vinyl-H's being orders of magnitude faster than the abstraction of alkyl-H's.

These rates have been calculated based on rates of primary- and secondary-alkyl H-abstractions by O2. 
The A-factors have remained the same.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    label = "Cd/H/NonDeC;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (57.81,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Increased rate 155 Ea by 9.6 kcal/mol (vinyl versus methyl)""",
    longDesc = 
u"""
JDM increased the activation energy for the abstraction of a vinyl-H hydrogen by O2.  August 2010.
Using the Evans-Polanyi principle with alpha = 1, the activation energy was increased by delta(vinyl radical - alkyl radical) = 9.6 kcal/mol.
Reaction rate 155 was the basis for this.

Previously, rates had been calculated by an averaging-of-averages technique, which resulted in the abstraction of vinyl-H's being orders of magnitude faster than the abstraction of alkyl-H's.

These rates have been calculated based on rates of primary- and secondary-alkyl H-abstractions by O2. 
The A-factors have remained the same.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    label = "Cd/H/NonDeC;O2b",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3  *2 H 0 {1,S}
4     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.985e+13,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (57.29,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Increased rate 188 Ea by 9.6 kcal/mol (vinyl versus methyl)""",
    longDesc = 
u"""
JDM increased the activation energy for the abstraction of a vinyl-H hydrogen by O2.  August 2010.
Using the Evans-Polanyi principle with alpha = 1, the activation energy was increased by delta(vinyl radical - alkyl radical) = 9.6 kcal/mol.
Reaction rate 188 was the basis for this.

Previously, rates had been calculated by an averaging-of-averages technique, which resulted in the abstraction of vinyl-H's being orders of magnitude faster than the abstraction of alkyl-H's.

These rates have been calculated based on rates of primary- and secondary-alkyl H-abstractions by O2. 
The A-factors have remained the same.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    label = "Orad_O_H;O_rad/NonDeO",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     O 1 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.75e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (-3.275,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""[8] Curran's estimation in reaction type 13, RO2 + HO2 --> RO2H + O2""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    label = "O/H/NonDeC;O2b",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2  *2 H 0 {1,S}
3     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 1,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Estimate [W.H. Green]""",
    longDesc = 
u"""
ROH + .OO. --> HOO. + RO.

This rate coefficient is an estimate from W.H. Green (personal communication).  The pre-exponential factor has been
 divided by 2 (from 1e11 to 5e10), to account for the symmetry of .OO.  The temperature range is estimated as 300-2000 K
 and the rank is assigned 1, so that this rate coefficient estimate will be used in all instances.
This is simply an estimate; JDM and/or MRH will refine this value in the near future.
See also rate 532 for X_H + .OO. --> HOO. + X.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    label = "C/H3/Cd;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cd 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.00057833,"cm^3/(mol*s)"),
        n = 4.65,
        alpha = 0,
        E0 = (9.78,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 525""",
    longDesc = 
u"""
This rate rules matches C=C-CH3 + HO-O* <=> C=C-CH2* + H2O2

Due to lack of better estimate SSM has given this node the value obtained from 2-Butene + HO2 calculations (Rate rule 525)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    label = "H2O2;Cd_rad/NonDeC",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.4375,"cm^3/(mol*s)"),
        n = 3.59,
        alpha = 0,
        E0 = (-4.03,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 527""",
    longDesc = 
u"""
This rate rules matches C=C*-C + H2O2 <=> C=C-C + HO-O*

Due to lack of better estimate SSM has given this node the value obtained from 2-Butene + HO2 calculations (Rate rule 527)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 528,
    label = "C/H2/OneDeC;O_rad/NonDeO",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     {Cd,Ct,CO,Cb} 0 {1,S}
5     Cs 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.000254,"cm^3/(mol*s)"),
        n = 4.59,
        alpha = 0,
        E0 = (7.16,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 529""",
    longDesc = 
u"""
This rate rules matches Cs-CH2-C=C + HO-O* <=> Cs-CH*-C=C + H2O2

Due to lack of better estimate SSM has given this node the value obtained from 1-Butene + HO2 calculations (Rate rule 529)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 530,
    label = "H2O2;Cd_pri_rad",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1,"cm^3/(mol*s)"),
        n = 3.52,
        alpha = 0,
        E0 = (-7.48,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""SSM due to lack of better value ref rate rule 531""",
    longDesc = 
u"""
This rate rules matches C-HC=CH* + H2O2 <=> C-HC=CH2 + HO=O*

Due to lack of better estimate SSM has given this node the value obtained from 1-Butene + HO2 calculations (Rate rule 531)
The rate was calculated using CBS-QB3 w/o hindered rotors and is valid in a range of temperature from 300 -2000 K.
The Wigner tunneling currection that was used to account for tunneling.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 532,
    label = "X_H;O2b",
    group1 = 
"""
1  *1 R 0 {2,S}
2  *2 H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 1,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Estimate [W.H. Green]""",
    longDesc = 
u"""
X_H + .OO. --> HOO. + X.

I have taken the estimated rate from 523, which assumes A=1e11 with Ea=enthothermicity,
and assigned it to the top level X_H node so that whenever .OO. is abstracting from 
something without a proper rate, this value is used instead of the lengthy average.
See notes to 523 for further details.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 533,
    label = "C_methane;C2b",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,T}
2     C 1 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (7.5e+12,"cm^3/(mol*s)","+|-",1.6e+12),
        n = 0,
        alpha = 0,
        E0 = (1.05,"kcal/mol","+|-",0.12),
        Tmin = (294,"K"),
        Tmax = (376,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Matsugi et al 10.1021/jp1012494""",
    longDesc = 
u"""
For CH4 + C2 = CH3 + C2H

J. Phys. Chem. A 2010, 114, 4580-4585
http://dx.doi.org/10.1021/jp1012494

Rate Constants and Kinetic Isotope Effects on the Reaction of C2($X^1\Sigma_g^+$) with CH4 and CD4.
Akira Matsugi, Kohsuke Suma, and Akira Miyoshi

It was measured at pretty low temperatures (294-376), but also calculated ab initio. The calculated
rates are plotted but the expression is not reported.

    k = (10.0 +- 2.1)E-11 exp[-(4.4+-0.5 kJ mol)/RT] cm3 molecule-1 s-1
which gives 
    A = 6e13+-1.3e13 cm3/mole/s
    n = 0
    Ea = 1.05+-0.12  kcal/mol
The degeneracy of this reaction is 8 though, so per-site A is:
    A = 7.5e12+-1.6e12
    
(See also  doi:10.1063/1.3480395  for reactions of C2, but that may be the wrong electronic state.)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 535,
    label = "H2O2;O_rad/OneDe",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.03495,"cm^3/(mol*s)","*|/",3),
        n = 3.75,
        alpha = 0,
        E0 = (10.89,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations, see node 534.""",
    longDesc = 
u"""
Rxn family nodes: H2O2 + O_rad/OneDe

The rate coefficient for this node was taken from node 534 (H2O2 + InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3)
by analogy: HOOH + *O-C=R.  Discussed with MRH.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 537,
    label = "H2O2;O_rad/NonDeO",
    group1 = 
"""
1  *1 O 0 {2,S} {3,S}
2     O 0 {1,S} {4,S}
3  *2 H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.092,"cm^3/(mol*s)","*|/",3),
        n = 3.96,
        alpha = 0,
        E0 = (6.63,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations, see node 536.""",
    longDesc = 
u"""
Rxn family nodes: H2O2 + O_rad/NonDeO

The rate coefficient for this node was taken from node 536 (H2O2 + OOCH3)
by analogy: HOOH + *O-O-R.  Discussed with MRH.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1001,
    label = "C/H3/O;H_rad",
    group1 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2  *2 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (451,"cm^3/(mol*s)"),
        n = 3.2,
        alpha = 0,
        E0 = (3.49,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Jodkowski et al. [100] ab initio calculations. added by Greg Magoon 08/25/09""",
    longDesc = 
u"""
[100] Jodkowski, J.T.; Rauez, M.-T.; Rayez, J.-C. J. Phys. Chem. A. 1999, 103, 3750.

CH3OH + H --> CH2OH + H2 (Rxn. R2 in paper)

divided original rate expression by 3 to get rate expression per H atom.

Created by Greg Magoon; maximum error of fitted expression from tabular data for kr2 is 20% (cf. p. 3758); rank of 2 assigned based on rank for other values reported in the paper in the rateLibrary (also 2)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

