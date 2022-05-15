#!/usr/bin/env python
# encoding: utf-8

name = "API"
shortDesc = ""
longDesc = """
A kinetic library for Active Pharmaceutical Ingredient (API) degradation.
"""

entry(
    index = 1,
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
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 2,
    label = "imipramine + OHCH2OO <=> imipramine_2_rad + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9416.35,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(43.8278,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.05306, dn = +|- 0, dEa = +|- 0.133341 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
u"""
Rate duplicated from "imipramine + OHCH2OO <=> imipramine_4_rad + OHCH2OOH"
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 3,
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
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 4,
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
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 5,
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
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 6,
    label = "imipramine + O2 <=> imipramine_1_rad + HO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.82123e+14,'cm^3/(mol*s)'), n=0, Ea=(149.699,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.0007, 
                         dn = +|- 0, dEa = +|- 0.00181463 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) as suggested by W.H. Green
""",
)

entry(
    index = 7,
    label = "imipramine + O2 <=> imipramine_2_rad + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.05571e+14,'cm^3/(mol*s)'), n=0, Ea=(176.536,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00064, 
                         dn = +|- 0, dEa = +|- 0.00164057 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) as suggested by W.H. Green
""",
)

entry(
    index = 8,
    label = "imipramine + O2 <=> imipramine_3_rad + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.44909e+14,'cm^3/(mol*s)'), n=0, Ea=(205.239,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00105, 
                         dn = +|- 0, dEa = +|- 0.0027046 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) as suggested by W.H. Green
""",
)

entry(
    index = 9,
    label = "imipramine + O2 <=> imipramine_4_rad + HO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.47872e+15,'cm^3/(mol*s)'), n=0, Ea=(185.599,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00053, 
                         dn = +|- 0, dEa = +|- 0.00137809 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) as suggested by W.H. Green
""",
)

entry(
    index = 10,
    label = "imipramine + O2 <=> imipramine_5_rad + HO2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(6.8117e+14,'cm^3/(mol*s)'), n=0, Ea=(186.187,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.0007, 
                         dn = +|- 0, dEa = +|- 0.00180928 kJ/mol"""),
    shortDesc = u"""diffusion limit""",
    longDesc =
u"""
Reversed from diffusion limit rate for HO2 + R = 1e+13 cm^3/(mol*s) as suggested by W.H. Green
""",
)

entry(
    index = 11,
    label = "imipramine_2_oo + CH3OH <=> imipramine_2_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(558.874,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(60.2925,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.27364, dn = +|- 0, dEa = +|- 0.623798 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Rate duplicated from "imipramine_4_oo + CH3OH <=> imipramine_4_ooh + CH2OH"
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 12,
    label = "imipramine_5_oo + CH3OH <=> imipramine_5_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(73.3098,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(50.8673,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.2162, dn = +|- 0, dEa = +|- 0.504781 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 13,
    label = "imipramine_4_oo + CH3OH <=> imipramine_4_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(558.874,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(60.2925,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.27528, dn = +|- 0, dEa = +|- 0.627125 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 14,
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
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 15,
    label = "imipramine_5_oo <=> imipramine_5_ooh_4_rad",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.18089e+08,'s^-1'), 
                         n=0, 
                         Ea=(63.6186,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 16,
    label = "imipramine_5_oo <=> imipramine_5_ooh_5_rad",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.18089e+08,'s^-1'), 
                         n=0, 
                         Ea=(63.6186,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

# entry(
#     index = 17,
#     label = "imipramine_2_od_4_ooh + H2O <=> imipramine_tail_acetate_1 + iminobibenzyl",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'),
#                          n=2,
#                          Ea=(20,'kJ/mol'),
#                          T0=(1,'K'),
#                          Tmin=(275,'K'),
#                          Tmax=(350,'K'),
#                          comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
#     shortDesc = u"""Estimated""",
#     longDesc =
# """
# Estimated based on amide alcoholysis training reactions. Ea is high on purpose to avoid endothermicity correction.
# """,
# )

# entry(
#     index = 18,
#     label = "imipramine_2_od_4_od + H2O <=> imipramine_tail_acetate_3 + iminobibenzyl",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'),
#                          n=2,
#                          Ea=(20,'kJ/mol'),
#                          T0=(1,'K'),
#                          Tmin=(275,'K'),
#                          Tmax=(350,'K'),
#                          comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
#     shortDesc = u"""Estimated""",
#     longDesc =
# """
# Estimated based on amide alcoholysis training reactions. Ea is high on purpose to avoid endothermicity correction.
# """,
# )

# entry(
#     index = 19,
#     label = "imipramine_2_oh_4_od <=> imipramine_tail_derivative_1 + iminobibenzyl",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(1e+13, 's^-1'), n=2.0, Ea=(60, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     shortDesc = u"""Estimated""",
#     longDesc =
# """
# Same estimation as hemiaminal hydrolysis training reaction.
# """,
# )

entry(
    index = 20,
    label = "imipramine_2_ooh_4_od + H2O <=> imipramine_2_oh_4_od + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+18,'cm^3/(mol*s)'), n=0, Ea=(25,'kcal/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    shortDesc = u"""Estimated""",
    longDesc =
"""
10x than training reaction estimation.
""",
)

entry(
    index = 21,
    label = "imipramine_1_oo + CH3OH <=> imipramine_1_ooh + CH2OH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(558.874,'m^3/(mol*s)'), 
                         n=0, 
                         Ea=(60.2925,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.27364, dn = +|- 0, dEa = +|- 0.623798 kJ/mol"""),
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic
conventional transition state theory with Eckart tunneling (MS-LH-CTST/Eckart).
Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 22,
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
    index = 23,
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
