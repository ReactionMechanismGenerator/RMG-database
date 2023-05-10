#!/usr/bin/env python
# encoding: utf-8

name = "Li_NO_Ring_Opening/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H4LiO <=> C2H4O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.79548e+09,'s^-1'), n=0.676137, Ea=(127.392,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9429002183123382,B=0.4142522035781646,E=0.9271382422782674,L=0.5080999191526422,A=1.2701035125702795,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC[CH2] <=> [Li] + O1CC1
TS method summary for TS1 in [Li]OC[CH2] <=> [Li] + O1CC1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.73301400   -1.23426700   -0.49793500
O       0.60551200    0.06249200   -0.10018600
C      -0.50388800    0.89554800    0.19652100
C      -1.00886000   -0.45148800   -0.03734900
H      -0.69990300    1.66086200   -0.55370500
H      -0.51073300    1.28290300    1.21479300
H      -1.15946900   -1.12920200    0.79035100
H      -1.35302600   -0.74247900   -1.01915400


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2253.8360605095613 J/mol
""",
)

entry(
    index = 2,
    label = "C4H9LiN <=> C4H9N + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41052e+13,'s^-1'), n=-0.0966111, Ea=(37.9728,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.7063184659079954,B=0.6546888841685338,E=1.4167685288377097,L=7.086460323740072,A=0.6763993010322846,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NCCC[CH2] <=> [Li] + N1CCCC1
TS method summary for TS8 in [Li]NCCC[CH2] <=> [Li] + N1CCCC1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.79696000   -2.05316500   -1.00229800
N      -1.02753700   -0.82446500    0.31048300
C      -1.17602900    0.62975500    0.34728300
C      -0.04031000    1.23440900   -0.48523000
C       1.26536000    0.60012900    0.03045100
C       1.10536400   -0.89281200    0.16065300
H      -1.14744700   -1.20628300    1.24655300
H      -2.14778300    0.93882900   -0.05818200
H      -1.11834800    1.02433100    1.37055800
H      -0.18192200    0.97424700   -1.54208700
H      -0.02609500    2.32742400   -0.41948200
H       2.09531900    0.85423100   -0.64191300
H       1.50425000    1.03272800    1.00804200
H       1.36740100   -1.36403600    1.10079100
H       1.41475700   -1.48698600   -0.70029100

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 14], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 5600.017004537509 J/mol
""",
)

entry(
    index = 3,
    label = "C6H12LiO <=> C6H12O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(685907,'s^-1'), n=0.809304, Ea=(91.8794,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8745309700808286,B=0.6489379258617733,E=0.27349172242979114,L=6.280608540134562,A=0.35178208431790287,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCCCCC[CH2] <=> [Li] + O1CCCCCC1
TS method summary for TS4 in [Li]OCCCCC[CH2] <=> [Li] + O1CCCCCC1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.21778400   -2.51460800    1.52748300
O       0.30780200   -0.93202600    1.17295000
C       1.22507300    0.05015800    0.75305900
C       1.16007100    0.34370200   -0.74604900
C      -0.18415100    0.88158700   -1.26317700
C      -1.37708100   -0.08782900   -1.14193800
C      -2.18529400   -0.00383000    0.17331100
C      -1.43642000   -0.15241200    1.46687200
H       2.23706500   -0.28675900    1.01225300
H       1.05582400    0.98241000    1.31722700
H       1.94770800    1.07203000   -0.98005100
H       1.41088600   -0.57386900   -1.29204500
H      -0.05269600    1.13539800   -2.32063300
H      -0.42385200    1.82754000   -0.75961200
H      -1.02546000   -1.11603800   -1.28152500
H      -2.08272100    0.11086500   -1.95663300
H      -2.68514000    0.97783700    0.18386800
H      -2.97901800   -0.75853500    0.12355800
H      -1.85839500   -0.83027000    2.20556000
H      -1.01299600    0.74101900    1.91000900

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 19], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 648.5792529213884 J/mol
""",
)

entry(
    index = 4,
    label = "C4H8LiO <=> C4H8O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.68382e+12,'s^-1'), n=-0.0538311, Ea=(99.5874,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.975919765798433,B=0.5933221434562257,E=0.10249027371088437,L=4.734916369654065,A=0.4382337255257122,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCCC[CH2] <=> [Li] + O1CCCC1
TS method summary for TS5 in [Li]OCCC[CH2] <=> [Li] + O1CCCC1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.18875700    4.40146700   -0.15965700
O       1.25526000    4.50560200    1.18500100
C       1.81848000    4.05586800    2.39368600
C       3.04718900    4.92469900    2.67844800
C       2.59628200    6.35626200    2.34735900
C       1.87760200    6.33368500    1.02998700
H       2.48003000    6.25991400    0.13113900
H       1.09474400    4.15021500    3.21790700
H       2.09303800    2.99768000    2.31072700
H       3.86832600    4.63175200    2.01575200
H       3.39490700    4.82429600    3.71124200
H       1.92993300    6.72532100    3.13318700
H       3.45844200    7.03440200    2.30740100
H       0.97428300    6.92366500    0.92199700

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1463.7250120069011 J/mol
""",
)

entry(
    index = 5,
    label = "C3H4O3 + Li <=> C3H4LiO3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.40229e+07,'cm^3/(mol*s)'), n=2.08453, Ea=(2.45304,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.0971475333838443,B=1.0651724160645786,E=2.8149716305609487,L=7.643459730707861,A=0.5170156663408971,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: O=C1OCCO1 + [Li] <=> [Li]OC(=O)OC[CH2]
TS method summary for TS1 in O=C1OCCO1 + [Li] <=> [Li]OC(=O)OC[CH2]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
O      -1.86849600   -0.34389700    0.15565300
C      -0.66560700   -0.08480900    0.09252000
O      -0.21610600    1.13496900   -0.11650000
C       1.46459400    1.02715100   -0.12713400
C       1.62862000   -0.44407800    0.11303000
O       0.26269000   -1.02218000    0.23159700
H       1.74745400    1.69347200    0.67895300
H       1.71712500    1.39749600   -1.11346200
H       2.10022500   -0.97192200   -0.71484300
H       2.13009200   -0.68039600    1.05062500
Li     -2.71413000    1.28166300   -0.09846000

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [11, 1, 2, 3], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2574.2194772490175 J/mol
""",
)

