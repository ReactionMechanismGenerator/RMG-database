#!/usr/bin/env python
# encoding: utf-8

name = "hemiacetal_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=0,
    label="CH2O + H2O <=> OHCH2OH",
    degeneracy=2,
    rank=1,
    kinetics=Arrhenius(A=(3.67e+06, 'cm^3/(mol*s)'), n=0, Ea=(5.83, 'kcal/mol'), T0=(1, 'K'),
                       Tmin=(285, 'K'), Tmax=(345, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
J.G.M. Winkelman, O.K. Voorwinde, M. Ottens, A.A.C.M. Beenackers, L.P.B.M. Janssen
Chemical Engineering Science, Volume 57, Issue 19, October 2002, Pages 4067-4076
https://doi.org/10.1016/S0009-2509(02)00358-5
The original rate was multiplied by 18 cm3/mol to convert units into a second order reaction.
""",
)

entry(
    index=1,
    label="MeCHOHOEt <=> MeCHO + EtOH",
    degeneracy=1,
    rank=1,
    kinetics=Arrhenius(A=(5.0e+08, 's^-1'), n=0, Ea=(16.64, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""""",
    longDesc=
    u"""
Yvonne ChiangA. Jerry Kresge. Kinetics of hydrolysis of acetaldehyde ethyl hemiacetal in aqueous solution.
J. Org. Chem. 1985, 50, 25, 5038-5040 Publication Date:December 1, 1985
https://doi.org/10.1021/jo00225a007
Measured at 25 degC, used non-catalyzed kH2O on page 5039
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (11.64 kcal), A adjusted to 313K
Arrhenius(A=(1.19e-03, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K'))
""",
)

entry(
    index=2,
    label="mNO2ArCHOEtOH <=> mNO2ArCHO + EtOH",
    degeneracy=1,
    rank=1,
    kinetics=Arrhenius(A=(4.6e+07, 's^-1'), n=0, Ea=(13.3, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 3""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
c1c(C(OCC)(O))cc(cc1)[N+](=O)[O-]
c1c(C(=O))cc(cc1)[N+](=O)[O-]
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (8.3 kcal), A adjusted to 313K
Arrhenius(A=(2.4e-02, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)

entry(
    index=3,
    label="ArCHOEtOH <=> ArCHO + EtOH",
    degeneracy=1,
    rank=1,
    kinetics=Arrhenius(A=(1.3e+09, 's^-1'), n=0, Ea=(15.22, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 4.544""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
c1c(C(OCC)(O))cc(cc1)
c1c(C(=O))cc(cc1)
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (10.22 kcal), A adjusted to 313K
Arrhenius(A=(3.0e-02, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)

entry(
    index=4,
    label="pMeArCHOEtOH <=> pMeArCHO + EtOH",
    degeneracy=1,
    rank=1,
    kinetics=Arrhenius(A=(6.5e+07, 's^-1'), n=0, Ea=(13.31, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 5.288""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
CCOC(O)C1=CC=C(C)C=C1
CC1=CC=C(C=O)C=C1
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (8.31 kcal), A adjusted to 313K
Arrhenius(A=(3.3e-02, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')) original data
""",
)

entry(
    index=5,
    label="pOMeArCHOEtOH <=> pOMeArCHO + EtOH",
    degeneracy=1,
    rank=1,
    kinetics=Arrhenius(A=(2.6e+07, 's^-1'), n=0, Ea=(12.21, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 5.972""",
    longDesc=
    u"""
James L. JensenPaul A. Lenz. Hemiacetal buildup during acetal hydrolysis.
J. Am. Chem. Soc. 1978, 100, 4, 1291-1293 Publication Date:February 1, 1978
https://doi.org/10.1021/ja00472a045
Measured at 25 degC, Table II
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (7.21 kcal), A adjusted to 313K
Arrhenius(A=(7.6e-02, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K'))
""",
)

entry(
    index=6,
    label="CbOMeOH <=> ArCHO + MeOH",
    degeneracy=1,
    rank=2,
    kinetics=Arrhenius(A=(1.7e+12, 's^-1'), n=0, Ea=(15.25, 'kcal/mol'), T0=(1, 'K')),
    shortDesc=u"""pH = 10""",
    longDesc=
    u"""
Brian Capon, Keith Nimmo and Gordon L. Reid. Kinetics and mechanism of the decomposition of α-acetoxy-α-methoxytoluene 
in aqueous solution. J. Chem. Soc., Chem. Commun., 1976, 871-873
https://doi.org/10.1039/C39760000871
Calculated at pH = 10 using equation and constants in caption of Figure.
k0 = k_H2O + k_acid([H+]) + k_base([OH-]) 
Original rate measured at 15 degC
Ea estimation: 5 kcal + delta H rxn (298) from rmg thermo GAV (10.25 kcal), A adjusted to 313K
Arrhenius(A=(3.9e+01, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K'))
""",
)
