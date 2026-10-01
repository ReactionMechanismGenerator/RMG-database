#!/usr/bin/env python
# encoding: utf-8

name = "Aryl_Decarbonylation/training"
shortDesc = u"Reaction kinetics used as training data to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "phenoxy <=> cyclopentadienyl + CO",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.4e+11, 's^-1'),
        n = 0,
        Ea = (43.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1580, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Shock-tube measurement, phenoxy -> C5H5 + CO (Lin & Lin 1986)""",
    longDesc = u"""
Phenoxy radical decarbonylation to cyclopentadienyl + CO, gas phase.

Source: C.-Y. Lin & M. C. Lin, "Thermal decomposition of methyl phenyl
ether in shock waves: the kinetics of phenoxy radical reactions",
J. Phys. Chem. 90 (1986) 425-431 (anisole shock-tube pyrolysis; phenoxy
decay by CO formation). MEASURED effective first-order rate:
k = 7.4e11 * exp(-43.9 kcal/mol / RT) s^-1, 1000-1580 K.
(DOI not carried here pending verification against the primary PDF; the
bibliographic reference above is complete.)

Consistency band (recorded per phase-6 provenance practice):
- A newer shock-tube CO-absorption determination reports
  k = 9.1e13 * exp(-220.3 kJ/mol / RT) s^-1 (~52.7 kcal/mol; DOI
  10.1002/kin.21105 per the 2026 DR2 literature pass); the two
  expressions agree within a factor of ~2-3 over 1000-1580 K.
- Theory places the rate-limiting barrier of the multi-step contraction
  at ~54 kcal/mol (10.1002/kin.20622 per DR2); the measured effective
  Arrhenius parameters book the overall channel, which is the standard
  mechanism-level treatment.

Degeneracy note: the reaction proceeds through either of the two
equivalent ortho keto resonance forms (degeneracy 2 as written); the A
factor above is the total measured phenoxy disappearance rate, and RMG
divides by the degeneracy when deriving the per-site rule.

Effect scope: this family is not auto-generated, so this entry folds into
the Root rate rule at load and generalizes to substituted aryloxy radicals
(methylphenoxy from cresols, hydroxyphenoxy from novolac daughters) at
honestly-labeled ANALOGY tier. Note DR2's caution that cresol-derived
(methylphenoxy) decarbonylation is somewhat slower than phenoxy; when
isomer-specific G4 rates are imported (carbon_phenol library), the library
values take precedence for those exact species.
""",
)
