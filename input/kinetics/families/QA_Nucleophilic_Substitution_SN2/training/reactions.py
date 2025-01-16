#!/usr/bin/env python
# encoding: utf-8

name = "QA_Nucleophilic_Substitution/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C6H5-CH2-(N+)(CH3)3 + (O-)H <=> C6H5-CH2-OH + N(CH3)3", #TMBA degradation
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.14134e+06,'cm^3/(mol*s)'), n=2.18948, Ea=(140.779,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8681935378213759,B=2.373498032935028,E=0.32859248603303737,L=5.004153890392606,A=0.8849787213003473,comment='')),
    rank = 3, # means that the data is calculated using high-level theoretical methods
    longDesc = 
"""
)
