#!/usr/bin/env python
# encoding: utf-8


name = "SurfaceThermoPt"
#Note: "-h" means "horizontal".

entry(
    index = 1,
    label = "vacant",
    molecule =
"""
1 X  u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
             0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "H_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.96702988E+00, 1.67920714E-02,  -2.50314139E-05, 1.80485455E-08, -5.11491197E-12,  -3.21277026E+03, 7.68211257E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.71968546E+00, -1.07696656E-03,  2.00193294E-06, -1.12865983E-09, 2.11269165E-13,  -4.24701712E+03, -1.52793490E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.479 eV.
            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = 0.00000 eV, gamma_H(X) = 1.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "H2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78935111E+00, 1.10148021E-03,  -2.31320100E-06, 2.11937826E-09, -6.31350224E-13, -1.86700333E+03, -1.00616465E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.06700165E+00, -5.01780079E-04,   6.70738856E-07, -1.79170942E-10, 8.86886631E-15, -1.89107687E+03, -1.12621699E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.054 eV.
            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = -0.05448 eV, gamma_H(X) = 0.000.
            The two lowest frequencies, 14.0 and 24.4 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "H2O_ads",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53777266E+00, 9.45372010E-03, -1.41325664E-05, 1.16730945E-08, -3.67657640E-12, -3.27590463E+04, -5.36548561E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.84789466E+00, -3.31526816E-03, 5.62018785E-06, -2.75864893E-09, 4.61279066E-13, -3.34885608E+04, -2.15622699E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.189 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.18932 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 49.5 and 68.6 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "OH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.07348583E+00, 1.72652206E-02, -3.17712232E-05, 2.71536568E-08, -8.69449304E-12, -1.96002909E+04, -5.65622336E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.01870328E+00, -1.35424298E-03, 2.27686310E-06, -1.09407298E-09, 1.79396487E-13, -2.02979842E+04, -2.41159621E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.970 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.18039 eV, gamma_O(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "HO-OH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83724199E+00, 1.40375175E-02, -1.46380418E-05, 8.15474904E-09, -1.74266851E-12, -2.52673006E+04, -5.58358715E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.63866612E+00, -4.64978374E-03,  8.11017779E-06, -4.17891893E-09, 7.28657000E-13, -2.67186621E+04, -3.48518226E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.286 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.28574 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 10.6 and 50.4 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "O2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.44370346E-01, 2.11027468E-02, -3.61266754E-05, 2.91032111E-08, -9.01689834E-12, -1.45323684E+04, -4.83356832E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.79639127E+00, -7.49042336E-04, 1.40680168E-06, -7.97092567E-10, 1.49696529E-13, -1.55278968E+04, -2.89715227E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.347 eV.
            Linear scaling parameters: ref_adatom_O1 = -3.586 eV, ref_adatom_O2 = -3.586 eV, psi = 3.23943 eV, gamma_O1(X) = 0.500, gamma_O2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "OOH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30951701E+00, 1.58303400E-02, -2.48037342E-05, 1.93368066E-08, -5.83664367E-12, -1.65355567E+04, -1.33537537E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.82755313E+00, -2.15021793E-03, 3.74021314E-06, -1.91291320E-09, 3.31650646E-13, -1.74991919E+04, -3.53134909E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.742 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.05105 eV, gamma_O(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "O_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79722382E-01, 1.25453156E-02, -2.29924588E-05, 1.94187177E-08, -6.22414099E-12, -1.73402246E+04, -2.22409728E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.92050897E+00, -2.70455589E-04, 5.15610634E-07, -2.93911213E-10, 5.54030466E-14, -1.78369003E+04, -1.50940536E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.586 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.00000 eV, gamma_O(X) = 1.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "O-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40658689E+00, 1.61838708E-02, -1.58074626E-05, 8.48925729E-09, -1.83038307E-12, -1.87460468E+04, -7.56970401E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.42636683E+00, -5.74378741E-03, 1.01435819E-05, -5.32742710E-09, 9.43135142E-13, -2.05528783E+04, -4.31963080E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.698 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.09537 eV, gamma_O(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "O-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88933974E+00, 1.02968448E-02, 5.34962049E-06, -1.25531705E-08, 5.32156610E-12, -2.04952765E+04, -1.15047899E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.12817565E+01, -9.42267565E-03, 1.67985868E-05, -8.95802947E-09, 1.60456258E-12, -2.29996396E+04, -5.57516428E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.41957 eV, gamma_O(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "NH3_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.31496774E+00, 1.46998289E-02, -1.30679071E-05, 6.99360870E-09, -1.52920905E-12, -1.45305774E+04, -4.29992592E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.39460262E+00, -7.22640455E-03, 1.26169819E-05, -6.50952664E-09, 1.13563586E-12, -1.63659104E+04, -4.02856883E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.673 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.67337 eV, gamma_N(X) = 0.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89010759E+00, 2.86217997E-02, -4.34545237E-05, 3.34143285E-08, -9.99500135E-12, -4.87893528E+03, 6.34997611E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.67968147E+00, -4.64266766E-03, 8.12871035E-06, -4.20436074E-09, 7.35132153E-13, -6.75225639E+03, -3.55181494E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.030 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.58258 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "NH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.68663098E+00, 2.89197486E-02, -4.76398566E-05, 3.77368064E-08, -1.14895177E-11, -1.39698939E+03, 9.81076735E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.82700699E+00, -2.46380210E-03, 4.35378855E-06, -2.27895186E-09, 4.02508146E-13, -2.92453268E+03, -2.63392973E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.440 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.54193 eV, gamma_N(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "N_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.62158075E-01, 1.65321723E-02, -2.95187453E-05, 2.44741387E-08, -7.73894837E-12, 4.56391760E+03, 2.27263793E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.87812725E+00, -4.32547150E-04, 8.18868468E-07, -4.65641564E-10, 8.76522110E-14, 3.86307901E+03, -1.54118153E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.352 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.00000 eV, gamma_N(X) = 1.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "H2N-OH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21930023E+00, 1.83079214E-02, -1.28981748E-05, 3.11969459E-09, 5.17141885E-13, -1.53124559E+04, 5.24764240E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.02488842E+01, -7.98164013E-03, 1.40252369E-05, -7.31456224E-09, 1.28796464E-12, -1.77173300E+04, -4.57361564E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.654 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.65407 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 17.1 and 68.9 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "HN-O_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.08095806E+00, 1.29219267E-02, -1.33374540E-05, 7.75158679E-09, -1.92612419E-12, -8.13728821E+03, 6.08546053E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.47671505E+00, -3.95793547E-03, 7.09299979E-06, -3.80627447E-09, 6.85388388E-13, -9.53610261E+03, -2.67996453E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -1.26632 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 36.2 and 74.0 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "HN-OH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.43834528E-02, 2.79801301E-02, -3.68717092E-05, 2.54797165E-08, -7.02746542E-12, -1.18361390E+04, -1.14442838E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.44761833E+00, -5.66879769E-03, 1.00234569E-05, -5.26997420E-09, 9.33985172E-13, -1.40902663E+04, -4.85973626E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.08004 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "NO_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.91253452E+00, 1.19742948E-02, -1.74150740E-05, 1.31050130E-08, -3.98440482E-12, -1.39133497E+04, -9.50920619E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.58200160E+00, -1.44698193E-03, 2.66840782E-06, -1.48667738E-09, 2.75613483E-13, -1.47707534E+04, -2.76785587E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.580 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.13417 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "NO-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23151905E+00, 6.07214925E-03, -7.46345407E-06, 5.43212687E-09, -1.71496758E-12, -1.16357520E+04, -1.30278030E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.54859951E+00, -1.48179602E-03, 2.71394293E-06, -1.49952005E-09, 2.76147146E-13, -1.22336367E+04, -2.47556107E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.390 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 1.51181 eV, gamma_N(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
    label = "NOH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.02968349E-01, 2.37024940E-02, -3.55330194E-05, 2.65623392E-08, -7.77662656E-12, -1.08269894E+04, -4.53311528E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.64521455E+00, -2.91720741E-03, 5.16378086E-06, -2.71526676E-09, 4.81634389E-13, -1.23572356E+04, -3.85225151E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.260 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.35381 eV, gamma_N(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "H2N-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.10937730E-01, 1.85814957E-02, -5.98243737E-06, -4.76023454E-09, 3.31121935E-12, -2.75700009E+03, 2.41162427E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.18367700E+01, -1.13177753E-02, 1.99338993E-05, -1.04342217E-08, 1.84230855E-12, -5.85969683E+03, -5.52432432E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.977 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.97746 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 6.9 and 79.2 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 23,
    label = "HN-NH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.62480603E-01, 2.37463930E-02, -2.79127702E-05, 1.76454048E-08, -4.52195226E-12, 1.08677882E+04, -3.53945184E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.40098406E+00, -5.98653308E-03, 1.06136322E-05, -5.60544216E-09, 9.96914912E-13, 8.66255190E+03, -4.84441559E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.676 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.67607 eV, gamma_N(X) = 0.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 24,
    label = "NN_ads",
    molecule =
"""
1 X  u0 p0 c0 
2 N  u0 p1 c0 {3,T}
3 N  u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13993917E+00, -9.92755910E-04, 1.76704033E-06, -1.57884342E-10, -3.64206712E-13, -4.38199802E+03, -7.98299353E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.38660517E+00, -1.50692391E-03, 2.67640594E-06, -1.41531803E-09, 2.51363379E-13, -4.48345747E+03, -9.36216462E+00], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.109 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.10949 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 6.3 and 24.2 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "HN-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47120056E-01, 2.68375643E-02, -2.81255056E-05, 1.59595219E-08, -3.61741193E-12, 5.50809497E+03, -2.02313697E+000], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.11788248E+01, -8.42590935E-03, 1.48660894E-05, -7.79652734E-09, 1.37881132E-12, 2.71736311E+03, -5.77901499E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.18029 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "N-NH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09323941E+00, 1.85333628E-02, -2.46837629E-05, 1.77191679E-08, -5.17017679E-12, 1.00757302E+04, -5.67671443E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.47568498E+00, -3.83877359E-03, 6.87143107E-06, -3.67728572E-09, 6.60773743E-13, 8.54387815E+03, -3.74961335E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.060 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.39360 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "N-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.70129737E-01, 2.46815562E-02, -3.14357040E-05, 2.15189651E-08, -5.94088667E-12, 5.19445129E+03, -4.18649200E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.37520921E+00, -5.75057579E-03, 1.01557341E-05, -5.32940833E-09, 9.43101134E-13, 3.07692090E+03, -4.81449524E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.040 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.86160 eV, gamma_N(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
    label = "HN-NH-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33495414E-01, 2.26610551E-02, -2.36224444E-05, 1.28389765E-08, -2.73372991E-12, 9.54917115E+03, -2.29491427E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.35953068E+00, -6.29553535E-03, 1.11894199E-05, -5.93532774E-09, 1.05926511E-12, 7.23245336E+03, -4.84748217E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.982 eV.
            Linear scaling parameters: ref_adatom_N1 = -4.352 eV, ref_adatom_N2 = -4.352 eV, psi = 1.91976 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "HN-N-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.33366824E-03, 2.28486010E-02, -3.13931005E-05, 2.25104861E-08, -6.48527412E-12, 7.54468891E+03, -1.63253226E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.45448958E+00, -3.87308208E-03, 6.93696999E-06, -3.71519284E-09, 6.68194144E-13, 5.79074311E+03, -3.86806230E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.280 eV.
            Linear scaling parameters: ref_adatom_N1 = -4.352 eV, ref_adatom_N2 = -4.352 eV, psi = 3.07184 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "HN-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.90039015E-01, 2.20932553E-02, -9.26149163E-06, -3.13927989E-09, 2.92569788E-12, -5.59423948E+03, -2.83380870E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.30787664E+01, -1.20311946E-02, 2.13949410E-05, -1.13636331E-08, 2.02934094E-12, -9.10419311E+03, -6.80318827E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.850 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.40192 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
    label = "N-CH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.25178555E-01, 2.12826243E-02, -2.34081427E-05, 1.47028746E-08, -3.89854468E-12, 2.52272059E+03, -4.11114694E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.38157685E+00, -6.59021782E-03, 1.17682807E-05, -6.28180522E-09, 1.12615562E-12, 3.18498804E+02, -4.78840793E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.660 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.21342 eV, gamma_N(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
    label = "N-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.57582464E-01, 2.08227846E-02, -1.31666200E-05, 2.48777975E-09, 6.58681443E-13, -5.31493961E+03, -3.12938558E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.12334649E+01, -9.61392101E-03, 1.71661622E-05, -9.17060199E-09, 1.64510419E-12, -8.26608573E+03, -5.86567081E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.050 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.14794 eV, gamma_N(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

# entry(
#     index = 33,
#     label = "ON-O_ads",
#     molecule =
# """
# 1 X  u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[
#              1.908949200E+00,   2.036846110E-02,  -3.030122180E-05,   2.191995790E-08,
#              -6.250090720E-12,   9.003214300E+03,  -2.726671970E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
#             NASAPolynomial(coeffs=[
#              7.636130060E+00,  -1.383989810E-03,   2.571362700E-06,  -1.448349250E-09,
#              2.709019330E-13,   7.732608970E+03,  -3.081328960E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
#         ],
#         Tmin = (298.0, 'K'),
#         Tmax = (2000.0, 'K'),
#     ),
#     longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
#            Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.688 eV.
#            Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.86302 eV, gamma_N(X) = 0.333.
#            The two lowest frequencies, -33.2 and 55.1 cm-1, where replaced by the 2D gas model.""",
# )

entry(
    index = 34,
    label = "C_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.73430697E+00, 1.89855471E-02, -3.23563661E-05, 2.59269890E-08, -7.99102104E-12, 6.36385922E+03, 6.25445028E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.82193241E+00, -6.61177416E-04, 1.24180431E-06, -7.03993893E-10, 1.32276605E-13, 5.46467816E+03, -1.55251271E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.00000 eV, gamma_C(X) = 1.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
    label = "C-C_ads",
    molecule =
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22282794E-01, 1.96908600E-02, -3.07626817E-05, 2.35937440E-08, -7.12438442E-12, 2.42830208E+04, -3.03635113E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.60759796E+00, -1.41921856E-03, 2.63409811E-06, -1.47830656E-09, 2.75649745E-13, 2.31084908E+04, -2.93177601E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.910 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.84219 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "C-CH2_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 H  u0  p0 c0 {3,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.04785706E+00, 3.38148654E-02, -4.45775300E-05, 3.08318279E-08, -8.56901355E-12, -2.28268064E+03, 6.64469050E+000], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.42830381E+00, -6.48123487E-03, 1.15879773E-05, -6.19494276E-09, 1.11218928E-12, -5.01217502E+03, -5.04945175E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.60024 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "C-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57603104E-01, 2.34293413E-02, -1.86683661E-05, 7.29234370E-09, -8.79008671E-13, -1.12523534E+04, -1.73582278E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.13050336E+01, -9.40622931E-03, 1.67935678E-05, -8.96901500E-09, 1.60855621E-12, -1.42348165E+04, -5.88363790E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.590 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52567 eV, gamma_C(X) = 0.750.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
    label = "CH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.00950779E+00, 3.02193341E-02, -4.99546294E-05, 3.99478464E-08, -1.23021593E-11, -3.13353859E+03, 1.12314464E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.88482023E+00, -2.70846119E-03, 4.84648118E-06, -2.58513645E-09, 4.63180319E-13, -4.75082800E+03, -2.67870735E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.240 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.17590 eV, gamma_C(X) = 0.750.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "CH-CH_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68898057E+00, 3.52831263E-02, -4.97578493E-05, 3.62176199E-08, -1.04588699E-11, 2.14683932E+02, 6.75238906E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.57180447E+00, -5.98074762E-03, 1.06737584E-05, -5.68837233E-09, 1.01860349E-12, -2.37703001E+03, -4.88869924E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.010 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 4.74337 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "CH-CH-vdw_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11180282E+00, 2.49061659E-02, -3.96404401E-05, 3.23914869E-08, -1.01975824E-11, 2.12123842E+04, 4.05476651E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.55328593E+00, -4.89148968E-03, 8.55317549E-06, -4.41304892E-09, 7.69510301E-13, 1.96129058E+04, -3.21219245E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.200 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20021 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 8.5 and 8.7 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "CH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.26602367E+00, 2.92517765E-02, -4.32728797E-05, 3.30655723E-08, -9.93242641E-12, -2.23619445E+02, 8.22751288E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.82572636E+00, -5.17192506E-03, 9.19551938E-06, -4.87101486E-09, 8.67713091E-13, -2.26886621E+03, -3.64410753E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.640 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.26541 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "CH2-CH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39737604E+00, 3.73194353E-02, -3.73140702E-05, 1.98435109E-08, -4.15883994E-12, -8.09105589E+03, 9.52383811E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.32599664E+01, -1.17874099E-02, 2.10016909E-05, -1.11823349E-08, 2.00074750E-12, -1.21090188E+04, -6.98822356E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.950 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.42761 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.80099877E-01, 1.66399977E-02, -1.39164870E-05, 6.70631582E-09, -1.31079175E-12, -6.31046932E+03, -7.57148375E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.67869881E+00, -7.84238420E-03, 1.38956076E-05, -7.33600190E-09, 1.30321431E-12, -8.45079729E+03, -4.20966823E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.770 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.08242 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "CH3-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.19974851E+00, 7.93841719E-03, 2.69413164E-05, -3.53453703E-08, 1.32207821E-11, -1.45807566E+04, -1.67952705E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.59169609E+01, -1.75616860E-02, 3.12255463E-05, -1.65874969E-08, 2.96156965E-12, -1.86136199E+04, -6.98567509E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.219 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.21852 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 5.6 and 8.8 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "CH4_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.26247002E+00, -7.42703413E-03, 3.36472336E-05, -3.29401150E-08, 1.10259250E-11, -1.16038320E+04, -1.00920541E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.54981008E+00, -1.03719404E-02, 1.83183536E-05, -9.63332916E-09, 1.70558531E-12, -1.32717208E+04, -3.45374475E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.122 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.12206 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 3.2 and 8.1 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 46,
    label = "CN_ads",
    molecule =
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,D} {4,D}
4 N  u0  p1 c0 {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11759999E+00, 2.61925458E-03, -2.38597242E-06, 1.99370899E-09, -8.12410469E-13, 7.23851375E+03, -1.73631138E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.52418021E+00, -1.46883611E-03, 2.67356881E-06, -1.46454792E-09, 2.67815680E-13, 6.83798413E+03, -2.46384099E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.340 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.13303 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
    label = "CNH_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59496949E+00, 1.65089177E-02, -2.53974408E-05, 2.02468005E-08, -6.32103397E-12, -2.38409128E+03, -1.15883837E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.61905419E+00, -2.92187763E-03, 5.15479567E-06, -2.69525498E-09, 4.75495658E-13, -3.50064919E+03, -3.61906347E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.740 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.63638 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "CNH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.53087538E+00, 2.16230806E-02, -2.71329649E-05, 1.84938021E-08, -5.09305792E-12, -1.03698193E+04, -8.38468416E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.40468481E+00, -5.41327535E-03,9.51693401E-06, -4.95946907E-09, 8.72860901E-13, -1.22719497E+04, -4.77373490E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.060 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.00119 eV, gamma_C(X) = 0.750.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "CO-f_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70112272E+00, 8.76650166E-03, -1.29512418E-05, 1.04194594E-08, -3.39700490E-12, -3.49476634E+04, -1.28730512E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.52820880E+00, -1.52631254E-03, 2.79791895E-06, -1.54550129E-09, 2.84523223E-13, -3.56231280E+04, -2.69156979E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.480 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.89529 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "COH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.63437744E-01, 2.14806054E-02, -3.00009525E-05, 2.11729011E-08, -5.90923491E-12, -3.09990999E+04, -5.10749731E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.59479056E+00, -3.06847382E-03, 5.43592647E-06, -2.86463560E-09, 5.09149225E-13, -3.25424988E+04, -3.83674793E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.260 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.80370 eV, gamma_C(X) = 0.750.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "H2C-CH_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.71741524E+00, 4.45639232E-02, -5.86622119E-05, 4.05880256E-08, -1.12584803E-11, -2.98721220E+03, 1.37056124E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.14826601E+01, -8.87645080E-03, 1.58590687E-05, -8.47088253E-09, 1.51944591E-12, -6.59838559E+03, -6.19545665E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.770 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.29437 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "H2C-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.32861243E-01, 2.34315125E-02, -6.21561097E-06, -7.04743109E-09, 4.32504726E-12, -1.03526448E+04, -4.22788616E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.50901779E+01, -1.47664787E-02, 2.62942501E-05, -1.39941239E-08, 2.50255356E-12, -1.44464142E+04, -7.55761454E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.06163 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "H2C-NH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.22576461E-01, 2.08807519E-02, -1.29691654E-05, 1.29682800E-09, 1.40594827E-12, 3.66393668E+03, 6.82500696E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.02705016E+01, -9.06171664E-03, 1.61074586E-05, -8.55119082E-09, 1.52673350E-12, 7.87732523E+02, -4.76927508E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.228 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.22807 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 46.0 and 79.7 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "H2C-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.94472063E-01, 2.62082323E-02, -2.05472442E-05, 7.54576090E-09, -5.98066735E-13, -1.00349448E+04, -1.63394338E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.30763281E+01, -1.10941325E-02, 1.95968859E-05, -1.03005801E-08, 1.82465302E-12, -1.33699538E+04, -6.45023766E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.29283 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "H2C-O_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.87258154E+00, -3.80708439E-03, 2.29126729E-05, -2.34870004E-08, 7.95457450E-12, -2.09616356E+04, -1.09618928E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.42973399E+00, -6.84404724E-03, 1.22430399E-05, -6.56317791E-09, 1.18019535E-12, -2.23198421E+04, -3.11097315E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.184 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.18361 eV, gamma_C(X) = 0.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "H2C-OH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.90559347E-01, 2.31880081E-02, -1.92723889E-05, 7.42264515E-09, -6.88671342E-13, -3.54054895E+04, -1.78049680E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.13189670E+01, -8.55328894E-03, 1.51576215E-05, -8.00760803E-09, 1.42446093E-12, -3.82049819E+04, -5.60575095E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.890 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.19820 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 57,
    label = "H2CN-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.02719609E-01, 2.77232113E-02, -3.31822780E-05, 2.12596176E-08, -5.54256988E-12, 2.08108433E+03, 1.56425884E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.43341136E+00, -6.49223331E-03, 1.16024225E-05, -6.20150120E-09, 1.11316221E-12, -4.41424500E+02, -4.98315612E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.710 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.37462 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "H2CNH-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.22318867E+00, 4.08379516E-02, -5.08218184E-05, 3.33893656E-08, -8.81880680E-12, -2.40066395E+03, 1.16307500E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.13347841E+01, -8.90691781E-03, 1.58626750E-05, -8.43510814E-09, 1.50807029E-12, -5.92362341E+03, -6.11697683E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.756 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.75753 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "H3C-NH2_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.90575940E-01, 1.65852324E-02, 6.48184437E-06, -1.79298156E-08, 7.87674440E-12, -1.51012090E+04, 2.42587438E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.37729719E+01, -1.46798316E-02, 2.60099894E-05, -1.37425622E-08, 2.44401396E-12, -1.89207219E+04, -6.57899167E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.879 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.87925 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.6 and 84.5 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "H3C-OH_ads",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70506726E+00, 1.00913594E-02, 1.00260680E-05, -1.80909603E-08, 7.44539499E-12, -3.09647604E+04, -4.48135960E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.21539459E+01, -1.13173411E-02, 2.00342036E-05, -1.05724068E-08, 1.87852776E-12, -3.38115989E+04, -5.44617359E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.316 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.31650 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.5 and 57.9 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "HC-C_ads",
    molecule =
"""
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.41170551E-02, 2.52700921E-02, -3.75803933E-05, 2.82910883E-08, -8.39575978E-12, 1.42484565E+04, -1.63766387E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.62295055E+00, -3.43322498E-03, 6.14771846E-06, -3.28932116E-09, 5.91021494E-13, 1.25529905E+04, -3.88019444E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.100 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.96689 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

#This is actually bidentate, so this input is not correct (should be the same as index 51).
#entry(
#    index = 62,
#    label = "HC-CH2_ads",
#    molecule =
#"""
#1 X  u0  p0 c0 {2,S}
#2 C  u0  p0 c0 {1,S} {3,D} {4,S}
#3 C  u0  p0 c0 {2,D} {5,S} {6,S}
#4 H  u0  p0 c0 {2,S}
#5 H  u0  p0 c0 {3,S}
#6 H  u0  p0 c0 {3,S}
#""",
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[
#             -3.761998800E+00,   4.463873830E-02,  -5.865136870E-05,   4.048714140E-08,
#             -1.120403080E-11,  -2.545452840E+03,   1.391918370E+01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
#            NASAPolynomial(coeffs=[
#             1.147737520E+01,  -8.889811580E-03,   1.588277200E-05,  -8.483602150E-09,
#             1.521747930E-12,  -6.167735370E+03,  -6.194706680E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
#        ],
#        Tmin = (298.0, 'K'),
#        Tmax = (2000.0, 'K'),
#    ),
#    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
#            Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -2.790 eV.
#            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.09643 eV, gamma_C(X) = 0.250.""",
#)

entry(
    index = 63,
    label = "HC-CH3_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39195145E-01, 2.71965302E-02, -1.96479590E-05, 6.17925647E-09, -1.84661314E-13, -5.60696357E+03, 2.67225219E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.32714698E+01, -1.19649775E-02, 2.13410724E-05, -1.13827464E-08, 2.03915294E-12, -9.25414727E+03, -6.90961026E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.580 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20205 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "HCN_ads",
    molecule =
"""
1 X  u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 H  u0  p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17889171E+00, 1.61639690E-02, -2.31637957E-05, 1.78894661E-08, -5.51067178E-12, 1.10206116E+04, 1.94585596E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.54320202E+00, -3.51550718E-03, 6.26384435E-06, -3.32803966E-09, 5.94359917E-13, 9.77019618E+03, -2.63488571E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.010 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.00995 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 51.9 and 72.8 cm-1, where replaced by the 2D gas model.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "HCN-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.45901289E-02, 2.36120976E-02, -3.37215849E-05, 2.50959079E-08, -7.46308917E-12, 3.55589882E+03, -1.50225522E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.52979178E+00, -3.89004433E-03, 6.99537195E-06, -3.76746392E-09, 6.80266036E-13, 1.81662108E+03, -3.86174029E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.650 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 2.37733 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.667.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "HCNH_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.05598404E-01, 2.12578896E-02, -2.26826133E-05, 1.31095137E-08, -3.07357265E-12, 4.10897731E+01, -1.71828775E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.39843610E+00, -6.24337353E-03, 1.11012002E-05, -5.89092739E-09, 1.05148038E-12, -2.13728786E+03, -4.51639342E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.220 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52691 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "HCNH-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.13239946E+00, 2.98484244E-02, -3.78145776E-05, 2.53616976E-08, -6.86307261E-12, -3.16836112E+03, 3.30113143E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.37828967E+00, -6.30048833E-03, 1.12203407E-05, -5.96428012E-09, 1.06621044E-12, -5.70392882E+03, -4.92130115E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.490 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.71054 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "HCNH2_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11835944E-01, 2.41104719E-02, -2.20379983E-05, 1.06103035E-08, -1.92226443E-12, -7.35704782E+03, -2.41270253E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.11491706E+01, -8.75052593E-03, 1.54802187E-05, -8.15334058E-09, 1.44682582E-12, -1.01528629E+04, -5.48979853E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.670 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.70666 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "HCO_ads",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.94156388E+00, 1.30882912E-02, -1.34260003E-05, 7.97044677E-09, -2.06719711E-12, -2.80413711E+04, -5.97802577E+0], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.49136303E+00, -4.18949199E-03, 7.54544313E-06, -4.07863095E-09, 7.38421146E-13, -2.94916141E+04, -3.42076640E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.210 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52049 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "HCO-h_ads",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.63229192E-02, 2.34818104E-02, -3.17556441E-05, 2.22347561E-08, -6.25650920E-12, -2.44241519E+04, -1.42351290E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.61171587E+00, -3.81051175E-03, 6.86938717E-06, -3.71585312E-09, 6.73352174E-13, -2.62393600E+04, -3.96330591E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.900 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.99512 eV, gamma_C1(X) = 0.500, gamma_O2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "HCOH_ads",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.68649725E-01, 2.04972050E-02, -1.85506813E-05, 8.22998468E-09, -1.23251062E-12, -2.63024443E+04, -9.21769145E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.39449002E+00, -6.56375678E-03, 1.17141780E-05, -6.25387815E-09, 1.12161443E-12, -2.86359494E+04, -4.64113344E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.960 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.42191 eV, gamma_C(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "H2CO-h_ads",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.02400610E-01, 2.37197512E-02, -2.57930815E-05, 1.52033151E-08, -3.68397327E-12, -2.14196483E+04, -4.98129327E-01], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.52719632E+00, -6.50602819E-03, 1.16581384E-05, -6.25773731E-09, 1.12684291E-12, -2.38121944E+04, -4.81511621E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.236 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.96700 eV, gamma_C1(X) = 0.250, gamma_O2(X) = 0.500.""",
    metal = "Pt",
    facet = "111",
)

