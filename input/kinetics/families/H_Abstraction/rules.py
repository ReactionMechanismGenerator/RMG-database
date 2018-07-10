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
entry(
    index = 0,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
If a biradical CH2JJ can abstract from RCH4 to make RCH3J and CH3J 
then a Y_rad CH3J should be able to abstract from RCH3J which means X_H needs 
to include Xrad_H. I.e. you can abstract from a radical. To make this possible
a head node has been created X_H_or_Xrad_H which is a union of X_H and Xrad_H.
The kinetics for it have just been copied from X_H and are only defined for 
abstraction by Y_rad_birad. I.e. the top level very approximate guess.

Do better kinetics for this exist? Do we in fact use the reverse kinetics anyway?
""",
)

entry(
    index = 1,
    label = "X_H;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 2,
    label = "X_H;H_rad",
    kinetics = ArrheniusEP(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0.65,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Dean, A. M. [118]""",
    longDesc = 
u"""
[118] Dean, A.M. Development and application of Detailed Kinetic Mechanisms for Free Radical Systems.
""",
)

entry(
    index = 257,
    label = "O_pri;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (2.417e-07, 'cm^3/(mol*s)'),
        n = 5.48,
        alpha = 0,
        E0 = (0.274, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (700, 'K'),
    ),
    rank = 5,
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
)

entry(
    index = 537,
    label = "H2O2;O_rad/NonDeO",
    kinetics = ArrheniusEP(
        A = (0.092, 'cm^3/(mol*s)', '*|/', 3),
        n = 3.96,
        alpha = 0,
        E0 = (6.63, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""MHS CBS-QB3 w/1dHR calculations, see node 536.""",
    longDesc = 
u"""
Rxn family nodes: H2O2 + O_rad/NonDeO

The rate coefficient for this node was taken from node 536 (H2O2 + OOCH3)
by analogy: HOOH + *O-O-R.  Discussed with MRH.
""",
)

entry(
    index = 2008,
    label = "C/H3/Ct;InChI=1S/NO3/c2-1(3)4",
    kinetics = ArrheniusEP(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0.15,
        E0 = (9.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser from 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli""",
)

entry(
    index = 3000,
    label = "N5dc/H/NonDeOO;H_rad",
    kinetics = ArrheniusEP(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0,
        E0 = (4.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HNO2 + H = H2 + NO2 (B&D #41a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3000,
    label = "N5dc/H/NonDeOO;O_atom_triplet",
    kinetics = ArrheniusEP(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0,
        E0 = (2.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HNO2 + O = OH + NO2 (B&D #41b) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3000,
    label = "N5dc/H/NonDeOO;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (-0.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HNO2 + OH = H2O + NO2 (B&D #41c) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3000,
    label = "N5dc/H/NonDeOO;C_methyl",
    kinetics = ArrheniusEP(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        alpha = 0,
        E0 = (4.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HNO2 + CH3 = NO2 + CH4 (B&D #41d) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3000,
    label = "N5dc/H/NonDeOO;NH2_rad",
    kinetics = ArrheniusEP(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        alpha = 0,
        E0 = (0.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HNO2 + NH2 = NH3 + NO2 (B&D #41e) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 4000,
    label = "H2;H_rad",
    kinetics = ArrheniusEP(
        A = (0.472, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (5.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4045,
    label = "C_methane;C_methyl",
    kinetics = ArrheniusEP(
        A = (0.00518, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4090,
    label = "C/H3/Cs;C_rad/H2/Cs",
    kinetics = ArrheniusEP(
        A = (0.00092, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4135,
    label = "C/H2/NonDeC;C_rad/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (0.000865, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4180,
    label = "C/H/Cs3;C_rad/Cs3",
    kinetics = ArrheniusEP(
        A = (0.000542, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4225,
    label = "C/H3/Cd;C_rad/H2/Cd",
    kinetics = ArrheniusEP(
        A = (0.00145, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (13.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4270,
    label = "C/H2/CdCs;C_rad/H/CdCs",
    kinetics = ArrheniusEP(
        A = (0.00229, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (11.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4315,
    label = "C/H/Cs2Cd;C_rad/CdCs2",
    kinetics = ArrheniusEP(
        A = (0.000119, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (8.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4360,
    label = "C/H2/CdCd;C_rad/H/CdCd",
    kinetics = ArrheniusEP(
        A = (0.000391, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4405,
    label = "C/H/CdCd;C_rad/CdCdCs",
    kinetics = ArrheniusEP(
        A = (3.92e-06, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4450,
    label = "C/H3/Ct;C_rad/H2/Ct",
    kinetics = ArrheniusEP(
        A = (0.00571, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (11.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4495,
    label = "C/H2/CtCs;C_rad/H/CtCs",
    kinetics = ArrheniusEP(
        A = (0.00166, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4540,
    label = "C/H/Cs2Ct;C_rad/CtCs2",
    kinetics = ArrheniusEP(
        A = (0.000324, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4585,
    label = "C/H2/CtCt;C_rad/H/CtCt",
    kinetics = ArrheniusEP(
        A = (0.00403, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4630,
    label = "C/H/CtCt;C_rad/CtCtCs",
    kinetics = ArrheniusEP(
        A = (8.1e-05, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4675,
    label = "C/H3/Cb;C_rad/H2/Cb",
    kinetics = ArrheniusEP(
        A = (0.00114, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (13.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4720,
    label = "C/H2/CbCs;C_rad/H/CbCs",
    kinetics = ArrheniusEP(
        A = (0.000475, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4765,
    label = "C/H/Cs2Cb;C_rad/CbCs2",
    kinetics = ArrheniusEP(
        A = (9.08e-06, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4810,
    label = "Cd_pri;Cd_pri_rad",
    kinetics = ArrheniusEP(
        A = (0.00925, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4855,
    label = "Cd/H/NonDeC;Cd_rad/NonDeC",
    kinetics = ArrheniusEP(
        A = (0.00556, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4900,
    label = "Cd/H/Cd;Cd_rad/Cd",
    kinetics = ArrheniusEP(
        A = (0.0043, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 4945,
    label = "Cb_H;Cb_rad",
    kinetics = ArrheniusEP(
        A = (0.0144, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5012,
    label = "Cd_Cdd/H2;Cd_Cdd_rad/H",
    kinetics = ArrheniusEP(
        A = (0.0308, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5035,
    label = "C/H3/S;C_rad/H2/S",
    kinetics = ArrheniusEP(
        A = (0.000139, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5058,
    label = "Cd/H/Ct;Cd_rad/Ct",
    kinetics = ArrheniusEP(
        A = (0.000816, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (6.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5080,
    label = "C/H2/CsS;C_rad/H/CsS",
    kinetics = ArrheniusEP(
        A = (0.000844, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5125,
    label = "C/H/Cs2S;C_rad/Cs2S",
    kinetics = ArrheniusEP(
        A = (0.000162, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5170,
    label = "C/H3/CS;C_rad/H2/CS",
    kinetics = ArrheniusEP(
        A = (0.00281, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (19.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5215,
    label = "C/H2/CSCs;C_rad/H/CSCs",
    kinetics = ArrheniusEP(
        A = (0.00289, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5260,
    label = "C/H/Cs2CS;C_rad/CSCs2",
    kinetics = ArrheniusEP(
        A = (0.000273, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5305,
    label = "Cd/H/NonDeS;Cd_rad/NonDeS",
    kinetics = ArrheniusEP(
        A = (0.00297, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (-3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5350,
    label = "Cd/H/CS;Cd_rad/CS",
    kinetics = ArrheniusEP(
        A = (0.051, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (20.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5395,
    label = "C/H2/CdS;C_rad/H/CdS",
    kinetics = ArrheniusEP(
        A = (0.00134, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5442,
    label = "C/H/CSCsS;C_rad/CSCsS",
    kinetics = ArrheniusEP(
        A = (0.000174, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5485,
    label = "C/H2/CSS;C_rad/H/CSS",
    kinetics = ArrheniusEP(
        A = (0.00145, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5530,
    label = "C/H/CSCsS;C_rad/CSCsS",
    kinetics = ArrheniusEP(
        A = (0.000143, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5575,
    label = "C/H2/CtS;C_rad/H/CtS",
    kinetics = ArrheniusEP(
        A = (0.00118, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5620,
    label = "C/H/CtCsS;C_rad/CtCsS",
    kinetics = ArrheniusEP(
        A = (0.000354, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5665,
    label = "C/H2/CbS;C_rad/H/CbS",
    kinetics = ArrheniusEP(
        A = (0.000212, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (6.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5710,
    label = "C/H/CbCsS;C_rad/CbCsS",
    kinetics = ArrheniusEP(
        A = (2.7e-05, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5755,
    label = "CS_pri;CS_pri_rad",
    kinetics = ArrheniusEP(
        A = (0.0548, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5800,
    label = "CS/H/NonDeC;CS_rad/Cs",
    kinetics = ArrheniusEP(
        A = (0.0141, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5845,
    label = "CS/H/NonDeS;CS_rad/S",
    kinetics = ArrheniusEP(
        A = (0.00677, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (9.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5890,
    label = "CS/H/Cd;CS_rad/Cd",
    kinetics = ArrheniusEP(
        A = (0.00797, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (12.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 5935,
    label = "CS/H/Ct;CS_rad/Ct",
    kinetics = ArrheniusEP(
        A = (0.0268, 'cm^3/(mol*s)'),
        n = 4.34,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for C--H--C abstractions, Aaron Vandeputte""",
)

entry(
    index = 7000,
    label = "S_pri;S_pri_rad",
    kinetics = ArrheniusEP(
        A = (301, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for S--H--S abstractions, Aaron Vandeputte""",
)

entry(
    index = 7007,
    label = "S/H/NonDeC;S_rad/NonDeC",
    kinetics = ArrheniusEP(
        A = (668, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for S--H--S abstractions, Aaron Vandeputte""",
)

entry(
    index = 7014,
    label = "S/H/Cd;S_rad/Cd",
    kinetics = ArrheniusEP(
        A = (789, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for S--H--S abstractions, Aaron Vandeputte""",
)

entry(
    index = 7021,
    label = "S/H/Ct;S_rad/Ct",
    kinetics = ArrheniusEP(
        A = (4210, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for S--H--S abstractions, Aaron Vandeputte""",
)

entry(
    index = 7028,
    label = "S/H/Cb;S_rad/Cb",
    kinetics = ArrheniusEP(
        A = (189, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for S--H--S abstractions, Aaron Vandeputte""",
)

entry(
    index = 7035,
    label = "S/H/NonDeS;S_rad/NonDeS",
    kinetics = ArrheniusEP(
        A = (113, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Group additivity method for S--H--S abstractions, Aaron Vandeputte""",
)

