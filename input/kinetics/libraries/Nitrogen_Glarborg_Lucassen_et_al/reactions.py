#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen_Glarborg_Lucassen_et_al"
shortDesc = u""
longDesc = u"""
Arnas Lucassen, Kuiwen Zhang, Julia Warkentin, Kai Moshammer, Peter Glarborg, Paul Marshall, Katharina Kohse-Höinghaus
Fuel-nitrogen conversion in the combustion of small amines using dimethylamine and ethylamine as biomass-related model fuels
Combustion and Flame 159 (2012) 2254–2279
"""
entry(
    index = 1,
    label = "CH3NH2 <=> CH2NH + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(107260, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 2,
    label = "CH3NH2 + H <=> CH2NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5464, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "CH3NH2 + H <=> CH3NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(9706, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "CH3NH2 + O <=> CH2NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5196, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "CH3NH2 + O <=> CH3NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6348, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "CH3NH2 + OH <=> CH2NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "CH3NH2 + OH <=> CH3NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "CH3NH2 + CH3 <=> CH2NH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9170, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "CH3NH2 + CH3 <=> CH3NH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "CH3NH2 + NH2 <=> CH2NH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5494, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "CH3NH2 + NH2 <=> CH3NH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "CH2NH2 <=> CH2NH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+45, 's^-1'), n=-10.24, Ea=(47817, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "CH2NH2 + H <=> CH2NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "CH2NH2 + O <=> CH2O + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "CH2NH2 + O <=> CH2NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "CH2NH2 + OH <=> CH2OH + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "CH2NH2 + OH <=> CH2NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "CH2NH2 + O2 <=> CH2NH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+22, 'cm^3/(mol*s)'), n=-3.09, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "CH2NH2 + CH3 <=> C2H5 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "CH2NH2 + CH3 <=> CH2NH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-626, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "CH3NH <=> CH2NH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+36, 's^-1'), n=-7.92, Ea=(36342, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "CH3NH + H <=> CH2NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "CH3NH + O <=> CH2NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "CH3NH + OH <=> CH2NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "CH3NH + CH3 <=> CH2NH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 26,
    label = "CH2NH + H <=> H2CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(7322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "CH2NH + H <=> HCNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "CH2NH + O <=> H2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "CH2NH + O <=> HCNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5404, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "CH2NH + O <=> CH2O + NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+06, 'cm^3/(mol*s)'), n=2.08, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "CH2NH + OH <=> H2CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "CH2NH + OH <=> HCNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(457, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "CH2NH + CH3 <=> H2CN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(7123, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "CH2NH + CH3 <=> HCNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(530000, 'cm^3/(mol*s)'), n=1.87, Ea=(9687, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "CH2NH + NH2 <=> H2CN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(4441, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "CH2NH + NH2 <=> HCNH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6090, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "H2CN <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+29, 's^-1'), n=-6.03, Ea=(29894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "H2CN + H <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "H2CN + O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "H2CN + OH <=> HCN + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.1e+17, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (318, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 42,
    label = "H2CN + O2 <=> CH2O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(5961, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "H2CN + NH2 <=> HCN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 44,
    label = "H2CN + NH <=> HCN + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "H2CN + N <=> CH2 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "HCNH <=> HCN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.7e+25, 's^-1'), n=-5.2, Ea=(21986, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "HCNH + H <=> H2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "HCNH + H <=> HCN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "HCNH + O <=> HNCO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "HCNH + O <=> HCN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "HCNH + OH <=> HCN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "HCNH + CH3 <=> HCN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 53,
    label = "CH3CH2NH2 <=> C2H4 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.2e+67, 's^-1'), n=-15.944, Ea=(99348, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "CH3CHNH2 + H <=> CH3CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0.22, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH2CH2NH2 + H <=> CH3CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0.16, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH3CH2NH2 + H <=> CH2CH2NH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(5100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "CH3CH2NH2 + H <=> CH3CHNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+07, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (2830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 58,
    label = "CH3CH2NH2 + H <=> CH3CH2NH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(9700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "CH3CH2NH2 + O <=> CH2CH2NH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.4e+07, 'cm^3/(mol*s)'), n=1.7, Ea=(5460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "CH3CH2NH2 + O <=> CH3CHNH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "CH3CH2NH2 + O <=> CH3CH2NH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6348, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "CH3CH2NH2 + OH <=> CH2CH2NH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(1300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "CH3CH2NH2 + OH <=> CH3CHNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "CH3CH2NH2 + OH <=> CH3CH2NH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(447, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "CH3CH2NH2 + HO2 <=> CH2CH2NH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12000, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "CH3CH2NH2 + HO2 <=> CH3CHNH2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "CH3CH2NH2 + CH3 <=> CH2CH2NH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.18, Ea=(9620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "CH3CH2NH2 + CH3 <=> CH3CHNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=2.99, Ea=(7950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 69,
    label = "CH3CH2NH2 + CH3 <=> CH3CH2NH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 70,
    label = "CH3CH2NH2 + NH2 <=> CH2CH2NH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.18, Ea=(9620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "CH3CH2NH2 + NH2 <=> CH3CHNH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=2.99, Ea=(7950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "CH3CH2NH2 + NH2 <=> CH3CH2NH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7140, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 73,
    label = "C2H4 + NH2 <=> CH2CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(3955, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "CH2CH2NH2 + H <=> CH2CHNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "CH2CH2NH2 + O <=> CH2O + CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "CH2CH2NH2 + OH <=> CH2CHNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 77,
    label = "CH2CH2NH2 + HO2 => CH2O + OH + CH2NH2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 78,
    label = "CH2CH2NH2 + O2 <=> CH2CHNH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+16, 'cm^3/(mol*s)'),
        n = -1.63,
        Ea = (3418, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 79,
    label = "CH2CH2NH2 + HCO <=> CH3CH2NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 80,
    label = "CH2CH2NH2 + CH3 <=> CH2CHNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=-0.32, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "CH3CHNH2 <=> CH3CHNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+45, 's^-1'), n=-10.24, Ea=(47817, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "CH3CHNH2 + H <=> CH2CHNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+08, 'cm^3/(mol*s)'), n=1.7, Ea=(588, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "CH3CHNH2 + H <=> CH3 + CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+16, 'cm^3/(mol*s)'),
        n = -0.891,
        Ea = (2903, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 84,
    label = "CH3CHNH2 + H <=> C2H4 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+21, 'cm^3/(mol*s)'),
        n = -3.02,
        Ea = (2845, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 85,
    label = "CH3CHNH2 + H <=> C2H5 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 86,
    label = "CH3CHNH2 + O <=> CH3 + H2NCHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 87,
    label = "CH3CHNH2 + O <=> CH2CHNH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "CH3CHNH2 + OH <=> CH2CHNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "CH3CHNH2 + HO2 => CH3 + OH + H2NCHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "CH3CHNH2 + O2 <=> CH2CHNH2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+20, 'cm^3/(mol*s)'),
        n = -3.02,
        Ea = (2504, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 91,
    label = "CH3CHNH2 + HCO <=> CH3CH2NH2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "CH3CHNH2 + CH3 <=> CH2CHNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(-769, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 93,
    label = "CH3CH2NH <=> CH2NH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+10, 's^-1'), n=0, Ea=(23500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 94,
    label = "CH3CH2NH <=> CH3CHNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+36, 's^-1'), n=-7.92, Ea=(36342, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 95,
    label = "CH3CH2NH + H <=> CH3 + CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12, 'cm^3/(mol*s)'),
        n = 0.701,
        Ea = (346, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "CH3CH2NH + H <=> CH3CHNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "CH3CH2NH + O <=> CH3CHNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "CH3CH2NH + OH <=> CH3CHNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "CH3CH2NH + CH3 <=> CH3CHNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 100,
    label = "CH2CHNH2 + H <=> CHCHNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.63, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "CH2CHNH2 + H <=> CH2CNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.63, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "CH2CHNH2 + H <=> CH2CHNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(9700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "CH2CHNH2 + O <=> CH3 + H2NCO",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(1494, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6855, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 105,
    label = "CH2CHNH2 + O <=> CH2CHNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6348, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "CH2CHNH2 + OH <=> CHCHNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "CH2CHNH2 + OH <=> CH2CNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "CH2CHNH2 + OH <=> CH2CHNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(447, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "CH2CHNH2 + CH3 <=> CHCHNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=1.56, Ea=(16630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "CH2CHNH2 + CH3 <=> CH2CNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+07, 'cm^3/(mol*s)'), n=1.56, Ea=(16630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "CH2CHNH2 + CH3 <=> CH2CHNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 112,
    label = "CH2CHNH2 + NH2 <=> CHCHNH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10274, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "CH2CHNH2 + NH2 <=> CH2CNH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(10274, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "CH2CHNH2 + NH2 <=> CH2CHNH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 115,
    label = "CH3CHNH <=> CH2CHNH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+18, 's^-1'), n=-2.4965, Ea=(67995, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "CH2CHNH + H <=> CH3CHNH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (-125, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 117,
    label = "CH3 + HCNH <=> CH3CHNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "CH3CHNH + H <=> CH2CHNH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "CH3CHNH + H <=> CH3CNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 120,
    label = "CH3CHNH + H <=> CH2CHNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0.4, Ea=(5359, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "CH3CHNH + H <=> CH3CHN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(7322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "CH3CHNH + O <=> CH3CNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 123,
    label = "CH3CHNH + O <=> CH2CHNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+13, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (3556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 124,
    label = "CH3CHNH + O <=> CH3CHN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH3CHNH + OH <=> CH3CNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+11, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 126,
    label = "CH3CHNH + OH <=> CH2CHNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=-0.6, Ea=(800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH3CHNH + OH <=> CH3CHN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH3CHNH + CH3 <=> CH3CNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "CH3CHNH + CH3 <=> CH2CHNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25, 'cm^3/(mol*s)'), n=3.15, Ea=(5727, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH3CHNH + CH3 <=> CH3CHN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(7123, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "CH3CHNH + NH2 <=> CH3CHN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(4441, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "NH2 + C2H2 <=> CHCHNH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e-18, 'cm^3/(mol*s)'),
        n = 8.31,
        Ea = (7430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 133,
    label = "CHCHNH2 + H <=> CHCNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "CHCHNH2 + OH <=> CHCNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "CHCHNH2 + O2 <=> OCHCHO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 136,
    label = "CHCHNH2 + CH3 <=> CHCNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "CH2CNH2 + H <=> CHCNH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 138,
    label = "CH2CNH2 + O <=> CH2CO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 139,
    label = "CH2CNH2 + OH <=> CHCNH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "CH2CNH2 + O2 <=> OCHCHO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 141,
    label = "CH2CNH2 + CH3 <=> CHCNH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "CH2CHNH + H <=> CH3 + HCNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "CH2CHNH + H <=> CH3CNH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "CH2CHNH + H <=> CH2CNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "CH2CHNH + O <=> CH2CNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "CH2CHNH + OH <=> CH2CNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "CH2CHNH + OH <=> CH2OH + HCNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "CH2CHNH + O2 <=> CH2O + CO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+17, 'cm^3/(mol*s)'),
        n = -1.757,
        Ea = (11067, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 149,
    label = "CH3CNH <=> CH3 + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+18, 's^-1'), n=-2.52, Ea=(33000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "CH3CNH <=> CH3CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.7e+25, 's^-1'), n=-5.2, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "CH3CNH + H <=> CH3 + HCNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "CH3CNH + H <=> CH2CNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "CH3CNH + H <=> CH3CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "CH3CNH + O <=> CH3 + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "CH3CNH + O <=> CH2CNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "CH3CNH + O <=> CH3CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "CH3CNH + OH <=> CH2CNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "CH3CNH + OH <=> CH3CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "CH3CNH + O2 <=> CH2O + CO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "CH3CNH + CH3 <=> CH2CNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "CH3CNH + CH3 <=> CH3CN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 162,
    label = "CH3 + HCN <=> CH3CHN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "CH3CHN + H <=> CH3CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 164,
    label = "CH3CHN + H <=> CH2CHN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(15100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "CH2CHN(S) + H2 <=> CH3CHN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "CH3CHN + O <=> CH3CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 167,
    label = "CH3CHN + OH <=> CH3CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 168,
    label = "CH3CHN + OH <=> CH2CHN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=3, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 169,
    label = "CH3CHN + OH <=> CH2CHN(S) + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+13, 'cm^3/(mol*s)'),
        n = -0.3485,
        Ea = (-727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 170,
    label = "CH3CHN + NH2 <=> CH3CN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 171,
    label = "CHCNH2 + H <=> CHCNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(9706, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "CHCNH2 + O <=> CHCNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6348, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "CHCNH2 + O <=> HCCO + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+07, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "CHCNH2 + OH <=> CHCNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "CHCNH2 + CH3 <=> CHCNH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 176,
    label = "CHCNH2 + NH2 <=> CHCNH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 177,
    label = "CH2CNH <=> CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 's^-1'), n=0, Ea=(70300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "CH2CNH + H <=> CH3CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "CH2CNH + H <=> CH3 + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+10, 'cm^3/(mol*s)'),
        n = 0.851,
        Ea = (2840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 180,
    label = "CH2CNH + H <=> CHCNH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+07, 'cm^3/(mol*s)'), n=2, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 181,
    label = "CH2CNH + H <=> CH2CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(7322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 182,
    label = "CH2CNH + O <=> CH2 + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 183,
    label = "CH2CNH + O <=> CHCNH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "CH2CNH + O <=> CH2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(4630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "CH2CNH + OH <=> CH2OH + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1013, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "CH2CNH + OH <=> CH3 + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1013, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "CH2CNH + OH <=> CHCNH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "CH2CNH + OH <=> CH2CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 189,
    label = "CH2CNH + CH3 <=> CH2CN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(820000, 'cm^3/(mol*s)'), n=1.87, Ea=(7123, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "CH2CNH + NH2 <=> CH2CN + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.94, Ea=(4441, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "CH2CHN + H <=> CH3 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 192,
    label = "CH2CHN + O <=> CH2O + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "CH2CHN + O2 <=> CH2O + HNCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "CH2CHN(S) + H <=> CH2CHN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 195,
    label = "CH2CHN(S) + H <=> CH3 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 196,
    label = "CH2CHN(S) <=> c-C2H3N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 197,
    label = "CH2CHN(S) <=> CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "CH2CHN(S) + O => HCO + HCN + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "CH2CHN(S) + OH => CH2O + HCN + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "c-C2H3N <=> CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.7e+13, 's^-1'), n=0, Ea=(41500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "c-C2H3N + H <=> CH2NCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+09, 'cm^3/(mol*s)'),
        n = 1.212,
        Ea = (1969, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 202,
    label = "c-C2H3N + H <=> CH2CHNH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+10, 'cm^3/(mol*s)'),
        n = 1.229,
        Ea = (2422, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 203,
    label = "c-C2H3N + O => H2CN + HCO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "c-C2H3N + O => C2H3 + NO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "c-C2H3N + OH => H2CN + CH2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "CH3CN <=> CH2CN + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.9e+14, 's^-1'), n=0, Ea=(94940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "CH3CN + H <=> HCN + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+10, 'cm^3/(mol*s)'), n=0.8, Ea=(6800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "CH3CN + H <=> HNC + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+15, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (20030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 209,
    label = "CH3CN + H <=> CH2CN + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60000, 'cm^3/(mol*s)'), n=3.01, Ea=(8522, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "CH3CN + O <=> CH3 + NCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+09, 'cm^3/(mol*s)'), n=1.8, Ea=(8130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 211,
    label = "CH3CN + O <=> CH2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+08, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (14360, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 212,
    label = "CH3CN + OH <=> CH2CN + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 213,
    label = "CH3CN + CH3 <=> CH2CN + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 214,
    label = "CH3CN + CN <=> CH2CN + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 215,
    label = "CH2CN + O <=> CH2O + CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0.64, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
    label = "CH2OH + CN <=> CH2CN + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 217,
    label = "CHCNH + H <=> CH2 + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 218,
    label = "CHCNH + O <=> H + CO + HNC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 219,
    label = "CHCNH + OH <=> HCO + HCNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 220,
    label = "CHCNH + O2 <=> HNCO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+12, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 221,
    label = "CHCNH + O2 <=> HNC + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+11, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 222,
    label = "CHCNH + O2 <=> HNC + HCO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=2.69, Ea=(3540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 223,
    label = "H2NCHO <=> HCO + NH2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.4e+16, 'cm^3/(mol*s)'), n=0, Ea=(72900, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 224,
    label = "H2NCHO <=> H2NCO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.6e+15, 'cm^3/(mol*s)'), n=0, Ea=(64200, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 225,
    label = "H2NCHO + H <=> H2NCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(6955, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "H2NCHO + H <=> HCO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "H2NCHO + O <=> H2NCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5196, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "H2NCHO + OH <=> H2NCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 229,
    label = "H2NCHO + CH3 <=> H2NCO + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(700000, 'cm^3/(mol*s)'), n=2, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "H2NCHO + NH2 <=> H2NCO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "H2NCO + H <=> HNCO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "H2NCO + O <=> HNCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "H2NCO + OH <=> HNCO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 234,
    label = "CH3NCH3 + H <=> CH3NHCH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 235,
    label = "CH3NHCH3 + H <=> CH3NHCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5464, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 236,
    label = "CH3NHCH3 + H <=> CH3NCH3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(9706, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "CH3NHCH3 + O <=> CH3NHCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(556, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "CH3NHCH3 + O <=> CH3NCH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(556, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "CH3NHCH3 + OH <=> CH3NHCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 240,
    label = "CH3NHCH3 + OH <=> CH3NCH3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 241,
    label = "CH3NHCH3 + CH3 <=> CH3NHCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9170, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 242,
    label = "CH3NHCH3 + CH3 <=> CH3NCH3 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 243,
    label = "CH3NHCH3 + NH2 <=> CH3NHCH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5494, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 244,
    label = "CH3NHCH3 + NH2 <=> CH3NCH3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 245,
    label = "CH3NHCH2 <=> CH3 + CH2NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.8e+43, 's^-1'), n=-10.302, Ea=(37459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "CH3NHCH2 <=> CH3NCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.9e+44, 's^-1'), n=-10.314, Ea=(46803, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 247,
    label = "CH3NHCH2 + H <=> CH3NCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 248,
    label = "CH3NHCH2 + O <=> CH2O + CH3NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 249,
    label = "CH3NHCH2 + O <=> CH3NCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(-894, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "CH3NHCH2 + OH <=> CH2OH + CH3NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 251,
    label = "CH3NHCH2 + OH <=> CH3NCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(-1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 252,
    label = "CH3NHCH2 + CH3 <=> C2H5 + CH3NH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2702, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "CH3NHCH2 + CH3 <=> CH3NCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-626, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 254,
    label = "CH3NCH3 <=> CH3NCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+15, 's^-1'), n=-7.544, Ea=(38425, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "CH3NCH3 + H <=> CH3NCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 256,
    label = "CH3NCH3 + O <=> CH3NO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "CH3NCH3 + OH <=> CH3NCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "CH3NCH3 + O2 <=> CH3NO + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 'cm^3/(mol*s)'), n=1, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "CH3NCH3 + CH3 <=> CH3NCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 260,
    label = "CH2NCH2 + H <=> CH3NCH2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (-125, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 261,
    label = "CH3NCH2 + H <=> CH2NCH2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5464, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 262,
    label = "CH3NCH2 + H <=> CH3NCH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 263,
    label = "CH3NCH2 + O <=> CH2NCH2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5196, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 264,
    label = "CH3NCH2 + O <=> CH3NCH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+08, 'cm^3/(mol*s)'), n=1.5, Ea=(5404, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 265,
    label = "CH3NCH2 + OH <=> CH2NCH2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 266,
    label = "CH3NCH2 + OH <=> CH3NCH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+06, 'cm^3/(mol*s)'), n=2, Ea=(457, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 267,
    label = "CH3NCH2 + CH3 <=> CH2NCH2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9170, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 268,
    label = "CH3NCH2 + CH3 <=> CH3NCH + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(530000, 'cm^3/(mol*s)'), n=1.87, Ea=(9687, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "CH3NCH2 + NH2 <=> CH2NCH2 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5494, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 270,
    label = "CH3NCH2 + NH2 <=> CH3NCH + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6090, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 271,
    label = "CH2NCH2 <=> CH3NCH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+45, 's^-1'), n=-10.068, Ea=(66111, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "CH2NCH2 + H <=> CH3 + H2CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 273,
    label = "CH2NCH2 + O <=> CH2O + H2CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 274,
    label = "CH2NCH2 + OH <=> CH2OH + H2CN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 275,
    label = "CH3NCH <=> CH3 + HCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.1e+15, 's^-1'), n=-2.375, Ea=(14942, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 276,
    label = "CH3NCH + H <=> CH2NCH2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 277,
    label = "CH3NCH + O => CH3 + NCO + H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 278,
    label = "CH3 + NH2 <=> CH3NH2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0.42, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -3.85,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 279,
    label = "C2H5 + NH2 <=> CH3CH2NH2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(7.2e+12, 'cm^3/(mol*s)'), n=0.42, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -3.85,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 280,
    label = "CH2CHNH2 + H <=> CH3CHNH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.4e+09, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 281,
    label = "CHCHNH2 + H <=> CH2CHNH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.9e+13, 'cm^3/(mol*s)'), n=0.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.1e+24, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 282,
    label = "CH2CNH2 + H <=> CH2CHNH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.9e+13, 'cm^3/(mol*s)'), n=0.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.1e+24, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 283,
    label = "CHCNH2 + H <=> CHCHNH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.7e+10, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.3e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7878,
        T3 = (-10212, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 284,
    label = "CHCNH2 + H <=> CH2CNH2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.7e+10, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.3e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7878,
        T3 = (-10212, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 285,
    label = "CH2CHN(S) <=> CH2CHN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H]': 0},
    ),
)

entry(
    index = 286,
    label = "H2NCHO <=> CO + NH3",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(75514, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(8.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(49084, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 287,
    label = "H2NCO <=> CO + NH2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(5.9e+12, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(21700, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 288,
    label = "CH3NHCH2 + H <=> CH3NHCH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.2e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {},
    ),
)

