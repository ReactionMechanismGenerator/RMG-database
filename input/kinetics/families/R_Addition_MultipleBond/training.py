#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     0 {1,S} {6,D}
6  *2 C     1 {5,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5.31,"kcal/mol"),
        T0 = (1,"K"),
        Tmin = (373,"K"),
        Tmax = (493,"K"),
    ),
    reference = Article(authors=["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals', journal="J. Chem. Soc.", pages="""940-944""", year="1962", url="http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:1"),
    referenceType = "",
    shortDesc = u"""Dominguez et al. (1962). Data derived from fitting a complex mechanism.""",
    longDesc = 
u"""
Dominguez et al. Data derived from fitting to a complex mechanism.
Pressure 0.01-0.32 atm. Excitation : direct photolysis, analysis : GC. 
C2H2 + Tert-C4H9 --> (CH3)3CCH=CH

Was in the rules database with rank=4. Richard moved to the training database and checked with NIST database. NIST squib: 1962GAR/TRO940-944
This is the full rate; NB the degeneracy=2 so the per-site rate is half this.
""",
    history = [
        ("2011-08-09","Richard West <rwest@mit.edu>","action","""New entry. Moved from rules to training, cross-referenced with NIST and PrIMe."""),
    ],
)

