#!/usr/bin/env python
# encoding: utf-8

name = "Li_Abstraction/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "FLi + CH3 <=> CH3F + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.14134e+06,'cm^3/(mol*s)'), n=2.18948, Ea=(140.779,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8681935378213759,B=2.373498032935028,E=0.32859248603303737,L=5.004153890392606,A=0.8849787213003473,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [CH3] + [Li]F <=> [Li] + CF
TS method summary for TS2 in [CH3] + [Li]F <=> [Li] + CF:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      4.49673700   -1.13011800    1.39763100
C       1.75580400    0.00037500    0.06602800
F       3.42440700   -0.39159000    0.25679400
H       1.58109900    0.66479500    0.90113000
H       1.28598600   -0.97216800    0.11894400
H       1.79999200    0.45924600   -0.91097200


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 2138.0682833668507 J/mol
""",
)

entry(
    index = 1,
    label = "ClLi + CH3 <=> CH3Cl + Li",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.57736e+07,'cm^3/(mol*s)'), n=1.91726, Ea=(119.96,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.40096476096442,B=0.7611537028291462,E=0.36695032193123533,L=5.182274882516309,A=0.578711830957878,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryKinetics
Original entry: [CH3] + [Li]Cl <=> [Li] + CCl
TS method summary for TS3 in [CH3] + [Li]Cl <=> [Li] + CCl:

The method that generated the best TS guess and its output used for the optimization: user guess 0


TS external symmetry: 1, TS optical isomers: 1

Optimized TS geometry:
Li      3.00547500   -0.87557900   -3.79036700
C       1.88221400    0.13984100   -0.18786500
Cl      3.00971200    0.32165900   -1.76333600
H       2.24700300    0.89978200    0.49361100
H       2.03861700   -0.86850900    0.17807800
H       0.86741800    0.32211300   -0.52269700


No rotors considered for this TS.
ccsd(t)-f12/cc-pvdz-f12//b3lyp/6-311++G(d,p)used COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide","dimethylsulfoxide","ethanol","acetonitrile",
     "ethylacetate","methanol","butan-2-one","cyclohexanone", "N,N-dimethylacetamide",
    "2-methylpropan-1-ol","propan-2-ol","N-methylformamide","pentan-1-ol",
    "propan-1-ol", "butan-2-ol", "oxolane", "2-methylpropan-2-ol", "propan-2-one",
    "methyl acetate", "formamide", "diethyl carbonate", "dimethyl carbonate",]
    MAE error: 1761.0833142781657 J/mol
""",
)

