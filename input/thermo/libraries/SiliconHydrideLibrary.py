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
			Cpdata = ([10.27, 12.30, 14.14, 15.75, 18.33, 20.2, 22.83],'cal/(mol*K)'),
			H298 = (8.2, 'kcal/mol'),
			S298 = (48.913, 'cal/(mol*K)'),
			),
		shortDesc = u"silane",
		longDesc = u"""
		From NIST Webbook
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
			Cpdata = ([9.579,10.781,11.968,13.031,14.702,15.93,17.732],'cal/(mol*K)'),
			H298 = (45.879, 'kcal/mol'),
			S298 = (54.005, 'cal/(mol*K)')
		),
		shortDesc = u"Silyl radical",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 10/24/14
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
			Cpdata = ([19.193,22.953,25.955,28.5,32.496,35.321,39.159],'cal/(mol*K)'),
			H298 = (15.954, 'kcal/mol'),
			S298 = (65.546, 'J/(mol*K)'),
			),
		shortDesc = u"Disilane",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 10/24/14
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
			S298 = (50.932, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 10/24/14
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
			Cpdata = ([8.472,8.926,9.439,9.959,10.855,11.549,12.629],'cal/(mol*K)'),
			H298 = (84.868, 'kcal/mol'),
			S298 = (52.781, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 10/24/14
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
			Cpdata = ([15.554,17.003,18.243,19.305,20.98,22.175,23.834], 'cal/(mol*K)'),
			H298 = (95.251, 'kcal/mol'),
			S298 = (68.744, 'cal/(mol*K)'),
			),
		shortDesc = u"",
		longDesc = u"""
		CBS-QB3 calculations using g03 and CanTherm, by Belinda Slakman 11/6/14 
		""",
		)

