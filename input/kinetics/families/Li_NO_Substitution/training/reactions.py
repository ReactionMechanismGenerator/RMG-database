#!/usr/bin/env python
# encoding: utf-8

name = "Li_NO_Substitution/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H5 + CH3LiO <=> C3H8O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00266112,'cm^3/(mol*s)'), n=4.54216, Ea=(65.2952,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC + C[CH2] <=> [Li] + COCC
TS method summary for TS2 in [Li]OC + C[CH2] <=> [Li] + COCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.95543900   -2.06606100    0.49168200
C      -1.75006400    0.40919300    0.35197900
C      -0.92556700   -0.39675200   -0.59963000
O       0.88790900   -0.39946500    0.11588300
C       1.47810800    0.86505900   -0.03509700
H      -1.29395600    1.37884800    0.56898500
H      -1.90037200   -0.11068200    1.30024000
H      -2.74501400    0.61653300   -0.07202800
H      -1.15395000   -1.45760200   -0.67306700
H      -0.66073800    0.05265400   -1.54957700
H       1.04427800    1.60592100    0.65130900
H       1.36341600    1.24189300   -1.06273700
H       2.55152500    0.80698400    0.17628500

1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 9], rotor symmetry: 3, max scan energy: 4.07 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [1, 4, 5, 11], invalidation reason: Two consecutive points are inconsistent by more than 0.60 kJ/molTwo consecutive points are inconsistent by more than 0.75 kJ/molTwo consecutive points are inconsistent by more than 0.80 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp
""",
)

entry(
    index = 2,
    label = "CH3 + CH4LiN <=> C2H7N + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(514.959,'cm^3/(mol*s)'), n=2.75171, Ea=(19.1236,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=5.9720845035693655,B=-11.11835148496454,E=1.2672065293713617,L=34.51723438776737,A=-10.461680798130194,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NC + [CH3] <=> [Li] + CNC
TS method summary for TS4 in [Li]NC + [CH3] <=> [Li] + CNC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.55807100    1.25431300    2.17607900
C       0.45911900   -0.67732400    0.78010500
N       2.03979300    0.43783800    1.54272500
C       2.89461700    0.71861100    0.39194100
H       1.12159700   -1.42531300    0.36122300
H      -0.04238100   -0.07878800    0.02372200
H      -0.21042200   -1.07927100    1.53776200
H       2.46067500   -0.31310800    2.08791500
H       3.84954800    1.15732300    0.70479900
H       2.40476300    1.44613800   -0.26337200
H       3.12222700   -0.17403500   -0.20975200

1D rotors:
pivots: [3, 4], dihedral: [1, 3, 4, 9], rotor symmetry: 3, max scan energy: 8.43 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 8.029132914089132e-10 J/mol
""",
)

entry(
    index = 3,
    label = "H + C2H6LiN <=> C2H7N-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.98085e+08,'cm^3/(mol*s)'), n=1.22191, Ea=(-78.8037,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.996332219215656,B=1.029302623121347,E=1.007550487792502,L=7.3685642232941575,A=0.4814345945968402,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]N(C)C + [H] <=> [Li] + CNC
TS method summary for TS5 in [Li]N(C)C + [H] <=> [Li] + CNC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li     -0.01255156   -2.15540609    0.17281461
C      -1.18904595    0.48655227   -0.00173058
N      -0.00119847   -0.32330655    0.13512720
C       1.19572522    0.47240045   -0.00552380
H      -1.29496161    1.17270913    0.84939970
H      -2.08251863   -0.14341129   -0.03173585
H      -1.18193779    1.09526007   -0.91713761
H      -0.00888523   -1.23541538   -1.24714949
H       2.08165534   -0.16803921   -0.03714132
H       1.31181522    1.15820060    0.84456073
H       1.19338693    1.08020408   -0.92156070

1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [6, 1, 3, 2], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [2, 3], dihedral: [9, 2, 3, 1], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1057.5062115419946 J/mol
""",
)

entry(
    index = 4,
    label = "C2H5 + CH4LiN <=> C3H9N + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(57.4636,'cm^3/(mol*s)'), n=2.93295, Ea=(29.2672,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9175438008860265,B=1.1395826064596657,E=0.4944811262263229,L=5.415263196320309,A=0.6943364764189893,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NC + C[CH2] <=> [Li] + CNCC
TS method summary for TS6 in [Li]NC + C[CH2] <=> [Li] + CNCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.86285000   -3.43375100    2.79902300
C       0.98777800   -2.65086100   -0.09382000
N       0.71786100   -3.57279300    1.00412300
C       2.58209000   -4.54615500    1.38240100
C       2.51791600   -5.74331000    0.47224200
H       1.57842000   -1.80331500    0.26902300
H       0.06101000   -2.23833800   -0.51244300
H       1.54339700   -3.11115800   -0.92583100
H       0.23428600   -4.38822600    0.63186500
H       2.73940400   -4.78839100    2.43474500
H       3.21675900   -3.72761600    1.05622300
H       2.23662900   -5.46469700   -0.54831800
H       1.79544000   -6.48501400    0.82582800
H       3.48948500   -6.25526200    0.40261200

1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 1], rotor symmetry: 3, max scan energy: 7.27 kJ/mol
pivots: [4, 5], dihedral: [10, 4, 5, 12], rotor symmetry: 1, max scan energy: 4.84 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1827.7398650288437 J/mol
""",
)

entry(
    index = 5,
    label = "CH3 + C2H6LiN-2 <=> C3H9N-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(563.399,'cm^3/(mol*s)'), n=2.71918, Ea=(25.4344,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.877486735996646,B=0.6916407047808263,E=0.748415650862252,L=5.385263016210897,A=0.5210754074032086,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NCC + [CH3] <=> [Li] + CNCC
TS method summary for TS7 in [Li]NCC + [CH3] <=> [Li] + CNCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.05606100   -3.45546000    2.01224800
C       1.02585900   -2.12623900    0.34507400
N       1.00888800   -4.16659200    0.73566500
C       2.41249300   -4.57313800    0.74711200
C       2.59339300   -6.09431100    0.80785700
H       1.60805900   -1.64413200    1.12608300
H       0.03900700   -1.69160400    0.19949800
H       1.57322900   -2.25185000   -0.58111600
H       0.59390100   -4.45373900   -0.15068400
H       2.88943300   -4.12236900    1.62589400
H       2.95316600   -4.18843300   -0.13225800
H       2.14825000   -6.57778000   -0.06703100
H       2.11573400   -6.50891300    1.69885700
H       3.65797100   -6.35433100    0.83047600

1D rotors:
pivots: [3, 4], dihedral: [1, 3, 4, 5], rotor symmetry: 1, max scan energy: 23.37 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 12], rotor symmetry: 3, max scan energy: 13.57 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1425.8896370647562 J/mol
""",
)

entry(
    index = 6,
    label = "H + C3H8LiN <=> C3H9N-3 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.33693e+09,'cm^3/(mol*s)'), n=1.12822, Ea=(-71.4349,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.1131935806214712,B=1.1556454917670655,E=1.2169728270193971,L=7.839572648134702,A=0.31656236651087616,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]N(C)CC + [H] <=> [Li] + CNCC
TS method summary for TS8 in [Li]N(C)CC + [H] <=> [Li] + CNCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.33837900   -4.64647900    1.22723600
C       1.24491900   -2.34667300    0.49201700
N       1.21107200   -3.75746400    0.84374800
C       2.49783000   -4.39820300    0.61837300
C       2.47997100   -5.87080600    1.02075500
H       1.87369600   -1.78539800    1.19871100
H       0.23758500   -1.91968100    0.53084900
H       1.64161700   -2.16740400   -0.51925300
H       0.20877800   -4.39361800   -0.34456500
H       3.26953700   -3.86937200    1.20156400
H       2.80323700   -4.30928200   -0.43751400
H       1.74538600   -6.42456000    0.42730500
H       2.23250200   -5.98351400    2.08218500
H       3.45557400   -6.33643600    0.85626200

1D rotors:
* Invalidated! pivots: [1, 3], dihedral: [7, 1, 3, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molCould not read energies
pivots: [2, 4], dihedral: [10, 2, 4, 3], rotor symmetry: 1, max scan energy: 26.26 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 2], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molCould not read energies
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1071.2824706634553 J/mol
""",
)

entry(
    index = 7,
    label = "H + HLiO <=> H2O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.03649e+11,'cm^3/(mol*s)'), n=0.812216, Ea=(-21.6525,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6576610150461983,B=2.4435784684265482,E=0.404796645816695,L=7.698368077501874,A=0.9750486732350473,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O + [H] <=> [Li] + O
TS method summary for TS9 in [Li]O + [H] <=> [Li] + O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.28826489    0.18010119    0.00207350
O      -0.36733064    0.11184220    0.00745957
H       0.39396705   -1.32898954   -0.00633395
H      -1.27901258   -0.17912694    0.00905353


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2114.547977695349 J/mol
""",
)

entry(
    index = 8,
    label = "H + H2LiN <=> H3N + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.12322e+09,'cm^3/(mol*s)'), n=1.12657, Ea=(-57.4909,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9471505265788214,B=1.7274624400621788,E=0.6115119617819315,L=6.871072605917964,A=0.6704069036466952,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]N + [H] <=> [Li] + N
TS method summary for TS10 in [Li]N + [H] <=> [Li] + N:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.91584700    2.00773900   -1.02886800
N       1.72410800    0.79367700    0.30433400
H       3.35327200    1.38343900   -0.34462600
H       1.91932800    0.99397300    1.28417000
H       1.91839100   -0.20073000    0.19609500


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1435.1628987975923 J/mol
""",
)

entry(
    index = 9,
    label = "H + CH3LiO <=> CH4O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.47113e+11,'cm^3/(mol*s)'), n=0.774968, Ea=(-24.6724,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.4067121409688057,B=1.4628968939845368,E=0.9656443938025181,L=7.661570379273675,A=0.443175955652443,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC + [H] <=> [Li] + CO
TS method summary for TS11 in [Li]OC + [H] <=> [Li] + CO:
Methods that successfully generated a TS guess:
user guess 0,user guess 0,
The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      2.05286763    0.11494012   -0.00863872
O       0.38320517    0.12959365   -0.00264163
C      -1.00062168   -0.00723588   -0.00489942
H       0.96172040   -1.23025812    0.00873654
H      -1.46633645    0.98431418   -0.00871499
H      -1.35936775   -0.54162168    0.88336582
H      -1.35623697   -0.54719021   -0.89107706

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 0.65 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1321.823066484516 J/mol
""",
)

entry(
    index = 10,
    label = "CH3 + HLiO <=> CH4O-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07712e+06,'cm^3/(mol*s)'), n=2.28023, Ea=(85.5904,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.4173362998736376,B=2.357499252462657,E=0.5167298959343533,L=7.9017680525604375,A=1.0064038665607862,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O + [CH3] <=> [Li] + CO
TS method summary for TS12 in [Li]O + [CH3] <=> [Li] + CO:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li     -0.28748200   -0.18010600    1.00319500
O       0.86993900    0.39784300   -0.11608000
C       2.59811800   -0.51057100   -0.06290500
H       0.96229700    1.06152900   -0.80658800
H       3.25030100    0.31559600    0.18187100
H       2.64875300   -0.90201200   -1.06889700
H       2.43978600   -1.23892300    0.72228500


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2046.4105178239631 J/mol
""",
)

entry(
    index = 11,
    label = "H + CH4LiN <=> CH5N + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.62458e+07,'cm^3/(mol*s)'), n=1.49444, Ea=(-71.5589,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-5.4761368991675985,B=-6.829449919467144,E=14.43663245128814,L=28.957970295010895,A=0.4259943743771139,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NC + [H] <=> [Li] + CN
TS method summary for TS13 in [Li]NC + [H] <=> [Li] + CN:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.97896700    2.55914500   -0.24504500
N       1.69265600    1.43053300    0.36161000
C       1.63546400   -0.02844300    0.34543400
H       3.12243000    1.84764100    1.28691400
H       1.03626400    1.77345000    1.06081000
H       2.44491900   -0.42885900   -0.27310200
H       0.69075100   -0.38108300   -0.09139200
H       1.72952400   -0.48126300    1.34115700

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 8], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 4708.787281816518 J/mol
""",
)

entry(
    index = 12,
    label = "C2H5 + HLiO <=> C2H6O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(26.5507,'cm^3/(mol*s)'), n=3.72095, Ea=(84.1068,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9913576154323054,B=3.1755887609180435,E=-0.2623364392566645,L=7.244831699370673,A=0.5572363451823703,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O + C[CH2] <=> [Li] + CCO
TS method summary for TS15 in [Li]O + C[CH2] <=> [Li] + CCO:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -2.57304700    0.27516400   -0.65750400
C       1.54543100   -0.31294900   -0.20991200
C       0.50691500    0.68250500    0.19066600
O      -1.20609000   -0.34489700    0.18644900
H       1.31703400   -0.75838900   -1.18091300
H       2.53974800    0.15487200   -0.28938100
H       1.63329600   -1.12303200    0.51949300
H       0.22894600    1.43785900   -0.53575000
H       0.48492400    1.02184600    1.21876200
H      -1.09958300   -1.00876300    0.87538500

1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 8], rotor symmetry: 3, max scan energy: 5.59 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1614.986893512281 J/mol
""",
)

entry(
    index = 13,
    label = "H + C2H5LiO <=> C2H6O-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.77483e+09,'cm^3/(mol*s)'), n=1.18598, Ea=(-23.16,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-8.623486006056842,B=14.917486429580572,E=-5.719694357458241,L=40.120001635540106,A=-6.502228345652631,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCC + [H] <=> [Li] + CCO
TS method summary for TS16 in [Li]OCC + [H] <=> [Li] + CCO:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.49143616    0.55729277   -0.12525674
C      -1.41113872    0.44040349   -0.02571704
C      -0.33003762   -0.62547457    0.03698411
O       0.94967788   -0.09370527   -0.11768223
H      -1.37208971    0.96882848   -0.98064514
H      -2.40427692   -0.00332329    0.08351568
H      -1.26743662    1.17043881    0.77319839
H      -0.49296294   -1.36694873   -0.75554854
H      -0.39930548   -1.16567232    0.99075815
H       1.34235779    0.48281906    1.16520496

1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 4], rotor symmetry: 3, max scan energy: 13.87 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 1], rotor symmetry: 1, max scan energy: 0.52 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1.736364652060729e-05 J/mol
""",
)

entry(
    index = 14,
    label = "C2H5 + H2LiN <=> C2H7N-3 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.337329,'cm^3/(mol*s)'), n=3.54967, Ea=(34.4127,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.6195332200790409,B=2.120893670736446,E=10.142480436000628,L=-0.8781474558081529,A=3.410407959634951,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]N + C[CH2] <=> [Li] + CCN
TS method summary for TS17 in [Li]N + C[CH2] <=> [Li] + CCN:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      2.24111023    0.88861561    0.00000000
C      -1.53683978   -0.23464256    0.00000000
C      -0.36949484    0.70943914    0.00000000
N       1.25313058   -0.61428298    0.00000000
H      -1.53341411   -0.88051875   -0.88086808
H      -2.49375547    0.30282603    0.00000000
H      -1.53341411   -0.88051875    0.88086808
H      -0.26776509    1.30799358   -0.90233509
H      -0.26776509    1.30799358    0.90233509
H       1.01858967   -1.18352112   -0.80784057
H       1.01858967   -1.18352112    0.80784057

1D rotors:
pivots: [2, 3], dihedral: [5, 2, 3, 8], rotor symmetry: 3, max scan energy: 4.88 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2191.6345368658176 J/mol
""",
)

entry(
    index = 15,
    label = "CH3 + CH3LiO <=> C2H6O-3 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3026.56,'cm^3/(mol*s)'), n=2.80221, Ea=(80.834,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.223920620501668,B=0.8264175269682525,E=0.40415741933873844,L=5.605210034978575,A=0.4397271958947774,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC + [CH3] <=> [Li] + COC
TS method summary for TS1 in [Li]OC + [CH3] <=> [Li] + COC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      6.51706400   -1.13632600   -3.21539400
C       4.02423400   -1.41606000   -2.34418400
O       5.56418700   -0.34050500   -2.05108800
C       5.26882800    0.60085300   -1.05050100
H       3.90830800   -1.82877700   -1.35110600
H       4.26586000   -2.13817000   -3.11854700
H       3.32573800   -0.64407500   -2.63764800
H       4.99996100    0.11042200   -0.10400400
H       4.43692100    1.25540800   -1.34741500
H       6.14543300    1.23014000   -0.86797000

1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [1, 3, 4, 8], invalidation reason: Two consecutive points are inconsistent by more than 1.40 kJ/molTwo consecutive points are inconsistent by more than 1.52 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1526.5386694571223 J/mol
""",
)

entry(
    index = 16,
    label = "CH3 + C2H5LiO <=> C3H8O-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.09569,'cm^3/(mol*s)'), n=3.2546, Ea=(82.2788,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.091886494292463,B=0.5254418313743373,E=1.2963729646265112,L=5.721969023897385,A=0.6575614317431779,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCC + [CH3] <=> [Li] + COCC
TS method summary for TS3 in [Li]OCC + [CH3] <=> [Li] + COCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li     -2.74010800   -4.87944000   -2.74685100
C      -2.29023200   -1.71339600   -1.09005000
C      -3.11923600   -1.87939400   -2.35977600
O      -3.12657200   -3.21901700   -2.79202100
C      -4.17095700   -3.35427200   -4.36839000
H      -1.25332700   -2.01355600   -1.26099300
H      -2.69616100   -2.32265000   -0.27855700
H      -2.29596500   -0.66546600   -0.76876900
H      -4.14967400   -1.54173400   -2.17015500
H      -2.70920200   -1.23314600   -3.15098300
H      -3.61682000   -2.67724300   -5.00431900
H      -5.11687000   -2.99859300   -3.98292400
H      -4.16500100   -4.39266700   -4.68634200

1D rotors:
pivots: [2, 3], dihedral: [6, 2, 3, 4], rotor symmetry: 3, max scan energy: 15.23 kJ/mol
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 1], invalidation reason: Two consecutive points are inconsistent by more than 6.75 kJ/molTwo consecutive points are inconsistent by more than 6.75 kJ/molTwo consecutive points are inconsistent by more than 6.64 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1616.2708289398845 J/mol
""",
)

entry(
    index = 17,
    label = "CH3 + H2LiN <=> CH5N-2 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5347.09,'cm^3/(mol*s)'), n=2.59727, Ea=(34.8806,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.8306578175990244,B=1.956506108230911,E=0.011774617070094268,L=6.100850860272114,A=1.0441801517777485,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]N + [CH3] <=> [Li] + CN
TS method summary for TS14 in [Li]N + [CH3] <=> [Li] + CN:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      2.40811800    2.01328500   -0.85438200
N       2.11561000    1.83611700    0.90968800
C       1.73450000   -0.09747600    0.20605700
H       2.80524200    1.62458700    1.63010700
H       1.24512600    2.01206100    1.41033200
H       2.64014000   -0.51618000   -0.22479700
H       0.88533500   -0.08035300   -0.47199800
H       1.49690500   -0.50092000    1.18138200


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 3733.7594052313543 J/mol
""",
)

entry(
    index = 18,
    label = "H + C2H6LiN-2 <=> C2H7N-4 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89074e+07,'cm^3/(mol*s)'), n=1.63253, Ea=(-67.2986,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.9852422925798727,B=1.2991389460904967,E=1.413033851489418,L=7.445245509701895,A=0.5371087291175491,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NCC + [H] <=> [Li] + CCN
TS method summary for TS18 in [Li]NCC + [H] <=> [Li] + CCN:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      4.96386900    0.59677000   -2.24670800
C       1.28798200   -0.93517900   -1.41482700
C       2.04070800    0.34605900   -1.78351100
N       3.41953300    0.41063200   -1.30736000
H       1.79730100   -1.80886900   -1.82862700
H       0.26120100   -0.91416400   -1.79495900
H       1.23888400   -1.05694700   -0.32722800
H       2.04864400    0.45971700   -2.87498700
H       1.48295900    1.21378300   -1.39663000
H       4.25148700   -0.92956300   -2.05992500
H       3.45414500    0.04969200   -0.35434500

1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 14.10 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 11], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1260.011897897355 J/mol
""",
)

entry(
    index = 19,
    label = "C4H10O2 + Li <=> C3H7LiO2 + CH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(62816.3,'cm^3/(mol*s)'), n=2.80799, Ea=(51.0438,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: COCCOC + [Li] <=> [Li]OCCOC + [CH3]
TS method summary for TS8 in COCCOC + [Li] <=> [Li]OCCOC + [CH3]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      3.39566800   -2.31746100   -6.27790800
C       6.61867600    1.61571200   -3.37584500
O       6.51399400    1.21245700   -4.72654400
C       5.55433000    0.18656100   -4.92836400
C       5.53861300   -0.15531900   -6.41417600
O       4.59984900   -1.17164200   -6.66983100
C       4.61304200   -1.56339100   -8.51793500
H       7.37522700    2.39972300   -3.32963700
H       6.92765900    0.78165200   -2.72975800
H       5.66584700    2.01521300   -3.00024800
H       4.55644800    0.52370000   -4.61045200
H       5.81471700   -0.70639700   -4.34072100
H       6.54752300   -0.47222600   -6.71292000
H       5.29389200    0.75333700   -6.98165600
H       3.88299800   -2.34830900   -8.69194200
H       5.64580400   -1.86472100   -8.62906800
H       4.34337200   -0.59145000   -8.90826500

1D rotors:
pivots: [2, 3], dihedral: [8, 2, 3, 4], rotor symmetry: 3, max scan energy: 9.81 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 28.73 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: Another conformer for TS8 exists which is 32.05 kJ/mol lower.Two consecutive points are inconsistent by more than 13.53 kJ/molAnother conformer for TS8 exists which is 32.05 kJ/mol lower. But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 1], invalidation reason: Two consecutive points are inconsistent by more than 6.99 kJ/molTwo consecutive points are inconsistent by more than 6.99 kJ/molTwo consecutive points are inconsistent by more than 6.85 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

