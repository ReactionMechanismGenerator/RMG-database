#!/usr/bin/env python
# encoding: utf-8

name = "LithiumSurface"
shortDesc = u""
longDesc = u"""
Reactions calculated with BEEF-vdW  on Libcc110 with Pynta
"""


# entry(
#     index = 1,
#     label = "NCCH3 + X + X <=> CH3X + NCX",
#     kinetics = SurfaceArrhenius(A=(7.21071e-50,'m^5/(molecules^2*s)'), n=2.61372, Ea=(-81.9951,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), 
#                                 Tmax=(2500,'K'), 
#                                 comment="""Fitted to 50 data points; dA = *|/ 1.09361, dn = +|- 0.0113301, dEa = +|- 0.0787021 kJ/mol"""),
#     shortDesc = u"""""",
#     longDesc = u"""""",
# 	metal = "Li",
#     facet = "110",
# )

# entry(
#     index = 2,
#     label = "NCCH3 + X + X <=> HX + CH2CNX",
#     kinetics = SurfaceArrhenius(A=(2.07084e-51,'m^5/(molecules^2*s)'), n=3.09905, Ea=(-37.6145,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
#                                 comment="""Fitted to 50 data points; dA = *|/ 1.1121, dn = +|- 0.0134532, dEa = +|- 0.0934501 kJ/mol"""),
#     shortDesc = u"""note this was not a target reaction NCCH3 + Li + Li => HX + NCCH2X was targetted and resulting in three TSs for this reaction""",
#     longDesc = u"""""",
# 	metal = "Li",
#     facet = "110",
# )

entry(
    index = 3,
    label = "LiOCOOCH2CH2X <=> CO2 + LiOCH2CH2X",
    kinetics = SurfaceArrhenius(A=(2.66452e+11,'s^-1'), n=1.27462, Ea=(70.1461,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
                                comment="""Fitted to 50 data points; dA = *|/ 1.11209, dn = +|- 0.0134516, dEa = +|- 0.0934388 kJ/mol"""),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Li",
    facet = "110",
)

entry(
    index = 4,
    label = "LiOCOOCH2CH2X + X <=> C2H4 + LiOCOOX + X",
    kinetics = SurfaceArrhenius(A=(3.5183e-07,'m^2/(molecule*s)'), n=0.128046, Ea=(-11.0304,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
                                comment="""Fitted to 50 data points; dA = *|/ 1.05314, dn = +|- 0.00655564, dEa = +|- 0.0455374 kJ/mol"""),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Li",
    facet = "110",
)

entry(
    index = 5,
    label = "LiOCOOX + X <=> CO2 + LiOX + X",
    kinetics = SurfaceArrhenius(A=(3.5183e-07,'m^2/(molecule*s)'), n=0.128046, Ea=(-11.0304,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
                                comment="""Fitted to 50 data points; dA = *|/ 1.05314, dn = +|- 0.00655564, dEa = +|- 0.0455374 kJ/mol"""),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Li",
    facet = "110",
)

# entry(
#     index = 6,
#     label = "LiOCOOCH2CH2X + LiOCOOX <=> LiOCOOCH2CH2OCOOLi + X + X",
#     kinetics = SurfaceArrhenius(A=(7.76425e-10,'m^2/(molecule*s)'), n=1.17184, Ea=(224.131,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
#                                 comment="""Fitted to 50 data points; dA = *|/ 1.05424, dn = +|- 0.00668821, dEa = +|- 0.0464584 kJ/mol"""),
#     shortDesc = u"""""",
#     longDesc = u"""""",
# 	metal = "Li",
#     facet = "110",
# )

entry(
    index = 7,
    label = "XOCOOX <=> CO2 + OX + X",
    kinetics = SurfaceArrhenius(A=(1.10312e+12,'s^-1'), n=0.682037, Ea=(95.3188,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
                                comment="""Fitted to 50 data points; dA = *|/ 1.2104, dn = +|- 0.0241775, dEa = +|- 0.167944 kJ/mol"""),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Li",
    facet = "110",
)

entry(
    index = 8,
    label = "LiNCCH3X + X <=> LiNX + CH3CX",
    kinetics = SurfaceArrhenius(A=(7.71978e-11,'m^2/(molecule*s)'), n=1.32625, Ea=(170.986,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), 
                                comment="""Fitted to 50 data points; dA = *|/ 1.03899, dn = +|- 0.00484281, dEa = +|- 0.0336396 kJ/mol"""),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Li",
    facet = "110",
)