#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol_Aromatic/training"
shortDesc = u"Reaction kinetics used as training data to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "phenol <=> cyclohexa-2,4-dien-1-one",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.06e+12, 's^-1'),
        n = 0,
        Ea = (69.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 phenol -> 2,4-cyclohexadienone tautomerization (Zhu & Bozzelli 2003)""",
    longDesc = u"""
Phenol -> cyclohexa-2,4-dien-1-one (keto tautomer), gas phase.

Source: L. Zhu & J.W. Bozzelli, "Kinetics and Thermochemistry of C4H6O
Isomers ... phenol <=> 2,4-cyclohexadienone", J. Phys. Chem. A 107 (2003)
3696-3703, DOI 10.1021/jp0212545. COMPUTED at CBS-QB3 with isodesmic
corrections: k = 8.06e12 * exp(-69.4 kcal/mol / RT) s^-1;
delta_H(reaction, 298 K) = +18.6 kcal/mol (2,4-keto);
Keq(298 K) = 7.15e-14. The 2,5-keto channel (delta_H = +17.0 kcal/mol) is
a distinct 1,5-shift and is NOT covered by this family's template.

Provenance class: COMPUTED (CBS-QB3). Attribution note carried from the
phase-6 evidence review: a "da Silva/Kim/Bozzelli 2006" attribution
circulating for these numbers is incorrect; the value is Zhu & Bozzelli
2003, DOI 10.1021/jp0212545.

Degeneracy note: the reaction as written has a reaction-path degeneracy of
2 (two equivalent ortho carbons of phenol); the A factor above is taken as
the total rate for phenol as reported by the source, and RMG divides by the
degeneracy when deriving the per-site rate rule. If the source A were
per-site, the derived rule would be a factor of 2 conservative.

Effect scope: this family is not auto-generated, so this training entry
folds into the Root rate rule at load time and generalizes to substituted
aromatic enols (o-cresol-type rings and hydroxylated diarylmethane novolac
bridges) at honestly-labeled ANALOGY tier through the ortho_C node falling
back to Root.
""",
)
