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
   label = "H2 + Ni_3 + Ni_4 <=> HX_3 + HX_4",
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
   label = "H2 + Ni_3 + Ni_4 <=> HX_3 + HX_4",
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
#    label = "HX_4 + HOX_1 <=> H2O + Ni_3 + Ni_4",
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
# entry(
#     index = 3,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.16477,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTAzNg==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: CH3OH + X + X <=> HX + H3COX
# equation : CH3OH(g) -> H3CO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: Studt et al submitted
# reactionEnergy: 0.12029 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "211",
# )

# entry(
#     index = 4,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.25,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE3Nw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.47 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "211",
# )

# entry(
#     index = 5,
#     label = "Ni_3 + Ni_4 + CH2O2 <=> CHO2X + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.14,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM4MA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: HCOOH + X + X <=> HX + COOHX
# equation : HCOOH(g) -> COOH* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -0.71 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 6,
#     label = "Ni_3 + Ni_4 + CH2O2-2 <=> CHO2X-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.22,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM4OQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: HCOOH + X + X <=> HX + HCOOX
# equation : HCOOH(g) -> HCOO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -0.58 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 7,
#     label = "Ni_3 + Ni_4 + CH4O-2 <=> CH3OX-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.997546,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI3ODk=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: X + X + CH3OH <=> HX + OCH3X
# equation : CH3OH(g) + 2.0* -> CH3O* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: -0.0270354634558 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 8,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.609341,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MzE=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: X + X + CH3OH <=> HX + H3COX
# equation : CH3OH(g) + 2.0* -> CH2OH* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: -0.239356853213 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 9,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.74238,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTU0""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: X + X + C2H6 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.6041198234306648 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 10,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.00597,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTU1""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: X + X + C2H6 <=> HX + CH3CH2X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.17933295961120166 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 11,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.44571,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDg1""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ni
# Original entry: X + X + C2H6 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: HansenFirst2018,
# reactionEnergy: 0.7371855372330174 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ni",
#     facet = "111",
# )

# entry(
#     index = 12,
#     label = "Ni_3 + Ni_4 + H2O <=> HOX_1 + HX_4",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.349,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTM3MQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ni
# Original entry: H2O + X + X <=> HX + OHX
# equation : H2O(g) -> OH* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: -0.921 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ni",
#     facet = "211",
# )

# entry(
#     index = 13,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.72,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE2NQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ni
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: -1.065 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ni",
#     facet = "211",
# )

# entry(
#     index = 14,
#     label = "Ni_3 + Ni_4 + CH4 <=> CH3X + HX_4",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.13,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTM2""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ni
# Original entry: CH4 + X + X <=> HX + CH3X
# equation : CH4(g) -> CH3* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: -0.035 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ni",
#     facet = "211",
# )

# entry(
#     index = 15,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.6,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE2MA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ir
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.133 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ir",
#     facet = "111",
# )

# entry(
#     index = 16,
#     label = "Ni_3 + Ni_4 + CH4 <=> CH3X + HX_4",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.946526,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MTQ=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ir
# Original entry: X + X + CH4 <=> HX + CH3X
# equation : CH4(g) + 2.0* -> CH3* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: 0.341271177429 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ir",
#     facet = "111",
# )

# entry(
#     index = 17,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.87438,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDAy""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ir
# Original entry: X + X + C2H6 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.19178910719347186 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ir",
#     facet = "111",
# )

# entry(
#     index = 18,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.909862,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDAz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ir
# Original entry: X + X + C2H6 <=> HX + CH3CH2X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.05811311010620557 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ir",
#     facet = "111",
# )

# entry(
#     index = 19,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.72461,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTE2""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: CH3CH3 + X + X <=> HX + CH2CH3X
# equation : CH3CH3(g) -> CH2CH3* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.05277 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 20,
#     label = "Ni_3 + Ni_4 + C3H8 <=> C2H5X + CH3X-2",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.999,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTIx""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: CH3CH2CH3 + X + X <=> CH3X + CH2CH3X
# equation : CH3CH2CH3(g) -> CH2CH3* + CH3*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.31775 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 21,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.30059,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTAzNw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: CH3OH + X + X <=> HX + H3COX
# equation : CH3OH(g) -> H3CO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: BehrensThe2012
# reactionEnergy: -0.03297 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 22,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.24,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE3Ng==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.149 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 23,
#     label = "Ni_3 + Ni_4 + CH2O2 <=> CHO2X + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.06,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM4Mw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: HCOOH + X + X <=> HX + COOHX
# equation : HCOOH(g) -> COOH* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.37 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 24,
#     label = "Ni_3 + Ni_4 + CH2O2-2 <=> CHO2X-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.44,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM5Mg==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: HCOOH + X + X <=> HX + HCOOX
# equation : HCOOH(g) -> HCOO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -0.49 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 25,
#     label = "Ni_3 + Ni_4 + CH4O-2 <=> CH3OX-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.14986,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI3OTQ=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: X + X + CH3OH <=> HX + OCH3X
# equation : CH3OH(g) + 2.0* -> CH3O* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: 0.111993965489 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 26,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.5036,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MzY=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: X + X + CH3OH <=> HX + H3COX
# equation : CH3OH(g) + 2.0* -> CH2OH* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: 1.11924855364 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 27,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.51085,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4Mjkz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: X + X + CH3CH3 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 1.4629379389225505 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 28,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.15338,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4Mjk0""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: X + X + CH3CH3 <=> HX + CH2CH3X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 1.0548785937717184 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 29,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.33496,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjQw""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Co
# Original entry: X + X + C2H6 <=> HX + CH3CH2X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.460976713366108 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Co",
#     facet = "111",
# )

# entry(
#     index = 30,
#     label = "Ni_3 + Ni_4 + CH4 <=> CH3X + HX_4",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.06,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTMy""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ru
# Original entry: CH4 + X + X <=> HX + CH3X
# equation : CH4(g) -> CH3* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 0.291 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ru",
#     facet = "111",
# )

# entry(
#     index = 31,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.3,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE1OA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ru
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -1.392 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ru",
#     facet = "211",
# )

# entry(
#     index = 32,
#     label = "Ni_3 + Ni_4 + H2O <=> HOX_1 + HX_4",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.739,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTM4NA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ru
# Original entry: H2O + X + X <=> HX + OHX
# equation : H2O(g) -> OH* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.25 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ru",
#     facet = "111",
# )

# entry(
#     index = 33,
#     label = "Ni_3 + Ni_4 + C3H8 <=> C2H5X + CH3X-2",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.709,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTE1""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ru
# Original entry: CH3CH2CH3 + X + X <=> CH3X + CH3CH2X
# equation : CH3CH2CH3(g) -> CH2CH3* + CH3*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.439 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ru",
#     facet = "211",
# )

# entry(
#     index = 34,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.68087,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTEz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: CH3CH3 + X + X <=> HX + CH2CH3X
# equation : CH3CH3(g) -> CH2CH3* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.03023 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 35,
#     label = "Ni_3 + Ni_4 + C3H8 <=> C2H5X + CH3X-2",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.029,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTE4""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: CH3CH2CH3 + X + X <=> CH3X + CH2CH3X
# equation : CH3CH2CH3(g) -> CH2CH3* + CH3*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 0.05775 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 36,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.59597,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTAzNA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: CH3OH + X + X <=> HX + H3COX
# equation : CH3OH(g) -> H3CO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: Studt et al submitted
# reactionEnergy: -0.64978 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 37,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.92,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE2Nw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -0.2 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 38,
#     label = "Ni_3 + Ni_4 + CH2O2 <=> CHO2X + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(-0.29,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM3Nw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: HCOOH + X + X <=> HX + COOHX
# equation : HCOOH(g) -> COOH* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -1.45 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 39,
#     label = "Ni_3 + Ni_4 + CH2O2-2 <=> CHO2X-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(-1.14,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM4NQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: HCOOH + X + X <=> HX + HCOOX
# equation : HCOOH(g) -> HCOO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -1.86 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 40,
#     label = "Ni_3 + Ni_4 + CH4O-2 <=> CH3OX-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.751824,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI3OTI=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: X + X + CH3OH <=> HX + OCH3X
# equation : CH3OH(g) + 2.0* -> CH3O* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: -0.387903736148 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 41,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.558281,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MzQ=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: X + X + CH3OH <=> HX + H3COX
# equation : CH3OH(g) + 2.0* -> CH2OH* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: -0.223686904996 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 42,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.66593,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODAz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: X + X + CH3CH3 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.5125052125076763 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 43,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.888677,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODA0""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: X + X + CH3CH3 <=> HX + CH2CH3X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 0.17133138378267176 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 44,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.68176,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTE0""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: CH3CH3 + X + X <=> HX + CH2CH3X
# equation : CH3CH3(g) -> CH2CH3* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: -0.07823 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 45,
#     label = "Ni_3 + Ni_4 + C3H8 <=> C2H5X + CH3X-2",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.799,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTIw""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: CH3CH2CH3 + X + X <=> CH3X + CH2CH3X
# equation : CH3CH2CH3(g) -> CH2CH3* + CH3*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: 0.11775 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 46,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.87272,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTAzNQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: CH3OH + X + X <=> HX + H3COX
# equation : CH3OH(g) -> H3CO* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: Studt et al submitted,
# reactionEnergy: -0.25706 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 47,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.69,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE2NA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: -0.96 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 48,
#     label = "Ni_3 + Ni_4 + CH2O2 <=> CHO2X + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.22,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM4MQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: HCOOH + X + X <=> HX + COOHX
# equation : HCOOH(g) -> COOH* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: YooTheoretical2014,
# reactionEnergy: -0.84 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 49,
#     label = "Ni_3 + Ni_4 + CH2O2-2 <=> CHO2X-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.3,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM5MQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: HCOOH + X + X <=> HX + HCOOX
# equation : HCOOH(g) -> HCOO* + H*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: YooTheoretical2014,
# reactionEnergy: -0.4 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 50,
#     label = "Ni_3 + Ni_4 + CH4O-2 <=> CH3OX-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.738073,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI3OTE=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: X + X + CH3OH <=> HX + OCH3X
# equation : CH3OH(g) + 2.0* -> CH3O* + H*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: SchumannSelectivity2018,
# reactionEnergy: 0.412708138145 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 51,
#     label = "Ni_3 + Ni_4 + H2O <=> HOX_1 + HX_4",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.895982,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MDk=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: X + X + H2O <=> HX + OHX
# equation : H2O(g) + 2.0* -> OH* + H*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: SchumannSelectivity2018,
# reactionEnergy: 0.687325776191 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 52,
#     label = "Ni_3 + Ni_4 + CH4 <=> CH3X + HX_4",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.985522,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MTU=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: X + X + CH4 <=> HX + CH3X
# equation : CH4(g) + 2.0* -> CH3* + H*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: SchumannSelectivity2018,
# reactionEnergy: 0.162446322385 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 53,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.684903,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MzM=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: X + X + CH3OH <=> HX + H3COX
# equation : CH3OH(g) + 2.0* -> CH2OH* + H*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: SchumannSelectivity2018,
# reactionEnergy: -0.339846049188 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 54,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.00741,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzEy""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: X + X + CH3CH3 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: HansenFirst2018,
# reactionEnergy: -0.039370928512653336 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 55,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.9232,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzEz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: X + X + CH3CH3 <=> HX + CH2CH3X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*,
# dft_code : Quantum ESPRESSO 5.1,
# dftFunctional : BEEF-vdW,
# pubId: HansenFirst2018,
# reactionEnergy: -0.10822661724523641 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 56,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.24261,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTE5""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: CH3CH3 + X + X <=> HX + CH2CH3X
# equation : CH3CH3(g) -> CH2CH3* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.77877 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 57,
#     label = "Ni_3 + Ni_4 + C3H8 <=> C2H5X + CH3X-2",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.539,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTIy""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: CH3CH2CH3 + X + X <=> CH3X + CH2CH3X
# equation : CH3CH2CH3(g) -> CH2CH3* + CH3*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 2.12775 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 58,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.73317,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTAzOA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: CH3OH + X + X <=> HX + H3COX
# equation : CH3OH(g) -> H3CO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: Studt et al submitted
# reactionEnergy: 0.95285 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 59,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.28,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE5Ng==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 0.857 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 60,
#     label = "Ni_3 + Ni_4 + CH2O2 <=> CHO2X + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.22,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM4NA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: HCOOH + X + X <=> HX + COOHX
# equation : HCOOH(g) -> COOH* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: 0.76 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 61,
#     label = "Ni_3 + Ni_4 + CH2O2-2 <=> CHO2X-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.29,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM5MA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: HCOOH + X + X <=> HX + HCOOX
# equation : HCOOH(g) -> HCOO* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: YooTheoretical2014
# reactionEnergy: -0.27 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 62,
#     label = "Ni_3 + Ni_4 + CH4O-2 <=> CH3OX-2 + HX_4",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.56421,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI3OTM=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: X + X + CH3OH <=> HX + OCH3X
# equation : CH3OH(g) + 2.0* -> CH3O* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: 0.910756077865 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "111",
# )

# entry(
#     index = 63,
#     label = "Ni_3 + Ni_4 + CH4O <=> CH3OX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.14481,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246ODI4MzU=""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: X + X + CH3OH <=> HX + H3COX
# equation : CH3OH(g) + 2.0* -> CH2OH* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: SchumannSelectivity2018
# reactionEnergy: 1.75125419629 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "111",
# )

# entry(
#     index = 64,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.8856,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTM4""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: X + X + CH3CH3 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 2.1257553049072158 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "111",
# )

# entry(
#     index = 65,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.36629,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTM5""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: X + X + CH3CH3 <=> HX + CH2CH3X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 1.742219948413549 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "111",
# )

# entry(
#     index = 66,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.78931,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTE3""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: CH3CH3 + X + X <=> HX + CH2CH3X
# equation : CH3CH3(g) -> CH2CH3* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.24177 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "211",
# )

# entry(
#     index = 67,
#     label = "Ni_3 + Ni_4 + C3H8 <=> C2H5X + CH3X-2",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.979,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTIz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: CH3CH2CH3 + X + X <=> CH3X + CH2CH3X
# equation : CH3CH2CH3(g) -> CH2CH3* + CH3*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.47775 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "211",
# )

# entry(
#     index = 68,
#     label = "Ni_3 + Ni_4 + CH4 <=> CH3X + HX_4",
#     degeneracy = 2.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.23,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTYw""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: CH4 + X + X <=> HX + CH3X
# equation : CH4(g) -> CH3* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.52 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "111",
# )

# entry(
#     index = 69,
#     label = "Ni_3 + Ni_4 + H3N <=> H2NX + HX_4",
#     degeneracy = 1.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.95,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTE5MQ==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: NH3 + X + X <=> HX + NH2X
# equation : NH3(g) -> NH2* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 0.73 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "211",
# )

# entry(
#     index = 70,
#     label = "Ni_3 + Ni_4 + H2O <=> HOX_1 + HX_4",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.997,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTQxMA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: H2O + X + X <=> HX + OHX
# equation : H2O(g) -> OH* + H*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 1.558 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "111",
# )

# entry(
#     index = 71,
#     label = "Ni_3 + Ni_4 + C2H6 <=> CH3X + CH3X-2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(4.26984,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTgy""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: X + X + CH3CH3 <=> CH3X + CH3X
# equation : C2H6(g) + 2.0* -> 2.0CH3*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 1.551312217998202 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "111",
# )

# entry(
#     index = 72,
#     label = "Ni_3 + Ni_4 + C2H6-2 <=> C2H5X + HX_4",
#     degeneracy = 3.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.04718,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTgz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: X + X + CH3CH3 <=> HX + CH2CH3X
# equation : C2H6(g) + 2.0* -> CH3CH2* + H*
# dft_code : Quantum ESPRESSO 5.1
# dftFunctional : BEEF-vdW
# pubId: HansenFirst2018
# reactionEnergy: 1.4054432074481156 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "111",
# )

