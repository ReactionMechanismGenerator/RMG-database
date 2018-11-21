#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C4H6 + C2H4 <=> C6H10",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1e+10,'cm^3/(mol*s)'), n=0, Ea=(83.68,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """default""",
    longDesc = 
"""
Converted to training reaction from rate rule: diene_out;diene_in;ene
""",
)

entry(
    index = 1,
    label = "C4H6-2 + C4H6 <=> C8H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.91e+09,'cm^3/(mol*s)'), n=0, Ea=(102.257,'kJ/mol'), T0=(1,'K'), Tmin=(464,'K'), Tmax=(557,'K')),
    rank = 6,
    shortDesc = """Huybrechts et al. [198]""",
    longDesc = 
"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.

Degeneracy not recalculated

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_2H_HDe
""",
)

entry(
    index = 2,
    label = "C4H6-3 + C4H6 <=> C8H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.91e+09,'cm^3/(mol*s)'), n=0, Ea=(102.257,'kJ/mol'), T0=(1,'K'), Tmin=(464,'K'), Tmax=(557,'K')),
    rank = 6,
    shortDesc = """Huybrechts et al. [198]""",
    longDesc = 
"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.

Degeneracy not recalculated

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_HDe_2H
""",
)

entry(
    index = 3,
    label = "C5H8 + C4H6 <=> C9H14",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.798e+09,'cm^3/(mol*s)'), n=0, Ea=(92.299,'kJ/mol'), T0=(1,'K'), Tmin=(515,'K'), Tmax=(572,'K')),
    rank = 6,
    shortDesc = """Kistiakowsky et al [112]""",
    longDesc = 
"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_HNd_HDe
""",
)

entry(
    index = 4,
    label = "C5H8-2 + C4H6 <=> C9H14-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.798e+09,'cm^3/(mol*s)'), n=0, Ea=(92.299,'kJ/mol'), T0=(1,'K'), Tmin=(515,'K'), Tmax=(572,'K')),
    rank = 6,
    shortDesc = """Kistiakowsky et al [112]""",
    longDesc = 
"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;ene_HDe_HNd
""",
)

entry(
    index = 5,
    label = "C5H8-3 + C2H4 <=> C7H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.64e+11,'cm^3/(mol*s)'), n=0, Ea=(123.888,'kJ/mol'), T0=(1,'K'), Tmin=(1000,'K'), Tmax=(1180,'K')),
    rank = 10,
    shortDesc = """Simmie [199]""",
    longDesc = 
"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_HNd;ene_unsub_unsub
""",
)

entry(
    index = 6,
    label = "C2H4 + C5H8-4 <=> C7H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.32e+11,'cm^3/(mol*s)'), n=0, Ea=(123.888,'kJ/mol'), T0=(1,'K'), Tmin=(1000,'K'), Tmax=(1180,'K')),
    rank = 10,
    shortDesc = """Simmie [199]""",
    longDesc = 
"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm

Degeneracy not recalculated

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_NdH;ene_unsub_unsub
""",
)

entry(
    index = 7,
    label = "C4H6-3 + C5H8-3 <=> C9H14-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.04e+09,'cm^3/(mol*s)'), n=0, Ea=(78.2408,'kJ/mol'), T0=(1,'K'), Tmin=(492,'K'), Tmax=(606,'K')),
    rank = 6,
    shortDesc = """Kistiakowsky et al [112]""",
    longDesc = 
"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_HNd;ene_HDe_2H
""",
)

entry(
    index = 8,
    label = "C4H6-2 + C5H8-4 <=> C9H14-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.04e+09,'cm^3/(mol*s)'), n=0, Ea=(78.2408,'kJ/mol'), T0=(1,'K'), Tmin=(492,'K'), Tmax=(606,'K')),
    rank = 6,
    shortDesc = """Kistiakowsky et al [112]""",
    longDesc = 
"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm

Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_NdH;ene_2H_HDe
""",
)

entry(
    index = 9,
    label = "C2H4 + C6H10-2 <=> C8H14",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.14e+09,'cm^3/(mol*s)','*|/',1.05), n=0, Ea=(108.91,'kJ/mol'), T0=(1,'K'), Tmin=(450,'K'), Tmax=(592,'K')),
    rank = 6,
    shortDesc = """Huybrechts et al. [109]""",
    longDesc = 
"""
[109] Huybrechts, G.; Rigaux, D.; Vankeerberghen, J.; Van Mele, B. Int. J. Chem. Kinet. 1980, 12, 253.
1,3-cyclohexadiene + C2H4 --> bicyclo[2.2.2]oct-2-ene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.05-0.25 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_unsub_unsub
""",
)

entry(
    index = 10,
    label = "C3H6 + C6H10-2 <=> C9H16",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.24e+09,'cm^3/(mol*s)','*|/',1.12), n=0, Ea=(111.42,'kJ/mol'), T0=(1,'K'), Tmin=(488,'K'), Tmax=(606,'K')),
    rank = 6,
    shortDesc = """Huybrechts et al. [108]""",
    longDesc = 
"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd
""",
)

entry(
    index = 11,
    label = "C3H6-2 + C6H10-2 <=> C9H16-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.24e+09,'cm^3/(mol*s)','*|/',1.12), n=0, Ea=(111.42,'kJ/mol'), T0=(1,'K'), Tmin=(488,'K'), Tmax=(606,'K')),
    rank = 6,
    shortDesc = """Huybrechts et al. [108]""",
    longDesc = 
"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_2H
""",
)

entry(
    index = 12,
    label = "C4H6-2 + C6H10-2 <=> C10H16",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4.08e+09,'cm^3/(mol*s)','*|/',1.07), n=0, Ea=(83.9729,'kJ/mol'), T0=(1,'K'), Tmin=(379,'K'), Tmax=(581,'K')),
    rank = 6,
    shortDesc = """Van Mele et al [110]""",
    longDesc = 
"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe
""",
)

entry(
    index = 13,
    label = "C4H6-3 + C6H10-2 <=> C10H16-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4.08e+09,'cm^3/(mol*s)','*|/',1.07), n=0, Ea=(83.9729,'kJ/mol'), T0=(1,'K'), Tmin=(379,'K'), Tmax=(581,'K')),
    rank = 6,
    shortDesc = """Van Mele et al [110]""",
    longDesc = 
"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_2H
""",
)

entry(
    index = 14,
    label = "C5H8 + C6H10-2 <=> C11H18",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.52e+09,'cm^3/(mol*s)'), n=0, Ea=(69.831,'kJ/mol'), T0=(1,'K'), Tmin=(352,'K'), Tmax=(423,'K')),
    rank = 6,
    shortDesc = """Benford et al [200]""",
    longDesc = 
"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_HDe
""",
)

entry(
    index = 15,
    label = "C5H8-2 + C6H10-2 <=> C11H18-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.52e+09,'cm^3/(mol*s)'), n=0, Ea=(69.831,'kJ/mol'), T0=(1,'K'), Tmin=(352,'K'), Tmax=(423,'K')),
    rank = 6,
    shortDesc = """Benford et al [200]""",
    longDesc = 
"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.

Converted to training reaction from rate rule: diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_HNd
""",
)

entry(
    index = 16,
    label = "C7H10 + C4H8 <=> C11H18-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.1622,'cm^3/(mol*s)'), n=3.05, Ea=(103.554,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """A. G. Vandeputte, BMK/cbsb7 HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: diene_5ring_Nd_Nd_out;diene_in_2H;ene_HNd_HNd
""",
)

entry(
    index = 17,
    label = "C3H4 + C4H6 <=> C7H10-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.244,'cm^3/(mol*s)'), n=2.98, Ea=(117.57,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """A. G. Vandeputte, BMK/cbsb7 HO, butadiene + propyne""",
    longDesc = 
"""
Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;yne_unsub_monosub
""",
)

entry(
    index = 18,
    label = "C3H4-2 + C4H6 <=> C7H10-3",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.708,'cm^3/(mol*s)'), n=2.94, Ea=(121.336,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """A. G. Vandeputte, BMK/cbsb7 HO, butadiene + allene""",
    longDesc = 
"""
Converted to training reaction from rate rule: diene_unsub_unsub_out;diene_in_2H;allene_unsub
""",
)

entry(
    index = 20,
    label = "C6H6 + C6H4 <=> C12H10",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(5809, 'cm^3/(mol*s)'), n=2.526, Ea=(5.92, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Comandini, A.', 'Brezinsky, K.'],
        title = 'Theoretical Study of the Formation of Naphthalene from the Radical/pi-Bond Addition between Single-Ring Aromatic Hydrocarbons',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115',
        pages = '5547-5559',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 6,
    longDesc = 
u"""
uCCSD(T) with Dunning's correclation-consistent polarized double basis set (cc-pVDZ), TST.
""",
)

entry(
    index = 21,
    label = "C12H10-2 <=> C2H2 + C10H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.458e+14, 's^-1'), n=0.0956, Ea=(54.82, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Comandini, A.', 'Brezinsky, K.'],
        title = 'Theoretical Study of the Formation of Naphthalene from the Radical/pi-Bond Addition between Single-Ring Aromatic Hydrocarbons',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115',
        pages = '5547-5559',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 6,
    longDesc = 
u"""
uCCSD(T) with Dunning's correclation-consistent polarized double basis set (cc-pVDZ), TST.
""",
)

entry(
    index = 22,
    label = "C12H10-3 + C2H2 <=> C14H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (16.92, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (42.193, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 8,
    longDesc = 
u"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations;
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: B1 + C2H2 <=> B2
""",
)

entry(
    index = 23,
    label = "C14H10 + C2H2 <=> C16H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (43.24, 'cm^3/(mol*s)'),
        n = 2.58,
        Ea = (41.945, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 8,
    longDesc = 
u"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations; 
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: P + C2H2 <=> P1
""",
)

entry(
    index = 24,
    label = "C6H6 + C2H2 <=> C8H8",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (261.981, 'cm^3/(mol*s)'),
        n = 2.6786,
        Ea = (147.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
CBS-QB3 calculation by MLIU
""",
)

entry(
    index = 25,
    label = "C10H8 + C2H2 <=> C12H10-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (286.399, 'cm^3/(mol*s)'),
        n = 2.61957,
        Ea = (115.627, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
CBS-QB3 calculation by MLIU
""",
)

entry(
    index = 26,
    label = "C10H8-2 + C2H2 <=> C12H10-4",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (133.129, 'cm^3/(mol*s)'),
        n = 2.69336,
        Ea = (173.905, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
CBS-QB3 calculation by MLIU
""",
)

