name = "Silicon"
shortDesc = u"Silicon hydride reaction rates"
longDesc = u"""
"""

entry(
		index = 1,
		label = "cSi3H6 <=> SiH3SiH2SiH",
		degeneracy = 1,
		kinetics = Arrhenius(A=(1.202E13, '1/s'), n=0, Ea=(17.2, 'kcal/mol')),
		longDesc = u"""
		Added by Belinda Slakman from Adamczyk et al., Theor. Chem. Acc. (2011) 128: 91-113
                Ring opening reaction direction; assumes step 2 in cyclization is the rate limiting step
                Rate from G3//B3LYP corrected for internal rotations 
		"""
		)

entry(
		index = 2,
		label = "cSi4H8 <=> SiH3SiH2SiH2SiH",
		degeneracy = 1,
		kinetics = Arrhenius(A=(1.047E14, '1/s'), n=0, Ea=(38.6, 'kcal/mol')),
		longDesc = u"""
		Added by Belinda Slakman from Adamczyk et al., Theor. Chem. Acc. (2011) 128: 91-113
                Ring opening reaction direction; assumes step 1 in cyclization is the rate limiting step (same for all reactions with >= 4 silicons)
                Rate from G3//B3LYP corrected for internal rotations 
		"""
		)

