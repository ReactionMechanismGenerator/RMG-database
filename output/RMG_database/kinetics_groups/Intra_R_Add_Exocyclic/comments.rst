General comments go at the top of the file,

-------
General
-------
or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')

---
813
---
MRH CBS-QB3 calculations for the reaction CH2=CH-CH2-OO => *CH2-cycle(CH-CH2-O-O)

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to
	a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable
	hindered rotor was accurate)
Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.724e+10 * (T/1K)^0.478 * exp(-29.169 kcal/mol / RT) cm3/mol/s.
