#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2H3O3 <=> C2H2O + HO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.6e+09, 's^-1', '*|/', 2.51189),
        n = 1.2,
        Ea = (34.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['J. W. Allen', 'C. F. Goldsmith', 'W. H. Green'],
        title = 'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '14',
        pages = '1131-1155',
        year = '2012',
    ),
    referenceType = "theory",
    rank = 10,
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
DOI: 10.1039/C1CP22765C
""",
)

entry(
    index = 1,
    label = "C2H5O2 <=> C2H4 + HO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3e+10, 's^-1'),
        n = 1,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO
""",
)

entry(
    index = 2,
    label = "C2H5O2 <=> C2H4 + HO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.68e+07, 's^-1'),
        n = 1.69,
        Ea = (124.683, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_2H_2H
""",
)

entry(
    index = 3,
    label = "C3H7O2 <=> C3H6 + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.58e+07, 's^-1'),
        n = 1.46,
        Ea = (123.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_HNd_2H
""",
)

entry(
    index = 4,
    label = "C4H9O2 <=> C4H8 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.06e+08, 's^-1'),
        n = 1.19,
        Ea = (125.102, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_NdNd_2H
""",
)

entry(
    index = 5,
    label = "C3H7O2-2 <=> C3H6-2 + HO2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (5.874e+09, 's^-1'),
        n = 1.17,
        Ea = (125.938, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_2H_HNd
""",
)

entry(
    index = 6,
    label = "C4H9O2-2 <=> C4H8-2 + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.3e+09, 's^-1'),
        n = 1.01,
        Ea = (123.846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_HNd_HNd
""",
)

entry(
    index = 7,
    label = "C5H11O2 <=> C5H10 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.48e+10, 's^-1'),
        n = 0.57,
        Ea = (125.102, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_NdNd_HNd
""",
)

entry(
    index = 8,
    label = "C4H9O2-3 <=> C4H8-3 + HO2",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (6.732e+10, 's^-1'),
        n = 1.08,
        Ea = (124.265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_2H_NdNd
""",
)

entry(
    index = 9,
    label = "C5H11O2-2 <=> C5H10-2 + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.622e+15, 's^-1'),
        n = -0.78,
        Ea = (127.194, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_HNd_NdNd
""",
)

entry(
    index = 10,
    label = "C6H13O2 <=> C6H12 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.1e+19, 's^-1'),
        n = -1.78,
        Ea = (132.633, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_NdNd_NdNd
""",
)

entry(
    index = 11,
    label = "C4H7O2 <=> C4H6 + HO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.4759e+06, 's^-1', '*|/', 5),
        n = 1.829,
        Ea = (101.449, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
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

Converted to training reaction from rate rule: R2OO_2H_HCd
""",
)

entry(
    index = 12,
    label = "C4H7O2 <=> C4H6 + HO2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.4759e+06, 's^-1', '*|/', 5),
        n = 1.829,
        Ea = (101.449, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Same as node 845 (MRH assumption)""",
    longDesc = 
u"""
MRH approximation for the general R2OO_2H_HDe node

MRH computed the rate coefficient for the reaction CH3-CH(OO)-CH=CH2 => CH2=CH-CH=CH2 + HO2 (see node 845).
The difference between the R2OO_2H_HDe and CH3CH(OO)CHCH2 nodes is defining the delocalized group (in the
case of the CH3CH(OO)CHCH2 node, the -CH=CH2 functional group).  MRH thinks using the kinetics for node 845
in the event node 846 is hit is reasonable, considering this part of the molecule does not play a role in the
TS (and it is certainly better than leaving RMG to estimate via "Average of Average").

Converted to training reaction from rate rule: R2OO_2H_HDe
""",
)

entry(
    index = 13,
    label = "C2H5O3 <=> C2H4O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.813e+10, 's^-1', '*|/', 10),
        n = 0.493,
        Ea = (123.219, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections.""",
    longDesc = 
u"""
MRH CBS-QB3 calculations for the reaction CH3-CH(OO)-OH => CH3-CH=O + HO2

Previous RMG estimate for this reaction was zero (RMG only allowed HO2 direct elimination
to occur for species with the structure H-C-C-O-O* ... note the atom next to the hydrogen
had to be a carbon).

MRH calculated the rate coefficient using the CBS-QB3 method.  1-d hindered rotor
corrections were applied and NO tunneling correction.  The reason no tunneling correction
was applied is that the TS is lower in energy than the products, CH3CHO + HO2.

da Silva, Bozzelli, Liang, and Farrell (dx.doi.org/10.1021/jp903210a) recently studied
this reaction system (ethanol + O2).  In their calculations (G3B3), they determined a stable
adduct existed between the reactant CH3CH(OO)OH and the products CH3CHO+HO2.  The adduct is
stable due to H-bonding.  MRH believes his TS is for the reactant to the adduct.
Comparing my k(T) with the da Silva et al. k(T) (for forming the adduct) shows very
good agreement, within a factor of 2 over the valid temperature range.  Furthermore, the
da Silva et al. calculation for the adduct going to product is between 2-5 orders of
magnitude faster than reactants going to adduct, so it is a reasonable assumption
to say the first step is the rate-limiting step.

Comparing my k(T) with two other sources for this reaction (dx.doi.org/10.1021/jp003762p and 
I. Hermans et al., AIAA Journal, 109, (2005), 4303-4311) also shows good agreement.
I am setting the rank for this k(T) to be 5 (very uncertain).

Information on the TST calculations:

Reactant: 3 hindered rotors were considered (the -OO, -CH3, and -OH torsions)
TS: 1 hindered rotor was considered (the -CH3 torsion)
Product: 1 hindered rotor was considered (the -CH3 torsion of CH3CHO)

All external symmetry numbers were set equal to one.
The k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 6.813e+10 * (T/1K)^0.493 * exp(-11.894 kcal/mol / RT) cm3/mol/s.

Converted to training reaction from rate rule: R2OO_O_HNd
""",
)

entry(
    index = 14,
    label = "CH3O3 <=> CH2O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.38e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (123.219, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Hermans et al. 2005 (doi:10.1021/jp044080v) G2M calculations""",
    longDesc = 
u"""
MRH approximation for the general OCOO node

In the event RMG finds any H-O-C-O-O* connection, the kinetics used for direct
HO2 elimination will be those of CH3-CH(OO)-OH => CH3CHO + HO2.

Converted to training reaction from rate rule: R2OO_O
""",
)

entry(
    index = 15,
    label = "C3H5O2 <=> C3H4 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.63e+09, 's^-1'),
        n = 1.11,
        Ea = (178.657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""BMK/cbsb7, HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OO_0H_2H
""",
)

