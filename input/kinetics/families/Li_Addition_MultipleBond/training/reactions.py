#!/usr/bin/env python
# encoding: utf-8

name = "Li_Addition_MultipleBond/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH3LiN <=> CH3N + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.3493e+15,'s^-1'), n=-0.259789, Ea=(57.8699,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.65419313965326,B=1.2542197583042969,E=-0.21990942778263972,L=-9.14111680402368,A=3.645314481406821,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]N[CH2] <=> [Li] + N=C
TS method summary for TS5 in [Li]N[CH2] <=> [Li] + N=C:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      6.05139304   -0.13209844    0.04731853
N      -0.59090151    0.44974234   -0.13918199
C      -1.50102245   -0.40751439    0.06649375
H      -0.84130096    1.35681132    0.26234830
H      -2.43737623   -0.21216607    0.60231309
H      -1.36253440   -1.42264825   -0.30947313


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 9225.750515830967 J/mol
""",
)

entry(
    index = 2,
    label = "CH2LiO <=> CH2O + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.12946e+16,'s^-1'), n=-0.125312, Ea=(91.4067,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-0.4735938637413528,B=2.67486764340657,E=-5.09678040094995,L=-4.876934525239067,A=3.9944267641274602,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O[CH2] <=> [Li] + C=O
TS method summary for TS2 in [Li]O[CH2] <=> [Li] + C=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      5.94953985   -0.41297703   -0.17000001
O      -1.44709358   -0.51595384   -0.58748736
C      -0.51807902   -0.11636709    0.05072105
H      -0.34294039    0.96399341    0.21662004
H       0.21655881   -0.80519630    0.51008017


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 9134.820807836515 J/mol
""",
)

entry(
    index = 3,
    label = "C3H4LiO3 <=> C3H4O3 + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.54076e+14,'s^-1'), n=-0.182294, Ea=(23.9219,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.018725993417632,B=4.93569039446143,E=-4.315782362402726,L=-1.68464261284562,A=3.5698295734222367,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]O[C]1OCCO1 <=> [Li] + O=C1OCCO1
TS method summary for TS2 in [Li]O[C]1OCCO1 <=> [Li] + O=C1OCCO1:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      2.19853800   -1.72038300   -0.07266600
O       1.76667000    0.85234100    0.00624500
C       0.64157500    0.45596800    0.00446400
O       0.35500500   -0.88546600   -0.06754100
C      -1.07057700   -1.09977700    0.11070100
C      -1.63216600    0.30832100   -0.11252500
O      -0.48175500    1.17430200    0.07309300
H      -1.23031400   -1.47803000    1.12084400
H      -1.39532400   -1.83156700   -0.62695100
H      -2.00519600    0.46029600   -1.12605700
H      -2.38753000    0.59754200    0.61515000


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 10990.041834280188 J/mol
""",
)

entry(
    index = 4,
    label = "C2H4 + Li <=> C2H4Li",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.10799e+08,'cm^3/(mol*s)'), n=1.74038, Ea=(37.7145,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: C=C + [Li] <=> [Li]C[CH2]
TS method summary for TS12 in C=C + [Li] <=> [Li]C[CH2]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.32478100    0.48677200   -2.28010300
C       0.66699000    0.47764200    0.12534900
C       1.96387400    0.14162800   -0.10323100
H      -0.11605000   -0.27260900    0.16841800
H       0.36914100    1.50519600    0.30784300
H       2.27746800   -0.89206400   -0.20216200
H       2.76028000    0.87702100   -0.06342100


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

