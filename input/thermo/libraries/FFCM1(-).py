#!/usr/bin/env python
# encoding: utf-8

name = "FFCM1(-)"
shortDesc = u""
longDesc = u"""
Foundational Fuel Chemistry Model Version 1.0 (excited species removed)
http://web.stanford.edu/group/haiwanglab/FFCM1/pages/FFCM1.html

FFCM-1
H2/CO/C1 reaction model - Chemkin form - version v1.0c 
Release date: 05/31/3016.

G. P. Smith, Y. Tao, and H. Wang, Foundational Fuel Chemistry Model Version 1.0 (FFCM-1),
http://nanoenergy.stanford.edu/ffcm1, 2016.

Species that were not included:
OH*               ATcT AO   1H   1    0    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 2.75582920E+00 1.39848756E-03-4.19428493E-07 6.33453282E-11-3.56042218E-15    2! OH A 2Sigma+ (excited)
 5.09751756E+04 5.62581429E+00 3.46084428E+00 5.01872172E-04-2.00254474E-06    3! CAS: 3352-57-6 (?)
 3.18901984E-09-1.35451838E-12 5.07349466E+04 1.73976415E+00 5.17770741E+04    4! Uncertainty unknown => -1.0
CH*               EG4/09C   1H   1    0    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 2.78220752E+00 1.47246754E-03-4.63436227E-07 7.32736021E-11-4.19705404E-15    2! CH A2Delta  excited state only
 1.04547060E+05 5.17421018E+00 3.47250101E+00 4.26443626E-04-1.95181794E-06    3! CAS: 3315-37-5
 3.51755043E-09-1.60436174E-12 1.04334869E+05 1.44799533E+00 1.05378099E+05    4! Uncertainty unknown => -1.0
CH2*              IU3/03C   1H   2    0    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 3.13501686E+00 2.89593926E-03-8.16668090E-07 1.13572697E-10-6.36262835E-15    2! Methylene radical excited 
 5.05040504E+04 4.06030621E+00 4.19331325E+00-2.33105184E-03 8.15676451E-06    3! CAS 2465-56-7
-6.62985981E-09 1.93233199E-12 5.03662246E+04-7.46734310E-01 5.15724919E+04    4! 429.039 +- 0.14 kJ/mol ATcT 31.01.2011 
HOCO              ATcT/AC   1O   2H   1    0G   200.000  6000.000              1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 5.39206152E+00 4.11221455E-03-1.48194900E-06 2.39875460E-10-1.43903104E-14    2! Carboxyl radical 
-2.38606717E+04-2.23529091E+00 2.92207919E+00 7.62453859E-03 3.29884437E-06    3! CAS 2564-86-5
-1.07135205E-08 5.11587057E-12-2.30281524E+04 1.12925886E+01-2.18076591E+04    4! -181.32+/-2.3 kJ/mol ATcT 31.01.201111
CH3O2             T04/10C   1H   3O   2    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 5.55530486E+00 9.12236137E-03-3.23851661E-06 5.18713798E-10-3.08834151E-14    2! Methylperoxide radical
-1.03569402E+03-3.99158547E+00 4.97169544E+00-5.29356557E-03 4.77334149E-05    3! CAS: 2143-58-0
-5.77065617E-08 2.22219969E-11-1.29022161E+02 2.81501182E+00 1.43618036E+03    4! 12.055 +- 0.9 kJ/mol AtcT 10-05-2012
CH3O2H            A 7/05C   1H   4O   2    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 7.76538058E+00 8.61499712E-03-2.98006935E-06 4.68638071E-10-2.75339255E-14    2! Methylperoxide
-1.82979984E+04-1.43992663E+01 2.90540897E+00 1.74994735E-02 5.28243630E-06    3! CAS: 3031-73-0
-2.52827275E-08 1.34368212E-11-1.68894632E+04 1.13741987E+01-1.52423685E+04    4! 12.055 +- 0.9 kJ/mol AtcT 10-05-2012
C2H5OH            L 8/88C   2H   6O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012  
 0.65624365E+01 0.15204222E-01-0.53896795E-05 0.86225011E-09-0.51289787E-13    2! Ethanol
-0.31525621E+05-0.94730202E+01 0.48586957E+01-0.37401726E-02 0.69555378E-04    3! CAS: 64-17-5
-0.88654796E-07 0.35168835E-10-0.29996132E+05 0.48018545E+01-0.28257829E+05    4! -234.56 +- 0.2 kJ/mol ATcT 10.05.2012
CH3OCH3           T03/10C   2H   6O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 5.64844274E+00 1.63381875E-02-5.86802189E-06 9.46836384E-10-5.66504295E-14    2! Dimethyl ether
-2.50864216E+04-5.96267354E+00 5.30562273E+00-2.14253958E-03 5.30873092E-05    3! CAS: 115-10-6
-6.23146897E-08 2.30730916E-11-2.39655820E+04 7.13244569E-01-2.21221696E+04    4! -184.02 +-0.43 kJ/mol ATcT 10.05.2012
CH2CH2OH          T05/11C   2H   5O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 7.01348674E+00 1.20204391E-02-4.21992012E-06 6.70675981E-10-3.97135273E-14    2! 2-Hydroxylethyl
-6.16161779E+03-8.62052409E+00 4.20954137E+00 9.12964578E-03 2.47462263E-05    3! CAS: 4422-54-2
-3.92945764E-08 1.66541312E-11-4.91511371E+03 8.30445413E+00-3.10541451E+03    4! -25.82+- 0.6 kJ/mol ATcT 10.05.2012
CH3CHOH           T06/11C   2H   5O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 6.35842302E+00 1.24356276E-02-4.33096839E-06 6.84530381E-10-4.03713238E-14    2! 1-Hydroxylethyl
-9.53018581E+03-6.05106112E+00 4.22283250E+00 5.12174798E-03 3.48386522E-05    3! CAS: 2348-46-1
-4.91943637E-08 2.01183723E-11-8.35622088E+03 8.01675700E+00-6.64945980E+03    4! -54.03 +- 4.0 kJ/mol ATcT 10.05.2012
CH3CH2O           T06/11C   2H   5O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 6.55053877E+00 1.32525511E-02-4.74726060E-06 7.64699226E-10-4.57008357E-14    2! Ethyl oxide radical
-4.47191998E+03-9.61231141E+00 3.26905655E+00 9.33562904E-03 2.96317166E-05    3! CAS: 2154-50-9
-4.53411341E-08 1.88795595E-11-2.95022955E+03 1.04200942E+01-1.37951605E+03    4! -13.6 +-4.0 kJ/mol ATcT 10.05.2012
CH3OCH2           A10/04C   2H   5O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 5.94067593E+00 1.29906358E-02-4.56921036E-06 7.26888932E-10-4.30599587E-14    2! CH2-O-CH3 radical   
-2.58503562E+03-4.52841964E+00 4.53195381E+00 7.81884271E-03 1.94968539E-05    3! CAS: 16520-04-0
-2.74538336E-08 1.06521135E-11-1.70629244E+03 5.06122980E+00 1.15460803E+02    4! -2.8 +- 1.2 kcal/mol ATcT 10.05.2012 (from MacMillen Golden 1982)
CH2OCH2           L 8/88C   2H   4O   1    0G   200.000  6000.000  1000.       1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 0.54887641E+01 0.12046190E-01-0.43336931E-05 0.70028311E-09-0.41949088E-13    2! Oxirane, cyc-(CH2)2O, Ethylene oxide
-0.91804251E+04-0.70799605E+01 0.37590532E+01-0.94412180E-02 0.80309721E-04    3! CAS: 75-21-8
-0.10080788E-06 0.40039921E-10-0.75608143E+04 0.78497475E+01 0.425             4! -52.681 +- 0.425 kJ/mol ATcT 31.01.2011
C2H3OH            T03/10C   2H   4O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 7.49818166E+00 1.03957000E-02-3.66891058E-06 5.85205827E-10-3.47373827E-14    2! Vinyl Alcohol 
-1.81643092E+04-1.38388104E+01 2.28758479E+00 1.97013262E-02 1.96382662E-06    3! CAS: 557-75-5
-1.94389758E-08 1.02616778E-11-1.65373421E+04 1.41333462E+01-1.49958566E+04    4! -28.85+/-2. kcal/mol ATcT 10.05.2012 
C2H3O             A 1/05C   2H   3O   1    0G   200.000  6000.000 1000.        1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 5.60158035E+00 9.17613962E-03-3.28028902E-06 5.27903888E-10-3.15362241E-14    2! Oxirane (ethylene oxide) radical 
 1.71446252E+04-5.47228512E+00 3.58349017E+00-6.02275805E-03 6.32426867E-05    3! 31586-84-2
-8.18540707E-08 3.30444505E-11 1.85681353E+04 9.59725926E+00 1.97814471E+04    4! No ATcT value, G3B3 +- 8 kJ/mol
HCCOH             T12/09C   2H   2O   1    0G   200.000  6000.000   1000.0     1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 6.37509678E+00 5.49429011E-03-1.88136576E-06 2.93803536E-10-1.71771901E-14    2! Ethynol, Hydroxyacetylene
 8.93277676E+03-8.24498007E+00 2.05541154E+00 2.52003372E-02-3.80821654E-05    3! CAS: 32038-79-2
 3.09890632E-08-9.89799902E-12 9.76872113E+03 1.22271534E+01 1.33              4! 92.7 +- 1.33 kJ/mol ATcT 31.01.2011
C2O               T 8/11C   2O   1    0    0G   200.000  6000.000   1000.0     1! Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
 5.42468378E+00 1.85393945E-03-5.17932956E-07 6.77646230E-11-3.53315237E-15    2! Carbon oxide
 4.37161379E+04-3.69608405E+00 2.86278214E+00 1.19701204E-02-1.80851222E-05    3! 12071-23-7 
 1.52777730E-08-5.20063163E-12 4.43125964E+04 8.89759099E+00 1.2               4! 378.86 +/- 1.2 kJ/mol ATcT 31.01.2011
"""
entry(
    index = 1,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Argon
CAS: 7440-37-1
Reference element
""",
)

entry(
    index = 2,
    label = "He",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Helium
CAS: 7440-59-7
Reference element""",
)

entry(
    index = 3,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Nitrogen
CAS:7727-37-9
Reference element
""",
)

entry(
    index = 4,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93287,0.000826608,-1.46402e-07,1.541e-11,-6.88805e-16,-813.066,-1.02433], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Hydrogen
CAS: 1333-74-0
Reference element
""",
)

entry(
    index = 5,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Atomic hydrogen
CAS: 12385-13-6
217.997805 +- 0.000008 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 6,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54364,-2.73162e-05,-4.1903e-09,4.95482e-12,-4.79554e-16,29226,4.92229], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Atomic oxygen
CAS:17778-80-2
249.22916 +- 0.00203 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 7,
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
            NASAPolynomial(coeffs=[3.66096,0.000656366,-1.4115e-07,2.05798e-11,-1.29913e-15,-1215.98,3.41536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Molecular oxygen
CAS: 7782-44-7
Reference element
""",
)

entry(
    index = 8,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198,-0.00240107,4.61664e-06,-3.87916e-09,1.3632e-12,3368.9,-0.103998], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83853,0.00110741,-2.94e-07,4.20699e-11,-2.4229e-15,3697.81,5.84495], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Hydroxyl radical
CAS: 3352-57-6
37.5011 +- 0.0259 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 9,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.0020364,6.52034e-06,-5.48793e-09,1.77197e-12,-30293.7,-0.849009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67704,0.00297318,-7.73769e-07,9.44335e-11,-4.269e-15,-29885.9,6.88255], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Water(v)
CAS: 7732-18-5
-241.8222 +- 0.0259 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 10,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,264.018,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17229,0.00188118,-3.46277e-07,1.94658e-11,1.76257e-16,31.0207,2.95768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Perhydroxyl radical 
CAS: 3170-83-0
12.271 +- 0.157 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 11,
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
            NASAPolynomial(coeffs=[4.31515,-0.000847391,1.76404e-05,-2.26763e-08,9.0895e-12,-17706.7,3.27373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57977,0.00405326,-1.29845e-06,1.98211e-10,-1.13969e-14,-18007.2,0.664971], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 8/03""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Hydrogen peroxide
CAS 7722-84-1
-135.4416 +- 0.0622 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 12,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04849,0.00135173,-4.85794e-07,7.88536e-11,-4.69807e-15,-14266.1,6.0171], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RUS 79""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Carbon monoxide
CAS 630-08-0
-110.525 +- 0.0251 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 13,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Carbon dioxide
CAS 124-38-9
-393.4743 +- 0.014 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 14,
    label = "C",
    molecule = 
"""
multiplicity 5
1 C u4 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85442.7,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60558,-0.000195934,1.06737e-07,-1.64239e-11,8.18706e-16,85411.7,4.19239], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Carbon atom
CAS 7440-44-0
716.8734 +- 0.0555 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 15,
    label = "CH",
    molecule = 
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48976,0.000324322,-1.68998e-06,3.16284e-09,-1.40618e-12,70612.6,2.08428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52094,0.00176536,-4.61477e-07,5.92897e-11,-3.34745e-15,70946.8,7.40518], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU3/03""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methylidyne
CAS 3315-37-5
596.173 +- 0.124 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 16,
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
            NASAPolynomial(coeffs=[3.71758,0.00127391,2.17347e-06,-3.48858e-09,1.65209e-12,45872.4,1.75298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14632,0.00303671,-9.96474e-07,1.50484e-10,-8.57336e-15,46041.3,4.72342], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU3/03""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methylene radical 
CAS 2465-56-7
391.458 +- 0.133 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 17,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19331,-0.00233105,8.15676e-06,-6.62986e-09,1.93233e-12,50366.2,-0.746734], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.13502,0.00289594,-8.16668e-07,1.13573e-10,-6.36263e-15,50504.1,4.06031], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU3/03""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methylene radical excited
CAS 2465-56-7
429.039 +- 0.14 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 18,
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
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU0702""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methyl radical
CAS 2229-07-4
146.4941 +- 0.079 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 19,
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
            NASAPolynomial(coeffs=[5.14911,-0.0136622,4.91454e-05,-4.84247e-08,1.66603e-11,-10246.6,-4.63849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.65326,0.0100263,-3.31661e-06,5.36483e-10,-3.14697e-14,-10009.6,9.90506], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/99""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methane 
CAS 74-82-8
-74.5335 +- 0.0554 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 20,
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
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/03""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Formyl radical  HC=O
CAS 2597-44-6
41.827 +- 0.101 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 21,
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
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14379.2,0.602798], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16953,0.00619321,-2.25056e-06,3.65976e-10,-2.20149e-14,-14548.7,6.04208], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/88""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Formaldehyde
CAS 50-00-0
-109.164 +- 0.101 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 22,
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
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Hydroxymethyl radical
CAS 2597-43-5
-16.097 +- 0.422 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 23,
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
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methoxy radical
CAS 2143-68-2
21.845 +- 0.35 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 24,
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
            NASAPolynomial(coeffs=[5.65851,-0.0162983,6.91938e-05,-7.58373e-08,2.80428e-11,-25612,-0.897331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52727,0.0103179,-3.62893e-06,5.77448e-10,-3.42183e-14,-26002.9,5.16759], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T06/02""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Methanol
CAS 67-56-1
-200.702 +- 0.169 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 25,
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
            NASAPolynomial(coeffs=[2.89868,0.0132988,-2.80733e-05,2.89485e-08,-1.07502e-11,67061.6,6.18548], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6627,0.00382492,-1.36633e-06,2.13455e-10,-1.23217e-14,67168.4,3.92206], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/10""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ethynyl radical
CAS 2122-48-7
567.905 +- 0.163 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 26,
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
            NASAPolynomial(coeffs=[0.80868,0.0233616,-3.55172e-05,2.80153e-08,-8.50075e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65878,0.00488397,-1.60829e-06,2.46975e-10,-1.38606e-14,25759.4,-3.99838], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 1/91""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ethyne, Acetylene
CAS: 74-86-2
228.324 +- 0.142 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 27,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36378,0.000265766,2.79621e-05,-3.72987e-08,1.5159e-11,34475,7.9151], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.15027,0.00754021,-2.62998e-06,4.15974e-10,-2.45408e-14,33856.6,1.72812], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ATcT/A""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Vinyl radical H2C=CH*
CAS: 2669-89-8
297.272 +- 0.454 kJ/mol ATcT 31.01.2011
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
            NASAPolynomial(coeffs=[3.9592,-0.00757051,5.7099e-05,-6.91588e-08,2.69884e-11,5089.78,4.0973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.99183,0.0104834,-3.71721e-06,5.94628e-10,-3.5363e-14,4268.66,-0.269082], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 1/00""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ethene, ethylene
CAS: 74-85-1
52.555 +- 0.142 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 29,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.24186,-0.00356905,4.82667e-05,-5.85401e-08,2.25805e-11,12969,4.44704], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.32196,0.0123931,-4.39681e-06,7.0352e-10,-4.18435e-14,12175.9,0.171104], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU1/07""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ethyl radical CH3CH2
CAS:2025-56-1
119.7 +- 0.7 kJ/mol ATcT 10.05.2012
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
            NASAPolynomial(coeffs=[4.29143,-0.00550155,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04666,0.0153539,-5.47039e-06,8.77827e-10,-5.23168e-14,-12447.3,-0.968698], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 8/88""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ethane
CAS: 74-84-0
-83.775 +- 0.159 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 31,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87608,0.0221205,-3.58869e-05,3.05403e-08,-1.01281e-11,20163.4,13.6968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91479,0.00371409,-1.30137e-06,2.06473e-10,-1.21477e-14,19359.6,-5.50567], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 4/09""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ketenyl radical
CAS: 51095-15-9
177.966 +- 0.585 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 32,
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
            NASAPolynomial(coeffs=[2.13241,0.0181319,-1.74093e-05,9.35336e-09,-2.01725e-12,-7148.09,13.3808], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75871,0.00635124,-2.25955e-06,3.62322e-10,-2.15856e-14,-8085.33,-4.9649], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 4/02""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Ketene H2C=C=O
CAS: 463-51-4
-48.569 +- 0.144 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 33,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66874,0.0096233,1.60617e-05,-2.87682e-08,1.2503e-11,219.438,12.5694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91637,0.0088465,-3.14955e-06,5.05413e-10,-3.01305e-14,-1047.8,-6.1065], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T04/06""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Vinoxy radical, CH2=CH-O
CAS: 6912-06-7
No ATcT value, G3B3 +- 8 kJ/mol
""",
)

entry(
    index = 34,
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
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012 
Acetaldehyde
CAS: 75-07-0
-165.374 +- 0.307 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 35,
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
            NASAPolynomial(coeffs=[4.03587,0.000877295,3.071e-05,-3.92476e-08,1.52969e-11,-2682.07,7.86177], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.31372,0.00917378,-3.32204e-06,5.39475e-10,-3.24524e-14,-3645.04,-1.67576], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU2/03""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
Acetyl radical   CH3-C=O
CAS: 3170-69-2
-9.678+- 0.385 kJ/mol ATcT 31.01.2011
""",
)

entry(
    index = 36,
    label = "H2CC",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u2 p0 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28155,0.00697643,-2.38528e-06,-1.21078e-09,9.82042e-13,48319.2,5.92036], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.27807,0.00475623,-1.63007e-06,2.54623e-10,-1.4886e-14,48014,0.639979], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L12/89""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012 no newer NASA polynom
Vinylidene
CAS: 2143-69-3
kk:1
""",
)

