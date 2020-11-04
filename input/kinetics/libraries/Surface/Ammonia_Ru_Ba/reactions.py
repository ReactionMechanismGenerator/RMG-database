#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ru_Ba"
shortDesc = u""
longDesc = u"""
Based primarily on "Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia
Supports for Ammonia Synthesis"
https://pubs.acs.org/doi/pdf/10.1021/acssuschemeng.9b04929
"""

entry(
    index = 1,
    label = " N2 + X + X <=>  N_X + N_X ",
    kinetics = StickingCoefficient(
        A=2.892E-10,   #2.892x10^-6 cm/s
        n = 0.,
        Ea = (38.949, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
""",
     metal = "Ru" ,
)

#Reverse reaction of index = 1
#entry(
#    index = 2,
#    label = " N_X + N_X  <=> X + X + N2 ",
#    kinetics = SurfaceArrhenius(
#        A=(2.015E13, 'm^2/(mol*s)'),   #2.015x10^17 cm/s
#        n = -0.279,
#        Ea = (134.027, 'kJ/mol'),  #148.027 - 14(N-Ru)
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
#Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
#ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
#""",
#     metal = "Ru" ,
#)

entry(
    index = 3,
    label = " H2 + X + X <=> H_X + H_X ",
    kinetics = StickingCoefficient(
        A=4.007E-7,    #4.007x10^-3cm/s
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
""",
    metal = "Ru" ,
)

#Reverse reaction of index = 3
#entry(
#    index = 4,
#    label = " H_X + H_X <=> H2 + X + X ",
#    kinetics = SurfaceArrhenius(
#        A=(3.6E16, 'm^2/(mol*s)'),   #3.6x10^20cm/s
#        n = 0.658,
#        Ea = (89.948, 'kJ/mol'),  #91.948 - 2(H_Ru)
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
#Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
#ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
#""",
#    metal = "Ru" ,
#)

entry(
    index = 5,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A=1.247E-9,    #1.247x10^-5cm/s
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
""",
    metal = "Ru" ,
)
#need to think about A in index= 5, looks like the value is very different than other literature.

#Reverse reaction of index = 5
#entry(
#    index = 6,
#    label = " NH3_X <=> NH3 + X ",
#    kinetics = SurfaceArrhenius(
#        A=(2.235E7, 'm^2/(mol*s)'),    #2.235x10^11cm/s
#        n = 0.083,
#        Ea = (83.536, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
#Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
#ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
#""",
#    metal = "Ru" ,
#)

entry(
    index = 7,
    label = " N_X + H_X <=> NH_X + X ",
    kinetics = SurfaceArrhenius(
        A=(8.424E16, 'm^2/(mol*s)'), #8.424x10^20cm/s
        n = 0.,
        Ea = (77.62, 'kJ/mol'),  #83.620 - 7(N-Ru)
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
""",
    metal = "Ru" ,
)

#Reverse reaction of index = 7
#entry(
#    index = 8,
#    label = " NH_X + X <=> N_X + H_X ",
#    kinetics = SurfaceArrhenius(
#        A=(6.813E15, 'm^2/(mol*s)'),   #6.813x10^19cm/s
#        n = 0.207,
#        Ea = (31.972, 'kJ/mol'),  #30.972 + 1(H-Ru)
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
#Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
#ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
#""",
#    metal = "Ru" ,
#)

entry(
    index = 9,
    label = " NH_X + H_X <=> NH2_X + X ",
    kinetics = SurfaceArrhenius(
        A=(4.949E15, 'm^2/(mol*s)'),  #4.949x10^19cm/s
        n = 0.083,
        Ea = (75.236, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
""",
    metal = "Ru" ,
)

#Reverse reaction of index = 9
#entry(
#    index = 10,
#    label = " NH2_X + X <=> NH_X + H_X ",
#    kinetics = SurfaceArrhenius(
#        A=(8.321E15, 'm^2/(mol*s)'), 8.321x10^19cm/s
#        n = -0.083,
#        Ea = (16.767, 'kJ/mol'), #15.767 + 1(H-Ru)
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
#Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
#ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
#""",
#    metal = "Ru" ,
#)

entry(
    index = 11,
    label = " NH2_X + H_X <=> NH3_X + X ",
    kinetics = SurfaceArrhenius(
        A=(3.886E15, 'm^2/(mol*s)'),   #3.886x10^19cm/s
        n = 0.083,
        Ea = (17.036, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
""",
    metal = "Ru" ,
)

#Reverse reaction of index = 11
#entry(
#    index = 12,
#    label = " NH3_X + X <=> NH2_X + H_X ",
#    kinetics = SurfaceArrhenius(
#        A=(1.478E16, 'm^2/(mol*s)'),   #1.478x10^20cm/s
#        n = 0.,
#        Ea = (65.98, 'kJ/mol'),  #64.98 + 1(H-Ru)
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Barium-Promoted Ruthenium Catalysts on Yittria-Stabilized Zirconia Supports for Ammonia Synthesis"
#Zhenyu Zhang, Canan Karakaya, Robert J. Kee, J. Douglas Way, and Colin A. Wolden
#ACS Sustainable Chemistry & Engineering 2019 7 (21), 18038-18047
#""",
#     metal = "Ru" ,
#)
