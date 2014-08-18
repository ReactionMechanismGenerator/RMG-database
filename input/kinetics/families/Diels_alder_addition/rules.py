#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 589,
    label = "diene_out;diene_in;ene",
    kinetics = ArrheniusEP(
        A = (5000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
    longDesc = 
u"""

""",
)

entry(
    index = 590,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_2H_HDe",
    kinetics = ArrheniusEP(
        A = (8910000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (24.44, 'kcal/mol'),
        Tmin = (464, 'K'),
        Tmax = (557, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [198]""",
    longDesc = 
u"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.
""",
)

entry(
    index = 591,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_HDe_2H",
    kinetics = ArrheniusEP(
        A = (8910000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (24.44, 'kcal/mol'),
        Tmin = (464, 'K'),
        Tmax = (557, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [198]""",
    longDesc = 
u"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.
""",
)

entry(
    index = 592,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_HNd_HDe",
    kinetics = ArrheniusEP(
        A = (899000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (22.06, 'kcal/mol'),
        Tmin = (515, 'K'),
        Tmax = (572, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
)

entry(
    index = 593,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_HDe_HNd",
    kinetics = ArrheniusEP(
        A = (899000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (22.06, 'kcal/mol'),
        Tmin = (515, 'K'),
        Tmax = (572, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
)

entry(
    index = 594,
    label = "diene_unsub_unsub_out;diene_in_HNd;ene_unsub_unsub",
    kinetics = ArrheniusEP(
        A = (132000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (29.61, 'kcal/mol'),
        Tmin = (1000, 'K'),
        Tmax = (1180, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Simmie [199]""",
    longDesc = 
u"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm
""",
)

entry(
    index = 595,
    label = "diene_unsub_unsub_out;diene_in_NdH;ene_unsub_unsub",
    kinetics = ArrheniusEP(
        A = (132000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (29.61, 'kcal/mol'),
        Tmin = (1000, 'K'),
        Tmax = (1180, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Simmie [199]""",
    longDesc = 
u"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm
""",
)

entry(
    index = 596,
    label = "diene_unsub_unsub_out;diene_in_HNd;ene_HDe_2H",
    kinetics = ArrheniusEP(
        A = (1020000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.7, 'kcal/mol'),
        Tmin = (492, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
)

entry(
    index = 597,
    label = "diene_unsub_unsub_out;diene_in_NdH;ene_2H_HDe",
    kinetics = ArrheniusEP(
        A = (1020000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (18.7, 'kcal/mol'),
        Tmin = (492, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
)

entry(
    index = 598,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_unsub_unsub",
    kinetics = ArrheniusEP(
        A = (4570000000.0, 'cm^3/(mol*s)', '*|/', 1.05),
        n = 0,
        alpha = 0,
        E0 = (26.03, 'kcal/mol'),
        Tmin = (450, 'K'),
        Tmax = (592, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [109]""",
    longDesc = 
u"""
[109] Huybrechts, G.; Rigaux, D.; Vankeerberghen, J.; Van Mele, B. Int. J. Chem. Kinet. 1980, 12, 253.
1,3-cyclohexadiene + C2H4 --> bicyclo[2.2.2]oct-2-ene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.05-0.25 atm.
""",
)

entry(
    index = 599,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    kinetics = ArrheniusEP(
        A = (1120000000.0, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        alpha = 0,
        E0 = (26.63, 'kcal/mol'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 600,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    kinetics = ArrheniusEP(
        A = (2090000000.0, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        alpha = 0,
        E0 = (28.81, 'kcal/mol'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 601,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    kinetics = ArrheniusEP(
        A = (708000000.0, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        alpha = 0,
        E0 = (26.23, 'kcal/mol'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + 1-C4H8 --> bicyclo[2.2.2]oct-2-ene,5-ETHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 602,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    kinetics = ArrheniusEP(
        A = (1170000000.0, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        alpha = 0,
        E0 = (28.62, 'kcal/mol'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + 1-C4H8 --> bicyclo[2.2.2]oct-2-ene,5-ETHYL-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 603,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    kinetics = ArrheniusEP(
        A = (372000000.0, 'cm^3/(mol*s)', '*|/', 1.07),
        n = 0,
        alpha = 0,
        E0 = (26.63, 'kcal/mol'),
        Tmin = (488, 'K'),
        Tmax = (600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + (CH3)2CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-(1-METHYLETHYL)-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 604,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    kinetics = ArrheniusEP(
        A = (295000000.0, 'cm^3/(mol*s)', '*|/', 1.1),
        n = 0,
        alpha = 0,
        E0 = (28.42, 'kcal/mol'),
        Tmin = (486, 'K'),
        Tmax = (600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + (CH3)2CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-(1-METHYLETHYL)-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 605,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_2H",
    kinetics = ArrheniusEP(
        A = (1120000000.0, 'cm^3/(mol*s)', '*|/', 1.12),
        n = 0,
        alpha = 0,
        E0 = (26.63, 'kcal/mol'),
        Tmin = (488, 'K'),
        Tmax = (606, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
)

entry(
    index = 606,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    kinetics = ArrheniusEP(
        A = (1020000000.0, 'cm^3/(mol*s)', '*|/', 1.07),
        n = 0,
        alpha = 0,
        E0 = (20.07, 'kcal/mol'),
        Tmin = (379, 'K'),
        Tmax = (581, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
)

entry(
    index = 607,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    kinetics = ArrheniusEP(
        A = (603000000.0, 'cm^3/(mol*s)', '*|/', 1.07),
        n = 0,
        alpha = 0,
        E0 = (20.87, 'kcal/mol'),
        Tmin = (379, 'K'),
        Tmax = (581, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2beta, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
)

entry(
    index = 608,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    kinetics = ArrheniusEP(
        A = (11500000000.0, 'cm^3/(mol*s)', '*|/', 1.05),
        n = 0,
        alpha = 0,
        E0 = (26.83, 'kcal/mol'),
        Tmin = (437, 'K'),
        Tmax = (526, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [111]""",
    longDesc = 
u"""
[111] Huybrechts, G.;Hubin, Y.; Narmon, M.; Van Mele, B. Int. J. Chem. Kinet. 1982, 14, 259.
1,3-cyclohexadiene + (E)CH2=CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-ethenyl(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.15-0.64 atm.
""",
)

entry(
    index = 609,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    kinetics = ArrheniusEP(
        A = (3800000000.0, 'cm^3/(mol*s)', '*|/', 1.05),
        n = 0,
        alpha = 0,
        E0 = (24.84, 'kcal/mol'),
        Tmin = (437, 'K'),
        Tmax = (526, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Huybrechts et al. [111]""",
    longDesc = 
u"""
[111] Huybrechts, G.;Hubin, Y.; Narmon, M.; Van Mele, B. Int. J. Chem. Kinet. 1982, 14, 259.
1,3-cyclohexadiene + (E)CH2=CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-ethenyl(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.15-0.64 atm.
""",
)

entry(
    index = 610,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_2H",
    kinetics = ArrheniusEP(
        A = (1020000000.0, 'cm^3/(mol*s)', '*|/', 1.07),
        n = 0,
        alpha = 0,
        E0 = (20.07, 'kcal/mol'),
        Tmin = (379, 'K'),
        Tmax = (581, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
)

entry(
    index = 611,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_HDe",
    kinetics = ArrheniusEP(
        A = (1260000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.69, 'kcal/mol'),
        Tmin = (352, 'K'),
        Tmax = (423, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.
""",
)

entry(
    index = 612,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_HNd",
    kinetics = ArrheniusEP(
        A = (1260000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.69, 'kcal/mol'),
        Tmin = (352, 'K'),
        Tmax = (423, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.
""",
)

entry(
    index = 614,
    label = "diene_5ring_Nd_Nd_out;diene_in_2H;ene_HNd_HNd",
    kinetics = ArrheniusEP(
        A = (3.24E-01, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (24.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A.G. Vandeputte""",
    longDesc = 
u"""
""",
)

