#!/usr/bin/env python
# encoding: utf-8

name = "Salicyl_Alcohol_Dehydration/training"
shortDesc = u"Reaction kinetics used as training data to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "salicyl_alcohol <=> oQM + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+15, 's^-1'),
        n = 0,
        Ea = (64.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 10,
    shortDesc = u"""ESTIMATED: salicyl alcohol -> o-QM + H2O gas-phase unimolecular dehydration""",
    longDesc = u"""
ESTIMATION - NOT a literature-cited elementary rate. Recorded honestly per
the phase-6 provenance protocol; do not promote in rank until verified
against the primary sources.

Basis of the estimate:
- Numerically identical to the in-repo phenolic_pyrolysis library entry R5
  ("oHO_BzOH <=> oQM + H2O", A = 1.995e15 s^-1 = 10^15.3, Ea = 64.3
  kcal/mol, provenance-labeled "Direct (model compound, VLPP-MS)" there but
  carried without a full citation), so the family and the library are
  mutually consistent.
- The expected primary sources are Dorrestijn, Pugin, Ciriano Nogales &
  Mulder, J. Org. Chem. 62 (1997) 4804-4810, and Dorrestijn, Epema,
  van Scheppingen & Mulder, J. Chem. Soc., Perkin Trans. 2 (1998)
  1173-1178, DOI 10.1039/a800189h (VLPP work on o-QM generation). The
  available Van De Water & Pettus review (Tetrahedron 58 (2002) 5367,
  checked 2026-07-22) cites Dorrestijn/Mulder only qualitatively and
  contains NO rate parameters; the primary PDFs remain to be retrieved.
- Qualitative condensed-phase sanity anchor: o-hydroxybenzyl alcohols
  generate trappable o-QM on heating to ~170-210 C in solution
  (Van De Water & Pettus 2002, sections 2.3/3.1); the much higher
  gas-phase unimolecular barrier booked here reflects the absence of the
  acid/base/water assistance that operates in the condensed phase.
- Reaction thermochemistry anchor: delta_f_H(298 K) of o-QM = 16.4
  kcal/mol at CBS-QB3 (da Silva & Bozzelli, J. Phys. Chem. A 111 (2007)
  7987, DOI 10.1021/jp073335c), which constrains the reverse (o-QM + H2O)
  rate through equilibrium.

Uncertainty: at least a factor of 10 in A and +/-5 kcal/mol in Ea.
""",
)
