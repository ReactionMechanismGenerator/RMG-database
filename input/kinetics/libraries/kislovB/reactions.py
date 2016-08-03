#!/usr/bin/env python
# encoding: utf-8

name = "kislovB"
shortDesc = u"level of theory:Ab initio G3(MP2,CC)//B3LYP"
longDesc = u"""
Kinetics from:
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion
Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel*
Department of Chemistry and Biochemistry, Florida International UniVersity, Miami, Florida 33199
Received: October 30, 2006; In Final Form: December 19, 2006
J. Phys. Chem. A 2007, 111, 3922-3931
"""
entry(
    index = 1,
    label = "benzene + methyl <=> KislovT1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2195.14, 'cm^3/(mol*s)'),
        n = 2.878,
        Ea = (10.9119, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT1	=	benzene	+	methyl		3.19945E+12	0.472	22.4157 0.0 0.0 0.0
""",
)

entry(
    index = 2,
    label = "benzene + methyl <=> phenyl + methane",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5151.28, 'cm^3/(mol*s)'),
        n = 2.896,
        Ea = (15.3076, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/phenyl	+	methane	=	benzene	+	methyl		223.6315877	3.202	6.6208 0.0 0.0 0.0
""",
)

entry(
    index = 3,
    label = "KislovT1 <=> toluene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.21711e+10, 's^-1'), n=0.87, Ea=(25.199, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/toluene	+	H	=	KislovT1		2741456.756	1.768	5.8153 0.0 0.0 0.0
""",
)

entry(
    index = 4,
    label = "toluene + H <=> KislovT2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15199e+06, 'cm^3/(mol*s)'),
        n = 1.985,
        Ea = (6.1749, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT2	+	H2	=	toluene	+	H		223462.7472	2.3	17.9762 0.0 0.0 0.0
""",
)

entry(
    index = 5,
    label = "toluene + H <=> KislovT3 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73829e+07, 'cm^3/(mol*s)'),
        n = 1.889,
        Ea = (15.4607, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT3	+	H2	=	toluene	+	H		84626.26852	2.371	5.6916 0.0 0.0 0.0
""",
)

entry(
    index = 6,
    label = "KislovT3 <=> KislovT2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.71217e+10, 's^-1'),
        n = 0.722,
        Ea = (41.8779, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT2	=	KislovT3		6.80436E+11	0.545	63.4434 0.0 0.0 0.0
""",
)

entry(
    index = 7,
    label = "KislovT2 + ethyne <=> KislovT4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31634.4, 'cm^3/(mol*s)'),
        n = 2.479,
        Ea = (11.0608, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT4	=	KislovT2	+	ethyne		1.73148E+12	0.675	27.3222 0.0 0.0 0.0
""",
)

entry(
    index = 8,
    label = "KislovT4 <=> KislovT5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25679e+11, 's^-1'),
        n = 0.139,
        Ea = (13.2335, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT5	=	KislovT4		3.80752E+12	0.267	27.8895 0.0 0.0 0.0
""",
)

entry(
    index = 9,
    label = "KislovT5 <=> indene + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.59718e+10, 's^-1'),
        n = 0.889,
        Ea = (20.8933, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/indene	+	H	=	KislovT5		118568332.7	1.554	7.8006 0.0 0.0 0.0
""",
)

entry(
    index = 10,
    label = "benzene + propargyl <=> KislovB1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (144.604, 'cm^3/(mol*s)'),
        n = 2.951,
        Ea = (14.0549, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB1	=	benzene	+	propargyl		3.54302E+12	0.342	15.3527 0.0 0.0 0.0
""",
)

entry(
    index = 11,
    label = "benzene + propargyl <=> KislovB5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (312.311, 'cm^3/(mol*s)'),
        n = 2.973,
        Ea = (16.3956, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB5	=	benzene	+	propargyl		6.83447E+12	0.322	19.1394 0.0 0.0 0.0
""",
)

entry(
    index = 12,
    label = "KislovB1 <=> KislovB2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.48547e+11, 's^-1'),
        n = 0.0648,
        Ea = (27.9414, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB2	=	KislovB1		7.32698E+11	0.548	21.6048 0.0 0.0 0.0
""",
)

entry(
    index = 13,
    label = "KislovB5 <=> KislovB2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.56537e+11, 's^-1'),
        n = 0.00935,
        Ea = (28.5208, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB2	=	KislovB5		7.08205E+11	0.534	20.8399 0.0 0.0 0.0
""",
)

entry(
    index = 14,
    label = "KislovB2 <=> KislovC3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.52718e+10, 's^-1'),
        n = 0.853,
        Ea = (47.8482, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovC3	=	KislovB2		76000062530	0.663	75.0119 0.0 0.0 0.0
""",
)

entry(
    index = 15,
    label = "KislovC3 <=> KislovT5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.43776e+10, 's^-1'),
        n = 0.625,
        Ea = (38.3239, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovT5	=	KislovC3		1.33718E+11	0.64	45.7951 0.0 0.0 0.0
""",
)

entry(
    index = 16,
    label = "KislovB2 <=> KislovB3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23068e+11, 's^-1'),
        n = 0.765,
        Ea = (55.9411, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB3	=	KislovB2		1.27451E+11	0.772	55.5603 0.0 0.0 0.0
""",
)

entry(
    index = 17,
    label = "KislovB3 <=> KislovB4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.67719e+10, 's^-1'),
        n = 0.839,
        Ea = (43.6379, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB4	=	KislovB3		1.67626E+11	0.707	85.3162 0.0 0.0 0.0
""",
)

entry(
    index = 18,
    label = "KislovB4 <=> indene + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.59124e+10, 's^-1'),
        n = 0.886,
        Ea = (24.9749, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/indene	+	H	=	KislovB4		154082695.5	1.5	5.2149 0.0 0.0 0.0
/commented out because triradical!
/KislovB2	=	KislovB6		24624309919	0.964	61.1662 0.0 0.0 0.0
/KislovB6	=	KislovB2		6.18152E+11	0.361	30.0646 0.0 0.0 0.0
/commented out because triradical!
/KislovB6	=	KislovB4		3.66189E+12	0.12	1.4313 0.0 0.0 0.0
/KislovB4	=	KislovB6		2.92872E+11	0.618	73.9642 0.0 0.0 0.0
""",
)

entry(
    index = 19,
    label = "KislovB10 + H <=> KislovB12 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.5395e+07, 'cm^3/(mol*s)'),
        n = 1.901,
        Ea = (15.4181, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB12	+	H2	=	KislovB10	+	H		84965.45151	2.378	5.602 0.0 0.0 0.0
""",
)

entry(
    index = 20,
    label = "KislovB12 <=> KislovB13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.53352e+11, 's^-1'),
        n = 0.102,
        Ea = (13.0485, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB13	=	KislovB12		5.2592E+12	0.445	44.9914 0.0 0.0 0.0
""",
)

entry(
    index = 21,
    label = "KislovB11 + H <=> KislovB14 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.72549e+07, 'cm^3/(mol*s)'),
        n = 1.892,
        Ea = (16.6195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB14	+	H2	=	KislovB11	+	H		111524.5472	2.365	5.9931 0.0 0.0 0.0
""",
)

entry(
    index = 22,
    label = "KislovB14 <=> KislovB13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.43073e+11, 's^-1'),
        n = 0.114,
        Ea = (15.5791, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/KislovB13	=	KislovB14		2.98613E+12	0.474	43.1633 0.0 0.0 0.0
""",
)

