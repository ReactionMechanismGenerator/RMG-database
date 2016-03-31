name = "DolletSi2H4"
shortDesc = u"Reactions involved in Si2H4 isomerization"
longDesc = u"""
Reactions and rate constants are from Table 5 in J. Anal. Appl. Pyrolysis 80, 460 (2007)
Authors A. Dollet and S. de Persis
Rates obtained from quantum RRK theory; pressure dependent. All parameters given are for Ar as bath gas. H2 and SiH4 also given in paper and not included here.
"""

entry(
		index = 1,
		label = "H3SiSiH => H2SiSiH2",
		degeneracy = 3,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(7.9E12, '1/s'), n=0, Ea=(5309.5, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (5E35, 'cm^3/mol/s'),
            			n = -6.55,
            			Ea = (10340, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = 0.0141,
        		T3 = (350.67, 'K'),
        		T1 = (-430.67, 'K'),
        		T2 = (300.25, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 2,
		label = "H3SiSiH => SiH4 + Si",
		degeneracy = 1,
		reversible = False,
    		duplicate = True,
		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(2.04E17, '1/s'), n=-1.21, Ea=(40834, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (3.14E23, 'cm^3/mol/s'),
            			n = -2.63,
            			Ea = (41883, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -1.1448,
        		T3 = (624.93, 'K'),
        		T1 = (692.71, 'K'),
        		T2 = (421.33, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 3,
		label = "H3SiSiH => SiH3 + SiH",
		degeneracy = 1,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(5.85E19, '1/s'), n=-1.79, Ea=(64940, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (3.46E23, 'cm^3/mol/s'),
            			n = -2.57,
            			Ea = (65262, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = 2.2323,
        		T3 = (3283.8, 'K'),
        		T1 = (5564.6, 'K'),
        		T2 = (8035.7, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 4,
		label = "H3SiSiH => SiH2Si + H2",
		degeneracy = 3,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(2.53E18, '1/s'), n=-1.30, Ea=(41338, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (1.11E24, 'cm^3/mol/s'),
            			n = -2.55,
            			Ea = (42141, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -1.0975,
        		T3 = (608.24, 'K'),
        		T1 = (671.96, 'K'),
        		T2 = (413.41, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		From H3SiSiH* adduct
		"""
		)

entry(
		index = 5,
		label = "H3SiSiH_T => SiH2Si_T + H2",
		degeneracy = 3,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(1.92E7, '1/s'), n=1.5, Ea=(19974, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (1.3E41, 'cm^3/mol/s'),
            			n = -7.46,
            			Ea = (26019, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.8146,
        		T3 = (165.85, 'K'),
        		T1 = (-3.65E14, 'K'),
        		T2 = (132.25, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		From H2SiSiH2* adduct
		"""
		)

entry(
		index = 6,
		label = "H3SiSiH => SiH2 + SiH2",
		degeneracy = 3,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(3.1E12, '1/s'), n=0.14, Ea=(54684, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (8.26E20, 'cm^3/mol/s'),
            			n = -1.65,
            			Ea = (56283, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.3811,
        		T3 = (159.08, 'K'),
        		T1 = (-4032.7, 'K'),
        		T2 = (86.611, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 7,
		label = "SiH4 + Si => H3SiSiH",
		degeneracy = 4,
		reversible = False,
		duplicate = True,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(2.37E14, 'cm^3/mol/s'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (5.94E19, 'cm^6/mol^2/s'),
            			n = -1.19,
            			Ea = (629.9, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = 2.6908,
        		T3 = (321.59, 'K'),
        		T1 = (373.15, 'K'),
        		T2 = (347.63, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 8,
		label = "SiH4 + Si => H2SiSiH2",
		degeneracy = 6,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(4.56E9, 'cm^3/mol/s'), n=1.07, Ea=(-440.1, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (3.8E20, 'cm^6/mol^2/s'),
            			n = -1.36,
            			Ea = (1036.5, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.2139,
        		T3 = (257.57, 'K'),
        		T1 = (-2062.9, 'K'),
        		T2 = (354.21, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 9,
		label = "SiH4 + Si => SiH2Si + H2",
		degeneracy = 6,
		reversible = False,
		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(3.85E-5, 'cm^3/mol/s'), n=5.01, Ea=(-54, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (3.34, 'cm^6/mol^2/s'),
            			n = 3.89,
            			Ea = (263.1, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.1166,
        		T3 = (1143.9, 'K'),
        		T1 = (457.12, 'K'),
        		T2 = (789.68, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		From H3SiSiH* adduct
		"""
		)

entry(
		index = 10,
		label = "SiH4 + Si => SiH2Si_T + H2",
		degeneracy = 6,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(2.62E2, 'cm^3/mol/s'), n=2.83, Ea=(-1546.7, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (2.37E14, 'cm^6/mol^2/s'),
            			n = 0,
            			Ea = (0, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.1859,
        		T3 = (272.14, 'K'),
        		T1 = (-1971.8, 'K'),
        		T2 = (399.69, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		From H2SiSiH2* adduct
		"""
		)

entry(
		index = 11,
		label = "SiH4 + Si => SiH3 + SiH",
		degeneracy = 4,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(4.27E4, 'cm^3/mol/s'), n=2.25, Ea=(21604, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (6.19E8, 'cm^6/mol^2/s'),
            			n = 1.33,
            			Ea = (21956, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = 2.627,
        		T3 = (876.57, 'K'),
        		T1 = (1485.5, 'K'),
        		T2 = (1947.7, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 12,
		label = "SiH4 + Si => SiH2 + SiH2",
		degeneracy = 6,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(5.95E-5, 'cm^3/mol/s'), n=4.61, Ea=(10819, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (1.03E4, 'cm^6/mol^2/s'),
            			n = 2.76,
            			Ea = (11784, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.1364,
        		T3 = (331.49, 'K'),
        		T1 = (-1772.6, 'K'),
        		T2 = (482.17, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 13,
		label = "Si2H2 + H2 => H2SiSiH2",
		degeneracy = 1,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(4.59E14, 'cm^3/mol/s'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (5.96E38, 'cm^6/mol^2/s'),
            			n = -6.32,
            			Ea = (4165, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = 3.6144,
        		T3 = (222.59, 'K'),
        		T1 = (356.22, 'K'),
        		T2 = (1665.3, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 14,
		label = "SiH2 + SiH2 => H2SiSiH2",
		degeneracy = 1,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(2.13E13, 'cm^3/mol/s'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (2.39E15, 'cm^6/mol^2/s'),
            			n = -0.2003,
            			Ea = (317.66, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = 1.0978,
        		T3 = (1559.3, 'K'),
        		T1 = (560.36, 'K'),
        		T2 = (314.68, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)

entry(
		index = 15,
		label = "SiH3 + SiH => H2SiSiH2",
		degeneracy = 3,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(2.77E9, 'cm^3/mol/s'), n=0.849, Ea=(-302.59, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (2.46E14, 'cm^6/mol^2/s'),
            			n = 0.0304,
            			Ea = (173.36, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.5098,
        		T3 = (48.255, 'K'),
        		T1 = (-17400, 'K'),
        		T2 = (20.582, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)
entry(
		index = 16,
		label = "SiH2 + SiH2 => Si2H2 + H2",
		degeneracy = 1,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(5.16E10, 'cm^3/mol/s'), n=0.4069, Ea=(-392.32, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (2.8E13, 'cm^6/mol^2/s'),
            			n =0.039,
            			Ea = (32.437, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.3829,
        		T3 = (459.73, 'K'),
        		T1 = (316.18, 'K'),
        		T2 = (342.63, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)
entry(
		index = 17,
		label = "SiH3 + SiH => Si2H2 + H2",
		degeneracy = 3,
		reversible = False,
    		kinetics = Troe(
        		arrheniusHigh = Arrhenius(A=(1.41E8, 'cm^3/mol/s'), n=0.9108, Ea=(-496.46, 'cal/mol'), T0=(1, 'K')),
        		arrheniusLow = Arrhenius(
            			A = (5.26E13, 'cm^6/mol^2/s'),
            			n = -0.12,
            			Ea = (94.685, 'cal/mol'),
           			T0 = (1, 'K'),
        			),
        		alpha = -0.5218,
        		T3 = (-0.5232, 'K'),
        		T1 = (16.824, 'K'),
        		T2 = (36.524, 'K'),
			),
		longDesc = u"""
		Added by Belinda Slakman from Dollet & de Persis, 2007, J. Anal. Appl. Pyrolysis
		"""
		)
