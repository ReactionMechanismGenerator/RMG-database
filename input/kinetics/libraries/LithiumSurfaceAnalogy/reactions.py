#!/usr/bin/env python
# encoding: utf-8

name = "LithiumSurfaceAnalogy"
shortDesc = u""
longDesc = u"""
Analogies to Reactions calculated with BEEF-vdW  on Libcc110 with Pynta
"""

#CFG: O2 is a special case: we need to treat it separately
# reverse of R10
# entry(
#     index = 1,
#     label = "LiOCOOCH2CH2X + LiOCOOCH2CH2X <=> LiOCOOCH2CH2CH2CH2OCOOLi + X + X",
#     kinetics = SurfaceArrhenius(A=(7.76425e-10,'m^2/(molecule*s)'), n=1.17184, Ea=(224.131,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
#                                 comment="""Fitted to 50 data points; dA = *|/ 1.05424, dn = +|- 0.00668821, dEa = +|- 0.0464584 kJ/mol"""),
#     shortDesc = u"""analogy to LiOCOOCH2CH2X + LiOCOOX <=> LiOCOOCH2CH2OCOOLi + X + X""",
#     longDesc = u"""""",
# 	metal = "Li",
# )

# entry(
#     index = 2,
#     label = "LiOCOOX + LiOCOOX <=> LiOCOOOCOOLi + X + X",
#     kinetics = SurfaceArrhenius(A=(7.76425e-10,'m^2/(molecule*s)'), n=1.17184, Ea=(224.131,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
#                                 comment="""Fitted to 50 data points; dA = *|/ 1.05424, dn = +|- 0.00668821, dEa = +|- 0.0464584 kJ/mol"""),
#     shortDesc = u"""analogy to LiOCOOCH2CH2X + LiOCOOX <=> LiOCOOCH2CH2OCOOLi + X + X""",
#     longDesc = u"""""",
# 	metal = "Li",
# )