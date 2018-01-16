#!/usr/bin/env python
# encoding: utf-8

name = "BurkeH2O2inN2"
shortDesc = u"Library for H2 combustion by Burke et al."
longDesc = u"""
Comprehensive H2/O2 kinetic model for high-pressure combustion
M.P. Burke, M. Chaos, Y. Ju, F.L. Dryer, S.J. Klippenstein
International Journal of Chemical Kinetics
Volume 44, Issue 7, pages 444-474, July 2012
DOI: 10.1002/kin.20603

In this version of the library, the reaction H+O2(+M)=HO2(+M)
takes the form reccomended by the authors for the case of
N2 as the main bath gas.
"""
entry(
    index = 1,
    label = "H + O2 <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+14, 'cm^3/(mol*s)'), n=0, Ea=(15286, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Hong et al., Proc. Comb. Inst. 33:309-316 (2011)""",
)

entry(
    index = 2,
    label = "O + H2 <=> H + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.818e+12, 'cm^3/(mol*s)'), n=0, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.792e+14, 'cm^3/(mol*s)'), n=0, Ea=(19170, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)""",
)

entry(
    index = 3,
    label = "H2 + OH <=> H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+08, 'cm^3/(mol*s)'), n=1.51, Ea=(3430, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Michael and Sutherland, J. Phys. Chem. 92:3853 (1988)""",
)

entry(
    index = 4,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(33400, 'cm^3/(mol*s)'), n=2.42, Ea=(-1930, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)""",
)

entry(
    index = 5,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.577e+19, 'cm^3/(mol*s)'), n=-1.40, Ea=(104380, 'cal/mol'), T0 = (1, 'K')),
        efficiencies = {'[H][H]': 2.5, 'O': 12, '[C-]#[O+]': 1.9, 'O=C=O': 3.8, '[Ar]': 0, '[He]': 0},
    ),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 6,
    label = "H2 + Ar <=> H + H + Ar",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.84e+18, 'cm^3/(mol*s)'), n=-1.10, Ea=(104380, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 7,
    label = "H2 + He <=> H + H + He",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.84e+18, 'cm^3/(mol*s)'), n=-1.10, Ea=(104380, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 8,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.165e+15, 'cm^6/(mol^2*s)'), n=-0.50, Ea = (0, 'cal/mol'),T0 = (1, 'K')),
        efficiencies = {'[H][H]': 2.5, 'O': 12, '[C-]#[O+]': 1.9, 'O=C=O': 3.8, '[Ar]': 0, '[He]': 0},
    ),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 9,
    label = "O + O + Ar <=> O2 + Ar",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.886e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(-1788, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 10,
    label = "O + O + He <=> O2 + He",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.886e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(-1788, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 11,
    label = "O + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2.5, 'O': 12, '[C-]#[O+]': 1.9, 'O=C=O': 3.8, '[Ar]': 0.75, '[He]': 0.75},
    ),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 12,
    label = "H2O <=> H + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.064e+27, 'cm^3/(mol*s)'), n=-3.322, Ea=(120790, 'cal/mol'), T0 = (1, 'K')),
        efficiencies = {'[H][H]': 3, 'O': 0, '[C-]#[O+]': 1.9, 'O=C=O': 3.8, '[O][O]': 1.5, '[He]': 1.1, 'N#N': 2},
    ),
    shortDesc = u"""Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)""",
    longDesc = 
u"""
Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)
Rate constant is for Ar with efficiencies from Michael et al., J. Phys. Chem. A, 106 (2002)
Efficiencies for CO and CO2 taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
""",
)

entry(
    index = 13,
    label = "H2O + H2O <=> H + OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.006e+26, 'cm^3/(mol*s)'), n = -2.44, Ea = (120180, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)""",
)

entry(
    index = 14,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.65084e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0 = (1, 'K')),
        arrheniusLow = Arrhenius(A=(6.366e+20, 'cm^6/(mol^2*s)'), n = -1.72, Ea = (524.8, 'cal/mol'), T0 = (1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[O][O]': 0.78, '[C-]#[O+]': 1.9, 'O=C=O': 3.8, 'O': 14, '[He]': 0.8, '[Ar]': 0.67},
    ),
    shortDesc = u"""MAIN BATH GAS IS N2""",
    longDesc = 
u"""
High-pressure limit from Troe, Proc. Comb. Inst. 28:1463-1469 (2000)
Low-pressure limit from Michael et al., J. Phys. Chem. A 106:5297-5313
Centering factors from Fernandes et al., Phys. Chem. Chem. Phys. 10:4313-4321 (2008)
""",
)

entry(
    index = 15,
    label = "HO2 + H <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.75e+06, 'cm^3/(mol*s)'), n = 2.09, Ea = (-1451, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Michael et al., Proc. Comb. Inst. 28:1471 (2000)""",
    longDesc = 
u"""
Scaled by 0.75
Originally: 3.659E+06 2.09 -1.451E+03
""",
)

entry(
    index = 16,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Mueller et al., Int. J. Chem. Kinetic. 31:113 (1999)""",
)

entry(
    index = 17,
    label = "HO2 + O <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+10, 'cm^3/(mol*s)'), n = 1, Ea = (-723.93, 'cal/mol'), T0 = (1, 'K')),
    shortDesc = u"""Fernandez-Ramos and Varandas, J. Phys. Chem. A 106:4077-4083 (2002)""",
    longDesc = 
u"""
Scaled by 0.60
Originally: 4.750E+10 1.00 -7.2393E+02
""",
)

entry(
    index = 18,
    label = "HO2 + OH <=> H2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Keyser, J. Phys. Chem. 92:1193 (1988)""",
)

entry(
    index = 19,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(11982, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1629.3, 'cal/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""Hippler et al., J. Chem. Phys. 93:1755 (1990)""",
)

entry(
    index = 20,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.49e+24, 'cm^3/(mol*s)'), n=-2.3, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.43,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 3.7, 'O': 7.5, '[O][O]': 1.2, 'N#N': 1.5, '[C-]#[O+]': 2.8, 'OO': 7.7, 'O=C=O': 1.6, '[He]': 0.65},
    ),
    shortDesc = u"""Troe, Combust. Flame, 158:594-601 (2011)""",
    longDesc = 
u"""
Rate constant is for Ar
Efficiencies for H2 and CO taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
""",
)

entry(
    index = 21,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 22,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(7950, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 23,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)""",
)

entry(
    index = 24,
    label = "H2O2 + OH <=> HO2 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    shortDesc = u"""Hong et al., J. Phys. Chem. A 114 (2010) 5718-5727""",
)

