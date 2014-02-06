General comments go at the top of the file,

-------
General
-------
or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')

---
845
---
MRH CBS-QB3 calculations for the reaction CH3-CH(OO)-CH=CH2 => CH2=CH-CH=CH2 + HO2

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to CH3-*CH-CH=CHOH => CH2=CH-CH=CHOH + HO2.
The high-p limit kinetics were necessary to estimate a k(T,P) for this PES.  MRH could not find a 
stable TS geometry for the exact reaction.  Instead, I removed the OH group and found
a stable TS for that reaction (the titled reaction for this node).

Reactant: 3 hindered rotors were considered (the -OO, -CH3, and -CH=CH2 torsions)
TS: 0 hindered rotors were considered (MRH attempted to treat the -CH=CH2 torsion as a hindered rotor,
	but with no luck.  The complete 360 degree spin would interfere with the HO2 elimination).
Product: 1 hindered rotor was considered (the -CH=CH2 torsion of 1,3-butadiene)

All external symmetry numbers were set equal to one, with the exception of 1,3-butadience which was set to two.
The k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.476e+06 * (T/1K)^1.829 * exp(-24.247 kcal/mol / RT) cm3/mol/s.  MRH divided this rate coefficient by
three to account for the reaction path degeneracy, yielding the value stored in the rateLibrary.

---
846
---
MRH approximation for the general R2OO_2H_HDe node

MRH computed the rate coefficient for the reaction CH3-CH(OO)-CH=CH2 => CH2=CH-CH=CH2 + HO2 (see node 845).
The difference between the R2OO_2H_HDe and CH3CH(OO)CHCH2 nodes is defining the delocalized group (in the
case of the CH3CH(OO)CHCH2 node, the -CH=CH2 functional group).  MRH thinks using the kinetics for node 845
in the event node 846 is hit is reasonable, considering this part of the molecule does not play a role in the
TS (and it is certainly better than leaving RMG to estimate via "Average of Average").

---
847
---
MRH CBS-QB3 calculations for the reaction CH3-CH(OO)-OH => CH3-CH=O + HO2

Previous RMG estimate for this reaction was zero (RMG only allowed HO2 direct elimination
to occur for species with the structure H-C-C-O-O* ... note the atom next to the hydrogen
had to be a carbon).

MRH calculated the rate coefficient using the CBS-QB3 method.  1-d hindered rotor
corrections were applied and NO tunneling correction.  The reason no tunneling correction
was applied is that the TS is lower in energy than the products, CH3CHO + HO2.

da Silva, Bozzelli, Liang, and Farrell (dx.doi.org/10.1021/jp903210a) recently studied
this reaction system (ethanol + O2).  In their calculations (G3B3), they determined a stable
adduct existed between the reactant CH3CH(OO)OH and the products CH3CHO+HO2.  The adduct is
stable due to H-bonding.  MRH believes his TS is for the reactant to the adduct.
Comparing my k(T) with the da Silva et al. k(T) (for forming the adduct) shows very
good agreement, within a factor of 2 over the valid temperature range.  Furthermore, the
da Silva et al. calculation for the adduct going to product is between 2-5 orders of
magnitude faster than reactants going to adduct, so it is a reasonable assumption
to say the first step is the rate-limiting step.

Comparing my k(T) with two other sources for this reaction (dx.doi.org/10.1021/jp003762p and 
I. Hermans et al., AIAA Journal, 109, (2005), 4303-4311) also shows good agreement.
I am setting the rank for this k(T) to be 5 (very uncertain).

Information on the TST calculations:

Reactant: 3 hindered rotors were considered (the -OO, -CH3, and -OH torsions)
TS: 1 hindered rotor was considered (the -CH3 torsion)
Product: 1 hindered rotor was considered (the -CH3 torsion of CH3CHO)

All external symmetry numbers were set equal to one.
The k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 6.813e+10 * (T/1K)^0.493 * exp(-11.894 kcal/mol / RT) cm3/mol/s.

---
848
---
MRH approximation for the general OCOO node

In the event RMG finds any H-O-C-O-O* connection, the kinetics used for direct
HO2 elimination will be those of CH3-CH(OO)-OH => CH3CHO + HO2.
