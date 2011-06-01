primaryThermoLibrary
====================

This thermochemistry library contains thermochemistry of a few small
molecules. Some of them, RMG may otherwise estimate poorly. In some instances
it would be OK estimating via group additivity, but if running with automatic
quantum calculations the calculations are likely to fail.

It is recommended that this library is included in all calculations. (It is
advisable to use a much larger library, as many other small molecules will be
poorly estimated by RMG. This should be considered a bare minimum.)

--------
Sources:
--------

For CO3 isomers:
Data is from the paper by Mebel et al. [1].
Geometries are from Figure 1.
Vibrational frequencies from the supplementary material.
H298 values are derived from the relative energies given in the paper.

For C3Hn species:
Geometries from Aguilera-Iparraguirre [2] and frequencies from Nguyen [3].
H298 values from a mixture of the two.

For OCCO species: 
QCI//DFT calculation by C.F. Goldsmith (2010): The lowest energy conformer
using CBS-QB3 method was selected, and this geometry was re-optimized using
the B3LYP functional with the larger 6-311++G(d,p) basis set. the DFT
equilibrium geometries were used for RQCISD(T)/cc-pVTZ and RQCISD(T)/cc-pVQZ
energies. To avoid spin contamination, all calculations were spin restricted.
The RQCISD(T) complete basis set limit was extrapolated from the triple and
quadruple zeta basis set calculations assuming an inverse power law.
Manuscript in preparation.

For C3H2 species:
Here is the website for "Burcat" as of 3/25/2011: http://garfield.chem.elte.hu/Burcat/BURCAT.THR
The species information present as of 3/25/2011 is the following:
16165-40-5
C3H2 CYCLOPROPENYLIDENE BI-RADICAL SINGLET SIGMA=2 STATWT=1 Ia=2.35340 Ib=2.4065  
Ic=4.8941  Nu=788,887,[898,979],1063,1277,[1588,3080,3114] REF=Webbook NIST2000
+[]Vereecken, et al JCP 108,(1998),1068   HF298=114 kcal  REF= Kiefer et.al. 
J. Phys. Chem 101, (1997), 4057   {HF298=121.63+/-6.3 kcal REF=Melius 1988 P60V}  
{HF298=136 kcal   REF=PM3 RHF calculation}   Max Lst Sq  Error Cp @ 200 K 0.82%
C3H2(1) Cyclo     T12/00C  3.H  2.   0.   0.G   200.000  6000.000  B  38.04888 1
 5.69445684E+00 6.53821901E-03-2.35907266E-06 3.82037384E-10-2.29227460E-14    2
 5.49264274E+04-6.96163733E+00 3.18167129E+00-3.37611741E-04 3.95343765E-05    3
-5.49792422E-08 2.28335240E-11 5.61816758E+04 9.06482468E+00 5.73666999E+04    4
MRH converted from the NASA-7 polynomials found here to the RMG format found in the Library.txt file


----------
References
----------

[1] A. M. Mebel, M. Hayashi, V. V. Kislov, and S. H. Lin. Theoretical Study of
Oxygen Isotope Exchange and Quenching in the O(1D) + CO2 Reaction. The Journal
of Physical Chemistry A, 108(39):7983–7994, September 2004.
http://dx.doi.org/10.1021/jp049315h

[2] J. Aguilera-Iparraguirre, A. Daniel Boese, W. Klopper, and B. Ruscic.
Accurate ab initio computation of thermochemical data for C3Hx
(x=0,...,4)(x=0,...,4) species. Chemical Physics, 346(1-3):56–68, May 2008.
http://dx.doi.org/10.1016/j.chemphys.2008.01.057

[3] T. L. Nguyen, A. M. Mebel, and R. I. Kaiser. A Theoretical Investigation
of the Triplet Carbon Atom C(3P) + Vinyl Radical C2H3(2A’) Reaction and
Thermochemistry of C3Hn (n = 14) Species. The Journal of Physical Chemistry A,
105(13):3284–3299, April 2001.
http://dx.doi.org/10.1021/jp003224c
