#!/usr/bin/env python
# encoding: utf-8

name = "acetal_hydrolysis/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "glycylglycine + H2O <=> glycine + glycine-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.539e+07,'cm^3/(mol*s)'), n=0, Ea=(98.9,'kJ/mol'), T0=(1,'K'), Tmin=(373,'K'), Tmax=(493,'K')),
    rank = 1,
    shortDesc = """experimental data""",
    longDesc = 
"""
Kinetics of peptide hydrolysis and amino acid decomposition at high temperature.
Yaorong Qian, Michael H. Engel, Stephen A. Macko, Shelly Carpenter, Jody W. Deming,
Geochimica et Cosmochimica Acta, Volume 57, Issue 14, 1993, Pages 3281-3293,
https://doi.org/10.1016/0016-7037(93)90540-D.
Ea from abstract, lnA estimated from Fig 2a
multiplied by 18 ml/mol to account for water as the reactant
""",
)

entry(
    index = 1,
    label = "methylacetamide + H2O <=> methylamine + aceticacid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1658,'cm^3/(mol*s)'), n=0, Ea=(21,'kJ/mol'), T0=(1,'K'), Tmin=(473,'K'), Tmax=(573,'K')),
    rank = 1,
    shortDesc = """experimental data, 0.05M NaOH""",
    longDesc = 
"""
Kinetics and mechanism of N-substituted amide hydrolysis in high-temperature water.
Peigao Duan, Liyi Dai, Phillip E. Savage,
The Journal of Supercritical Fluids, Volume 51, Issue 3, 2010, Pages 362-368,
https://doi.org/10.1016/j.supflu.2009.09.012.
Ea and lnA from Table 4 0.05M NaOH 
multiplied by 18 ml/mol to account for water as the reactant
Rates under neutral and acidic conditions are also available
""",
)

entry(
    index = 2,
    label = "acetamide + H2O <=> ammonia + aceticacid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.54e+11,'cm^3/(mol*s)'), n=0, Ea=(76,'kJ/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = """experimental data""",
    longDesc = 
"""
Kinetics of alkaline hydrolysis of organic esters and amides in neutrally‐buffered solution
Bruce A. Robinson  Jefferson W. Tester
International Journal of Chemical Kinetics May 1990 Vol 22 Issue 5 Pg 431-448
https://doi.org/10.1002/kin.550220502
Table IV
Rates for esters are also available
""",
)

entry(
    index = 3,
    label = "butyramide + H2O <=> ammonia + butyricacid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.25e+10,'cm^3/(mol*s)'), n=0, Ea=(67.6,'kJ/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = """experimental data""",
    longDesc = 
"""
Kinetics of alkaline hydrolysis of organic esters and amides in neutrally‐buffered solution
Bruce A. Robinson  Jefferson W. Tester
International Journal of Chemical Kinetics May 1990 Vol 22 Issue 5 Pg 431-448
https://doi.org/10.1002/kin.550220502
Table IV
Rates for esters are also available
""",
)

entry(
    index = 4,
    label = "benzamide + H2O <=> ammonia + benzoicacid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.47e+08,'cm^3/(mol*s)'), n=0, Ea=(49.3,'kJ/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = """experimental data""",
    longDesc = 
"""
Kinetics of alkaline hydrolysis of organic esters and amides in neutrally‐buffered solution
Bruce A. Robinson  Jefferson W. Tester
International Journal of Chemical Kinetics May 1990 Vol 22 Issue 5 Pg 431-448
https://doi.org/10.1002/kin.550220502
Table IV
Rates for esters are also available
""",
)

entry(
    index = 5,
    label = "asparagine + H2O <=> ammonia + asparticacid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.3e+11,'cm^3/(mol*s)'), n=0, Ea=(20.55,'kcal/mol'), T0=(1,'K')),
    rank = 1,
    shortDesc = """experimental data""",
    longDesc = 
"""
The kinetics of hydrolysis of the amide group in proteins and peptides. 
Part 2. Acid hydrolysis of glycyl- and L-leucyl-L-asparagine
S. J. Leach  and  H. Lindley
Transactions of the Faraday Society Vol 49, 1953
https://doi.org/10.1039/TF9534900921
Figure 3
""",
)

