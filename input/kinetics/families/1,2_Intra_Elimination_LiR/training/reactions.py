#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Intra_Elimination_LiR"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3H4LiO3 <=> C3H4LiO3-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.57285e+17,'s^-1'), n=-0.785762, Ea=(69.0722,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.0810004035910854,B=2.1395342731524263,E=1.574243739442836,L=12.72791320115644,A=0.4805246849919219,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O[C]1OCCO1 <=> [Li]OCCO[C]=O
TS method summary for TS2 in [Li]O[C]1OCCO1 <=> [Li]OCCO[C]=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
O       2.59867100   -0.18728600   -1.35132100
C       1.56185200    0.17450300   -0.90257500
O       1.11484400    0.02288600    0.33185500
C      -0.23857200    0.51166800    0.61927300
C      -1.32472800   -0.56246600    0.36870000
O      -2.30958000   -0.11570300   -0.47987400
Li     -3.43222200    0.30055100   -1.54626500
H      -0.43948800    1.37473300   -0.01534500
H      -0.17835100    0.82215200    1.66217400
H      -1.74337700   -0.86314000    1.34516400
H      -0.80689900   -1.45309200   -0.02768100

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 38.37 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 11.02 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Could not read energies
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 0.22 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1716.0525411150861 J/mol
""",
)

entry(
    index = 2,
    label = "C3H5LiO2 <=> C3H5LiO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.22949e+12,'s^-1'), n=0.0425752, Ea=(-0.0643594,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6463081864477556,B=1.3642592064572354,E=2.83101426768693,L=6.499926586799369,A=1.3639449338060428,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC1OCC1 <=> O=CCCO[Li]
TS method summary for TS7 in [Li]OC1OCC1 <=> O=CCCO[Li]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -1.13093225   -1.47782476   -0.52938465
O      -1.71415457    0.21718059   -0.13786126
C      -0.60832813    0.42268843    0.42486000
O       0.44495341   -1.09247544    0.19796183
C       1.46777571   -0.14965544   -0.03324304
C       0.58784040    1.07473776   -0.26303306
H      -0.57618074    0.46549170    1.52547654
H       2.11736192   -0.42023494   -0.87312379
H       2.10541851   -0.03741197    0.85335523
H       0.35290002    1.23671989   -1.31600879
H       0.90847788    2.01537435    0.18857794

1D rotors:
* Invalidated! pivots: [3, 6], dihedral: [2, 3, 6, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molTwo consecutive points are inconsistent by more than 0.39 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 3], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 383.9871972817142 J/mol
""",
)

entry(
    index = 3,
    label = "C4H7LiO2 <=> C4H7LiO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.92231e+16,'s^-1'), n=-0.357468, Ea=(90.256,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.8258378208381454,B=2.5221250810295626,E=1.614714374506913,L=12.761980701907916,A=0.608203513102231,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC1OCCC1 <=> O=CCCCO[Li]
TS method summary for TS5 in [Li]OC1OCCC1 <=> O=CCCCO[Li]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.22951500   -8.28055600    1.65539800
O       0.68519100   -2.60872700   -1.25971800
C       1.79766000   -3.06680400   -1.37724100
O       3.01142700   -7.05534000    0.98825700
C       3.68295800   -5.99093900    0.43042200
C       2.84010400   -5.23936600   -0.64613300
C       2.57331200   -3.76228300   -0.29332800
H       2.31835000   -3.00937400   -2.36068900
H       4.62637300   -6.32192200   -0.04005100
H       3.97620800   -5.26015300    1.20678500
H       1.88728800   -5.76856000   -0.73282900
H       3.32837000   -5.29792800   -1.62623300
H       3.53476000   -3.24110100   -0.18547300
H       2.02723700   -3.67881900    0.64973300

1D rotors:
pivots: [3, 7], dihedral: [2, 3, 7, 6], rotor symmetry: 1, max scan energy: 7.20 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason: Could not read energies
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
pivots: [6, 7], dihedral: [5, 6, 7, 3], rotor symmetry: 1, max scan energy: 25.95 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1791.841785505636 J/mol
""",
)

entry(
    index = 4,
    label = "C5H9LiO2 <=> C5H9LiO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.20531e+14,'s^-1'), n=0.219161, Ea=(98.9886,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.959149780060317,B=2.5380295864101,E=2.0257428425399984,L=13.738628302899908,A=0.411629130549155,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC1OCCCC1 <=> O=CCCCCO[Li]
TS method summary for TS6 in [Li]OC1OCCCC1 <=> O=CCCCCO[Li]:
Methods that successfully generated a TS guess:
user guess 0,user guess 1,
The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -2.20746100   -3.36971300   -3.70952100
O       1.25187300    1.95405300   -1.04632200
C       1.04640200    0.88280800   -1.56571700
O      -0.61905500   -3.34540100   -3.52965300
C       0.75057700   -3.40515400   -3.37372500
C       1.33014800   -2.18325400   -2.63924900
C       1.17117900   -0.87493200   -3.42052900
C       1.82427700    0.33951000   -2.74581800
H       0.23182200    0.22912600   -1.18197300
H       1.26013900   -3.48345200   -4.35441500
H       1.04873000   -4.30660500   -2.80769200
H       2.39940800   -2.39734300   -2.50177400
H       0.89693800   -2.08083500   -1.63590000
H       0.10876700   -0.72003200   -3.63956100
H       1.66878000   -0.97713400   -4.39144100
H       1.96556900    1.17143800   -3.44430700
H       2.82865100    0.08557500   -2.37989200

1D rotors:
* Invalidated! pivots: [3, 8], dihedral: [2, 3, 8, 7], invalidation reason:
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason:
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: Another conformer for TS6 exists which is 7.66 kJ/mol lower.
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 3], invalidation reason:
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1729.1474107981676 J/mol
""",
)

