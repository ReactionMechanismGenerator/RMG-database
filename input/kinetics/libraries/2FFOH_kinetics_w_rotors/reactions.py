#!/usr/bin/env python
# encoding: utf-8

name = "2BF_kinetics"
shortDesc = u""
longDesc = u"""ARC v1.1.0

Levels of theory used:

Conformers:       wb97xd/def2svp, software: gaussian (dft)
TS guesses:       wb97xd/def2svp, software: gaussian (dft)
Composite method: cbs-qb3, software: gaussian (composite) (using a fine grid)
Frequencies:      b3lyp/cbsb7, software: gaussian (dft)
Rotor scans:      b3lyp/cbsb7, software: gaussian (dft)
Using p-type bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local']}
"""

entry(
    index = 0,
    label = "R1_0 <=> P1_0",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.62154e-05,'s^-1'), n=4.70143, Ea=(287.679,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in R1 <=> P1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.27858200   -1.77788100    0.91217300
C      -1.34788200   -0.48869800    0.47735300
C      -0.40975200    0.52437200    0.84203200
C       0.99275000    0.22394700    0.72324900
C       1.32390500    0.62871600   -0.54582300
C       0.12124400    1.16877100   -1.11193900
O      -0.68701600    1.55928200   -0.05629000
H      -0.35154600   -2.01966600    1.02578300
H      -2.37774400   -0.19949000    0.29341400
H       1.57891300   -0.38234600    1.39863200
H       2.24841700    0.46466700   -1.07971000
H       0.07146700    1.79291600   -1.99725600
H      -0.75551500   -0.19467800   -0.96516200

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [8, 1, 2, 3], invalidation reason: Another conformer for TS0 exists which is 4.39 kJ/mol lower.
""",
)

