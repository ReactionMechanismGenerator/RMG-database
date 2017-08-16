#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = u""
longDesc = u"""
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 600,
    label = "N5d-OdOs;O_rad",
    kinetics = ArrheniusEP(
        A = (7e+12, 'cm^3/(mol*s)'),
        n = 0.24,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Experimental, J. Hahn, K. Luther and J. Troe""",
    longDesc = 
u"""
J. Hahn, K. Luther and J. Troe
Experimental and theoretical study of the temperature and pressure dependences of the recombination reactions O + NO2(+M)  NO3(+M) and NO2 + NO3(+M)  N2O5(+M)
Phys. Chem. Chem. Phys., 2000, 2, 5098-5104
DOI: 10.1039/B005756H

NO2 + O <=> NO3

Also appears in the Nitrogen_Glarborg_Zhang_et_al library (index 712)
and in the Nitrogen_Glarborg_Gimenez_et_al library (index 936)

The high-pressure limit kinetics was taken. Troe coefficients are:
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.5e+12, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.5e+20, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.71,
        T3 = (1e-30, 'K'),
        T1 = (1700, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),

Converted to training reaction from rate rule: N5d-OdOs;O_rad
""",
)

entry(
    index = 601,
    label = "N5d-OdOs;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""J. Troe""",
    longDesc = 
u"""
J. Troe
Analysis of the temperature and pressure dependence of the reaction HO + NO2 + M  HONO2 + M
International Journal of Chemical Kinetics, Volume 33, Issue 12 December 2001 Pages 878889
DOI: 10.1002/kin.10019

NO2 + OH <=> HONO2; T range: 50 to 1400 K, P range: 10E-4 to 10E3 bar

Also appears in the Nitrogen_Glarborg_Zhang_et_al library (index 713)
and in the Nitrogen_Glarborg_Gimenez_et_al library (index 937)

The high-pressure limit kinetics was taken. Troe coefficients are:
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.938e+25, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.4,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),

Converted to training reaction from rate rule: N5d-OdOs;O_pri_rad
""",
)

