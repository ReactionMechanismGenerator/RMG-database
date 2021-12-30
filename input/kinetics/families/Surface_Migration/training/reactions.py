#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

# entry(
#     index = 1,
#     label = "*nbutane <=> *nbutane2",
#     degeneracy = 4,
#     kinetics = SurfaceArrhenius(
#         A = (1e13, 's^-1'),
#         n = 0.,
#         Ea = (59.33, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""n-butane migration from C1 to C2""",
#     longDesc = u"""
# From Xu et al. Doi:10.1021/acscatal.7b03205
# Paper assumes 1e13 for A and fits Ea to experimental data
# """,
#     metal = "Co",
# )

# entry(
#     index = 2,
#     label = "*nhexane <=> *nhexane2",
#     degeneracy = 4,
#     kinetics = SurfaceArrhenius(
#         A = (1e13, 's^-1'),
#         n = 0.,
#         Ea = (58.93, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""n-hexane migration from C1 to C2""",
#     longDesc = u"""
# From Xu et al. Doi:10.1021/acscatal.7b03205
# Paper assumes 1e13 for A and fits Ea to experimental data
# """,
#     metal = "Co",
# )

# entry(
#     index = 3,
#     label = "*noctane <=> *noctane2",
#     degeneracy = 4,
#     kinetics = SurfaceArrhenius(
#         A = (1e13, 's^-1'),
#         n = 0.,
#         Ea = (63.31, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""n-octane migration from C1 to C2""",
#     longDesc = u"""
# From Xu et al. Doi:10.1021/acscatal.7b03205
# Paper assumes 1e13 for A and fits Ea to experimental data
# """,
#     metal = "Co",
# )
