#!/usr/bin/env python
# encoding: utf-8

#This libraries need to add more data of Cu_SSZ_13
name = "Ammonia_Cu_SSZ_13"
shortDesc = u""
longDesc = u"""
Based primarily on "New insights into the mechanism of NH3-SCR over Cu- and Fe-zeolite catalyst: 
Apparent negative activation energy at high temperature and catalyst unit design consequences"
https://doi.org/10.1016/j.apcatb.2017.12.076
And based on "Combined experimental and kinetic modeling study of the bi-modal NOx conversion profile 
on commercial Cu-SAPO-34 catalyst under standard SCR conditions"
https://doi.org/10.1016/j.apcatb.2014.09.060
"""
#NH3 adsorption on Cu_SSZ_13
entry(
    index = 1,
    label = " NH3 + X <=>  NH3_X ",
    kinetics = StickingCoefficient(
        A=3.2189E10,
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
S.Y. Joshi, A. Kumar, J. Luo, K. Kamasamudram, N.W. Currier, A. Yezerets
"New insights into the mechanism of NH3-SCR over Cu- and Fe-zeolite catalyst:
apparent negative activation energy at high temperature and catalyst unit design consequences"
Appl. Catal. B Environ., 226 (2018), pp. 565-574
""",
    metal = "Cu" ,
)

#Reverse reaction of index = 1, NH3 desorption on Cu_SSZ_13
#Need to think about the A, 7.8376E27...very large?
#entry(
#    index = 2,
#    label = " NH3_X <=>  NH3 + X ",
#    kinetics = StickingCoefficient(
#        A=7.8376E27,
#        n = 0.,
#        Ea = (128, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#S.Y. Joshi, A. Kumar, J. Luo, K. Kamasamudram, N.W. Currier, A. Yezerets
#"New insights into the mechanism of NH3-SCR over Cu- and Fe-zeolite catalyst:
#apparent negative activation energy at high temperature and catalyst unit design consequences"
#Appl. Catal. B Environ., 226 (2018), pp. 565-574
#""",
#    metal = "Cu" ,
#)

#NO2 oxidation
entry(
    index = 3,
    label = " NO + O <=> NO2 ",
    kinetics = SurfaceArrhenius( #Not Sure
        A=(6.9229E21, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (68, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
S.Y. Joshi, A. Kumar, J. Luo, K. Kamasamudram, N.W. Currier, A. Yezerets
Combined experimental and kinetic modeling study of the bi-modal NOx conversion profile on commercial Cu-SAPO-34 catalyst under standard SCR conditions
Appl. Catal., B, 165 (2015), pp. 27-35
""",
    metal = "Cu" ,
)