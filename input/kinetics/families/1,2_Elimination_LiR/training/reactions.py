#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Elimination_LiR"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH2LiO2 <=> CHO + HLiO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.59528e+12,'s^-1'), n=0.518458, Ea=(46.6821,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.7137053723954238,B=2.3116450623393274,E=-0.028001584137479975,L=6.399784910596449,A=1.0368467911904864,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O[CH]O <=> O=[CH] + [Li]O
TS method summary for TS3 in [Li]O[CH]O <=> O=[CH] + [Li]O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.87424500    0.73974100    0.09129300
O       1.75669700   -0.86642000    0.56373200
C       2.58297500   -1.53104300    1.11098800
O       4.34504900    0.32811600    0.72907500
H       3.18306800   -1.22575300    1.99446700
H       5.29067900    0.34100400    0.85554700


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1999.2439277651972 J/mol
""",
)

entry(
    index = 1,
    label = "C3H4LiO3 <=> CO2 + C2H4LiO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.8039e+12,'s^-1'), n=0.472198, Ea=(80.6393,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.697605152955986,B=2.4862812293190593,E=-4.1974148204255775,L=2.872587466227873,A=0.9296666032597313,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC(=O)OC[CH2] <=> [Li]OC[CH2] + O=C=O
TS method summary for TS5 in [Li]OC(=O)OC[CH2] <=> [Li]OC[CH2] + O=C=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.96701700   -1.13824900   -0.15895200
O      -2.46633000   -0.36661300    0.95261900
C      -2.69790600    0.67181500    1.43609500
O      -2.94565100    1.68669600    1.92040500
O       0.40069800   -0.49898400   -0.72233300
C       1.57073700    0.05670900   -1.18237000
C       2.36317900    0.78094900   -0.14406400
H       3.22407400    1.38251500   -0.42071200
H       1.38606500    0.76055700   -2.02340400
H       2.23211500   -0.72124600   -1.63365600
H       2.17387800    0.59315200    0.90679500

1D rotors:
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 7], invalidation reason: Could not read energies
pivots: [6, 7], dihedral: [5, 6, 7, 8], rotor symmetry: 6, max scan energy: 2.96 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2756.9521557186627 J/mol
""",
)

entry(
    index = 2,
    label = "C2H3LiO3 <=> CO2 + CH3LiO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.20441e+16,'s^-1'), n=0.126298, Ea=(88.7875,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC(=O)OC <=> [Li]OC + O=C=O
TS method summary for TS6 in [Li]OC(=O)OC <=> [Li]OC + O=C=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      5.04185400   -0.21852400   -0.03835700
O       3.25247800   -1.11583300   -0.33860900
C       2.36548400   -0.96686600   -1.08434100
O       1.48076300   -0.83623400   -1.81011400
O       5.78339200    1.00550600   -0.77059600
C       6.45425100    2.04955800   -1.36939800
H       6.65054600    1.86707100   -2.44274400
H       7.43841500    2.24421200   -0.90374600
H       5.89254200    3.00108300   -1.31473500

1D rotors:
pivots: [5, 6], dihedral: [1, 5, 6, 7], rotor symmetry: 1, max scan energy: 0.04 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

entry(
    index = 3,
    label = "CH3LiO2 <=> CH2O + HLiO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.67089e+11,'s^-1'), n=0.423598, Ea=(30.5741,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-0.3926746359480871,B=2.430874130082185,E=1.0969664301003625,L=5.26139300991494,A=1.5271891998852951,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCO <=> [Li]O + C=O
TS method summary for TS1 in [Li]OCO <=> [Li]O + C=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.78877200    1.23956200    0.07241700
O       1.16034300    1.22721100    0.06023400
C       1.39171400    0.02905600    0.10137600
O      -1.23386700   -0.34577400   -0.14916500
H       2.09301700   -0.42740500   -0.61722300
H       0.93534900   -0.62824800    0.84977000
H      -1.80092200   -1.09439000   -0.31740600


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2852.7605391591824 J/mol
""",
)

entry(
    index = 4,
    label = "CH2FLiO <=> CH2O + FLi",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.47928e+13,'s^-1'), n=0.0523532, Ea=(1.77399,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.2544775378071295,B=3.8435703486608483,E=0.6208281974105191,L=9.542895814948176,A=0.874941113523824,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCF <=> [Li]F + C=O
TS method summary for TS8 in [Li]OCF <=> [Li]F + C=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.73637500   -1.17722200    0.05547000
O      -1.11732500   -0.58062100   -0.02059700
C      -0.94937700    0.62629300    0.04611900
F       1.57678000    0.22561600   -0.04626600
H      -0.44153100    1.10232800    0.89325700
H      -1.33358500    1.29011400   -0.74570300


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2167.4878926153538 J/mol
""",
)

entry(
    index = 5,
    label = "CH2ClLiO <=> CH2O + ClLi",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.03509e+13,'s^-1'), n=-0.00858289, Ea=(0.072948,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.49973283735009,B=-1.363801515776159,E=11.671483182052631,L=9.85481016575309,A=1.7632374622781073,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OCCl <=> [Li]Cl + C=O
TS method summary for TS9 in [Li]OCCl <=> [Li]Cl + C=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.00585826   -1.37546289    0.07580004
O      -1.70390800   -0.51267720   -0.03767821
C      -1.46459925    0.68381718    0.02582362
Cl      1.51931730    0.06620772    0.01568653
H      -1.66736974    1.34639439   -0.82976904
H      -1.07809033    1.15217907    0.94055248

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 3473.2666466033193 J/mol
""",
)

entry(
    index = 6,
    label = "Li2O + CH2O <=> CH2Li2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(60668.5,'cm^3/(mol*s)'), n=2.48558, Ea=(-44.9325,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-6.237601960913579,B=9.474105452618263,E=1.6329134231750524,L=15.17499274807221,A=3.5783211118513525,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O[Li] + O=C <=> [Li]OCO[Li]
TS method summary for TS7 in [Li]O[Li] + O=C <=> [Li]OCO[Li]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 2, TS optical isomers: 1

Optimized TS geometry:
Li      5.26122200   -2.16488900   -1.43635000
O       4.16581000   -1.00650700   -0.36650500
C       3.47523600   -0.27668500    0.30751600
O       6.20422100   -3.16227700   -2.35757800
Li      7.12770800   -4.13885600   -3.25991800
H       3.91701800    0.40191100    1.05639300
H       2.37777900   -0.26233900    0.19860600


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 6992.493889350707 J/mol
""",
)

entry(
    index = 7,
    label = "C2H5Li <=> C2H4 + HLi",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.20882e+11,'s^-1'), n=0.349755, Ea=(9.42179,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.7309852404322288,B=2.3232904077453425,E=0.8831500260776306,L=9.72969334125182,A=0.8794516433866466,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]CC <=> C=C + [Li][H]
TS method summary for TS1 in [Li]CC <=> C=C + [Li][H]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.61403700    1.76672400   -0.70523200
C       3.74739900    0.26828100   -0.29006800
C       3.52138200    0.70505900    1.17932700
H       4.80154100    0.39826200   -0.56515800
H       3.51666300   -0.79317000   -0.40677400
H       3.24455300    1.78628400    1.30105800
H       4.38360300    0.59677300    1.85446400
H       2.69158000    0.15525900    1.63951800

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [4, 1, 2, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2061.526158269488 J/mol
""",
)

entry(
    index = 8,
    label = "CH4LiN <=> CH3N + HLi",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.20406e+11,'s^-1'), n=0.395823, Ea=(4.40595,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.708205772421329,B=2.5356143801240445,E=0.23679859997568953,L=9.472880397262012,A=1.0783864304846873,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]NC <=> N=C + [Li][H]
TS method summary for TS3 in [Li]NC <=> N=C + [Li][H]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.98746585   -0.52738947   -0.00361624
N       0.45147254    0.30262629    0.00522525
C      -0.92611851   -0.15975163    0.00259877
H       0.43824316    1.31338637    0.01447592
H      -1.17387633   -0.78335004    0.87699274
H      -1.17511304   -0.76926072   -0.88130944
H      -1.65482009    0.66025357    0.00967177

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2139.3398223085746 J/mol
""",
)

entry(
    index = 9,
    label = "C2H4LiO2 <=> CHO + CH3LiO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.54823e+14,'s^-1'), n=0.356617, Ea=(65.3953,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O[CH]OC <=> O=[CH] + [Li]OC
TS method summary for TS4 in [Li]O[CH]OC <=> O=[CH] + [Li]OC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      3.11938200    0.00580200    2.75259500
O       1.62524600   -0.33884700    1.46544000
C       1.40627800   -0.20972400    0.31263200
O       4.61316700    0.60600100    2.66739200
C       5.89388500    1.11128900    2.64427900
H       2.12421500    0.21023400   -0.43421800
H       6.36930700    1.11127900    3.64324000
H       5.93134700    2.15747800    2.28506200
H       6.56678700    0.53303700    1.98263000

1D rotors:
pivots: [4, 5], dihedral: [1, 4, 5, 7], rotor symmetry: 1, max scan energy: 0.04 kJ/mol (set as a FreeRotor)
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

