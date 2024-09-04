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

# entry(
#     index = 0,
#     label = "2FFOH + H_rad <=> P1 + H2",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(578.285,'cm^3/(mol*s)'), n=3.0612, Ea=(38.7555,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# RXN 2
# TS method summary for TS0 in 2FFOH + H_rad <=> P1 + H2:
# Methods that successfully generated a TS guess:
# autotst,autotst,autotst,autotst,heuristics,
# The method that generated the best TS guess and its output used for the optimization: autotst


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# O       0.66737700    0.64839500   -1.26344600
# O      -2.26188800   -0.08593100    0.77829200
# C      -1.54618400    0.51507800   -0.25784600
# C      -0.06712200    0.33196700   -0.15656100
# C       0.75238200   -0.08826500    0.84614100
# C       2.08592200   -0.03184500    0.32466400
# C       1.97715400    0.42164700   -0.95028400
# H      -1.79888100    1.58478800   -0.16418200
# H      -1.89381500    0.21198400   -1.25602400
# H       0.43878800   -0.39396100    1.83062400
# H       2.99879300   -0.29653100    0.83403000
# H       2.68751300    0.62532800   -1.73324100
# H      -2.12037600   -1.29270700    0.68191000
# H      -1.91966200   -2.15004700    0.48582000

# 1D rotors:
# pivots: [2, 3], dihedral: [13, 2, 3, 4], rotor symmetry: 1, max scan energy: 18.85 kJ/mol
# * Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 1], invalidation reason: Another conformer for TS0 exists which is 3.88 kJ/mol lower.Another conformer for TS0 exists which is 3.88 kJ/mol lower.
# """,
# )

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

# entry(
#     index = 4,
#     label = "2FFOH + OH_rad <=> P3 + H2O",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(0.00753898,'cm^3/(mol*s)'), n=4.02856, Ea=(6.5407,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# RXN 9 
# TS method summary for TS0 in 2FFOH + OH_rad <=> P3 + H2O:
# Methods that successfully generated a TS guess:
# autotst,autotst,autotst,autotst,heuristics,heuristics,
# The method that generated the best TS guess and its output used for the optimization: autotst


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# O       0.28234900   -1.64226800    0.83785100
# O       1.64695300    1.69373200    0.38569000
# O      -0.67420800    2.13950300   -1.34704200
# C       1.75583400    0.28540100    0.41503800
# C       0.43310500   -0.40634400    0.27389000
# C      -1.67177300   -1.13174300   -0.14967000
# C      -0.99484900   -2.06189000    0.57252600
# C      -0.72274100   -0.08519400   -0.36123000
# H       2.19135600    0.01219200    1.37908100
# H       2.44100300   -0.08322900   -0.36462700
# H      -2.68468000   -1.20019400   -0.51041500
# H      -1.25219300   -3.03732300    0.94912800
# H       1.15539700    1.94998900   -0.40901600
# H      -0.80738900    1.00227700   -1.08576700
# H      -1.09816100    2.56519000   -0.58533900

# 1D rotors:
# * Invalidated! pivots: [2, 4], dihedral: [13, 2, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
# * Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason: Another conformer for TS0 exists which is 7.36 kJ/mol lower.Another conformer for TS0 exists which is 7.36 kJ/mol lower.
# """,
# )

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

# entry(
#     index = 6,
#     label = "2FFOH + OH_rad <=> P4 + H2O",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(9.78402,'cm^3/(mol*s)'), n=3.60945, Ea=(13.4437,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# RXN 12
# TS method summary for TS0 in 2FFOH + OH_rad <=> P4 + H2O:
# Methods that successfully generated a TS guess:
# autotst,autotst,autotst,autotst,heuristics,heuristics,
# The method that generated the best TS guess and its output used for the optimization: heuristics


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# O       0.01844900   -2.14694100   -2.20019200
# C      -0.09590100   -2.21044500   -0.77982000
# C      -0.05843900   -0.87140400   -0.12621000
# C       0.84578300   -0.22761100    0.66323700
# C       0.26647700    1.04859200    0.93414100
# C      -0.91992500    1.12127200    0.28911000
# O      -1.14308600   -0.06128800   -0.36196000
# H      -0.72820500   -1.63348300   -2.52549700
# H      -1.01565100   -2.73581100   -0.48706300
# H       0.75265200   -2.79790400   -0.42813100
# H       1.78859800   -0.61566500    1.01247200
# H       0.75121700    1.98631600    1.72732500
# H      -1.68347400    1.87349900    0.19812100
# O       1.28180900    2.92812600    2.12226300
# H       1.72594800    3.24963900    1.32330200

# 1D rotors:
# pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.29 kJ/mol
# pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.18 kJ/mol
# """,
# )

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

# entry(
#     index = 8,
#     label = "2FFOH + OH_rad <=> P5 + H2O",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(9.53484,'cm^3/(mol*s)'), n=3.65382, Ea=(16.8022,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# RXN 15
# TS method summary for TS0 in 2FFOH + OH_rad <=> P5 + H2O:
# Methods that successfully generated a TS guess:
# user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,
# The method that generated the best TS guess and its output used for the optimization: heuristics


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# O       0.43725000   -2.03928000   -1.95462300
# C       0.54953200   -2.09889800   -0.53464400
# C       0.55881900   -0.75830400    0.11269300
# C       1.47400200   -0.04207300    0.82274100
# C       0.85349800    1.20180200    1.18243500
# C      -0.41288700    1.11265200    0.69616800
# O      -0.61169300   -0.03134200    0.01278500
# H      -0.40653000   -1.62345800   -2.15985100
# H      -0.25545400   -2.71195600   -0.10589900
# H       1.49715400   -2.59448600   -0.31939300
# H       2.47577400   -0.35963600    1.06742800
# H       1.27788000    2.02083800    1.73868900
# H      -1.44768200    1.96286500    0.75939200
# O      -2.15339800    2.80584400    0.47745000
# H      -1.77872000    3.13646200   -0.35202700

# 1D rotors:
# pivots: [1, 2], dihedral: [8, 1, 2, 3], rotor symmetry: 1, max scan energy: 11.63 kJ/mol
# pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 12.00 kJ/mol
# """,
# )

entry(
    index = 9,
    label = "s34_n-C4H5 + 2FFOH <=> s35_1,3-butadiene + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0665901,'cm^3/(mol*s)'), n=3.59977, Ea=(1.56916,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 16
TS method summary for TS0 in s34_n-C4H5 + s19_furfuryl <=> s35_1,3-butadiene + s21_P2:
Methods that successfully generated a TS guess:
user guess 0 + autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.59256400    1.41900400   -1.21605900
O       1.33438800   -1.17670300   -0.32984800
C       0.92559700   -0.16813000    0.56686800
C       1.05420800    1.20886700    0.05764900
C       1.46919700    2.39146300    0.59521400
C       1.25870500    3.39257300   -0.40773100
C       0.73289800    2.75089200   -1.48183700
H      -0.23911100   -0.36421600    0.85464200
H       1.47125800   -0.29878900    1.50105300
H       1.88496300    2.53126000    1.58036700
H       1.48012800    4.44557400   -0.33716100
H       0.42622500    3.06830300   -2.46375000
H       0.95089000   -0.97431900   -1.19093500
C      -1.42668400   -3.08275400    0.63503000
C      -2.19433100   -1.93495600    1.11169800
C      -1.92600200   -4.31955700    0.54292200
C      -1.74130900   -0.69496500    1.23039100
H      -0.39829500   -2.88826500    0.34343400
H      -3.23405300   -2.14154100    1.38890300
H      -2.95072700   -4.54210100    0.82488300
H      -1.32582500   -5.14733500    0.18471300
H      -2.25317500    0.19614800    1.57527300

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [13, 2, 3, 4], invalidation reason: Another conformer for TS0 exists which is 4.86 kJ/mol lower.Another conformer for TS0 exists which is 4.86 kJ/mol lower.
pivots: [3, 4], dihedral: [2, 3, 4, 1], rotor symmetry: 1, max scan energy: 12.77 kJ/mol
* Invalidated! pivots: [14, 15], dihedral: [16, 14, 15, 17], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 10,
    label = "CHO + 2FFOH <=> formaldehyde + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.27509e-08,'cm^3/(mol*s)'), n=5.52049, Ea=(25.2695,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN18
TS method summary for TS0 in CHO + furfuryl <=> formaldehyde + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       1.52186300   -0.84542900    0.43284700
O      -1.48725300   -0.22325300   -1.43556300
O      -3.59993100   -0.04821300    0.59543400
C      -0.73556800   -0.74664300   -0.38865200
C       0.59675900   -0.17506300   -0.32363700
C       1.14865900    0.97417100   -0.82363400
C       2.49724400    1.00822200   -0.35482400
C       2.66982800   -0.10946400    0.40058700
C      -2.65435900   -0.08212500    1.32681500
H      -1.41383900   -0.35773200    0.68620200
H      -0.75036500   -1.83968500   -0.30265000
H       0.64581100    1.68708700   -1.45548300
H       3.24086900    1.76274600   -0.55686300
H       3.50160400   -0.51534600    0.95068500
H      -2.42183300   -0.26117600   -1.18398400
H      -2.75949000   -0.22789900    2.43261900

1D rotors:
* Invalidated! pivots: [2, 4], dihedral: [15, 2, 4, 5], invalidation reason: Another conformer for TS0 exists which is 2.88 kJ/mol lower.Another conformer for TS0 exists which is 2.88 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [2, 4, 5, 1], invalidation reason:
""",
)

entry(
    index = 11,
    label = "H_rad + P389 <=> H2 + P390",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.69896e+06,'cm^3/(mol*s)'), n=2.14096, Ea=(13.5192,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN19
TS method summary for TS0 in H_rad + r1 <=> H2 + p1:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.72246500    1.46954900   -0.41574300
O      -1.36831400    1.99849700    0.28101600
C      -0.52493000   -0.30982000    0.46342800
C       0.85502700   -0.73647000    0.14066000
C      -0.52295600    1.17138600    0.14363100
C       1.48823300    0.32155400   -0.37270800
H      -1.32705800   -0.80411000   -0.26984500
H      -0.92384200   -0.53543000    1.45250100
H       1.26930600   -1.72370200    0.26870900
H       2.49327700    0.43744300   -0.74748900
H      -2.16110600   -1.28879600   -0.94416300


No rotors considered for this TS.
""",
)

entry(
    index = 12,
    label = "Vinyl_radical + 2FFOH <=> ethylene + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0230744,'cm^3/(mol*s)'), n=3.92469, Ea=(3.15646,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 21
TS method summary for TS0 in Vinyl_radical + furfuryl <=> ethylene + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.23380200    1.06131200   -0.64530000
O       1.13260800   -1.63146100   -0.59056900
C       0.45490300   -1.04827200    0.49885100
C       0.48662200    0.42442100    0.54224000
C       0.63746800    1.34825600    1.53405700
C       0.47477300    2.63403100    0.92332700
C       0.23845000    2.40351900   -0.39298900
H      -0.70411500   -1.41180400    0.44070300
H       0.84432600   -1.48302100    1.41917300
H       0.84970100    1.13978700    2.57059600
H       0.53655200    3.59805700    1.40261900
H       0.07057500    3.04150600   -1.24370100
H       0.88580000   -1.13808600   -1.38118000
C      -2.06190000   -2.13192100    0.11635900
C      -1.91391300   -3.13366500   -0.72042400
H      -2.94834200   -1.72374200    0.59011800
H      -2.75633100   -3.73271900   -1.07181200
H      -0.93252900   -3.41093800   -1.09953200

1D rotors:
pivots: [2, 3], dihedral: [13, 2, 3, 4], rotor symmetry: 2, max scan energy: 16.26 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 1], rotor symmetry: 1, max scan energy: 12.81 kJ/mol
""",
)

entry(
    index = 13,
    label = "methanol_rad + 2FFOH <=> methanol + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.28079e-09,'cm^3/(mol*s)'), n=5.5223, Ea=(8.89939,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 24
TS method summary for TS0 in methanol_rad + furfuryl <=> methanol + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -0.85166300    0.03063000    0.82759400
O       1.96353100    0.71644400    1.43600800
O       1.34047700   -1.85036800    0.29571400
C       2.22509400    1.05452600    0.10483300
C      -0.62638000   -0.57048800   -0.39517100
C      -1.76671300   -0.50036100   -1.14329000
C      -2.75265900    0.16101500   -0.34270700
C      -2.15354200    0.45717000    0.83708300
C       0.74137900   -1.02425000   -0.66332100
H       1.48445300    0.06573000   -0.63093600
H       3.27723800    0.90175900   -0.11911500
H       1.82824300    2.02140700   -0.21199400
H      -1.89295900   -0.89468000   -2.13900500
H      -3.77613400    0.37259500   -0.60888300
H       0.83873300   -1.46924900   -1.65245500
H      -2.48852300    0.92473600    1.74718100
H       1.02946100    0.89298500    1.60959400
H       1.57986300   -1.28969700    1.04906800

1D rotors:
pivots: [2, 4], dihedral: [17, 2, 4, 11], rotor symmetry: 2, max scan energy: 28.36 kJ/mol
pivots: [3, 9], dihedral: [18, 3, 9, 5], rotor symmetry: 1, max scan energy: 24.56 kJ/mol
pivots: [5, 9], dihedral: [1, 5, 9, 3], rotor symmetry: 1, max scan energy: 25.00 kJ/mol
""",
)

entry(
    index = 14,
    label = "P1 + MF <=> 2FFOH + P10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0287753,'cm^3/(mol*s)'), n=4.01573, Ea=(-3.05482,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 22
TS method summary for TS0 in P1 + MF <=> furfuryl + P10:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.89241300   -1.94588900   -0.43036900
C       1.54233900   -0.84470500    0.09396400
C       1.33190800   -0.66330800    1.56725300
C       0.79849400   -1.46032800    2.53127200
C       0.89182100   -0.72565200    3.76053100
C       1.47469900    0.46006000    3.45182000
O       1.74927600    0.51870000    2.11386700
H       1.26553800    0.08997600   -0.42982600
H       2.61844100   -0.97264900   -0.12110500
H       0.39989700   -2.44941000    2.37710000
H       0.56823200   -1.04348400    4.73913800
H       1.75217400    1.32790200    4.02557300
O      -1.32227900    0.29217900   -2.84016700
C      -1.50593000   -1.08336400   -0.86569600
C      -1.40155000    0.22703900   -1.47280300
C      -1.29672600    1.50158500   -0.95787800
C      -1.15818100    2.38524400   -2.06444200
C      -1.17917000    1.60068700   -3.17856500
H      -0.39488500   -1.54836100   -0.69907200
H      -1.99116800   -1.81879200   -1.50758600
H      -1.93953900   -1.05695300    0.13242000
H      -1.32282100    1.75948300    0.08901600
H      -1.05850900    3.45852800   -2.03967700
H      -1.11391800    1.80909800   -4.23312600

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 11.50 kJ/mol
* Invalidated! pivots: [14, 15], dihedral: [19, 14, 15, 13], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
""",
)

entry(
    index = 15,
    label = "P10 + 2FFOH <=> MF + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.95041e-10,'cm^3/(mol*s)'), n=5.77838, Ea=(31.3798,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 23
TS method summary for TS0 in P10 + furfuryl <=> MF + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       2.75301300   -1.04846200   -1.20446100
O      -3.03521900   -0.91916600   -0.27983000
O       0.26012900    1.46932400   -0.60256000
C       0.71467700    0.18933800   -0.91923900
C       2.12988800    0.03565800   -0.64474400
C      -2.13820500   -0.43402200    0.64367000
C       3.01410100    0.72458600    0.14291300
C      -2.62712800    0.75327900    1.15462900
C      -3.88534800    0.98911900    0.52459900
C       4.25805100    0.02734700    0.05444900
C      -4.08492300   -0.04927200   -0.33123900
C       4.04581800   -1.03510100   -0.76690000
C      -0.90315800   -1.14596700    0.80957900
H       0.02063200   -0.61572500   -0.10750300
H       0.41132300   -0.18330900   -1.90435600
H      -2.14588600    1.35924500    1.90604600
H      -4.55588800    1.81722800    0.69122600
H       2.79321500    1.62139700    0.69726700
H       5.18801300    0.28567100    0.53580700
H      -4.87955500   -0.31170200   -1.00865600
H       4.67101000   -1.83251900   -1.13065800
H      -0.37518800   -0.94079400    1.73691900
H      -0.92697300   -2.19684200    0.53409400
H      -0.70239800    1.44089300   -0.53105500

1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [24, 3, 4, 5], invalidation reason: Another conformer for TS0 exists which is 2.54 kJ/mol lower.Another conformer for TS0 exists which is 2.54 kJ/mol lower.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 1], invalidation reason:
""",
)

entry(
    index = 16,
    label = "methane_rad + 2FFOH <=> mathane + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.021089,'cm^3/(mol*s)'), n=4.38858, Ea=(17.9507,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 25
TS method summary for TS0 in methane_rad + furfuryl <=> mathane + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -1.24058600    0.43924200    0.72383200
O       0.73334600    2.21447100   -0.23930000
C       2.64261700   -0.40769600    0.84451600
C      -0.60670300    0.19842000   -0.46905100
C      -1.32244300   -0.71150100   -1.19104100
C      -2.47047400   -1.04776200   -0.40273900
C      -2.37527300   -0.32224100    0.73999100
C       0.68958000    0.87022900   -0.64730000
H       1.54166900    0.24618300    0.00962200
H       3.44254000    0.32326800    0.78205500
H       2.17196500   -0.50061500    1.81868300
H       2.82319000   -1.34524000    0.32749200
H      -1.06992200   -1.08711600   -2.16982400
H      -3.26356200   -1.73114800   -0.66151100
H       1.03981300    0.80498800   -1.67723100
H      -2.99478900   -0.22291100    1.61474300
H       0.25893200    2.27942600    0.59696500

1D rotors:
pivots: [2, 8], dihedral: [17, 2, 8, 4], rotor symmetry: 1, max scan energy: 16.07 kJ/mol
pivots: [4, 8], dihedral: [1, 4, 8, 2], rotor symmetry: 1, max scan energy: 14.41 kJ/mol
""",
)

# entry(
#     index = 17,
#     label = "2FFOH + H_rad <=> P2 + H2",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(2.53704e+06,'cm^3/(mol*s)'), n=2.18658, Ea=(14.9787,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
#     longDesc = 
# """
# RXN 5
# TS method summary for TS0 in 2FFOH + H_rad <=> P2 + H2:
# Methods that successfully generated a TS guess:
# autotst,autotst,autotst,autotst,heuristics,
# The method that generated the best TS guess and its output used for the optimization: autotst


# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# O       0.69390400   -0.94115100    0.07284900
# O      -1.84620100   -0.89974100    1.40199500
# C      -1.53493100   -0.05029200    0.32476800
# C      -0.08897200    0.18274500    0.11357200
# C       0.67877400    1.28584900   -0.10510800
# C       2.02146900    0.81920200   -0.28784900
# C       1.97377900   -0.53144100   -0.16589700
# H      -1.98360000   -0.49897300   -0.66172100
# H      -2.05992300    0.89371000    0.47283600
# H       0.33393700    2.30742200   -0.12586300
# H       2.90064700    1.41410300   -0.47699100
# H       2.71516000   -1.31073100   -0.21175900
# H      -1.27506300   -1.67329000    1.33795500
# H      -2.52888100   -0.99741200   -1.68878700

# 1D rotors:
# pivots: [2, 3], dihedral: [13, 2, 3, 4], rotor symmetry: 1, max scan energy: 16.40 kJ/mol
# pivots: [3, 4], dihedral: [2, 3, 4, 1], rotor symmetry: 1, max scan energy: 12.89 kJ/mol
# """,
# )

entry(
    index = 18,
    label = "But-2-yn-1-yl_radical + 2FFOH <=> buta-1,2-diene + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.72695e-09,'cm^3/(mol*s)'), n=5.22517, Ea=(34.3294,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
RXN 26
TS method summary for TS0 in r1 + furfuryl <=> p1 + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,
The method that generated the best TS guess and its output used for the optimization: autotst


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O      -2.11445900    0.38651300   -0.51032200
O      -0.50329500   -1.10952200   -2.19324400
C      -0.35274400   -1.21315500   -0.80782100
C       2.76546300   -0.10787200   -1.57916000
C      -1.44781800   -0.69648200    0.00496800
C      -1.92816100   -0.97682800    1.25529700
C      -2.95501700   -0.01799100    1.52107400
C      -3.03113100    0.77942300    0.42452400
C       1.95068600    1.64348900    1.76801300
C       1.92318200    0.20244600   -0.39110500
C       1.98450900    0.92482400    0.65456900
H      -0.05679300   -2.22707700   -0.54393000
H       0.71566000   -0.51371000   -0.49292500
H       3.64535000    0.54054800   -1.62104400
H       2.19495300    0.01527100   -2.50363100
H       3.10783900   -1.14754300   -1.55355200
H      -1.59402300   -1.77283100    1.90115900
H      -3.56084800    0.05991500    2.40978600
H      -3.65021100    1.61654300    0.15147700
H       1.55123600    2.65240600    1.77707400
H       2.33791600    1.25406900    2.70399200
H      -0.98239000   -0.29243800   -2.37519900

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [22, 2, 3, 5], invalidation reason: Two consecutive points are inconsistent by more than 5.35 kJ/molTwo consecutive points are inconsistent by more than 5.35 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 1], rotor symmetry: 1, max scan energy: 24.68 kJ/mol
pivots: [4, 10], dihedral: [14, 4, 10, 11], rotor symmetry: 3, max scan energy: 2.05 kJ/mol
""",
)

entry(
    index = 19,
    label = "HO2 + 2FFOH <=> H2O2 + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.51255e-08,'cm^3/(mol*s)'), n=5.32856, Ea=(14.8414,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
TS method summary for TS0 in HO2 + furfuryl <=> H2O2 + P2:
Methods that successfully generated a TS guess:
user guess 0,autotst,autotst,autotst,autotst,heuristics,heuristics,heuristics,heuristics,heuristics,
The method that generated the best TS guess and its output used for the optimization: heuristics


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       0.56301300    1.18587000   -0.48457000
O       1.17083700   -1.51504600   -0.80673700
C       0.45913300   -1.08184100    0.30783500
C       0.47973400    0.34937000    0.59479200
C       0.32583200    1.08776100    1.73839100
C       0.32446500    2.45831200    1.33831900
C       0.47174600    2.46261300   -0.01329700
H      -0.76271400   -1.37303000    0.02917900
H       0.70423600   -1.70397500    1.16713800
H       0.23178600    0.69818600    2.73948100
H       0.23375600    3.32470400    1.97371900
H       0.53879900    3.24150300   -0.75331100
H       0.93031500   -0.94321400   -1.54759400
O      -1.45567400   -1.76035200   -1.91711300
O      -1.82854300   -1.73471200   -0.56627500
H      -1.18340000   -2.68097400   -2.04809700

1D rotors:
pivots: [2, 3], dihedral: [13, 2, 3, 4], rotor symmetry: 2, max scan energy: 25.89 kJ/mol
pivots: [14, 15], dihedral: [16, 14, 15, 8], rotor symmetry: 2, max scan energy: 53.56 kJ/mol
""",
)














