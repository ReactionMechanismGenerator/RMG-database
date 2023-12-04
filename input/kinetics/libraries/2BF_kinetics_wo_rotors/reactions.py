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
    label = "R1_44 + R2_44 <=> P1_44 + P2_44",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5.95314e-05,'cm^3/(mol*s)'), n=4.90414, Ea=(32.576,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS1 in s46_CH3 + s14_2BF <=> s47_CH4 + s12_2BF_radical_0:
Methods that successfully generated a TS guess:
heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,autotst,autotst,autotst,autotst,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       0.51807500    3.30898900   -0.64164200
H      -0.50754600    3.31685500   -1.00384600
H       1.07739000    4.20094200   -0.91434100
H       0.60968500    3.04453300    0.40899100
O      -0.73188900   -1.80890000    0.78449800
C       0.47044900   -0.74819800   -1.78028100
C       1.76071600   -0.00413600   -1.40460100
C      -0.81208400   -0.24724300   -1.08286500
C       1.89026700    1.39637400   -1.97609200
C      -0.84531900   -0.50239700    0.38661300
C      -0.98632000    0.29263000    1.48340500
C      -0.96027800   -0.57092800    2.62925500
C      -0.80325800   -1.82865300    2.14765900
H       1.86934700    0.02387700   -0.31361200
H       2.60939700   -0.60165200   -1.76640400
H       0.58908200   -1.81044000   -1.54744700
H       0.32352200   -0.68340400   -2.86463200
H      -1.67364000   -0.74238600   -1.54737700
H      -0.94527500    0.82495800   -1.24311200
H       1.15488600    2.28369900   -1.31891000
H       2.88531000    1.82764600   -1.85438100
H       1.55066000    1.49650100   -3.00973500
H      -1.10303800    1.36455300    1.47713600
H      -1.04639900   -0.28720800    3.66615900
H      -0.72597600   -2.79923400    2.60735300

1D rotors:
* Invalidated! pivots: [6, 7], dihedral: [8, 6, 7, 9], invalidation reason: 
* Invalidated! pivots: [6, 8], dihedral: [7, 6, 8, 10], invalidation reason: 
* Invalidated! pivots: [7, 9], dihedral: [6, 7, 9, 20], invalidation reason: 
* Invalidated! pivots: [8, 10], dihedral: [6, 8, 10, 5], invalidation reason:
""",
)

