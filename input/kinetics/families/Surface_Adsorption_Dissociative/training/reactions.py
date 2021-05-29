#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociative/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
   index = 1,
   label = "H2 + X_3 + X_4 <=> HX_3 + HX_4",
   degeneracy = 2,
   kinetics = StickingCoefficient(
       A = 3e-2,
       n = 0,
       Ea = (5, 'kJ/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   rank = 10,
   shortDesc = u"""Deutschmann Ni""",
   longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904
""",
    metal = "Ni"
)

entry(
   index = 2,
   label = "H2 + X_3 + X_4 <=> HX_3 + HX_4",
   degeneracy = 2,
   kinetics = StickingCoefficient(
       A = 0.046,
       n = 0,
       Ea = (0, 'J/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   rank = 10,
   shortDesc = u"""H2 on Pt""",
   longDesc = u"""
    Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
    Xu, Clayton, Balakotaiah, Harold et al.
    doi: 10.1016.j.apcatb.2007.08.008

    This is R2
    """,
    metal = 'Pt'
)

# entry(
#    index = 6,
#    label = "HX_4 + HOX_1 <=> H2O + X_3 + Ni_4",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A = (4.02e14, 'm^2/(mol*s)'),
#        n = 0,
#        Ea = (17.4, 'kJ/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    rank = 10,
#    shortDesc = u"""H2O dissociative adsorption on Pt""",
#    longDesc = u"""
#     Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
#     Xu, Clayton, Balakotaiah, Harold et al.
#     doi: 10.1016.j.apcatb.2007.08.008
#
#     This is R6
#     """,
#     metal = "Pt"
# )
entry(
    index = 3,
    label = "X_3 + X_4 + H2 <=> HX_3 + HX_4",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.129, n=0.858, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: H2 + X + X <=> H_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R11 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "X_3 + X_4 + CH4 <=> CH3X + HX_4",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.116, n=0.154, Ea=(9,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH4 + X + X <=> CH3_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R55 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "X_3 + X_4 + H2 <=> HX_3 + HX_4",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.87, n=0, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Ru0001
Original entry: H2 + X + X <=> H_X + H_X
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This is R1 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 6,
    label = "X_3 + X_4 + H2 <=> HX_3 + HX_4",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.773, n=0.9387, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: H2 + X + X <=> H_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R1 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 7,
    label = "X_3 + X_4 + CH4 <=> CH3X + HX_4",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.572, n=0.7883, Ea=(14.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CH4 + X + X <=> CH3_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R55 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 8,
    label = "X_3 + X_4 + H2 <=> HX_3 + HX_4",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0236, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: H2 + X + X <=> H_X + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R7 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

