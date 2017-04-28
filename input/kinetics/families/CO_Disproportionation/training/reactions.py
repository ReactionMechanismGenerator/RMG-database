#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "HCO + H <=> CO + H2",
    kinetics=Arrhenius(A=(9.03e+13,'cm^3/(mol*s)','*|/',2), n=0, Ea=(0,'cal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 519
R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J.A. Kerr, J. Troe,
Evaluated Kinetic Data for Combustion Modelling
Journal of Physical and Chemical Reference Data, 1992, 21, 411,
doi: 10.1063/1.555918
""",
)

entry(
    index = 2,
    label = "HCO + O <=> CO + OH",
    kinetics=Arrhenius(A=(3.01e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = u"""FFCM-1""",
    longDesc = 
u"""
Taken from the FFCM-1 library
""",
)

entry(
    index = 3,
    label = "HCO + O2 <=> CO + HO2",
    kinetics=Arrhenius(A=(5.12e+13,'cm^3/(mol*s)'), n=0, Ea=(1690,'cal/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 1147, rxn (15,3)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index = 4,
    label = "HCO + CH3 <=> CO + CH4",
    kinetics=Arrhenius(A=(4.0e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K'), Tmin=(1004,'K'), Tmax=(1006,'K')),
    rank = 1,
    shortDesc = u"""Shock Tube""",
    longDesc = 
u"""
p. 4131, Table 1, rxn [16]
reported at 1005 K (value is anyway T-independent)
A.M. Held, K.C. Manthorne, P.D. Pacey, H.P. Reinholdt,
Canadian Journal of Chemistry, 1977, 55(23), 4128-4134
doi: 10.1139/v77-585
""",
)

entry(
    index = 5,
    label = "HCO + CH3O <=> CO + CH3OH",
    kinetics=Arrhenius(A=(9.03e+13,'cm^3/(mol*s)','*|/',3), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 1246, rxn (24,15)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index = 6,
    label = "HCO + HCO_Y <=> CO + CH2O",
    kinetics=Arrhenius(A=(1.8e+13,'cm^3/(mol*s)','+|-',9e+12), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 1151, rxn (15,15 a)
W. Tsang and R. F. Hampson
Journal of Physical and Chemical Reference Data, 1986, 15, 1087
doi: 10.1063/1.555759
""",
)

entry(
    index = 7,
    label = "HCO + C2H3 <=> CO + C2H4",
    kinetics=Arrhenius(A=(9.033e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = u"""JetSurF2.0""",
    longDesc = 
u"""
Taken from the JetSurF2.0 library
""",
)

entry(
    index = 8,
    label = "HCO + nC3H7 <=> CO + C3H8_n",
    kinetics=Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = u"""JetSurF2.0""",
    longDesc = 
u"""
Taken from the JetSurF2.0 library
""",
)

entry(
    index = 9,
    label = "HCO + iC3H7 <=> CO + C3H8_i",
    kinetics=Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = u"""JetSurF2.0""",
    longDesc = 
u"""
Taken from the JetSurF2.0 library
""",
)

entry(
    index = 10,
    label = "HCO + NO <=> CO + HNO",
    kinetics=Arrhenius(A=(7.1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    rank = 1,
    shortDesc = u"""Shock Tube""",
    longDesc = 
u"""
p. 4180, Table 2, rxn 1
J. Dammeier , M. Colberg, G. Friedrichs,
Phys. Chem. Chem. Phys., 2007, 9, 4177-4188
doi: 10.1039/B704197G

[Also available from: Z.F. Xu, C.-H. Hsu, M.C. Lin, J. Chem. Phys., 2005, 122, 234308, doi: 10.1063/1.1917834
calculations done at the G2M(CC5)//B3LYP/6-311G(d, p) level of theory
T ranges: 200-500 & 500-3000 K]
""",
)

entry(
    index = 11,
    label = "HCO + NO2 <=> CO + HONO",
    kinetics=Arrhenius(A=(1.24e+23,'cm^3/(mol*s)'), n=-3.29, Ea=(2355,'cal/mol'), T0=(1,'K'), Tmin=(1140,'K'), Tmax=(1650,'K')),
    rank = 1,
    shortDesc = u"""Shock Tube""",
    longDesc = 
u"""
p. 463, Table II, rxn 2
C-Y. Lin, H-T. Wang, M.C. Lin, C.F. Melius,
Int. J. Chem. Kin, 1990, 22(5), 455-482
doi: 10.1002/kin.550220504
""",
)

