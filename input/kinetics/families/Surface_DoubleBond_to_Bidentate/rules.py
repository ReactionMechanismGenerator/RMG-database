#!/usr/bin/env python
# encoding: utf-8

name = "Surface_DoubleBond_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (4.27e15, 'm^2/(mol*s)'),
        n = 0.549,
        alpha = 0,
        E0 = (1.0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Pre-exponential value, n and E0 are from R31 in Table 1 of "A Catalytic Reaction Mechanism for Methane
Partial Oxidation at Short ContactTimes, Reforming, and Combustion, and
for Oxygenate Decomposition and Oxidation on Platinum"
Authors:  A.B. Mhadeshwar and D.G. Vlachos
doi:10.1021/ie070322c

Pre-exponential factor from paper / surface site density of Pt
1.06e11 1/s / 2.483e-5 mol/m2 = 4.27e15 m2/(mol*s)

The reaction R31 is
   COOH* + *  -> CO2* + H*
They report a nonlinear dependence of the activation energy on specific coverage (of H*)
and temperature, but don't say what this dependence is.
Note that this reaction is not in fact an example of this reaction family!
The products have dissocated and are not the bidentate COOH** (or CHOO**).
However, in the absence of better data, it is currently our best estimate. (KB, CFG, RHW, 2020-11-30).
"""
)



