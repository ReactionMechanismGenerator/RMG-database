#!/usr/bin/env python2
# -*- coding: utf-8 -*-

name = "ZhouCyclopentanone"
shortDesc = u"G4 calculations related to Cyclopentanone combustion"
longDesc = u"""
Zhou et al. 2016, Journal of Physical Chemistry A
Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
Decomposition 
  G4 level calculations
"""
entry(
    index = 1,
    label = "CPO + OH <=> H2O + CPO-2",
    degeneracy = 4,
    kinetics = Arrhenius(A=(2.34e3, 'cm^3/(mol*s)'), n=3.04, Ea=(6792.5, 'J/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)
    
entry(
    index = 2,
    label = "CPO + OH <=> H2O + CPO-3",
    degeneracy = 4,
    kinetics = Arrhenius(A=(1.13e5, 'cm^3/(mol*s)'), n=2.58, Ea=(5204.6, 'J/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)
    
entry(
    index = 3,
    label = "CPO + HO2 <=> H2O2 + CPO-2",
    degeneracy = 4,
    kinetics = Arrhenius(A=(9.91e-4, 'cm^3/(mol*s)'), n=4.74, Ea=(-4.19026e4, 'J/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)
  
entry(
    index = 4,
    label = "CPO + HO2 <=> H2O2 + CPO-3",
    degeneracy = 4,
    kinetics = Arrhenius(A=(5.45e-2, 'cm^3/(mol*s)'), n=4.27, Ea=(-4.95265e4, 'J/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)

entry(
    index = 5,
    label = "CPO + H <=> H2 + CPO-2",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(5.28e6, 'cm^3/(mol*s)'), n=2.185, Ea=(18.1, 'kJ/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.78e6, 'cm^3/(mol*s)'), n=2.121, Ea=(10.8, 'kJ/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)

entry(
    index = 6,
    label = "CPO + H <=> H2 + CPO-3",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.10e6, 'cm^3/(mol*s)'), n=2.259, Ea=(24.6, 'kJ/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.42e6, 'cm^3/(mol*s)'), n=2.263, Ea=(18.5, 'kJ/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)
        
entry(
    index = 7,
    label = "CPO + O <=> OH + CPO-2",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.18e5, 'cm^3/(mol*s)'), n=2.501, Ea=(15.8, 'kJ/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.66e5, 'cm^3/(mol*s)'), n=2.389, Ea=(8.6, 'kJ/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)    

entry(
    index = 8,
    label = "CPO + O <=> OH + CPO-3",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(10.28e4, 'cm^3/(mol*s)'), n=2.629, Ea=(10.9, 'kJ/mol'), T0=(1, 'K')),
            Arrhenius(A=(14.06e4, 'cm^3/(mol*s)'), n=2.522, Ea=(6.6, 'kJ/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)      

entry(
    index = 9,
    label = "CPO + CH3 <=> CH4 + CPO-2",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(10.98e1, 'cm^3/(mol*s)'), n=3.270, Ea=(25.2, 'kJ/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.76e1, 'cm^3/(mol*s)'), n=3.232, Ea=(18.7, 'kJ/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)    

entry(
    index = 10,
    label = "CPO + CH3 <=> CH4 + CPO-3",
    degeneracy = 2,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(16.96, 'cm^3/(mol*s)'), n=3.483, Ea=(33.2, 'kJ/mol'), T0=(1, 'K')),
            Arrhenius(A=(19.38, 'cm^3/(mol*s)'), n=3.468, Ea=(28.7, 'kJ/mol'), T0 = (1, 'K')),
        ],
    ),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  

entry(
    index = 11,
    label = "CPO-2 <=> RO1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.32e14, '1/s'), n=0, Ea=(169.5, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)       

entry(
    index = 12,
    label = "CPO-2 <=> RO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.50e13, '1/s'), n=0, Ea=(153.5, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)      

entry(
    index = 13,
    label = "CPO-3 <=> RO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e13, '1/s'), n=0, Ea=(138.1, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  

entry(
    index = 14,
    label = "CPO-3 <=> RO4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e13, '1/s'), n=0, Ea=(121.8, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  
    
entry(
    index = 15,
    label = "RO3 <=> RO5 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e13, '1/s'), n=0, Ea=(127.1, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  

entry(
    index = 16,
    label = "RO4 <=> RO5 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.50e11, '1/s'), n=0, Ea=(68.7, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  
    
entry(
    index = 17,
    label = "RO4 <=> RO7 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.08e14, '1/s'), n=0, Ea=(65.1, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  
    
entry(
    index = 18,
    label = "RO1 <=> RO8 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e14, '1/s'), n=0, Ea=(105.7, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  

entry(
    index = 19,
    label = "RO2 <=> RO9 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.69e13, '1/s'), n=0, Ea=(104.6, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 level calculation""",
    longDesc = """
    Zhou et al. 2016, Journal of Physical Chemistry A
    Toward the Development of a Fundamentally Based Chemical Model for Cyclopentanone: 
        High-Pressure-Limit Rate Constants for H Atom Abstraction and Fuel Radical 
        Decomposition 
    G4 level calculations
    """
)  