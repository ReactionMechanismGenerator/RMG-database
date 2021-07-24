#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dual_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "COOH* + OH* <=> CO2* + H2O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.398e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0., 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 12 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

A factor from paper / surface site density of Cu
1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.398e17 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 2,
    label = "H2O* + CO2* <=> COOH* + OH*",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(7.15e+20,'cm^2/(mol*s)'), n=-0.1992, Ea=(13.1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dual_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Methane/Vlachos_Rh
Original entry: CO2_X + H2O_X <=> COOH_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.78E12(1/s)/2.49E-9(mol/cm^2) = 7.15E20 cm^2/(mol*s)

This is R39 in Table 4
""",
    metal = "Rh",
)

