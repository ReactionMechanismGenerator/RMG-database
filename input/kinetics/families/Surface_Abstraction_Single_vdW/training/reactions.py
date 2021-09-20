#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "HCO_X + H2O_X <=> CH2O_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (18.3, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012).
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R103 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)
