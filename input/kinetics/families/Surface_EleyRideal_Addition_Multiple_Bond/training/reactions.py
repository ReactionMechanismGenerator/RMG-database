#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Addition_Multiple_Bond/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "C2 + ethylene <=>  X_C4",
    kinetics = StickingCoefficient(
        A = 5.0E-2,
        n = 0.,
        Ea = (68.66, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205""",
    metal = "Co",
)

entry(
    index = 2,
    label = "C4 + ethylene <=> X_C6",
    kinetics = StickingCoefficient(
        A = 5.0E-2,
        n = 0.,
        Ea = (68.34, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205""",
    metal = "Co",
)

entry(
    index = 3,
    label = "C6 + ethylene <=> X_C8",
    kinetics = StickingCoefficient(
        A = 5.0E-2,
        n = 0.,
        Ea = (77.62, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205""",
    metal = "Co",
)

entry(
    index = 4,
    label = "C8 + ethylene <=> X_C10",
    kinetics = StickingCoefficient(
        A = 5.0E-2,
        n = 0.,
        Ea = (77.62, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""Same as *C6.  E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205""",
    metal = "Co",
)

# entry(
#     index = 5,
#     label = "CHO2X <=> HX + CO2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(0.74,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM2Mg==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: COOHX <=> HX + CO2
# equation : COOH* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.11 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Pd",
#     facet = "211",
# )

# entry(
#     index = 6,
#     label = "CHO2X-2 <=> HX + CO2-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM2NQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: HCOOX <=> HX + CO2
# equation : HCOO* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.23 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Pd",
#     facet = "211",
# )

# entry(
#     index = 7,
#     label = "CHO2X <=> HX + CO2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.32,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM3Mw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: COOHX <=> HX + CO2
# equation : COOH* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -0.12 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 8,
#     label = "CHO2X-2 <=> HX + CO2-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.32,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM3NA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: HCOOX <=> HX + CO2
# equation : HCOO* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.88 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 9,
#     label = "CHO2X <=> HX + CO2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.01,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM2Nw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: COOHX <=> HX + CO2
# equation : COOH* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.54 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 10,
#     label = "CHO2X-2 <=> HX + CO2-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.45,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM3Ng==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: HCOOX <=> HX + CO2
# equation : HCOO* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.95 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 11,
#     label = "CHO2X <=> HX + CO2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM2Ng==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: COOHX <=> HX + CO2
# equation : COOH* -> CO2(g) + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: YooTheoretical2014,
# reactionEnergy: 0.41 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 12,
#     label = "CHO2X-2 <=> HX + CO2-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.09,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM2OQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: HCOOX <=> HX + CO2
# equation : HCOO* -> CO2(g) + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: YooTheoretical2014,
# reactionEnergy: -0.31 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 13,
#     label = "CHO2X <=> HX + CO2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.32,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM3Mg==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: COOHX <=> HX + CO2
# equation : COOH* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -0.16 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 14,
#     label = "CHO2X-2 <=> HX + CO2-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.45,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM3NQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: HCOOX <=> HX + CO2
# equation : HCOO* -> CO2(g) + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.86 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# """,
#     metal = "Ag",
#     facet = "211",
# )

