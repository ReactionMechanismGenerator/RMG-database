#!/usr/bin/env python
# encoding: utf-8

name = "API_Intra_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "R3;Y_rad_NDe;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (1.62e+10, 's^-1'),
        n = -0.305,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1, increase barrier and decreased A""",
)

entry(
    index = 2,
    label = "R4;Y_rad_NDe;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (7.76e+08, 's^-1'),
        n = 0.311,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 3,
    label = "R5;Y_rad_NDe;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 4,
    label = "R6;Y_rad_NDe;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 5,
    label = "R7;Y_rad_NDe;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 6,
    label = "R3;Y_rad_De;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (1.62e+10, 's^-1'),
        n = -0.305,
        alpha = 0,
        E0 = (32.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 7,
    label = "R4;Y_rad_De;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (7.76e+08, 's^-1'),
        n = 0.311,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 8,
    label = "R5;Y_rad_De;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 9,
    label = "R6;Y_rad_De;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 10,
    label = "R7;Y_rad_De;XH_Rrad_NDe",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 11,
    label = "R3;Y_rad_De;XH_Rrad_De",
    kinetics = ArrheniusEP(
        A = (5.4e+09, 's^-1'),
        n = -0.305,
        alpha = 0,
        E0 = (22.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 12,
    label = "R4;Y_rad_De;XH_Rrad_De",
    kinetics = ArrheniusEP(
        A = (2.59e+08, 's^-1'),
        n = 0.311,
        alpha = 0,
        E0 = (4.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 13,
    label = "R5;Y_rad_De;XH_Rrad_De",
    kinetics = ArrheniusEP(
        A = (1.07e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (4.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 14,
    label = "R6;Y_rad_De;XH_Rrad_De",
    kinetics = ArrheniusEP(
        A = (1.07e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (4.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

entry(
    index = 15,
    label = "R7;Y_rad_De;XH_Rrad_De",
    kinetics = ArrheniusEP(
        A = (1.07e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (4.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimate""",
    longDesc = 
u"""
Estimates for intra disproportionation involving resonance stabilized rads, I just added some DGAV*s for H abstractions 
Y_rad_De increases barrier with 12.5 kcal/mol, no effect on A
XH_Rrad_De decreases barrier with 6.25 kcal/mol, decreases A by factor 3
Resonanance corrections, 1 kcal/mol for C <-> Cd, 2 kcal/mol for Cd <-> Cd
""",
)

