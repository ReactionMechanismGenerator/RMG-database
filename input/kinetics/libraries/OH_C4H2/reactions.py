#!/usr/bin/env python
# encoding: utf-8

name = "OH_C4H2"
shortDesc = u"level of theory: UB3LYP/6-311++G(d,p) for geometry, RQCISD(T) and two basis set extrapolation schemes for energy, internal rotors were considered"
longDesc = u"""
Kinetics from: Oxidation pathways in the reaction of diacetylene with OH radicals, 2007
The high pressure limit rate for initial addition
"""
entry(
    index = 1,
    label = "OH + C4H2 <=> C4H3O",
    degeneracy = 2,
    kinetics = MultiArrhenius(
                arrhenius = [
                    Arrhenius(
                        A = (2.758e+14, 'cm^3/(mol*s)'),
                        n = -0.39,
                        Ea = (20853, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.613e+12, 'cm^3/(mol*s)'),
                        n = 0.06,
                        Ea = (-1156, 'J/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
	    ),
)

