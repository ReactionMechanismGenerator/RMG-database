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
    label = "2FFOH + H_rad <=> P1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(578.285,'cm^3/(mol*s)'), n=3.0612, Ea=(38.7555,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 2
TS method summary for TS0 in 2FFOH + H_rad <=> P1 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.66737700    0.64839500   -1.26344600
O      -2.26188800   -0.08593100    0.77829200
C      -1.54618400    0.51507800   -0.25784600
C      -0.06712200    0.33196700   -0.15656100
C       0.75238200   -0.08826500    0.84614100
C       2.08592200   -0.03184500    0.32466400
C       1.97715400    0.42164700   -0.95028400
H      -1.79888100    1.58478800   -0.16418200
H      -1.89381500    0.21198400   -1.25602400
H       0.43878800   -0.39396100    1.83062400
H       2.99879300   -0.29653100    0.83403000
H       2.68751300    0.62532800   -1.73324100
H      -2.12037600   -1.29270700    0.68191000
H      -1.91966200   -2.15004700    0.48582000

1D rotors:
pivots: [2, 3], dihedral: [13, 2, 3, 4], rotor symmetry: 1, max scan energy: 18.85 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 1], invalidation reason: Another conformer for TS0 exists which is 3.88 kJ/mol lower.Another conformer for TS0 exists which is 3.88 kJ/mol lower.
""",
)

entry(
    index = 1,
    label = "2FFOH + OH_rad <=> P1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.21054,'cm^3/(mol*s)'), n=3.59488, Ea=(-7.09582,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 3
TS method summary for TS0 in 2FFOH + OH_rad <=> P1 + H2O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.08014400    0.92974500   -0.31711900
O       1.66410600   -1.40537500    0.70001000
O       2.99021400    0.22530000   -0.18958800
C       0.60065400   -1.45040200   -0.23304300
C      -0.38041600   -0.33908400   -0.06383800
C      -1.68679400   -0.28221900    0.30594600
C      -2.06490700    1.10102100    0.28164700
C      -0.95951900    1.78870800   -0.09603800
H       0.99380300   -1.46844200   -1.25638300
H       0.07978800   -2.39805500   -0.05608600
H      -2.30874700   -1.12334100    0.56852400
H      -3.02968700    1.52036000    0.51787900
H      -0.74709000    2.83284600   -0.25021100
H       2.48301700   -0.82403500    0.29147200
H       2.28543600    0.89297400   -0.20317100

1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [14, 2, 4, 5], invalidation reason: Two consecutive points are inconsistent by more than 5.13 kJ/molTwo consecutive points are inconsistent by more than 5.13 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason: Two consecutive points are inconsistent by more than 5.10 kJ/molTwo consecutive points are inconsistent by more than 5.10 kJ/mol
""",
)

entry(
    index = 2,
    label = "2FFOH + O2 <=> P2 + OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00706335,'cm^3/(mol*s)'), n=3.98429, Ea=(123.422,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 4
TS method summary for TS0 in 2FFOH + O2 <=> P2 + [O]O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.00103800   -0.26792000   -1.31948800
O      -1.47599200   -1.01268500    1.18152500
O      -2.80158300    1.04999900   -0.46483800
O      -3.62118300    0.54074100    0.39757600
C       0.36957700   -0.28223600   -0.10187400
C       1.21956900    0.21113800    0.86601200
C       2.43372600    0.53681700    0.20428600
C       2.24922500    0.23244800   -1.11280600
C      -0.99021700   -0.72238000   -0.07353100
H       0.98278100    0.31133900    1.91214300
H       3.33045200    0.94302700    0.64427900
H      -1.29371600   -1.39201800   -0.88602000
H       2.87550600    0.30477500   -1.98574600
H      -2.43457200   -0.83828500    1.17580900
H      -1.84460900    0.38524000   -0.43732800

1D rotors:
* Invalidated! pivots: [2, 9], dihedral: [14, 2, 9, 5], invalidation reason: Two consecutive points are inconsistent by more than 8.53 kJ/mol But unable to propose troubleshooting methods.Two consecutive points are inconsistent by more than 8.53 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 3,
    label = "2FFOH + H_rad <=> P3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62742e+08,'cm^3/(mol*s)'), n=1.85495, Ea=(82.4166,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 8
TS method summary for TS0 in 2FFOH + H_rad <=> P3 + H2:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.10520900   -1.68049700   -1.86200200
C       0.09855700   -1.67974700   -0.43493400
C       0.09093100   -0.31409800    0.15617500
C       0.97230500    0.45918100    0.82975600
C       0.37966200    1.72464600    1.10780900
C      -0.86379000    1.64161100    0.56309200
O      -1.06771600    0.42181300   -0.01421500
H      -0.68497300   -1.21322800   -2.15195400
H      -0.75938300   -2.24940700   -0.05151200
H       1.00892900   -2.19096000   -0.12192700
H       2.46624400   -0.00060900    1.22859500
H       0.80649300    2.56612200    1.62859700
H      -1.69035800    2.33012800    0.50417700
H       3.21704100   -0.23240400    1.42841300

1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 10.80 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.48 kJ/mol
""",
)

entry(
    index = 4,
    label = "2FFOH + OH_rad <=> P3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00753898,'cm^3/(mol*s)'), n=4.02856, Ea=(6.5407,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 9 
TS method summary for TS0 in 2FFOH + OH_rad <=> P3 + H2O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.28234900   -1.64226800    0.83785100
O       1.64695300    1.69373200    0.38569000
O      -0.67420800    2.13950300   -1.34704200
C       1.75583400    0.28540100    0.41503800
C       0.43310500   -0.40634400    0.27389000
C      -1.67177300   -1.13174300   -0.14967000
C      -0.99484900   -2.06189000    0.57252600
C      -0.72274100   -0.08519400   -0.36123000
H       2.19135600    0.01219200    1.37908100
H       2.44100300   -0.08322900   -0.36462700
H      -2.68468000   -1.20019400   -0.51041500
H      -1.25219300   -3.03732300    0.94912800
H       1.15539700    1.94998900   -0.40901600
H      -0.80738900    1.00227700   -1.08576700
H      -1.09816100    2.56519000   -0.58533900

1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [13, 2, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason: Another conformer for TS0 exists which is 7.36 kJ/mol lower.Another conformer for TS0 exists which is 7.36 kJ/mol lower.
""",
)

entry(
    index = 5,
    label = "2FFOH + H_rad <=> P4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.22601e+08,'cm^3/(mol*s)'), n=1.8853, Ea=(82.5542,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 11
TS method summary for TS0 in 2FFOH + H_rad <=> P4 + H2:
Methods that successfully generated a TS guess:
user guess 0 + autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.13192900   -1.74217900   -1.87791200
C       0.13102000   -1.74653100   -0.45113000
C       0.13018500   -0.38017100    0.14415100
C       1.05721700    0.35927200    0.81747400
C       0.41845900    1.60715600    1.06995800
C      -0.82682500    1.57349900    0.55142200
O      -1.02482600    0.34234500   -0.02625200
H      -0.65847400   -1.27196600   -2.16276700
H      -0.72818000   -2.31330600   -0.06556000
H       1.04006500   -2.26490600   -0.14465900
H       2.05505400    0.05155100    1.08484400
H       1.04017100    2.87413600    1.84655300
H      -1.64969700    2.26413600    0.49899400
H       1.34830100    3.51456400    2.23787500

1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.80 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.20 kJ/mol
""",
)

entry(
    index = 6,
    label = "2FFOH + OH_rad <=> P4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.78402,'cm^3/(mol*s)'), n=3.60945, Ea=(13.4437,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 12
TS method summary for TS0 in 2FFOH + OH_rad <=> P4 + H2O:
Methods that successfully generated a TS guess:
autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.01844900   -2.14694100   -2.20019200
C      -0.09590100   -2.21044500   -0.77982000
C      -0.05843900   -0.87140400   -0.12621000
C       0.84578300   -0.22761100    0.66323700
C       0.26647700    1.04859200    0.93414100
C      -0.91992500    1.12127200    0.28911000
O      -1.14308600   -0.06128800   -0.36196000
H      -0.72820500   -1.63348300   -2.52549700
H      -1.01565100   -2.73581100   -0.48706300
H       0.75265200   -2.79790400   -0.42813100
H       1.78859800   -0.61566500    1.01247200
H       0.75121700    1.98631600    1.72732500
H      -1.68347400    1.87349900    0.19812100
O       1.28180900    2.92812600    2.12226300
H       1.72594800    3.24963900    1.32330200

1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.29 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.18 kJ/mol
""",
)

entry(
    index = 7,
    label = "2FFOH + H_rad <=> P5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.532e+07,'cm^3/(mol*s)'), n=1.94459, Ea=(83.0328,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 14
TS method summary for TS0 in 2FFOH + H_rad <=> P5 + H2:
Methods that successfully generated a TS guess:
user guess 0 + autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.22506200   -1.74050400   -1.84474500
C       0.18734900   -1.73947800   -0.41756300
C       0.20346000   -0.37732300    0.17973700
C       1.12619400    0.37469100    0.83670100
C       0.52303700    1.65224100    1.12120600
C      -0.72262400    1.55529600    0.59718800
O      -0.96135700    0.36613500    0.02953100
H      -0.55422600   -1.26639300   -2.15268200
H      -0.68953900   -2.29182800   -0.05276000
H       1.08021100   -2.27271500   -0.08816900
H       2.12817700    0.06528700    1.09172800
H       0.95763500    2.49496200    1.63164300
H      -1.94003200    2.59117200    0.53925700
H      -2.56667000    3.10836000    0.50176300

1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.80 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 13.00 kJ/mol
""",
)

entry(
    index = 8,
    label = "2FFOH + OH_rad <=> P5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.53484,'cm^3/(mol*s)'), n=3.65382, Ea=(16.8022,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 15
TS method summary for TS0 in 2FFOH + OH_rad <=> P5 + H2O:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.43725000   -2.03928000   -1.95462300
C       0.54953200   -2.09889800   -0.53464400
C       0.55881900   -0.75830400    0.11269300
C       1.47400200   -0.04207300    0.82274100
C       0.85349800    1.20180200    1.18243500
C      -0.41288700    1.11265200    0.69616800
O      -0.61169300   -0.03134200    0.01278500
H      -0.40653000   -1.62345800   -2.15985100
H      -0.25545400   -2.71195600   -0.10589900
H       1.49715400   -2.59448600   -0.31939300
H       2.47577400   -0.35963600    1.06742800
H       1.27788000    2.02083800    1.73868900
H      -1.44768200    1.96286500    0.75939200
O      -2.15339800    2.80584400    0.47745000
H      -1.77872000    3.13646200   -0.35202700

1D rotors:
pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.63 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 12.00 kJ/mol
""",
)





