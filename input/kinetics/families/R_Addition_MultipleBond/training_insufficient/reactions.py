#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 28,
    label = "C7H7-2 <=> C7H6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.16e+10, 's^-1'), n=1.24, Ea=(65.98, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)

Thermo data for C7H6 from `Group additivity`.
""",
)

entry(
    index = 38,
    label = "C7H9-20 <=> C7H8-11 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=1.27, Ea=(44.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc =
u"""
Taken from entry: prod_14 <=> prod_15 + H

Diverging thermo data for C7H8-11 for `C3` library and `Group additivity`.
""",
)

entry(
    index = 40,
    label = "C7H9-22 <=> C7H8-12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.47e+10, 's^-1'), n=1.22, Ea=(45.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc =
u"""
Taken from entry: prod_17 <=> prod_18 + H

Diverging thermo data for C7H9-22 for `C3` library and `Group additivity`.
""",
)

entry(
    index = 69,
    label = "C10H8-2 + H <=> C10H9-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc =
u"""
Taken from entry: biCPD3ene + H <=> adductb

Diverging thermo data for C10H9-2 for `SABIC_aromatics` library and `Group additivity`.
""",
)

entry(
    index = 70,
    label = "C10H8-3 + H <=> C10H9-3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc =
u"""
Taken from entry: biCPD3ene + H <=> adductc

Diverging thermo data for C10H9-3 for `SABIC_aromatics` library and `Group additivity`.
""",
)

entry(
    index = 76,
    label = "C9H11-1 <=> C8H8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+12, 's^-1'),
        n = 0.733,
        Ea = (35.918, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    rank = 10,
    longDesc =
u"""
Originally from reaction library: From 2012 Kislov

Duplicate to training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP,
Taken from entry: i7 <=> p1 + CH3
""",
)

entry(
    index = 97,
    label = "C9H11-3 <=> C2H4 + C7H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.39e+09, 's^-1'), n=1.1, Ea=(22.881, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc =
u"""
Taken from entry: i4 <=> benzyl + C2H4

Duplicate to originally from reaction library: New_Phenyl_Propene_Pathway, CBS-QB3
""",
)

entry(
    index = 99,
    label = "C7H9-8 <=> C6H6-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.831e+11, 's^-1'), n=0.669, Ea=(19.862, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2001_Tokmakov_H_Toluene_to_CH3_Benzene_high_P""",
    longDesc =
u"""
Taken from entry: ipso-(C7H9) <=> C6H6 + CH3

Duplicate to training reaction from kinetics library: vinylCPD_H, Taken from entry: product2 <=> BENZENE + CH3
""",
)

entry(
    index = 160,
    label = "C10H9-29 <=> C10H8-24 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.427e+09, 's^-1'), n=1.431, Ea=(66.532, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W106 <=> P109 + H

Diverging thermo data for C10H9-29, C10H8-24 for `SABIC_aromatics` library and `Group additivity`.
""",
)
	
entry(
    index = 161,
    label = "C10H9-30 <=> C10H8-25 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.893e+15, 's^-1'), n=-0.16, Ea=(65.494, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W108 <=> P109 + H

Diverging thermo data for C10H8-25 for `SABIC_aromatics` library and `Group additivity`.
""",
)

entry(
    index = 169,
    label = "C10H6-5 + H <=> C10H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc =
u"""
Taken from entry: P4 + H <=> W5

Diverging thermo data for C10H6-5 for `SABIC_aromatics` library and `Group additivity`.
""",
)

entry(
    index = 178,
    label = "C7H9-9 <=> C7H8-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.217e+10, 's^-1'), n=0.87, Ea=(25.199, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C7H9_12 <=> C7H8_17 + H_15

Duplicate to training reaction from kinetics library: vinylCPD_H, taken from entry: product2 <=> TOLUENE + H
""",
)

entry(
    index = 179,
    label = "C2H2 + C7H7-3 <=> C9H9-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (31630, 'cm^3/(mol*s)'),
        n = 2.479,
        Ea = (11.061, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C7H7_10 + ethyne_8 <=> C9H9_13

Duplicate to training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP, taken from entry: benzyl + C2H2 <=> W20
""",
)

entry(
    index = 200,
    label = "C4H5-3 <=> C4H4-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.385e+09, 's^-1'), n=1.347, Ea=(37.909, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ

Thermo for C4H5-3 and C4H4-5 from `Group additivity`.
""",
)
	
entry(
    index = 201,
    label = "C4H5-4 <=> C4H4-6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.905e+11, 's^-1'), n=0.877, Ea=(54.203, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ

Thermo for C4H5-4 and C4H4-6 from `Group additivity`.
""",
)

entry(
    index = 215,
    label = "C7H7-4 <=> C7H6-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.06e+10, 's^-1'), n=1.16, Ea=(26.18, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)

Thermo for C7H7-4 and C7H6-2 from `Group additivity`.
""",
)
	
entry(
    index = 216,
    label = "C7H7-5 <=> C7H6-3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.02e+13, 's^-1'), n=0.34, Ea=(46.7, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)

Thermo for C7H7-5 and C7H6-3 from `Group additivity`.
""",
)

entry(
    index = 2262,
    label = "C2H2 + C7H7-3 <=> C9H9-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (65600, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (44.9362, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Ct-H_Ct-H;CsJ-CbHH

Duplicate to training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP, taken from entry: benzyl + C2H2 <=> W20
""",
)

entry(
    index = 2268,
    label = "C2H2 + C2H3 <=> C4H5-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (91600, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (12.301, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Ct-H_Ct-H;CdsJ-H

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2547,
    label = "H + C4H4 <=> C4H5-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-0.8368, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Cds-HH_Cds-CtH;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2619,
    label = "H + C4H4-4 <=> C4H5-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (10.9202, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Cds-CtH_Cds-HH;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2699,
    label = "H + C4H4-3 <=> C4H5-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.7e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (6.86176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Ct-H_Ct-Cd;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2700,
    label = "H + C4H2 <=> C4H3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.48e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (6.19232, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Ct-H_Ct-Ct;HJ

Duplicate to
Klippenstein, S. J., Miller, J. A., The Addition of Hydrogen Atoms to Diacetylene and the Heats of Formation of i-C4H3 and n-C4H3, The Journal of Physical Chemistry A, 109 (19), 4285-4295, 2005. The restricted QCISD(T)/inf barrier heights//B3LYP/6-311++G(d,p)
These QCISD(T) calculations employed the correlation-consistent, polarized-valence, triple- (cc-pvtz) and quadruple- (cc-pvqz) basis sets and were extrapolated to the infinite basis-set limit via the expression.
""",
)

entry(
    index = 2705,
    label = "H + C4H4-2 <=> C4H5-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (14.7277, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Ct-Cd_Ct-H;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2807,
    label = "C2H4 + O2 <=> C2H4O2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (444, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (132.214, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cds-HH_Cds-HH;O2b

Thermo for C2H4O2 from `Group additivity`.
""",
)
	
entry(
    index = 2808,
    label = "propene_2 + O2 <=> C3H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (88.4, 'cm^3/(mol*s)'),
        n = 3.08,
        Ea = (126.357, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cds-CsH_Cds-HH;O2b

Thermo for C3H6O2 from `Group additivity`.
""",
)
	
entry(
    index = 2809,
    label = "propene_1 + O2 <=> C3H6O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (552, 'cm^3/(mol*s)'),
        n = 2.78,
        Ea = (124.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cds-HH_Cds-CsH;O2b

Thermo for C3H6O2-2 from `Group additivity`.
""",
)

entry(
    index = 2847,
    label = "CHN-2 + O <=> CHNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.99e+25, 'cm^3/(mol*s)'),
        n = -5.73,
        Ea = (61.463, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + O = HCNO (B&D #54) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
	
Converted to training reaction from rate rule: N3t_Ct-H;O_atom_triplet

Thermo data for `NitrogenCurran` very different from other library values. Strongly diverging thermo data for CHNO.
""",
)

entry(
    index = 2862,
    label = "C7H9-15 <=> C7H8-9 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc =
u"""
Taken from entry: product24 <=> product13 + H

This training reaction violates the collision limit in the backward direction when using thermo data from `vinylCPD_H` or `SABIC_aromatics`.
""",
)

entry(
    index = 2864,
    label = "H + C4H4 <=> C4H5-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-0.8368, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Cds-HH_Cds-CtH;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2866,
    label = "H + C4H4-3 <=> C4H5-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.7e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (6.86176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Ct-H_Ct-Cd;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

entry(
    index = 2867,
    label = "H + C4H4-2 <=> C4H5-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (14.7277, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc =
u"""
Converted to training reaction from rate rule: Ct-Cd_Ct-H;HJ

Duplicate to Ribeiro, J. M., Mebel, A. M., Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study, Physical Chemistry Chemical Physics, 19 (22), 14543-14554, 2017.
""",
)

