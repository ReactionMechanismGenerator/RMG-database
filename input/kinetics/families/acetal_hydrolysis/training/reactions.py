#!/usr/bin/env python
# encoding: utf-8

name = "acetal_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=0,
    label="r1 + H2O <=> p1 + p2",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(9, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol')),
    rank=1,
    shortDesc=u"""""",
    longDesc=
    u"""
Table 3 in Waterman et al. Hydrolysis in Pharmaceutical Formulations,
Pharmaceutical Development and Technology, 7:2, 113-146, https://doi.org/10.1081/PDT-120003494

Rate taken for Erythromycin at 60C, pH 10. THere are two acetals there, *assumed* the one close to N reacted here
multiplied by 18 ml/mol to account for water as the reactant
A value for pH 7 is 1.6E-2 (s^-1)
""",
)

entry(
    index=1,
    label="mNO2ArCHOEt2 + H2O <=> mNO2ArCHOEtOH + EtOH",
    degeneracy=2,
    rank=1,
    kinetics=Arrhenius(A=(2.4e+04, 'cm^3/(mol*s)'), n=0, Ea=(8.86, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 3""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
c1c(C(OCC)(OCC))cc(cc1)[N+](=O)[O-]
multiplied by 18 ml/mol to account for water as the reactant
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (3.86 kcal), A adjusted to 313K
Arrhenius(A=(1.57e-02, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)

entry(
    index=2,
    label="ArCHOEtO2 + H2O <=> ArCHOEtOH + EtOH",
    degeneracy=2,
    rank=1,
    kinetics=Arrhenius(A=(1.3e+05, 'cm^3/(mol*s)'), n=0, Ea=(8.86, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 4.544""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
c1c(C(OCC)(OCC))cc(cc1)
multiplied by 18 ml/mol to account for water as the reactant
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (3.86 kcal), A adjusted to 313K
Arrhenius(A=(8.3e-02, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)

entry(
    index=3,
    label="pMeArCHOEtO2 + H2O <=> pMeArCHOEtOH + EtOH",
    degeneracy=2,
    rank=1,
    kinetics=Arrhenius(A=(1.1e+05, 'cm^3/(mol*s)'), n=0, Ea=(8.86, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 5.288""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
CCOC(OCC)C1=CC=C(C)C=C1
multiplied by 18 ml/mol to account for water as the reactant
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (3.86 kcal), A adjusted to 313K
Arrhenius(A=(7.4e-02, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)

entry(
    index=4,
    label="pOMeArCHOEtO2 + H2O <=> pOMeArCHOEtOH + EtOH",
    degeneracy=2,
    rank=1,
    kinetics=Arrhenius(A=(7.4e+04, 'cm^3/(mol*s)'), n=0, Ea=(8.86, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 5.972""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
multiplied by 18 ml/mol to account for water as the reactant
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (3.86 kcal), A adjusted to 313K
Arrhenius(A=(4.8e-02, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)
