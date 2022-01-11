#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 5,
    label = "H2O + X <=> H2OX",
    kinetics = StickingCoefficient(
        A = 1.0E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R5
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 7,
    label = "CO2 + X <=> CO2X",
    kinetics = StickingCoefficient(
        A = 7.0E-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R7
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 11,
    label = "CH4 + X <=> CH4X",
    kinetics = StickingCoefficient(
        A = 8.0E-3,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R11
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

# entry(
#     index = 12,
#     label = "X + H3N <=> H3NX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'m^3/(mol*s)'), n=0, Ea=(0.42,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODA1""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ru
# Original entry: X + NH3 <=> NH3X
# equation : NH3(g) + * -> NH3*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: LogadottirAmmonia2003
# reactionEnergy: -0.42 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Ru",
#     facet = "1",
# )

