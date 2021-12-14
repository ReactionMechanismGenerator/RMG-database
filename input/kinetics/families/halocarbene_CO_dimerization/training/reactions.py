#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_CO_dimerization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""


entry(
    index = 1,
    label = "C3H3BrO <=> C2H3Br + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.3531e+12,'s^-1'), n=0.729529, Ea=(237.53,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21767, dn = +|- 0.025874, dEa = +|- 0.140805 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/halocarbene_CO_dimerization
Original entry: CC(Br)DCDO <=> C[C]Br + CO
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 233.421 kJ/mol

Br    1.262789    1.690256    -0.327397
O    -2.474208    -0.038289    0.151542
C    1.451279    -1.064968    -0.083258
C    0.676364    0.069316    0.470802
C    -1.488359    -0.255078    -0.34218
H    2.335547    -1.075389    0.57226
H    0.919233    -2.000431    0.084688
H    1.804145    -0.980936    -1.110967
""",
)

entry(
    index = 2,
    label = "C3H3ClO <=> C2H3Cl + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.43849e+12,'s^-1'), n=0.705824, Ea=(225.715,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.2099, dn = +|- 0.0250331, dEa = +|- 0.136229 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/halocarbene_CO_dimerization
Original entry: CC(Cl)DCDO <=> C[C]Cl + CO
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 221.922 kJ/mol

Cl    1.225347    1.561177    -0.299216
O    -2.435615    -0.057154    0.158668
C    1.444139    -1.046367    -0.082946
C    0.667738    0.103515    0.442435
C    -1.446755    -0.217366    -0.352108
H    2.328049    -1.052996    0.570884
H    0.90893    -1.977967    0.090237
H    1.794956    -0.968363    -1.112464
""",
)

entry(
    index = 3,
    label = "C3H3FO <=> C2H3F + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.62099e+12,'s^-1'), n=0.640083, Ea=(177.782,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18906, dn = +|- 0.0227498, dEa = +|- 0.123804 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/halocarbene_CO_dimerization
Original entry: CC(F)DCDO <=> C[C]F + CO
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 174.189 kJ/mol

F    -0.802172    1.088369    0.680746
O    2.53538    -0.175629    -0.33759
C    -1.316907    -0.993521    -0.045567
C    -0.496563    0.228355    -0.278056
C    1.563865    -0.359613    0.19953
H    -2.26911    -0.756639    -0.536472
H    -0.887563    -1.851276    -0.556223
H    -1.519461    -1.206106    1.004712
""",
)

