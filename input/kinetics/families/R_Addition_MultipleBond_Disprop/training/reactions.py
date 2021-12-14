#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond_Disprop/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3H4LiO3 + Li <=> CLi2O3 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.23949e+06,'cm^3/(mol*s)'), n=2.34337, Ea=(16.2698,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-1.3791416734787092,B=0.9825775784337702,E=1.344561385839825,L=1.6867692078977448,A=2.9918711355986547,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC(=O)OC[CH2] + [Li] <=> C=C + [Li]OC(=O)O[Li]
TS method summary for TS1 in [Li]OC(=O)OC[CH2] + [Li] <=> C=C + [Li]OC(=O)O[Li]:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      1.87425800   -2.04299200   -3.07332600
Li      1.24014100   -0.15538500   -1.27249500
O       2.82154600    0.46235800   -0.47530800
C       3.50085500   -0.32785200   -1.18110600
O       2.93902200   -1.11785300   -2.03089600
O       4.79372500   -0.30481500   -1.00802000
C       5.85165800   -1.68424300   -2.25495500
C       7.14070000   -1.45297600   -1.87549700
H       7.58629300   -1.98304400   -1.04193200
H       7.73833200   -0.68372700   -2.35031200
H       5.44554600   -1.22113500   -3.14361200
H       5.29429900   -2.51368000   -1.84205000

1D rotors:
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 1], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molTwo consecutive points are inconsistent by more than 1.98 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [11, 7, 8, 9], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 8067.650715137258 J/mol
""",
)

entry(
    index = 2,
    label = "C4H6N + Li <=> C2H2LiN + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(162517,'cm^3/(mol*s)'), n=2.55635, Ea=(59.4607,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: N#CCC[CH2] + [Li] <=> C=C + [Li]N=C=C
TS method summary for TS4 in N#CCC[CH2] + [Li] <=> C=C + [Li]N=C=C:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      2.20866700   -3.26362100    0.69535500
N       2.76324600   -1.36738800    0.52284100
C       3.08763300   -0.25769800    0.42194700
C       3.55202200    1.05372200    0.27042400
C       5.61636500    0.76198000   -0.55956300
C       6.13960300    2.01125800   -0.73612200
H       5.99188800    2.56160300   -1.65835400
H       6.67588100    2.51773700    0.05829500
H       3.80464300    1.58961900    1.17622700
H       3.12229100    1.63338000   -0.53630400
H       5.22760700    0.20947200   -1.40717800
H       5.90695700    0.16590300    0.29781600


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

entry(
    index = 3,
    label = "C3H5O2 + Li <=> CHLiO2 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(419384,'cm^3/(mol*s)'), n=2.21898, Ea=(48.2832,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.0247091484586592,B=2.5777645372278832,E=0.3431344611927818,L=9.346538089381045,A=0.8860009592023523,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: O=COC[CH2] + [Li] <=> C=C + [Li]OC=O
TS method summary for TS5 in O=COC[CH2] + [Li] <=> C=C + [Li]OC=O:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      1.47146600    0.74106900    0.34679500
O       1.74203700   -0.90158000   -0.33076200
C       3.01837200   -0.90979200    0.01521300
O       3.16343900    0.14671400    0.94399000
C       5.05439400    1.01094500    0.89916500
C       5.82789100    0.09990700    1.55097100
H       6.29799000   -0.71908900    1.01934900
H       5.93637200    0.12012200    2.62899600
H       3.47455200   -1.85913300    0.33255600
H       5.03391400    1.04006800   -0.18277800
H       4.67644000    1.88053200    1.42227500

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [10, 5, 6, 7], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2119.3556871894884 J/mol
""",
)

entry(
    index = 4,
    label = "C3H5O2-2 + Li <=> C2H3LiO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.74272e+07,'cm^3/(mol*s)'), n=2.05933, Ea=(-27.3358,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.2490249849978214,B=2.6960753668589854,E=2.1706425235190108,L=14.985510873166351,A=0.7334126588566799,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: O=CCC[O] + [Li] <=> O=C + [Li]OC=C
TS method summary for TS6 in O=CCC[O] + [Li] <=> O=C + [Li]OC=C:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li     -0.12483600    1.05743400   -1.25410700
O       1.46505300    0.73245600   -1.16275100
C       2.74034000    0.37502600   -1.09913800
C       3.04331700   -0.78995100   -0.24359400
C       5.23224300   -1.20192000   -0.57446500
O       5.53528300   -2.13497400    0.16495700
H       3.49482900    1.15012100   -1.25222600
H       3.09995100   -0.67302800    0.84369900
H       2.69585800   -1.77304600   -0.55668300
H       5.44674400   -0.15439900   -0.29353200
H       4.98321600   -1.36209900   -1.63871500

1D rotors:
pivots: [2, 3], dihedral: [1, 2, 3, 4], rotor symmetry: 1, max scan energy: 0.15 kJ/mol (set as a FreeRotor)
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 8], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1868.0308622468697 J/mol
""",
)

entry(
    index = 5,
    label = "C3H7N2 + Li <=> C2H4LiN + CH3N",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.45437e+09,'cm^3/(mol*s)'), n=0.869935, Ea=(-36.817,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: N=CCN[CH2] + [Li] <=> N=C + [Li]NC=C
TS method summary for TS9 in N=CCN[CH2] + [Li] <=> N=C + [Li]NC=C:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      1.43792400    2.18346800    3.13495900
N       1.34945800    2.03367400    1.29552300
C       1.99493600    1.25306300    0.41510400
C       2.96296800    0.23412800    0.92093300
N       4.27184500    0.83660900    1.22913800
C       5.23741200    0.10972200    1.89794800
H       5.27720600   -0.95423700    1.69896300
H       6.15316900    0.62651600    2.15482900
H       0.80698400    2.74089000    0.80369300
H       1.97804700    1.46965400   -0.65057600
H       3.11843300   -0.55503700    0.17739200
H       2.55868300   -0.25464600    1.82436900
H       4.22048000    1.82091600    1.45401500

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [3, 4], dihedral: [2, 3, 4, 5], invalidation reason: Could not read energies
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 7], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

entry(
    index = 6,
    label = "C4H9O2S + Li <=> C2H5LiO2S + C2H4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(312580,'cm^3/(mol*s)'), n=2.72776, Ea=(68.0852,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: O=S(=O)(C)CC[CH2] + [Li] <=> C=C + [Li]OS(=O)(=C)C
TS method summary for TS1 in O=S(=O)(C)CC[CH2] + [Li] <=> C=C + [Li]OS(=O)(=C)C:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
Li      0.23360500   -0.43826800    1.05757300
O       1.85305100   -0.48614800    0.18589400
S       3.03288500    0.16000500   -0.45526700
O       4.11761400   -0.69474000   -0.93728000
C       2.38600100    1.10779500   -1.85159000
C       3.67254200    1.32635100    0.68881200
C       4.48291700   -0.08700100    2.46471000
C       5.08941300    0.77695100    3.31110200
H       4.54151500    1.26621700    4.10890900
H       6.13803800    1.03308600    3.20640600
H       1.96675400    0.37577700   -2.54325400
H       3.21334900    1.64592300   -2.31400900
H       1.61020800    1.78181000   -1.48749800
H       2.93045600    1.89337800    1.23838600
H       4.61031100    1.78138900    0.39657800
H       3.46456700   -0.41452700    2.64278500
H       5.05211100   -0.65010600    1.73396300

1D rotors:
* Invalidated! pivots: [2, 3], dihedral: [1, 2, 3, 4], invalidation reason:
pivots: [3, 6], dihedral: [2, 3, 6, 14], rotor symmetry: 1, max scan energy: 14.75 kJ/mol
pivots: [3, 5], dihedral: [2, 3, 5, 11], rotor symmetry: 3, max scan energy: 10.77 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [16, 7, 8, 9], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)
""",
)

entry(
    index = 7,
    label = "C4H7O + C2H5 <=> C4H8O + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00014888,'cm^3/(mol*s)'), n=4.19462, Ea=(96.1568,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.249762479827305,B=0.15073926135565738,E=0.365495135486543,L=3.0529218751533116,A=-0.05234289083492228,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: O=CCC[CH2] + C[CH2] <=> C=C + CCOC=C
TS method summary for TS2 in O=CCC[CH2] + C[CH2] <=> C=C + CCOC=C:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       1.80499000   -0.31672700   -0.13698200
C       3.11562500   -0.58331900    0.57687900
H       2.96837500   -0.64397400    1.66347700
H       3.84416000    0.21178900    0.37787500
O       3.64516200   -1.82826200    0.10708300
C       4.79558600   -2.24513600    0.72170700
C       5.33927400   -3.54792400    0.32389400
C       4.64293600   -3.98413200   -1.82976400
C       5.01988400   -5.24577300   -2.16574500
H       4.38950700   -6.10175000   -1.95087900
H       5.99028500   -5.45304700   -2.60353700
H       1.95689000   -0.25982400   -1.21717700
H       1.38175600    0.63295900    0.20133600
H       1.08171000   -1.10904600    0.06903800
H       4.92338500   -1.88552200    1.74729600
H       6.40068500   -3.60205000    0.10302900
H       4.94526700   -4.44913500    0.79888300
H       5.21896500   -3.12936800   -2.16467800
H       3.63061500   -3.76903800   -1.51360500

1D rotors:
pivots: [1, 2], dihedral: [12, 1, 2, 5], rotor symmetry: 3, max scan energy: 12.42 kJ/mol
pivots: [2, 5], dihedral: [1, 2, 5, 6], rotor symmetry: 1, max scan energy: 21.66 kJ/mol
pivots: [5, 6], dihedral: [2, 5, 6, 7], rotor symmetry: 3, max scan energy: 30.90 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 16], invalidation reason: Two consecutive points are inconsistent by more than 10.51 kJ/molTwo consecutive points are inconsistent by more than 10.51 kJ/molTwo consecutive points are inconsistent by more than 10.60 kJ/mol
* Invalidated! pivots: [8, 9], dihedral: [18, 8, 9, 10], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 195.65591478399634 J/mol
""",
)

entry(
    index = 8,
    label = "C5H9O3 + Li <=> C3H5LiO3 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.5603e+07,'cm^3/(mol*s)'), n=1.70021, Ea=(38.7352,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.1943783976602214,B=0.894154843812189,E=5.394280864555017,L=8.956244842828797,A=0.23494209646668668,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: CCOC(=O)OC[CH2] + [Li] <=> C=C + [Li]OC(=O)OCC
TS method summary for TS3 in CCOC(=O)OC[CH2] + [Li] <=> C=C + [Li]OC(=O)OCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      6.15090500    0.72133600    0.42432000
C       0.69762600   -1.44643100    0.53480800
C       2.11807200   -0.92420900    0.60007900
O       2.38556900   -0.25306300   -0.65733700
C       3.60042300    0.29329700   -0.82256500
O       4.45641600    0.21443300    0.08917100
O       3.73553900    0.85755400   -1.95701200
C       5.57908600    1.62870500   -2.07928300
C       5.58464500    2.22255700   -3.39086700
H       5.26738000    3.24626900   -3.53806700
H       5.88708100    1.65063700   -4.25790300
H       0.45342500   -1.96207500    1.46758300
H       0.57798900   -2.15182500   -0.29021500
H      -0.01338200   -0.62914800    0.39670900
H       2.84317900   -1.73058800    0.73052300
H       2.25294100   -0.21082900    1.41613000
H       6.11245900    0.69387500   -1.93751400
H       5.49418900    2.28581200   -1.21934500

1D rotors:
pivots: [2, 3], dihedral: [12, 2, 3, 4], rotor symmetry: 3, max scan energy: 12.87 kJ/mol
pivots: [3, 4], dihedral: [2, 3, 4, 5], rotor symmetry: 1, max scan energy: 32.24 kJ/mol
pivots: [4, 5], dihedral: [3, 4, 5, 6], rotor symmetry: 2, max scan energy: 33.94 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [4, 5, 6, 1], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
pivots: [8, 9], dihedral: [17, 8, 9, 10], rotor symmetry: 2, max scan energy: 7.62 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 14583.764309070988 J/mol
""",
)

entry(
    index = 9,
    label = "C5H9O3 + C2H5 <=> C5H10O3 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20.523,'cm^3/(mol*s)'), n=2.58803, Ea=(182.358,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.7109399685673664,B=0.5561097043959204,E=0.394916410780481,L=4.3126161018203115,A=-0.0721543234535927,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: CCOC(=O)OC[CH2] + C[CH2] <=> C=C + CCOC(=O)OCC
TS method summary for TS4 in CCOC(=O)OC[CH2] + C[CH2] <=> C=C + CCOC(=O)OCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       1.65518400   -1.33932100   -1.76538000
C       1.68476400   -1.53804000   -0.42800400
O       3.68496600   -0.66602300   -0.03318800
C       4.60513800   -1.65814800   -0.02060600
O       5.75382300   -1.20329200    0.60473400
C       5.65511000   -0.89378100    2.00927500
C       5.52569200    0.60020800    2.25601300
O       4.87889000   -2.29493900   -1.18961300
C       5.40351100   -1.47316800   -2.27215700
C       5.67501200   -2.38331600   -3.45207000
H       6.07206900   -1.80284300   -4.28995700
H       6.40509500   -3.15166600   -3.18815800
H       2.05331700   -2.07823000   -2.45038600
H       1.27485600   -0.41797600   -2.19155400
H       1.25203400   -0.82044500    0.25639900
H       2.00216700   -2.48468800   -0.00918700
H       6.57860000   -1.28138800    2.44770200
H       4.81175700   -1.44529300    2.43354800
H       6.36372700    1.14026100    1.80875700
H       5.52429300    0.80017200    3.33224100
H       4.59691200    0.98005100    1.82599400
H       4.66607900   -0.70228700   -2.51649200
H       6.31818600   -0.98426300   -1.92572100
H       4.75944600   -2.88035100   -3.78232500

1D rotors:
* Invalidated! pivots: [1, 2], dihedral: [13, 1, 2, 15], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
* Invalidated! pivots: [4, 5], dihedral: [3, 4, 5, 6], invalidation reason:
* Invalidated! pivots: [4, 8], dihedral: [3, 4, 8, 9], invalidation reason: Another conformer for TS4 exists which is 7.80 kJ/mol lower.Another conformer for TS4 exists which is 7.80 kJ/mol lower. But unable to propose troubleshooting methods.
pivots: [5, 6], dihedral: [4, 5, 6, 7], rotor symmetry: 1, max scan energy: 14.36 kJ/mol
pivots: [6, 7], dihedral: [5, 6, 7, 19], rotor symmetry: 3, max scan energy: 13.46 kJ/mol
pivots: [8, 9], dihedral: [4, 8, 9, 10], rotor symmetry: 1, max scan energy: 20.65 kJ/mol
pivots: [9, 10], dihedral: [8, 9, 10, 11], rotor symmetry: 3, max scan energy: 12.05 kJ/mol
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 250.18842050131107 J/mol
""",
)

entry(
    index = 10,
    label = "C3H4LiO3 + C2H5 <=> C3H5LiO3-2 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.734475,'cm^3/(mol*s)'), n=3.69312, Ea=(202.73,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.4561557547476465,B=2.2803199654633044,E=1.3183361925504222,L=11.121493210990602,A=0.5459030628779227,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [Li]OC(=O)OC[CH2] + C[CH2] <=> C=C + [Li]OC(=O)OCC
TS method summary for TS5 in [Li]OC(=O)OC[CH2] + C[CH2] <=> C=C + [Li]OC(=O)OCC:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
C       0.67288600   -1.17516800    0.31294700
C       2.06435500   -1.66195100    0.67939600
H       2.18645600   -1.69956000    1.76596700
H       2.25015400   -2.66470800    0.28021300
Li      3.64481700    0.47057400   -1.10250800
O       5.09535600   -0.55989900   -0.88559200
C       4.47601700   -1.30189500   -0.03667000
O       3.03995900   -0.76927000    0.12909600
O       4.95765600   -1.40359200    1.23187000
C       7.59816500   -0.88988500    1.21102200
C       7.68720200   -2.15273000    0.78372600
H       7.92758900   -2.96752900    1.45825400
H       7.49700000   -2.40859500   -0.25216300
H       0.49240700   -0.16951500    0.70265000
H      -0.08183600   -1.84165200    0.74047600
H       0.53369900   -1.16144200   -0.77201300
H       7.76951000   -0.62851800    2.24971700
H       7.33726200   -0.08794200    0.53227400

1D rotors:
pivots: [1, 2], dihedral: [14, 1, 2, 8], rotor symmetry: 3, max scan energy: 14.10 kJ/mol
* Invalidated! pivots: [2, 8], dihedral: [1, 2, 8, 7], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol
* Invalidated! pivots: [6, 7], dihedral: [5, 6, 7, 8], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molTwo consecutive points are inconsistent by more than 0.24 kJ/mol
* Invalidated! pivots: [7, 8], dihedral: [6, 7, 8, 2], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molTwo consecutive points are inconsistent by more than 0.08 kJ/mol
* Invalidated! pivots: [10, 11], dihedral: [17, 10, 11, 12], invalidation reason: initial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/molinitial and final points are inconsistent by more than 5.00 kJ/mol But unable to propose troubleshooting methods.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1431.1465293831595 J/mol
""",
)

