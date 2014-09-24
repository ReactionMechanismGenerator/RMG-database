entry(
		index = 1,
		label = 'SiH4',
		molecule = 
		"""
		1 Si 0
		""".
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

