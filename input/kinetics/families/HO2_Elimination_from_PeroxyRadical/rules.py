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
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 1,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 836,
    label = "R2OO_2H_2H",
    kinetics = ArrheniusEP(
        A = (15600000.0, 's^-1'),
        n = 1.69,
        alpha = 0,
        E0 = (29.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 837,
    label = "R2OO_HNd_2H",
    kinetics = ArrheniusEP(
        A = (47900000.0, 's^-1'),
        n = 1.46,
        alpha = 0,
        E0 = (29.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 838,
    label = "R2OO_NdNd_2H",
    kinetics = ArrheniusEP(
        A = (506000000.0, 's^-1'),
        n = 1.19,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 839,
    label = "R2OO_2H_HNd",
    kinetics = ArrheniusEP(
        A = (979000000.0, 's^-1'),
        n = 1.17,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 840,
    label = "R2OO_HNd_HNd",
    kinetics = ArrheniusEP(
        A = (1650000000.0, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 841,
    label = "R2OO_NdNd_HNd",
    kinetics = ArrheniusEP(
        A = (64800000000.0, 's^-1'),
        n = 0.57,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 842,
    label = "R2OO_2H_NdNd",
    kinetics = ArrheniusEP(
        A = (7480000000.0, 's^-1'),
        n = 1.08,
        alpha = 0,
        E0 = (29.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 843,
    label = "R2OO_HNd_NdNd",
    kinetics = ArrheniusEP(
        A = (811000000000000.0, 's^-1'),
        n = -0.78,
        alpha = 0,
        E0 = (30.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 844,
    label = "R2OO_NdNd_NdNd",
    kinetics = ArrheniusEP(
        A = (3.1e+19, 's^-1'),
        n = -1.78,
        alpha = 0,
        E0 = (31.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.""",
    longDesc = 
u"""

""",
)

entry(
    index = 845,
    label = "R2OO_2H_HCd",
    kinetics = ArrheniusEP(
        A = (825300, 's^-1', '*|/', 5),
        n = 1.829,
        alpha = 0,
        E0 = (24.247, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
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
)

entry(
    index = 846,
    label = "R2OO_2H_HDe",
    kinetics = ArrheniusEP(
        A = (825300, 's^-1', '*|/', 5),
        n = 1.829,
        alpha = 0,
        E0 = (24.247, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
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
)

entry(
    index = 847,
    label = "R2OO_O_HNd",
    kinetics = ArrheniusEP(
        A = (68130000000.0, 's^-1', '*|/', 10),
        n = 0.493,
        alpha = 0,
        E0 = (11.894, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
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
""",
)

entry(
    index = 848,
    label = "R2OO_O",
    kinetics = ArrheniusEP(
        A = (6380000000000.0, 's^-1', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (11.4, 'kcal/mol', '+|-', 2),
        Tmin = (200, 'K'),
        Tmax = (600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Hermans et al. 2005 (doi:10.1021/jp044080v) G2M calculations""",
    longDesc = 
u"""
MRH approximation for the general OCOO node

In the event RMG finds any H-O-C-O-O* connection, the kinetics used for direct
HO2 elimination will be those of CH3-CH(OO)-OH => CH3CHO + HO2.
""",
)

entry(
    index = 849,
    label = "R2OO_2H_2H",
    kinetics = ArrheniusEP(
        A = (4840000.0, 's^-1'),
        n = 1.67,
        alpha = 0,
        E0 = (29.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""pp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 850,
    label = "R2OO_2H_HNd",
    kinetics = ArrheniusEP(
        A = (136000000.0, 's^-1'),
        n = 1.28,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""sp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 851,
    label = "R2OO_HNd_2H",
    kinetics = ArrheniusEP(
        A = (208000000.0, 's^-1'),
        n = 1.25,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ps, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 852,
    label = "R2OO_2H_NdNd",
    kinetics = ArrheniusEP(
        A = (36600000000.0, 's^-1'),
        n = 0.62,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""tp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 853,
    label = "R2OO_NdNd_2H",
    kinetics = ArrheniusEP(
        A = (194000000.0, 's^-1'),
        n = 1.27,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""pt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 855,
    label = "R2OO_HNd_HNd",
    kinetics = ArrheniusEP(
        A = (108700000000.0, 's^-1'),
        n = 0.8,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ss ,Multiplied 1.5 to trans rate coefficient , CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 856,
    label = "R2OO_NdNd_HNd",
    kinetics = ArrheniusEP(
        A = (35000000000.0, 's^-1'),
        n = 0.71,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""st, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 857,
    label = "R2OO_HNd_NdNd",
    kinetics = ArrheniusEP(
        A = (56200000000.0, 's^-1'),
        n = 0.58,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ts, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 858,
    label = "R2OO_NdNd_NdNd",
    kinetics = ArrheniusEP(
        A = (6250000000000.0, 's^-1'),
        n = 0.02,
        alpha = 0,
        E0 = (30.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""tt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 849,
    label = "R2OO_2H_2H",
    kinetics = ArrheniusEP(
        A = (4840000.0, 's^-1'),
        n = 1.67,
        alpha = 0,
        E0 = (29.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""pp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 850,
    label = "R2OO_2H_HNd",
    kinetics = ArrheniusEP(
        A = (136000000.0, 's^-1'),
        n = 1.28,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""sp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 851,
    label = "R2OO_HNd_2H",
    kinetics = ArrheniusEP(
        A = (208000000.0, 's^-1'),
        n = 1.25,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ps, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 852,
    label = "R2OO_2H_NdNd",
    kinetics = ArrheniusEP(
        A = (36600000000.0, 's^-1'),
        n = 0.62,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""tp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 853,
    label = "R2OO_NdNd_2H",
    kinetics = ArrheniusEP(
        A = (194000000.0, 's^-1'),
        n = 1.27,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""pt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 855,
    label = "R2OO_HNd_HNd",
    kinetics = ArrheniusEP(
        A = (108700000000.0, 's^-1'),
        n = 0.8,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ss ,Multiplied 1.5 to trans rate coefficient , CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 856,
    label = "R2OO_NdNd_HNd",
    kinetics = ArrheniusEP(
        A = (35000000000.0, 's^-1'),
        n = 0.71,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""st, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 857,
    label = "R2OO_HNd_NdNd",
    kinetics = ArrheniusEP(
        A = (56200000000.0, 's^-1'),
        n = 0.58,
        alpha = 0,
        E0 = (29.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ts, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 858,
    label = "R2OO_NdNd_NdNd",
    kinetics = ArrheniusEP(
        A = (6250000000000.0, 's^-1'),
        n = 0.02,
        alpha = 0,
        E0 = (30.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""tt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
)

entry(
    index = 869,
    label = "R2OO_0H_2H",
    kinetics = ArrheniusEP(
        A = (3630000000.0, 's^-1'),
        n = 1.11,
        alpha = 0,
        E0 = (42.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""BMK/cbsb7, HO""",
    longDesc = 
u"""

""",
)

