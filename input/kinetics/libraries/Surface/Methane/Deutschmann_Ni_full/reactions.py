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

#skip R2

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
#skip R5 vdW
#skip R6 vdW
#skip R7 vdW
#skip R8 vdW

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
#skip R11 vdW
#skip R12 vdW
#skip R13

#entry(
#    index = 7,
#    label = "CH4 + Ni + Ni <=> CH3X + HX",
#    kinetics = StickingCoefficient(
#        A = 8.0E-3,
#        n = 0,
#        Ea=(0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""R11. Deutschmann actually has physisorbed ch4 going to ch3 + h""",
#	 metal = "Ni",
#)

#CFG: Modified version of R14: reverse of dissociative adsorption
#since vdW is not yet functioning, we include this reaction in library
entry(
    index = 14,
    label = "CH3X + HX <=> CH4 + Ni + Ni",
    kinetics = SurfaceArrhenius(
        A=(1.44E18, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(63400.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R14. Deutschmann actually uses vdW CH4 as product, but we skip it and this reaction as the reverse of our adsorption step""",
	metal = "Ni",
)

#skip R15

entry(
    index = 16,
    label = "CH2X + HX <=> CH3X + Ni",
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R16""",
	metal = "Ni",
)

#skip R17

entry(
    index = 18,
    label = "CHX + HX <=> CH2X + Ni",
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R18""",
	metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R20.
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

entry(
    index = 20,
    label = "CX + HX <=> CHX + Ni",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.70E20, 'm^2/(mol*s)'),
        n = -0.5,
        Ea=(157900., 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R20
""",
	metal = "Ni",
)
#skip R21

entry(
    index = 22,
    label = "CH3X + HOX <=> CH4 + OX + Ni",
    kinetics = SurfaceArrhenius(
        A=(2.98E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(25800.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R22. Deutschmann actually goes to vdW CH4, but we'll skip that. We input reverse direction""",
	metal = "Ni",
)

#skip R23

entry(
    index = 24,
    label = "CH2X + HOX <=> CH3X + OX",
    kinetics = SurfaceArrhenius(
        A=(1.39E17, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(19000.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R24""",
	metal = "Ni",
)

#skip R25

entry(
    index = 26,
    label = "CHX + HOX <=> CH2X + OX",
    kinetics = SurfaceArrhenius(
        A=(4.40E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(42400.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R26""",
	metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R28.
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

entry(
    index = 28,
    label = "HOX + CX <=> OX + CHX ",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.43E17, 'm^2/(mol*s)'),
        n = -0.312,
        Ea=(118900.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    #rank = 3,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
	metal = "Ni",
)
#skip R29 vdW


entry(
    index = 30,
    label = "HX + HOX <=> H2O + Ni + Ni",
    kinetics = SurfaceArrhenius(
        A=(1.85E16, 'm^2/(mol*s)'),
        n = 0.086,
        Ea=(41500.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R30. Deutschmann actually goes to vdW H2O, but we'll skip that. We input reverse direction""",
	metal = "Ni",
)

#skip R31

entry(
    index = 32,
    label = "HOX + Ni <=> HX + OX",
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R32""",
	metal = "Ni",
)

entry(
    index = 33,
    label = "HOX + HOX <=> H2O + OX + Ni",
    kinetics = SurfaceArrhenius(
        A=(2.34E16, 'm^2/(mol*s)'),
        n = 0.274,
        Ea=(92300.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R33""",
	metal = "Ni",
)

#skip R34 vdW
#skip R35

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

entry(
    index = 39,
    label = "OCX + OCX <=> CO2 + Ni + CX",
    kinetics = SurfaceArrhenius(
        A=(1.62E10, 'm^2/(mol*s)'),
        n = 0.5,
        Ea=(241700.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R39 is used instead of R40 to avoid having CO2(s) as reactant""",
	metal = "Ni",
)

#skip R40

entry(
    index = 41,
    label = "OCX + OX <=> CO2 + Ni + Ni",
    kinetics = SurfaceArrhenius(
        A=(2.00E15, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(123600.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R41. Deutschmann actually uses vdW CO2, but we skip it and use reverse reaction""",
	metal = "Ni",
)


#skip R42
#skip R43

entry(
    index = 44,
    label = "HOCXO + Ni <=> OCX + HOX",
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R44""",
	metal = "Ni",
)

#skip R45

entry(
    index = 46,
    label = "HOCXO + Ni <=> CO2 + HX + Ni",
    kinetics = SurfaceArrhenius(
        A=(3.73E16, 'm^2/(mol*s)'),
        n = 0.475,
        Ea=(33600.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R46""",
	metal = "Ni",
)


#skip R47

entry(
    index = 48,
    label = "CXHO + Ni <=> OCX + HX",
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R48""",
	metal = "Ni",
)

#skip R49

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




# CFG: I removed this reaction and replaced it with a forbidden structure in the Surface_Adsorption_Single group.
#entry(
#    index = 3,
#    label = "O2 + Ni <=> O2X",
#    kinetics = StickingCoefficient(
#        A = 0.0,
#        n = 0,
#        Ea=(0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""Prevent O2 non-dissociative adsorption""",
#	 metal = "Ni",
# )
