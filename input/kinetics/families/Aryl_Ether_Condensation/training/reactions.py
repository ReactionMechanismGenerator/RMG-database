#!/usr/bin/env python
# encoding: utf-8

name = "Aryl_Ether_Condensation/training"
shortDesc = u"Reaction kinetics used as training data to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "phenol_A + phenol_B <=> diphenyl_ether + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.0e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (45.0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 10,
    shortDesc = u"""ESTIMATED: 2 phenol -> diphenyl ether + H2O, uncatalyzed gas-phase bimolecular condensation""",
    longDesc = u"""
ESTIMATION - NOT a literature-cited elementary rate. The 2026 DR2
deep-research pass confirmed that no MEASURED or QM/TST elementary rate
exists in the open literature for the uncatalyzed reaction
2 C6H5OH -> C6H5-O-C6H5 + H2O in any phase. Recorded honestly per the
phase-6 provenance protocol; do not promote in rank until replaced.

Basis of the estimate:
- Ea = 45 kcal/mol sits in the ReaxFF intrinsic water-generation barrier
  range for highly crosslinked phenolic resins, 42-49 kcal/mol (Jiang,
  Wang, Wu et al., Polymer (2011), DOI 10.1016/j.polymer.2010.12.034,
  ReaxFF MD 2000-3000 K), which is the closest computed ELEMENTARY
  surrogate identified by DR2.
- The condensed-phase isoconversional "stage-I" apparent Ea for cured
  phenolic water loss is 81.6-93.5 kJ/mol (~20-22 kcal/mol;
  Torres-Herrador et al., DOI 10.2514/1.J059423); that value is
  transport/diffusion-convolved and NOT elementary -- it is deliberately
  not used here, but it means the condensed-phase EFFECTIVE channel is
  much faster than this gas-phase elementary estimate. Polymer-pool decks
  should carry the lumped condensed-phase step separately (see the
  carbon_phenol library) rather than relying on this family for
  condensed-phase flux.
- Catalyzed etherification operates at 300-480 C (zeolite: US5288922;
  WO3: US5144094), bounding the uncatalyzed barrier from below.
- A = 1e11 cm^3/(mol*s) is a generic tight four-center bimolecular
  A-factor (entropically strangled TS; cf. molecular elimination/insertion
  families).

Uncertainty: at least a factor of 100 in A and +/-10 kcal/mol in Ea.

This reaction is the highest-priority in-house ARC/Arkane CBS-QB3 (or
G4/CCSD(T)) target of the phase-6 campaign: both DR2 reports independently
recommend computing it, since no literature value will ever fill the gap.
Replace this entry (and promote the rank per the rank rubric) when the
computed value lands.
""",
)
