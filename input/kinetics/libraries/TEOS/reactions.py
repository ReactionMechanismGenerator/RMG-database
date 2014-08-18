#!/usr/bin/env python
# encoding: utf-8

name = "TEOS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Si(OC2H5)4 <=> C2H4 + Si(OC2H5)3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+15, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "Si(OC2H5)4 <=> CH3 + CH2OSi(OC2H5)3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.981e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "Si(OC2H5)3OH <=> C2H4 + Si(OC2H5)2(OH)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.585e+15, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "Si(OC2H5)3OH <=> C2H5OH + O_Si(OC2H5)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.012e+11, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "Si(OC2H5)3OH <=> CH3 + CH2OSi(OC2H5)2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.162e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "Si(OC2H5)2(OH)2 <=> C2H4 + Si(OC2H5)(OH)3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "Si(OC2H5)2(OH)2 <=> H2O + O_Si(OC2H5)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.012e+11, 's^-1'), n=0, Ea=(39.74, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "Si(OC2H5)2(OH)2 <=> C2H5OH + O_Si(OC2H5)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+11, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "Si(OC2H5)2(OH)2 <=> CH3 + CH2OSi(OC2H5)(OH)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "Si(OC2H5)(OH)3 <=> C2H4 + Si(OH)4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "Si(OC2H5)(OH)3 <=> H2O + O_Si(OC2H5)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.012e+11, 's^-1'), n=0, Ea=(39.74, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "Si(OC2H5)(OH)3 <=> C2H5OH + O_Si(OH)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.012e+11, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "Si(OC2H5)(OH)3 <=> CH3 + CH2OSi(OH)3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "O_Si(OC2H5)2 <=> C2H4 + O_Si(OC2H5)OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(52.059, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1e+15, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 16,
    label = "O_Si(OC2H5)2 <=> CH3 + CH2OSiO(OC2H5)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "O_Si(OC2H5)OH <=> C2H4 + O_Si(OH)2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(5.012e+12, 's^-1'), n=0, Ea=(52.059, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.012e+14, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 19,
    label = "O_Si(OC2H5)OH <=> C2H5OH + SiO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.585e+11, 's^-1'), n=0, Ea=(47.092, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "O_Si(OC2H5)OH <=> CH3 + CH2OSiO(OH)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "CH3OSi(OC2H5)2(OC2H3) <=> C2H4 + CH3OSi(OC2H5)(OC2H3)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "CH3OSi(OC2H5)2(OC2H3) <=> CH3 + CH2OSi(OC2H5)(OC2H3)(OCH3)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "CH3OSi(OC2H5)(OC2H3)OH <=> C2H4 + CH3OSi(OC2H3)(OH)2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.012e+14, 's^-1'), n=0, Ea=(68.552, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "CH3OSi(OC2H5)(OC2H3)OH <=> CH3 + CH2OSi(OCH3)(OC2H3)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "CH3OSi(OC2H5)(OC2H3)OH <=> C2H5OH + CH3OSi(O)OC2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.585e+11, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "C2H5OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+13, 's^-1'), n=0, Ea=(66.167, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "C2H5OH <=> CH3 + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(83.057, 'kcal/mol'), T0=(1, 'K')),
)

