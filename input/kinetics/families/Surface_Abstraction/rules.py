#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Abstracting;Donating",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e15, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (80., 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"Arrhenius preexponential values for surface recombination...reactions are, in the SI system,... 10^13 - 10^14 m2/mol/s ...for bimolecular reactions"
from page 54 of "Silicon epitaxy"
Author:	Danilo Crippa; Daniel L Rode; Maurizio Masi
Publisher:	San Diego : Academic Press, 2001.
Series:	Semiconductors and semimetals, v. 72.

Ea made up.

CFG: I bumped the prefactor from E13 to E15. The Delgado mechanism has pre-exponential factors 
on the order of 1E17 for H abstraction. This rule is specific for non-H abstraction. 
There is no instance of non-H abstraction in Delgado, so I reduced it from 1E17 to 1E15. Completely arbitrary!
    """,
)

entry(
    index = 1,
    label = "Abstracting;R-H",
    kinetics = SurfaceArrheniusBEP(
        A = (5.0e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.0, #0.26
        E0 = (40.0, 'kJ/mol'), #34.3
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Made up""",
    longDesc = u"""
CFG increased the pre-exponential factor from 1E13, which is what we originally had, 
based upon the above citation, to 1E17, to bring it closer to the values in the 
Deutschmann_Ni (Delgado) mechanism
    """
)
