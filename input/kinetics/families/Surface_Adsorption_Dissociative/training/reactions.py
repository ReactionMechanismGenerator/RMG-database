#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociative/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
   index = 1,
   label = "H2 + Ni_3 + Ni_4 <=> HX_3 + HX_4",
   degeneracy = 2,
   kinetics = StickingCoefficient(
       A = 3e-2,
       n = 0,
       Ea = (5, 'kJ/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   rank = 3,
   shortDesc = u"""Deutschmann Ni""",
   longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904
""",
    metal = "Ni"
)

entry(
   index = 2,
   label = "H2 + Ni_3 + Ni_4 <=> HX_3 + HX_4",
   degeneracy = 2,
   kinetics = StickingCoefficient(
       A = 0.046,
       n = 0,
       Ea = (0, 'J/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   rank = 10,
   shortDesc = u"""H2 on Pt""",
   longDesc = u"""
    Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
    Xu, Clayton, Balakotaiah, Harold et al.
    doi: 10.1016.j.apcatb.2007.08.008

    This is R2
    """,
    metal = 'Pt'
)

# entry(
#    index = 6,
#    label = "HX_4 + HOX_1 <=> H2O + Ni_3 + Ni_4",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A = (4.02e14, 'm^2/(mol*s)'),
#        n = 0,
#        Ea = (17.4, 'kJ/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    rank = 10,
#    shortDesc = u"""H2O dissociative adsorption on Pt""",
#    longDesc = u"""
#     Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
#     Xu, Clayton, Balakotaiah, Harold et al.
#     doi: 10.1016.j.apcatb.2007.08.008
#
#     This is R6
#     """,
#     metal = "Pt"
# )
