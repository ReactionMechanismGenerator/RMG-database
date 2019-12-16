#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_beta/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (6.335e16, 'm^2/(mol*s)'),
        n = 1,
        alpha = 0.26,
        E0 = (73.3286, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"Just imaginary values for this family. A literature research is necessary to populate this family.
BEP relation for O-H bond scission in J. Sutton, D. Vlachos, Ethanol Activation on Closed-Packed Surfaces, Ind. Eng. Chem. Res., 2015, 54
Added by B.K., Comment: I'm not sure if this is relation is valid for the O-H bond fission, when the O atom is in the beta position. Ethanol or alcohol intermediates tend to bind through the oxygen atom. It was not clear in the paper, if this is always the case, but it was mentioned for ethanol. 

E0 and alpha are taken from: Table 5, for all metals, the value for A is just a guess.
"
"""
)



