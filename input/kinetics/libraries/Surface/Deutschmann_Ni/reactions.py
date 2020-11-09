#!/usr/bin/env python
# encoding: utf-8

name = "Deutschmann_Ni"
shortDesc = u""
longDesc = u"""
test surface mechanism: based upon Olaf Deutschmann's work:
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904
"""

#moved to Surface_Adsorption_Dissociative/training
#actually, no. moved back here. Including it in training made all other dissociative adsorption too facile.
entry(
    index = 1,
    label = "H2 + Ni + Ni <=> HX + HX",
    kinetics = StickingCoefficient(
        A = 3.2E-2,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R1""",
	metal = "Ni",
)

#skip R2 - reverse included

#CFG: O2 is a special case: we need to treat it separately
entry(
    index = 3,
    label = "O2 + Ni + Ni <=> OX + OX",
    kinetics = StickingCoefficient(
        A = 4.36E-2,
        n = -0.206,
        Ea=(1.5E3, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R3""",
	metal = "Ni",
)

#skip R4
#R5 moved to Surface_Adsorption_vdW
#skip R6 vdW, reverse of R5
#R7 moved to Surface_Adsorption_vdW
#skip R8 vdW, reverse of R7

#CFG: CO is a special case: we need to treat it separately
entry(
    index = 9,
    label = "CO + Ni <=> OCX",
    kinetics = StickingCoefficient(
        A = 5.0E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R9 """,
	metal = "Ni",
)

#skip R10
#R11 moved to Surface_Adsorption_vdW
#skip R12, reverse of R11
#R13 moved to Surface_Dissociation_vdW

#CFG: Modified version of R14: reverse of dissociative adsorption
#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning and R13 was added, this can be commented out
# entry(
#     index = 14,
#     label = "CH3X + HX <=> CH4X + Ni",
#     kinetics = SurfaceArrhenius(
#         A=(1.44E18, 'm^2/(mol*s)'),
#         n = -0.087,
#         Ea=(63400.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R14. We input reverse direction""",
# 	metal = "Ni",
# )

#skip R15
# moved to Surface_Dissociation/training
#entry(
#    index = 16,
#    label = "CH2X + HX <=> CH3X + Ni",
#    kinetics = SurfaceArrhenius(
#        A=(3.09E19, 'm^2/(mol*s)'),
#        n = -0.087,
#        Ea=(57200.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R16""",
#	 metal = "Ni",
#)

#skip R17
# moved to Surface_Dissociation/training
#entry(
#    index = 18,
#    label = "CHX + HX <=> CH2X + Ni",
#    kinetics = SurfaceArrhenius(
#        A=(9.77E20, 'm^2/(mol*s)'),
#        n = -0.087,
#        Ea=(81000.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R18""",
#	 metal = "Ni",
#)

# moved to Surface_Dissociation/training
#entry(
#    index = 19,
#    label = "CHX + Ni <=> CX + HX",
#    kinetics = SurfaceArrhenius(
#        A=(9.88E16, 'm^2/(mol*s)'),
#        n = 0.5,
#        Ea=(21900.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R19""",
#	 metal = "Ni",
#)

#skip R20
#moved R21 to Surface_Abstraction_vdW

#CFG: Modified version of R22: CH4* now goes directly to CH4(g)
#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning and R21 was added, this can be commented out
# entry(
#     index = 22,
#     label = "CH3X + HOX <=> CH4X + OX",
#     kinetics = SurfaceArrhenius(
#         A=(2.98E18, 'm^2/(mol*s)'),
#         n = 0.101,
#         Ea=(25800.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R22. We input reverse direction""",
# 	metal = "Ni",
# )

#skip R23
#moved R24 to Surface_Abstraction/training
#entry(
#    index = 24,
#    label = "CH2X + HOX <=> CH3X + OX",
#    kinetics = SurfaceArrhenius(
#        A=(1.39E17, 'm^2/(mol*s)'),
#        n = 0.101,
#        Ea=(19000.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R24""",
#	 metal = "Ni",
#)

#skip R25
#moved R26 to Surface_Abstraction/training
#entry(
#    index = 26,
#    label = "CHX + HOX <=> CH2X + OX",
#    kinetics = SurfaceArrhenius(
#        A=(4.40E18, 'm^2/(mol*s)'),
#        n = 0.101,
#        Ea=(42400.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R26""",
#	 metal = "Ni",
#)

#moved R27 to Surface_Abstraction/training
#entry(
#    index = 27,
#    label = "CHX + OX <=> CX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(2.47E17, 'm^2/(mol*s)'),
#        n = 0.312,
#        Ea=(57700.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R27""",
#	 metal = "Ni",
#)

#skip R28
#moved R29 to Surface_Dissociation_vdW

#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning and R29 was added, this can be commented out
# entry(
#     index = 30,
#     label = "HX + HOX <=> H2OX + Ni",
#     kinetics = SurfaceArrhenius(
#         A=(1.85E16, 'm^2/(mol*s)'),
#         n = 0.086,
#         Ea=(41500.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R30. We input reverse direction""",
# 	metal = "Ni",
# )

#skip R31
#moved to Surface_Dissociation/training
#entry(
#    index = 32,
#    label = "HOX + Ni <=> HX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(2.25E16, 'm^2/(mol*s)'),
#        n = 0.188,
#        Ea=(29600.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R32""",
#	 metal = "Ni",
#)

#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning and R34 was added, this can be commented out
# entry(
#     index = 33,
#     label = "HOX + HOX <=> H2O + OX + Ni",
#     kinetics = SurfaceArrhenius(
#         A=(2.34E16, 'm^2/(mol*s)'),
#         n = 0.274,
#         Ea=(92300.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R33""",
# 	metal = "Ni",
# )

#moved R34 to Surface_Abstraction_vdW
#skip R35

#We don't yet have a template for breaking a double bond for surface dissociation.
#when we do, this should move there.
entry(
    index = 36,
    label = "OCX + Ni <=> CX + OX",
    kinetics = SurfaceArrhenius(
        A=(1.75E9, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(116200.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R36""",
	metal = "Ni",
)

#skip R37

#not an elementary reaction according to our families
entry(
    index = 38,
    label = "CX + HOX <=> HX + OCX",
    kinetics = SurfaceArrhenius(
        A=(3.88E21, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(62500.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R38""",
	metal = "Ni",
)

#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning, but we do not have a family for this
entry(
    index = 39,
    label = "OCX + OCX <=> CO2X + CX",
    kinetics = SurfaceArrhenius(
        A=(1.62E10, 'm^2/(mol*s)'),
        n = 0.5,
        Ea=(241700.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R39. We input reverse direction""",
	metal = "Ni",
)

#skip R40, reverse of R39

#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning and R42 was added, this can be commented out
# entry(
#     index = 41,
#     label = "OCX + OX <=> CO2X + Ni",
#     kinetics = SurfaceArrhenius(
#         A=(2.00E15, 'm^2/(mol*s)'),
#         n = 0.0,
#         Ea=(123600.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R41. We use reverse reaction""",
# 	metal = "Ni",
# )


#moved R42 to Surface_Dissociation_Double_vdW
#skip R43
# moved to Surface_Dissociation/training
#entry(
#    index = 44,
#    label = "HOCXO + Ni <=> OCX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(1.46E20, 'm^2/(mol*s)'),
#        n = -0.213,
#        Ea=(54300.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R44""",
#	 metal = "Ni",
#)

#moved R45 to Surface_Addition_Single_vdW

#since vdW is not yet functioning, we include this reaction in library
#now vdW is functioning and R45 was added, this can be commented out
# entry(
#     index = 46,
#     label = "HOCXO + Ni <=> CO2X + HX",
#     kinetics = SurfaceArrhenius(
#         A=(3.73E16, 'm^2/(mol*s)'),
#         n = 0.475,
#         Ea=(33600.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R46""",
# 	metal = "Ni",
# )


#skip R47
# moved to Surface_Dissociation/training
#entry(
#    index = 48,
#    label = "CXHO + Ni <=> OCX + HX",
#    kinetics = SurfaceArrhenius(
#        A=(3.71E17, 'm^2/(mol*s)'),
#        n = 0.0,
#        Ea=(0.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R48""",
#	 metal = "Ni",
#)

#skip R49

#We don't yet have a template for breaking a double bond for surface dissociation.
#when we do, this should move there.
entry(
    index = 50,
    label = "CHX + OX <=> CXHO + Ni",
    kinetics = SurfaceArrhenius(
        A=(4.59E16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(109900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R50""",
	metal = "Ni",
)

#similar to R38. curious O-insertion
#not an elementary reaction according to our families
entry(
    index = 52,
    label = "CXHO + HOX <=> HOCXO + HX",
    kinetics = SurfaceArrhenius(
        A=(2.28E16, 'm^2/(mol*s)'),
        n = 0.263,
        Ea=(15900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R52""",
	metal = "Ni",
)
