#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3HF4O <=> C3HF4O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.01526e+12,'s^-1'), n=0.18834, Ea=(147.694,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10613, dn = +|- 0.0132522, dEa = +|- 0.0721181 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CF2CF2CHO <=> CF3CFCHO
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 145.777 kJ/mol

F    -0.081348    1.78715    -0.490023
F    -0.263782    0.35288    1.614731
F    -1.998141    -0.068619    -0.408418
F    -0.574466    -1.649453    -0.11926
O    2.128893    -0.882804    -0.220012
C    0.243197    0.536669    -0.262621
C    -0.767727    -0.39416    -0.247597
C    1.688472    0.22613    -0.139999
H    2.304691    1.121958    0.033928
""",
)

entry(
    index = 2,
    label = "C4H6F3 <=> C4H6F3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000550858,'s^-1'), n=4.50663, Ea=(210.996,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 35.7263, dn = +|- 0.4698, dEa = +|- 2.55664 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CF2CH2CH2CH2F <=> CH2CH2CH2CF3
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 245.167 kJ/mol

F    -0.702779    1.792388    0.098311
F    -2.062972    -0.448609    -0.588073
F    -1.388837    -0.156899    1.43638
C    1.315516    0.502681    0.476685
C    0.303398    -0.398034    -0.230773
C    1.088477    1.938292    0.091363
C    -1.08247    0.021217    0.164424
H    2.329884    0.184622    0.219347
H    1.209485    0.389073    1.555472
H    0.378059    -0.280002    -1.311718
H    0.448699    -1.458654    0.005532
H    1.31562    2.709364    0.81215
H    1.230852    2.208941    -0.945251
""",
)

entry(
    index = 3,
    label = "C2H2F3 <=> C2H2F3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.36622e+11,'s^-1'), n=0.48217, Ea=(122.23,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17845, dn = +|- 0.0215722, dEa = +|- 0.117395 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CF2CH2F <=> CH2CF3
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 121.070 kJ/mol

F    1.347752    1.069335    -0.341494
F    1.347827    -1.068543    -0.343712
H    -1.251244    -0.939104    -0.284958
H    -1.251335    0.939705    -0.28305
F    -0.089079    -0.001721    1.643004
C    0.623435    0.000325    -0.298646
C    -0.727456    0.000243    -0.266644
""",
)

entry(
    index = 4,
    label = "C3H6Cl <=> C3H6Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.00221e+06,'s^-1'), n=1.90111, Ea=(169.648,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.59483, dn = +|- 0.061324, dEa = +|- 0.333723 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2Cl <=> CH2CH2CH2Cl
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 179.426 kJ/mol

H    -0.210922    -2.048344    0.553291
H    -0.204988    2.044651    0.553322
H    0.167674    1.383778    -1.107898
C    -0.128456    -1.179389    -0.086684
C    -1.015991    -0.00066    0.139361
C    -0.124869    1.175392    -0.086548
H    0.163188    -1.388732    -1.108094
H    -1.404542    -0.000116    1.155317
H    -1.8628    0.000663    -0.556372
Cl    1.611586    -0.004644    0.543876
""",
)

entry(
    index = 5,
    label = "C3H6F <=> C3H6F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00930803,'s^-1'), n=4.16824, Ea=(227.637,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 33.1868, dn = +|- 0.460113, dEa = +|- 2.50392 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2F <=> CH2CH2CH2F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 261.477 kJ/mol

H    0.323382    -1.588291    0.997034
H    -0.010948    1.680124    0.898052
H    0.00737    1.62633    -0.938705
C    0.025647    -1.143551    0.061814
C    -1.054905    -0.106051    0.020696
C    -0.206843    1.129174    -0.007023
H    0.341642    -1.642036    -0.839709
H    -1.688493    -0.144114    0.904315
H    -1.670807    -0.196107    -0.871613
F    1.345025    0.139951    0.037479
""",
)

entry(
    index = 6,
    label = "C4H8Cl <=> C4H8Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.50247e+07,'s^-1'), n=1.58353, Ea=(156.188,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.34324, dn = +|- 0.0387684, dEa = +|- 0.210976 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2CH2Cl <=> CH2CH2CH2CH2Cl
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 163.692 kJ/mol

Cl    0.008511    1.884275    0.000242
H    -2.160579    0.698257    -0.52456
H    -1.690077    0.329961    1.193926
C    0.724553    -0.966582    0.286976
C    -0.721808    -0.963182    -0.286738
C    1.449466    0.243619    -0.143757
C    -1.440803    0.250817    0.143305
H    1.221917    -1.868007    -0.077918
H    0.681014    -1.024525    1.375152
H    -0.678525    -1.021984    -1.374877
H    -1.223617    -1.861939    0.078647
H    2.172057    0.687398    0.523519
H    1.698521    0.321271    -1.194546
""",
)

entry(
    index = 7,
    label = "C4H8Br <=> C4H8Br-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.62119e+10,'s^-1'), n=0.157944, Ea=(121.704,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06787, dn = +|- 0.00862677, dEa = +|- 0.0469466 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2CH2Br <=> CH2CH2CH2CH2Br
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 124.951 kJ/mol

Br    0.008663    1.989451    -0.000855
H    -2.210236    0.653722    -0.500667
H    -1.703294    0.29805    1.203136
C    0.717465    -0.963259    0.293076
C    -0.714785    -0.959875    -0.292941
C    1.458012    0.241842    -0.151009
C    -1.449401    0.249006    0.150751
H    1.224217    -1.870898    -0.043856
H    0.662268    -0.999181    1.382239
H    -0.659884    -0.996505    -1.382098
H    -1.225929    -1.864918    0.044368
H    2.220667    0.643018    0.500484
H    1.712867    0.288928    -1.203257
""",
)

entry(
    index = 8,
    label = "C2H4F <=> C2H4F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.31151e+11,'s^-1'), n=0.116194, Ea=(135.383,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06904, dn = +|- 0.00877084, dEa = +|- 0.0477306 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2F <=> CH2CH2F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 134.936 kJ/mol

H    0.818162    -0.926794    -0.127948
H    0.814169    0.922804    -0.137186
H    -1.096169    0.926456    1.431698
H    -1.09165    -0.922491    1.441638
F    -1.360804    -0.011328    -0.836242
C    0.379254    -0.000986    0.212836
C    -0.670492    0.001069    1.074944
""",
)

entry(
    index = 9,
    label = "C2H4Cl <=> C2H4Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.03108e+13,'s^-1'), n=-0.0707693, Ea=(47.2642,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01008, dn = +|- 0.00131731, dEa = +|- 0.00716878 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2Cl <=> CH2CH2Cl
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 45.481 kJ/mol

H    0.851913    -0.927102    -0.087801
H    0.840414    0.92049    -0.106588
H    -1.065318    0.924586    1.461741
H    -1.053831    -0.92301    1.48054
Cl    -1.67787    -0.0305    -1.224009
C    0.407827    -0.00249    0.251794
C    -0.632765    -0.000252    1.108133
""",
)

entry(
    index = 10,
    label = "C3H6Br <=> C3H6Br-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.2885e+08,'s^-1'), n=1.30127, Ea=(134.618,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11448, dn = +|- 0.0142406, dEa = +|- 0.0774968 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2Br <=> CH2CH2CH2Br
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 139.348 kJ/mol

H    -0.230774    -2.059531    0.545077
H    -0.225024    2.055723    0.546004
H    0.13287    1.404117    -1.116806
C    -0.130385    -1.187635    -0.089079
C    -1.013476    -0.000729    0.142475
C    -0.126823    1.183651    -0.088267
H    0.128346    -1.408482    -1.117781
H    -1.39045    -0.000542    1.163217
H    -1.86917    0.000922    -0.541624
Br    1.714764    -0.004894    0.556354
""",
)

entry(
    index = 11,
    label = "C4H8F <=> C4H8F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.35274e-11,'s^-1'), n=6.31569, Ea=(202.311,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 193.49, dn = +|- 0.691746, dEa = +|- 3.76445 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2CH2F <=> CH2CH2CH2CH2F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 255.682 kJ/mol

F    -0.751312    1.70264    0.137576
H    -1.882555    -0.266513    -0.449519
H    -1.291761    -0.128329    1.273928
C    1.328286    0.503627    0.47053
C    0.335088    -0.436276    -0.207788
C    1.027395    1.917212    0.047501
C    -1.059297    -0.062647    0.220407
H    2.362    0.229649    0.229675
H    1.223662    0.417294    1.554059
H    0.423871    -0.333291    -1.291259
H    0.554512    -1.483703    0.029747
H    1.2771    2.726486    0.718925
H    1.101562    2.14882    -1.005652
""",
)

entry(
    index = 12,
    label = "C2F5 <=> C2F5-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.28412e+12,'s^-1'), n=0.253035, Ea=(209.151,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14701, dn = +|- 0.0180193, dEa = +|- 0.0980605 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CF3CF2 <=> CF3CF2
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 206.908 kJ/mol

F    1.36878    1.08729    -0.31472
F    1.36885    -1.08644    -0.31714
F    -1.36912    -1.08649    -0.31599
F    -1.36918    1.08723    -0.3148
F    0.00086    -0.00204    1.61364
C    0.68234    0.00034    -0.26344
C    -0.68263    0.00035    -0.26305
""",
)

entry(
    index = 13,
    label = "C5H10Br <=> C5H10Br-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68639e+09,'s^-1'), n=0.389834, Ea=(137.78,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.23187, dn = +|- 0.0273974, dEa = +|- 0.149096 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2CH2CH2Br <=> CH2CH2CH2CH2CH2Br
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 145.518 kJ/mol

Br    0.014974    -1.981947    -1.005692
H    2.375342    -1.170835    -0.190721
H    1.207672    -0.955349    1.168343
C    -0.00176    1.36136    0.29542
C    1.278058    0.732384    -0.246687
C    -1.27567    0.718479    -0.244357
C    1.452298    -0.708735    0.139104
H    -0.007805    2.425693    0.056643
H    -0.000312    1.284909    1.387193
H    1.309732    0.822029    -1.336279
H    2.138734    1.298513    0.129595
H    -2.141664    1.275303    0.133602
H    -1.31043    0.807851    -1.333883
C    -1.433982    -0.724471    0.141596
H    -1.185622    -0.96841    1.170584
H    -2.352696    -1.196093    -0.186862
""",
)

entry(
    index = 14,
    label = "C5H10Cl <=> C5H10Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.11837e-16,'s^-1'), n=7.45351, Ea=(118.459,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 301.9, dn = +|- 0.750193, dEa = +|- 4.08252 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2CH2CH2Cl <=> CH2CH2CH2CH2CH2Cl
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 186.956 kJ/mol

Cl    1.213586    7.1e-05    -0.11957
H    0.342577    2.321182    0.375849
H    -0.33856    1.16932    1.594778
C    -2.257827    -0.000227    -0.000698
C    -1.47274    1.274196    -0.296818
C    -1.472527    -1.274475    -0.297002
C    -0.242963    1.426166    0.544718
H    -3.179316    -0.00026    -0.584143
H    -2.55296    -0.000327    1.053109
H    -1.18995    1.3064    -1.352949
H    -2.122005    2.142541    -0.129725
H    -2.121647    -2.142953    -0.130039
H    -1.189729    -1.306475    -1.353137
C    -0.242721    -1.426352    0.544515
H    -0.338383    -1.169682    1.594613
H    0.342954    -2.321257    0.375529
""",
)

entry(
    index = 15,
    label = "C5H10F <=> C5H10F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.64853e+07,'s^-1'), n=1.15307, Ea=(198.221,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.79242, dn = +|- 0.0766688, dEa = +|- 0.417229 kJ/mol"""),
    rank = 3,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/intra_halogen_migration
Original entry: CH2CH2CH2CH2CH2F <=> CH2CH2CH2CH2CH2F
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 209.346 kJ/mol

F    -0.633423    1.567292    0.141329
H    -2.484085    0.462483    -0.550589
H    -2.016022    0.165333    1.187287
C    0.664929    -0.714831    0.362371
C    -0.72995    -0.875997    -0.272895
C    1.52753    0.41133    -0.239974
C    -1.718945    0.157479    0.147393
H    1.203532    -1.656297    0.242264
H    0.554894    -0.549296    1.437883
H    -0.628048    -0.873603    -1.360065
H    -1.112129    -1.863967    0.003601
H    2.566073    0.233623    0.057415
H    1.497695    0.338307    -1.329059
C    1.132149    1.783449    0.18879
H    1.252805    2.030219    1.234814
H    1.274034    2.605945    -0.496042
""",
)

