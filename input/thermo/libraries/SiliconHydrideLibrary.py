entry(
		index = 1,
		label = 'SiH4',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		4 H u0 p0 c0 {1,S}
		5 H u0 p0 c0 {1,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([10.294,12.197,14.028,15.663,18.268,20.118,22.738],'cal/(mol*K)'),
			H298 = (5.572, 'kcal/mol'),
			S298 = (48.865, 'cal/(mol*K)'),
			),
		shortDesc = u"silane",
		longDesc = u"""
		CBS-QB3 calculations using g09 and Cantherm, by Belinda Slakman 09/17/15; symm=12
		""",
		)


entry(
		index = 2,
		label = 'Si',
		molecule = 
		"""
		1 Si u2 p1 c0
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968,],'cal/(mol*K)'),
			H298 = (107.731, 'kcal/mol'),
			S298 = (38.099, 'cal/(mol*K)'),
			),
		shortDesc = u"Si atom",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 10/24/14
		""",
		)

entry(
		index = 3,
		label = 'SiH',
		molecule = 
		"""
		1 Si u1 p1 c0 {2,S}
		2 H u0 p0 c0 {1,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([30.10, 30.01, 30.52, 31.21, 32.68, 34.00, 36.08],'J/(mol*K)'),
			H298 = (376.66, 'kJ/mol'),
			S298 = (198.04, 'J/(mol*K)'),
			),
		shortDesc = u"silylidyne",
		longDesc = u"""
		From NIST Webbook
		""",
		)

entry(
		index = 4,
		label = 'Si2',
		molecule = 
		"""
		1 Si u1 p0 c0 {2,T}
		2 Si u1 p0 c0 {1,T}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([34.50, 36.20, 38.04, 39.76, 42.43, 43.80, 43.40],'J/(mol*K)'),
			H298 = (589.94, 'kJ/mol'),
			S298 = (229.8, 'J/(mol*K)'),
			),
		shortDesc = u"Diatomic Si. Si#Si",
		longDesc = u"""
		From NIST Webbook
		""",
		)

entry(
		index = 5,
		label = 'SiH3',
		molecule = 
		"""
		1 Si u1 p0 c0 {2,S} {3,S} {4,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		4 H u0 p0 c0 {1,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([9.589,10.795,11.96,13.01,14.705,15.934,17.717],'cal/(mol*K)'),
			H298 = (45.894, 'kcal/mol'),
			S298 = (51.821, 'cal/(mol*K)')
		),
		shortDesc = u"Silyl radical",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 10/03/15; symm=3
		""",
		)

entry(
		index = 6,
		label = 'Si2H6',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		4 H u0 p0 c0 {1,S}
		5 Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
		6 H u0 p0 c0 {5,S}
		7 H u0 p0 c0 {5,S}
		8 H u0 p0 c0 {5,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([19.08,22.854,26.004,28.602,32.517,35.236,39.146],'cal/(mol*K)'),
			H298 = (15.974, 'kcal/mol'),
			S298 = (65.426, 'cal/(mol*K)'),
			),
		shortDesc = u"Disilane",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 9/16/15; symm=6
		""",
		)

entry(
		index = 7,
		label = 'SiH2_singlet',
		molecule = 
		"""
		1 Si u0 p1 c0 {2,S} {3,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([8.35,8.821,9.381,9.954,10.921,11.651,12.734],'cal/(mol*K)'),
			H298 = (62.875, 'kcal/mol'),
			S298 = (49.554, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 10/03/15; symm=2
		""",
		)

entry(
		index = 8,
		label = 'SiH2_triplet',
		molecule = 
		"""
		1 Si u2 p0 c0 {2,S} {3,S}
		2 H u0 p0 c0 {1,S}
		3 H u0 p0 c0 {1,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([8.471,8.935,9.442,9.944,10.841,11.547,12.622],'cal/(mol*K)'),
			H298 = (84.884, 'kcal/mol'),
			S298 = (51.402, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 10/03/15; symm=2
		""",
		)

entry(
		index = 9,
		label = 'Si2H2',
		molecule = 
		"""
		1 Si u0 p1 c0 {2,S} {3,S}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p1 c0 {1,S} {4,S}
		4 H u0 p0 c0 {3,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([13.713,14.706,15.409,15.934,16.754,17.481,18.612], 'cal/(mol*K)'),
			H298 = (108.784, 'kcal/mol'),
			S298 = (63.217, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 11/5/14 
		""",
		)

entry(
		index = 10,
		label = 'H2SiSiH',
		molecule = 
		"""
		1 Si u1 p0 c0 {2,S} {3,D}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p0 c0 {1,D} {4,S} {5,S}
		4 H u0 p0 c0 {3,S}
		5 H u0 p0 c0 {3,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([15.501,17.076,18.319,19.344,20.949,22.12,23.855], 'cal/(mol*K)'),
			H298 = (95.238, 'kcal/mol'),
			S298 = (69.912, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 10/03/15; symm=1 
		""",
		)

entry(
		index = 11,
		label = 'Si2H4',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,D} {6,S}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p0 c0 {1,D} {4,S} {5,S}
		4 H u0 p0 c0 {3,S}
		5 H u0 p0 c0 {3,S}
                6 H u0 p0 c0 {1,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([16.524,19.06,21.043,22.599,24.858,26.427,28.838], 'cal/(mol*K)'),
			H298 = (64.556, 'kcal/mol'),
			S298 = (64.263, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 9/16/15; symm=2 
		""",
		)

entry(
		index = 12,
		label = 'H3SiSiH',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p1 c0 {1,S} {6,S}
		4 H u0 p0 c0 {1,S}
		5 H u0 p0 c0 {1,S}
                6 H u0 p0 c0 {3,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([16.597,18.912,20.863,22.48,24.913,26.585,28.948], 'cal/(mol*K)'),
			H298 = (72.429, 'kcal/mol'),
			S298 = (70.02, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g09 and CanTherm, by Belinda Slakman 10/05/15; symm=1
		""",
		)

entry(
		index = 13,
		label = 'cSi3H6',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
		4 H u0 p0 c0 {1,S}
		5 Si u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
                6 H u0 p0 c0 {3,S}
                7 H u0 p0 c0 {3,S}
                8 H u0 p0 c0 {5,S}
                9 H u0 p0 c0 {5,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([25.3,29.6,32.6,35.1,38.9,41.6,45.5], 'cal/(mol*K)'),
			H298 = (67.3, 'kcal/mol'),
			S298 = (76.3, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
                H298 from Katzer et al., J. Phys. Chem. A (101), 1997.
		G3//B3LYP calculations with bond additivity corrections from Wong et al., J. Phys. Chem. A (108), 2004.
		""",
		)

entry(
		index = 14,
		label = 'cSi3H4-lp',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
		4 H u0 p0 c0 {1,S}
		5 Si u0 p1 c0 {1,S} {3,S}
                6 H u0 p0 c0 {3,S}
                7 H u0 p0 c0 {3,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([21.4,24.3,26.4,28.0,30.6,32.4,35.0], 'cal/(mol*K)'),
			H298 = (115.5, 'kcal/mol'),
			S298 = (73.9, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
                H298 from Katzer et al., J. Phys. Chem. A (101), 1997.
		G3//B3LYP calculations with bond additivity corrections from Wong et al., J. Phys. Chem. A (108), 2004.
		""",
		)

entry(
		index = 15,
		label = 'cSi3H4-D',
		molecule = 
		"""
		1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
		2 H u0 p0 c0 {1,S}
		3 Si u0 p0 c0 {1,S} {5,D} {6,S}
		4 H u0 p0 c0 {1,S}
		5 Si u0 p0 c0 {1,S} {3,D} {7,S}
                6 H u0 p0 c0 {3,S}
                7 H u0 p0 c0 {5,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([21.4,24.4,26.5,28.1,30.7,32.5,35.0], 'cal/(mol*K)'),
			H298 = (112.0, 'kcal/mol'),
			S298 = (73.9, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
                H298 from Katzer et al., J. Phys. Chem. A (101), 1997.
		G3//B3LYP calculations with bond additivity corrections from Wong et al., J. Phys. Chem. A (108), 2004.
		""",
		)

entry(
		index = 16,
		label = 'cSi3H2-lp-D',
		molecule = 
		"""
		1 Si u0 p1 c0 {2,S} {3,S}
		2 Si u0 p0 c0 {1,S} {3,D} {4,S}
		3 Si u0 p0 c0 {1,S} {2,D} {5,S}
                4 H u0 p0 c0 {2,S}
                5 H u0 p0 c0 {3,S}
		""",
		thermo = ThermoData(
			Tdata = ([300,400,500,600,800,1000,1500],'K'),
			Cpdata = ([17.4,19.2,20.3,21.1,22.4,23.3,24.5], 'cal/(mol*K)'),
			H298 = (123.0, 'kcal/mol'),
			S298 = (70.3, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		G3//B3LYP calculations with bond additivity corrections from Wong et al., J. Phys. Chem. A (108), 2004.
		""",
		)

