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
    '2+2_cycloaddition',
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

# Families for pyrolysis of C/H systems
ch_pyrolysis = {
    '1+2_Cycloaddition',
    '1,2_Insertion_carbene',
    'Birad_R_Recombination',
    'CO_Disproportionation',
    'Diels_alder_addition',
    'Disproportionation',
    'H_Abstraction',
    'intra_H_migration',
    'Intra_R_Add_Endocyclic',
    'Intra_R_Add_Exocyclic',
    'Intra_R_Add_Exo_scission',
    'Intra_Retro_Diels_alder_bicyclic',
    'R_Addition_COm',
    'R_Addition_MultipleBond',
    'R_Recombination',
    '6_membered_central_C-C_shift',
    'Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH',
    'Cyclopentadiene_scission',
    'Intra_2+2_cycloaddition_Cd',
    'Intra_5_membered_conjugated_C=C_C=C_addition',
    'Intra_Diels_alder_monocyclic',
    'Intra_ene_reaction',
    'Singlet_Carbene_Intra_Disproportionation',
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
surface = {
    'Surface_Adsorption_Single',
    'Surface_Adsorption_vdW',
    'Surface_Adsorption_Dissociative',
    'Surface_Dissociation',
    'Surface_Abstraction',
    'Surface_EleyRideal_Addition_Multiple_Bond',
    'Surface_Migration',
    'Surface_Dissociation_Double_vdW',
    'Surface_Addition_Single_vdW',
    'Surface_Dissociation_vdW',
    'Surface_Abstraction_vdW',
    'Surface_Dual_Adsorption_vdW',
    'Surface_Dissociation_Beta',
    'Surface_Adsorption_Abstraction_vdW',
    'Surface_Adsorption_Bidentate',
    'Surface_Bidentate_Dissociation',
    'Surface_DoubleBond_to_Bidentate', 
    'Surface_vdW_to_Bidentate',
    'Surface_Abstraction_Single_vdW',
    'Surface_Adsorption_Dissociative_Double',
}

# Surface chemistry families that are under development and not yet working well.
surface_development = {
    #'Surface_Adsorption_Double',
}
