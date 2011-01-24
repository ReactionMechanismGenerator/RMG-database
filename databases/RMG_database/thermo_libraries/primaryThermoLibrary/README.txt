primaryThermoLibrary
====================

This thermochemistry library contains thermochemistry of a few small
molecules. Some of them, RMG may otherwise estimate poorly. In some instances
it would be OK estimating via group additivity, but if running with automatic
quantum calculations the calculations are likely to fail.

It is recommended that this library is included in all calculations. (It is
advisable to use a much larger library, as many other small molecules will be
poorly estimated by RMG. This should be considered a bare minimum.)

--

For CO3 isomers:
Data is from the paper by Mebel et al. [1].
Geometries are from Figure 1.
Vibrational frequencies from the supplementary material.
H298 values are derived from the relative energies given in the paper.

For C3Hn species:
Geometries from [2] and frequencies from [3].
H298 values from a mixture of the two.



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
