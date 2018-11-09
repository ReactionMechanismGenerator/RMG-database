#!/usr/bin/env python
# encoding: utf-8

name = "USC-Mech-ii"
shortDesc = u"USC Mech Version II. High-Temperature Combustion Reaction Model of H2/CO/C1-C4 Compounds."
longDesc = u"""
Downloaded from http://ignis.usc.edu/Mechanisms/USC-Mech%20II/USC_Mech%20II.htm in August 2013.
Imported into RMG format by Richard West <r.west@neu.edu> using the importChemkin.py script
in the RMG-Py project at commit 2d82cddaac009e61cb15b5014474b6c6a09c9800.

Citation
========
Hai Wang, Xiaoqing You, Ameya V. Joshi, Scott G. Davis, Alexander Laskin, Fokion Egolfopoulos & Chung K. Law,
USC Mech Version II. High-Temperature Combustion Reaction Model of H2/CO/C1-C4 Compounds.
http://ignis.usc.edu/USC_Mech_II.htm, May 2007.

Abstract
========

This  H2/CO/C1-C4 kinetic model (111 species and 784 reactions), applicable to a wide variety
of combustion scenarios, incorporates the recent thermodynamic, kinetic, and species transport
updates relevant to high-temperature oxidation of hydrogen, carbon monoxide, and C1-C4 hydrocarbons.
This model was developed on the basis of

 * an optimized reaction model of H2/CO combustion
 * GRI-Mech1.2 and 3.0
 * a comprehensive reaction model of ethylene and acetylene combustion
 * reaction mechanism of C3 fuel combustion
 * 1,3-Butadiene oxidation at high temperatures.

Also, the rate parameters of CO+OH, OH+HO2 and CO+HO2 were updated from more recent studies.
Rate parameters of several C1 and C2 reactions were reevaluated.  The oxidation model of benzene
and toluene is included.

The reaction model was subject to validation tests against reliable H2/CO/C1-C4 combustion data.
"""
entry(
    index = 0,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186""",
    longDesc = 
u"""
120186
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[Ar]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 1,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44485e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""121286""",
    longDesc = 
u"""
121286
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N#N
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 2,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,7.05333e-13,-1.99592e-15,2.30082e-18,-9.27732e-22,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,-2.30843e-11,1.61562e-14,-4.73515e-18,4.98197e-22,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
[H]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 3,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.56942,-8.59741e-05,4.19485e-08,-1.00178e-11,1.22834e-15,29217.6,4.78434], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/90""",
    longDesc = 
u"""
L 1/90.
[O]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 4,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12531,-0.00322545,6.52765e-06,-5.79854e-09,2.06237e-12,3381.54,-0.690433], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86473,0.0010565,-2.59083e-07,3.05219e-11,-1.33196e-15,3718.86,5.70164], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""S 9/01""",
    longDesc = 
u"""
S 9/01.
[OH]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 5,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 5/89""",
    longDesc = 
u"""
L 5/89.
[O]O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 6,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.33728,-4.94025e-05,4.99457e-07,-1.79566e-10,2.00255e-14,-950.159,-3.20502], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""TPIS78""",
    longDesc = 
u"""
TPIS78.
[H][H]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 7,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.00203643,6.5204e-06,-5.48797e-09,1.77198e-12,-30293.7,-0.849032], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.03399,0.00217692,-1.64073e-07,-9.7042e-11,1.68201e-14,-30004.3,4.96677], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/89""",
    longDesc = 
u"""
L 8/89.
O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 8,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27611,-0.000542822,1.67336e-05,-2.15771e-08,8.62454e-12,-17702.6,3.43505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.165,0.00490832,-1.90139e-06,3.71186e-10,-2.87908e-14,-17861.8,2.91616], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
OO
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 9,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.28254,0.00148309,-7.57967e-07,2.09471e-10,-2.16718e-14,-1088.46,5.45323], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""TPIS89""",
    longDesc = 
u"""
TPIS89.
[O][O]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 10,
    label = "C(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85443.9,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49267,4.79889e-05,-7.24335e-08,3.74291e-11,-4.87278e-15,85451.3,4.8015], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L11/88""",
    longDesc = 
u"""
L11/88.
[C]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 11,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48982,0.000323836,-1.68899e-06,3.16217e-09,-1.40609e-12,70797.3,2.08401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87846,0.000970914,1.44446e-07,-1.30688e-10,1.76079e-14,71012.4,5.48498], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""TPIS79""",
    longDesc = 
u"""
TPIS79.
[CH]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 12,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76268,0.000968872,2.7949e-06,-3.85091e-09,1.68742e-12,46004,1.56253], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.8741,0.00365639,-1.40895e-06,2.6018e-10,-1.87728e-14,46263.6,6.17119], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L S/93""",
    longDesc = 
u"""
L S/93.
[CH2]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 13,
    label = "CH2*",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1986,-0.00236661,8.23296e-06,-6.68816e-09,1.94315e-12,50496.8,-0.769119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.29204,0.00465589,-2.01192e-06,4.17906e-10,-3.39716e-14,50926,8.6265], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L S/93""",
    longDesc = 
u"""
L S/93.
singlet[CH2]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 14,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67359,0.00201095,5.73022e-06,-6.87117e-09,2.54386e-12,16445,1.60456], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.28572,0.0072399,-2.98714e-06,5.95685e-10,-4.67154e-14,16775.6,8.48007], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L11/89""",
    longDesc = 
u"""
L11/89.
[CH3]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 15,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14988,-0.013671,4.91801e-05,-4.84743e-08,1.66694e-11,-10246.6,-4.6413], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0748515,0.0133909,-5.73286e-06,1.22293e-09,-1.01815e-13,-9468.34,18.4373], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 16,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22119,-0.00324393,1.37799e-05,-1.33144e-08,4.33769e-12,3839.56,3.39437], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.77217,0.00495696,-2.48446e-06,5.89162e-10,-5.33509e-14,4011.92,9.79834], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L12/89""",
    longDesc = 
u"""
L12/89.
[CH]=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 17,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14309,0.602813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76069,0.0092,-4.42259e-06,1.00641e-09,-8.83856e-14,-13995.8,13.6563], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
C=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 18,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU1/03""",
    longDesc = 
u"""
IU1/03.
C[O]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 19,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU2/03""",
    longDesc = 
u"""
IU2/03.
[CH2]O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 20,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.7154,-0.0152309,6.52441e-05,-7.10807e-08,2.61353e-11,-25642.8,-1.5041], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.78971,0.0140938,-6.36501e-06,1.38171e-09,-1.1706e-13,-25374.9,14.5024], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
CO
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 21,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.71519,0.00206253,-9.98826e-07,2.30053e-10,-2.03648e-14,-14151.9,7.81869], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""TPIS79""",
    longDesc = 
u"""
TPIS79.
[C]=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 22,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35677,0.0089846,-7.12356e-06,2.45919e-09,-1.437e-13,-48372,9.90105], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.85746,0.00441437,-2.21481e-06,5.2349e-10,-4.72084e-14,-48759.2,2.27164], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
O=C=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 23,
    label = "C2O",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86486,0.0119902,-1.83624e-05,1.57697e-08,-5.38975e-12,33749.9,8.88678], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.15127,0.00237267,-7.6136e-07,1.17064e-10,-7.02578e-15,33241.9,-2.21831], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RUS 79""",
    longDesc = 
u"""
RUS 79.
[C]#C[O]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 24,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88966,0.01341,-2.8477e-05,2.94791e-08,-1.09332e-11,66839.4,6.22296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16781,0.00475222,-1.83787e-06,3.0419e-10,-1.77233e-14,67121.1,6.63589], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""
L 1/91.
[C]#C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 25,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.808681,0.0233616,-3.55172e-05,2.80152e-08,-8.50073e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14757,0.00596167,-2.37295e-06,4.67412e-10,-3.61235e-14,25936,-1.23028], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""
L 1/91.
C#C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 26,
    label = "H2CC",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28155,0.00697648,-2.38552e-06,-1.21044e-09,9.81895e-13,48621.8,5.92039], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.27803,0.00475628,-1.6301e-06,2.54628e-10,-1.48864e-14,48316.7,0.640237], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L12/89""",
    longDesc = 
u"""
L12/89.
singlet [C]=C
Imported from USC-Mech ii thermdat.txt.
Corrected from Triplet to Singlet state:
    Reactions of this species in USC-Mech ii correspond to what RMG would think of
    as the triplet, but this thermochemistry is definitely that of the singlet, which
    is roughly 200kJ/mol more stable.
""",
)

entry(
    index = 27,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21247,0.00151479,2.59209e-05,-3.57658e-08,1.47151e-11,34859.8,8.51054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.01672,0.0103302,-4.68082e-06,1.01763e-09,-8.62607e-14,34612.9,7.78732], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 2/92""",
    longDesc = 
u"""
L 2/92.
[CH]=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 28,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9592,-0.00757052,5.7099e-05,-6.91589e-08,2.69884e-11,5089.78,4.09733], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.03611,0.0146454,-6.71078e-06,1.47223e-09,-1.25706e-13,4939.89,10.3054], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""
L 1/91.
C=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 29,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30647,-0.00418659,4.97143e-05,-5.99127e-08,2.30509e-11,12841.6,4.70721], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.95466,0.0173973,-7.98207e-06,1.75218e-09,-1.49642e-13,12857.5,13.4624], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L12/92""",
    longDesc = 
u"""
L12/92.
[CH2]C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 30,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29142,-0.00550154,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.07188,0.0216853,-1.00256e-05,2.21412e-09,-1.90003e-13,-11426.4,15.1156], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 31,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25172,0.017655,-2.37291e-05,1.72758e-08,-5.06648e-12,20059.4,12.4904], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62821,0.00408534,-1.59345e-06,2.86261e-10,-1.94078e-14,19327.2,-3.93026], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""SRIC91""",
    longDesc = 
u"""
SRIC91
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 32,
    label = "HCCOH",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24237,0.0310722,-5.08669e-05,4.31371e-08,-1.40146e-11,8031.61,13.8743], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92383,0.00679236,-2.56586e-06,4.49878e-10,-2.99401e-14,7264.63,-7.60177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""SRI91""",
    longDesc = 
u"""
SRI91
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CO
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 33,
    label = "CH2CO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13584,0.0181189,-1.73947e-05,9.34398e-09,-2.01458e-12,-7270,12.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5113,0.0090036,-4.1694e-06,9.23346e-10,-7.94838e-14,-7778.5,0.632247], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""D05/90""",
    longDesc = 
u"""
D05/90.
C=C=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 34,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16343,-0.000232616,3.42678e-05,-4.41052e-08,1.72756e-11,-2657.45,7.34683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.94477,0.00786672,-2.88659e-06,4.72709e-10,-2.85999e-14,-3787.31,-5.01368], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 9/92""",
    longDesc = 
u"""
T 9/92.
C[C]=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 35,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40906,0.0107386,1.89149e-06,-7.15858e-09,2.86739e-12,62,9.57145], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.97567,0.00813059,-2.74362e-06,4.0703e-10,-2.17602e-14,-969.5,-5.03209], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""D05/83""",
    longDesc = 
u"""
D05/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 36,
    label = "CH2OCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.383961,0.023879,-1.24676e-05,-1.76864e-09,2.81424e-12,18836.2,25.7417], Tmin=(298,'K'), Tmax=(500,'K')),
            NASAPolynomial(coeffs=[4.49941,0.0115526,-4.81441e-06,8.92349e-10,-5.68706e-14,17474,0.339255], Tmin=(500,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""A12/04""",
    longDesc = 
u"""
A12/04
Low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
[CH]1CO1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 37,
    label = "CH3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
CC=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 38,
    label = "CH2OCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75905,-0.00944122,8.03097e-05,-1.00808e-07,4.00399e-11,-7560.81,7.84975], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.48876,0.0120462,-4.33369e-06,7.00283e-10,-4.19491e-14,-9180.43,-7.07996], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""T 6/92""",
    longDesc = 
u"""
T 6/92
Low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
C1CO1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 39,
    label = "C3H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u1 p0 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,40105.8,15.2059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,38908.7,-12.5848], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/97""",
    longDesc = 
u"""
T 5/97.
C#C[CH2]
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 40,
    label = "pC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68039,0.0157997,2.50706e-06,-1.36576e-08,6.61543e-12,20802.4,9.87694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02524,0.0113365,-4.02234e-06,6.43761e-10,-3.82996e-14,19620.9,-8.60438], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 2/90""",
    longDesc = 
u"""
T 2/90.
C#CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 41,
    label = "aC3H4",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61304,0.0121226,1.85399e-05,-3.45251e-08,1.53351e-11,21541.6,10.2261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31687,0.0111337,-3.96294e-06,6.35642e-10,-3.78755e-14,20117.5,-10.9958], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 8/89""",
    longDesc = 
u"""
L 8/89.
C=C=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 42,
    label = "cC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.024621,0.0231972,-1.84744e-06,-1.59276e-08,8.68462e-12,32334.1,22.7298], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.69999,0.0103574,-3.45512e-06,5.06529e-10,-2.66823e-14,30199.1,-13.3788], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T12/81""",
    longDesc = 
u"""
T12/81
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1=CC1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 43,
    label = "aC3H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36318,0.0198138,1.24971e-05,-3.33556e-08,1.58466e-11,19245.6,17.1732], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.50079,0.0143247,-5.67816e-06,1.10808e-09,-9.03639e-14,17482.4,-11.2431], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""PD5/98""",
    longDesc = 
u"""
PD5/98
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 44,
    label = "CH3CCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73292,0.0223946,-5.14906e-06,-6.75965e-09,3.82532e-12,29040.5,16.5689], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42555,0.0155111,-5.66784e-06,7.92244e-10,-1.6878e-14,27843,-3.35272], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""PD5/98""",
    longDesc = 
u"""
PD5/98
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 45,
    label = "CH3CHCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.913729,0.0264323,-1.1759e-05,-2.30357e-09,2.77155e-12,30916.9,19.9893], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.37253,0.0157805,-5.99229e-06,9.30897e-10,-3.6551e-14,29614.8,-3.41865], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""PD5/98""",
    longDesc = 
u"""
PD5/98
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 46,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49331,0.0209252,4.48679e-06,-1.66891e-08,7.15815e-12,1074.83,16.1453], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.73226,0.0149083,-4.9499e-06,7.21202e-10,-3.7662e-14,-923.57,-13.3133], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""120186""",
    longDesc = 
u"""
120186
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 47,
    label = "nC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.04912,0.026009,2.35425e-06,-1.95951e-08,9.37202e-12,10312.3,21.136], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.70975,0.0160315,-5.27202e-06,7.58884e-10,-3.88627e-14,7976.22,-15.5153], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""P11/94""",
    longDesc = 
u"""
P11/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 48,
    label = "iC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44492,0.0209991,7.70362e-06,-1.84763e-08,7.1283e-12,9422.37,20.1163], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.51927,0.0172201,-5.73642e-06,8.41307e-10,-4.45659e-14,7322.72,-9.08302], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""P11/94""",
    longDesc = 
u"""
P11/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 49,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.928511,0.0264606,6.03324e-06,-2.1915e-08,9.49615e-12,-14057.9,19.2255], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.52442,0.0188983,-6.2921e-06,9.21615e-10,-4.86845e-14,-16564.4,-17.8384], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""P11/94""",
    longDesc = 
u"""
P11/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 50,
    label = "CH2CHCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31358,0.0282531,-2.57378e-05,1.22227e-08,-2.13534e-12,9521.35,14.1051], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.33387,0.0114019,-4.56964e-06,7.9431e-10,-4.41631e-14,8309.49,-11.0199], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C[C]=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 51,
    label = "C2H3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.27135,0.0262311,-9.29123e-06,-4.78373e-09,3.34805e-12,-9335.73,19.4981], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.81119,0.0171143,-7.48342e-06,1.42522e-09,-9.17468e-14,-10784.1,-4.8588], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 52,
    label = "CH3CHOCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.487338,0.0285197,3.00962e-06,-2.26526e-08,1.07067e-11,-12556.4,22.6053], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.69006,0.016021,-5.39718e-06,7.99415e-10,-4.26564e-14,-15420.7,-22.485], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""T 6/92""",
    longDesc = 
u"""
T 6/92
Low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
CC1CO1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 53,
    label = "CH3CH2CHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.72557,0.023236,2.97407e-06,-1.66134e-08,7.42501e-12,-24556.7,14.1663], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.26374,0.0199763,-7.61951e-06,1.16871e-09,-4.196e-14,-25886,-5.77865], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 54,
    label = "CH3COCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.55579,-0.00283654,7.05689e-05,-8.78105e-08,3.40283e-11,-28113.3,2.32266], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.2976,0.0175662,-6.31705e-06,1.02031e-09,-6.1094e-14,-29817.7,-12.757], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/92""",
    longDesc = 
u"""
T 5/92.
CC(C)=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 55,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0544,0.041627,-6.58718e-05,5.32571e-08,-1.66832e-11,54185.2,14.8666], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.15763,0.00554305,-1.35916e-06,1.87801e-11,2.31895e-14,52588,-23.7115], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""D11/99""",
    longDesc = 
u"""
D11/99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 56,
    label = "nC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.816677,0.0387162,-4.80457e-05,3.20668e-08,-8.56282e-12,64455.8,19.7405], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.80457,0.0107124,-4.19391e-06,7.04463e-10,-3.62713e-14,62987.8,-14.1297], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC#C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 57,
    label = "iC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72215,0.0259575,-2.63563e-05,1.55089e-08,-3.80406e-12,58837.1,7.56372], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.65385,0.0112041,-4.64013e-06,8.67866e-10,-5.74306e-14,57954.4,-11.7565], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#C[C]=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 58,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.58857,0.0365467,-3.4107e-05,1.66526e-08,-3.00646e-12,33359.5,20.6579], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.25396,0.0139141,-5.29322e-06,8.34805e-10,-3.51979e-14,31766,-12.6295], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 59,
    label = "nC4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.226113,0.0367424,-2.21205e-05,1.43901e-09,2.64358e-12,42428.4,24.0664], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.40873,0.0177527,-7.56015e-06,1.42038e-09,-9.11002e-14,40438.8,-13.15], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 60,
    label = "iC4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.113081,0.0409506,-3.54136e-05,1.5531e-08,-2.33551e-12,36383.4,23.6925], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.9646,0.0182743,-7.81337e-06,1.52922e-09,-1.09205e-13,34725.1,-10.6493], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 61,
    label = "C4H5-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {4,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96963,0.0244422,-9.12514e-06,-4.24669e-18,1.63047e-21,35503.3,12.0361], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.5382,-0.00856771,2.35595e-05,-1.36764e-08,2.44369e-12,33259.1,-45.3695], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H6W/94""",
    longDesc = 
u"""
H6W/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C#CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 62,
    label = "c-C4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {4,S} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.63976,0.0415492,-2.1921e-05,-4.6559e-09,6.13489e-12,35373.8,35.7018], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.74672,0.017283,-6.51686e-06,9.89176e-10,-3.46049e-14,32808.4,-12.9129], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""PUPM3""",
    longDesc = 
u"""
PUPM3
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]1C=CC1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 63,
    label = "C4H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.112845,0.034369,-1.11074e-05,-9.21067e-09,6.20652e-12,11802.3,23.09], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.86731,0.0149187,-3.15487e-06,-4.18413e-10,1.57613e-13,9133.85,-23.3282], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H6W/94""",
    longDesc = 
u"""
H6W/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 64,
    label = "C4H612",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.02347,0.0349592,-2.2009e-05,6.94227e-09,-7.87919e-13,18118,19.7507], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8156,-0.0042575,1.05118e-05,-4.47384e-09,5.84814e-13,12673.4,-69.8266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""A 8/83""",
    longDesc = 
u"""
A 8/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 65,
    label = "C4H6-2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13733,0.0264862,-9.05687e-06,-5.53864e-19,2.12819e-22,15710.9,13.5294], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.03381,0.00821245,7.1754e-06,-5.88343e-09,1.03439e-12,14335.1,-20.9858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""A 8/83""",
    longDesc = 
u"""
A 8/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC#CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 66,
    label = "C4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.744494,0.0396789,-2.28981e-05,2.1353e-09,2.30964e-12,22653.3,23.4379], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.01348,0.0226346,-9.25455e-06,1.68079e-09,-1.04086e-13,20955,-8.88931], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 67,
    label = "iC4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.03759,0.0455667,-3.04762e-05,7.11026e-09,9.96857e-13,14896.5,29.8637], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14859,0.0221897,-8.44002e-06,1.31334e-09,-5.16179e-14,12712.3,-12.1312], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=C)C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 68,
    label = "C4H81",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18114,0.0308534,5.08652e-06,-2.46549e-08,1.11102e-11,-1790.4,21.0625], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.05358,0.0343505,-1.58832e-05,3.30897e-09,-2.5361e-13,-2139.72,15.5432], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T 6/83""",
    longDesc = 
u"""
T 6/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 69,
    label = "C4H82",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.25943,0.0278084,8.70139e-06,-2.44022e-08,9.89777e-12,-2964.77,20.5011], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.827977,0.0358645,-1.66345e-05,3.47328e-09,-2.66574e-13,-3052.1,21.3425], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T 6/83""",
    longDesc = 
u"""
T 6/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 70,
    label = "iC4H8",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64714,0.025903,8.19854e-06,-2.21933e-08,8.89586e-12,-4037.31,12.6764], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.46095,0.0296115,-1.30771e-05,2.65719e-09,-2.01347e-13,-5006.68,1.06715], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T 6/83""",
    longDesc = 
u"""
T 6/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 71,
    label = "pC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2087,0.0382975,-7.26605e-06,-1.54285e-08,8.68594e-12,7322.1,22.1693], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.68224,0.0236911,-7.59489e-06,6.64271e-10,5.48451e-14,4964.41,-17.8917], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 72,
    label = "sC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.6457,0.00793132,7.0027e-05,-9.59733e-08,3.86289e-11,6234.12,7.96428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.80573,0.0236304,-8.45647e-06,1.36126e-09,-8.13132e-14,3794.12,-19.9968], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T07/95""",
    longDesc = 
u"""
T07/95.
C[CH]CC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 73,
    label = "iC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.975279,0.0416138,-1.44673e-05,-9.38524e-09,6.87974e-12,6668.83,21.2776], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.49817,0.0246895,-8.64876e-06,1.07793e-09,-6.43406e-16,4428.82,-18.4414], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 74,
    label = "tC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.961676,0.0257359,1.5609e-05,-2.66565e-08,8.9418e-12,4656.44,24.8054], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.66073,0.0238794,-8.08904e-06,1.20575e-09,-6.50098e-14,1620.76,-14.8003], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""P11/94""",
    longDesc = 
u"""
P11/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 75,
    label = "C4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56854,0.0346523,6.81681e-06,-2.79951e-08,1.23077e-11,-17130,17.908], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5268,0.0235907,-7.85225e-06,1.14484e-09,-5.98277e-14,-20479.2,-32.1986], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""P11/94""",
    longDesc = 
u"""
P11/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 76,
    label = "iC4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.541095,0.0378603,5.54598e-06,-3.05001e-08,1.40334e-11,-17977.6,21.1509], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8462,0.0233384,-7.7834e-06,1.13938e-09,-5.99183e-14,-21669.9,-35.8706], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""P11/94""",
    longDesc = 
u"""
P11/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 77,
    label = "H2C4O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18119,0.0298408,-3.28324e-05,2.06318e-08,-5.42006e-12,24125.6,9.42101], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.42922,0.0105027,-4.20668e-06,7.11849e-10,-3.57966e-14,22907.8,-16.512], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=C=C=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 78,
    label = "C4H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,D} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {1,D} {4,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.847469,0.0131774,5.99736e-05,-9.71563e-08,4.22734e-11,-5367.85,21.4945], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.38935,0.0140291,-5.07755e-06,8.24137e-10,-4.9532e-14,-8682.42,-27.9163], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T03/97""",
    longDesc = 
u"""
T03/97.
c1ccoc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 79,
    label = "CH2CHCHCHO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  O u0 p2 c0 {4,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21087,0.0352059,-1.09391e-05,-1.17206e-08,7.61749e-12,2266.57,20.6135], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.30106,0.0199453,-8.29038e-06,1.51008e-09,-9.15812e-14,157.884,-16.9106], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CC=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 80,
    label = "CH3CHCHCO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.30535,0.0157494,2.16239e-05,-3.66078e-08,1.49325e-11,5758.86,4.20435], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76082,0.0200318,-8.0631e-06,1.33614e-09,-6.23084e-14,4570.83,-11.0956], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""USC/07""",
    longDesc = 
u"""
USC/07
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[C]=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 81,
    label = "C2H3CHOCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.797985,0.0344034,-1.24599e-05,-5.18063e-18,1.9936e-21,-648.928,21.8897], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-4.72093,0.0391414,-6.52873e-06,-7.68209e-09,2.51473e-12,1753.52,51.719], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""A 8/83""",
    longDesc = 
u"""
A 8/83
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC1CO1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 82,
    label = "C4H6O23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-10278.8,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-13239.3,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T 3/97""",
    longDesc = 
u"""
T 3/97.
C1=COCC1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 83,
    label = "CH3CHCHCHO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55578,0.0409641,-1.69869e-05,-6.00928e-18,2.31369e-21,-14139.5,37.4708], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.8795,-0.0209131,4.45361e-05,-2.60375e-08,4.86836e-12,-19527.9,-68.72], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""T 5/92""",
    longDesc = 
u"""
T 5/92
Low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
CC=CC=O
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 84,
    label = "C4H6O25",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {1,S} {3,D} {11,S}
5  O u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-14657.2,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-17617.7,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""T 3/97""",
    longDesc = 
u"""
T 3/97.
C1=CCOC1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 85,
    label = "C5H4O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.264576,0.0334874,1.67738e-06,-2.96207e-08,1.54431e-11,5111.59,23.541], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0807,0.0161143,-5.83315e-06,9.46759e-10,-5.68972e-14,1943.65,-29.4522], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 8/99""",
    longDesc = 
u"""
T 8/99.
O=C1C=CC=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 86,
    label = "C5H5O(1,3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u1 p0 c0 {1,S} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {3,S} {4,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.9567,0.0558519,-3.72416e-05,4.16244e-09,3.9272e-12,4857.32,38.6767], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.24314,0.0222013,-9.31059e-06,1.71552e-09,-1.0614e-13,1590.84,-24.0877], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""DU0997""",
    longDesc = 
u"""
DU0997
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C1C=C[CH]C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 87,
    label = "C5H5O(2,4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.07776,0.0525817,-2.88565e-05,-3.38855e-09,6.33614e-12,25510.5,39.5915], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.54053,0.0229895,-9.54376e-06,1.70616e-09,-9.74594e-14,22263.7,-20.8188], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""D 9/97""",
    longDesc = 
u"""
D 9/97
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]C1C=CC=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 88,
    label = "C5H4OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u1 p0 c0 {1,S} {5,S} {10,S}
4  C u0 p0 c0 {2,S} {5,D} {8,S}
5  C u0 p0 c0 {3,S} {4,D} {9,S}
6  O u0 p2 c0 {1,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28398,0.0490299,-1.35844e-05,-2.92984e-08,1.90821e-11,6373.65,30.8074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3741,0.0151996,-5.45685e-06,8.80945e-10,-5.27493e-14,2203.58,-45.9569], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 8/99""",
    longDesc = 
u"""
T 8/99.
OC1=CC=C[CH]1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 89,
    label = "C5H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.04302,0.0712535,-7.09182e-05,3.86802e-08,-8.78883e-12,-6416.78,48.6171], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.4894,0.0380526,-2.16545e-05,5.92386e-09,-6.27635e-13,-8213.1,7.12481], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HWZD99""",
    longDesc = 
u"""
HWZD99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OC1C=CC=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 90,
    label = "C5H5",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.983498,0.0336515,-1.10542e-07,-3.67434e-08,2.31412e-11,29626,16.5855], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.47439,0.0160127,-6.48231e-09,-3.58197e-09,9.23651e-13,28086,-16.133], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""T12/89""",
    longDesc = 
u"""
T12/89
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]1C=CC=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 91,
    label = "C5H6",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.86109,0.014804,7.21089e-05,-1.13381e-07,4.869e-11,14801.8,21.3535], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.97578,0.0189055,-6.84115e-06,1.10993e-09,-6.66802e-14,11081.7,-32.2095], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 1/90""",
    longDesc = 
u"""
T 1/90.
C1=CCC=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 92,
    label = "lC5H7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.09743,0.061832,-4.87708e-05,1.66964e-08,-7.53349e-13,23683.6,45.1481], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.22465,0.0396013,-2.23456e-05,6.06497e-09,-6.384e-13,22303.4,14.01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HWZD99""",
    longDesc = 
u"""
HWZD99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CC=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 93,
    label = "C6H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {8,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.451,0.0674752,-0.000118099,1.03676e-07,-3.4851e-11,82173.1,17.7041], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.8939,0.00791451,-2.40272e-06,2.43401e-10,3.13832e-15,79832.4,-40.772], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""D11/99""",
    longDesc = 
u"""
D11/99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#CC#C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 94,
    label = "C6H3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {9,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17906,0.0555474,-7.30762e-05,5.20767e-08,-1.5047e-11,85647.3,19.1792], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.81883,0.0279334,-1.78254e-05,5.37025e-09,-6.17076e-13,85188.2,-0.921478], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H6W/94""",
    longDesc = 
u"""
H6W/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC#CC#C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 95,
    label = "l-C6H4",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {7,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,T}
4  C u0 p0 c0 {3,T} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {8,S}
6  C u0 p0 c0 {5,D} {9,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.295902,0.0580533,-6.77668e-05,4.33768e-08,-1.14189e-11,60001.4,22.319], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7152,0.0138397,-4.37654e-06,3.15416e-10,4.6619e-14,57031.1,-39.4646], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H6W/94""",
    longDesc = 
u"""
H6W/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#CC=C
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 96,
    label = "o-C6H4",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,T} {6,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u1 p0 c0 {4,S} {6,S} {9,S}
6  C u1 p0 c0 {1,S} {5,S} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.84542,0.0583916,-4.86448e-05,1.67703e-08,-7.85807e-13,52592.5,40.5871], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.8433,0.0203015,-8.86743e-06,1.72643e-09,-1.1786e-13,49317.1,-24.0143], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""D11/99""",
    longDesc = 
u"""
D11/99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1#CC=C[CH][CH]1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 97,
    label = "C6H5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {7,S}
3  C u0 p0 c0 {1,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  C u0 p0 c0 {2,D} {6,S} {11,S}
6  C u1 p0 c0 {4,D} {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.69315,0.052179,-2.55584e-05,-7.06611e-09,7.5834e-12,39779.6,41.3325], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.59731,0.0222416,-8.72e-06,1.37888e-09,-5.31461e-14,36261,-22.9546], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""D11/99""",
    longDesc = 
u"""
D11/99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1=C[CH]C=CC=1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 98,
    label = "C6H6",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.84377,0.0584276,-2.94859e-05,-6.93904e-09,8.21253e-12,9181.78,43.8898], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.13812,0.0238544,-8.81277e-06,1.2099e-09,-1.82215e-14,5204.35,-29.1157], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""D11/99""",
    longDesc = 
u"""
D11/99
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
c1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 99,
    label = "C6H5CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.481115,0.0385128,3.28615e-05,-7.69727e-08,3.54231e-11,23307,23.5488], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.044,0.0234939,-8.53754e-06,1.38908e-09,-8.36144e-14,18564.2,-51.6656], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T08/90""",
    longDesc = 
u"""
T08/90.
[CH2]c1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 100,
    label = "C6H5CH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {12,S}
5  C u0 p0 c0 {4,D} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  C u0 p0 c0 {2,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61527,0.0210994,8.5366e-05,-1.32611e-07,5.59566e-11,4075.63,20.2822], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.94,0.0266913,-9.68385e-06,1.57386e-09,-9.46636e-14,-697.649,-46.7288], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 6/87""",
    longDesc = 
u"""
L 6/87.
Cc1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 101,
    label = "C6H5C2H",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {9,S}
2  C u0 p0 c0 {1,T} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u0 p0 c0 {6,S} {8,D} {13,S}
8  C u0 p0 c0 {3,S} {7,D} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.2645,0.084511,-7.65978e-05,3.3217e-08,-4.76731e-12,35566.2,46.3788], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[24.0908,0.000782324,1.1454e-05,-6.16205e-09,9.33467e-13,27429.4,-104.996], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H6W/94""",
    longDesc = 
u"""
H6W/94
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#Cc1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 102,
    label = "C6H5O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u1 p0 c0 {4,S} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {2,S} {6,D} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.466204,0.0413444,1.32413e-05,-5.72873e-08,2.89764e-11,4778.58,27.699], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7222,0.0174689,-6.35505e-06,1.03492e-09,-6.23411e-14,287.275,-48.8182], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T05/02""",
    longDesc = 
u"""
T05/02.
O=C1C=C[CH]C=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 103,
    label = "C6H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {5,S} {7,D} {12,S}
7  C u0 p0 c0 {2,S} {6,D} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69565,0.0522713,-7.20241e-06,-3.58596e-08,2.04491e-11,-13284.1,32.5422], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.9121,0.0183781,-6.19831e-06,9.19832e-10,-4.92096e-14,-18375.2,-55.9241], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""L 4/84""",
    longDesc = 
u"""
L 4/84
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
Oc1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 104,
    label = "C6H4O2",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  C u0 p0 c0 {5,S} {8,D} {11,S}
8  C u0 p0 c0 {2,S} {7,D} {12,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.95193,0.0578424,-3.82144e-05,4.63127e-09,3.62967e-12,-17611,29.2395], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7308,0.023615,-1.02346e-05,1.95322e-09,-1.2746e-13,-21085.8,-36.3005], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""PUML96""",
    longDesc = 
u"""
PUML96
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C1C=CC(=O)C=C1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 105,
    label = "C6H5CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {3,S} {7,D} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.02512,0.0615125,-3.16037e-05,-6.97246e-09,7.98351e-12,11255.8,35.7782], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3744,0.0239993,-1.04657e-05,2.16691e-09,-1.8007e-13,6914.78,-44.6592], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = u"""EST/BUR P 1/93""",
    longDesc = 
u"""
EST/BUR P 1/93
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]c1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 106,
    label = "C6H5CHO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u0 p0 c0 {6,S} {8,D} {13,S}
8  C u0 p0 c0 {3,S} {7,D} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.16273,0.0663692,-3.48164e-05,-6.29994e-09,8.58071e-12,-6116.93,40.2317], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.6507,0.0256804,-1.04667e-05,1.94134e-09,-1.34838e-13,-11019.7,-47.9658], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""L 3/86""",
    longDesc = 
u"""
L 3/86
Low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
O=Cc1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 107,
    label = "C6H5CH2OH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {2,S} {7,D} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {13,S}
7  C u0 p0 c0 {4,D} {6,S} {14,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0642,0.0227751,9.59721e-05,-1.50851e-07,6.41758e-11,-14285,18.1483], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2812,0.0272085,-9.85847e-06,1.60122e-09,-9.62781e-14,-19700.5,-59.4187], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 7/87""",
    longDesc = 
u"""
L 7/87.
OCc1ccccc1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 108,
    label = "OC6H4CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  C u0 p0 c0 {4,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {8,S} {14,S}
8  C u1 p0 c0 {2,S} {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.288558,0.0480035,1.8033e-05,-6.17415e-08,2.88526e-11,-689.456,26.7201], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[22.6094,0.00756462,6.59609e-06,-4.71509e-09,8.04091e-13,-8202.52,-97.2925], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = u"""EST/BUR P 1/93""",
    longDesc = 
u"""
EST/BUR P 1/93
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1=CC(=O)C=C[CH]1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 109,
    label = "HOC6H4CH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u0 p0 c0 {4,D} {6,S} {8,S}
4  C u0 p0 c0 {2,S} {3,D} {15,S}
5  C u0 p0 c0 {2,D} {7,S} {12,S}
6  C u0 p0 c0 {3,S} {7,D} {14,S}
7  C u0 p0 c0 {5,S} {6,D} {13,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.422583,0.0455516,3.20125e-05,-8.1122e-08,3.76657e-11,-18202.6,26.0329], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.933,0.0270112,-9.94487e-06,1.62967e-09,-9.85133e-14,-23592.1,-59.7328], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""AVG CRESOL6/87""",
    longDesc = 
u"""
AVG CRESOL6/87.
Cc1cccc(O)c1
Imported from USC-Mech ii thermdat.txt.
""",
)

entry(
    index = 110,
    label = "C6H4CH3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u1 p0 c0 {2,S} {6,S} {12,S}
5  C u0 p0 c0 {3,S} {7,D} {13,S}
6  C u0 p0 c0 {4,S} {7,D} {14,S}
7  C u0 p0 c0 {5,D} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.14159,0.0567231,-8.68851e-06,-3.42496e-08,1.92669e-11,35738.5,39.7428], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.6155,0.0274318,-1.08993e-05,1.86418e-09,-1.01916e-13,31209.3,-38.9946], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
    ),
    shortDesc = u"""P 1/93""",
    longDesc = 
u"""
P 1/93
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC1=CC=C=C[CH]1
Imported from USC-Mech ii thermdat.txt.
""",
)

