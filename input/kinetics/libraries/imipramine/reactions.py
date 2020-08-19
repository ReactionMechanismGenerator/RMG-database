#!/usr/bin/env python
# encoding: utf-8

name = "imipramine"
shortDesc = ""
longDesc = """
Calculated using Arkane v2.4.1.

Indices are 1-indexed, corresponding to the following atom order of imipramine:

 N                 -0.00634640   -0.33884115    0.59014543
 C                  1.34971160   -0.59332915    0.28011243
 C                 -0.33884640    1.02531185    0.80935343
 C                  1.90724860   -1.99720215    0.28906443
 H                  1.54683540   -0.24043385   -0.74445243
 H                  2.01383960    0.10240385    0.81678743
 C                 -1.04087840   -1.29842115    0.44492743
 C                  0.01734260    1.63227285    2.01649843
 C                 -0.96251440    1.76363785   -0.20843657
 C                  3.36262660   -1.96925415   -0.18238057
 H                  1.84605060   -2.43910815    1.30009143
 H                  1.31932360   -2.66123715   -0.36605157
 C                 -0.98498540   -2.42954315    1.27978143
 C                 -2.12109040   -1.15216515   -0.45091657
 C                 -0.25921040    2.98164885    2.22905943
 H                  0.51102860    1.03046785    2.78373243
 C                 -1.27502340    1.08404885   -1.50705857
 C                 -1.25012340    3.11152385    0.02862343
 N                  4.20026960   -1.13768215    0.65915443
 H                  3.38114260   -1.55505415   -1.20088257
 H                  3.75199360   -3.00993915   -0.25151957
 C                 -1.94181640   -3.43312815    1.21393843
 H                 -0.17359640   -2.49346015    2.00576243
 C                 -2.36378440    0.02234685   -1.37389557
 C                 -3.08445640   -2.17367815   -0.48437757
 C                 -0.90050640    3.72118885    1.23368643
 H                  0.01841160    3.45358985    3.17527243
 H                 -1.60779740    1.83365885   -2.24172757
 H                 -0.34933940    0.64413985   -1.91332857
 H                 -1.73933540    3.69591885   -0.75661957
 C                  5.30282460   -0.53382415   -0.04745657
 C                  4.60551260   -1.78583115    1.87822243
 C                 -3.00436540   -3.30587615    0.31758043
 H                 -1.86875240   -4.30196615    1.87337043
 H                 -2.58743840   -0.38168415   -2.37611257
 H                 -3.29548040    0.51591885   -1.04184457
 H                 -3.92342640   -2.06790415   -1.17971757
 H                 -1.12568540    4.77886885    1.39528643
 H                  5.84454960    0.15200385    0.62333943
 H                  6.04077360   -1.27564415   -0.43015257
 H                  4.92157960    0.05386585   -0.89461757
 H                  5.12651860   -1.07235215    2.53562043
 H                  5.28861260   -2.65058115    1.70831543
 H                  3.73034460   -2.16058715    2.43060043
 H                 -3.77247840   -4.08092015    0.25152943
"""

# imipramine + OHCH2OO updated to two para arrhenius fit (same as in training reaction)
entry(
    index = 1000,
    label = "imipramine + OHCH2OO <=> imipramine_1_rad + OHCH2OOH",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(85.9968,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(22.9212,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.05754, dn = +|- 0, dEa = +|- 0.144274 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
u"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1001,
    label = "imipramine + OHCH2OO <=> imipramine_2_rad + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.07986,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(27.7183,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.05306, dn = +|- 0, dEa = +|- 0.133341 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
u"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1002,
    label = "imipramine + OHCH2OO <=> imipramine_3_rad + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(179.049,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(59.466,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.0447, dn = +|- 0, dEa = +|- 0.11279 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
u"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1003,
    label = "imipramine + OHCH2OO <=> imipramine_4_rad + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9416.35,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(43.8278,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.02193, dn = +|- 0, dEa = +|- 0.0559449 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
u"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1004,
    label = "imipramine + OHCH2OO <=> imipramine_5_rad + OHCH2OOH",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(134.27,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(26.6523,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.02551, dn = +|- 0, dEa = +|- 0.0649776 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
u"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1005,
    label = "imipramine + O2 <=> imipramine_1_rad + HO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.82123e+14,'cm^3/(mol*s)'), n=0, Ea=(149.699,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.0007, 
                         dn = +|- 0, dEa = +|- 0.00181463 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) after discussing with Prof. Green
""",
)

entry(
    index = 1006,
    label = "imipramine + O2 <=> imipramine_2_rad + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.05571e+14,'cm^3/(mol*s)'), n=0, Ea=(176.536,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00064, 
                         dn = +|- 0, dEa = +|- 0.00164057 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) after discussing with Prof. Green
""",
)

entry(
    index = 1007,
    label = "imipramine + O2 <=> imipramine_3_rad + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.44909e+14,'cm^3/(mol*s)'), n=0, Ea=(205.239,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00105, 
                         dn = +|- 0, dEa = +|- 0.0027046 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) after discussing with Prof. Green
""",
)

entry(
    index = 1008,
    label = "imipramine + O2 <=> imipramine_4_rad + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.47872e+15,'cm^3/(mol*s)'), n=0, Ea=(185.599,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00053, 
                         dn = +|- 0, dEa = +|- 0.00137809 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) after discussing with Prof. Green
""",
)

entry(
    index = 1009,
    label = "imipramine + O2 <=> imipramine_5_rad + HO2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(6.8117e+14,'cm^3/(mol*s)'), n=0, Ea=(186.187,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.0007, 
                         dn = +|- 0, dEa = +|- 0.00180928 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) after discussing with Prof. Green
""",
)

entry(
    index = 1010,
    label = "imipramine_2_oo + CH3OH <=> imipramine_2_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.35515e-07,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(113.076,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.27364, dn = +|- 0, dEa = +|- 0.623798 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1011,
    label = "imipramine_5_oo + CH3OH <=> imipramine_5_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.65724e-06,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(127.668,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.2162, dn = +|- 0, dEa = +|- 0.504781 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1014,
    label = "imipramine_4_oo + CH3OH <=> imipramine_4_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(7.69603e-05,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(141.246,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.27528, dn = +|- 0, dEa = +|- 0.627125 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 1015,
    label = "imipramine_4_oo <=> imipramine_4_ooh_2_rad",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.90675e+08,'s^-1'), 
                         n=0, 
                         Ea=(57.3664,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 99999,
    label = "imipramine_5_oo <=> imipramine_5_ooh_4_rad",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.90675e+07,'s^-1'), 
                         n=0, 
                         Ea=(57.3664,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    shortDesc = u"""Estimated based on 1015""",
    longDesc =
"""
Estimated to be 10 times slower than 1015 MS-TST rate. Factor based on previous single structure TST rate.
""",
)

entry(
    index = 99998,
    label = "imipramine_2_od_4_ooh + H2O <=> imipramine_tail_acetate_1 + iminobibenzyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), 
                         n=0, 
                         Ea=(60,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    shortDesc = u"""Estimated""",
    longDesc =
"""
Estimated based on amide alcoholysis training reactions.
""",
)

entry(
    index = 99997,
    label = "imipramine_2_od_4_ooh + CH3OH <=> imipramine_tail_acetate_2 + iminobibenzyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), 
                         n=0, 
                         Ea=(60,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    shortDesc = u"""Estimated""",
    longDesc =
"""
Estimated based on amide alcoholysis training reactions.
""",
)

entry(
    index = 99996,
    label = "imipramine_2_oh_4_od + H2O <=> imipramine_tail_derivative_1 + iminobibenzyl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=2.0, Ea=(60, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    shortDesc = u"""Estimated""",
    longDesc =
"""
Same estiamtion as hemiaminal hydrolysis training reaction.
""",
)



# entry(
#     index = 1010,
#     label = "imipramine_4_oo <=> imipramine_4_ooh_5_rad",
#     degeneracy = 6.0,
#     kinetics=Arrhenius(A=(5.55355e+10, 's^-1'), n=0, Ea=(50.4749, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1047

# TS1 optimized at wb97xd/def2tzvp
# N      -2.82974200   -0.44078400    0.83542100
# C      -2.44010600    0.14791800   -0.44194400
# C      -1.12266900    0.91151100   -0.33422200
# C       0.00126500    0.05561700    0.20532000
# H      -0.86094800    1.29520800   -1.32229400
# H      -1.24189000    1.75938000    0.34335700
# N       1.26608000    0.74049100    0.39434500
# C       1.76059400    1.52104100   -0.72906700
# C       2.20078300   -0.11291200    1.00235500
# H       2.71308700    1.96765200   -0.44944900
# H       1.06709500    2.32883000   -0.95568400
# H       3.23271200    0.20270200    0.88256900
# H       1.91197200   -1.25471800    0.39072000
# H       1.93840800   -0.38002500    2.02609000
# H      -2.34850200   -1.31861100    0.98290000
# H      -3.81788800   -0.64953700    0.84243800
# H       1.90463800    0.91138700   -1.62695600
# H      -3.21332700    0.85938600   -0.73741600
# H      -0.27347400   -0.37512500    1.17200100
# O       0.22712400   -1.00465300   -0.71670900
# O       1.01910600   -1.97367000   -0.11425800
# H      -2.35839600   -0.59050300   -1.24739900
# """,
# )

# entry(
#     index = 1011,
#     label = "imipramine_4_oo <=> imipramine_4_ooh_2_rad",
#     degeneracy = 2.0,
#     kinetics=Arrhenius(A=(1.46807e+10,'s^-1'), n=0, Ea=(52.6413,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water

# ts2008 fragment

# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# C      -2.44221400   -0.43974200   -0.65695200
# N      -1.41331300   -0.48824500    0.36312000
# C      -1.76930400    0.28557300    1.53666900
# C      -0.09828500   -0.29978300   -0.15925400
# O       0.06265300    1.05510800   -0.60436200
# O       0.84600400    1.07967000   -1.78053900
# C       1.01644900   -0.66556200    0.84257600
# C       2.40156800   -0.60241800    0.29338600
# H       2.76877200   -1.41154200   -0.34488100
# N       2.95369600    0.66075500    0.01948300
# H      -2.59250700    0.57544000   -1.07360600
# H      -3.39806400   -0.78709400   -0.23539100
# H      -2.17678600   -1.10969200   -1.48817700
# H      -2.74334200   -0.06125700    1.91411300
# H      -1.04085300    0.13604200    2.34494100
# H      -1.84953600    1.37284400    1.33728400
# H       0.00725100   -0.93128700   -1.05665900
# H       1.74698800    1.12447700   -1.39769000
# H       0.94361100    0.01459200    1.70964200
# H       0.81128400   -1.68232700    1.21067700
# H       3.95170200    0.64862700   -0.16986200
# H       2.73640500    1.36338800    0.72346800
# """,
# )

entry(
    index = 1012,
    label = "imipramine_5_rad <=> imipramine_1_rad",
    degeneracy = 4.0,
    kinetics=Arrhenius(A=(32980, 's^-1'), n=0, Ea=(44.6304, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1022

This TS restricts 5 rotors, the A factor, originally A=(8.01453e+06, 's^-1'),
was divided by a factor of 3^5 = 243

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.38070300   -0.24956800    0.11972200
C       0.70709000   -1.18047800    0.38654100
C      -1.65446000   -0.80105700   -0.13833900
C       1.68022700   -0.66402600    1.44452100
H       0.24035900   -2.09002300    0.76062400
H       1.26305400   -1.46828300   -0.51424400
C      -0.08605700    1.05853000   -0.30707600
C      -1.77756100   -1.91160900   -0.96898600
C      -2.78987100   -0.27790300    0.50364600
C       0.98925100    0.02206400    2.61721700
H       2.27557400   -1.51450700    1.78598000
H       2.38377600    0.05107400    1.01149500
C       1.04123100    1.27012800   -1.11023800
C      -0.87071300    2.16006700    0.06562000
C      -3.00770900   -2.52028300   -1.16949300
H      -0.89540300   -2.30724100   -1.45729400
C      -2.66778000    0.82840200    1.45440300
C      -4.02011000   -0.90658800    0.28463900
N      -0.10373200   -0.74219000    3.19155000
H       0.57958800    0.97190200    2.27329700
H       1.73887300    0.26290500    3.38610800
C       1.39151100    2.53162700   -1.55369300
H       1.64938600    0.42318000   -1.39835400
C      -2.04763800    2.13574800    1.01830200
C      -0.51246200    3.41709300   -0.42214100
C      -4.13609500   -2.01324200   -0.53998400
H      -3.08204600   -3.38417700   -1.81826400
H      -3.60907600    1.02169600    1.96853200
H      -1.91535300    0.38543200    2.50267200
H      -4.89769600   -0.51676700    0.78813800
C      -1.19982800    0.04066400    3.60012300
C       0.31667500   -1.79780100    4.08922300
C       0.60151500    3.62043200   -1.21653600
H       2.27142300    2.65824500   -2.17243200
H      -1.74866400    2.68796600    1.91700600
H      -2.83586500    2.74530400    0.56283500
H      -1.12483000    4.26681400   -0.13928300
H      -5.10202700   -2.48027400   -0.68745700
H      -1.90624500   -0.51204400    4.21673100
H      -0.96386300    1.02516100    4.02229300
H      -0.54135400   -2.40301100    4.38412300
H       0.79365700   -1.40682200    5.00148300
H       1.03215400   -2.45228800    3.58759700
H       0.85208800    4.61545700   -1.56189000
""",
)

entry(
    index = 1013,
    label = "imipramine_5_rad <=> imipramine_2_rad",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.46807e+08,'s^-1'), n=0, Ea=(48.7508,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1023

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.31000500   -0.21198800    0.31644400
C       0.81520800   -1.07594900    0.47504900
C      -1.51164300   -0.82642400   -0.13385500
C       1.87332800   -0.65914300    1.47462300
H       0.45272000   -2.08012900    0.69172600
H       1.53714600   -1.30051400   -0.56708800
C      -0.11966600    1.14959700   -0.04417800
C      -1.49037400   -1.79342200   -1.13310000
C      -2.71547200   -0.45972300    0.46838200
C       3.15974700   -1.43809700    1.23380700
H       2.08309900    0.40892000    1.39961000
H       1.52343300   -0.84979300    2.49360100
C       1.03336400    1.50059000   -0.75424900
C      -1.05249600    2.14903600    0.27737600
C      -2.67073600   -2.39276000   -1.54642100
H      -0.54828600   -2.07257700   -1.58934400
C      -2.69259500    0.57052000    1.55442100
C      -3.89080600   -1.05837000    0.03123600
N       3.69257400   -1.20198500   -0.10636200
H       2.97702200   -2.51545600    1.39363500
H       3.91246600   -1.13087900    1.96084000
C       1.29057000    2.80672800   -1.12502400
H       1.73897600    0.72969400   -1.02746000
C      -2.35996900    1.95987200    1.02197500
C      -0.77261800    3.45589700   -0.12314700
C      -3.87552000   -2.02111800   -0.96811300
H      -2.64743300   -3.14418900   -2.32580000
H      -3.66823200    0.61385900    2.04000000
H      -1.96293700    0.28144600    2.31429100
H      -4.82875900   -0.77583100    0.49570200
C       2.79961800   -1.73070700   -1.09775700
C       5.02107400   -1.78483300   -0.24210700
C       0.37840500    3.80086500   -0.80721800
H       2.19691200    3.04022600   -1.66975200
H      -2.37320000    2.66721700    1.85479300
H      -3.16783300    2.27029900    0.35247300
H      -1.49224700    4.22780300    0.12777100
H      -4.80052800   -2.48339900   -1.28924400
H       2.96074700   -1.33646200   -2.09906800
H       2.67143100   -2.82211900   -1.07745400
H       5.40663400   -1.59704000   -1.24502800
H       5.01250300   -2.87392600   -0.07815000
H       5.70493500   -1.33463600    0.48015200
H       0.55859300    4.83041200   -1.08926400
""",
)

# entry(
#     index = 1014,
#     label = "imipramine_5_oo <=> imipramine_5_ooh_4_rad",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(6.3936e+09,'s^-1'), n=0, Ea=(45.6853,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# based on fragment ts1046

# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# N      -2.97691900   -0.20418800    0.88345800
# C      -2.41889300    0.07848800   -0.43419500
# C      -1.13904700    0.90418600   -0.34550800
# C      -0.06262900    0.19172500    0.42639800
# H      -0.80405200    1.11995200   -1.36258000
# H      -1.36620500    1.86065200    0.13890400
# N       1.21191400    0.77938800    0.51991100
# C       1.70309300    1.48088500   -0.65178800
# C       2.18384200   -0.10508700    1.14783600
# H       2.69094700    1.88619500   -0.43749300
# H       1.04769900    2.31770900   -0.88645900
# H       3.13450200   -0.00589700    0.61557800
# H       2.31700200    0.13099900    2.20650000
# H      -2.49255800   -0.97383000    1.32563400
# H      -3.94614200   -0.47819200    0.80797700
# H       1.77607800    0.82362500   -1.52795000
# H      -3.15655500    0.65772300   -0.99238600
# H      -0.38568200   -0.16170700    1.40789000
# H      -2.21549300   -0.82814400   -1.02073000
# H       0.28724500   -0.95878900   -0.09434400
# O       1.75460800   -1.44726100    1.16225100
# O       1.26626200   -1.79167800   -0.09015600
# """,
# )

# entry(
#     index = 1015,
#     label = "imipramine_5_oo + CH3OH <=> imipramine_5_ooh + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(4.22297e+08,'cm^3/(mol*s)'), n=0, Ea=(49.2508,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
# ts2007 based on a fragment

# TS external symmetry: 1, TS optical isomers: 2

# TS0 optimized at wb97xd/def2tzvp
# N       2.64279400   -0.50044300    1.63237100
# C       2.41271500    0.12615100    0.33930500
# C       1.18277100   -0.33806000   -0.44600500
# H       3.30050000   -0.04256700   -0.27464300
# C      -0.12370300    0.02079700    0.24332100
# H       1.22374800    0.12219900   -1.43705400
# H       1.22956400   -1.42290400   -0.58979400
# N      -1.30465600   -0.58188600   -0.35582200
# H      -0.08928900   -0.33613900    1.27655200
# C      -1.47030900   -0.39072900   -1.74491200
# C      -2.49005300   -0.39773300    0.45999000
# H      -2.39073100   -0.87209300   -2.07850500
# H      -0.61992500   -0.79780500   -2.29428600
# H      -3.34911000   -0.85535400   -0.03050300
# H      -2.72767900    0.65807500    0.64148800
# H      -2.34264100   -0.89206100    1.42321200
# H       2.65867600   -1.50842500    1.54762100
# H       1.91793400   -0.26361900    2.29500400
# H       2.35497900    1.20682900    0.49784000
# H      -0.21903700    1.11719400    0.29014100
# O      -1.49140000    0.97988300   -2.20486000
# O      -2.67855200    1.58136000   -1.82056900
# H      -3.35349600    1.49763500   -2.81034800
# C      -3.74288000    1.33291500   -4.07957900
# H      -4.76337100    0.95969400   -4.07881100
# H      -3.63192700    2.34750500   -4.47131500
# O      -2.88985500    0.40337300   -4.60774500
# H      -1.98637300    0.71920500   -4.50118400
# """,
# )

# entry(
#     index = 1016,
#     label = "imipramine_2_ooh_4_oo <=> imipramine_2_ooh_4_ooh_2_rad",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(1.5081e+08,'s^-1'), n=0, Ea=(67.4495,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(200,'K'), Tmax=(495, 'K')),
#     longDesc =
# u"""
# This is a fake reaction. products are unstable so forward rate calcualted using '
#                                  'reactant as products. Fitted to 60 data points; dA = *|/ 1.62624, dn = +|- 0, '
#                                  'dEa = +|- 1.26739 kJ/mol'

# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1038 forward only

# TS geom
#  N                  2.51752000   -1.07335300   -1.05889900
#  C                  1.51453700   -0.47971400   -0.28901200
#  C                  0.15956600   -1.13100800   -0.28745500
#  C                 -0.98287800   -0.11707700   -0.55433900
#  H                  0.11586200   -1.89937400   -1.06110000
#  H                 -0.00224800   -1.61576900    0.67755800
#  N                 -2.20835100   -0.49660300    0.04572600
#  C                 -3.36558800    0.15224000   -0.53792900
#  C                 -2.24894800   -0.45253700    1.49624700
#  H                 -4.27231500   -0.32399400   -0.15887900
#  H                 -3.35011800    0.03386000   -1.62268900
#  H                 -3.11261400   -1.02241100    1.84578700
#  H                 -2.32837700    0.57124400    1.88501200
#  H                 -1.35338100   -0.90033300    1.92488700
#  H                  2.56009300   -2.08286300   -0.98646400
#  H                  3.42359900   -0.65795000   -0.89194600
#  H                 -1.13043800   -0.03219200   -1.63536700
#  H                 -3.41755600    1.22528300   -0.30539000
#  O                 -0.58359700    1.19063800   -0.09804800
#  O                  0.43090900    1.63287600   -0.93751900
#  H                  1.19923900    0.70282200   -0.80556700
#  O                  1.80871200   -0.13775100    1.04256800
#  O                  2.91687200    0.75794600    1.03187500
#  H                  2.46077200    1.61028200    0.95028200
# """,
# )

# entry(
#     index = 1017,
#     label = "imipramine_4_oo + CH3OH <=> imipramine_4_ooh + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(4.22297e+08,'cm^3/(mol*s)'), n=0, Ea=(49.2508,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
# Fake, copied from ts2007 based on a fragment, should recalcualte ts2009

# TS external symmetry: 1, TS optical isomers: 2

# TS0 optimized at wb97xd/def2tzvp
# N       2.64279400   -0.50044300    1.63237100
# C       2.41271500    0.12615100    0.33930500
# C       1.18277100   -0.33806000   -0.44600500
# H       3.30050000   -0.04256700   -0.27464300
# C      -0.12370300    0.02079700    0.24332100
# H       1.22374800    0.12219900   -1.43705400
# H       1.22956400   -1.42290400   -0.58979400
# N      -1.30465600   -0.58188600   -0.35582200
# H      -0.08928900   -0.33613900    1.27655200
# C      -1.47030900   -0.39072900   -1.74491200
# C      -2.49005300   -0.39773300    0.45999000
# H      -2.39073100   -0.87209300   -2.07850500
# H      -0.61992500   -0.79780500   -2.29428600
# H      -3.34911000   -0.85535400   -0.03050300
# H      -2.72767900    0.65807500    0.64148800
# H      -2.34264100   -0.89206100    1.42321200
# H       2.65867600   -1.50842500    1.54762100
# H       1.91793400   -0.26361900    2.29500400
# H       2.35497900    1.20682900    0.49784000
# H      -0.21903700    1.11719400    0.29014100
# O      -1.49140000    0.97988300   -2.20486000
# O      -2.67855200    1.58136000   -1.82056900
# H      -3.35349600    1.49763500   -2.81034800
# C      -3.74288000    1.33291500   -4.07957900
# H      -4.76337100    0.95969400   -4.07881100
# H      -3.63192700    2.34750500   -4.47131500
# O      -2.88985500    0.40337300   -4.60774500
# H      -1.98637300    0.71920500   -4.50118400
# """,
# )

# entry(
#     index = 1018,
#     label = "imipramine_5_oo <=> imipramine_5_ooh_5_rad",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(3.17045e+08,'s^-1'), n=0, Ea=(39.9856,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# u"""
# ts2006 based on fragment

# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2svp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water

# TS0 optimized at wb97xd/def2svp
# C      -0.58442700   -0.77762800   -0.78705500
# O      -0.88207500   -1.46570500    0.41017200
# O      -2.25191700   -1.47365300    0.60143700
# N      -0.89819200    0.61904600   -0.59084600
# C      -2.28218900    0.78837100   -0.39547100
# C      -0.06412600    1.36758100    0.35035200
# C       1.44254600    1.32144300    0.09741600
# C       2.19688500    0.06778900    0.58422300
# N       2.58392700   -0.79898900   -0.52157100
# H       0.48594900   -0.93550600   -0.98198500
# H      -1.20545500   -1.17280800   -1.60821500
# H      -2.53425000   -0.28622200    0.36608500
# H      -2.88359900    0.53962500   -1.28178200
# H      -2.55825100    1.74374700    0.06653000
# H      -0.27085600    1.04516800    1.38993000
# H      -0.39200800    2.41547900    0.27620300
# H       1.86018300    2.20244200    0.60854400
# H       1.63295000    1.47464900   -0.97816500
# H       1.54149600   -0.51397400    1.25231600
# H       3.06027800    0.38693000    1.20012000
# H       2.97118300   -1.67485200   -0.17829600
# H       3.30522700   -0.35968600   -1.09025300
# """,
# )

# entry(
#     index = 20,
#     label = "imipramine + OHCH2OO <=> imipramine_rad_2 + OHCH2OOH",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0,
#                          dEa = +|- 0.000483392 kJ/mol"""),    shortDesc = u"""k5+k6""",
#     longDesc =
# u"""
# H6 is blocked, H5 and H6 have the same 2D connectivity
# k6 = 0  =>  k5 + k6 = k5
# """,
# )



# entry(
#     index = 21,
#     label = "imipramine + OHCH2OO <=> imipramine_rad_3 + OHCH2OOH",
#     degeneracy = 2.0,
#     # duplicate = True,
#     kinetics = Arrhenius(A=(3.94097e+07,'cm^3/(mol*s)'), n=0, Ea=(56.0508,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0,
#                          dEa = +|- 0.000364259 kJ/mol"""),    # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
#     #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k11+k12""",
# )



# entry(
#     index = 22,
#     label = "imipramine + OHCH2OO <=> imipramine_rad_4 + OHCH2OOH",
#     degeneracy = 2.0,
#     # duplicate = True,
#     kinetics = Arrhenius(A=(1.32296e+09,'cm^3/(mol*s)'), n=0, Ea=(41.7324,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0,
#                          dEa = +|- 4.59316e-05 kJ/mol"""),    # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
#     #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k20+k21""",
# )



# entry(
#     index = 23,
#     label = "imipramine + OHCH2OO <=> imipramine_rad_1 + OHCH2OOH",
#     degeneracy = 4.0,
#     # duplicate = True,
#     kinetics = Arrhenius(A=(4.7123e+06,'cm^3/(mol*s)'), n=0, Ea=(24.1853,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0,
#                          dEa = +|- 0.000717396 kJ/mol"""),    # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
#     #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
#     #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
#     #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k28+k29+k35+k36""",
# )

# entry(
#     index = 24,
#     label = "imipramine + OHCH2OO <=> imipramine_rad_5 + OHCH2OOH",
#     degeneracy = 6.0,
#     kinetics = Arrhenius(A=(2.41761e+09,'cm^3/(mol*s)'), n=0, Ea=(48.4544,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     shortDesc = u"""based on fragment h40""",
#     longDesc =
# u"""
# Based on fragment h40
# """,
# )



# entry(
#     index = 24,
#     label = "imipramine + OHCH2OO <=> imipramine_rad_5 + OHCH2OOH",
#     degeneracy = 6.0,
#     # duplicate = True,
#     kinetics = Arrhenius(A=(2.1327e+09,'cm^3/(mol*s)'), n=0, Ea=(46.4329,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0,
#                          dEa = +|- 0.00509461 kJ/mol"""),#     kinetics = MultiArrhenius(
# # #        arrhenius = [
# # #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# # #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# # #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# # #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# # #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# # #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# # #        ],
# #         arrhenius = [
# #             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #         ],
# #     ),
#     shortDesc = u"""k39+k40+k41+k42+k43+k44""",
#     longDesc =
# u"""
# Here rotors we not included in the calculation (Eventually we'd like to use rotors).
# We're definitely missing a factor of x3 of the torsion missing in the TS,
# we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
# """,
# )

# # imipramine + cyanoisopropylOO copied from OHCH2OO
#
#
# entry(
#     index = 25,
#     label = "imipramine + cyanoisopropylOO <=> imipramine_rad_2 + cyanoisopropylOOH",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0,
#                          dEa = +|- 0.000483392 kJ/mol"""),
#     longDesc =
# u"""
# copied over, not calculated!!
# """,
# )
#
# entry(
#     index = 26,
#     label = "imipramine + cyanoisopropylOO <=> imipramine_rad_3 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(3.94097e+07, 'cm^3/(mol*s)'), n=0, Ea=(56.0508, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0,
#                      dEa = +|- 0.000364259 kJ/mol"""),
#     shortDesc = u"""k11+k12""",
# )
#
# entry(
#     index = 27,
#     label = "imipramine + cyanoisopropylOO <=> imipramine_rad_4 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(1.32296e+09, 'cm^3/(mol*s)'), n=0, Ea=(41.7324, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0,
#                      dEa = +|- 4.59316e-05 kJ/mol"""),
#     longDesc=
#     u"""
#     copied over, not calculated!!
#     """,
# )
#
# entry(
#     index = 28,
#     label = "imipramine + cyanoisopropylOO <=> imipramine_rad_1 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(4.7123e+06, 'cm^3/(mol*s)'), n=0, Ea=(24.1853, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0,
#                      dEa = +|- 0.000717396 kJ/mol"""),
#     longDesc=
#     u"""
#     copied over, not calculated!!
#     """,
# )
#
# entry(
#     index = 29,
#     label = "imipramine + cyanoisopropylOO <=> imipramine_rad_5 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(2.1327e+09, 'cm^3/(mol*s)'), n=0, Ea=(46.4329, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0,
#                      dEa = +|- 0.00509461 kJ/mol"""),
#     longDesc=
#     u"""
#     copied over, not calculated!!
#     """,
# )
#
# entry(
#     index = 800,
#     label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_2 + cyanoisopropylOOH",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0,
#                          dEa = +|- 0.000483392 kJ/mol"""),
#     longDesc =
# u"""
# copied over, not calculated!!
# """,
# )
#
# entry(
#     index = 801,
#     label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_3 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(3.94097e+07, 'cm^3/(mol*s)'), n=0, Ea=(56.0508, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0,
#                      dEa = +|- 0.000364259 kJ/mol"""),
#     shortDesc = u"""k11+k12""",
# )
#
# entry(
#     index = 802,
#     label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_4 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(1.32296e+09, 'cm^3/(mol*s)'), n=0, Ea=(41.7324, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0,
#                      dEa = +|- 4.59316e-05 kJ/mol"""),
#     longDesc=
#     u"""
#     copied over, not calculated!!
#     """,
# )
#
# entry(
#     index = 803,
#     label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_1 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(4.7123e+06, 'cm^3/(mol*s)'), n=0, Ea=(24.1853, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0,
#                      dEa = +|- 0.000717396 kJ/mol"""),
#     longDesc=
#     u"""
#     copied over, not calculated!!
#     """,
# )
#
# entry(
#     index = 804,
#     label = "imipramine_ol_5 + cyanoisopropylOO <=> imipramine_ol_5_rad_5 + cyanoisopropylOOH",
#     kinetics=Arrhenius(A=(2.1327e+09, 'cm^3/(mol*s)'), n=0, Ea=(46.4329, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0,
#                      dEa = +|- 0.00509461 kJ/mol"""),
#     longDesc=
#     u"""
#     copied over, not calculated!!
#     """,
# )

# entry(
#     index = 30,
#     label = "imipramine_peroxide_2 + CH2OH <=> imipramine_peroxy_2 + CH3OH",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(4.95946e+07,'cm^3/(mol*s)'), n=0, Ea=(26.4854,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
# ts1043 rev
#
# TS external symmetry: 1, TS optical isomers: 2
#
# Optimized TS geometry:
# N      -0.38667800   -0.17036500   -0.19575800
# C       0.91071800   -0.48833400    0.32187200
# C      -1.27357400   -1.22967500   -0.53610800
# C       1.77296900   -1.37430200   -0.55933700
# C      -0.85172600    1.16059000   -0.06663400
# C      -1.12093700   -1.89646100   -1.74884000
# C      -2.30018000   -1.60773600    0.33222000
# C       2.18844300   -0.66867400   -1.84148200
# H       2.65588800   -1.66626500    0.01219400
# H       1.24332500   -2.29749100   -0.80502200
# C      -0.01869000    2.16039300   -0.58478900
# C      -2.06872100    1.52553000    0.52747600
# C      -1.94284400   -2.96205500   -2.08518400
# H      -0.35855800   -1.56531700   -2.44170000
# C      -2.55631900   -0.79932700    1.55991300
# C      -3.12734700   -2.66857000   -0.02244000
# N       2.90379100    0.57438500   -1.62547200
# H       1.29436000   -0.41919800   -2.41828800
# C      -0.36302800    3.49677300   -0.52480800
# H       0.92182500    1.86139400   -1.03666900
# C      -3.05915400    0.59124600    1.18110200
# C      -2.40514800    2.88154500    0.54436100
# C      -2.94651700   -3.35665300   -1.21311800
# H      -1.80550700   -3.47230000   -3.03231300
# H      -3.31313800   -1.29582700    2.17310600
# H      -1.65254700   -0.71154200    2.16494600
# H      -3.92651100   -2.95802800    0.65326400
# C       3.05699600    1.29651400   -2.86713900
# C       4.17805400    0.39070800   -0.96686400
# C      -1.57894600    3.86598900    0.03495900
# H       0.30829900    4.24508500   -0.93274100
# H      -3.42970800    1.09123600    2.08191200
# H      -3.92925900    0.47881000    0.52148200
# H      -3.34852700    3.16552100    1.00275400
# H      -3.59646800   -4.18751000   -1.46568400
# H       3.54097600    2.25728900   -2.68036300
# H       3.66486100    0.74769100   -3.60893400
# H       2.07759200    1.49094300   -3.31033000
# H       4.66557200    1.35985400   -0.84562900
# H       4.85923400   -0.26342600   -1.54120900
# H       4.04405800   -0.03472400    0.02727800
# H      -1.87669300    4.90772700    0.08042700
# C       2.77789300    0.25277900    3.32854800
# H       3.07670100    1.29204800    3.22023900
# H       2.75189200   -0.11372200    4.35907100
# O       3.44428300   -0.53922600    2.43220300
# H       3.07062500   -1.42838000    2.46390700
# H       1.42583200    0.45521400    0.49839100
# O       0.84690200   -1.17824100    1.59032900
# O       0.44028700   -0.28154400    2.56607500
# H       1.46269800    0.14166300    2.98121900
# H       2.78231100   -1.36900700   -2.45949100
# """,
# )
#


# entry(
#     index = 1057,
#     label = "imipramine_2_OOH_4_OO <=> imipramine_2_OOH_4_OOH_5_rad",
#     degeneracy = 6.0,
#     kinetics = Arrhenius(A=(5.0738e+10, 's^-1'), n=0, Ea=(43.3198, 'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     shortDesc = u"""""",
#     longDesc =
# u"""
# dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction
#
# Optimized TS geometry:
# O      -0.08336300   -0.90551700    3.12781100
# O      -0.84456100   -0.13681400    2.21753300
# C      -0.48128900   -0.45566200    0.87344300
# N       0.84602600   -0.02369200    0.51611600
# C       1.05526500    1.37779800    0.37548700
# C       0.99581600    2.19890700    1.49677600
# C       1.12341800    3.57296200    1.37579600
# C       1.32634400    4.13817200    0.12802800
# C       1.39686600    3.32196600   -0.98922800
# C       1.25135300    1.94477200   -0.88393700
# C       1.37874300    1.04981400   -2.07631400
# C       2.65677700    0.22324000   -1.98842000
# C       2.68351900   -0.87253800   -0.94407100
# C       1.83619000   -0.98397300    0.16981400
# C       1.95927300   -2.11172700    0.99082200
# C       2.89070200   -3.09923200    0.74516400
# C       3.75583600   -2.97492500   -0.32893700
# C       3.63718900   -1.87114400   -1.14743900
# C      -1.57994600    0.21912200    0.05820100
# C      -2.91369400   -0.48529200    0.23040900
# N      -4.02014700    0.22088400   -0.37998700
# C      -5.33050000   -0.21133500    0.08327100
# C      -3.88897700    0.33683600   -1.77370100
# O      -2.91446800   -1.81007800   -0.30614500
# O      -2.59992800   -1.77260900   -1.65974900
# H       0.74376600   -0.40765200    3.18096300
# H      -0.52635300   -1.53600300    0.73729100
# H       0.83151700    1.76050000    2.47093400
# H       1.07092000    4.19745100    2.25827800
# H       1.43219900    5.21048400    0.02413200
# H       1.55870700    3.76007400   -1.96747900
# H       0.51906100    0.37962500   -2.15563600
# H       1.40332100    1.65158800   -2.98588800
# H       3.49667200    0.90472700   -1.81796700
# H       2.83891900   -0.24880900   -2.95616500
# H       1.30371500   -2.20941400    1.84405400
# H       2.94621900   -3.95605500    1.40450000
# H       4.50224700   -3.73122600   -0.53351500
# H       4.29246500   -1.77793300   -2.00667500
# H      -1.68607500    1.26037500    0.36464600
# H      -1.28164000    0.19469400   -0.98643200
# H      -3.12992700   -0.63556700    1.28711400
# H      -6.08224000    0.49121500   -0.27422400
# H      -5.58276600   -1.21642300   -0.26987400
# H      -5.34736600   -0.20807000    1.17250600
# H      -3.34458100   -0.84863100   -2.04468400
# H      -4.83102100    0.50761700   -2.28581300
# H      -3.09566400    1.01038900   -2.09313600
# """,
# )
#
# entry(
#     index = 1061,
#     label = "imipramine_2_OO_4_OOH + CH3OH  <=> imipramine_2_OOH_4_OOH + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(6.95552e+06, 'cm^3/(mol*s)'), n=0, Ea=(60.5826, 'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     shortDesc = u"""""",
#     longDesc =
# u"""
# dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction
#
# Optimized TS geometry:
# O       0.78558000    1.71420700    2.10256500
# O       0.96652500    0.47424600    1.53138600
# C       0.34742300    0.39146700    0.24023300
# N      -1.06374100    0.14754400    0.25318900
# C      -1.52669800   -1.10748900    0.73480800
# C      -1.31999700   -1.46945000    2.06127200
# C      -1.72435700   -2.71571400    2.51384400
# C      -2.35180800   -3.59707200    1.64838800
# C      -2.57025900   -3.22831900    0.32993800
# C      -2.15302900   -1.99154000   -0.14346100
# C      -2.40508000   -1.55069100   -1.55232000
# C      -3.44115200   -0.43163300   -1.60654700
# C      -3.06227000    0.90590800   -1.00235800
# C      -1.97467600    1.15688700   -0.15193400
# C      -1.76220100    2.45833200    0.31215600
# C      -2.58270700    3.50391300   -0.06089000
# C      -3.66489600    3.26445400   -0.89193100
# C      -3.88908700    1.97773800   -1.33924000
# C       1.11643000   -0.72770400   -0.46209500
# C       2.61232000   -0.46958300   -0.50494200
# N       3.45183100   -1.50925600   -1.06104200
# C       3.84184500   -2.51733100   -0.09328000
# C       2.97120900   -2.08759300   -2.30464300
# O       2.77582600    0.70146300   -1.29330600
# O       4.14795800    1.06550200   -1.22680900
# H       1.78668100    2.36622500    1.73080400
# H       0.51503800    1.33735700   -0.27353000
# H      -0.83852400   -0.76850700    2.72813600
# H      -1.55834300   -2.99096000    3.54758500
# H      -2.67576400   -4.56874700    1.99926400
# H      -3.06448200   -3.91487900   -0.34812900
# H      -1.47486500   -1.20998100   -2.01410800
# H      -2.76774500   -2.39395600   -2.14247300
# H      -4.35161100   -0.78913500   -1.11426500
# H      -3.71166000   -0.25402700   -2.65024700
# H      -0.94447000    2.62730900    0.99910000
# H      -2.38710400    4.49939300    0.31736800
# H      -4.32659700    4.06825900   -1.18775000
# H      -4.73039000    1.78484400   -1.99636900
# H       0.94658200   -1.67249300    0.05911000
# H       0.71816200   -0.82813500   -1.47177700
# H       2.97412700   -0.26907800    0.50597300
# H       3.00294600   -3.15745600    0.21670300
# H       4.60973800   -3.15795900   -0.52882100
# H       4.25695800   -2.04065800    0.79503600
# H       2.67062500   -1.29310300   -2.98710200
# H       3.77865200   -2.65116900   -2.77361400
# H       2.12172800   -2.76887200   -2.15622200
# H       4.56552900    0.19314700   -1.37502000
# C       2.82339100    3.03616900    1.32948800
# O       3.93047700    2.24442700    1.32337900
# H       2.52370100    3.42130300    0.35221400
# H       2.89029000    3.80111100    2.10312100
# H       4.06165200    1.85116200    0.44448300
# """,
# )

# entry(
#     index = 1056,
#     label = "imipramine_2_OOH_4_OO + CH3OH  <=> imipramine_2_OOH_4_OOH + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(1.32522e+07,'cm^3/(mol*s)'), n=0, Ea=(54.2276,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction
#
# Optimized TS geometry:
# O      -2.34413400    0.29141200    2.93913700
# O      -1.67567600   -0.84794600    2.43125100
# C      -2.09775800   -2.03160000    3.11918400
# N      -1.62497500   -2.11174500    4.47753600
# C      -0.22956600   -2.32181700    4.67569300
# C       0.66471500   -1.30043400    4.36908500
# C       2.03183900   -1.50185100    4.48320000
# C       2.51362100   -2.72490800    4.92309300
# C       1.62246900   -3.73565100    5.25040400
# C       0.25020700   -3.55338000    5.12374800
# C      -0.71956300   -4.61529900    5.53583800
# C      -1.49024000   -4.18547300    6.77843100
# C      -2.50079600   -3.07143900    6.60600300
# C      -2.55897200   -2.15264200    5.54392600
# C      -3.60464600   -1.21937700    5.52311700
# C      -4.56859500   -1.17455300    6.51039500
# C      -4.49934200   -2.05840600    7.57678800
# C      -3.47261100   -2.98153200    7.60620400
# C      -1.58242100   -3.15234100    2.22277000
# C      -2.33206000   -3.23900300    0.89795500
# N      -1.70371600   -4.03025600   -0.13655700
# C      -0.65584100   -3.28036200   -0.81200700
# C      -1.19716000   -5.31182500    0.33498100
# O      -3.61204200   -3.77783200    1.24693800
# O      -4.55939500   -3.44595200    0.29731000
# H      -1.81537500    0.53213700    3.71324400
# H      -3.18587300   -2.04476700    3.14962900
# H       0.28794400   -0.34159400    4.04096400
# H       2.71579000   -0.69939800    4.23724400
# H       3.57948400   -2.89031900    5.01888800
# H       1.99395200   -4.68998900    5.60575000
# H      -1.42108500   -4.83580200    4.72832000
# H      -0.17928800   -5.53602500    5.75689700
# H      -0.76935000   -3.89597700    7.54976400
# H      -2.02695000   -5.04866900    7.17627500
# H      -3.64813300   -0.50564200    4.71296100
# H      -5.35998400   -0.43759300    6.45210300
# H      -5.23699500   -2.03423100    8.36876100
# H      -3.42204700   -3.69122600    8.42487500
# H      -0.51919200   -3.00371800    2.02495900
# H      -1.68647000   -4.09509900    2.75885600
# H      -2.49487900   -2.24108100    0.49125700
# H       0.19858300   -3.05139000   -0.15796400
# H      -0.28144700   -3.86442400   -1.65346300
# H      -1.05365700   -2.34097300   -1.19761900
# H      -1.97089200   -5.84338000    0.88852700
# H      -0.91770600   -5.92346900   -0.52351500
# H      -0.31181000   -5.21287700    0.97819100
# C      -5.31902000   -1.13566500    1.05509600
# O      -4.60211000   -0.16556900    0.39526300
# H      -4.96717900   -2.30049000    0.64554100
# H      -5.04916000   -1.16572300    2.10975100
# H      -6.39265200   -1.12191600    0.86111100
# H      -5.00837900    0.00646500   -0.45995300
# """,
# )
#
# entry(
#     index = 1059,
#     label = "imipramine_5_oo + CH3OH  <=> imipramine_5_ooh + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(3.42355e+06,'cm^3/(mol*s)'), n=0, Ea=(59.0094,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(T)/def2tzvp//wb97xd/def2svp with APFD SMD water for solvation sp correction
#
# Optimized TS geometry:
# C       2.62196200   -3.27034900   -0.04309900
# N       2.81787400   -2.34152300    1.04863700
# C       1.72956100   -2.14968400    1.99331700
# C       0.69847400   -1.05473700    1.68749000
# C      -0.02209900   -1.21316300    0.35056400
# N      -1.12565000   -0.27364600    0.20919000
# C      -0.85051900    1.11937500    0.16391500
# C       0.39385500    1.54711700   -0.33435500
# C       0.74177200    2.89076600   -0.38708000
# C      -0.16647200    3.85546900    0.04116900
# C      -1.40415800    3.44298100    0.51832900
# C      -1.77517200    2.09370500    0.60374700
# C      -3.15936200    1.82329400    1.16977600
# C      -3.54409900    0.37109900    1.44841600
# C      -3.54609300   -0.46224700    0.20018400
# C      -4.71719900   -0.94140300   -0.38955100
# C      -4.67379000   -1.72869300   -1.53923800
# C      -3.44354000   -2.03760600   -2.11623300
# C      -2.26763500   -1.54840800   -1.55203800
# C      -2.31079700   -0.75713800   -0.39862800
# C       3.70920800   -1.27666800    0.86664300
# O       3.18260900   -0.13873400    0.14444500
# O       3.04485200   -0.46056700   -1.19409100
# H       1.94446000   -2.90657500   -0.83679900
# H       3.59077700   -3.48862200   -0.51692600
# H       2.21864700   -4.21786500    0.34721700
# H       1.21563200   -3.11970300    2.09700200
# H       2.17028300   -1.93201700    2.98283400
# H      -0.05757900   -1.06712200    2.49032300
# H       1.18322400   -0.06799300    1.72803700
# H       0.70413500   -1.14646400   -0.47963000
# H      -0.45910700   -2.22223200    0.30301000
# H       1.11117600    0.81517600   -0.70242900
# H       1.72486300    3.16820700   -0.77430200
# H       0.08451400    4.91753600    0.00398500
# H      -2.12314900    4.19451300    0.85863300
# H      -3.90398900    2.24788200    0.47403800
# H      -3.25786000    2.40213800    2.10301000
# H      -2.83391300   -0.06496300    2.16957600
# H      -4.54078600    0.35218000    1.91400600
# H      -5.67963100   -0.70912300    0.07493200
# H      -5.59931100   -2.10415600   -1.98083600
# H      -3.39760000   -2.65183500   -3.01834300
# H      -1.30349600   -1.76968900   -2.01469400
# H       3.97688800   -0.82622000    1.83666000
# H       4.61429100   -1.61251900    0.33368000
# C       4.66224100    1.34507300   -1.74177900
# O       4.10232000    2.23942500   -0.88817200
# H       3.86746700    0.30759800   -1.71694400
# H       4.70149500    1.73621100   -2.76629000
# H       5.61117200    0.88637000   -1.40506300
# H       3.90051500    1.77260600   -0.06005300
# """,
# )
#
# entry(
#     index = 1060,
#     label = "imipramine_1_oo + CH3OH  <=> imipramine_1_ooh + CH2OH",
#     degeneracy = 3.0,
#     kinetics = Arrhenius(A=(1.17017e+07,'cm^3/(mol*s)'), n=0, Ea=(61.3971,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     longDesc =
# """
# dlpno-ccsd(T)/def2tzvp//wb97xd/def2svp with APFD SMD water for solvation sp correction
#
# Optimized TS geometry:
# C       2.70123500   -1.89470100    0.94991700
# N       1.66066200   -1.27122000    1.73383800
# C       0.81668900   -2.22679500    2.43020500
# C      -0.59996300   -1.71808800    2.71810800
# C      -1.61329300   -1.89787500    1.58107500
# N      -1.32534400   -1.14885500    0.37041800
# C      -0.43052300   -1.64406600   -0.60585200
# C      -0.47949800   -3.00607700   -0.95028200
# C       0.35970900   -3.55126100   -1.91419000
# C       1.26183600   -2.72960600   -2.58572700
# C       1.31409900   -1.38122000   -2.25417400
# C       0.50330700   -0.81565500   -1.26203400
# C       0.77187600    0.64002600   -0.94052300
# C      -0.02446900    1.29216800    0.18572600
# O       0.36320300    2.65664600    0.31479600
# O       1.43576700    2.77453100    1.16007300
# C      -1.50753400    1.24081200   -0.05425900
# C      -2.27567800    2.36179800   -0.37185200
# C      -3.65301400    2.24249300   -0.54583800
# C      -4.26813700    0.99842300   -0.41039600
# C      -3.50264700   -0.12656700   -0.11562800
# C      -2.11982000   -0.01407900    0.06334400
# C       2.19089300   -0.24699900    2.60079700
# H       2.26584600   -2.61364300    0.24087200
# H       3.45373500   -2.42981900    1.57402200
# H       3.23007700   -1.12985500    0.35983400
# H       1.29425000   -2.55003700    3.38316600
# H       0.74462600   -3.13331500    1.80782600
# H      -0.99707100   -2.26484600    3.59006600
# H      -0.56860000   -0.65661000    3.01341500
# H      -2.59814100   -1.57182600    1.94536500
# H      -1.71730900   -2.97523100    1.36734900
# H      -1.20937700   -3.65157200   -0.46016900
# H       0.29037900   -4.61466000   -2.15389800
# H       1.92273400   -3.13501600   -3.35430200
# H       2.03803300   -0.73376300   -2.75742100
# H       0.61397300    1.24837200   -1.84782200
# H       1.83938600    0.71659300   -0.68354100
# H       0.19907100    0.77568700    1.12890400
# H       2.40745800    2.76700600    0.49353000
# H      -1.78750500    3.33373500   -0.45377400
# H      -4.24934500    3.12594600   -0.78371900
# H      -5.34707700    0.90020800   -0.54909100
# H      -3.97173500   -1.10947400   -0.03065200
# H       2.66110100    0.54289500    1.99753500
# H       1.38947400    0.23982100    3.17506700
# H       2.93839800   -0.64191000    3.32758400
# C       3.56091000    2.71145700   -0.21028100
# O       4.08523800    1.44876600   -0.20120400
# H       4.17197400    3.48566100    0.28193400
# H       3.22528400    2.98507900   -1.21862100
# H       4.49410300    1.26931100    0.65178500
# """,
# )

# # imipramine + CH3OO updated to two para arrhenius fit (same as in training reaction)
#
# entry(
#     index = 0,
#     label = "imipramine + CH3OO <=> imipramine_rad_2 + CH3OOH",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(1.13218e+09,'cm^3/(mol*s)'), n=0, Ea=(58.5589,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.02664, dn = +|- 0,
#                          dEa = +|- 0.0671562 kJ/mol"""),
#     shortDesc = u"""k5+k6""",
#     longDesc =
# u"""
# H6 is blocked, H5 and H6 have the same 2D connectivity
# k6 = 0  =>  k5 + k6 = k5
# """,
# )
#
# entry(
#     index = 1,
#     label = "imipramine + CH3OO <=> imipramine_rad_3 + CH3OOH",
#     degeneracy = 2.0,
#     # duplicate = True,
#     kinetics = Arrhenius(A=(1.18283e+09,'cm^3/(mol*s)'), n=0, Ea=(71.1023,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00034, dn = +|- 0,
#                          dEa = +|- 0.000870252 kJ/mol"""),
#     # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
#     #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k11+k12""",
# )
#
# entry(
#     index = 2,
#     label = "imipramine + CH3OO <=> imipramine_rad_4 + CH3OOH",
#     degeneracy = 2.0,
#     # duplicate = True,
#     kinetics=Arrhenius(A=(1.11619e+10, 'cm^3/(mol*s)'), n=0, Ea=(52.9458, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00001, dn = +|- 0,
#                      dEa = +|- 1.85328e-05 kJ/mol"""),
#     # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
#     #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k20+k21""",
# )
#
# entry(
#     index = 3,
#     label = "imipramine + CH3OO <=> imipramine_rad_1 + CH3OOH",
#     degeneracy = 4.0,
#     # duplicate = True,
#     kinetics=Arrhenius(A=(3.18843e+07, 'cm^3/(mol*s)'), n=0, Ea=(35.8139, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00148, dn = +|- 0,
#                      dEa = +|- 0.00380887 kJ/mol"""),
#     # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
#     #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
#     #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
#     #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k28+k29+k35+k36""",
# )
#
# entry(
#     index = 4,
#     label = "imipramine + CH3OO <=> imipramine_rad_5 + CH3OOH",
#     degeneracy = 6.0,
#     # duplicate = True,
#     kinetics=Arrhenius(A=(8.81896e+09, 'cm^3/(mol*s)'), n=0, Ea=(56.8704, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00345, dn = +|- 0,
#                      dEa = +|- 0.00889234 kJ/mol"""),
# #     kinetics = MultiArrhenius(
# # #        arrhenius = [
# # #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# # #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# # #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# # #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# # #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# # #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# # #        ],
# #         arrhenius = [
# #             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #         ],
# #     ),
#     shortDesc = u"""k39+k40+k41+k42+k43+k44""",
#     longDesc =
# u"""
# Here rotors we not included in the calculation (Eventually we'd like to use rotors).
# We're definitely missing a factor of x3 of the torsion missing in the TS,
# we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
# """,
# )
#
#
#
# # imipramine + HO2 copied from CH3OO
#
# entry(
#     index = 10,
#     label = "imipramine + HO2 <=> imipramine_rad_2 + H2O2",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(1.13218e+09,'cm^3/(mol*s)'), n=0, Ea=(58.5589,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.02664, dn = +|- 0,
#                          dEa = +|- 0.0671562 kJ/mol"""),    shortDesc = u"""k5+k6""",
#     longDesc =
# u"""
# H6 is blocked, H5 and H6 have the same 2D connectivity
# k6 = 0  =>  k5 + k6 = k5
# """,
# )
#
# entry(
#     index = 11,
#     label = "imipramine + HO2 <=> imipramine_rad_3 + H2O2",
#     degeneracy = 2.0,
#     # duplicate = True,
#     kinetics = Arrhenius(A=(1.18283e+09,'cm^3/(mol*s)'), n=0, Ea=(71.1023,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00034, dn = +|- 0,
#                          dEa = +|- 0.000870252 kJ/mol"""),    # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
#     #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k11+k12""",
# )
#
# entry(
#     index = 12,
#     label = "imipramine + HO2 <=> imipramine_rad_4 + H2O2",
#     degeneracy = 2.0,
#     # duplicate = True,
#     kinetics=Arrhenius(A=(1.11619e+10, 'cm^3/(mol*s)'), n=0, Ea=(52.9458, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00001, dn = +|- 0,
#                      dEa = +|- 1.85328e-05 kJ/mol"""),    # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
#     #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k20+k21""",
# )
#
# entry(
#     index = 13,
#     label = "imipramine + HO2 <=> imipramine_rad_1 + H2O2",
#     degeneracy = 4.0,
#     # duplicate = True,
#     kinetics=Arrhenius(A=(3.18843e+07, 'cm^3/(mol*s)'), n=0, Ea=(35.8139, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00148, dn = +|- 0,
#                      dEa = +|- 0.00380887 kJ/mol"""),    # kinetics = MultiArrhenius(
#     #     arrhenius = [
#     #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
#     #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
#     #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
#     #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
#     #     ],
#     # ),
#     shortDesc = u"""k28+k29+k35+k36""",
# )
#
# entry(
#     index = 14,
#     label = "imipramine + HO2 <=> imipramine_rad_5 + H2O2",
#     degeneracy = 6.0,
#     # duplicate = True,
#     kinetics=Arrhenius(A=(8.81896e+09, 'cm^3/(mol*s)'), n=0, Ea=(56.8704, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
#                        Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00345, dn = +|- 0,
#                      dEa = +|- 0.00889234 kJ/mol"""),#     kinetics = MultiArrhenius(
# # #        arrhenius = [
# # #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# # #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# # #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# # #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# # #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# # #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# # #        ],
# #         arrhenius = [
# #             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #         ],
# #     ),
#     shortDesc = u"""k39+k40+k41+k42+k43+k44""",
#     longDesc =
# u"""
# Here rotors we not included in the calculation (Eventually we'd like to use rotors).
# We're definitely missing a factor of x3 of the torsion missing in the TS,
# we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
# """,
# )






