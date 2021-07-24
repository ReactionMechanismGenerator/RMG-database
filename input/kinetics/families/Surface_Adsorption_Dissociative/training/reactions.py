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
   rank = 3,
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
#    index = 3,
#    label = "HX_4 + HOX_1 <=> H2O + X_3 + X_4",
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
    kinetics = StickingCoefficient(A=0.773, n=0.9387, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Methane/Vlachos_Rh
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
    index = 4,
    label = "X_3 + X_4 + CH4 <=> CH3X_1 + HX_4",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.572, n=0.7883, Ea=(14.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Methane/Vlachos_Rh
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
    index = 5,
    label = "X_3 + X_4 + H2 <=> HX_3 + HX_4",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.87, n=0, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Vlachos_Ru0001
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
   index = 3,
   label = "C2H6 + X_3 + X_4 <=> CH3X_1 + CH3X_2",
   degeneracy = 2,
   kinetics = StickingCoefficient(
       A = 0.1,
       n = 0,
       Ea = (2.59, 'eV/molecule'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   rank = 10,
   shortDesc = u"""Made up by Emily""",
   longDesc = u"""
   Ea is from "Universal Brønsted-evans-polanyi Relations For C-c, C-o, C-n,
   N-o, N-n, And O-o Dissociation Reactions".
   Wang, Shengguang; Temel, Burcin; Shen, Juan; Jones, Glenn; Grabow,
   Lars C; Studt, Felix; Bligaard, Thomas; Abild-Pedersen, Frank;
   Christensen, Claus H; Nørskov, Jens K.. Catalysis letters. ,
   3, 370--373 (2011)
   Doi:10.1007/s10562-010-0477-y

   A is made up by Emily
    """,
    metal = 'Ni'
)

entry(
    index = 55,
    label = "X_3 + X_4 + C2H6-2 <=> C2H5X + HX_4",
    degeneracy = 3.0,
    kinetics = StickingCoefficient(
        A=0.1,
        n=0,
        Ea=(0.9232,'eV/molecule'),
        T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzEz""",
    longDesc =
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + X + CH3CH3 <=> HX + CH2CH3X
equation : C2H6(g) + 2.0* -> CH3CH2* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.10822661724523641 eV

A is made up by Emily
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "X_3 + X_4 + C3H8 <=> C2H5X + CH3X_2",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(
    A=0.1,
    n=0,
    Ea=(2.799,'eV/molecule'),
    T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTIw""",
    longDesc =
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH3CH2CH3 + X + X <=> CH3X + CH2CH3X
equation : CH3CH2CH3(g) -> CH2CH3* + CH3*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.11775 eV

A is made up by Emily
""",
    metal = "Pt",
    facet = "211",
)
