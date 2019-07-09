
#!/usr/bin/env python
# encoding: utf-8

name = "fascella"
shortDesc = u"All calculations were performed both at the G2MP2* levels of theory. The rate coefficients of the backward reactions were determined through thermodynamic consistence."
longDesc = u"""
Kinetics from:
The Peculiar Kinetics of the Reaction between Acetylene and the Cyclopentadienyl Radical 
Simone Fascella, Carlo Cavallotti,* Renato Rota,* and Sergio Carra`
Politecnico di Milano, Dipartimento di Chimica, Materiali e Ingegneria Chimica G. Natta / CIIRCO
J. Phys. Chem. A 2005, 109, 7546-7557
a Kinetic parameters are reported in units consistent with kcal, s, mol, and cm.

"""
entry(
    index = 1,
    label = "cC5H5 + ethyne <=> C7H71",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(13.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/C7H71	=	cC5H5 +	ethyne	4.20E+15	-1	19.5	   0.0	0.0	0.0
""",
)

entry(
    index = 2,
    label = "C7H71 <=> C7H7c4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+12, 's^-1'), n=0, Ea=(13.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/cC7H7c4	=	C7H71			1.60E+13	0	28.7	  	   0.0	0.0	0.0
""",
)

entry(
    index = 3,
    label = "C7H7c4 <=> cC7H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 's^-1'), n=0, Ea=(26.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/cC7H7		= C7H7c4				2.70E+13	0	52.9	   	   0.0	0.0	0.0
""",
)

entry(
    index = 4,
    label = "cC7H7 + ethyne <=> C9H91",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(20.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/C9H91	=	cC7H7 +	ethyne		7.50E+15	-1	20.1	   	   0.0	0.0	0.0
""",
)

entry(
    index = 5,
    label = "C9H91 <=> C9H9c4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.7e+12, 's^-1'), n=0, Ea=(17.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/C9H9c4	=	C9H91				1.80E+13	0	31.9	   	   0.0	0.0	0.0
""",
)

entry(
    index = 6,
    label = "C9H9c4 <=> cC9H9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 's^-1'), n=0, Ea=(23.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/cC9H9	 =	C9H9c4				2.40E+11	0	25.6	   	   0.0	0.0	0.0
""",
)

entry(
    index = 7,
    label = "cC9H9 <=> C9H9c5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+11, 's^-1'), n=0, Ea=(26.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/C9H9c5 =		cC9H9				7.70E+12	0	40.5	   	   0.0	0.0	0.0
""",
)

entry(
    index = 8,
    label = "C9H9c5 <=> C9H9c5_T",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.9e+12, 's^-1'), n=0, Ea=(33.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/C9H9c5_T	=	C9H9c5			4.10E+12	0	47.8	   	   0.0	0.0	0.0
""",
)

entry(
    index = 9,
    label = "C9H9c5_T <=> indene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+12, 's^-1'), n=0, Ea=(23.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/indene +	H	= C9H9c5_T			5.50E+12	0	11.6	 	   0.0	0.0	0.0
""",
)

