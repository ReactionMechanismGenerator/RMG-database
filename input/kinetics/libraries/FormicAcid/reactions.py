#!/usr/bin/env python
# encoding: utf-8

name = "FormicAcid"
shortDesc = u"FormicAcid"
longDesc =u"""
This library includes important formic acid related reactions.
If it is calculated by ARC, the level of thoery is CCSD(T)-F12/Aug-cc-pVTZ-F12//b2plypd3/def2tzvp.
Prepared by Alon Grinberg Dana

Notes:
- Consider setting maximumRadicalElectrons = 3 to allow [N] quartet if you're interested in NOx (also allow N2 to be reactive)
- For NOx, the Nitrogen_Dean_and_Bozzelli library should be used conjointly with this one.
- It is reccomended to consider the SOxNOx, NitrogenCurran, SulfurLibrary, thermo_DFT_CCSDTF12_BAC, primaryThermoLibrary,
  CHN, CHON, and BurcatNS thermo libraries for your model generation (in this order)
- Some reactions have different kinetics coefficients reported for different T range,
  'The Low T' rate is reported in the comments. You can also use the "primaryNitrogenLibrary/LowT" sub-library, and give it priority over this library
- This library should be used along with a library which handles well the transition of ground/excited states of small radicals (e.g., FFCM)
- At present (when this library was written) RMG does not differentiate between cis and trans conformers.
  When data was available seperately for the production or consumption of two conformers
  (e.g.: 'A + B <=> cis-X + C' and 'A + B <=> trans-X + C')
  the two rates were summed and reported in this library as a duplicate reaction (using MultiArrhenius, unless otherwise mentioned).
  Such instances are marked with the comment 'conformer-dup'.
- Some excited species were combined with their ground state in this library (e.g.: NCN, CH2NCN).

This library contains the following subsets:
* Thermal NO
* Prompt NO
* N2O Pathway
* NNH Pathway
* NHx Pathway
* N2H4 + N2O4
* CH3NO2
* Thermal de-NOx
* NO2 decomposition
* NOx
* HCN
* C1-oxygenates

Reference legend:
example [Baulch1992a] D.L. Baulch, C.J. Cobos, R.A. Cox, C. Esser, P. Frank, Th. Just, J.A. Kerr, M.J. Philling, J. Troe, R.W. Walker, J. Warnatz, "Evaluated Kinetic Data for Combustion Modelling", Journal of Physical and Chemical Reference Data, 1992, 21(3), 411, doi: 10.1063/1.555908
[Marshall2015] P. Marshall, P. Glarborg, "Ab initio and kinetic modeling studies of formic acid oxidation", Proc. Combust. Inst. 35 (2015) 153-160, https://doi.org/10.1016/j.proci.2014.05.091.
"""

entry(
    index = 01,
    label = "N + NO <=> O + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.29e+13, 'cm^3/(mol*s)','+|-',8.58e+12), n=0, Ea=(1564, 'cal/mol'), T0=(1, 'K'), Tmin=(1400, 'K'), Tmax=(3500, 'K')),
    shortDesc = u"""[Hanson1990b]""",
    longDesc =
u"""
Part of the "Thermal (Zeldovich) NO" mechanism
See [Hanson1990b] R1; p. 856
Uncertainty: +/-20% at 1400 K to +/- 10% at 3500 K
[DeanBozz2000] recommend using [Hanson1990b]'s value, sicne its shock-tube measurements are in close agreement with 5 other studies (see Fig 2.1 in [DeanBozz2000] p. 142)
[GRI] fitted to the data of 3 of the sources in [DeanBozz2000]
Also available in RMG's libraries as:
[DeanBozz2000] *reverse direction given: A = 2e+14 cm^3/(mol*s); n = 0; Ea = 76774 cal/mol
[GlarZha]  A = 2.1e13 cm^3/(mol*s); n = 0; Ea = 0
[GlarGim]  A = 3.3e12 cm^3/(mol*s); n = 0.3; Ea = 0 cal/mol
[GRI]      A = 2.7e13 cm^3/(mol*s); n = 0; Ea = 355 cal/mol
""",
)

entry(
    index = 02,
    label = "CH2(S) + N2 <=> CH2N2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(1.22e+30, 'cm^3/(mol*s)'), n=-7.25, Ea=(2730, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(9.45e+30, 'cm^3/(mol*s)'), n=-7.22, Ea=(2734, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(4.55e+31, 'cm^3/(mol*s)'), n=-7.13, Ea=(2653, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.46e+32, 'cm^3/(mol*s)'), n=-7.13, Ea=(2774, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(7.41e+32, 'cm^3/(mol*s)'), n=-7.21, Ea=(3088, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
            Arrhenius(A=(1.39e+34, 'cm^3/(mol*s)'), n=-7.28, Ea=(3804, 'cal/mol'), T0 = (1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K')),
        ],
    ),
    shortDesc = u"""[Lin2010a]""",
    longDesc =
u"""
Part of the "Prompt NO" mechanism
k1 in [Lin2010a]
T range: 300-3000 K
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index=03,
    label="HOCHO + H <=> HOCO + H2",
    degeneracy=1,
    kinetics=Arrhenius(A=(4.3E+02, 'cm^3/(mol*s)'), n=3.272, Ea=(4858, 'cal/mol'), T0=(1, 'K')),
),

entry(
    index=04,
    label="HOCO + O2 <=> HOC(O)OO",
    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(4.49E-09, 'cm^3/(mol*s)'), n=0.00, Ea=(-17910.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.68E-06, 'cm^3/(mol*s)'), n=0.00, Ea=(-10760.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51E-11, 'cm^3/(mol*s)'), n=0.00, Ea=(-24300.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.70E-12, 'cm^3/(mol*s)'), n=5.21, Ea=(4355.0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.71E+00, 'cm^3/(mol*s)'), n=2.17, Ea=(-2871.0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
),

entry(
    index=1,
    label="HOCHO + H <=> HOCO + H2",
    kinetics=Arrhenius(A=(2.3E+02, 'cm^3/(mol*s)'), n=3.272, Ea=(4860, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2015]""",
    longDesc =
u"""
[Marshall2015], done at the W1Usc level of theory
""",
),

entry(
    index=2,
    label="HOCHO + H <=> OCHO + H2",
    kinetics=Arrhenius(A=(4.2E+05, 'cm^3/(mol*s)'), n=2.25, Ea=(1.4090, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""[Marshall2015]""",
    longDesc =
u"""
[Marshall2015], done at the W1Usc level of theory
""",
),

