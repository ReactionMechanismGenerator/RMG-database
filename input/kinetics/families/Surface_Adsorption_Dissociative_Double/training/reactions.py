#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociation_Double/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
# entry(
#     index = 1,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.84,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTkx""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: CatappTrends2008
# reactionEnergy: 0.74 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 2,
#     label = "X + X-2 + CH2O <=> OX + CH2X",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.34,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTMyNw==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pd
# Original entry: CH2O + X + X <=> OX + CH2X
# equation : CH2O(g) -> CH2* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 0.48 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pd",
#     facet = "211",
# )

# entry(
#     index = 3,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.89,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTg1""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ni
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: CatappTrends2008,
# reactionEnergy: -0.38 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ni",
#     facet = "111",
# )

# entry(
#     index = 4,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.82,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTkw""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: CatappTrends2008
# reactionEnergy: 1.29 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "111",
# )

# entry(
#     index = 5,
#     label = "X + X-2 + CH2O <=> OX + CH2X",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.38,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTMyOA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: CH2O + X + X <=> OX + CH2X
# equation : CH2O(g) -> CH2* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 0.77 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "211",
# )

# entry(
#     index = 6,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.372,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTc5""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Co
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: JiangTrends2009
# reactionEnergy: -1.107 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Co",
#     facet = "211",
# )

# entry(
#     index = 7,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(-0.009,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTcy""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ru
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: JiangTrends2009
# reactionEnergy: -1.477 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ru",
#     facet = "211",
# )

# entry(
#     index = 8,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.74,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTg0""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: CatappTrends2008
# reactionEnergy: -0.47 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 9,
#     label = "X + X-2 + CH2O <=> OX + CH2X",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(0.77,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTI3NA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Rh
# Original entry: CH2O + X + X <=> OX + CH2X
# equation : CH2O(g) -> CH2* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: -1.34 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Rh",
#     facet = "211",
# )

# entry(
#     index = 10,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.68,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTg5""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: CatappTrends2008,
# reactionEnergy: 0.96 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 11,
#     label = "X + X-2 + CH2O <=> OX + CH2X",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(1.3,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTI5Mg==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Pt
# Original entry: CH2O + X + X <=> OX + CH2X
# equation : CH2O(g) -> CH2* + O*,
# dft_code : DACAPO,
# dftFunctional : RPBE,
# pubId: WangUniversal2011,
# reactionEnergy: -0.3 eV
# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 12,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(2.739,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTkz""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: JiangTrends2009
# reactionEnergy: 2.623 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 13,
#     label = "X + X-2 + CH2O <=> OX + CH2X",
#     degeneracy = 0.5,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.72,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MTM1OA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Ag
# Original entry: CH2O + X + X <=> OX + CH2X
# equation : CH2O(g) -> CH2* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: WangUniversal2011
# reactionEnergy: 2.6 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Ag",
#     facet = "211",
# )

# entry(
#     index = 14,
#     label = "X + X-2 + CO2 <=> OX + COX",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^5/(mol^2*s)'), n=0, Ea=(3.38,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246OTk1""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Au
# Original entry: CO2 + X + X <=> OX + COX
# equation : CO2(g) -> CO* + O*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: CatappTrends2008
# reactionEnergy: 3.29 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Au",
#     facet = "111",
# )

