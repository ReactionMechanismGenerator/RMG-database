#!/usr/bin/env python
# encoding: utf-8

name = "primaryH2O2"
shortDesc = u"primaryH2O2"
longDesc = u"""
Based on:
[Baulch2005] D.L. Baulch, C.T. Bowman, C.J. Cobos, R.A. Cox, Th. Just, J.A. Kerr, M.J. Pilling, D. Stocker, J. Troe,
    W. Tsang, R.W. Walker, J. Warnatz, J. Phys. Chem. Ref. Data, 2005, 34, 757-1397, doi: 10.1063/1.1748524
[Hosein2007] M.S. Hosein, S. Vahid, Bull. Chem. Soc. Jpn., 2007, 80(10), 1901-1913, doi: 10.1246/bcsj.80.1901
[Klippenstein2022] S.J. Klippenstein, R. Sivaramakrishnan, U. Burke, K.P. Somers, H.J. Curran, L. Cai, H. Pitsch,
    M. Pelucchi, T. Faravelli, P. Glarborg, "HO2 + HO2: High level theory and the role of singlet channels",
    Combustion and Flame 2022, 243, 111975, doi: 10.1016/j.combustflame.2021.111975
[Konnov2015] A.A. Konnov, "On the role of excited species in hydrogen combustion", Combustion and Flame 2015, 
    162, 3755-3772, doi: 10.1016/j.combustflame.2015.07.014
[Konnov2019] A.A. Konnov, "Yet another kinetic mechanism for hydrogen combustion", Combustion and Flame 2019, 
    203, 14-22, doi: 10.1016/j.combustflame.2019.01.032
[Tsang1986] W. Tsang, R.F. Hampson, "Chemical Kinetic Data Base for Combustion Chemistry. Part I. Methane and Related Compounds",
    Journal of Physical and Chemical Reference Data, 1986,  15, 1087–1279, doi: 10.1063/1.555759
"""

entry(
    index=1,
    label="H + H <=> H2",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)', '*|/', 2), n=-1.0, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                               Tmin=(77, 'K'), Tmax=(5000, 'K')),
        efficiencies={'[Ar]': 0.0, '[He]': 0.0, 'N#N': 0.0, '[H]': 0.0, '[H][H]': 0.0, '[O][O]': 0.0, 'O': 14.3}),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 1a""",
)

entry(
    index=2,
    label="H + H + O2 <=> H2 + O2",
    kinetics=Arrhenius(A=(8.80e+22, 'cm^6/(mol^2*s)', '*|/', 2), n=-1.835, Ea=(800, 'cal/mol'), Tmin=(300, 'K'),
                       Tmax=(3000, 'K')),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""Table 1, Reaction 1""",
)

entry(
    index=3,
    label="H2 + Ar <=> H + H + Ar",
    kinetics=Arrhenius(A=(5.84e+18, 'cm^3/(mol*s)'), n=-1.10, Ea=(104380, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Tsang1986]""",
)

entry(
    index=4,
    label="H2 + He <=> H + H + He",
    kinetics=Arrhenius(A=(5.84e+18, 'cm^3/(mol*s)'), n=-1.10, Ea=(104380, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Tsang1986]""",
)

entry(
    index=5,
    label="H + H + H2 <=> H2 + H2",
    kinetics=Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)', '*|/', 2.5), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(50, 'K'), Tmax=(5000, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 1b""",
)

entry(
    index=6,
    label="H + H + N2 <=> H2 + N2",
    kinetics=Arrhenius(A=(5.4e+18, 'cm^6/(mol^2*s)', '*|/', 3.2), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(77, 'K'), Tmax=(2000, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Konnov (2015) https://doi.org/10.1016/j.combustflame.2015.07.014, Table 1, Reaction 1c""",
)

entry(
    index=7,
    label="H + H + H <=> H2 + H",
    kinetics=Arrhenius(A=(3.2e+15, 'cm^6/(mol^2*s)', '*|/', 3.2), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(50, 'K'),
                       Tmax=(5000, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 1d""",
)

entry(
    index=8,
    label="H + O2 + H <=> OH + OH",
    kinetics=Arrhenius(A=(4.00e+22, 'cm^6/(mol^2*s)', '*|/', 2), n=-1.835, Ea=(800, 'cal/mol'), Tmin=(300, 'K'),
                       Tmax=(3000, 'K')),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""Table 1, Reaction 2""",
)

entry(
    index=9,
    label="O + H <=> OH",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(6.75e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(2950, 'K'),
                               Tmax=(3700, 'K')),
        efficiencies={'O': 5.0, '[H][H]': 2.5, '[C-]#[O+]': 1.9, 'O=C=O': 3.8, '[Ar]': 0.75, '[He]': 0.75,
                      '[O][O]': 0.0}),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
Table 1, Reaction 3
The efficiency for H2O was taken from Konnov 2015, other collider efficiencies were taken from Curran 10.1016/j.combustflame.2015.09.014
Note that in the Curran library th efficiency for O2 was 12, her for consistency we remain with
the Konnov recommendation of collision efficiency for O2 of 5.
""",
)

entry(
    index=10,
    label="H + O + O2 <=> OH + O2",
    kinetics=Arrhenius(A=(7.35e+22, 'cm^6/(mol^2*s)', '*|/', 2), n=-1.835, Ea=(800, 'cal/mol'), Tmin=(300, 'K'),
                       Tmax=(3000, 'K')),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""Table 1, Reaction 3""",
)

entry(
    index=11,
    label="H2O <=> H + OH",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(6.06e+27, 'cm^3/(mol*s)'), n=-3.312, Ea=(120770, 'cal/mol'), T0=(1, 'K'),
                               Tmin=(300, 'K'), Tmax=(3400, 'K')),
        efficiencies={'N#N': 2.0, 'O': 0.0, '[H][H]': 3.0, '[He]': 1.1, '[O][O]': 0.0, '[C-]#[O+]': 1.9, 'O=C=O': 3.8}),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 4a
Note that in Konnov2015 the collision efficiency for O2 was 1.5, but Konnov2019 updated the rate
for the specific collider (see reaction index 13). THerefore, an efficiency of 0 was given here for O2.
""",
)

entry(
    index=12,
    label="H2O + H2O <=> H + OH + H2O",
    kinetics=Arrhenius(A=(1e+26, 'cm^3/(mol*s)'), n=-2.44, Ea=(120160, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'),
                       Tmax=(3400, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
Table 1, Reaction 4b
Originally from Srinivasan and Michael, Int. J. Chem. Kinetic 38 (2006)
""",
)

entry(
    index=13,
    label="H + OH + O2 <=> H2O + O2",
    kinetics=Arrhenius(A=(2.56e+22, 'cm^6/(mol^2*s)', '*|/', 2), n=-1.835, Ea=(800, 'cal/mol'), Tmin=(300, 'K'),
                       Tmax=(3000, 'K')),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""Table 1, Reaction 4""",
)

entry(
    index=14,
    label="H + O2 <=> HO2",
    kinetics=Troe(
        arrheniusHigh=Arrhenius(A=(4.66e+12, 'cm^3/(mol*s)', '*|/', 1.2), n=0.44, Ea=(0, 'cal/mol'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        arrheniusLow=Arrhenius(A=(1.225e+19, 'cm^6/(mol^2*s)', '*|/', 1.2), n=-1.2, Ea=(0.0, 'cal/mol'), Tmin=(1000, 'K'), Tmax=(1430, 'K')),
        T1=(1e-10, 'K'), T2=(1e+30, 'K'), T3=(1752, 'K'),
        efficiencies={'[H][H]': 1.5, 'O=C=O': 3.61, '[He]': 0.57, '[Ar]': 0.72, 'O': 16.6}, ),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""
Table 1, Reaction 6
The value of T3 was calculated with the first factor of the Lindemann model and an Fcent 
value of 0.5 specified in the Konnov 2019 paper.
""",
)

entry(
    index=15,
    label="H + O2 <=> OH + O",
    kinetics=Arrhenius(A=(1.04e+14, 'cm^3/(mol*s)'), n=0, Ea=(15286, 'cal/mol'), T0=(1, 'K'), Tmin=(1100, 'K'),
                       Tmax=(3370, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
Table 1, Reaction 8
Originally based on Hong et al., Proc. Comb. Inst. 33:309-316 (2011)
""",
)

entry(
    index=16,
    label="OH + OH <=> H2O + O",
    kinetics=Arrhenius(A=(2.668e+06, 'cm^3/(mol*s)', '*|/', 1.4), n=1.82, Ea=(-1647, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(200, 'K'), Tmax=(2000, 'K')),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""Table 1, Reaction 5""",
)

entry(
    index=17,
    label="OH + HO2 <=> H2O + O2",
    kinetics=Arrhenius(A=(2.14e+06, 'cm^3/(mol*s)', '*|/', 2), n=1.65, Ea=(2180, 'cal/mol'), Tmin=(200, 'K'),
                       Tmax=(2500, 'K')),
    shortDesc=u"""[Konnov2019]""",
    longDesc=u"""Table 1, Reaction 7""",
)

entry(
    index=18,
    label="O + O <=> O2",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'),
                               Tmax=(5000, 'K')),
        efficiencies={'[Ar]': 0.0, '[He]': 0.0, 'N#N': 2.0, '[N]=O': 2.0, '[N]': 2.0, 'O': 5.0, '[O-][O+]=O': 8.0,
                      '[O]': 28.8, '[O][O]': 8.0}),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 2""",
)

entry(
    index=19,
    label="O + O + Ar <=> O2 + Ar",
    kinetics=Arrhenius(A=(1.886e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(-1788, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Tsang1986]""",
)

entry(
    index=20,
    label="O + O + He <=> O2 + He",
    kinetics=Arrhenius(A=(1.886e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(-1788, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Tsang1986]""",
)

entry(
    index=21,
    label="H2O + O <=> H + HO2",
    kinetics=Arrhenius(A=(2.2e+08, 'cm^3/(mol*s)'), n=2, Ea=(61600, 'cal/mol'), T0=(1, 'K'), Tmin=(1500, 'K'),
                       Tmax=(4000, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 13""",
)

entry(
    index=22,
    label="H2O + OH <=> H2 + HO2",
    kinetics=Arrhenius(A=(7.9e+09, 'cm^3/(mol*s)'), n=0.43, Ea=(71700, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X22""",
)

entry(
    index=23,
    label="H2O2 <=> OH + OH",
    kinetics=Troe(
        arrheniusHigh=Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48750, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(1500, 'K')),
        arrheniusLow=Arrhenius(A=(2.49e+24, 'cm^3/(mol*s)'), n=-2.3, Ea=(48750, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(1500, 'K')),
        alpha=0.42, T3=(1e+30, 'K'), T1=(1e+30, 'K'),
        efficiencies={'N#N': 1.5, 'O': 7.5, 'OO': 7.7, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2, '[C-]#[O+]': 2.8,
                      'O=C=O': 1.6, }),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 6""",
)

entry(
    index=24,
    label="H2O2 + H <=> HO2 + H2",
    kinetics=Arrhenius(A=(5.02e+06, 'cm^3/(mol*s)'), n=2.07, Ea=(4300, 'cal/mol'), Tmin=(300, 'K'), Tmax=(2400, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 17""",
)

entry(
    index=25,
    label="H2O2 + H <=> H2O + OH",
    kinetics=Arrhenius(A=(2.03e+07, 'cm^3/(mol*s)'), n=2.02, Ea=(2620, 'cal/mol'), Tmin=(300, 'K'), Tmax=(2400, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 18""",
)

entry(
    index=26,
    label="H2O2 + O <=> HO2 + OH",
    kinetics=Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
Table 1, Reaction 19
Originally from Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index=27,
    label="H2O2 + OH <=> HO2 + H2O",
    kinetics=MultiArrhenius(
        arrhenius=[Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), Tmin=(280, 'K'), Tmax=(1640, 'K')),
                   Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7269, 'cal/mol'), T0=(1, 'K'))]),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
Table 1, Reaction 20
Originally from Hong et al., J. Phys. Chem. A, 114:5718 (2010)
""",
)

entry(
    index=28,
    label="O + H2 <=> OH + H",
    kinetics=Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6292, 'cal/mol'), Tmin=(297, 'K'), Tmax=(2495, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 7""",
)

entry(
    index=29,
    label="H2 + OH <=> H2O + H",
    kinetics=Arrhenius(A=(2.14e+08, 'cm^3/(mol*s)'), n=1.52, Ea=(3450, 'cal/mol'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
    Table 1, Reaction 9
    Originally based on Michael and Sutherland, J. Phys. Chem. 92:3853 (1988)
    """,
)

entry(
    index=30,
    label="HO2 + O <=> OH + O2",
    kinetics=Arrhenius(A=(2.85e+10, 'cm^3/(mol*s)'), n=1, Ea=(-723.9, 'cal/mol'), Tmin=(150, 'K'), Tmax=(1600, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
    Table 1, Reaction 11
    Originally taken from Fernandez-Ramos and Varandas, J. Phys. Chem. A 106:4077-4083 (2002)
    """,
)

entry(
    index=31,
    label="H + HO2 <=> OH + OH",
    kinetics=Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), Tmin=(300, 'K'), Tmax=(1000, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
    Table 1, Reaction 12
    Originally taken by Mueller et al., Int. J. Chem. Kinetic. 31:113 (1999)
    """,
)

entry(
    index=32,
    label="H2 + O2 <=> H + HO2",
    kinetics=Arrhenius(A=(740000, 'cm^3/(mol*s)'), n=2.43, Ea=(53500, 'cal/mol'), Tmin=(400, 'K'), Tmax=(2300, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 14""",
)

entry(
    index=33,
    label="HO2 + HO2 <=> H2O2 + O2",
    kinetics=Arrhenius(A=(1.93E-02, 'cm^3/(mol*s)'), n=4.12, Ea=(-9857, 'cal/mol'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
    shortDesc=u"""[Klippenstein2022]""",
    longDesc=u"""CASPT2""",
)

entry(
    index=34,
    label="HO2 + HO2 <=> H2O + O3",
    kinetics=Arrhenius(A=(100, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X4""",
)

entry(
    index=35,
    label="O2 + O <=> O3",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(6.53e+17, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                               Tmin=(100, 'K'), Tmax=(1000, 'K')),
        efficiencies={'[Ar]': 0.0, '[He]': 0.0, '[O-][O+]=O': 2.5, '[O]': 4.0, '[O][O]': 0.95}),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 21b""",
)

entry(
    index=36,
    label="O2 + O + Ar <=> O3 + Ar",
    kinetics=MultiArrhenius(
        arrhenius=[Arrhenius(A=(4.29e+17, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                             Tmin=(80, 'K'), Tmax=(1500, 'K')),
                   Arrhenius(A=(5.1e+21, 'cm^6/(mol^2*s)'), n=-3.2, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                             Tmin=(80, 'K'), Tmax=(1500, 'K'))]),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 21a""",
)

entry(
    index=37,
    label="O2 + O + He <=> O3 + He",
    kinetics=MultiArrhenius(
        arrhenius=[Arrhenius(A=(4.29e+17, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                             Tmin=(80, 'K'), Tmax=(1500, 'K')),
                   Arrhenius(A=(5.1e+21, 'cm^6/(mol^2*s)'), n=-3.2, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                             Tmin=(80, 'K'), Tmax=(1500, 'K'))]),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
Duplicated reaction of Konnov (2015) https://doi.org/10.1016/j.combustflame.2015.07.014, Table 1, 
Reaction 21a using He as a collider instead of Ar since it is expected to behave similarly as Ar in terms
of energy transfer.
""",
)

entry(
    index=38,
    label="O3 + O <=> O2 + O2",
    kinetics=Arrhenius(A=(4.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(4094, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(200, 'K'), Tmax=(400, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 22a""",
)

entry(
    index=39,
    label="O3 + H <=> OH + O2",
    kinetics=Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(934, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(200, 'K'), Tmax=(430, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 36""",
)

entry(
    index=40,
    label="O3 + H <=> O + HO2",
    kinetics=Arrhenius(A=(100, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""
    Table 2, Reaction X15 
    No data was given, the rate is very low.
    """,
)

entry(
    index=41,
    label="O3 + OH <=> HO2 + O2",
    kinetics=Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(1870, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(220, 'K'), Tmax=(450, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 37""",
)
entry(
    index=42,
    label="O3 + HO2 <=> OH + O2 + O2",
    kinetics=Arrhenius(A=(5.85e-4, 'cm^3/(mol*s)'), n=4.57, Ea=(-1377, 'cal/mol'), T0=(1, 'K'),
                       Tmin=(250, 'K'), Tmax=(340, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 1, Reaction 38""",
)

entry(
    index=43,
    label="O3 + H2 <=> OH + HO2",
    kinetics=Arrhenius(A=(6e+10, 'cm^3/(mol*s)'), n=0, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X18""",
)

entry(
    index=44,
    label="H2 + O2 <=> OH + OH",
    kinetics=Arrhenius(A=(2.04e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(69155, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X1""",
)

entry(
    index=45,
    label="H2 + O2 => O + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(69545, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X2""",
)

entry(
    index=46,
    label="H2 + O2 + O2 => HO2 + HO2",
    reversible = False,
    kinetics=Arrhenius(A=(2e+17, 'cm^6/(mol^2*s)'), n=0, Ea=(25830, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X3""",
)

entry(
    index=47,
    label="O + OH <=> HO2",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(1e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'))),
    shortDesc=u"""[Konnov2015]""",
    longDesc=u"""Table 2, Reaction X13""",
)

entry(
    index=48,
    label="HO2 + H <=> H2O2",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(6.0E+14, 'cm^6/(mol^2*s)'), n=1.25, Ea=(-270, 'cal/mol'), T0=(1, 'K'))),
    shortDesc=u"""[Hosein2007]""",
    longDesc = u"""
Reaction X2 in Burke at el. (Table III),
p. 1909 in Hosein2007
Declared 'negligible' by Burke at el.
The original rate Arrhenius(A=(7.20E+09, 'cm^6/(mol^2*s)'), n=1.25, Ea=(-270, 'cal/mol'), T0 = (1, 'K')) was
multiplied by the inverse of ~1.2E-05 mol cm^-3 which is the density of an ideal gas at 1000 K,
so that a ThirdBody kinetics format could be written here
""",
)

entry(
    index=49,
    label="H2O2 + O <=> H2O + O2",
    kinetics=Arrhenius(A=(8.43E+11, 'cm^3/(mol*s)'), n=0.00, Ea=(3.970E+03, 'cal/mol'), T0=(1, 'K')),
    shortDesc=u"""[Baulch2005]""",
    longDesc=u"""Added from the BurkeH2O2 library Reaction X5 in Burke at el. (Table III), Upper limit""",
)

entry(
    index=50,
    label="HO2 + HO2 <=> O2 + OH + OH",
    kinetics=Arrhenius(A=(6.41E17, 'cm^3/(mol*s)'), n=-1.54, Ea=(16971, 'cal/mol'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
    shortDesc=u"""[Klippenstein2022]""",
    longDesc=u"""CASPT2""",
)
