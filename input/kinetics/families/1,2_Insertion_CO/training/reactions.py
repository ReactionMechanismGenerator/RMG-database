#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H6 + CO <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (538, 'cm^3/(mol*s)'),
        n = 3.29,
        Ea = (437.228, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_methyl_C_methyl
""",
)

entry(
    index = 2,
    label = "H2 + CO <=> CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.89e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (343.506, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;H2
""",
)

entry(
    index = 3,
    label = "CH4 + CO <=> C2H4O",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (65600, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (363.59, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_methane
""",
)

entry(
    index = 4,
    label = "C2H6-2 + CO <=> C3H6O-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (548400, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (357.732, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_pri/NonDeC
""",
)

entry(
    index = 5,
    label = "C3H8 + CO <=> C4H8O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.532e+06, 'cm^3/(mol*s)'),
        n = 2.07,
        Ea = (343.925, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C/H2/NonDeC
""",
)

entry(
    index = 6,
    label = "C4H10 + CO <=> C5H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.89e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (331.373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: CO;C/H/Cs3
""",
)

entry(
    index = 7,
    label = "CH4O + CO <=> C2H4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.127, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (223.258, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations by Franklin, 2010""",
    longDesc = 
u"""
CBS-QB3 calculations by CFG, Jan 2010 
Methyl group was hindered rotor. ester CO bond also a rotor.

Converted to training reaction from rate rule: CO;CsO_H
""",
)

entry(
    index = 8,
    label = "CF4 + CO <=> C2F4O",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(10782.4,'cm^3/(mol*s)'), n=2.93313, Ea=(397.886,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.13366, dn = +|- 0.016482, dEa = +|- 0.0896944 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 402.994 kJ/mol

Coordinates (Angstoms):
F    -1.135412    0.146899    1.204966
F    -1.511149    0.75232    -0.763505
F    -0.563616    -1.195046    -0.296891
F    0.593202    0.397982    -1.257751
O    1.916715    1.501744    0.670309
C    -0.647686    0.080374    -0.062139
C    0.934106    0.984407    0.50501
""",
)

entry(
    index = 9,
    label = "CH3Cl + CO <=> C2H3ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7341.96,'cm^3/(mol*s)'), n=2.97843, Ea=(311.689,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19217, dn = +|- 0.0230932, dEa = +|- 0.125672 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 317.326 kJ/mol

Coordinates (Angstoms):
H    0.679213    -1.177163    -0.195709
H    1.13967    0.47297    -0.791057
H    0.914395    0.176895    1.003033
Cl    -0.610908    1.968796    -0.214713
O    -2.468538    -0.475933    0.041716
C    0.687492    -0.114043    -0.010488
C    -1.355735    -0.410872    0.185367
""",
)

entry(
    index = 10,
    label = "ClH + CO <=> CHClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6108,'cm^3/(mol*s)'), n=2.57909, Ea=(159.246,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.43991, dn = +|- 0.0478989, dEa = +|- 0.260664 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 173.746 kJ/mol

Coordinates (Angstoms):
Cl    0.795619    -1.592659    -0.000909
O    -2.09663    -0.467479    -0.000236
C    -1.03292    -0.107343    -0.000268
H    0.0768    0.10188    -0.000357
""",
)

entry(
    index = 11,
    label = "BrH + CO <=> CHBrO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(15238.4,'cm^3/(mol*s)'), n=2.47236, Ea=(142.16,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.36179, dn = +|- 0.0405705, dEa = +|- 0.220783 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 155.251 kJ/mol

Coordinates (Angstoms):
Br    -1.366657    -0.108247    -0.0
O    1.885848    -0.313506    -2e-06
C    1.085328    0.47511    4e-06
H    0.178861    1.145233    8e-06
""",
)

entry(
    index = 12,
    label = "CHF3 + CO <=> C2HF3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.81927e-10,'cm^3/(mol*s)'), n=6.80628, Ea=(325.917,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 33.5544, dn = +|- 0.46156, dEa = +|- 2.51179 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 362.466 kJ/mol

Coordinates (Angstoms):
F    1.658656    0.635138    0.720295
F    1.143012    -1.248824    -0.203816
F    1.387618    0.516797    -1.425206
H    -0.720868    0.883098    -0.086002
O    -1.556816    -1.147495    0.132763
C    0.909531    0.0697    -0.247018
C    -1.289634    -0.042905    0.037533
""",
)

entry(
    index = 13,
    label = "FH + CO <=> CHFO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.66811e-05,'cm^3/(mol*s)'), n=4.88105, Ea=(180.508,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 11.5455, dn = +|- 0.321395, dEa = +|- 1.74902 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 215.580 kJ/mol

Coordinates (Angstoms):
F    0.48745    -1.445399    -0.000825
O    -1.964898    -0.570793    -0.000479
H    0.237845    -0.081498    0.000329
C    -0.892948    -0.233661    -2.5e-05
""",
)

entry(
    index = 14,
    label = "CH3Br + CO <=> C2H3BrO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(16318.9,'cm^3/(mol*s)'), n=2.90186, Ea=(300.412,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16266, dn = +|- 0.0198, dEa = +|- 0.107751 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 305.421 kJ/mol

Coordinates (Angstoms):
H    0.667086    -1.177951    -0.165677
H    1.077611    0.464734    -0.823529
H    0.935836    0.212516    0.988604
Br    -0.653897    2.177297    -0.164966
O    -2.456975    -0.521038    -0.026659
C    0.677229    -0.110622    -0.007247
C    -1.364841    -0.430895    0.220615
""",
)

entry(
    index = 15,
    label = "CH3F + CO <=> C2H3FO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(614.234,'cm^3/(mol*s)'), n=3.16963, Ea=(318.436,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.27036, dn = +|- 0.0314397, dEa = +|- 0.171094 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 326.736 kJ/mol

Coordinates (Angstoms):
H    0.70707    -1.141584    -0.255448
H    1.239017    0.523712    -0.688312
H    0.843458    0.106221    1.034785
F    -0.570329    1.254419    -0.457782
O    -2.430475    -0.291641    0.186491
C    0.661128    -0.089303    -0.010744
C    -1.298819    -0.288242    0.19857
""",
)

