// MRH 15-APR-2011

1) Copy and pasted entire Dooley et al. mechanism to reactions.txt file
2) By hand, moved pressure-dependent reactions to pdepreactions.txt file
3) Replace "!" with "//"
4) Add "	0.0	0.0	0.0" to end of each high-p limit kinetics
5) Place comments from end of high-p kinetics line to next line
6) Replace "<=>" with " <=> "
7) pdepreactions.txt: 
					: Change "PRESSURE DEPENDANCE" to PLOG format
					: Comment reactions that have "+AR" and "+HE"
8) reactions.txt: Replace "2CH2OH" with "CH2OH+CH2OH"
				: Replace "2CH3O" with "CH3O+CH3O"
				: Replace "C3KET21" with "CH3COCH2O2H"
				: Replace "HOOCH2OCHO" with "HO2CH2OCHO"