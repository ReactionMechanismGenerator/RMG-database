#!/usr/bin/env python
# encoding: utf-8

name = "imine_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=0,
    label="C11H15N + H2O <=> tert_butylamine + benzaldehyde",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(648, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Fig 8.4 in F.A. Carey, R.J. Sundberg, Advanced Organic Chemistry, 3rd Edn., Part A, ISBN 0-306-43447-4, p. 450
Originally from: J. Am. Chem. Soc. 85, 2843, 1963
C11H15N is benzylidene-1,1-dimethylethylamine with SMILES CC(N=Cc1ccccc1)(C)C

Fig value taken for "H" at pH=6: 0.6 min^-1
multiplied by 60 to convert to s^-1
multiplied by 18 ml/mol to account for water as the reactant
Rate measured at 25 degC from original paper
""",
)

entry(
    index=1,
    label="C11H14N_p_NO2 + H2O <=> tert_butylamine + benzaldehyde_p_NO2",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(11880, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Fig 8.4 in F.A. Carey, R.J. Sundberg, Advanced Organic Chemistry, 3rd Edn., Part A, ISBN 0-306-43447-4, p. 450
Originally from: J. Am. Chem. Soc. 85, 2843, 1963

Fig value taken for "p-NO2" at pH=6: 11 min^-1
multiplied by 60 to convert to s^-1
multiplied by 18 ml/mol to account for water as the reactant
Rate measured at 25 degC from original paper
""",
)

entry(
    index=2,
    label="C11H14N_m_Br + H2O <=> tert_butylamine + benzaldehyde_m_Br",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(3240, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Fig 8.4 in F.A. Carey, R.J. Sundberg, Advanced Organic Chemistry, 3rd Edn., Part A, ISBN 0-306-43447-4, p. 450
Originally from: J. Am. Chem. Soc. 85, 2843, 1963

Fig value taken for "m-Br" at pH=6: 3 min^-1
multiplied by 60 to convert to s^-1
multiplied by 18 ml/mol to account for water as the reactant
Rate measured at 25 degC from original paper
""",
)

entry(
    index=3,
    label="C11H14N_p_Cl + H2O <=> tert_butylamine + benzaldehyde_p_Cl",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(1080, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Fig 8.4 in F.A. Carey, R.J. Sundberg, Advanced Organic Chemistry, 3rd Edn., Part A, ISBN 0-306-43447-4, p. 450
Originally from: J. Am. Chem. Soc. 85, 2843, 1963

Fig value taken for "p-Cl" at pH=6: 1 min^-1
multiplied by 60 to convert to s^-1
multiplied by 18 ml/mol to account for water as the reactant
Rate measured at 25 degC from original paper
""",
)

entry(
    index=4,
    label="C11H14N_p_CH3 + H2O <=> tert_butylamine + benzaldehyde_p_CH3",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(216, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Fig 8.4 in F.A. Carey, R.J. Sundberg, Advanced Organic Chemistry, 3rd Edn., Part A, ISBN 0-306-43447-4, p. 450
Originally from: J. Am. Chem. Soc. 85, 2843, 1963

Fig value taken for "p-CH3" at pH=6: 0.2 min^-1
multiplied by 60 to convert to s^-1
multiplied by 18 ml/mol to account for water as the reactant
Rate measured at 25 degC from original paper
""",
)

entry(
    index=5,
    label="C11H14N_p_OCH3 + H2O <=> tert_butylamine + benzaldehyde_p_OCH3",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(32, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Fig 8.4 in F.A. Carey, R.J. Sundberg, Advanced Organic Chemistry, 3rd Edn., Part A, ISBN 0-306-43447-4, p. 450
Originally from: J. Am. Chem. Soc. 85, 2843, 1963

Fig value taken for "p-OCH3" at pH=6: 0.03 min^-1
multiplied by 60 to convert to s^-1
multiplied by 18 ml/mol to account for water as the reactant
Rate measured at 25 degC from original paper
""",
)
