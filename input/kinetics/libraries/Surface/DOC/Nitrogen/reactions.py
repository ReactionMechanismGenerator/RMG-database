#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen"
shortDesc = u""
longDesc = u"""
Nitrogen surface reactions that are too specific to make families for.
"""

entry(
    index = 2,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 0.011,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NH3 Surface Adsorption vdW""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R2
    """,
    metal = 'Ni',
)

entry(
    index = 3,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 1.0e-6,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Adsorption Dissociative""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R3
    """,
    metal = 'Ni',
)

#Reverse reaction of index = 3
# entry(
#     index = 4,
#     label = "N_X + N_X <=> N2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.7e21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (113.9, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#         coverage_dependence = {'CO_X': {'a':0.0, 'm':0.0, 'E':(-75, 'kJ/mol')}},
#     ),
#     shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
#     longDesc = """
# Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
# Deutschmann et al. (2009)
# doi:10.1016/j.apcatb.2009.05.006
# """,
#     metal = "Pt",
# )

entry(
    index = 51,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (5e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(107.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NO Dissociation""",
    longDesc = u"""
    Detailed surface reaction mechanism in a three-way catalyst
    Chatterjee, Deutschmann, Warnatz et al.
    doi: 10.1039/b101968f

    is supposedly only valid for a Pt/Rh ratio of 75%/25%

    This is R51
    """,
    metal = 'Pt',
)

#Reverse reaction of index = 51
# entry(
#     index = 5,
#     label = "N_X + O_X <=> NO_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (1e21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (122.6, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#         coverage_dependence = {'O_X': {'a':0.0, 'm':0.0, 'E':(-60, 'kJ/mol')}},
#     ),
#     shortDesc = u"""Nitrogen/51""",
#     longDesc = """
#   Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
#   Deutschmann et al. (2009)
#   doi:10.1016/j.apcatb.2009.05.006
#   """,
#     metal = "Pt",
# )

entry(
    index = 6,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = 0.85,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 6
# entry(
#     index = 7,
#     label = "NO_X <=> NO + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.1e12, '1/s'),  
#         n = 0.0,
#         Ea = (80.7, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = """
#   Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
#   Deutschmann et al. (2009)
#   doi:10.1016/j.apcatb.2009.05.006
#   """,
#     metal = "Pt",
# )

entry(
    index = 8,
    label = "NO2 + X <=> NO2_X",
    kinetics = StickingCoefficient(
        A = 0.9,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 8
# entry(
#     index = 9,
#     label = "NO2_X <=> NO2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.4e13, '1/s'),  
#         n = 0.0,
#         Ea = (61, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )

entry(
    index = 10,
    label = "N2O + X <=> N2O_X",
    kinetics = StickingCoefficient(
        A = 0.025,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 10
# entry(
#     index = 11,
#     label = "N2O_X <=> N2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.2e10, '1/s'),  
#         n = 0.0,
#         Ea = (0.7, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )

#Reverse reaction of index = 13
# entry(
#     index = 12,
#     label = "O_X + NO <=> NO2_X",
#     kinetics = SurfaceArrhenius(
#         A = (2e13, 'cm^3/(mol*s)'),
#         n = 0.0,
#         Ea = (111.3, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#         coverage_dependence = {'CO_X': {'a':0.0, 'm':0.0, 'E':(75, 'kJ/mol')},
#                                'O_X': {'a':0.0, 'm':0.0, 'E':(-60, 'kJ/mol')}},
#     ),
#     shortDesc = u"""""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )

entry(
    index = 13,
    label = "NO2_X <=> O_X + NO",
    kinetics = SurfaceArrhenius(
        A = (3.3e14, '1/s'),  
        n = 0.0,
        Ea = (115.5, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (1e21, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (90.9, 'kJ/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 14
# entry(
#     index = 15,
#     label = "N2O_X + X <=> N_X + NO_X",
#     kinetics = SurfaceArrhenius(
#         A = (2.9e24, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (133.1, 'kJ/mol'), 
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )

entry(
    index = 16,
    label = "NO_X + O_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.3e17, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (133, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        coverage_dependence = {'CO_X': {'a':0.0, 'm':0.0, 'E':(75, 'kJ/mol')}},
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 16
# entry(
#     index = 17,
#     label = "NO2_X + X <=> NO_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (8.1e18, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (58, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )

entry(
    index = 18,
    label = "NO_X + H_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.2e21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (25, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 18
# entry(
#     index = 19,
#     label = "N_X + OH_X <=> NO_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.4e21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (99, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )

entry(
    index = 20,
    label = "NO2_X + H_X <=> NO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.9e21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (20, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

#Reverse reaction of index = 20
# entry(
#     index = 21,
#     label = "NO_X + OH_X <=> NO2_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.1e22, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (175.3, 'kJ/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = """
    # Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    # Deutschmann et al. (2009)
    # doi:10.1016/j.apcatb.2009.05.006
    # """,
#     metal = "Pt",
# )
