# This file contains multiple sets of suggested kinetics families for various
# systems of interest. They can be used by including the name of a set in the
# kineticsFamilies part of the input file. Multiple sets can be specified at
# the same time, and the union of them will be loaded. These sets can also be
# specified along with individual families. Custom sets can be easily defined
# in this file and immediately used in input files without any additional
# changes.

default = {
    '1+2_Cycloaddition',
    '1,2-Birad_to_alkene',
    '1,2_Insertion_CO',
    '1,2_Insertion_carbene',
    '1,2_shiftS',
    '1,3_Insertion_CO2',
    '1,3_Insertion_ROR',
    '1,3_Insertion_RSR',
    '1,4_Cyclic_birad_scission',
    '1,4_Linear_birad_scission',
    '2+2_cycloaddition_CCO',
    '2+2_cycloaddition_CO',
    '2+2_cycloaddition_CS',
    '2+2_cycloaddition_Cd',
    'Birad_recombination',
    'CO_Disproportionation',
    'Birad_R_Recombination',
    'Cyclic_Ether_Formation',
    'Cyclic_Thioether_Formation',
    'Diels_alder_addition',
    'Disproportionation',
    'HO2_Elimination_from_PeroxyRadical',
    'H_Abstraction',
    'Intra_Retro_Diels_alder_bicyclic',
    'Intra_Disproportionation',
    'Intra_R_Add_Endocyclic',
    'Intra_R_Add_Exocyclic',
    'R_Addition_COm',
    'R_Addition_MultipleBond',
    'R_Recombination',
    'intra_H_migration',
    'intra_NO2_ONO_conversion',
    'intra_OH_migration',
    'intra_substitutionCS_cyclization',
    'intra_substitutionCS_isomerization',
    'intra_substitutionS_cyclization',
    'intra_substitutionS_isomerization',
    'ketoenol',
    'Singlet_Carbene_Intra_Disproportionation',
    'Singlet_Val6_to_triplet',
    'Intra_5_membered_conjugated_C=C_C=C_addition',
    'Intra_Diels_alder_monocyclic',
    'Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH',
    'Intra_2+2_cycloaddition_Cd',
    'Intra_ene_reaction',
    'Cyclopentadiene_scission',
    '6_membered_central_C-C_shift',
    'Intra_R_Add_Exo_scission',
    '1,2_shiftC',
    '1,2_NH3_elimination',
    '1,3_NH3_elimination',
    'Retroene',
}
#api family useful in large drug like molecues.
# templates are modified to restric production of unnessary products
api = {
    'API_1+2_Cycloaddition',  # exclude aromatic rings
    '1,2-Birad_to_alkene',  # only forward by default
    '1,2_Insertion_CO',
    '1,2_Insertion_carbene',
    'API_1,2_NH3_elimination',
    '1,2_shiftC',
    '1,2_shiftS',
    '1,3_Insertion_CO2',
    'API_1,3_Insertion_ROR',  # exclude aromatic rings
    'API_1,3_Insertion_RSR',  # exclude aromatic rings
    '1,3_NH3_elimination',  # only forward
    'API_1,4_Cyclic_birad_scission',  # only forward
    'API_1,4_Linear_birad_scission',  # only forward
    'API_2+2_cycloaddition_CCO',  # only reverse
    'API_2+2_cycloaddition_CO',  # only reverse
    'API_2+2_cycloaddition_CS',  # only reverse
    'API_2+2_cycloaddition_Cd',  # only reverse
    '6_membered_central_C-C_shift',
    'API_Birad_R_Recombination',  # only forward
    'API_Birad_recombination',  # only forward
    'CO_Disproportionation',
    'Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH',
    'Cyclic_Ether_Formation',
    'Cyclic_Thioether_Formation',
    'Diels_alder_addition',
    'API_Disproportionation',  # only forward
    'API_HO2_Elimination_from_PeroxyRadical',
    'API_H_Abstraction',  # exclude aromatic rings, don't abstract from a radical site
    'API_Intra_2+2_cycloaddition_Cd',  # only reverse
    'Intra_5_membered_conjugated_C=C_C=C_addition',
    'Intra_Diels_alder_monocyclic',
    'Intra_Retro_Diels_alder_bicyclic',
    'API_Intra_Disproportionation',  # only forward
    # 'API_Intra_RH_Add_Endocyclic',
    # 'API_Intra_RH_Add_Exocyclic',
    'API_Intra_R_Add_Endocyclic',  # exclude aromatic rings
    'API_Intra_R_Add_Exocyclic',  # exclude aromatic rings
    'Intra_R_Add_Exo_scission',
    'Intra_ene_reaction',
    'API_intra_H_migration',
    'intra_NO2_ONO_conversion',
    'intra_OH_migration',
    'intra_substitutionCS_cyclization',
    'intra_substitutionCS_isomerization',
    'intra_substitutionS_cyclization',
    'intra_substitutionS_isomerization',
    'R_Addition_COm',
    'API_R_Addition_MultipleBond',  # exclude aromatic rings
    'API_R_Recombination',  # only forward
    'ketoenol',
    # 'Singlet_Carbene_Intra_Disproportionation',  not recommended for APIs
    'Singlet_Val6_to_triplet',
    'Substitution_O',
    'SubstitutionS',
    'Cyclopentadiene_scission',
    'Retroene',
    'Fake_amine_hydrolysis',  # custom
    'Fake_HOCK_rearrangement',  # custom
    'acetal_hydrolysis',  # custom
    'hemiaminal_hydrolysis',  # custom
    'hemiacetal_hydrolysis',  # custom
    'hydroperoxide_to_alcohol',  # custom
    'imine_hydrolysis',  # custom
    'methanoate_hydrolysis',  # custom
    'thione_ketone',  # custom
    'amine_COH_HCN',  # custom
    'amide_alcoholysis',  # custom
    'alcohol_dehydrogenation',  # custom
}

# Peroxide chemistry families that are likely relevant in liquid-phase
# hydrocarbon oxidation systems
liquid_peroxide = {
    'Peroxyl_Disproportionation',
    'Peroxyl_Termination',
    'Bimolec_Hydroperoxide_Decomposition',
    'Korcek_step1',
    'Korcek_step1_cat',
    'Korcek_step2',
    'Baeyer-Villiger_step1_cat',
    'Baeyer-Villiger_step2',
    'Baeyer-Villiger_step2_cat',
}

# Surface chemistry for heterogeneous catalysis.
# surface = {
#     'Surface_Adsorption_Single',
#     'Surface_Adsorption_vdW',
#     'Surface_Adsorption_Dissociative',
#     'Surface_Dissociation',
#     'Surface_Abstraction',
# }

# Surface chemistry families that are under development and not yet working well.
# surface_development = {
#     'Surface_Adsorption_Double',
#     'Surface_Dissociation_vdW',
#     'Surface_Adsorption_Bidentate',
#     'Surface_Bidentate_Dissociation'
#     # 'Surface_Recombination' #DEPRECATED. USE Surface_Dissociation INSTEAD
# }
