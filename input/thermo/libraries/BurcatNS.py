#!/usr/bin/env python
# encoding: utf-8

name = "BurcatNS"
shortDesc = u""
longDesc = u"""
Alexander Burcat and Branko Ruscic
"Third Millennium Ideal Gas and Condensed Phase Thermochemical Database for
Combustion with updates from Active Thermochemical Tables" TAE # 960; ANL-50/20
Technion-IIT, Aerospace Engineering, and Argonne National Laboratory, Chemistry
Division, 2005.
http://garfield.chem.elte.hu/Burcat/burcat.html

Thermo data of species relevant for S/N systems which are not already present in other RMG libraries at better levels were taken here.
"""
entry(
    index = 0,
    label = "TrinitroMethane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {11,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S}
5  N u0 p0 c+1 {1,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p3 c-1 {5,S}
8  N u0 p0 c+1 {1,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p3 c-1 {8,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67089,0.0680307,-7.78812e-05,4.43795e-08,-1.00716e-11,-4527.09,25.6726], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.6787,0.0097922,-3.98954e-06,6.90038e-10,-4.30975e-14,-9129.56,-65.3723], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T09/10""",
    longDesc = 
u"""
517-25-9
CH(NO2)3 Tri-Nitro Methane STATWT = 1 SYMNO = 3  IA = 50.830948  IB = 68.4055572
IC = 99.2098743      (Ir(NO2)= 5.96    ROSYM = 2  V(2) = 0.1 kcal/mole)3
NU = 2749,1962,1572,1261,1232,1167,1135,1064,993,884,724,708,670,619,563,490,
449,421,368,347,335,210,170,157. REF= A.BURCAT PM3 JPCRD 28,(1999),63
Moments=Melius HF298=-3.2 kcal  REF=Carpenter et. al. JCED 15,(1970),535   Max
Lst Sq Error Cp @ 1300 K 0.50%
""",
)

entry(
    index = 1,
    label = "CNH2",
    molecule = 
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77102,-0.000848553,1.88163e-05,-2.33774e-08,9.13379e-12,43145.2,5.09399], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.84864,0.00516805,-1.7856e-06,2.80594e-10,-1.64782e-14,42842.2,3.24371], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""triradical  T 2/12""",
    longDesc = 
u"""
35430-17-2
CNH2  triradical  SIGMA=2.  STATWT=2.  IA=0.2456  IB=2.2408  IC=2.4865
Nu=3331.5,3304,1652,1438,1029,718  HF298=368.7+/-1.45 kJ  REF=ATcT C 2011
{HF298=366.7+/-8. kJ  REF=Burcat G3B3}  Max Lst Sq Error Cp @ 6000 K 0.40%.
CNH2  triradical  T 2/12C  1.H  2.N  1.   0.G   200.000  6000.000  B  28.03332 1
""",
)

entry(
    index = 2,
    label = "NH2CO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5364,0.00973407,-3.87293e-07,-5.90128e-09,3.01182e-12,-3096.24,8.47952], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69169,0.00608718,-2.09434e-06,3.28449e-10,-1.92704e-14,-3810.29,-3.2271], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H2N-C*=O  T09/09""",
    longDesc = 
u"""
3858-51-7
CH2NO  H2N-C(*)=O RADICAL   STATWT=2  SIGMA=2  IA=0.6788  IB=7.7562  IC=8.4350
NU=3695,3484,1871,1626,1233,1090,641,521,211.  HF298=-3.225+/-2. kcal REF=Burcat
G3B3   {HF298=-5.57 +/-2.37 kcal  REF= C. Melius Database BAC/MP4 C37;
HF298=-15.1+/-4. kJ  REF=Luo Comprehensive Handbook Chem. Bond Energ. CRC press
2007; HF298=-15.7 kJ REF=Morochkin & Dorofeeva Comp.& Theo Chem. 991,(2012),182}
Max Lst Sq Error Cp @ 6000 K 0.36%.
""",
)

entry(
    index = 3,
    label = "CH2ONO2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 N u0 p0 c+1 {4,S} {6,D} {7,S}
6 O u0 p2 c0 {5,D}
7 O u0 p3 c-1 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.98654,0.0247991,-1.17176e-05,-5.3682e-09,4.80947e-12,10020.3,13.6939], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3914,0.00766104,-3.02728e-06,5.16125e-10,-3.19767e-14,7784.86,-25.4152], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RADICAL   T05/98""",
    longDesc = 
u"""
38082-43-8 ??
*CH2ONO2  METHYL-NITRATE-RADICAL   STATWT = 2  SYMNO = 1  IA = 6.5230882
IB = 16.246015   IC = 22.69382   Ir(NO2) = 5.96  ROSYM = 2  V(2) = 9.1 kcal
Ir(CH2) = 0.345711   ROSYM = 2  V(2) = 2.3 kcal   NU= 3142,3009,1727,1412,
1306,1165,1120,921,766,718,683,608,364.   HF298 = 23.65 kcal
REF = Melius Database 1988 P73BJ  Max Lst Sq Error Cp @ 1300 K 0.56%
""",
)

entry(
    index = 4,
    label = "NH2CN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52226,0.0163678,-1.69373e-05,1.085e-08,-2.97871e-12,14833,10.538], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.34124,0.00632803,-2.16285e-06,3.37451e-10,-1.97201e-14,14145.5,-3.51782], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H2N-CN      T09/09""",
    longDesc = 
u"""
420-04-2
CH2N2  CYANAMIDE H2N-CN  SIGMA=2 STATWT=1    IA=0.2746   IB=8.3336  IC=8.5352
NU =406,484,603,1098,1209,1662,2367,3541,3635  HF298=32.159+/-2. kcal
REF=Burcat  G3B3  {HF298= 32.478+/-4.8 kcal   REF=C. MELIUS, BAC/MP4 Database
N62Z}  Max Lst Sq Error Cp @ 6000 K 0.36%
""",
)

entry(
    index = 5,
    label = "NHCNH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 N u0 p1 c0 {1,D} {4,S}
3 N u0 p1 c0 {1,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7513,0.0185799,-1.40651e-05,2.15779e-09,1.63974e-12,16388.4,13.8507], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.94596,0.0058076,-1.98052e-06,3.0856e-10,-1.80146e-14,15345.5,-7.36413], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Carbodiimi  T09/09""",
    longDesc = 
u"""
151-51-9
CH2N2 CARBODIIMIDE HN=C=NH   SIGMA=2  STATWT=1  IA=0.2286  IB=8.1420  IC=8.1433
NU=3572(2),2242,1290,941,938,748,522.6(2)   HF298=35.009+/-2. kcal  REF=Burcat
G3B3   {HF298=35.613+/-3.56 Kcal  REF=C.MELIUS BAC/MP4 Database N62Y}    Max Lst
Sq Error Cp @ 6000 K 0.33%
""",
)

entry(
    index = 6,
    label = "cCH2NN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01289,-0.00729541,5.24659e-05,-6.47585e-08,2.55023e-11,36709.7,6.07517], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.9494,0.00716065,-2.57368e-06,4.15744e-10,-2.49024e-14,35703.5,-2.6732], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""cyc-CH2-N  T01/07""",
    longDesc = 
u"""
157-22-2
CH2N2 CYCLO DIAZIRINE H2(CN=N)  STATWT=1  SIGMA=2  IA=2.0465   IB=3.5255
IC=4.9876   NU=849,996,1014,1066,1160,1521,1743,3155,3268  HF298=75.374 kcal
REF=Burcat G3B3 calc  {HF298=75.1 kcal  REF=G3X calc;  HF298=76.516+/-4.54 KCAL
REF=MELIUS BAC/MP4 Database N62;  HF298=74.10 kcal   REF=G2 calc Catoire &
Swihart J. Prop & Power 18,(2002),1242}   MAX LST SQ ERROR CP @ 200 K 0.73%
""",
)

entry(
    index = 7,
    label = "cCHNNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {1,D} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17248,0.00253367,2.71936e-05,-3.91007e-08,1.62465e-11,46646.4,9.89092], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40396,0.00665047,-2.36584e-06,3.79549e-10,-2.26261e-14,45593.4,-3.9535], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""c(-CH=N-NH)T01/07""",
    longDesc = 
u"""
157-23-3
CH2N2 1H-Diazirine Cyclo H(-C=N-NH-)  SIGMA=1  STATWT=1  IA=2.1104  IB=3.7455
IC=5.5668  Nu=3324,3234,1804,1372,1194,1045,978,805,554  HF298=95.139 kcal
REF=Burcat G3B3 calc  {HF298=94.36 kcal REF=G2 calc Catoire & Swihart J. Prop &
Power 18,(2002),1242}  Max Lst Sq Error Cp @ 200 K 0.51%.
""",
)

entry(
    index = 8,
    label = "CH2N2O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48959,0.0125272,5.44139e-06,-1.61064e-08,7.36625e-12,25996.1,9.37452], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.26219,0.00787392,-2.85369e-06,4.63521e-10,-2.78698e-14,24651.5,-11.5596], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H2C=N-N=O T05/08""",
    longDesc = 
u"""
90251-09-5
CH2N2O   H2C=N-N=O   SIGMA=2  STATWT=1  Ia=1.5340  Ib=15.3036  Ic=16.7906
Nu=3209,3084,1758,1682,1457,1207,1101,823,700,562,396,74.26  HF298=54.873 kcal
REF=Burcat G3B3 calc.  {HF298=      REF=Pitz and Westbrook Proc. Comb. Inst
31(2),(2007),2343}  Max Lst Sq Error Cp @ 1300 K 0.48%
""",
)

entry(
    index = 9,
    label = "CH2N2O2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p3 c-1 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31412,0.0247488,-1.3686e-05,-1.21679e-09,2.77887e-12,13879.9,15.2896], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.91359,0.00871159,-3.1685e-06,5.13059e-10,-3.0767e-14,11922.7,-19.3937], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H2C=N-N  T05/08""",
    longDesc = 
u"""
647700-85-2
CH2N2O2   H2C=N-NO2  SIGMA=2  STATWT=1  IA=6.9821  IB=16.6633  IC=23.5617
Ir(NO2)=2.3634  ROSYM=2  V(3)=811. cm-1  Nu=3238,3132,1734,1705,1439,1358,1188,
1093,881,838,647,556,526,400  HF298=30.897 kcal  REF=Burcat G3B3 calc.
{HF298=        REF=Pitz and Westbrook Proc. Comb. Inst 31(2),(2007),2343}   Max
Lst Sq Error Cp @ 1300 K 0.48%.
""",
)

entry(
    index = 10,
    label = "CH2N4",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 C u0 p0 c0 {1,S} {4,D} {7,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42186,0.00270901,6.32709e-05,-9.18466e-08,3.85276e-11,37248.8,15.6707], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.56211,0.00942178,-3.42556e-06,5.5813e-10,-3.3647e-14,34595.4,-21.2704], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Cy Tetrazol T 8/14""",
    longDesc = 
u"""
288-94-8
CH2N4 Cy 1H-Tetrazol  SIGMA=1  STATWT=1  IA=7.9934  IB=8.1428  IC=16.1362
Nu=563,690,737,848,969,1011,1046,1069,1151,1273,1300,1466,1518,3311,3654
REF=Burcat B3LYP/6-31G(d)  HF298=320.+/-3. kJ  REF=Balepin Lebedev et al 
Svoistva Veshchestv Str. Mol. 1977 93-98.  HF298(sol)=236.+/-0.4 kJ  REF=IBID.
Max Lst Sq Error Cp @ 200 K ***1.1%*** @ 6000 K 0.49%.
""",
)

entry(
    index = 11,
    label = "HCNH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06783,0.00575753,1.28819e-05,-2.16396e-08,9.41882e-12,27486.8,9.32859], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.54681,0.00696592,-2.37422e-06,3.69518e-10,-2.15501e-14,26874.8,0.555536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Aminomethy  T10/14""",
    longDesc = 
u"""
35430-17-2
HCNH2 Aminomethylene  SIGMA=1  STATWT=3  IA=0.3748  IB=2.9137  IC=3.0035
Nu=3517,3450,3086,1665,1274,1120,1096,667,523  REF=Burcat G3B3  HF298=238.9
+/-2.5 kJ  REF=Ruscic ATcT D 2013  {HF298=91.216+/-2. kcal  REF=Burcat G3B3}
Max Lst Sq Error Cp @ 6000 K 0.39%
""",
)

entry(
    index = 12,
    label = "CH2NOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2875,7.43413e-06,4.28079e-05,-5.73648e-08,2.3207e-11,986.54,10.3124], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40781,0.00929482,-3.23171e-06,5.03362e-10,-2.92822e-14,-250.712,-4.0821], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""C2H=NO  T12/09""",
    longDesc = 
u"""
75-17-2
CH3NO  FORMALDEHYDE-OXIME  CH2=N-OH   SIGMA=2  STATWT=1   A0=2.258  B0=0.396
C0=0.336 Ir(OH)=0.12676  ROSYM=1  V(3)=8897. cm-1  NU=3650,3110,2973,1647,1410,
1318,1166,893,530,953,774,400   REF= M.E. JACOX JPCRD 19,(1990),1485
HF298=4.457+/-2 kJ  REF=Burcat G3B3  {HF298=~7. KCAL  REF=NIST 1991}  Max Lst Sq
Error Cp @ 200 K 0.63%
""",
)

entry(
    index = 13,
    label = "cCHNHNH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50921,-0.00528962,6.24244e-05,-8.21227e-08,3.3442e-11,54259.9,9.17833], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.79825,0.00880092,-3.10084e-06,4.94272e-10,-2.93339e-14,52807.4,-7.13285], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""(-CH*N=NH-T01/07""",
    longDesc = 
u"""
133473-39-9
CH3N2 Diaziridine C Radical,   cyclo(-CH*-NH-NH-) SIGMA=2  STATWT=2  IA=2.8583
IB=3.4835  IC=5.6503  Nu=3427,3390,3147,1396,1298,1259,1184,1126,1026,883,855,
726  HF298=110.243 kcal REF=Burcat G3B3 calc  {HF298=115.88 kcal REF= G2 Catoire
& Swihart J Prop. Power 18,(2002),1242}  Max Lst Sq Error Cp @ 200 K **1.06%***
""",
)

entry(
    index = 14,
    label = "cNNHCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u1 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70718,-0.0072698,6.66436e-05,-8.56628e-08,3.45245e-11,44865.1,9.11001], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.59949,0.00908271,-3.22556e-06,5.16867e-10,-3.07864e-14,43452.4,-5.46725], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""(-CH2N=N*-T01/07""",
    longDesc = 
u"""
127843-62-3
CH3N2 Diaziridine N Radical  Cyclo(-CH2-NH-N*-)  SIGMA=1  STATWT=2  IA=2.8352
IB=3.4685  IC=5.5084  Nu=3412,3199,3108,1546,1325,1230,1130,1094,1018,974,891,
765  HF298=91.577 kcal  REF=Burcat G3B3 calc   {HF298=91.33 kcal REF= G2 Catoire
& Swihart J Prop. Power 18,(2002),1242}  Max Lst Sq Error Cp @ 200 K **1.06%***
""",
)

entry(
    index = 15,
    label = "OHCH2NNO2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 N u0 p0 c+1 {3,S} {7,S} {8,D}
3 N u1 p1 c0 {1,S} {2,S}
4 O u0 p2 c0 {1,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p3 c-1 {2,S}
8 O u0 p2 c0 {2,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53461,0.0240086,5.84816e-06,-2.79984e-08,1.38116e-11,2772.99,13.9279], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.3244,0.011443,-4.20916e-06,6.87755e-10,-4.14592e-14,217.51,-28.3866], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""rad     T05/08""",
    longDesc = 
u"""
CH3N2O3 radical  H2C(OH)-N*NO2  SIGMA=1  STATWT=2  IA=11.8164  IB=28.3471
IC=32.4371  Ir(NO2)=4.93279  ROSYM=2  V(3)=811. cm-1  Ir(OH)=0.18219  ROSYM=1
V(3)=323.2  V(6)=-0.521 (like methanol)  Nu=3701,3091,2967,1626,1486,1425,1383,
1332,1231,1136,979,945,856,824,619,543,499,446,244  HF298=9.731 kcal  REF=Burcat
G3B3 calc  {HF298=     REF=Pitz & Westbrook  Proc. Comb. Inst. 32(2),2007,2343}
Max Lst Sq Error Cp @ 6000 K 0.48%
""",
)

entry(
    index = 16,
    label = "CH3N3O4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  N u0 p1 c0 {1,S} {3,S} {6,S}
3  N u0 p0 c+1 {2,S} {4,S} {5,D}
4  O u0 p3 c-1 {3,S}
5  O u0 p2 c0 {3,D}
6  N u0 p0 c+1 {2,S} {7,S} {8,D}
7  O u0 p3 c-1 {6,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52556,0.0287065,1.12708e-05,-3.9357e-08,1.88296e-11,8865.25,10.7454], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.6091,0.0137699,-5.21915e-06,8.68671e-10,-5.30055e-14,5466.8,-44.4152], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""CH3N(NO2)2T 4/13""",
    longDesc = 
u"""
25346-05-8
CH3N3O4  MethylDinitramine  CH3-N(NO2)2  SIGMA=2  STATWT=1  IA=24.1959
IB=42.1294  IC=60.9276  Ir(CH3)=0.51926  ROSYM=3  V(3)=1253 cm-1 [Ir(NO2)=5.96
ROSYM=2  V(3)=270. cm-1]x2  Nu=3218,3183,3091,1757,1707,1516,1512,1469,1373,
1307,1189,1182.5,1114,864,831,776,746,715,607,451,414,380,271,243
HF298=95.793+/-8. kJ  REF=Burcat G3B3  {HF298=43.1+/-6.3 kJ REF=Korsunskii et al
Bull Acad Sci USSR Div Chem Sci (1989),710; also Keshavarz et al. Indian J Mater.
Sci 13,(2006),542; HF298=53.5+/-0.8 kJ  REF=Miroshnichenko et al Dokl Akad Nauk 
SSSR 295,(1987),419}  Max Lst Sq Error Cp @ 6000 K 0.53%.
""",
)

entry(
    index = 17,
    label = "NH2CHNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52724,0.00993995,2.39539e-05,-3.93377e-08,1.66472e-11,4648.21,12.9718], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.50776,0.0103026,-3.62249e-06,5.76836e-10,-3.42163e-14,3036.11,-10.2337], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""NH=CH-NH2 T02/16""",
    longDesc = 
u"""
77269-36-4 or 155835-45-3
CH4N2  AminoMethen-Imine  NH=CH-NH2  SIGMA=1  STATWT=1  IA=1.2688  IB=7.8067
IC=9.0133  Ir(NH2)=0.2934  ROSYM=2  V(3)=2500. cm-1  Nu=3673,3555,3490,3056,
1759,1651,1435,1351,1125,1107,1052,811,611,555,[415  internal rotation]
HF298=11.893+/-2. kcal  REF=Burcat G3B3  Max Lst Sq Error cp @ 6000 K 0.47%
""",
)

entry(
    index = 18,
    label = "cCH2NHNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.31065,-0.0141446,9.03614e-05,-1.10333e-07,4.33491e-11,27548.3,5.682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.16688,0.011966,-4.22259e-06,6.73715e-10,-4.00072e-14,26091.1,-5.20599], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""c-CH2-N  T01/07""",
    longDesc = 
u"""
41977-52-0 or 41977-53-1 or 76612-78-7
CH4N2  Diaziridine-trans  Cy(-H2C-NH-NH-)  SIGMA=2  STATWT=1  IA=3.5188
IB=3.5460  IC=5.9552  Nu=3440,3432,3198,3116,1562,1428,1350,1260,1228,1216,1153,
989,973,892,776.5  HF298=57.24 kcal  REF=G3B3 calc  REF=Burcat G3B3 calc
{HF298=60.67 kcal cis-G2  REF=Catoire & Swithart J. Prop. & Power 18,(2002),1242;
HF298=58.12 kcal trans-G3 HF298=56.1 kcal trans-G2  REF=Gessner & Ball THEOCHEM,
730,(2005),95}  Max Lst Sq Error Cp @ 200 K  ***1.15%***
""",
)

entry(
    index = 19,
    label = "urea",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u0 p1 c0 {2,S} {7,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.210708,0.0436949,-4.60608e-05,2.36548e-08,-4.42051e-12,-29419.9,26.0662], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3465,0.00895411,-3.10368e-06,4.89573e-10,-2.88532e-14,-32012.8,-26.9745], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Urea (NH2  T 2/06""",
    longDesc = 
u"""
57-13-6
CH4N2O  Urea  (NH2)2C=O  SIGMA=1  STATWT=1  IA=7.5773 IB=8.1422  IC=15.5603
(Ir=0.27257 ROSYM=1 V3=1980. cm-1 from CH3NH2)x2   NU=3548,3448,3440(2),1734,
1594(2),1394,1014,1000,790,618,600,578,542,410   HF298=-231.999 kJ HF0=-215.617
kJ  REF=Burcat G3B3  {HF298=-235.5 kJ  REF=Dorofeeva & Tolmach Thermochim. Acta
240, (1994),47-66}. Max Lst Sq Error Cp @ 6000 K  0.34%
""",
)

entry(
    index = 20,
    label = "NH2CNHNHNO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,D}
2  N u0 p1 c0 {1,S} {4,S} {6,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  N u0 p0 c+1 {2,S} {7,S} {8,D}
5  N u0 p1 c0 {1,D} {11,S}
6  H u0 p0 c0 {2,S}
7  O u0 p3 c-1 {4,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.28862,0.0428325,-7.12055e-06,-2.97723e-08,1.71991e-11,8565.3,23.5165], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.836,0.0126172,-4.76894e-06,7.91212e-10,-4.81568e-14,4150.21,-53.8101], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""ogua  T 2/06""",
    longDesc = 
u"""
556-88-7
CH4N4O2 NITROGUANIDINE (PICRITE) NH2C(NH-NO2)=NH SIGMA=1 STATWT=1  IA=13.9665
IB=44.0715  IC=57.0936  Ir(NH)=0.3093  ROSYM=1 V(3)=1980 cm-1 as CH3NH2
Ir(-NHNO2)=5.428 ROSYM=1 V(3)=2000. cm-1  estim   Ir(NO2)=4.7846 ROSYM=2
V(3)=2800 cm-1 as in (CH3)2N-NO2  Nu=3629,3590,3540,3525,1790,1704,1660,1467,
1378,1339,1192,1107,1063,969,892,800,787,757,631,607,575,450,401,371
HF298=89.295 kJ  HF0=113.75 kJ REF=Burcat G3B3 calc { HF298=1.+/-20. kJ estim.
REF= Dorofeeva & Tolmach Thermochim. Acta 240, (1994),47-66;  Hf298=44.77+/-12.5
kJ  REF=Osmont Catoire et al Comb Flame 151,(2007),262}.  Max Lst Sq Error
Cp @ 6000 K 0.47%
""",
)

entry(
    index = 21,
    label = "NH2CNH2NNO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,D}
2  N u0 p1 c0 {1,S} {6,S} {7,S}
3  N u0 p1 c0 {1,S} {8,S} {9,S}
4  N u0 p0 c+1 {5,S} {10,S} {11,D}
5  N u0 p1 c0 {1,D} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 O u0 p3 c-1 {4,S}
11 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.573278,0.0568402,-4.15607e-05,5.46018e-09,4.28389e-12,3791.46,30.0417], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.9838,0.0123303,-4.56952e-06,7.51185e-10,-4.55e-14,-797.938,-55.6641], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u""")2CNNOT 2/06""",
    longDesc = 
u"""
CH4N4O2 NITROGUANIDINE  (NH2)2C=N-NO2  SIGMA=1  STATWT=1  IA=13.7657  IB=42.1226
IC=55.7429  (Ir(NH2)=0.27642  ROSYM=1  V(3)=1980 cm-1)x2  Ir(NO2)=4.8768
ROSYM=2  V(3)=2800 cm-1   NU=3680,3670,3571,3503,1697,1665,1636,1569,1492,1307,
1307,1196,1106,1060,927,796,786,746,668,616,589,464,432,424,374  HF298=48.162 kJ
HF0=73.410 kJ   REF=Burcat G3B3  Max Lst Sq Error Cp @ 1300 K 0.46%
""",
)

entry(
    index = 22,
    label = "CH3NNH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 N u1 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34217,0.0109605,2.39705e-05,-4.06075e-08,1.76013e-11,23790,10.1531], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.77444,0.0120667,-4.19822e-06,6.63042e-10,-3.90817e-14,22404.6,-9.92485], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""CH3N*NH2  T02/07""",
    longDesc = 
u"""
51891-74-8
CH5N2  METHYL HYDRAZINE RADICAL CH3N*NH2  SIGMA=1  STATWT=2  IA=1.8218 IB=8.0247
IC=9.2375  Ir(CH3)=0.4776 ROSYM=3  V(3)=1283 cm-1  Ir(NH2)=0.2727  ROSYM=2
V(3)=1301 cm-1  Nu=3588,3374,3135,3009,2948,1683,1511,1508,1453,1339,1292,1116,
1072,966,742,481  HF298=50.502 kcal REF=Burcat G3B3 calc {HF298=50.72 kcal
REF=Catoire & Swihart J. Prop Power 18, (2002),1242;  HF298=51.43+/-1.3 kcal
REF=C.MELIUS DATABASE  N86A}   Max Lst Sq Error Cp @ 6000 K 0.46%
""",
)

entry(
    index = 23,
    label = "CH2NHNH2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31544,0.0218627,-3.68464e-06,-1.3271e-08,8.00413e-12,30774.4,15.0726], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.12771,0.0114177,-3.88835e-06,6.04847e-10,-3.52613e-14,29391.5,-10.238], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""2*NHNH2  T02/07""",
    longDesc = 
u"""
442197-99-1
CH5N2  METHENYL HYDRAZINE RADICAL CH2*NH-NH2  SIGMA=1  STATWT=2  IA=1.8334
IB=8.2204  IC=9.4246  Ir(CH2)=0.3023 ROSYM=2  V(3)=1000 cm-1  Ir(NH2)=0.2934
ROSYM=1  V(3)=1301 cm-1  Nu=3551,3514,3339,3250,3141,1714,1521,1481,1343,1263,
1254,1043,926,744,710,439  HF298=64.349 kcal REF=Burcat G3B3 calc {HF298=66.04
kcal  REF=Catoire & Swihart J. Prop Power 18, (2002),1242;  HF298=65. kcal est.
Orlov et al J. Mol Struct 608,(2002),109}   Max Lst Sq Error Cp @ 6000 K 0.39%
""",
)

entry(
    index = 24,
    label = "NHC(NH2)2",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 N u0 p1 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.395239,0.0330449,-8.09864e-06,-1.90812e-08,1.19155e-11,1876.53,24.2297], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.95418,0.0116167,-3.98187e-06,6.23233e-10,-3.65275e-14,-876.306,-26.0115], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""guanidinT 2/06""",
    longDesc = 
u"""
113-00-8
CH5N3 GUANIDINE  (NH2)2C=NH  SIGMA=1 STATWT=1  IA=8.0205  IB=8.2786  IC=16.0571
(Ir=0.2849  ROSYM=1 V(3)=1980 cm-1)x2    NU=3642,3638,3536,3531,3466,1767,1673,
1657,1470,1211,1154,1116,945,836,794,688,599,543,478   HF298=27.932 kJ
HF0=48.939 kJ  REF=Burcat G3B3 {HF298=15.+/-10. kJ  REF= Dorofeeva & Tolmach
Thermochim. Acta 240, (1994),47-66.}   Max Lst Sq Error Cp @ 6000 K  0.37%
""",
)

entry(
    index = 25,
    label = "cC(NO)",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35125,0.00462452,3.17563e-06,-8.80253e-09,4.152e-12,53081.7,9.24843], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.44276,0.00157049,-6.09403e-07,1.03422e-10,-6.40607e-15,52384.1,-2.18174], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""cyclo     T 8/12""",
    longDesc = 
u"""
228850-18-8
C(NO)  cyclo radical  SIGMA=1  STATWT=2  IA=1.9035  IB=2.5928  IC=4.4963
Nu=564,960,1477   REF=Burcat G3B3  HF298=451.47+/-1.64 kJ  REF=ATcT C 2011
{HF298=450.+/-8. kJ  REF=Burcat G3B3  Max Lst Sq Error Cp @ 1300 K 0.30%.
""",
)

entry(
    index = 26,
    label = "CON3",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 C u1 p0 c0 {1,S} {4,D}
3 N u0 p0 c+1 {1,D} {5,D}
4 O u0 p2 c0 {2,D}
5 N u0 p2 c-1 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12287,0.0216723,-2.46112e-05,1.53311e-08,-4.05562e-12,40642.4,12.3603], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.48006,0.00437741,-1.65815e-06,2.77125e-10,-1.69887e-14,39237.4,-14.8192], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Radical    T 1/13""",
    longDesc = 
u"""
*C(O)N3  Formil Azide Radical SIGMA=1  STATWT=2  IA=4.6661  IB=20.4976
IC=25.1637  Nu=2270,1885,1140,918,812,576,453,239,154  REF=Burcat G3B3
HF298=352.1+/-3.3 kJ  REF=Maroshkin & Dorofeeva  Comp Theor. Chem 991,(2012),182
{HF298=360.0+/-8. kJ  REF=Burcat G3B3}  Max Lst Sq Error Cp @ 1300 K 0.42%.
""",
)

entry(
    index = 27,
    label = "CS",
    molecule = 
"""
1 S u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73125,-0.00309804,1.24828e-05,-1.41633e-08,5.33371e-12,32442.1,4.54855], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7696,0.000730981,-2.42921e-07,2.88071e-11,-5.21956e-17,32249.9,3.42023], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g11/01""",
    longDesc = 
u"""
2944-05-0
CS  CARBON SULFIDE  SIGMA=1  Be=0.820046  WE=1285.08  WEXE=6.44  WEYE=-.00077
ALPHAA1=.0059115  ALPHA2=-4.7E-06  DE=1.348E-06  BETA1=-3.6E-09  STATWT=1
T0=27661.0  WE=1135.1  WEXE=7.73  BE=0.7851  ALPHA1=.0072  DE=1.5E-06 STATWT=6
T0=31339.4  WE= 828.4  WEXE=4.85  WEYE=-.0056  BE=0.6489 ALPHA1=.006 DE=1.6E-06
STATWT=3  T0=35675.  WE=795.6  WEXE=4.91  BE=.6367  ALPHA1=.0062  DE=1.6E-06
STATWT=6  T0=38681.9 WE=752.8  WEXE=4.95  BE=.6227  ALPHA1=.0062  DE=1.7E-06
STATWT=3  T0=38895.7 WE=1077.3 WEXE=10.66 BE=.7881  ALPHA1=.0092  DE=1.9D-06
STATWT=2. T0=39300.  WE=665.   BE=.57     STATWT=2.
          T0=39345.  WE=720.   BE=.58     STATWT 1.
          T0=56504.  WE=462.4  WEXE=7.46  WEYE=-.108  WEZE=.0377   STATWT=1.
BE=.58  REF=Gurvich 91   HF298=278.55 kJ  H0=275.307+/-3.8 kJ  REF=Prinslow
JCP 94,(1991),3563  {HF298=279.9+/-0.85 kJ  REF=Denis J Sulfur Chem 29,(2008),
327;  HF298=280.3+/-25 kJ REF=JANAF76}  Max Lst Sq Error Cp @ 2200 K 0.18%
""",
)

entry(
    index = 28,
    label = "HCCN(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.62983,0.00431798,4.65185e-06,-9.03602e-09,3.88976e-12,61731.9,2.58604], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.97313,0.00356298,-1.27604e-06,2.05621e-10,-1.22949e-14,61212.1,-5.07923], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T04/09""",
    longDesc = 
u"""
2612-62-6
HCCN  singlet HC**-CN  STATWT=1  SIGMA=1  [IA=0.1513  IB=7.6445  IC=7.6765]
NU=3229,1735,1178.6,[937],383,128,9 REF=Jacox Webbook 2009; [] Burcat G3B3
HF298=125.849+/-2. kcal REF=Burcat G3B3 {HF298=126.5+/-3. kcal  REF=Poutsma et
al JPC A 106,(2002),1073}  Max Lst Sq Error Cp @ 6000 K 0.32%.
""",
)

entry(
    index = 29,
    label = "HCCN(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,T}
3 H u0 p0 c0 {1,S}
4 N u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66958,0.0190287,-3.17733e-05,2.83582e-08,-9.84842e-12,55902,10.1148], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.0382,0.00342241,-1.2069e-06,1.92501e-10,-1.14297e-14,55221.8,-5.90236], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T04/09""",
    longDesc = 
u"""
2612-62-6
C2HN Triplet  HC*=C=N*  SIGMA=1  STATWT=3  IA=0.0320  IB=7.6445  IC=7.6765
Nu=3406,1800,1248,475,452,389 HF298=113.876+/-2. kcal  REF=Burcat G3B3 calc
{HF298=115.6+/-5 kcal  REF=Poutsma et al JPC A 1006,(2002),1073;  HF0=609.241+/-
100. kJ  REF=Gurvich 89}  Max Lst Sq Error Cp @ 1300 K 0.31%
""",
)

entry(
    index = 30,
    label = "NCCHO",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63363,0.0118742,-5.03743e-06,-8.99835e-10,1.01584e-12,3741.09,8.57238], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.42262,0.00603503,-2.21102e-06,3.61593e-10,-2.18402e-14,2821.71,-6.42841], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T06/04""",
    longDesc = 
u"""
4471-47-0
C2HNO  CYANOKETENE  NC-CHO  SIGMA=1  STATWT=1  IA=1.2675  IB=16.7941  IC=18.0617
NU=3018,2347,1800,1425,1004,932,628,313,222  HF298=10.545 kcal  HF0=10.994 kcal
REF=Burcat G2B3 Calc   Max Lst Sq Error Cp @ 1300 K 0.48%
""",
)

entry(
    index = 31,
    label = "HCCNO2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {6,S}
2 C u0 p0 c0 {1,T} {3,S}
3 N u0 p0 c+1 {2,S} {4,S} {5,D}
4 O u0 p3 c-1 {3,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.34403,0.0333183,-3.93939e-05,2.41125e-08,-5.90505e-12,31935.8,18.7891], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.24323,0.00611883,-2.22735e-06,3.63051e-10,-2.18882e-14,30008.2,-20.7148], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A 1/05""",
    longDesc = 
u"""
32038-80-5
C2HNO2  Nitroacetylene  HCC-NO2  SIGMA=1  STATWT=1  IA=6.4119  IB=18.5936
IC=25.0056  Nu=3494,2241,1632,1339,935,764,715,643,611,602,273,206  REF=Burcat
B3LYP calc  HF298=66.6 kcal  G3B3 calc  REF=Politzer Lane Concha JPC A 108,
(2004), 3493-98  Max Lst Sq Error Cp @ 1300 K 0.39%.
""",
)

entry(
    index = 32,
    label = "NO2CHCNO2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 N u0 p0 c+1 {1,S} {6,S} {7,D}
3 N u0 p0 c+1 {4,S} {8,S} {9,D}
4 C u1 p0 c0 {1,D} {3,S}
5 H u0 p0 c0 {1,S}
6 O u0 p3 c-1 {2,S}
7 O u0 p2 c0 {2,D}
8 O u0 p3 c-1 {3,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09929,0.0391027,-1.69246e-05,-1.51337e-08,1.13217e-11,37009,16.1402], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.5743,0.00740298,-2.99656e-06,5.16982e-10,-3.22543e-14,33099.3,-54.5845], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""1  T 3/08""",
    longDesc = 
u"""
244294-17-5 for 1,1-Dinitroetylene radical)
C2H(NO2)2 1,2-Dinitroethylene-trans radical NO2-HC=C*NO2  SIGMA=1  STATWT=2
IA=15.5706  IB=64.8436  IC=70.3382  Ir(NO2)=5.8010  ROSYM=2  V(3)=1753 cm-1
(5.04 kcal) Ir(NO2)=5.8635  ROSYM=2  V(3)=1700 cm-1  Nu=3263,1744,1671,1586,
1375,1334,1237,910,889,817,790,701,656,627,553,465,307,228,117  HF298=78.489
kcal  REF=Burcat G3B3 calc  Max Lst Sq Error Cp @ 1300 K 0.44%
""",
)

entry(
    index = 33,
    label = "C2HN7O2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,D} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {6,D}
3  N u0 p1 c0 {1,S} {6,S} {9,S}
4  N u0 p0 c+1 {2,S} {10,S} {11,D}
5  N u0 p1 c0 {1,D} {2,S}
6  N u0 p1 c0 {2,D} {3,S}
7  N u0 p1 c0 {1,S} {8,D}
8  N u0 p0 c+1 {7,D} {12,D}
9  H u0 p0 c0 {3,S}
10 O u0 p3 c-1 {4,S}
11 O u0 p2 c0 {4,D}
12 N u0 p2 c-1 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0541,0.0551942,-3.95348e-05,6.47426e-09,2.96745e-12,58162.4,16.7114], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.1642,0.0133214,-5.14134e-06,8.63898e-10,-5.30265e-14,53530.9,-67.2721], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""5-Azido  T 5/13""",
    longDesc = 
u"""
53566-50-0
C2HN7O2  Cy  5-Azido-2-nitrotriazole  SIGMA=1  STATWT=1  IA=18.0999  IB=148.8712
IC=166.9710  Ir(NO2)=5.96  ROSYM=2  V(3)=480. cm-1  Ir(N3)=4.17776  ROSYM=2
V(3)=800.  cm-1  Nu=3641,2311,1657,1581,1523,1485,1411,1389,1294,1142,1119,1044,
1028,836,791,752,710,643,602,587,541,535,433,367,345,207,179,111  REF=Burcat
B3LYP/6-31G(d)  HF298=121.6+/-3 kcal  REF=Osmont Catoire et al C&F 151,(2007),
262   Max Lst Sq Error Cp @ 1300 K 0.51%
""",
)

entry(
    index = 34,
    label = "NCCH2O",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96392,0.0164646,-3.33503e-06,-8.15626e-09,4.80225e-12,19549.8,12.2143], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.26373,0.00791027,-2.87373e-06,4.67365e-10,-2.81207e-14,18183.6,-10.8309], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RADICAL  T06/04""",
    longDesc = 
u"""
350610-21-8
C2H2NO  Cyanoethoxy Radical  NCCH2O*  SIGMA=1  STATWT=2  IA=2.0417  IB=17.2593
IB=18.7911  NU=2976,2957,2371,1404,1348,1171,1078,902,599,589,335,225
HF298=41.974 kcal  HF0=43.312 kcal  REF=Burcat G3B3 calc Max Lst Sq Error Cp
@ 6000 K 0.48%.
""",
)

entry(
    index = 35,
    label = "NCCH2OO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u1 p2 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.25159,0.0146469,9.70672e-06,-2.46314e-08,1.13321e-11,19445.8,8.75951], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.10482,0.0089597,-3.25671e-06,5.29969e-10,-3.19049e-14,17739.8,-18.1426], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HF298  T06/04""",
    longDesc = 
u"""
119437-64-8
C2H2NO2  Cyanoethylperoxy Radical NC-CH2-O-O*  SIGMA=1  STATWT=2  IA=2.4622
IB=32.7369  IB=34.6635  NU=3147,3091,2384.1493,1379,1230,1192,996,984,946,521,
441,364,183,59.96   HF298=42.54  kcal  HF0=44.24  kcal  REF=Burcat G3B3 calc
Max Lst Sq Error Cp @ 6000 K 0.46%.
""",
)

entry(
    index = 36,
    label = "C2H2(NO2)2",
    molecule = 
"""
1  N u0 p0 c+1 {2,S} {3,D} {4,S}
2  O u0 p3 c-1 {1,S}
3  O u0 p2 c0 {1,D}
4  C u0 p0 c0 {1,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  N u0 p0 c+1 {5,S} {7,S} {8,D}
7  O u0 p3 c-1 {6,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.46008,0.0238753,3.45147e-05,-7.10367e-08,3.2087e-11,2354.83,9.91351], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.5193,0.0109828,-4.28161e-06,7.24665e-10,-4.47052e-14,-1840.03,-56.9856], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""DI-N  A 5/05""",
    longDesc = 
u"""
88055-17-8
C2H2(NO2)2 Di-Nitroethylene-trans(E)    SYMNO = 2  STATWT = 1   IA = 13.5875
IB = 80.5878   IC = 94.1753  (Ir(NO2)= 5.96  ROSYM = 2  V(3) = 5.04 kcal)x2
NU=3398,3290,1732,1652,1644,1399,1398(2),1277,1217,1004,972.5(2),900,789,767,
702,643,580,421,295,169,155    HF298=9.788 kcal  REF = BURCAT  G3B3 calc
{HF298 = 14.2  kcal    REF=NIST 94.}   Max Lst Sq  Error Cp @ 6000 K 0.49%.
""",
)

entry(
    index = 37,
    label = "cCH2NCH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37128,-0.00290988,5.17607e-05,-6.76267e-08,2.72556e-11,31730.7,9.47467], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.26997,0.0094393,-3.36707e-06,5.41051e-10,-3.22865e-14,30449,-4.32695], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Haziridin T12/14""",
    longDesc = 
u"""
157-16-4
C2H3N 2-H azeridine cy(-CH2-CH=N-)  SIGMA=1  STATWT=1  IA=2.3518  IB=3.7663
Nu=3227,3197,3113,1765,1538,1293,1132,1045,1010,992,791,722  HF298=65.465+/-2.
kcal  REF=Burcat G3B3  Max Lst Sq Error Cp @ 200 K 0.84%.
""",
)

entry(
    index = 38,
    label = "NCCH2OH",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 O u0 p2 c0 {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90219,0.0163747,5.68148e-06,-2.10178e-08,1.02634e-11,-7585.31,12.2671], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.59341,0.00944576,-3.33631e-06,5.32676e-10,-3.16483e-14,-9134.77,-13.3107], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T06/04""",
    longDesc = 
u"""
107-16-4
C2H3NO  CYANOMETHANOL  NC-CH2-OH  STATWT=1  SIGMA=1  IA=2.3575  IB=17.4351
IC=19.2646  Ir(OH)=0.14242  ROSYM=2  V(3)=1399. cm-1  NU=3751,3031,3004,2383,
1530,1477,1266,1264,1089,1044,900,578,373,233  HF298=-10.881 kcal  HF0=-9.765
kcal  REF=Burcat G3B3 calc. Max Lst sq Error Cp @ 6000 K 0.44%.
""",
)

entry(
    index = 39,
    label = "NCCH2OOH",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 O u0 p2 c0 {3,S} {5,S}
5 O u0 p2 c0 {4,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.71323,0.0182104,1.77782e-06,-1.68345e-08,8.6421e-12,1343.99,6.62658], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.50764,0.0100846,-3.63252e-06,5.84207e-10,-3.48052e-14,-203.334,-19.298], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A08/04""",
    longDesc = 
u"""
180330-47-6
C2H3NO2  CYANOMETHYLPEROXIDE  NC-CH2-O-OH  SIGMA=1  STATWT=1  IA=2.5577
IB=34.3766  IC=36.1945  Ir(OH)=0.1531  ROSYM=1  V(3)=447.7 cm-1  Ir(OOH)=4.3879
ROSYM=3  V(3)=1165. cm-1  NU=3702,3082,3041,2382,1526,1416,1387,1237,1073,1048,
972,945,529,403,377,202  HF298=7.045 kcal HF0=9.421 kcal REF=Burcat G3B3 calc
Max Lst Sq Error Cp @ 6000 K 0.43%
""",
)

entry(
    index = 40,
    label = "CH3C(O)ONO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  N u0 p0 c+1 {4,S} {6,S} {7,D}
6  O u0 p3 c-1 {5,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.58678,0.0257381,7.22442e-06,-2.89638e-08,1.36357e-11,-39045.5,8.42921], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.0727,0.0134926,-5.15307e-06,8.61746e-10,-5.275e-14,-42001.5,-38.2748], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T10/05""",
    longDesc = 
u"""
591-09-3
C2H3NO4  Acetyl-Nitrate CH3C(O)-O-NO2  SIGMA=1  STATWT=1  IA=14.2331  IB=46.1172
IC=47.0587  Ir(CH3)=0.5224  ROSYM=3  V(3)=316. cm-1 (as in acetone) Ir(NO2)=
4.91976  ROSYM=2  V(3)=3183 cm-1 (as in ethyl-nitrate)  Nu=3187,3144,3077,1872,
1841,1501,1498,1422,1386,1201,1075,1010,918,807,733,630,611,528,524.5,322,177,
110.6  HF298=-72.575 kcal  HF0=-287.915 kJ  REF=Burcat G3B3  {HF298=-79.39 kcal
REF=Thergas, Benson; -90.66 kcal Yoneda}  Max Lst Sq Error Cp @ 1300 K 0.59%
""",
)

entry(
    index = 41,
    label = "CH3C(O)OONO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  N u0 p0 c+1 {5,S} {7,S} {8,D}
7  O u0 p3 c-1 {6,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.2449,0.0367553,-8.51527e-06,-1.82736e-08,1.08142e-11,-33419.3,10.352], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.5408,0.0140049,-5.36495e-06,8.99942e-10,-5.52251e-14,-37009.7,-50.1762], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T10/05""",
    longDesc = 
u"""
2278-22-0
C2H3NO5 Peroxy-Acetyl Nitrate  CH3C(O)-OO-NO2  SIGMA=1  STATWT=1  IA=16.7510
IB=64.9955  IC=65.3601  Ir(CH3)=0.5260  ROSYM=3  V(3)=316. cm-1 (as in acetone)
Ir(NO2)=5.82726 ROSYM=2  V(3)=3183. cm-1 (as in ethyl-nitrate)  Nu=3187.5,3145,
3077,1908,1841,1500,1498,1421,1370,1191,1074,1006,979,838,807,726,720,612,578,
494,371,331,314,96.96,94.75  HF298=-60.861 kcal  HF0=-237.02 kJ  REF=Burcat
G3B3 calc  {HF298=-60.3 kcal  REF=NIST 94} Max Lst Sq Error Cp @ 1300 K 0.57%.
""",
)

entry(
    index = 42,
    label = "C2H3NS",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.39195,0.0271158,-2.12406e-05,5.35375e-09,1.08149e-12,13949,15.6366], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.61153,0.00874624,-3.12894e-06,5.03621e-10,-3.00832e-14,12311.8,-16.1185], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HS-CH2-CN T 3/16""",
    longDesc = 
u"""
54524-31-1
C2H3NS  MercaptoAcetonitrile  HS-CH2-CN  SIGMA=1  STATWT=1  IA=3.6302  
IB=27.6468  IC=30.3265  Ir(SH)=0.55764  ROSYM=1  V(3)=13001. cm-1  Nu=3135.5,
3085,2687.5,2368,1466,1287,1221,1019,947,796,696,491,379,217,[176 intern. rotat] 
HF298=31.181+/-2. kcal  REF=Burcat G3B3  {HF298=2.36 kcal?  REF=RMG Greene 2013}  Max Lst Sq Error Cp @ 6000 K 0.43%.
""",
)

entry(
    index = 43,
    label = "C(O)CH2NH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N u0 p1 c0 {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09588,0.0226389,-9.28632e-06,-4.68682e-09,4.03903e-12,1684.09,12.6338], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.0103,0.0110812,-3.86479e-06,6.09941e-10,-3.59556e-14,232.166,-13.2137], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 1/13""",
    longDesc = 
u"""
C2H4ON  *C(O)CH2NH2  Radical  SIGMA=1  STATWT=2  IA=1.9786  IB=19.7527
IC=20.9831  Ir(NH2)=0.3219  ROSYM=2  V(3)=1106 cm-1  Ir(-CO)=1.9145  ROSYM=1
V(3)=900. cm-1  Nu=3568,3480,3068,2938,1939,1691.5,1494,1391.5,1295,1161,1103,
902,837.5,794,512,335  REF=Burcat G3B3  HF298=29.3+/-3.3 kJ  REF=Marochkin &
Dorofeeva  Comp Theor Chem 991,(2012),182  Max Lst Sq Error Cp @ 6000 K 0.43%.
""",
)

entry(
    index = 44,
    label = "C2H4(NO2)2",
    molecule = 
"""
1  N u0 p0 c+1 {2,S} {3,D} {4,S}
2  O u0 p3 c-1 {1,S}
3  O u0 p2 c0 {1,D}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  N u0 p0 c+1 {5,S} {7,S} {8,D}
7  O u0 p3 c-1 {6,S}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16496,0.0205653,4.77904e-05,-8.16586e-08,3.49355e-11,-14057.5,16.9052], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.353,0.0168115,-6.35596e-06,1.05307e-09,-6.40116e-14,-17997.9,-41.4649], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 4/12""",
    longDesc = 
u"""
7570-26-5
1,2-C2H4(NO2)2 1,2-DinitroEthane  SIGMA=1  STATWT=1  IA=14.2459  IB=83.5171
IC=96.7229  [Ir(NO2)=5.97  ROSYM=2  V(3)=28. cm-1]x2  Ir(CH2NO2)=3.222  ROSYM=1
V3=1763 cm-1  Nu=3193,3176,3134,3128,1679,1674,1497(2),1444,1427,1386,1312,1312,
1300,1226.5,1107(2),942,921,812,745,668,598,578,565,400,266,158  REF=Burcat G3B3
HF298=-23.1+/-0.3 kcal exper REF=Miroshnichenko et al Russ Chem. Bul
{HF298=-26.14+/-8. kcal  REF=Burcat G3B3}  HF298(liq)=-42.6+/-0.1 kcal
REF=Miroshnichenko et al ibid.  Max Lst Sq Error Cp @ 6000 K 0.57%.
""",
)

entry(
    index = 45,
    label = "C2H4S4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  S u0 p2 c0 {1,S} {7,S}
3  S u0 p2 c0 {1,S} {8,S}
4  C u0 p0 c0 {1,D} {5,S} {6,S}
5  S u0 p2 c0 {4,S} {9,S}
6  S u0 p2 c0 {4,S} {10,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.656699,0.0902111,-0.000160456,1.36722e-07,-4.42764e-11,16131,24.2713], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.6799,0.00746105,-2.69248e-06,4.3587e-10,-2.61405e-14,13116.7,-55.0859], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""(HS)2C=C(  T 5/14""",
    longDesc = 
u"""
95241-02-4
C2H4S4 Ethylenetetrathiol  2(HS)C=C(SH)2  SIGMA=4  STATWT=1  IA=50.7592  
IB=61.5320  IC=111.3179  [Ir(SH)=0.55764  ROSYM=1  V(3)=1100. cm-1]x4  
Nu=2664.5(2),2659,1581.5,1033,1000,975,927,905.5,848,685,523,421.5,362,326,301,
277,240,228  HF298=38.091+/-2. kcal  REF=Burcat G3B3  Max Lst Sq Error Cp @
6000 K 0.27%.
""",
)

entry(
    index = 46,
    label = "Glycine",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  N u0 p1 c0 {1,S} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15851,0.029522,2.14979e-06,-2.87489e-08,1.52878e-11,-49036.3,22.2831], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4281,0.0141735,-4.97242e-06,7.86326e-10,-4.63337e-14,-51574.5,-21.9428], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""NH2-CH2  T06/10""",
    longDesc = 
u"""
56-70-6
C2H5NO2  Glycine  NH2-CH2-C(O)OH  SIGMA=1  STATWT=1  IA=8.1465  IB=21.2300
IC=28.4581  Ir(NH2)=0.3042  ROSYM=2  V(3)=1224. cm-1 est  Ir(-C(O)OH)=3.1684
ROSYM=1  V(3)=1224. Cm-1  Nu=3685,3579,3489,3083,2942,1853,1677,1526,1471,1355,
1281,1233,1167,1119.5,1038,871,847,689,630,524,461,284   HF298=-93.62+/-2 kcal
REF=Burcat G3B3 calc  {HF298=-390.5+/-4.6 kJ  REF=Thermochim Acta 20,(1977),371;
HF298=-94.2 kcal  REF=Karton Martin et al Theor Chem Acc 133,(2014),1483}  Max
Lst Sq Error Cp @ 6000 K 0.43%
""",
)

entry(
    index = 47,
    label = "CH3OC(O)NH2",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  N u0 p1 c0 {2,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9831,0.0343814,-1.6458e-05,-5.14921e-09,5.50415e-12,-51518.4,16.1848], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1703,0.0143671,-5.02606e-06,7.97251e-10,-4.71522e-14,-53885.4,-26.6662], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H  T07/12""",
    longDesc = 
u"""
598-55-0
C2H5NO2  Methyl Carbamate CH3-O-C(O)-NH2  SIGMA=1  STATWT=1  IA=7.9098
IB=19.1979  IC=26.5461  Ir(CH3)=0.5166  ROSYM=3  V(3)=1224. cm-1  Ir(NH2)=0.312
ROSYM=2  V(3)=1106. cm-1  REF=Burcat G3B3  HF298=412+/-3 kJ  REF=Marochkin and
Dorofeeva Ind Eng Chem Res  51,(2012),5372 G4  {HF298=-425.3 kJ Bernard Boukari
Thermochim Acta 16,(1976),267;  HF298=-439.8 kJ  REF=Zeng et al Ind Eng Chem Res
49,(2010),5543} HF298(cr)=-485.6 kJ  REF=Marochkin & Dorofeeva Ind Eng Chem Res
51,(2012),5372 G4  Max Lst Sq Error Cp @ 6000 K 0.44%.
""",
)

entry(
    index = 48,
    label = "C2H5N3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  N u0 p1 c0 {1,S} {4,D}
4  N u0 p0 c+1 {3,D} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 N u0 p2 c-1 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12866,0.0166009,3.04097e-05,-4.97574e-08,2.05156e-11,30246.5,12.7193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.45448,0.0182737,-6.90154e-06,1.13973e-09,-6.90183e-14,27914,-18.9069], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""EthylAzyd  A12/04""",
    longDesc = 
u"""
871-31-8
C2H5N3  Ethyl Azide   SIGMA=1  STATWT=1  IA=6.1562    IB=25.6515    IC=29.3530
Ir(CH3)=0.52082 ROSYM=3 V(3)=5533 cm-1  Ir(N3)=4.17776  ROSYM=2  V(3)=3186 cm-1
Nu=3143,3132,3117,3055,3043,2257,1537,1522,1520,1438,1400,1345,1301,1172,1105,
1005,856,808,663,576,400,282  HF298=63.784 kJ  HF0=68.689 kJ  REF=Burcat G3B3
calc  {HF298=64.5 kcal REF=G2 calc Rogers & McLafferty JCP 103(18),(1995),8302}
Max Lst Sq Error Cp @ 6000 K 0.69%
""",
)

entry(
    index = 49,
    label = "C2H5N3O5",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {5,S} {11,S}
2  N u0 p0 c+1 {1,S} {3,S} {4,D}
3  O u0 p3 c-1 {2,S}
4  O u0 p2 c0 {2,D}
5  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p0 c+1 {7,S} {9,S} {10,D}
9  O u0 p3 c-1 {8,S}
10 O u0 p2 c0 {8,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.89114,0.0209076,6.6984e-05,-1.06508e-07,4.4724e-11,-12415.1,4.46589], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.9524,0.0219529,-8.17143e-06,1.34695e-09,-8.17156e-14,-16949.7,-60.1602], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""NENA    T 4/14""",
    longDesc = 
u"""
41719-24-8
C2H5N3O5  NENA  Nitrato Ethyl NitrAmide  HN(NO2)CH2CH2ONO2  SIGMA=1 STATWT=1
IA=18.5  IB=171.1916  IC=177.1192  [Ir(NO2)=5.96  ROSYM=2  V(3)=280. cm-1]x2
Nu=3600,3169,3137,3099,3084,1765,1706,1544,1503,1458,1437.5,1393,1632,1345,1325,
1258,1174,1128,1090,1033,965,876,831,777,761,734,709,649,582,531,379.5,325,282,
180,158.6,113,77.6  REF=Burcat B3LYP/6-31G(d)  HF298=-75.07+/-3. kJ  REF=Turker 
& Atalar  J.Hazardous Materials 162,(2009),193 cis  {HF298=-13.2 kcal  REF=Therm 94
very rough approx.}  HF298=-64.09+/-3 kJ  trans  REF=Turker & Atalar IBID   Max 
Lst Sq Error Cp @ 6000 K 0.55%.
""",
)

entry(
    index = 50,
    label = "CH2NHCH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p1 c0 {1,S} {5,S} {6,S}
5 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14378,0.0140062,2.3506e-05,-4.17415e-08,1.82376e-11,17138.5,10.8365], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.97607,0.0144633,-5.03599e-06,7.95671e-10,-4.69087e-14,15614.3,-11.43], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A09/04""",
    longDesc = 
u"""
31277-24-4
C2H6N  Methyl-Methylen-Amine Radical *CH2-NH-CH3  SIGMA=1  STATWT=2  Ia=1.9758
Ib=8.6300  Ic=9.0053  Ir(CH3)=0.46839  ROSYM=3 V(3)=1253. cm-1  Ir(CH2)=0.30207
ROSYM=2  V(3)=1253. cm-1  Nu=3550,3249,3143,3128,3084,2993,1556,1525,1513,1493,
1467,1304,1261,1149,1053,973,722,675,392   HF298=156.58  kJ  HF0=174.070 kJ
REF=Janoschek & Rossi Int. J. Chem Kin. 36,(2004),     Max Lst Sq Error Cp @
6000 K 0.48%
""",
)

entry(
    index = 51,
    label = "(CH3)2N-NH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  N u0 p1 c0 {1,S} {2,S} {4,S}
4  N u1 p1 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09065,0.0173629,3.01166e-05,-4.98285e-08,2.07771e-11,23108,11.7273], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.94122,0.0196087,-7.1165e-06,1.15466e-09,-6.9305e-14,20969.1,-17.1913], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A10/04""",
    longDesc = 
u"""
40613-93-2
(CH3)2N-NH* UNSYMETRICAL DIMETHYL HYDRAZINE RADICAL    SIGMA=2  STATWT=2
Ia=8.5287  Ib=9.4466  Ic=16.6828  (Ir(CH3)=0.50137  V(3)=1049 cm-1 ROSYM=3)x2
Ir(NH)=0.162277  ROSYM=2  V(3)=3778 cm-1  Nu=3371,3170,3130,3099,3089,3004,2991,
1545,1530,1517,1504,1490,1478,1456,1376,1211,1173,1136,1114,1058,840,548,492,416
HF298=207.685 kJ  HF0=232.276 kJ  REF=G3B3 calc.   {HF298=40.2+/-2. kcal
REF=Bozzelli & Ritter}   Max Lst Sq Error Cp @ 6000 K 0.64%.
""",
)

entry(
    index = 52,
    label = "CH2(CH3)NNH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  N u0 p1 c0 {1,S} {3,S} {4,S}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  N u0 p1 c0 {2,S} {10,S} {11,S}
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
            NASAPolynomial(coeffs=[2.29772,0.0330028,-1.1078e-05,-1.02853e-08,7.39126e-12,29071.6,16.4347], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.24073,0.0171697,-5.96838e-06,9.41907e-10,-5.54852e-14,27024.5,-20.1283], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 2/07""",
    longDesc = 
u"""
760115-05-7 ??
C2H7N2  UNSYMETRICAL METHYL METHENYL HYDRAZINE RADICAL *CH2(CH3)N-NH2  STATWT=2
SIGMA=1  IA=8.5947  IB=9.3234  IC=16.6130  Ir(CH#)=0.5021  ROSYM=3  V(3)=1200.
cm-1  Ir(NH2)=0.3073  ROSYM=1  V(3)=1105. cm-1  Ir(CH2)=0.3102  ROSYM=1
V(3)=1049.  cm-1  Nu=3505,3375,3251,3159,3145,3104,3000,1704,1537,1511,1504,
1465,1367,1341,1320,1153,1126,1063,970,842,705,468,434,361  HF298=61.82 kcal
REF=Burcat G3B3 calc  Max Lst Sq Error Cp @ 6000 K 0.46%.
""",
)

entry(
    index = 53,
    label = "CH3NHNHCH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  N u0 p1 c0 {1,S} {3,S} {8,S}
3  N u0 p1 c0 {2,S} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.41669,0.00250625,7.35471e-05,-9.60749e-08,3.79945e-11,10565.4,3.29279], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.19444,0.0219114,-7.91706e-06,1.27708e-09,-7.62826e-14,8515.92,-17.5013], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Sy  T 2/07""",
    longDesc = 
u"""
540-73-8
CH3NH-NHCH3 SYMETRICAL DIMETHYL HYDRAZINE SIGMA=1 IA=2.9954    IB=20.2056
IC=21.6926  [Ir(CH3)=0.50567  ROSYM=3 V(3)=1049 cm-1]x2  Ir(NH2)=3.0882  ROSYM=1
V(3)=3778 cm-1  Nu=3442,3421,3123.8(2),3075(2),3003.5(2),1564,1345.5(2),1512,
1508,1470.7(2),1447,1325,1200,1168,1122,1117,1055,981,924,830,478,295
HF298=25.376.kcal  REF=Burcat G3B3 calc  {HF298=22.584+/-1.8 kcal REF=C. Melius
BAC/MP4 Calculations, Private Communication}  Max Lst Sq Error Cp @ 1300 K 0.61%
""",
)

entry(
    index = 54,
    label = "CCN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 N u0 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40723,0.00944214,-1.30137e-05,1.06894e-08,-3.6857e-12,80332.9,6.78654], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.51786,0.001955,-7.53385e-07,1.27744e-10,-7.82861e-15,79783.9,-3.83516], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Radical      ATcT/A""",
    longDesc = 
u"""
4120-02-9
CCN RADICAL  SIGMA=1  STATWT=2  B0=0.398  NU=1923,324(2),1051
T0=40.34     SIGMA=1  STATWT=2  B0=0.398  Nu=1923,324(2),1051
T0=21259.20  SIGMA=1  STATWT=4  B0=0.414  Nu=1771,451(2),1242
T0=22413.25  SIGMA=1  STATWT=2  B0=0.405  Nu=1771,445(2),1242
T0=26661.73  SIGMA=1  STATWT=2  B0=0.413  Nu=1859,470(2),1257   REF=Jacox 98
HF298=679.07+/-6.23 kJ  REF=ATcT A {HF298=678.32+/-4.3 kJ  REF=ATcT C 2011;
HF298=604.85+/-20 kJ REF=Gurvich 91;  HF298=584.51  REF=JANAF 66}   Max Lst Sq
Error Cp @ 1300 K 0.34%.
""",
)

entry(
    index = 55,
    label = "C2N2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79226,0.0128464,-1.49556e-05,1.06206e-08,-3.23981e-12,48088,10.065], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.46649,0.00378556,-1.40601e-06,2.31962e-10,-1.40934e-14,47379.7,-3.4654], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Isocyanogen  T 2/12""",
    longDesc = 
u"""
83951-85-3
C2N2 Isocyanogen  linear?  *C=N-CN  SIGMA=1  STATWT=1  IB=16.3131  Nu=2404,2139,
965,884,470,223,1?  REF=Burcat G3B3 + Jacox Webbook  HF298=413.04+/-1.54 kJ
REF=ATcT C 2011  Max Lst Sq Error Cp @ 1300 K 0.39%.
""",
)

entry(
    index = 56,
    label = "C2(NO2)6",
    molecule = 
"""
1  N u0 p0 c+1 {2,S} {3,D} {4,S}
2  O u0 p3 c-1 {1,S}
3  O u0 p2 c0 {1,D}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {11,S}
5  N u0 p0 c+1 {4,S} {6,S} {7,D}
6  O u0 p3 c-1 {5,S}
7  O u0 p2 c0 {5,D}
8  N u0 p0 c+1 {4,S} {9,S} {10,D}
9  O u0 p3 c-1 {8,S}
10 O u0 p2 c0 {8,D}
11 C u0 p0 c0 {4,S} {12,S} {15,S} {18,S}
12 N u0 p0 c+1 {11,S} {13,S} {14,D}
13 O u0 p3 c-1 {12,S}
14 O u0 p2 c0 {12,D}
15 N u0 p0 c+1 {11,S} {16,S} {17,D}
16 O u0 p3 c-1 {15,S}
17 O u0 p2 c0 {15,D}
18 N u0 p0 c+1 {11,S} {19,S} {20,D}
19 O u0 p3 c-1 {18,S}
20 O u0 p2 c0 {18,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.62432,0.121633,-0.000140858,8.72738e-08,-2.39798e-11,10215.1,-4.71547], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[44.591,0.0134251,-6.44998e-06,1.20668e-09,-7.88597e-14,286.586,-189.446], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HexaNit  T 4/12""",
    longDesc = 
u"""
918-37-6
C2N6O12 HEXANITROETHANE C2(NO2)6 SIGMA=6 IAIBIC=6364500.E-117  [IR(NO2)=5.96]x6
IR(C(NO2)3)=68.4  V(2)-NO2=28 cm-1  V(3)-C(NO2)3=1000 cm-1   NU=1627,1353,
1143,858,375,335,113,1630(2),1268(2),1003(2),665(2),391(4),238(2),103(2),1621,
1333,888,582,376,240,1639(2),1285(2),820(2),633(2),383(2),347(2),155(2),92(2),
642,774  REF= Olga Dorofeeva Unpublished Results 1999   HF298=142.256+/-0.84 kJ
REF= Miroshnichenko et al  Russ Chem Bull Int Ed 59,(2010),890  {HF298=179.
+/-5.9 kJ  REF= Pepekin Miroshnichenko, Lebedev, Aspin Rus J. Phys. Chem. Eng.
Trans. 42,(1968),1583-1584;  HF298=179.0 kJ  REF=Keshavarz et al  Indian J Eng 
Mater Sci 13,(2006),542}  HF298(liq)=80.333+/-0.42 kJ  REF=Miroshnichenko et
al ibid.  Max Lst Sq Error Cp @ 1300 K 0.64%
""",
)

entry(
    index = 57,
    label = "C2S2",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 S u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93494,0.0252356,-4.4537e-05,4.04728e-08,-1.41865e-11,43625,10.3727], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.5584,0.00357347,-1.4444e-06,2.47666e-10,-1.53534e-14,42690.5,-11.5836], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 6/01""",
    longDesc = 
u"""
83917-77-5
C2S2  Dicarbon Disulfide  S=C=C=S From original TRC(6/01) data to 2000 extrapo-
lated using Wilhoit's polynomials to 6000. HF298=376.66 kJ HF0=373.8 kJ
Max Lst Sq Error Cp @ 5500 K 0.40%
""",
)

entry(
    index = 58,
    label = "CHCHCN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 C u0 p0 c0 {1,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,T}
5 N u0 p1 c0 {4,T}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15325,0.0206639,-1.33975e-05,7.77215e-10,2.02897e-12,51818.4,14.8729], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.9967,0.00750618,-2.683e-06,4.31684e-10,-2.57821e-14,50479.6,-10.1552], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""CH=CHCN    A12/04""",
    longDesc = 
u"""
203455-97-4
C3H2N CYANO-ETHYLENE RADICAL HC*=CH-CN  SIGMA=1  STATWT=2 IA=1.2735  IB=16.6759
IC=17.9494  Ir=0.0028296 V(3)=0.  ROSYM=1  Nu=3280,3087,2352,1661,1274,1018,835,
801,701,557,374  HF298=442.855 kJ HF0=445.486 kJ  REF=Burcat G3B3 calc
{HF298=97. kcal REF= MACKIE & COLKET 22nd COMBUST SYMP. 1990}   Max Lst Sq Error
Cp @ 6000 0.43%
""",
)

entry(
    index = 59,
    label = "cCH2NCH2CH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 N u0 p1 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.53058,0.0144707,2.46486e-05,-4.75223e-08,2.14727e-11,54195.5,17.7555], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.52011,0.0101772,-3.65071e-06,5.89007e-10,-3.52527e-14,52059.7,-15.8356], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""azete T12/14""",
    longDesc = 
u"""
287-24-1
C3H3N Cy azete Cy(-CH=CH-CH=N-)  SIGMA=1  STATWT=1  IA=4.5445  IB=6.2531  
IC=10.7977  Nu=3262,3226,3161,1661,1647,1283,1191,1111,961,881,874,854,690,634,
491  HF298=110.1495 kcal  REF=Burcat G3B3  Max Lst Sq Error Cp @ 200 K 0.76%
""",
)

entry(
    index = 60,
    label = "CH3CHCN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {8,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 N u0 p1 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90886,0.021025,-3.11711e-06,-1.06743e-08,5.98989e-12,25029.2,12.2021], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.65918,0.0121423,-4.32089e-06,6.93007e-10,-4.12937e-14,23485.9,-13.4087], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""CH3CH*-CN A01/05""",
    longDesc = 
u"""
3264-99-1
C3H4N 2-PROPIONITRILE RADICAL CH3-CH*CN  STATWT=2  SIGMA=1  IA=2.1315 IB=18.4528
IC=20.0640  Ir(CH3)=0.5065  ROSYM=3  [V(3)=1087 cm-1 REF=East & Radom JCP 106,
(1997),6655]  Nu=3199,3149,3071,3028,2152,1519,1500,1432,1401,1153,1112,1011,
868,591,575,426,223    HF298=222.71 kJ  HF0=232.213 kJ  REF=Burcat G3B3 calc.
Max Lst Sq Error Cp @ 6000 K 0.49%
""",
)

entry(
    index = 61,
    label = "Nitroglycerin",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {12,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  O u0 p2 c0 {3,S} {5,S}
5  N u0 p0 c+1 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p3 c-1 {5,S}
8  O u0 p2 c0 {2,S} {9,S}
9  N u0 p0 c+1 {8,S} {10,D} {11,S}
10 O u0 p2 c0 {9,D}
11 O u0 p3 c-1 {9,S}
12 O u0 p2 c0 {1,S} {13,S}
13 N u0 p0 c+1 {12,S} {14,D} {15,S}
14 O u0 p2 c0 {13,D}
15 O u0 p3 c-1 {13,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.70798,0.0952018,-7.18229e-05,1.66305e-08,3.01836e-12,-38897.5,7.78536], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[32.4464,0.024415,-9.67605e-06,1.65298e-09,-1.02555e-13,-46589.6,-131.431], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T05/98""",
    longDesc = 
u"""
55-63-0
C3H5N3O9 NG  Nitroglycerine      STATWT = 1  SYMNO = 2     IA = 113.023087
IB = 216.411718  IC = 260.003555  (Ir(NO2)= 5.96  ROSYM = 2  V(3) = 9.1 kcal)x3
NU = 3024,3014,2953,2941,2831,2142,3132,1537,1522,1363,1359,1329,1318,1303,1231,
1209,1160,1151,1145,1118,1093,1085,971,928,915,798,701,676,654,639,627,622,582,
478,470,463,409,379,348,317,312,276, 264,232,188,173,97.7,62,60,54.1,44.4
REF = BURCAT, JPCRD 29 (1999)63-130  HF298 =-66.7 kcal  REF=Miroshnichenko et al
Bul Acad. Sci. USSR, Chem Sci. (1988),1778.  HF298(liq)=-88.4+/-0.5 kcal
REF=Byrd & Rice JPC A 110,(2006),1005   Max Lst Sq Error Cp @ 1300 K 0.59%
""",
)

entry(
    index = 62,
    label = "NO2CH2CH2CH2NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  N u0 p0 c+1 {2,S} {12,D} {13,S}
5  N u0 p0 c+1 {3,S} {14,D} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 O u0 p3 c-1 {4,S}
14 O u0 p2 c0 {5,D}
15 O u0 p3 c-1 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.81228,0.0124295,8.69062e-05,-1.24692e-07,5.07948e-11,-20087.3,4.15693], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.9716,0.0237237,-8.80614e-06,1.44898e-09,-8.7797e-14,-24348.4,-51.8778], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T10/15""",
    longDesc = 
u"""
6125-21-9
C3H6N2O4  1,3-DiNitroPropane  O2N-(CH2)3-NO2  SIGMA=2  STATWT=1  IA=18.7057
IB=119.5001  IC=125.4863  [Ir(NO2)=5.97  ROSYM=2  V(3)=270. cm-1]x2  Nu=3164,
3150,3139,3096(2),3087,1675.3(2),1490,1486,1481,1437,1431,1400,1369,1327,1316,
1262,1221,1118,1112,1016,941,893,888,801,709,632,592,583,553,478.5,321,255,201,
127,58.68,[32.49,21.93  int.rot]  REF=Burcat B3LYP/6-31G(d)  HF298=-33.7 kcal  
REF=NIST 94  {HF298=-19.0 kcal  HF298(liq)=-207.+/-0.8 kJ REF=Lebedeva Rayadenko 
Russ JPC 42,(1968)1125 Engl.    Max Lst Sq Error Cp @ 6000 K 0.59%
""",
)

entry(
    index = 63,
    label = "C3H6(NO2)2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  N u0 p0 c+1 {1,S} {12,D} {13,S}
5  N u0 p0 c+1 {1,S} {14,D} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 O u0 p3 c-1 {4,S}
14 O u0 p2 c0 {5,D}
15 O u0 p3 c-1 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.93907,0.0315608,2.94413e-05,-6.16964e-08,2.69346e-11,-15904.8,4.58388], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.7932,0.0224013,-8.29508e-06,1.36246e-09,-8.24468e-14,-19961.7,-56.6313], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""1,1 d  T10/15""",
    longDesc = 
u"""
601-76-3
C3H6N2O4  1,1-Dinitropropane C2H5CH(NO2)2  SIGMA=1  STATWT=1  IA=39.8209
IB=54.3284  IC=78.4356  Ir(CH3)=0.51666  ROSYM=3  V(3)=1200. cm-1  [Ir(NO2)=5.96
ROSYM=2  V(3)=580. cm-1]x2   Nu=3165,3145,3140,3123,3092,3063,1696,1683,1534,
1529,1506,1452,1443,1393,1387,1340,1307,1282.5,1174,1123,1054,972.5,918,901,837,      
807,713,682,574,474,436,357,296,210,197,181,[90.2,62.5,24.83  int. rot.]
REF=Burcat B3LYP/6-31G(d)  HF298=-25.0 kcal  REF=NIST 94  {HF298=-19.0 kcal
REF=Indian J. Eng. Material Sci 13(6),2006,542}  HF298(liq)=-163+/-1 kJ
REF=Lebedeva Rayadenko Russ JPC 42,(1968)1125 Engl.    Max Lst Sq Error Cp @ 
1300 K 0.57%
""",
)

entry(
    index = 64,
    label = "C(CH3)2(NO2)2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p0 c+1 {1,S} {12,D} {13,S}
5  N u0 p0 c+1 {1,S} {14,D} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 O u0 p3 c-1 {4,S}
14 O u0 p2 c0 {5,D}
15 O u0 p3 c-1 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.49699,0.0362992,1.95282e-05,-5.47952e-08,2.54532e-11,-12889.7,5.69352], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.2887,0.021368,-7.88959e-06,1.29329e-09,-7.81515e-14,-16992.4,-59.4341], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 9/14""",
    longDesc = 
u"""
595-49-3
C3H6N2O4  DiMethyl-DiNitro-Methan  (CH3)2C(NO2)2  SIGMA=2  STATWT=1  IA=36.6249
IB=55.3949  IC=59.0722  [Ir(CH3)=0.51926  ROSYM=3  V(3)=273. cm-1]x2 
[Ir(NO2)=5.97  ROSYM=2  V(3)=1200. cm-1]x2  Nu=3187(2),3164,3159,3086,3082,1690,
1678,1530,1519,1503(2),1465,1430,1415,1389,1276,1222,1198,1037,972,959,860,855,
756,729,659,555,476,429,350,339,297,268  REF=Burcat B3LYP/6-31G(d)  HF298=-19.0
+/-5.1 kcal  REF=Keshavarz et al Indian J. Eng. Mater. Sci 13,(2006),542   Max
Lst Sq Error Cp @ 6000 K 0.53%.
""",
)

entry(
    index = 65,
    label = "CH3CH2CH2S",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  S u1 p2 c0 {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.99141,0.00715731,5.95887e-05,-8.37611e-08,3.41008e-11,6910.79,6.4203], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.44634,0.0181967,-6.5609e-06,1.05822e-09,-6.32705e-14,4614.01,-22.0499], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T12/08""",
    longDesc = 
u"""
4985-58-4
C3H7S Propylthiol Radical C2H5CH2S*  SIGMA=1  STATWT=2  IA=3.1580  IB=35.6361
IC=37.2425  Ir(CH3)=1.4885 ROSYM=3  V(3)=1200. cm-1  Ir(C2H5)=4.7212  ROSYM=2
V(3)=2000. cm-1 est.  Nu=3119,3114,3089,3057,3044,3032,3019,1536,1530,1518,1462,
1441,1383,1329,1275,1250,1118,1044,985,909,778,726.5,487,366,247  HF298=18.072
kcal {HF298=17.3 kcal  REF=NIST 94}  Max Lst Sq Error Cp @ 6000 K 0.56%.
""",
)

entry(
    index = 66,
    label = "C3N2O",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 C u0 p0 c0 {3,S} {6,T}
6 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90256,0.0360775,-5.74096e-05,4.90465e-08,-1.66007e-11,27716.4,12.1452], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2505,0.00552056,-2.08011e-06,3.4645e-10,-2.11883e-14,26062.9,-23.6322], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""NC-CO-CN   T 6/03""",
    longDesc = 
u"""
1115-12-4
C3N2O  Oxopropandinitrile NC-CO-CN  SIGMA=2  STATWT=1  IAIBIC=14666. E-117
NU=2230,1711,712,553,127.5,307,712,208.2,2230,1124,550,245.2 HF298=247.5+/-6.4
kJ  HF0=246.5+/-6.4 kJ  REF= Dorofeeva et al, 30, (2001), 475  Max Lst Sq Error
Cp @ 1300 K  0.45%
""",
)

entry(
    index = 67,
    label = "NCCHCHCN",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 C u0 p0 c0 {4,S} {6,T}
6 N u0 p1 c0 {5,T}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08972,0.0301706,-2.22304e-05,6.22606e-09,3.38799e-13,37731.2,11.4968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.261,0.0105849,-3.83687e-06,6.23219e-10,-3.74698e-14,35697.6,-25.6899], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Fumaroni T05/04""",
    longDesc = 
u"""
764-42-1
C4H2N2  FUMARONITRILE trans-NC-CH=CH-CN SIGMA=2  STATWT=1  IA=1.7899  IB=56.8850
IC=58.6750  Nu=3213,3207,2357,2340,1680,1334,1304,1034(2),982,864,566,539,537,
391,258,137,127.4  HF298=331.+/-3 kJ HF0=334.8 kJ  REF= Burcat G3B3 calc.
{HF298=340+/-3 kJ REF=Boyd et al JPC 71,(1967),2187}  Max Lst Sq Error Cp @
1300 K 0.47%
""",
)

entry(
    index = 68,
    label = "Pyrazine",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {5,S} {8,S}
3  C u0 p0 c0 {4,S} {5,D} {9,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  N u0 p1 c0 {2,S} {3,D}
6  N u0 p1 c0 {1,S} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.31169,0.0141004,6.44438e-05,-1.01639e-07,4.33905e-11,22143.8,19.9919], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5513,0.0160367,-5.88637e-06,9.64222e-10,-5.83155e-14,18418.3,-33.9434], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 9/96""",
    longDesc = 
u"""
290-37-9
C4H4N2 PYRAZINE (SIX MEMBERED RING WITH N IN PARA POSITION)   SIGMA=4  STATWT=1
IA=12.8266  IB=13.8011  IC=26.6277  NU= 3037,3031,3015,3014,1615,1579,1493,1404,
1337,1215,1227,1074,1010,1003,1001,995,982,935,801,748,695,584,435.7,380.6
REF= C. Melius Database #PJ11 HF298=46.8+-0.3 Kcal   REF=Pedley, Nylor & Kirby
Max Lst Sq Error Cp @ 200 K **1.06 %**.
""",
)

entry(
    index = 69,
    label = "Pyrimidine",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {9,S}
4  C u0 p0 c0 {5,D} {6,S} {10,S}
5  N u0 p1 c0 {2,S} {4,D}
6  N u0 p1 c0 {3,D} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.63714,0.0119774,6.83832e-05,-1.0465e-07,4.42186e-11,22212.5,18.6564], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4317,0.016151,-5.92923e-06,9.71339e-10,-5.87497e-14,18552,-33.2492], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 9/96""",
    longDesc = 
u"""
289-95-2
C4H4N2 PYRIMIDINE (SIX MEMBERED RING WITH N IN meta POSITION) SIGMA=2  STATWT=1
IA=13.10379  IB=13.46  IC=26.57  NU=3045,3033,3015,3010,1608,1607.5,1466,1405,
1357,1214,1126,1083,1040,1039,1032,1010,985,978,813.7,704,671,610,411.7,371.3
REF=C.Melius Database #PI11  HF298=47.0+-0.2 Kcal REF=Pedley, Naylor & Kirby
Max Lst Sq Error Cp @ 200 K **1.08 %**.
""",
)

entry(
    index = 70,
    label = "Uracil",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  N u0 p1 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {8,D}
6  N u0 p1 c0 {1,S} {5,S} {12,S}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {5,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00318544,0.0482332,-9.46927e-06,-2.96144e-08,1.75709e-11,-38270.9,26.1588], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.7707,0.017223,-6.22609e-06,1.01024e-09,-6.07182e-14,-42750.6,-52.3073], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T07/12""",
    longDesc = 
u"""
66-22-8 ?
C4H4N2O2 Uracil (DNA/RNA Nucleobase) SIGMA=1  STATWT=1  IA=21.5490  IB=41.6282
IC=63.1771  Nu=3601,3559,3207,3161,1811,1776,1657,1474,1397,1381,1355,1211,
1176,1176,1072,975,960,948,814,762,759,729,682,558,550,533,509,394,380,166,149
HF298=-301.5+/-2.5 kJ  REF=Dorofeeva & Vogt JCED 54,(2009),1348  {HF298=-303.1
+/-2.3 kJ  REF=Nabavian, Sabbah, et al J Chim. Phys 74,(1977),115}
HF298(cr)=-429.6+/-0.6  REF=Dorofeeva & Vogt JCED 54,(2009),1348  Max Lst Sq
Error Cp @ 1300 K 0.49%
""",
)

entry(
    index = 71,
    label = "Thiophene",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,D} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {8,S}
4 S u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {1,D} {4,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.533957,0.0304279,1.57129e-05,-5.21637e-08,2.60142e-11,12705.4,27.226], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3362,0.0131485,-4.75133e-06,7.70341e-10,-4.62622e-14,9274.99,-31.4803], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T11/08""",
    longDesc = 
u"""
110-02-1
C4H4S THIOPHENE (CY)  SIGMA=2 IA=10.5311  IB=15.6737  IC=26.2048   NU=3126,3125,
3098(2),1507,1409,1360,1256,1085,1083,1036,898,872,867,839,751,712,683,608,565,
452  HF298=115.96 kJ  REF=Burcat G3B3  {HF298=114.9 kJ  REF=Dorofeeva & Gurvich
JPCRD 24,(1995),1351;  HF298=116.4 kJ REF=Sunner Acta Chem Scand 17,(1963),728 ;
HF298=115.0+/-1 kJ  REF=Hubbard Scott et al JACS 77,(1955),5855}  Max Lst Sq
Error Cp @ 200 K 0.99%
""",
)

entry(
    index = 72,
    label = "Pyrrolidine",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  N u0 p1 c0 {3,S} {5,S} {12,S}
5  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.54759,-0.0202998,0.000173431,-2.15285e-07,8.47212e-11,-2330.33,5.65934], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.19145,0.027302,-9.88748e-06,1.60491e-09,-9.64626e-14,-5928.05,-26.5465], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 3/95""",
    longDesc = 
u"""
123-75-1
C4H9N PYRROLIDINE (TETRAHYDROPYRROLE, TETRAMETHYLENEIMINE)  IAIBIC=3330.5
IR=1.119  ROSYM=2. V(2)=280. cm-1    NU=3367,2970(2),2882(4),2818(2),1480(2),
1468(2),1418,1348,1299,1284,1239,1220,1205,1171,1136,1105,1080,1053,1025,980,
925,909,872,844,792,612,570,145   HF298=-3.59+/-0.80 kJ  REF=Das et. al JPCRD 22
(1993), 659  Max Lst Sq Error Cp @ 200 K **1.48**
""",
)

entry(
    index = 73,
    label = "C4H9SH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  S u0 p2 c0 {4,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.43822,-0.000792238,0.000102591,-1.31946e-07,5.20772e-11,-13186.8,-0.800716], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.6273,0.0268608,-9.55936e-06,1.5306e-09,-9.10324e-14,-15754.4,-25.8578], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T02/13""",
    longDesc = 
u"""
109-79-5
C4H10S  1-Butanethiol  C4H9SH  SIGMA=1  STATWT=1  IA=5.2637  IB=63.8326
IC=67.0085  Ir(CH3)=0.5145  ROSYM=3 V(3)=270. cm-1  Ir(SH)=0.55764  ROSYM=1
V(3)=600. cm-1  Ir(C2H5)=4.6966  ROSYM=1  V(3)=1200. cm-1  Nu=3122.6,3116,3111,
3078,3069,3054,3046,3039,3028,2681,1542,1529.6(2),1518(2),1443.5,1417,1354(2),
1324.5,1277,1247.5,1144,1094,1072,1040,939.5,934,855,803,749,738,390,318.6,249,
187  HF298=-20.536+/-2 kcal  REF=Burcat G3B3  {HF298=-26.0 kcal  REF=NIST 94}
Max Lst Sq Error Cp @ 200 K & 6000 K 0.57%.
""",
)

entry(
    index = 74,
    label = "C4N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 N u0 p1 c0 {5,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17476,0.0476127,-8.98017e-05,8.4151e-08,-2.97993e-11,61524.3,11.662], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4154,0.00571824,-2.12579e-06,3.50943e-10,-2.13328e-14,60000,-26.7166], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""g 6/01""",
    longDesc = 
u"""
1071-98-3
C4N2  CARBON SUBNITRID (2-BUTYNEDINITRILE)  SIGMA=2  STATWT=1  B0=0.044891 cm-1
Nu=2333,2267,2241,1154,640,504(2),471(2),263(2),107(2) REF=Khanna et al Spectro-
chim Acta 43A,(1987),421 & Brown et al JPC 93(1989),5679  HF298=529.2+/-0.8 kJ
REF=TRC 12/93  Max Lst Sq Error Cp @ 1300 K 0.43%
""",
)

entry(
    index = 75,
    label = "CPD-triNT",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {15,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S}
5  C u0 p0 c0 {1,S} {6,D} {16,S}
6  C u0 p0 c0 {5,D} {7,S} {10,S}
7  N u0 p0 c+1 {6,S} {8,D} {9,S}
8  O u0 p2 c0 {7,D}
9  O u0 p3 c-1 {7,S}
10 C u0 p0 c0 {6,S} {11,D} {17,S}
11 C u0 p0 c0 {1,S} {10,D} {12,S}
12 N u0 p0 c+1 {11,S} {13,D} {14,S}
13 O u0 p2 c0 {12,D}
14 O u0 p3 c-1 {12,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.29494,0.0668079,-3.53474e-05,-9.13677e-09,1.03714e-11,14423.6,2.64146], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[26.0774,0.0177275,-6.91292e-06,1.17034e-09,-7.22141e-14,8215.1,-106.88], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""7/14""",
    longDesc = 
u"""
C5H2N3O6  1,3,4-triNitro-2,4-Cyclopentadiene-1-yl  C5H2(NO2)3  SIGMA=2  STATWT=2
A=3.6246  B=1.6655  C=1.1890  [Ir(NO2)=5.96  ROSYM=2  V(3)=600. cm-1]x3
Nu=3301,3297,1650,1641,1631,1582,1486,1431,1413,1391,1364,1309,1173,1165,1086,
1068,870,864,858,845,802,752,742,728,712,648,589,548,510,479.5,361,351,317,268,
235,163,159,135,101  REF=Burcat B3LYP/6-31G(d)  HF298=155.034 kJ  REF=Pitz &
Westbrook  Proc. Comb. Inst. 31,(2007),2343  Max Lst Sq Error Cp @ 1300 K 0.53%
""",
)

entry(
    index = 76,
    label = "NCCHCHCCH",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {7,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 C u0 p0 c0 {4,S} {6,T}
6 N u0 p1 c0 {5,T}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.68494,0.0434234,-4.45293e-05,2.43655e-08,-5.26531e-12,48743.8,17.5459], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.2215,0.0121359,-4.33358e-06,6.96956e-10,-4.16178e-14,46324.8,-30.557], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A01/05""",
    longDesc = 
u"""
13086-68-5
C5H3N  CYANO VINYL ACETYLENE HCC-CH=CH-CN  SIGMA=1  STATWT=1  IA=1.7817
IB=57.4233  IC=59.2050  No Internal Rotation  Nu=3492,3209,3181,2341,2222,1669,
1335,1304,1052,1034,981,860,641,623,558,543,521,384,256,134,126  HF298=422.6 kJ
HF0=426.538 kJ  REF=Burcat G3B3 calc   {HF298=416.3 kJ REF=MACKIE & COLKET
22 COMB. SYMP. 1990}  Max Lst Sq Error Cp @ 6000 0.44%
""",
)

entry(
    index = 77,
    label = "CHCHCHCHCN",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,D}
2  H u0 p0 c0 {1,S}
3  C u0 p0 c0 {1,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {5,S} {7,T}
7  N u0 p1 c0 {6,T}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68687,0.0353836,-1.44995e-05,-1.0329e-08,8.19906e-12,58260.5,15.9522], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7574,0.0138995,-4.96375e-06,7.9519e-10,-4.73266e-14,55621.7,-31.6349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""A 4/05""",
    longDesc = 
u"""
189230-13-5
C5H4N 1,3-Butadiene-4-cyano-1-yl RADICAL  *CH=CH-CH=CH-CN   SIGMA=1   STATWT=2
IA=3.0692  IB=56.2707  IC=59.3398  Ir(*CH=CH-)=2.4298  ROSYM=1  [V(3)=1049. cm-1
REF=Langowski et al THEOCHEM 258,(1992),341]  Nu=3263,3198,3186,3126,2337,1671,
1636,1338,1328,1254,1144,1035,1005,919,864,843,683,567,505,437,315,201,146
HF298=120.106 kcal REF=Burcat  G3B3 calc QCISD/SCF=QC  {HF298=114+/-3 KCAL
REF=Mackie & Colket, 22 COMB. Symp 1990}.  Max Lst Sq Error Cp @ 6000 K 0.45%.
""",
)

entry(
    index = 78,
    label = "OroticAcid",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {11,S}
3  N u0 p1 c0 {1,S} {6,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {9,D}
5  N u0 p1 c0 {4,S} {6,S} {12,S}
6  C u0 p0 c0 {3,S} {5,S} {10,D}
7  C u0 p0 c0 {1,S} {8,S} {14,D}
8  O u0 p2 c0 {7,S} {15,S}
9  O u0 p2 c0 {4,D}
10 O u0 p2 c0 {6,D}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {7,D}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.879245,0.0642948,-2.29281e-05,-2.59099e-08,1.78583e-11,-67688.8,25.5436], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.5274,0.0197861,-7.22573e-06,1.17745e-09,-7.09125e-14,-73502.8,-78.0704], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""O  T 5/13""",
    longDesc = 
u"""
65-86-1
C5H4N2O4  Orotic acid  1,2,3,6-Tetrahydro-2,6-dioxo-4-pyrimidinecarboxylic acid
SIGMA=1  STATWT=1 IA=48.5538  IB=94.8494  IC=143.4022  Ir(COOH)=4.4406  ROSYM=1
V(3)=280. cm-1  Nu=3710,3700,3685,3278,1854,1661,1644,1539,1484,1463.5,1373,
1366,1270,1224,1189,1163,1071,1006,952,872,802,789,717,683,650,627,589,586,573,
568,505.5,418.5,394,330,228,203,179,139.5  REF=Burcat B3LYP/6-31G(d)
HF298=-128.8 kcal  REF=NIST 94  Max Lst Sq Error Cp @ 1300 K 0.47%.
""",
)

entry(
    index = 79,
    label = "Pyridine",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  N u0 p1 c0 {4,D} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.23341,0.0140843,7.37761e-05,-1.1406e-07,4.84333e-11,15404.7,20.4145], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.7374,0.0184113,-6.70894e-06,1.0937e-09,-6.59272e-14,11477.1,-35.5805], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/10""",
    longDesc = 
u"""
110-86-1
C5H5N PYRIDINE (AZINE) SIGMA=2  STATWT=1  IA=13.9036  IB=14.4578  IV=28.3613
NU=3094.2,3086.9,3072.8,3042.4,3030.1,1583.9,1580.5,1483.4,1441.9,1362.3,1227,
1218,1143.3,1079,1071.9,1031.7,1007,991.4,980,936.6,880,744,700.3,652,601.4,
403.3,373  REF=Das et al (1993)  HF298=140.080+/-8. kcal  REF=Burcat G3B3
{HF298=140.37+/-0.54 kJ REF=Das et al. JPCRD 22,(1993),659}  Max Lst Sq Error Cp
@ 200 K **1.12%**
""",
)

entry(
    index = 80,
    label = "nitPDE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S}
5  C u0 p0 c0 {1,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {6,S} {8,D} {12,S}
8  C u0 p0 c0 {1,S} {7,D} {13,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.87277,0.0260567,6.03726e-05,-1.0736e-07,4.73168e-11,13177.8,21.3129], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.5943,0.0198283,-7.28348e-06,1.19192e-09,-7.19947e-14,8462.36,-50.8444], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 4/13""",
    longDesc = 
u"""
58683-60-6
C5H5NO2 1-NitroCyclo-2,4-Pentadiene  SIGMA=2  STATWT=1  IA=18.2725  IB=48.4822
IC=61.5868  Ir(NO2)=5.96  ROSYM=2  V(3)=140. cm-1  Nu=3278,3275,3239,3227,3060,
1676,1664.5,1597,1428,1398.5,1324.5,1280,1251,1141,1121,1057,1020,965,961.5,959,
911,854.5,810,794.5,725,701,623,540.5,462,404.5,221.5,144  HF298=30.281+/-2 kcal
REF=Burcat G3B3  Max Lst Sq Error Cp @ 200 K 0.84%
""",
)

entry(
    index = 81,
    label = "Glutamine",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  N u0 p1 c0 {2,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {8,S} {17,S}
7  N u0 p1 c0 {6,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,S} {20,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77081,0.0532503,2.30046e-05,-7.08813e-08,3.2978e-11,-79555.5,13.6858], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.0865,0.0316902,-1.13786e-05,1.83399e-09,-1.09621e-13,-85191.4,-76.2339], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 2/15""",
    longDesc = 
u"""
56-85-9
C5H10N2O3 Glutamine (amino acid) H2N-C(O)-CH2CH2CH(NH2)COOH SIGMA=1  STATWT=1
IA=29.5723  IB=152.7438  IC=158.4153  Ir(OH)=0.1390  ROSYM=1  V(3)=272. cm-1
[Ir(NH2)=0.2827  ROSYM=2  V(3)=580. cm-1]x2  Ir(COOH)=4.4058  ROSYM=1 V(3)=2400.
REF=Burcat B3LYP/6-31G(d)  Nu=3739,3604,3574,3418,3304,3103,3075,3054,3037,3032,
1850,1769,1680,1622,1466,1465,1459,1423,1410,1385,1337,1301,1284,1226,1210,1201,
1137,1097,1075,1034,984,946,921,881,837,768,747,672,611,566,543,522,479,420,381,
364,288,251,231,205,[169,79,40,29.7 inter rot]  HF298=-151.o+/-1 kcal REF=Karton
Martin et al Theor Chem Acc 133,(2014),1453  Max Lst Sq Error Cp @ 1300 K 0.52%.
""",
)

entry(
    index = 82,
    label = "C5N4",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
4 C u0 p0 c0 {3,S} {5,T}
5 N u0 p1 c0 {4,T}
6 C u0 p0 c0 {3,S} {7,T}
7 N u0 p1 c0 {6,T}
8 C u0 p0 c0 {3,S} {9,T}
9 N u0 p1 c0 {8,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47251,0.0693758,-0.000119038,1.03964e-07,-3.50849e-11,77960.9,12.7882], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.704,0.00872411,-3.24111e-06,5.34885e-10,-3.2508e-14,75303,-50.1455], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""C(CN)4      T 6/14""",
    longDesc = 
u"""
24331-09-7
C5N4  MethaneTetraCarboNitrile C(CN)4  SIGMA=12  STATWT=1  A=B=C=0.051 cm-1
Nu=2391,2382(3),1072(2),583,567(2),552(3),344(3),147(3),111(2)  REF=CCCBDB NIST
Comparrison Calculations G3B3  HF298=672.80+/-9.20 kJ  REF=Barnes & Mortimer JCT
5,(1973),371  HF298(c)=611.6+/-1.8 kJ  REF=Barnes & Mortimer ibid.  Max Lst Sq
Error Cp @ 1300 K ).42%.
""",
)

entry(
    index = 83,
    label = "C6H3N2O4",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {5,S}
2  O u0 p3 c-1 {6,S}
3  O u0 p2 c0 {5,D}
4  O u0 p2 c0 {6,D}
5  N u0 p0 c+1 {1,S} {3,D} {7,S}
6  N u0 p0 c+1 {2,S} {4,D} {8,S}
7  C u0 p0 c0 {5,S} {9,B} {11,B}
8  C u0 p0 c0 {6,S} {9,B} {10,B}
9  C u0 p0 c0 {7,B} {8,B} {13,S}
10 C u0 p0 c0 {8,B} {12,B} {14,S}
11 C u0 p0 c0 {7,B} {12,B} {15,S}
12 C u1 p0 c0 {10,B} {11,B}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {10,S}
15 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33144,0.0454141,2.58179e-05,-7.58728e-08,3.58995e-11,33225.4,19.2774], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.2769,0.0196212,-7.48367e-06,1.25241e-09,-7.67525e-14,27190.8,-78.9564], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""1,3-Di  T 4/13""",
    longDesc = 
u"""
118903-54-1
C6H3(NO2)2  1,3-DiNitro-5-yl Benzen Radical SIGMA=2  STATWT=2  IA=40.7663
IB=137.762  IC=178.5283  [Ir(NO2)=5.96  ROSYM=2  V(3)=280. cm-1]x2  Nu=3280,
3142.5(2),1670,1667,1636,1584.5,1450,1443,1401,1390,1370,1244,1152,1090(2),1007,
959.5,930,917,894.5,844,763.5,733,730.5,656,634,570,515,466,456,405,352,304,
190.4,161,158  REF=Burcat B3LYP/6-31G(d)  HF298=72.2 kcal  REF=NIST 94
{HF298=73.87 kcal  REF=Pitz database Therm 2004}  Max Lst Sq Error Cp @ 1300 K
0.56%
""",
)

entry(
    index = 84,
    label = "TriNitroBenzen",
    molecule = 
"""
1  O u0 p3 c-1 {7,S}
2  O u0 p3 c-1 {8,S}
3  O u0 p3 c-1 {9,S}
4  O u0 p2 c0 {7,D}
5  O u0 p2 c0 {8,D}
6  O u0 p2 c0 {9,D}
7  N u0 p0 c+1 {1,S} {4,D} {10,S}
8  N u0 p0 c+1 {2,S} {5,D} {11,S}
9  N u0 p0 c+1 {3,S} {6,D} {12,S}
10 C u0 p0 c0 {7,S} {13,B} {15,B}
11 C u0 p0 c0 {8,S} {13,B} {14,B}
12 C u0 p0 c0 {9,S} {14,B} {15,B}
13 C u0 p0 c0 {10,B} {11,B} {16,S}
14 C u0 p0 c0 {11,B} {12,B} {17,S}
15 C u0 p0 c0 {10,B} {12,B} {18,S}
16 H u0 p0 c0 {13,S}
17 H u0 p0 c0 {14,S}
18 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18818,0.102515,-0.000105643,5.50716e-08,-1.13738e-11,3118.93,19.5711], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[28.7195,0.0208056,-8.0368e-06,1.35348e-09,-8.32406e-14,-3921.48,-115.711], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 5/98""",
    longDesc = 
u"""
99-35-4
C6H3(NO2)3    1,3,5-Tri-Nitro-Benzene   SYMNO = 6  STATWT = 1  IA = 111.42859
IB = 172.18627  IC = 252.862147  Ir(NO2)=5.96  ROSYM = 2  V(2) = 3.11 kcal
NU = 3071,3038,2993,1923,1913,1742,1720,1671,1594,1580,1431,1368,1321,1209,1183,
1121,1113,1018,1000,970,952,939,843,778,751,748,688,680,644,591,568,522,504,448,
393,350,335,323,294,256,251,147,129,87.5,66.  REF =BURCAT, TAE Report # 824 1998
HF298=14.9 kcal  REF=Pedley, Naylor & Kirby 1986  HF298(sol)=-8.9+/-3 kcal
REF=Byrd & Rice JPC A 110,(2006),1005 Max Lst Sq Error Cp @ 1300 K 0.53%
""",
)

entry(
    index = 85,
    label = "C6H3N3O7",
    molecule = 
"""
1  O u0 p2 c0 {14,S} {19,S}
2  O u0 p3 c-1 {8,S}
3  O u0 p3 c-1 {9,S}
4  O u0 p3 c-1 {10,S}
5  O u0 p2 c0 {8,D}
6  O u0 p2 c0 {9,D}
7  O u0 p2 c0 {10,D}
8  N u0 p0 c+1 {2,S} {5,D} {11,S}
9  N u0 p0 c+1 {3,S} {6,D} {12,S}
10 N u0 p0 c+1 {4,S} {7,D} {13,S}
11 C u0 p0 c0 {8,S} {14,B} {15,B}
12 C u0 p0 c0 {9,S} {14,B} {16,B}
13 C u0 p0 c0 {10,S} {15,B} {16,B}
14 C u0 p0 c0 {1,S} {11,B} {12,B}
15 C u0 p0 c0 {11,B} {13,B} {17,S}
16 C u0 p0 c0 {12,B} {13,B} {18,S}
17 H u0 p0 c0 {15,S}
18 H u0 p0 c0 {16,S}
19 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61304,0.0771088,-1.51896e-05,-4.85978e-08,2.84717e-11,-20767.4,22.779], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[28.4273,0.0236094,-9.05319e-06,1.51547e-09,-9.27895e-14,-28692.8,-114.672], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""PicricaciT02/12""",
    longDesc = 
u"""
88-89-1
C6H3N3O7 2,4,6-TriNitroPhenol (Picric Acid)  SIGMA=2  STATWT=1  IA=149.7947
IB=160.5608  IC=307.1843  Ir(OH)=0.1336  ROSYM=1  V(3)=1212. cm-1 [Ir(NO2)=4.722
ROSYM=2  V(3)=260. cm-1]x3  Nu=3309,3271,3268,1699,1672,1655,1630,1613,1523,
1486,1436,1400,1389,1365,1336,1323.5,1199,1186,1101.5,978,970,956.934,840,837,
792.5,780,758,742.5(2),719.5,707,657,550,543,507,452,408,389,349,345,328,318,
203,189.5,155,127  REF=Burcat B3LYP/6-31G(d)  HF298=-139.5 kJ  REF=NIST 94 estim
HF298(sol)=-217.9 kJ  REF=Finch & Smith Thermochim. Acta 69,(1983),375   Max Lst
Sq Error Cp @ 1300 K 0.53%.
""",
)

entry(
    index = 86,
    label = "SOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69441,0.000394328,1.10155e-05,-1.63103e-08,7.03353e-12,-1992.57,7.31636], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.37246,0.00201399,-6.50854e-07,9.74413e-11,-5.52225e-15,-2285.78,3.13657], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T04/07""",
    longDesc = 
u"""
62803-12-7
S-OH RADICAL  STATWT=2  SIGMA=1  IA=0.1222028  IB=5.0098556  IC=5.132059
REF=Melius S9 NU=3700,1176,830  REF=Wang & Wilson JPC 109,(2005),7187
HF298=-1.6+/-0.5. kcal  REF=Denis CPL 402,(2005),289  {HF298=-1.062+/-1.9 kcal
REF=Burcat G3B3 calc;  HF298=-4.994+/-2.1 kcal  REF=C. Melius BAC/MP4 DATABASE,
S8  Problematic specie!}  Max Lst Sq Error Cp @ 400 K 0.35%
""",
)

entry(
    index = 87,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13565,-0.00369243,2.0517e-05,-2.40531e-08,9.17084e-12,-3823.72,5.8877], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.34724,0.00253372,-9.51431e-07,1.58095e-10,-9.65295e-15,-4208.94,3.15888], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HS=O         T04/07""",
    longDesc = 
u"""
62470-71-7
HS=O RADICAL   STATWT=2  SIGMA=1  IA=0.272571  IB=4.331163   IC=4.603734
REF=Melius S8  NU=1026,1164,2271  REF=Wang & Wilson JPC 109,(2005),7187
HF298=-5.2+/-0.5 kcal  REF=Denis CPL 402,(2005),289  {HF298=-4.442+/-1.9 kcal
REF=Burcat G3B3 calc  HF298=-1.143+/-1.37 kcal  REF=C. MELIUS  BAC/MP4 Database
S9; HF298=5.0 kcal  REF=Benson 1979  Problematic specie}  Max Lst Sq Error Cp @
6000 K 0.40%
""",
)

entry(
    index = 88,
    label = "SH",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68467,0.00324609,-1.28635e-05,1.69512e-08,-7.07595e-12,15903.6,2.01782], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.03153,0.00125805,-4.05524e-07,6.19648e-11,-3.50862e-15,16206,6.15022], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""IU2/03""",
    longDesc = 
u"""
13940-21-1
SH  T0(STATWT)=0(2), Be=9.461  WE=2711.6  WEXE=59.0  ALFAE=0.27   T0=376.96(2)
    T0=31038(2)  Be=8.5214  WE=1979.8  WEXE=97.65  ALFAE=0.464  DE=6.36E-4
    T0=59641(2)  Be=8.785   WE=2557.   WEXE=56.8   ALFAE=0.259  DE=8.2E-4
T0=63900(4),71195(4),71318(2),76708(4) Be=9.4611 WE=2711.6  WEXE=59.0
ALFAE=0.27  DE=4.8E-4   T0=79343(4),80848(4)   HF298=141.87+/-0.52 kJ HF0=141.24
+/-0.52 kJ REF=Csazar Leninger & Burcat J.Chem Phys 2003  {HF298=34.+/-0.3 kcal
REF=Denis J Sulfur Chem 29,(2008),327}  Max Lst Sq Error Cp @ 400 K 0.47%.
""",
)

entry(
    index = 89,
    label = "HOSO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73733,0.00930978,-3.85404e-06,-4.07783e-09,3.09632e-12,-29826.1,10.1081], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.39567,0.00256432,-8.77533e-07,1.37135e-10,-8.02657e-15,-30536.7,-3.6268], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HO-SO Rad  T09/10""",
    longDesc = 
u"""
12306-07-9
HSO2 HOSO RADICAL STATWT=2 SIGMA=1 IA=2.397408  IB=8.7861523  IC=11.010938
IR=0.11955  ROSYM=2  V(3)=409.2 cm-1  NU=403.6,[776],1011,[1168,3544]
HF298=-56.315+/-2 kcal  REF=Burcat G3B3  {HF0=-56.751+/-2.5 kcal  REF=B McBride
NASA TP-2002-211556;  HF298=-61.158 kcal  REF=C. MELIUS BAC/MP4 Database}   Max
Lst Sq Error Cp @ 6000 K 0.20%
""",
)

entry(
    index = 90,
    label = "HSO3",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p0 c0 {1,S} {3,D} {5,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18471,0.0192278,-1.85976e-05,7.95502e-09,-9.42255e-13,-44215.7,13.0497], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.1942,0.00377828,-1.34903e-06,2.17197e-10,-1.29875e-14,-45501.3,-12.3825], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T10/10""",
    longDesc = 
u"""
104267-22-3
HSO3 HO-SO2 RADICAL STATWT=2  SIGMA=1 IA=9.4168978  IB=9.7757253  IC=16.401348
IR=0.125875  ROSYM=1 V(3)=954.8 cm-1  NU=323.6,433,[538,759,1097,1296,1309,3540]
REF=C. MELIUS BAC/MP4 Database, Private communication S19 HF298=-84.577+/-2 kcal
REF=Burcat G3B3  {HF298=-92.1 KCAL REF=Margitan J.J. JPC 88 (1984), 3314
HF298=-67.62+/-3.47  kcal  REF=Melius Database S19 (1992)}   Max Lst Sq Error
Cp @ 6000 K 0.18%.
""",
)

entry(
    index = 91,
    label = "HSS",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96324,0.00855502,-1.00388e-05,6.25269e-09,-1.52826e-12,51449.8,11.58], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.00285,0.00153334,-3.71726e-07,4.1231e-11,-1.83713e-15,50946.2,1.3679], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""RRHO         T 4/02""",
    longDesc = 
u"""
14541-24-3
HS2 HYDROTHIOSULFENO RADICAL RRHO SIGMA=1  STATWT=2  A0=9.9261912 B0=0.2643802
C0=0.2571927   Nu=2463,903,595. HF298=25+/-2.5 kcal exper. REF=Decker et, al
Int. J. Mass. Spec,185-187,(1999),727-747.  {HF298=25.0+/-0.5 kcal  REF=Denis
J Sulfur Chem 29,(2008),327}  Max Lst Sq Error Cp @ 6000 K 0.29%
""",
)

entry(
    index = 92,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12024,-0.00187907,8.21427e-06,-7.06426e-09,2.14235e-12,-3682.15,1.53174], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97879,0.0035976,-1.22803e-06,1.96833e-10,-1.16716e-14,-3516.08,6.77921], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""anharmonic    g 4/01""",
    longDesc = 
u"""
7783-06-4
H2S  anharmonic  SIGMA=2  STATWT=1  A0=10.3613  B0=9.0162  C0=4.7314
Nu=2614.56,1182.68,2627.9  X11=-24.69  X22=-5.72  X33=-24.28  X12=-19.58
X23=-21.3  X13=-95.10  DARD=47.1 B000=9.0162  ALFAB1=0.185  ALFAB2=-0.2703
ALFAB3=0.1392  ALFAA1=0.1057  ALFAA2=-0.2975  ALFAA3=.1703  ALFAC1=0.0697
ALFAC2=0.0619  ALFAC3=0.0541  TAAA=-0.00504   TBBB=-0.00825  TCCC=-0.00027
TAAB=0.00412   TBBC=-0.00059  TAAC=-0.00053   TABA=-0.00073  HF298=-20.60+/-0.5
kJ  REF=Gurvich 1989 {HF298=-20.6+/-0.5 kJ  REF=Cox Wagman 1984  HF298=-20.5 kJ
REF=JANAF 77;  HF298=20.5+/-2.1 kJ  REF=Denis  J Sulfur Chem 29,(2008),327}  Max
Lst Sq Error Cp @ 6000 K 0.37%
""",
)

entry(
    index = 93,
    label = "H2SO4",
    molecule = 
"""
1 S u0 p0 c0 {2,D} {3,D} {4,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,S} {6,S}
5 O u0 p2 c0 {1,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.53388,0.0310348,-4.10422e-05,2.95752e-08,-8.81459e-12,-90545.9,3.93961], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.3355,0.00560829,-1.94574e-06,3.07136e-10,-1.8111e-14,-92108.7,-29.6094], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 8/03""",
    longDesc = 
u"""
7664-93-9
H2SO4  SULFURIC ACID  SIGMA=2  STATWT=1  IAIBIC=4669.95E-117  NU=3563,1216,1136,
831,548,420,355,3567,1452,1157,882,558,475, Ir=0.8097  HF0=-720.8+/-2 KJ
HF298=-732.7 kJ   REF=Dorofeeva et al JPCRD 32 (2003),879    Max Lst Sq Error
Cp @ 6000 K 0.25%. Calculated from original tables.
""",
)

entry(
    index = 94,
    label = "HSSH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09117,0.019422,-2.89396e-05,2.30252e-08,-7.20187e-12,591.057,13.5884], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69403,0.00390495,-1.41886e-06,2.30689e-10,-1.38746e-14,-165.807,-3.74139], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H-S-S-  T 3/03""",
    longDesc = 
u"""
63344-86-5
H2S2 HS-SH  DISULFANE  SIGMA=2  STATWT=1  Ia=0.5381381  Ib=10.4557619 Ic=10.9939
REF=MOPAC AM1-UHF  NU=2557,2556,883,882,516,416   REF= Jacox+Shimanouchi NIST
Webbook 2000   HF298=15.5 kcal  REF=Kerr CRC Handbook of Chem and Phys 2002.
{HF298=15.48+/-2.1 kJ  REF=Denis  J. Sulfur Chem 29,(2008),327}  Max Lst Sq
Error Cp @ 6000 0.37%
""",
)

entry(
    index = 95,
    label = "NH2N",
    molecule = 
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.53204,-0.00732419,3.00804e-05,-3.04001e-08,1.04701e-11,34958,1.51074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.05904,0.00618382,-2.22171e-06,3.58539e-10,-2.14533e-14,34853,6.69894], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Isodiazene   T 9/11""",
    longDesc = 
u"""
28647-38-3
N2H2 Isodiazene  H2NN  SIGMA=2  STATWT=1  IA=0.2514  IB=2.1721  IC=2.4235
Nu=2992,2919,1780,1639,1340,987  REF=Burcat G3B3  HF298-300.938+/-0.785 kJ
REF=ATcT C 2011  {HF298=301.984+/-8. kJ  REF=Burcat G3B3}  Max Lst Sq Error Cp
@ 1300 K 0.57%.
""",
)

entry(
    index = 96,
    label = "cONN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41662,0.00860086,-1.2177e-05,9.92351e-09,-3.33763e-12,40858.3,7.39864], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.30339,0.00165205,-6.27741e-07,1.05116e-10,-6.45213e-15,40384.5,-2.02053], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""cyclo O(NN)  T10/11""",
    longDesc = 
u"""
227934-45-4
N2O cyclo O(NN)  SIGMA=2  STATWT=1  IA=1.6309  IB=3.3758  IC=5.0067  Nu=1911,
799.5,344  REF=Burcat G3B3  HF298=350.62+/-1.69 kJ  REF=ATcT C 2011
{HF298=351.70+/-8 kJ  REF=Burcat G3B3}  Max Lst Sq Error Cp @ 1300 K 0.31%.
""",
)

entry(
    index = 97,
    label = "HN3O4",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {8,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p3 c-1 {2,S}
5 N u0 p0 c+1 {1,S} {6,D} {7,S}
6 O u0 p2 c0 {5,D}
7 O u0 p3 c-1 {5,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59966,0.0323887,-7.78882e-06,-2.25247e-08,1.39408e-11,11060.8,16.0197], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.0915,0.00667859,-2.54949e-06,4.20455e-10,-2.54161e-14,7734.45,-44.4298], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HN(NO2)2   T 3/13""",
    longDesc = 
u"""
114045-20-4
HN3O4  Dinitramin  HN(NO2)2  SIGMA=2  STATWT=1  IA=13.4731  IB=40.9517
IC=52.9082  [Ir(NO2)=3.22  ROSYM=2  V(3)=1600. cm-1]x2  Nu=3537,1773,1744,1391,
1372,1310,1051.5,853.5,841.5,794,740,716,656,423,402,239  HF298=26.169+/-2. kcal
REF=Burcat G3B3  {HF298=19. kcal  REF=Politzer, Seminario, Concha J Mol Struct
(THEOCEM) 427,(1998),123}  Max Lst Sq Error Cp @ 200 & 6000 K 0.34%
""",
)

entry(
    index = 98,
    label = "N4chain",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p1 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.92835,0.00070449,-3.44525e-06,7.07977e-09,-3.4986e-12,80201.5,-2.07614], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.80231,0.00281877,-1.00354e-06,1.60788e-10,-9.56687e-15,80488.4,3.80121], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T12/14""",
    longDesc = 
u"""
147363-92-6
N4 chain  N=N-N=N  SIGMA=2  STATWT=1  IA=1.3970  IB=39.9081  IC=41.3049
Nu=2458(2),61.2,25.4,24,11.5  REF=Burcat G3B3  HF298=686.6+/-7.6 kJ 
REF=Glukhovtsev Laiter JPC 100(5),(1996),1569  G2  Max Lst Sq Cp @ 6000 K 0.24%
""",
)

entry(
    index = 99,
    label = "cN4",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u0 p1 c0 {1,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.98734,0.000357879,-2.65838e-06,6.29744e-09,-3.2147e-12,89448.7,0.230299], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.80513,0.00281576,-1.00234e-06,1.60579e-10,-9.55374e-15,89743.1,6.35512], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T12/14""",
    longDesc = 
u"""
42851-09-2
N4 cyclo  (N=N)2  SIGMA=8  STATWT=1  IA=2.8419  IB=IC=64.17  Nu=2458(2),23(2),
17.23,8.11 REF=Burcat G3B3  HF298=763.55+/-2.3 kJ  REF=Ruscic ATcT C 2011  
{HF298=746.5+/-7.6 kJ  REF=Glukhovtsev Laiter JPC 100(5),(1996),1569}  Max Lst 
Sq Error Cp @ 6000. K 0.24%
""",
)

entry(
    index = 100,
    label = "tetrahedralN4",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 N u0 p1 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77367,0.00412794,2.67193e-05,-4.36896e-08,1.91734e-11,90168.1,10.0883], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.15691,0.00289928,-1.13238e-06,1.92969e-10,-1.1986e-14,88549.5,-14.8667], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 1/11""",
    longDesc = 
u"""
12596-63-3
N4 Terahedral  SIGMA=12  STATWT=1  IA=AB=IC=4.90485  Nu=1372,82(3),765(2)
REF=Elke Goos G3B3  HF0=183.09+/-0.5 kcal  REF=average of 6 ab initio calc by
Ruscic.  {HF0=182.22+/-0.5 kcal  REF=Lee & Martin Chem Phys Letters 357,(2002),
319;  HF298=757.40+/-1.62 kJ  REF=ATcT C 2011;  HF0=184.2+/-2. kcal
REF=Elke Goos G3B3;  HF298=732.5+/-8. kJ  REF=Glukhovtsev Laiter JPC 100(5),
(1996),1569}  Max Lst Sq Error Cp @ 200 K 0.75%.
""",
)

entry(
    index = 101,
    label = "O3",
    molecule = 
"""
1 O u0 p1 c+1 {2,S} {3,D}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40738,0.00205379,1.38486e-05,-2.23312e-08,9.76073e-12,15864.5,8.28248], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3303,-0.0119325,7.98741e-06,-1.77195e-09,1.26076e-13,12675.6,-40.8823], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 5/90""",
    longDesc = 
u"""
10028-15-6
O3  OZONE  SIGMA=2  STATWT=1   A0=3.553664  B0=.4452762  C0=.394758   NU=1103,
701,1042   X11=-4.9   X12=-9.1   X13=-34.8    X22=-1.0    X23=-17.   X33=-10.6
ALFAA1=-.002981  ALFAA2=-.053415  ALFAA3=.053118  ALFAB1=.002554  ALFAB2=.001269
ALFAB3=.003992   ALFAC1=.002319   ALFAC2=.002307  ALFAC3=.003613  W=-27.05
TAAA=-8.1429E-6  TBBB=-2.3864E-6  TCCC=-1.2694E-6 TAAB=16.947E-6  TAAC=3.2717E-6
TBBC=-1.6665E-6  TABA=-9.2093E-6  T0=10000.  STATWT=3  SIGMA=2   IAIBIC=48.
NU=600(2),350  T0=12500.  STATWT=3  SIGMA=2  IAIBIC=51.  NU=600(2),350
T0=13000.  STATWT=1 SIGMA=6  IAIBIC=32.  NU=850,500(2)  T0=13500.  STATWT=3
SIGMA=2  IAIBIC=48.  NU=600(2),350  HF298=141.8 KJ  REF= Gurvich 1989.
{HF298=141.75+/-0.039 kJ  REF=ATcT C; HF298=148.3 kJ  G3MP2B3  HF298=154.0 kJ
W1U  REF=Janoschek & Fabian J. Mol Struct 780/1,(2006),80}
""",
)

entry(
    index = 102,
    label = "cO3",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43378,0.00141964,1.53559e-05,-2.41415e-08,1.04881e-11,31589.4,7.20806], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.58604,0.00144418,-5.64567e-07,9.62618e-11,-5.98138e-15,30771.1,-5.17927], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T10/11""",
    longDesc = 
u"""
153851-84-4
O3  Cyclo  O(OO)  SIGMA=6  STATWT=1  IA=2.7471  IB=2.7473  IC=5.4944  Nu=1211,
856.6  REF=Burcat G3B3  HF298=272.46+/-1.55  REF=ATcT C 2011  (HF298=277.62+/-8.
kJ  REF=BUrcat G3B3 }  Max Lst Sq Error Cp @ 400 K 0.49%.
""",
)

entry(
    index = 103,
    label = "cO4",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {1,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.90386,0.0165202,-4.81057e-06,-1.22755e-08,8.03977e-12,46589.8,14.1925], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.98777,0.00207474,-8.15656e-07,1.39579e-10,-8.69453e-15,44902.9,-17.5119], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""T 1/11""",
    longDesc = 
u"""
852461-27-9
O4 cyclo  SIGMA=8  STATWT=1  IA=5.7309  IB=5.7319  IC=10.8665  Nu=997,917,847,
802(2),375  HF298=95.046+/-2. kcal  REF=Burcat G3B3  Max Lst Sq Error Cp @ 400
K 0.53%
""",
)

entry(
    index = 104,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6186,-0.00232174,1.16463e-05,-1.42093e-08,5.60765e-12,-480.622,6.36504], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.96894,0.000377297,7.67103e-09,-1.37544e-11,1.37139e-15,-728.572,3.73493], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""tpis89""",
    longDesc = 
u"""
13827-32-2
SO Calculated from Original Tables of Gurvich by B.McBride  HF298=4.76+/-0.18 kJ
   {T0(STATWT)=0(3)        BE=0.72082  WE=1148.19  WEXE=6.12  ALFAE=0.00574
T0(STATWT)=6350(2)         BE=0.7119   WE=1148.19  WEXE=6.12  ALFAE=0.00574
T0(STATWT)=10510(1)        BE=0.70261  WE=1067.66  WEXE=7.8   ALFAE=0.00635
T0(STATWT)=38292(2)        BE=0.6067   WE=415.2    WEXE=1.6   ALFAE=0.0194
TO(STATWT)=38455(2)        BE=0.6107   WE=413.3    WEXE=1.6   ALFAE=0.0194
T0(STATWT)=38616(2)        BE=0.6164   WE=412.7    WEXE=1.7   ALFAE=0.0204
T0(STATWT)=41629(3)        BE=0.502    WE=630.4    WEXE=4.8   ALFAE=0.0062
T0(STATWT)=42200(6)        BE=0.5      WE=170      WEXE=0     ALFAE=0
HF298=5.01+/-1.3 kJ   REF=JANAF 77;  HF298=5.02+/-1.2 kJ  REF=Denis J Sulfur
Chem 29,(2008),327}  Max Lst Sq Error Cp @ 400 K 0.22%.
""",
)

entry(
    index = 105,
    label = "SO2",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67481,0.00228302,8.46893e-06,-1.36562e-08,5.76272e-12,-36945.5,7.96866], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.38423,0.00167931,-6.32063e-07,1.08465e-10,-6.6689e-15,-37606.7,-1.83131], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""tpis89""",
    longDesc = 
u"""
7446-09-5
SO2     O-S-O     SIGMA=2  STATWT=1  Calculated by B. McBride from Gurvich's
original tables  HF298=-296.81+/-0.20 kJ  REF=Gurvich 89   {IA=1.38   IB=8.131
IC=9.534   NU=1361.76,1151.38,517.69   HF298=-296.842+/-0.21 kJ   REF=JANAF 61}
Max Lst Sq Error Cp @ 1300 K 0.31%.
""",
)

entry(
    index = 106,
    label = "SO4",
    molecule = 
"""
multiplicity 3
1 S u0 p0 c0 {2,D} {3,D} {4,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {1,S}
5 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.00307,0.0356251,-4.82496e-05,3.24326e-08,-8.72724e-12,-30516.6,19.0841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0844,0.0029774,-1.16402e-06,1.98505e-10,-1.23364e-14,-32653.7,-25.9765], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Sulfate radi  T 6/16""",
    longDesc = 
u"""
12772-98-4
SO4 Sulfate Radical  SIGMA=4  STATWT=1  IA=11.89035  IB=15.6268  IC=20.8268
Nu=1398,1229,939,697,669,461,456.5,452,289.5  HF298=-57.630+/-2. kcal  
REF=Burcat G3B3  Max Lst Sq Error Cp @ 1300 K 0.35%
""",
)

entry(
    index = 107,
    label = "cS2O",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0145,0.01851,-2.9502e-05,2.2264e-08,-6.49644e-12,14949.6,15.5712], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.30895,0.000720129,-2.84932e-07,4.89644e-11,-3.05891e-15,14066.2,-5.13081], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""SOS Cyclo   T 4/15""",
    longDesc = 
u"""
488092-02-0
S2O  SOS Cyclo Oxadithiirane  SIGMA=2  STATWT=1  IA=4.1516  IB=11.4251  
IC=15.5767  Nu=807,589,528  REF=Burcat B3LYP/63-1G(d)  HF298=32.1+/-1. kcal
REF=Denis  Molecular Physics 108,(2010),171  Max Lst Sq Error Cp @ 1200 K 0.16%.
""",
)

entry(
    index = 108,
    label = "S3",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 S u0 p2 c0 {1,D}
3 S u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67426,0.0185726,-3.39241e-05,2.89518e-08,-9.41516e-12,16032,13.727], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.53302,0.000489117,-1.9412e-07,3.34257e-11,-2.09107e-15,15318.7,-4.42378], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""tpis89""",
    longDesc = 
u"""
12597-03-4
S3  Trisulphur  SIGMA=2  STATWT=1  IAIBIC=4200.  Nu=656,575,256  HF0=146+/-4. kJ
HF298=144.74 kJ  REF=Gurvich 89  Max Lst Sq Error Cp @ 700 K & 1200 K 0.14%
""",
)

