#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.02E14, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(11.5, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
    Xu, Clayton, Balakotaiah, Harold et al.
    doi: 10.1016.j.apcatb.2007.08.008
"""
)

entry(
    index = 4,
    label = "HOCXO_1 + Ni_4 <=> OCX_3 + HOX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R4

metal = 'Ni'
"""
)

entry(
    index = 10,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.667E11, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(12.9139069, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 10 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 9,
    label = "NH2_X + Ni_4 <=> NHX_1 + HX_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (2.718e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (75.74, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH2 Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R9
    """
)

entry(
    index = 11,
    label = "NHX_2 + Ni_4 <=> NX + HX_5",
    kinetics = SurfaceArrhenius(
        A = (6.213e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (22.93, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R11
    """
)

entry(
    index = 16,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + Ni_4",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R16

metal = 'Ni'
"""
)


entry(
    index = 18,
    label = "CHX_3 + HX_5 <=> CH2X_1 + Ni_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R18

metal = 'Ni'
"""
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R20.
#entry(
#    index = 19,
#    label = "CHX_1 + Ni_4 <=> CX_3 + HX_5",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(9.88E16, 'm^2/(mol*s)'),
#        n = 0.5,
#        Ea=(21900.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    rank = 10,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R19
#
# metal = 'Cu'
#"""
#)

entry(
    index = 20,
    label = "CX_3 + HX_5 <=> CHX_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.70E20, 'm^2/(mol*s)'),
        n = -0.5,
        Ea=(157900., 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R20

metal = 'Ni'
"""
)

entry(
    index = 28,
    label = "HCOO* + Ni_4 <=> HCO* + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.570E12, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 28 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 31,
    label = "HCOH* + HX_5 <=> CH2OH* + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.698E12, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(54.4228933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 32 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 32,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R32

metal = 'Ni'
"""
)

entry(
    index = 15,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.193E13, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(38.7417207, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 15 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 36,
    label = "CH3O2* + Ni_4 <=> CH2OH*_2 + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(5.485E13, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(46.3517015, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 36 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 48,
    label = "CXHO_1 + Ni_4 <=> OCX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R8

metal = 'Ni'
"""
)

entry(
    index = 26,
    label = "OCX_3 + HX_5 <=> CXHO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(9.240E12, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(22.8299425, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 26 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)
