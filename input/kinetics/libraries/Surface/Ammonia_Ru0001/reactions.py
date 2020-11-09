#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ru0001"
shortDesc = u""
longDesc = u"""
Based primarily on "Ammonia synthesis over a Ru(0001) surface studied by density functional calculations"
https://doi.org/10.1016/S0021-9517(03)00156-8  and
"The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1
"""
entry(
    index = 1,
    label = " H2 + X + X <=> H_X + H_X ",
    kinetics = StickingCoefficient(
        A = 8.7E-1,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H adsorption""",
    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
    metal = 'Ru',
)

entry(
    index = 2,
    label = " N2 + X + X <=> N_X + N_X ",
    kinetics = StickingCoefficient(
        A = 6.3E-3,
        n = 0,
        Ea=(29.68, 'kJ/mol'), #7.1kcal/mol
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N adsorption""",
    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
    metal = 'Ru',
)

entry(
    index = 6,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A = 1.5E-4,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""ammonia adsorption""",
    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
    metal = 'Ru',
)

entry(
    index = 7,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(8.1E11, 'm^2/(mol*s)'),  #unit=-s
        n = 0.0,
        Ea = (73.99, 'kJ/mol'), #17.7.1kcal/mol
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
    metal = "Ru" ,
)

entry(
    index = 8,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(2E12, 'm^2/(mol*s)'),  #unit=-s
        n = 0.0,
        Ea = (85.27, 'kJ/mol'), #H coverage = 0.25, 20.4kcal/mol
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
    metal = "Ru" ,
)

entry(
    index = 9,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.9E12, 'm^2/(mol*s)'),  #unit=-s
        n = 0.0,
        Ea = (39.42, 'kJ/mol'), #H coverage = 0.25,N coverage = 0.25,  9.43kcal/mol
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
    metal = "Ru" ,
)

#Reverse of R1
#entry(
#    index = 10,
#    label = " H_X + H_X  <=>  H2 + X + X ",
#    kinetics = SurfaceArrhenius(
#        A=( 2.5E13 , 'm^2/(mol*s)'),   #unit=-s
#        n = 0.0,
#        Ea = (74.61, 'kJ/mol'),  #H coverage = 0.25
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""H desorption""",
#    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
#https://doi.org/10.1023/B:CATL.0000029523.22277.e1
#""",
#    metal = "Ru" ,
#)

#Reverse of R2
#entry(
#    index = 11,
#    label = " N_X + N_X  <=>  N2 + X + X ",
#    kinetics = SurfaceArrhenius(
#        A=( 1E15, 'm^2/(mol*s)'),   #unit=-s
#        n = 0.0,
#        Ea = ( 213.18 , 'kJ/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""N desorption""",
#    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
#https://doi.org/10.1023/B:CATL.0000029523.22277.e1
#""",
#    metal = "Ru" ,
#)


#Reverse of R6
#entry(
#    index = 15,
#    label = " NH3_X <=> NH3 + X ",
#    kinetics = SurfaceArrhenius(
#        A=(8.1E11, 'm^2/(mol*s)'),  #unit=-s
#        n = 0.0,
#        Ea = (73.99, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""ammonia desorption""",
#    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
#https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
#    metal = "Ru" ,
#)

#Reverse of R7
#entry(
#    index = 16,
#    label = " NH2_X + H_X <=> NH3_X + X ",
#    kinetics = SurfaceArrhenius(
#        A=(1.8E10, 'm^2/(mol*s)'),  #unit=-s
#        n = 0.0,
#        Ea = (46.19, 'kJ/mol'), #H coverage = 0.25
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
#https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
#    metal = "Ru" ,
#)

#Reverse of R8
#entry(
#    index = 17,
#    label = " NH_X + H_X <=> NH2_X + X ",
#    kinetics = SurfaceArrhenius(
#        A=(2E12, 'm^2/(mol*s)'),  #unit=-s
#        n = 0.0,
#        Ea = (64.06, 'kJ/mol'), #H coverage = 0.25
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
#https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
#    metal = "Ru" ,
#)

#Reverse of R9
#entry(
#    index = 18,
#    label = " N_X + H_X <=> NH_X + X ",
#    kinetics = SurfaceArrhenius(
#        A=(1.6E12, 'm^2/(mol*s)'),  #unit=-s
#        n = 0.0,
#        Ea = (154.56, 'kJ/mol'),  #H coverage = 0.25
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u""""The Role of Adsorbate–Adsorbate Interactions in the Rate Controlling Step and the Most Abundant Reaction Intermediate of NH3 Decomposition on Ru"
#https://doi.org/10.1023/B:CATL.0000029523.22277.e1""",
#    metal = "Ru" ,
#)