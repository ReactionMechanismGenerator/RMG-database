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
			Tdata = ([3600, 4800, 6000],'K'),
			Cpdata = ([23.05, 23.10, 23.15],'J/(mol*K)'),
			H298 = (450, 'kJ/mol', 8),
			S298 = (167.981, 'J/(mol*K)', 0.004),
			),
		shortDesc = u"Si atom",
		longDesc = u"""
		From NIST Webbook
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
			Tdata = ([298.15],'K'),
			Cpdata = ([217.3],'J/(mol*K)', [4]),
			H298 = (200.5, 'kJ/mol', 2.5),
			S298 = (217.3, 'J/(mol*K)', 4),
			),
		shortDesc = u"Silyl radical",
		longDesc = u"""
		From NIST Computational Chemistry Comparison and Benchmark Database (CCCBDB).
		From this references uncertainties are either given or determined from the spread of data 
		(whichever is greatest).
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
			Tdata = ([298.15],'K'),
			Cpdata = ([275],'J/(mol*K)', [10]),
			H298 = (80.3, 'kJ/mol', 1.5),
			S298 = (270.3, 'J/(mol*K)', 10),
			),
		shortDesc = u"Disilane",
		longDesc = u"""
		From NIST CCCBDB
		""",
		)

