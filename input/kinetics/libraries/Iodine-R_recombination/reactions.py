#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination kinetic parameters for iodine-containing species"
shortDesc = u""" 
(see Table S2 of Supplementary material of Buras et al., Phys. Chem. Chem. Phys., 2018, 20, 13191-13214
DOI: 10.1039/C8CP01159A)
longDesc = u"""

entry(
    index = 1,
    label = "H + I <=> HI",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3E-31, 'cm^3/(molecule*s)'),
        n = -1.87,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (950, 'K'),
        Tmax = (1200, 'K'),
        Pmin=(1.87E5, 'Pa'),
        Pmax=(2.47E5, 'Pa'),
    ),
    reference = Article(
        authors = ["Lifshitz, A.; Tamburu, C.; Dubnikova, F."],
        title = u'Reactions of 1-naphthyl radicals with ethylene. Single pulse shock tube experiments, quantum chemical, transition state theory, and multiwell calculations',
        journal = "J. Phys. Chem. A",
        volume = "112",
        pages = """925-933""",
        year = "2008",
        url = "https://pubs.acs.org/doi/abs/10.1021/jp077289s",
    ),
    referenceType = "experiment",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc =
u"""
Bath gas: Ar
Excitation technique: Shock Tube
Analytical technique: GC-MS
""",
)

entry(
    index = 2,
    label = "I + I <=> I2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.51E-34,'cm^3/(molecule*s)'),
        n = 0,
        Ea = (-4.78, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (290, 'K'),
        Tmax = (1250, 'K'),
    ),
    reference = Article(
        authors = ["DL Baulch, J Duxbury, SJ Grant, DC Montague"],
        title = u'Evaluated kinetic data for high temperature reactions. Volume 4 Homogeneous gas phase reactions of halogen- and cyanide- containing species',
        journal = "Journal of Physical and Chemical Reference Data",
        volume = "10",
        year = "1981",
        url = "https://aip.scitation.org/doi/abs/10.1063/1.555664",
    ),
    referenceType = "experiment",
    shortDesc = u""" """,
    longDesc =
u"""
Bath gas: He
""",
)

entry(
    index = 3,
    label = "CH3 + I <=> CH3I",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.17E-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
     ),
    reference = Article(
        authors = ["Mulenko, S.A."],
        title = u'The application of an intracavity laser spectroscopy method for elementary processes study in gas-phase reactions',
        journal = "Rev. Roum. Phys.",
        volume = "32",
        pages = """173-178""",
        year = "1987",
        url = "https://scholar.google.com/scholar?cluster=5677687402182665117&hl=en&as_sdt=40000005&sciodt=0,22",
    ),
    referenceType = "experiment",
    shortDesc = u"""Measured at 400 K, 82 Torr CH3I bath gas""",
    longDesc =
u"""
Bath gas: CH3I
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 4,
    label = "C3H5 + I <=> C3H5I",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6E-10, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
     ),
    reference = Article(
        authors = ["Jenkin, M.E.; Murrells, T.P.; Shalliker, S.J.; Hayman, G.D."],
        title = u'Kinetics and product study of the self-reactions of allyl and allyl peroxy radicals at 296 K',
        journal = "Rev. Roum. Phys.",
        volume = "89",
        pages = """433-446""",
        year = "1993",
        url = "https://pubs.rsc.org/en/content/articlehtml/1993/ft/ft9938900433",
    ),
    referenceType = "experiment",
    shortDesc = u"""Measured at 296 K, 750 Torr N2 bath gas""",
    longDesc =
u"""
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 5,
    label = "C6H5 + I <=> C6H5I",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7E-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
     ),
    reference = Article(
        authors = ["A. Comandini, T. Malewicki, and K. Brezinsky"],
        title = u'Chemistry of Polycyclic Aromatic Hydrocarbons Formation from Phenyl Radical Pyrolysis and Reaction of Phenyl and Acetylene',
        journal = "J. Phys. Chem. A",
        volume = "116",
        pages = """2409−2434""",
        year = "2012",
        url = "https://pubs.acs.org/doi/pdf/10.1021/jp207461a",
    ),
    referenceType = "estimate",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc =
u"""
""",
)

entry(
    index = 6,
    label = "C6H5CH2 + I <=> C6H5CH2I",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8E-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
     ),
    reference=Article(
        authors=["Tom F. Hunter and Kristjan S. Kristjansson"],
        title=u'Optoacoustic method of measuring reaction rates of the radicals CH3, CD3, C2H5 and CH2I with I and I2',
        journal="J. Chem. Soc., Faraday Trans. 2",
        volume="78",
        pages="""2067-2076""",
        year="1982",
        url="http://pubs.rsc.org/-/content/articlehtml/1982/f2/f29827802067",
    ),
    referenceType="experiment",
    shortDesc=u"""Estimated from I + C2H5 -> C2H5I by Zach et al (Table S2)""",
    longDesc=
    u"""
    Bath gas: Kr (100 Torr)
    Estimated by Zach et al. by analogy to I + C2H5 -> C2H5I measured at 298 K, 100 Torr Kr bath gas and increased by 5 x to match MBMS experiments.
    Supplementary Information (Table S2) for Buras, Z. J. et al. Phenyl Radical + Propene: A Prototypical Reaction Surface for Aromatic-Catalyzed 1,2Hydrogen-Migration and Subsequent Resonance Stabilized Radical Formation
    """,
)

entry(
    index = 7,
    label = "C6H5CH2CHCH3 + I <=> C6H5CH2CHCH3I",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8E-11, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
     ),
    reference = Article(
        authors = ["Tom F. Hunter and Kristjan S. Kristjansson"],
        title = u'Optoacoustic method of measuring reaction rates of the radicals CH3, CD3, C2H5 and CH2I with I and I2',
        journal = "J. Chem. Soc., Faraday Trans. 2",
        volume = "78",
        pages = """2067-2076""",
        year = "1982",
        url = "http://pubs.rsc.org/-/content/articlehtml/1982/f2/f29827802067",
    ),
    referenceType = "experiment",
    shortDesc = u"""Estimated from I + C2H5 -> C2H5I by Zach et al (Table S2)""",
    longDesc =
u"""
Bath gas: Kr (100 Torr)
Estimated by analogy by Zach et al. to I + C2H5 -> C2H5I measured at 298 K, 100 Torr Kr bath gas and increased by 5 x to match MBMS experiments.
Supplementary Information (Table S2) for Buras, Z. J. et al. Phenyl Radical + Propene: A Prototypical Reaction Surface for Aromatic-Catalyzed 1,2Hydrogen-Migration and Subsequent Resonance Stabilized Radical Formation
""",
)
