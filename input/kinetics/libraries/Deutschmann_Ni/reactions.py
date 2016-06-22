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
    longDesc = u"""R1"""
)


entry(
    index = 2,
    label = "O2 + Ni + Ni <=> OX + OX",
    kinetics = StickingCoefficient(
        A = 4.36E-2,
        n = -0.206,
        Ea=(1.5E3, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R3"""
)


entry(
    index = 3,
    label = "O2 + Ni <=> O2X",
    kinetics = StickingCoefficient(
        A = 0.0,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Prevent O2 non-dissociative adsorption"""
)


entry(
    index = 4,
    label = "HX + HOX <=> H2O + Ni + Ni",
    kinetics = SurfaceArrhenius(
        A=(1.85E16, 'm^2/(mol*s)'),
        n = 0.086,
        Ea=(41500.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R30. Deutschmann actually goes to vdW H2O, but we'll skip that. We input reverse direction"""
)



entry(
    index = 5,
    label = "OCX + OX <=> CO2 + Ni + Ni",
    kinetics = SurfaceArrhenius(
        A=(2.00E15, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(123600.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R41. Deutschmann actually uses vdW CO2, but we skip it and use reverse reaction"""
)

entry(
    index = 6,
    label = "CO + Ni <=> OCX",
    kinetics = StickingCoefficient(
        A = 5.0E-1,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R9 """
)

entry(
    index = 7,
    label = "CH4 + Ni + Ni <=> CH3X + HX",
    kinetics = StickingCoefficient(
        A = 8.0E-3,
        n = 0,
        Ea=(0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R11. Deutschmann actually has physisorbed ch4 going to ch3 + h"""
)

entry(
    index = 8,
    label = "CH2X + HX <=> CH3X + Ni",
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R16"""
)

entry(
    index = 9,
    label = "CHX + HX <=> CH2X + Ni",
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R18"""
)

entry(
    index = 10,
    label = "CHX + Ni <=> CX + HX",
    kinetics = SurfaceArrhenius(
        A=(9.88E16, 'm^2/(mol*s)'),
        n = 0.5,
        Ea=(21900.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R19"""
)

entry(
    index = 11,
    label = "CH3X + HOX <=> CH4 + OX + Ni",
    kinetics = SurfaceArrhenius(
        A=(2.98E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(25800.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R22. Deutschmann actually goes to vdW CH4, but we'll skip that. We input reverse direction"""
)

entry(
    index = 12,
    label = "CH2X + HOX <=> CH3X + OX",
    kinetics = SurfaceArrhenius(
        A=(1.39E17, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(19000.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R24"""
)


entry(
    index = 13,
    label = "CHX + HOX <=> CH2X + OX",
    kinetics = SurfaceArrhenius(
        A=(4.40E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(42400.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R26"""
)

entry(
    index = 14,
    label = "CHX + OX <=> CX + HOX",
    kinetics = SurfaceArrhenius(
        A=(2.47E17, 'm^2/(mol*s)'),
        n = 0.312,
        Ea=(57700.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R27"""
)


entry(
    index = 15,
    label = "HOX + Ni <=> HX + OX",
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R32"""
)


entry(
    index = 16,
    label = "HOX + HOX <=> H2O + OX + Ni",
    kinetics = SurfaceArrhenius(
        A=(2.34E16, 'm^2/(mol*s)'),
        n = 0.274,
        Ea=(92300.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R33"""
)

#entry(
#    index = 17,
#    label = "CO2 + Ni + Ni <=> OCXOX",
#    kinetics = StickingCoefficient(
#        A = 0.0,
#        n = 0.0,
#        Ea=(0.0, 'J/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""TEST TO PREVENT BIDENTATE"""
#)



entry(
    index = 17,
    label = "OCX + Ni <=> CX + OX",
    kinetics = SurfaceArrhenius(
        A=(1.75E9, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(116200.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R36"""
)



entry(
    index = 18,
    label = "CX + HOX <=> HX + OCX",
    kinetics = SurfaceArrhenius(
        A=(3.88E21, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(62500.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R38"""
)


entry(
    index = 19,
    label = "CO2 + Ni + CX <=> OCX + OCX",
    kinetics = SurfaceArrhenius(
        A=(7.29E24, 'm^2/(mol*s)'),
        n = -0.55,
        Ea=(239200.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R38"""
)


entry(
    index = 20,
    label = "HOCXO + Ni <=> OCX + HOX",
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R44"""
)


entry(
    index = 21,
    label = "HOCXO + Ni <=> CO2 + HX + Ni",
    kinetics = SurfaceArrhenius(
        A=(3.73E16, 'm^2/(mol*s)'),
        n = 0.475,
        Ea=(33600.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R46"""
)


entry(
    index = 22,
    label = "CXHO + Ni <=> OCX + HX",
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R48"""
)

entry(
    index = 23,
    label = "CHX + OX <=> CXHO + Ni",
    kinetics = SurfaceArrhenius(
        A=(4.59E16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(109900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R50"""
)


entry(
    index = 24,
    label = "CXHO + HOX <=> HOCXO + HX",
    kinetics = SurfaceArrhenius(
        A=(2.28E16, 'm^2/(mol*s)'),
        n = 0.263,
        Ea=(15900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R50"""
)


