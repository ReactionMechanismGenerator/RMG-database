#!/usr/bin/env python
# encoding: utf-8

name = "H2_transfer/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "H3SiSiH + SiH4 <=> Si2H6 + SiH2(S)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73E14, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (37.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["Ho, P.", "Coltrin, M.E.", "Breiland, W.G."],
        title = "Laser-Induced fluorescence measurements and kinetic analysis of Si atom formation in a rotating disk chemical vapor deposition reactor",
        journal = "J. Phys. Chem.",  
        pages = """10138-10147""",
        year = "1994",
    ),
    longDesc = 
u"""
Experimental CVD in a rotating disk reactor, measurement via LIF of Si atoms in both silane and disilane CVD. Showed that Si atoms is produced from bimolecular pathways.
""",
)

entry(
    index = 2,
    label = "Si + Si2H6 <=> SiH2(S) + H3SiSiH",  
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3E15, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (52.7, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["Ho, P.", "Coltrin, M.E.", "Breiland, W.G."],
        title = "Laser-Induced fluorescence measurements and kinetic analysis of Si atom formation in a rotating disk chemical vapor deposition reactor",
        journal = "J. Phys. Chem.",  
        pages = """10138-10147""",
        year = "1994",
    ),
    longDesc = 
u"""
Experimental CVD in a rotating disk reactor, measurement via LIF of Si atoms in both silane and disilane CVD. Showed that Si atoms is produced from bimolecular pathways.
""",
)

entry(
    index = 3,
    label = "SiH4 + Si <=> SiH2(S) + SiH2(T)",      
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03E4, 'cm^3/(mol*s)'),
        n = 2.76, 
        Ea = (49.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Dollet, A.", "de Persis, S."],               
        title = "Pressure-dependent rate coefficients of chemical reactions involving Si2H4 isomerization from QRRK calculations",                       
        journal = "J. Anal. Appl. Pyrolysis",
        pages = """460-470""",
        year = "2007",
    ),
    longDesc = 
u"""
Paper is one of our reaction libraries. Rates determined from QRRK calculations and fitted to SRI and Troe's forms as well as Arrhenius for highP and lowP limits.
""",
)

entry(
    index = 4,
    label = "SiH2(S) + Si2H6 <=> H3SiSiH + SiH4",
    duplicate = True,
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65E15, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (35.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1150, 'K'),
    ),
    reference = Article(
        authors = ["Ho, P.", "Coltrin, M.E.", "Breiland, W.G."],
        title = "Laser-Induced fluorescence measurements and kinetic analysis of Si atom formation in a rotating disk chemical vapor deposition reactor",
        journal = "J. Phys. Chem.",  
        pages = """10138-10147""",
        year = "1994",
    ),
    longDesc = 
u"""
Experimental CVD in a rotating disk reactor, measurement via LIF of Si atoms in both silane and disilane CVD. Showed that Si atoms is produced from bimolecular pathways.
""",
)
