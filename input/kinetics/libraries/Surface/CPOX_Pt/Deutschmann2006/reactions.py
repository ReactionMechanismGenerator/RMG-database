#!/usr/bin/env python
# encoding: utf-8

name = "Deutschmann_Pt"
shortDesc = u""
longDesc = u"""
test surface mechanism: based upon Olaf Deutschmann's work:
"Modeling the high-temperature catalytic partial oxidation of methane over platinum gauze: Detailed gas-phase and surface chemistries coupled with 3D flow field simulations"
Quiceno et al
Applied Catalysis, 2006, 303, 166-176
"""

entry(
    index = 1,
    label = "H2 + Pt + Pt <=> HX + HX",
    kinetics = StickingCoefficient(
        A = 4.6E-2,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R1""",
	metal = "Pt",
)

#CFG: O2 is a special case: we need to treat it separately
entry(
    index = 2,
    label = "O2 + Pt + Pt <=> OX + OX",
    kinetics = SurfaceArrhenius(
        A=(1.89E21, 'cm^5/(mol^2*s)'),
        n = -0.5,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R2""",
	metal = "Pt",
)

entry(
    index = 3,
    label = "CH4 + Pt + Pt <=> CH3X + HX",
    kinetics = StickingCoefficient(
        A = 9.0E-4,
        n = 0,
        Ea=(72000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R3""",
	metal = "Pt",
)

entry(
    index = 4,
    label = "CH4 + OX + Pt <=> CH3X + HOX",
    kinetics = SurfaceArrhenius(
        A=(5.0E18, 'cm^5/(mol^2*s)'),
        n = 0.7,
        Ea=(42000.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R4""",
	metal = "Pt",
)

entry(
    index = 5,
    label = "CH4 + HOX + Pt <=> CH3X + H2OX",
    kinetics = StickingCoefficient(
        A = 1.0,
        n = 0,
        Ea=(10000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R5""",
	metal = "Pt",
)

entry(
    index = 6,
    label = "H2O + Pt <=> H2OX",
    kinetics = StickingCoefficient(
        A = 7.5E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R6. H2OX is vdW H2O.""",
	metal = "Pt",
)

entry(
    index = 7,
    label = "CO2 + Pt <=> CO2X",
    kinetics = StickingCoefficient(
        A = 5.0E-3,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R7. H2OX is vdW CO2.""",
	metal = "Pt",
)

#CFG: CO is a special case: we need to treat it separately
entry(
    index = 8,
    label = "CO + Pt <=> OCX",
    kinetics = StickingCoefficient(
        A = 8.4E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R8""",
	metal = "Pt",
)


#endothermic - reverse of R1
#entry(
#    index = 9,
#    label = "HX + HX <=> Pt + Pt + H2",
#    kinetics = SurfaceArrhenius(
#        A=(3.7E17, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(67400.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R9""",
#	 metal = "Pt",
#)

#endothermic - reverse of R2
#entry(
#    index = 10,
#    label = "OX + OX <=> Pt + Pt + O2",
#    kinetics = SurfaceArrhenius(
#        A=(3.7E17, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(235500.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R10""",
#	 metal = "Pt",
#)

#endothermic - reverse of R6
#entry(
#    index = 11,
#    label = "H2OX <=> H2O + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(4.5E8, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(41800.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R11. H2OX is vdW H2O.""",
#	 metal = "Pt",
#)

#endothermic - reverse of R8
#entry(
#    index = 12,
#    label = "OCX <=> CO + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.0E11, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(146000.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R12""",
#	 metal = "Pt",
#)

#endothermic - reverse of R7
#entry(
#    index = 13,
#    label = "CO2X <=> CO2 + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.0E9, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(27100.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R13. CO2X is vdW CO2.""",
#	 metal = "Pt",
#)

entry(
    index = 14,
    label = "CX + OX <=> OCX + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.7E19, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R14""",
	metal = "Pt",
)

#endothermic - reverse of R14
#entry(
#    index = 15,
#    label = "OCX + Pt <=> CX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(3.7E15, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(236500, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R15""",
#	 metal = "Pt",
#)

#There is an error in the paper. This value is consistent with the file on the DETCHEM mechanisms website.
entry(
    index = 16,
    label = "OCX + OX <=> CO2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.7E21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(117600, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R16. CO2X is vdW CO2.
    The table in the paper pdf says 3.7e19, but the supplementary material has 3.7e21,
    which is apparently correct and the paper is wrong.
    """,
	metal = "Pt",
)


#endothermic - reverse of R16
#entry(
#    index = 17,
#    label = "CO2X + Pt <=> OCX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(3.7E15, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(173300, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R17. CO2X is vdW CO2.""",
#	 metal = "Pt",
#)

#endothermic - reverse of R19
#entry(
#    index = 18,
#    label = "OCX + HOX <=> CO2X + HX",
#    kinetics = SurfaceArrhenius(
#        A=(1.0E15, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(38700, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R18. CO2X is vdW CO2.""",
#	 metal = "Pt",
#)


entry(
    index = 19,
    label = "CO2X + HX <=> OCX + HOX",
    kinetics = SurfaceArrhenius(
        A=(1.0E19, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(8400, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R19. CO2X is vdW CO2.""",
	metal = "Pt",
)

#endothermic - reverse of R21
#entry(
#    index = 20,
#    label = "CH3X + Pt <=> CH2X + HX",
#    kinetics = SurfaceArrhenius(
#        A=(1.26E18, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(70300, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R20""",
#	 metal = "Pt",
#)

entry(
    index = 21,
    label = "CH2X + HX <=> CH3X + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.09E22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R21""",
	metal = "Pt",
)

#endothermic - reverse of R23
#entry(
#    index = 22,
#    label = "CH2X + Pt <=> CHX + HX",
#    kinetics = SurfaceArrhenius(
#        A=(7.31E18, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(58900, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R22""",
#	 metal = "Pt",
#)


entry(
    index = 23,
    label = "CHX + HX <=> CH2X + Pt",
    kinetics = SurfaceArrhenius(
        A=(3.09E22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R23""",
	metal = "Pt",
)

entry(
    index = 24,
    label = "CHX + Pt <=> CX + HX",
    kinetics = SurfaceArrhenius(
        A=(3.09E22, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R24""",
	metal = "Pt",
)

#endothermic - reverse of R24
#entry(
#    index = 25,
#    label = "CX + HX <=> CHX + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(1.25E18, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(138000, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R25""",
#	 metal = "Pt",
#)

entry(
    index = 26,
    label = "HX + OX <=> HOX + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.28E21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(11200, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R26""",
	metal = "Pt",
)

#endothermic - reverse of R26
#entry(
#    index = 27,
#    label = "HOX + Pt <=> HX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(7.39E15, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(77300, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R27""",
#	 metal = "Pt",
#)

#endothermic - reverse of R33
#entry(
#    index = 28,
#    label = "H2OX + Pt <=> HX + HOX",
#    kinetics = SurfaceArrhenius(
#        A=(1.15E15, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(101400, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R28. H2OX is vdW H2O.""",
#	 metal = "Pt",
#)

#endothermic - reverse of R30
#entry(
#    index = 29,
#    label = "HOX + HOX <=> H2OX + OX",
#    kinetics = SurfaceArrhenius(
#        A=(7.4E16, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(74000, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R29. H2OX is vdW H2O.""",
#	 metal = "Pt",
#)


entry(
    index = 30,
    label = "H2OX + OX <=> HOX + HOX",
    kinetics = SurfaceArrhenius(
        A=(1.0E20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(43100, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R30. H2OX is vdW H2O.""",
	metal = "Pt",
)



entry(
    index = 31,
    label = "H2 + CX <=> CH2X",
    kinetics = StickingCoefficient(
        A = 4.0E-2,
        n = 0,
        Ea=(29700, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R31""",
	metal = "Pt",
)

# - reverse of R31
#entry(
#    index = 32,
#    label = "CH2X <=> H2 + CX",
#    kinetics = SurfaceArrhenius(
#        A=(7.69E13, '1/s'),
#        n = 0,
#        Ea=(25100, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R32""",
#	 metal = "Pt",
#)

entry(
    index = 33,
    label = "HX + HOX <=> H2OX + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.04E21, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(66220, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R33. H2OX is vdW H2O.""",
	metal = "Pt",
)


#entry(
#    index = 34,
#    label = "CH3X + HX <=> CH4 + Pt + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(3.3E21, 'cm^2/(mol*s)'),
#        n = 0,
#        Ea=(50000, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R34""",
#	 metal = "Pt",
#)

#endothermic - reverse of R5
#entry(
#    index = 35,
#    label = "CH3X + H2OX <=> CH4 + HOX + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(3.7E17, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(110600, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R35. H2OX is vdW H2O.""",
#	 metal = "Pt",
#)

#endothermic - reverse of R4
#entry(
#    index = 36,
#    label = "CH3X + HOX <=> CH4 + OX + Pt",
#    kinetics = SurfaceArrhenius(
#        A=(3.7E17, 'm^2/(mol*s)'),
#        n = 0,
#        Ea=(87900, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R36""",
#	 metal = "Pt",
#)
