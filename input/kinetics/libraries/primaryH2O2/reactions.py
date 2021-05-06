#!/usr/bin/env python
# encoding: utf-8

name = "primaryH2O2"
shortDesc = u"primaryH2O2"
longDesc = u"""
Based on:
[Konnov2015] A.A. Konnov, "On the role of excited species in hydrogen combustion", Combustion and Flame 2015, 162, 3755-3772, DOI: 10.1016/j.combustflame.2015.07.014
[Konnov2019] A.A. Konnov, "Yet another kinetic mechanism for hydrogen combustion", Combustion and Flame 2019, 203, 14-22, DOI: 10.1016/j.combustflame.2019.01.032
Some reactions were commented out, because they have excited species, currently RMG dosn't support these excited species. 
"""

entry(
    index = 1,
    label = "H + O2 + H <=> H2 + O2",
    kinetics = Arrhenius(
             A = (8.80e+22, 'cm^6/(mol^2*s)', '*|/', 2),
             n = -1.835,
             Ea = (800, 'cal/mol'),
             Tmin = (300, 'K'),
             Tmax = (3000, 'K')),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 1""",
)

entry(
    index = 2,
    label = "H + O2 + H <=> OH + OH",
    kinetics = Arrhenius(
             A = (4.00e+22, 'cm^6/(mol^2*s)', '*|/', 2),
             n = -1.835,
             Ea = (800, 'cal/mol'),
             Tmin = (300, 'K'),
             Tmax = (3000, 'K')),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 2""",
)

entry(
    index = 3,
    label = "H + O2 + O <=> OH + O2",
    kinetics = Arrhenius(
             A = (7.35e+22, 'cm^6/(mol^2*s)', '*|/', 2),
             n = -1.835,
             Ea = (800, 'cal/mol'),
             Tmin = (300, 'K'),
             Tmax = (3000, 'K')),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 3""",
)

entry(
    index = 4,
    label = "H + O2 + OH <=> H2O + O2",
    kinetics = Arrhenius(
             A = (2.56e+22, 'cm^6/(mol^2*s)', '*|/', 2),
             n = -1.835,
             Ea = (800, 'cal/mol'),
             Tmin = (300, 'K'), 
             Tmax = (3000, 'K')),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 4""",
)

entry(
    index = 5,
    label = "OH + OH <=> H2O + O",
    kinetics = Arrhenius(
             A=(2.668e+06,'cm^3/(mol*s)', '*|/', 1.4),
             n=1.82,
             Ea=(-1647, 'cal/mol'),
             T0=(1, 'K'),
             Tmin=(200, 'K'),
             Tmax=(2000, 'K')),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 5""",
)

entry(
    index = 6,
    label = "H + O2 <=> HO2",
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
                      A = (4.66e+12, 'cm^3/(mol*s)', '*|/', 1.2), 
                      n = 0.44, 
                      Ea = (0, 'cal/mol'),
                      Tmin = (300, 'K'),
                      Tmax = (2000, 'K')),
        arrheniusLow = Arrhenius(
                      A = (1.225e+19, 'cm^6/(mol^2*s)', '*|/', 1.2),
                      n = -1.2, 
                      Ea = (0.0, 'cal/mol'),
                      Tmin = (1000, 'K'),
                      Tmax = (1430, 'K')),
#the value of T3 was calculated with the first factor of the Lindemann model
#and an Fcent value of 0.5 specified in the Konnov 2019 paper.
        T3 = (1752, 'K'),
        T1 = (1e-10, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 1.5, 'O=C=O': 3.61, '[He]': 0.57, '[Ar]': 0.72, 'O': 16.6}),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 6""",
)

entry(
    index = 7,
    label = "OH + HO2 <=> H2O + O2",
    kinetics = Arrhenius(
             A = (2.14e+06, 'cm^3/(mol*s)', '*|/', 2),
             n = 1.65, 
             Ea = (2180, 'cal/mol'),
             Tmin = (200, 'K'),
             Tmax = (2500, 'K')),
    shortDesc = u"""[Konnov2019]""",
    longDesc =u"""Table 1, Reaction 7""",
)

entry(
    index = 8,
    label = "H + H <=> H2",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow=Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)', '*|/', 2), n=-1.0, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                               Tmin=(77, 'K'), Tmax=(5000, 'K')),
            efficiencies={'N#N': 0.0, '[H]': 0.0, '[H][H]': 0.0, 'O': 14.3}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 1a""",
)

entry(
    index = 9,
    label = "H + H + H2 <=> H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)', '*|/', 2.5), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(50, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 1b""",
)

entry(
    index = 10,
    label = "H + H + N2 <=> H2 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.4e+18, 'cm^6/(mol^2*s)', '*|/', 3.2), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(77, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 1c""",
)

entry(
    index = 11,
    label = "H + H + H <=> H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+15, 'cm^6/(mol^2*s)', '*|/', 3.2), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(50, 'K'), Tmax=(5000, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 1d""",
)

entry(
    index = 12,
    label = "O + O <=> O2",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow=Arrhenius(
            A=(1e+17, 'cm^6/(mol^2*s)'),
            n=-1,
            Ea=(0, 'cal/mol'),
            T0=(1, 'K')),
        efficiencies={'N#N': 2.0, 'O': 5.0, '[O-][O+]=O': 8.0, '[O]': 28.8, '[O][O]': 8.0}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 2""",
)

entry(
    index = 13,
    label = "O + H <=> OH",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.75e+18, 'cm^6/(mol^2*s)'),
            n=-1,
            Ea=(0, 'cal/mol'),
            T0=(1, 'K')),
        efficiencies={'O': 5.0},
        comment="""NO/2.0/ N/2.0/"""),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 3""",
)

entry(
    index = 14,
    label = "H2O <=> H + OH",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.06e+27, 'cm^3/(mol*s)'),
            n=-3.312,
            Ea=(120770, 'cal/mol'),
            T0=(1, 'K')),
        efficiencies={'N#N': 2.0, 'O': 0.0, '[H][H]': 3.0, '[He]': 1.1, '[O][O]': 1.5}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 4a""",
)

entry(
    index = 15,
    label = "H2O + H2O <=> H + OH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(1e+26, 'cm^3/(mol*s)'),
        n=-2.44,
        Ea=(120160, 'cal/mol'),
        T0=(1, 'K'),
        comment="""CH4/7/ CO2 /4/"""),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 4b""",
)

entry(
    index = 16,
    label = "H + O2 (+AR) <=> HO2 (+AR)",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(4.66e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    arrheniusLow=Arrhenius(A=(4.57e+18, 'cm^6/(mol^2*s)'), n=-1.12, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    alpha=0.5, T3=(1, 'K'), T1=(1e+10, 'K'), efficiencies={}, comment="""CO2/2.4/ CH4/3.5/"""),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 5a""",
)

entry(
    index = 17,
    label = "H + O2 (+O2) <=> HO2 (+O2)",
    degeneracy = 1.0,
    kinetics = Troe(
        arrheniusHigh=Arrhenius(
            A=(4.66e+12, 'cm^3/(mol*s)'),
            n=0.44, Ea=(0, 'cal/mol'),
            T0=(1, 'K')),
        arrheniusLow=Arrhenius(
            A=(5.69e+18, 'cm^6/(mol^2*s)'),
            n=-1.094,
            Ea=(0, 'cal/mol'),
            T0=(1, 'K')),
        alpha=0.5,
        T3=(1, 'K'),
        T1=(1e+10, 'K'),
        efficiencies={}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 5c""",
)

entry(
    index = 18,
    label = "H + O2 (+H2O) <=> HO2 (+H2O)",
    degeneracy = 1.0,
    kinetics = Troe(
        arrheniusHigh=Arrhenius(A=(4.66e+12, 'cm^3/(mol*s)', '*|/', 1.2), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow=Arrhenius(A=(3.67e+19, 'cm^6/(mol^2*s)'), n=-1.0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha=0.8, T3=(1, 'K'), T1=(1e+10, 'K'),
        efficiencies={}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 5d""",
)

entry(
    index = 19,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1.0,
    kinetics = Troe(
        arrheniusHigh=Arrhenius(
            A=(2e+12, 's^-1'),
            n=0.9,
            Ea=(48750, 'cal/mol'),
            T0=(1, 'K')),
        arrheniusLow=Arrhenius(
            A=(2.49e+24, 'cm^3/(mol*s)'),
            n=-2.3,
            Ea=(48750, 'cal/mol'),
            T0=(1, 'K')),
        alpha=0.42,
        T3=(1, 'K'),
        T1=(1e+10, 'K'),
        efficiencies={'N#N': 1.5, 'O': 7.5, 'OO': 7.7, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 6""",
)

entry(
    index = 20,
    label = "O + H2 <=> OH + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(50800, 'cm^3/(mol*s)'),
        n=2.67,
        Ea=(6292, 'cal/mol'),
        T0=(1, 'K'),
        comment="""CO2/1.6/ CO/2.8/"""),
        shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 7""",
)

entry(
    index = 21,
    label = "H + O2 <=> OH + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(1.04e+14, 'cm^3/(mol*s)'),
        n=0,
        Ea=(15286, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 8""",
)

entry(
    index = 22,
    label = "H2 + OH <=> H2O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(2.14e+08, 'cm^3/(mol*s)'),
        n=1.52,
        Ea=(3450, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 9""",
)

entry(
    index = 23,
    label = "HO2 + O <=> OH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(2.85e+10, 'cm^3/(mol*s)'),
        n=1,
        Ea=(-723.9, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 11""",
)

entry(
    index = 24,
    label = "H + HO2 <=> OH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(7.08e+13, 'cm^3/(mol*s)'),
        n=0,
        Ea=(300, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 12""",
)

entry(
    index = 25,
    label = "H2O + O <=> H + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(2.2e+08, 'cm^3/(mol*s)'),
        n=2,
        Ea=(61600, 'cal/mol'),
        T0=(1, 'K')),
        shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 13""",
)

entry(
    index = 26,
    label = "H2 + O2 <=> H + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(740000, 'cm^3/(mol*s)'),
        n=2.43,
        Ea=(53500, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 14""",
)

entry(
    index = 27,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius=[Arrhenius(
            A=(1.03e+14, 'cm^3/(mol*s)'),
            n=0,
            Ea=(11040, 'cal/mol'),
            T0=(1, 'K')),
        Arrhenius(
            A=(1.94e+11, 'cm^3/(mol*s)'),
            n=0,
            Ea=(-1409, 'cal/mol'),
            T0=(1, 'K'))]),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 16""",
)

entry(
   index = 42,
   label = "HO2 + HO2 <=> H2O2 + O2",
   duplicate = True,
   kinetics = ThirdBody(
       arrheniusLow = Arrhenius(A=(6.84e+14, 'cm^6/(mol^2*s)'),
                                n=0,
                                Ea=(-1950, 'cal/mol'),
                                T0=(1, 'K'))),
   shortDesc = u"""[Konnov2015]""",
   longDesc = u"""Table 2, Reaction X6 It is pressure dependent, we need to fix it to ThirdBody""",
)

entry(
    index = 28,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(5.02e+06, 'cm^3/(mol*s)'),
        n=2.07,
        Ea=(4300, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 17""",
)

entry(
    index = 29,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(2.03e+07, 'cm^3/(mol*s)'),
        n=2.02,
        Ea=(2620, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 18""",
)

entry(
    index = 30,
    label = "H2O2 + O <=> HO2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(9.55e+06, 'cm^3/(mol*s)'),
        n=2,
        Ea=(3970, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 19""",
)

entry(
    index = 31,
    label = "H2O2 + OH <=> HO2 + H2O",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(
        arrhenius=[Arrhenius(
            A=(1.74e+12, 'cm^3/(mol*s)'),
            n=0,
            Ea=(318, 'cal/mol'),
            T0=(1, 'K')),
        Arrhenius(
            A=(7.59e+13, 'cm^3/(mol*s)'),
            n=0,
            Ea=(7269, 'cal/mol'),
            T0=(1, 'K'))]),
   shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 20""",
)

entry(
    index = 32,
    label = "O2 + O <=> O3",
    degeneracy = 1.0,
    kinetics = ThirdBody(
        arrheniusLow=Arrhenius(
            A=(6.53e+17, 'cm^6/(mol^2*s)'),
            n=-1.5,
            Ea=(0, 'cal/mol'),
            T0=(1, 'K')),
        efficiencies={'[Ar]': 0.0, '[O-][O+]=O': 2.5, '[O]': 4.0, '[O][O]': 0.95}),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 21a""",
)

entry(
    index = 33,
    label = "O3 + O <=> O2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(4.82e+12, 'cm^3/(mol*s)'),
        n=0,
        Ea=(4094, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 22a""",
)

entry(
    index = 34,
    label = "O3 + H <=> OH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(8.43e+13, 'cm^3/(mol*s)'),
        n=0,
        Ea=(934, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 36""",
)

entry(
    index = 35,
    label = "O3 + OH <=> HO2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(1e+12, 'cm^3/(mol*s)'),
        n=0,
        Ea=(1870, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 37""",
)
entry(
    index = 36,
    label = "O3 + HO2 <=> OH + O2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A=(0.000585, 'cm^3/(mol*s)'),
        n=4.57,
        Ea=(-1377, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 38""",
)

entry(
    index = 37,
    label = "O2 + O + AR <=> O3 + AR",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(
        arrhenius=[Arrhenius(
            A=(4.29e+17, 'cm^6/(mol^2*s)'),
            n=-1.5,
            Ea=(0, 'cal/mol'),
            T0=(1, 'K')),
        Arrhenius(
            A=(5.1e+21, 'cm^6/(mol^2*s)'),
            n=-3.2,
            Ea=(0, 'cal/mol'),
            T0=(1, 'K'))]),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 1, Reaction 21a""",
)

entry(
    index = 38,
    label = "H2 + O2 <=> OH + OH",
    kinetics = Arrhenius(
        A=(2.04e+12, 'cm^3/(mol*s)'),
        n=0.44,
        Ea=(69155, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 2, Reaction X1""",
)

entry(
    index = 39,
    label = "H2 + O2 <=> O + H2O",
    kinetics = Arrhenius(
        A=(3e+13, 'cm^3/(mol*s)'),
        n=0,
        Ea=(69545, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 2, Reaction X2""",
)

entry(
    index = 40,
    label = "H2 + O2 + O2 <=> HO2 + HO2",
    kinetics = Arrhenius(
        A=(2e+17, 'cm^6/(mol^2*s)'),
        n=0,
        Ea=(25830, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 2, Reaction X3""",
)

entry(
    index = 41,
    label = "HO2 + HO2 <=> H2O + O3",
    kinetics = Arrhenius(
        A=(100, 'cm^3/(mol*s)'),
        n=0,
        Ea=(0, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 2, Reaction X4, Data was not given """,
)

# entry (
#      index = 43
#      label = "HO2* + O2 = HO2 + O2"
#      kinetics = Arrhenius(
#          A=(3.6e+12, 'cm^3/(mol*s)'),
#          n=0,
#          Ea=(0,'cal/mol'),
#          T0=(1,'K')),
#      shortDesc = u"""[Konnov2015]""",
#      longDesc = u"""Table 2, Reaction X12"""
# )

entry(
   index = 44,
   label = "O + OH (+M) <=> HO2 (+M)",
   kinetics = Arrhenius(
       A=(1e+15, 'cm^3/(mol*s)'),
       n=0,
       Ea=(0, 'cal/mol'),
       T0=(1, 'K')),
   shortDesc = u"""[Konnov2015]""",
   longDesc =u"""Table 2, Reaction X13""",
)

entry(
   index = 45,
   label = "O3 + H <=> O + HO2 ",
   kinetics = Arrhenius(
       A=(100, 'cm^3/(mol*s)'),
       n=0,
       Ea=(0, 'cal/mol'),
       T0=(1, 'K')),
   shortDesc = u"""[Konnov2015]""",
   longDesc =u"""Table 2, Reaction X15. Data wasn't available from konnov 2015""",
)

entry(
    index = 46,
    label = "O3 + H2 <=> OH + HO2",
    kinetics = Arrhenius(
        A=(6e+10, 'cm^3/(mol*s)'),
        n=0,
        Ea=(20000, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 2, Reaction X18""",
)

# entry(
#     index = 47,
#     label = "H + OH + OH <=> OH* + H2O",
#     kinetics = Arrhenius(
#         A=(1.1e+16, 'cm^6/(mol^2*s)'),
#         n=0,
#         Ea=(0, 'cal/mol'),
#         T0=(1, 'K')),
#     shortDesc = u"""[Konnov2015]""",
#     longDesc =u"""Table 2, Reaction X19""",
# )

# entry(
#     index = 48,
#     label = "O + H (+M) <=> OH* (+M)",
#     kinetics = Arrhenius(
#         A=(1.5e+18, 'cm^6/(mol^2*s)'),
#         n=-1,
#         Ea=(0, 'cal/mol'),
#         T0=(1, 'K')),
#     shortDesc = u"""[Konnov2015]""",
#     longDesc =u"""Table 2, Reaction X20, It shouldn't be Arrhenius because its pressure dependant, we need to treat it differently """,
# as ThirdBody)
# entry(
#     index = 49,
#     label = "H2 + HO2 <=> H2O + OH*",
#     kinetics = Arrhenius(
#         A=(4.8e+19, 'cm^3/(mol*s)'),
#         n=-1.7,
#         Ea=(38000, 'cal/mol'),
#         T0=(1, 'K')),
#     shortDesc = u"""[Konnov2015]""",
#     longDesc =u"""Table 2, Reaction X21""",
# )

entry(
    index = 50,
    label = "H2O + OH <=> H2 + HO2",
    kinetics = Arrhenius(
        A=(7.9e+09, 'cm^3/(mol*s)'),
        n=0.43,
        Ea=(71700, 'cal/mol'),
        T0=(1, 'K')),
    shortDesc = u"""[Konnov2015]""",
    longDesc =u"""Table 2, Reaction X22""",
)

