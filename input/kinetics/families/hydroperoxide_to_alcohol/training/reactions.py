#!/usr/bin/env python
# encoding: utf-8

name = "hydroperoxide_to_alcohol/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 0,
    label = "CH3OOH + H2O <=> CH3OH + H2O2",
    degeneracy = 1.0,
    rank = 5,
    kinetics = Arrhenius(A=(1.2e+16,'cm^3/(mol*s)'), n=0, Ea=(25,'kcal/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
estimated to have a lifetime of about 1 min
this rate at 313K is 4.2E-1 cm^3/(mol*s),
accounting for the [H2O] which is 69.2% * 0.00556 mol/cm^3 it becomes 1.62E-2 s^-1,
which is a lifetime of ~1 min
""",
)

entry(
    index = 1,
    label = "H2O + cyanoisopropylOOH <=> H2O2 + cyanoisopropylOH",
    degeneracy = 1.0,
    rank = 5,
    kinetics = Arrhenius(A=(1.2e+16,'cm^3/(mol*s)'), n=0, Ea=(25,'kcal/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
estimated to have a lifetime of about 1 min, see explanation above
""",
)
