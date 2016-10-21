#!/usr/bin/env python
# encoding: utf-8

name = "Narayanaswamy_aromatic_only"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "N-C4H5(60) + C2H3(29) <=> H2(6) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e-13, 'cm^3/(mol*s)'),
        n = 7.07,
        Ea = (-3.611, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "H(2) + C6H6(91) <=> H(2) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "C2H2(21) + N-C4H5(60) <=> H(2) + C6H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+15, 'cm^3/(mol*s)'),
        n = -0.89,
        Ea = (9.142, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "C2H2(21) + I-C4H5(61) <=> H(2) + C6H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+24, 'cm^3/(mol*s)'),
        n = -3.45,
        Ea = (20.337, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "C6H6(91) <=> A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+45, 's^-1'), n=-8.9, Ea=(97.003, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "C6H6(91) <=> H(2) + A1-(92)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.24e+68, 's^-1'), n=-14.65, Ea=(142.576, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C2H2(21) + N-C4H3(45) <=> A1-(92)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+70, 'cm^3/(mol*s)'),
        n = -17.77,
        Ea = (31.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "C2H2(21) + N-C4H5(60) <=> H(2) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+16, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (8.901, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "C2H2(21) + I-C4H5(61) <=> H(2) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e+23, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (24.959, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "A-C3H5(47) + C3H3(41) => H(2) + H(2) + C6H6(91)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.16e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23.853, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "C3H3(41) + C3H3(41) <=> C6H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.25e+46, 'cm^3/(mol*s)'),
        n = -10.1,
        Ea = (16.96, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "C3H3(41) + C3H3(41) <=> A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+45, 'cm^3/(mol*s)'),
        n = -9.57,
        Ea = (17.015, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = "C3H3(41) + C3H3(41) <=> H(2) + A1-(92)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.77e+37, 'cm^3/(mol*s)'),
        n = -7,
        Ea = (31.506, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "A1-(92) + C2H2(21) <=> A1C2H2(93)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 15,
    label = "A1-(92) + C2H3(29) <=> A1C2H3(94)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "A1(62) + C2H3(29) <=> H(2) + A1C2H3(94)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.87e+07, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (5.533, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 17,
    label = "A1-(92) + C2H4(30) <=> A1(62) + C2H3(29)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00945, 'cm^3/(mol*s)'),
        n = 4.47,
        Ea = (4.472, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 18,
    label = "A1C2H(95) <=> H(2) + A1C2H*(96)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148.086, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "H(2) + A1C2H(95) <=> H2(6) + A1C2H*(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.29e+08, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (17.579, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "OH(5) + A1C2H(95) <=> A1C2H*(96) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7800, 'cm^3/(mol*s)'), n=2.68, Ea=(0.734, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "A1C2H2(93) <=> C8H7(97)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.9e+10, 's^-1'), n=0.54, Ea=(27.567, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "A1C2H2(93) <=> H(2) + A1C2H(95)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38.673, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "H(2) + A1C2H2(93) <=> H2(6) + A1C2H(95)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10.631, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "OH(5) + A1C2H2(93) <=> A1C2H(95) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "A1C2H3(94) <=> H(2) + C8H7(97)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148.086, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "H(2) + A1C2H3(94) <=> H2(6) + C8H7(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.23e+06, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (16.917, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "OH(5) + A1C2H3(94) <=> C8H7(97) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(134, 'cm^3/(mol*s)'), n=3.33, Ea=(1.456, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "A1C2H3(94) <=> H(2) + A1C2H2(93)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+14, 's^-1'), n=0.34, Ea=(111.255, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "H(2) + A1C2H3(94) <=> H2(6) + A1C2H2(93)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63500, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (11.649, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "OH(5) + A1C2H3(94) <=> A1C2H2(93) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0655, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-0.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = "A1C2H*(96) + C2H2(21) <=> A2-(98)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13400, 'cm^3/(mol*s)'), n=2.5, Ea=(1.283, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "C8H7(97) + C2H2(21) <=> H(2) + A2(99)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3020, 'cm^3/(mol*s)'), n=2.55, Ea=(3.181, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "A1C2H2(93) + C2H2(21) <=> H(2) + A2(99)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4.438, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "A1C2H(95) + C2H3(29) <=> H(2) + A2(99)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 35,
    label = "A1C2H*(96) + C2H4(30) <=> H(2) + A2(99)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23.865, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 36,
    label = "A1-(92) + C4H4(49) <=> H(2) + A2(99)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1.434, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "A2(99) <=> H(2) + A2-(98)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "H(2) + A2(99) <=> H2(6) + A2-(98)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 39,
    label = "OH(5) + A2(99) <=> A2-(98) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4.374, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "A2(99) <=> H(2) + A2*(100)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "H(2) + A2(99) <=> H2(6) + A2*(100)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 42,
    label = "OH(5) + A2(99) <=> A2*(100) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4.374, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "A2-(98) + C2H2(21) <=> C12H9(101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1.931, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 44,
    label = "A2*(100) + C2H2(21) <=> C12H9(102)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 45,
    label = "A2-(98) + C2H3(29) <=> H(2) + C12H9(101)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "A2*(100) + C2H3(29) <=> H(2) + C12H9(102)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "A2(99) + C2H3(29) <=> H2(6) + C12H9(101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 48,
    label = "A2(99) + C2H3(29) <=> H2(6) + C12H9(102)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 49,
    label = "A2-(98) + C2H4(30) <=> H2(6) + C12H9(101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23.865, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 50,
    label = "A2*(100) + C2H4(30) <=> H2(6) + C12H9(102)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23.865, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 51,
    label = "C12H9(101) <=> H(2) + C12H8(103)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38.673, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 52,
    label = "H(2) + C12H9(101) <=> H2(6) + C12H8(103)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10.631, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 53,
    label = "OH(5) + C12H9(101) <=> C12H8(103) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "C12H9(102) <=> H(2) + C12H8(104)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38.673, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "H(2) + C12H9(102) <=> H2(6) + C12H8(104)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10.631, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 56,
    label = "OH(5) + C12H9(102) <=> C12H8(104) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "C12H8(103) <=> H(2) + C12H7(105)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "H(2) + C12H8(103) <=> H2(6) + C12H7(105)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (16.821, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 59,
    label = "OH(5) + C12H8(103) <=> H2O(7) + C12H7(105)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(67.2, 'cm^3/(mol*s)'), n=3.33, Ea=(1.456, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "C12H8(104) <=> H(2) + C12H7(106)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "H(2) + C12H8(104) <=> H2(6) + C12H7(106)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (16.821, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 62,
    label = "OH(5) + C12H8(104) <=> H2O(7) + C12H7(106)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(67.2, 'cm^3/(mol*s)'), n=3.33, Ea=(1.456, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "C12H9(101) <=> H(2) + A2R5(107)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+11, 's^-1'), n=0.23, Ea=(17.027, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "H(2) + C12H8(103) <=> H(2) + A2R5(107)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.52e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.36, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 65,
    label = "A2R5(107) <=> H(2) + A2R5-(108)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "H(2) + A2R5(107) <=> H2(6) + A2R5-(108)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 67,
    label = "OH(5) + A2R5(107) <=> H2O(7) + A2R5-(108)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4.374, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "C2H2(21) + A2R5-(108) <=> C14H9(109)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 69,
    label = "A2R5-(108) + C2H3(29) <=> H(2) + C14H9(109)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "A2R5(107) + C2H3(29) <=> H2(6) + C14H9(109)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 71,
    label = "A2R5-(108) + C2H4(30) <=> H2(6) + C14H9(109)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23.865, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 72,
    label = "C14H8(110) <=> H(2) + C14H7(111)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "H(2) + C14H8(110) <=> H2(6) + C14H7(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (16.821, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 74,
    label = "OH(5) + C14H8(110) <=> H2O(7) + C14H7(111)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(67.2, 'cm^3/(mol*s)'), n=3.33, Ea=(1.456, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "C14H9(109) <=> H(2) + C14H8(110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+10, 's^-1'), n=1.02, Ea=(38.673, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "H(2) + C14H9(109) <=> H2(6) + C14H8(110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (10.631, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 77,
    label = "OH(5) + C14H9(109) <=> H2O(7) + C14H8(110)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 78,
    label = "A1-(92) + A1(62) <=> H(2) + P2(112)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.55e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.168, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 79,
    label = "A1-(92) + A1-(92) <=> P2(112)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.112, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "P2(112) <=> H(2) + P2-(113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "H(2) + P2(112) <=> H2(6) + P2-(113)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.01e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 82,
    label = "OH(5) + P2(112) <=> H2O(7) + P2-(113)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(269, 'cm^3/(mol*s)'), n=3.33, Ea=(1.456, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "C2H2(21) + C12H7(105) <=> A3-(114)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13400, 'cm^3/(mol*s)'), n=2.5, Ea=(1.283, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 84,
    label = "C2H2(21) + C12H7(106) <=> A3-(114)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13400, 'cm^3/(mol*s)'), n=2.5, Ea=(1.283, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "C12H9(101) + C2H2(21) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4.438, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 86,
    label = "C12H9(102) + C2H2(21) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4.438, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 87,
    label = "C2H2(21) + P2-(113) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.29e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (3.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 88,
    label = "C12H7(105) + C2H3(29) <=> A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "C12H7(106) + C2H3(29) <=> A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "C12H8(103) + C2H3(29) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 91,
    label = "C12H8(104) + C2H3(29) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (15.758, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 92,
    label = "C12H7(105) + C2H4(30) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23.865, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 93,
    label = "C12H7(106) + C2H4(30) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+28, 'cm^3/(mol*s)'),
        n = -4.24,
        Ea = (23.865, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 94,
    label = "A2-(98) + C4H4(49) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1.434, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 95,
    label = "A2*(100) + C4H4(49) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1.434, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 96,
    label = "A1-(92) + A1C2H(95) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.18e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.168, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 97,
    label = "A1C2H*(96) + A1(62) <=> H(2) + A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.39e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.168, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 98,
    label = "A1-(92) + A1C2H*(96) <=> A3(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.112, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "A3(115) <=> H(2) + A3-(114)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "H(2) + A3(115) <=> H2(6) + A3-(114)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 101,
    label = "OH(5) + A3(115) <=> H2O(7) + A3-(114)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(134, 'cm^3/(mol*s)'), n=3.33, Ea=(1.456, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "A3(115) <=> H(2) + A3*(116)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.3e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "H(2) + A3(115) <=> H2(6) + A3*(116)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 104,
    label = "OH(5) + A3(115) <=> H2O(7) + A3*(116)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4.374, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "A3-(114) <=> C2H2(21) + A2R5-(108)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 's^-1'), n=1.08, Ea=(70.399, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "C2H2(21) + C14H7(111) <=> A3R5-(117)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13400, 'cm^3/(mol*s)'), n=2.5, Ea=(1.283, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "C2H2(21) + C14H9(109) <=> H(2) + A3R5(118)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (4.438, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 108,
    label = "C2H2(21) + A3*(116) <=> H(2) + A3R5(118)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1.931, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 109,
    label = "A3*(116) + C2H3(29) <=> H2(6) + A3R5(118)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "C4H4(49) + A2R5-(108) <=> H(2) + A3R5(118)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (1.434, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 111,
    label = "A3R5(118) <=> H(2) + A3R5-(117)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 112,
    label = "H(2) + A3R5(118) <=> H2(6) + A3R5-(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 113,
    label = "OH(5) + A3R5(118) <=> H2O(7) + A3R5-(117)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(963, 'cm^3/(mol*s)'), n=3.02, Ea=(4.374, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "C2H2(21) + A3-(114) <=> H(2) + A4(119)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1.931, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 115,
    label = "A4(119) <=> H(2) + A4-(120)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+60, 's^-1'), n=-12.48, Ea=(148.076, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "H(2) + A4(119) <=> H2(6) + A4-(120)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+08, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (17.096, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 117,
    label = "OH(5) + A4(119) <=> H2O(7) + A4-(120)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1930, 'cm^3/(mol*s)'), n=3.02, Ea=(4.374, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "C2H2(21) + A4-(120) <=> H(2) + A4R5(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1.931, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 119,
    label = "C2H2(21) + A3R5-(117) <=> H(2) + A4R5(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+06, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (1.931, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 120,
    label = "A2(99) + A1-(92) => H(2) + H2(6) + FLTN(122)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.37e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.168, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 121,
    label = "A2-(98) + A1(62) => H(2) + H2(6) + FLTN(122)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (9.55e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.168, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 122,
    label = "A2-(98) + A1-(92) => H2(6) + FLTN(122)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.39e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.112, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 123,
    label = "C5H6(123) <=> H(2) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+68, 's^-1'), n=-15.16, Ea=(116.372, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "H(2) + C5H6(123) <=> H2(6) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(2.259, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "H(2) + C5H6(123) => C2H2(21) + S-C3H5(44)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.3e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.345, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'H(2)+C5H6(123)=C2H2(21)+A-C3H5(47)                  3.300e+14 0.000     12.345',
    ),
    longDesc = 
u"""
H(2)+C5H6(123)=C2H2(21)+A-C3H5(47)                  3.300e+14 0.000     12.345
""",
)

entry(
    index = 126,
    label = "O(4) + C5H6(123) <=> OH(5) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47700, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (1.107, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 127,
    label = "OH(5) + C5H6(123) <=> H2O(7) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.08e+06, 'cm^3/(mol*s)'), n=2, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "O2(3) + C5H6(123) <=> HO2(9) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(37.151, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "HO2(9) + C5H6(123) <=> H2O2(10) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (12.899, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 130,
    label = "CH3(16) + C5H6(123) <=> CH4(1) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.18, 'cm^3/(mol*s)'), n=4, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "C5H6(123) + C2H3(29) <=> C5H5(124) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "N-C4H5(60) + C5H6(123) <=> C4H6(59) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "O(4) + C5H6(123) <=> H(2) + C5H5O(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.66e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (1.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 134,
    label = "O(4) + C5H6(123) => CO(11) + C2H2(21) + C2H4(30)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.89e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (0.887, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 135,
    label = "OH(5) + C5H6(123) => HCO(12) + C4H6(59)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.75e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 136,
    label = "OH(5) + C5H6(123) => HCO(12) + C2H2(21) + C2H4(30)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.75e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 137,
    label = "C2H2(21) + C3H3(41) <=> C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+55, 'cm^3/(mol*s)'),
        n = -12.5,
        Ea = (42.065, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 138,
    label = "CH3(16) + C5H5(124) => H(2) + H(2) + C6H6(91)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.91e+31, 'cm^3/(mol*s)'),
        n = -4.85,
        Ea = (24.773, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C5H5(124)+C5H5(124)=>H(2)+H(2)+A2(99)               6.390e+29 -4.030    35.206',
    ),
    longDesc = 
u"""
C5H5(124)+C5H5(124)=>H(2)+H(2)+A2(99)               6.390e+29 -4.030    35.206
""",
)

entry(
    index = 139,
    label = "O(4) + C5H5(124) <=> H(2) + C5H4O(126)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 140,
    label = "O2(3) + C5H5(124) <=> OH(5) + C5H4O(126)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17.667, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 141,
    label = "HO2(9) + C5H5(124) <=> OH(5) + C5H5O(127)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "OH(5) + C5H5(124) => H(2) + C5H5O(127)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "C5H5O(127) <=> H(2) + C5H4O(126)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 's^-1'), n=0, Ea=(30, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "C5H5O(125) => CO(11) + N-C4H5(60)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 's^-1'), n=0, Ea=(35.999, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "H(2) + C5H5O(127) => H2(6) + C5H4O(126)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "O(4) + C5H5O(127) => OH(5) + C5H4O(126)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "OH(5) + C5H5O(127) => H2O(7) + C5H4O(126)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "O2(3) + C5H5O(127) => HO2(9) + C5H4O(126)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.43e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 149,
    label = "H(2) + C5H5O(125) => H2(6) + C5H4O(126)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 150,
    label = "O2(3) + C5H5O(125) => HO2(9) + C5H4O(126)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.28e+07, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (-2.034, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 151,
    label = "C5H4O(126) => CO(11) + C2H2(21) + C2H2(21)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.37e+44, 's^-1'), n=-8, Ea=(108.676, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "H(2) + C5H4O(126) <=> C5H5O(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.74e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (1.355, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 153,
    label = "O(4) + C5H4O(126) <=> CO2(8) + C4H4(49)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "A1-(92) + C3H3(41) <=> C9H8(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C5H6(123)+C5H5(124)=>CH3(16)+C9H8(128)              7.860e-01 3.070     5.729',
    ),
    longDesc = 
u"""
C5H6(123)+C5H5(124)=>CH3(16)+C9H8(128)              7.860e-01 3.070     5.729
""",
)

entry(
    index = 155,
    label = "C9H8(128) <=> H(2) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+68, 's^-1'), n=-15.16, Ea=(116.372, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "H(2) + C9H8(128) <=> H2(6) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(2.259, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 157,
    label = "C2H2(21) + A1CH2(130) <=> H(2) + C9H8(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31600, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (11.061, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 158,
    label = "O(4) + C9H8(128) <=> OH(5) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47700, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (1.107, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 159,
    label = "OH(5) + C9H8(128) <=> H2O(7) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.08e+06, 'cm^3/(mol*s)'), n=2, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "O2(3) + C9H8(128) <=> HO2(9) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(37.151, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "HO2(9) + C9H8(128) <=> H2O2(10) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (12.899, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 162,
    label = "CH3(16) + C9H8(128) <=> CH4(1) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.18, 'cm^3/(mol*s)'), n=4, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "O(4) + C9H8(128) => H(2) + H(2) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.83e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (1.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 164,
    label = "OH(5) + C9H8(128) => HCO(12) + C6H4(132) + C2H4(30)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 165,
    label = "C5H5(124) + C9H7(129) => H(2) + H(2) + A3(115)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.56e+29, 'cm^3/(mol*s)'),
        n = -4.03,
        Ea = (35.206, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 166,
    label = "CH3(16) + C9H7(129) => H(2) + H(2) + A2(99)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.96e+31, 'cm^3/(mol*s)'),
        n = -4.85,
        Ea = (24.773, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 167,
    label = "O(4) + C9H7(129) <=> H(2) + C9H6O(131)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 168,
    label = "O2(3) + C9H7(129) <=> OH(5) + C9H6O(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17.667, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 169,
    label = "HO2(9) + C9H7(129) => H2O(7) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.24e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 170,
    label = "OH(5) + C9H7(129) => H(2) + H(2) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.08e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "C9H7(129) + C3H3(41) => H(2) + H(2) + A2R5(107)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23.853, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 172,
    label = "C9H6O(131) => CO(11) + C2H2(21) + C6H4(132)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.37e+44, 's^-1'), n=-8, Ea=(108.676, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "H(2) + C9H6O(131) => C8H7(97) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.37e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (1.355, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 174,
    label = "H(2) + A1CH3(133) <=> CH3(16) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 175,
    label = "A1CH3(133) <=> H(2) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0.68, Ea=(89.207, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "A1CH3(133) <=> A1-(92) + CH3(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.35e+22, 's^-1'), n=-1.73, Ea=(104.209, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "H(2) + A1CH2(130) <=> A1-(92) + CH3(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+67, 'cm^3/(mol*s)'),
        n = -14.15,
        Ea = (68.329, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 178,
    label = "O2(3) + A1CH3(133) <=> HO2(9) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46.044, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'A1CH2(130)=C2H2(21)+C5H5(124)                       8.200e+14 0.000     80.676',
    ),
    longDesc = 
u"""
A1CH2(130)=C2H2(21)+C5H5(124)                       8.200e+14 0.000     80.676
""",
)

entry(
    index = 179,
    label = "H(2) + A1CH3(133) <=> H2(6) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.47, 'cm^3/(mol*s)'), n=3.98, Ea=(3.384, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 180,
    label = "OH(5) + A1CH3(133) <=> H2O(7) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-0.602, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 181,
    label = "OH(5) + A1CH3(133) <=> CH3(16) + A1OH(134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3.222, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 182,
    label = "OH(5) + A1CH3(133) <=> H(2) + C7H8O(135)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.4, 'cm^3/(mol*s)'), n=3.37, Ea=(4.72, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 183,
    label = "O(4) + A1CH3(133) <=> OH(5) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18, 'cm^3/(mol*s)'), n=4.09, Ea=(2.545, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "O(4) + A1CH3(133) <=> C7H8O(135)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+12, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (4.402, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 185,
    label = "O(4) + A1CH3(133) <=> H(2) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (3.975, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 186,
    label = "CH3(16) + A1CH3(133) <=> CH4(1) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22.256, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 187,
    label = "HO2(9) + A1CH3(133) <=> H2O2(10) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14.685, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 188,
    label = "A1-(92) + A1CH3(133) <=> A1(62) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.95, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 189,
    label = "O(4) + A1CH2(130) <=> C7H7O(137)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.28e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "OH(5) + A1CH2(130) <=> C7H8O(138)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "HO2(9) + A1CH2(130) <=> OH(5) + C7H7O(137)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.19e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (-2.249, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 192,
    label = "A1CH2(130) + C3H3(41) => H(2) + H(2) + A2(99)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23.853, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 193,
    label = "O2(3) + A1CH2(130) <=> OH(5) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.76e+15, 'cm^3/(mol*s)'),
        n = -1.55,
        Ea = (11.322, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 194,
    label = "O2(3) + A1CH2(130) <=> CH2O(17) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.26e+37, 'cm^3/(mol*s)'),
        n = -8.86,
        Ea = (16.582, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 195,
    label = "H(2) + C7H7O(137) <=> C7H8O(138)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.43e+12, 'cm^3/(mol*s)'),
            n = 0.52,
            Ea = (0.05, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14.08, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 196,
    label = "H(2) + C7H8O(138) <=> H2(6) + C7H7O(137)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4.871, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 197,
    label = "O(4) + C7H8O(138) <=> OH(5) + C7H7O(137)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(130000, 'cm^3/(mol*s)'), n=2.5, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "OH(5) + C7H8O(138) <=> H2O(7) + C7H7O(137)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(1.501, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "CH3(16) + C7H8O(138) <=> CH4(1) + C7H7O(137)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.5, Ea=(9.94, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "A1-(92) + CH2O(17) <=> HCO(12) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (85500, 'cm^3/(mol*s)'),
        n = 2.19,
        Ea = (0.038, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 201,
    label = "C7H7O(137) <=> H(2) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.26e+28, 's^-1'), n=-5.08, Ea=(22.249, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "C7H7O(137) <=> A1-(92) + CH2O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.21e+33, 's^-1'), n=-6.21, Ea=(36.85, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "C7H7O(137) <=> HCO(12) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.37e+32, 's^-1'), n=-6.1, Ea=(28.81, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 204,
    label = "H(2) + C7H7O(137) <=> H2(6) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "O(4) + C7H7O(137) <=> OH(5) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "OH(5) + C7H7O(137) <=> H2O(7) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "O2(3) + C7H7O(137) <=> HO2(9) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 208,
    label = "A1CHO(139) => H(2) + A1-(92) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+16, 's^-1'), n=0, Ea=(81.74, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "H(2) + A1CHO(139) => H2(6) + A1-(92) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.404, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 210,
    label = "O(4) + A1CHO(139) => OH(5) + A1-(92) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.809, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 211,
    label = "OH(5) + A1CHO(139) => A1-(92) + H2O(7) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1.573, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 212,
    label = "O2(3) + A1CHO(139) => A1-(92) + HO2(9) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37.555, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 213,
    label = "HO2(9) + A1CHO(139) => A1-(92) + H2O2(10) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10.203, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 214,
    label = "CH3(16) + A1CHO(139) => CH4(1) + A1-(92) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 215,
    label = "C7H8O(135) <=> H(2) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+71, 's^-1'), n=-15.92, Ea=(124.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 216,
    label = "H(2) + C7H8O(135) <=> H2(6) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.397, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 217,
    label = "O(4) + C7H8O(135) <=> OH(5) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.352, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 218,
    label = "OH(5) + C7H8O(135) <=> H2O(7) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.95e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.312, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 219,
    label = "C7H7O(136) => H(2) + C6H6(91) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.9e+10, 's^-1'), n=0, Ea=(36.425, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 220,
    label = "A1CH3(133) <=> H(2) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.39e+60, 's^-1'), n=-12.48, Ea=(148.086, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 221,
    label = "H(2) + A1CH3(133) <=> H2(6) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.91e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 222,
    label = "O(4) + A1CH3(133) <=> OH(5) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.699, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 223,
    label = "OH(5) + A1CH3(133) <=> H2O(7) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13600, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (0.619, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 224,
    label = "CH3(16) + A1CH3(133) <=> CH4(1) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0179, 'cm^3/(mol*s)'),
        n = 4.46,
        Ea = (13.638, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 225,
    label = "O(4) + C7H7(141) <=> C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "OH(5) + C7H7(141) <=> H(2) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "HO2(9) + C7H7(141) <=> OH(5) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "O2(3) + C7H7(141) <=> O(4) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 229,
    label = "O2(3) + C7H7(141) => H(2) + C6H6(91) + CO2(8)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.55e+13, 'cm^3/(mol*s)'),
        n = -0.44,
        Ea = (-1.649, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 230,
    label = "H(2) + C8H9(142) <=> C8H10(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "CH3(16) + A1CH2(130) <=> C8H10(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "A1-(92) + C2H5(31) <=> C8H10(143)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "H(2) + C8H10(143) <=> A1(62) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 234,
    label = "OH(5) + C8H10(143) <=> A1OH(134) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3.222, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 235,
    label = "H(2) + C8H10(143) <=> H2(6) + C8H9(142)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0483, 'cm^3/(mol*s)'),
        n = 4.71,
        Ea = (6.212, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 236,
    label = "O(4) + C8H10(143) <=> OH(5) + C8H9(142)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.96, 'cm^3/(mol*s)'), n=4.09, Ea=(2.545, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "OH(5) + C8H10(143) <=> H2O(7) + C8H9(142)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.47e+06, 'cm^3/(mol*s)'),
        n = 2.01,
        Ea = (0.366, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 238,
    label = "HO2(9) + C8H10(143) <=> H2O2(10) + C8H9(142)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8030, 'cm^3/(mol*s)'), n=2.6, Ea=(13.91, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "CH3(16) + C8H10(143) <=> CH4(1) + C8H9(142)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.753, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7.153, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 240,
    label = "C8H9(142) <=> A1-(92) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+11, 's^-1'), n=0.78, Ea=(38.705, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 241,
    label = "C8H9(142) <=> H(2) + A1C2H3(94)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.79e+06, 's^-1'), n=2.08, Ea=(32.106, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 242,
    label = "H(2) + C8H9(142) <=> H2(6) + A1C2H3(94)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "OH(5) + C8H9(142) <=> A1C2H3(94) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 244,
    label = "CH3(16) + C8H9(142) <=> CH4(1) + A1C2H3(94)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.77, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 245,
    label = "O2(3) + C8H9(142) <=> A1C2H3(94) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+16, 'cm^3/(mol*s)'),
        n = -1.63,
        Ea = (3.418, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 246,
    label = "O(4) + C8H9(142) <=> CH2O(17) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-0.394, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 247,
    label = "O(4) + C8H9(142) <=> CH3(16) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.17e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-0.394, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 248,
    label = "HO2(9) + C8H9(142) => OH(5) + CH2O(17) + A1CH2(130)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-0.999, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 249,
    label = "O2(3) + C8H9(142) <=> S(144)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4.82e+36, 'cm^3/(mol*s)'),
                n = -8.23,
                Ea = (5.167, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.82e+36, 'cm^3/(mol*s)'),
                n = -8.23,
                Ea = (5.167, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 250,
    label = "O2(3) + C8H9(142) => OH(5) + HCO(12) + A1CH2(130)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (38800, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (-0.578, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 251,
    label = "S(144) <=> O2(3) + C8H9(142)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.21e+45, 's^-1'), n=-10.15, Ea=(40.815, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.21e+45, 's^-1'), n=-10.15, Ea=(40.815, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 252,
    label = "S(144) => A1C2H3(94) + HO2(9)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.45e+25, 's^-1'), n=-4.48, Ea=(32.608, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "S(144) => OH(5) + HCO(12) + A1CH2(130)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+13, 's^-1'), n=-1.12, Ea=(27.015, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "S(144) => S(145)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(0.0545, 's^-1'), n=3.57, Ea=(16.097, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "O2(3) + S(145) => OH(5) + S(146)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 256,
    label = "A1C2H3(94) => A1(62) + H2C2(35)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.4e+14, 's^-1'), n=0, Ea=(78.131, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "O(4) + A1C2H3(94) <=> HCO(12) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+07, 'cm^3/(mol*s)'),
        n = 1.66,
        Ea = (0.657, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 258,
    label = "A1C2H3(94) + CH3(16) <=> CH4(1) + A1C2H2(93)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(114000, 'cm^3/(mol*s)'), n=2, Ea=(9.199, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 259,
    label = "OH(5) + A1C2H3(94) <=> CH3(16) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 260,
    label = "OH(5) + A1C2H3(94) <=> CH2O(17) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.88e+36, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (7.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 261,
    label = "OH(5) + A1C2H3(94) <=> A1OH(134) + C2H3(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3.222, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 262,
    label = "O(4) + A1C2H3(94) <=> OH(5) + C8H7(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.699, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 263,
    label = "O(4) + A1C2H2(93) <=> CO(11) + A1CH2(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+13, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (-0.428, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 264,
    label = "O2(3) + A1C2H2(93) <=> A1C2H(95) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-0.385, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 265,
    label = "O2(3) + A1C2H2(93) => O(4) + CO(11) + A1CH2(130)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.03e+11, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (0.012, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 266,
    label = "O2(3) + A1C2H2(93) <=> HCO(12) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 267,
    label = "OH(5) + A1C2H(95) <=> HCCO(18) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 268,
    label = "C8H10(147) <=> H(2) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+18, 's^-1'), n=-0.6, Ea=(94.787, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 269,
    label = "C8H10(147) <=> CH3(16) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.32e+29, 's^-1'), n=-3.58, Ea=(110.165, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 270,
    label = "H(2) + C8H10(147) <=> H2(6) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12.9, 'cm^3/(mol*s)'), n=3.98, Ea=(3.384, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 271,
    label = "O(4) + C8H10(147) <=> OH(5) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.36, 'cm^3/(mol*s)'), n=4.09, Ea=(2.545, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 272,
    label = "OH(5) + C8H10(147) <=> H2O(7) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (354000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-0.602, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 273,
    label = "O2(3) + C8H10(147) <=> HO2(9) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.36e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46.044, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 274,
    label = "HO2(9) + C8H10(147) <=> H2O2(10) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (187000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14.685, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 275,
    label = "CH3(16) + C8H10(147) <=> CH4(1) + C8H9(148)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.44e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22.256, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 276,
    label = "H(2) + C8H10(147) <=> CH3(16) + A1CH3(133)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 277,
    label = "OH(5) + C8H10(147) <=> CH3(16) + C7H8O(135)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1570, 'cm^3/(mol*s)'), n=2.88, Ea=(3.222, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 278,
    label = "C8H9(148) => H(2) + C2H2(21) + A1(62)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.2e+14, 's^-1'), n=0, Ea=(80.676, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 279,
    label = "H(2) + C8H9(148) <=> CH3(16) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+67, 'cm^3/(mol*s)'),
        n = -14.15,
        Ea = (68.329, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 280,
    label = "O(4) + C8H9(148) <=> H(2) + C8H8O(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.37e+18, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1.592, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 281,
    label = "O(4) + C8H9(148) <=> CH2O(17) + C7H7(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.99e+23, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (16.193, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 282,
    label = "O(4) + C8H9(148) <=> HCO(12) + A1CH3(133)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+22, 'cm^3/(mol*s)'),
        n = -2.36,
        Ea = (8.152, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 283,
    label = "OH(5) + C8H9(148) => H2(6) + C8H8O(149)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 284,
    label = "O2(3) + C8H9(148) <=> OH(5) + C8H8O(149)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(138, 'cm^3/(mol*s)'), n=2.42, Ea=(7.44, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 285,
    label = "O2(3) + C8H9(148) <=> CH2O(17) + C7H7O(136)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6570, 'cm^3/(mol*s)'), n=1.87, Ea=(5.002, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "HO2(9) + C8H9(148) => H(2) + OH(5) + C8H8O(149)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.28e+13, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (-0.657, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 287,
    label = "HO2(9) + C8H9(148) => OH(5) + CH2O(17) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.13e+18, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (13.944, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 288,
    label = "HO2(9) + C8H9(148) => OH(5) + HCO(12) + A1CH3(133)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.03e+17, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (5.903, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 289,
    label = "C8H9(148) + C3H3(41) => H(2) + H(2) + A2CH3(150)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23.853, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 290,
    label = "C8H8O(149) <=> H(2) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+18, 's^-1'), n=-0.6, Ea=(94.787, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 291,
    label = "C8H8O(149) => A1-(92) + CO(11) + CH3(16)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.16e+29, 's^-1'), n=-3.58, Ea=(110.165, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 292,
    label = "C8H8O(149) => H(2) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+16, 's^-1'), n=0, Ea=(81.74, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 293,
    label = "H(2) + C8H8O(149) <=> H2(6) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.47, 'cm^3/(mol*s)'), n=3.98, Ea=(3.384, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 294,
    label = "O(4) + C8H8O(149) <=> OH(5) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18, 'cm^3/(mol*s)'), n=4.09, Ea=(2.545, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 295,
    label = "OH(5) + C8H8O(149) <=> H2O(7) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-0.602, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 296,
    label = "O2(3) + C8H8O(149) <=> HO2(9) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46.044, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 297,
    label = "HO2(9) + C8H8O(149) <=> H2O2(10) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14.685, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 298,
    label = "CH3(16) + C8H8O(149) <=> CH4(1) + C8H7O(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22.256, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 299,
    label = "H(2) + C8H8O(149) => H2(6) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.404, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 300,
    label = "O(4) + C8H8O(149) => OH(5) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.809, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 301,
    label = "OH(5) + C8H8O(149) => H2O(7) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1.573, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 302,
    label = "O2(3) + C8H8O(149) => HO2(9) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37.555, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 303,
    label = "HO2(9) + C8H8O(149) => H2O2(10) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10.203, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 304,
    label = "CH3(16) + C8H8O(149) => CH4(1) + CO(11) + C7H7(141)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 305,
    label = "H(2) + C8H8O(149) <=> HCO(12) + A1CH3(133)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 306,
    label = "H(2) + C8H8O(149) <=> CH3(16) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 307,
    label = "OH(5) + C8H8O(149) <=> HCO(12) + C7H8O(135)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3.222, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 308,
    label = "O(4) + C8H7O(151) <=> H(2) + S(152)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.37e+18, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1.592, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 309,
    label = "O(4) + C8H7O(151) => A1-(92) + CO(11) + CH2O(17)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.99e+23, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (16.193, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 310,
    label = "O(4) + C8H7O(151) <=> HCO(12) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+22, 'cm^3/(mol*s)'),
        n = -2.36,
        Ea = (8.152, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 311,
    label = "OH(5) + C8H7O(151) => H2(6) + S(152)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 312,
    label = "O2(3) + C8H7O(151) <=> OH(5) + S(152)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(138, 'cm^3/(mol*s)'), n=2.42, Ea=(7.643, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 313,
    label = "HO2(9) + C8H7O(151) => H(2) + OH(5) + S(152)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.19e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (-2.249, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 314,
    label = "H(2) + S(152) => H(2) + CO(11) + A1CHO(139)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.18e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.404, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 315,
    label = "O(4) + S(152) => O(4) + CO(11) + A1CHO(139)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.17e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.809, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 316,
    label = "OH(5) + S(152) => OH(5) + CO(11) + A1CHO(139)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.78e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1.573, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 317,
    label = "O2(3) + S(152) => O2(3) + CO(11) + A1CHO(139)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37.555, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 318,
    label = "HO2(9) + S(152) => HO2(9) + CO(11) + A1CHO(139)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (81800, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10.203, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 319,
    label = "CH3(16) + S(152) => CO(11) + CH3(16) + A1CHO(139)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.98e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 320,
    label = "H(2) + S(152) <=> HCO(12) + A1CHO(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 321,
    label = "H(2) + A2CH3(150) <=> A2(99) + CH3(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (4.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 322,
    label = "OH(5) + A2CH3(150) <=> CH3(16) + A2OH(153)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(783, 'cm^3/(mol*s)'), n=2.88, Ea=(3.222, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 323,
    label = "A2CH3(150) <=> H(2) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+18, 's^-1'), n=-0.6, Ea=(94.787, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
    label = "A2CH3(150) <=> A2-(98) + CH3(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+34, 's^-1'), n=-5.02, Ea=(114.252, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 325,
    label = "H(2) + A2CH2(154) <=> A2-(98) + CH3(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+67, 'cm^3/(mol*s)'),
        n = -14.15,
        Ea = (68.329, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 326,
    label = "A2CH2(154) <=> C2H2(21) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.2e+14, 's^-1'), n=0, Ea=(80.676, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 327,
    label = "H(2) + A2CH3(150) <=> H2(6) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.47, 'cm^3/(mol*s)'), n=3.98, Ea=(3.384, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 328,
    label = "O(4) + A2CH3(150) <=> OH(5) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18, 'cm^3/(mol*s)'), n=4.09, Ea=(2.545, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 329,
    label = "OH(5) + A2CH3(150) <=> H2O(7) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177000, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (-0.602, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 330,
    label = "O2(3) + A2CH3(150) <=> HO2(9) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+07, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (46.044, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 331,
    label = "CH3(16) + A2CH3(150) <=> CH4(1) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22.256, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 332,
    label = "HO2(9) + A2CH3(150) <=> H2O2(10) + A2CH2(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93300, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (14.685, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 333,
    label = "O(4) + A2CH3(150) => CO(11) + CH3(16) + C9H7(129)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.47e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.532, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 334,
    label = "O(4) + A2CH2(154) <=> S(155)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.28e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 335,
    label = "OH(5) + A2CH2(154) => S(155) + H(2)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 336,
    label = "HO2(9) + A2CH2(154) <=> S(155) + OH(5)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.19e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (-2.249, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 337,
    label = "A2CH2(154) + C3H3(41) => H(2) + H(2) + A3(115)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.32e+39, 'cm^3/(mol*s)'),
        n = -7.74,
        Ea = (23.853, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 338,
    label = "O2(3) + A2CH2(154) <=> A2CHO(156) + OH(5)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.76e+15, 'cm^3/(mol*s)'),
        n = -1.55,
        Ea = (11.322, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 339,
    label = "O2(3) + A2CH2(154) <=> A2O(157) + CH2O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+09, 'cm^3/(mol*s)'),
        n = 0.37,
        Ea = (16.91, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 340,
    label = "S(155) <=> A2CHO(156) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.26e+28, 's^-1'), n=-5.08, Ea=(22.249, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
    label = "S(155) <=> A2-(98) + CH2O(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.21e+33, 's^-1'), n=-6.21, Ea=(36.85, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 342,
    label = "S(155) + H(2) <=> A2CHO(156) + H2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "S(155) + O(4) <=> A2CHO(156) + OH(5)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.67e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 344,
    label = "S(155) + OH(5) <=> A2CHO(156) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 345,
    label = "S(155) + O2(3) <=> A2CHO(156) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e-13, 'cm^3/(mol*s)'),
        n = 7.6,
        Ea = (-3.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 346,
    label = "A2CHO(156) => H(2) + A2-(98) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.1e+16, 's^-1'), n=0, Ea=(81.74, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "A2CHO(156) + H(2) => H2(6) + A2-(98) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.09e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.404, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 348,
    label = "A2CHO(156) + O(4) => OH(5) + A2-(98) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.84e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.809, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 349,
    label = "A2CHO(156) + OH(5) => A2-(98) + H2O(7) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.89e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1.573, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 350,
    label = "A2CHO(156) + O2(3) => A2-(98) + HO2(9) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37.555, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 351,
    label = "A2CHO(156) + HO2(9) => A2-(98) + H2O2(10) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (40900, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10.203, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 352,
    label = "A2CHO(156) + CH3(16) => CH4(1) + A2-(98) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.49e-08, 'cm^3/(mol*s)'),
        n = 6.21,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 353,
    label = "A1(62) <=> H(2) + A1-(92)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+61, 's^-1'), n=-12.48, Ea=(148.086, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 354,
    label = "A1-(92) <=> H(2) + C6H4(132)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+12, 's^-1'), n=0.62, Ea=(77.302, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1e+84, 'cm^3/(mol*s)'),
            n = -18.87,
            Ea = (90.1, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.902,
        T3 = (696, 'K'),
        T1 = (358, 'K'),
        T2 = (3860, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.6, 'CC': 3, 'O': 12, '[H][H]': 2, '[Ar]': 0.7},
    ),
)

entry(
    index = 355,
    label = "C2H2(21) + C4H2(52) <=> C6H4(132)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+78, 'cm^3/(mol*s)'),
        n = -19.31,
        Ea = (67.921, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 356,
    label = "H(2) + A1(62) <=> H2(6) + A1-(92)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (16.353, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 357,
    label = "OH(5) + A1(62) <=> A1-(92) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23400, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (0.734, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 358,
    label = "OH(5) + A1(62) <=> H(2) + A1OH(134)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(132, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 359,
    label = "O2(3) + A1(62) <=> A1-(92) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (64.293, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "O(4) + A1(62) <=> H(2) + A1O(140)",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.74e+08, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (3.09, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.99e+07, 'cm^3/(mol*s)'),
                n = 1.8,
                Ea = (3.975, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 361,
    label = "O(4) + A1(62) <=> A1OH(134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.03e+12, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (4.402, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 362,
    label = "O(4) + A1(62) <=> CO(11) + C5H6(123)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+16, 'cm^3/(mol*s)'),
        n = -0.77,
        Ea = (15.292, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 363,
    label = "O(4) + A1(62) <=> OH(5) + A1-(92)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(14.699, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 364,
    label = "O2(3) + A1-(92) <=> O(4) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 365,
    label = "O2(3) + A1-(92) <=> S(158) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8.982, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 366,
    label = "O(4) + A1-(92) <=> A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "OH(5) + A1-(92) <=> H(2) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 368,
    label = "A1-(92) + HO2(9) <=> OH(5) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 369,
    label = "CH4(1) + A1-(92) <=> CH3(16) + A1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00389, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (5.258, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 370,
    label = "A1OH(134) <=> CO(11) + C5H6(123)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.59e+15, 's^-1'), n=-0.61, Ea=(74.118, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 371,
    label = "A1OH(134) <=> H(2) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+71, 's^-1'), n=-15.92, Ea=(124.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 372,
    label = "H(2) + A1OH(134) <=> H2(6) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(68.3, 'cm^3/(mol*s)'), n=3.4, Ea=(7.232, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "OH(5) + A1OH(134) <=> H2O(7) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17.3, 'cm^3/(mol*s)'), n=3.4, Ea=(-1.142, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 374,
    label = "CH3(16) + A1OH(134) <=> CH4(1) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00037, 'cm^3/(mol*s)'),
        n = 4.7,
        Ea = (4.828, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 375,
    label = "O2(3) + A1OH(134) <=> HO2(9) + A1O(140)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.32e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41.401, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 376,
    label = "A1O(140) <=> CO(11) + C5H5(124)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+10, 's^-1'), n=0, Ea=(36.425, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 377,
    label = "O(4) + A1O(140) <=> S(158) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.34e+13, 'cm^3/(mol*s)'),
        n = 0.03,
        Ea = (-0.394, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 378,
    label = "O2(3) + A1O(140) <=> S(158) + OH(5)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.51e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17.667, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 379,
    label = "S(158) <=> CO(11) + C5H4O(126)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.4e+11, 's^-1'), n=0, Ea=(59.001, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "S(158) + H(2) <=> CO(11) + C5H5O(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+09, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 381,
    label = "O(4) + A2(99) <=> A2O(157) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.83e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.529, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 382,
    label = "O(4) + A2(99) <=> A2OH(153)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.83e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.529, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 383,
    label = "OH(5) + A2(99) <=> H(2) + A2OH(153)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 384,
    label = "O2(3) + A2-(98) <=> A2O(157) + O(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 385,
    label = "O2(3) + A2*(100) <=> A2O(157) + O(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 386,
    label = "O2(3) + A2-(98) => H(2) + CO(11) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8.982, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 387,
    label = "O2(3) + A2*(100) => H(2) + CO(11) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(8.982, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 388,
    label = "O(4) + A2-(98) <=> A2O(157)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 389,
    label = "O(4) + A2*(100) <=> A2O(157)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "OH(5) + A2-(98) <=> A2O(157) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 391,
    label = "OH(5) + A2*(100) <=> A2O(157) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 392,
    label = "A2OH(153) <=> CO(11) + C9H8(128)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.62e+15, 's^-1'), n=-0.61, Ea=(74.118, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "A2OH(153) <=> A2O(157) + H(2)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+71, 's^-1'), n=-15.92, Ea=(124.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 394,
    label = "H(2) + A2OH(153) <=> A2O(157) + H2(6)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(68.3, 'cm^3/(mol*s)'), n=3.4, Ea=(7.232, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 395,
    label = "OH(5) + A2OH(153) <=> A2O(157) + H2O(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17.3, 'cm^3/(mol*s)'), n=3.4, Ea=(-1.142, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "CH3(16) + A2OH(153) <=> CH4(1) + A2O(157)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00037, 'cm^3/(mol*s)'),
        n = 4.7,
        Ea = (4.828, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 397,
    label = "A2O(157) <=> CO(11) + C9H7(129)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+10, 's^-1'), n=0, Ea=(36.425, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 398,
    label = "A2O(157) + O(4) => H(2) + CO(11) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.68e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "A2O(157) + O2(3) => OH(5) + CO(11) + C9H6O(131)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.51e+07, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (17.667, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 400,
    label = "O2(3) + A3-(114) => C12H9(102) + CO(11) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 401,
    label = "O2(3) + A3*(116) => C12H9(101) + CO(11) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 402,
    label = "O2(3) + A4-(120) => CO(11) + CO(11) + A3-(114)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 403,
    label = "O2(3) + A2R5-(108) => A2-(98) + CO(11) + CO(11)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 404,
    label = "O2(3) + A3R5-(117) => CO(11) + CO(11) + A3-(114)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (8.57e+20, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (7.189, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 405,
    label = "OH(5) + A3(115) => C12H8(103) + CO(11) + CH3(16)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(110, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 406,
    label = "OH(5) + A3(115) => C12H8(104) + CO(11) + CH3(16)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(110, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 407,
    label = "OH(5) + A4(119) => HCCO(18) + A3(115)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 408,
    label = "OH(5) + A2R5(107) => A2(99) + HCCO(18)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(176, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "OH(5) + A3R5(118) => HCCO(18) + A3(115)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "OH(5) + A4R5(121) => HCCO(18) + A4(119)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "OH(5) + FLTN(122) => HCCO(18) + A3(115)",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.25, Ea=(5.59, 'kcal/mol'), T0=(1, 'K')),
)

