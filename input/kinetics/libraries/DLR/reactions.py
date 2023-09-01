#!/usr/bin/env python
# encoding: utf-8

name = "DLR"
shortDesc = ""
longDesc = """

"""

entry(
    index = 0,
    label = "C + OH <=> CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "O2 + C <=> CO + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(16711.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "CO + HO2 <=> CO2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(320000,'cm^3/(mol*s)'), n=2.18, Ea=(75079.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "CO + O <=> CO2",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(6.17e+14,'cm^6/(mol^2*s)'), n=0, Ea=(12550.7,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 16.25, 'O=C=O': 3.75, '[Ar]': 0.87, '[C-]#[O+]': 1.87, '[H][H]': 2.5, '[He]': 0.87}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "CO + OH <=> CO2 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(1.01e+11,'cm^3/(mol*s)'), n=0, Ea=(249.434,'J/mol'), T0=(1,'K')), Arrhenius(A=(9.03e+11,'cm^3/(mol*s)'), n=0, Ea=(19123.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.01e+13,'cm^3/(mol*s)'), n=0, Ea=(66931.5,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "O2 + CO <=> CO2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+13,'cm^3/(mol*s)'), n=0, Ea=(196911,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "CH + OH <=> HCO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "CH + CO2 <=> HCO + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.383e+07,'cm^3/(mol*s)'), n=1.51, Ea=(-2993.21,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "HCO <=> CO + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(5.7e+11,'cm^3/(mol*s)'), n=0.66, Ea=(62128.7,'J/mol'), T0=(1,'K')), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "HCO + HO2 <=> CO2 + OH + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "HCO + OH <=> CO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.011e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "HCO + O <=> CO2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "HCO + O <=> CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 13,
    label = "HCO + H <=> CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 14,
    label = "HCO + O2 <=> HO2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.7e+10,'cm^3/(mol*s)'), n=0.68, Ea=(-1962.22,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 15,
    label = "CH + CO <=> HCCO",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.024e+15,'cm^3/(mol*s)'), n=-0.4, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.285e+24,'cm^6/(mol^2*s)'), n=-2.5, Ea=(0,'J/mol'), T0=(1,'K')), alpha=0.6, T3=(1e-31,'K'), T1=(1e+31,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 16,
    label = "HCCO + OH => H2 + CO + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 17,
    label = "HCCO + O <=> CO + CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.64e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 18,
    label = "HCCO + H <=> CH2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.06e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 19,
    label = "HCCO + O2 => OH + CO + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.91e+11,'cm^3/(mol*s)'), n=-0.02, Ea=(4261.69,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 20,
    label = "HCCO + O2 => CO2 + CO + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.78e+12,'cm^3/(mol*s)'), n=-0.142, Ea=(4804.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 21,
    label = "CH2O <=> HCO + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(4.872e+15,'cm^3/(mol*s)'), n=0, Ea=(316366,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.2, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 22,
    label = "CH2O <=> H2 + CO",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.83e+15,'cm^3/(mol*s)'), n=0, Ea=(266895,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.2, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 23,
    label = "CH2O + H <=> HCO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.74e+07,'cm^3/(mol*s)'), n=1.9, Ea=(11448,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 24,
    label = "CH2O + O <=> HCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.16e+11,'cm^3/(mol*s)'), n=0.57, Ea=(11560.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 25,
    label = "CH2O + OH <=> HCO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.391e+13,'cm^3/(mol*s)'), n=0, Ea=(2527.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 26,
    label = "CH2O + HO2 <=> HCO + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(40950,'cm^3/(mol*s)'), n=2.5, Ea=(42736.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 27,
    label = "CH2O + O2 <=> HCO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.07e+15,'cm^3/(mol*s)'), n=0, Ea=(223195,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 28,
    label = "CH2OH <=> CH2O + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.8e+14,'s^-1'), n=-0.73, Ea=(137314,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.022e+33,'cm^3/(mol*s)'), n=-5.39, Ea=(151465,'J/mol'), T0=(1,'K')), alpha=0.96, T3=(67.6,'K'), T1=(1855,'K'), T2=(7543,'K'), efficiencies={'C': 1.0, 'N#N': 0.4, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.35, '[C-]#[O+]': 0.75, '[H][H]': 1.0, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 29,
    label = "CH2OH + H <=> CH2O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.445e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 30,
    label = "CH2OH + H <=> CH3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.635e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 31,
    label = "CH2OH + O <=> CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.221e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 32,
    label = "CH2OH + OH <=> CH2O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.409e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 33,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.807e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 34,
    label = "CH2OH + CH3 <=> CH2O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.409e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 35,
    label = "CH2OH + O2 <=> CH2O + HO2",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(1.51e+15,'cm^3/(mol*s)'), n=-1, Ea=(0,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.41e+14,'cm^3/(mol*s)'), n=0, Ea=(20961.7,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 36,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 37,
    label = "CH2CO <=> CH2 + CO",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.3e+15,'cm^3/(mol*s)'), n=0, Ea=(240545,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.2, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 38,
    label = "CH2CO + H <=> CH3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.252e+10,'cm^3/(mol*s)'), n=0.85, Ea=(11889.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 39,
    label = "CH2CO + H <=> HCCO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.401e+15,'cm^3/(mol*s)'), n=-0.171, Ea=(36697.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 40,
    label = "CH2CO + OH <=> CH3 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.553e+11,'cm^3/(mol*s)'), n=0, Ea=(-4240.38,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 41,
    label = "CH2CO + OH <=> CH2OH + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.012e+12,'cm^3/(mol*s)'), n=0, Ea=(-4240.38,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 42,
    label = "CH2CO + OH <=> HCCO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.686e+10,'cm^3/(mol*s)'), n=0, Ea=(-4240.38,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 43,
    label = "CH2CO + O <=> CH2O + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.613e+11,'cm^3/(mol*s)'), n=0, Ea=(5653.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 44,
    label = "CH2CO + O <=> HCO + H + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.807e+11,'cm^3/(mol*s)'), n=0, Ea=(5653.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 45,
    label = "CH2CO + O <=> HCO + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.807e+11,'cm^3/(mol*s)'), n=0, Ea=(5653.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 46,
    label = "CH2CO + O <=> CH2 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.084e+12,'cm^3/(mol*s)'), n=0, Ea=(5653.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 47,
    label = "CH2O + H <=> CH3O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.08e+11,'cm^3/(mol*s)'), n=0.5, Ea=(10808.8,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.2e+30,'cm^6/(mol^2*s)'), n=-4.8, Ea=(23114.2,'J/mol'), T0=(1,'K')), alpha=0.758, T3=(94,'K'), T1=(1555,'K'), T2=(4200,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 48,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.794e+13,'cm^3/(mol*s)'), n=0, Ea=(2494.34,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 49,
    label = "CH3 + OH => CH3O + H",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(6.943e+07,'cm^3/(mol*s)'), n=1.343, Ea=(46795,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 50,
    label = "CH3O + H => CH3 + OH",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+12,'cm^3/(mol*s)'), n=0.5, Ea=(-459.594,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 51,
    label = "CH3O + O <=> CH3 + O2",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(1.129e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 52,
    label = "CH3 + O2 <=> CH3O + O",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(2.108e+13,'cm^3/(mol*s)'), n=0, Ea=(135858,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 53,
    label = "CH3O + O <=> CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.764e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 54,
    label = "CH3 + HO2 <=> CH3O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0.269, Ea=(-2872.46,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 55,
    label = "CH3O + O2 <=> CH2O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.17e+10,'cm^3/(mol*s)'), n=0, Ea=(7316.74,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 56,
    label = "CH3OH <=> CH3 + OH",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.084e+18,'s^-1'), n=-0.615, Ea=(386646,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.5e+43,'cm^3/(mol*s)'), n=-6.995, Ea=(409424,'J/mol'), T0=(1,'K')), alpha=-0.4748, T3=(35580,'K'), T1=(1116,'K'), T2=(9023,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 57,
    label = "CH2OH + H <=> CH3OH",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.06e+12,'cm^3/(mol*s)'), n=0.5, Ea=(359.185,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4.36e+31,'cm^6/(mol^2*s)'), n=-4.65, Ea=(21225.2,'J/mol'), T0=(1,'K')), alpha=0.6, T3=(100,'K'), T1=(90000,'K'), T2=(10000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 58,
    label = "CH3O + H <=> CH3OH",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.43e+12,'cm^3/(mol*s)'), n=0.5, Ea=(208.693,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4.66e+41,'cm^6/(mol^2*s)'), n=-7.44, Ea=(58828,'J/mol'), T0=(1,'K')), alpha=0.7, T3=(100,'K'), T1=(90000,'K'), T2=(10000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 59,
    label = "CH3OH <=> CH2(S) + H2O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.121e+18,'s^-1'), n=-1.017, Ea=(383184,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.43e+47,'cm^3/(mol*s)'), n=-8.227, Ea=(415377,'J/mol'), T0=(1,'K')), alpha=2.545, T3=(3290,'K'), T1=(47320,'K'), T2=(47110,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 60,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+13,'cm^3/(mol*s)'), n=0, Ea=(81055.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 61,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.05e+13,'cm^3/(mol*s)'), n=0, Ea=(187598,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 62,
    label = "CH3OH + H <=> CH2OH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.089e+09,'cm^3/(mol*s)'), n=1.24, Ea=(18790.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 63,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.433e+08,'cm^3/(mol*s)'), n=1.24, Ea=(18790.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 64,
    label = "CH3OH + O <=> CH2OH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.222e+13,'cm^3/(mol*s)'), n=0, Ea=(22199.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 65,
    label = "CH3OH + O <=> CH3O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.469e+12,'cm^3/(mol*s)'), n=0, Ea=(22199.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 66,
    label = "CH3OH + OH <=> CH2OH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.272e+06,'cm^3/(mol*s)'), n=1.92, Ea=(-1197.28,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 67,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(930400,'cm^3/(mol*s)'), n=1.92, Ea=(-1197.28,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 68,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.936,'cm^3/(mol*s)'), n=3.45, Ea=(33424.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 69,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20.17,'cm^3/(mol*s)'), n=3.45, Ea=(33424.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 70,
    label = "CH2HCO <=> CH2CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.81e+43,'s^-1'), n=-9.61, Ea=(191642,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 71,
    label = "CH2HCO + H <=> CH3 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 72,
    label = "CH2HCO + H <=> CH3CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 73,
    label = "CH2HCO + H <=> CH2CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(16712.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 74,
    label = "CH2HCO + O <=> CH2CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(16712.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 75,
    label = "CH2HCO + OH <=> CH2CO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(8356.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 76,
    label = "CH2HCO + O2 <=> CH2CO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 77,
    label = "CH3CHO <=> CH3 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+15,'s^-1'), n=0, Ea=(341244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 78,
    label = "CH3CHO + H <=> CH3CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.1e+09,'cm^3/(mol*s)'), n=1.16, Ea=(10060.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 79,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.891e+08,'cm^3/(mol*s)'), n=1.35, Ea=(-6585.06,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 80,
    label = "CH3CHO + O <=> CH3CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.8e+12,'cm^3/(mol*s)'), n=0, Ea=(7566.17,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 81,
    label = "CH3CHO + HO2 <=> CH3CO + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(40950,'cm^3/(mol*s)'), n=2.5, Ea=(42694.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 82,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.9e-07,'cm^3/(mol*s)'), n=5.8, Ea=(9191.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 83,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(120400,'cm^3/(mol*s)'), n=2.5, Ea=(157144,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 84,
    label = "CH3CHO + H <=> CH2HCO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.85e+12,'cm^3/(mol*s)'), n=0.4, Ea=(22428.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 85,
    label = "CH3CHO + OH <=> CH2HCO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+11,'cm^3/(mol*s)'), n=0, Ea=(-2594.12,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 86,
    label = "CH3CHO + O <=> CH2HCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.72e+13,'cm^3/(mol*s)'), n=-0.2, Ea=(14897,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 87,
    label = "CH3CHO + HO2 <=> CH2HCO + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.32e+11,'cm^3/(mol*s)'), n=0.4, Ea=(62347.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 88,
    label = "CH3CHO + CH3 <=> CH2HCO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(24.5,'cm^3/(mol*s)'), n=3.1, Ea=(23976.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 89,
    label = "CH3CO <=> CH3 + CO",
    degeneracy = 1.0,
    kinetics = Lindemann(arrheniusHigh=Arrhenius(A=(3e+12,'s^-1'), n=0, Ea=(71753.9,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4.215e+06,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 90,
    label = "H + CH <=> C + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 91,
    label = "CH + O <=> CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.97e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 92,
    label = "O2 + CH <=> CO2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.469e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 93,
    label = "O2 + CH <=> CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.431e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 94,
    label = "CH2 + O <=> CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.19e+13,'cm^3/(mol*s)'), n=0, Ea=(2244.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 95,
    label = "CH2 + O <=> CO + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.23e+14,'cm^3/(mol*s)'), n=0, Ea=(2244.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 96,
    label = "CH2 + H <=> CH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.204e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 97,
    label = "CH2 + O2 <=> CO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.72e+22,'cm^3/(mol*s)'), n=-3.3, Ea=(11947.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 98,
    label = "CH2 + O2 <=> CO2 + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.613e+21,'cm^3/(mol*s)'), n=-3.3, Ea=(11947.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 99,
    label = "CH2 + O2 <=> CO2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.613e+21,'cm^3/(mol*s)'), n=-3.3, Ea=(11947.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 100,
    label = "CH2(S) + AR <=> CH2 + AR",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.807e+10,'cm^3/(mol*s)'), n=0.93, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 101,
    label = "CH2(S) + N2 <=> CH2 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.204e+13,'cm^3/(mol*s)'), n=0, Ea=(1970.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 102,
    label = "CH2(S) + O2 <=> CH2 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.131e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 103,
    label = "CH2(S) + H2 <=> CH2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.022e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 104,
    label = "CH3 <=> CH2 + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.024e+16,'cm^3/(mol*s)'), n=0, Ea=(379140,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.4, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 105,
    label = "CH3 <=> CH + H2",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(6.624e+16,'cm^3/(mol*s)'), n=0, Ea=(355859,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.4, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 106,
    label = "CH3 + OH <=> CH2(S) + H2O",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(4.936e+14,'cm^3/(mol*s)'), n=-0.669, Ea=(-1862.61,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.207e+15,'cm^3/(mol*s)'), n=-0.778, Ea=(-733.669,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.282e+17,'cm^3/(mol*s)'), n=-1.518, Ea=(7403.62,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.788e+23,'cm^3/(mol*s)'), n=-3.155, Ea=(29259.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.433e+19,'cm^3/(mol*s)'), n=-1.962, Ea=(34444.4,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 107,
    label = "CH2(S) + H2 <=> CH3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 108,
    label = "CH3 + O <=> CH2O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.745e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 109,
    label = "CH3 + O <=> CO + H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.686e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 110,
    label = "CH3 + O2 <=> CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.641,'cm^3/(mol*s)'), n=3.28, Ea=(33863.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 111,
    label = "CH3 + H <=> CH4",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.27e+16,'cm^3/(mol*s)'), n=-0.63, Ea=(1600.2,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.477e+33,'cm^6/(mol^2*s)'), n=-4.76, Ea=(10194.6,'J/mol'), T0=(1,'K')), alpha=0.783, T3=(74,'K'), T1=(2941,'K'), T2=(6964,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0, '[He]': 0.7}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 112,
    label = "CH4 + O <=> CH3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.02e+09,'cm^3/(mol*s)'), n=1.5, Ea=(35931.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 113,
    label = "CH4 + O2 <=> CH3 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(487800,'cm^3/(mol*s)'), n=2.5, Ea=(219253,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 114,
    label = "CH4 + H <=> CH3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(614300,'cm^3/(mol*s)'), n=2.5, Ea=(40055.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 115,
    label = "CH4 + OH <=> CH3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.367e+06,'cm^3/(mol*s)'), n=2.18, Ea=(11224.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 116,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(46970,'cm^3/(mol*s)'), n=2.5, Ea=(87884,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 117,
    label = "CH4 + CH2(S) <=> CH3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.401e+12,'cm^3/(mol*s)'), n=0, Ea=(-2078.62,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 118,
    label = "CH4 + CH2(S) <=> C2H5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.401e+12,'cm^3/(mol*s)'), n=0, Ea=(-2078.62,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 119,
    label = "CH3 + CH2O <=> CH4 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(38.3,'cm^3/(mol*s)'), n=3.36, Ea=(18042.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 120,
    label = "CH3 + HCO <=> CH4 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.48e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 121,
    label = "CH3 + O2 <=> CH3O2",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(7.812e+09,'cm^3/(mol*s)'), n=0.9, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.85e+24,'cm^6/(mol^2*s)'), n=-3, Ea=(0,'J/mol'), T0=(1,'K')), alpha=0.6, T3=(1000,'K'), T1=(70,'K'), T2=(1700,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 122,
    label = "CH3O2 + CH3 => CH3O + CH3O",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(5.08e+12,'cm^3/(mol*s)'), n=0, Ea=(-5895.33,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 123,
    label = "CH3O + CH3O => CH3O2 + CH3",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.967e+12,'cm^3/(mol*s)'), n=0.176, Ea=(117280,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 124,
    label = "CH3O2 + H => CH3O + OH",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(9.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 125,
    label = "CH3O + OH => CH3O2 + H",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.72e+09,'cm^3/(mol*s)'), n=1.019, Ea=(170384,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 126,
    label = "CH3O2 + O => CH3O + O2",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 127,
    label = "CH3O + O2 => CH3O2 + O",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(2.229e+11,'cm^3/(mol*s)'), n=0.628, Ea=(240326,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 128,
    label = "CH3O2 + OH => CH3OH + O2",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 129,
    label = "CH3OH + O2 => CH3O2 + OH",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.536e+13,'cm^3/(mol*s)'), n=0.434, Ea=(247178,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 130,
    label = "CH3O2 + CH3O2 => O2 + CH3O + CH3O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.4e+16,'cm^3/(mol*s)'), n=-1.61, Ea=(7771.31,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 131,
    label = "CH3O2H => CH3O + OH",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(6.31e+14,'s^-1'), n=0, Ea=(176735,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 132,
    label = "CH3O + OH => CH3O2H",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(2.514e+06,'cm^3/(mol*s)'), n=1.883, Ea=(-12012.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 133,
    label = "CH3O2 + CH2O => CH3O2H + HCO",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.99e+12,'cm^3/(mol*s)'), n=0, Ea=(48717,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 134,
    label = "CH3O2H + HCO => CH3O2 + CH2O",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.323e+14,'cm^3/(mol*s)'), n=-0.853, Ea=(38685.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 135,
    label = "CH4 + CH3O2 => CH3 + CH3O2H",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.81e+11,'cm^3/(mol*s)'), n=0, Ea=(77211.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 136,
    label = "CH3 + CH3O2H => CH4 + CH3O2",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(2.233e+12,'cm^3/(mol*s)'), n=-0.694, Ea=(-2736.68,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 137,
    label = "CH3OH + CH3O2 => CH2OH + CH3O2H",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1.81e+12,'cm^3/(mol*s)'), n=0, Ea=(57282.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 138,
    label = "CH2OH + CH3O2H => CH3OH + CH3O2",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(2.346e+14,'cm^3/(mol*s)'), n=-1.031, Ea=(10044.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 139,
    label = "CH3O2 + HO2 => CH3O2H + O2",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(2.47e+11,'cm^3/(mol*s)'), n=0, Ea=(-6559.66,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 140,
    label = "CH3O2H + O2 => CH3O2 + HO2",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(5.302e+14,'cm^3/(mol*s)'), n=-0.792, Ea=(148407,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 141,
    label = "CH3O2 + CH3O2 => CH2O + CH3OH + O2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3.11e+14,'cm^3/(mol*s)'), n=-1.61, Ea=(-4391.21,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 142,
    label = "C2H + H <=> C2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.607e+13,'cm^3/(mol*s)'), n=0, Ea=(118007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 143,
    label = "C2H + OH <=> CH2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.807e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 144,
    label = "C2H + O <=> CH + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.962e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 145,
    label = "C2H + O2 <=> CO + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.36e+13,'cm^3/(mol*s)'), n=-0.35, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 146,
    label = "C2H + O2 <=> CO + CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.083e+14,'cm^3/(mol*s)'), n=-0.35, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 147,
    label = "C2H2 <=> C2H + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(3.999e+16,'cm^3/(mol*s)'), n=0, Ea=(446156,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.35, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 148,
    label = "C2H2 + H <=> C2H + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.006e+10,'cm^3/(mol*s)'), n=1.64, Ea=(126796,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 149,
    label = "C2H2 + O <=> HCCO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.394e+08,'cm^3/(mol*s)'), n=1.4, Ea=(9229.06,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 150,
    label = "C2H2 + O <=> CH2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.349e+08,'cm^3/(mol*s)'), n=1.4, Ea=(9229.06,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 151,
    label = "C2H2 + OH <=> CH2CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000218,'cm^3/(mol*s)'), n=4.5, Ea=(-4178.13,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 152,
    label = "C2H2 + OH <=> C2H + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+07,'cm^3/(mol*s)'), n=2, Ea=(58493.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 153,
    label = "C2H2 + OH <=> CH3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000483,'cm^3/(mol*s)'), n=4, Ea=(-8356.29,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 154,
    label = "C2H2 + O2 <=> C2H + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(312018,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 155,
    label = "C2H2 + HO2 => CH2 + CO + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6.09e+09,'cm^3/(mol*s)'), n=0, Ea=(33262,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 156,
    label = "C2H2 + CH2OH <=> CH2O + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.2e+11,'cm^3/(mol*s)'), n=0, Ea=(37415.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 157,
    label = "C2H2 + CO <=> C2H + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.818e+14,'cm^3/(mol*s)'), n=0, Ea=(446026,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 158,
    label = "C2H2 + CH3 <=> C2H + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.813e+11,'cm^3/(mol*s)'), n=0, Ea=(72203.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 159,
    label = "C2H2 <=> H2CC",
    degeneracy = 1.0,
    kinetics = Lindemann(arrheniusHigh=Arrhenius(A=(8e+14,'s^-1'), n=-0.52, Ea=(212040,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.45e+15,'cm^3/(mol*s)'), n=-0.64, Ea=(207653,'J/mol'), T0=(1,'K')), efficiencies={'C': 2.0, 'C#C': 2.5, 'C=C': 2.5, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 160,
    label = "H2CC + H <=> C2H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 161,
    label = "H2CC + OH <=> CH2CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 162,
    label = "H2CC + O2 <=> HCO + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 163,
    label = "C2H3 <=> C2H2 + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.86e+08,'s^-1'), n=1.62, Ea=(155065,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.565e+27,'cm^3/(mol*s)'), n=-3.4, Ea=(149835,'J/mol'), T0=(1,'K')), alpha=1.9816, T3=(5383.7,'K'), T1=(4.2932,'K'), T2=(-0.0795,'K'), efficiencies={'C': 2.0, 'C#C': 3.0, 'C=C': 3.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 164,
    label = "C2H3 + H <=> C2H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.215e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 165,
    label = "C2H3 + O <=> CH3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 166,
    label = "C2H3 + O <=> C2H2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 167,
    label = "C2H3 + O <=> CH2 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 168,
    label = "C2H3 + OH <=> C2H2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 169,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.92e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 170,
    label = "C2H3 + HO2 <=> CH2HCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 171,
    label = "C2H3 + O2 <=> HCO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.6e+16,'cm^3/(mol*s)'), n=-1.39, Ea=(4219.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 172,
    label = "C2H3 + O2 <=> CH2HCO + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+11,'cm^3/(mol*s)'), n=0.29, Ea=(44.8981,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 173,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+06,'cm^3/(mol*s)'), n=1.61, Ea=(-1604.69,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 174,
    label = "C2H3 + C2H <=> C2H2 + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.635e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 175,
    label = "C2H3 + CH2 <=> C2H2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.81e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 176,
    label = "C2H4 <=> C2H2 + H2",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.047e+17,'cm^3/(mol*s)'), n=0, Ea=(327507,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.35, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 177,
    label = "C2H4 <=> C2H3 + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.589e+17,'cm^3/(mol*s)'), n=0, Ea=(404083,'J/mol'), T0=(1,'K')), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.2, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 178,
    label = "C2H4 + H <=> C2H3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(235,'cm^3/(mol*s)'), n=3.63, Ea=(47143.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 179,
    label = "CH + CH4 <=> C2H4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.325e+16,'cm^3/(mol*s)'), n=-0.94, Ea=(241.12,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 180,
    label = "CH2 + CH3 <=> C2H4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.227e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 181,
    label = "C2H4 + O <=> CH2HCO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.742e+06,'cm^3/(mol*s)'), n=1.88, Ea=(764.931,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 182,
    label = "C2H4 + O <=> HCO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.13e+06,'cm^3/(mol*s)'), n=1.88, Ea=(764.931,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 183,
    label = "C2H4 + O <=> CH2CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(677500,'cm^3/(mol*s)'), n=1.88, Ea=(764.931,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 184,
    label = "C2H4 + OH <=> C2H3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.6e+06,'cm^3/(mol*s)'), n=2, Ea=(10443,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 185,
    label = "C2H4 + CH3 <=> C2H3 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.022e+07,'cm^3/(mol*s)'), n=1.56, Ea=(69592.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 186,
    label = "C2H3 + C2H3 <=> C2H2 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.431e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 187,
    label = "C2H4 + CO <=> C2H3 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.512e+14,'cm^3/(mol*s)'), n=0, Ea=(378284,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 188,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+13,'cm^3/(mol*s)'), n=0, Ea=(239457,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 189,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.367e+09,'cm^3/(mol*s)'), n=1.463, Ea=(5662.16,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.027e+39,'cm^6/(mol^2*s)'), n=-6.642, Ea=(24103.7,'J/mol'), T0=(1,'K')), alpha=-0.569, T3=(299,'K'), T1=(-9147,'K'), T2=(152.4,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 190,
    label = "C2H5 + CH3 <=> C2H4 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.033e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 191,
    label = "C2H5 + O <=> CH3CHO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 192,
    label = "C2H5 + O <=> CH2O + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.975e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 193,
    label = "C2H5 + O <=> C2H4 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.65e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 194,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.215e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 195,
    label = "CH3 + CH3 <=> H + C2H5",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(4.74e+12,'cm^3/(mol*s)'), n=0.105, Ea=(44556.8,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.57e+13,'cm^3/(mol*s)'), n=-0.096, Ea=(47656.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.1e+14,'cm^3/(mol*s)'), n=-0.362, Ea=(55872,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.15e+10,'cm^3/(mol*s)'), n=0.885, Ea=(56540.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(103.2,'cm^3/(mol*s)'), n=3.23, Ea=(46945.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 196,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 197,
    label = "C2H5 + CH2OH <=> CH3OH + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 198,
    label = "C2H5 + HCO <=> C2H6 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.21e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 199,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.277e+15,'cm^3/(mol*s)'), n=-0.69, Ea=(730.759,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(8.054e+31,'cm^6/(mol^2*s)'), n=-3.75, Ea=(4101.28,'J/mol'), T0=(1,'K')), T3=(570,'K'), T1=(1e-30,'K'), T2=(1e+30,'K'), efficiencies={'O': 5.0, 'O=C=O': 3.0, '[C-]#[O+]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 200,
    label = "C2H6 + H <=> C2H5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.816e+13,'cm^3/(mol*s)'), n=0, Ea=(38579.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 201,
    label = "C2H6 + O <=> C2H5 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(180700,'cm^3/(mol*s)'), n=2.8, Ea=(24278.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 202,
    label = "C2H6 + OH <=> C2H5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.154e+06,'cm^3/(mol*s)'), n=2, Ea=(4157.24,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 203,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(110200,'cm^3/(mol*s)'), n=2.5, Ea=(70506.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 204,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(728700,'cm^3/(mol*s)'), n=2.5, Ea=(205700,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 205,
    label = "C2H6 + CH <=> C2H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+14,'cm^3/(mol*s)'), n=0, Ea=(-1097.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 206,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(5.601e+10,'cm^3/(mol*s)'), n=0, Ea=(39410.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.431e+14,'cm^3/(mol*s)'), n=0, Ea=(93122.1,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 207,
    label = "C2H5OH <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.79e+13,'s^-1'), n=0.09, Ea=(276739,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.57e+83,'cm^3/(mol*s)'), n=-18.85, Ea=(361763,'J/mol'), T0=(1,'K')), alpha=0.7, T3=(350,'K'), T1=(800,'K'), T2=(3800,'K'), efficiencies={'O': 6.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 208,
    label = "C2H5OH <=> CH2OH + CH3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(6e+23,'s^-1'), n=-1.68, Ea=(380803,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.88e+85,'cm^3/(mol*s)'), n=-18.9, Ea=(459957,'J/mol'), T0=(1,'K')), alpha=0.5, T3=(200,'K'), T1=(890,'K'), T2=(4600,'K'), efficiencies={'O': 5.0, 'O=C=O': 3.0, '[C-]#[O+]': 2.0, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 209,
    label = "C2H5OH <=> C2H5 + OH",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.25e+21,'s^-1'), n=-1.54, Ea=(401123,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.252e+85,'cm^3/(mol*s)'), n=-18.81, Ea=(480194,'J/mol'), T0=(1,'K')), alpha=0.5, T3=(300,'K'), T1=(900,'K'), T2=(5000,'K'), efficiencies={'O': 5.0, 'O=C=O': 3.0, '[C-]#[O+]': 2.0, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 210,
    label = "C2H5OH + O <=> CH3CHOH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88e+07,'cm^3/(mol*s)'), n=1.85, Ea=(7616.06,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 211,
    label = "C2H5OH + O <=> CH2CH2OH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.41e+07,'cm^3/(mol*s)'), n=1.7, Ea=(22847.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 212,
    label = "C2H5OH + O <=> CH3CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+07,'cm^3/(mol*s)'), n=2, Ea=(18621.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 213,
    label = "C2H5OH + H <=> CH3CH2O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+07,'cm^3/(mol*s)'), n=1.6, Ea=(12720.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 214,
    label = "C2H5OH + H <=> CH3CHOH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e+07,'cm^3/(mol*s)'), n=1.65, Ea=(11842.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 215,
    label = "C2H5OH + H <=> CH2CH2OH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.23e+07,'cm^3/(mol*s)'), n=1.8, Ea=(21340.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 216,
    label = "C2H5OH + OH <=> CH3CH2O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.46e+11,'cm^3/(mol*s)'), n=0.3, Ea=(6826.18,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 217,
    label = "C2H5OH + OH <=> CH3CHOH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.64e+11,'cm^3/(mol*s)'), n=0.15, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 218,
    label = "C2H5OH + OH <=> CH2CH2OH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.74e+11,'cm^3/(mol*s)'), n=0.27, Ea=(2506.81,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 219,
    label = "C2H5OH + HO2 <=> CH3CH2O + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+12,'cm^3/(mol*s)'), n=0, Ea=(100426,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 220,
    label = "C2H5OH + HO2 <=> CH3CHOH + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8200,'cm^3/(mol*s)'), n=2.5, Ea=(45191.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 221,
    label = "C2H5OH + HO2 <=> CH2CH2OH + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12300,'cm^3/(mol*s)'), n=2.5, Ea=(66114.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 222,
    label = "C2H5OH + CH3 <=> CH3CH2O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(145,'cm^3/(mol*s)'), n=2.99, Ea=(32010.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 223,
    label = "C2H5OH + CH3 <=> CH3CHOH + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(728,'cm^3/(mol*s)'), n=2.99, Ea=(33266.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 224,
    label = "C2H5OH + CH3 <=> CH2CH2OH + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(219,'cm^3/(mol*s)'), n=3.18, Ea=(40254.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 225,
    label = "C2H4 + OH <=> CH2CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.41e+11,'cm^3/(mol*s)'), n=0, Ea=(-9964.81,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 226,
    label = "CH3CHOH <=> CH3CHO + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(104611,'J/mol'), T0=(1,'K')), efficiencies={'C': 2.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 227,
    label = "CH3CHOH + H <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 228,
    label = "CH3CHOH + H <=> CH3 + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 229,
    label = "CH3CHOH + O <=> CH3CHO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 230,
    label = "CH3CHOH + OH <=> CH3CHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 231,
    label = "CH3CHOH + HO2 <=> CH3CHO + OH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 232,
    label = "CH3CHOH + CH3 <=> C3H6 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 233,
    label = "CH3CHOH + O2 <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(4.82e+13,'cm^3/(mol*s)'), n=0, Ea=(21005.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.43e+15,'cm^3/(mol*s)'), n=-1.2, Ea=(0,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 234,
    label = "CH3CH2O <=> CH3 + CH2O",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.35e+38,'cm^3/(mol*s)'), n=-6.96, Ea=(99441.1,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 235,
    label = "CH3CH2O <=> CH3CHO + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.16e+35,'cm^3/(mol*s)'), n=-5.89, Ea=(105598,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 236,
    label = "CH3CH2O + H <=> C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 237,
    label = "CH3CH2O + H <=> CH3 + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 238,
    label = "CH3CH2O + OH <=> CH3CHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 239,
    label = "C2H5 + HO2 <=> CH3CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 240,
    label = "CH3CH2O + CO <=> C2H5 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(468,'cm^3/(mol*s)'), n=3.16, Ea=(22512.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 241,
    label = "CH3CH2O + O2 <=> CH3CHO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+10,'cm^3/(mol*s)'), n=0, Ea=(4602.89,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 242,
    label = "C3H2 + OH <=> C2H2 + CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 243,
    label = "C3H2 + O <=> C2H + H + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 244,
    label = "C3H2 + O2 <=> C2H2 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 245,
    label = "C3H2 + O2 <=> H + CO + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(4178.13,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 246,
    label = "C3H2 + H <=> C3H3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.02e+13,'cm^3/(mol*s)'), n=0.27, Ea=(1168.37,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.8e+30,'cm^6/(mol^2*s)'), n=-3.86, Ea=(13870.5,'J/mol'), T0=(1,'K')), alpha=0.782, T3=(207.5,'K'), T1=(2663,'K'), T2=(6095,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 12.0, 'O=C=O': 3.6, '[Ar]': 0.7, '[C-]#[O+]': 1.75, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 247,
    label = "C3H3 + OH <=> HCO + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 248,
    label = "C3H3 + OH <=> C3H2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 249,
    label = "C3H3 + H <=> C3H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 250,
    label = "C3H3 + O <=> C2H2 + CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 251,
    label = "C3H3 + O <=> CH2O + C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 252,
    label = "C3H3 + O2 <=> CH2CO + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+10,'cm^3/(mol*s)'), n=0, Ea=(12000.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 253,
    label = "C3H3 + O2 <=> CH3CO + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+10,'cm^3/(mol*s)'), n=0, Ea=(11997.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 254,
    label = "C3H3 + O2 <=> C2H3 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+10,'cm^3/(mol*s)'), n=0, Ea=(11997.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 255,
    label = "C2H2 + HCCO <=> C3H3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(12471.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 256,
    label = "C2H2 + CH2 <=> C3H3 + H",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(27520.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified

Originally from reaction library: Unclassified
""",
)

entry(
    index = 257,
    label = "C3H3 + H <=> C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.75e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 258,
    label = "C2H2 + CH2 <=> C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(27691.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 259,
    label = "C3H4 + H <=> C3H3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+06,'cm^3/(mol*s)'), n=2, Ea=(22979.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 260,
    label = "C3H4 + H <=> C2H2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(16708.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 261,
    label = "C2H3 + CH2 <=> C3H4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 262,
    label = "C2H4 + CH <=> C3H4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.32e+14,'cm^3/(mol*s)'), n=0, Ea=(-1440.07,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 263,
    label = "C3H4 + O <=> C2H4 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8e+12,'cm^3/(mol*s)'), n=0, Ea=(6651.58,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 264,
    label = "C3H4 + O <=> HCCO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.3e+12,'cm^3/(mol*s)'), n=0, Ea=(8314.47,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 265,
    label = "C3H4 + O <=> C3H3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+10,'cm^3/(mol*s)'), n=0.7, Ea=(31595,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 266,
    label = "C3H4 + OH <=> C3H3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+06,'cm^3/(mol*s)'), n=2, Ea=(1247.17,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 267,
    label = "C3H4 + OH <=> CH2CO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.3e+11,'cm^3/(mol*s)'), n=0, Ea=(-3325.79,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 268,
    label = "C3H4 + OH <=> CH2O + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.3e+11,'cm^3/(mol*s)'), n=0, Ea=(-3325.79,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 269,
    label = "C3H4 + HO2 <=> C3H3 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9600,'cm^3/(mol*s)'), n=2.6, Ea=(56538.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 270,
    label = "C3H4 + O2 <=> C3H3 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(256950,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 271,
    label = "C3H4 + CH3 <=> C3H3 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2,'cm^3/(mol*s)'), n=3.5, Ea=(32010.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 272,
    label = "C3H4 + C2H <=> C3H3 + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 273,
    label = "C3H4 + C2H3 <=> C3H3 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2,'cm^3/(mol*s)'), n=3.5, Ea=(19539,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 274,
    label = "C3H4 + C2H5 <=> C3H3 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2,'cm^3/(mol*s)'), n=3.5, Ea=(27437.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 275,
    label = "C3H4 + H <=> C3H5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3e+24,'cm^6/(mol^2*s)'), n=-2, Ea=(0,'J/mol'), T0=(1,'K')), alpha=0.8, T3=(1e+15,'K'), T1=(1e+30,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 276,
    label = "C3H5 + H <=> C3H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 277,
    label = "C3H5 + H <=> C2H3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.686e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 278,
    label = "C3H5 + OH <=> C3H4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.02e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 279,
    label = "C3H5 + OH <=> C2H4 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 280,
    label = "C3H5 + O <=> CH2CO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 281,
    label = "C3H5 + HO2 <=> C3H6 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.66e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 282,
    label = "C3H5 + HO2 <=> C2H3 + CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 283,
    label = "C3H5 + HO2 <=> C2H4 + HCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 284,
    label = "C3H5 + O2 <=> C3H4 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(94785,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 285,
    label = "C3H5 + O2 <=> CH3 + CH2O + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.577e+12,'cm^3/(mol*s)'), n=0, Ea=(78571.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 286,
    label = "C3H5 + CH3 <=> C3H4 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+12,'cm^3/(mol*s)'), n=-0.32, Ea=(-417.386,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 287,
    label = "C3H5 + C2H3 <=> C3H4 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.41e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 288,
    label = "C3H5 + C2H5 <=> C3H4 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(-417.386,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 289,
    label = "C3H5 <=> C2H2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.163e+10,'s^-1'), n=-8.31, Ea=(188475,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 290,
    label = "C3H5 + H <=> C3H6",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.33e+60,'cm^6/(mol^2*s)'), n=-12, Ea=(24968.4,'J/mol'), T0=(1,'K')), alpha=0.02, T3=(1097,'K'), T1=(1097,'K'), T2=(6860,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 291,
    label = "CH3 + C2H3 <=> C3H6",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4.27e+58,'cm^6/(mol^2*s)'), n=-11.94, Ea=(40882.3,'J/mol'), T0=(1,'K')), alpha=0.175, T3=(1341,'K'), T1=(60000,'K'), T2=(10140,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 292,
    label = "C2H4 + CH2(S) <=> C3H6",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(9.64e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.2e+12,'cm^3/(mol*s)'), n=0, Ea=(21617.6,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified

Originally from reaction library: Unclassified
""",
)

entry(
    index = 293,
    label = "C3H6 <=> C2H2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+12,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 294,
    label = "C3H6 <=> C3H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(332579,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 295,
    label = "C3H6 + H <=> C3H5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(170000,'cm^3/(mol*s)'), n=2.5, Ea=(10426.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 296,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.227e+12,'cm^3/(mol*s)'), n=0, Ea=(5445.98,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 297,
    label = "C3H6 + O <=> C2H4 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+07,'cm^3/(mol*s)'), n=1.65, Ea=(-4099.03,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 298,
    label = "C3H6 + O <=> C2H5 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+07,'cm^3/(mol*s)'), n=1.65, Ea=(-4099.03,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 299,
    label = "C3H6 + O <=> C3H5 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+11,'cm^3/(mol*s)'), n=0.7, Ea=(24604.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 300,
    label = "C3H6 + O <=> CH2CO + CH3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+08,'cm^3/(mol*s)'), n=1.65, Ea=(1368.56,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 301,
    label = "C3H6 + O <=> CH3 + CH3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.96e+07,'cm^3/(mol*s)'), n=1.57, Ea=(-2624.88,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 302,
    label = "C3H6 + OH <=> C3H5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+06,'cm^3/(mol*s)'), n=2, Ea=(-1255.49,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 303,
    label = "C3H6 + OH <=> C2H5 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9e+12,'cm^3/(mol*s)'), n=0, Ea=(-3760.64,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 304,
    label = "C3H6 + HO2 <=> C3H5 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9640,'cm^3/(mol*s)'), n=2.6, Ea=(58226.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 305,
    label = "C3H5 + CH2O <=> C3H6 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.2e+07,'cm^3/(mol*s)'), n=1.8, Ea=(76110.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 306,
    label = "C3H6 + CH2(S) <=> C3H5 + CH3",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(5.239e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.227e+11,'cm^3/(mol*s)'), n=0, Ea=(25907.9,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified

Originally from reaction library: Unclassified
""",
)

entry(
    index = 307,
    label = "C3H6 + CH3 <=> C3H5 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.216,'cm^3/(mol*s)'), n=3.5, Ea=(23735.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 308,
    label = "C3H6 + C2H2 <=> C3H5 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.035e+13,'cm^3/(mol*s)'), n=0, Ea=(195889,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 309,
    label = "C3H6 + C2H3 <=> C3H5 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.02e+12,'cm^3/(mol*s)'), n=0, Ea=(60778.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 310,
    label = "C3H6 + C2H5 <=> C3H5 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.228,'cm^3/(mol*s)'), n=3.5, Ea=(27770.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 311,
    label = "C3H5 + C2H5 <=> C2H4 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+12,'cm^3/(mol*s)'), n=0, Ea=(-548.755,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 312,
    label = "C3H5 + C3H4 <=> C3H3 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(32010.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 313,
    label = "C3H5 + C3H5 <=> C3H4 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.431e+10,'cm^3/(mol*s)'), n=0, Ea=(-1097.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 314,
    label = "C3H6 + C2H <=> C3H4 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 315,
    label = "C3H6 + H <=> nC3H7",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.33e+13,'cm^3/(mol*s)'), n=0, Ea=(13644,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.26e+38,'cm^6/(mol^2*s)'), n=-6.66, Ea=(29291.9,'J/mol'), T0=(1,'K')), alpha=1, T3=(1000,'K'), T1=(1310,'K'), T2=(48100,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 316,
    label = "nC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 317,
    label = "nC3H7 <=> C2H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'s^-1'), n=0, Ea=(125762,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 318,
    label = "C3H6 + H <=> iC3H7",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.33e+13,'cm^3/(mol*s)'), n=0, Ea=(6526.86,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(8.7e+42,'cm^6/(mol^2*s)'), n=-7.5, Ea=(19755.2,'J/mol'), T0=(1,'K')), alpha=1, T3=(1000,'K'), T1=(645.4,'K'), T2=(6844,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 319,
    label = "iC3H7 + H <=> C3H6 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.613e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 320,
    label = "iC3H7 + H <=> C2H5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.409e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 321,
    label = "iC3H7 + OH <=> C3H6 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.41e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 322,
    label = "iC3H7 + HO2 <=> CH3CHO + CH3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.41e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 323,
    label = "iC3H7 + O <=> CH3CHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.818e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 324,
    label = "iC3H7 + O2 <=> C3H6 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.265e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 325,
    label = "iC3H7 + CH3 <=> C3H6 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+14,'cm^3/(mol*s)'), n=-0.68, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 326,
    label = "iC3H7 <=> C2H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'s^-1'), n=0, Ea=(144406,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 327,
    label = "iC3H7 <=> C3H6 + H",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(6.31e+13,'s^-1'), n=0, Ea=(154649,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 328,
    label = "iC3H7 + iC3H7 <=> C3H8 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.12e+14,'cm^3/(mol*s)'), n=-0.7, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 329,
    label = "C3H8 <=> iC3H7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.3e+15,'s^-1'), n=0, Ea=(397016,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 330,
    label = "C3H8 <=> nC3H7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+16,'s^-1'), n=0, Ea=(408024,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 331,
    label = "C3H8 <=> CH3 + C2H5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.1e+17,'s^-1'), n=0, Ea=(353116,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(7.83e+18,'cm^3/(mol*s)'), n=0, Ea=(271883,'J/mol'), T0=(1,'K')), alpha=0.5, T3=(1e+15,'K'), T1=(1e+30,'K'), efficiencies={'O': 12.0, 'O=C=O': 3.8, '[Ar]': 0.75, '[C-]#[O+]': 1.9, '[H][H]': 2.5, '[He]': 0.75}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 332,
    label = "C3H8 + H <=> nC3H7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.33e+06,'cm^3/(mol*s)'), n=2.54, Ea=(28269.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 333,
    label = "C3H8 + H <=> iC3H7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+06,'cm^3/(mol*s)'), n=2.4, Ea=(18707.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 334,
    label = "C3H8 + O <=> nC3H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(192700,'cm^3/(mol*s)'), n=2.68, Ea=(15548.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 335,
    label = "C3H8 + O <=> iC3H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(47600,'cm^3/(mol*s)'), n=2.71, Ea=(8817.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 336,
    label = "C3H8 + OH <=> nC3H7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1400,'cm^3/(mol*s)'), n=2.66, Ea=(2200.01,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 337,
    label = "C3H8 + OH <=> iC3H7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(27000,'cm^3/(mol*s)'), n=2.39, Ea=(1700.31,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 338,
    label = "C3H8 + HO2 <=> nC3H7 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(47600,'cm^3/(mol*s)'), n=2.55, Ea=(69010.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 339,
    label = "C3H8 + HO2 <=> iC3H7 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9640,'cm^3/(mol*s)'), n=2.6, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 340,
    label = "C3H8 + O2 <=> nC3H7 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+13,'cm^3/(mol*s)'), n=0, Ea=(213125,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 341,
    label = "C3H8 + O2 <=> iC3H7 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+13,'cm^3/(mol*s)'), n=0, Ea=(199132,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 342,
    label = "C3H8 + CH3 <=> nC3H7 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.9033,'cm^3/(mol*s)'), n=3.65, Ea=(29932.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 343,
    label = "C3H8 + CH3 <=> iC3H7 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.505,'cm^3/(mol*s)'), n=3.46, Ea=(22931.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 344,
    label = "C3H8 + iC3H7 <=> nC3H7 + C3H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0084,'cm^3/(mol*s)'), n=4.2, Ea=(36301.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 345,
    label = "C4H2 + O <=> C3H2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.891e+13,'cm^3/(mol*s)'), n=0, Ea=(7186.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 346,
    label = "C4H2 + OH <=> C3H3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e+19,'cm^3/(mol*s)'), n=-2.44, Ea=(12676.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 347,
    label = "C2H2 + C2H <=> C4H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.03e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 348,
    label = "C2H2 + C2H2 <=> C4H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.51e+13,'cm^3/(mol*s)'), n=0, Ea=(177514,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 349,
    label = "iC4H3 <=> C4H2 + H",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.12e+14,'s^-1'), n=0, Ea=(229797,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2e+15,'cm^3/(mol*s)'), n=0, Ea=(200550,'J/mol'), T0=(1,'K')), alpha=1, T3=(1,'K'), T1=(1e+08,'K'), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.2, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 350,
    label = "iC4H3 + H <=> C4H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 351,
    label = "C3H2 + CH2 <=> iC4H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(3342.42,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 352,
    label = "C3H3 + CH <=> iC4H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 353,
    label = "C2H2 + C2H2 <=> iC4H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(242013,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 354,
    label = "iC4H3 + O <=> CH2CO + C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 355,
    label = "iC4H3 + OH <=> C4H2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 356,
    label = "iC4H3 + O2 <=> CH2CO + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 357,
    label = "iC4H3 + CH2 <=> C3H4 + C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 358,
    label = "iC4H3 + C2H3 <=> C3H3 + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 359,
    label = "C4H4 <=> iC4H3 + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(8.63e+12,'cm^3/(mol*s)'), n=0, Ea=(247015,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 360,
    label = "C4H4 + H <=> iC4H3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+07,'cm^3/(mol*s)'), n=2, Ea=(20890.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 361,
    label = "C4H4 + OH <=> iC4H3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+07,'cm^3/(mol*s)'), n=2, Ea=(8356.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 362,
    label = "C4H4 + O <=> C3H4 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(7649.31,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 363,
    label = "C4H4 + C2H3 => iC4H3 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(67762.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 364,
    label = "C4H4 + C2H => iC4H3 + C2H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 365,
    label = "C2H3 + C2H2 => C4H4 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(104453,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 366,
    label = "C3H3 + CH2 <=> C4H4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 367,
    label = "C4H4 <=> C2H2 + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+15,'s^-1'), n=0, Ea=(361317,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 368,
    label = "C2H4 + C2H <=> C4H4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 369,
    label = "C4H4 + O <=> C3H3 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+08,'cm^3/(mol*s)'), n=1.44, Ea=(2298.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 370,
    label = "C4H4 + H <=> C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+51,'cm^3/(mol*s)'), n=-11.92, Ea=(68939.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 371,
    label = "C2H3 + C2H2 <=> C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.3e+38,'cm^3/(mol*s)'), n=-8.76, Ea=(50137.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 372,
    label = "C4H5 + H <=> C4H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 373,
    label = "C4H5 + H <=> iC4H5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 374,
    label = "C4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 375,
    label = "C4H5 + HCO <=> C4H6 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 376,
    label = "C4H5 + HO2 <=> C2H3 + CH2CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 377,
    label = "C4H5 + HO2 <=> C4H6 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 378,
    label = "C4H5 + H2O2 <=> C4H6 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.21e+10,'cm^3/(mol*s)'), n=0, Ea=(-2490.18,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 379,
    label = "C4H5 + O2 <=> CH2CO + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.16e+10,'cm^3/(mol*s)'), n=0, Ea=(10445.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 380,
    label = "iC4H5 <=> C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13,'s^-1'), n=0, Ea=(283274,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 381,
    label = "iC4H5 + H <=> C4H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 382,
    label = "iC4H5 + H <=> C3H3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(8356.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 383,
    label = "iC4H5 + OH <=> C4H4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 384,
    label = "iC4H5 + HCO <=> C4H6 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 385,
    label = "iC4H5 + HO2 <=> C2H3 + CH2CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 386,
    label = "iC4H5 + H2O2 <=> C4H6 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.21e+10,'cm^3/(mol*s)'), n=0, Ea=(-2490.18,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 387,
    label = "iC4H5 + O2 <=> CH2CO + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.16e+10,'cm^3/(mol*s)'), n=0, Ea=(10445.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 388,
    label = "C4H4 + H <=> iC4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.9e+51,'cm^3/(mol*s)'), n=-11.92, Ea=(73953.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 389,
    label = "C2H3 + C2H2 <=> iC4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+46,'cm^3/(mol*s)'), n=-10.98, Ea=(77712.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 390,
    label = "C2H3 + C2H3 <=> iC4H5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+22,'cm^3/(mol*s)'), n=-2.44, Ea=(57048.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 391,
    label = "C4H6 <=> C3H3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+15,'s^-1'), n=0, Ea=(311793,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 392,
    label = "C4H6 <=> iC4H5 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.0263,0.1184,1],'atm'), arrhenius=[Arrhenius(A=(8.2e+51,'s^-1'), n=-10.92, Ea=(494728,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.3e+45,'s^-1'), n=-8.95, Ea=(484387,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.7e+36,'s^-1'), n=-6.27, Ea=(469425,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 393,
    label = "C4H6 <=> C4H5 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.0263,0.1184,1],'atm'), arrhenius=[Arrhenius(A=(3.5e+61,'s^-1'), n=-13.87, Ea=(541807,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.5e+54,'s^-1'), n=-11.78, Ea=(532594,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.3e+44,'s^-1'), n=-8.62, Ea=(516450,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 394,
    label = "C4H6 <=> C4H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+15,'s^-1'), n=0, Ea=(395668,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 395,
    label = "C2H3 + C2H3 <=> C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 396,
    label = "C4H6 + H <=> C4H5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.33e+06,'cm^3/(mol*s)'), n=2.53, Ea=(51140.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 397,
    label = "C4H6 + H <=> iC4H5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(665000,'cm^3/(mol*s)'), n=2.53, Ea=(38605.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 398,
    label = "C4H6 + H <=> C3H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(29247,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 399,
    label = "C2H4 + C2H3 <=> C4H6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(30597.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 400,
    label = "C4H6 + O <=> C4H5 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.5e+06,'cm^3/(mol*s)'), n=1.9, Ea=(15626.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 401,
    label = "C4H6 + O <=> iC4H5 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.5e+06,'cm^3/(mol*s)'), n=1.9, Ea=(15626.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 402,
    label = "C4H6 + O <=> C2H4 + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 403,
    label = "C4H6 + O <=> C3H4 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 404,
    label = "C4H6 + OH <=> C4H5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.2e+06,'cm^3/(mol*s)'), n=2, Ea=(14384,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 405,
    label = "C4H6 + OH <=> iC4H5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+06,'cm^3/(mol*s)'), n=2, Ea=(1679.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 406,
    label = "C4H6 + OH <=> C3H5 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 407,
    label = "C4H6 + OH <=> CH2CO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 408,
    label = "C4H6 + O2 <=> iC4H5 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(241914,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 409,
    label = "C4H6 + CH3 <=> C4H5 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(95261.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 410,
    label = "C4H6 + CH3 <=> iC4H5 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+13,'cm^3/(mol*s)'), n=0, Ea=(64936,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 411,
    label = "C4H6 + C2H3 <=> C4H5 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(95261.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 412,
    label = "C4H6 + C2H3 <=> iC4H5 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'cm^3/(mol*s)'), n=0, Ea=(82726.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 413,
    label = "nC4H7 <=> C3H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'s^-1'), n=0, Ea=(154591,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 414,
    label = "nC4H7 <=> C2H4 + C2H3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.78e+14,'s^-1'), n=0, Ea=(154707,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4.155e+37,'cm^3/(mol*s)'), n=-6.26, Ea=(157701,'J/mol'), T0=(1,'K')), alpha=1, T3=(50,'K'), T1=(1670,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 415,
    label = "nC4H7 <=> C4H6 + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.17e+13,'s^-1'), n=0, Ea=(142730,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.439e+28,'cm^3/(mol*s)'), n=-3.68, Ea=(114783,'J/mol'), T0=(1,'K')), alpha=0.81, T3=(50,'K'), T1=(1150,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 416,
    label = "nC4H7 + H <=> C4H6 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 417,
    label = "nC4H7 + O2 <=> C4H6 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 418,
    label = "nC4H7 + CH3 <=> C4H6 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 419,
    label = "nC4H7 + C2H3 <=> C4H6 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 420,
    label = "nC4H7 + C2H5 <=> C4H6 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 421,
    label = "nC4H7 + C3H5 <=> C4H6 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 422,
    label = "nC4H7 + C2H5 <=> C4H8 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 423,
    label = "nC4H7 + nC4H7 <=> C4H6 + C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 424,
    label = "nC4H7 + H <=> C4H8",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24373.9,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 425,
    label = "C4H8 <=> C3H5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(304542,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 426,
    label = "C2H5 + C2H3 <=> C4H8",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.55e+56,'cm^6/(mol^2*s)'), n=-11.79, Ea=(37538.2,'J/mol'), T0=(1,'K')), alpha=0.198, T3=(2277.9,'K'), T1=(60000,'K'), T2=(5723.2,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 427,
    label = "C4H8 + H <=> nC4H7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(16296.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 428,
    label = "C4H8 + H <=> C3H6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 429,
    label = "C4H8 + H <=> C2H4 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 430,
    label = "C4H8 + H <=> C2H4 + C2H3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(660000,'cm^3/(mol*s)'), n=2.54, Ea=(28256.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 431,
    label = "C4H8 + O <=> nC4H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(18759.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 432,
    label = "C4H8 + O <=> C2H4 + CH3CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.25e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 433,
    label = "C4H8 + O <=> C2H5 + CH3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 434,
    label = "C4H8 + O <=> C3H6 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 435,
    label = "C4H8 + O <=> nC3H7 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+06,'cm^3/(mol*s)'), n=2.34, Ea=(-4157.24,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 436,
    label = "C4H8 + OH <=> nC4H7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(4988.68,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 437,
    label = "C4H8 + OH <=> C2H5 + CH3CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 438,
    label = "C4H8 + OH => C2H6 + CH3 + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 439,
    label = "C4H8 + OH <=> nC3H7 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 440,
    label = "C4H8 + O2 <=> nC4H7 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(164582,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 441,
    label = "C4H8 + HO2 <=> nC4H7 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(71404.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 442,
    label = "C4H8 + CH3 <=> nC4H7 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(30597.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 443,
    label = "C4H8 + C2H5 <=> nC4H7 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(33471.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 444,
    label = "C4H8 + C3H5 <=> nC4H7 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+10,'cm^3/(mol*s)'), n=0, Ea=(54401.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 445,
    label = "C4H8 <=> C4H6 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(273583,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 446,
    label = "C3H6 + CH3 <=> iC4H9",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(9.6e+10,'cm^3/(mol*s)'), n=0, Ea=(33440,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.3e+28,'cm^6/(mol^2*s)'), n=-4.27, Ea=(10157.8,'J/mol'), T0=(1,'K')), alpha=0.565, T3=(60000,'K'), T1=(534.2,'K'), T2=(3007.2,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 447,
    label = "iC4H9 + H <=> iC3H7 + CH3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10],'atm'), arrhenius=[Arrhenius(A=(1.1e+32,'cm^3/(mol*s)'), n=-5.04, Ea=(70025.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.9e+35,'cm^3/(mol*s)'), n=-5.83, Ea=(93882.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.35e+40,'cm^3/(mol*s)'), n=-7.02, Ea=(129522,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 448,
    label = "iC4H9 + CH3 <=> iC4H8 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+12,'cm^3/(mol*s)'), n=-0.32, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 449,
    label = "iC4H9 + O2 <=> iC4H8 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 450,
    label = "iC4H9 + OH <=> iC4H8 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 451,
    label = "iC4H9 + H <=> iC4H8 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 452,
    label = "iC4H8 <=> C3H5 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(389018,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 453,
    label = "iC4H8 + H <=> iC4H9",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.33e+13,'cm^3/(mol*s)'), n=0, Ea=(13623.6,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.26e+38,'cm^6/(mol^2*s)'), n=-6.66, Ea=(29246.9,'J/mol'), T0=(1,'K')), alpha=1, T3=(1000,'K'), T1=(1310,'K'), T2=(48097,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 454,
    label = "iC4H8 + H <=> iC4H7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+06,'cm^3/(mol*s)'), n=2.54, Ea=(28244.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 455,
    label = "iC4H8 + H <=> C3H6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+21,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 456,
    label = "iC4H8 + O <=> CH3 + CH3 + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+08,'cm^3/(mol*s)'), n=1.65, Ea=(1366.23,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 457,
    label = "iC4H8 + O <=> iC3H7 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+07,'cm^3/(mol*s)'), n=1.65, Ea=(-4061.12,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 458,
    label = "iC4H8 + O <=> iC4H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(290000,'cm^3/(mol*s)'), n=2.5, Ea=(15208.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 459,
    label = "iC4H8 + OH <=> iC4H7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+08,'cm^3/(mol*s)'), n=1.53, Ea=(3238.07,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 460,
    label = "iC4H8 + HO2 <=> iC4H7 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(20000,'cm^3/(mol*s)'), n=2.55, Ea=(64760.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 461,
    label = "iC4H8 + O2 <=> iC4H7 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.7e+13,'cm^3/(mol*s)'), n=0, Ea=(212667,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 462,
    label = "iC4H8 + CH3 <=> iC4H7 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.91,'cm^3/(mol*s)'), n=3.65, Ea=(29873.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 463,
    label = "iC4H7 <=> C3H4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(213197,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 464,
    label = "iC4H7 <=> C4H6 + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(206199,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 465,
    label = "iC4H7 <=> C2H4 + C2H3",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(154649,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 466,
    label = "iC4H7 + O2 => C3H4 + CH2O + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7.29e+31,'cm^3/(mol*s)'), n=-5.71, Ea=(89620.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 467,
    label = "iC4H7 + H <=> C4H6 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 468,
    label = "iC4H7 + C2H3 <=> C4H6 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 469,
    label = "iC4H7 + C2H5 <=> C4H6 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 470,
    label = "iC4H7 + CH3 <=> C4H6 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 471,
    label = "iC4H7 + C3H5 <=> C4H6 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 472,
    label = "pC4H9 <=> C2H4 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(120327,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 473,
    label = "pC4H9 <=> C4H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+13,'s^-1'), n=0, Ea=(161276,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 474,
    label = "pC4H9 + O2 <=> C4H8 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(8356.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 475,
    label = "sC4H9 <=> C4H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(166289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 476,
    label = "sC4H9 <=> C3H6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+14,'s^-1'), n=0, Ea=(138710,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 477,
    label = "sC4H9 + O2 <=> C4H8 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+12,'cm^3/(mol*s)'), n=0, Ea=(18383.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 478,
    label = "tC4H9 <=> iC4H8 + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(8.3e+13,'s^-1'), n=0, Ea=(159398,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.9e+41,'cm^3/(mol*s)'), n=-7.36, Ea=(153052,'J/mol'), T0=(1,'K')), alpha=0.293, T3=(649,'K'), T1=(60000,'K'), T2=(3425.9,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 479,
    label = "tC4H9 + H <=> iC3H7 + CH3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10],'atm'), arrhenius=[Arrhenius(A=(2.8e+34,'cm^3/(mol*s)'), n=-5.69, Ea=(85651.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.6e+36,'cm^3/(mol*s)'), n=-6.12, Ea=(107127,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.6e+36,'cm^3/(mol*s)'), n=-6.12, Ea=(107127,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 480,
    label = "tC4H9 + CH3 <=> iC4H8 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.8e+15,'cm^3/(mol*s)'), n=-1, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 481,
    label = "tC4H9 + O2 <=> iC4H8 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.837,'cm^3/(mol*s)'), n=3.6, Ea=(49970,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 482,
    label = "tC4H9 + OH <=> iC4H8 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 483,
    label = "tC4H9 + O <=> iC4H8 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 484,
    label = "tC4H9 + H <=> iC4H8 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.42e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 485,
    label = "nC3H7 + CH3 <=> N-C4H10",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.93e+14,'cm^3/(mol*s)'), n=-0.32, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.68e+61,'cm^6/(mol^2*s)'), n=-13.24, Ea=(25068.8,'J/mol'), T0=(1,'K')), alpha=1, T3=(1000,'K'), T1=(1433.9,'K'), T2=(5328.8,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 486,
    label = "C2H5 + C2H5 <=> N-C4H10",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.88e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.61e+61,'cm^6/(mol^2*s)'), n=-13.42, Ea=(25068.8,'J/mol'), T0=(1,'K')), alpha=1, T3=(1000,'K'), T1=(1433.9,'K'), T2=(5328.8,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 487,
    label = "N-C4H10 + H <=> pC4H9 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.8e+13,'cm^3/(mol*s)'), n=0, Ea=(50873.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 488,
    label = "N-C4H10 + H <=> sC4H9 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.108e+13,'cm^3/(mol*s)'), n=0, Ea=(32947.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 489,
    label = "N-C4H10 + O <=> pC4H9 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+14,'cm^3/(mol*s)'), n=0, Ea=(32800.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 490,
    label = "N-C4H10 + O <=> sC4H9 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.62e+13,'cm^3/(mol*s)'), n=0, Ea=(21726.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 491,
    label = "N-C4H10 + OH <=> pC4H9 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.71e+09,'cm^3/(mol*s)'), n=1.05, Ea=(7566.17,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 492,
    label = "N-C4H10 + OH <=> sC4H9 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.57e+09,'cm^3/(mol*s)'), n=1.25, Ea=(2926.69,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 493,
    label = "N-C4H10 + O2 <=> pC4H9 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(218671,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 494,
    label = "N-C4H10 + O2 <=> sC4H9 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(208070,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 495,
    label = "N-C4H10 + CH3 <=> pC4H9 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.29e+12,'cm^3/(mol*s)'), n=0, Ea=(48465.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 496,
    label = "N-C4H10 + CH3 <=> sC4H9 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+11,'cm^3/(mol*s)'), n=0, Ea=(39693.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 497,
    label = "nC4H9OH <=> CH3 + CH2CH2CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(352617,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 498,
    label = "nC4H9OH <=> C2H5 + CH2CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(342141,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 499,
    label = "nC4H9OH <=> nC3H7 + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(342141,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 500,
    label = "nC4H9OH <=> C4H8 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.9e+13,'s^-1'), n=0, Ea=(291747,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 501,
    label = "nC4H9O-2 + H <=> nC4H9OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 502,
    label = "CH3CH2CH2CHOH + H <=> nC4H9OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 503,
    label = "nC4H9OH + O <=> nC4H9O-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(428900,'cm^3/(mol*s)'), n=2.65, Ea=(10794.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 504,
    label = "nC4H9OH + O <=> CH3CH2CH2CHOH + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(428900,'cm^3/(mol*s)'), n=2.79, Ea=(9123.55,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 505,
    label = "nC4H9OH + H <=> nC4H9O-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14e+06,'cm^3/(mol*s)'), n=2.25, Ea=(22729,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 506,
    label = "nC4H9OH + H <=> CH3CH2CH2CHOH + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(925000,'cm^3/(mol*s)'), n=2.28, Ea=(15709.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 507,
    label = "nC4H9OH + OH <=> nC4H9O-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+06,'cm^3/(mol*s)'), n=1.9, Ea=(1086.31,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 508,
    label = "nC4H9OH + OH <=> CH3CH2CH2CHOH + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.9e+06,'cm^3/(mol*s)'), n=1.9, Ea=(668.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 509,
    label = "nC4H9OH + CH3 <=> nC4H9O-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.29,'cm^3/(mol*s)'), n=3.37, Ea=(32547.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 510,
    label = "nC4H9OH + CH3 <=> CH3CH2CH2CHOH + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(15.3,'cm^3/(mol*s)'), n=3.31, Ea=(29038,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 511,
    label = "nC4H9OH + O2 <=> nC4H9O-2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.588e+14,'cm^3/(mol*s)'), n=0, Ea=(199255,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 512,
    label = "nC4H9OH + O2 <=> CH3CH2CH2CHOH + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.588e+14,'cm^3/(mol*s)'), n=0, Ea=(199255,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 513,
    label = "C4H8 + OH <=> nC4H9O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(34263.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 514,
    label = "C3H6 + CH2OH <=> nC4H9O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(34263.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 515,
    label = "H + nC4H7OH <=> nC4H9O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(12114.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 516,
    label = "CH3CH2CH2CHOH <=> Ethenol + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.516e+12,'s^-1'), n=0.602, Ea=(121667,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 517,
    label = "CH3CH2CH2CHOH <=> nC4H9O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.8e+10,'s^-1'), n=0.67, Ea=(152920,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 518,
    label = "CH3CH2CH2CHOH <=> nC4H7OH + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.065e+11,'s^-1'), n=0.4, Ea=(148031,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 519,
    label = "Ethenol + OH <=> CH2HCO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.46e+11,'cm^3/(mol*s)'), n=0.3, Ea=(6826.18,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 520,
    label = "Ethenol + H <=> CH2HCO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+07,'cm^3/(mol*s)'), n=1.6, Ea=(12696.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 521,
    label = "Ethenol + O <=> CH2HCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+13,'cm^3/(mol*s)'), n=0, Ea=(21725.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 522,
    label = "Ethenol + HO2 <=> CH2HCO + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.6e+12,'cm^3/(mol*s)'), n=0, Ea=(73957.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 523,
    label = "Ethenol + CH3 <=> CH2HCO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+11,'cm^3/(mol*s)'), n=0, Ea=(39693.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 524,
    label = "Ethenol <=> CH3CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.42e+46,'s^-1'), n=-10.56, Ea=(281689,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 525,
    label = "C2H4 + CH2OH <=> CH2CH2CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(34263.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 526,
    label = "nC3H7CHO <=> C2H5 + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+16,'s^-1'), n=0, Ea=(342606,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 527,
    label = "nC3H7CHO <=> nC3H7 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+16,'s^-1'), n=0, Ea=(355144,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 528,
    label = "nC3H7CHO <=> C4H7O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+15,'s^-1'), n=0, Ea=(355141,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 529,
    label = "nC3H7CHO <=> C4H7O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+15,'s^-1'), n=0, Ea=(396881,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 530,
    label = "nC3H7CHO + H <=> C4H7O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(29246.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 531,
    label = "nC3H7CHO + H <=> C4H7O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+06,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 532,
    label = "nC3H7CHO + O <=> C4H7O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.85e+12,'cm^3/(mol*s)'), n=0, Ea=(7554.06,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 533,
    label = "nC3H7CHO + O <=> C4H7O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(47700,'cm^3/(mol*s)'), n=2.71, Ea=(8799.12,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 534,
    label = "nC3H7CHO + OH <=> C4H7O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.65e+12,'cm^3/(mol*s)'), n=0, Ea=(-3050.03,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 535,
    label = "nC3H7CHO + OH <=> C4H7O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.68e+07,'cm^3/(mol*s)'), n=1.61, Ea=(-146.234,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 536,
    label = "nC3H7CHO + HO2 <=> C4H7O + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+12,'cm^3/(mol*s)'), n=0, Ea=(44705.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 537,
    label = "nC3H7CHO + HO2 <=> C4H7O + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.6e+12,'cm^3/(mol*s)'), n=0, Ea=(73911.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 538,
    label = "nC3H7CHO + CH3 <=> C4H7O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+12,'cm^3/(mol*s)'), n=0, Ea=(35263.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 539,
    label = "nC3H7CHO + CH3 <=> C4H7O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(27050,'cm^3/(mol*s)'), n=2.26, Ea=(30446,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 540,
    label = "nC3H7CHO + O2 <=> C4H7O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0.5, Ea=(176317,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 541,
    label = "nC3H7CHO + O2 <=> C4H7O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(199255,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 542,
    label = "C4H7O <=> nC3H7 + CO",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(8.64e+15,'cm^3/(mol*s)'), n=0, Ea=(60165,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 543,
    label = "C4H7O <=> CH2CO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.745e+09,'s^-1'), n=1.41, Ea=(149702,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 544,
    label = "C4H7O <=> C4H6O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.658e+10,'s^-1'), n=0.79, Ea=(177779,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 545,
    label = "C4H7O <=> C3H6 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.249e+12,'s^-1'), n=-0.18, Ea=(91500.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 546,
    label = "C4H7O <=> C2H4 + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.4e+11,'s^-1'), n=0, Ea=(91793.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 547,
    label = "C4H7O <=> C4H6O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.431e+15,'s^-1'), n=-0.6, Ea=(168796,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 548,
    label = "C4H6O + OH <=> nC3H7 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.73e+12,'cm^3/(mol*s)'), n=0, Ea=(-4219.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 549,
    label = "C4H6O + H <=> nC3H7 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.4e+12,'cm^3/(mol*s)'), n=0, Ea=(6095.89,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 550,
    label = "C4H6O + O <=> C3H6 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+12,'cm^3/(mol*s)'), n=0, Ea=(-1825.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 551,
    label = "nC4H7OH <=> C3H5 + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.644e+19,'s^-1'), n=-1.132, Ea=(311646,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 552,
    label = "nC4H7OH <=> nC4H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.367e+20,'s^-1'), n=-1.189, Ea=(394106,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 553,
    label = "nC4H7OH <=> C2H3 + CH2CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.644e+19,'s^-1'), n=-1.132, Ea=(311793,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 554,
    label = "nC4H7OH <=> C2H5 + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.214e+22,'s^-1'), n=-1.576, Ea=(407409,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 555,
    label = "DME <=> CH3 + CH3O",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+19,'s^-1'), n=-0.66, Ea=(352076,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.722e+59,'cm^3/(mol*s)'), n=-11.4, Ea=(390389,'J/mol'), T0=(1,'K')), alpha=1, T3=(1e-30,'K'), T1=(880,'K'), efficiencies={'C': 3.0, 'CC': 4.5, 'COC': 5.0, 'N#N': 1.5, 'O': 9.0, 'O=C=O': 3.0, '[C-]#[O+]': 2.25, '[H][H]': 3.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 556,
    label = "DME + CH3 <=> (C2H5O) + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(52298,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 557,
    label = "DME + HO2 <=> (C2H5O) + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00317,'cm^3/(mol*s)'), n=4.64, Ea=(44104.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 558,
    label = "DME + O <=> (C2H5O) + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.391e+12,'cm^3/(mol*s)'), n=2, Ea=(10979.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 559,
    label = "DME + H <=> (C2H5O) + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.721e+06,'cm^3/(mol*s)'), n=2.09, Ea=(14138.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 560,
    label = "DME + OH <=> (C2H5O) + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.745e+11,'cm^3/(mol*s)'), n=2.07, Ea=(-2175.89,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 561,
    label = "(C2H5O) <=> CH3 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.27e+14,'s^-1'), n=-0.22, Ea=(114008,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 562,
    label = "OME1 <=> COCO* + CH3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+19,'s^-1'), n=-0.66, Ea=(351546,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.72e+59,'cm^3/(mol*s)'), n=-11.4, Ea=(389801,'J/mol'), T0=(1,'K')), alpha=1, T3=(1e-30,'K'), T1=(880,'K'), efficiencies={'C': 3.0, 'CC': 4.5, 'O': 9.0, 'O=C=O': 3.0, '[Ar]': 1.0, '[C-]#[O+]': 2.25, '[H][H]': 3.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 563,
    label = "OME1 <=> (C2H5O) + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24e+25,'s^-1'), n=-2.29, Ea=(356520,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 564,
    label = "OME1*-1 <=> (C2H5O) + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.23997e+14,'s^-1'), n=-0.22, Ea=(105289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 565,
    label = "OME1 + H <=> OME1*-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.3e+12,'cm^3/(mol*s)'), n=0, Ea=(14151.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 566,
    label = "OME1 + OH <=> OME1*-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.954e+07,'cm^3/(mol*s)'), n=1.89, Ea=(-1527.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 567,
    label = "OME1 + O <=> OME1*-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.689e+07,'cm^3/(mol*s)'), n=2, Ea=(10996.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 568,
    label = "OME1 + CH3 <=> OME1*-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.19,'cm^3/(mol*s)'), n=3.78, Ea=(40477.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 569,
    label = "OME1 + HO2 <=> OME1*-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1680,'cm^3/(mol*s)'), n=0, Ea=(73911.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 570,
    label = "OME1 + CH3O <=> OME1*-1 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.02e+11,'cm^3/(mol*s)'), n=0, Ea=(17021.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 571,
    label = "OME1*-2 <=> (C2H4O2) + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(218.6,'s^-1'), n=1.1549, Ea=(56580.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 572,
    label = "OME1 + H <=> OME1*-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.4e+12,'cm^3/(mol*s)'), n=0, Ea=(13244.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 573,
    label = "OME1 + OH <=> OME1*-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 574,
    label = "OME1 + O <=> OME1*-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 575,
    label = "OME1 + CH3 <=> OME1*-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 576,
    label = "OME1 + HO2 <=> OME1*-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 577,
    label = "OME1 + CH3O <=> OME1*-2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 578,
    label = "(C2H4O2) + H <=> (C2H3O2) + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(665000,'cm^3/(mol*s)'), n=2.54, Ea=(28227.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 579,
    label = "(C2H4O2) + OH <=> (C2H3O2) + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.27e+09,'cm^3/(mol*s)'), n=0.97, Ea=(6626.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 580,
    label = "(C2H4O2) + O <=> (C2H3O2) + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.373e+13,'cm^3/(mol*s)'), n=0, Ea=(23945.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 581,
    label = "(C2H4O2) + CH3 <=> (C2H3O2) + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.452,'cm^3/(mol*s)'), n=3.65, Ea=(29890.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 582,
    label = "(C2H4O2) + H <=> (C2H3O2) + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 583,
    label = "(C2H4O2) + OH <=> (C2H3O2) + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+07,'cm^3/(mol*s)'), n=1.8, Ea=(3902.37,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 584,
    label = "(C2H4O2) + CH3 <=> (C2H3O2) + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.755,'cm^3/(mol*s)'), n=3.46, Ea=(22900.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 585,
    label = "(C2H4O2) <=> (CHO2) + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 586,
    label = "CH2O + HCO <=> (C2H3O2)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+11,'cm^3/(mol*s)'), n=0, Ea=(49719.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 587,
    label = "(C2H3O2) <=> CH3 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.55e+12,'s^-1'), n=0.515, Ea=(126155,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 588,
    label = "(C2H3O2) <=> CH3O + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.37e+12,'s^-1'), n=0.479, Ea=(197818,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 589,
    label = "(CHO2) <=> H + CO2",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.443e+15,'cm^3/(mol*s)'), n=-0.5, Ea=(110749,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 590,
    label = "COCO* <=> CH3O + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 591,
    label = "COCO* <=> (C2H4O2) + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 592,
    label = "OME2 <=> (C2H5O) + COCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 593,
    label = "OME2 <=> OME1*-1 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24e+25,'s^-1'), n=-2.29, Ea=(356520,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 594,
    label = "OME2 <=> CH3 + COCOCO*",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+19,'s^-1'), n=-0.66, Ea=(351546,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.72e+59,'cm^3/(mol*s)'), n=-11.4, Ea=(389801,'J/mol'), T0=(1,'K')), alpha=1, T3=(1e-30,'K'), T1=(880,'K'), efficiencies={'C': 3.0, 'CC': 4.5, 'O': 9.0, 'O=C=O': 3.0, '[Ar]': 1.0, '[C-]#[O+]': 2.25, '[H][H]': 3.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 595,
    label = "OME2*-1 <=> OME1*-1 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+14,'s^-1'), n=-0.22, Ea=(105289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 596,
    label = "OME2 + CH3 <=> OME2*-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.19,'cm^3/(mol*s)'), n=3.78, Ea=(40477.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 597,
    label = "OME2 + OH <=> OME2*-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.954e+06,'cm^3/(mol*s)'), n=1.89, Ea=(-1527.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 598,
    label = "OME2 + H <=> OME2*-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.3e+12,'cm^3/(mol*s)'), n=0, Ea=(14151.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 599,
    label = "OME2 + O <=> OME2*-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.689e+06,'cm^3/(mol*s)'), n=2, Ea=(10996.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 600,
    label = "OME2 + HO2 <=> OME2*-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1680,'cm^3/(mol*s)'), n=0, Ea=(73911.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 601,
    label = "OME2 + CH3O <=> OME2*-1 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.02e+10,'cm^3/(mol*s)'), n=0, Ea=(17021.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 602,
    label = "OME2*-2 <=> COCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 603,
    label = "OME2*-2 <=> (C2H4O2) + (C2H5O)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+14,'s^-1'), n=-0.22, Ea=(105289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 604,
    label = "OME2 + H <=> OME2*-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 605,
    label = "OME2 + CH3 <=> OME2*-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 606,
    label = "OME2 + HO2 <=> OME2*-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 607,
    label = "OME2 + OH <=> OME2*-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 608,
    label = "OME2 + O <=> OME2*-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 609,
    label = "OME2 + CH3O <=> OME2*-2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 610,
    label = "COCOCO* <=> COCO* + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 611,
    label = "COCOCO* <=> COCOCHO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 612,
    label = "iOME2 <=> (C3H7O3) + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.658e+24,'s^-1'), n=-1.79, Ea=(353820,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 613,
    label = "iOME2 <=> OME1*-1 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.21e+22,'s^-1'), n=-0.36, Ea=(424624,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 614,
    label = "iOME2 <=> iOME2*-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.562e+16,'s^-1'), n=-2.02, Ea=(379022,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 615,
    label = "iOME2 <=> iOME2*-1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.048e+16,'s^-1'), n=0.05, Ea=(406023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 616,
    label = "iOME2*-1 <=> OME1*-2 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.206e+14,'s^-1'), n=0.34, Ea=(91005.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 617,
    label = "iOME2 + H <=> iOME2*-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(162000,'cm^3/(mol*s)'), n=0, Ea=(7798.97,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 618,
    label = "iOME2 + O <=> iOME2*-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.3e+07,'cm^3/(mol*s)'), n=0, Ea=(22000.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 619,
    label = "iOME2 + OH <=> iOME2*-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(450,'cm^3/(mol*s)'), n=1.44, Ea=(498.868,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 620,
    label = "iOME2 + CH3 <=> iOME2*-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.57e-13,'cm^3/(mol*s)'), n=5.58, Ea=(16296.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 621,
    label = "iOME2 + HO2 <=> iOME2*-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.05e-09,'cm^3/(mol*s)'), n=4.85, Ea=(43301.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 622,
    label = "iOME2 + CH3O <=> iOME2*-1 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.26e-07,'cm^3/(mol*s)'), n=4.13, Ea=(26997.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 623,
    label = "iOME2 + O2 <=> iOME2*-1 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08,'cm^3/(mol*s)'), n=2.27, Ea=(199007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 624,
    label = "iOME2*-2 <=> (C3H6O3) + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(446200,'s^-1'), n=2.84, Ea=(2702.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 625,
    label = "iOME2 + H <=> iOME2*-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.414,'cm^3/(mol*s)'), n=2.34, Ea=(11199.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 626,
    label = "iOME2 + O <=> iOME2*-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.383,'cm^3/(mol*s)'), n=2.41, Ea=(62001,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 627,
    label = "iOME2 + OH <=> iOME2*-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.62,'cm^3/(mol*s)'), n=1.47, Ea=(34006.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 628,
    label = "iOME2 + CH3 <=> iOME2*-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.37e-07,'cm^3/(mol*s)'), n=3.72, Ea=(43002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 629,
    label = "iOME2 + HO2 <=> iOME2*-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+06,'cm^3/(mol*s)'), n=0, Ea=(67014.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 630,
    label = "iOME2 + CH3O <=> iOME2*-2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(19000,'cm^3/(mol*s)'), n=0, Ea=(40599.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 631,
    label = "iOME2 + O2 <=> iOME2*-2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+07,'cm^3/(mol*s)'), n=0, Ea=(216010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 632,
    label = "(C3H7O3) <=> (C2H4O2) + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.471,'s^-1'), n=3.5, Ea=(65002.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 633,
    label = "(C3H6O3) <=> (C2H3O3) + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.02e+22,'s^-1'), n=-1.61, Ea=(373020,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 634,
    label = "(C3H6O3) <=> (C2H3O2) + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.38e+23,'s^-1'), n=-2.06, Ea=(439021,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 635,
    label = "(C2H3O3) <=> (C2H3O2) + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.925e+16,'s^-1'), n=-0.41, Ea=(435021,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 636,
    label = "(C2H3O3) <=> CH3O + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.084e+17,'s^-1'), n=-1.52, Ea=(16005.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 637,
    label = "OME3 <=> OME1*-1 + COCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 638,
    label = "OME3 <=> (C2H5O) + COCOCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 639,
    label = "OME3 <=> OME2*-1 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24e+25,'s^-1'), n=-2.29, Ea=(356520,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 640,
    label = "OME3 <=> CH3 + COCOCOCO*",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+19,'s^-1'), n=-0.66, Ea=(351546,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.72e+59,'cm^3/(mol*s)'), n=-11.4, Ea=(389801,'J/mol'), T0=(1,'K')), alpha=1, T3=(1e-30,'K'), T1=(880,'K'), efficiencies={'C': 3.0, 'CC': 4.5, 'O': 9.0, 'O=C=O': 3.0, '[Ar]': 1.0, '[C-]#[O+]': 2.25, '[H][H]': 3.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 641,
    label = "OME3*-1 <=> OME2*-1 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+14,'s^-1'), n=-0.22, Ea=(105289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 642,
    label = "OME3 + CH3 <=> OME3*-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.19,'cm^3/(mol*s)'), n=3.78, Ea=(40477.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 643,
    label = "OME3 + OH <=> OME3*-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.954e+06,'cm^3/(mol*s)'), n=1.89, Ea=(-1527.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 644,
    label = "OME3 + H <=> OME3*-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.3e+12,'cm^3/(mol*s)'), n=0, Ea=(14151.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 645,
    label = "OME3 + O <=> OME3*-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.689e+06,'cm^3/(mol*s)'), n=2, Ea=(10996.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 646,
    label = "OME3 + HO2 <=> OME3*-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1680,'cm^3/(mol*s)'), n=0, Ea=(73911.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 647,
    label = "OME3 + CH3O <=> OME3*-1 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.02e+10,'cm^3/(mol*s)'), n=0, Ea=(17021.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 648,
    label = "OME3*-2 <=> OME1*-1 + (C2H4O2)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.483e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 649,
    label = "OME3*-2 <=> COCOCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 650,
    label = "OME3*-2 + H <=> OME3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 651,
    label = "OME3 + H <=> OME3*-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 652,
    label = "OME3 + CH3 <=> OME3*-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 653,
    label = "OME3 + HO2 <=> OME3*-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 654,
    label = "OME3 + OH <=> OME3*-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 655,
    label = "OME3 + O <=> OME3*-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 656,
    label = "OME3 + CH3O <=> OME3*-2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 657,
    label = "OME3*-3 <=> COCOCHO + (C2H5O)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.967e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 658,
    label = "OME3*-3 + H <=> OME3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 659,
    label = "OME3 + H <=> OME3*-3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 660,
    label = "OME3 + CH3 <=> OME3*-3 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 661,
    label = "OME3 + HO2 <=> OME3*-3 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 662,
    label = "OME3 + OH <=> OME3*-3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 663,
    label = "OME3 + O <=> OME3*-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 664,
    label = "OME3 + CH3O <=> OME3*-3 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 665,
    label = "COCOCOCO* <=> COCOCO* + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 666,
    label = "COCOCOCO* <=> COCOCOCHO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 667,
    label = "COCOCOCHO + H <=> COCOCOC*O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.668e+12,'cm^3/(mol*s)'), n=2.05, Ea=(37172.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 668,
    label = "COCOCOCHO + OH <=> COCOCOC*O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.915e+11,'cm^3/(mol*s)'), n=2, Ea=(6102.82,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 669,
    label = "COCOCOCHO + O <=> COCOCOC*O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.373e+13,'cm^3/(mol*s)'), n=0, Ea=(23945.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 670,
    label = "COCOCOCHO + CH3 <=> COCOCOC*O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.764e+09,'cm^3/(mol*s)'), n=3.35, Ea=(48223.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 671,
    label = "COCOCOCHO + H <=> COCOC*OCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 672,
    label = "COCOCOCHO + OH <=> COCOC*OCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 673,
    label = "COCOCOCHO + CH3 <=> COCOC*OCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 674,
    label = "COCOCOCHO + H <=> COC*OCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 675,
    label = "COCOCOCHO + OH <=> COC*OCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 676,
    label = "COCOCOCHO + CH3 <=> COC*OCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 677,
    label = "COCOCOCHO + H <=> C*OCOCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 678,
    label = "COCOCOCHO + OH <=> C*OCOCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 679,
    label = "COCOCOCHO + CH3 <=> C*OCOCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 680,
    label = "COCOCOC*O <=> OME1*-1 + CO2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.0066,0.0395,0.0921,0.2632,1,10],'atm'), arrhenius=[Arrhenius(A=(6.63e+07,'s^-1'), n=-0.07, Ea=(32943.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.21e+08,'s^-1'), n=0, Ea=(32738.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.12e+08,'s^-1'), n=0, Ea=(33127.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(9.56e+08,'s^-1'), n=0.05, Ea=(33165.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.89e+09,'s^-1'), n=0.13, Ea=(33317.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.06e+10,'s^-1'), n=0.18, Ea=(35002.3,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 681,
    label = "OCOCHO + (C2H5O) <=> COCOC*OCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(27861.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 682,
    label = "COCOCHO + HCO <=> COCOC*OCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(27861.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 683,
    label = "(C2H4O2) + (C2H3O2) <=> COC*OCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 684,
    label = "COC*OCOCHO <=> OCOCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 685,
    label = "C*OCOCOCHO <=> C*OCOCHO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+13,'s^-1'), n=-0.4, Ea=(102823,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 686,
    label = "(C2H3O2) + CH2O <=> C*OCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(27861.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 687,
    label = "COC*OCHO + H <=> COCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 688,
    label = "COC*OCHO <=> OCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 689,
    label = "(CHO2) + (C2H3O2) <=> OCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 690,
    label = "(CHO2) + HCO <=> OCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 691,
    label = "(C2H5O) + O2 <=> CH3OCH2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 692,
    label = "CH3OCH2O2 + CH3CHO <=> CH3OCH2O2H + CH3CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+12,'cm^3/(mol*s)'), n=0, Ea=(56822.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 693,
    label = "CH3OCH2O2 + CH2O <=> CH3OCH2O2H + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(48717,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 694,
    label = "COCO* + OH <=> CH3OCH2O2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 695,
    label = "OME4 <=> (C2H5O) + COCOCOCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 696,
    label = "OME4 <=> OME2*-1 + COCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 697,
    label = "OME4 <=> OME1*-1 + COCOCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 698,
    label = "OME4 <=> OME3*-1 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.24e+25,'s^-1'), n=-2.29, Ea=(356520,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 699,
    label = "OME4 <=> CH3 + COCOCOCOCO*",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+19,'s^-1'), n=-0.66, Ea=(351546,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.72e+59,'cm^3/(mol*s)'), n=-11.4, Ea=(389801,'J/mol'), T0=(1,'K')), alpha=1, T3=(1e-30,'K'), T1=(880,'K'), efficiencies={'C': 3.0, 'CC': 4.5, 'O': 9.0, 'O=C=O': 3.0, '[Ar]': 1.0, '[C-]#[O+]': 2.25, '[H][H]': 3.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 700,
    label = "OME4*-1 <=> OME3*-1 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+14,'s^-1'), n=-0.22, Ea=(105289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 701,
    label = "OME4 + CH3 <=> OME4*-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.19,'cm^3/(mol*s)'), n=3.78, Ea=(40477.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 702,
    label = "OME4 + OH <=> OME4*-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.954e+06,'cm^3/(mol*s)'), n=1.89, Ea=(-1527.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 703,
    label = "OME4 + H <=> OME4*-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.3e+12,'cm^3/(mol*s)'), n=0, Ea=(14151.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 704,
    label = "OME4 + O <=> OME4*-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.689e+06,'cm^3/(mol*s)'), n=2, Ea=(10996.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 705,
    label = "OME4 + HO2 <=> OME4*-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1680,'cm^3/(mol*s)'), n=0, Ea=(73911.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 706,
    label = "OME4*-2 <=> (C2H4O2) + OME2*-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.48e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 707,
    label = "OME4*-2 <=> COCOCOCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 708,
    label = "OME4*-2 + H <=> OME4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 709,
    label = "OME4 + H <=> OME4*-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 710,
    label = "OME4 + CH3 <=> OME4*-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 711,
    label = "OME4 + HO2 <=> OME4*-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 712,
    label = "OME4 + OH <=> OME4*-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 713,
    label = "OME4 + O <=> OME4*-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 714,
    label = "OME4 + CH3O <=> OME4*-2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 715,
    label = "OME4*-3 <=> COCOCOCHO + (C2H5O)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.967e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 716,
    label = "OME4*-3 <=> COCOCHO + OME1*-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.967e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 717,
    label = "OME4*-3 + H <=> OME4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 718,
    label = "OME4 + H <=> OME4*-3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 719,
    label = "OME4 + CH3 <=> OME4*-3 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 720,
    label = "OME4 + HO2 <=> OME4*-3 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 721,
    label = "OME4 + OH <=> OME4*-3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 722,
    label = "OME4 + O <=> OME4*-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 723,
    label = "OME4 + CH3O <=> OME4*-3 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 724,
    label = "COCOCOCOCO* <=> COCOCOCO* + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 725,
    label = "COCOCOCOCO* <=> COCOCOCOCHO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 726,
    label = "COCOCOCOCHO + H <=> COCOCOCOC*O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.668e+12,'cm^3/(mol*s)'), n=2.05, Ea=(37172.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 727,
    label = "COCOCOCOCHO + OH <=> COCOCOCOC*O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.915e+11,'cm^3/(mol*s)'), n=2, Ea=(6102.82,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 728,
    label = "COCOCOCOCHO + O <=> COCOCOCOC*O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.373e+13,'cm^3/(mol*s)'), n=0, Ea=(23945.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 729,
    label = "COCOCOCOCHO + CH3 <=> COCOCOCOC*O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.764e+09,'cm^3/(mol*s)'), n=3.35, Ea=(48223.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 730,
    label = "COCOCOCOCHO + H <=> COCOCOC*OCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 731,
    label = "COCOCOCOCHO + OH <=> COCOCOC*OCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 732,
    label = "COCOCOCOCHO + CH3 <=> COCOCOC*OCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 733,
    label = "COCOCOCOCHO + H <=> COCOC*OCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 734,
    label = "COCOCOCOCHO + OH <=> COCOC*OCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 735,
    label = "COCOCOCOCHO + CH3 <=> COCOC*OCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 736,
    label = "COCOCOCOCHO + H <=> COC*OCOCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 737,
    label = "COCOCOCOCHO + OH <=> COC*OCOCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 738,
    label = "COCOCOCOCHO + CH3 <=> COC*OCOCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 739,
    label = "COCOCOCOCHO + H <=> C*OCOCOCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 740,
    label = "COCOCOCOCHO + OH <=> C*OCOCOCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 741,
    label = "COCOCOCOCHO + CH3 <=> C*OCOCOCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 742,
    label = "COCOCOCOC*O <=> OME2*-1 + CO2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.0066,0.0395,0.0921,0.2632,1,10],'atm'), arrhenius=[Arrhenius(A=(6.63e+07,'s^-1'), n=-0.07, Ea=(32943.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.21e+08,'s^-1'), n=0, Ea=(32738.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.12e+08,'s^-1'), n=0, Ea=(33127.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(9.56e+08,'s^-1'), n=0.05, Ea=(33165.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.89e+09,'s^-1'), n=0.13, Ea=(33317.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.06e+10,'s^-1'), n=0.18, Ea=(35002.3,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 743,
    label = "OCOCHO + OME1*-1 <=> COCOCOC*OCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(27861.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 744,
    label = "OCOCOCHO + (C2H5O) <=> COCOCOC*OCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(27861.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 745,
    label = "(C2H3O2) + COCOCHO <=> COCOC*OCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 746,
    label = "C*OCOCHO + (C2H4O2) <=> COC*OCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 747,
    label = "COC*OCOCOCHO <=> OCOCOCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 748,
    label = "C*OCOCOCOCHO <=> C*OCOCOCHO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+13,'s^-1'), n=-0.4, Ea=(102823,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 749,
    label = "O*COCHO + HCO <=> OCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 750,
    label = "O*COCHO + (C2H3O2) <=> OCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 751,
    label = "C*OCOCHO + (CHO2) <=> OCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 752,
    label = "O*COCOCHO + HCO <=> OCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 753,
    label = "O*COCHO <=> (CHO2) + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+13,'s^-1'), n=-0.4, Ea=(102823,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 754,
    label = "OCOCOCHO + H <=> O*COCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.023e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(17449.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 755,
    label = "O*COCOCHO <=> O*COCHO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+13,'s^-1'), n=-0.4, Ea=(102823,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 756,
    label = "OME5 <=> (C2H5O) + COCOCOCOCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 757,
    label = "OME5 <=> OME1*-1 + COCOCOCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 758,
    label = "OME5 <=> OME2*-1 + COCOCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 759,
    label = "OME5 <=> OME3*-1 + COCO*",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 760,
    label = "OME5 <=> OME4*-1 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e+10,'s^-1'), n=0, Ea=(201127,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 761,
    label = "OME5 <=> CH3 + COCOCOCOCOCO*",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+19,'s^-1'), n=-0.66, Ea=(351546,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.72e+59,'cm^3/(mol*s)'), n=-11.4, Ea=(389801,'J/mol'), T0=(1,'K')), alpha=1, T3=(1e-30,'K'), T1=(880,'K'), efficiencies={'C': 3.0, 'CC': 4.5, 'O': 9.0, 'O=C=O': 3.0, '[Ar]': 1.0, '[C-]#[O+]': 2.25, '[H][H]': 3.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 762,
    label = "OME5*-1 <=> OME4*-1 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+14,'s^-1'), n=-0.22, Ea=(105289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 763,
    label = "OME5 + CH3 <=> OME5*-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.19,'cm^3/(mol*s)'), n=3.78, Ea=(40477.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 764,
    label = "OME5 + OH <=> OME5*-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.954e+06,'cm^3/(mol*s)'), n=1.89, Ea=(-1527.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 765,
    label = "OME5 + H <=> OME5*-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.3e+12,'cm^3/(mol*s)'), n=0, Ea=(14151.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 766,
    label = "OME5 + O <=> OME5*-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.689e+06,'cm^3/(mol*s)'), n=2, Ea=(10996.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 767,
    label = "OME5 + HO2 <=> OME5*-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1680,'cm^3/(mol*s)'), n=0, Ea=(73911.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 768,
    label = "OME5*-2 <=> (C2H4O2) + OME3*-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.48e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 769,
    label = "OME5*-2 <=> COCOCOCOCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 770,
    label = "OME5*-2 + H <=> OME5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 771,
    label = "OME5 + H <=> OME5*-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 772,
    label = "OME5 + CH3 <=> OME5*-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 773,
    label = "OME5 + HO2 <=> OME5*-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 774,
    label = "OME5 + OH <=> OME5*-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 775,
    label = "OME5 + O <=> OME5*-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 776,
    label = "OME5 + CH3O <=> OME5*-2 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 777,
    label = "OME5*-3 <=> COCOCOCOCHO + (C2H5O)",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.967e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 778,
    label = "OME5*-3 <=> COCOCHO + OME2*-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.967e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 779,
    label = "OME5*-3 + H <=> OME5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 780,
    label = "OME5 + H <=> OME5*-3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 781,
    label = "OME5 + CH3 <=> OME5*-3 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 782,
    label = "OME5 + HO2 <=> OME5*-3 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 783,
    label = "OME5 + OH <=> OME5*-3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 784,
    label = "OME5 + O <=> OME5*-3 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 785,
    label = "OME5 + CH3O <=> OME5*-3 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 786,
    label = "OME5*-4 <=> OME1*-1 + COCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.967e+11,'s^-1'), n=0.544, Ea=(53503.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 787,
    label = "OME5*-4 + H <=> OME5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.2e+06,'cm^3/(mol*s)'), n=-0.09, Ea=(2372.95,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 788,
    label = "OME5 + H <=> OME5*-4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0176,'cm^3/(mol*s)'), n=2.68, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 789,
    label = "OME5 + CH3 <=> OME5*-4 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.993e+11,'cm^3/(mol*s)'), n=0, Ea=(40807.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 790,
    label = "OME5 + HO2 <=> OME5*-4 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29500,'cm^3/(mol*s)'), n=2.6, Ea=(58075.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 791,
    label = "OME5 + OH <=> OME5*-4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2260,'cm^3/(mol*s)'), n=2.93, Ea=(16879.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 792,
    label = "OME5 + O <=> OME5*-4 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(12693.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 793,
    label = "OME5 + CH3O <=> OME5*-4 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+10,'cm^3/(mol*s)'), n=0, Ea=(19018.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 794,
    label = "COCOCOCOCOCO* <=> COCOCOCOCO* + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 795,
    label = "COCOCOCOCOCO* <=> COCOCOCOCOCHO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43e+15,'s^-1'), n=-0.69, Ea=(93005.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 796,
    label = "COCOCOCOCOCHO + H <=> COCOCOCOCOC*O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.668e+12,'cm^3/(mol*s)'), n=2.05, Ea=(37172.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 797,
    label = "COCOCOCOCOCHO + OH <=> COCOCOCOCOC*O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.915e+11,'cm^3/(mol*s)'), n=2, Ea=(6102.82,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 798,
    label = "COCOCOCOCOCHO + O <=> COCOCOCOCOC*O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.373e+13,'cm^3/(mol*s)'), n=0, Ea=(23945.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 799,
    label = "COCOCOCOCOCHO + CH3 <=> COCOCOCOCOC*O + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.764e+09,'cm^3/(mol*s)'), n=3.35, Ea=(48223.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 800,
    label = "COCOCOCOCOCHO + H <=> COCOCOCOC*OCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 801,
    label = "COCOCOCOCOCHO + OH <=> COCOCOCOC*OCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 802,
    label = "COCOCOCOCOCHO + CH3 <=> COCOCOCOC*OCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 803,
    label = "COCOCOCOCOCHO + H <=> COCOCOC*OCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 804,
    label = "COCOCOCOCOCHO + OH <=> COCOCOC*OCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 805,
    label = "COCOCOCOCOCHO + CH3 <=> COCOCOC*OCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 806,
    label = "COCOCOCOCOCHO + H <=> COCOC*OCOCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 807,
    label = "COCOCOCOCOCHO + OH <=> COCOC*OCOCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 808,
    label = "COCOCOCOCOCHO + CH3 <=> COCOC*OCOCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 809,
    label = "COCOCOCOCOCHO + H <=> COC*OCOCOCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 810,
    label = "COCOCOCOCOCHO + OH <=> COC*OCOCOCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 811,
    label = "COCOCOCOCOCHO + CH3 <=> COC*OCOCOCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 812,
    label = "COCOCOCOCOCHO + H <=> C*OCOCOCOCOCHO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(650000,'cm^3/(mol*s)'), n=2.4, Ea=(18680.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 813,
    label = "COCOCOCOCOCHO + OH <=> C*OCOCOCOCOCHO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.986e+10,'cm^3/(mol*s)'), n=1.87, Ea=(109.751,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 814,
    label = "COCOCOCOCOCHO + CH3 <=> C*OCOCOCOCOCHO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+10,'cm^3/(mol*s)'), n=3.32, Ea=(41871.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 815,
    label = "COCOCOCOCOC*O <=> OME3*-1 + CO2",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.0066,0.0395,0.0921,0.2632,1,10],'atm'), arrhenius=[Arrhenius(A=(6.63e+07,'s^-1'), n=-0.07, Ea=(32943.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.21e+08,'s^-1'), n=0, Ea=(32738.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.12e+08,'s^-1'), n=0, Ea=(33127.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(9.56e+08,'s^-1'), n=0.05, Ea=(33165.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.89e+09,'s^-1'), n=0.13, Ea=(33317.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.06e+10,'s^-1'), n=0.18, Ea=(35002.3,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 816,
    label = "OCOCHO + OME2*-1 <=> COCOCOCOC*OCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+07,'cm^3/(mol*s)'), n=-0.67, Ea=(27861.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 817,
    label = "(C2H3O2) + COCOCOCHO <=> COCOCOC*OCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 818,
    label = "OME1*-1 + OCOCOCHO <=> COCOCOC*OCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 819,
    label = "COCOCHO + C*OCOCHO <=> COCOC*OCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 820,
    label = "(C2H5O) + OCOCOCOCHO <=> COCOC*OCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 821,
    label = "(C2H4O2) + C*OCOCOCHO <=> COC*OCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.5e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 822,
    label = "COC*OCOCOCOCHO <=> OCOCOCOCOCHO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.37e+29,'s^-1'), n=-15.95, Ea=(478082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 823,
    label = "C*OCOCOCOCOCHO <=> C*OCOCOCOCHO + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+13,'s^-1'), n=-0.4, Ea=(102823,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 824,
    label = "C*OCOCHO + O*COCHO <=> OCOCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 825,
    label = "O*COCOCHO + (C2H3O2) <=> OCOCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 826,
    label = "C*OCOCOCHO + (CHO2) <=> OCOCOCOCOCHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.54e+06,'cm^3/(mol*s)'), n=0.02, Ea=(7025.73,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 827,
    label = "C5H8 + OH <=> CH3CHO + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 828,
    label = "C5H9 + C3H5 <=> C5H8 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 829,
    label = "C5H9 <=> C3H5 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(125549,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 830,
    label = "C5H9 <=> C4H6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(266063,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 831,
    label = "C5H9 + CH3 <=> C5H8 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 832,
    label = "C5H9 + H <=> C5H8 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 833,
    label = "iC5H9 <=> C4H6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-3, Ea=(187076,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 834,
    label = "iC5H9 <=> C3H5 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(125549,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 835,
    label = "iC5H9 <=> C3H4 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.983e+20,'s^-1'), n=-1.63, Ea=(247505,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 836,
    label = "C5H9 + H <=> C5H10",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24373.9,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 837,
    label = "C5H10 <=> C2H5 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.24e+22,'s^-1'), n=-1.94, Ea=(315323,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 838,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62e+06,'s^-1'), n=1.81, Ea=(223338,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 839,
    label = "C5H10 + H <=> nC3H7 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+21,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 840,
    label = "C5H10 + H <=> C3H6 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+22,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 841,
    label = "C5H10 + H <=> C5H9 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(54000,'cm^3/(mol*s)'), n=2.5, Ea=(-7938.66,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 842,
    label = "C5H10 + O <=> pC4H9 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+08,'cm^3/(mol*s)'), n=1.45, Ea=(-1679.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 843,
    label = "C5H10 + O <=> C5H9 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.745,'cm^3/(mol*s)'), n=4.17, Ea=(11557.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 844,
    label = "C5H10 + OH <=> C5H9 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(700,'cm^3/(mol*s)'), n=2.66, Ea=(2201.67,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 845,
    label = "C5H10 + O2 <=> C5H9 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(212792,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 846,
    label = "C5H10 + HO2 <=> C5H9 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(59914.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 847,
    label = "C5H10 + CH3 <=> C5H9 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e-08,'cm^3/(mol*s)'), n=6.08, Ea=(26000.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 848,
    label = "iC5H10 <=> iC4H7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.56e+16,'s^-1'), n=-0.65, Ea=(307261,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 849,
    label = "iC5H10 <=> C3H5 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.922e+24,'s^-1'), n=-2.41, Ea=(419902,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 850,
    label = "nC4H7 + CH3 <=> iC5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 851,
    label = "iC5H10 + H <=> iC5H9 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(173000,'cm^3/(mol*s)'), n=2.5, Ea=(10411.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 852,
    label = "iC5H10 + O <=> iC5H9 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(370000,'cm^3/(mol*s)'), n=2.56, Ea=(-4721.29,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 853,
    label = "iC5H10 + OH <=> iC5H9 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.12e+06,'cm^3/(mol*s)'), n=2, Ea=(-1245.09,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 854,
    label = "iC5H10 + HO2 <=> iC5H9 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9639,'cm^3/(mol*s)'), n=2.6, Ea=(58117.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 855,
    label = "iC5H10 + CH3 <=> iC5H9 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.21,'cm^3/(mol*s)'), n=3.5, Ea=(23710.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 856,
    label = "C5H11 <=> C3H6 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1917,'s^-1'), n=0.27, Ea=(122007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 857,
    label = "C5H11 <=> C4H8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+16,'s^-1'), n=0, Ea=(215012,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 858,
    label = "C5H11 <=> nC3H7 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.04e+13,'s^-1'), n=0.32, Ea=(121009,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 859,
    label = "C5H11 + O2 <=> C5H10 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.903e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 860,
    label = "iC5H11 <=> iC5H10 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.55e+16,'s^-1'), n=-0.92, Ea=(151955,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 861,
    label = "iC5H11 <=> iC4H8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+13,'s^-1'), n=1.09, Ea=(125008,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 862,
    label = "iC5H11 + O2 <=> iC4H8 + CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.198e+16,'cm^3/(mol*s)'), n=-6.64, Ea=(76044.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 863,
    label = "iC5H11 <=> C3H6 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.028e+18,'s^-1'), n=-1.19, Ea=(131369,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 864,
    label = "iC5H11 <=> C4H8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.094e+16,'s^-1'), n=-0.86, Ea=(124509,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 865,
    label = "C6H10 + H <=> C4H8 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.46e+30,'cm^3/(mol*s)'), n=-4.34, Ea=(90444,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 866,
    label = "C6H10 + H <=> nC4H7 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+22,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 867,
    label = "C6H10 + H <=> C4H6 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(8356.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 868,
    label = "C6H11 <=> C6H10 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([1,10],'atm'), arrhenius=[Arrhenius(A=(2.48e+53,'s^-1'), n=-12.3, Ea=(217263,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.85e+48,'s^-1'), n=-10.5, Ea=(430440,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 869,
    label = "C6H11 <=> C5H8 + CH3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(8.13e+10,'s^-1'), n=0.8, Ea=(123873,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4e-39,'cm^3/(mol*s)'), n=16.8, Ea=(-2508.48,'J/mol'), T0=(1,'K')), alpha=-7.03, T3=(314,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 870,
    label = "C6H11 <=> C4H6 + C2H5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.39e+11,'s^-1'), n=0.66, Ea=(134798,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4e-42,'cm^3/(mol*s)'), n=18.05, Ea=(-2517.62,'J/mol'), T0=(1,'K')), alpha=-18.5, T3=(246,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 871,
    label = "C6H11 <=> C3H6 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-2.99, Ea=(224491,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 872,
    label = "C4H8 + C2H3 <=> C6H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.23e+10,'cm^3/(mol*s)'), n=0, Ea=(35918.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 873,
    label = "C6H11 + H <=> CH3 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+21,'cm^3/(mol*s)'), n=-2, Ea=(45959.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 874,
    label = "C6H11 + H <=> C6H10 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 875,
    label = "C6H11 + HO2 <=> C6H10 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 876,
    label = "C6H11 + HCO <=> C6H12 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 877,
    label = "C6H11 + CH3 <=> C6H10 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 878,
    label = "tC4H9 + C2H2 <=> iC6H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.23e+10,'cm^3/(mol*s)'), n=0, Ea=(35918.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 879,
    label = "iC6H11 => C3H6 + C3H5",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-3, Ea=(187076,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 880,
    label = "iC6H11 => C5H8 + CH3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-3, Ea=(187076,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 881,
    label = "C6H11 + H <=> C6H12",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24373.9,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 882,
    label = "C6H12 <=> C3H5 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+23,'s^-1'), n=-2.03, Ea=(313184,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 883,
    label = "C6H12 <=> C3H6 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.08e+06,'s^-1'), n=1.65, Ea=(224583,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 884,
    label = "C6H12 + H <=> C2H4 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+21,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 885,
    label = "C6H12 + H <=> C3H6 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+22,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 886,
    label = "C6H12 + H <=> C6H11 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0317,'cm^3/(mol*s)'), n=4.65, Ea=(5598.97,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 887,
    label = "C6H12 + O <=> C5H11 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+08,'cm^3/(mol*s)'), n=1.45, Ea=(-1679.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 888,
    label = "C6H12 + O <=> C6H11 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.745,'cm^3/(mol*s)'), n=4.17, Ea=(11557.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 889,
    label = "C6H12 + OH <=> C6H11 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(700,'cm^3/(mol*s)'), n=2.66, Ea=(2201.67,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 890,
    label = "C6H12 + O2 <=> C6H11 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(212792,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 891,
    label = "C6H12 + HO2 <=> C6H11 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(59914.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 892,
    label = "C6H12 + CH3 <=> C6H11 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e-08,'cm^3/(mol*s)'), n=6.08, Ea=(26000.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 893,
    label = "iC6H12 => iC4H7 + C2H5",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(296647,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 894,
    label = "iC4H7 + C2H5 => iC6H12",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 895,
    label = "iC6H12 => C5H9 + CH3",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(296647,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 896,
    label = "C5H9 + CH3 => iC6H12",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 897,
    label = "iC6H12 => iC3H7 + C3H5",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(296647,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 898,
    label = "iC3H7 + C3H5 => iC6H12",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 899,
    label = "iC6H12 + H <=> iC6H11 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(16213.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 900,
    label = "iC6H12 + OH <=> iC6H11 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(5113.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 901,
    label = "iC6H12 + O <=> iC6H11 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(16628.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 902,
    label = "iC6H12 + CH3 <=> iC6H11 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(30347.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 903,
    label = "C6H13 <=> C5H10 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+10,'s^-1'), n=1.08, Ea=(122971,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 904,
    label = "C6H13 <=> C6H12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(166289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 905,
    label = "C6H13 <=> nC3H7 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+10,'s^-1'), n=0.84, Ea=(116411,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 906,
    label = "C6H13 <=> C4H8 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.04e+13,'s^-1'), n=0.04, Ea=(119230,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 907,
    label = "C6H13 <=> pC4H9 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.04e+13,'s^-1'), n=0.04, Ea=(119230,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 908,
    label = "C6H13 + O2 <=> C6H12 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 909,
    label = "iC6H13 <=> C6H12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(166289,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 910,
    label = "iC6H13 <=> C5H10 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.29e+11,'s^-1'), n=0, Ea=(97861.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 911,
    label = "iC6H13 <=> C3H6 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.88e+12,'s^-1'), n=0, Ea=(88258.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 912,
    label = "iC6H13 <=> C3H6 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.79e+11,'s^-1'), n=0, Ea=(94452.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 913,
    label = "iC6H13 <=> tC4H9 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'s^-1'), n=0, Ea=(92623.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 914,
    label = "iC6H13 <=> iC4H8 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+12,'s^-1'), n=0, Ea=(87967.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 915,
    label = "iC6H13 + O2 <=> C6H12 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(8314.47,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 916,
    label = "C5H11 + CH3 <=> N-C6H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(-2493.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 917,
    label = "pC4H9 + C2H5 <=> N-C6H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(-2493.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 918,
    label = "nC3H7 + nC3H7 <=> N-C6H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(-2493.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 919,
    label = "C6H13 + H <=> N-C6H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.61e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 920,
    label = "N-C6H14 + H <=> C6H13 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+06,'cm^3/(mol*s)'), n=2.4, Ea=(18706.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 921,
    label = "N-C6H14 + OH <=> C6H13 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.36e+07,'cm^3/(mol*s)'), n=1.61, Ea=(-146.335,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 922,
    label = "N-C6H14 + O <=> C6H13 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.189e+06,'cm^3/(mol*s)'), n=2.44, Ea=(11908,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 923,
    label = "N-C6H14 + HO2 <=> C6H13 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+13,'cm^3/(mol*s)'), n=0, Ea=(74015.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 924,
    label = "N-C6H14 + CH3 <=> C6H13 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(168000,'cm^3/(mol*s)'), n=2.13, Ea=(31689.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 925,
    label = "C7H13 <=> C3H4 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-2.99, Ea=(224491,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 926,
    label = "C7H13 <=> nC3H7 + C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-2.99, Ea=(224491,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 927,
    label = "C7H13 <=> C2H5 + C5H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+23,'s^-1'), n=-2.99, Ea=(224491,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 928,
    label = "C7H13 <=> C6H10 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.5e+24,'s^-1'), n=-2.99, Ea=(224491,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 929,
    label = "C7H13 + H <=> C7H14",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24373.9,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 930,
    label = "C7H14 <=> pC4H9 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+23,'s^-1'), n=-2.03, Ea=(313184,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 931,
    label = "C7H14 <=> C4H8 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.08e+06,'s^-1'), n=1.65, Ea=(224583,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 932,
    label = "C7H14 + H <=> C2H4 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+21,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 933,
    label = "C7H14 + H <=> C3H6 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+22,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 934,
    label = "C7H14 + H <=> C7H13 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0323,'cm^3/(mol*s)'), n=4.7, Ea=(15371,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 935,
    label = "C7H14 + O <=> C6H13 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+08,'cm^3/(mol*s)'), n=1.45, Ea=(-1679.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 936,
    label = "C7H14 + O <=> C7H13 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.745,'cm^3/(mol*s)'), n=4.17, Ea=(11556.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 937,
    label = "C7H14 + OH <=> C7H13 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(700,'cm^3/(mol*s)'), n=2.66, Ea=(2201.67,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 938,
    label = "C7H14 + O2 <=> C7H13 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(212792,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 939,
    label = "C7H14 + HO2 <=> C7H13 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(59914.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 940,
    label = "C7H14 + CH3 <=> C7H13 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e-08,'cm^3/(mol*s)'), n=6.08, Ea=(26000.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 941,
    label = "C7H14 + H <=> C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.56e+09,'cm^3/(mol*s)'), n=1.6, Ea=(2422.84,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 942,
    label = "C7H15 <=> C6H12 + CH3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.1e+11,'s^-1'), n=0.75, Ea=(122846,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.06e-42,'cm^3/(mol*s)'), n=18, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-20.94, T3=(217,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 943,
    label = "C7H15 <=> pC4H9 + C3H6",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(5.01e+11,'s^-1'), n=0.56, Ea=(117375,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(8.9e-39,'cm^3/(mol*s)'), n=16.934, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-25.27, T3=(223,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 944,
    label = "C7H15 <=> nC3H7 + C4H8",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.95e+12,'s^-1'), n=0.31, Ea=(118066,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2e-38,'cm^3/(mol*s)'), n=16.814, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-20.96, T3=(221,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 945,
    label = "C7H15 <=> C2H4 + C5H11",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(7.94e+11,'s^-1'), n=0.33, Ea=(113684,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.8e-44,'cm^3/(mol*s)'), n=18.729, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-14.66, T3=(219,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 946,
    label = "C7H15 <=> C2H5 + C5H10",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(5.89e+12,'s^-1'), n=0.31, Ea=(118066,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(2.1e-38,'cm^3/(mol*s)'), n=16.897, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-27.54, T3=(224,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 947,
    label = "C7H15 + O2 <=> C7H14 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07,'cm^3/(mol*s)'), n=3.7, Ea=(38948.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 948,
    label = "N-C7H16 <=> C6H13 + CH3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.1,1,2,5,10,20,50],'atm'), arrhenius=[Arrhenius(A=(3.21e+84,'s^-1'), n=-20.2, Ea=(503824,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.98e+69,'s^-1'), n=-15.58, Ea=(476962,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.48e+51,'s^-1'), n=-10.36, Ea=(440044,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.58e+46,'s^-1'), n=-8.84, Ea=(428392,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.36e+40,'s^-1'), n=-6.96, Ea=(413593,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.73e+35,'s^-1'), n=-5.68, Ea=(403293,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.09e+31,'s^-1'), n=-4.56, Ea=(394098,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.41e+27,'s^-1'), n=-3.35, Ea=(383982,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 949,
    label = "N-C7H16 <=> C5H11 + C2H5",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.1,1,2,5,10,20,50],'atm'), arrhenius=[Arrhenius(A=(5.31e+77,'s^-1'), n=-18.03, Ea=(488565,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.48e+61,'s^-1'), n=-13.11, Ea=(457463,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.62e+43,'s^-1'), n=-7.87, Ea=(418991,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.04e+38,'s^-1'), n=-6.39, Ea=(407405,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.82e+32,'s^-1'), n=-4.59, Ea=(393003,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.11e+28,'s^-1'), n=-3.39, Ea=(383180,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.56e+24,'s^-1'), n=-2.35, Ea=(374548,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.45e+20,'s^-1'), n=-1.24, Ea=(365226,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 950,
    label = "N-C7H16 <=> pC4H9 + nC3H7",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.1,1,2,5,10,20,50],'atm'), arrhenius=[Arrhenius(A=(8.03e+87,'s^-1'), n=-20.87, Ea=(501726,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.26e+72,'s^-1'), n=-16.19, Ea=(474201,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.14e+54,'s^-1'), n=-10.97, Ea=(436999,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.51e+49,'s^-1'), n=-9.45, Ea=(425346,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.27e+43,'s^-1'), n=-7.58, Ea=(410593,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.04e+39,'s^-1'), n=-6.31, Ea=(400361,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.6e+35,'s^-1'), n=-5.2, Ea=(391240,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.21e+31,'s^-1'), n=-4.01, Ea=(381238,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 951,
    label = "N-C7H16 <=> C7H15 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.1,1,2,5,10,20,50],'atm'), arrhenius=[Arrhenius(A=(1.12e+104,'s^-1'), n=-27.26, Ea=(562159,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.21e+112,'s^-1'), n=-29.16, Ea=(591710,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.82e+118,'s^-1'), n=-30.48, Ea=(624137,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.58e+118,'s^-1'), n=-30.39, Ea=(630024,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.04e+117,'s^-1'), n=-29.83, Ea=(633387,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.16e+114,'s^-1'), n=-29.08, Ea=(632439,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.15e+111,'s^-1'), n=-28.11, Ea=(628729,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.42e+106,'s^-1'), n=-26.58, Ea=(620472,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 952,
    label = "N-C7H16 + H <=> C7H15 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+06,'cm^3/(mol*s)'), n=2.4, Ea=(18680.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 953,
    label = "N-C7H16 + O <=> C7H15 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.62e+13,'cm^3/(mol*s)'), n=0, Ea=(21726.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 954,
    label = "N-C7H16 + OH <=> C7H15 + H2O",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(1.41e+10,'cm^3/(mol*s)'), n=0.935, Ea=(2108.55,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.144e+07,'cm^3/(mol*s)'), n=1.811, Ea=(-4242.88,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 955,
    label = "N-C7H16 + O2 <=> C7H15 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+13,'cm^3/(mol*s)'), n=0, Ea=(209575,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 956,
    label = "N-C7H16 + HO2 <=> C7H15 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1260,'cm^3/(mol*s)'), n=3.4, Ea=(57324.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 957,
    label = "N-C7H16 + CH3 <=> C7H15 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(168000,'cm^3/(mol*s)'), n=2.1, Ea=(31644.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 958,
    label = "N-C7H16 + C2H3 <=> C7H15 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+11,'cm^3/(mol*s)'), n=0, Ea=(70192.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 959,
    label = "N-C7H16 + C2H5 <=> C7H15 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(43452.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 960,
    label = "tC4H9 + iC4H9 <=> I-C8H18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.59e+14,'cm^3/(mol*s)'), n=-0.75, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 961,
    label = "iC5H11 + iC3H7 <=> I-C8H18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.59e+14,'cm^3/(mol*s)'), n=-0.75, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 962,
    label = "I-C8H18 <=> p-iC8H17 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.748e+17,'s^-1'), n=-0.36, Ea=(422827,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 963,
    label = "I-C8H18 <=> s-iC8H17 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(1.146e+19,'s^-1'), n=-0.94, Ea=(398719,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.299e+18,'s^-1'), n=-0.72, Ea=(412507,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 964,
    label = "I-C8H18 + H <=> p-iC8H17 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.998e+06,'cm^3/(mol*s)'), n=2.54, Ea=(28227.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 965,
    label = "I-C8H18 + H <=> s-iC8H17 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(602000,'cm^3/(mol*s)'), n=2.4, Ea=(10792.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 966,
    label = "I-C8H18 + O <=> p-iC8H17 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.943e+06,'cm^3/(mol*s)'), n=2.43, Ea=(19846.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 967,
    label = "I-C8H18 + O <=> s-iC8H17 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(383000,'cm^3/(mol*s)'), n=2.41, Ea=(4763.03,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 968,
    label = "I-C8H18 + OH <=> p-iC8H17 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.93e+07,'cm^3/(mol*s)'), n=1.76, Ea=(3104.96,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 969,
    label = "I-C8H18 + OH <=> s-iC8H17 + H2O",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(36.14,'cm^3/(mol*s)'), n=3.5, Ea=(-9754.79,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.409e+09,'cm^3/(mol*s)'), n=1, Ea=(-41.5724,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 970,
    label = "I-C8H18 + HO2 <=> p-iC8H17 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(61.2,'cm^3/(mol*s)'), n=3.59, Ea=(71696.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 971,
    label = "I-C8H18 + HO2 <=> s-iC8H17 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(433.2,'cm^3/(mol*s)'), n=3.01, Ea=(50513.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 972,
    label = "I-C8H18 + O2 <=> p-iC8H17 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(218474,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 973,
    label = "I-C8H18 + O2 <=> s-iC8H17 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(201386,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 974,
    label = "I-C8H18 + CH3 <=> p-iC8H17 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.359,'cm^3/(mol*s)'), n=3.65, Ea=(29890.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 975,
    label = "I-C8H18 + CH3 <=> s-iC8H17 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.01e-10,'cm^3/(mol*s)'), n=6.36, Ea=(3731.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 976,
    label = "I-C8H18 + CH3O <=> p-iC8H17 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.507e+11,'cm^3/(mol*s)'), n=0, Ea=(26982.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 977,
    label = "I-C8H18 + CH3O <=> s-iC8H17 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.45e+11,'cm^3/(mol*s)'), n=0, Ea=(19098.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 978,
    label = "I-C8H18 + C2H5 <=> p-iC8H17 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(55986.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 979,
    label = "I-C8H18 + C2H5 <=> s-iC8H17 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(33007.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 980,
    label = "I-C8H18 + C2H3 <=> p-iC8H17 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+12,'cm^3/(mol*s)'), n=0, Ea=(75206.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 981,
    label = "I-C8H18 + C2H3 <=> s-iC8H17 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(59747.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 982,
    label = "s-iC8H17 <=> iC7H14 + CH3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.417,'s^-1'), n=3.5, Ea=(82881.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.95e+13,'s^-1'), n=-0.59, Ea=(115028,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.04e+21,'s^-1'), n=-2.73, Ea=(134916,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.01e+21,'s^-1'), n=-2.52, Ea=(137915,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.05e+16,'s^-1'), n=-1.03, Ea=(130370,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 983,
    label = "s-iC8H17 <=> iC4H8 + tC4H9",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(1610,'s^-1'), n=2.4, Ea=(77904.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.36e+16,'s^-1'), n=-1.34, Ea=(108623,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.77e+22,'s^-1'), n=-3.06, Ea=(126000,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.38e+21,'s^-1'), n=-2.49, Ea=(126580,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.23e+16,'s^-1'), n=-0.94, Ea=(118534,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 984,
    label = "s-iC8H17 <=> iC8H16 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(23020,'s^-1'), n=1.061, Ea=(145498,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 985,
    label = "s-iC8H17 + O2 <=> iC8H16 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+11,'cm^3/(mol*s)'), n=0, Ea=(10445.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 986,
    label = "p-iC8H17 <=> iC4H8 + iC4H9",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.000971,'s^-1'), n=4.4, Ea=(79726.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.72e+15,'s^-1'), n=-1.01, Ea=(120000,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.47e+25,'s^-1'), n=-3.85, Ea=(144952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.66e+25,'s^-1'), n=-3.57, Ea=(147793,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.99e+19,'s^-1'), n=-1.87, Ea=(138889,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 987,
    label = "p-iC8H17 <=> iC3H7 + iC5H10",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.000971,'s^-1'), n=4.4, Ea=(79726.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.72e+15,'s^-1'), n=-1.01, Ea=(120000,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.47e+25,'s^-1'), n=-3.85, Ea=(144952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.66e+25,'s^-1'), n=-3.57, Ea=(147793,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.99e+19,'s^-1'), n=-1.87, Ea=(138889,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 988,
    label = "p-iC8H17 <=> iC5H11 + C3H6",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.000971,'s^-1'), n=4.4, Ea=(79726.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.72e+15,'s^-1'), n=-1.01, Ea=(120000,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.47e+25,'s^-1'), n=-3.85, Ea=(144952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.66e+25,'s^-1'), n=-3.57, Ea=(147793,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.99e+19,'s^-1'), n=-1.87, Ea=(138889,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 989,
    label = "p-iC8H17 <=> iC4H8 + tC4H9",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.000971,'s^-1'), n=4.4, Ea=(79726.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.72e+15,'s^-1'), n=-1.01, Ea=(120000,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.47e+25,'s^-1'), n=-3.85, Ea=(144952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.66e+25,'s^-1'), n=-3.57, Ea=(147793,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.99e+19,'s^-1'), n=-1.87, Ea=(138889,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 990,
    label = "p-iC8H17 <=> iC7H14 + CH3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.00224,'s^-1'), n=4.1, Ea=(78595,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.72e+15,'s^-1'), n=-1.11, Ea=(117639,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.84e+24,'s^-1'), n=-3.76, Ea=(141162,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.73e+24,'s^-1'), n=-3.42, Ea=(143444,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.09e+18,'s^-1'), n=-1.76, Ea=(134724,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 991,
    label = "p-iC8H17 <=> s-iC8H17",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(12,'s^-1'), n=2.59, Ea=(49923.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.48e+10,'s^-1'), n=-0.09, Ea=(72002.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.02e+14,'s^-1'), n=-1.01, Ea=(82060.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.82e+11,'s^-1'), n=-0.27, Ea=(79952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.56e+07,'s^-1'), n=1.07, Ea=(72592.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 992,
    label = "p-iC8H17 + O2 <=> iC8H16 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(212077,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 993,
    label = "iC8H16 <=> iC7H13 + CH3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([4,10,15,30],'atm'), arrhenius=[Arrhenius(A=(7.05e+64,'s^-1'), n=-14.79, Ea=(418235,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.09e+56,'s^-1'), n=-11.79, Ea=(780579,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.06e+52,'s^-1'), n=-10.51, Ea=(757872,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.09e+44,'s^-1'), n=-8.42, Ea=(720599,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 994,
    label = "iC8H16 + H <=> iC4H8 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(10445.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 995,
    label = "iC8H16 + O <=> iC8H15 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.7e+13,'cm^3/(mol*s)'), n=0, Ea=(16294.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 996,
    label = "iC8H16 + H <=> iC8H15 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.7e+13,'cm^3/(mol*s)'), n=0, Ea=(16294.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 997,
    label = "iC8H16 + OH <=> iC8H15 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.7e+13,'cm^3/(mol*s)'), n=0, Ea=(16294.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 998,
    label = "iC8H16 + CH3 <=> iC8H15 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(30500,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 999,
    label = "iC8H16 + HO2 <=> iC8H15 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e-19,'cm^3/(mol*s)'), n=0, Ea=(73117.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1000,
    label = "iC8H16 + O => iC6H12 + C2H3 + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(-4387.05,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1001,
    label = "iC8H16 + O => iC5H10 + C3H5 + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(-4387.05,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1002,
    label = "iC8H16 + O => iC6H11 + C2H4 + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(-4387.05,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1003,
    label = "iC8H16 + OH => iC6H12 + C2H3 + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(-16712.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1004,
    label = "iC8H16 + OH => iC5H10 + C3H5 + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(-16712.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1005,
    label = "iC8H16 + OH => iC6H11 + C2H4 + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(-16712.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1006,
    label = "iC8H15 <=> iC4H7 + iC4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.986e+24,'s^-1'), n=-3, Ea=(223948,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1007,
    label = "iC8H15 <=> C3H5 + iC4H7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.986e+24,'s^-1'), n=-3, Ea=(223948,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1008,
    label = "iC7H14 => iC4H7 + iC3H7",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.211e+24,'s^-1'), n=-2.39, Ea=(311981,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1009,
    label = "iC7H14 => iC6H11 + CH3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.469e+22,'s^-1'), n=-2.13, Ea=(315156,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1010,
    label = "iC7H14 + H <=> iC7H13 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(16213.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1011,
    label = "iC7H14 + OH <=> iC7H13 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(5113.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1012,
    label = "iC7H14 + O <=> iC7H13 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(16628.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1013,
    label = "iC7H14 + CH3 <=> iC7H13 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(30514.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1014,
    label = "iC7H13 => C3H4 + C3H5 + H + CH3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.986e+24,'s^-1'), n=-3, Ea=(223948,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1015,
    label = "iC7H13 => C3H3 + tC4H9 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.986e+24,'s^-1'), n=-3, Ea=(223948,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1016,
    label = "iC7H13 => iC4H7 + C3H5 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.986e+24,'s^-1'), n=-3, Ea=(223948,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1017,
    label = "iC7H15 <=> iC4H9 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.429e+20,'s^-1'), n=-2.22, Ea=(135455,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1018,
    label = "iC7H15 <=> iC4H8 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.49e+12,'s^-1'), n=-0.13, Ea=(109086,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1019,
    label = "iC7H15 <=> iC7H14 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.75e+12,'s^-1'), n=0.69, Ea=(143732,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1020,
    label = "iC7H15 <=> iC6H12 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.009e+19,'s^-1'), n=-1.8, Ea=(139257,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1021,
    label = "C8H16 <=> pC4H9 + nC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1022,
    label = "C8H16 <=> C3H5 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1023,
    label = "C8H16 <=> CH3 + C7H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1024,
    label = "C8H16 + OH => C4H8 + nC4H7 + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+09,'cm^3/(mol*s)'), n=1.25, Ea=(2494.34,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1025,
    label = "C8H16 + OH <=> C7H15 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1026,
    label = "C8H16 + OH <=> nC8H15 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(5113.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1027,
    label = "C8H16 + H <=> nC8H15 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(15381.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1028,
    label = "C8H16 + O <=> nC8H15 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(16628.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1029,
    label = "C8H16 + CH3 <=> nC8H15 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(30347.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1030,
    label = "C8H16 + HO2 <=> nC8H15 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(71088.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1031,
    label = "C8H16 + O2 <=> nC8H15 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(167121,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1032,
    label = "C8H16 <=> C2H3 + C6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1033,
    label = "C8H16 <=> nC3H7 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1034,
    label = "C8H16 <=> nC8H15 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+17,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1035,
    label = "nC8H17 <=> C2H4 + C6H13",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(9.12e+11,'s^-1'), n=0.31, Ea=(113963,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.8e-57,'cm^3/(mol*s)'), n=23.46, Ea=(-2520.12,'J/mol'), T0=(1,'K')), alpha=-2.46, T3=(206,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1036,
    label = "nC8H17 + H <=> C6H13 + C2H5",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10],'atm'), arrhenius=[Arrhenius(A=(3.4e+18,'cm^3/(mol*s)'), n=-1.33, Ea=(22534.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.7e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(52321.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.1e+27,'cm^3/(mol*s)'), n=-3.59, Ea=(79743.3,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1037,
    label = "nC8H17 + H <=> C8H16 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1038,
    label = "nC8H17 + O <=> C7H15 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1039,
    label = "nC8H17 + OH <=> C8H16 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1040,
    label = "nC8H17 + O2 <=> C8H16 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1041,
    label = "nC8H17 + HO2 <=> C7H15 + OH + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1042,
    label = "nC8H17 + CH3 <=> C8H16 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1043,
    label = "nC8H17 + CH3 <=> N-C9H20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.93e+14,'cm^3/(mol*s)'), n=-0.32, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1044,
    label = "C7H15 + C2H5 <=> N-C9H20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1045,
    label = "C6H13 + nC3H7 <=> N-C9H20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1046,
    label = "C5H11 + pC4H9 <=> N-C9H20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1047,
    label = "pC9H19 + H <=> N-C9H20",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24416.3,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1048,
    label = "sC9H19 + H <=> N-C9H20",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.7e+58,'cm^6/(mol^2*s)'), n=-12.08, Ea=(47127.3,'J/mol'), T0=(1,'K')), alpha=0.649, T3=(1213.1,'K'), T1=(1213.1,'K'), T2=(13369.7,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1049,
    label = "N-C9H20 + OH <=> pC9H19 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.73e+07,'cm^3/(mol*s)'), n=1.81, Ea=(3632.59,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1050,
    label = "N-C9H20 + O2 <=> pC9H19 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(213092,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1051,
    label = "N-C9H20 + HO2 <=> pC9H19 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(61100,'cm^3/(mol*s)'), n=2.65, Ea=(73203.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1052,
    label = "N-C9H20 + H <=> pC9H19 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0645,'cm^3/(mol*s)'), n=4.7, Ea=(15392.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1053,
    label = "N-C9H20 + O <=> pC9H19 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.49,'cm^3/(mol*s)'), n=4.17, Ea=(11572.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1054,
    label = "N-C9H20 + CH3 <=> pC9H19 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.16e-08,'cm^3/(mol*s)'), n=6.08, Ea=(26036.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1055,
    label = "N-C9H20 + OH <=> sC9H19 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+10,'cm^3/(mol*s)'), n=0.94, Ea=(2111.63,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1056,
    label = "N-C9H20 + O2 <=> sC9H19 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+13,'cm^3/(mol*s)'), n=0, Ea=(199117,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1057,
    label = "N-C9H20 + HO2 <=> sC9H19 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(14200,'cm^3/(mol*s)'), n=2.77, Ea=(62396,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1058,
    label = "N-C9H20 + H <=> sC9H19 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0634,'cm^3/(mol*s)'), n=4.65, Ea=(5606.45,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1059,
    label = "N-C9H20 + O <=> sC9H19 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(36.5,'cm^3/(mol*s)'), n=3.75, Ea=(3452.17,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1060,
    label = "N-C9H20 + CH3 <=> sC9H19 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.82e-07,'cm^3/(mol*s)'), n=5.89, Ea=(19948.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1061,
    label = "pC9H19 <=> C2H4 + C7H15",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(9.12e+11,'s^-1'), n=0.31, Ea=(113963,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.8e-57,'cm^3/(mol*s)'), n=23.46, Ea=(-2520.12,'J/mol'), T0=(1,'K')), alpha=-2.46, T3=(206,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1062,
    label = "pC9H19 + H <=> C7H15 + C2H5",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10],'atm'), arrhenius=[Arrhenius(A=(3.4e+18,'cm^3/(mol*s)'), n=-1.33, Ea=(22534.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.7e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(52321.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.1e+27,'cm^3/(mol*s)'), n=-3.59, Ea=(79743.3,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1063,
    label = "pC9H19 + H <=> nC9H18 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1064,
    label = "pC9H19 + O <=> nC8H17 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1065,
    label = "pC9H19 + OH <=> nC9H18 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1066,
    label = "pC9H19 + HO2 <=> nC8H17 + OH + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1067,
    label = "pC9H19 + HCO <=> N-C9H20 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1068,
    label = "pC9H19 + CH3 <=> nC9H18 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1069,
    label = "pC9H19 + O2 <=> nC9H18 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1070,
    label = "sC9H19 <=> pC9H19",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(3.56e+10,'s^-1'), n=0.88, Ea=(162947,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.8e+10,'s^-1'), n=0.67, Ea=(156680,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1071,
    label = "sC9H19 <=> C3H6 + C6H13",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(6.03e+10,'s^-1'), n=0.84, Ea=(116399,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1e-43,'cm^3/(mol*s)'), n=18.591, Ea=(-2520.95,'J/mol'), T0=(1,'K')), alpha=-43.32, T3=(200,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1072,
    label = "sC9H19 <=> C5H11 + C4H8",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.04e+13,'s^-1'), n=0.04, Ea=(119050,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3e-43,'cm^3/(mol*s)'), n=18.43, Ea=(-2518.45,'J/mol'), T0=(1,'K')), alpha=-34.47, T3=(208,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1073,
    label = "sC9H19 <=> C8H16 + CH3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(9.55e+09,'s^-1'), n=1.08, Ea=(122786,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(5.3e-46,'cm^3/(mol*s)'), n=19.133, Ea=(-2518.45,'J/mol'), T0=(1,'K')), alpha=-34.36, T3=(210,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1074,
    label = "sC9H19 <=> pC4H9 + C5H10",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(5.5e+11,'s^-1'), n=0.55, Ea=(117340,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.1e-43,'cm^3/(mol*s)'), n=18.42, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-32.13, T3=(207,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1075,
    label = "sC9H19 <=> C7H14 + C2H5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(6.76e+09,'s^-1'), n=1.11, Ea=(112906,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(8.2e-43,'cm^3/(mol*s)'), n=18.28, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-30.04, T3=(210,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1076,
    label = "sC9H19 <=> nC3H7 + C6H12",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1.1e+12,'s^-1'), n=0.55, Ea=(117340,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.2e-43,'cm^3/(mol*s)'), n=18.42, Ea=(-2519.29,'J/mol'), T0=(1,'K')), alpha=-32.13, T3=(207,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1077,
    label = "sC9H19 + H <=> C7H15 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+28,'cm^3/(mol*s)'), n=-3.94, Ea=(66592.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1078,
    label = "sC9H19 + H <=> nC9H18 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1079,
    label = "sC9H19 + O <=> CH3CHO + C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1080,
    label = "sC9H19 + OH <=> nC9H18 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1081,
    label = "sC9H19 + HO2 <=> CH3CHO + C7H15 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1082,
    label = "sC9H19 + HCO <=> N-C9H20 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1083,
    label = "sC9H19 + CH3 <=> CH4 + nC9H18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+14,'cm^3/(mol*s)'), n=-0.68, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1084,
    label = "sC9H19 + O2 <=> nC9H18 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.2e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1085,
    label = "nC9H18 <=> C6H13 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+23,'s^-1'), n=-2.03, Ea=(313624,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1086,
    label = "nC9H18 <=> C6H12 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.08e+06,'s^-1'), n=1.65, Ea=(224899,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1087,
    label = "nC9H17 + H <=> nC9H18",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24408,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1088,
    label = "nC9H18 + H <=> C2H4 + C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+21,'cm^3/(mol*s)'), n=-2.39, Ea=(46777.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1089,
    label = "nC9H18 + H <=> C3H6 + C6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+22,'cm^3/(mol*s)'), n=-2.39, Ea=(46777.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1090,
    label = "nC9H18 + H <=> nC9H17 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0323,'cm^3/(mol*s)'), n=4.7, Ea=(15392.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1091,
    label = "nC9H18 + O <=> nC8H17 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+08,'cm^3/(mol*s)'), n=1.45, Ea=(-1682.02,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1092,
    label = "nC9H18 + O <=> nC9H17 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.745,'cm^3/(mol*s)'), n=4.17, Ea=(11573.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1093,
    label = "nC9H18 + OH <=> nC9H17 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(700,'cm^3/(mol*s)'), n=2.66, Ea=(2205,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1094,
    label = "nC9H18 + O2 <=> nC9H17 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(213092,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1095,
    label = "nC9H18 + HO2 <=> nC9H17 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(59998.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1096,
    label = "nC9H18 + CH3 <=> nC9H17 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.58e-08,'cm^3/(mol*s)'), n=6.08, Ea=(26036.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1097,
    label = "nC9H17 + HCO <=> nC9H18 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1098,
    label = "nC9H17 + H <=> CH3 + nC8H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+21,'cm^3/(mol*s)'), n=-2, Ea=(46023.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1099,
    label = "C2H4 + C7H13 <=> nC9H17",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+11,'cm^3/(mol*s)'), n=0, Ea=(30543.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1100,
    label = "nC9H17 + HO2 <=> CH2O + OH + nC8H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1101,
    label = "N-C10H22 <=> C5H11 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1102,
    label = "N-C10H22 <=> C7H15 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1103,
    label = "N-C10H22 <=> C6H13 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1104,
    label = "N-C10H22 + H <=> pC10H21 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.6e+07,'cm^3/(mol*s)'), n=2, Ea=(32193.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1105,
    label = "N-C10H22 + OH <=> pC10H21 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04e+10,'cm^3/(mol*s)'), n=0.97, Ea=(6651.58,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1106,
    label = "N-C10H22 + O <=> pC10H21 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.35e+06,'cm^3/(mol*s)'), n=2.4, Ea=(23001.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1107,
    label = "N-C10H22 + HO2 <=> pC10H21 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+13,'cm^3/(mol*s)'), n=0, Ea=(81093.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1108,
    label = "N-C10H22 + H <=> sC10H21 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.83e+07,'cm^3/(mol*s)'), n=2, Ea=(20902.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1109,
    label = "N-C10H22 + OH <=> sC10H21 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.38e+07,'cm^3/(mol*s)'), n=1.6, Ea=(-169.615,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1110,
    label = "N-C10H22 + O <=> sC10H21 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(620000,'cm^3/(mol*s)'), n=2.5, Ea=(9320.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1111,
    label = "N-C10H22 + HO2 <=> sC10H21 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.79e+12,'cm^3/(mol*s)'), n=0, Ea=(71063.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1112,
    label = "N-C10H22 + CH3 <=> sC10H21 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.98e+11,'cm^3/(mol*s)'), n=0, Ea=(39709.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1113,
    label = "N-C10H22 + O2 <=> pC10H21 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(213092,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1114,
    label = "N-C10H22 + O2 <=> sC10H21 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+13,'cm^3/(mol*s)'), n=0, Ea=(199117,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1115,
    label = "pC10H21 <=> nC8H17 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(120410,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1116,
    label = "pC10H21 + O2 <=> nC10H20 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(8356.04,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1117,
    label = "pC10H21 => sC10H21",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11,'s^-1'), n=0, Ea=(46403.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1118,
    label = "sC10H21 <=> C7H15 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1119,
    label = "sC10H21 <=> C6H13 + C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1120,
    label = "sC10H21 <=> C5H10 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1121,
    label = "sC10H21 <=> C8H16 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1122,
    label = "sC10H21 <=> C7H14 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1123,
    label = "sC10H21 <=> C6H12 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1124,
    label = "sC10H21 + O2 <=> nC10H20 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(17768,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1125,
    label = "nC10H20 <=> C5H10 + C5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1126,
    label = "nC10H20 <=> C4H8 + C6H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1127,
    label = "nC10H20 <=> C8H16 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1128,
    label = "nC10H20 <=> C7H15 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1129,
    label = "pC12H25 + H <=> N-C12H26",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24373.9,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1130,
    label = "N-C12H26 <=> sC10H21 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1131,
    label = "N-C12H26 <=> pC9H19 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1132,
    label = "N-C12H26 <=> nC8H17 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1133,
    label = "N-C12H26 <=> C7H15 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1134,
    label = "C6H13 + C6H13 <=> N-C12H26",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.4e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1135,
    label = "pC9H19 + C2H4 + CH3 <=> N-C12H26",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.93e+14,'cm^6/(mol^2*s)'), n=-0.32, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1136,
    label = "N-C12H26 + H <=> pC12H25 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.6e+07,'cm^3/(mol*s)'), n=2, Ea=(32193.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1137,
    label = "N-C12H26 + OH <=> pC12H25 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04e+10,'cm^3/(mol*s)'), n=0.97, Ea=(6651.58,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1138,
    label = "N-C12H26 + O <=> pC12H25 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.35e+06,'cm^3/(mol*s)'), n=2.4, Ea=(23001.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1139,
    label = "N-C12H26 + HO2 <=> pC12H25 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+13,'cm^3/(mol*s)'), n=0, Ea=(81093.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1140,
    label = "N-C12H26 + H <=> sC12H25 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.83e+07,'cm^3/(mol*s)'), n=2, Ea=(20902.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1141,
    label = "N-C12H26 + OH <=> sC12H25 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.38e+07,'cm^3/(mol*s)'), n=1.6, Ea=(-169.615,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1142,
    label = "N-C12H26 + O <=> sC12H25 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(620000,'cm^3/(mol*s)'), n=2.5, Ea=(9320.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1143,
    label = "N-C12H26 + HO2 <=> sC12H25 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.79e+12,'cm^3/(mol*s)'), n=0, Ea=(71063.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1144,
    label = "N-C12H26 + CH3 <=> sC12H25 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.98e+11,'cm^3/(mol*s)'), n=0, Ea=(39709.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1145,
    label = "N-C12H26 + O2 <=> pC12H25 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(213092,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1146,
    label = "N-C12H26 + O2 <=> sC12H25 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+13,'cm^3/(mol*s)'), n=0, Ea=(199117,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1147,
    label = "pC12H25 <=> pC10H21 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(120410,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1148,
    label = "pC12H25 <=> sC12H25",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.95,'s^-1'), n=3.08, Ea=(46025.6,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.9e-34,'cm^3/(mol*s)'), n=15.85, Ea=(-2532.59,'J/mol'), T0=(1,'K')), alpha=-15.24, T3=(216,'K'), T1=(28,'K'), T2=(5e+06,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1149,
    label = "sC12H25 <=> pC10H21 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1150,
    label = "sC12H25 <=> nC10H20 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1151,
    label = "sC12H25 <=> sC9H19 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1152,
    label = "sC12H25 <=> nC9H18 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1153,
    label = "sC12H25 <=> nC8H17 + C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1154,
    label = "sC12H25 <=> C8H16 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.4e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1155,
    label = "sC12H25 <=> N-C7H16 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+12,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1156,
    label = "sC12H25 <=> C7H15 + C5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1157,
    label = "sC12H25 <=> C7H14 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1158,
    label = "sC12H25 <=> N-C6H14 + C6H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+12,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1159,
    label = "sC12H25 <=> C6H12 + C6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1160,
    label = "sC12H25 + O2 <=> nC12H24 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(17768,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1161,
    label = "nC12H24 <=> nC4H7 + nC8H17",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1162,
    label = "nC12H24 <=> C6H11 + C6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1163,
    label = "nC12H24 <=> C5H9 + C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1164,
    label = "nC12H24 <=> nC9H18 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1165,
    label = "nC12H24 <=> pC9H19 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+23,'s^-1'), n=-2.03, Ea=(313184,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1166,
    label = "nC12H24 + H <=> nC12H23 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(16213.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1167,
    label = "nC12H24 + H <=> C3H6 + pC9H19",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+22,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1168,
    label = "nC12H24 + H <=> C2H4 + pC10H21",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+21,'cm^3/(mol*s)'), n=-2.39, Ea=(46711.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1169,
    label = "nC12H24 + CH3 <=> nC12H23 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(30347.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1170,
    label = "nC12H24 + C2H5 <=> nC12H23 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(33257.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1171,
    label = "nC12H24 + O <=> nC12H23 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+08,'cm^3/(mol*s)'), n=1.45, Ea=(-1679.61,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1172,
    label = "nC12H24 + OH <=> nC12H23 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(5113.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1173,
    label = "nC12H24 + HO2 <=> nC12H23 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(71088.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1174,
    label = "nC12H24 + O2 <=> nC12H23 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(167121,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1175,
    label = "nC12H23 <=> C6H10 + C6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(187076,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1176,
    label = "nC12H23 <=> nC8H17 + C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(187076,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1177,
    label = "nC12H23 <=> C7H15 + C5H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(187076,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1178,
    label = "C16H33 + H <=> N-C16H34",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.01e+48,'cm^6/(mol^2*s)'), n=-9.32, Ea=(24373.9,'J/mol'), T0=(1,'K')), alpha=0.498, T3=(1314,'K'), T1=(1314,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1179,
    label = "N-C16H34 <=> pC12H25 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1180,
    label = "N-C16H34 <=> pC10H21 + C6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1181,
    label = "N-C16H34 <=> pC9H19 + C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+16,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1182,
    label = "N-C16H34 <=> nC8H17 + nC8H17",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+15,'s^-1'), n=0, Ea=(339023,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1183,
    label = "N-C16H34 + H <=> C16H33 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.83e+07,'cm^3/(mol*s)'), n=2, Ea=(20902.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1184,
    label = "N-C16H34 + OH <=> C16H33 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.38e+07,'cm^3/(mol*s)'), n=1.6, Ea=(-169.615,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1185,
    label = "N-C16H34 + O <=> C16H33 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(620000,'cm^3/(mol*s)'), n=2.5, Ea=(9320.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1186,
    label = "N-C16H34 + HO2 <=> C16H33 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.79e+12,'cm^3/(mol*s)'), n=0, Ea=(71063.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1187,
    label = "N-C16H34 + CH3 <=> C16H33 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.98e+11,'cm^3/(mol*s)'), n=0, Ea=(39709.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1188,
    label = "C16H33 <=> pC4H9 + nC12H24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1189,
    label = "C16H33 <=> C6H13 + nC10H20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1190,
    label = "C16H33 <=> C7H15 + nC9H18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1191,
    label = "C16H33 <=> nC8H17 + C8H16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1192,
    label = "C16H33 <=> pC9H19 + C7H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1193,
    label = "C16H33 <=> pC10H21 + C6H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1194,
    label = "C16H33 <=> pC12H25 + C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0, Ea=(118315,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1195,
    label = "C16H33 + O2 <=> C16H32 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(17768,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1196,
    label = "C16H32 <=> nC12H24 + C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1197,
    label = "C16H32 <=> nC10H20 + C6H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1198,
    label = "C16H32 <=> nC9H18 + C7H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1199,
    label = "C16H32 <=> C8H16 + C8H16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(295164,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1200,
    label = "cyC6H12 => C2H4 + C2H4 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+12,'s^-1'), n=0, Ea=(239824,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1201,
    label = "cyC6H12 <=> C3H6 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'s^-1'), n=0, Ea=(239823,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1202,
    label = "cyC6H12 <=> C4H8 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'s^-1'), n=0, Ea=(239824,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1203,
    label = "cyC6H11 + H <=> cyC6H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1204,
    label = "cyC6H12 <=> C6H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.83e+13,'s^-1'), n=0, Ea=(286202,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1205,
    label = "cyC6H12 + H <=> cyC6H11 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+14,'cm^3/(mol*s)'), n=0, Ea=(34983.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1206,
    label = "cyC6H12 + OH <=> cyC6H11 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+07,'cm^3/(mol*s)'), n=2, Ea=(-4733.82,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1207,
    label = "cyC6H12 + O <=> cyC6H11 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.54e+14,'cm^3/(mol*s)'), n=0, Ea=(18789,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1208,
    label = "cyC6H12 + HO2 <=> cyC6H11 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(400000,'cm^3/(mol*s)'), n=2.5, Ea=(59109.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1209,
    label = "cyC6H12 + CH3 <=> cyC6H11 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.35e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1210,
    label = "cyC6H12 + HCO <=> cyC6H11 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.35e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1211,
    label = "cyC6H12 + CH3O <=> cyC6H11 + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.32e+11,'cm^3/(mol*s)'), n=0, Ea=(18688.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1212,
    label = "cyC6H12 + C3H5 <=> cyC6H11 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.05e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1213,
    label = "cyC6H12 + C2H3 <=> cyC6H11 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.35e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1214,
    label = "cyC6H12 + C2H5 <=> cyC6H11 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.35e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1215,
    label = "cyC6H12 + O2 <=> cyC6H11 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68e+14,'cm^3/(mol*s)'), n=0, Ea=(201427,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1216,
    label = "cyC6H11 <=> cyC6H10 + H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(3.34e+11,'s^-1'), n=0.69, Ea=(141838,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3e-40,'cm^3/(mol*s)'), n=17.33, Ea=(-2518.15,'J/mol'), T0=(1,'K')), alpha=-19.22, T3=(230,'K'), T1=(28,'K'), T2=(50000,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1217,
    label = "cyC6H11 <=> C6H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(125341,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1218,
    label = "cyC6H11 + O2 <=> cyC6H10 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+10,'cm^3/(mol*s)'), n=0, Ea=(-8356.29,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1219,
    label = "cyC6H11 + OH <=> cyC6H10 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1220,
    label = "cyC6H11 + HO2 => C5H9 + CH2O + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1221,
    label = "cyC6H11 + HO2 <=> cyC6H10 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(8356.29,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1222,
    label = "cyC6H11 + O <=> C5H9 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1223,
    label = "cyC6H11 + O <=> cyC6H10 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.64e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1224,
    label = "cyC6H11 + H <=> cyC6H10 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1225,
    label = "cyC6H11 + HCO <=> cyC6H10 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1226,
    label = "cyC6H11 + CH3 <=> cyC6H10 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1227,
    label = "cyC6H11 + C2H3 <=> cyC6H10 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1228,
    label = "cyC6H11 + C2H5 <=> cyC6H10 + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1229,
    label = "cyC6H11 + C3H5 <=> cyC6H10 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1230,
    label = "cyC6H10 + H <=> cyC6H9 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(230000,'cm^3/(mol*s)'), n=2.5, Ea=(10403.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1231,
    label = "cyC6H10 + O <=> cyC6H9 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+11,'cm^3/(mol*s)'), n=0.7, Ea=(24567.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1232,
    label = "cyC6H10 + OH <=> cyC6H9 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.14e+06,'cm^3/(mol*s)'), n=2, Ea=(-1245.08,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1233,
    label = "cyC6H9 + HO2 <=> cyC6H10 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.66e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1234,
    label = "cyC6H10 + CH3 <=> cyC6H9 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.94,'cm^3/(mol*s)'), n=3.5, Ea=(23710.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1235,
    label = "cyC6H9 + H <=> cyC6H10",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.33e+60,'cm^6/(mol^2*s)'), n=-12, Ea=(24934.2,'J/mol'), T0=(1,'K')), alpha=0.02, T3=(1096.6,'K'), T1=(1096.6,'K'), T2=(6859.5,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1236,
    label = "cyC6H9 + O2 <=> cyC6H8 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1237,
    label = "cyC6H9 <=> cyC6H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.67e+12,'s^-1'), n=0.71, Ea=(208038,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1238,
    label = "cyC6H9 + H <=> cyC6H8 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1239,
    label = "cyC6H9 + CH3 <=> cyC6H8 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1240,
    label = "cyC6H8 + H <=> cyC6H7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(230000,'cm^3/(mol*s)'), n=2.5, Ea=(10403.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1241,
    label = "cyC6H8 + O <=> cyC6H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+11,'cm^3/(mol*s)'), n=0.7, Ea=(24567.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1242,
    label = "cyC6H8 + OH <=> cyC6H7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.14e+06,'cm^3/(mol*s)'), n=2, Ea=(-1245.08,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1243,
    label = "cyC6H7 + HO2 <=> cyC6H8 + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.66e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1244,
    label = "cyC6H7 + H <=> cyC6H8",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.33e+60,'cm^6/(mol^2*s)'), n=-12, Ea=(24934.2,'J/mol'), T0=(1,'K')), alpha=0.02, T3=(1096.6,'K'), T1=(1096.6,'K'), T2=(6859.5,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1245,
    label = "cyC6H7 <=> H + A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.8e+25,'s^-1'), n=-3.5, Ea=(139884,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1246,
    label = "cyC6H7 + O2 <=> A1 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1247,
    label = "cyC6H7 + O <=> A1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1248,
    label = "cyC6H7 + O <=> cyclopentadiene + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.256e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1249,
    label = "cyC6H7 + H <=> A1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1250,
    label = "cyC6H7 + OH <=> A1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.02e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1251,
    label = "cyC6H7 + HO2 <=> A1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1252,
    label = "cyC6H7 + HO2 => cyclopentadiene + HCO + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1253,
    label = "cyC6H7 + CH3 <=> A1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1254,
    label = "cyC6H7 + C2H3 <=> A1 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1255,
    label = "cyC5H8 <=> cyclopentadiene + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+16,'s^-1'), n=0, Ea=(249768,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1256,
    label = "cyC5H8 + O2 <=> cyC5H7 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.28e+13,'cm^3/(mol*s)'), n=0, Ea=(104453,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1257,
    label = "cyC5H8 + O <=> cyC5H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.78e+14,'cm^3/(mol*s)'), n=0, Ea=(10478.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1258,
    label = "cyC5H8 + HO2 <=> cyC5H7 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+14,'cm^3/(mol*s)'), n=0, Ea=(71278.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1259,
    label = "cyC5H7 + O2 <=> cyclopentadiene + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01e+15,'cm^3/(mol*s)'), n=0, Ea=(55790.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1260,
    label = "C5H8 + OH <=> CH2O + nC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1261,
    label = "C5H8 + O <=> CH2O + C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1262,
    label = "cyC6H10OH => CH2HCO + C2H4 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(107378,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1263,
    label = "cyC6H10OH => C2H3 + C2H4 + CH3CHO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(115734,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1264,
    label = "C3H5 + HO2 <=> (Acrolein) + H + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+18,'cm^3/(mol*s)'), n=-2, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1265,
    label = "cyC6H10 + O => (Acrolein) + H + C3H5",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(120000,'cm^3/(mol*s)'), n=2.56, Ea=(-4739.25,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1266,
    label = "(Acrolein) + H => H2 + C2H3 + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(17460.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1267,
    label = "(Acrolein) + OH <=> CO + C2H3 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1268,
    label = "C5H5 + H <=> cyclopentadiene",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(4.4e+80,'cm^6/(mol^2*s)'), n=-18.28, Ea=(54290.6,'J/mol'), T0=(1,'K')), alpha=0.068, T3=(400.7,'K'), T1=(4135.8,'K'), T2=(5501.9,'K'), efficiencies={'C': 2.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1269,
    label = "C3H3 + C2H3 <=> C5H5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+40,'cm^3/(mol*s)'), n=-7.8, Ea=(119812,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1270,
    label = "C3H3 + C2H2 <=> C5H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.87e+55,'cm^3/(mol*s)'), n=-12.5, Ea=(175011,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1271,
    label = "cyclopentadiene + H <=> C5H5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+13,'cm^3/(mol*s)'), n=0, Ea=(9453.55,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1272,
    label = "C5H5 + O <=> C5H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e-12,'cm^3/(mol*s)'), n=5.87, Ea=(-72323.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1273,
    label = "C5H5 + OH <=> C5H5O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.36e+51,'cm^3/(mol*s)'), n=-10.46, Ea=(238571,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1274,
    label = "C5H5 + HO2 <=> C5H5O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.27e+29,'cm^3/(mol*s)'), n=-4.69, Ea=(48675.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1275,
    label = "C5H5 + O2 <=> C5H5O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.78e+15,'cm^3/(mol*s)'), n=-0.73, Ea=(203642,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1276,
    label = "C5H5O <=> C5H4O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1277,
    label = "C5H5O + O2 <=> C5H4O + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1278,
    label = "C5H5 + O2 <=> C5H4O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'cm^3/(mol*s)'), n=0.08, Ea=(75206.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1279,
    label = "C5H5 + O <=> C5H4O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.81e+13,'cm^3/(mol*s)'), n=-0.02, Ea=(83.5629,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1280,
    label = "C5H4O <=> C2H2 + C2H2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.2e+41,'s^-1'), n=-7.87, Ea=(412381,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1281,
    label = "C5H4O + H <=> CO + C4H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.3e+09,'cm^3/(mol*s)'), n=1.45, Ea=(16294.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1282,
    label = "C5H4O + O <=> CO + HCO + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.2e+08,'cm^3/(mol*s)'), n=1.45, Ea=(-3584.83,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1283,
    label = "cyclopentadiene + H <=> C3H5 + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+14,'cm^3/(mol*s)'), n=0, Ea=(51549.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1284,
    label = "cyclopentadiene + OH <=> C5H5 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.43e+09,'cm^3/(mol*s)'), n=1.18, Ea=(-1870.76,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1285,
    label = "cyclopentadiene + HO2 <=> C5H5 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(48781,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1286,
    label = "cyclopentadiene + O2 <=> C5H5 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(155217,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1287,
    label = "cyclopentadiene + CH3 <=> C5H5 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.1,'cm^3/(mol*s)'), n=4, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1288,
    label = "cyclopentadiene + C2H3 <=> C5H5 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1289,
    label = "cyclopentadiene + iC4H5 <=> C5H5 + C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+15,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1290,
    label = "cyC6H11 + O2 <=> cyC6H11OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+18,'cm^3/(mol*s)'), n=-2.5, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1291,
    label = "cyC6H11OO <=> cyC6H10OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+11,'s^-1'), n=0, Ea=(100593,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1292,
    label = "cyC6H11OO <=> HO2 + cyC6H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+12,'s^-1'), n=0, Ea=(124926,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1293,
    label = "cyC6H11OO + HO2 <=> cyC6H11OOH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6000,'cm^3/(mol*s)'), n=2.5, Ea=(59747.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1294,
    label = "cyC6H11OO + cyC6H11OO => cyC6H11O + cyC6H11O + O2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.4e+16,'cm^3/(mol*s)'), n=-1.6, Ea=(7771.31,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1295,
    label = "cyC6H10 + HO2 <=> cyC6H10OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(50137.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1296,
    label = "cyC6H11 + O2 <=> cyC6H10OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.95e+13,'cm^3/(mol*s)'), n=0, Ea=(50471.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1297,
    label = "cyC6H10OOH => OH + CO + C5H10",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.45e+12,'s^-1'), n=0, Ea=(75457,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1298,
    label = "cyC6H10OOH + O2 <=> cyOOC6H10OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1299,
    label = "cyC6H11OOH => OH + cyC6H11O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.26e+16,'s^-1'), n=0, Ea=(177571,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1300,
    label = "cyC6H11OOH + HO2 <=> H2O2 + cyC6H11OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6000,'cm^3/(mol*s)'), n=2.5, Ea=(59747.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1301,
    label = "cyOOC6H10OOH <=> OH + cyOC6H9OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+16,'s^-1'), n=0, Ea=(177571,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1302,
    label = "cyOOC6H10OOH => OH + cyC6H9O + HO2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+15,'s^-1'), n=0, Ea=(171303,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1303,
    label = "cyOC6H9OOH => CH3CH2O + CH2HCO + CH2CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+15,'s^-1'), n=0, Ea=(171303,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1304,
    label = "cyC6H9O => C2H4 + C2H4 + HCCO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12,'s^-1'), n=0, Ea=(91500.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1305,
    label = "cyC6H9O => C2H3 + C2H4 + CH2CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12,'s^-1'), n=0, Ea=(91500.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1306,
    label = "iC4H5 + CH3CHO <=> cyC6H9O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(49719.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1307,
    label = "C5H9 + CO <=> cyC6H9O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(49719.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1308,
    label = "cyC6H9O + HO2 <=> cyOC6H9OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1309,
    label = "HO2 + cyC6H11 <=> cyC6H11O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+12,'cm^3/(mol*s)'), n=0, Ea=(-4178.13,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1310,
    label = "cyC6H11O => CH2HCO + C2H4 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(107378,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1311,
    label = "cyC6H11O => C2H3 + C2H4 + CH3CHO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(115734,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1312,
    label = "C5H9 + CH2O <=> cyC6H11O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(49719.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1313,
    label = "cyC9H18 => C2H4 + C2H4 + C5H10",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6.5e+16,'s^-1'), n=0, Ea=(350963,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1314,
    label = "cyC9H18 => C2H4 + nC3H7 + nC4H7",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.6e+17,'s^-1'), n=0, Ea=(350963,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1315,
    label = "cyC9H18 <=> cyC6H11 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+17,'s^-1'), n=0, Ea=(350963,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1316,
    label = "cyC9H18 <=> cyC7H13 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.5e+16,'s^-1'), n=0, Ea=(350963,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1317,
    label = "cyC9H18 <=> cyC8H15 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.5e+16,'s^-1'), n=0, Ea=(355141,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1318,
    label = "cyC9H18 + O2 => cyC9H17B + HO2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.4e+14,'cm^3/(mol*s)'), n=0, Ea=(207486,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1319,
    label = "cyC9H18 + HO2 => cyC9H17B + H2O2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(34300,'cm^3/(mol*s)'), n=2.61, Ea=(58117.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1320,
    label = "cyC9H18 + OH <=> cyC9H17B + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+07,'cm^3/(mol*s)'), n=1.85, Ea=(488.841,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1321,
    label = "cyC9H18 + O <=> cyC9H17B + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+10,'cm^3/(mol*s)'), n=1.55, Ea=(35865.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1322,
    label = "cyC9H18 + H <=> cyC9H17B + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.7e+09,'cm^3/(mol*s)'), n=1.56, Ea=(43431.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1323,
    label = "cyC9H18 + CH3 <=> cyC9H17B + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+08,'cm^3/(mol*s)'), n=1.55, Ea=(77161.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1324,
    label = "cyC9H18 + C2H3 <=> cyC9H17B + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+08,'cm^3/(mol*s)'), n=1.55, Ea=(77161.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1325,
    label = "cyC9H18 + C2H5 <=> cyC9H17B + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+08,'cm^3/(mol*s)'), n=1.55, Ea=(77161.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1326,
    label = "cyC9H18 + HCO => cyC9H17B + CH2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.8e+08,'cm^3/(mol*s)'), n=1.55, Ea=(77161.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1327,
    label = "cyC9H18 + CH3O <=> cyC9H17B + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+12,'cm^3/(mol*s)'), n=0, Ea=(18688.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1328,
    label = "cyC9H18 + O2 => cyC9H17E + HO2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.09e+14,'cm^3/(mol*s)'), n=0, Ea=(206082,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1329,
    label = "cyC9H18 + HO2 => cyC9H17E + H2O2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(130000,'cm^3/(mol*s)'), n=2.5, Ea=(60591.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1330,
    label = "cyC9H18 + OH <=> cyC9H17E + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+07,'cm^3/(mol*s)'), n=2, Ea=(-4733.82,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1331,
    label = "cyC9H18 + O <=> cyC9H17E + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+06,'cm^3/(mol*s)'), n=2.6, Ea=(10708.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1332,
    label = "cyC9H18 + H <=> cyC9H17E + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+14,'cm^3/(mol*s)'), n=0, Ea=(34983.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1333,
    label = "cyC9H18 + CH3 <=> cyC9H17E + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.13e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1334,
    label = "cyC9H18 + C2H3 <=> cyC9H17E + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.13e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1335,
    label = "cyC9H18 + C2H5 <=> cyC9H17E + C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.13e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1336,
    label = "cyC9H18 + HCO => cyC9H17E + CH2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.13e+12,'cm^3/(mol*s)'), n=0, Ea=(39859.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1337,
    label = "cyC9H18 + CH3O <=> cyC9H17E + CH3OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+12,'cm^3/(mol*s)'), n=0, Ea=(18688.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1338,
    label = "cyC9H17E <=> cyC9H17B",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'s^-1'), n=0, Ea=(67267.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1339,
    label = "cyC9H17B => cyC6H11 + C3H6",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(175481,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1340,
    label = "cyC9H17B => C2H4 + C2H4 + C5H9",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(175481,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1341,
    label = "cyC9H17B <=> cyC8H14 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(188016,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1342,
    label = "cyC9H17B <=> cyC7H13 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(175481,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1343,
    label = "cyC9H17B <=> cyC7H12 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(175481,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1344,
    label = "cyC9H17E => C4H6 + C2H4 + nC3H7",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(183838,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1345,
    label = "cyC9H17E <=> nC4H7 + C5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'s^-1'), n=0, Ea=(208906,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1346,
    label = "cyC9H17E <=> cyC6H10 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(165036,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1347,
    label = "cyC9H17E <=> C6H10 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(188016,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1348,
    label = "cyC7H13 + O2 <=> cyC7H12 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(41781.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1349,
    label = "cyC7H13 + H <=> cyC7H12 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1350,
    label = "cyC7H13 + OH <=> cyC7H12 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1351,
    label = "cyC7H13 + O <=> cyC7H12 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1352,
    label = "cyC7H13 + CH3 <=> cyC7H12 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1353,
    label = "cyC7H13 => C2H4 + C2H4 + C3H5",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(121166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1354,
    label = "cyC7H12 => C4H6 + C3H6",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(296647,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1355,
    label = "cyC8H15 <=> cyC6H11 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(121166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1356,
    label = "cyC8H15 + O2 <=> cyC8H14 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(41781.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1357,
    label = "cyC8H15 + H <=> cyC8H14 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1358,
    label = "cyC8H15 + OH <=> cyC8H14 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1359,
    label = "cyC8H15 + O <=> cyC8H14 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1360,
    label = "cyC8H15 + CH3 <=> cyC8H14 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1361,
    label = "cyC8H14 <=> C2H4 + C2H4 + C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(296647,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1362,
    label = "C3H3 + C3H3 <=> A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+36,'cm^3/(mol*s)'), n=-7.18, Ea=(35203.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1363,
    label = "C3H3 + C3H3 <=> A1- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+35,'cm^3/(mol*s)'), n=-7.18, Ea=(35203.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1364,
    label = "C3H3 + C3H4 <=> A1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+12,'cm^3/(mol*s)'), n=0, Ea=(41572.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1365,
    label = "iC4H3 + C2H3 <=> A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1366,
    label = "iC4H3 + C2H3 <=> A1- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1367,
    label = "iC4H3 + C2H2 <=> A1-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(61942.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1368,
    label = "C4H2 + H <=> iC4H3",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(1.1e+30,'cm^3/(mol*s)'), n=-4.92, Ea=(44898.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1369,
    label = "C4H4 + C2H3 <=> A1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+12,'cm^3/(mol*s)'), n=0, Ea=(10393.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1370,
    label = "C4H5 + C2H3 <=> A1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.84e-13,'cm^3/(mol*s)'), n=7.07, Ea=(-15087.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1371,
    label = "C4H5 + C2H2 <=> A1 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(2.38e+08,'cm^3/(mol*s)'), n=1.18, Ea=(15631.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(15460.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1372,
    label = "iC4H5 + C2H4 => A1 + H + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3e+11,'cm^3/(mol*s)'), n=0, Ea=(29250.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1373,
    label = "iC4H5 + C2H2 <=> A1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(22449.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1374,
    label = "iC4H5 + C2H3 <=> A1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e-13,'cm^3/(mol*s)'), n=7.07, Ea=(-14966,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1375,
    label = "iC4H5 + C2H <=> A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1376,
    label = "iC4H5 + C2H <=> A1- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1377,
    label = "C5H5 + CH3 <=> A1 + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+18,'cm^3/(mol*s)'), n=0, Ea=(249434,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1378,
    label = "cyclopentadiene + C2H3 <=> A1 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.12e+67,'cm^3/(mol*s)'), n=-16.08, Ea=(177265,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1379,
    label = "A1 <=> A1- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+14,'s^-1'), n=0, Ea=(449480,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1380,
    label = "A1 + O <=> A1- + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1381,
    label = "A1 + O <=> C5H5 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(18957,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1382,
    label = "A1 + O <=> C6H5O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(18957,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1383,
    label = "A1 + H <=> A1- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.51e+14,'cm^3/(mol*s)'), n=0, Ea=(67014.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1384,
    label = "A1 + OH <=> C6H5OH + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(43900.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1385,
    label = "A1 + OH <=> A1- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.45e+13,'cm^3/(mol*s)'), n=0, Ea=(18790.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1386,
    label = "A1 + CH3 <=> A1- + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(62608,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1387,
    label = "A1 + C2H <=> A1- + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1388,
    label = "A1 + O2 <=> A1- + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(261906,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1389,
    label = "A1- + O2 <=> C6H5O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+12,'cm^3/(mol*s)'), n=0, Ea=(25359.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1390,
    label = "A1- + O <=> C5H5 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1391,
    label = "A1- + OH <=> C6H5O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1392,
    label = "A1- + C6H5OH <=> C6H5O + A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.91e+12,'cm^3/(mol*s)'), n=0, Ea=(18291.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1393,
    label = "C6H5O <=> C5H5 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.4e+11,'s^-1'), n=0, Ea=(183750,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1394,
    label = "C6H5O + O <=> C5H5 + CO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1395,
    label = "C6H5O + H <=> cyclopentadiene + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1396,
    label = "C6H5O + H <=> C6H5OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1397,
    label = "C6H5OH <=> cyclopentadiene + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'s^-1'), n=0, Ea=(254423,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1398,
    label = "C6H5OH + O <=> C6H5O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8e+13,'cm^3/(mol*s)'), n=0, Ea=(29932.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1399,
    label = "C6H5OH + H <=> C6H5O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+13,'cm^3/(mol*s)'), n=0, Ea=(24943.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1400,
    label = "C6H5OH + OH <=> C6H5O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+10,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1401,
    label = "C6H5OH + C2H3 <=> C6H5O + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1402,
    label = "A1 + CH2 <=> C7H8",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(1.7e+13,'cm^3/(mol*s)'), n=0, Ea=(36334.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(36334.2,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified

Originally from reaction library: Unclassified
""",
)

entry(
    index = 1403,
    label = "C7H8 <=> A1- + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+16,'s^-1'), n=0, Ea=(414892,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1404,
    label = "iC4H5 + C3H3 <=> C7H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+36,'cm^3/(mol*s)'), n=-7.18, Ea=(35203.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1405,
    label = "C7H7 + H <=> C7H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1406,
    label = "C7H8 + O2 <=> C7H7 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(172110,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1407,
    label = "C7H8 + O <=> C7H7 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.3e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1408,
    label = "C7H8 + H <=> A1 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(21201.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1409,
    label = "C7H8 + H <=> C7H7 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(34089.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1410,
    label = "iC4H5 + C3H4 <=> C7H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(15381.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1411,
    label = "C7H8 + OH <=> C7H7 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.18e+09,'cm^3/(mol*s)'), n=1, Ea=(3658.37,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1412,
    label = "C7H8 + HO2 <=> C7H7 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(62192.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1413,
    label = "C7H8 + CH3 <=> C7H7 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(46477.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1414,
    label = "C7H8 + C2H3 <=> C7H7 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(33923,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1415,
    label = "C7H8 + C3H3 <=> C7H7 + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+12,'cm^3/(mol*s)'), n=0, Ea=(63023.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1416,
    label = "C7H8 + C3H5 <=> C7H7 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+12,'cm^3/(mol*s)'), n=0, Ea=(62192.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1417,
    label = "C7H8 + C5H5 <=> C7H7 + cyclopentadiene",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+12,'cm^3/(mol*s)'), n=0, Ea=(46394.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1418,
    label = "C7H8 + C6H5O <=> C7H7 + C6H5OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.431e+12,'cm^3/(mol*s)'), n=0, Ea=(86553.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1419,
    label = "C7H8 + HCO <=> C7H7 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.771e+13,'cm^3/(mol*s)'), n=0, Ea=(98892.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1420,
    label = "C7H8 + iC4H5 <=> C7H7 + C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(32010.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1421,
    label = "C7H8 + A1- <=> C7H7 + A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+13,'cm^3/(mol*s)'), n=0, Ea=(46527.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1422,
    label = "C7H7 => C4H4 + C3H3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+14,'s^-1'), n=0, Ea=(351702,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1423,
    label = "C7H7 <=> C5H5 + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.1e+13,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1424,
    label = "A1- + CH3 <=> C7H7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1425,
    label = "iC4H5 + C3H3 <=> C7H7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+35,'cm^3/(mol*s)'), n=-7.18, Ea=(35203.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1426,
    label = "C7H7 + H + OH <=> A1 + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^6/(mol^2*s)'), n=0, Ea=(21551.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1427,
    label = "C7H7 + O <=> A1 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1428,
    label = "C7H7 + O <=> A1- + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1429,
    label = "C7H7 + OH <=> A1- + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(21401.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1430,
    label = "C7H7 + HO2 <=> A1- + CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.17e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1431,
    label = "C7H7 + O2 <=> A1- + HCO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.31e+12,'cm^3/(mol*s)'), n=0, Ea=(178761,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1432,
    label = "A1- + C2H <=> A1C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.24e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(2494.34,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1433,
    label = "iC4H5 + C4H2 <=> A1C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+11,'cm^3/(mol*s)'), n=0, Ea=(7483.02,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1434,
    label = "A1C2H- + H <=> A1C2H",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.6e+75,'cm^6/(mol^2*s)'), n=-16.3, Ea=(58201.3,'J/mol'), T0=(1,'K')), alpha=1, T3=(0.1,'K'), T1=(584.9,'K'), T2=(6113,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1435,
    label = "A1C2H + O <=> A1C2H- + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+13,'cm^3/(mol*s)'), n=0, Ea=(34089.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1436,
    label = "A1C2H + O <=> A1- + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+07,'cm^3/(mol*s)'), n=2, Ea=(7898.75,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1437,
    label = "A1C2H + O <=> C6H5O + C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(18790.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1438,
    label = "A1C2H + H <=> A1C2H- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.7e+13,'cm^3/(mol*s)'), n=0, Ea=(40591.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1439,
    label = "A1C2H + H <=> A1- + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(40591.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1440,
    label = "A1C2H + H <=> A1C2H2",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(3e+43,'cm^3/(mol*s)'), n=-9.22, Ea=(63289.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1441,
    label = "A1 + C2H <=> A1C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1442,
    label = "A1C2H + OH <=> A1C2H- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+13,'cm^3/(mol*s)'), n=0, Ea=(19123.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1443,
    label = "A1C2H + OH <=> A1- + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000218,'cm^3/(mol*s)'), n=4.5, Ea=(-4157.24,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1444,
    label = "A1C2H + OH <=> A1 + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2440,'cm^3/(mol*s)'), n=3.02, Ea=(46344.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1445,
    label = "A1- + C4H2 <=> A1C2H + C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(91459.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1446,
    label = "A1- + C2H3 <=> A1C2H + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.9e+12,'cm^3/(mol*s)'), n=0, Ea=(26606.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1447,
    label = "A1- + C4H4 <=> A1C2H + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+11,'cm^3/(mol*s)'), n=0, Ea=(5656.83,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1448,
    label = "A1C2H + C2H <=> A1C2H- + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1449,
    label = "iC4H3 + C4H2 <=> A1C2H-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.6e+70,'cm^3/(mol*s)'), n=-17.77, Ea=(130205,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1450,
    label = "C5H5 + C3H3 <=> A1C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(34704.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1451,
    label = "C4H4 + C4H4 <=> A1C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+20,'cm^3/(mol*s)'), n=-1.9, Ea=(168202,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1452,
    label = "iC4H5 + C4H4 => A1C2H3 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3.16e+11,'cm^3/(mol*s)'), n=0, Ea=(2494.34,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1453,
    label = "A1- + C2H3 <=> A1C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.06e+26,'cm^3/(mol*s)'), n=-4, Ea=(22033.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1454,
    label = "A1C2H3 + H <=> A1C2H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.65e+06,'cm^3/(mol*s)'), n=2.53, Ea=(50884.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1455,
    label = "A1C2H3 + H <=> A1C2H3* + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(303,'cm^3/(mol*s)'), n=3.3, Ea=(23862.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1456,
    label = "A1C2H3 + O <=> A1- + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+08,'cm^3/(mol*s)'), n=1.45, Ea=(3741.51,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1457,
    label = "A1C2H3 + O <=> A1- + CH3 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.92e+07,'cm^3/(mol*s)'), n=1.83, Ea=(914.592,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1458,
    label = "A1C2H3 + O <=> C2H3 + C6H5O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(18832.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1459,
    label = "A1C2H3 + O <=> A1C2H2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.55e+06,'cm^3/(mol*s)'), n=1.91, Ea=(15631.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1460,
    label = "A1C2H3 + OH <=> A1C2H2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.1e+06,'cm^3/(mol*s)'), n=2, Ea=(14259.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1461,
    label = "A1C2H3 + OH => C6H5O + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(44066.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1462,
    label = "A1C2H3 + OH <=> A1C2H3* + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.63e+08,'cm^3/(mol*s)'), n=1.42, Ea=(6092.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1463,
    label = "A1C2H3 + OH <=> C7H7 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1464,
    label = "A1C2H3 + O2 <=> C6H5O + CH2HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88e+11,'cm^3/(mol*s)'), n=0, Ea=(31251.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1465,
    label = "A1C2H3 + CH3 <=> A1C2H3* + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(62608,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1466,
    label = "C7H7 + CH3 <=> A1C2H3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.06e+26,'cm^3/(mol*s)'), n=-4, Ea=(22033.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1467,
    label = "A1 + C2H3 <=> A1C2H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.9e+11,'cm^3/(mol*s)'), n=0, Ea=(26606.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1468,
    label = "A1- + C2H4 <=> A1C2H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.51e+12,'cm^3/(mol*s)'), n=0, Ea=(25733.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1469,
    label = "C7H7 + CH2 <=> A1C2H3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1470,
    label = "A1- + C4H4 <=> A1C2H3 + C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(83144.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1471,
    label = "A1- + C4H6 <=> A1C2H3 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+11,'cm^3/(mol*s)'), n=0, Ea=(7961.44,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1472,
    label = "A1C2H3* + O2 <=> C6H5O + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88e+12,'cm^3/(mol*s)'), n=0, Ea=(31251.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1473,
    label = "A1C2H3* + H <=> A1C2H3",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.6e+75,'cm^6/(mol^2*s)'), n=-16.3, Ea=(58201.3,'J/mol'), T0=(1,'K')), alpha=1, T3=(0.1,'K'), T1=(584.9,'K'), T2=(6113,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1474,
    label = "C5H5 + C3H3 <=> A1C2H3* + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+35,'cm^3/(mol*s)'), n=-7.18, Ea=(35203.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1475,
    label = "A1C2H3* + CH3 <=> INDENE + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+18,'cm^3/(mol*s)'), n=0, Ea=(303478,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1476,
    label = "A1C2H2 <=> A1C2H + H",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2e+17,'cm^3/(mol*s)'), n=0, Ea=(166289,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1477,
    label = "A1 + C2H <=> A1C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+38,'cm^3/(mol*s)'), n=-8.02, Ea=(68178.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1478,
    label = "A1- + C2H2 <=> A1C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(48872.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1479,
    label = "A1C2H2 + H <=> A1C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.4e+12,'cm^3/(mol*s)'), n=0, Ea=(10060.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1480,
    label = "A1C2H2 + H <=> A1C2H + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1481,
    label = "A1C2H2 + OH <=> A1C2H + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1482,
    label = "C5H5 + C3H3 <=> A1C2H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+35,'cm^3/(mol*s)'), n=-7.18, Ea=(35203.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1483,
    label = "A1- + C2H3 <=> A1C2H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.4,'cm^3/(mol*s)'), n=4.14, Ea=(96589.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1484,
    label = "H + INDANYL-2 <=> INDANE",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1485,
    label = "H + INDANYL-1 <=> INDANE",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1486,
    label = "INDANE => C6H4C2H3CH3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.26e+16,'s^-1'), n=0, Ea=(354723,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1487,
    label = "INDANE + H <=> INDANYL-2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(108000,'cm^3/(mol*s)'), n=2.5, Ea=(-7938.44,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1488,
    label = "INDANE + H <=> INDANYL-1 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+06,'cm^3/(mol*s)'), n=2, Ea=(20890.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1489,
    label = "INDANE + OH <=> INDANYL-2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+06,'cm^3/(mol*s)'), n=2, Ea=(-6350.75,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1490,
    label = "INDANE + OH <=> INDANYL-1 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+06,'cm^3/(mol*s)'), n=2, Ea=(-3217.16,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1491,
    label = "INDANE + O <=> INDANYL-2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+11,'cm^3/(mol*s)'), n=0.7, Ea=(13578.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1492,
    label = "INDANE + O <=> INDANYL-1 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.6e+13,'cm^3/(mol*s)'), n=0, Ea=(21726.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1493,
    label = "INDANE + HO2 <=> INDANYL-2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12800,'cm^3/(mol*s)'), n=2.6, Ea=(51808.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1494,
    label = "INDANE + HO2 <=> INDANYL-1 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(64760.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1495,
    label = "INDANE + CH3 <=> INDANYL-2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(30500.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1496,
    label = "INDANE + CH3 <=> INDANYL-1 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'cm^3/(mol*s)'), n=0, Ea=(40110,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1497,
    label = "INDANE + A1- <=> INDANYL-2 + A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(33425,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1498,
    label = "INDANE + C7H7 <=> INDANYL-2 + C7H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.8e+12,'cm^3/(mol*s)'), n=0, Ea=(54733.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1499,
    label = "INDANYL-1 <=> INDANYL-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.95e+10,'s^-1'), n=1, Ea=(142892,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1500,
    label = "INDANYL-2 <=> C6H4C2H3CH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.36e+12,'s^-1'), n=0.44, Ea=(172682,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1501,
    label = "INDANYL-2 <=> INDENE + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.21e+11,'s^-1'), n=0.985, Ea=(176317,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1502,
    label = "INDANYL-2 + O2 <=> INDENE + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+12,'cm^3/(mol*s)'), n=0, Ea=(63507.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1503,
    label = "INDANYL-1 <=> INDENE + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.57e+10,'s^-1'), n=0.885, Ea=(149452,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1504,
    label = "INDANYL-1 <=> C6H4C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.11e+13,'s^-1'), n=0.15, Ea=(191651,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1505,
    label = "INDANYL-1 + O2 <=> INDENE + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16e+12,'cm^3/(mol*s)'), n=0, Ea=(20890.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1506,
    label = "C6H4C2H3CH2 + H <=> C6H4C2H3CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1507,
    label = "C6H4C3H5 <=> A1C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.4e+13,'s^-1'), n=0, Ea=(144146,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1508,
    label = "A1C3H4 <=> C7H7 + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1509,
    label = "A1C3H4 <=> A1- + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(129522,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1510,
    label = "A1C3H4 <=> A1C2H + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(131611,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1511,
    label = "A1C2H3* + CH3 <=> C6H4C2H3CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1512,
    label = "C6H4C2H3CH3 + H <=> C6H4C2H3CH2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(170000,'cm^3/(mol*s)'), n=2.5, Ea=(10445.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1513,
    label = "C6H4C2H3CH3 + OH <=> C6H4C2H3CH2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+06,'cm^3/(mol*s)'), n=2, Ea=(-1245.08,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1514,
    label = "C6H4C2H3CH3 + H <=> A1C2H3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.8e+13,'cm^3/(mol*s)'), n=0, Ea=(33842.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1515,
    label = "C6H4C2H3CH3 + H <=> C7H8 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.8e+13,'cm^3/(mol*s)'), n=0, Ea=(33842.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1516,
    label = "C6H4C2H3CH3 + O2 => C3H4 + A1- + HO2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(204728,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1517,
    label = "C6H4C2H3CH3 + O => OH + C3H4 + A1-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(5.1e+13,'cm^3/(mol*s)'), n=0, Ea=(32798.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1518,
    label = "C6H4C2H3CH3 + H => H2 + C3H4 + A1-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.85e+07,'cm^3/(mol*s)'), n=2, Ea=(32171.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1519,
    label = "C6H4C2H3CH3 + OH => H2O + C3H4 + A1-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.67e+06,'cm^3/(mol*s)'), n=2, Ea=(1880.16,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1520,
    label = "C6H4C2H3CH3 + HO2 => H2O2 + C3H4 + A1-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11,'cm^3/(mol*s)'), n=0, Ea=(71028.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1521,
    label = "C6H4C2H3CH3 + CH3 => CH4 + C3H4 + A1-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(0.3,'cm^3/(mol*s)'), n=4, Ea=(34260.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1522,
    label = "C5H5 + iC4H3 <=> INDENE",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(34704.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1523,
    label = "A1- + C3H3 <=> INDENE",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.86e+11,'cm^3/(mol*s)'), n=0, Ea=(56958.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1524,
    label = "INDENE <=> INDENYL + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+15,'s^-1'), n=0, Ea=(322602,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1525,
    label = "INDENE + O <=> INDENYL + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1526,
    label = "INDENE + O <=> C7H7 + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(16628.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1527,
    label = "INDENE + H <=> INDENYL + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1528,
    label = "INDENE + H <=> A1C2H + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+14,'cm^3/(mol*s)'), n=0, Ea=(191233,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1529,
    label = "INDENE + H <=> A1 + C3H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(203705,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1530,
    label = "INDENE + OH <=> C7H7 + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(41572.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1531,
    label = "INDENE + OH <=> INDENYL + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1532,
    label = "INDENE + O2 <=> INDENYL + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(103931,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1533,
    label = "INDENE + HO2 <=> INDENYL + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(48468,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1534,
    label = "INDENE + CH3 <=> INDENYL + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1535,
    label = "INDENE + C3H3 <=> INDENYL + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8e+10,'cm^3/(mol*s)'), n=0, Ea=(23032.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1536,
    label = "INDENE + A1- <=> INDENYL + A1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(24943.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1537,
    label = "INDENE + C7H7 <=> INDENYL + C7H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(29100.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1538,
    label = "C4H6 + A1- <=> INDENE + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+13,'cm^3/(mol*s)'), n=0, Ea=(116403,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1539,
    label = "iC4H5 + A1 <=> INDENE + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+13,'cm^3/(mol*s)'), n=0, Ea=(116403,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1540,
    label = "A1- + C3H4 <=> INDENE + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+16,'cm^3/(mol*s)'), n=0, Ea=(138020,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1541,
    label = "C5H5 + C4H4 <=> INDENE + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+11,'cm^3/(mol*s)'), n=0, Ea=(41821.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1542,
    label = "C7H7 + C2H2 <=> INDENE + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+11,'cm^3/(mol*s)'), n=0, Ea=(41821.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1543,
    label = "C5H5 + cyclopentadiene <=> INDENE + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.63e+13,'cm^3/(mol*s)'), n=1.63, Ea=(249201,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1544,
    label = "C5H5 + C4H2 <=> INDENYL",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+12,'cm^3/(mol*s)'), n=0, Ea=(41821.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1545,
    label = "C5H5 + C5H5 <=> INDENYL + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+12,'cm^3/(mol*s)'), n=0, Ea=(40000.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1546,
    label = "INDENYL => C2H2 + C4H2 + C3H3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+14,'s^-1'), n=0, Ea=(311793,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1547,
    label = "INDENYL + O <=> A1C2H2 + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1548,
    label = "INDENYL + O <=> A1C2H3* + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1549,
    label = "INDENYL + HO2 => A1C2H2 + CO + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1550,
    label = "INDENYL + HO2 => A1C2H + CO + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1551,
    label = "INDENYL + HO2 => A1C2H3* + CO + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1552,
    label = "pbz <=> C7H7 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+15,'s^-1'), n=0, Ea=(286400,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1553,
    label = "pbz <=> C9H11 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(4.48e+16,'s^-1'), n=0, Ea=(311018,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.77e+12,'s^-1'), n=0, Ea=(225013,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1554,
    label = "pbz <=> A1C2H4 + CH3",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(4.48e+16,'s^-1'), n=0, Ea=(311018,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.77e+12,'s^-1'), n=0, Ea=(225013,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1555,
    label = "pbz <=> A1- + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+16,'s^-1'), n=0, Ea=(408024,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1556,
    label = "pbz + H <=> C9H11 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.33e+06,'cm^3/(mol*s)'), n=2.54, Ea=(28294.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1557,
    label = "pbz + H <=> A1 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.78e+13,'cm^3/(mol*s)'), n=0, Ea=(33788.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1558,
    label = "pbz + O2 <=> C9H11 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+13,'cm^3/(mol*s)'), n=0, Ea=(199547,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1559,
    label = "pbz + CH3 <=> C9H11 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+15,'cm^3/(mol*s)'), n=0, Ea=(105594,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1560,
    label = "pbz + HO2 <=> C9H11 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+13,'cm^3/(mol*s)'), n=0, Ea=(81565,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1561,
    label = "pbz + OH <=> C9H11 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.75e+08,'cm^3/(mol*s)'), n=1.4, Ea=(3575.22,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1562,
    label = "pbz + O <=> C9H11 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(19000,'cm^3/(mol*s)'), n=2.68, Ea=(17601.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1563,
    label = "C9H11 <=> C7H7 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+13,'s^-1'), n=0, Ea=(124717,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1564,
    label = "C9H11 <=> A1C2H3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+13,'s^-1'), n=0, Ea=(124717,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1565,
    label = "C9H11 <=> A1C3H5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'s^-1'), n=0, Ea=(158765,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1566,
    label = "C9H11 <=> A1- + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.08e+14,'s^-1'), n=0, Ea=(182010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1567,
    label = "A1C3H4 + H <=> A1C3H5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(1.33e+60,'cm^6/(mol^2*s)'), n=-12, Ea=(24943.4,'J/mol'), T0=(1,'K')), alpha=0.02, T3=(1096.6,'K'), T1=(1096.6,'K'), T2=(6859.5,'K'), efficiencies={'C': 2.0, 'CC': 3.0, 'O': 6.0, 'O=C=O': 2.0, '[Ar]': 0.7, '[C-]#[O+]': 1.5, '[H][H]': 2.0}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1568,
    label = "A1C3H4 <=> INDENE + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(137008,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1569,
    label = "A1C2H4 <=> A1C2H3 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(3.16e+13,'s^-1'), n=0, Ea=(212012,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.08e+14,'s^-1'), n=0, Ea=(126007,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1570,
    label = "A1C2H4 <=> A1- + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.08e+14,'s^-1'), n=0, Ea=(182010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1571,
    label = "ebz <=> A1 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+09,'s^-1'), n=0, Ea=(216005,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1572,
    label = "ebz <=> A1C2H3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.01e+12,'s^-1'), n=0, Ea=(267350,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1573,
    label = "ebz <=> C7H7 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.11e+96,'s^-1'), n=-23.78, Ea=(493688,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1574,
    label = "A1- + C2H5 <=> ebz",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(2.33e+14,'cm^3/(mol*s)'), n=-0.283, Ea=(-798.022,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.73e+83,'cm^6/(mol^2*s)'), n=-19.22, Ea=(62588.4,'J/mol'), T0=(1,'K')), alpha=0.5918, T3=(320.14,'K'), T1=(1858.22,'K'), T2=(5394.99,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1575,
    label = "A1C2H4 + H <=> ebz",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(7.22e+13,'cm^3/(mol*s)'), n=0.062, Ea=(-183.838,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.02e+136,'cm^6/(mol^2*s)'), n=-33.35, Ea=(232137,'J/mol'), T0=(1,'K')), alpha=2.545, T3=(2.156,'K'), T1=(453.23,'K'), T2=(4551.5,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1576,
    label = "ebz + H <=> A1C2H4 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.22e+08,'cm^3/(mol*s)'), n=1.5, Ea=(30968.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1577,
    label = "ebz + H <=> A1 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.78e+13,'cm^3/(mol*s)'), n=0, Ea=(33788.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1578,
    label = "ebz + OH <=> C6H5OH + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(263,'cm^3/(mol*s)'), n=2.88, Ea=(13461,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1579,
    label = "ebz + OH <=> A1C2H4 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14e+06,'cm^3/(mol*s)'), n=2.12, Ea=(3634.97,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1580,
    label = "ebz + O <=> A1C2H4 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+07,'cm^3/(mol*s)'), n=1.92, Ea=(23773.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1581,
    label = "C10H12 => C3H5 + C7H7",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+14,'s^-1'), n=0, Ea=(319627,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1582,
    label = "C10H12 => C2H3 + A1C2H3 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+14,'s^-1'), n=0, Ea=(319627,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1583,
    label = "C10H12 => A1- + C2H3 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(319627,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1584,
    label = "C10H12 => A1 + C2H2 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12,'s^-1'), n=0, Ea=(292469,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1585,
    label = "C10H12 => A1C2H3 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+13,'s^-1'), n=0, Ea=(292469,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1586,
    label = "C10H12 + H => A1- + C2H4 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(20890.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1587,
    label = "C10H12 + H => C2H5 + A1C2H3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+12,'cm^3/(mol*s)'), n=0, Ea=(20890.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1588,
    label = "C10H12 + H => C7H7 + C3H6",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(20890.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1589,
    label = "C10H12 + H => C2H4 + A1C2H3 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(20890.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1590,
    label = "C10H12 + OH => C7H8 + HCO + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12,'cm^3/(mol*s)'), n=0, Ea=(8356.29,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1591,
    label = "C10H12 + O2 => C10H11 + HO2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.726e+07,'cm^3/(mol*s)'), n=2, Ea=(170144,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1592,
    label = "C10H12 + H => C10H11 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3.851e+07,'cm^3/(mol*s)'), n=2, Ea=(16506,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1593,
    label = "C10H12 + OH => C10H11 + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6.39e+06,'cm^3/(mol*s)'), n=2, Ea=(-9441.83,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1594,
    label = "C10H12 + O => C10H11 + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.165e+07,'cm^3/(mol*s)'), n=2, Ea=(10777.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1595,
    label = "C10H12 + HO2 => C10H11 + H2O2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(862000,'cm^3/(mol*s)'), n=2, Ea=(49668.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1596,
    label = "C10H12 + HCO => C10H11 + CH2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.021e+06,'cm^3/(mol*s)'), n=2, Ea=(51643.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1597,
    label = "C10H12 + CH3 => C10H11 + CH4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(624500,'cm^3/(mol*s)'), n=2, Ea=(20352.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1598,
    label = "C10H12 + C2H5 => C10H11 + C2H6",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(367700,'cm^3/(mol*s)'), n=2, Ea=(31996.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1599,
    label = "C10H11 => INDENE + CH3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+13,'s^-1'), n=0, Ea=(127433,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1600,
    label = "C10H11 => A2 + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(127433,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1601,
    label = "DECALIN => C5H9 + C5H9",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+16,'s^-1'), n=0, Ea=(346784,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1602,
    label = "DECALIN => cyC6H10 + C2H4 + C2H4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+16,'s^-1'), n=0, Ea=(338428,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1603,
    label = "DECALIN + H => RDECALIN + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.813e+07,'cm^3/(mol*s)'), n=2, Ea=(16506,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1604,
    label = "DECALIN + OH => RDECALIN + H2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7.988e+06,'cm^3/(mol*s)'), n=2, Ea=(-9441.83,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1605,
    label = "DECALIN + O => RDECALIN + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.707e+07,'cm^3/(mol*s)'), n=2, Ea=(10777.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1606,
    label = "DECALIN + HCO => RDECALIN + CH2O",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.526e+06,'cm^3/(mol*s)'), n=2, Ea=(51643.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1607,
    label = "DECALIN + CH3 => RDECALIN + CH4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(780600,'cm^3/(mol*s)'), n=2, Ea=(20352.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1608,
    label = "DECALIN + C2H5 => RDECALIN + C2H6",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(459700,'cm^3/(mol*s)'), n=2, Ea=(31996.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1609,
    label = "DECALIN + HO2 => RDECALIN + H2O2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.6e+13,'cm^3/(mol*s)'), n=0, Ea=(66273.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1610,
    label = "DECALIN + O2 => RDECALIN + HO2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(5e+14,'cm^3/(mol*s)'), n=0, Ea=(186750,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1611,
    label = "RDECALIN => C3H5 + C2H4 + C5H8",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+12,'s^-1'), n=0, Ea=(249434,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1612,
    label = "RDECALIN => nC4H7 + cyC6H10",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1613,
    label = "RDECALIN => pC4H9 + cyC6H8",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1614,
    label = "RDECALIN => CH3 + C4H6 + C5H8",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1615,
    label = "RDECALIN => nC3H7 + C7H8 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1616,
    label = "RDECALIN => CH3 + INDENE + H2 + H2 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1617,
    label = "RDECALIN => C2H5 + ebz + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1618,
    label = "RDECALIN => cyC6H11 + C4H6",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1619,
    label = "RDECALIN => nC3H7 + C2H4 + cyclopentadiene",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12,'s^-1'), n=0, Ea=(125344,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1620,
    label = "INDENYL + C3H3 => P2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1621,
    label = "A1- + A1 <=> P2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+23,'cm^3/(mol*s)'), n=-2.92, Ea=(61942.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1622,
    label = "INDENE + C3H3 => P2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.55e+14,'cm^3/(mol*s)'), n=0, Ea=(215446,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1623,
    label = "A1- + A1- <=> P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+19,'cm^3/(mol*s)'), n=-2.05, Ea=(12056,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1624,
    label = "P2 <=> INDENE + C3H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'s^-1'), n=0, Ea=(457296,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1625,
    label = "P2 <=> P2- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+19,'s^-1'), n=-2.72, Ea=(476419,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1626,
    label = "P2 + H <=> P2- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1627,
    label = "P2 + OH <=> P2- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+08,'cm^3/(mol*s)'), n=1.42, Ea=(6402.14,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1628,
    label = "P2 + CH3 <=> P2- + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(62608,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1629,
    label = "P2- + O2 <=> A2 + HCO + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(30763.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1630,
    label = "A1- + A1- <=> P2- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.23,'cm^3/(mol*s)'), n=4.62, Ea=(120560,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1631,
    label = "iC4H5 + A1 => A2 + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(12500.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1632,
    label = "C4H6 + A1- => A2 + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(5e+11,'cm^3/(mol*s)'), n=0, Ea=(12500.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1633,
    label = "C5H5 + C5H5 <=> A2 + H + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(3e+16,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')), Arrhenius(A=(453000,'cm^3/(mol*s)'), n=1.83, Ea=(150001,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1634,
    label = "A1- + iC4H3 <=> A2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.18e+23,'cm^3/(mol*s)'), n=-3.2, Ea=(17709.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1635,
    label = "A1- + C4H4 <=> A2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1636,
    label = "C7H7 + C3H3 => A2 + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1637,
    label = "A1C2H3* + C2H2 <=> A2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(27437.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1638,
    label = "A1C2H2 + C2H2 <=> A2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(22449.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1639,
    label = "INDENYL + CH3 <=> A2 + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+18,'cm^3/(mol*s)'), n=0, Ea=(303478,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1640,
    label = "INDENE + CH2 => A2 + H + H",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(36334.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1641,
    label = "INDENE + CH2(S) <=> A2 + H + H",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(36334.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1642,
    label = "A2 + O <=> CH2CO + A1C2H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(18832.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1643,
    label = "A2 + O => INDENYL + CO + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3.6e+14,'cm^3/(mol*s)'), n=0, Ea=(183692,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1644,
    label = "A2 + O <=> A1C2H2 + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(174604,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1645,
    label = "A2 + O <=> A1C2H3* + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(174604,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1646,
    label = "A2 + O <=> A2- + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1647,
    label = "A2 + H <=> A2- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1648,
    label = "A2 + OH <=> A2- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+13,'cm^3/(mol*s)'), n=0, Ea=(19123.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1649,
    label = "A2 + OH => A1C2H + CH2CO + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(44066.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1650,
    label = "A2 + CH3 <=> A2- + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(62608,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1651,
    label = "A2 + C2H <=> A2- + C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1652,
    label = "A2 + C2H <=> A2C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1653,
    label = "A1C2H- + C2H2 <=> A2-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(42403.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1654,
    label = "A2- + O2 => A1C2H + HCO + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(30763.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1655,
    label = "A2- + O => INDENYL + CO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1656,
    label = "A2- + H <=> A2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1657,
    label = "A2- + HO2 => INDENYL + CO + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1658,
    label = "A2- + C2H2 <=> A2C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+24,'cm^3/(mol*s)'), n=-3.06, Ea=(93953.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1659,
    label = "A1- + iC4H3 <=> A2- + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e-10,'cm^3/(mol*s)'), n=7.1, Ea=(6536.75,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1660,
    label = "A2C2H + H <=> A2C2H* + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1661,
    label = "A2C2H + OH <=> A2- + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000218,'cm^3/(mol*s)'), n=4.5, Ea=(-4157.24,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1662,
    label = "A2C2H + OH <=> A2C2H* + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+13,'cm^3/(mol*s)'), n=0, Ea=(19123.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1663,
    label = "INDENYL + C3H3 => A2C2H + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1664,
    label = "A2 + CH2 <=> A2CH3",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(36334.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.4e+13,'cm^3/(mol*s)'), n=0, Ea=(36334.2,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified

Originally from reaction library: Unclassified
""",
)

entry(
    index = 1665,
    label = "A2CH3 <=> A2- + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+16,'s^-1'), n=0, Ea=(405746,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1666,
    label = "A2CH3 <=> A2CH2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+15,'s^-1'), n=0, Ea=(371657,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1667,
    label = "A2CH3 + O2 <=> A2CH2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+14,'cm^3/(mol*s)'), n=0, Ea=(173008,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1668,
    label = "A2CH3 + O <=> A2CH2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(5379.46,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1669,
    label = "A2CH3 + H <=> A2CH2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(39.8,'cm^3/(mol*s)'), n=3.44, Ea=(12970.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1670,
    label = "A2CH3 + H <=> A2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(21201.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1671,
    label = "A2CH3 + OH <=> A2CH2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.19e+08,'cm^3/(mol*s)'), n=1, Ea=(3658.37,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1672,
    label = "A2CH3 + HO2 <=> A2CH2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1673,
    label = "A2CH3 + CH3 <=> A2CH2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+12,'cm^3/(mol*s)'), n=0, Ea=(45729.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1674,
    label = "A2CH3 + C2H3 <=> A2CH2 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.1e+12,'cm^3/(mol*s)'), n=0, Ea=(31179.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1675,
    label = "A2CH3 + A2- <=> A2CH2 + A2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+12,'cm^3/(mol*s)'), n=0, Ea=(18292.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1676,
    label = "A2CH2 + O <=> A2CHO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.65e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1677,
    label = "A2CH2 + O2 <=> A2CHO + H + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.3e+12,'cm^3/(mol*s)'), n=0, Ea=(178749,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1678,
    label = "A2CH2 + HO2 <=> A2CHO + OH + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1679,
    label = "A2CH2 + OH => A2CHO + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1680,
    label = "A2CH2 + OH <=> C11H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1681,
    label = "C11H10O + O2 <=> A2CHO + HO2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+14,'cm^3/(mol*s)'), n=0, Ea=(171898,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1682,
    label = "C11H10O + OH <=> A2CHO + H2O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.2e+09,'cm^3/(mol*s)'), n=1, Ea=(3635.09,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1683,
    label = "C11H10O + H <=> A2CHO + H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+14,'cm^3/(mol*s)'), n=0, Ea=(34924.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1684,
    label = "C11H10O + H <=> A2 + CH2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(21402.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1685,
    label = "A2CHO <=> A2CO + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+15,'s^-1'), n=0, Ea=(347958,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1686,
    label = "A2CHO + O2 <=> A2CO + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.03e+13,'cm^3/(mol*s)'), n=0, Ea=(169022,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1687,
    label = "A2CHO + HO2 <=> A2CO + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.01e+12,'cm^3/(mol*s)'), n=0, Ea=(54350,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1688,
    label = "A2CHO + OH <=> A2CO + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.83e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1689,
    label = "A2CHO + H <=> A2CO + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.2e+10,'cm^3/(mol*s)'), n=1.1, Ea=(13612.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1690,
    label = "A2CHO + H <=> A2 + HCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(21402.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1691,
    label = "A2CHO + O <=> A2CO + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+12,'cm^3/(mol*s)'), n=0, Ea=(7520.44,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1692,
    label = "A2CHO + CH3 <=> A2CO + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8e-08,'cm^3/(mol*s)'), n=6.1, Ea=(8178.53,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1693,
    label = "A2CHO + A2CH2 <=> A2CO + A2CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2770,'cm^3/(mol*s)'), n=2.8, Ea=(23999.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1694,
    label = "A2CHO + A2- <=> A2CO + A2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.01e+11,'cm^3/(mol*s)'), n=0, Ea=(18296,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1695,
    label = "A2CO <=> A2- + CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+14,'s^-1'), n=0, Ea=(122214,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1696,
    label = "A2 + O <=> A2O + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.23e+13,'cm^3/(mol*s)'), n=0, Ea=(22992.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1697,
    label = "A2 + O2 <=> A2- + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.03e+13,'cm^3/(mol*s)'), n=0, Ea=(249434,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1698,
    label = "A2- + HO2 <=> A2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.03e+13,'cm^3/(mol*s)'), n=0, Ea=(4153.08,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1699,
    label = "A2- + O2 <=> A2O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.09e+12,'cm^3/(mol*s)'), n=0, Ea=(31050,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1700,
    label = "INDENYL + CO => A2O",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(9500,'cm^3/(mol*s)'), n=1.4, Ea=(110400,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1701,
    label = "A2O => INDENYL + CO",
    degeneracy = 1.0,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(7.4e+11,'s^-1'), n=0, Ea=(223880,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1702,
    label = "A2O + H <=> A2OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1703,
    label = "A2OH + OH <=> A2O + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.03e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1704,
    label = "A2OH + H <=> A2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.23e+13,'cm^3/(mol*s)'), n=0, Ea=(32957.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1705,
    label = "A2OH + H <=> A2O + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+14,'cm^3/(mol*s)'), n=0, Ea=(51548.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1706,
    label = "A2OH + O <=> A2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+13,'cm^3/(mol*s)'), n=0, Ea=(12051.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1707,
    label = "A2CH2 + O <=> A2- + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.65e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1708,
    label = "A2CH2 + HO2 <=> A2- + CH2O + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1709,
    label = "A2CH2 + CH2 <=> A2C2H + H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1710,
    label = "A2CH2 + C3H3 <=> A3 + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1711,
    label = "A1C2H- + C4H4 <=> A2R5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(27437.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1712,
    label = "A1C2H3* + C4H2 <=> A2R5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(22449.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1713,
    label = "A1C2H2 + C4H2 <=> A2R5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(22449.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1714,
    label = "INDENYL + C3H3 => A2R5 + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.3e+13,'cm^3/(mol*s)'), n=0, Ea=(40643.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1715,
    label = "INDENE + C3H3 => A2R5 + H + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.55e+14,'cm^3/(mol*s)'), n=0, Ea=(215446,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1716,
    label = "INDENYL + C3H3 <=> A2R5 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.5e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1717,
    label = "A2- + C2H2 <=> A2R5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+31,'cm^3/(mol*s)'), n=-5.26, Ea=(87302,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1718,
    label = "A2C2H* + H <=> A2R5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1719,
    label = "A2C2H + H <=> A2R5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.6e+37,'cm^3/(mol*s)'), n=-7.03, Ea=(96032.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1720,
    label = "A2R5- + H <=> A2R5",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(6.6e+75,'cm^6/(mol^2*s)'), n=-16.3, Ea=(29.1007,'J/mol'), T0=(1,'K')), alpha=1, T3=(0.1,'K'), T1=(585,'K'), T2=(6113,'K'), efficiencies={'C': 3.0, 'CC': 3.0, 'O': 6.5, 'O=C=O': 1.5, '[Ar]': 0.2, '[C-]#[O+]': 0.75, '[O][O]': 0.4}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1721,
    label = "A2R5 <=> A1C2H + C4H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+16,'s^-1'), n=0, Ea=(482239,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1722,
    label = "A2R5 + O <=> A2R5- + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1723,
    label = "A2R5 + O => A2- + HCCO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1724,
    label = "A2R5 + H <=> A2R5- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1725,
    label = "A2R5 + OH <=> A2R5- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+08,'cm^3/(mol*s)'), n=1.42, Ea=(6027.99,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1726,
    label = "A2R5 + OH <=> A2- + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(41572.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1727,
    label = "A2R5 + CH3 <=> A2R5- + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(62608,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1728,
    label = "A2R5 + OH => A2 + HCCO",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(176,'cm^3/(mol*s)'), n=3.25, Ea=(23240.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1729,
    label = "A3- + H <=> A3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1730,
    label = "A1C2H + A1- <=> A3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+23,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1731,
    label = "A1C2H- + A1 <=> A3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+23,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1732,
    label = "A2- + C4H4 <=> A3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1733,
    label = "P2- + C2H2 <=> A3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.64e+06,'cm^3/(mol*s)'), n=1.97, Ea=(30181.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1734,
    label = "A2R5 + C2H2 => A3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(27651.5,'cm^3/(mol*s)'), n=2.45, Ea=(121689,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1735,
    label = "A2 + C4H2 => A3",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(27651.5,'cm^3/(mol*s)'), n=2.45, Ea=(121689,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1736,
    label = "INDENYL + C5H5 => A3 + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1737,
    label = "A3 + O <=> A2C2H + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(22989.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1738,
    label = "A3 + O <=> A3- + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1739,
    label = "A3 + O => HCCO + P2-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(174604,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1740,
    label = "A3 + H <=> A3- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1741,
    label = "A3 + OH <=> A3- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+12,'cm^3/(mol*s)'), n=1.42, Ea=(6260.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1742,
    label = "A3 + OH => A2C2H + CH2CO + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(41572.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1743,
    label = "A3 + OH <=> CH2CO + P2-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(133032,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1744,
    label = "A3 + CH3 <=> A3- + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(62608,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1745,
    label = "A3- + O2 => CO + HCO + A2R5",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(30763.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1746,
    label = "A2- + C4H2 <=> A3-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1747,
    label = "A2C2H* + C2H2 <=> A3-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+62,'cm^3/(mol*s)'), n=-14.56, Ea=(137605,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1748,
    label = "A2R5- + C2H2 <=> A3-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+37,'cm^3/(mol*s)'), n=-8.02, Ea=(68178.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1749,
    label = "A3 + CH2 <=> A3CH3",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(2.2e+13,'cm^3/(mol*s)'), n=0, Ea=(29898.8,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.2e+13,'cm^3/(mol*s)'), n=0, Ea=(29898.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified

Originally from reaction library: Unclassified
""",
)

entry(
    index = 1750,
    label = "A3CH3 <=> A3CH2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+15,'s^-1'), n=0, Ea=(371657,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1751,
    label = "A3CH3 + O <=> A3CH2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(5342.05,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1752,
    label = "A3CH3 + H <=> A3CH2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+14,'cm^3/(mol*s)'), n=0, Ea=(34920.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1753,
    label = "A3CH3 + H <=> A3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+13,'cm^3/(mol*s)'), n=0, Ea=(21201.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1754,
    label = "A3CH3 + OH <=> A3CH2 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+13,'cm^3/(mol*s)'), n=0, Ea=(10601,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1755,
    label = "A3CH3 + HO2 <=> A3CH2 + H2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(58201.3,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1756,
    label = "A3CH3 + O2 <=> A3CH2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+14,'cm^3/(mol*s)'), n=0, Ea=(173008,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1757,
    label = "A3CH3 + CH3 <=> A3CH2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.58e+12,'cm^3/(mol*s)'), n=0, Ea=(45729.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1758,
    label = "A3CH2 + H <=> A3- + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+16,'cm^3/(mol*s)'), n=0, Ea=(405746,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1759,
    label = "A3CH2 + O <=> A3- + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.65e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1760,
    label = "A3CH2 + HO2 => A3- + CH2O + OH",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1761,
    label = "A3 + C2H <=> A3C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1762,
    label = "A3C2H + OH <=> A3- + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.000218,'cm^3/(mol*s)'), n=4.5, Ea=(-4157.24,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1763,
    label = "A3- + C2H2 <=> A3C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+26,'cm^3/(mol*s)'), n=-3.44, Ea=(125549,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1764,
    label = "A3C2H + H <=> A3C2H* + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(303,'cm^3/(mol*s)'), n=3.3, Ea=(23862.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1765,
    label = "A3CH2 + CH2 <=> A4 + H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.4e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1766,
    label = "A4- + H <=> A4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1767,
    label = "C4H2 + A2R5 => A4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(500,'cm^3/(mol*s)'), n=2.231, Ea=(-4732.38,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1768,
    label = "A1C2H + A1C2H- <=> A4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1769,
    label = "A1C2H2 + A1C2H => A4 + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1770,
    label = "A1C2H3* + A1C2H => A4 + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1771,
    label = "INDENYL + C7H7 => A4 + H2 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.3e+37,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1772,
    label = "INDENYL + INDENYL => A4 + C2H2 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.3e+36,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1773,
    label = "A2 + A1- <=> A4 + H + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(20786.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1774,
    label = "A2- + A1 <=> A4 + H + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(20786.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1775,
    label = "A2- + A1- => A4 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(4.3e+37,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1776,
    label = "A2C2H* + C4H4 <=> A4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1777,
    label = "A2R5- + iC4H3 <=> A4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.4e+23,'cm^3/(mol*s)'), n=-3.2, Ea=(17709.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1778,
    label = "A3- + C2H2 <=> A4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.6e+24,'cm^3/(mol*s)'), n=-3.36, Ea=(73998.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1779,
    label = "A3C2H + H <=> A4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+38,'cm^3/(mol*s)'), n=-7.39, Ea=(86470.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1780,
    label = "A1C2H2 + A1C2H- => A4 + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(3e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1781,
    label = "A1C2H3* + A1C2H- <=> A4 + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1782,
    label = "A4 + O <=> A3- + HCCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(174604,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1783,
    label = "A4 + H <=> A4- + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1784,
    label = "A4 + OH <=> A4- + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+08,'cm^3/(mol*s)'), n=1.42, Ea=(6092.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1785,
    label = "A4 + OH <=> A3- + CH2CO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(174604,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1786,
    label = "A4 + CH3 <=> A4- + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(303,'cm^3/(mol*s)'), n=3.3, Ea=(23862.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1787,
    label = "A2 + C6H <=> A4-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+37,'cm^3/(mol*s)'), n=-8.02, Ea=(68178.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1788,
    label = "A2- + C6H2 <=> A4-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+37,'cm^3/(mol*s)'), n=-8.02, Ea=(68178.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1789,
    label = "A2R5- + C4H2 => A4-",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(7e+37,'cm^3/(mol*s)'), n=-8.02, Ea=(68178.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1790,
    label = "A4- + O2 <=> CO + CO + A3-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(30763.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1791,
    label = "A4- + C2H2 <=> A4C2H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+26,'cm^3/(mol*s)'), n=-3.44, Ea=(125549,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1792,
    label = "A4C2H + H <=> A4C2H* + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+14,'cm^3/(mol*s)'), n=0, Ea=(66515.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1793,
    label = "A4C2H* + C2H2 <=> BAPYR*S",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+37,'cm^3/(mol*s)'), n=-8.02, Ea=(68178.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1794,
    label = "A4C2H* + H <=> BGHIF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1795,
    label = "A4C2H + H <=> BGHIF + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.6e+37,'cm^3/(mol*s)'), n=-7.03, Ea=(96032.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1796,
    label = "P2- + C6H2 <=> BGHIF + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1797,
    label = "A3C2H* + C2H2 <=> BGHIF + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+16,'cm^3/(mol*s)'), n=-1.33, Ea=(27437.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1798,
    label = "A2R5 + C6H2 => BGHIF",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(241.296,'cm^3/(mol*s)'), n=2.23132, Ea=(-4732.38,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1799,
    label = "A1C2H- + A2 => BGHIF + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+25,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1800,
    label = "A1C2H + A2- => BGHIF + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+25,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1801,
    label = "INDENYL + INDENYL => BGHIF + H2 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.3e+38,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1802,
    label = "A2 + Octatetrayne => BGHIF",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(241.296,'cm^3/(mol*s)'), n=2.23132, Ea=(-4732.38,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1803,
    label = "A2R5- + A1 => BGHIF + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.1e+25,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1804,
    label = "BGHIF + O <=> HCCO + A4-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1805,
    label = "BGHIF + OH <=> CH2CO + A4-",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(44066.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1806,
    label = "A2R5- + A1- => BGHIF + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1807,
    label = "A3- + C4H4 <=> C18H12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1808,
    label = "INDENE + INDENYL => C18H12 + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1809,
    label = "A2C2H + A1- <=> C18H12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1810,
    label = "A2C2H* + A1 <=> C18H12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1811,
    label = "INDENYL + INDENYL => C18H12 + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1812,
    label = "C18H12 + O <=> C18H11 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(61527.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1813,
    label = "C18H12 + H <=> C18H11 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(303,'cm^3/(mol*s)'), n=3.3, Ea=(23862.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1814,
    label = "C18H12 + OH <=> C18H11 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+08,'cm^3/(mol*s)'), n=1.42, Ea=(6092.6,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1815,
    label = "C18H11 + O2 => HCO + CO + A4",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(30763.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1816,
    label = "C18H11 + H <=> BGHIF + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1817,
    label = "C18H11 + C2H => BAPYR",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(5.24e+14,'cm^3/(mol*s)'), n=-0.5, Ea=(2910.07,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1818,
    label = "C18H11 + C2H2 <=> BAPYR + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+24,'cm^3/(mol*s)'), n=-3.36, Ea=(73998.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1819,
    label = "A3C2H* + C4H4 <=> BAPYR + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1820,
    label = "A4- + C4H4 <=> BAPYR + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.3e+33,'cm^3/(mol*s)'), n=-5.7, Ea=(106010,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1821,
    label = "P2 + A1C2H- => BAPYR + H2 + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.1e+24,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1822,
    label = "P2- + A1C2H3* => BAPYR + H2 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.3e+38,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1823,
    label = "P2- + A1C2H2 => BAPYR + H2 + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(8.3e+38,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1824,
    label = "A2R5- + A1C2H- <=> BAPYR",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.3e+38,'cm^3/(mol*s)'), n=-6.3, Ea=(187325,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1825,
    label = "A2R5 + A1C2H- <=> BAPYR + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+25,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1826,
    label = "A2R5- + A1C2H <=> BAPYR + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1e+25,'cm^3/(mol*s)'), n=-2.92, Ea=(66598.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1827,
    label = "BAPYR + O <=> HCCO + C18H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(174604,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1828,
    label = "BAPYR + OH <=> CH2CO + C18H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+13,'cm^3/(mol*s)'), n=0, Ea=(44066.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1829,
    label = "A2C2H* + A1C2H2 <=> BAPYR + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1830,
    label = "A2C2H* + A1C2H3* <=> BAPYR + H + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1831,
    label = "P2- + A1C2H- => BAPYR + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6e+17,'cm^3/(mol*s)'), n=0, Ea=(196429,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1832,
    label = "BAPYR*S + H <=> BAPYR",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1833,
    label = "BAPYR*S + O2 => HCO + CO + BGHIF",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(30763.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1834,
    label = "C3H2 + C3H2 <=> C6H2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1835,
    label = "C4H + H <=> C4H2",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1e+17,'cm^3/(mol*s)'), n=-1, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.75e+33,'cm^6/(mol^2*s)'), n=-4.8, Ea=(7938.44,'J/mol'), T0=(1,'K')), alpha=0.6464, T3=(132,'K'), T1=(1315,'K'), T2=(5566,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1836,
    label = "C4H2 + OH <=> C4H + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.15e+09,'cm^3/(mol*s)'), n=1.03, Ea=(90862.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1837,
    label = "C4H2 + C2H <=> C6H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.3e+13,'cm^3/(mol*s)'), n=0.28, Ea=(-307.635,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1838,
    label = "C2H2 + C4H <=> C6H2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1839,
    label = "C4H + C2H <=> C6H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1840,
    label = "C6H + H <=> C6H2",
    degeneracy = 1.0,
    kinetics = Troe(arrheniusHigh=Arrhenius(A=(1e+17,'cm^3/(mol*s)'), n=-1, Ea=(0,'J/mol'), T0=(1,'K')), arrheniusLow=Arrhenius(A=(3.75e+33,'cm^6/(mol^2*s)'), n=-4.8, Ea=(7938.44,'J/mol'), T0=(1,'K')), alpha=0.6464, T3=(132,'K'), T1=(1315,'K'), T2=(5566,'K'), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1841,
    label = "C6H2 + OH <=> C6H + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.15e+09,'cm^3/(mol*s)'), n=1.03, Ea=(90862.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1842,
    label = "C6H2 + C2H <=> Octatetrayne + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1843,
    label = "C4H2 + C4H <=> Octatetrayne + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1844,
    label = "C2H2 + C6H <=> Octatetrayne + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1845,
    label = "C4H2 + C4H2 => Octatetrayne + H + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.51e+14,'cm^3/(mol*s)'), n=0, Ea=(233971,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1846,
    label = "C4H2 + C4H2 => Octatetrayne + H2",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(1.51e+13,'cm^3/(mol*s)'), n=0, Ea=(178409,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1847,
    label = "Octatetrayne <=> C8H + H",
    degeneracy = 1.0,
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(5e+16,'cm^3/(mol*s)'), n=0, Ea=(335073,'J/mol'), T0=(1,'K')), efficiencies={}),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1848,
    label = "Octatetrayne + OH <=> C8H + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.15e+09,'cm^3/(mol*s)'), n=1.03, Ea=(90862.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1849,
    label = "Octatetrayne + C2H <=> Decapentayne + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1850,
    label = "C6H2 + C4H <=> Decapentayne + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1851,
    label = "C4H2 + C6H <=> Decapentayne + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1852,
    label = "C2H2 + C8H => Decapentayne + H",
    degeneracy = 1.0,
    reversible = False,
    kinetics = Arrhenius(A=(6.4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1853,
    label = "C8H + C2H <=> Decapentayne",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1854,
    label = "C6H + C4H <=> Decapentayne",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1855,
    label = "iC10H22 <=> p-iC10H21 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(5.748e+17,'s^-1'), n=-0.36, Ea=(422827,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.919e+17,'s^-1'), n=-0.36, Ea=(419484,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1856,
    label = "iC10H22 <=> s-iC10H21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.299e+18,'s^-1'), n=-0.721, Ea=(412507,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1857,
    label = "iC10H22 <=> t-iC10H21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.146e+19,'s^-1'), n=-0.941, Ea=(398719,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1858,
    label = "CH3 + iC9H19 <=> iC10H22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1859,
    label = "iC3H7 + iC7H15 <=> iC10H22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1860,
    label = "iC4H9 + iC6H13 <=> iC10H22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1861,
    label = "iC5H11 + iC5H11 <=> iC10H22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1862,
    label = "iC10H22 + H <=> p-iC10H21 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(564000,'cm^3/(mol*s)'), n=2.75, Ea=(26275.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1863,
    label = "iC10H22 + H <=> s-iC10H21 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(574000,'cm^3/(mol*s)'), n=2.49, Ea=(17255,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1864,
    label = "iC10H22 + H <=> t-iC10H21 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+06,'cm^3/(mol*s)'), n=2.4, Ea=(10807.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1865,
    label = "iC10H22 + O <=> p-iC10H21 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(885000,'cm^3/(mol*s)'), n=2.5, Ea=(15250.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1866,
    label = "iC10H22 + O <=> s-iC10H21 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(191000,'cm^3/(mol*s)'), n=2.71, Ea=(8811.68,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1867,
    label = "iC10H22 + O <=> t-iC10H21 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(766000,'cm^3/(mol*s)'), n=2.41, Ea=(3736.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1868,
    label = "iC10H22 + OH <=> p-iC10H21 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.34e+07,'cm^3/(mol*s)'), n=1.8, Ea=(5987.25,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1869,
    label = "iC10H22 + OH <=> s-iC10H21 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.6e+06,'cm^3/(mol*s)'), n=2, Ea=(-4740.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1870,
    label = "iC10H22 + OH <=> t-iC10H21 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.4e+06,'cm^3/(mol*s)'), n=1.9, Ea=(-6071.23,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1871,
    label = "iC10H22 + CH3 <=> p-iC10H21 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.441,'cm^3/(mol*s)'), n=3.87, Ea=(28484.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1872,
    label = "iC10H22 + CH3 <=> s-iC10H21 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(105000,'cm^3/(mol*s)'), n=2.26, Ea=(30488.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1873,
    label = "iC10H22 + CH3 <=> t-iC10H21 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17900,'cm^3/(mol*s)'), n=2.33, Ea=(25719.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1874,
    label = "p-iC10H21 <=> iC9H18 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1875,
    label = "p-iC10H21 <=> s-iC10H20 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1876,
    label = "p-iC10H21 <=> C3H6 + iC7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1877,
    label = "s-iC10H21 <=> s-iC10H20 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1878,
    label = "s-iC10H21 <=> t-iC10H20 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1879,
    label = "s-iC10H21 <=> iC9H18 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1880,
    label = "s-iC10H21 <=> iC7H14 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1881,
    label = "s-iC10H21 <=> iC6H12 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1882,
    label = "s-iC10H21 + O2 <=> t-iC10H20 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1883,
    label = "s-iC10H21 + O2 <=> s-iC10H20 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1884,
    label = "t-iC10H21 <=> s-iC10H20 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1885,
    label = "t-iC10H21 <=> t-iC10H20 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1886,
    label = "t-iC10H21 <=> iC4H8 + iC6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1887,
    label = "t-iC10H21 + O2 <=> t-iC10H20 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1888,
    label = "p-iC10H21 <=> s-iC10H21",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(3.43e+06,'s^-1'), n=0.871, Ea=(36974.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.51e+10,'s^-1'), n=-0.354, Ea=(47848.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.38e+11,'s^-1'), n=-0.551, Ea=(51475.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.81e+09,'s^-1'), n=0.123, Ea=(48626.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.33e+06,'s^-1'), n=1.024, Ea=(43517.9,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1889,
    label = "p-iC10H21 <=> t-iC10H21",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(12,'s^-1'), n=2.588, Ea=(49923.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.48e+10,'s^-1'), n=-0.089, Ea=(72002.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.02e+14,'s^-1'), n=-1.009, Ea=(82060.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.82e+11,'s^-1'), n=-0.267, Ea=(79952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.56e+07,'s^-1'), n=1.067, Ea=(72592.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1890,
    label = "s-iC10H21 <=> t-iC10H21",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(2.04e+07,'s^-1'), n=0.769, Ea=(64822.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.18e+13,'s^-1'), n=-1.022, Ea=(81948.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.39e+14,'s^-1'), n=-1.128, Ea=(87320.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.39e+10,'s^-1'), n=0.18, Ea=(81889.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(219000,'s^-1'), n=1.765, Ea=(73002.7,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1891,
    label = "s-iC10H20 <=> s-iC10H19 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+19,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1892,
    label = "s-iC10H20 <=> iC9H17 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+17,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1893,
    label = "s-iC10H20 <=> iC7H13 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1894,
    label = "s-iC10H20 <=> iC6H11 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1895,
    label = "t-iC10H20 <=> t-iC10H19 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+19,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1896,
    label = "t-iC10H20 <=> s-iC10H19 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+19,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1897,
    label = "t-iC10H20 <=> iC9H17 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+17,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1898,
    label = "t-iC10H20 <=> iC6H13 + iC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1899,
    label = "t-iC10H20 <=> iC7H13 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1900,
    label = "t-iC10H20 <=> iC6H11 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1901,
    label = "t-iC10H20 <=> iC5H11 + iC5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1902,
    label = "s-iC10H19 <=> iC6H11 + iC4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1903,
    label = "s-iC10H19 <=> iC5H10 + iC5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1904,
    label = "t-iC10H19 <=> iC6H12 + iC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1905,
    label = "t-iC10H19 <=> iC6H11 + iC4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1906,
    label = "t-iC10H19 <=> iC5H10 + iC5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1907,
    label = "iC9H19 <=> iC9H18 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(157975,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1908,
    label = "iC9H19 <=> iC6H13 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.33e+12,'s^-1'), n=0.498, Ea=(116319,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1909,
    label = "iC9H18 <=> iC9H17 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.88e+19,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1910,
    label = "iC9H18 <=> nC8H15 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+17,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1911,
    label = "iC9H18 <=> iC6H13 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1912,
    label = "iC9H18 <=> C6H11 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1913,
    label = "iC9H18 <=> iC5H11 + nC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1914,
    label = "iC9H18 <=> C5H9 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1915,
    label = "iC9H18 + H <=> iC9H17 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(16213.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1916,
    label = "iC9H18 + OH <=> iC9H17 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(5113.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1917,
    label = "iC9H18 + O <=> iC9H17 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(16628.9,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1918,
    label = "iC9H18 + CH3 <=> iC9H17 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+11,'cm^3/(mol*s)'), n=0, Ea=(30514.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1919,
    label = "iC9H17 <=> iC6H12 + C3H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1920,
    label = "iC9H17 <=> C6H10 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1921,
    label = "iC9H17 <=> iC5H10 + nC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1922,
    label = "iC9H17 <=> C5H9 + iC4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1923,
    label = "iC9H17 <=> C5H8 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(186244,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1924,
    label = "2-methyldecane <=> p-iC11H23 + H",
    degeneracy = 1.0,
    kinetics = MultiArrhenius(arrhenius=[Arrhenius(A=(5.748e+17,'s^-1'), n=-0.36, Ea=(422827,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.919e+17,'s^-1'), n=-0.36, Ea=(419484,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1925,
    label = "2-methyldecane <=> s-iC11H23 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.299e+18,'s^-1'), n=-0.721, Ea=(412507,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1926,
    label = "2-methyldecane <=> t-iC11H23 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.146e+19,'s^-1'), n=-0.941, Ea=(398719,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1927,
    label = "CH3 + sC10H21 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1928,
    label = "CH3 + p-iC10H21 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1929,
    label = "iC9H19 + C2H5 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1930,
    label = "nC8H17 + iC3H7 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1931,
    label = "p-iC8H17 + nC3H7 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1932,
    label = "C7H15 + iC4H9 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1933,
    label = "iC7H15 + pC4H9 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1934,
    label = "iC6H13 + C5H11 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1935,
    label = "C6H13 + iC5H11 <=> 2-methyldecane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1936,
    label = "2-methyldecane + H <=> p-iC11H23 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(564000,'cm^3/(mol*s)'), n=2.75, Ea=(26275.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1937,
    label = "2-methyldecane + H <=> s-iC11H23 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.02e+06,'cm^3/(mol*s)'), n=2.49, Ea=(17255,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1938,
    label = "2-methyldecane + H <=> t-iC11H23 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(602000,'cm^3/(mol*s)'), n=2.4, Ea=(10807.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1939,
    label = "2-methyldecane + O <=> p-iC11H23 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(885000,'cm^3/(mol*s)'), n=2.5, Ea=(15250.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1940,
    label = "2-methyldecane + O <=> s-iC11H23 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(334000,'cm^3/(mol*s)'), n=2.71, Ea=(8811.68,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1941,
    label = "2-methyldecane + O <=> t-iC11H23 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(383000,'cm^3/(mol*s)'), n=2.41, Ea=(3736.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1942,
    label = "2-methyldecane + OH <=> p-iC11H23 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.34e+07,'cm^3/(mol*s)'), n=1.8, Ea=(5987.25,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1943,
    label = "2-methyldecane + OH <=> s-iC11H23 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.3e+06,'cm^3/(mol*s)'), n=2, Ea=(-4740.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1944,
    label = "2-methyldecane + OH <=> t-iC11H23 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+06,'cm^3/(mol*s)'), n=1.9, Ea=(-6071.23,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1945,
    label = "2-methyldecane + CH3 <=> p-iC11H23 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.441,'cm^3/(mol*s)'), n=3.87, Ea=(28484.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1946,
    label = "2-methyldecane + CH3 <=> s-iC11H23 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(190000,'cm^3/(mol*s)'), n=2.26, Ea=(30488.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1947,
    label = "2-methyldecane + CH3 <=> t-iC11H23 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8960,'cm^3/(mol*s)'), n=2.33, Ea=(25719.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1948,
    label = "p-iC11H23 <=> s-iC11H22 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1949,
    label = "p-iC11H23 <=> t-iC11H22 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1950,
    label = "p-iC11H23 <=> nC10H20 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1951,
    label = "p-iC11H23 <=> C2H4 + iC9H19",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1952,
    label = "p-iC11H23 <=> nC8H17 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1953,
    label = "p-iC11H23 <=> C8H16 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1954,
    label = "p-iC11H23 + O2 <=> p-iC11H22 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1955,
    label = "s-iC11H23 <=> s-iC11H22 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1956,
    label = "s-iC11H23 <=> t-iC11H22 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1957,
    label = "s-iC11H23 <=> nC10H20 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1958,
    label = "s-iC11H23 <=> p-iC8H17 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1959,
    label = "s-iC11H23 <=> iC9H18 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1960,
    label = "s-iC11H23 <=> iC8H16 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1961,
    label = "s-iC11H23 <=> C8H16 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1962,
    label = "s-iC11H23 <=> iC7H15 + C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1963,
    label = "s-iC11H23 <=> iC7H14 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1964,
    label = "s-iC11H23 <=> C7H14 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1965,
    label = "s-iC11H23 <=> C6H13 + iC5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1966,
    label = "s-iC11H23 <=> iC6H13 + C5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1967,
    label = "s-iC11H23 <=> C6H12 + iC5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1968,
    label = "s-iC11H23 <=> iC6H12 + C5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1969,
    label = "s-iC11H23 + O2 <=> p-iC11H22 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1970,
    label = "s-iC11H23 + O2 <=> s-iC11H22 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1971,
    label = "t-iC11H23 <=> p-iC11H22 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1972,
    label = "t-iC11H23 <=> nC10H20 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1973,
    label = "t-iC11H23 <=> iC9H19 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1974,
    label = "t-iC11H23 <=> nC8H17 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1975,
    label = "t-iC11H23 + O2 <=> t-iC11H22 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+11,'cm^3/(mol*s)'), n=0, Ea=(21002.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1976,
    label = "p-iC11H23 <=> s-iC11H23",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(3.43e+06,'s^-1'), n=0.871, Ea=(36974.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.51e+10,'s^-1'), n=-0.354, Ea=(47848.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.38e+11,'s^-1'), n=-0.551, Ea=(51475.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.81e+09,'s^-1'), n=0.123, Ea=(48626.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.33e+06,'s^-1'), n=1.024, Ea=(43517.9,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1977,
    label = "p-iC11H23 <=> t-iC11H23",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(12,'s^-1'), n=2.588, Ea=(49923.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.48e+10,'s^-1'), n=-0.089, Ea=(72002.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.02e+14,'s^-1'), n=-1.009, Ea=(82060.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.82e+11,'s^-1'), n=-0.267, Ea=(79952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.56e+07,'s^-1'), n=1.067, Ea=(72592.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1978,
    label = "s-iC11H23 <=> t-iC11H23",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(2.04e+07,'s^-1'), n=0.769, Ea=(64822.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.18e+13,'s^-1'), n=-1.022, Ea=(81948.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.39e+14,'s^-1'), n=-1.128, Ea=(87320.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.39e+10,'s^-1'), n=0.18, Ea=(81889.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(219000,'s^-1'), n=1.765, Ea=(73002.7,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1979,
    label = "p-iC11H22 <=> s-iC11H21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+17,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1980,
    label = "p-iC11H22 <=> nC8H15 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1981,
    label = "p-iC11H22 <=> C7H13 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1982,
    label = "p-iC11H22 <=> iC7H15 + nC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1983,
    label = "p-iC11H22 <=> iC6H13 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1984,
    label = "s-iC11H22 <=> s-iC11H21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+17,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1985,
    label = "s-iC11H22 <=> t-iC11H21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+17,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1986,
    label = "s-iC11H22 <=> iC9H17 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1987,
    label = "s-iC11H22 <=> nC8H15 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1988,
    label = "s-iC11H22 <=> C7H13 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1989,
    label = "s-iC11H22 <=> C6H11 + iC5H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1990,
    label = "s-iC11H22 <=> iC6H13 + C5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1991,
    label = "t-iC11H22 <=> s-iC11H21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8e+17,'s^-1'), n=0, Ea=(415724,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1992,
    label = "t-iC11H22 <=> iC9H17 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1993,
    label = "t-iC11H22 <=> iC8H15 + nC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1994,
    label = "t-iC11H22 <=> iC7H13 + pC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1995,
    label = "t-iC11H22 <=> C6H13 + iC5H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1996,
    label = "t-iC11H22 <=> C7H15 + iC4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+16,'s^-1'), n=0, Ea=(291007,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1997,
    label = "s-iC11H21 <=> C6H11 + iC5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(236131,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1998,
    label = "s-iC11H21 <=> iC4H8 + C7H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(236131,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1999,
    label = "t-iC11H21 <=> iC8H15 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(236131,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2000,
    label = "t-iC11H21 <=> C4H8 + iC7H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0, Ea=(236131,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2001,
    label = "a-iC15H31 + H <=> Farnesane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2002,
    label = "b-iC15H31 + H <=> Farnesane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2003,
    label = "c-iC15H31 + H <=> Farnesane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2004,
    label = "d-iC15H31 + H <=> Farnesane",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2005,
    label = "Farnesane <=> b-iC13H27 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+16,'s^-1'), n=0, Ea=(319691,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2006,
    label = "Farnesane <=> d-iC12H25 + iC3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+16,'s^-1'), n=0, Ea=(319691,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2007,
    label = "Farnesane <=> p-iC11H23 + sC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+16,'s^-1'), n=0, Ea=(314038,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2008,
    label = "Farnesane <=> p-iC11H23 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.5e+16,'s^-1'), n=0, Ea=(314038,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2009,
    label = "Farnesane <=> s-iC8H17 + iC7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6e+16,'s^-1'), n=0, Ea=(310130,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2010,
    label = "Farnesane + H <=> a-iC15H31 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(752000,'cm^3/(mol*s)'), n=2.75, Ea=(26275.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2011,
    label = "Farnesane + H <=> b-iC15H31 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.02e+06,'cm^3/(mol*s)'), n=2.49, Ea=(17255,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2012,
    label = "Farnesane + H <=> c-iC15H31 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.81e+06,'cm^3/(mol*s)'), n=2.4, Ea=(10807.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2013,
    label = "Farnesane + H <=> d-iC15H31 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(188000,'cm^3/(mol*s)'), n=2.75, Ea=(26275.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2014,
    label = "Farnesane + O <=> a-iC15H31 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14e+06,'cm^3/(mol*s)'), n=2.5, Ea=(15250.4,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2015,
    label = "Farnesane + O <=> b-iC15H31 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(334000,'cm^3/(mol*s)'), n=2.71, Ea=(8811.68,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2016,
    label = "Farnesane + O <=> c-iC15H31 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+06,'cm^3/(mol*s)'), n=2.41, Ea=(3736.52,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2017,
    label = "Farnesane + O <=> d-iC15H31 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.13e+14,'cm^3/(mol*s)'), n=0, Ea=(32844.7,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2018,
    label = "Farnesane + OH <=> a-iC15H31 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.12e+07,'cm^3/(mol*s)'), n=1.8, Ea=(5987.25,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2019,
    label = "Farnesane + OH <=> b-iC15H31 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.3e+06,'cm^3/(mol*s)'), n=2, Ea=(-4740.91,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2020,
    label = "Farnesane + OH <=> c-iC15H31 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.1e+06,'cm^3/(mol*s)'), n=1.9, Ea=(-6071.23,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2021,
    label = "Farnesane + OH <=> d-iC15H31 + H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.05e+10,'cm^3/(mol*s)'), n=0.97, Ea=(6635.78,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2022,
    label = "Farnesane + CH3 <=> a-iC15H31 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.588,'cm^3/(mol*s)'), n=3.87, Ea=(28484.5,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2023,
    label = "Farnesane + CH3 <=> b-iC15H31 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(190000,'cm^3/(mol*s)'), n=2.26, Ea=(30488.8,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2024,
    label = "Farnesane + CH3 <=> c-iC15H31 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(26900,'cm^3/(mol*s)'), n=2.33, Ea=(25719.2,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2025,
    label = "Farnesane + CH3 <=> d-iC15H31 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.904,'cm^3/(mol*s)'), n=3.65, Ea=(29932.1,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2026,
    label = "a-iC15H31 <=> iC15H30 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2027,
    label = "a-iC15H31 <=> iC14H28 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2028,
    label = "a-iC15H31 <=> iC9H18 + iC6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2029,
    label = "a-iC15H31 <=> iC8H16 + iC7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2030,
    label = "a-iC15H31 <=> C4H8 + p-iC11H23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2031,
    label = "a-iC15H31 <=> C3H6 + d-iC12H25",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2032,
    label = "d-iC15H31 <=> C2H4 + b-iC13H27",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2033,
    label = "b-iC15H31 <=> iC15H30 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2034,
    label = "b-iC15H31 <=> iC14H28 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.9e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2035,
    label = "b-iC15H31 <=> p-iC11H22 + iC4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.76e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2036,
    label = "b-iC15H31 <=> iC9H18 + iC6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2037,
    label = "b-iC15H31 <=> iC8H16 + iC7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2038,
    label = "b-iC15H31 <=> iC7H14 + s-iC8H17",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2039,
    label = "b-iC15H31 <=> iC6H12 + iC9H19",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.76e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2040,
    label = "b-iC15H31 <=> iC5H10 + p-iC10H21",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2041,
    label = "b-iC15H31 <=> C4H8 + p-iC11H23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2042,
    label = "c-iC15H31 <=> iC15H30 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2043,
    label = "c-iC15H31 <=> iC14H28 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2044,
    label = "c-iC15H31 <=> iC9H18 + iC6H13",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2045,
    label = "c-iC15H31 <=> iC5H10 + p-iC10H21",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2046,
    label = "c-iC15H31 <=> iC4H8 + p-iC11H23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2047,
    label = "a-iC15H31 <=> b-iC15H31",
    degeneracy = 1.0,
    kinetics = MultiPDepArrhenius(arrhenius=[PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(3.43e+06,'s^-1'), n=0.871, Ea=(36974.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.51e+10,'s^-1'), n=-0.354, Ea=(47848.1,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.38e+11,'s^-1'), n=-0.551, Ea=(51475.7,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.81e+09,'s^-1'), n=0.123, Ea=(48626.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.33e+06,'s^-1'), n=1.024, Ea=(43517.9,'J/mol'), T0=(1,'K'))]), PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(12,'s^-1'), n=2.588, Ea=(49923.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.48e+10,'s^-1'), n=-0.089, Ea=(72002.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.02e+14,'s^-1'), n=-1.009, Ea=(82060.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.82e+11,'s^-1'), n=-0.267, Ea=(79952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.56e+07,'s^-1'), n=1.067, Ea=(72592.8,'J/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2048,
    label = "a-iC15H31 <=> c-iC15H31",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(12,'s^-1'), n=2.588, Ea=(49923.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.48e+10,'s^-1'), n=-0.089, Ea=(72002.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.02e+14,'s^-1'), n=-1.009, Ea=(82060.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(5.82e+11,'s^-1'), n=-0.267, Ea=(79952,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.56e+07,'s^-1'), n=1.067, Ea=(72592.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2049,
    label = "d-iC15H31 <=> a-iC15H31",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(8.75e-10,'s^-1'), n=5.594, Ea=(25673.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.08,'s^-1'), n=2.898, Ea=(45953.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.64e+07,'s^-1'), n=0.848, Ea=(62856.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.73e+09,'s^-1'), n=0.374, Ea=(68981.8,'J/mol'), T0=(1,'K')), Arrhenius(A=(8.06e+06,'s^-1'), n=1.171, Ea=(65429.1,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2050,
    label = "b-iC15H31 <=> c-iC15H31",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(2.04e+07,'s^-1'), n=0.769, Ea=(64822.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(7.18e+13,'s^-1'), n=-1.022, Ea=(81948.3,'J/mol'), T0=(1,'K')), Arrhenius(A=(4.39e+14,'s^-1'), n=-1.128, Ea=(87320.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.39e+10,'s^-1'), n=0.18, Ea=(81889.2,'J/mol'), T0=(1,'K')), Arrhenius(A=(219000,'s^-1'), n=1.765, Ea=(73002.7,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2051,
    label = "d-iC15H31 <=> b-iC15H31",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(7.45e-12,'s^-1'), n=6.23, Ea=(26756.8,'J/mol'), T0=(1,'K')), Arrhenius(A=(0.169,'s^-1'), n=3.25, Ea=(49015.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(2.66e+07,'s^-1'), n=0.926, Ea=(68002.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.01e+09,'s^-1'), n=0.316, Ea=(75282.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.8e+07,'s^-1'), n=1.115, Ea=(71847.8,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2052,
    label = "d-iC15H31 <=> c-iC15H31",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.1,1,10,100,1000],'atm'), arrhenius=[Arrhenius(A=(0.0929,'s^-1'), n=3.131, Ea=(17363.9,'J/mol'), T0=(1,'K')), Arrhenius(A=(21800,'s^-1'), n=1.594, Ea=(29254.5,'J/mol'), T0=(1,'K')), Arrhenius(A=(1.16e+08,'s^-1'), n=0.548, Ea=(38241.6,'J/mol'), T0=(1,'K')), Arrhenius(A=(3.84e+08,'s^-1'), n=0.442, Ea=(40689.4,'J/mol'), T0=(1,'K')), Arrhenius(A=(6.48e+06,'s^-1'), n=0.995, Ea=(38020.4,'J/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2053,
    label = "b-iC13H27 <=> p-iC10H21 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+13,'s^-1'), n=0.17, Ea=(125166,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2054,
    label = "d-iC12H25 <=> p-iC10H21 + C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e+13,'s^-1'), n=0.13, Ea=(120843,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2055,
    label = "s-iC11H23 + C3H5 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2056,
    label = "s-iC11H21 + iC3H7 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2057,
    label = "p-iC10H21 + iC4H7 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2058,
    label = "iC9H19 + iC5H9 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2059,
    label = "iC9H17 + iC5H11 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2060,
    label = "s-iC8H17 + iC6H11 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2061,
    label = "iC6H13 + iC8H15 <=> iC14H28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2062,
    label = "d-iC12H25 + C3H5 <=> iC15H30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2063,
    label = "p-iC11H23 + iC4H7 <=> iC15H30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2064,
    label = "p-iC10H21 + iC5H9 <=> iC15H30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2065,
    label = "iC9H19 + iC6H11 <=> iC15H30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2066,
    label = "iC7H15 + iC8H15 <=> iC15H30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.15e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K')),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2101,
    label = "C2H2 + CH2OH + H + H <=> C3H6OH",
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(1457,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2102,
    label = "C3H4 + OH + H + H <=> C3H6OH",
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(1457,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2103,
    label = "nC4H9O-4 + O2 <=> nC3H7CHO + HO2",
    kinetics = Arrhenius(A=(4.683E+11,'cm^3/(mol*s)'), n=0.33, Ea=(-534.422,'cal/mol'), T0=(1,'K')),
    longDesc =
"""
nC4H9O-4 + O2 = nC3H7CHO + HO2                 4.683E+11    0.330 -534.422   !k51, [k52]
  DUPLICATE 
nC4H9O-4 + O2 = nC3H7CHO + HO2                 0.000        0.000     0.00   !k51, [k52] 
  DUPLICATE 
  PLOG/0.00986923 4.830E+15 -0.8809 445.704/ 
  PLOG/0.0986923 4.910E+15 -0.8828 448.287/ 
  PLOG/0.986923 5.730E+15 -0.9015 473.463/ 
  PLOG/9.86923 1.900E+16 -1.0462 675.802/ 
  PLOG/98.6923 4.500E+17 -1.4228 1369.89/ 
""",
)

entry(
    index = 2104,
    label = "DECALIN => C3H5 + C3H5 + C2H4 + C2H4",
    kinetics = Arrhenius(A=(2e+16,'cm^3/(mol*s)'), n=0, Ea=(41708.5,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2105,
    label = "cyC9H18 => C2H4 + C2H4 + C3H5 + C2H5",
    kinetics = Arrhenius(A=(6.5e+16,'cm^3/(mol*s)'), n=0, Ea=(42211.1,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2106,
    label = "cyC9H18 => C2H4 + C2H4 + C2H4 + C3H6",
    kinetics = Arrhenius(A=(1.3e+17,'cm^3/(mol*s)'), n=0, Ea=(42211.1,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2107,
    label = "RTETRALIN + O2 => CO + CO + A1- + H2 + C2H4",
    kinetics = Arrhenius(A=(2.5e+11,'cm^3/(mol*s)'), n=0, Ea=(502.513,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2108,
    label = "RTETRALIN + HO2 => OH + CO + C2H4 + C7H7",
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
)

entry(
    index = 2109,
    label = "DECALIN => C5H8 + C5H8 + H + H",
    kinetics = Arrhenius(A=(1e+17,'cm^3/(mol*s)'), n=0, Ea=(39196,'cal/mol'), T0=(1,'K')),
)

