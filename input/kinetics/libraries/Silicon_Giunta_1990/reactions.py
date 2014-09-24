name = "Silicon_Giunta_1990"
shortDesc = u"Silane and disilane gas phase kinetics"
longDesc = u"""
Reactions and rate constants are from Table 1 in Journal of Applied Physics 67, 1062 (1990); doi: 10.1063/1.345792
Authors C.J. Giunta, R.J. McCurdy, J.D. ChappleSokol, and R.G. Gordon
"""

entry(
		index = 1,
		label = "SiH4 <==> SiH2 + H2",
		degeneracy = 1,
		kinetics = Arrhenius(A=(3.3E15, '1/s'), n=-0.5, Ea=(55.9, 'kcal/mol')),
		longDesc = u"""
		Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
		"""
		)

entry(
                index = 2,
                label = "Si2H6 <==> SiH2 + SiH4",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.5E19, '1/s'), n=-1.0, Ea=(54.9, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 3,
                label = "Si2H6 <==> SiH3SiH + H2",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.0E15, '1/s'), n=0.0, Ea=(55.3, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 4,
                label = "Si3H8 <==> SiH2 + Si2H6",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.6E19, '1/s'), n=-1.0, Ea=(55.5, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 21,
                label = "SiH2 + H2 <==> SiH4",
                degeneracy = 1,
                kinetics = Arrhenius(A=(3.0E10, 'cm^3/mol/s'), n=0.5, Ea=(-0.7, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
		A note about numbering: the indices reflect those used in the paper, except for a few. This index 21 is
		because it is the reverse of reaction 1, assume the same for all reactions with index > 20 in this set.
                """
                )

entry(
                index = 5,
                label = "Si3H8 <==> SiH3SiH + SiH4",
                degeneracy = 1,
                kinetics = Arrhenius(A=(4.8E14, '1/s'), n=0.0, Ea=(49.2, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
		index = 22,
		label = "SiH2 + SiH4 <==> Si2H6",
		degeneracy = 1,
		kinetics = Arrhenius(A=(1.3E14, 'cm^3/mol/s'), n=0.0, Ea=(0.0, 'kcal/mol')),
		longDesc = u"""
		Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
		"""
		)

entry(
                index = 23,
                label = "SiH3SiH + H2 <==> Si2H6",
                degeneracy = 1,
                kinetics = Arrhenius(A=(1.8E10, 'cm^3/mol/s'), n=1.0, Ea=(4.5, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 24,
                label = "SiH2 + Si2H6 <==> Si3H8",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.5E14, 'cm^3/mol/s'), n=0.0, Ea=(0.0, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 25,
                label = "SiH3SiH + SiH4 <==> Si3H8",
                degeneracy = 1,
                kinetics = Arrhenius(A=(4.6E9, 'cm^3/mol/s'), n=1.0, Ea=(0.0, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 11,
                label = "SiH3SiH <==> SiH2=SiH2",
                degeneracy = 1,
                kinetics = Arrhenius(A=(1.15E20, '1/s'), n=-3.06, Ea=(6.63, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 31,
                label = "SiH2=SiH2 <==> SiH3SiH",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.48E20, '1/s'), n=-3.06, Ea=(17.71, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 16,
                label = "SiH2 + SiH2 <==> SiH2=SiH2",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.5E14, 'cm^3/mol/s'), n=0.0, Ea=(0.0, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )

entry(
                index = 36,
                label = "SiH2=SiH2 <==> SiH2 + SiH2",
                degeneracy = 1,
                kinetics = Arrhenius(A=(2.6E20, 'cm^3/mol/s'), n=-1.0, Ea=(71.8, 'kcal/mol')),
                longDesc = u"""
                Added by Belinda Slakman from Giunta et al., 1990, J. Appl. Phys.
                """
                )
