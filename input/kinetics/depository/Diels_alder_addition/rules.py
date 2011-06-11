#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 589,
    label = "diene_out;diene_in;ene",
    group1 = "OR{diene_unsub_unsub_out, diene_unsub_monosub_out, diene_unsub_disub_out, diene_monosub_monosub_out, diene_monosub_disub_out, diene_disub_disub_out}",
    group2 = 
"""
1  *4 Cd 0 {2,S}
2  *5 Cd 0 {1,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (5e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 590,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_2H_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (8.91e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (24.44,"kcal/mol"),
        Tmin = (464,"K"),
        Tmax = (557,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [198]""",
    longDesc = 
u"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 591,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_HDe_2H",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (8.91e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (24.44,"kcal/mol"),
        Tmin = (464,"K"),
        Tmax = (557,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [198]""",
    longDesc = 
u"""
[198] Huybrechts, G.; Luyckx, L.; Vandenboom, T.; Van Mele, B. Int. J. Chem. Kinet. 1977, 9, 283.
(E)-CH2=CHCH=CH2 + (E)-CH2=CHCH=CH2 --> 4-vinylcyclohexene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.59 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 592,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_HNd_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (8.99e+08,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (22.06,"kcal/mol"),
        Tmin = (515,"K"),
        Tmax = (572,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 593,
    label = "diene_unsub_unsub_out;diene_in_2H;ene_HDe_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (8.99e+08,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (22.06,"kcal/mol"),
        Tmin = (515,"K"),
        Tmax = (572,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
(Z)-CH3CH=CHCHO + (E)-CH2=CHCH=CH2 --> 3-cyclohexene-1-carboxaldehyde,6-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 594,
    label = "diene_unsub_unsub_out;diene_in_HNd;ene_unsub_unsub",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.32e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (29.61,"kcal/mol"),
        Tmin = (1000,"K"),
        Tmax = (1180,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Simmie [199]""",
    longDesc = 
u"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 595,
    label = "diene_unsub_unsub_out;diene_in_NdH;ene_unsub_unsub",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cs,O} 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.32e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (29.61,"kcal/mol"),
        Tmin = (1000,"K"),
        Tmax = (1180,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Simmie [199]""",
    longDesc = 
u"""
[199] Simmie, J. M. Int. J. Chem. Kinet. 1978, 10, 227.
CH2=C(CH3)CH=CH2 + C2H4 --> 1-methyl-cyclohexane

Data derived from fitting to a complex mechanism. Excitation: thermal. Analysis: GC. Presure 2.50 atm
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 596,
    label = "diene_unsub_unsub_out;diene_in_HNd;ene_HDe_2H",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.7,"kcal/mol"),
        Tmin = (492,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 597,
    label = "diene_unsub_unsub_out;diene_in_NdH;ene_2H_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     {Cs,O} 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (18.7,"kcal/mol"),
        Tmin = (492,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Kistiakowsky et al [112]""",
    longDesc = 
u"""
[112] Kistiakowsky, G. B.; Lacher, J. R. J. Am. Chem. Soc. 1936, 58, 123.
CH2=CHCHO + CH2=C(CH3)CH=CH2 --> 3-cyclohexene-1-carboxaldehyde,4-methyl

Absolute value measured directly. Excitation: thermal. Pressure 0.64-0.78 atm
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 598,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_unsub_unsub",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (4.57e+09,"cm^3/(mol*s)","*|/",1.05),
        n = 0,
        alpha = 0,
        E0 = (26.03,"kcal/mol"),
        Tmin = (450,"K"),
        Tmax = (592,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [109]""",
    longDesc = 
u"""
[109] Huybrechts, G.; Rigaux, D.; Vankeerberghen, J.; Van Mele, B. Int. J. Chem. Kinet. 1980, 12, 253.
1,3-cyclohexadiene + C2H4 --> bicyclo[2.2.2]oct-2-ene

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.05-0.25 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 599,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (26.63,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 600,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.09e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (28.81,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 601,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7.08e+08,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (26.23,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + 1-C4H8 --> bicyclo[2.2.2]oct-2-ene,5-ETHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 602,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.17e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (28.62,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + 1-C4H8 --> bicyclo[2.2.2]oct-2-ene,5-ETHYL-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 603,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3.72e+08,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (26.63,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + (CH3)2CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-(1-METHYLETHYL)-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 604,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.95e+08,"cm^3/(mol*s)","*|/",1.1),
        n = 0,
        alpha = 0,
        E0 = (28.42,"kcal/mol"),
        Tmin = (486,"K"),
        Tmax = (600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + (CH3)2CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-(1-METHYLETHYL)-(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 605,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_2H",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+09,"cm^3/(mol*s)","*|/",1.12),
        n = 0,
        alpha = 0,
        E0 = (26.63,"kcal/mol"),
        Tmin = (488,"K"),
        Tmax = (606,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [108]""",
    longDesc = 
u"""
[108] Huybrechts, G.; Poppelsdorf, H.; Maesschalck, L.; Van Mele, B. Int. J. Chem. Kinet. 1984, 16, 93.
1,3-cyclohexadiene + CH3CH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-METHYL-(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.07-0.82 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 606,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+09,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (20.07,"kcal/mol"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 607,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (6.03e+08,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (20.87,"kcal/mol"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2beta, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 608,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.15e+10,"cm^3/(mol*s)","*|/",1.05),
        n = 0,
        alpha = 0,
        E0 = (26.83,"kcal/mol"),
        Tmin = (437,"K"),
        Tmax = (526,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [111]""",
    longDesc = 
u"""
[111] Huybrechts, G.;Hubin, Y.; Narmon, M.; Van Mele, B. Int. J. Chem. Kinet. 1982, 14, 259.
1,3-cyclohexadiene + (E)CH2=CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-ethenyl(1alpha, 4alpha, 5alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.15-0.64 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 609,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_2H_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3.8e+09,"cm^3/(mol*s)","*|/",1.05),
        n = 0,
        alpha = 0,
        E0 = (24.84,"kcal/mol"),
        Tmin = (437,"K"),
        Tmax = (526,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Huybrechts et al. [111]""",
    longDesc = 
u"""
[111] Huybrechts, G.;Hubin, Y.; Narmon, M.; Van Mele, B. Int. J. Chem. Kinet. 1982, 14, 259.
1,3-cyclohexadiene + (E)CH2=CHCH=CH2 --> bicyclo[2.2.2]oct-2-ene,5-ethenyl(1alpha, 4alpha, 5beta)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.15-0.64 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 610,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_2H",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.02e+09,"cm^3/(mol*s)","*|/",1.07),
        n = 0,
        alpha = 0,
        E0 = (20.07,"kcal/mol"),
        Tmin = (379,"K"),
        Tmax = (581,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Van Mele et al [110]""",
    longDesc = 
u"""
[110] Van Mele, B.; Tybaert, C.; Huybrechts, G.  Int. J. Chem. Kinet. 1987, 19, 1063.
1,3-cyclohexadiene + CH2=CHCHO --> bicyclo[2.2.2]oct-2-ene,2-carboxaldehyde(1alpha, 2alpha, 4alpha)

Absolute value measured directly using thermal excitation technique and GC. Pressure 0.06-0.27 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 611,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HNd_HDe",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.69,"kcal/mol"),
        Tmin = (352,"K"),
        Tmax = (423,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 612,
    label = "diene_monosubNd_monosubNd_out;diene_in_2H;ene_HDe_HNd",
    group1 = 
"""
1  *3 Cd 0 {2,D} {5,S} {6,S}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *6 Cd 0 {3,D} {7,S} {8,S}
5     H 0 {1,S}
6     {Cs,O} 0 {1,S}
7     {Cs,O} 0 {4,S}
8     H 0 {4,S}
""",
    group2 = 
"""
1  *4 Cd 0 {2,S} {3,S}
2  *5 Cd 0 {1,S} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group3 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.69,"kcal/mol"),
        Tmin = (352,"K"),
        Tmax = (423,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Benford et al [200]""",
    longDesc = 
u"""
[200] Benford, G. A.; Wassermann, A. J. Chem. Soc. 1939, 362. 
Cyclopentadiene + cyclopentadiene --> Tricyclo[5.2.1.02,6]deca-c,8-diene.

Absolute value measured directly using thermal excitation technique and mass spectrometry. Pressure 0.20-0.97 atm.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

