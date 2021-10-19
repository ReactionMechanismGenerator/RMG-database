#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/training"
shortDesc = "Retroene reaction family"
longDesc = """
Training reactions for retroene reaction family.
Some species are marked as '(rxnX)' to allow it to match different template.
"""
entry(
    index = 0,
    label = "nBA <=> C4H8-1 + AcOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3496.64,'s^-1'), n=2.72265, Ea=(192.668,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.90869, dn = +|- 0.0858988, dEa = +|- 0.439996 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 1,
    label = "iBA <=> iC4H8(rxn2) + AcOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16053e+06,'s^-1'), n=1.87467, Ea=(202.966,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.39386, dn = +|- 0.0441278, dEa = +|- 0.226034 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 2,
    label = "sBA(rxn1) <=> C4H8-1 + AcOH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.8952e+07,'s^-1'), n=1.63805, Ea=(190.506,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.44153, dn = +|- 0.0485968, dEa = +|- 0.248926 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 3,
    label = "tBA <=> iC4H8(rxn1) + AcOH",
    degeneracy = 9.0,
    kinetics = Arrhenius(A=(3.89757e+09,'s^-1'), n=1.19379, Ea=(176.117,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.13961, dn = +|- 0.0173664, dEa = +|- 0.0889553 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 4,
    label = "sBA(rxn2) <=> C4H8-2 + AcOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.16601e+09,'1/s'), n=1.07561, Ea=(193.552,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to Multiple Arrhenius kinetics over range 300.0-2000.0 K. """),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
    longDesc = 
"""
There are two different TS conformers (cis and trans) related to different H atom
reacting. The kinetics is fitted from the sum of the individual rate coeffs.
""",
)

entry(
    index = 5,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.7e+11,'1/s'), n=0, Ea=(233,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 6,
    label = "C6H12 <=> C3H6 + C3H6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.1e+11,'1/s'), n=0, Ea=(226,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 7,
    label = "C6H12-2 <=> C4H8 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(9.7e+11,'1/s'), n=0, Ea=(238,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 8,
    label = "C7H12 <=> C3H6 + C4H6",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(9.1e+11,'1/s'), n=0, Ea=(205,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 9,
    label = "C8H14O2 <=> C3H6 + C5H8O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1e+12,'1/s'), n=0, Ea=(223,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 10,
    label = "C7H12O2 <=> C3H6 + C4H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.7e+10,'1/s'), n=0, Ea=(198,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 11,
    label = "C8H14O2-2 <=> C4H8 + C4H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.3e+11,'1/s'), n=0, Ea=(205,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 12,
    label = "C4H6O2-2 <=> C3H4O + CH2O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.4e+12,'1/s'), n=0, Ea=(272,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 13,
    label = "C4H9N <=> C3H6 + CH3N",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.34423e+11,'1/s'), n=0, Ea=(181.5,'kJ/mol'), T0=(1,'K'), Tmin=(602,'K'), Tmax=(694,'K')),
    rank = 9,
    shortDesc = """Measured from experiment""",
    longDesc = 
"""
Cited from: Vitins P, Egger K W. The thermochemical kinetics of the retro-‘ene’reactions of
molecules with the general structure (allyl) XYH in the gas phase. Part IX.
Unimolecular thermal decompostion of allylmethylamine[J]. Journal of the Chemical
Society, Perkin Transactions 2, 1974 (11): 1289-1291.
""",
)

entry(
    index = 14,
    label = "C4H8O <=> C3H6 + CH2O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.23027e+11,'1/s'), n=0, Ea=(174.05,'kJ/mol'), T0=(1,'K'), Tmin=(725,'K'), Tmax=(810,'K')),
    rank = 9,
    shortDesc = """Measured from experiment""",
    longDesc = 
"""
Cited from: Kwart H, Sarner S F, Slutsky J. Mechanisms of thermolytic fragmentation of allyl
ethers. I[J]. Journal of the American Chemical Society, 1973, 95(16): 5234-5242.
""",
)

entry(
    index = 15,
    label = "C4H8S <=> C3H6 + CH2S",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.69824e+11,'1/s'), n=0, Ea=(160,'kJ/mol'), T0=(1,'K'), Tmin=(588,'K'), Tmax=(691,'K')),
    rank = 9,
    shortDesc = """Measured from experiment""",
    longDesc = 
"""
Cited from: Martin G, Ropero M, Avila R. Gas-phase thermolysis of sulfur compounds.
Part V. Methyl allyl, diallyl and benzyl allyl sulfides[J]. Phosphorus and Sulfur
and the Related Elements, 1982, 13(2): 213-220.
""",
)

entry(
    index = 16,
    label = "C4H8O-2 <=> C2H4O + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1e+08,'1/s'), n=1.2, Ea=(44,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3""",
    longDesc = 
"""
Cited from: Jarvis, M. W., Daily, J. W., Carstensen, H. H., Dean, A. M., Sharma, S., Dayton,
D. C., ... & Nimlos, M. R. (2011). Direct detection of products from the pyrolysis
of 2-phenethyl phenyl ether. The Journal of Physical Chemistry A, 115(4), 428-438.
""",
)

entry(
    index = 17,
    label = "C8H10O <=> C6H6O + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(5.5e+07,'1/s'), n=1.6, Ea=(54,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3""",
    longDesc = 
"""
Cited from: Jarvis, M. W., Daily, J. W., Carstensen, H. H., Dean, A. M., Sharma, S., Dayton,
D. C., ... & Nimlos, M. R. (2011). Direct detection of products from the pyrolysis
of 2-phenethyl phenyl ether. The Journal of Physical Chemistry A, 115(4), 428-438.
""",
)

entry(
    index = 18,
    label = "C5H10O2 <=> AcOH + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(7.94328e+12,'1/s'), n=0, Ea=(44.7,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 19,
    label = "C14H14O <=> C6H6O + C8H8",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.2e+06,'1/s'), n=0.9, Ea=(49,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3""",
    longDesc = 
"""
Cited from: Jarvis, M. W., Daily, J. W., Carstensen, H. H., Dean, A. M., Sharma, S., Dayton,
D. C., ... & Nimlos, M. R. (2011). Direct detection of products from the pyrolysis
of 2-phenethyl phenyl ether. The Journal of Physical Chemistry A, 115(4), 428-438.
""",
)

entry(
    index = 20,
    label = "C7H14O2 <=> AcOH + C5H10-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.91251e+12,'1/s'), n=0, Ea=(39.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 21,
    label = "C7H14O2-2 <=> C3H6O2 + iC4H8(rxn1)",
    degeneracy = 9.0,
    kinetics = Arrhenius(A=(1.25893e+13,'1/s'), n=0, Ea=(40,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 22,
    label = "C7H12O3 <=> AcOH + C5H8O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.98107e+11,'1/s'), n=0, Ea=(36.6,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 23,
    label = "C7H12O2-2 <=> AcOH + C5H8",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.51189e+12,'1/s'), n=0, Ea=(43.9,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 24,
    label = "C7H12O2-3 <=> AcOH + C5H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(43.9,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 25,
    label = "C4H6O3 <=> AcOH + C2H2O",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(36.1,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 26,
    label = "C10H12O2 <=> AcOH + C8H8-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(43.7,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 27,
    label = "C10H12O2-2 <=> AcOH + C8H8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(45.1,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 28,
    label = "C16H16O2 <=> AcOH + C14H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.51189e+12,'1/s'), n=0, Ea=(41.7,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 29,
    label = "C4H8O2 <=> CH2O2 + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(6.30957e+12,'1/s'), n=0, Ea=(44.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 30,
    label = "C5H10O2-2 <=> CH2O2 + iC4H8(rxn1)",
    degeneracy = 9.0,
    kinetics = Arrhenius(A=(1e+13,'1/s'), n=0, Ea=(39.3,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 31,
    label = "C5H10O2-3 <=> AcOH + C3H6-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.99526e+12,'1/s'), n=0, Ea=(47.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 32,
    label = "C7H14O2-3 <=> AcOH + C5H10-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(46.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 33,
    label = "C7H14O2-4 <=> AcOH + C5H10-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(46.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 34,
    label = "C8H16O2 <=> AcOH + C6H12-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94328e+11,'1/s'), n=0, Ea=(45.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 35,
    label = "C5H10O3 <=> AcOH + C3H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(48.6,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 36,
    label = "C6H12O3 <=> AcOH + C4H8O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(48.3,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 37,
    label = "C7H14O2-5 <=> AcOH + C5H10-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.23872e+12,'1/s'), n=0, Ea=(43.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 38,
    label = "C7H14O2-6 <=> AcOH + C5H10-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(43.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 39,
    label = "C7H14O2-7 <=> AcOH + C5H10-7",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(7.94328e+12,'1/s'), n=0, Ea=(44.1,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc = 
"""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 40,
    label = "C3H6O2-2 <=> CH2O2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.19e+11,'1/s'), n=0.59, Ea=(49800,'cal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """calculated at CCSD(T)/CBS//M06-2X/cc-pVTZ""",
    longDesc = 
"""
Cited from: Sun, W., Tao, T., Zhang, R., Liao, H., Huang, C., Zhang, F., ... & Yang, B. (2017).
Experimental and modeling efforts towards a better understanding of the high-temperature
combustion kinetics of C3C5 ethyl esters. Combustion and Flame, 185, 173-187. The original data
is P-dep, and the rate coeff. recorded in this library is the rate coeff. for 100 atm.
""",
)

entry(
    index = 41,
    label = "C4H8O2-2 <=> AcOH + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.36e+14,'1/s'), n=-0.3, Ea=(49900,'cal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """calculated at CCSD(T)/CBS//M06-2X/cc-pVTZ""",
    longDesc = 
"""
Cited from: Sun, W., Tao, T., Zhang, R., Liao, H., Huang, C., Zhang, F., ... & Yang, B. (2017).
Experimental and modeling efforts towards a better understanding of the high-temperature
combustion kinetics of C3C5 ethyl esters. Combustion and Flame, 185, 173-187. The original data
is P-dep, and the rate coeff. recorded in this library is the rate coeff. for 100 atm.
""",
)

entry(
    index = 42,
    label = "C5H10O2-4 <=> C3H6O2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(6.93e+08,'1/s'), n=1.27, Ea=(48500,'cal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """calculated at CCSD(T)/CBS//M06-2X/cc-pVTZ""",
    longDesc = 
"""
Cited from: Sun, W., Tao, T., Zhang, R., Liao, H., Huang, C., Zhang, F., ... & Yang, B. (2017).
Experimental and modeling efforts towards a better understanding of the high-temperature
combustion kinetics of C3C5 ethyl esters. Combustion and Flame, 185, 173-187. The original data
is P-dep, and the rate coeff. recorded in this library is the rate coeff. for 100 atm.
""",
)

entry(
    index = 43,
    label = "C7H12O3-2 <=> C5H8O3 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.0893e+13,'1/s'), n=0, Ea=(49518,'cal/mol'), T0=(1,'K'), Tmin=(900,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at G3//MP2/aug-cc-pVDZ""",
    longDesc = 
"""
AlAbbad, M., Giri, B. R., Szőri, M., & Farooq, A. (2017). On the high-temperature
unimolecular decomposition of ethyl levulinate. Proceedings of the Combustion
Institute, 36(1), 187-193.
""",
)

entry(
    index = 44,
    label = "C5H10O3-2 <=> C3H6O3 + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(348015,'1/s'), n=0.286, Ea=(158771,'J/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1300,'K')),
    rank = 5,
    shortDesc = """calculated at G3//MP2/aug-cc-pVDZ""",
    longDesc = 
"""
AlAbbad, M., Giri, B. R., Szőri, M., Viskolcz, B., & Farooq, A. (2017). A high
temperature kinetic study for the thermal unimolecular decomposition of diethyl
carbonate. Chemical Physics Letters, 684, 390-396.
""",
)

entry(
    index = 45,
    label = "C5H10O <=> C2H4O-2 + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(127.587,'s^-1'), n=2.97303, Ea=(221.127,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.52331, dn = +|- 0.0559292, dEa = +|- 0.286484 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 46,
    label = "C5H10O-2 <=> C3H6O-2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(34.7517,'s^-1'), n=3.09547, Ea=(214.25,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.47481, dn = +|- 0.0516299, dEa = +|- 0.264462 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 47,
    label = "C5H10O-3 <=> C2H4O-2 + C3H6-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(13.6131,'s^-1'), n=3.07798, Ea=(218.469,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.52121, dn = +|- 0.0557459, dEa = +|- 0.285545 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 48,
    label = "C4H9NO <=> C2H5NO + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(7.78487,'s^-1'), n=3.40032, Ea=(211.103,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.70197, dn = +|- 0.0706665, dEa = +|- 0.361972 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 49,
    label = "C4H10N2O <=> C2H5NO + C2H5N",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(171001,'s^-1'), n=2.19797, Ea=(217.237,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.46775, dn = +|- 0.050992, dEa = +|- 0.261195 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 50,
    label = "C5H11NO <=> C3H6O-2 + C2H5N",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(13104.2,'s^-1'), n=2.29082, Ea=(214.941,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.43309, dn = +|- 0.0478167, dEa = +|- 0.24493 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 51,
    label = "C6H12O <=> C3H6O-2 + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(6102.65,'s^-1'), n=2.55399, Ea=(214.789,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.35527, dn = +|- 0.0403969, dEa = +|- 0.206924 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 52,
    label = "C5H11NO-2 <=> C2H5NO + C3H6-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3416.42,'s^-1'), n=2.62955, Ea=(212.275,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.33575, dn = +|- 0.0384693, dEa = +|- 0.19705 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 53,
    label = "C6H12O-2 <=> C3H6O-2 + C3H6-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(918.473,'s^-1'), n=2.68918, Ea=(213.037,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.44504, dn = +|- 0.0489194, dEa = +|- 0.250578 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 54,
    label = "C4H8O-4 <=> C2H4O-2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.21309,'s^-1'), n=3.32108, Ea=(220.256,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.52174, dn = +|- 0.0557923, dEa = +|- 0.285783 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 55,
    label = "C4H8O2-3 <=> C2H4O2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.7605e+06,'s^-1'), n=1.80968, Ea=(236.043,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.60655, dn = +|- 0.0629992, dEa = +|- 0.322699 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 56,
    label = "C5H10O2-5 <=> C2H4O2 + C3H6-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.2279e+08,'s^-1'), n=1.36832, Ea=(234.848,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.45449, dn = +|- 0.049786, dEa = +|- 0.255017 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 57,
    label = "C4H8O2-4 <=> C2H4O-2 + C2H4O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.13509e+12,'s^-1'), n=0.169307, Ea=(240.476,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.14422, dn = +|- 0.0179031, dEa = +|- 0.0917044 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 58,
    label = "C5H10O2-6 <=> C3H6O-2 + C2H4O-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(6.05189e+12,'s^-1'), n=0.0499164, Ea=(232.901,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.22917, dn = +|- 0.0274189, dEa = +|- 0.140447 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 59,
    label = "C5H10O2-7 <=> C2H4O2 + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(9.91109e+07,'s^-1'), n=1.51788, Ea=(236.313,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.50331, dn = +|- 0.0541732, dEa = +|- 0.277489 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 60,
    label = "C4H9NO-2 <=> C2H4O-2 + C2H5N",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4838.42,'s^-1'), n=2.3826, Ea=(221.139,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.44929, dn = +|- 0.04931, dEa = +|- 0.252579 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 61,
    label = "C5H11NO-3 <=> C2H5NO + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(669082,'s^-1'), n=2.05353, Ea=(215.947,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.26289, dn = +|- 0.0310154, dEa = +|- 0.158869 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 62,
    label = "C4H8O3 <=> C2H4O2 + C2H4O-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.4836e+09,'s^-1'), n=1.04991, Ea=(238.94,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.28482, dn = +|- 0.0333034, dEa = +|- 0.170589 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 63,
    label = "C4H9NO2 <=> C2H5NO + C2H4O-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.89231e+07,'s^-1'), n=1.41637, Ea=(213.544,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.17678, dn = +|- 0.0216307, dEa = +|- 0.110798 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 64,
    label = "C4H9NO2-2 <=> C2H4O2 + C2H5N",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.75702e+08,'s^-1'), n=1.30992, Ea=(238.61,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.87631, dn = +|- 0.083625, dEa = +|- 0.428349 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.""",
    longDesc = 
"""
Calculated at CBS-QB3 using TST + 1DSHR approximation by Jeffrey Herron, Xiaorui Dong, and Duminda Ranasinghe.
""",
)

entry(
    index = 65,
    label = "C2H4N2O2 <=> CH3NO + CHNO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.3103e+06,'s^-1'), n=1.91844, Ea=(215.344,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 2.14216, dn = +|- 0.101085, dEa = +|- 0.521248 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction index that corresponds to the raw QM log files from the kinetics dataset from Spiekermann et al.: rxn001091
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 66,
    label = "C2H4N2O2-2 <=> CH3NO-2 + CHNO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.91827e+10,'s^-1'), n=0.736578, Ea=(60.3985,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14366, dn = +|- 0.0178114, dEa = +|- 0.0918447 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction index that corresponds to the raw QM log files from the kinetics dataset from Spiekermann et al.: rxn001689
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 67,
    label = "C2H4N2O <=> CH3NO + CHN",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.96843e+10,'s^-1'), n=0.78544, Ea=(151.759,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12608, dn = +|- 0.0157564, dEa = +|- 0.0812481 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction index that corresponds to the raw QM log files from the kinetics dataset from Spiekermann et al.: rxn005591
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

