#!/usr/bin/env python
# encoding: utf-8

name = "HAN"
shortDesc = u""
longDesc = u"""
Reactions pertinent to the decomposition of HAN
"""

entry(
    index = 1,
    label = "NH4NO3 + X + X <=> N2O_X + H2O_X + H2O",
    kinetics = StickingCoefficient(
        A = 1.0e-6,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Ammonium Nitrate Adsorption decomposition""",
    longDesc = u"""
Currently modeling this as one step, adsorbs and breaks down immediately.
The pathway is insipred by Inazu et al. 2004.  http://dx.doi.org/10.1016/j.cattod.2004.06.055
Hopefully the reverse is calculated correctly, with there being a gas phase product.
Assume N2O_X is vdw-adsorbed (because "weakly bound", and I can't figure out a Lewis structure with bonds).
For the rate, just copied Deutschmann's dissociative adsorption of N2 from above, i.e.
a fixed sticking coefficient of 1e-6.
    """
)

entry(
    index = 2,
    label = "HAN + X <=> HAN_X",
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""HAN vdW adsorbing on the surface""",
    longDesc = u"""
    Deutchmann 2006 seems to have things vdW adsorbing with these sticking coefficients:
     H2O   0.75
     CO2   0.005
     CO    0.84 (not vdW)
     NH3   0.011   in 10.1016/j.ces.2011.07.007 on Ni

    I was about to put 0.01, but our vdW reaction family only
    has the top level estimate and that's currently 0.10, so 
    for consistency I have put that.
    """
)

entry( 
    index = 3,
    label = "HAN_Pd + X_Pd <=> HO_Pd + NH2O_Pd + HONO",
    kinetics = SurfaceArrhenius(
        A = (5e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(8.07, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""HONO elimination from HAN on Pd""",
    longDesc = u"""
    The "HONO elimaniton" pathway which is fastest on Pd(111) from Banerjee
    """
)

entry( 
    index = 4,
    label = "HAN_Ir <=> HO_Ir + NH2OH + NO2",
    kinetics = SurfaceArrhenius(
        A = (7.7e13, '1/s'),
        n = 0,
        Ea=(8.07, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NO2 elimination from HAN on Ir""",
    longDesc = u"""
    The "NO2 elimaniton" pathway which is fastest on Ir(111) from Banerjee.
    Their products look more like OX and NH3OH (and NO2) but then the NH3OH 
    needs a positive charge, and that can't work.  i.e. it's not clear 
    what hapens next from their "product" structure.

    The pre-exponential factor is based on CH2X <=> H2 + CX Deutchmann 2006
    """
)
